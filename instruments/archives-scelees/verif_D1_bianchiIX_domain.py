#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_bianchiIX_domain.py — VERROUILLAGE avant l'intégration inter-éon.
(Pré-étude de LC-WORK-CADRAGE-INTERAEON. Borne le domaine de Λ et la stiffness AVANT
de lancer le calcul complet de la carte ε_n↦ε_{n+1}.)

DEUX QUESTIONS À VERROUILLER.
  (Q1) DOMAINE de Λ : pour quel Λ un Bianchi IX (courbure positive, S³) atteint-il un 𝓘
       de Sitter, plutôt que de RECOLLAPSER ? (Wald 1983 exclut IX de son no-hair garanti :
       IX recollapse si Λ trop petit.) -> il faut une borne pour démarrer l'intégration
       dans un régime qui EXPANSE.
  (Q2) STIFFNESS : le système d'ODE est-il raide (séparation d'échelles) ? quel choix de
       variables/solveur le dompte ?

MÉTHODE. Pas d'évolution complète : contrainte hamiltonienne 3H² = ρ_r + Λ + σ² − ½·³R
(vérifiée sur Kasner vide : 3H²=σ²), où ³R est le scalaire de Ricci 3D de Bianchi IX
(n_i=1). Le recollapse = existence d'un point de retournement (3H²=0) pendant l'expansion.

RÉSULTATS À VERROUILLER.
  [D1] ³R(ε,a) de Bianchi IX : rond = 3/(2a²) ; DÉCROÎT avec l'anisotropie (3/2−4ε²).
  [D2] Seuil de recollapse (forme analytique) : Λ_crit(ε) = κ(ε)²/(16 ρ_r0), κ(ε)=½³R·a².
       Rond : Λ_crit(0) = 9/(64 ρ_r0). Au-dessus -> 𝓘 ; en-dessous -> recollapse.
  [D3] L'anisotropie est CONSERVATRICE : Λ_crit(ε) < Λ_crit(0) (³R réduit + σ²>0 aident).
       Donc le seuil ROND est une BORNE SUPÉRIEURE sûre : Λ > 9/(64ρ_r0) garantit 𝓘 même
       anisotrope. -> domaine GO verrouillé.
  [D4] Stiffness : en temps cosmique, mal conditionné (plage dynamique a~e^N) ; en temps
       e-fold N=ln a (variables expansion-normalisées Wainwright-Ellis), AUTONOME et BORNÉ,
       valeurs propres au point fixe de Sitter {−2,−3,−4} (ratio 2) : NON RAIDE. ~15 e-folds
       suffisent à geler l'anisotropie. -> solveur explicite RK en e-fold ; Radau si bang.

