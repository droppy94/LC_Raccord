#!/usr/bin/env python3
"""var_E3c_sensibilite.py -- audit FA-2, point E3 (c) : controle de sensibilite.
 (c1) scalaire reel de Friedrich avec terme cubique mu phi^3 (le cas exclu par le theoreme 3.1) : une singularite
      Omega^-1 proportionnelle a mu doit apparaitre et ne doit pas disparaitre a m^2 = 2 lambda/3.
 (c2) Higgs complexe (jauge, YM, xi) avec terme cubique mu |H|^3.
 (c3) terme « Majorana-like » dans That : ghat_ab M psi^T C psi = M Omega eta_ab B (B bilineaire rescale generique de poids 0
      au sens de psi_r, poids total Omega^3 x Omega^-2) : singularite Omega^-1 attendue, proportionnelle a M B.
"""
import sympy as sp, time
from fw3_fa2_lib import *

t0 = time.time()
T1, ex1, src1, c1, _ = sector("(c1) scalaire reel xi=0 + cubique mu phi^3", 0, dds_mode='friedrich', gauge=False, ym=False, real_scalar=True, cubic=True)
msp = {m: sp.sqrt(2*lam/3)}
print("  Omega^-2 nul a m^2 = 2 lambda/3 :", all(sp.simplify(v.subs(msp)) == 0 for v in c1[-2].values()))
print("  Omega^-1 nul a m^2 = 2 lambda/3 :", all(sp.simplify(v.subs(msp)) == 0 for v in c1[-1].values()))
print("  exemple Omega^-1 a m^2 = 2 lambda/3 :", sp.factor(list(c1[-1].values())[0].subs(msp)))
print("  mu present dans Omega^-1 :", any(mu in v.free_symbols for v in c1[-1].values()), "; mu present dans Omega^-2 :", any(mu in v.free_symbols for v in c1[-2].values()))

T2, ex2, src2, c2, _ = sector("(c2) Higgs complexe, jauge, YM, xi + cubique mu |H|^3", xi, dds_mode='friedrich', gauge=True, ym=True, cubic=True)
msub = {m: sp.sqrt(2*lam/3 - 4*lam*xi)}
print("  Omega^-2 nul a m^2 + 4 lambda xi = 2 lambda/3 :", all(sp.simplify(v.subs(msub)) == 0 for v in c2[-2].values()))
print("  Omega^-1 nul a m^2 + 4 lambda xi = 2 lambda/3 :", all(sp.simplify(v.subs(msub)) == 0 for v in c2[-1].values()))
print("  exemple Omega^-1 a la condition :", sp.factor(list(c2[-1].values())[0].subs(msub)))
print("  mu present dans Omega^-1 :", any(mu in v.free_symbols for v in c2[-1].values()))

T3, ex3, src3, c3, _ = sector("(c3) Higgs complexe, jauge, YM, xi + terme Majorana-like M Omega eta_ab B", xi, dds_mode='friedrich', gauge=True, ym=True, majorana_like=True)
print("  Omega^-2 nul a la condition :", all(sp.simplify(v.subs(msub)) == 0 for v in c3[-2].values()))
print("  Omega^-1 nul a la condition :", all(sp.simplify(v.subs(msub)) == 0 for v in c3[-1].values()))
print("  exemple Omega^-1 a la condition :", sp.factor(list(c3[-1].values())[0].subs(msub)))
print("  M present dans Omega^-1 :", any(MM in v.free_symbols for v in c3[-1].values()))
print(f"\n[temps total {time.time()-t0:.0f} s]")
