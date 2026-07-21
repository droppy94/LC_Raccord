#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_sceau.py — Silo G-2 (portabilité des sceaux sur le layout git).

CONSTAT (2026-07-21, cas témoin verif_paquet_propre.py) : les sceaux
résolvent leurs fichiers KB RELATIVEMENT AU CWD — convention du mount
/mnt/project (layout plat). Sur le dépôt git, la KB vit sous kb/ ⟹ un
sceau lancé depuis la racine échoue (« paquet introuvable »).

CORRECTIF : ce lanceur exécute le sceau avec cwd = racine KB, SANS
TOUCHER AUX OCTETS DU SCEAU — les sha8 cités au manifeste restent
conformes ; aucun swap d'instrument, aucun grade déplacé.

Usage :
  python3 instruments/run_sceau.py NOM[.py] [-- args du sceau…]
  Options : --kb-root DIR (défaut $LC_KB_ROOT sinon <depot>/kb)
            --timeout S   (défaut 900)
Résolution du sceau : instruments/ puis instruments/archives-scelees/.
Sortie : sortie du sceau, puis une ligne CONSIGNATION (nom, sha8 du
sceau, rc, durée, kb-root). Code retour = rc du sceau.

§6.4 : lancer un sceau n'atteste que cette exécution-ci sur ce clone ;
un EXIT 0 ici ne rejoue aucune gate, ne requalifie aucun grade, ne
scelle, ne réduit, ne compte, ne démontre rien.
"""
import argparse
import hashlib
import os
import subprocess
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def sha8(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:8]


def resolve(name: str) -> str:
    if not name.endswith(".py"):
        name += ".py"
    for d in ("instruments", os.path.join("instruments", "archives-scelees")):
        p = os.path.join(ROOT, d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERREUR : sceau introuvable ({name}) — cherché dans "
             f"instruments/ et instruments/archives-scelees/")


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("sceau")
    ap.add_argument("--kb-root",
                    default=os.environ.get("LC_KB_ROOT",
                                           os.path.join(ROOT, "kb")))
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("args", nargs="*")
    ns = ap.parse_args()

    kb = os.path.abspath(ns.kb_root)
    if not os.path.isdir(kb):
        sys.exit(f"ERREUR : racine KB introuvable ({kb})")
    seal = resolve(ns.sceau)
    digest = sha8(seal)
    zone = ("ARCHIVE" if os.sep + "archives-scelees" + os.sep in seal
            else "LIVE")

    t0 = time.time()
    try:
        rc = subprocess.run([sys.executable, seal, *ns.args],
                            cwd=kb, timeout=ns.timeout).returncode
        note = ""
    except subprocess.TimeoutExpired:
        rc, note = 124, f" [TIMEOUT {ns.timeout}s]"
    dt = time.time() - t0

    print(f"\nCONSIGNATION run_sceau : {os.path.basename(seal)} [{zone}] "
          f"sha8={digest} rc={rc}{note} durée={dt:.1f}s kb-root={kb}")
    print("§6.4 : cette ligne atteste UNE exécution sur CE clone — "
          "rien d'autre.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
