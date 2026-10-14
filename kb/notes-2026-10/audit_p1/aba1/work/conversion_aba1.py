# -*- coding: utf-8 -*-
# Conversion [calcule] ABA-1 : sympy
# Conventions : kappa^2 = 16 pi G (S8 eq. 12, S27 sec. 3) ; kappa_P^2 = 8 pi G ;
# b = (N_S + 6 N_F + 12 N_V) / (120 (4 pi)^2).
import sympy as sp

G, H, mu, D = sp.symbols('G H mu D', positive=True)
NS, NF, NV = sp.symbols('N_S N_F N_V', nonnegative=True)
pi = sp.pi

kappa2 = 16*pi*G          # convention de S8 et S27
kappaP2 = 8*pi*G          # convention demandee
b = (NS + 6*NF + 12*NV) / (120*(4*pi)**2)

print("=== 1. Coefficient du ln a de S8 pour le photon (eq. 53), forme n b kappa_P^2 H^2 ===")
coef_S8 = kappa2*H**2/(40*pi**2)             # S8 eq. (53)
coef_S8_hbar = 2*G*H**2/(5*pi)               # S8 eq. (60), hbar = c = 1
assert sp.simplify(coef_S8 - coef_S8_hbar) == 0
print("coef (eq.53) = kappa^2 H^2/(40 pi^2) =", sp.simplify(coef_S8), " ; egal a (eq.60) 2 G H^2/(5 pi) :", sp.simplify(coef_S8 - coef_S8_hbar) == 0)
b_photon = b.subs({NS: 0, NF: 0, NV: 1})
print("b(photon, N_V=1) =", sp.simplify(b_photon))
n = sp.simplify(coef_S8 / (b_photon*kappaP2*H**2))
print("n =", n)

print()
print("=== 2. gamma de S8 a partir de c_2 (eq. 56), c_1 = 0, deltaZ (eq. 57) ===")
c1_S8 = 0
c2_S8 = mu**(D-4)/(D-4) * sp.gamma(D/2)/(2**8*pi**(D/2)) * (D-2)*D/((D+1)*(D-3)**2)
dZ_S8 = D*(2*(D-1)*c1_S8 - c2_S8)*kappa2*H**2
# gamma = d ln(1+dZ)/d ln(mu^2) = (1/2) d dZ/d ln mu + O(kappa^4) ; d mu^{D-4}/d ln mu = (D-4) mu^{D-4}
ddZ_dlnmu_S8 = sp.diff(dZ_S8, mu)*mu
gamma_S8 = sp.limit(sp.simplify(ddZ_dlnmu_S8/2), D, 4)
gamma_S8 = sp.simplify(gamma_S8)
print("gamma_S8 (calcule) =", gamma_S8)
gamma_S8_affiche = -kappa2*H**2/(80*pi**2)
print("gamma_S8 (affiche, eq. 58) = -kappa^2 H^2/(80 pi^2) =", sp.simplify(gamma_S8_affiche))
print("accord :", sp.simplify(gamma_S8 - gamma_S8_affiche) == 0)
expo_S8 = sp.simplify(-2*gamma_S8)
print("-2 gamma_S8 =", expo_S8, " ; exposant resomme eq. (60) = 2 G H^2/(5 pi) :", sp.simplify(expo_S8 - coef_S8_hbar) == 0)
print("Verification : coefficient du ln a en (53) = -2 gamma :", sp.simplify(coef_S8 - expo_S8) == 0)

print()
print("=== 3. gamma de S27 a partir de c_1, c_2 (eq. 85-86), deltaZ (eq. 91) ===")
pref = mu**(D-4)*sp.gamma(D/2)/(2**8*pi**(D/2))
c1_S27 = pref*(D-2)/((D-1)**2*(D-3)*(D-4))
c2_S27 = pref*2/((D+1)*(D-1)*(D-3)**2*(D-4))
dZ_S27 = D*(2*(D-1)*c1_S27 - c2_S27)*kappa2*H**2
ddZ_dlnmu_S27 = sp.diff(dZ_S27, mu)*mu
gamma_S27 = sp.simplify(sp.limit(sp.simplify(ddZ_dlnmu_S27/2), D, 4))
print("gamma_S27 (calcule) =", gamma_S27)
gamma_S27_affiche = 3*G*H**2/(20*pi)
print("gamma_S27 (affiche, eq. 91) = 3 G H^2/(20 pi)")
print("accord :", sp.simplify(gamma_S27 - gamma_S27_affiche) == 0)
print("-2 gamma_S27 =", sp.simplify(-2*gamma_S27), " ; exposant eq. (93) = -3 G H^2/(10 pi) :", sp.simplify(-2*gamma_S27 + 3*G*H**2/(10*pi)) == 0)
# Contributions separees c_1 et c_2 (pour tracabilite)
g_c1 = sp.simplify(sp.limit(sp.simplify(sp.diff(D*2*(D-1)*c1_S27*kappa2*H**2, mu)*mu/2), D, 4))
g_c2 = sp.simplify(sp.limit(sp.simplify(sp.diff(-D*c2_S27*kappa2*H**2, mu)*mu/2), D, 4))
print("part c_1 :", g_c1, " ; part c_2 :", g_c2, " ; somme :", sp.simplify(g_c1+g_c2))

print()
print("=== 4. Coefficient scalaire MMC de S27 en forme n b kappa_P^2 H^2 (complement) ===")
coef_S27 = 3*G*H**2/(10*pi)
b_scalar = b.subs({NS: 1, NF: 0, NV: 0})
n_scalar = sp.simplify(coef_S27/(b_scalar*kappaP2*H**2))
print("b(scalaire, N_S=1) =", sp.simplify(b_scalar), " ; |coef (eq.80)| = 3 G H^2/(10 pi) = n b kappa_P^2 H^2 avec n =", n_scalar, " (signe : negatif en (80))")
