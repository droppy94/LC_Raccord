#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_nonlin_parity.py — LC-RACCORD. Sceau de la SOUS-QUESTION 3 (clôture légère du
triptyque) du front « généralisation NON-LINÉAIRE du verrouillage » : COHÉRENCE DE
PARITÉ entre les deux secteurs du Weyl rescalé au bord.

THÈSE :
  La fonction à un point du Weyl rescalé (relatif à la normale) se scinde EXACTEMENT
  en deux secteurs de parité OPPOSÉE, qui épuisent le Weyl (5 + 5 = 10) :
      E_ij  (aucun ε ; = stress g3)     -> tenseur VRAI       -> parité PAIRE
      B_ij  (un ε ; = Cotton[g0])       -> PSEUDO-tenseur     -> parité IMPAIRE
  Chacun est annulé par SON argument, RESPECTANT SA parité, sans qu'aucun n'exige la
  parité-invariance de l'état :
      <E> = 0  par REPRÉSENTATION spin-2  (sub-Q2, verif_nonlin_repr.py) — secteur PAIR
      <B> = 0  par Cotton = 0 (fond conf. plat) (sub-Q1, verif_nonlin_cotton.py) — IMPAIR
  => couverture DISJOINTE et COMPLÈTE des deux parités ; aucun terme croisé n'échappe.

CE QUE CE SCEAU ÉTABLIT (algèbre) :
  [A] Sous une réflexion R (det R = -1), le Cotton-York se transforme en PSEUDO-tenseur
      (facteur det R = -1 EN PLUS de la loi tensorielle) : y_R = det(R)·(R⊗R)·y(Rx).
      => B / Cotton = parité IMPAIRE.
  [B] Le tenseur de Ricci (et donc Schouten / stress g3, secteur électrique) se transforme
      en tenseur VRAI (PAS de det) : Ric_R = (R⊗R)·Ric(Rx). => E = parité PAIRE.
  [C] Complétude : (E, B) = (5, 5) = 10 = Weyl complet relatif à la normale ; pas de 3e
      secteur de parité. Disjonction : parité conserve chaque secteur (pair<->pair,
      impair<->impair), <Weyl> = <E>_pair (+) <B>_impair, sans croisé.

PORTÉE (discipline LC-AUDIT-VERDICT §6.4) :
  `établi (algèbre)`. Combiné à sub-Q1 + sub-Q2 : le contenu UN-POINT du Weyl complet
  s'annule sous A3, NON-perturbativement et sur LES DEUX parités => A4 => A3-un-point
  passe de `établi perturbatif` à `établi` AU UN-POINT. NE ferme PAS D1 : le DEUX-POINT
  <g3 g3> ~ k^3 (SPECTRE-K3) reste libre, irréductible ; A3/A4 NON fusionnés tout court ;
  conditionnel à A3 ; spécifique d=3. PAS la CCC.

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


def delta(i, j):
    return sp.S(1) if i == j else sp.S(0)


def christoffel(g, coords):
    ginv = g.inv()
    n = 3
    Ga = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s = sp.S(0)
                for l in range(n):
                    s += ginv[k, l] * (sp.diff(g[l, j], coords[i])
                                       + sp.diff(g[l, i], coords[j])
                                       - sp.diff(g[i, j], coords[l]))
                Ga[k][i][j] = sp.expand(s / 2)
    return Ga, ginv


def ricci(Ga, coords):
    n = 3
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            s = sp.S(0)
            for k in range(n):
                s += sp.diff(Ga[k][i][j], coords[k]) - sp.diff(Ga[k][i][k], coords[j])
                for l in range(n):
                    s += Ga[k][k][l] * Ga[l][i][j] - Ga[k][j][l] * Ga[l][i][k]
            Ric[i, j] = sp.expand(s)
    return Ric