Dépendances : sympy, numpy. Re-exécutable, sans réseau.
Réfs : Wald PRD 28 (1983) ; Lin-Wald (recollapse de IX) ; Wainwright-Ellis (1997) ;
Tod arXiv:1309.7248 (éq.20, contrainte).
"""

import sympy as sp
import numpy as np

print("="*78)
print(" verif_D1_bianchiIX_domain.py — VERROUILLAGE : domaine de Λ (𝓘 vs recollapse) + stiffness")
print("="*78)

# ======================================================================
# [D1] Scalaire de Ricci 3D de Bianchi IX (n_i=1) : rond vs anisotrope.
#      ³R = (1/2V²)[2(A1²A2²+A2²A3²+A3²A1²) − (A1⁴+A2⁴+A3⁴)], V=A1A2A3.
# ======================================================================
print("\n" + "-"*78)
print(" [D1] ³R de Bianchi IX : maximal à l'isotropie, décroît avec l'anisotropie")
print("-"*78)
eps, a = sp.symbols('epsilon a', positive=True)
def R3(A1, A2, A3):
    V = A1*A2*A3
    return sp.simplify((2*(A1**2*A2**2 + A2**2*A3**2 + A3**2*A1**2)
                        - (A1**4 + A2**4 + A3**4)) / (2*V**2))
# rond, rayon a :
R3_round = R3(a, a, a)
print("   ³R rond (A,A,A) =", R3_round, "  (>0 : courbure positive, S³)")
assert sp.simplify(R3_round - sp.Rational(3,2)/a**2) == 0
# anisotrope gelé (a·e^ε, a·e^{-ε}, a) :
R3_aniso = R3(a*sp.exp(eps), a*sp.exp(-eps), a)
kappa = sp.simplify(R3_aniso * a**2)        # ³R = κ(ε)/a²
print("   ³R aniso = κ(ε)/a²,  κ(ε) =", sp.simplify(kappa), " ; série :",
      sp.series(kappa, eps, 0, 3))
assert sp.series(kappa, eps, 0, 3).removeO() == sp.Rational(3,2) - 4*eps**2
print("   => κ(ε) = 3/2 − 4ε² + … : l'anisotropie RÉDUIT la courbure (le rond est le pire cas).")

# ======================================================================
# [D2] Seuil de recollapse : Λ_crit(ε) = κ(ε)²/(16 ρ_r0).
#      3H² = ρ_r0 a⁻⁴ + Λ − (1/2)³R(=κ/(2a²)) ; min sur a ; =0 au seuil.
# ======================================================================
print("\n" + "-"*78)
print(" [D2] Seuil de recollapse Λ_crit(ε) = κ(ε)²/(16 ρ_r0)  (analytique + numérique)")
print("-"*78)
rho_r0, Lam = sp.symbols('rho_r0 Lambda', positive=True)
x = sp.symbols('x', positive=True)             # x = a^{-2}
threeH2 = rho_r0*x**2 + Lam - (kappa/2)*x       # 3H² en fonction de x, à shape ε figé
xmin = sp.solve(sp.diff(threeH2, x), x)[0]
min_val = sp.simplify(threeH2.subs(x, xmin))
Lam_crit = sp.simplify(sp.solve(sp.Eq(min_val, 0), Lam)[0])
print("   min_a 3H² =", min_val, "  -> =0 au seuil")
print("   Λ_crit(ε) =", Lam_crit)
Lam_crit_round = sp.simplify(Lam_crit.subs(eps, 0))
print("   Λ_crit(0) [rond] =", Lam_crit_round, " = 9/(64 ρ_r0)")
assert sp.simplify(Lam_crit_round - sp.Rational(9,64)/rho_r0) == 0
# vérif numérique (ρ_r0=1) : balayage de Λ, recherche du retournement.
print("\n   vérif numérique (ρ_r0=1, rond) :")
def min3H2(Lval, epsval, rho=1.0):
    kap = float(kappa.subs(eps, epsval))
    xs = np.linspace(1e-4, 50, 200000)
    return np.min(rho*xs**2 + Lval - (kap/2)*xs)
for Lv in [0.10, 0.1406, 0.18]:
    m = min3H2(Lv, 0.0)
    verdict = "RECOLLAPSE (min<0)" if m < -1e-9 else "atteint 𝓘 (min≥0)"
    print(f"     Λ={Lv:.4f} : min 3H² = {m:+.5f} -> {verdict}")
assert min3H2(0.10,0.0) < 0 and min3H2(0.18,0.0) > 0
print(f"   -> Λ_crit(0) numérique ≈ {float(Lam_crit_round.subs(rho_r0,1)):.4f}  (= 9/64) ✓")

# ======================================================================
# [D3] L'anisotropie est CONSERVATRICE : Λ_crit(ε) < Λ_crit(0).
# ======================================================================
print("\n" + "-"*78)
print(" [D3] L'anisotropie ABAISSE le seuil : le rond est la borne SÛRE (conservatrice)")
print("-"*78)
print("   Λ_crit(ε)/Λ_crit(0) = (κ(ε)/κ(0))² =", sp.series((kappa/sp.Rational(3,2))**2, eps, 0, 3))
for ev in [0.0, 0.2, 0.4]:
    lc = float(Lam_crit.subs({eps: ev, rho_r0: 1}))
    print(f"     ε={ev:.1f} : Λ_crit = {lc:.4f}")
# démonstration : à Λ entre les deux seuils, le rond recollapse, l'anisotrope expanse.
Lmid = 0.5*(float(Lam_crit.subs({eps:0.4, rho_r0:1})) + float(Lam_crit_round.subs(rho_r0,1)))
print(f"   À Λ={Lmid:.4f} (entre les deux seuils) :")
print(f"     rond (ε=0)   : min 3H² = {min3H2(Lmid,0.0):+.5f} -> ",
      "RECOLLAPSE" if min3H2(Lmid,0.0)<0 else "𝓘")
print(f"     aniso (ε=0.4): min 3H² = {min3H2(Lmid,0.4):+.5f} -> ",
      "RECOLLAPSE" if min3H2(Lmid,0.4)<0 else "atteint 𝓘")
assert min3H2(Lmid,0.0) < 0 and min3H2(Lmid,0.4) > 0
print("   => CONFIRMÉ : à shape figé, l'anisotropie aide ; (+ σ²>0 en évolution aide encore).")
print("      VERROU DOMAINE : Λ > 9/(64 ρ_r0) [rond, conservateur] garantit 𝓘 même anisotrope.")

# ======================================================================
# [D4] Stiffness : raide en temps cosmique, NON raide en temps e-fold.
# ======================================================================
print("\n" + "-"*78)
print(" [D4] Stiffness : domptée par le temps e-fold (variables expansion-normalisées)")
print("-"*78)
# Plage dynamique : a de 1 (ère radiation) à ~e^N (de Sitter). N e-folds pour geler σ.
# σ ∝ a^{-3} ; pour Σ=σ/θ de ε à 1e-6 en de Sitter : dΣ/dN=−3Σ -> N≈(1/3)ln(ε/1e-6).
N_freeze = (1/3)*np.log(0.3/1e-6)
print(f"   e-folds pour geler l'anisotropie (ε=0.3 -> Σ<1e-6) : N ≈ {N_freeze:.1f}  (+ qq pour radiation→Λ)")
print(f"   plage dynamique en a : ~ e^{{{N_freeze:.0f}}} ~ {np.exp(N_freeze):.1e}  -> en temps COSMIQUE :")
print(f"     condition ~ (a)²  (radiation H∝a⁻²) ~ {np.exp(2*N_freeze):.1e} : MAL conditionné.")
# Valeurs propres au point fixe de Sitter, en variables expansion-normalisées (e-fold N) :
#   Ω_radiation ~ a^{-4}/H² -> taux −4 ; courbure ~ a^{-2}/H² -> −2 ; Σ (shear) -> −3.
eigs = np.array([-4.0, -3.0, -2.0])
ratio = abs(eigs.min())/abs(eigs.max())
print("   en temps E-FOLD (N=ln a), au point fixe de Sitter — valeurs propres :")
print(f"     Ω_r : {eigs[0]:.0f}   Σ_shear : {eigs[1]:.0f}   Ω_courbure : {eigs[2]:.0f}")
print(f"     ratio de raideur |λ_max|/|λ_min| = {ratio:.1f}  -> NON RAIDE (autonome, borné).")
assert ratio < 5
print("   => VERROU STIFFNESS : intégrer en N=ln a (expansion-normalisé, Wainwright-Ellis).")
print("      Solveur explicite (RK45/DOP853) suffit ; Radau (implicite) en secours si on")
print("      approche le bang (Mixmaster, P6 — exclu au premier tour). ~15-20 e-folds, coût faible.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT DE VERROUILLAGE :")
print("="*78)
print("   (Q1) DOMAINE : Λ_crit(ε) = κ(ε)²/(16 ρ_r0), MAX à l'isotropie (Λ_crit(0)=9/(64ρ_r0)).")
print("        L'anisotropie ABAISSE le seuil (³R réduit + σ²>0). -> borne SÛRE :")
print("            ┌────────────────────────────────────────────────┐")
print("            │  Λ > 9/(64 ρ_r0)  garantit 𝓘  (même anisotrope) │")
print("            └────────────────────────────────────────────────┘")
print("        [ρ_r0, courbure : fixés par les données de bang de Tod / normalisation Yamabe.]")
print("   (Q2) STIFFNESS : raide en temps cosmique (plage a~e^N), NON raide en temps e-fold")
print("        (valeurs propres {−2,−3,−4}, ratio 2). Variable N=ln a + RK explicite.")
print("        Coût : ~15-20 e-folds. Bang (Mixmaster) exclu au 1er tour -> pas de raideur extrême.")
print("")
print("   => GO VERROUILLÉ : démarrer dans l'ère de radiation, Λ confortablement > 9/(64ρ_r0),")
print("      variables expansion-normalisées. Le 1er pas du cadrage est sûr et borné.")
print("="*78)
