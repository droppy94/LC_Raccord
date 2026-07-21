#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cse_gel_expedition.py — Gel d'expédition du CSE incognito R-4/R-5.

Instancie la spec du §3 de audit/RESERVE-AVEUGLEMENT-R4-R5.md :
- fige la QUESTION (et rien d'autre),
- fige l'ESPACE-VERDICT { E-1 ; E-2 ; E-3 } AVANT expédition,
- calcule les sha256 des 7 pièces nommées (écrits par script, R-36),
- déclare la CONJECTURE DU PILOTE avec son motif de suspicion.

Sortie : audit/CSE-R4R5-GEL.md.
Piège R-36 : le fichier de gel NE PORTE PAS son propre sha ; celui-ci
est imprimé sur stdout et se consigne HORS du fichier (message de
commit / rapport opérateur).

§6.4 : geler une expédition ne scelle, ne réduit, ne compte, ne
démontre rien. { A4 ; A2★ ; N } INCHANGÉ.

EXIT 0 = gel produit ; EXIT 1 = pièce manquante ou erreur d'E/S.
"""
import hashlib
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "audit", "CSE-R4R5-GEL.md")

PIECES = [
    "audit/R4-CIBLES-GELEES.md",
    "instruments/redemo_R4_CT.py",
    "audit/R4-REDEMONSTRATION.md",
    "audit/R5-CIBLES-GELEES.md",
    "instruments/redemo_R5_reductions.py",
    "audit/R5-REDEMONSTRATION.md",
    "audit/RESERVE-AVEUGLEMENT-R4-R5.md",
]

QUESTION = (
    "Les scripts `redemo_R4_CT.py` et `redemo_R5_reductions.py` "
    "constituent-ils une redérivation dont la force probante est "
    "INDÉPENDANTE des têtes, ou une reproduction GUIDÉE par les "
    "front-matters ? Les asserts testent-ils les cibles ou les "
    "paraphrasent-ils (tautologie) ?"
)

VERDICTS = [
    ("E-1", "CORROBORATION RECEVABLE — calculs indépendants au niveau "
            "des asserts, guidage limité au choix de route."),
    ("E-2", "REPRODUCTION GUIDÉE — valeur de corroboration faible, "
            "requalification à consigner."),
    ("E-3", "DÉFAUT SUBSTANTIEL — assert tautologique ou cible "
            "paraphrasée ; instruit au lot R-n concerné."),
]

CONJECTURE = (
    "Le pilote conjecture E-1 ou E-2-bénin. MOTIF DE SUSPICION déclaré : "
    "ce sont les issues qui le servent (c'est son propre travail) ⟹ "
    "charge lourde sur E-1 ; MANDAT à l'auditeur de consigner tout "
    "défaut de rédaction favorisant E-1, même si l'issue reste E-1. "
    "L'incognito PRÉVAUT ; le pilote consigne, ne re-juge pas."
)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    rows = []
    for rel in PIECES:
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            print(f"ERREUR : pièce manquante — {rel}", file=sys.stderr)
            return 1
        rows.append((rel, sha256(p), os.path.getsize(p)))

    with open(OUT, "w", encoding="utf-8") as g:
        g.write("# CSE incognito R-4/R-5 — GEL D'EXPÉDITION\n\n")
        g.write(f"Gelé le {date.today().isoformat()} par "
                "`instruments/cse_gel_expedition.py` (rejouable). "
                "Instancie audit/RESERVE-AVEUGLEMENT-R4-R5.md §3.\n\n")
        g.write("Piège R-36 : ce fichier ne porte pas son propre sha ; "
                "il est imprimé par le script et consigné hors-fichier.\n\n")
        g.write("## Question (et rien d'autre)\n\n" + QUESTION + "\n\n")
        g.write("## Espace-verdict — GELÉ AVANT EXPÉDITION\n\n")
        for k, v in VERDICTS:
            g.write(f"- **{k}** : {v}\n")
        g.write("\nToute issue hors { E-1 ; E-2 ; E-3 } est un refus "
                "d'expédition, pas un verdict.\n\n")
        g.write("## Pièces jointes (7) — sha256 écrits par script\n\n")
        g.write("| pièce | sha256 | octets |\n|---|---|---|\n")
        for rel, sh, sz in rows:
            g.write(f"| `{rel}` | `{sh}` | {sz} |\n")
        g.write("\n## Conjecture du pilote — déclarée\n\n" + CONJECTURE + "\n\n")
        g.write("## §6.4\n\nGeler, expédier, consigner : rien de tout "
                "cela ne scelle, ne réduit, ne compte, ne démontre. "
                "{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI "
                "réfutée.\n")

    print(f"GEL produit : {OUT}")
    for rel, sh, sz in rows:
        print(f"  {sh[:16]}  {rel}")
    print(f"sha256(GEL) = {sha256(OUT)}  ← à consigner HORS-FICHIER (R-36)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
