#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_spectre_k3.py — LC-RACCORD. Sceau de la note LC-WORK-D3-SPECTRE-K3 (Tâche 1
du pivot post-porte (ii), LC-WORK-REPRISE-POST-PORTE-II §4). Tâche 2 : NUMÉRIQUE +
SYMBOLIQUE du critère pré-enregistré §5.

Position. La porte (ii) est CLOSE (LC-D3-CROSSOVER-ATTRACTEUR v0.1, det J*=1) ; ce
front en est INDÉPENDANT. On passe de la coïncidence UN-POINT <g3>_BD = 0 (acquise,
LC-D3-WEYL-BUNCHDAVIES) au contrôle du DEUX-POINTS (le spectre).

Extension de :
    verif_D3_bunchdavies.py  — relation d'état BD  g3 = -(i/3) k^3 g0  (bloc [3], scellé).
    verif_D3_WCH_GWE.py      — noyau exact  g(x) = (x cos x - sin x)^2/(3 x^2)  (bloc [6bis]).
    verif_E_planck.py        — N = S_dS = 3π/(Λ ℓ_P^2),  √(N/π) = ℓ_dS/ℓ_P  (~10^61).

Blocs (= critère §5 de LC-WORK-D3-SPECTRE-K3) :
    [1] CHAÎNE SPECTRALE (symbolique). Re-dérive g3 = -(i/3)k^3 g0 sur le mode BD, puis
        propage un spectre invariant d'échelle : P_h = const  <=>  P_{g0} ∝ k^-3
        =>  P_{g3} = (1/9) k^6 P_{g0} ∝ k^3  =>  <TT> = (d/16πG)^2 P_{g3} ∝ k^3 = k^{2Δ-d}.
    [2] VARIANCE EXACTE (numérique — le cœur). C(x_UV) = ∫ dx/x · g(x).
        FINDING : C croît LOGARITHMIQUEMENT (enveloppe g->cos^2 x/3, moyenne 1/6),
        PAS en (x_UV)^4. Ajustement  C ≈ α ln x_UV + β  : assert |α - 1/6| < 1e-2.
        Contrôles : max g = 0.3767 à x≈2.744 ; petit x : g -> x^4/27 ; enveloppe -> 1/6.
    [3] CONTRASTE leading/exact. Reproduit la table §3.1 : le leading (x_UV)^4/108 DIVERGE
        tandis que C(x_UV) reste O(ln). Scelle que la divergence quartique du §8 de
        LC-D3-WCH-GWE est un ARTEFACT de troncature (cohérent audit C5).
    [4] CIBLE PHYSIQUE. x_UV = √(N/π) = ℓ_dS/ℓ_P (cellules d'horizon, LC-E) ; assert
        C(x_UV) ≈ 23 ± 1. Circularité N <-> ℓ_P REPORTÉE (commentaire, non assert).

Cibles (LC-WORK-D3-SPECTRE-K3, papier ; ce sceau doit les reproduire) :
    propagation         P_{g3} ∝ k^3   (= k^{2Δ-d}, Δ=d=3)
    pente log           α = 1/6,  β ≈ 0.045
    max noyau           g_max = 0.3767  à  x ≈ 2.744
    intercept asympt.   β∞ ≈ 0.04503
    cutoff Planck/N     x_UV = √(N/π) ≈ 1.0e61
    variance attendue   C(x_UV) = (1/6)ln√(N/π) + β∞ ≈ 23.5  (<< 0.5 si A_T << 1 : (A))

Dépendances : sympy, numpy, scipy. Re-exécutable, sans réseau.
Discipline (LC-AUDIT-VERDICT §6.4) : un `établi` de sceau = « l'algèbre/le numérique
sont corrects ET les cibles reproduites » ; JAMAIS « la physique de la CCC est établie ».
Ici restent décision ouverte / à inventer : la normalisation A_T ~ (H/M_P)^2 et la
fixation de N (circularité LC-E, non brisée).
"""

import sympy as sp
import numpy as np
from scipy import integrate


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


print("=" * 72)
print(" verif_D3_spectre_k3.py — la 2-points <g3 g3> ~ k^3 et le rôle de N")
print("=" * 72)

# ======================================================================
# [1] CHAÎNE SPECTRALE (symbolique) : P_h=const <=> P_{g0}∝k^-3 => P_{g3}∝k^3 => <TT>∝k^3
# ======================================================================
banner("[1] CHAÎNE SPECTRALE  —  P_h=const <=> P_{g0}∝k^-3 => P_{g3}∝k^3 => <TT>∝k^3")

eta, k, A, H, G_N = sp.symbols('eta k A H G_N', positive=True)
I = sp.I

# (a) Re-dérivation de la relation d'état BD g3 = -(i/3) k^3 g0 (autoportant, cf. parent).
f = A * (1 + I * k * eta) * sp.exp(-I * k * eta)               # mode de Bunch-Davies
EOM = sp.simplify(sp.diff(f, eta, 2) - (2 / eta) * sp.diff(f, eta) + k**2 * f)
assert EOM == 0                                                # BD solution de l'EOM TT de dS
ser = sp.expand(sp.series(f, eta, 0, 5).removeO())             # expansion FG près de I+
g0 = ser.coeff(eta, 0)                                         # source
g2 = ser.coeff(eta, 2)                                         # local (Schouten)
g3 = ser.coeff(eta, 3)                                         # donnée radiative libre
assert ser.coeff(eta, 1) == 0                                  # pas de eta^1 (d=3 impair)
rel = sp.simplify(g3 - (-(I * sp.Rational(1, 3)) * k**3 * g0))
assert rel == 0
print("  (a) mode BD -> FG :  g0 =", g0, " ; g2 =", g2, " ; g3 =", g3)
print("      relation d'état (par polarisation) :  g3 = -(i/3) k^3 g0   [vérif =", rel, "]")

# (b) Propagation du spectre. On POSE l'invariance d'échelle du strain :
#     P_h = (k^3/2π^2) <|g0|^2> = const  <=>  P_{g0}(k) ∝ k^-3.
#     Puis P_{g3} = |g3/g0|^2 P_{g0} = (1/9) k^6 · P_{g0}.
C0 = sp.symbols('C0', positive=True)                           # amplitude (∝ A_T), libre
P_g0 = C0 * k**(-3)                                            # P_{g0} ∝ k^-3 (P_h=const)
fac = sp.simplify(sp.Abs(g3 / g0)**2)                          # = (1/9) k^6
P_g3 = sp.simplify(fac * P_g0)                                 # P_{g3}
print("\n  (b) |g3/g0|^2 =", fac, "  (= (1/9) k^6)")
print("      P_{g0} ∝ k^-3  (P_h=const)  =>  P_{g3} =", P_g3)
# Exposant de P en k = dérivée logarithmique  k·d(ln P)/dk  (insensible aux constantes).
expo = sp.simplify(k * sp.diff(sp.log(P_g3), k))
print("      exposant de P_{g3} en k  (k·dlnP/dk) :", expo, "  -> P_{g3} ∝ k^3  [CIBLE]")
assert sp.simplify(expo - 3) == 0

# (c) Dictionnaire holographique <T> = (d/16πG) g3  =>  <TT> = (d/16πG)^2 P_{g3} ∝ k^3.
d, Delta = 3, 3
coef = (sp.Rational(d, 1) / (16 * sp.pi * G_N))**2
P_TT = sp.simplify(coef * P_g3)
expo_TT = sp.simplify(k * sp.diff(sp.log(P_TT), k))
print("\n  (c) <T_ij>=(d/16πG) g3  =>  <TT> = (d/16πG)^2 P_{g3} ∝ k^", expo_TT,
      "  (Δ=d=3 ; k^{2Δ-d}=k^", 2 * Delta - d, ")")
assert sp.simplify(expo_TT - 3) == 0 and (2 * Delta - d) == 3
print("\n  >>> CHAÎNE : P_h=const  <=>  P_{g0}∝k^-3  <=>  P_{g3}∝k^3  <=>  <TT>∝k^3.")
print("      Le k^3 de g3 = l'invariance d'échelle vue côté donnée radiative (Δ=3).")

# ======================================================================
# [2] VARIANCE EXACTE (numérique) : C(x_UV)=∫dx/x g(x) croît en (1/6) ln x_UV  [le cœur]
# ======================================================================
banner("[2] VARIANCE EXACTE  —  C(x_UV) = ∫ dx/x g(x) ~ (1/6) ln x_UV  (PAS quartique)")


def g_kernel(x):
    """Noyau exact par mode (LC-D3-WCH-GWE [6bis]) : Omega_sigma/eps^2."""
    return (x * np.cos(x) - np.sin(x))**2 / (3.0 * x**2)


# (a) Contrôles du noyau : max, petit-x (-> leading x^4/27), enveloppe (-> 1/6).
xs = np.linspace(1e-4, 30, 400000)
gx = g_kernel(xs)
g_max, x_at_max = gx.max(), xs[gx.argmax()]
print("  (a) max g(x) = %.4f  à x = %.4f   (cible 0.3767 à 2.744)" % (g_max, x_at_max))
assert abs(g_max - 0.3767) < 1e-3 and abs(x_at_max - 2.744) < 5e-3
for xv in (1e-2, 1e-1):
    lead = xv**4 / 27
    print("      petit x=%g :  g=%.6e   leading x^4/27=%.6e   (ratio %.4f)"
          % (xv, g_kernel(xv), lead, g_kernel(xv) / lead))
    assert abs(g_kernel(xv) / lead - 1) < 5e-2
env = integrate.quad(g_kernel, 50, 150, limit=500)[0] / 100.0
print("      enveloppe <g>_[50,150] = %.4f   (cible 1/6 = 0.1667)" % env)
assert abs(env - 1.0 / 6.0) < 5e-3


def C_quad(xUV, xIR=1e-8):
    """Variance réduite par QUADRATURE directe C(x_UV) = ∫ dx/x g(x). Fiable seulement
    pour x_UV modéré (au-delà, ~x_UV/2π oscillations : quad décroche)."""
    val, _ = integrate.quad(lambda u: g_kernel(np.exp(u)),
                            np.log(xIR), np.log(xUV), limit=4000)
    return val


# (b) Ajustement log sur la PLAGE FIABLE (x_UV ≤ 1e4) : C ≈ α ln x_UV + β.
xUV_fit = np.array([1e1, 1e2, 1e3, 1e4])
C_fit = np.array([C_quad(x) for x in xUV_fit])
alpha, beta = np.polyfit(np.log(xUV_fit), C_fit, 1)
print("\n  (b) ajustement (plage fiable x_UV≤1e4)  C ≈ α ln x_UV + β :")
print("      α = %.5f   (cible 1/6 = %.5f)   |α-1/6| = %.2e" % (alpha, 1 / 6, abs(alpha - 1 / 6)))
assert abs(alpha - 1.0 / 6.0) < 1e-2
print("\n  >>> La variance est LOG-divergente (pente 1/6), non quartique.")

# (c) Intercept ASYMPTOTIQUE β∞ = lim[C(X) - (1/6)ln X], calcul ROBUSTE (sans quad géant).
#     Décomposition d'enveloppe : g(x) = cos^2 x/3 - sin(2x)/(3x) + sin^2 x/(3x^2),
#     enveloppe -> 1/6 (moyenne). Donc
#       β∞ = ∫_0^1 g/x dx + ∫_1^∞ (g-1/6)/x dx
#     (la queue oscillatoire ∫ cos(2x)/(6x) dx ~ -Ci(2x) décroît en 1/x : tronquer à 2000
#      est exact à ~1e-4). Insensible à l'IR (g~x^4/27 -> g/x intégrable en 0).
b_lo, _ = integrate.quad(lambda x: g_kernel(x) / x, 1e-8, 1.0, limit=400)
b_hi, _ = integrate.quad(lambda x: (g_kernel(x) - 1.0 / 6.0) / x, 1.0, 2000, limit=4000)
beta_inf = b_lo + b_hi
print("  (c) intercept asymptotique  β∞ = %.5f   (cible ≈ 0.045)" % beta_inf)
assert abs(beta_inf - 0.045) < 5e-3


def C_law(xUV):
    """Loi asymptotique (le résultat) : C(x_UV) = (1/6) ln x_UV + β∞. Valable ∀ x_UV
    (vérifiée contre C_quad sur la plage fiable au bloc [3]) ; SEULE voie pour x_UV géant."""
    return np.log(xUV) / 6.0 + beta_inf

# ======================================================================
# [3] CONTRASTE leading/exact : la loi log VALIDÉE vs l'artefact (x_UV)^4/108  [table §3.1]
# ======================================================================
banner("[3] CONTRASTE leading/exact  —  loi log validée vs artefact (x_UV)^4")
# (a) la loi C_law reproduit la quadrature sur la plage fiable (diff < 1e-2).
print("  validation de la loi sur la plage fiable :")
print("  %-8s | %-12s | %-12s | %-9s" % ("x_UV", "C_quad", "C_law", "diff"))
for xUV in (1e1, 1e2, 1e3, 1e4):
    cq, cl = C_quad(xUV), C_law(xUV)
    print("  %-8.0e | %-12.4f | %-12.4f | %-9.4f" % (xUV, cq, cl, cq - cl))
    assert abs(cq - cl) < 1e-2
# (b) extrapolation + contraste avec le leading (divergent).
print("\n  extrapolation (loi) + contraste leading :")
print("  %-8s | %-12s | %-14s" % ("x_UV", "C_law (exact)", "leading x^4/108"))
print("  " + "-" * 42)
for xUV in (1e6, 1e20, 1e40, 1e60):
    print("  %-8.0e | %-12.4f | %-14.3e" % (xUV, C_law(xUV), xUV**4 / 108))
assert (1e60)**4 / 108 > 1e200 and C_law(1e60) < 30   # leading -> ∞ ; loi reste O(ln) ~ 23
print("\n  >>> leading (x_UV)^4/108 -> ∞ (artefact, audit C5) ; C exact ~ (1/6)ln x_UV.")

# ======================================================================
# [4] CIBLE PHYSIQUE : x_UV = √(N/π) = ℓ_dS/ℓ_P  =>  C ≈ 23  [cutoff holographique]
# ======================================================================
banner("[4] CIBLE PHYSIQUE  —  cutoff N : x_UV = √(N/π) = ℓ_dS/ℓ_P  =>  C ≈ 23")

# Constantes (identiques à verif_E_planck.py).
c_l, hbar, G = 2.998e8, 1.055e-34, 6.674e-11
lP = np.sqrt(hbar * G / c_l**3)
Lam = 1.1e-52
ldS = np.sqrt(3 / Lam)
N = 3 * np.pi / (Lam * lP**2)                     # N = S_dS (entropie/aire d'horizon)
xUV_planck = np.sqrt(N / np.pi)                   # = ℓ_dS/ℓ_P (cellules d'horizon)
print("  ℓ_P = %.3e m ; ℓ_dS = %.3e m ; N = S_dS = %.3e (~10^122)" % (lP, ldS, N))
print("  √(N/π) = %.3e   ;   ℓ_dS/ℓ_P = %.3e   (doivent coïncider)" % (xUV_planck, ldS / lP))
assert abs(xUV_planck / (ldS / lP) - 1) < 1e-6    # √(N/π) == ℓ_dS/ℓ_P

C_planck = C_law(xUV_planck)                       # via la LOI (quad direct non fiable à 1e61)
print("\n  Omega_sigma^tot / A_T = C(√(N/π)) = (1/6)ln(√(N/π)) + β∞ = %.3f   (cible ≈ 23)" % C_planck)
print("  vs leading (√(N/π))^4/108 = %.3e   (ARTEFACT divergent)" % (xUV_planck**4 / 108))
assert 23.0 < C_planck < 24.0

print("\n  CIRCULARITÉ (reportée, non scellée — LC-E §3) : N = S_dS = (ℓ_dS/ℓ_P)^2")
print("  présuppose ℓ_P. La part non établie du spectre est isolée dans :")
print("    - l'amplitude  A_T ~ (H/M_P)^2   [décision ouverte]")
print("    - la coupure   x_UV = √(N/π)     [log-douce ; fixation de N : à inventer]")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-" * 72)
print(" VERDICT (établi : algèbre + numérique ; cibles reproduites) :")
print("   [1] CHAÎNE      : P_h=const <=> P_{g0}∝k^-3 <=> P_{g3}∝k^3 <=> <TT>∝k^3 (Δ=3).")
print("   [2] VARIANCE    : C(x_UV) ~ (1/6) ln x_UV + 0.045   (LOG, pas quartique).")
print("   [3] CONTRASTE   : la divergence (x_UV)^4 du §8 WCH-GWE est un ARTEFACT (C5).")
print("   [4] CUTOFF N    : C(√(N/π)) ≈ 23.5  =>  Omega_sigma^tot ≈ 23.5 A_T << 0.5 si A_T<<1.")
print("   ==> SPECTRE k^3 CONTRÔLÉ, conditionnel à A_T<<1 (H sous-Planckien) et au cadre CCC.")
print("   Décision ouverte / à inventer : normalisation A_T ; fixation de N (circularité LC-E).")
print("   Discipline §6.4 : 'spectre contrôlé cond. A_T<<1' != 'spectre dérivé'.")
print("-" * 72)
print("\nTOUS LES ASSERT PASSENT.")
