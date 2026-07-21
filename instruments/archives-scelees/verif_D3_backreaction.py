#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_backreaction.py — LC-RACCORD, front (a) du raccord, étape (a2).
(Compagnon de LC-D3-CROSSOVER-BACKREACTION. Étend verif_D3_bunchdavies.py.)

QUESTION (a2). L'homogénéité linéaire de (a1) (ĝ₃=0 ↦ ǧ₃=0) survit-elle à O(h²) ?
Au second ordre, les fluctuations de Bunch-Davies — dont la 2-points est IRRÉDUCTIBLE,
⟨g₃ g₃⟩ ~ k³ (LC-D3 §4) — back-réagissent gravitationnellement (stress effectif des
ondes, Isaacson). La 1-point de la marée acquiert-elle un terme ⟨g₃^(2)⟩ ≠ 0 (qui
casserait « né dans le vide ») ?

MÉCANISME testé. La 1-point ⟨g₃^(2)⟩ est la part traceless-symétrique (= la part TT du
secteur homogène k->0) du stress effectif ⟨τ_ij⟩ dans l'état. Pour un MODE unique,
τ_ij ∝ k̂_i k̂_j est ANISOTROPE (part traceless ≠ 0) : une OG isolée porte un
cisaillement. Mais le vide de Bunch-Davies est dS-invariant => statistiquement ISOTROPE :
la moyenne d'ensemble est l'intégrale angulaire sur les directions k̂, qui rend ⟨τ_ij⟩
ISOTROPE (∝ δ_ij). Or la part traceless d'un tenseur isotrope est NULLE (lemme [S4] de a1).
Donc ⟨g₃^(2)⟩ = 0 : l'homogénéité SURVIT à O(h²). La part isotrope non nulle (densité
d'énergie, pression du bain de gravitons BD) renormalise le FOND (Λ, (m,λ)) -> source de
l'itération de l'atlas -> (a3). Conditionnel à l'invariance dS de l'état (= hypothèse BD).

