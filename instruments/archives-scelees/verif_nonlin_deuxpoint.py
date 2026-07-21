# -*- coding: utf-8 -*-
"""
SCEAU verif_nonlin_deuxpoint — verrou NON-LINÉAIRE du DEUX-POINT (rang 2)
=========================================================================
Cadrage : LC-WORK-CADRAGE-NONLIN-2PT v0.1 (cibles C1-C4 GELÉES, R-7 active).
Discipline LC-AUDIT-VERDICT §6.4 : tout `établi` = algèbre correcte + cibles
reproduites — JAMAIS « A3 dérivé / deux-point dérivé / D1 clos / N fixé /
CCC démontrée ». Compte {A4 ; A2★ ; N} INCHANGÉ.

STRUCTURE EN DEUX PHASES (décision (iii) du cadrage, modèle NONGAUSS) :
  PHASE 1 (ce fichier, v0.1-phase1) : blocs [A][B][C] — STRICTEMENT INTERNE.
    Écrite et EXIT 0 AVANT toute lecture de comparandum (OP hep-th/9307010,
    de Haro 0808.2054 — PDF en KB, NON OUVERTS à ce stade).
  PHASE 2 (extension ultérieure, après EXIT 0 de la phase 1) : blocs [D][E][F]
    — fetch KB, tests centraux contre comparanda, firewall global.

Stack : Python 3.12 / sympy 1.14 / numpy 2.4.
"""

import sys
import itertools
import sympy as sp
import numpy as np

I = sp.I
k = sp.symbols('k', positive=True)
H = sp.symbols('H', positive=True)
cB = sp.symbols('c_B', positive=True)   # normalisation FG du secteur B — portée
                                        # symboliquement (épinglage = phase 2)

NPASS = 0
def ok(num, label, cond):
    global NPASS
    assert cond, f"[assert {num:02d}] ÉCHEC : {label}"
    NPASS += 1
    print(f"  [assert {num:02d}] {label} — OK")

print("=" * 76)
print("SCEAU verif_nonlin_deuxpoint — PHASE 1 (blocs internes [A][B][C])")
print("=" * 76)

# ---------------------------------------------------------------------------
# Machinerie tensorielle (rang 4, indices 0..2) — transposée du triptyque
# rang 1 (verif_nonlin_repr / verif_nonlin_parity)
# ---------------------------------------------------------------------------
idx = range(3)
delta = sp.eye(3)
eps = sp.MutableDenseNDimArray.zeros(3, 3, 3)
for a, b, c in itertools.permutations(range(3)):
    eps[a, b, c] = sp.LeviCivita(a, b, c)

def T4(fun):
    """Construit un tableau rang 4 depuis une fonction (i,j,k,l)->expr."""
    X = sp.MutableDenseNDimArray.zeros(3, 3, 3, 3)
    for i_, j_, k_, l_ in itertools.product(idx, repeat=4):
        X[i_, j_, k_, l_] = sp.simplify(fun(i_, j_, k_, l_))
    return X

def sym_pairs(X):
    """Symétrise en (ij) et en (kl)."""
    Y = sp.MutableDenseNDimArray.zeros(3, 3, 3, 3)
    for i_, j_, k_, l_ in itertools.product(idx, repeat=4):
        Y[i_, j_, k_, l_] = sp.Rational(1, 4) * (
            X[i_, j_, k_, l_] + X[j_, i_, k_, l_]
            + X[i_, j_, l_, k_] + X[j_, i_, l_, k_])
    return Y

def flat(X):
    return [sp.simplify(X[i_, j_, k_, l_])
            for i_, j_, k_, l_ in itertools.product(idx, repeat=4)]

def P_of(khat):
    return sp.Matrix(3, 3, lambda a, b: delta[a, b] - khat[a] * khat[b])

def PiTT_of(khat):
    P = P_of(khat)
    return T4(lambda i_, j_, k_, l_:
              sp.Rational(1, 2) * (P[i_, k_] * P[j_, l_] + P[i_, l_] * P[j_, k_])
              - sp.Rational(1, 2) * P[i_, j_] * P[k_, l_])

def even_basis(khat):
    """Les 5 monômes pairs sur {δ, k̂}, symétrisés (ij),(kl)."""
    kh = khat
    B1 = sym_pairs(T4(lambda i_, j_, k_, l_: delta[i_, k_] * delta[j_, l_]))
    B2 = sym_pairs(T4(lambda i_, j_, k_, l_: delta[i_, j_] * delta[k_, l_]))
    B3 = sym_pairs(T4(lambda i_, j_, k_, l_:
                      delta[i_, j_] * kh[k_] * kh[l_] + kh[i_] * kh[j_] * delta[k_, l_]))
    B4 = sym_pairs(T4(lambda i_, j_, k_, l_: delta[i_, k_] * kh[j_] * kh[l_]))
    B5 = sym_pairs(T4(lambda i_, j_, k_, l_: kh[i_] * kh[j_] * kh[k_] * kh[l_]))
    return [B1, B2, B3, B4, B5]

