#!/usr/bin/env python3
# =====================================================================
# LC-WORK-GEN-PAQUET-v2_1.py — GENERATEUR DE PAQUETS, v2.1
# codename: LC-RACCORD
# MANDAT : P-8 de LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE v0.1
#          (gel cc856f67, date 2026-07-17). Les cibles (i)-(iv) du
#          mandat sont figees AVANT ce fichier ; elles ne sont pas
#          re-choisies ici. Ce script les INSTRUMENTE, il ne les vote pas.
#
# CE QUE LE MANDAT P-8 EXIGE, ET CE QUE CE SCRIPT FAIT :
#   (i)   emet DEUX tranches nommees ; REFUSE par defaut la tranche unique.
#   (ii)  tranche unique UNIQUEMENT sur drapeau d'inapplicabilite explicite,
#         et alors ECRIT LUI-MEME la clause P-6 en clair dans le PROMPT
#         (le texte de la clause est ecrit PAR LE SCRIPT, jamais a la main).
#   (iii) SCANNE la tranche 1 pour les formulations interdites par P-7 et
#         rend un CODE DE SORTIE NON NUL si l'une y figure.
#   (iv)  consigne au manifeste, par un CHAMP NOMME, le regime employe :
#         'sequence' ou 'inapplicabilite-declaree'. Champ absent = DEFAUT.
#   + P-1 : test MATERIEL de multi-tours. Un paquet qui instancie un
#           mecanisme de retour (droit de tirage / clarification /
#           livraison differee) EST multi-tours : --inapplicable est REFUSE.
#
# GRADE : INSTRUMENT. Ne scelle rien, ne vote rien, ne fait foi de rien.
#         LE MOUNT FAIT FOI (R-54). §6.4 : produire des tranches,
#         calculer des sha NE SCELLE, NE REDUIT, NE COMPTE, NE DEMONTRE RIEN.
#
# P-9 (rappele) : le DEPOT de ce script n'atteste RIEN d'autre que son
#         existence. Sa valeur se mesure A LA PROCHAINE GATE, par un fait
#         verifiable : la tranche 2 a-t-elle ete expediee APRES l'issue de
#         Phase 2, oui ou non. Ecrire l'instrument ne solde pas la gate.
#
# R-36 : ce fichier n'embarque NI son propre sha NI aucune valeur qu'il
#         produirait. sha256 a consigner HORS-FICHIER au depot.
#
# BORNES CLOSES :
#   b1 — Ne TOUCHE PAS le mount. Les sources restent INTACTES (lecture seule).
#   b2 — Ne JUGE PAS le scope. Le scan de blinding reste DU, cote operateur.
#   b3 — N'EXPEDIE RIEN. Il produit des fichiers ; l'envoi (et son ORDRE)
#         reste un geste operateur — c'est exactement ce que P-9 mesure.
#   b4 — Le scan P-7 est une PORTE (exit != 0), pas un verdict d'usage :
#         il rend non nul sur presence, il n'interprete pas l'intention.
#   b5 — Ne dit RIEN de la substance. {A4 ; A2* ; N} INCHANGE.
# =====================================================================

import os, re, sys, hashlib, argparse, tempfile, shutil

# --------------------------------------------------------------------------
# Clause P-6 — VERBATIM du mandat (§2, P-6). Ecrite PAR LE SCRIPT (P-8 ii).
# Ne jamais la reformuler a la main : c'est le point de (ii).
CLAUSE_P6 = (
    "anti-ancrage NON instrumente, les pieces aval sont jointes au meme "
    "envoi, l'ordre de lecture est une DEMANDE et non une CONTRAINTE."
)

