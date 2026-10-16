# Q5 : reponse metrique d'ordre eps^2 (secteur q = k1-k2 et secteur homogene) en jauge
#   h_{0i} = 0 (decalage nul), delta^{ij} h_ij = 0 (trace spatiale nulle) ; lapse h_00 libre
import sympy as sp, pickle, sys, time, os
from conv import gu, gl, eta, E4, I, g0
from spinors import mode, dirac_residual, T_phys_pair, mu, Om
import linE

NH = int(sys.argv[1]) if len(sys.argv) > 1 else 8          # ordre max de h
MUNUM = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2] != 'None') else None          # valeur numerique de mu (sinon symbolique)
m = mu if MUNUM is None else sp.Rational(MUNUM)
Npsi = NH - 3

Hs, E = pickle.load(open('linE.pkl', 'rb'))
s = linE.s; qs = linE.q

k1 = (1, 1, 0); k2 = (-1, 2, 1)
neg = lambda k: tuple(-c for c in k)
A1 = ([1, 2*I, 0, 0], [0, 0, 1 - I, 2]); A2 = ([2 - I, 1, 0, 0], [0, 0, I, 1 + I])
SINGLE = len(sys.argv) > 3 and sys.argv[3] == 'single'
if SINGLE:   # classe a un seul exposant : seulement Omega^{+i mu} (c_0 dans P+)
    A1 = (A1[0], None); A2 = (A2[0], None)
    print("CLASSE A UN SEUL EXPOSANT (Omega^{+i mu} seulement)")
def mk(k, A):
    return mode(k, A[0], A[1], Npsi, m)
def mkP(k, A):  # partenaire de parite : k -> -k, c -> gamma^0 c
    return mode(neg(k), list(g0*sp.Matrix(A[0])), None if A[1] is None else list(g0*sp.Matrix(A[1])), Npsi, m)
t0 = time.time()
modes = {k1: mk(k1, A1), neg(k1): mkP(k1, A1), k2: mk(k2, A2), neg(k2): mkP(k2, A2)}
# verification : equation de Dirac satisfaite ordre par ordre
for k, d in modes.items():
    res = dirac_residual(k, d, m)
    bad = [key for key, v in res.items() if key[0] < Npsi and v != sp.zeros(4, 1)]
    print("mode", k, ": residu de Dirac nul jusqu'a l'ordre", Npsi - 1, ":", bad == [])

def sub_mu(T):
    return T if MUNUM is None else T
def add(D, E_):
    for key, v in E_.items():
        D[key] = D.get(key, sp.zeros(4)) + v
    return D

def source(pairs, nmax):
    D = {}
    for (p, r) in pairs:
        if MUNUM is None:
            add(D, T_phys_pair(p, modes[p], r, modes[r], nmax))
        else:
            add(D, {kk: v.subs(mu, m) for kk, v in T_phys_pair(p, modes[p], r, modes[r], nmax).items()})
    return {kk: v.applyfunc(sp.simplify) for kk, v in D.items()}

def conservation_check(qv, T, nmax):
    """nabla^mu T_{mu nu} = 0 sur g = eta/t^2, t = -Omega, coefficient par coefficient.
    Gam^l_{ab} = (1/Omega)(d^l_a d^0_b + d^l_b d^0_a - eta_ab eta^{l0}) ; d_t = -d_Omega"""
    def Gam(l, a, b):
        return ((1 if (l == a and b == 0) else 0) + (1 if (l == b and a == 0) else 0) - eta[a, b]*eta[l, 0])
    out = {}
    for (n, j), v in T.items():
        sv = n + I*j*m
        for nu in range(4):
            # d_0 : -d_Omega Omega^s = -s Omega^{s-1}
            key = (n-1, j)
            val = sum(eta[0, 0]*(-sv)*v[0, nu] for _ in [0])
            val += -sum(eta[a, a]*sum(Gam(l, a, a)*v[l, nu] + Gam(l, a, nu)*v[a, l] for l in range(4)) for a in range(4))
            out.setdefault(key, [0]*4); out[key][nu] += val
            key2 = (n, j)
            val2 = sum(eta[a, a]*I*qv[a-1]*v[a, nu] for a in (1, 2, 3))
            out.setdefault(key2, [0]*4); out[key2][nu] += val2
    bad = [k for k, vv in out.items() if k[0] < nmax and any(sp.simplify(x) != 0 for x in vv)]
    return bad