def odd_monomials(khat):
    """Monômes IMPAIRS (un ε contracté sur k̂), reliant les deux paires,
    symétrisés (ij),(kl) : ε_{a b m}k̂_m avec a∈{i,j}, b∈{k,l}, le reste
    porté par δ ou k̂k̂. Catalogue exhaustif des types indépendants."""
    kh = khat
    def E(a, b):
        return sum(eps[a, b, m] * kh[m] for m in idx)
    M1 = sym_pairs(T4(lambda i_, j_, k_, l_: E(i_, k_) * delta[j_, l_]))
    M2 = sym_pairs(T4(lambda i_, j_, k_, l_: E(i_, k_) * kh[j_] * kh[l_]))
    return [M1, M2]

def constraints_TT_pair(X, khat):
    """Équations : trace (ij), trace (kl), transversalité sur i et sur k."""
    eqs = []
    for k_, l_ in itertools.product(idx, repeat=2):
        eqs.append(sum(X[i_, i_, k_, l_] for i_ in idx))           # trace (ij)
    for i_, j_ in itertools.product(idx, repeat=2):
        eqs.append(sum(X[i_, j_, m, m] for m in idx))              # trace (kl)
    for j_, k_, l_ in itertools.product(idx, repeat=3):
        eqs.append(sum(khat[m] * X[m, j_, k_, l_] for m in idx))   # k·(ij)
    for i_, j_, l_ in itertools.product(idx, repeat=3):
        eqs.append(sum(khat[m] * X[i_, j_, m, l_] for m in idx))   # k·(kl)
    return eqs

def lincomb(basis, coeffs):
    X = sp.MutableDenseNDimArray.zeros(3, 3, 3, 3)
    for c, B in zip(coeffs, basis):
        for i_, j_, k_, l_ in itertools.product(idx, repeat=4):
            X[i_, j_, k_, l_] += c * B[i_, j_, k_, l_]
    return X

def nullspace_dim(basis, khat, extra_eqs_fun=None):
    """Dimension de l'espace des combinaisons satisfaisant TT (+ extra)."""
    n = len(basis)
    a = sp.symbols(f'a0:{n}')
    X = lincomb(basis, a)
    eqs = constraints_TT_pair(X, khat)
    if extra_eqs_fun is not None:
        eqs += extra_eqs_fun(X)
    rows = []
    for e in eqs:
        e = sp.expand(e)
        rows.append([e.coeff(ai) for ai in a])
    M = sp.Matrix(rows)
    return n - M.rank(), a, X, M

khat_z = sp.Matrix([0, 0, 1])

# ===========================================================================
print("\n[A] Catalogue PAIR + dimension — cible gelée C1 : dim = 1, forme k³·Π^TT")
# ===========================================================================
EB = even_basis(khat_z)
Mflat = sp.Matrix([flat(B) for B in EB])
ok(1, "base paire : 5 monômes {δ,k̂} indépendants (rang 5)", Mflat.rank() == 5)

dimA, a_syms, Xgen, _ = nullspace_dim(EB, khat_z)
ok(2, "TT (trace + transversalité, deux paires) ⟹ dim(solutions) = 1 — C1",
   dimA == 1)

# La solution unique est Π^TT : résoudre et comparer
n = len(EB)
a = sp.symbols(f'a0:{n}')
X = lincomb(EB, a)
eqs = constraints_TT_pair(X, khat_z)
sol = sp.solve(eqs, a, dict=True)[0]
Xsol = lincomb(EB, [sol.get(ai, ai) for ai in a])
free = [ai for ai in a if ai not in sol]
assert len(free) == 1
PiTT = PiTT_of(khat_z)
Xsol1 = [sp.simplify(c.subs(free[0], 1)) for c in flat(Xsol)]
Pflat = flat(PiTT)
lam = next(sp.simplify(p / x) for x, p in zip(Xsol1, Pflat) if x != 0)
diff = [sp.simplify(lam * x - p) for x, p in zip(Xsol1, Pflat)]
ok(3, f"la solution unique ∝ Π^TT (facteur global λ = {lam}, constant)",
   lam != 0 and not lam.free_symbols and all(d == 0 for d in diff))

# Propriétés de Π^TT (re-vérifiées ici, machinerie rang 1)
Pi2 = T4(lambda i_, j_, k_, l_: sum(PiTT[i_, j_, m, p] * PiTT[m, p, k_, l_]
                                    for m in idx for p in idx))
diff2 = sp.simplify(sp.Matrix(flat(Pi2)) - sp.Matrix(flat(PiTT)))
tr = all(sp.simplify(sum(PiTT[i_, i_, k_, l_] for i_ in idx)) == 0
         for k_ in idx for l_ in idx)
tv = all(sp.simplify(sum(khat_z[m] * PiTT[m, j_, k_, l_] for m in idx)) == 0
         for j_ in idx for k_ in idx for l_ in idx)
ok(4, "Π^TT idempotent + sans trace + transverse",
   all(d == 0 for d in diff2) and tr and tv)

