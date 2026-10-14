# Tenseur T^{ab} = (2/sqrt g) dS/dg_ab des termes de Wess-Zumino a l'ordre eps sur le mode plus de de Sitter.
# Famille g = diag(-(1+e N), 1, 1+e P, 1+e Q), action developpee a l'ordre e^2, Euler-Lagrange en P (et N pour le fond).
import sympy as sp, pickle
from sympy.calculus.euler import euler_equations
from sb_geom import *
e = sp.symbols('e')
k, A, B, b, a_, kap = sp.symbols('k A B b a kappa')
sig = -sp.log(s)
def tr2(ex, order=2):
    ex = sp.expand(ex)
    return sum(ex.coeff(e, i)*e**i for i in range(order+1))
def lagr(N, P, Q, order):
    tr = lambda ex: tr2(ex, order)
    g = sp.diag(-(1 + e*N), 1, 1 + e*P, 1 + e*Q)
    gi0 = sp.diag(*[tr(sp.series(1/g[i, i], e, 0, order+1).removeO()) for i in range(4)])
    # geom avec inverse tronquee
    G = [[[tr(sum(gi0[a, a]*(sp.diff(g[a, bb], X[c]) + sp.diff(g[a, c], X[bb]) - sp.diff(g[bb, c], X[a]))/2 for _ in [0]))
           for c in range(4)] for bb in range(4)] for a in range(4)]
    Rup = {}
    for a in range(4):
        for bb in range(4):
            for c in range(4):
                Rup[(a, bb, c, c)] = 0
                for d in range(c+1, 4):
                    v = tr(sp.diff(G[a][bb][d], X[c]) - sp.diff(G[a][bb][c], X[d]) + sum(G[a][c][f]*G[f][bb][d] - G[a][d][f]*G[f][bb][c] for f in range(4)))
                    Rup[(a, bb, c, d)] = v; Rup[(a, bb, d, c)] = -v
    Ric = sp.Matrix(4, 4, lambda bb, d: tr(sum(Rup[(a, bb, a, d)] for a in range(4))))
    Rs = tr(sum(gi0[a, a]*Ric[a, a] for a in range(4)))
    Riem2 = tr(sum(tr(Rup[(a, bb, c, d)]**2)*tr(g[a, a]*gi0[bb, bb]*gi0[c, c]*gi0[d, d]) for a in range(4) for bb in range(4) for c in range(4) for d in range(c+1, 4))*2)
    Ric2 = tr(sum(tr(Ric[a, bb]**2)*tr(gi0[a, a]*gi0[bb, bb]) for a in range(4) for bb in range(4)))
    E = tr(Riem2 - 4*Ric2 + Rs**2); C2 = tr(Riem2 - 2*Ric2 + Rs**2/3)
    sq = tr(sp.series(sp.sqrt(-g.det()), e, 0, order+1).removeO())
    dsig = sp.diff(sig, s)
    boxsig = tr(sp.diff(tr(sq*gi0[0, 0]*dsig), s)*tr(sp.series(1/sq, e, 0, order+1).removeO()))
    gradsig2 = tr(gi0[0, 0]*dsig**2)
    LC = tr(sq*sig*C2)
    LE = tr(sq*sig*E)
    LR = tr(-sp.Rational(2, 3)*sq*Rs*boxsig)
    LD = tr(2*sq*(boxsig**2 - 2*tr(gi0[0, 0]**2*Ric[0, 0])*dsig**2 + sp.Rational(2, 3)*Rs*gradsig2))
    return dict(C=LC, E=LE, R=LR, D=LD)
fN, fP, fQ = [sp.Function(nm)(s, x) for nm in ('N', 'P', 'Q')]
# fond : ordre 1, variations N et P en 0
L1 = lagr(fN, fP, fQ, 1)
back = {}
for key, Lk in L1.items():
    l1 = Lk.coeff(e, 1)
    back[key] = [sp.simplify(2*EL(l1, ff, [s, x])) for ff in (fN, fP)]   # T^{ss}, T^{yy} de fond (g^{-1} = eta a l'ordre 0)
    print(f"fond [{key}] : dS/dg_ss*2 = {back[key][0]} (T^ss = -ce terme, car g_ss = -(1+eN)) ; T^yy = {back[key][1]}")
# ordre 2, N = 0
L2 = lagr(0, fP, fQ, 2)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
mode = {fP: u*sp.cos(k*x), fQ: -u*sp.cos(k*x)}
res = {}
for key, Lk in L2.items():
    l2 = Lk.coeff(e, 2)
    eq = EL(l2, fP, [s, x])
    Tyy_up1 = 2*eq                                  # partie d'ordre e de T^yy
    Tyy_low1 = Tyy_up1 + 2*fP*back[key][1]          # T_yy = (1+eP)^2 T^yy
    Tyy_low1 = sp.simplify(Tyy_low1.subs(mode).doit())
    res[key] = Tyy_low1
    print(f"ordre eps [{key}] : T_yy^(1) =", sp.simplify(Tyy_low1))
pickle.dump((back, res), open('sb_euler.pkl', 'wb'))
