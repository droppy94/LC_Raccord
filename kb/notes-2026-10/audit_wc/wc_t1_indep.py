"""wc_t1_indep.py -- audit W-c, reproduction independante de t-1.
Differences volontaires avec irt_a.py :
 * densite sous forme integree par parties (meme equation d'Euler-Lagrange, densite differente) :
     sqrt(g) [ sigma E - (2/3) R box(sigma) + c4 ( (box sigma)^2 - 2 R^{ab} d_a sigma d_b sigma + (2/3) R (d sigma)^2 ) ]
   (car Int sqrt g sigma box R = Int sqrt g R box sigma, et Int sqrt g sigma Delta4 sigma = Int sqrt g [(box s)^2 - 2 Ric(ds,ds) + 2/3 R (ds)^2])
 * le mode (P, Q) est substitue AVANT la variation ; on varie une fonction test F inseree dans une composante g_ab ;
   operateur d'Euler ecrit a la main ; inverse et sqrt(g) par serie automatique (pas a la main) ;
 * toutes les composantes ss, sx, xx, yy, zz testees, fond et ordre e.
T^{ab} = (2/sqrt g) dS/dg_ab (convention T_ab = -(2/sqrt g) dS/dg^ab), puis T_hat_ab = s^2 g_ac g_bd T^{cd}.
"""
import sys, itertools
import sympy as sp
c4 = sp.Rational(sys.argv[1]) if len(sys.argv) > 1 else sp.Integer(2)
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True)
e, dl = sp.symbols('e dl')
k, A, B = sp.symbols('k A B', positive=True)
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]; n = 4
F = sp.Function('F')(s, x)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
Pm = u*sp.cos(k*x)

def trunc(ex):
    ex = sp.expand(ex)
    return sum(ex.coeff(e, i).coeff(dl, j)*e**i*dl**j for i in range(2) for j in range(2))

def run(comp):
    a0, b0 = comp
    g = sp.diag(-1, 1, 1 + e*Pm, 1 - e*Pm)
    g = g.as_mutable()
    g[a0, b0] += dl*F
    if a0 != b0:
        g[b0, a0] += dl*F
    # inverse par serie de Neumann : g = eta + h, g^-1 = eta - eta h eta + eta h eta h eta
    eta = sp.diag(-1, 1, 1, 1); h = g - eta
    gi = (eta - eta*h*eta + eta*h*eta*h*eta - eta*h*eta*h*eta*h*eta).applyfunc(trunc)
    detg = sp.expand(-g.det())
    sq = trunc(sp.series(sp.sqrt(1 + sp.Symbol('w')), sp.Symbol('w'), 0, 4).removeO().subs(sp.Symbol('w'), detg - 1))
    d = lambda f, i: sp.diff(f, X[i])
    Gam = [[[trunc(sum(gi[a, m]*(d(g[m, b], c) + d(g[m, c], b) - d(g[b, c], m)) for m in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    # Riemann tout en bas : R_abcd
    Rup = {}
    for a, b, c, dd in itertools.product(range(n), repeat=4):
        Rup[(a, b, c, dd)] = trunc(d(Gam[a][b][dd], c) - d(Gam[a][b][c], dd)
                                  + sum(Gam[a][c][m]*Gam[m][b][dd] - Gam[a][dd][m]*Gam[m][b][c] for m in range(n)))
    Rdn = {key: trunc(sum(g[key[0], m]*Rup[(m,) + key[1:]] for m in range(n))) for key in Rup}
    # indices tout en haut
    Rhi = {}
    for key in Rdn:
        a, b, c, dd = key
        v = 0
        for p, q, r, t in itertools.product(range(n), repeat=4):
            co = gi[a, p]*gi[b, q]*gi[c, r]*gi[dd, t]
            if co != 0 and Rdn[(p, q, r, t)] != 0:
                v += co*Rdn[(p, q, r, t)]
        Rhi[key] = trunc(v)
    Riem2 = trunc(sum(Rdn[kk]*Rhi[kk] for kk in Rdn))
    Ric = sp.Matrix(n, n, lambda b, dd: trunc(sum(Rup[(a, b, a, dd)] for a in range(n))))
    Ricu = (gi*Ric*gi).applyfunc(trunc)
    Ric2 = trunc(sum(Ric[a, b]*Ricu[a, b] for a in range(n) for b in range(n)))
    Rs = trunc(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    Eu = trunc(Riem2 - 4*Ric2 + Rs**2)
    sig = -sp.log(s)
    dsg = [d(sig, i) for i in range(n)]
    boxs = trunc(sum(gi[a, b]*(sp.diff(sig, X[a], X[b]) - sum(Gam[m][a][b]*dsg[m] for m in range(n)))
                     for a in range(n) for b in range(n)))
    grad2 = trunc(sum(gi[a, b]*dsg[a]*dsg[b] for a in range(n) for b in range(n)))
    Ricss = trunc(sum(Ricu[a, b]*dsg[a]*dsg[b] for a in range(n) for b in range(n)))
    L = trunc(sq*(sig*Eu - sp.Rational(2, 3)*Rs*boxs + c4*(boxs**2 - 2*Ricss + sp.Rational(2, 3)*Rs*grad2)))
    L1 = sp.expand(L.coeff(dl, 1))   # lineaire en F et ses derivees
    # operateur d'Euler a la main : L1 = sum c_{i,j} d_s^i d_x^j F
    derivs = {}
    for t in sp.Add.make_args(L1):
        ds_ = [f for f in t.atoms(sp.Derivative) if f.expr == F]
        if ds_:
            D = ds_[0]; i = sum(cnt for v, cnt in D.variable_count if v == s); j = sum(cnt for v, cnt in D.variable_count if v == x)
            co = t/D
        else:
            i = j = 0; co = t/F
        assert not co.has(F)
        derivs[(i, j)] = derivs.get((i, j), 0) + co
    EL = 0
    for (i, j), co in derivs.items():
        ex = co
        if i: ex = sp.diff(ex, s, i)
        if j: ex = sp.diff(ex, x, j)
        EL += (-1)**(i + j)*ex
    EL = sp.expand(EL)            # = dS/dF ; pour diag : dS/dg_ab ; hors diag : 2 dS/dg_ab
    dSdg = EL if a0 == b0 else EL/2
    # T^{ab} = 2/sqrt g dS/dg_ab, avec g (e seulement)
    g0 = g.subs(dl, 0); sq0 = sq.subs(dl, 0)
    Tup_ab = trunc(2*dSdg*trunc(2 - sq0))       # 1/sqrt g ~ 2 - sqrt g a l'ordre e (sqrt g - 1 = O(e^2) ici)
    # T_hat_{a0 b0} = s^2 g_{a0 c} g_{b0 d} T^{cd} ; g diagonal a l'ordre e (sans dl) : seul T^{a0 b0} contribue
    That = trunc(s**2*g0[a0, a0]*g0[b0, b0]*Tup_ab)
    ghat = g0[a0, b0]/s**2
    res = [sp.simplify(sp.expand(That - 6*ghat).coeff(e, i)) for i in range(2)]
    T0 = sp.simplify(That.coeff(e, 0))
    return T0, res

for comp in [(2, 2), (3, 3), (0, 0), (1, 1), (0, 1)]:
    T0, res = run(comp)
    nm = 'sxyz'[comp[0]] + 'sxyz'[comp[1]]
    print(f"c4={c4} comp {nm}: T_hat fond = {T0} ; (T_hat - 6 ghat) ordre e^0 = {res[0]} ; ordre e^1 = {res[1]}")
print("EXIT 0")
