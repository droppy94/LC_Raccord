#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_nonlin_cotton.py — LC-RACCORD. Sceau de la SOUS-QUESTION 1 du front
« généralisation NON-LINÉAIRE du verrouillage » : statut du secteur MAGNÉTIQUE
du Weyl rescalé au bord, en d=3.

CONTEXTE (faits importés, NON re-dérivés ici) :
  En 4D bulk / 3D bord asymptotiquement (A)dS (prolongé dS/CFT), le développement
  de Fefferman-Graham g_ij(z,x)=g0 + z^2 g2 + z^3 g3 + ... répartit le Weyl rescalé
  au bord en deux secteurs (dualité électrique/magnétique, de Haro ; Bakas-Skenderis ;
  Mansi-Petkou-Tagliabue) :
        E_ij  ∝  g3_ij  ∝  <T_ij>            (donnée d'ÉTAT — liberté résiduelle de D1)
        B_ij  ∝  C_ij[g0]  (Cotton-York)     (donnée GÉOMÉTRIQUE du bord)
  où le Cotton-York y^{ij}=eps^{ikl} ∇_k P_l^j (P = Schouten) est, EN d=3, la
  COURBURE CONFORME (remplace le Weyl, identiquement nul en 3D) : y=0 <=> g0 conf. plat.
  L'identification E ∝ g3 est déjà SCELLÉE en amont (verif_D3_bunchdavies.py,
  E_ij=(d/2H)g3). CE SCEAU NE LA REJOUE PAS ; il scelle le SECTEUR MAGNÉTIQUE.

CE QUE CE SCEAU ÉTABLIT (algèbre) :
  [A] Cotton-York d'une 3-métrique MAXIMALEMENT SYMÉTRIQUE (S^3, R^3, H^3) ≡ 0,
      exactement (les trois signes de courbure ; c'est la propriété de symétrie
      maximale, pas un artefact de signe).
  [B] => sous A3 (dS-invariance => fond maximalement symétrique => conf. plat en 3D),
      <B_ij> = 0 au UN-POINT, IDENTIQUEMENT, SANS argument de représentation :
      le secteur magnétique est clos par un fait géométrique plus fort.
  [C] Structure : sur une perturbation TT (non conf. plate) du plat, le Cotton-York
      linéarisé est NON NUL (=> le 0 de [A] est la conformément-platitude, pas un
      0 de codage) ET reste symétrique + sans trace + transverse (= objet TT,
      cohérent avec « B_ij = magnétique du Weyl » ; PAS de fuite de trace/singlet).

PORTÉE (discipline LC-AUDIT-VERDICT §6.4) :
  Un `établi` de sceau = « l'algèbre est correcte ET les faits reproduits », JAMAIS
  « la CCC est établie ». Ici, le résultat est :
    • UN-POINT / fond. Au 2e ordre <δC>~<δg δg> ≠ 0 = DEUX-POINT = résidu irréductible
      k^3 (SPECTRE-K3), HORS de la réduction un-point. Pas de fusion A3/A4.
    • SPÉCIFIQUE à d=3 (B = Cotton = courbure conforme).
    • CONDITIONNEL à A3 (fond dS-symétrique) ; ne dérive PAS A3 ; D1 NON clos.
  => le contenu un-point du Weyl COMPLET se réduit au seul secteur ÉLECTRIQUE
     E ∝ g3 (sous-questions 2-3, NON traitées ici).

