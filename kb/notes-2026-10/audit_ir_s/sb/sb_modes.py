# Reproduction independante R-B, R-C, R-D + contre-exemples de polarisation/direction/superposition
import sympy as sp, sys
from sb_lib import *
b, kap, k = sp.symbols('b kappa k', positive=True)
A1, B1, A2, B2 = sp.symbols('A1 B1 A2 B2', real=True)
phi = -sp.log(s); c0 = -8   # convention T^ab = (2/sqrt g) dS/dg_ab (verifiee par sb_RA.py)
def umode(A, B, K):
    return A*(sp.cos(K*s) + K*s*sp.sin(K*s)) + B*(sp.sin(K*s) - K*s*sp.cos(K*s))
def tt(kv, pol):
    k1, k2 = kv; K2 = k1**2 + k2**2
    e1 = sp.Matrix([-k2, k1, 0]); e2 = sp.Matrix([0, 0, 1])
    return (e1*e1.T - K2*e2*e2.T) if pol == '+' else (e1*e2.T + e2*e1.T)
def build(modes):
    H = sp.zeros(4, 4)
    for (kv, pol, A, B, K) in modes:
        E = tt(kv, pol); ph = sp.cos(kv[0]*x + kv[1]*y)
        for i in range(3):
            for j in range(3):
                H[i+1, j+1] += E[i, j]*umode(A, B, K)*ph
    return H
cases = {
 'plus_x (reproduction)': [((k, 0), '+', A1, B1, k)],   # e1 = (0,k,0) : h_yy = k^2 u, h_zz = -k^2 u
 'croix_x (h_yz)':        [((k, 0), 'x', A1, B1, k)],
 'plus_oblique k=(3,4)':  [((3, 4), '+', A1, B1, 5)],
 'croix_oblique k=(3,4)': [((3, 4), 'x', A1, B1, 5)],
 'superposition':         [((k, 0), '+', A1, B1, k), ((3, 4), 'x', A2, B2, 5)],
}
ghat = s**-2*eta; ghi = s**2*eta
Gam = christoffel_full(ghat)
which = sys.argv[1:] or list(cases)
for name in which:
    H = build(cases[name])
    Rd, Ric, Rs, P, C = lin_curv(H)
    T = sp.Matrix(4, 4, lambda a, bb: c0*b*sp.expand(sum(eta[c,c]*eta[d,d]*sp.diff(phi*C[(a,c,bb,d)], X[c], X[d]) for c in range(4) for d in range(4))))
    Th = (s**2*T).applyfunc(sp.expand)
    tr = sp.simplify(sum(ghi[a,bb]*Th[a,bb] for a in range(4) for bb in range(4)))
    div = [sp.simplify(sum(ghi[a,c]*covd2(Th, Gam, a, bb, c) for a in range(4) for c in range(4))) for bb in range(4)]
    haslog = any(sp.expand(Th[a,bb]).has(sp.log) for a in range(4) for bb in range(4))
    L = (kap/2*(Th - ghat*tr/3)).applyfunc(sp.expand)
    print(f"== {name}\n   trace = {tr} ; divergence = {div} ; ln s dans That : {haslog}")
    # W_E,ij a scri
    WE = sp.Matrix(3, 3, lambda i, j: sp.limit(sp.simplify(C[(0, i+1, 0, j+1)]/s), s, 0))
    # residus des poles de R
    okres = True; others = []
    for r in range(4):
        for nu in range(4):
            for la in range(nu+1, 4):
                e = sp.simplify((covd2(L, Gam, la, r, nu) - covd2(L, Gam, nu, r, la))/s)
                res = sp.simplify(sp.limit(s*e, s, 0))
                if nu == 0 and r > 0:
                    target = 8*b*kap*WE[r-1, la-1]
                    if sp.simplify(res - target) != 0: okres = False; print("   ecart residu", r, la, res, target)
                elif res != 0:
                    others.append((r, nu, la, res))
    print("   residu R_isj = 8 b kappa W_E,ij(scri) pour tous i,j :", okres, " ; autres composantes polaires :", others)
    print("   W_E(scri) =", [sp.factor(WE[i, j]) for i in range(3) for j in range(i, 3)])
    if name.startswith('plus_x'):
        print("   That_yy (s^1,s^2) =", sp.expand(sp.series(sp.simplify(Th[2,2]), s, 0, 3).removeO()))
        print("   That_zz (s^1,s^2) =", sp.expand(sp.series(sp.simplify(Th[3,3]), s, 0, 3).removeO()))
        for (r, nu, la) in [(2,0,2), (3,0,3), (2,1,2)]:
            e = sp.simplify((covd2(L, Gam, la, r, nu) - covd2(L, Gam, nu, r, la))/s)
            print(f"   R_{'sxyz'[r]}{'sxyz'[nu]}{'sxyz'[la]} =", sp.expand(sp.series(e, s, 0, 2).removeO()))
