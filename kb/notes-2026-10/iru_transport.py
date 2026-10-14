"""iru_transport.py -- IR-u (NOTE-132/133). Equation d'Einstein linearisee completee :
(G_ab + 3 ghat_ab)[ghat] = kappa That_ab,  ghat = s^-2 (eta + eps h),  h_yy = -h_zz = u(s) cos kx,
That = s^2 T, T_ab = c0 b d^c d^d (sigma C_acbd), sigma = -ln s, c0 = +8 (convention T_ab = (2/sqrt g) dS/dg^ab, gel NOTE-124).
Reduction d'ordre : u = u0 + b*kappa*u1, L[u1] = That_yy[u0] / b. Solution en serie (Frobenius avec logarithmes) pres de s = 0.
Puis W_E,yy = C_sysy[eta + h]/s pour u0 + b kappa u1 : coefficient gamma du terme ln s.
"""
import sympy as sp
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True)
k, A, B, kap, b, eps = sp.symbols('k A B kappa b epsilon', positive=True)
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]; n = 4
eta = sp.diag(-1, 1, 1, 1)
c0 = 8
uf = sp.Function('u')(s)
def lin(e):
    return sp.expand(sp.series(e, eps, 0, 2).removeO())
# --- operateur L : (G + 3 ghat)_yy a l'ordre eps
gh = s**-2*(eta + eps*sp.diag(0, 0, uf*sp.cos(k*x), -uf*sp.cos(k*x)))
ghi = sp.diag(*[lin(1/gh[i, i]) for i in range(n)])
d = lambda f, i: sp.diff(f, X[i])
Gam = [[[lin(sum(ghi[a, m]*(d(gh[m, bb], c) + d(gh[m, c], bb) - d(gh[bb, c], m)) for m in range(n))/2)
         for c in range(n)] for bb in range(n)] for a in range(n)]
def ric(bb, dd):
    return lin(sum(d(Gam[a][bb][dd], a) - d(Gam[a][bb][a], dd)
                   + sum(Gam[a][a][m]*Gam[m][bb][dd] - Gam[a][dd][m]*Gam[m][bb][a] for m in range(n)) for a in range(n)))
Ric = sp.diag(*[ric(i, i) for i in range(n)])
Rs = lin(sum(ghi[i, i]*Ric[i, i] for i in range(n)))
Eyy = lin(Ric[2, 2] - Rs*gh[2, 2]/2 + 3*gh[2, 2])
Eyy0 = sp.simplify(Eyy.coeff(eps, 0)); Lyy = sp.simplify(Eyy.coeff(eps, 1))
print("controle fond (G+3g)_yy ordre 0 :", Eyy0)
print("L[u] (ordre eps de (G+3g)_yy) =", sp.factor(Lyy))
# --- That_yy pour u general (forme fermee, Weyl lineaire de eta + h)
H = sp.zeros(n, n); H[2, 2] = uf*sp.cos(k*x); H[3, 3] = -uf*sp.cos(k*x)
dd_ = lambda f, *ix: sp.diff(f, *[X[i] for i in ix])
R4 = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for q in range(n):
                R4[(a, bb, c, q)] = (dd_(H[a, q], bb, c) + dd_(H[bb, c], a, q) - dd_(H[bb, q], a, c) - dd_(H[a, c], bb, q))/2
Ric1 = sp.Matrix(n, n, lambda bb, q: sum(eta[a, a]*R4[(a, bb, a, q)] for a in range(n)))
Rs1 = sum(eta[a, a]*Ric1[a, a] for a in range(n))
C = {kk: v - (eta[kk[0], kk[2]]*Ric1[kk[1], kk[3]] - eta[kk[0], kk[3]]*Ric1[kk[1], kk[2]] - eta[kk[1], kk[2]]*Ric1[kk[0], kk[3]] + eta[kk[1], kk[3]]*Ric1[kk[0], kk[2]])/2
     + Rs1/6*(eta[kk[0], kk[2]]*eta[kk[1], kk[3]] - eta[kk[0], kk[3]]*eta[kk[1], kk[2]]) for kk, v in R4.items()}
sig = -sp.log(s)
Tyy = c0*b*sum(eta[c, c]*eta[q, q]*dd_(sig*C[(2, c, 2, q)], c, q) for c in range(n) for q in range(n))
Thyy = sp.simplify(s**2*Tyy)
print("That_yy[u] (u general) =", sp.factor(Thyy))
CE = sp.simplify(C[(0, 2, 0, 2)])
print("C_sysy[u] =", sp.factor(CE))
# --- mode du vide
u0 = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
print("controle : L[u0] =", sp.simplify(Lyy.subs(uf, u0).doit()))
src = sp.simplify(kap*Thyy.subs(uf, u0).doit()/(b*kap))    # L[u1] = That_yy[u0]/b  (on a pose u = u0 + b kappa u1)
print("source That_yy[u0]/b =", sp.simplify(src))
# --- solution en serie : u1 = sum a_n s^n + sum c_n s^n ln s, n = 0..7
N = 8
a_ = sp.symbols('a0:%d' % N); c_ = sp.symbols('c0:%d' % N)
L_ = sp.log(s)
u1 = sum(a_[i]*s**i for i in range(N)) + sum(c_[i]*s**i*L_ for i in range(N))
res = sp.expand((Lyy.subs(uf, u1).doit() - src)/sp.cos(k*x))
res = sp.expand(sp.series(res*s**2, s, 0, N-1).removeO())
eqs = []
for pw in range(0, N-1):
    for lp in (0, 1):
        co = sp.expand(res).coeff(s, pw)
        co = sp.expand(co).coeff(L_, lp) if lp else sp.expand(co).subs(L_, 0)
        if co != 0:
            eqs.append(co)
sol = sp.solve(eqs, list(a_) + list(c_), dict=True)
print("nombre de solutions :", len(sol))
sol = sol[0]
u1s = sp.expand(u1.subs(sol))
print("u1 (serie, termes libres = modes homogenes) :", sp.collect(u1s, L_))
# --- Weyl rescale electrique
u_tot = u0 + b*kap*u1s
WE = sp.expand(CE.subs(uf, u_tot).doit()/s/sp.cos(k*x))
WE = sp.expand(sp.series(WE, s, 0, 2).removeO())
WE0 = sp.limit(sp.expand(WE).subs(b, 0), s, 0)
logco = sp.simplify(sp.expand(WE).coeff(L_, 1).subs(s, 0))
print("W_E,yy(s) a l'ordre s^0 :", sp.collect(sp.expand(WE.subs(s**1, 0) if False else WE), L_))
print("W_E,yy sans correction (b = 0) en s = 0 :", WE0)
print("coefficient de ln s dans W_E,yy a s^0 :", logco)
gam = sp.simplify(logco/(b*kap*WE0)) if WE0 != 0 else None
print("gamma (W_E ~ W0 (1 + gamma b kappa ln s)) :", gam)
print("EXIT 0")