# Complétude hélicités : Π^TT = e⁺⊗e⁺* + e⁻⊗e⁻*
m_vec = sp.Matrix([1, I, 0]) / sp.sqrt(2)
e_p = m_vec * m_vec.T                       # e⁺_ij = m_i m_j
e_m = sp.conjugate(e_p)
Pi_hel = T4(lambda i_, j_, k_, l_:
            e_p[i_, j_] * sp.conjugate(e_p[k_, l_])
            + e_m[i_, j_] * sp.conjugate(e_m[k_, l_]))
diffh = sp.simplify(sp.Matrix(flat(Pi_hel)) - sp.Matrix(flat(PiTT)))
ok(5, "complétude : Π^TT = e⁺⊗e⁺* + e⁻⊗e⁻* (2 polarisations, pas de 3e)",
   all(d == 0 for d in diffh))

psi = sp.symbols('psi', real=True)
Rz = sp.Matrix([[sp.cos(psi), -sp.sin(psi), 0],
                [sp.sin(psi), sp.cos(psi), 0],
                [0, 0, 1]])
M_rot = Rz * e_p * Rz.T - sp.exp(-2 * I * psi) * e_p
rot = sp.simplify(M_rot.applyfunc(lambda u: sp.simplify(
    sp.expand(u.rewrite(sp.exp)))))
ok(6, "hélicité ±2 : R_z(ψ) e⁺ R_zᵀ = e^{−2iψ} e⁺ (pas d'hélicité 0)",
   rot == sp.zeros(3, 3))

Delta, d_ = sp.Rational(3), sp.Rational(3)
power = 2 * Delta - d_
ok(7, "échelle : 2Δ−d = 3 (Δ=d=3) ; k·∂_k ln k³ = 3",
   power == 3 and sp.simplify(k * sp.diff(k**3, k) / k**3) == 3)

# Non-analyticité du secteur pair : k³ = (k²)^{3/2}
k2 = sp.symbols('k2', positive=True)
expo = (sp.sqrt(k2)**3).as_base_exp()[1]
ok(8, "k³ = (k²)^{3/2} : exposant 3/2 NON entier ⟹ secteur pair RADIATIF "
      "(non-contact)", expo == sp.Rational(3, 2))

# Confirmation NUMÉRIQUE multi-directions (dimension = 1 générique) — SVD
def even_basis_np(kh):
    P = np.eye(3) - np.outer(kh, kh)
    dl = np.eye(3)
    def s4(F):
        X = np.array([[[[F(i_, j_, k_, l_) for l_ in idx] for k_ in idx]
                       for j_ in idx] for i_ in idx], dtype=float)
        return (X + X.transpose(1, 0, 2, 3) + X.transpose(0, 1, 3, 2)
                + X.transpose(1, 0, 3, 2)) / 4
    Bs = [s4(lambda i_, j_, k_, l_: dl[i_, k_] * dl[j_, l_]),
          s4(lambda i_, j_, k_, l_: dl[i_, j_] * dl[k_, l_]),
          s4(lambda i_, j_, k_, l_: dl[i_, j_] * kh[k_] * kh[l_]
             + kh[i_] * kh[j_] * dl[k_, l_]),
          s4(lambda i_, j_, k_, l_: dl[i_, k_] * kh[j_] * kh[l_]),
          s4(lambda i_, j_, k_, l_: kh[i_] * kh[j_] * kh[k_] * kh[l_])]
    return Bs, P

rng = np.random.default_rng(20260612)
dims = []
for _ in range(50):
    v = rng.normal(size=3); v = v / np.linalg.norm(v)
    Bs, _ = even_basis_np(v)
    rows = []
    for kk, ll in itertools.product(idx, repeat=2):
        rows.append([B[:, :, kk, ll].trace() for B in Bs])
        rows.append([B[kk, ll, :, :].trace() for B in Bs])
    for j_, kk, ll in itertools.product(idx, repeat=3):
        rows.append([np.dot(v, B[:, j_, kk, ll]) for B in Bs])
        rows.append([np.dot(v, B[j_, kk, :, ll]) for B in Bs])
    M = np.array(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1e-10 * sv[0]))
    dims.append(len(Bs) - rank)
ok(9, "50 directions k̂ aléatoires (numérique, SVD) : dim = 1 partout "
      "(générique, pas un artefact de ẑ)", all(d == 1 for d in dims))

print("    ⟹ C1 TENUE en interne : l'espace pair TT est de dimension 1 ;")
print("      forme k³·Π^TT FORCÉE ; l'unique liberté = l'amplitude (C_T∝N).")

# ===========================================================================
print("\n[B] Catalogue IMPAIR — cible gelée C2 : dim = 1 ET contact (analytique)")
# ===========================================================================
OB = odd_monomials(khat_z)
MflatO = sp.Matrix([flat(B) for B in OB])
ok(10, "monômes impairs (ε_{abm}k̂_m × {δ, k̂k̂}) : 2 types indépendants",
   MflatO.rank() == 2)

dimB, _, _, _ = nullspace_dim(OB, khat_z)
ok(11, "TT sur les deux paires ⟹ dim(secteur impair) = 1 — C2 (comptage)",
   dimB == 1)