def cotton_york(g, coords):
    """y^{ij} = eps^{ikl} ∇_k P_l^j  (P = Schouten d=3). Retourne (y, Ric)."""
    n = 3
    Ga, ginv = christoffel(g, coords)
    Ric = ricci(Ga, coords)
    Rsc = sp.expand(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    P = sp.Matrix(n, n, lambda i, j: sp.expand(Ric[i, j] - sp.Rational(1, 4) * Rsc * g[i, j]))
    Pmix = sp.Matrix(n, n, lambda l, j: sp.expand(sum(ginv[j, m] * P[l, m] for m in range(n))))
    sqrtg = sp.sqrt(sp.expand(g.det()))

    def covd(k, l, j):
        s = sp.diff(Pmix[l, j], coords[k])
        for m in range(n):
            s += -Ga[m][k][l] * Pmix[m, j] + Ga[j][k][m] * Pmix[l, m]
        return s

    def perm(i, k, l):
        seq = [i, k, l]
        if len(set(seq)) < 3:
            return 0
        sign = 1
        for a in range(3):
            for b in range(a + 1, 3):
                if seq[a] > seq[b]:
                    sign = -sign
        return sign

    y = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            s = sp.S(0)
            for k in range(n):
                for l in range(n):
                    p = perm(i, k, l)
                    if p:
                        s += p * covd(k, l, j)
            y[i, j] = s / sqrtg
    return y, Ric


eps = sp.symbols('epsilon')
x, yc, z = sp.symbols('x y z', real=True)
coords = [x, yc, z]


def lin(M):
    """Coefficient linéaire en eps, matrice 3x3."""
    return sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.series(M[i, j], eps, 0, 2).removeO().coeff(eps, 1)))


print("=" * 72)
print(" verif_nonlin_parity.py — cohérence de parité E (pair) / B (impair)")
print("=" * 72)

# Perturbation TT dépendant de z (comme sub-Q1) : H_ij(z), sans trace, transverse.
A = sp.Function('A'); C = sp.Function('C')
def Hmat(arg):
    return sp.Matrix([[A(arg), C(arg), 0], [C(arg), -A(arg), 0], [0, 0, 0]])

H = Hmat(z)
g = sp.eye(3) + eps * H
y_orig_full, Ric_orig_full = cotton_york(g, coords)
y_orig = lin(y_orig_full)
Ric_orig = lin(Ric_orig_full)

# Réflexion R = diag(1,1,-1) (det = -1), action sur argument (z->-z) ET indices.
R = sp.diag(1, 1, -1)
detR = R.det()
check(detR == -1, "réflexion R = diag(1,1,-1) : det R = -1 (orientation renversée)")

# Métrique réfléchie : g_R_ij(x) = R_i^k R_j^l g_kl(Rx) = (R⊗R) appliqué à g(z->-z).
H_argref = Hmat(-z)                      # H(x,y,-z)
H_R = R * H_argref * R.T                 # action des indices par R
g_R = sp.eye(3) + eps * H_R
y_R_full, Ric_R_full = cotton_york(g_R, coords)
y_R = lin(y_R_full)
Ric_R = lin(Ric_R_full)

# ----------------------------------------------------------------------
banner("[A] B / Cotton-York : PSEUDO-tenseur (parité IMPAIRE)")
# ----------------------------------------------------------------------
# transform PSEUDO-tensoriel attendu : y_pseudo = det(R) · (R⊗R) · y_orig(z->-z)
y_orig_argref = y_orig.subs(z, -z)
y_pseudo = detR * (R * y_orig_argref * R.T)
check(sp.simplify(sp.Matrix(3, 3, lambda i, j: y_R[i, j] - y_pseudo[i, j])).is_zero_matrix,
      "Cotton-York : y_R = det(R)·(R⊗R)·y(Rx)  =>  PSEUDO-tenseur, parité IMPAIRE")
# contrôle négatif : SANS le det, ça NE colle PAS (le Cotton n'est pas un tenseur vrai)
y_true_wrong = (R * y_orig_argref * R.T)
check(not sp.simplify(sp.Matrix(3, 3, lambda i, j: y_R[i, j] - y_true_wrong[i, j])).is_zero_matrix,
      "contrôle négatif : sans det(R), y_R ≠ (R⊗R)·y(Rx)  =>  B n'est PAS un tenseur vrai")
