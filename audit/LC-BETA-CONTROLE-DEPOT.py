#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# LC-BETA-CONTROLE-DEPOT v1.0 — controle COTE DEPOT, mandate par
# LC-BETA-03-AMENDEMENT-2 §5.5 (arbitrage operateur nº2 du 2026-07-25).
#
# Complement de LC-BETA-BOOT.py, qui inspecte le MOUNT et le PROJET beta.
# Celui-ci inspecte le DEPOT GIT, et lui seul. Les deux ne se recouvrent pas.
#
# Ce qu'il fait :
#   1. zero BETA-COPIE-* dans l'ARBRE du depot          -> sinon exit != 0
#   2. zero BETA-COPIE-* dans TOUT L'HISTORIQUE git     -> sinon exit != 0
#   3. chaque piece de gouvernance declaree est PRESENTE -> sinon exit != 0
#   4. chaque piece presente est BYTE-IDENTIQUE a l'atelier -> sinon exit != 0
#   5. manifeste absent                                  -> exit != 0
#   6. manifeste declarant ZERO piece                    -> exit != 0  (non-vacuite)
#   7. piece du depot divergente du sha DECLARE          -> sinon exit != 0
#
# Ce qu'il ne fait PAS : attester une physique, un verdict, une identite
#   editoriale, une pertinence. Il n'atteste QUE des octets et des absences.
#
# R-36 : ce script n'embarque AUCUNE valeur attendue. Le manifeste est fourni
#        de l'exterieur ; le script ne connait pas d'avance ce qu'il doit voir.
#
# Precedent S13 : un instrument mandate se prouve par un AUTO-TEST MORDANT.
#        Chaque garde a un porteur mutable ; une garde qu'aucune mutation ne
#        fait tomber est un FAUX PASS. Precedent S9 : une garde qui passe sur
#        l'ensemble vide est un FAUX PASS -> garde 6.
#
# Usage :
#   LC-BETA-CONTROLE-DEPOT.py --depot DIR --atelier DIR --manifeste FICHIER
#   LC-BETA-CONTROLE-DEPOT.py --self-test

import os, re, sys, hashlib, subprocess, tempfile, shutil

PREFIXE_COPIE = 'BETA-COPIE-'
LIGNE_MANIF = re.compile(r'^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|')


