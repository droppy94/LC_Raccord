#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1c3_genericite.py — LC-RACCORD / verrou-D1, Phase B-2 (cible D1c3-3).
Cadrage gelé : LC-WORK-CADRAGE-D1C3-INHOMOGENE (sha 6d3baa6f...f44e433), D1c3-3.
Étend verif_D1c3_regularite.py (D1c3-2, verdict D1c3-c sur Bianchi A homogène).

QUESTION (D1c3-3). Le verdict D1c3-c — « la régularité du crossover ne force pas
â_ij Einstein-3D ⟹ σ̌=-4·(Ricci sans-trace de â)≠0 » — SURVIT-il aux perturbations
INHOMOGÈNES (k-dépendantes) de FLRW, ou est-ce un ARTEFACT d'homogénéité (le testbed
Bianchi A étant homogène-anisotrope) ? C'est la cible D1c3-3 du cadrage gelé
(LC-WORK-CADRAGE-D1C3-INHOMOGENE).

MÉTHODE. On perturbe la 3-géométrie de bord â plate par un mode TT genuinement
INHOMOGÈNE (onde plane, k≠0) et on calcule le Ricci sans-trace (source de σ̌) :
  â_ij = δ_ij + ε·H_ij(z),  H = diag(cos kz, -cos kz, 0)  [polarisation +,
  TT : trace=0, transverse à k=(0,0,k)].
Si le Ricci sans-trace linéaire est ∝ k² (k-dépendant, ≠0), la source de marée est un
phénomène INHOMOGÈNE intrinsèque, PAS réductible à l'anisotropie homogène ⟹ D1c3-c
n'est pas un artefact. Friedrich (1986) : h^{TT} est donnée de bord LIBRE ⟹ la
régularité ne la force pas à 0.

SCEAUX :
  [G1] Ricci sans-trace linéaire d'une perturbation TT inhomogène : = +½ k² H_ij·ε
       (k-dépendant, ≠0, oscillant en z) ⟹ σ̌ = -4·(Ricci sans-trace) = -2 k² H_ij·ε ≠ 0.
       Comparaison homogène (k→0) : s'annule — la marée inhomogène est STRICTEMENT un
       effet de mode (k²), distinct du secteur homogène. ⟹ pas un artefact d'homogénéité.
  [G2] Friedrich : h^{TT} (le mode) est donnée de bord LIBRE ⟹ régularité-lisse ⊉
       (Ricci sans-trace = 0). Même structure qu'en Bianchi A : D1c3-c GÉNÉRIQUE.
  [G3] Rappel (verif_D1c3_regularite [R2]) : le gap Cotton/Einstein-3D a DÉJÀ été montré
       sur un â INHOMOGÈNE (g=e^{2x}δ : Cotton≡0 mais Ricci sans-trace≠0) ⟹ « Cotton→0 »
       ne force pas non plus Einstein-3D dans l'inhomogène. (Non recalculé ici.)