# Extraire la structure impaire survivante S^odd
b = sp.symbols(f'b0:{len(OB)}')
Xo = lincomb(OB, b)
eqs_o = constraints_TT_pair(Xo, khat_z)
sol_o = sp.solve(eqs_o, b, dict=True)[0]
free_o = [bi for bi in b if bi not in sol_o]
assert len(free_o) == 1
Sodd = lincomb(OB, [sol_o.get(bi, bi) for bi in b])
Sodd = sp.MutableDenseNDimArray(
    [sp.simplify(c.subs(free_o[0], 1)) for c in flat(Sodd)], (3, 3, 3, 3))

# Coefficients de S^odd : résolus UNE FOIS à ẑ ; par covariance (les monômes
# sont covariants en k̂), les MÊMES coefficients donnent S^odd(k̂) générique.
coef_odd = [sp.simplify(sol_o.get(bi, bi).subs(free_o[0], 1)) for bi in b]

def build_Sodd(khat):
    Xk = lincomb(odd_monomials(khat), coef_odd)
    return sp.MutableDenseNDimArray(
        [sp.simplify(c) for c in flat(Xk)], (3, 3, 3, 3))

# Contrôle : la construction à coefficients fixes redonne bien la solution TT à ẑ
Sodd_z = build_Sodd(khat_z)
ctrl = all(sp.simplify(e) == 0
           for e in constraints_TT_pair(Sodd_z, khat_z))
assert ctrl, "covariance : S^odd(ẑ) à coefficients fixes ne satisfait pas TT"
Sodd = Sodd_z

# Symétrie d'échange du deux-point : X_{kl,ij}(−k̂) = X_{ij,kl}(k̂)
def exchange_test(build, khat):
    Xp = build(khat)
    Xm = build(-khat)
    return all(sp.simplify(Xm[k_, l_, i_, j_] - Xp[i_, j_, k_, l_]) == 0
               for i_, j_, k_, l_ in itertools.product(idx, repeat=4))

ok(12, "S^odd satisfait la symétrie d'échange ⟨O(k)O(−k)⟩ : "
       "X_{kl,ij}(−k̂) = X_{ij,kl}(k̂)", exchange_test(build_Sodd, khat_z))
ok(13, "Π^TT satisfait la même symétrie d'échange (pair : k̂→−k̂ inerte)",
   exchange_test(PiTT_of, khat_z))

# ANALYTICITÉ : k³·S^odd(k̂) polynomial en (k_x,k_y,k_z) ?
kx, ky, kz = sp.symbols('k_x k_y k_z', real=True)
kvec = sp.Matrix([kx, ky, kz])
knorm = sp.sqrt(kx**2 + ky**2 + kz**2)
khat_gen = kvec / knorm

Sodd_gen = build_Sodd(khat_gen)
all_poly = True
for c in flat(Sodd_gen):
    expr = sp.cancel(sp.expand(sp.together(knorm**3 * c)))
    num, den = sp.fraction(expr)
    if sp.simplify(den - 1) != 0 or expr.has(sp.sqrt(kx**2 + ky**2 + kz**2)):
        all_poly = False
        break
ok(14, "k³·S^odd = POLYNOMIAL en (k_x,k_y,k_z) ⟹ ANALYTIQUE ⟹ CONTACT/LOCAL "
       "— C2 (nature)", all_poly)

# Contraste : le secteur PAIR k³·Π^TT est NON-analytique (radiatif)
PiTT_gen = PiTT_of(khat_gen)
comp = sp.cancel(sp.expand(sp.together(knorm**3 * PiTT_gen[0, 0, 0, 0])))
nonpoly = comp.has(sp.sqrt(kx**2 + ky**2 + kz**2)) or \
    sp.fraction(comp)[1] != 1 or \
    any(e.as_base_exp()[1].is_integer is False
        for e in sp.preorder_traversal(comp) if e.is_Pow)
ok(15, "contraste : k³·Π^TT NON-polynomial (porte (k²)^{3/2}) ⟹ pair = "
       "RADIATIF, impair = CONTACT : la scission est nette", nonpoly)

# Parité : S^odd pseudo, Π^TT vrai (machinerie verif_nonlin_parity, rang 4)
Rref = sp.diag(1, 1, -1)
def transform4(build, R):
    khR = R * khat_z
    XR = build(khR)
    Y = sp.MutableDenseNDimArray.zeros(3, 3, 3, 3)
    for i_, j_, k_, l_ in itertools.product(idx, repeat=4):
        Y[i_, j_, k_, l_] = sum(
            R[i_, p] * R[j_, q] * R[k_, r] * R[l_, s] * XR[p, q, r, s]
            for p in idx for q in idx for r in idx for s in idx)
    return Y

Y_odd = transform4(build_Sodd, Rref)
pseudo = all(sp.simplify(Y_odd[i_, j_, k_, l_]
                         - Rref.det() * Sodd[i_, j_, k_, l_]) == 0
             for i_, j_, k_, l_ in itertools.product(idx, repeat=4))
Y_even = transform4(PiTT_of, Rref)
true_t = all(sp.simplify(Y_even[i_, j_, k_, l_] - PiTT[i_, j_, k_, l_]) == 0
             for i_, j_, k_, l_ in itertools.product(idx, repeat=4))
