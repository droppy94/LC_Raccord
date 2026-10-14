"""irv_conversion.py -- IR-v (NOTE-135). Exposants resommes de Woodard (arXiv:2501.05077, eq. 148, 151, 154), kW^2 = 16 pi G, H = 1,
compares a 8 b kappa (kappa = 8 pi G, b = (N_S + 6 N_F + 12 N_V)/(120 (4 pi)^2)), regle de conversion figee NOTE-134 §1.
W_E ∝ a^p  <=>  W_E ∝ Omega^(-p)  (Omega ∝ 1/a)."""
import sympy as sp
G = sp.symbols('G', positive=True); pi = sp.pi; kW2 = 16*pi*G
woodard = {'scalaire MCC': (kW2/(480*pi**2), (1, 0, 0)), 'fermion de Dirac': (kW2/(80*pi**2), (0, 1, 0)), 'photon': (kW2/(40*pi**2), (0, 0, 1))}
for nom, (p, (NS, NF, NV)) in woodard.items():
    b = sp.Rational(NS + 6*NF + 12*NV, 120)/(4*pi)**2
    g = sp.simplify(8*b*8*pi*G)
    print(f"{nom:18s} exposant Woodard (a^p) : {sp.simplify(p)} ; 8 b kappa : {g} ; rapport : {sp.simplify(p/g)} ; d'ou W_E ∝ Omega^(-{g})")
print("EXIT 0")
