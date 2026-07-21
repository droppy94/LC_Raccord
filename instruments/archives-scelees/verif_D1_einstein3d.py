#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_einstein3d.py — LC-RACCORD / porte (i), POINT DYNAMIQUE RÉSIDUEL.
(Compagnon de LC-D3-CROSSOVER-ANISOTROPE §4. Étend verif_D1_bianchiA.py.)

QUESTION (§4 de LC-D3-CROSSOVER-ANISOTROPE). La marée future est σ̌ = -4·(Ricci sans-
trace de la 3-métrique â_ij de 𝓘) (Tod éq. 33), donc σ̌=0 ⟺ â_ij Einstein-3D ⟺ (en
dim. 3) courbure constante ⟺ isotrope. La question décisive du sort du pivot A3 est :

    UNE CONDITION DE RÉGULARITÉ DU CROSSOVER FORCE-T-ELLE â_ij À ÊTRE EINSTEIN-3D ?
      • si OUI  -> issue FORTE restaurée : A3 ⟸ A4 (régularité) ;
      • si NON  -> issue FAIBLE définitive : A3 est un postulat séparé.

MÉTHODE. On teste la HIÉRARCHIE des conditions naturelles, de la plus faible (celle que
Tod impose réellement) à la plus forte, sur la famille-test de 3-géométries de 𝓘
(Bianchi IX squashé, anisotropie ε) déjà utilisée en [B2] :

  [E1] YAMABE (courbure SCALAIRE constante) — la prescription RÉELLE de Tod. Une métrique
       homogène a une courbure scalaire constante POUR TOUT ε ; Yamabe fixe l'échelle φ₁,
       PAS la forme ε. Donc Yamabe NE force PAS Einstein-3D (l'écart scalaire-constant →
       Einstein-3D est exactement le Ricci sans-trace = l'anisotropie libre).
  [E2] WCH (Weyl nul AU bang, C=O(τ̃²)→0) — automatique dans la construction de Tod.
       Compatible avec â anisotrope : le Ricci sans-trace de 𝓘 ∝ α₁ (Tod éq. 26), et
       E_ij=O(τ̃²)→0 à τ̃=0 POUR TOUT α₁. WCH ne force pas α₁=0. NE force PAS Einstein-3D.
  [E3] Les conditions qui DONNENT Einstein-3D, et leur statut :
       (a) « fluide parfait après le bang » (σ̌=0) ⟺ Einstein-3D — mais = A3 (CIRCULAIRE) ;
       (b) WCH FORTE (C=o(τ̃²), α₁=0) ⟹ Einstein-3D — postulat EN PLUS, équivaut à A3 ;
       (c) C≡0 PARTOUT (conformément plat) ⟹ FRW — VACUEUX (tue toute onde grav. ; on le
           montre : pour Bianchi I vide, E≡0 ⟺ Kasner dégénéré (1,0,0) = plat).

VERDICT. Aucune condition PLUS FAIBLE que A3 ne force Einstein-3D. La condition Einstein-3D
est LOGIQUEMENT ÉQUIVALENTE à A3 (ou vacueuse). ⟹ ISSUE FAIBLE DÉFINITIVE au niveau d'un
crossover. La seule route restante vers l'isotropie est DYNAMIQUE INTER-ÉONS (la carte de
l'anisotropie d'éon en éon attire-t-elle vers ε=0 ?), au-delà des deux premiers ordres de
Tod — `à inventer`, NON clos ici.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs : Tod arXiv:1309.7248v2 (éq. 26, 33 ; Yamabe ; α₁) ; Anguige-Tod Ann.Phys.276 (1999)
(Weyl nul ⟹ FRW, fluide parfait) ; Milnor Adv.Math.21 (1976) ; Markwell-Stevens GRG 55
(2023) éq.(6)-(7) (la part sans-trace W̌_ab « has yet to obtain a physical interpretation »).
"""

import sympy as sp

print("="*78)
print(" verif_D1_einstein3d.py — la régularité du crossover force-t-elle â_ij Einstein-3D ?")
print("   (= σ̌=0 = isotropie = pivot A3). Test de la hiérarchie des conditions.")
print("="*78)

eps = sp.symbols('epsilon', real=True)

# 3-Ricci d'une métrique invariante à gauche (Milnor), Bianchi IX (n_i=1), facteurs A_i.
def milnor_ricci(A1, A2, A3, n1=1, n2=1, n3=1):
    l1=n1*A1/(A2*A3); l2=n2*A2/(A3*A1); l3=n3*A3/(A1*A2)
    s=sp.Rational(1,2)*(l1+l2+l3)
    return sp.Matrix([2*(s-l2)*(s-l3), 2*(s-l3)*(s-l1), 2*(s-l1)*(s-l2)])

# Famille-test de 𝓘 : (A1,A2,A3)=(e^ε, e^{-ε}, 1), volume gelé, α₀+β₀+γ₀=0.
Ric = milnor_ricci(sp.exp(eps), sp.exp(-eps), 1)
Rscal = sp.simplify(sum(Ric))                                   # courbure scalaire 3D
S = sp.Matrix([sp.simplify(Ric[i]-Rscal/3) for i in range(3)])  # Ricci sans-trace
normS2 = sp.simplify(sum(S[i]**2 for i in range(3)))

# ======================================================================
# [E1] YAMABE (courbure scalaire constante) — la prescription RÉELLE de Tod.
# ======================================================================
print("\n" + "-"*78)
print(" [E1] Yamabe (R scalaire constante) : satisfaite ∀ε -> NE sélectionne PAS ε=0")
print("-"*78)
print("   R^(3)(ε) =", sp.simplify(Rscal), "  (un NOMBRE : homogène ⟹ scalaire constant ∀ε)")
print("   R^(3)(0) =", Rscal.subs(eps,0), " >0 (S³ ronde légitime) ;  série :",
      sp.series(Rscal, eps, 0, 3))
# Échelle : sous a_ij -> φ₁² a_ij, R -> R/φ₁². Yamabe fixe φ₁ pour une cible, PAS ε.
phi1 = sp.symbols('phi1', positive=True)
print("   sous rescaling a->φ₁²a : R -> R/φ₁² -> Yamabe FIXE φ₁ (l'échelle), laisse ε LIBRE.")
print("   écart à Einstein-3D = Ricci sans-trace : |S|²(ε) =", sp.series(normS2,eps,0,4))
assert sp.series(normS2, eps, 0, 2).removeO() == 0      # nul à l'ordre 0 et 1
assert sp.simplify(normS2.subs(eps, sp.Rational(1,3))) != 0
print("   => Yamabe (R const) est SATISFAITE par toute la famille ε ; l'écart vers")
print("      Einstein-3D (|S|²=8ε²) reste LIBRE. La prescription de Tod NE force PAS l'isotropie.")

# ======================================================================
# [E2] WCH (Weyl nul AU bang) : compatible avec α₁ ≠ 0 (â anisotrope).
# ======================================================================
print("\n" + "-"*78)
print(" [E2] WCH (C=0 au bang, E=O(τ̃²)) : compatible avec â anisotrope -> ne force rien")
print("-"*78)
# Tod : α = α₀ + α₁ τ̃² + O(τ̃³) ; E_ij = O(τ̃²) ; R^I_ij - (1/3)s^I a_ij = -(H²/a₁²) α₁ (éq.26).
tau, a1, H, alpha1 = sp.symbols('tau_tilde a1 H alpha1', real=True)
E_leading = alpha1 * tau**2          # modèle du Weyl électrique près de 𝓘 (Tod : O(τ̃²))
tracefree_ricci_I = -(H**2/a1**2)*alpha1     # Tod éq. (26) : ∝ α₁
print("   E_ij(τ̃) ~ α₁·τ̃²  (Tod : E=O(τ̃²)) :")
print("     E_ij(0) =", E_leading.subs(tau,0), "  -> Weyl NUL au bang ∀α₁ (WCH satisfaite).")
print("     dE/dτ̃|₀ =", sp.diff(E_leading,tau).subs(tau,0), "  -> aussi nul ; C=O(τ̃²).")
print("   Ricci sans-trace de 𝓘 = -(H²/a₁²)·α₁ (Tod éq.26) =", tracefree_ricci_I)
assert E_leading.subs(tau,0) == 0                 # WCH : C=0 au bang ∀ α₁
assert sp.simplify(tracefree_ricci_I.subs(alpha1, 1)) != 0   # mais ≠0 si α₁≠0
print("   => WCH impose C=0 AU bang (τ̃=0), ce qui est vrai ∀α₁. Elle NE force PAS α₁=0,")
print("      donc NE force PAS le Ricci sans-trace de 𝓘 à s'annuler : â peut être anisotrope.")
print("      (Une WCH FORTE C=o(τ̃²) forcerait α₁=0 -> [E3b] : postulat EN PLUS.)")

# ======================================================================
# [E3] Les conditions qui DONNENT Einstein-3D — circulaires ou vacueuses.
# ======================================================================
print("\n" + "-"*78)
print(" [E3] Les conditions qui FORCENT Einstein-3D : circulaire (a,b) ou vacueuse (c)")
print("-"*78)

# (E3a) σ̌=0  ⟺  Einstein-3D  ⟺  fluide parfait post-bang  =  A3 (circulaire).
print("\n (E3a) « fluide parfait après le bang » (σ̌=0) :")
print("       Tod (33) : σ̌ = -4·(Ricci sans-trace) ; σ̌=0 ⟺ Ricci sans-trace=0 ⟺ Einstein-3D.")
print("       Or σ̌=0 EST l'hypothèse de fluide parfait (Anguige-Tod) = A3. CIRCULAIRE :")
print("       supposer le fluide parfait, c'est supposer l'isotropie qu'on veut dériver.")
# vérif d'équivalence sur la famille : σ̌=0 <=> ε=0 <=> Einstein-3D.
sigma2 = sp.simplify(16*normS2)
print("       sur la famille : σ̌=0 ⟺ |σ̌|²=", sp.series(sigma2,eps,0,4), "=0 ⟺ ε=0 ⟺ Einstein-3D ✓")

# (E3b) WCH forte C=o(τ̃²) => α₁=0 => Einstein-3D : postulat supplémentaire (= A3 aussi).
print("\n (E3b) WCH FORTE (C = o(τ̃²), i.e. α₁=0) :")
print("       force α₁=0 -> Ricci sans-trace=0 (Tod 26) -> Einstein-3D. MAIS c'est une")
print("       condition EN PLUS, non requise par la régularité de Tod (dont les solutions")
print("       régulières ont α₁≠0). Équivaut à imposer l'isotropie de 𝓘 = A3.")

# (E3c) C≡0 PARTOUT (conformément plat) => FRW : on le MONTRE (Bianchi I vide).
print("\n (E3c) C≡0 PARTOUT (conformément plat) : vacueux — tue toute onde gravitationnelle.")
t = sp.symbols('t', positive=True)
Xk = [t, *sp.symbols('x y z', real=True)]
def weyl_E_kasner(p1, p2, p3):
    g = sp.diag(-1, t**(2*p1), t**(2*p2), t**(2*p3)); n=4; gi=g.inv()
    G=[[[sp.simplify(sum(sp.Rational(1,2)*gi[l,m]*(sp.diff(g[m,i],Xk[j])+sp.diff(g[m,j],Xk[i])
        -sp.diff(g[i,j],Xk[m])) for m in range(n))) for j in range(n)] for i in range(n)] for l in range(n)]
    def Ru(a,b,c,d): return sp.simplify(sp.diff(G[a][d][b],Xk[c])-sp.diff(G[a][c][b],Xk[d])
        + sum(G[a][c][e]*G[e][d][b]-G[a][d][e]*G[e][c][b] for e in range(n)))
    Rl=lambda a,b,c,d: sp.simplify(sum(g[a,e]*Ru(e,b,c,d) for e in range(n)))
    Ric=sp.Matrix(n,n,lambda b,d: sp.simplify(sum(Ru(a,b,a,d) for a in range(n))))
    Rs=sp.simplify(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
    C0101=sp.simplify(Rl(0,1,0,1)
        - sp.Rational(1,2)*(g[0,0]*Ric[1,1]-g[0,1]*Ric[1,0]-g[1,0]*Ric[0,1]+g[1,1]*Ric[0,0])
        + sp.Rational(1,6)*Rs*(g[0,0]*g[1,1]-g[0,1]*g[1,0]))
    return sp.simplify(C0101/(-g[0,0]*g[1,1])), sp.simplify(Rs)   # E_xx orthonormal, R
# Kasner non trivial (2/3,2/3,-1/3) : vide mais Weyl ≠ 0.
Exx_k, R_k = weyl_E_kasner(sp.Rational(2,3), sp.Rational(2,3), sp.Rational(-1,3))
print("       Kasner (2/3,2/3,-1/3) : vide (R=", R_k, "), mais E_xx =", Exx_k, "≠0.")
assert R_k == 0 and Exx_k != 0
# Kasner dégénéré (1,0,0) : plat (Milne/Minkowski), Weyl = 0.
Exx_d, R_d = weyl_E_kasner(1, 0, 0)
print("       Kasner dégénéré (1,0,0) : E_xx =", Exx_d, " (plat) — seul cas vide Weyl-nul.")
assert Exx_d == 0
print("       => pour Bianchi I vide, C≡0 ⟺ exposants (1,0,0) = espace-temps PLAT. Imposer")
print("          C≡0 partout = imposer FRW/plat : VACUEUX comme principe de sélection.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT (point dynamique résiduel) — la régularité force-t-elle â Einstein-3D ?")
print("="*78)
print("   [E1] Yamabe (R scalaire const, la prescription RÉELLE de Tod) : satisfaite ∀ε.")
print("        L'écart vers Einstein-3D (|S|²=8ε²) reste LIBRE. -> ne force PAS l'isotropie.")
print("   [E2] WCH (C=0 au bang) : automatique ∀α₁ ; le Ricci sans-trace de 𝓘 ∝ α₁ survit.")
print("        -> ne force PAS l'isotropie.")
print("   [E3] Les seules conditions qui DONNENT Einstein-3D sont :")
print("        (a) fluide parfait post-bang (σ̌=0) = A3 -> CIRCULAIRE ;")
print("        (b) WCH forte C=o(τ̃²) (α₁=0) -> postulat EN PLUS, = A3 ;")
print("        (c) C≡0 partout -> FRW/plat -> VACUEUX (tue toute onde grav.).")
print("")
print("   ==> RÉPONSE : NON. Aucune condition de régularité PLUS FAIBLE que A3 ne force")
print("       â_ij à être Einstein-3D. La condition Einstein-3D est LOGIQUEMENT ÉQUIVALENTE")
print("       à A3 (ou vacueuse). L'ISSUE FAIBLE est DÉFINITIVE au niveau d'UN crossover :")
print("       A3 ne se réduit pas à A4 + régularité. C'est un postulat-socle indépendant.")
print("")
print(" CE QUI RESTE (la seule route non close vers l'isotropie) `[à inventer]` :")
print("   l'isotropisation DYNAMIQUE INTER-ÉONS — la carte ε_n ↦ ε_{n+1} de l'anisotropie")
print("   de 𝓘 d'éon en éon attire-t-elle vers ε=0 ? (analogue anisotrope du runaway (m,λ)")
print("   de l'atlas FLRW, porte ii). Cela exige de propager â À TRAVERS tout l'éon futur")
print("   jusqu'à son propre 𝓘 — au-delà des DEUX premiers ordres post-bang de Tod (éq.33).")
print("   NON calculable avec la machinerie actuelle : prochain chantier, hors de ce sceau.")
print("")
print(" DISCIPLINE D'AUDIT (§6.4) : cet `établi` valide L'ALGÈBRE (la hiérarchie des")
print("   conditions et leurs implications), JAMAIS « la physique de la CCC est établie ».")
print("="*78)