def sha256(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def lire_manifeste(chemin):
    """Rend [(chemin_relatif_depot, sha_declare)]. Leve si absent."""
    if not os.path.exists(chemin):
        raise FileNotFoundError(chemin)
    out = []
    for ligne in open(chemin, encoding='utf-8'):
        m = LIGNE_MANIF.match(ligne)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def copies_arbre(depot):
    """BETA-COPIE-* presents dans l'arbre de travail, .git exclu."""
    trouves = []
    for racine, dirs, fichiers in os.walk(depot):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in fichiers:
            if f.startswith(PREFIXE_COPIE):
                trouves.append(os.path.relpath(os.path.join(racine, f), depot))
    return sorted(trouves)


def copies_historique(depot):
    """BETA-COPIE-* ayant EXISTE dans un commit quelconque.

    git conserve tout blob pour toujours : un retrait de l'arbre ne retire
    rien de l'historique. On interroge donc les objets, pas HEAD.
    """
    if not os.path.isdir(os.path.join(depot, '.git')):
        return []          # pas un depot git : rien a dire, la garde 1 couvre
    try:
        r = subprocess.run(['git', '-C', depot, 'rev-list', '--objects', '--all'],
                           capture_output=True, text=True, timeout=180)
    except Exception:
        return ['<historique ILLISIBLE>']
    if r.returncode != 0:
        return ['<historique ILLISIBLE>']
    trouves = set()
    for ligne in r.stdout.splitlines():
        parts = ligne.split(' ', 1)
        if len(parts) == 2 and os.path.basename(parts[1]).startswith(PREFIXE_COPIE):
            trouves.add(parts[1])
    return sorted(trouves)


def controler(depot, atelier, manifeste, bavard=True):
    """Rend (rc, rapport:dict). rc=0 seulement si TOUTES les gardes passent."""
    rap = {'manifeste_absent': False, 'manifeste_vide': False,
           'copies_arbre': [], 'copies_historique': [],
           'absents': [], 'divergents_atelier': [], 'divergents_manifeste': [],
           'confrontes': 0}

    # ---- garde 5 : manifeste absent
    try:
        pieces = lire_manifeste(manifeste)
    except FileNotFoundError:
        rap['manifeste_absent'] = True
        if bavard:
            print("!! MANIFESTE ABSENT — un controle sans referentiel ne controle rien.")
        return 2, rap

    # ---- garde 6 : non-vacuite
    if len(pieces) == 0:
        rap['manifeste_vide'] = True
        if bavard:
            print("!! MANIFESTE DECLARANT ZERO PIECE — un controle qui passe sur")
            print("   l'ensemble vide est un FAUX PASS (precedent S9).")
        return 2, rap

    # ---- gardes 1 et 2 : aucune copie de substance, arbre puis historique
    rap['copies_arbre'] = copies_arbre(depot)
    rap['copies_historique'] = copies_historique(depot)

    # ---- gardes 3, 4, 7 : presence, identite a l'atelier, identite au manifeste
    for rel, sha_declare in pieces:
        p_depot = os.path.join(depot, rel)
        if not os.path.exists(p_depot):
            rap['absents'].append(rel)
            continue
        h_depot = sha256(p_depot)
        p_atelier = os.path.join(atelier, os.path.basename(rel))
        if not os.path.exists(p_atelier) or sha256(p_atelier) != h_depot:
            rap['divergents_atelier'].append(rel)
        if h_depot != sha_declare:
            rap['divergents_manifeste'].append(rel)
        rap['confrontes'] += 1

    rc = 0
    if (rap['copies_arbre'] or rap['copies_historique'] or rap['absents']
            or rap['divergents_atelier'] or rap['divergents_manifeste']):
        rc = 1

    if bavard:
        print("=" * 66)
        print("  LC-BETA-CONTROLE-DEPOT v1.0 — cote DEPOT")
        print("=" * 66)
        print("pieces declarees      ", len(pieces))
        print("pieces confrontees    ", rap['confrontes'])
        print("copies arbre          ", len(rap['copies_arbre']), rap['copies_arbre'] or "")
        print("copies historique     ", len(rap['copies_historique']), rap['copies_historique'] or "")
        print("declarees absentes    ", len(rap['absents']), rap['absents'] or "")
        print("divergentes/atelier   ", len(rap['divergents_atelier']), rap['divergents_atelier'] or "")
        print("divergentes/manifeste ", len(rap['divergents_manifeste']), rap['divergents_manifeste'] or "")
        print("-" * 66)
        if rc:
            print("  ECART. Le BORNER et le NOMMER avant toute suite. Ne pas continuer.")
        else:
            print("  Conforme sur les OCTETS et sur les ABSENCES.")
        print("-" * 66)
        print("""
CE QUE CE rc=0 N'ATTESTE PAS :
  - qu'une piece deposee est JUSTE. Il atteste qu'elle est LA, et IDENTIQUE.
  - qu'une piece est A JOUR. Un texte perime se depose aussi bien qu'un autre.
  - une physique, un verdict, une identite editoriale, une pertinence.
  - que P-0 est rendu, que S-B1 est ouvert, que S-B2 est arme.
§6.4 : {A4 ; A2*  ; N} INCHANGE. beta T-b, SEUL facteur d'O2 ouvert.
       CCC n'est ni demontree ni refutee.
""")
    return rc, rap


# --------------------------------------------------------------- AUTO-TEST
def _ecrire(p, txt):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(txt)


def _manif(pieces):
    lignes = ["| piece | sha256 |", "|---|---|"]
    for rel, sha in pieces:
        lignes.append("| `%s` | `%s` |" % (rel, sha))
    return "\n".join(lignes) + "\n"


def _scenario(base, avec_git=True):
    """Monte un cas NOMINAL : 2 pieces de gouvernance, atelier concordant."""
    depot, atelier = os.path.join(base, 'depot'), os.path.join(base, 'atelier')
    os.makedirs(depot, exist_ok=True)
    os.makedirs(atelier, exist_ok=True)
    contenus = {'audit/PIECE-A.md': "alpha\n", 'audit/PIECE-B.md': "beta\n"}
    pieces = []
    for rel, txt in contenus.items():
        _ecrire(os.path.join(depot, rel), txt)
        _ecrire(os.path.join(atelier, os.path.basename(rel)), txt)
        pieces.append((rel, sha256(os.path.join(depot, rel))))
    manifeste = os.path.join(base, 'MANIFESTE.md')
    _ecrire(manifeste, _manif(pieces))
    if avec_git:
        subprocess.run(['git', 'init', '-q', depot], check=True)
        subprocess.run(['git', '-C', depot, 'add', '-A'], check=True)
        subprocess.run(['git', '-C', depot, '-c', 'user.email=a@b', '-c', 'user.name=t',
                        'commit', '-q', '-m', 'nominal'], check=True)
    return depot, atelier, manifeste


def self_test():
    resultats = []

    def cas(nom, attendu_rc_non_nul, monteur):
        base = tempfile.mkdtemp()
        try:
            depot, atelier, manifeste = _scenario(base)
            monteur(base, depot, atelier, manifeste)
            rc, _ = controler(depot, atelier, manifeste, bavard=False)
            mord = (rc != 0) if attendu_rc_non_nul else (rc == 0)
            resultats.append((nom, mord, rc))
        finally:
            shutil.rmtree(base, ignore_errors=True)

    # T0 — le cas NOMINAL doit passer. Sans lui, un controle qui echoue
    # TOUJOURS satisferait toutes les mutations : ce serait le faux PASS
    # symetrique. C'est la garde de la garde.
    cas("T0  nominal -> rc=0 (garde de la garde)", False, lambda b, d, a, m: None)

    # G1 — copie de substance dans l'ARBRE
    cas("G1  BETA-COPIE-* dans l'arbre", True,
        lambda b, d, a, m: _ecrire(os.path.join(d, 'kb', 'BETA-COPIE-X.md'), "x\n"))

    # G2 — copie de substance dans l'HISTORIQUE, retiree de l'arbre
    def g2(b, d, a, m):
        p = os.path.join(d, 'kb', 'BETA-COPIE-Y.md')
        _ecrire(p, "y\n")
        subprocess.run(['git', '-C', d, 'add', '-A'], check=True)
        subprocess.run(['git', '-C', d, '-c', 'user.email=a@b', '-c', 'user.name=t',
                        'commit', '-q', '-m', 'ajout'], check=True)
        os.remove(p)
        subprocess.run(['git', '-C', d, 'add', '-A'], check=True)
        subprocess.run(['git', '-C', d, '-c', 'user.email=a@b', '-c', 'user.name=t',
                        'commit', '-q', '-m', 'retrait'], check=True)
    cas("G2  BETA-COPIE-* dans l'historique seul", True, g2)

    # G3 — piece declaree ABSENTE du depot
    cas("G3  piece declaree absente", True,
        lambda b, d, a, m: os.remove(os.path.join(d, 'audit', 'PIECE-A.md')))

    # G4 — piece presente mais DIVERGENTE de l'atelier
    cas("G4  divergence depot/atelier", True,
        lambda b, d, a, m: _ecrire(os.path.join(a, 'PIECE-A.md'), "alpha MUTE\n"))

    # G5 — manifeste ABSENT
    cas("G5  manifeste absent", True, lambda b, d, a, m: os.remove(m))

    # G6 — manifeste declarant ZERO piece (non-vacuite)
    cas("G6  manifeste vide (non-vacuite)", True,
        lambda b, d, a, m: _ecrire(m, _manif([])))

    # G7 — depot divergent du sha DECLARE (atelier suit, donc G4 ne mord pas)
    def g7(b, d, a, m):
        _ecrire(os.path.join(d, 'audit', 'PIECE-B.md'), "beta MUTE\n")
        _ecrire(os.path.join(a, 'PIECE-B.md'), "beta MUTE\n")
    cas("G7  divergence depot/manifeste", True, g7)

    print("=" * 66)
    print("  LC-BETA-CONTROLE-DEPOT — AUTO-TEST MORDANT")
    print("=" * 66)
    ok = 0
    for nom, mord, rc in resultats:
        print("  [%s] %-42s rc=%d" % ("MORD" if mord else "FAUX PASS", nom, rc))
        ok += mord
    print("-" * 66)
    print("  %d/%d gardes mordantes." % (ok, len(resultats)))
    print("  §6.4 : passer l'auto-test NE SCELLE, NE COMPTE, NE DEMONTRE RIEN.")
    print("=" * 66)
    return 0 if ok == len(resultats) else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--self-test' in a:
        sys.exit(self_test())

    def opt(nom):
        return a[a.index(nom) + 1] if nom in a and a.index(nom) + 1 < len(a) else None

    depot, atelier, manifeste = opt('--depot'), opt('--atelier'), opt('--manifeste')
    if not (depot and atelier and manifeste):
        print(__doc__ or "")
        print("usage : --depot DIR --atelier DIR --manifeste FICHIER | --self-test")
        sys.exit(2)
    rc, _ = controler(depot, atelier, manifeste)
    sys.exit(rc)
