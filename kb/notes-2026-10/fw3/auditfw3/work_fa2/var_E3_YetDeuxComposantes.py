#!/usr/bin/env python3
"""var_E3_YetDeuxComposantes.py -- audit FA-2, point E3 (a), (b) et critere K-6.
 (a) tenseur generique regulier Omega^2 Y_ab ajoute a That (Y symetrique, fonction generique des jets, derivees dY generiques)
 (b) seconde composante complexe H_2 = (p2 + i q2)/sqrt 2, meme champ de jauge, quartique lambda_h (|H_1|^2 + |H_2|^2)^2
 Les deux ensemble (K-6), avec (2.15) sous la forme de Friedrich (facteur Omega^-1).
"""
import sympy as sp, time
from fw3_fa2_lib import *

t0 = time.time()
Ta, exa, srca, ca, _ = sector("(a) C2 + Omega^2 Y_ab generique, une composante", xi, dds_mode='friedrich', gauge=True, ym=True, add_Y=True)
check_K6(ca, exa, srca, '(a)')
print(f"[{time.time()-t0:.0f} s]")
Tb, exb, srcb, cb, _ = sector("(b) C2 + Omega^2 Y_ab + deux composantes complexes (K-6)", xi, dds_mode='friedrich', gauge=True, ym=True, add_Y=True, n_comp=2)
okb = check_K6(cb, exb, srcb, '(b)')
print("  exemple de coefficient Omega^-2 :", sp.factor(list(cb[-2].values())[0]))
print("  exemple de coefficient Omega^-1 :", sp.factor(list(cb[-1].values())[0]))
print("  K-6 satisfait :", okb)
print(f"\n[temps total {time.time()-t0:.0f} s]")