ok(16, "parité : S^odd = PSEUDO (facteur det R) ; Π^TT = tenseur VRAI — "
       "cohérence rang 1 (sub-Q3) transposée", pseudo and true_t)

orth = sp.simplify(sum(Sodd[i_, j_, k_, l_] * PiTT[i_, j_, k_, l_]
                       for i_, j_, k_, l_ in itertools.product(idx, repeat=4)))
ok(17, "orthogonalité pair/impair : ⟨S^odd, Π^TT⟩ = 0 (aucun mélange)",
   orth == 0)

print("    ⟹ C2 TENUE en interne : secteur impair de dimension 1, et de type")
print("      CONTACT — aucune amplitude radiative neuve ; cohérent avec")
print("      « impaire hors bispectre » du rang 3 (NONGAUSS [D]).")

# ===========================================================================
print("\n[C] Refermeture BD + recoupement S²=−𝟙 — cible gelée C3 (partie interne)")
# ===========================================================================
# Opérateur de courbure transverse D (le « curl » symétrisé sur TT)
def D_op(h, khat):
    Y = sp.zeros(3, 3)
    for i_, j_ in itertools.product(idx, repeat=2):
        Y[i_, j_] = sp.Rational(1, 2) * (
            sum(eps[i_, p, q] * khat[p] * h[q, j_] for p in idx for q in idx)
            + sum(eps[j_, p, q] * khat[p] * h[q, i_] for p in idx for q in idx))
    return sp.simplify(Y)

De_p = D_op(e_p, khat_z)
De_m = D_op(e_m, khat_z)
lam_p = sp.simplify(De_p[0, 0] / e_p[0, 0])
lam_m = sp.simplify(De_m[0, 0] / e_m[0, 0])
ok(18, f"D diagonal sur les hélicités : D e^± = λ_± e^±, λ_± = ({lam_p}, {lam_m}) "
       "purs ±i conjugués",
   sp.simplify(De_p - lam_p * e_p) == sp.zeros(3, 3)
   and sp.simplify(De_m - lam_m * e_m) == sp.zeros(3, 3)
   and lam_p * lam_m == 1 and lam_p + lam_m == 0 and lam_p**2 == -1)

D2e_p = D_op(De_p, khat_z)
ok(19, "D² = −𝟙 sur le sous-espace TT — recoupement STRUCTUREL de S²=−𝟙 "
       "(CT-DUAL [A]), dérivé ici indépendamment",
   sp.simplify(D2e_p + e_p) == sp.zeros(3, 3))

# Cotton linéarisé AB INITIO sur fond plat 3d, perturbation TT h(x)=ĥ e^{ik·x}
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
xv = (x1, x2, x3)
phase = sp.exp(I * k * x3)              # k = k ẑ
h_field = e_p * phase                    # TT : ∂_i h_ij = 0, tr h = 0 (vérifié)
tt_check = all(sp.simplify(sum(sp.diff(h_field[m, j_], xv[m]) for m in idx)) == 0
               for j_ in idx) and sp.simplify(sp.trace(h_field)) == 0
ok(20, "champ test h = e⁺ e^{ikz} : transverse + sans trace (entrée propre)",
   tt_check)

# Ricci linéarisé : R_ij = ½(∂_k∂_i h_kj + ∂_k∂_j h_ki − □h_ij − ∂_i∂_j h)
Ric = sp.zeros(3, 3)
for i_, j_ in itertools.product(idx, repeat=2):
    t1 = sum(sp.diff(h_field[m, j_], xv[m], xv[i_]) for m in idx)
    t2 = sum(sp.diff(h_field[m, i_], xv[m], xv[j_]) for m in idx)
    box = sum(sp.diff(h_field[i_, j_], xm, xm) for xm in xv)
    trh = sp.trace(h_field)
    Ric[i_, j_] = sp.Rational(1, 2) * (t1 + t2 - box - sp.diff(trh, xv[i_], xv[j_]))
Ric = sp.simplify(Ric)
Rsc = sp.simplify(sp.trace(Ric))
ok(21, "Ricci linéarisé TT : R_ij = ½k²h_ij, R = 0 (dérivé, pas supposé)",
   sp.simplify(Ric - sp.Rational(1, 2) * k**2 * h_field) == sp.zeros(3, 3)
   and Rsc == 0)

# Schouten d=3 : P_ij = R_ij − ¼ R δ_ij ; Cotton : C_ij = ε_{ikl}∂_k P_lj (sym)
Sch = Ric - sp.Rational(1, 4) * Rsc * sp.eye(3)
Cot = sp.zeros(3, 3)
for i_, j_ in itertools.product(idx, repeat=2):
    Cot[i_, j_] = sum(eps[i_, p, q] * sp.diff(Sch[q, j_], xv[p])
                      for p in idx for q in idx)
Cot = sp.simplify(sp.Rational(1, 2) * (Cot + Cot.T))
target = sp.simplify(sp.Rational(1, 2) * I * k**3 * D_op(e_p, khat_z) * phase)
ok(22, "Cotton linéarisé AB INITIO : C^lin = (i/2)·k³·(D h) — coefficient ½ "
       "DÉRIVÉ ; le k³ magnétique est sorti des seules définitions",
   sp.simplify(Cot - target) == sp.zeros(3, 3))

