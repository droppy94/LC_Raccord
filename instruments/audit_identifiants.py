#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_identifiants.py — état de l'espace des identifiants du dépôt.

RAISON D'ÊTRE. L'opérateur a tranché que `depend_de:` référencerait l'`id:` des
pièces, et non leur nom de fichier. Un renvoi par clé ne vaut que si la clé
existe, est unique, et est bien formée. Cet instrument mesure cela AVANT que la
convention soit déposée, et sert ensuite de contrôle permanent.

CE QU'IL MESURE
  1. pièces sans `id:`
  2. `id:` mal formés (placeholders, phrases, guillemets, espaces)
  3. `id:` revendiqués par plusieurs fichiers (collisions)
  4. front-matter absent ou non clos
  5. champs `parent:` existants — convention de dépendance informelle à absorber

GARDES
  - lecture SEULE : cet instrument n'écrit rien dans le dépôt.
  - le front-matter est BORNÉ au bloc `---` … `---` de tête. Un `id:` situé dans
    le corps n'est PAS un identifiant et ne doit pas être lu comme tel.
  - aucun parseur YAML : trois registres du dépôt portent un front-matter YAML
    invalide (dette connue). La lecture est ligne à ligne, donc robuste.

CODES DE RETOUR
  rapport            : 0 toujours (c'est un constat, pas une barrière)
  rapport --strict   : 1 si un défaut est trouvé
  --self-test        : 0 si les 14 assertions passent, 1 sinon

§6.4 — mesurer un espace de noms ne scelle rien, ne compte rien, ne démontre rien.
"""

import os
import re
import sys
import tempfile
import shutil

ID_VALIDE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._\-/]*$')
EXCLUS = {'.git', '__pycache__', 'node_modules'}


# ----------------------------------------------------------------------------
# Lecture bornée du front-matter
# ----------------------------------------------------------------------------

def front_matter(texte):
    """Rend (dict, statut). Statut : 'ok' | 'absent' | 'non_clos'.

    Le bloc s'ouvre sur la PREMIÈRE ligne si elle vaut '---', et se ferme sur la
    ligne '---' suivante. Rien au-delà n'est lu : c'est la borne.
    """
    lignes = texte.split('\n')
    if not lignes or lignes[0].strip() != '---':
        return {}, 'absent'
    champs, clos = {}, False
    for ligne in lignes[1:]:
        if ligne.strip() == '---':
            clos = True
            break
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$', ligne)
        if m and m.group(1) not in champs:
            champs[m.group(1)] = m.group(2).strip()
    return champs, ('ok' if clos else 'non_clos')


def nettoie(valeur):
    """Retire guillemets encadrants et espaces. Ne normalise rien d'autre."""
    v = valeur.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1].strip()
    return v


# ----------------------------------------------------------------------------
# Analyse
# ----------------------------------------------------------------------------