# --------------------------------------------------------------------------
# P-7 — formulations de PRETENTION DE CONTRAINTE, interdites (§2, P-7).
# Les trois nommees + equivalentes. Une pretention de contrainte n'est
# jamais legitime : la contrainte est un FAIT du dispositif (deux tranches),
# elle se DECRIT, elle ne se PRETEND pas. Scan sur la tranche 1 (P-8 iii).
P7_INTERDITS = [
    r"cet ordre est contraignant",
    r"ordre\s+contraignant",
    r"ordre\s+impos[ée]",
    r"tu\s+ne\s+peux\s+pas",
    r"vous\s+ne\s+pouvez\s+pas",
    r"il\s+(?:t'|vous\s+)?est\s+interdit\s+de\s+lire",
    r"lecture\s+contrainte",
]

# --------------------------------------------------------------------------
# P-1 — marqueurs de MECANISME DE RETOUR. Presence => canal multi-tours
# ACQUIS PAR LE PAQUET LUI-MEME. Le test est FACTUEL, pas declaratif.
RETOUR_MARQUEURS = [
    r"droit\s+de\s+tirage",
    r"livr[ée]\s+.{0,20}\bau\s+tour\s+suivant\b",
    r"\btour\s+suivant\b",
    r"livraison\s+diff[ée]r[ée]e",
    r"question\s+de\s+clarification",
    r"tranche\s*2",
]


def _sha_size(path):
    b = open(path, "rb").read()
    return hashlib.sha256(b).hexdigest(), len(b)


def _verifie_gel(path, gel8):
    """Verifie qu'une source du mount porte le gel attendu. ARRET sinon."""
    s, _ = _sha_size(path)
    if gel8 is not None and s[:8] != gel8:
        raise SystemExit(
            f"*** {os.path.basename(path)} : sha {s[:8]} != gel attendu {gel8} "
            f"— ARRET (le mount a bouge ?)")
    return s


def _bloc_sha(pieces, livrees):
    """Bloc sha COMPLET (P-2) : nom / sha256 / octets de TOUTES les pieces,
    y compris celles NON ENCORE LIVREES en tranche 1. 'livrees' = ensemble
    des noms deja joints (pour marquer JOINTE / AVAL-NON-JOINTE)."""
    lignes = ["--- BLOC SHA (complet, y compris pieces aval non jointes) ---"]
    for nom, sha, taille in pieces:
        etat = "JOINTE" if nom in livrees else "AVAL — NON JOINTE (a confronter au tour suivant)"
        lignes.append(f"{nom}  sha256={sha}  octets={taille}  [{etat}]")
    lignes.append("--- fin bloc sha ---")
    return "\n".join(lignes)


def _scan_p7(texte):
    """P-8 (iii). Retourne la liste des occurrences interdites (l.n, motif, ctx)."""
    hits = []
    for pat in P7_INTERDITS:
        for m in re.finditer(pat, texte, re.I):
            ln = texte[: m.start()].count("\n") + 1
            hits.append((ln, pat, texte.split("\n")[ln - 1].strip()[:90]))
    return sorted(hits)


def _est_multitours(prompt_texte, aval):
    """P-1. Multi-tours si le paquet instancie un mecanisme de retour, OU si
    des pieces aval sont declarees (une livraison differee EST un retour)."""
    if aval:
        return True, "des pieces aval sont declarees (livraison differee = retour)"
    for pat in RETOUR_MARQUEURS:
        if re.search(pat, prompt_texte, re.I):
            return True, f"marqueur de retour present : {pat!r}"
    return False, "aucun mecanisme de retour instancie"


