#!/usr/bin/env python3
"""
hx_check.py -- NOTE-186 (chantier HX). H = 1. s = Omega = -eta.
(1) homogeneous Higgs near the symmetric point on dS: h = s^alpha, alpha(alpha - 3) + M2 = 0,
    M2 = m_h^2 + 12 xi (effective mass with non-minimal coupling); alpha = 3/2 -+ mu.
(2) classification of m_f = y h against Prop. 4 of the article (generic data, c1 != 0):
    (a) int m dt < inf  <=>  Re(alpha_min) > 0
    (b) m a bounded      <=>  Re(alpha_min) >= 1
    (c) m/Omega smooth   <=>  alpha_min - 1 and alpha_max - 1 are non-negative integers (no log)
(3) conformal weights: Yukawa sqrt(-g) y H psibar psi and gauge mass sqrt(-g) g^{mn} |H|^2 A_m A_n
    are invariant under ghat = Omega^-2 g, H = Omega Hr, psi = Omega^{3/2} psir, A weight 0.
"""
import sympy as sp

s, al, M2 = sp.symbols('s alpha M2')
h = s**al
# KG on dS, homogeneous, in s = -eta (H = 1): h'' - (2/s) h' + M2 h / s^2 = 0  (conformal time, a = 1/s)
kg = sp.simplify((sp.diff(h, s, 2) - 2/s*sp.diff(h, s) + M2*h/s**2)/s**(al - 2))
print("(1) indicial equation:", sp.factor(kg), "=0  ->  alpha =", sp.solve(kg, al))

def classify(m2):
    m2 = sp.nsimplify(m2)
    roots = sp.solve(al*(al - 3) + m2, al)
    roots = sorted(roots, key=lambda r: sp.re(r))
    if len(roots) == 1:                       # double root: log branch
        roots = [roots[0], roots[0]]; log = True
    else:
        log = roots[0] == roots[1]
    amin, amax = roots[0], roots[-1]
    a = sp.re(amin) > 0
    b = sp.re(amin) >= 1
    def nonneg_int(z): return z.is_integer and z >= 0
    c = (not log) and all(sp.im(r) == 0 and nonneg_int(sp.nsimplify(r - 1)) for r in (amin, amax))
    return amin, amax, bool(a), bool(b), bool(c), log

print("\n(2) classification (M2 = m_h^2 + 12 xi, in units of H^2), generic data c1 != 0")
print("   M2      alpha_min          alpha_max          (a)    (b)    (c)")
for m2 in [-1, 0, sp.Rational(1, 2), 1, sp.Rational(3, 2), sp.Rational(19, 10), 2, sp.Rational(21, 10), sp.Rational(9, 4), 3, 10]:
    amin, amax, a, b, c, log = classify(m2)
    print(f"   {str(m2):6s}  {str(sp.nsimplify(amin)):17s}  {str(sp.nsimplify(amax)):17s}  {str(a):5s}  {str(b):5s}  {str(c):5s}" + ("  (double root, log)" if log else ""))
# thresholds
print("   thresholds: (a) Re(3/2 - mu) > 0 <=> M2 > 0 ;  (b) Re(3/2 - mu) >= 1 <=> mu <= 1/2 or complex <=> M2 >= 2 ;"
      " (c) only M2 = 2 (alpha = 1, 2)")
print("   conformal coupling xi = 1/6, m_h = 0  ->  M2 =", 12*sp.Rational(1, 6))

# (3) conformal weights
Om = sp.symbols('Omega', positive=True)
w_sqrtg = -4      # sqrt(-ghat) = Omega^-4 sqrt(-g)
w_ginv = 2        # ghat^{mn} = Omega^2 g^{mn}
yuk = w_sqrtg + 1 + 3          # H -> Omega Hr ; psibar psi -> Omega^3
gauge = w_sqrtg + w_ginv + 2   # |H|^2 -> Omega^2 ; A weight 0
higgs_mass = w_sqrtg + 2       # m^2 |H|^2 -> Omega^-2 : not invariant (the Friedrich term)
print("\n(3) Omega-weight of sqrt(-g) y H psibar psi :", yuk, " (0 = conformally invariant)")
print("    Omega-weight of sqrt(-g) g^{mn} |H|^2 A_m A_n :", gauge)
print("    Omega-weight of sqrt(-g) m^2 |H|^2 :", higgs_mass, " (-> Omega^-2 m^2 |Hr|^2 : Friedrich's singular term, cancelled by R/6 at m^2 = 2 lambda/3)")
print("    rescaled Dirac mass coefficient: y Hr = y h / Omega = m_f / Omega")