Sceaux :
  [1] Recap linéaire BD : mode solution TT, 1-point nulle (vide gaussien), 2-points ~k³.
  [2] Back-réaction RÉELLE : stress effectif quadratique du mode BD, densité ≠ 0.
  [3] MODE UNIQUE anisotrope : τ_ij ∝ k̂_i k̂_j, part traceless ≠ 0 (cisaillement).
  [4] MOYENNE BD isotrope : ∫dΩ k̂_i k̂_j = (4π/3)δ_ij ; ∫dΩ Λ_ij,kl(k̂) isotrope
      => ⟨τ_ij⟩ ∝ δ_ij.
  [5] Isotrope => part traceless nulle => ⟨g₃^(2)⟩ = 0 (homogénéité survit à O(h²)).

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs (cf. LC-04) : Bunch-Davies, Proc. R. Soc. A 360, 117 (1978) ; Isaacson, Phys. Rev.
166, 1272 (1968) — stress effectif des ondes ; Maldacena astro-ph/0210603 (dS/CFT) ;
de Haro-Skenderis-Solodukhin CMP 217 (2001).
"""

import sympy as sp

print("="*74)
print(" verif_D3_backreaction.py — (a2) ⟨g₃⟩=0 survit-il à O(h²) ? (back-réaction BD)")
print("="*74)

eta, k, H, A = sp.symbols('eta k H A', positive=True)
I = sp.I
th, ph = sp.symbols('theta phi', real=True)

# ======================================================================
# [1] Recap linéaire BD (depuis verif_D3_bunchdavies) : 1-point nulle, 2-points ~k³.
# ======================================================================
print("\n[1] Recap linéaire (Bunch-Davies) :")
f = A*(1 + I*k*eta)*sp.exp(-I*k*eta)
EOM = sp.simplify(sp.diff(f, eta, 2) - (2/eta)*sp.diff(f, eta) + k**2*f)
print("    mode BD f=(1+ikη)e^{-ikη} : EOM TT =", EOM, "-> solution.")
assert EOM == 0
g3_lin = sp.expand(sp.series(f, eta, 0, 5).removeO()).coeff(eta, 3)
print("    g₃ (lin) =", sp.simplify(g3_lin), " ; ⟨g₃⟩^(1) = 0 (vide gaussien : 1-point nulle)")
print("    ⟨g₃ g₃⟩ ~ k³ ≠ 0 (conforme Δ=3, IRRÉDUCTIBLE) -> le résidu source la BR.")

# ======================================================================
# [2] Back-réaction RÉELLE : stress effectif quadratique du mode BD, densité ≠ 0.
#     Isaacson : t_μν ∝ ⟨∂_μ h_ab ∂_ν h_ab⟩. Ici on confirme t_00 (densité) ≠ 0.
# ======================================================================
print("\n[2] Back-réaction réelle (stress effectif d'Isaacson, ordre h²) :")
# profil temporel du mode (partie réelle pour l'énergie) ; densité ~ |∂_η h|² + k²|h|².
dh = sp.diff(f, eta)
rho_mode = sp.simplify(sp.Abs(dh)**2 + k**2*sp.Abs(f)**2)  # densité d'un mode (schématique)
rho_mode = sp.simplify(sp.expand(rho_mode))
print("    densité d'un mode  ~ |h'|² + k²|h|²  =", rho_mode)
print("    -> ≠ 0 : la back-réaction EXISTE (bain de gravitons d'énergie non nulle).")
assert rho_mode != 0

# ======================================================================
# [3] MODE UNIQUE : stress spatial ∝ k̂_i k̂_j -> ANISOTROPE (part traceless ≠ 0).
# ======================================================================
print("\n[3] Mode unique (k̂ = ẑ) : le stress spatial est anisotrope.")
kz = sp.Matrix([0, 0, 1])                          # direction du mode
tau_mode = kz*kz.T                                 # τ_ij ∝ k̂_i k̂_j (flux de moment)
trace_mode = sp.trace(tau_mode)
tau_mode_tl = sp.simplify(tau_mode - sp.Rational(1,3)*trace_mode*sp.eye(3))  # part traceless
print("    τ_ij ∝ k̂_i k̂_j =", tau_mode.tolist())
print("    part traceless =", tau_mode_tl.tolist(), " -> ≠ 0 : une OG isolée porte un cisaillement.")
assert tau_mode_tl != sp.zeros(3, 3)

# ======================================================================
# [4] MOYENNE BD : isotropie par intégration angulaire sur k̂.
# ======================================================================
print("\n[4] Vide de Bunch-Davies = dS-invariant => moyenne d'ensemble ISOTROPE.")
nhat = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
dOm = sp.sin(th)
def sph_avg(expr):  # (1/4π) ∫ expr sinθ dθ dφ
    return sp.simplify(sp.integrate(sp.integrate(expr*dOm, (ph, 0, 2*sp.pi)),
                                     (th, 0, sp.pi)) / (4*sp.pi))

# (4a) ⟨k̂_i k̂_j⟩ = (1/3) δ_ij
M = sp.Matrix(3, 3, lambda i, j: sph_avg(nhat[i]*nhat[j]))
print("    ⟨k̂_i k̂_j⟩ =", M.tolist(), " (= (1/3)δ_ij : isotrope)")
assert sp.simplify(M - sp.Rational(1,3)*sp.eye(3)) == sp.zeros(3, 3)

# (4b) somme de polarisation Λ_ij,kl(k̂) = P_ik P_jl + P_il P_jk - P_ij P_kl, P=I-k̂k̂.
P = sp.eye(3) - nhat*nhat.T
def Lam(i, j, kk, l):
    return P[i,kk]*P[j,l] + P[i,l]*P[j,kk] - P[i,j]*P[kk,l]
# Contraction de stress polarisé : S_ij = ⟨ Λ_ia,ja (somme a) ⟩  (structure ∂_a h_ib type)
S = sp.Matrix(3, 3, lambda i, j: sph_avg(sum(Lam(i, a, j, a) for a in range(3))))
S = sp.simplify(S)
coeff = sp.simplify(S[0, 0])
print("    ⟨Σ_a Λ_ia,ja⟩ =", S.tolist())
print("    -> proportionnel à δ_ij (coeff =", coeff, ") : ISOTROPE.")
assert sp.simplify(S - coeff*sp.eye(3)) == sp.zeros(3, 3)

# stress effectif moyenné : combinaison des structures isotropes -> ∝ δ_ij
tau_avg = M + sp.Rational(1,1)*S          # somme de structures (flux + polarisation), toutes ∝ δ
tau_avg = sp.simplify(tau_avg)
print("    ⟨τ_ij⟩_BD (somme des structures) =", tau_avg.tolist(), " -> ∝ δ_ij.")
assert sp.simplify(tau_avg - sp.Rational(tau_avg[0,0].p, tau_avg[0,0].q)*sp.eye(3)) == sp.zeros(3,3) \
       if tau_avg[0,0].is_Rational else True

# ======================================================================
# [5] Isotrope => part traceless nulle => ⟨g₃^(2)⟩ = 0.
# ======================================================================
print("\n[5] La 1-point ⟨g₃^(2)⟩ = part traceless-symétrique de ⟨τ_ij⟩_BD :")
trace_avg = sp.trace(tau_avg)
g3_2 = sp.simplify(tau_avg - sp.Rational(1,3)*trace_avg*sp.eye(3))   # part traceless de l'isotrope
print("    part traceless de ⟨τ_ij⟩_BD =", g3_2.tolist())
assert g3_2 == sp.zeros(3, 3)
print("    => ⟨g₃^(2)⟩ = 0 : l'homogénéité ⟨g₃⟩=0 SURVIT à O(h²).")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-"*74)
print(" VERDICT (a2) — O(h²), conditionnel à l'invariance dS de l'état :")
print("   [2] la back-réaction des fluctuations BD est RÉELLE (densité ≠ 0).")
print("   [3] un mode unique est ANISOTROPE (part traceless ≠ 0 : cisaillement).")
print("   [4] mais le vide BD est isotrope => ⟨τ_ij⟩ ∝ δ_ij (∫dΩ k̂k̂=(1/3)δ, Λ isotrope).")
print("   [5] part traceless d'un isotrope = 0 => ⟨g₃^(2)⟩ = 0.")
print("   ==> ⟨g₃⟩=0 SURVIT à O(h²). « Né dans le vide » tient au second ordre,")
print("       SI l'état de raccordement reste dS-invariant (= hypothèse BD).")
print(" CE QUE FAIT LA BACK-RÉACTION (la part NON nulle, isotrope) :")
print("   densité ρ + pression p (bain de gravitons) -> renormalise le FOND (Λ, (m,λ))")
print("   = source de l'itération de l'atlas §4-bis -> question du runaway = (a3).")
print("   [UV de ρ ~ ∫dk k³ -> coupure holographique N (LC-E) : ρ ~ énergie du vide.]")
print(" RÉSERVES (décision ouverte) :")
print("   - le résultat est CONDITIONNEL à l'isotropie (dS-invariance) de l'état ;")
print("     un état de raccordement ANISOTROPE (a1: Bianchi A ; dS/CFT non unitaire)")
print("     donnerait ⟨k̂k̂⟩ ≠ (1/3)δ -> ⟨g₃^(2)⟩ ≠ 0 : c'est LA porte d'une marée.")
print("   - 2-points ⟨g₃g₃⟩~k³ inchangée (spectre primordial) : WCH reste un-point.")
print("-"*74)
