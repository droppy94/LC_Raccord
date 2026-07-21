#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inventaire_sceaux.py — Silo G-0 (LC-WORK-LOTISSEMENT-SILOS §6).

Inventaire rejouable de l'écart « sceaux verif_*.py cités dans la KB »
↔ « sceaux présents dans le dépôt » (LIVE = instruments/, ARCHIVE =
instruments/archives-scelees/). Sortie : audit/INVENTAIRE-SCEAUX.md.

§6.4 : inventorier ne scelle, ne réduit, ne compte, ne démontre rien.
Un fichier présent n'atteste que des octets ; un EXIT 0 relève du rejeu
(Silo G-3), jamais de cet inventaire.

Usage : python3 instruments/inventaire_sceaux.py [racine_depot]
        (défaut : parent du dossier du script)
EXIT 0 = inventaire produit ; EXIT 1 = erreur d'E/S.
"""
import hashlib
import os
import re
import sys
from datetime import date

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                       else os.path.join(os.path.dirname(__file__), ".."))
KB = os.path.join(ROOT, "kb")
MANIFEST = os.path.join(ROOT, "manifest")
LIVE = os.path.join(ROOT, "instruments")
ARCH = os.path.join(LIVE, "archives-scelees")
OUT = os.path.join(ROOT, "audit", "INVENTAIRE-SCEAUX.md")

PAT = re.compile(r"verif_[A-Za-z0-9_]+\.py")
CANON = re.compile(r"(__\d+_?)+(?=\.py$)")  # suffixes __1_, __2_ ...


def canon(name: str) -> str:
    return CANON.sub("", name)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    cited = {}
    for base in (KB, MANIFEST):
        if not os.path.isdir(base):
            continue
        for fn in sorted(os.listdir(base)):
            if not fn.endswith(".md"):
                continue
            with open(os.path.join(base, fn), encoding="utf-8",
                      errors="replace") as f:
                for m in PAT.findall(f.read()):
                    cited.setdefault(canon(m), set()).add(fn)

    def listing(d):
        if not os.path.isdir(d):
            return {}
        return {f: sha256(os.path.join(d, f))
                for f in sorted(os.listdir(d))
                if f.endswith(".py") and PAT.fullmatch(f)}

    live = listing(LIVE)
    arch = listing(ARCH)

    rows = []
    for name in sorted(set(cited) | set(live) | set(arch)):
        statut = ("LIVE" if name in live else
                  "ARCHIVE" if name in arch else "ABSENT")
        sha = live.get(name) or arch.get(name) or "—"
        rows.append((name, statut, sha[:16] if sha != "—" else sha,
                     len(cited.get(name, ()))))

    n_live = sum(1 for r in rows if r[1] == "LIVE")
    n_arch = sum(1 for r in rows if r[1] == "ARCHIVE")
    n_abs = sum(1 for r in rows if r[1] == "ABSENT")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as g:
        g.write("# Inventaire sceaux cités ↔ présents (G-0)\n\n")
        g.write(f"Généré par `instruments/inventaire_sceaux.py` le "
                f"{date.today().isoformat()} — rejouable.\n\n")
        g.write(f"**Bilan** : {len(rows)} sceaux au total — "
                f"{n_live} LIVE · {n_arch} ARCHIVE (pinnés-clos, non rejoués) "
                f"· {n_abs} ABSENTS.\n\n")
        g.write("§6.4 : un statut LIVE/ARCHIVE atteste des octets, jamais un "
                "EXIT 0 ni une conclusion physique.\n\n")
        g.write("| sceau (canon) | statut | sha256 (16) | citations KB |\n")
        g.write("|---|---|---|---|\n")
        for name, st, sh, nc in rows:
            g.write(f"| `{name}` | {st} | `{sh}` | {nc} |\n")
    print(f"OK : {OUT} — {n_live} LIVE / {n_arch} ARCHIVE / {n_abs} ABSENTS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
