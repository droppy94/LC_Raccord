"""Outils communs AA-1 : base de Weyl en 4D (signature -+++), jets, Omega au premier ordre."""
import sympy as sp
import itertools as it
from sympy.combinatorics import Permutation
from math import factorial

eta = sp.diag(-1, 1, 1, 1)
etainv = eta.inv()
X = sp.symbols('x0:4', real=True)
Om0 = sp.Symbol('Omega', positive=True)
ell = sp.Symbol('ell')          # ell = ln(Omega) au point x = 0
n = sp.symbols('n0:4', real=True)  # n_a (indices bas)
s = sp.Symbol('s', real=True)
lam, kap, b, c0 = sp.symbols('lambda kappa b c0', real=True)

pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def zeros4(rank):
    return sp.MutableDenseNDimArray.zeros(*([4] * rank))


def riemann_from_bivector(Mx):
    R = zeros4(4)
    for I, (a, bb) in enumerate(pairs):
        for J, (c, d) in enumerate(pairs):
            v = Mx[I, J]
            R[a, bb, c, d] = v; R[bb, a, c, d] = -v
            R[a, bb, d, c] = -v; R[bb, a, d, c] = v
    # retrait de la partie totalement antisymetrique (1re identite de Bianchi)
    A = zeros4(4)
    for idx in it.product(range(4), repeat=4):
        tot = 0
        for p in it.permutations(range(4)):
            sgn = Permutation(list(p)).signature()
            tot += sgn * R[tuple(idx[i] for i in p)]
        A[idx] = sp.Rational(1, 24) * tot
    for idx in it.product(range(4), repeat=4):
        R[idx] = R[idx] - A[idx]
    return R


def weyl_part(R):
    Ric = sp.zeros(4, 4)
    for bb, d in it.product(range(4), repeat=2):
        Ric[bb, d] = sum(etainv[a, c] * R[a, bb, c, d] for a in range(4) for c in range(4))
    Rs = sum(etainv[bb, d] * Ric[bb, d] for bb in range(4) for d in range(4))
    P = (Ric - Rs / 6 * eta) / 2
    C = zeros4(4)
    for a, bb, c, d in it.product(range(4), repeat=4):
        C[a, bb, c, d] = R[a, bb, c, d] - (eta[a, c] * P[bb, d] - eta[a, d] * P[bb, c]
                                          + eta[bb, d] * P[a, c] - eta[bb, c] * P[a, d])
    return C


def weyl_basis():
    vecs = []
    for I in range(6):
        for J in range(I, 6):
            Mx = sp.zeros(6, 6); Mx[I, J] = 1; Mx[J, I] = 1
            C = weyl_part(riemann_from_bivector(Mx))
            vecs.append([C[idx] for idx in it.product(range(4), repeat=4)])
    M = sp.Matrix(vecs)
    _, piv = M.T.rref()
    basis = []
    for p in piv:
        C = zeros4(4)
        for k, idx in enumerate(it.product(range(4), repeat=4)):
            C[idx] = M[p, k]
        basis.append(C)
    return basis


def check_weyl(C):
    ok = True
    for a, bb, c, d in it.product(range(4), repeat=4):
        v = C[a, bb, c, d]
        ok &= (v == -C[bb, a, c, d]) and (v == -C[a, bb, d, c]) and (v == C[c, d, a, bb])
        ok &= sp.simplify(v + C[a, c, d, bb] + C[a, d, bb, c]) == 0
    for bb, d in it.product(range(4), repeat=2):
        ok &= sp.simplify(sum(etainv[a, c] * C[a, bb, c, d] for a in range(4) for c in range(4))) == 0
    return ok


def multi_indices(maxorder):
    out = []
    for k in range(maxorder + 1):
        out += list(it.combinations_with_replacement(range(4), k))
    return out


def jet_poly(name, maxorder):
    """Polynome de Taylor generique ; d_alpha f(0) = symbole f_alpha."""
    syms = {}
    expr = 0
    for al in multi_indices(maxorder):
        sym = sp.Symbol(f"{name}_{''.join(map(str, al))}" if al else f"{name}_")
        syms[al] = sym
        mon = 1; den = 1
        for i in range(4):
            cnt = al.count(i)
            mon *= X[i] ** cnt; den *= factorial(cnt)
        expr += sym * mon / den
    return expr, syms


def Omega_x():
    """Omega au premier ordre : d_a d_b Omega = s eta_ab, d s = 0."""
    return Om0 + sum(n[a] * X[a] for a in range(4)) + s / 2 * sum(eta[a, a] * X[a] ** 2 for a in range(4))


def at0(e):
    return e.subs({x: 0 for x in X})


def logsub(e):
    return sp.expand(e.subs(sp.log(Om0), ell))


def R_from_T(T0, T1, Ofun=None):
    """R_{rho nu lam} au point x=0 depuis T(x) = T0 + x^e T1[e] (symetriques),
    via That = Omega^2 T, ghat = Omega^-2 eta, Lhat de Friedrich, Christoffel de ghat.
    Retour : tableau R[rho,nu,lam]."""
    Om = Omega_x() if Ofun is None else Ofun
    T = sp.Matrix(4, 4, lambda a, c: T0[a, c] + sum(X[e] * T1[e][a, c] for e in range(4)))
    gh = Om ** -2 * eta
    ghi = Om ** 2 * etainv
    That = Om ** 2 * T
    tr = sum(ghi[a, c] * That[a, c] for a in range(4) for c in range(4))
    L = (kap / 2) * (That - tr * gh / 3) + lam / 6 * gh
    # Christoffel de ghat
    dgh = [[[sp.diff(gh[a, c], X[e]) for e in range(4)] for c in range(4)] for a in range(4)]
    Gam = [[[at0(sum(ghi[a, dd] * (dgh[dd][bb][c] + dgh[dd][c][bb] - dgh[bb][c][dd]) for dd in range(4)) / 2)
             for c in range(4)] for bb in range(4)] for a in range(4)]
    L0 = L.applyfunc(at0)
    dL = [L.applyfunc(lambda v: at0(sp.diff(v, X[e]))) for e in range(4)]

    def nabL(nu, a, c):
        return dL[nu][a, c] - sum(Gam[m][nu][a] * L0[m, c] + Gam[m][nu][c] * L0[a, m] for m in range(4))
    R = zeros4(3)
    for rho, nu, la in it.product(range(4), repeat=3):
        R[rho, nu, la] = sp.expand((nabL(nu, la, rho) - nabL(la, nu, rho)) / Om0)
    return R