def analyse(racine):
    pieces = []
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [d for d in sous if d not in EXCLUS]
        for f in sorted(fichiers):
            if f.endswith('.md'):
                chemin = os.path.join(dossier, f)
                rel = os.path.relpath(chemin, racine)
                try:
                    t = open(chemin, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                champs, statut = front_matter(t)
                pieces.append({
                    'chemin': rel,
                    'statut': statut,
                    'id': nettoie(champs['id']) if 'id' in champs else None,
                    'parent': nettoie(champs['parent']) if 'parent' in champs else None,
                    'version': nettoie(champs.get('version', '')),
                })

    sans_id, mal_formes, fm_absent, fm_non_clos, parents = [], [], [], [], []
    index = {}
    for p in pieces:
        if p['statut'] == 'absent':
            fm_absent.append(p)
        elif p['statut'] == 'non_clos':
            fm_non_clos.append(p)
        if p['parent']:
            parents.append(p)
        if p['id'] is None:
            sans_id.append(p)
        elif not ID_VALIDE.match(p['id']):
            mal_formes.append(p)
        else:
            index.setdefault(p['id'], []).append(p)

    collisions = {k: v for k, v in index.items() if len(v) > 1}
    return {
        'pieces': pieces, 'sans_id': sans_id, 'mal_formes': mal_formes,
        'fm_absent': fm_absent, 'fm_non_clos': fm_non_clos,
        'parents': parents, 'collisions': collisions, 'index': index,
    }


# ----------------------------------------------------------------------------
# Rapport
# ----------------------------------------------------------------------------

def rapport(r, complet=False):
    n = len(r['pieces'])
    exploitables = len(r['index'])
    print(f"ESPACE DES IDENTIFIANTS — {n} pièces .md examinées\n")
    print(f"  id: exploitables et uniques ......... {exploitables}")
    print(f"  pièces SANS id: ..................... {len(r['sans_id'])}")
    print(f"  id: MAL FORMÉS ...................... {len(r['mal_formes'])}")
    print(f"  id: EN COLLISION .................... {len(r['collisions'])}")
    print(f"  front-matter ABSENT ................. {len(r['fm_absent'])}")
    print(f"  front-matter NON CLOS ............... {len(r['fm_non_clos'])}")
    print(f"  champs `parent:` à absorber ......... {len(r['parents'])}")

    borne = None if complet else 12

    if r['collisions']:
        print("\n--- COLLISIONS (bloquant : un renvoi par id ne résout pas) ---")
        for k, v in sorted(r['collisions'].items()):
            print(f"  [CONSIGNATION] `{k}` revendiqué par {len(v)} fichiers :")
            for p in v:
                print(f"      {p['chemin']}  (version {p['version'] or '—'})")

    if r['mal_formes']:
        print("\n--- ID MAL FORMÉS (bloquant) ---")
        for p in r['mal_formes'][:borne]:
            print(f"  {p['chemin']}\n      id = {p['id'][:90]}")
        if borne and len(r['mal_formes']) > borne:
            print(f"  … {len(r['mal_formes']) - borne} autres (--complet)")

    if r['sans_id']:
        print("\n--- SANS ID (non référençables en l'état) ---")
        for p in r['sans_id'][:borne]:
            print(f"  {p['chemin']}")
        if borne and len(r['sans_id']) > borne:
            print(f"  … {len(r['sans_id']) - borne} autres (--complet)")

    if r['fm_absent'] or r['fm_non_clos']:
        print("\n--- FRONT-MATTER DÉFECTUEUX ---")
        for p in (r['fm_absent'] + r['fm_non_clos'])[:borne]:
            print(f"  {p['chemin']}  ({p['statut']})")

    if r['parents']:
        print("\n--- CHAMPS `parent:` EXISTANTS (convention informelle à absorber) ---")
        for p in r['parents'][:borne]:
            print(f"  {p['chemin']}\n      parent = {p['parent'][:90]}")
        if borne and len(r['parents']) > borne:
            print(f"  … {len(r['parents']) - borne} autres (--complet)")

    bloquants = len(r['collisions']) + len(r['mal_formes'])
    print(f"\nBILAN : {bloquants} défaut(s) BLOQUANT(S) pour un renvoi par `id:` ; "
          f"{len(r['sans_id'])} pièce(s) non référençable(s).")
    print("§6.4 : ce constat ne scelle rien, ne compte rien, ne démontre rien.")
    return bloquants + len(r['sans_id'])


# ----------------------------------------------------------------------------
# Auto-test MORDANT
#
# Chaque contrôle est apparié : un cas qui DOIT être signalé, et un cas voisin
# qui NE DOIT PAS l'être. Un détecteur qui répondrait toujours « défaut » ou
# toujours « rien » échoue sur la moitié des assertions. C'est ce qui interdit
# le PASS structurellement vacant (précédent S9 : quatre faux PASS sur un lot
# qui se présentait à 38/38).
# ----------------------------------------------------------------------------

CAS = {
    'a_valide.md':        '---\nid: LC-A-VALIDE\nversion: 1.0\n---\n\ncorps\n',
    'b_sans_id.md':       '---\ntitre: "rien"\nversion: 1.0\n---\n\ncorps\n',
    'c_placeholder.md':   '---\nid: "à assigner — proposé : HKB-07"\n---\n\ncorps\n',
    'd_collision_1.md':   '---\nid: LC-DOUBLON\nversion: 1.0\n---\n\ncorps\n',
    'd_collision_2.md':   '---\nid: LC-DOUBLON\nversion: 2.0\n---\n\ncorps\n',
    'e_non_clos.md':      '---\nid: LC-NON-CLOS\nversion: 1.0\n\ncorps sans fermeture\n',
    'f_fm_absent.md':     '# Titre direct\n\nid: LC-PIEGE\n\ncorps\n',
    'g_parent.md':        '---\nid: LC-AVEC-PARENT\nparent: NOTE-BORD-EON-05 (§6)\n---\n\ncorps\n',
    'h_ponctue.md':       '---\nid: LC-D3.CROSS_over-2/b\n---\n\ncorps\n',
    'i_id_en_corps.md':   '---\nid: LC-PROPRE\n---\n\nid: LC-USURPATEUR\n\ncorps\n',
    # Cas DISCRIMINANT de la borne : le front-matter ne porte PAS d'id, le corps
    # en porte un. Sans borne, l'usurpateur est lu et la pièce paraît identifiée.
    # Le cas `i` ci-dessus ne discriminait pas : la règle « première occurrence
    # gagne » masquait l'absence de borne. Trouvé par mutation, non par relecture.
    'j_id_corps_seul.md': '---\ntitre: "sans id"\n---\n\nid: LC-USURPATEUR\n\ncorps\n',
}


def self_test():
    tmp = tempfile.mkdtemp(prefix='audit_id_')
    try:
        for nom, contenu in CAS.items():
            open(os.path.join(tmp, nom), 'w', encoding='utf-8').write(contenu)
        r = analyse(tmp)
        par_chemin = {p['chemin']: p for p in r['pieces']}
        ids = {p['chemin']: p['id'] for p in r['pieces']}
        sans = {p['chemin'] for p in r['sans_id']}
        mal = {p['chemin'] for p in r['mal_formes']}
        par = {p['chemin'] for p in r['parents']}
        nclos = {p['chemin'] for p in r['fm_non_clos']}
        abs_ = {p['chemin'] for p in r['fm_absent']}

        A = [
            # paire 1 — présence de l'id
            ("id présent non signalé absent",      'a_valide.md' not in sans),
            ("id absent signalé",                  'b_sans_id.md' in sans),
            # paire 2 — bonne formation
            ("id propre non signalé mal formé",    'a_valide.md' not in mal),
            ("placeholder signalé mal formé",      'c_placeholder.md' in mal),
            # paire 3 — collision
            ("id unique sans collision",           'LC-A-VALIDE' not in r['collisions']),
            ("id doublé en collision",             'LC-DOUBLON' in r['collisions']),
            ("collision porte ses 2 fichiers",     len(r['collisions'].get('LC-DOUBLON', [])) == 2),
            # paire 4 — front-matter
            ("front-matter clos non signalé",      'a_valide.md' not in nclos | abs_),
            ("front-matter non clos signalé",      'e_non_clos.md' in nclos),
            ("front-matter absent signalé",        'f_fm_absent.md' in abs_),
            # paire 5 — parent
            ("absence de parent non listée",       'a_valide.md' not in par),
            ("parent présent listé",               'g_parent.md' in par),
            # gardes
            ("ponctuation licite non rejetée",     'h_ponctue.md' not in mal),
            ("id du CORPS non lu comme id",        ids.get('i_id_en_corps.md') == 'LC-PROPRE'),
            ("hors borne : aucun id retenu",       ids.get('j_id_corps_seul.md') is None),
            ("hors borne : pièce dite sans id",    'j_id_corps_seul.md' in sans),
        ]
        ko = 0
        for libelle, ok in A:
            print(f"  [{'PASS' if ok else 'FAIL'}] {libelle}")
            ko += 0 if ok else 1
        print(f"\nAUTO-TEST MORDANT : {len(A) - ko}/{len(A)} — "
              f"8 paires appariées, aucun PASS obtenable par réponse constante.")
        return 1 if ko else 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ----------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    if '--self-test' in args:
        return self_test()
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for a in args:
        if not a.startswith('--'):
            racine = a
    defauts = rapport(analyse(racine), complet='--complet' in args)
    return 1 if ('--strict' in args and defauts) else 0


if __name__ == '__main__':
    sys.exit(main())
