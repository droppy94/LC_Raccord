#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""harnais_R9.py — mutations du PORTEUR de chaque cible (précédent S7) :
chaque mutant doit sortir rc != 0. Une mutation qui ne mord pas se
REMPLACE, ne se compte jamais."""
import subprocess
import sys
import pathlib

SRC = pathlib.Path(__file__).parent / "redemo_R9_tracteur.py"
base = SRC.read_text()

MUTS = [
    ("m1 rang tracteur n+2 -> n+1 (porteur A1)",
     "rang = n + 2", "rang = n + 1"),
    ("m2 identite 2D : K -> 2K (porteur A2, coeff de section)",
     "cible = K*(g[a_, m_]*g[b_, nu] - g[a_, nu]*g[b_, m_])",
     "cible = 2*K*(g[a_, m_]*g[b_, nu] - g[a_, nu]*g[b_, m_])"),
    ("m3 comptage Weyl (n-3) -> (n-4) (porteur A3)",
     "f = n*(n + 1)*(n + 2)*(n - 3)/12",
     "f = n*(n + 1)*(n + 2)*(n - 4)/12"),
    ("m4 facteur rond 4/(1+r2)**2 -> 4/(1+r2) (porteur A4)",
     "Om2 = 4/(1 + r2)**2", "Om2 = 4/(1 + r2)"),
    ("m5 Schouten n=3 : R/4 -> R/6 (porteur A5, la jambe Cotton)",
     "P3 = Ric - Rsc/4*g3", "P3 = Ric - Rsc/6*g3"),
    ("m6 temoin Nil -> delta3 (porteur A6, le firewall lui-meme)",
     "gN = sp.Matrix([[1, 0, 0], [0, 1 + x**2, -x], [0, -x, 1]])",
     "gN = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])"),
]

morda = 0
for nom, old, new in MUTS:
    if old not in base:
        print("[VACANTE-CIBLAGE] %s : motif absent — A REMPLACER" % nom)
        continue
    mut = base.replace(old, new)
    p = pathlib.Path("/tmp/mutant_R9.py")
    p.write_text(mut)
    r = subprocess.run([sys.executable, str(p)], capture_output=True,
                       text=True, timeout=900)
    if r.returncode != 0:
        ligne = [l for l in r.stdout.splitlines() if "[FAIL]" in l]
        print("[MORD] %s -> rc=%d, premier FAIL : %s"
              % (nom, r.returncode, ligne[0].strip() if ligne else "(exit)"))
        morda += 1
    else:
        print("[VACANTE] %s -> rc=0 : NE MORD PAS, a remplacer" % nom)

print("\nHARNAIS R-9 : %d/%d mordantes" % (morda, len(MUTS)))
sys.exit(0 if morda == len(MUTS) else 1)
