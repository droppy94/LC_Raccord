#!/usr/bin/env python3
"""var_E2_substitutions.py -- audit FA-2, point E2.
 (i)  Reproduction C1 et C2 avec la bibliotheque (controle que la copie parametree reproduit l'original).
 (ii) (2.15) : facteur Omega (script original) contre Omega^-1 (Friedrich (2.8), (2.15) : -(kappa/(24 Omega)) nablahat T̂).
      Les coefficients singuliers de (2.17) doivent etre identiques (le terme n'entre qu'a l'ordre >= 0).
 (iii) Reduction modulo (3.8) en eliminant n1^2 au lieu de n0^2 : les conclusions (K-6) doivent etre invariantes.
 (iv) Plus basse puissance avant reduction (verifie que W^K suffit a rendre polynomial).
 (v) Trace de S (T* est sans trace pour ghat, le script garde S_ab generique non sans trace) : verifie que
      S et Str n'apparaissent pas dans les coefficients singuliers (sinon l'omission compterait).
"""
import sympy as sp, time
import fw3_fa2_lib as F
from fw3_fa2_lib import *

t0 = time.time()
# (i) reproduction C1
T1, ex1, src1, c1, J1 = sector("(i) C1 reproduction : scalaire reel, xi=0, sans jauge", 0, gauge=False, ym=False, real_scalar=True)
p = sp.Symbol('p', real=True)
pred = {k: sp.expand(kap/3*(m**2 - 2*lam/3)*p**2*antisym(k[1], k[2], k[0])) for k in src1}
print("  Omega^-2 == (kappa/3)(m^2 - 2 lambda/3) p^2 n_[nu eta_lambda]rho :", all(sp.simplify(c1[-2].get(k, 0) - pred[k]) == 0 for k in src1))
msp = {m: sp.sqrt(2*lam/3)}
print("  Omega^-1 nul a m^2 = 2 lambda/3 :", all(sp.simplify(v.subs(msp)) == 0 for v in c1[-1].values()))

# (ii) C2 avec les deux formes de (2.15)
T2a, ex2a, src2a, c2a, _ = sector("(ii-a) C2 reproduction, (2.15) facteur Omega (original)", xi, dds_mode='orig', gauge=True, ym=True)
check_K6(c2a, ex2a, src2a, '(ii-a)')
T2b, ex2b, src2b, c2b, _ = sector("(ii-b) C2, (2.15) facteur Omega^-1 (Friedrich)", xi, dds_mode='friedrich', gauge=True, ym=True)
check_K6(c2b, ex2b, src2b, '(ii-b)')
same = all(sp.simplify(c2a[k].get(key, 0) - c2b[k].get(key, 0)) == 0 for k in (-3, -2, -1) for key in src2a)
print("  coefficients Omega^-3, Omega^-2, Omega^-1 identiques entre (ii-a) et (ii-b) :", same)
# ou le facteur de (2.15) agit-il ? comparer les coefficients d'ordre 0 et 1
diff0 = [sp.simplify(sp.expand(laurent(reduce_nn(src2a[key])).get(0, 0) - laurent(reduce_nn(src2b[key])).get(0, 0))) for key in list(src2a)[:3]]
print("  difference a l'ordre Omega^0 (3 premieres composantes) :", [d != 0 for d in diff0])
d0 = [d for d in diff0 if d != 0]
if d0: print("  exemple de difference a l'ordre 0 :", sp.factor(d0[0]))

# (iii) reduction via n1
F.NREDUCE = 1
T2c, ex2c, src2c, c2c, _ = sector("(iii) C2, reduction (3.8) via n1^2", xi, dds_mode='friedrich', gauge=True, ym=True)
check_K6(c2c, ex2c, src2c, '(iii)')
F.NREDUCE = 0

# (v) symboles S, Str dans les coefficients singuliers
syms = set()
for k in (-3, -2, -1):
    for v in c2b[k].values(): syms |= v.free_symbols
print("  (v) S_ab, dS, Str, s, L dans les coefficients singuliers :", any(str(x)[0] in 'S' or str(x).startswith(('dS', 'Str', 'L', 'dL')) or x == s for x in syms))
print(f"\n[temps total {time.time()-t0:.0f} s]")