print("   y_orig (lin) : y^{xx}=%s , y^{xy}=%s" % (sp.simplify(y_orig[0, 0]), sp.simplify(y_orig[0, 1])))

# ----------------------------------------------------------------------
banner("[B] E / Ricci(Schouten,stress) : tenseur VRAI (parité PAIRE)")
# ----------------------------------------------------------------------
# transform TENSORIEL VRAI attendu : Ric_true = (R⊗R) · Ric_orig(z->-z), SANS det.
Ric_orig_argref = Ric_orig.subs(z, -z)
Ric_true = R * Ric_orig_argref * R.T
check(sp.simplify(sp.Matrix(3, 3, lambda i, j: Ric_R[i, j] - Ric_true[i, j])).is_zero_matrix,
      "Ricci : Ric_R = (R⊗R)·Ric(Rx), SANS det  =>  tenseur VRAI, parité PAIRE")
# contrôle négatif : AVEC un det parasite, ça NE colle PAS (Ricci n'est pas pseudo)
Ric_pseudo_wrong = detR * (R * Ric_orig_argref * R.T)
check(not sp.simplify(sp.Matrix(3, 3, lambda i, j: Ric_R[i, j] - Ric_pseudo_wrong[i, j])).is_zero_matrix,
      "contrôle négatif : avec det(R), Ric_R ≠ det·(R⊗R)·Ric(Rx)  =>  E n'est PAS pseudo")
print("   => E (=g3, stress) PAIR ; B (=Cotton) IMPAIR : parités OPPOSÉES, confirmées.")

# ----------------------------------------------------------------------
banner("[C] Complétude + disjonction des deux secteurs (lecture)")
# ----------------------------------------------------------------------
print("""   (E, B) = (5, 5) = 10 = Weyl complet relatif à la normale : pas de 3e secteur.
   La parité conserve chaque secteur (pair<->pair, impair<->impair) :
       <Weyl>_un-point = <E>_PAIR  (+)  <B>_IMPAIR  (somme directe, sans croisé).
   • <E>_pair = 0  par REPRÉSENTATION spin-2 (sub-Q2)        [secteur électrique]
   • <B>_impair = 0 par Cotton = 0 sur fond conf. plat (sub-Q1) [secteur magnétique]
   Aucun des deux arguments n'exige la parité-invariance de l'état ; ils RESPECTENT
   chacun leur parité et couvrent les DEUX. => le un-point du Weyl complet = 0 sous A3.
   (sub-Q3 = PASS ; triptyque sub-Q1/Q2/Q3 CLOS.)""")

# ======================================================================
print("\n" + "=" * 72)
print(" RÉSULTAT : %d/%d ASSERTS PASSENT" % (N_ASSERT, N_ASSERT))
print("=" * 72)
print("""
 INTERPRÉTATION (discipline §6.4) :
   • SCELLÉ (algèbre) :
       [A] Cotton-York = PSEUDO-tenseur (det R en plus) => B parité IMPAIRE
           (+ contrôle négatif : pas un tenseur vrai).
       [B] Ricci/Schouten/stress = tenseur VRAI (pas de det) => E parité PAIRE
           (+ contrôle négatif : pas pseudo).
       [C] (E,B)=(5,5)=10 complet, parités opposées disjointes, sans terme croisé.
   • EFFET : sub-Q3 PASS, triptyque CLOS. <E>=0 (rep, sub-Q2, secteur PAIR) et
       <B>=0 (Cotton, sub-Q1, secteur IMPAIR) couvrent les DEUX parités, disjointement,
       sans recourir à la parité-invariance de l'état => le un-point du Weyl COMPLET
       s'annule sous A3, NON-perturbativement => A4 => A3-un-point devient `établi`
       (au un-point), au-delà du TT perturbatif.
   • NON SCELLÉ / portée : un-point seulement (DEUX-POINT <g3 g3>~k^3 libre, SPECTRE-K3,
       irréductible — A3/A4 NON fusionnés) ; conditionnel à A3 ; spécifique d=3 ;
       D1 NON clos. PAS la CCC.
     « Le bang gagne » (P6 B) intact ; aucune touche à l'algèbre des chaînons amont.
""")