def solve_sector(qv, T, label):
    Esub = E.subs({qs[0]: qv[0], qs[1]: qv[1], qs[2]: qv[2]})
    Ecoef = {(a, b, r): sp.expand(Esub[a, b]).coeff(Om, r) for a in range(4) for b in range(a, 4) for r in (-4, -3, -2)}
    import os
    SYNC = os.environ.get('GAUGE') == 'sync'
    comps = [(0, 0), (1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]   # (3,3) = -(1,1)-(2,2) ; (0,i) = 0
    if SYNC:   # jauge synchrone conforme : h_00 = h_0i = 0, trace libre
        comps = [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)]
    js = sorted(set(j for (n, j) in T))
    sol_all = {}
    for j in js:
        unk = {}
        for n in range(NH+1):
            for (a, b) in comps:
                unk[(n, a, b)] = sp.Symbol('c_%d_%d%d' % (n, a, b))
        eqs = []
        for p in range(-2, NH - 1):
            for a in range(4):
                for b in range(a, 4):
                    lhs = 0
                    for n in range(NH+1):
                        sv = n + I*j*m
                        Hsub = {}
                        for (aa, bb) in comps:
                            Hsub[sp.Symbol('H%d%d' % (aa, bb))] = unk[(n, aa, bb)]
                        if SYNC:
                            Hsub[sp.Symbol('H00')] = 0
                        else:
                            Hsub[sp.Symbol('H33')] = -unk[(n, 1, 1)] - unk[(n, 2, 2)]
                        for i_ in (1, 2, 3):
                            Hsub[sp.Symbol('H0%d' % i_)] = 0
                        # contribution a la puissance p : Omega^{-4} -> n-2, Omega^{-3} -> n-1, Omega^{-2} -> n
                        for r, sh in ((-4, -2), (-3, -1), (-2, 0)):
                            if n + sh == p:
                                coef = Ecoef[(a, b, r)]
                                lhs += coef.subs(s, sv).subs(Hsub)
                    rhs = T.get((p, j), sp.zeros(4))[a, b]
                    ex = sp.expand(lhs - rhs)
                    if ex != 0:
                        eqs.append(ex)
        U = list(unk.values())
        sol = sp.linsolve(eqs, U)
        if sol == sp.EmptySet:
            print(label, "j =", j, ": SYSTEME INCOMPATIBLE (logarithme necessaire)")
            sol_all[j] = None
            continue
        (sv_,) = list(sol)
        d = dict(zip(U, sv_))
        free = set().union(*[sp.sympify(v).free_symbols for v in sv_]) & set(U)
        sol_all[j] = (unk, d, free)
        print(label, "j =", j, ": systeme compatible (aucun log jusqu'a Omega^%d) ; parametres libres :" % NH, sorted(free, key=str))
    return sol_all

if __name__ == "__main__":
    q = tuple(a - b for a, b in zip(k1, k2))
    secteurs = {
        'q=k1-k2': (q, [(k2, k1), (neg(k1), neg(k2))]),
        'homogene': ((0, 0, 0), [(k, k) for k in modes]),
    }
    results = {}
    for lab, (qv, pairs) in secteurs.items():
        T = source(pairs, NH - 2)
        print("=== secteur", lab, "q =", qv, "; termes source (n,j) :", sorted(T), " t=%.0fs" % (time.time()-t0))
        bad = conservation_check(qv, T, NH - 2)
        print("   conservation exacte nabla^mu T_mu nu = 0 a tous les ordres < Omega^%d :" % (NH-2), bad == [], bad)
        results[lab] = (qv, T, solve_sector(qv, T, lab))
        print("   t=%.0fs" % (time.time()-t0))
    pickle.dump((results, NH, MUNUM), open('q5_res_%s_%s%s.pkl' % (NH, str(MUNUM).replace('/', 'o'), ('_single' if SINGLE else '') + ('_sync' if os.environ.get('GAUGE') == 'sync' else '')), 'wb'))
