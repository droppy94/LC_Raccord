#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_bianchiA.py — LC-RACCORD / LC-AUDIT, PORTE (i). Atlas anisotrope (Bianchi A).
(Compagnon de LC-WORK-REPRISE-AUDIT §3. Étend verif_D1_stabilite.py [B],
 verif_D3_crossover_matching.py [S4] et verif_D3_backreaction.py [4]-[5].)

QUESTION (porte i). En FLRW le crossover donne 0↦0 (a1), car le fond isotrope
n'admet AUCUNE source TT (lemme [S4] : la projection TT de c·δ_ij est nulle). On
refait (a1)+(a2) sur un fond HOMOGÈNE ANISOTROPE (Bianchi A), où le cisaillement
σ_ij fournit une structure TT — exactement là où [S4] peut tomber :

    un passé sans marée propre (ĝ₃=0, Weyl→0 à 𝓘) mais avec une 3-géométrie de
    raccordement anisotrope est-il mappé en ǧ₃=0, ou le cisaillement INJECTE-t-il
    une marée future ǧ₃≠0 ?  (Et alors : A3 (isotropie de l'état) ⟸ A4 (WCH) ?)

MÉCANISME testé — ANCRÉ SUR TOD 2015 (arXiv:1309.7248v2, « The equations of CCC »,
qui traite explicitement « FRW and Class A Bianchi cosmologies »). Tod calcule, dans
son cas général anisotrope (sa §7), la matière post-bang : à l'ordre dominant c'est un
fluide de radiation isotrope (p=ρ/3), mais à l'ordre suivant apparaît un terme SANS
TRACE — un CISAILLEMENT — donné par son éq. (33) :

    σ̌_ij = -4 ( R^(ǎ)_ij - (1/3) R^(ǎ) ǎ_ij )  ~  -4 ( R^(â)_ij - (1/3) R^(â) â_ij ),

c.-à-d. : la marée de l'éon futur est SOURCÉE par le tenseur de Ricci SANS TRACE de
la 3-géométrie â_ij de 𝓘. Donc :
  • 𝓘 isotrope (courbure constante 3D = Einstein)  ⟹ Ricci sans-trace = 0 ⟹ σ̌=0  (on
    RETROUVE [S4] : 0↦0) ;
  • 𝓘 anisotrope (Bianchi A, exposants distincts)   ⟹ Ricci sans-trace ≠ 0 ⟹ σ̌≠0  (le
    LEMME [S4] TOMBE : 0↦≠0).

Sceaux :
  [B1] Weyl du fond anisotrope ≠ 0, sourcé par le cisaillement (contraste FLRW≡0) :
       (a) Kasner (Bianchi I vide) : C_txtx = 2/(9 t^{2/3}) ≠ 0 — RETROUVE verif_D1_
           stabilite [B] ; part électrique E_ij traceless non nulle (= marée de cisaill.) ;
       (b) formules de Tod (21)-(22) : Bianchi I → E≠0, B=0 ; Bianchi IX → B≠0 (part
           MAGNÉTIQUE du Weyl, absente en FLRW).
  [B2] Carte ĝ₃↦ǧ₃ anisotrope (LE cœur) : Ricci sans-trace de la 3-géométrie de 𝓘
       (Bianchi IX squashé, anisotropie ε ; Ricci par formule de Milnor, auto-vérifiée
       Einstein à ε=0), puis σ̌(ε) via Tod (33). Verdict : σ̌→0 quand ε→0 (raccord [S4]),
       σ̌≠0 sinon ⟹ [S4] tombe, 0↦≠0.
  [B3] Back-réaction sur état non dS-invariant : ⟨k̂k̂⟩ remplacé par une moyenne pondérée
       par une anisotropie quadrupolaire ε (P₂) ; part traceless ≠ 0 ⟹ ⟨g₃^(2)⟩(ε) ≠ 0,
       →0 quand ε→0. (Lève la réserve de verif_D3_backreaction l.144-146.)

VERDICT §3.4 (A3 ⟸ A4 ?) : le mécanisme est ÉTABLI (algèbre) — la marée future est
sourcée par le Ricci sans-trace de 𝓘, objet de 3-géométrie INTRINSÈQUE, indépendant du
Weyl de cœur que WCH supprime. La rigidité d'Anguige-Tod (« Weyl nul au bang ⟹ FRW »,
citée par Tod en intro) ne vaut QUE pour un fluide parfait ; or la matière post-bang CCC
n'est PAS un fluide parfait (elle porte σ̌). De plus le no-hair de Starobinsky (Λ-
domination) tue le cisaillement CINÉTIQUE (α̇,β̇,γ̇→0) mais pas la courbure-anisotropie
GELÉE de la métrique rescalée de 𝓘. ⟹ penche vers l'ISSUE FAIBLE/NEUTRE : A3 n'est PAS
automatiquement entraînée par A4 ; consigné honnêtement comme le point ouvert précis.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs : Tod, arXiv:1309.7248v2 = GRG 47, 17 (2015) — éq. (18),(21),(22),(33), prescription
Bianchi A ; Markwell-Stevens GRG 55, 93 (2023) — atlas FLRW (KB) ; Milnor, Adv. Math. 21
(1976) — courbures des métriques invariantes à gauche ; Starobinsky, JETP Lett. 37 (1983)
— isotropisation (no-hair) ; Anguige-Tod, Ann. Phys. 276 (1999) — Weyl nul ⟹ FRW (fluide).
"""

import sympy as sp

print("="*78)
print(" verif_D1_bianchiA.py — PORTE (i) : atlas anisotrope (Bianchi A)")
print("   le cisaillement de 𝓘 injecte-t-il une marée future ? (le lemme [S4] tombe-t-il ?)")
print("="*78)

# ======================================================================
# Machinerie : Weyl (0,4) complet, n=4 (reprise de verif_D3_crossover_matching).
# ======================================================================
def weyl_04(g, X):
    n = len(X); gi = g.inv()
    G = [[[sp.simplify(sum(sp.Rational(1,2)*gi[l,m]*(sp.diff(g[m,i],X[j])
          + sp.diff(g[m,j],X[i]) - sp.diff(g[i,j],X[m])) for m in range(n)))
          for j in range(n)] for i in range(n)] for l in range(n)]
    def Ru(a,b,c,d):
        return sp.simplify(sp.diff(G[a][d][b],X[c]) - sp.diff(G[a][c][b],X[d])
               + sum(G[a][c][e]*G[e][d][b] - G[a][d][e]*G[e][c][b] for e in range(n)))
    Rl = [[[[sp.simplify(sum(g[a,e]*Ru(e,b,c,d) for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n,n, lambda b,d: sp.simplify(sum(Ru(a,b,a,d) for a in range(n))))
    Rs = sp.simplify(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
    def Cl(a,b,c,d):
        return sp.simplify(Rl[a][b][c][d]
            - sp.Rational(1,2)*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])
            + sp.Rational(1,6)*Rs*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    return Cl, Ric, Rs

# ======================================================================
# [B1] Weyl du fond anisotrope ≠ 0, sourcé par le cisaillement.
# ======================================================================
print("\n" + "-"*78)
print(" [B1] Weyl du fond anisotrope : ≠ 0 et sourcé par le cisaillement (vs FLRW≡0)")
print("-"*78)

t = sp.symbols('t', positive=True)
Xk = [t, *sp.symbols('x y z', real=True)]

# (B1a) Kasner (Bianchi I vide), exposants (2/3,2/3,-1/3) — métrique du sceau [B].
gK = sp.diag(-1, t**sp.Rational(4,3), t**sp.Rational(4,3), t**sp.Rational(-2,3))
Cl, RicK, RsK = weyl_04(gK, Xk)
Ctxtx = Cl(0,1,0,1)
print("\n (B1a) Kasner (2/3,2/3,-1/3), vide :  Ric scalaire =", sp.simplify(RsK),
      " (vide ✓)")
print("       C_txtx =", sp.simplify(Ctxtx), "  -> RETROUVE verif_D1_stabilite [B] (≠0).")
assert sp.simplify(Ctxtx - sp.Rational(2,9)*t**sp.Rational(-2,3)) == 0

# Part électrique orthonormale E_ii = C_{0i0i}/(|g00| g_ii) (frame), i=1,2,3.
gii = [gK[i,i] for i in range(1,4)]
E = [sp.simplify(Cl(0,i,0,i)/(-gK[0,0]*gK[i,i])) for i in range(1,4)]
print("       E_xx,E_yy,E_zz (orthonormal) =", [sp.simplify(e) for e in E])
print("       trace E =", sp.simplify(sum(E)), " (sans trace : marée pure de cisaillement)")
assert sp.simplify(sum(E)) == 0
assert sp.simplify(E[0]) != 0
print("       => E_ij ≠ 0, traceless : le Weyl est une MARÉE sourcée par l'anisotropie.")

# (B1b) Formules de Tod (21)-(22) : décomposition électrique/magnétique générale.
print("\n (B1b) Formules de Tod (21)-(22) — parts électrique/magnétique du Weyl :")
Rt, ad, bd, gd = sp.symbols('Rdot adot bdot gdot', real=True)   # Ṙ, α̇, β̇, γ̇
Rr = sp.symbols('R', positive=True)
A, B, C = sp.symbols('A B C', real=True)   # A=(-n1 e^2α+n2 e^2β+n3 e^2γ)/2R, cycl.
# α̇+β̇+γ̇=0 (cisaillement sans trace) ; impose γ̇ = -α̇-β̇.
sub_tracefree = {gd: -ad-bd}
E11_tod = (-Rt*ad/Rr
           + sp.Rational(1,3)*(2*bd*gd - gd*ad - ad*bd - 4*B*C + 2*C*A + 2*A*B))
B11_tod = ad*(B+C) - bd*C - gd*B
E11_tod = sp.expand(E11_tod.subs(sub_tracefree))
B11_tod = sp.expand(B11_tod.subs(sub_tracefree))
# Bianchi I : n_i=0 => A=B=C=0.
E11_BI = sp.simplify(E11_tod.subs({A:0,B:0,C:0}))
B11_BI = sp.simplify(B11_tod.subs({A:0,B:0,C:0}))
print("   Bianchi I (A=B=C=0) :  E_11 =", E11_BI)
print("                          B_11 =", B11_BI, " (magnétique nul : Weyl purement électrique)")
assert B11_BI == 0 and E11_BI != 0
# Bianchi IX : n_i=1 => A,B,C génériques non nuls.
print("   Bianchi IX (A,B,C ≠ 0) : B_11 =", sp.simplify(B11_tod),
      "\n                            -> ≠ 0 génériquement : PART MAGNÉTIQUE (absente en FLRW).")
assert sp.simplify(B11_tod.subs({A:1,B:1,C:0,ad:1,bd:0})) != 0
print("   => [B1] établi : fond anisotrope ⟹ Weyl ≠ 0 (électrique + magnétique), sourcé")
print("      par le cisaillement. D3 a enfin un contenu, là où FLRW l'annulait (sceau [B]).")

# ======================================================================
# [B2] Carte ĝ₃↦ǧ₃ anisotrope — LE cœur (Tod éq. 33 + Ricci de Milnor).
# ======================================================================
print("\n" + "-"*78)
print(" [B2] Carte ĝ₃↦ǧ₃ : la marée future σ̌ = -4·(Ricci sans-trace de 𝓘)  [Tod éq.33]")
print("-"*78)

# 3-Ricci d'une métrique invariante à gauche (Milnor) pour Bianchi IX (n_i=1),
# facteurs d'échelle (A1,A2,A3). [e_i,e_j]=ε_ijk λ_k e_k, λ_k = n_k A_k/(A_i A_j).
def milnor_ricci(A1, A2, A3, n1=1, n2=1, n3=1):
    lam1 = n1*A1/(A2*A3); lam2 = n2*A2/(A3*A1); lam3 = n3*A3/(A1*A2)
    s = sp.Rational(1,2)*(lam1+lam2+lam3)
    mu1, mu2, mu3 = s-lam1, s-lam2, s-lam3
    # Ric(e_i,e_i) orthonormal :
    return sp.Matrix([2*mu2*mu3, 2*mu3*mu1, 2*mu1*mu2])

# Auto-vérification : sphère ronde (A1=A2=A3) => Einstein (Ricci ∝ δ, sans-trace=0).
a = sp.symbols('a', positive=True)
Rround = milnor_ricci(a, a, a)
print("\n auto-check ε=0 (S³ ronde, A1=A2=A3=a) : Ric =", list(Rround),
      " -> isotrope (Einstein) ✓")
assert sp.simplify(Rround[0]-Rround[1])==0 and sp.simplify(Rround[1]-Rround[2])==0

# 3-géométrie de 𝓘 anisotrope : (A1,A2,A3)=(e^ε, e^{-ε}, 1)  (volume gelé, α₀+β₀+γ₀=0).
eps = sp.symbols('epsilon', real=True)
Ric3 = milnor_ricci(sp.exp(eps), sp.exp(-eps), 1)
Rscal = sp.simplify(sum(Ric3))                       # courbure scalaire 3D
S = sp.Matrix([sp.simplify(Ric3[i] - Rscal/3) for i in range(3)])   # Ricci sans-trace
sigma = [sp.simplify(-4*S[i]) for i in range(3)]                    # Tod (33) : σ̌ = -4 S
normS2 = sp.simplify(sum(S[i]**2 for i in range(3)))
print(" 𝓘 anisotrope (A1,A2,A3)=(e^ε,e^{-ε},1)  [α₀=ε, β₀=-ε, γ₀=0, volume gelé] :")
ser = sp.series(16*normS2, eps, 0, 4)                # développement limité propre
print("   |σ̌|²(ε) = 16·|S|² =", ser, " -> ∝ ε² au voisinage de l'isotropie.")
assert sp.series(16*normS2, eps, 0, 2).removeO() == 0   # pas de terme constant ni linéaire

# Limites : ε→0 (raccord [S4]) vs ε≠0 ([S4] tombe).
print("\n   table  ε  ->  σ̌_ii = -4·(Ricci sans-trace de 𝓘)  et  |σ̌|² (marée injectée) :")
for ev in [sp.Integer(0), sp.Rational(1,10), sp.Rational(3,10), sp.Rational(1,2)]:
    sig = [float(sigma[i].subs(eps, ev)) for i in range(3)]
    val = float(16*normS2.subs(eps, ev))
    print(f"     ε={float(ev):+.2f}  σ̌=({sig[0]:+.4f},{sig[1]:+.4f},{sig[2]:+.4f})"
          f"   |σ̌|²={val:.5f}")
lim0 = sp.limit(16*normS2, eps, 0)
print("   lim_{ε→0} |σ̌|² =", lim0, "  -> RACCORD CONTINU au cas isotrope ([S4], 0↦0).")
assert lim0 == 0
assert sp.simplify(normS2.subs(eps, sp.Rational(1,2))) != 0
print("   => [B2] : 𝓘 isotrope (ε=0) ⟹ σ̌=0 (on retrouve [S4]) ; 𝓘 anisotrope (ε≠0) ⟹")
print("      σ̌≠0. Un passé SANS marée propre (ĝ₃=0, Weyl→0 à 𝓘) hérite d'une marée")
print("      FUTURE ǧ₃=σ̌≠0 : le LEMME [S4] TOMBE, la carte devient INHOMOGÈNE (0↦≠0).")

# ======================================================================
# [B3] Back-réaction sur état non dS-invariant : ⟨k̂k̂⟩ ≠ (1/3)δ.
# ======================================================================
print("\n" + "-"*78)
print(" [B3] Back-réaction (a2) sur état anisotrope : ⟨g₃^(2)⟩(ε) ≠ 0")
print("-"*78)

th, ph = sp.symbols('theta phi', real=True)
nhat = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
# état anisotrope : poids quadrupolaire w = 1 + ε P₂(cosθ) (plus bas multipôle traceless).
P2 = (3*sp.cos(th)**2 - 1)/2
w = 1 + eps*P2
def avg_w(expr):   # ⟨expr⟩ = ∫ expr·w dΩ / ∫ w dΩ
    num = sp.integrate(sp.integrate(expr*w*sp.sin(th), (ph,0,2*sp.pi)), (th,0,sp.pi))
    den = sp.integrate(sp.integrate(w*sp.sin(th),      (ph,0,2*sp.pi)), (th,0,sp.pi))
    return sp.simplify(num/den)

Kaniso = sp.Matrix(3,3, lambda i,j: avg_w(nhat[i]*nhat[j]))
Kaniso = sp.simplify(Kaniso)
print("\n ⟨k̂_i k̂_j⟩_ε =", Kaniso.tolist())
trK = sp.trace(Kaniso)
g3_2 = sp.simplify(Kaniso - trK/3*sp.eye(3))          # part traceless = ⟨g₃^(2)⟩ (∝)
print(" part traceless ⟨g₃^(2)⟩(ε) ∝", [sp.simplify(g3_2[i,i]) for i in range(3)],
      " (hors-diag 0)")
# isotropie à ε=0 ; anisotropie ≠0 sinon.
assert sp.simplify(g3_2.subs(eps,0)) == sp.zeros(3,3)
assert sp.simplify(g3_2.subs(eps,sp.Rational(1,2))) != sp.zeros(3,3)
print("\n   table  ε  ->  ⟨g₃^(2)⟩_zz(ε)  (composante traceless dominante) :")
for ev in [sp.Integer(0), sp.Rational(1,10), sp.Rational(3,10), sp.Rational(1,2)]:
    print(f"     ε = {float(ev):+.2f}   ⟨g₃^(2)⟩_zz = {sp.nsimplify(g3_2[2,2].subs(eps,ev))}"
          f"  ≈ {float(g3_2[2,2].subs(eps,ev)):+.4f}")
print("   lim_{ε→0} ⟨g₃^(2)⟩ = 0  -> raccord continu au cas dS-invariant d'(a2).")
print("   => [B3] : un état de raccordement anisotrope (⟨k̂k̂⟩≠⅓δ) DONNE ⟨g₃^(2)⟩≠0 :")
print("      la back-réaction injecte elle aussi une marée. (Lève la réserve l.144-146.)")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT (porte i) — fond/état ANISOTROPE, ancré sur Tod 2015 (1309.7248) :")
print("="*78)
print("   [B1] fond anisotrope ⟹ Weyl ≠ 0 (E + B), sourcé par le cisaillement σ_ij ;")
print("        D3 a un contenu, là où FLRW l'annule (contraste au sceau [B]).")
print("   [B2] Tod (33) : σ̌ = -4·(Ricci sans-trace de 𝓘). 𝓘 isotrope ⟹ σ̌=0 ([S4]) ;")
print("        𝓘 anisotrope ⟹ σ̌≠0. ĝ₃=0 ↦ ǧ₃≠0 : LE LEMME [S4] TOMBE (0↦≠0).")
print("   [B3] état anisotrope ⟹ ⟨g₃^(2)⟩≠0 : la back-réaction injecte aussi une marée.")
print("   ==> ISSUE (cf. §3.4) : c'est l'ISSUE FAIBLE/NEUTRE qui est exhibée —")
print("       l'anisotropie SOURCE une marée future ǧ₃≠0 ; le point fixe 0↦0 d'(a1) NE")
print("       SURVIT PAS hors isotropie. A3 n'est donc PAS une conséquence triviale.")
print("")
print(" A3 ⟸ A4 ? (le vrai enjeu) — verdict honnête `[décision ouverte]` :")
print("   • La marée future est sourcée par le Ricci SANS TRACE de la 3-géométrie de 𝓘,")
print("     objet INTRINSÈQUE (donnée libre â_ij de Friedrich), distinct du Weyl de cœur.")
print("   • WCH (A4) supprime le Weyl de cœur au bang ; mais la rigidité d'Anguige-Tod")
print("     « Weyl nul ⟹ FRW » ne vaut QUE pour fluide parfait — or la matière post-bang")
print("     CCC n'est PAS un fluide parfait (elle PORTE σ̌). La rigidité ne s'applique pas.")
print("   • Le no-hair de Starobinsky (Λ-domination) tue le cisaillement CINÉTIQUE")
print("     (α̇,β̇,γ̇→0) mais pas la courbure-anisotropie GELÉE du â_ij rescalé de 𝓘.")
print("   ⟹ A3 (isotropie de l'état de raccordement) n'est PAS entraînée automatiquement")
print("     par A4 (WCH). Réduction A3⟸A4 NON acquise : la CCC requiert un mécanisme")
print("     d'isotropisation du â_ij de 𝓘 (ou A3 reste un postulat séparé). Réfutation")
print("     partielle de la conjecture de consolidation, à consigner honnêtement.")
print("")
print(" DISCIPLINE D'AUDIT (LC-AUDIT-VERDICT §6.4) : ces `établi` valident L'ALGÈBRE")
print("   (le mécanisme de sourcing de Tod est exact, [S4] tombe quantitativement),")
print("   JAMAIS « la physique de la CCC est établie ». Le seul point qui RESTE ouvert")
print("   est dynamique : WCH/régularité force-t-il â_ij de 𝓘 à être Einstein 3D ?")
print("="*78)
