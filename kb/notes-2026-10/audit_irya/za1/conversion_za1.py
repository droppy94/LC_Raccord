# Conversion ZA-1 : coefficients du ln a de arXiv:2501.01972 en unites n * b * kappa_P^2 * H^2
import sympy as sp
pi = sp.pi
G, H, kP = sp.symbols('G H kappa_P', positive=True)
NS, NF, NV = sp.symbols('N_S N_F N_V', nonnegative=True)

# Convention de la source : kappa^2 = 16 pi G  (eq. 2). Convention de l'audit : kappa_P^2 = 8 pi G.
kappa2_source = 16*pi*G
kappaP2 = 8*pi*G
ratio = sp.simplify(kappa2_source/kappaP2)   # = 2
print("kappa^2 / kappa_P^2 =", ratio)

# Coefficient b du carre de Weyl dans la trace anomale
b = (NS + 6*NF + 12*NV)/(120*(4*pi)**2)

# Coefficients du ln a de la source (coefficient de kappa^2 H^2), eq. (35), (46) et ratio Dirac = 1/2 EM (p. 6), MCC = 1/12 EM (p. 8)
coef_dirac_src  = sp.Rational(1, 80)/pi**2          # eq. (35)
coef_scalar_src = sp.Rational(1, 480)/pi**2         # eq. (46)
coef_photon_src = 2*coef_dirac_src                  # derive : Dirac = 1/2 EM  (coherent avec MCC = 1/12 EM : 12*coef_scalar)
assert sp.simplify(12*coef_scalar_src - coef_photon_src) == 0

results = {}
for name, coef, subs in [("Dirac", coef_dirac_src, {NS:0, NF:1, NV:0}),
                         ("scalaire conf.", coef_scalar_src, {NS:1, NF:0, NV:0}),
                         ("photon (derive)", coef_photon_src, {NS:0, NF:0, NV:1})]:
    # coef_source * kappa^2 H^2 = coef_source * 2 * kappa_P^2 H^2 = n * b * kappa_P^2 H^2
    coef_in_kP = coef*ratio
    n = sp.simplify(coef_in_kP / b.subs(subs))
    results[name] = (sp.simplify(coef_in_kP), n)
    print(f"{name:18s}: coefficient de kappa_P^2 H^2 = {sp.simplify(coef_in_kP)} ; b = {sp.simplify(b.subs(subs))} ; n = {n}")

ns = {v[1] for v in results.values()}
print("Tous les n egaux :", len(ns) == 1, "; n =", ns)