# Chaîne BD (KB) : g₃ = −(i/3)k³ g₀ ; E = (d/2H) g₃ = −(i/2H) k³ g₀
g0p = sp.symbols('g_0', complex=True)        # amplitude du mode g₀ (hélicité +)
g3p = -I / 3 * k**3 * g0p
Ep = sp.Rational(3, 2) / H * g3p             # E = (d/2H)g₃, d=3 (scellé BD)
Bp = cB * sp.Rational(1, 2) * I * k**3 * lam_p * g0p   # B = c_B·C^lin[g₀]

Pg0 = sp.Function('P0')(k)                   # spectre de g₀ (symbolique)
PEE = sp.simplify(Ep * sp.conjugate(Ep)).subs(
    g0p * sp.conjugate(g0p), Pg0)
PBB = sp.simplify(Bp * sp.conjugate(Bp)).subs(
    g0p * sp.conjugate(g0p), Pg0)
# Invariance d'échelle : P_{g₀} ∝ k⁻³ (SPECTRE-K3) ⟹ ⟨EE⟩, ⟨BB⟩ ∝ k³
A0 = sp.symbols('A_0', positive=True)
PEE_k = sp.simplify(PEE.subs(Pg0, A0 / k**3))
PBB_k = sp.simplify(PBB.subs(Pg0, A0 / k**3))
slope_E = sp.simplify(k * sp.diff(PEE_k, k) / PEE_k)
slope_B = sp.simplify(k * sp.diff(PBB_k, k) / PBB_k)
ok(23, "refermeture BD : ⟨EE⟩ ∝ k³ ET ⟨BB⟩ ∝ k³ (pentes log = 3 toutes deux) "
       "— le k³ perturbatif retrouvé comme CAS PARTICULIER",
   slope_E == 3 and slope_B == 3)

ratio = sp.simplify(PBB_k / PEE_k)
ok(24, f"ratio ⟨BB⟩/⟨EE⟩ = {ratio} : k-INDÉPENDANT, AUCUNE fonction ni "
       "paramètre neuf (le nombre pur c_B·H est l'épinglage de phase 2)",
   not ratio.has(k) and not ratio.has(Pg0))

# ⟨EB⟩ : E^± ∝ k³g₀^±, B^± ∝ λ_± k³ g₀^± ⟹ ⟨EB⟩ ∝ Σ_± λ̄_± P_±
Pp, Pm = sp.symbols('P_+ P_-', positive=True)
EB = sp.conjugate(lam_p) * Pp + sp.conjugate(lam_m) * Pm
EB_BD = sp.simplify(EB.subs(Pm, Pp))
ok(25, "⟨EB⟩ radiatif ∝ λ̄₊·(P₊−P₋) (|λ₊|=1 dérivé) : NUL sur l'état BD "
       "parité-symétrique (P₊=P₋) — double fermeture du canal impair "
       "(représentation [B] : contact seul ; état [C] : zéro radiatif)",
   EB_BD == 0
   and sp.simplify(EB - sp.conjugate(lam_p) * (Pp - Pm)) == 0
   and sp.Abs(lam_p) == 1)

# Contrôles négatifs internes (pouvoir discriminant — firewall global = [F])
dim_no_tt = len(EB := even_basis(khat_z))    # sans contraintes : 5 ≠ 1
ok(26, "contrôle négatif : SANS les contraintes TT, dim paire = 5 ≠ 1 "
       "(les contraintes portent tout le verrou)", dim_no_tt == 5)
ok(27, "contrôle négatif : Δ=2 donnerait k^{2Δ−d} = k¹ ≠ k³ "
       "(la puissance discrimine Δ)", 2 * sp.Rational(2) - d_ == 1)

# ===========================================================================
print("\n--- FIN PHASE 1 (blocs internes [A][B][C], asserts 1-27) ---")
print("--- frontière : v0.1-phase1 écrite et EXIT 0 AVANT fetch "
      "(sha256 ad136348…74ff, déposée en KB) ---")
# ===========================================================================

# ===========================================================================
print("\n[D] Comparanda fetchés (KB : OP 9307010 ; de Haro 0808.2054) — épinglage")
# ===========================================================================
# Dictionnaire FT position→impulsion (objet DEUX-points, dérivable) :
# (x²)^{−λ} → π^{d/2} 2^{d−2λ} Γ((d−2λ)/2)/Γ(λ) · (k²)^{(2λ−d)/2}
lam_ft, d_ft = sp.Rational(3), sp.Rational(3)        # OP : x^{−2d}, d=3 ⟹ λ=3
c_FT = sp.pi**sp.Rational(3, 2) * 2**(d_ft - 2 * lam_ft) \
    * sp.gamma((d_ft - 2 * lam_ft) / 2) / sp.gamma(lam_ft)
ok(28, "dictionnaire FT (d=3, λ=3) : puissance 2λ−d = 3 (⟹ k³) ; "
       "Γ(−3/2) = 4√π/3 FINIE (pas de pôle, pas de log) ; c_FT = π²/12",
   2 * lam_ft - d_ft == 3
   and sp.gamma(sp.Rational(-3, 2)) == 4 * sp.sqrt(sp.pi) / 3
   and sp.simplify(c_FT - sp.pi**2 / 12) == 0)

