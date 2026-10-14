"""irt_gamma_phi.py -- IR-t (NOTE-130/131), t-2 et t-3.
t-2 : pour T_hat = s^p Y, Y_yy = -Y_zz = y(s) cos kx lisse (y = y0 + y1 s + y2 s^2 + y3 s^3), conserve et sans trace,
      ordre de R de (2.17) ; p = 1 (cas du terme sigma C^2) contre p = 2 (toute contribution s^2 * tenseur lisse du repere plat, dont Gamma[g]).
t-3 : (a) box_eta^2 (ln s) != 0 ; (b) phi_h lisse avec box^2 phi_h = 0 : T = c0 d^c d^d (phi_h C_acbd), T_hat = s^2 T, ordre de R.
"""
import sympy as sp
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True)
k, A, B, kap, b = sp.symbols('k A B kappa b', positive=True)
y0, y1, y2, y3, c1, c2, c3, c4 = sp.symbols('y0 y1 y2 y3 c1 c2 c3 c4')
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]; n = 4
eta = sp.diag(-1, 1, 1, 1); ghat = s**-2*eta; ghi = s**2*eta
sig = sp.log(1/s); ds_ = [sp.diff(sig, X[i]) for i in range(n)]
Gam = [[[(1 if a == bb else 0)*ds_[c] + (1 if a == c else 0)*ds_[bb] - eta[bb, c]*sum(eta[a, m]*ds_[m] for m in range(n))
         for c in range(n)] for bb in range(n)] for a in range(n)]
def cov(Tm, a, bb, c):
    return sp.diff(Tm[a, bb], X[c]) - sum(Gam[m][c][a]*Tm[m, bb] + Gam[m][c][bb]*Tm[a, m] for m in range(n))
def Rof(That):
    tr = sum(ghi[a, a]*That[a, a] for a in range(n))
    L = (kap/2*(That - ghat*tr/3)).applyfunc(sp.expand)
    out = {}
    for r in range(n):
        for nu in range(n):
            for la in range(nu+1, n):
                v = sp.expand(((cov(L, la, r, nu) - cov(L, nu, r, la))/s))
                if v != 0:
                    out[(r, nu, la)] = v
    return out, sp.simplify(tr), [sp.simplify(sum(ghi[a, c]*cov(That, a, bb, c) for a in range(n) for c in range(n))) for bb in range(n)]
def lowest(ex):
    ex = sp.expand(ex)
    pw = [sp.degree(t.as_independent(s)[1], s) if t.has(s) else 0 for t in sp.Add.make_args(sp.expand(ex*s**5))]
    return min(pw) - 5 if pw else None
names = 'sxyz'
yfun = y0 + y1*s + y2*s**2 + y3*s**3
print("t-2 : T_hat = s^p * Y, Y_yy = -Y_zz = y(s) cos kx")
for p in (1, 2):
    T = sp.zeros(n, n); T[2, 2] = s**p*yfun*sp.cos(k*x); T[3, 3] = -T[2, 2]
    R, tr, div = Rof(T)
    print(f"  p = {p} : trace = {tr} ; divergence = {div}")
    for key, v in R.items():
        print(f"     R_{''.join(names[i] for i in key)} : plus basse puissance de s = {lowest(v)} ; terme en 1/s = {sp.simplify(sp.expand(v*s).subs(s, 0))}")
# t-3
print("t-3 (a) : box_eta^2 de ln s (repere plat, box = -d_s^2 + d_x^2) :", sp.simplify((-sp.diff(-sp.diff(sp.log(s), s, 2), s, 2))))
phih = c1*s + c2*s**2 + c3*s**3 + c4*(x**2 + s**2)
boxf = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2)
print("t-3 (b) : box^2 phi_h =", sp.simplify(boxf(boxf(phih))), " (phi_h lisse en s = 0)")
# Weyl lineaire du mode et tenseur c0 d d (phi_h C)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(n, n); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
d = lambda f, *ix: sp.diff(f, *[X[i] for i in ix])
R4 = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for dd in range(n):
                R4[(a, bb, c, dd)] = (d(H[a, dd], bb, c) + d(H[bb, c], a, dd) - d(H[bb, dd], a, c) - d(H[a, c], bb, dd))/2
Ric = sp.Matrix(n, n, lambda bb, dd: sum(eta[a, a]*R4[(a, bb, a, dd)] for a in range(n)))
Rs = sum(eta[a, a]*Ric[a, a] for a in range(n))
C = {kk: v - (eta[kk[0], kk[2]]*Ric[kk[1], kk[3]] - eta[kk[0], kk[3]]*Ric[kk[1], kk[2]] - eta[kk[1], kk[2]]*Ric[kk[0], kk[3]] + eta[kk[1], kk[3]]*Ric[kk[0], kk[2]])/2
     + Rs/6*(eta[kk[0], kk[2]]*eta[kk[1], kk[3]] - eta[kk[0], kk[3]]*eta[kk[1], kk[2]]) for kk, v in R4.items()}
Tph = sp.zeros(n, n)
for a in range(n):
    for bb in range(n):
        Tph[a, bb] = 8*b*sum(eta[c, c]*eta[dd, dd]*d(phih*C[(a, c, bb, dd)], c, dd) for c in range(n) for dd in range(n))
That = (s**2*Tph).applyfunc(sp.expand)
R, tr, div = Rof(That)
print("   T_hat(phi_h) : trace =", sp.simplify(tr))
pole = False
for key, v in R.items():
    lv = sp.series(sp.simplify(v), s, 0, 1).removeO()
    co = sp.simplify(sp.expand(lv*s).subs(s, 0))
    if co != 0:
        pole = True
    print(f"     R_{''.join(names[i] for i in key)} : coefficient de 1/s = {co}")
print("   pole produit par phi_h lisse :", pole)
print("EXIT 0")