VERDICT (D1c3-3) = D1c3-c CONFIRMÉ GÉNÉRIQUE (non-artefact d'homogénéité). Le sceau
établit l'algèbre [G1]-[G3] sur â INHOMOGÈNE ; il ne porte PAS la couche programme.
(Rattachement R-53 — levée de la condition (ii) du verdict d'axe — porté HORS sceau par
LC-WORK-AMENDEMENT-R7-D1-AXE-II-LEVEE.) SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N}
inchangé ; D1 non clos.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs : Friedrich CMP 107 (1986) — donnée conforme TT LIBRE à 𝓘 spacelike ; linéarisation
standard du 3-Ricci ; Tod 1309.7248 éq.(33) ; Milnor 1976 (cas homogène, verif_D1_bianchiA).
"""

import sympy as sp

print("="*78)
print(" verif_D1c3_genericite.py — D1c3-3 : D1c3-c survit-il à l'inhomogénéité (k≠0) ?")
print("="*78)

# ----------------------------------------------------------------------
# 3-Ricci covariant exact (reprend la machinerie de verif_D1c3_regularite).
# ----------------------------------------------------------------------
def ricci(g, X):
    n = len(X); gi = g.inv()
    Ga = [[[sp.Rational(1,2)*sum(gi[l,m]*(sp.diff(g[m,i],X[j])
            + sp.diff(g[m,j],X[i]) - sp.diff(g[i,j],X[m])) for m in range(n))
            for j in range(n)] for i in range(n)] for l in range(n)]
    def Ru(a,b,c,d):
        return (sp.diff(Ga[a][d][b],X[c]) - sp.diff(Ga[a][c][b],X[d])
                + sum(Ga[a][c][e]*Ga[e][d][b] - Ga[a][d][e]*Ga[e][c][b] for e in range(n)))
    return sp.Matrix(n,n, lambda b,d: sum(Ru(a,b,a,d) for a in range(n)))

# ======================================================================
# [G1] Perturbation TT INHOMOGÈNE (onde plane k≠0) : Ricci sans-trace ∝ k².
# ======================================================================
print("\n" + "-"*78)
print(" [G1] â = δ + ε·H(z), H=diag(cos kz,-cos kz,0) [TT, k=(0,0,k)] : Ricci sans-trace")
print("-"*78)

x, y, z = sp.symbols('x y z', real=True)
X = [x, y, z]
eps, k = sp.symbols('epsilon k', real=True, positive=True)
c = sp.cos(k*z)
H = sp.diag(c, -c, 0)                      # polarisation + ; trace 0 ; ∂_z seulement
# vérifs TT (au niveau du mode) :
assert sp.simplify(H[0,0]+H[1,1]+H[2,2]) == 0, "H doit etre traceless (TT)"
# transverse : k^i H_ij = k·H_zj = 0 (ligne/colonne z nulles) ✓ (par construction)

g = sp.eye(3) + eps*H
Ric = ricci(g, X)
# linéarisation en ε : coefficient d'ordre 1
Ric1 = sp.Matrix(3,3, lambda i,j: sp.simplify(sp.diff(Ric[i,j], eps).subs(eps,0)))
trace1 = sp.simplify(Ric1[0,0]+Ric1[1,1]+Ric1[2,2])   # trace au sens delta (ordre 1)
print(" δR_ij (ordre ε, /ε) :")
for i in range(3):
    print("   ", [sp.simplify(Ric1[i,j]) for j in range(3)])
print(" trace (δ^{ij} δR_ij) à l'ordre ε =", trace1, "  (TT préservé)")
# Ricci sans-trace linéaire = δR_ij - (1/3) trace δ_ij ; ici trace=0 ⟹ = δR_ij.
Slin = sp.Matrix(3,3, lambda i,j: sp.simplify(Ric1[i,j] - sp.Rational(1,3)*trace1*(1 if i==j else 0)))
print(" Ricci sans-trace linéaire S_ij =")
for i in range(3):
    print("   ", [sp.simplify(Slin[i,j]) for j in range(3)])
# attendu : S = +½ k² H  (k-dépendant)
target = sp.Rational(1,2)*k**2*H
assert sp.simplify(Slin - target) == sp.zeros(3,3), "S_ij doit valoir ½k²H_ij"
print(" => S_ij = +½ k²·H_ij  (k-DÉPENDANT, oscillant en z) ✓")
sigma_lin = sp.simplify(-4*Slin[0,0])      # σ̌_xx linéaire = -4 S_xx
print(" σ̌_xx (linéaire) = -4·S_xx =", sigma_lin, "  ≠ 0 pour k≠0.")
assert sp.simplify(sigma_lin) != 0
# limite homogène k→0 : la marée de mode s'éteint (effet strictement inhomogène).
lim_k0 = sp.limit(Slin[0,0], k, 0)
print(" lim_{k→0} S_xx =", lim_k0, " -> la marée de MODE est ∝ k² (effet STRICTEMENT")
print("    inhomogène, distinct du secteur homogène-anisotrope de Bianchi A).")
assert lim_k0 == 0
print(" => [G1] : un mode TT INHOMOGÈNE source un Ricci sans-trace ≠0, k-dépendant ⟹")
print("    σ̌≠0 n'est PAS un artefact d'homogénéité.")

# ======================================================================
# [G2] Friedrich : h^TT = donnée de bord LIBRE ⟹ régularité ⊉ (Ricci sans-trace=0).
# ======================================================================
print("\n" + "-"*78)
print(" [G2] Friedrich (1986) : h^TT est donnée de bord LIBRE")
print("-"*78)
print("   La 3-métrique conforme de bord (mode TT h_ij^{TT}) est librement spécifiable à")
print("   un 𝓘 spacelike (Λ>0). L'amplitude ε du mode est libre ⟹ aucune lissité")
print("   d'extension conforme ne la force à 0 ⟹ régularité ⊉ (S_ij=0). Même structure")
print("   qu'en Bianchi A (verif_D1c3_regularite [R1]) : le verdict D1c3-c est GÉNÉRIQUE.")
# [G2] est une prémisse IMPORTÉE (Friedrich 1986) : NON code-vérifiable ici (Mode B).
# Le check ci-dessous n'est PAS un test de Friedrich : c'est un RE-CHECK concret de [G1]
# (S≠0 à k=1), conservé comme garde-fou de non-régression de l'algèbre.
assert sp.simplify(Slin[0,0].subs(k, 1)) != 0   # re-check [G1] @k=1 (PAS un test de [G2])

# ======================================================================
# [G3] Rappel : gap Cotton/Einstein-3D déjà montré sur un â INHOMOGÈNE.
# ======================================================================
print("\n" + "-"*78)
print(" [G3] (rappel verif_D1c3_regularite [R2]) Cotton/Einstein-3D : déjà inhomogène")
print("-"*78)
print("   g=e^{2x}δ (INHOMOGÈNE, dépend de x) a Cotton≡0 mais Ricci sans-trace≠0 ⟹")
print("   « Cotton→0 » ne force pas Einstein-3D dans l'inhomogène non plus. (Non recalculé.)")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT (D1c3-3) :")
print("="*78)
print("   [G1] mode TT inhomogène ⟹ Ricci sans-trace = ½k²H ≠0 (k-dépendant) ⟹ σ̌≠0 ;")
print("        ∝k² ⟹ effet STRICTEMENT inhomogène (pas réductible à l'homogène).")
print("   [G2] h^TT = donnée de bord LIBRE (Friedrich) ⟹ régularité ⊉ (Ricci sans-trace=0).")
print("   [G3] gap Cotton/Einstein-3D déjà établi sur un â inhomogène (e^{2x}δ).")
print("   ⟹ D1c3-c CONFIRMÉ GÉNÉRIQUE : la régularité ne force pas â Einstein-3D, ni en")
print("      homogène-anisotrope (Bianchi A) ni en INHOMOGÈNE (mode TT). PAS un artefact.")
print("   (Couche programme — levée condition (ii) du verdict d'axe — HORS sceau :")
print("    voir LC-WORK-AMENDEMENT-R7-D1-AXE-II-LEVEE.)")
print("")
print(" DISCIPLINE (§6.4) : `établi` valide L'ALGÈBRE (linéarisation exacte du 3-Ricci),")
print("   JAMAIS une conclusion physique. {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ;")
print("   N non fixé (≡Λ) ; CCC non démontrée NI réfutée.")
print("="*78)
print("EXIT 0 (G1: S=½k²H, ∝k², σ̌≠0, lim_{k→0}=0 ; G2: mode libre ; assertions OK)")