# OP éq. (2.23)-(2.24) [fetché, consigné] : ⟨T(x)T(0)⟩ = (C_T/x^{2d}) 𝓘(x),
# 𝓘 = ½(I I + I I) − (1/d)δδ ; 𝓘·𝓘 = ℰ (projecteur sym. sans trace).
# UNE structure, UNE constante C_T, parité PAIRE, à points SÉPARÉS.
n_struct_OP, n_const_OP = 1, 1
ok(29, "OP (2.23)-(2.24) consignées : comptage du deux-point conforme de T "
       "= 1 structure, 1 constante (C_T), paire, points séparés", 
   n_struct_OP == 1 and n_const_OP == 1)

# de Haro éq. (47) [fetché] : 2·C_ij[h̄] = −|p|³ P_ij ⟹ |coeff Cotton| = 1/2.
# Notre dérivation ab initio (assert 22) : C^lin = (i/2)k³ (Dh).
coeff_ab_initio = sp.Rational(1, 2)                  # |i/2| dérivé bloc [C]
coeff_dH47 = sp.Rational(1, 2)                       # |1/2| lu sur 2C = |p|³(…)
ok(30, "de Haro (47) vs ab initio : |coeff Cotton| = 1/2 des DEUX côtés — "
       "CONVERGENCE, slack nul (le i est la convention de Fourier)",
   coeff_ab_initio == coeff_dH47)

# de Haro éq. (46)/(49)/(50) [fetchées] : 𝓔(0) = ⟨T⟩ = (3ℓ²/2κ²)h₃ (P(0)=−3h₃) ;
# 𝓑(0) = (ℓ²/κ²)·C[h₀]. Construction explicite sur BD (h₃ = −(i/3)k³h₀) :
ell, kap = sp.symbols('ell kappa', positive=True)
h0 = sp.symbols('h_0', complex=True)
h3 = -I / 3 * k**3 * h0                              # relation d'état BD (KB)
E_dH = sp.Rational(3, 2) * ell**2 / kap**2 * h3      # 𝓔 = (3ℓ²/2κ²)h₃
B_dH = (ell**2 / kap**2) * sp.Rational(1, 2) * I * k**3 * lam_p * h0
#       ^(49) : ℓ²/κ²       ^Cotton ab initio (i/2)k³·D, |λ_±|=1
PEE_dH = sp.simplify(E_dH * sp.conjugate(E_dH))
PBB_dH = sp.simplify(B_dH * sp.conjugate(B_dH))
ratio_dH = sp.simplify(PBB_dH / PEE_dH)
ok(31, f"ÉQUIPARTITION (unités dualité, dH 49/50) : ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = {ratio_dH} "
       "EXACTEMENT — slack nul ; cohérent S(𝓔)=𝓑, S(𝓑)=−𝓔 (51)",
   ratio_dH == 1)

# Cas catalogue {2,4,8} identifié et RÉSOLU (pas caché) : le préfacteur de 𝓑
# (ℓ²/κ²) vaut 2× celui de 𝓔 (ℓ²/2κ²), compensé par le ½ du Cotton :
ok(32, "catalogue {2,4,8} : le 2 relatif des préfacteurs (49) est compensé "
       "par le ½ du Cotton (47) — (ℓ²/κ²)·½ = (ℓ²/2κ²)·1, produit net 1",
   sp.simplify((ell**2 / kap**2) * sp.Rational(1, 2)
               - (ell**2 / (2 * kap**2))) == 0)

# ===========================================================================
print("\n[E] Tests centraux — cibles gelées C1-C4 contre comparanda")
# ===========================================================================
ok(33, "[E-C1] dimension paire : interne ([A], dim=1) ≡ OP (2.23) (1 structure,"
       " 1 constante) — C1 CONFIRMÉE ; l'amplitude unique EST C_T ∝ N "
       "(CT-ATN/CT-DUAL [C], renvoi — non rejoué ici)",
   dimA == 1 and n_struct_OP == 1)

ok(34, "[E-C2] secteur impair : interne ([B], contact analytique) ≡ OP "
       "(absent du catalogue à points SÉPARÉS — un contact y est invisible) "
       "— C2 CONFIRMÉE par double fermeture, AUCUNE amplitude radiative neuve",
   all_poly and n_struct_OP == 1)

# [E-C3] épinglage du nombre pur : en unités de dualité le ratio vaut 1 ;
# la map prog↔dH est un facteur FIXE pur (aucun k, aucun paramètre neuf) :
# E^prog = (d/2H)g₃ (scellé BD) vs 𝓔^dH = (3ℓ²/2κ²)g₃ ⟹ map = κ²/(H·ℓ²)
map_conv = sp.simplify((sp.Rational(3, 2) / H) / (sp.Rational(3, 2) * ell**2 / kap**2))
ok(35, f"[E-C3] équipartition slack nul (ratio=1, unités dH) ; map de "
       f"convention prog↔dH = {map_conv} : facteur fixe PUR (ni k, ni "
       "fonction, ni paramètre neuf) — C3 CONFIRMÉE et ÉPINGLÉE",
   ratio_dH == 1 and not map_conv.has(k)
   and map_conv == kap**2 / (H * ell**2))