def _ecrit_manifeste(out, regime, tranches, pieces):
    """P-8 (iv). CHAMP NOMME 'REGIME' toujours ecrit. Absent = defaut :
    ce script ne l'omet jamais."""
    lignes = [
        "# MANIFESTE DE PAQUET (genere) — LE MOUNT FAIT FOI (R-54)",
        f"REGIME: {regime}",            # <-- champ nomme (iv). JAMAIS absent.
        f"TRANCHES: {len(tranches)}",
    ]
    for i, (nom, sha) in enumerate(tranches, 1):
        lignes.append(f"TRANCHE-{i}: {nom}  sha256={sha}")
    lignes.append("PIECES:")
    for nom, sha, taille in pieces:
        lignes.append(f"  {nom}  sha256={sha}  octets={taille}")
    lignes.append("# §6.4 : ce manifeste n'atteste que des octets, jamais une conclusion.")
    p = os.path.join(out, "MANIFESTE.txt")
    open(p, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    return p


# ==========================================================================
# GENERATION
# ==========================================================================
def generer(prompt_texte, amont, aval, out, inapplicable=False):
    """amont / aval : listes de (nom, chemin, gel8|None). Retourne (regime, exit)."""
    os.makedirs(out, exist_ok=True)

    # Mesure + verif gel de toutes les pieces (lecture seule, b1).
    def _mesure(liste):
        r = []
        for nom, chemin, gel8 in liste:
            if not os.path.exists(chemin):
                raise SystemExit(f"*** SOURCE ABSENTE DU MOUNT : {nom} — ARRET")
            sha = _verifie_gel(chemin, gel8)
            r.append((nom, sha, os.path.getsize(chemin)))
        return r

    pm, pv = _mesure(amont), _mesure(aval)
    toutes = pm + pv

    multitours, motif = _est_multitours(prompt_texte, aval)

    # ---- Cas INAPPLICABILITE (tranche unique) — P-6 / P-1 -----------------
    if inapplicable:
        # P-1 : refus si le canal est materiellement multi-tours.
        if multitours:
            print(f"*** --inapplicable REFUSE (P-1) : {motif}.")
            print("    Le pilote ne peut pas declarer one-shot un canal dont le "
                  "paquet exploite le retour.")
            return "REFUSE-P1", 2
        # Le SCRIPT ecrit la clause P-6 en clair (P-8 ii), jamais a la main.
        prompt_final = (
            prompt_texte.rstrip()
            + "\n\n--- CLAUSE P-6 (ecrite par le generateur, inapplicabilite) ---\n"
            + CLAUSE_P6 + "\n"
            + _bloc_sha(toutes, livrees={n for n, *_ in toutes}) + "\n"
        )
        hits = _scan_p7(prompt_final)                       # (iii) scan
        chemin_t1 = os.path.join(out, "TRANCHE-UNIQUE.txt")
        open(chemin_t1, "w", encoding="utf-8").write(prompt_final)
        sha_t1, _ = _sha_size(chemin_t1)
        _ecrit_manifeste(out, "inapplicabilite-declaree",
                         [("TRANCHE-UNIQUE.txt", sha_t1)], toutes)
        if hits:
            print("*** SCAN P-7 : formulation(s) de PRETENTION DE CONTRAINTE presente(s) :")
            for ln, pat, ctx in hits:
                print(f"      l.{ln}  [{pat}]  {ctx}")
            print("    Code de sortie NON NUL (P-8 iii).")
            return "inapplicabilite-declaree", 3
        print(f"Regime : INAPPLICABILITE DECLAREE. Tranche unique : {chemin_t1}")
        print(f"Clause P-6 ecrite par le script. sha T1 = {sha_t1[:8]}")
        return "inapplicabilite-declaree", 0

    # ---- Cas SEQUENCE (defaut) — P-2 : DEUX tranches ----------------------
    # (i) refus implicite de la tranche unique : la seule sortie sans drapeau
    #     est en deux fichiers separes.
    livrees_t1 = {n for n, *_ in pm}
    tranche1 = (
        prompt_texte.rstrip() + "\n\n"
        + "--- PIECES AMONT (identite / source) ---\n"
        + ("\n".join(f"[JOINTE] {n}" for n, *_ in pm) or "(aucune)") + "\n\n"
        + _bloc_sha(toutes, livrees_t1) + "\n\n"
        + "Les pieces AVAL ne sont PAS jointes a cette tranche. Elles seront "
        "expediees APRES votre Phase 2 rendue ; a reception, recomputez leur "
        "sha256 et confrontez-le au bloc ci-dessus (P-5). Ecart => ARRET, "
        "tranche 2 reputee contaminee, la Phase 2 reste ACQUISE.\n"
    )
    hits = _scan_p7(tranche1)                               # (iii) scan sur T1
    chemin_t1 = os.path.join(out, "TRANCHE-1.txt")
    open(chemin_t1, "w", encoding="utf-8").write(tranche1)

    tranche2 = (
        "--- TRANCHE 2 — pieces aval (a n'expedier qu'APRES la Phase 2 rendue) ---\n"
        + ("\n".join(f"[AVAL] {n}  (sha pre-communique en tranche 1)" for n, *_ in pv)
           or "(aucune piece aval)") + "\n"
    )
    chemin_t2 = os.path.join(out, "TRANCHE-2.txt")
    open(chemin_t2, "w", encoding="utf-8").write(tranche2)

    sha_t1, _ = _sha_size(chemin_t1)
    sha_t2, _ = _sha_size(chemin_t2)
    _ecrit_manifeste(out, "sequence",
                     [("TRANCHE-1.txt", sha_t1), ("TRANCHE-2.txt", sha_t2)], toutes)

    if hits:
        print("*** SCAN P-7 (tranche 1) : PRETENTION DE CONTRAINTE presente :")
        for ln, pat, ctx in hits:
            print(f"      l.{ln}  [{pat}]  {ctx}")
        print("    Code de sortie NON NUL (P-8 iii).")
        return "sequence", 3

    print("Regime : SEQUENCE (deux tranches, tranche unique refusee par defaut).")
    print(f"  {chemin_t1}   sha={sha_t1[:8]}")
    print(f"  {chemin_t2}   sha={sha_t2[:8]}   (a expedier APRES Phase 2 rendue)")
    print(f"  bloc sha complet (aval pre-communique) : {len(toutes)} piece(s).")
    print("§6.4 : rien de scelle. LE MOUNT FAIT FOI.")
    return "sequence", 0


# ==========================================================================
# AUTO-TEST MORDANT — chaque garde a un PORTEUR MUTABLE ; sans lui, un
# assert vrai serait un FAUX PASS (discipline harnais R-9/R-11).
# ==========================================================================
def auto_test():
    tmp = tempfile.mkdtemp(prefix="p8test_")
    ok = []
    try:
        # fabrique deux pieces sources bidon (mount simule, lecture seule)
        pa = os.path.join(tmp, "AMONT.md"); open(pa, "w").write("piece amont\n")
        pv = os.path.join(tmp, "AVAL.md");  open(pv, "w").write("piece aval\n")
        sha_pa, _ = _sha_size(pa)
        amont = [("AMONT.md", pa, sha_pa[:8])]
        aval  = [("AVAL.md",  pv, None)]
        PROMPT = "Phase 0-2. Identite + source seulement.\n"

        # T1 (i) : mode defaut => DEUX fichiers tranche, PAS de fichier unique.
        o1 = os.path.join(tmp, "o1")
        reg, rc = generer(PROMPT, amont, aval, o1, inapplicable=False)
        deux = os.path.exists(os.path.join(o1, "TRANCHE-1.txt")) and \
               os.path.exists(os.path.join(o1, "TRANCHE-2.txt"))
        pas_unique = not os.path.exists(os.path.join(o1, "TRANCHE-UNIQUE.txt"))
        # porteur mutable : si la garde tombait, l'un des deux serait faux.
        ok.append(("(i) deux tranches, refus tranche unique", deux and pas_unique and rc == 0))

        # T2 (P-2) : le sha+octets de la piece AVAL figure dans la tranche 1.
        t1 = open(os.path.join(o1, "TRANCHE-1.txt")).read()
        sha_pv, taille_pv = _sha_size(pv)
        aval_precommis = (sha_pv in t1) and (str(taille_pv) in t1) and ("NON JOINTE" in t1)
        # mutation-controle : un sha modifie NE doit PAS matcher (garde non vacante)
        faux = sha_pv[:-1] + ("0" if sha_pv[-1] != "0" else "1")
        garde_non_vacante = faux not in t1
        ok.append(("(P-2) sha+octets aval PRE-COMMIS en tranche 1", aval_precommis and garde_non_vacante))

        # T3 (iii) : PRETENTION DE CONTRAINTE plantee => code non nul ;
        #            retiree => code nul. Porteur = la phrase elle-meme.
        o3a = os.path.join(tmp, "o3a")
        _, rc_avec = generer(PROMPT + "\ncet ordre est contraignant.\n", amont, aval, o3a)
        o3b = os.path.join(tmp, "o3b")
        _, rc_sans = generer(PROMPT, amont, aval, o3b)
        ok.append(("(iii) scan P-7 mord (non nul avec / nul sans)", rc_avec != 0 and rc_sans == 0))

        # T4 (iv) : le manifeste porte TOUJOURS le champ REGIME.
        man = open(os.path.join(o1, "MANIFESTE.txt")).read()
        champ_present = re.search(r"^REGIME:\s*\S", man, re.M) is not None
        # mutation-controle : sans le prefixe exact, la garde ne matcherait pas.
        garde4 = re.search(r"^REGIME:\s*$", man, re.M) is None
        ok.append(("(iv) champ REGIME present au manifeste (absent=defaut)", champ_present and garde4))

        # T5 (P-1) : --inapplicable REFUSE quand des pieces aval existent
        #            (canal materiellement multi-tours) ; ACCEPTE en one-shot.
        o5a = os.path.join(tmp, "o5a")
        reg5a, rc5a = generer(PROMPT, amont, aval, o5a, inapplicable=True)   # doit refuser
        o5b = os.path.join(tmp, "o5b")
        reg5b, rc5b = generer(PROMPT, amont, [], o5b, inapplicable=True)     # one-shot => OK
        clause_ecrite = os.path.exists(os.path.join(o5b, "TRANCHE-UNIQUE.txt")) and \
            CLAUSE_P6 in open(os.path.join(o5b, "TRANCHE-UNIQUE.txt")).read()
        ok.append(("(P-1) inapplicable refuse si retour ; clause P-6 ecrite en one-shot",
                   rc5a == 2 and reg5a == "REFUSE-P1" and rc5b == 0 and clause_ecrite))

        # T6 (ii) : la clause P-6 est ecrite PAR LE SCRIPT verbatim, jamais a la main.
        #           porteur : le texte doit etre IDENTIQUE a la constante du script.
        t_unique = open(os.path.join(o5b, "TRANCHE-UNIQUE.txt")).read()
        ok.append(("(ii) clause P-6 verbatim = constante du script", CLAUSE_P6 in t_unique))

        print("\n############ AUTO-TEST MORDANT P-8 ############")
        n_ok = 0
        for nom, val in ok:
            print(f"  [{'PASS' if val else 'FAIL'}]  {nom}")
            n_ok += bool(val)
        print(f"  ---> {n_ok}/{len(ok)} gardes mordantes.")
        print("  §6.4 : passer l'auto-test NE SCELLE, NE COMPTE, NE DEMONTRE RIEN.")
        print("  P-9 : la valeur de P-8 se mesure A LA PROCHAINE GATE, pas ici.")
        return 0 if n_ok == len(ok) else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description="Generateur de paquets v2.1 (mandat P-8).")
    ap.add_argument("--self-test", action="store_true", help="auto-test mordant des gardes (i)-(iv), P-1")
    ap.add_argument("--inapplicable", action="store_true",
                    help="tranche unique : SEULEMENT si canal one-shot materiel (P-1/P-6)")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(auto_test())
    print("Ce script est le GENERATEUR (mandat P-8). Import comme module pour "
          "'generer(prompt, amont, aval, out, inapplicable=)', ou lance --self-test.")
    print("R-36 : sha256 a consigner hors-fichier. LE MOUNT FAIT FOI (R-54). §6.4.")


if __name__ == "__main__":
    main()