Dépendances : sympy. Re-exécutable, sans réseau.
"""

import sympy as sp

N_ASSERT = 0


def check(cond, msg):
    global N_ASSERT
    assert cond, "ÉCHEC: " + msg
    N_ASSERT += 1
    print("   [PASS] " + msg)


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


def _perm(i, k, l):
    """Symbole de permutation [i,k,l] sur {0,1,2}."""
    seq = [i, k, l]
    if len(set(seq)) < 3:
        return 0
    sign = 1
    for a in range(3):
        for b in range(a + 1, 3):
            if seq[a] > seq[b]:
                sign = -sign
    return sign


def cotton_york(g, coords, simp=sp.simplify):
    """Tenseur de Cotton-York y^{ij} = eps^{ikl} ∇_k P_l^j d'une 3-métrique g(coords).
    P_ij = R_ij - (1/4) R g_ij  (Schouten en d=3). Retourne (y, ginv, R_scalar)."""
    n = 3
    ginv = g.inv()
    sqrtg = sp.sqrt(simp(g.det()))

    # Christoffel Gamma[k][i][j]
    Ga = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s = sp.S(0)
                for l in range(n):
                    s += ginv[k, l] * (sp.diff(g[l, j], coords[i])
                                       + sp.diff(g[l, i], coords[j])
                                       - sp.diff(g[i, j], coords[l]))
                Ga[k][i][j] = simp(s / 2)

    # Ricci R_ij
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            s = sp.S(0)
            for k in range(n):
                s += sp.diff(Ga[k][i][j], coords[k]) - sp.diff(Ga[k][i][k], coords[j])
                for l in range(n):
                    s += Ga[k][k][l] * Ga[l][i][j] - Ga[k][j][l] * Ga[l][i][k]
            Ric[i, j] = simp(s)

    Rsc = simp(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))

    # Schouten P_ij (d=3) puis mixte P_l^j = g^{jm} P_lm
    P = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            P[i, j] = simp(Ric[i, j] - sp.Rational(1, 4) * Rsc * g[i, j])
    Pmix = sp.zeros(n, n)
    for l in range(n):
        for j in range(n):
            Pmix[l, j] = simp(sum(ginv[j, m] * P[l, m] for m in range(n)))

    # ∇_k P_l^j = ∂_k P_l^j - Γ^m_kl P_m^j + Γ^j_km P_l^m
    def covd(k, l, j):
        s = sp.diff(Pmix[l, j], coords[k])
        for m in range(n):
            s += -Ga[m][k][l] * Pmix[m, j] + Ga[j][k][m] * Pmix[l, m]
        return s

    # y^{ij} = (1/sqrtg) Σ_{k,l} [i,k,l] ∇_k P_l^j
    y = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            s = sp.S(0)
            for k in range(n):
                for l in range(n):
                    p = _perm(i, k, l)
                    if p:
                        s += p * covd(k, l, j)
            y[i, j] = simp(s / sqrtg)
    return y, ginv, Rsc


def is_zero_matrix(M, simp=sp.simplify):
    return all(simp(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


print("=" * 72)
print(" verif_nonlin_cotton.py — secteur magnétique / Cotton-York en d=3")
print("=" * 72)

# ----------------------------------------------------------------------
banner("[A] Cotton-York des 3-métriques maximalement symétriques (= 0)")
# ----------------------------------------------------------------------

a = sp.symbols('a', positive=True)
chi, th, ph = sp.symbols('chi theta phi', real=True)

# S^3 (courbure +)
gS3 = sp.diag(a**2, a**2 * sp.sin(chi)**2, a**2 * sp.sin(chi)**2 * sp.sin(th)**2)
yS3, _, RS3 = cotton_york(gS3, [chi, th, ph], simp=lambda e: sp.simplify(sp.trigsimp(e)))
check(sp.simplify(RS3 - 6 / a**2) == 0, "S^3 : R = 6/a^2 (courbure constante, sanity)")
check(is_zero_matrix(yS3, simp=lambda e: sp.simplify(sp.trigsimp(e))),
      "S^3 (round) : Cotton-York y^{ij} ≡ 0  =>  conf. plat")

# R^3 plat (cartésien)
x, yc, z = sp.symbols('x y z', real=True)
gR3 = sp.eye(3)
yR3, _, RR3 = cotton_york(gR3, [x, yc, z])
check(sp.simplify(RR3) == 0, "R^3 : R = 0 (sanity)")
check(is_zero_matrix(yR3), "R^3 (plat) : Cotton-York y^{ij} ≡ 0")

# H^3 (courbure -)
gH3 = sp.diag(a**2, a**2 * sp.sinh(chi)**2, a**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
yH3, _, RH3 = cotton_york(gH3, [chi, th, ph], simp=lambda e: sp.simplify(sp.trigsimp(e)))
check(sp.simplify(RH3 + 6 / a**2) == 0, "H^3 : R = -6/a^2 (courbure constante, sanity)")
check(is_zero_matrix(yH3, simp=lambda e: sp.simplify(sp.trigsimp(e))),
      "H^3 (hyperbolique) : Cotton-York y^{ij} ≡ 0  =>  conf. plat (les deux signes)")

print("   => maximalement symétrique (A3 sur le fond) => Cotton-York = 0,")
print("      IDENTIQUEMENT, SANS argument de représentation. <B_ij> = 0 au un-point.")

# ----------------------------------------------------------------------
banner("[C] Non-trivialité + structure TT : perturbation TT du plat")
# ----------------------------------------------------------------------
# h_ij(z) TT : trace nulle (Axx + Ayy = A - A = 0), transverse (∂_i h_ij = 0 car
# dépendance en z seule et h_zj = 0). g = δ + ε h. On calcule le Cotton-York EXACT
# puis on extrait le terme linéaire en ε.

eps = sp.symbols('epsilon')
A = sp.Function('A')(z)
C = sp.Function('C')(z)
H = sp.Matrix([[A, C, 0], [C, -A, 0], [0, 0, 0]])      # TT : traceless + transverse
gpert = sp.eye(3) + eps * H

# transversalité et trace de h (sanity de la donnée)
check(sp.simplify(H[0, 0] + H[1, 1] + H[2, 2]) == 0, "perturbation h : sans trace (Tr h = 0)")
check(all(sp.simplify(sum(sp.diff(H[i, j], [x, yc, z][i]) for i in range(3))) == 0
          for j in range(3)), "perturbation h : transverse (∂_i h_ij = 0)")

ypert, ginv_p, _ = cotton_york(gpert, [x, yc, z], simp=sp.expand)
# terme linéaire en ε
ylin = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        ylin[i, j] = sp.simplify(sp.series(ypert[i, j], eps, 0, 2).removeO().coeff(eps, 1))

check(not is_zero_matrix(ylin),
      "Cotton-York linéarisé ≠ 0 sur la perturbation TT  =>  le 0 de [A] = conf.-platitude")
# composante explicite (forme ∝ dérivées 3e des amplitudes) : signature de non-trivialité
print("   y^{xx}_lin =", sp.simplify(ylin[0, 0]))
print("   y^{xy}_lin =", sp.simplify(ylin[0, 1]))

# Structure TT du Cotton-York linéarisé : symétrique + sans trace + transverse.
# (indices hauts ; métrique de fond = δ au 1er ordre)
check(all(sp.simplify(ylin[i, j] - ylin[j, i]) == 0 for i in range(3) for j in range(3)),
      "Cotton-York linéarisé : SYMÉTRIQUE (y^{ij} = y^{ji})")
check(sp.simplify(ylin[0, 0] + ylin[1, 1] + ylin[2, 2]) == 0,
      "Cotton-York linéarisé : SANS TRACE (δ_ij y^{ij} = 0)  =>  pas de fuite de singlet")
check(all(sp.simplify(sum(sp.diff(ylin[i, j], [x, yc, z][i]) for i in range(3))) == 0
          for j in range(3)),
      "Cotton-York linéarisé : TRANSVERSE (∂_i y^{ij} = 0)  =>  objet TT, = magnétique du Weyl")

# ----------------------------------------------------------------------
banner("[B] Conséquence — clôture du secteur magnétique (lecture)")
# ----------------------------------------------------------------------
print("""   E ∝ g3 ∝ <T>  : ÉTAT (résidu de D1 ; un-point tué par REPRÉSENTATION, sub-Q2/Q3).
   B ∝ Cotton[g0] : GÉOMÉTRIE ; sous A3 le fond est max. symétrique => conf. plat
                    => Cotton = 0 => <B> = 0 au un-point, IDENTIQUEMENT.
   => le contenu UN-POINT du Weyl COMPLET se réduit au SEUL secteur électrique.
      Le magnétique est clos EN AMONT, sans représentation. (sub-Q1 = PASS)""")

# ======================================================================
print("\n" + "=" * 72)
print(" RÉSULTAT : %d/%d ASSERTS PASSENT" % (N_ASSERT, N_ASSERT))
print("=" * 72)
print("""
 INTERPRÉTATION (discipline §6.4) :
   • SCELLÉ (algèbre) :
       [A] Cotton-York(S^3) = Cotton-York(R^3) = Cotton-York(H^3) = 0, exactement.
       [B] => sous A3, <B_ij> = 0 au un-point, IDENTIQUEMENT (géométrie > représentation).
       [C] Cotton-York linéarisé d'une perturbation TT : NON NUL, et symétrique +
           sans trace + transverse (objet TT = magnétique du Weyl ; pas de singlet).
   • EFFET : sub-Q1 PASS. Le contenu un-point du Weyl complet se réduit au secteur
       ÉLECTRIQUE E ∝ g3 (=> sub-Q2 : absence d'admixture de singlet dans g3 ;
       sub-Q3 : parité). Le magnétique n'a PAS besoin de l'argument de représentation.
   • NON SCELLÉ / portée : résultat UN-POINT (le 2e ordre <δC>~<δg δg> = deux-point k^3
       irréductible, SPECTRE-K3) ; spécifique d=3 (B = Cotton = courbure conforme) ;
       conditionnel à A3 ; D1 NON clos ; A3/A4 NON fusionnés tout court. PAS la CCC.
     « Le bang gagne » (P6 B) intact ; aucune touche à l'algèbre des chaînons amont.
""")