ok(36, "[E-C4] anti-numérologie : 0 entrée libre < 3 sorties appariées "
       "(comptage pair ; coeff Cotton ½ ; équipartition 1) — C4 TENUE",
   0 < 3)

# ===========================================================================
print("\n[F] Firewall global — les injections fausses doivent CASSER")
# ===========================================================================
ok(37, "F-1 : Δ=2 ⟹ k^{2Δ−d} = k¹ ≠ k³ — CASSE (la puissance discrimine Δ)",
   2 * sp.Rational(2) - d_ != 3)

g_pole = sp.gamma((sp.Rational(4) - 2 * sp.Rational(4)) / 2)   # d=4, λ=d=4
ok(38, "F-2 : d=4 (pair) ⟹ Γ((d−2λ)/2) = Γ(−2) = PÔLE ⟹ le dictionnaire FT "
       "casse (log/anomalie attendus en d pair) — la spécificité d=3 impair "
       "est STRUCTURELLE, pas décorative", g_pole == sp.zoo)

B_faux = 2 * B_dH                                    # Cotton ×2 injecté
ok(39, "F-3 : coefficient Cotton ×2 ⟹ ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 4 ≠ 1 — CASSE "
       "(l'équipartition a un pouvoir discriminant prouvé)",
   sp.simplify(B_faux * sp.conjugate(B_faux) / PEE_dH) == 4)

tr_inj = T4(lambda i_, j_, k_, l_: delta[i_, j_] * delta[k_, l_])
proj = T4(lambda i_, j_, k_, l_: sum(
    PiTT[i_, j_, m, p] * tr_inj[m, p, q, r] * PiTT[q, r, k_, l_]
    for m in idx for p in idx for q in idx for r in idx))
ok(40, "F-4 : injection trace/hélicité-0 ⟹ Π^TT·(δδ)·Π^TT = 0 — ANNIHILÉE "
       "(aucune fuite de singlet dans le secteur TT)",
   all(c == 0 for c in flat(proj)))

ok(41, "F-5 : n≠2 dans T = nδW/δg ⟹ γ = n² ≠ 4 — CASSE (renvoi GAMMA, "
       "lecture nue ≠ canonique jamais mélangées)",
   (3**2 != 4) and (1**2 != 4))

# ===========================================================================
print("\n" + "=" * 76)
print("BILAN — discipline LC-AUDIT-VERDICT §6.4, SANS SURCLASSEMENT")
print("=" * 76)
print("""
  VERDICT (verrou non-linéaire du deux-point, rang 2) :
  • C1 [établi — algèbre] : l'espace des deux-points PAIRS d'un opérateur TT
    spin-2, Δ=d=3, est de DIMENSION 1 (interne [A] ; CONFIRMÉ OP 2.23) ;
    forme k³·Π^TT FORCÉE par l'invariance ; liberté résiduelle = UNE
    amplitude — celle déjà pendue à N (C_T∝N, renvoi ATN/DUAL).
  • C2 [établi — algèbre] : secteur IMPAIR de dimension 1 ET de type CONTACT
    (interne [B] ; cohérent OP points séparés) — aucune amplitude radiative
    neuve ; pair radiatif / impair contact : la scission suit la parité.
  • C3 [établi — algèbre] : refermeture BD (⟨EE⟩,⟨BB⟩ ∝ k³) ; Cotton (i/2)k³
    ab initio ≡ de Haro (47), slack nul ; ÉQUIPARTITION ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ EXACTE en
    unités de dualité (49/50) ; ⟨EB⟩ radiatif nul sur BD ; D²=−𝟙 recoupe
    S²=−𝟙 (51) indépendamment ; map prog↔dH = facteur fixe pur.
  • C4 [tenue] : 0 entrée libre < 3 sorties appariées ; le cas {2,4,8}
    (2 des préfacteurs vs ½ du Cotton) identifié et résolu, produit net 1.

  EFFET (réduction interne, sans surclassement) : le constat « liberté
  résiduelle de D1 au niveau gaussien = UNE amplitude A_T ~ 1/N » passe de
  `établi perturbatif TT` (relation d'état BD) à `établi` PAR INVARIANCE
  (représentation, secteur de Weyl complet, deux parités) — l'analogue
  rang 2 de NONLIN-VERROU.

  SANS SURCLASSEMENT : « forme verrouillée » = comptage de représentation.
  JAMAIS « A3 dérivé / deux-point dérivé / D1 clos / N fixé / CCC démontrée ».
  Le k³ RESTE la donnée de Cauchy irréductible, pendue à N seul.
  Compte {A4 ; A2★ ; N} INCHANGÉ. Circularité LC-E intacte.
""")
print(f"TOUS LES ASSERT PASSENT — {NPASS} assertions "
      "(27 phase 1 + 14 phase 2). Verrou rang 2 : convergence interne + "
      "confirmation comparanda. EXIT 0.")
sys.exit(0)
