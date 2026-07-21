#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_bunchdavies.py — LC-RACCORD, plan §6 (LC-WORK-REPRISE-RACCORD).
Test de la PROCHAINE QUESTION DURE :
    « L'hypothèse de Weyl (D3 : C->0 au crossover) <=> l'état de Bunch-Davies ? »
sur une perturbation tensorielle (TT) de de Sitter — un mode de graviton.

maj: v1.1 — §5 : le lien « Weyl rescalé électrique = g₃ » n'est plus IMPORTÉ de LC-A
     mais DÉRIVÉ explicitement sur le mode (Riemann linéarisé -> Weyl -> partie
     électrique -> rescaling à 𝓘⁺). Résultat : E_ij = (d/2H) g₃_ij, avec annulation
     explicite des pièces locales g₀ (eta^0) et g₂ (eta^2). v1.0 : import depuis LC-A.

Cadre. dS4 planaire (conforme), temps conforme eta in (-inf, 0^-), 𝓘⁺ en eta->0^-.
  ds² = (1/(H²eta²))(-deta² + (delta_ij + h_ij) dx^i dx^j),  a(eta) = -1/(H eta).
  Frame conforme : ĝ = a^{-2} g = (eta_Mink + H_munu) ;  Omega = 1/a = -H eta.
Perturbation TT : h_ij(eta,x) = A eps_ij f(eta) e^{i k.x},  eps transverse-sans-trace.

Étapes (cf. §6) :
  1. Mode de Bunch-Davies f(eta) = (1 + i k eta) e^{-i k eta} : solution de l'EOM TT de dS.
  2. g₃ dans l'état BD : expansion FG près de 𝓘⁺ (eta->0), coefficient en eta³ = g₃ = ⟨T⟩.
  3. Décomposition local/libre : g₂ (Schouten, local) vs g₃ (radiatif, non-local).
  4. dS/CFT : Δ=d=3, ⟨T T⟩ ~ k³, comptage TT = 2.
  5. Weyl DÉRIVÉ : E_ij (Weyl électrique rescalé à 𝓘⁺) = (d/2H) g₃_ij ; g₀,g₂ annulés.
     => « C->0 au crossover »  <=>  « g₃ -> 0 ».
  6. Le test : g₃(C->0) vs g₃(BD) — coïncidence un-point / résidu deux-points.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs (vérifiées) : Bunch-Davies, Proc. R. Soc. A 360, 117 (1978) ; de Haro-Skenderis-
