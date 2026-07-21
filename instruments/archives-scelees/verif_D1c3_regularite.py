#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1c3_regularite.py — LC-RACCORD / verrou-D1, Phase B-1 (cible D1c3-2).
Cadrage gelé : LC-WORK-CADRAGE-D1C3-INHOMOGENE (sha 6d3baa6f...f44e433).
Étend verif_D1_bianchiA.py [B2] (Milnor + Tod éq.33) et répond au SEUL point
ouvert qu'il laissait (sa l.259) : « WCH/régularité force-t-il â_ij de 𝓘 à être
Einstein 3D ? ».

QUESTION (D1c3-2). La marée future est σ̌ = -4·(Ricci sans-trace de â) [Tod 33].
La tuer (σ̌=0) ⟺ â_ij Einstein-3D (en dim 3 : Ricci sans-trace nul ⟺ courbure
constante ⟺ isotropie). On teste si une CONDITION DE RÉGULARITÉ au crossover force
â_ij à être Einstein-3D — d'abord la régularité au sens de Friedrich/Tod (lissité de
l'extension conforme), puis le candidat « extended-WCH » le plus fort : Cotton→0
(conforme-plat, analogue 3D du Weyl-4D→0).

SCEAUX :
  [R1] Régularité-Friedrich/Tod NE force PAS Einstein-3D — contre-exemple CONSTRUCTIF :
       â Bianchi IX squashé (anisotropie ε) admet un crossover LISSE de Tod (1309.7248,
       §7) avec σ̌≠0. On re-dérive σ̌(ε) via Milnor (comme [B2]) : σ̌→0 quand ε→0 mais
       σ̌≠0 sinon ; |σ̌|² ∝ ε². Donc « extension conforme lisse » (donnée de bord LIBRE
       de Friedrich 1986) admet â NON-Einstein ⟹ régularité ⊉ Einstein-3D.
  [R2] Le candidat le plus fort « extended-WCH = Cotton→0 » NE force PAS non plus
       Einstein-3D : le tenseur de Cotton (qui s'annule ⟺ conforme-plat en dim 3) est
       STRICTEMENT plus faible que « Ricci sans-trace = 0 » (Einstein-3D). Contre-exemple
       explicite : g = e^{2x}·δ_3 (conforme-plat par construction ⟹ Cotton≡0) a un Ricci
       SANS TRACE ≠ 0 (donc PAS Einstein-3D, σ̌≠0). On calcule Cotton (≡0) ET Ricci
       sans-trace (≠0) symboliquement.

VERDICT (D1c3-2, secteur Bianchi A) = D1c3-c (issue faible DÉFINITIVE pour les
conditions de régularité NATURELLES) : ni la lissité de Friedrich/Tod, ni « Cotton→0 »
ne forcent â_ij Einstein-3D. La seule condition qui le ferait (Ricci sans-trace=0
imposé) est ≥ postuler la courbure constante = un POSTULAT INDÉPENDANT (non dérivable
de A4, qui contraint le Weyl 4D de cœur, pas la 3-géométrie de bord). ⟹ A3 reste socle
indépendant ; D3-régularité ne sélectionne pas la prescription ; D1 non fermé par cette
voie. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} inchangé ; D1 non clos.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs : Tod arXiv:1309.7248v2 = GRG 47,17 (2015) éq.(33), §7 Bianchi A ; Friedrich CMP
107 (1986) — donnée conforme LIBRE à 𝓘 spacelike (Λ>0) ; Milnor Adv.Math.21 (1976) ;
Cotton (1899) / York — tenseur de Cotton, conforme-platitude en dim 3.
"""

import sympy as sp

print("="*78)
print(" verif_D1c3_regularite.py — D1c3-2 : la régularité force-t-elle â_ij Einstein-3D ?")
print("="*78)

# ======================================================================
# Outils 3D : Christoffel, Ricci, scalaire, Cotton.
# ======================================================================
def christoffel(g, X):
    n = len(X); gi = g.inv()
    return [[[sp.simplify(sum(sp.Rational(1,2)*gi[l,m]*(
                sp.diff(g[m,i],X[j]) + sp.diff(g[m,j],X[i]) - sp.diff(g[i,j],X[m]))
              for m in range(n))) for j in range(n)] for i in range(n)] for l in range(n)]

def ricci(g, X):
    n = len(X); Ga = christoffel(g, X)
    def Ru(a,b,c,d):
        return (sp.diff(Ga[a][d][b],X[c]) - sp.diff(Ga[a][c][b],X[d])
                + sum(Ga[a][c][e]*Ga[e][d][b] - Ga[a][d][e]*Ga[e][c][b] for e in range(n)))
    Ric = sp.Matrix(n,n, lambda b,d: sp.simplify(sum(Ru(a,b,a,d) for a in range(n))))
    return Ric, Ga

def cov_grad_ricci(g, X):
    # ∇_k R_ij  (R_ij covariant) = ∂_k R_ij - Γ^m_ki R_mj - Γ^m_kj R_im
    n = len(X); Ric, Ga = ricci(g, X)
    def nabla(i,j,k):
        return sp.simplify(sp.diff(Ric[i,j],X[k])
                - sum(Ga[m][k][i]*Ric[m,j] + Ga[m][k][j]*Ric[i,m] for m in range(n)))
    return Ric, nabla

def cotton(g, X):
    # C_ijk = ∇_k R_ij - ∇_j R_ik - (1/4)(g_ij ∂_k R - g_ik ∂_j R)   (n=3 ; ≡0 ⟺ conforme-plat)
    n = len(X); gi = g.inv()
    Ric, nabla = cov_grad_ricci(g, X)
    Rs = sp.simplify(sum(gi[a,b]*Ric[a,b] for a in range(n) for b in range(n)))
    C = [[[sp.simplify(nabla(i,j,k) - nabla(i,k,j)
            - sp.Rational(1,4)*(g[i,j]*sp.diff(Rs,X[k]) - g[i,k]*sp.diff(Rs,X[j])))
           for k in range(n)] for j in range(n)] for i in range(n)]
    return C, Ric, Rs

# ======================================================================
# [R1] Régularité-Friedrich/Tod ⊉ Einstein-3D — contre-exemple constructif (Milnor + Tod 33)
# ======================================================================
print("\n" + "-"*78)
print(" [R1] Friedrich/Tod : extension conforme LISSE admet â NON-Einstein (σ̌≠0)")
print("-"*78)

# 3-Ricci de Milnor (Bianchi IX, n_i=1), facteurs (A1,A2,A3) — repris de verif_D1_bianchiA.
def milnor_ricci(A1, A2, A3, n1=1, n2=1, n3=1):
    lam1 = n1*A1/(A2*A3); lam2 = n2*A2/(A3*A1); lam3 = n3*A3/(A1*A2)
    s = sp.Rational(1,2)*(lam1+lam2+lam3)
    mu1, mu2, mu3 = s-lam1, s-lam2, s-lam3
    return sp.Matrix([2*mu2*mu3, 2*mu3*mu1, 2*mu1*mu2])

a = sp.symbols('a', positive=True)
Rround = milnor_ricci(a,a,a)
print(" auto-check ε=0 (S³ ronde) : Ric =", list(Rround), " -> Einstein (sans-trace 0) ✓")
assert sp.simplify(Rround[0]-Rround[1])==0 and sp.simplify(Rround[1]-Rround[2])==0

eps = sp.symbols('epsilon', real=True)
Ric3 = milnor_ricci(sp.exp(eps), sp.exp(-eps), 1)          # â squashé, volume gelé
Rscal = sp.simplify(sum(Ric3))
S = sp.Matrix([sp.simplify(Ric3[i]-Rscal/3) for i in range(3)])   # Ricci sans-trace
sigma = [sp.simplify(-4*S[i]) for i in range(3)]                  # Tod (33)
normS2 = sp.simplify(sum(S[i]**2 for i in range(3)))
ser = sp.series(16*normS2, eps, 0, 4)
print(" â anisotrope (e^ε,e^{-ε},1) : |σ̌|²(ε) = 16|S|² =", ser, " (∝ ε²)")
assert sp.series(16*normS2, eps, 0, 2).removeO() == 0             # ni constant ni linéaire
assert sp.limit(16*normS2, eps, 0) == 0                           # raccord continu à l'isotropie
assert sp.simplify(normS2.subs(eps, sp.Rational(1,2))) != 0       # σ̌ ≠ 0 hors isotropie
print(" σ̌(ε=1/2) =", [sp.nsimplify(sigma[i].subs(eps,sp.Rational(1,2))) for i in range(3)],
      " ≠ 0")
print(" => un â NON-Einstein admet un crossover de Tod LISSE (1309.7248 §7) avec σ̌≠0.")
print("    Donnée conforme de bord = LIBRE (Friedrich 1986). ⟹ régularité ⊉ Einstein-3D.")

# ======================================================================
# [R2] « extended-WCH = Cotton→0 » ⊉ Einstein-3D — gap conforme-plat / courbure constante
# ======================================================================
print("\n" + "-"*78)
print(" [R2] Cotton→0 (conforme-plat) est STRICTEMENT plus faible que Einstein-3D")
print("-"*78)

x, y, z = sp.symbols('x y z', real=True)
Xc = [x, y, z]
# g = e^{2x} δ_3 : conforme à l'espace plat ⟹ conforme-plat ⟹ Cotton ≡ 0 (à vérifier),
# mais Ricci sans-trace ≠ 0 (à vérifier) ⟹ PAS Einstein-3D.
phi = x
gC = sp.diag(sp.exp(2*phi), sp.exp(2*phi), sp.exp(2*phi))

C3, RicC, RsC = cotton(gC, Xc)
cotton_zero = all(sp.simplify(C3[i][j][k])==0 for i in range(3) for j in range(3) for k in range(3))
print(" g = e^{2x}·δ₃ :")
print("   Cotton C_ijk ≡ 0 ?", cotton_zero, "  (conforme-plat ✓)")
assert cotton_zero, "Cotton de e^{2x}δ doit etre nul (conforme-plat)"

giC = gC.inv()
# Ricci sans-trace (1,1) : R^i_j - (1/3) R δ^i_j  -> mesure l'écart à Einstein.
Rmix = sp.simplify(giC*RicC)                      # R^i_j
trfree = sp.simplify(Rmix - (RsC/3)*sp.eye(3))    # part sans-trace mixte
print("   R^i_j =", [sp.simplify(Rmix[i,i]) for i in range(3)],
      "  R =", sp.simplify(RsC))
print("   (R^i_j - ⅓R δ^i_j) =", [sp.simplify(trfree[i,i]) for i in range(3)])
nonEinstein = sp.simplify(trfree) != sp.zeros(3,3)
print("   Ricci sans-trace ≠ 0 ?", nonEinstein, "  (PAS Einstein-3D ✓)")
assert nonEinstein, "e^{2x}δ doit avoir un Ricci sans-trace non nul (non-Einstein)"
# σ̌ ∝ Ricci sans-trace ⟹ σ̌ ≠ 0 sur ce conforme-plat.
assert sp.simplify(trfree[0,0]-trfree[1,1]) != 0
print(" => Cotton=0 (conforme-plat) N'IMPLIQUE PAS Ricci sans-trace=0 (Einstein-3D).")
print("    Même « extended-WCH = Cotton→0 » laisse σ̌ ∝ (Ricci sans-trace) ≠ 0.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT (D1c3-2, testbed Bianchi A) :")
print("="*78)
print("   σ̌ = -4·(Ricci sans-trace de â)  ⟹  σ̌=0 ⟺ â Einstein-3D.")
print("   [R1] régularité-Friedrich/Tod (extension conforme lisse, donnée de bord libre)")
print("        ⊉ Einstein-3D : contre-exemple constructif (Tod §7, σ̌≠0 pour â squashé).")
print("   [R2] « extended-WCH = Cotton→0 » ⊉ Einstein-3D : conforme-platitude est")
print("        STRICTEMENT plus faible (g=e^{2x}δ : Cotton=0 mais Ricci sans-trace≠0).")
print("   ⟹ AUCUNE condition de régularité NATURELLE/dérivable ne force â Einstein-3D.")
print("      La seule qui le ferait (Ricci sans-trace=0 imposé) ≥ postuler la courbure")
print("      constante = POSTULAT INDÉPENDANT (non dérivable de A4 : la WCH supprime le")
print("      Weyl 4D de cœur, pas la 3-géométrie de bord). [firewall FW-3]")
print("   ⟹ ISSUE = D1c3-c : A3 socle INDÉPENDANT (issue faible DÉFINITIVE pour la")
print("      régularité naturelle) ; D3-régularité NE SÉLECTIONNE PAS la prescription ;")
print("      la marée = donnée libre ⟹ D1 NON fermé par cette voie. Converge avec")
print("      LC-D-IRREDUCTIBILITE-MOYENS.")
print("")
print(" DISCIPLINE (§6.4) : ces `établi` valident L'ALGÈBRE (Cotton/Ricci exacts ;")
print("   contre-exemples explicites), JAMAIS une conclusion physique. {A4 ; A2★ ; N}")
print("   INCHANGÉ ; D1 non clos ; N non fixé (≡Λ) ; CCC non démontrée NI réfutée.")
print("="*78)
print("EXIT 0 (R1: σ̌∝ε², σ̌≠0 hors isotropie, raccord à 0 ; R2: Cotton=0 ∧ Ricci sans-trace≠0)")
