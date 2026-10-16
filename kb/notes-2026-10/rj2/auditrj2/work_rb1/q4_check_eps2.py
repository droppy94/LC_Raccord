# Verification croisee : la solution d'ordre eps^2 satisfait (3.3) :
#   g_c(dOmega,dOmega) = -lambda/3 + 2 Omega s + That/12,  That = -m Omega^3 psibar_c psi_c   (lambda = 3)
# au premier ordre en h : -1 - h_00 = -1 + 2 Omega s^(1) + That/12
import sympy as sp, pickle, sys
from conv import eta, I
from spinors import mu, Om
t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
eps = sp.Symbol('epsilon')
fn = sys.argv[1]
results, NH, MUNUM = pickle.load(open(fn, 'rb'))
m = mu if MUNUM is None else sp.Rational(MUNUM)
sS = sp.Symbol('s'); q = sp.symbols('q1:4', real=True)
Hs = sp.Matrix(4, 4, lambda a, b: sp.Symbol('H%d%d' % (min(a, b), max(a, b))))
ph = (-t)**sS*sp.exp(I*(q[0]*x + q[1]*y + q[2]*z))
g = eta + eps*Hs*ph
gi = eta - eps*eta*Hs*ph*eta
OmF = -t
def Gam(l, a, b):
    return sum(gi[l, r]*(sp.diff(g[r, a], X[b]) + sp.diff(g[r, b], X[a]) - sp.diff(g[a, b], X[r])) for r in range(4))/2
G = [[[Gam(l, a, b) for b in range(4)] for a in range(4)] for l in range(4)]
box = sum(gi[a, b]*(sp.diff(OmF, X[a], X[b]) - sum(G[c][a][b]*sp.diff(OmF, X[c]) for c in range(4))) for a in range(4) for b in range(4))
Ric = sp.zeros(4)
for b in range(4):
    for d in range(4):
        Ric[b, d] = sum(sp.diff(G[a][b][d], X[a]) - sp.diff(G[a][b][a], X[d]) + sum(G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a] for e in range(4)) for a in range(4))
R = sum(gi[b, d]*Ric[b, d] for b in range(4) for d in range(4))
s1 = sp.diff(box/4 + OmF*R/24, eps).subs(eps, 0)
grad1 = sp.diff(sum(gi[a, b]*sp.diff(OmF, X[a])*sp.diff(OmF, X[b]) for a in range(4) for b in range(4)), eps).subs(eps, 0)
# normalisation : Omega s^(1) et grad^(1) en unites Omega^{s} e^{iqx}
Os = sp.expand(sp.simplify(OmF*s1/ph)).subs(t, -Om)
gr = sp.expand(sp.simplify(grad1/ph)).subs(t, -Om)
print("grad^(1)/(Omega^s e^{iqx}) =", gr, " (attendu -H00)")
print("Omega s^(1) / (Omega^s e^{iqx}) =", sp.collect(sp.expand(Os), Om))
for lab, (qv, T, sols) in results.items():
    subq = {q[0]: qv[0], q[1]: qv[1], q[2]: qv[2]}
    worst = []
    for j, S in sols.items():
        unk, d, free = S
        z = {f: 0 for f in free}
        # assemble les coefficients : residu R(p) = [grad1 - 2 Omega s1 - That/12] a la puissance Omega^{p + i j mu}
        res = {}
        for n in range(NH + 1):
            sv = n + I*j*m
            Hsub = {Hs[a, b]: 0 for a in range(4) for b in range(4)}
            for (nn, a, b), sym in unk.items():
                if nn == n:
                    Hsub[sp.Symbol('H%d%d' % (a, b))] = sp.sympify(d[sym]).subs(z)
            Hsub[sp.Symbol('H33')] = -Hsub[sp.Symbol('H11')] - Hsub[sp.Symbol('H22')]
            expr = sp.expand((gr - 2*Os).subs(subq).subs(sS, sv).subs(Hsub))
            for k in range(-3, 4):
                cf = expr.coeff(Om, k)
                if cf != 0:
                    res[n + k] = res.get(n + k, 0) + cf
        # That = -tr(T) physique en coordonnees : That = g^{mu nu} T_mu nu = Omega^2 eta^{ab} T_ab
        for (n, jj), v in T.items():
            if jj != j: continue
            tr = sum(eta[a, a]*v[a, a] for a in range(4))      # Omega^2 * tr -> puissance n+2
            res[n + 2] = res.get(n + 2, 0) - tr/12
        bad = {p: sp.simplify(v) for p, v in res.items() if p <= NH - 2 and sp.simplify(v) != 0}
        print("secteur", lab, "j =", j, ": (3.3) verifiee ordre par ordre jusqu'a Omega^%d :" % (NH - 2), bad == {}, bad if bad else "")