Solodukhin, CMP 217, 595 (2001) ; Strominger hep-th/0106113 ; Maldacena astro-ph/0210603.
"""

import sympy as sp

eta, k, H, A = sp.symbols('eta k H A', positive=True)
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
I = sp.I

print("="*72)
print(" verif_D3_bunchdavies.py — D3 (C->0) <=> Bunch-Davies, sur un mode TT de dS4")
print("="*72)

# ----------------------------------------------------------------------
# [1] Mode de Bunch-Davies : solution de l'équation TT de de Sitter.
#     EOM du mode tensoriel (métrique, non rescalé) : f'' - (2/eta) f' + k² f = 0.
# ----------------------------------------------------------------------
f = A*(1 + I*k*eta)*sp.exp(-I*k*eta)
EOM = sp.simplify(sp.diff(f, eta, 2) - (2/eta)*sp.diff(f, eta) + k**2*f)
print("\n[1] Mode BD  f(eta) = A (1 + i k eta) e^{-i k eta}")
print("    EOM TT de dS  f'' - (2/eta) f' + k² f  =", EOM, " -> BD est bien solution.")
assert EOM == 0

# ----------------------------------------------------------------------
# [2] Expansion de Fefferman-Graham près de 𝓘⁺ (eta -> 0^-).
# ----------------------------------------------------------------------
ser = sp.expand(sp.series(f, eta, 0, 5).removeO())
c0, c1, c2, c3 = (ser.coeff(eta, n) for n in (0, 1, 2, 3))
print("\n[2] Expansion FG  f(eta) =", ser)
print("    eta^0 :", c0, "  (g₍₀₎=source) | eta^1 :", c1, " | eta^2 :", c2,
      " (g₍₂₎=local) | eta^3 :", c3, " (g₍₃₎=⟨T⟩ libre)")
assert c1 == 0

# ----------------------------------------------------------------------
# [3] Identification FG + décomposition local / libre.
# ----------------------------------------------------------------------
g0, g2, g3 = c0, c2, c3
rel = sp.simplify(g3 - (-(I*sp.Rational(1,3))*k**3*g0))
print("\n[3] g₍₀₎ =", g0, " ; g₍₂₎ =", g2, " ; g₍₃₎ =", g3)
print("    Relation d'état (BD) :  g₃ = -(i/3) k³ g₀  ->  vérif =", rel)
assert rel == 0
print("    g₂/g₀ =", sp.simplify(g2/g0), " (polynôme => LOCAL, Schouten du fond)")
print("    g₃/g₀ =", sp.simplify(g3/g0), " (k³=k²·|k|, non polynôme => NON LOCAL, libre)")
print("    [check Schouten d=3] g₂ = (1/2)k² g₀ ?",
      sp.simplify(g2 - sp.Rational(1,2)*k**2*g0) == 0)

# ----------------------------------------------------------------------
# [4] dS/CFT : dimension de l'opérateur de bord et scaling 2-points.
# ----------------------------------------------------------------------
d, Delta = 3, 3
print("\n[4] dS/CFT (bord d=3) : T_ij, Δ =", Delta, " -> ⟨T T⟩(k) ~ k^{2Δ-d} = k^",
      2*Delta - d, " (cohérent g₃ ∝ k³).")
ncomp = d*(d+1)//2 - 1 - d
print("    Comptage TT (d=3) :", d*(d+1)//2, "- 1 -", d, "=", ncomp, "polarisations.")
assert ncomp == 2

# ----------------------------------------------------------------------
# [5] WEYL — DÉRIVÉ EXPLICITEMENT sur le mode (plus d'import depuis LC-A).
# ----------------------------------------------------------------------
print("\n[5] Weyl électrique du mode TT — dérivation explicite :")

# (a) Fond : dS planaire pure est conformément plate -> Weyl de fond = 0.
coords_b = [eta, x1, x2, x3]
a_dS = -1/(H*eta)
gb = sp.diag(-a_dS**2, a_dS**2, a_dS**2, a_dS**2)
gbi = gb.inv()
def Chr_b(l,i,j):
    return sum(sp.Rational(1,2)*gbi[l,m]*(sp.diff(gb[m,i],coords_b[j])
            + sp.diff(gb[m,j],coords_b[i]) - sp.diff(gb[i,j],coords_b[m])) for m in range(4))
Gb = [[[Chr_b(l,i,j) for j in range(4)] for i in range(4)] for l in range(4)]
def Rie_b(l,i,j,kk):
    return sp.simplify(sp.diff(Gb[l][i][kk],coords_b[j]) - sp.diff(Gb[l][i][j],coords_b[kk])
        + sum(Gb[l][j][m]*Gb[m][i][kk] - Gb[l][kk][m]*Gb[m][i][j] for m in range(4)))
Ricb = sp.Matrix(4,4, lambda i,j: sp.simplify(sum(Rie_b(l,i,l,j) for l in range(4))))
Rsb = sp.simplify(sum(gbi[i,j]*Ricb[i,j] for i in range(4) for j in range(4)))
Cb_0101 = sp.simplify(sum(gb[0,l]*Rie_b(l,1,0,1) for l in range(4))
    - sp.Rational(1,2)*(gb[0,0]*Ricb[1,1]-gb[0,1]*Ricb[1,0]-gb[1,0]*Ricb[0,1]+gb[1,1]*Ricb[0,0])
    + sp.Rational(1,6)*Rsb*(gb[0,0]*gb[1,1]-gb[0,1]*gb[1,0]))
print("    (a) dS planaire pure : R =", sp.simplify(Rsb), " (=4Λ) ; Weyl C_{0101} =",
      Cb_0101, "-> conformément plate (Weyl de fond = 0).")
assert Cb_0101 == 0

# (b) Perturbation TT (k le long de x3, polarisation "+"), Riemann LINÉARISÉ exact.
eta_M = sp.diag(-1,1,1,1)                 # fond (frame conforme = Minkowski)
P = A*f/A * sp.exp(I*k*x3)                # f/A = profil ; P = profil de mode (H_11)
Hm = sp.zeros(4,4); Hm[1,1] = P; Hm[2,2] = -P   # TT : transverse à x3, sans trace
def dd(e,i,j): return sp.diff(e, coords_b[i], coords_b[j])
def R1(m,n,a,b):  # Riemann linéarisé (tout bas), fond Minkowski
    return sp.Rational(1,2)*(dd(Hm[m,b],n,a)+dd(Hm[n,a],m,b)-dd(Hm[m,a],n,b)-dd(Hm[n,b],m,a))
Ric1 = sp.Matrix(4,4, lambda m,n: sp.simplify(
        sum(eta_M[a,b]*R1(a,m,b,n) for a in range(4) for b in range(4))))
Rsc1 = sp.simplify(sum(eta_M[m,n]*Ric1[m,n] for m in range(4) for n in range(4)))
def W1(m,n,a,b):  # Weyl linéarisé (n=4), g-facteurs = fond Minkowski (R1 déjà O(A))
    g = eta_M
    return sp.simplify(R1(m,n,a,b)
        - sp.Rational(1,2)*(g[m,a]*Ric1[n,b]-g[m,b]*Ric1[n,a]-g[n,a]*Ric1[m,b]+g[n,b]*Ric1[m,a])
        + sp.Rational(1,6)*Rsc1*(g[m,a]*g[n,b]-g[m,b]*g[n,a]))
print("    (b) Mode TT : Ricci scalaire linéarisé R =", Rsc1, " (TT => 0).")
assert Rsc1 == 0

# Weyl électrique physique : E_ij = C^phys_{0i0j}(u^0_phys)² = Ĉ_{0i0j} (Omega s'annulent).
E11, E22 = W1(0,1,0,1), W1(0,2,0,2)
E12, E13, E33 = W1(0,1,0,2), W1(0,1,0,3), W1(0,3,0,3)
print("        Ĉ_{0101} =", E11)
print("        Ĉ_{0202} =", E22, " (= -Ĉ_{0101} : sans trace)")
print("        Ĉ_{0102}=", E12, " Ĉ_{0103}=", E13, " Ĉ_{0303}=", E33,
      " (hors-diag/longitudinal = 0 : E est TT, 2 polar.)")
assert E12 == 0 and E13 == 0 and E33 == 0 and sp.simplify(E11+E22) == 0

# E démarre à eta^1 : pièces locales g₀ (eta^0) et g₂ (eta^2) ANNULÉES.
serE = sp.series(E11, eta, 0, 4)
print("        Ĉ_{0101} en série eta :", serE)
print("        -> pas de eta^0 ni eta^2 : g₀ et g₂ sont annulés par l'opérateur de Weyl.")
assert sp.series(E11, eta, 0, 1).removeO() == 0   # pas de terme eta^0

# Weyl rescalé à 𝓘⁺ : E^resc = Ĉ_{0i0j}/Omega, Omega = -H eta, limite eta->0.
Omega = -H*eta
Eresc11 = sp.simplify(E11/Omega)
Eresc_scri = sp.simplify(sp.limit(Eresc11, eta, 0))
g3_11 = sp.expand(sp.series(P, eta, 0, 5).removeO()).coeff(eta, 3)   # g₃ composante 11
ratio = sp.simplify(Eresc_scri / g3_11)
print("        Weyl rescalé E^resc_{11} =", Eresc11)
print("        limite 𝓘⁺ (eta->0) :", Eresc_scri, "   ;   g₃_{11} =", sp.simplify(g3_11))
print("        >>> E^resc_{11}|𝓘⁺ / g₃_{11} =", ratio, " = d/(2H)  (const, indép. k,x).")
assert sp.simplify(ratio - sp.Rational(d,1)/(2*H)) == 0
print("    => DÉRIVÉ (non importé) : E_ij (Weyl électrique rescalé à 𝓘⁺) = (d/2H) g₃_ij.")
print("       Donc « C -> 0 au crossover »  <=>  « g₃ -> 0 ».")

# ----------------------------------------------------------------------
# [6] LE TEST : g₃(C->0)  vs  g₃(BD).
# ----------------------------------------------------------------------
print("\n" + "="*72)
print(" [6] LE TEST  —  D3 (C->0)  vs  état de Bunch-Davies")
print("="*72)
print("\n  g₃ imposé par D3 (C->0)            : 0")
print("  ⟨g₃⟩_BD  (un-point, classique)     : 0   <- vide dS-invariant, pas de condensat")
print("  ⟨g₃ g₃⟩_BD (deux-points, fluct.)   ~ k³   <- spectre conforme irréductible (Δ=3)")

print("\n  >>> UN-POINT  : ⟨g₃⟩_BD = 0 = g₃(C->0)   =>  COÏNCIDENCE.")
print("      Via [5], E_ij = (d/2H) g₃_ij : ⟨g₃⟩=0 <=> ⟨Weyl rescalé⟩=0 au Big Bang.")
print("      => D1 (fixe g₃), D3 (C->0) et [D] (état du bord) CONVERGENT :")
print("         « le nouvel éon naît dans le vide de Bunch-Davies ».")
print("\n  >>> DEUX-POINTS : ⟨g₃ g₃⟩_BD ~ k³ ≠ 0  =>  RÉSIDU IRRÉDUCTIBLE.")
print("      Aucun état non trivial n'annule les fluctuations : WCH = condition")
print("      UN-POINT (entropie, lecture thermodynamique de Penrose). Résidu k³ =")
print("      spectre primordial invariant d'échelle : contact avec [E]/CMB.")

print("\n" + "-"*72)
print(" VERDICT (perturbatif, formalisable) :")
print("   D3 (C->0)  <=>  Bunch-Davies   AU NIVEAU UN-POINT  : OUI (coïncidence).")
print("   Lien Weyl<->g₃ désormais DÉRIVÉ : E_ij = (d/2H) g₃_ij (d=3).")
print("   Caveat (décision ouverte jusqu'au non-linéaire) : état de RACCORDEMENT")
print("   (deux éons recollés) vs vide de bord ; dS/CFT non unitaire ;")
print("   fluctuations k³ irréductibles -> WCH = condition un-point, non stricte.")
print("-"*72)
