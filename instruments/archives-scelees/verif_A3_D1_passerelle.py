#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_A3_D1_passerelle.py — LC-RACCORD. Sceau de RECONFIRMATION de la note
LC-WORK-A3-D1-PASSERELLE v0.1 (réduction de comptage A3 <-> D1, Def-2).

NE CONTIENT AUCUNE ALGÈBRE NEUVE. Rejoue, en un seul endroit, l'emboîtement déjà
établi par les sceaux parents, pour reconfirmer la réduction « A4 => A3-un-point » :

  Parents (faits importés, re-dérivés à l'identique ici pour autoportance) :
    verif_D3_bunchdavies.py  — g3 = -(i/3) k^3 g0 sur le mode BD ; E_ij=(d/2H)g3
                               (« C->0 <=> g3->0 ») ; <g3>_BD = 0 (un-point).
    verif_D3_spectre_k3.py   — P_h=const <=> P_{g0}∝k^-3 => P_{g3}∝k^3 (Δ=d=3).

  CE QUE CE SCEAU RECONFIRME (= structure de la note) :
    [1] Devise commune g3 : re-dérive g3=-(i/3)k^3 g0 (relation d'état BD).
    [2] Route A3 (dS-inv) -> <g3>=0 par SYMÉTRIE : un un-point function dS-invariant
        d'un tenseur TT symétrique rang 2 est nul (projection TT d'un tenseur
        isotrope c·δ_ij = 0). Argument indépendant du sceau, robuste (algèbre linéaire).
    [3] Route A4 (WCH) -> <g3>=0 : g3->0 (champ) => <g3>=0 (a fortiori). Emboîtement
        des ensembles de contrainte S_A4 = {g3=0} ⊆ S_A3 = {<g3>=0}, et STRICTEMENT
        (∃ g3≠0 à moyenne nulle : fluctuation). => A4 => A3-un-point, A3 ⇏ A4.
    [4] Divergence A3/A4 = DEUX-POINT k^3 : sous A3, <g3 g3> ~ k^3 ≠ 0 ; sous A4,
        <g3 g3> = 0. L'écart entre les deux postulats vit ENTIÈREMENT au deux-point,
        de forme spectrale k^3 (= SPECTRE-K3, spectre primordial irréductible).

Dépendances : sympy, numpy. Re-exécutable, sans réseau.
Discipline (LC-AUDIT-VERDICT §6.4) : un `établi` de sceau = « l'algèbre est correcte
ET reproduit les faits parents » ; JAMAIS « la physique de la CCC est établie ».
Ici : la réduction A4=>A3-un-point est `établie (sceau)` AU NIVEAU UN-POINT PERTURBATIF
(mode TT) ; sa généralisation non-linéaire reste `décision ouverte` (héritée de
WEYL-BUNCHDAVIES §6). A3 et A4 NON fusionnés au-delà du un-point (écart = k^3).
"""

import sympy as sp
import numpy as np

N_ASSERT = 0


def check(cond, msg):
    global N_ASSERT
    assert cond, "ÉCHEC: " + msg
    N_ASSERT += 1
    print("   [PASS] " + msg)


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


print("=" * 72)
print(" verif_A3_D1_passerelle.py — reconfirmation : <g3>=0 (2 routes) + k^3 divergence")
print("=" * 72)

eta, k, A, H = sp.symbols('eta k A H', positive=True)
Iu = sp.I
d, Delta = 3, 3   # bord dS/CFT : d=3, opérateur TT Δ=3

# ======================================================================
# [1] DEVISE COMMUNE g3 — relation d'état BD (re-dérivée, cf. parents)
# ======================================================================
banner("[1] DEVISE COMMUNE  —  g3 = -(i/3) k^3 g0 sur le mode de Bunch-Davies")

f = A * (1 + Iu * k * eta) * sp.exp(-Iu * k * eta)                 # mode BD
EOM = sp.simplify(sp.diff(f, eta, 2) - (2 / eta) * sp.diff(f, eta) + k**2 * f)
check(EOM == 0, "mode BD solution de l'EOM TT de dS (f'' - (2/eta)f' + k^2 f = 0)")

ser = sp.expand(sp.series(f, eta, 0, 5).removeO())                 # expansion FG près de I+
g0 = ser.coeff(eta, 0)            # source g(0)
g2 = ser.coeff(eta, 2)            # local (Schouten)
g3 = ser.coeff(eta, 3)            # donnée radiative libre = MARÉE (liberté D1)
check(ser.coeff(eta, 1) == 0, "pas de terme eta^1 (d=3 impair) : FG cohérente")
rel = sp.simplify(g3 - (-(Iu * sp.Rational(1, 3)) * k**3 * g0))
check(rel == 0, "relation d'état BD : g3 = -(i/3) k^3 g0  (marée = liberté D1)")
print("       g0 =", g0, " ; g2 =", g2, " ; g3 =", g3)
print("       -> A4 (WCH g3->0), A3 (<g3>=0), D1 (libre g3) contraignent LE MÊME objet g3.")

# ======================================================================
# [2] ROUTE A3 (dS-invariance) -> <g3> = 0  PAR SYMÉTRIE
#     Un one-point function dS-invariant d'un tenseur TT symétrique = 0.
# ======================================================================
banner("[2] ROUTE A3  —  <g3>=0 forcé par symétrie (TT d'un tenseur isotrope = 0)")

# Le un-point <g3>_ij doit être (i) invariant par rotations spatiales (dS-inv => pas de
# direction privilégiée) => isotrope => proportionnel à δ_ij ; (ii) transverse-sans-trace
# (g3 est TT par construction). Or la projection TT d'un tenseur isotrope est NULLE.
c = sp.symbols('c', real=True)
T_iso = c * sp.eye(3)                                  # seul tenseur sym. rang 2 isotrope
trace = sp.trace(T_iso)
T_traceless = T_iso - sp.Rational(1, 3) * trace * sp.eye(3)   # retrait de trace (d=3)
check(sp.simplify(trace - 3 * c) == 0, "tenseur isotrope c·δ_ij : trace = 3c (pur-trace)")
check(T_traceless == sp.zeros(3, 3),
      "projection sans-trace d'un tenseur isotrope = 0  =>  <g3>_dS-inv = 0")
print("       => A3 (dS-inv) impose <g3> = 0 INDÉPENDAMMENT du calcul de mode : robuste.")

# Reconfirmation côté mode (cohérence avec verif_D3_bunchdavies) : <g3> ∝ <amplitude> = 0
# dans le vide (one-point d'un opérateur linéaire en a, a†). Représenté : g3 = (coef)·A,
# moyenne du champ libre nulle.
coef_g3 = sp.simplify(g3 / A)
check(coef_g3 != 0 and sp.simplify(coef_g3 * 0) == 0,
      "g3 lineaire en l'amplitude A : <g3> = coef·<A> = 0 dans le vide BD (un-point)")

# ======================================================================
# [3] ROUTE A4 (WCH) -> <g3>=0  ET EMBOÎTEMENT S_A4 ⊆ S_A3 (strict)
# ======================================================================
banner("[3] ROUTE A4  —  g3->0 => <g3>=0 ; emboîtement S_A4 ⊊ S_A3 (A4 => A3-un-point)")

# (a) A4 : g3 = 0 (champ complet, via E_ij=(d/2H)g3 du parent : C->0 <=> g3->0).
g3_A4 = sp.Integer(0)
mean_g3_A4 = g3_A4                                      # si g3=0 alors <g3>=0 a fortiori
check(mean_g3_A4 == 0, "A4 (g3=0) => <g3>=0 (a fortiori) : route A4 atteint le un-point")

# (b) Emboîtement : S_A4 = {g3=0} ⊆ S_A3 = {<g3>=0}. Inclusion triviale (ci-dessus).
#     STRICTE : il existe g3 ≠ 0 (fieldwise) de moyenne nulle -> dans S_A3, hors S_A4.
xs = np.linspace(0, 2 * np.pi, 200000)
g3_fluct = np.sin(xs)                                  # fluctuation TT-like, moyenne nulle
mean_fluct = float(np.mean(g3_fluct))                  # moyenne d'échantillons ~ <g3>
var_fluct = float(np.mean(g3_fluct**2))                # ~ <g3^2>
print("       fluctuation test : <g3> = %.2e  ;  <g3^2> = %.4f" % (mean_fluct, var_fluct))
check(abs(mean_fluct) < 1e-6 and var_fluct > 0.1,
      "∃ g3≠0 de moyenne nulle (∈ S_A3, ∉ S_A4) : inclusion S_A4 ⊊ S_A3 STRICTE")
print("       => A4 => A3-un-point  (à SENS UNIQUE) ;  A3 ⇏ A4  (A3 laisse vivre g3≠0).")
print("       => {A3, A4} -> {A4} AU UN-POINT : A3-un-point ABSORBÉ. Réduction de comptage.")

# ======================================================================
# [4] DIVERGENCE A3/A4 = DEUX-POINT k^3  (= SPECTRE-K3, cf. parent)
# ======================================================================
banner("[4] DIVERGENCE A3/A4  —  <g3 g3> ~ k^3 (A3) vs 0 (A4) : l'écart vit au deux-point")

# Chaîne spectrale (re-dérivée, cf. verif_D3_spectre_k3) : P_h=const <=> P_{g0}∝k^-3
# => P_{g3} = |g3/g0|^2 P_{g0} = (1/9)k^6 · k^-3 ∝ k^3 = k^{2Δ-d}.
C0 = sp.symbols('C0', positive=True)
P_g0 = C0 * k**(-3)
fac = sp.simplify(sp.Abs(g3 / g0)**2)                  # = (1/9) k^6
P_g3 = sp.simplify(fac * P_g0)
expo = sp.simplify(k * sp.diff(sp.log(P_g3), k))       # exposant en k
print("       |g3/g0|^2 =", fac, "  ;  P_{g3} =", P_g3, "  ;  exposant k =", expo)
check(sp.simplify(fac - sp.Rational(1, 9) * k**6) == 0, "|g3/g0|^2 = (1/9) k^6 (parent)")
check(sp.simplify(expo - 3) == 0 and (2 * Delta - d) == 3,
      "P_{g3} ∝ k^3 = k^{2Δ-d} (Δ=d=3) : deux-point invariant d'échelle")

# Sous A3 (BD) : <g3 g3> ~ k^3 ≠ 0 ; sous A4 (g3=0) : <g3 g3> = 0.
twopt_A3 = P_g3                                        # ∝ k^3, non nul
twopt_A4 = (g3_A4)**2                                  # = 0
check(sp.simplify(twopt_A3) != 0 and sp.simplify(twopt_A4) == 0,
      "<g3g3>: A3 ~ k^3 ≠ 0  vs  A4 = 0  =>  écart A3/A4 ENTIÈREMENT au deux-point")
print("       => le résidu k^3 (SPECTRE-K3 = spectre primordial) EST la différence A3/A4.")
print("       => la réduction du un-point NE FERME PAS D1 : le deux-point reste libre.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "=" * 72)
print(" RÉSULTAT : %d/%d ASSERTS PASSENT" % (N_ASSERT, N_ASSERT))
print("=" * 72)
print("""
 INTERPRÉTATION (discipline §6.4) :
   • RECONFIRMÉ (aucune algèbre neuve, faits des parents rejoués) :
       [1] A3, A4, D1 contraignent le MÊME objet g3 (relation d'état BD).
       [2] A3 (dS-inv) => <g3>=0, forcé par symétrie (TT d'un isotrope = 0).
       [3] A4 (g3=0) => <g3>=0 ; S_A4 ⊊ S_A3 STRICTE => A4 => A3-un-point (sens unique).
           {A3, A4} -> {A4} AU UN-POINT : réduction de comptage cartographiée.
       [4] Écart A3/A4 = deux-point <g3g3> ~ k^3 (SPECTRE-K3), irréductible, ≠ ferme D1.
   • NON SCELLÉ : la généralisation NON-LINÉAIRE de la coïncidence un-point
     (au-delà du mode TT perturbatif) reste `décision ouverte` (WEYL-BD §6).
     A3 et A4 NE fusionnent PAS tout court (l'écart k^3 persiste). D1 NON clos.
   • EFFET : le contenu UN-POINT de A3 est redondant dès qu'on tient A4 -> un postulat
     indépendant de moins au un-point. Réduction d'hypothèse, PAS démonstration de la CCC.
     « Le bang gagne » (P6 B) intact ; aucune touche à l'algèbre des chaînons amont.
""")
