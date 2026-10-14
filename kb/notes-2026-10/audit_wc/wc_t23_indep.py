"""wc_t23_indep.py -- audit W-c : reproduction independante de t-2 et t-3, et contre-exemples.
Christoffel calcules directement depuis ghat = s^-2 eta (pas via la formule conforme) ; derivee covariante propre.
R_{rho nu lam} = Omega^-1 (nabla_nu L_{lam rho} - nabla_lam L_{nu rho}), L = (kap/2)(T - ghat trT/3), Omega = s.
"""
import itertools
import sympy as sp
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
k, A, B, kap, b, q = sp.symbols('k A B kappa b q', positive=True)
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1); gh = eta/s**2; ghi = gh.inv()
G = [[[sp.simplify(sum(ghi[a, m]*(sp.diff(gh[m, bb], X[c]) + sp.diff(gh[m, c], X[bb]) - sp.diff(gh[bb, c], X[m]))
                       for m in range(n))/2) for c in range(n)] for bb in range(n)] for a in range(n)]
def nab(T, c, a, bb):   # nabla_c T_{a bb}
    return sp.diff(T[a, bb], X[c]) - sum(G[m][c][a]*T[m, bb] + G[m][c][bb]*T[a, m] for m in range(n))
def Rcomp(T):
    tr = sp.expand(sum(ghi[a, bb]*T[a, bb] for a in range(n) for bb in range(n)))
    L = (kap/2*(T - gh*tr/3)).applyfunc(sp.expand)
    R = {}
    for r, nu, la in itertools.product(range(n), repeat=3):
        if nu < la:
            v = sp.expand((nab(L, nu, la, r) - nab(L, la, nu, r))/s)
            if v != 0:
                R[(r, nu, la)] = v
    div = [sp.simplify(sum(ghi[a, c]*nab(T, c, a, bb) for a in range(n) for c in range(n))) for bb in range(n)]
    return R, sp.simplify(tr), div
def rapport(nom, T):
    R, tr, div = Rcomp(T)
    print(f"== {nom} : trace = {tr} ; div = {div}")
    pole = False
    for key, v in R.items():
        lim = sp.limit(v*s, s, 0)
        lim0 = sp.limit(v, s, 0) if lim == 0 else None
        if lim != 0:
            pole = True
        print(f"   R_{''.join('sxyz'[i] for i in key)} : lim s*R = {sp.simplify(lim)}" + (f" ; lim R = {sp.simplify(lim0)}" if lim0 is not None else ""))
    print(f"   pole 1/s (ou pire) : {pole}")
    return pole
cx = sp.cos(k*x)
y0, y1, y2, f0, f1, w0, w1 = sp.symbols('y0 y1 y2 f0 f1 w0 w1')
yf = y0 + y1*s + y2*s**2
def TT(p, yv):
    T = sp.zeros(n, n); T[2, 2] = s**p*yv*cx; T[3, 3] = -T[2, 2]; return T
print("##### t-2 reproduction")
rapport("p=1, y generique", TT(1, yf))
rapport("p=2, y generique", TT(2, yf))
print("##### t-2 contre-exemples")
rapport("p=1, y0 = 0", TT(1, yf.subs(y0, 0)))
T = sp.zeros(n, n); T[0, 0] = s**2*(f0 + f1*s)*cx
rapport("p=2, Y_ss seul (trace non nulle, non conserve)", T)
T = sp.zeros(n, n); T[0, 1] = T[1, 0] = s**2*(f0 + f1*s)*cx
rapport("p=2, Y_sx seul (sans trace, non conserve)", T)
T = sp.zeros(n, n); T[2, 2] = T[3, 3] = s**2*(f0 + f1*s)*cx
rapport("p=2, Y_yy = Y_zz (trace, non conserve)", T)
T = s**2*(w0 + w1*s)*cx*eta
rapport("p=2, Y = w eta (pure trace)", T)
T = TT(2, sp.log(s)*y0)
rapport("p=2 mais Y non lisse : y = y0 ln s", T)
T = TT(sp.Rational(3, 2), y0)
rapport("p=3/2 (non entier)", T)
# p = 1 : noyau du coefficient du pole pour Y0 constant symetrique quelconque
Ys = sp.symbols('Y0:10'); Y0 = sp.zeros(n, n); it = iter(Ys)
for a in range(n):
    for bb in range(a, n):
        Y0[a, bb] = Y0[bb, a] = next(it)
R, tr, div = Rcomp(s*Y0)
eqs = [sp.limit(v*s, s, 0) for v in R.values()]
sol = sp.solve(eqs, Ys, dict=True)
print("##### p=1, Y0 constant symetrique general : solutions de 'pas de pole' :", sol)
print("      trace(s*Y0) =", tr, "; div =", div)

print("##### t-3 (a)")
box = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
print("box^2 ln s =", sp.simplify(box(box(sp.log(s)))), " (4D, ne depend que de s :", not sp.simplify(box(box(sp.log(s)))).has(x, y, z), ")")
print("##### t-3 contre-exemples : box^2 de candidats non lisses")
for f in [s**2*sp.log(s), s**3*sp.log(s), s*sp.log(s), sp.log(s), 1/s, s**-2]:
    print(f"   box^2({f}) = {sp.simplify(box(box(f)))}")
fs = sp.Function('f')
print("   solutions de box^2 f(s) = 0 :", sp.dsolve(sp.diff(fs(s), s, 4), fs(s)))
print("   solutions de box^2 [f(s) cos(q x)] = 0 :", sp.dsolve(sp.diff(fs(s), s, 4) + 2*q**2*sp.diff(fs(s), s, 2) + q**4*fs(s), fs(s)))
# famille : s^a cos qx, test d'une puissance singuliere
al = sp.symbols('alpha')
ex = sp.simplify(box(box(s**al*sp.cos(q*x)))/(s**(al-4)*sp.cos(q*x)))
print("   box^2(s^alpha cos qx)/(s^(alpha-4) cos qx) =", sp.factor(ex), " -> nul pour tout s ssi q=0 et alpha in {0,1,2,3}")

print("##### t-3 (b) reproduction, phi_h plus general que le polynome, et phi singuliers")
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(n, n); H[2, 2] = u*cx; H[3, 3] = -u*cx
dd_ = lambda f, *ix: sp.diff(f, *[X[i] for i in ix])
R4 = {(a, bb, c, d): (dd_(H[a, d], bb, c) + dd_(H[bb, c], a, d) - dd_(H[bb, d], a, c) - dd_(H[a, c], bb, d))/2
      for a, bb, c, d in itertools.product(range(n), repeat=4)}
Ric = sp.Matrix(n, n, lambda bb, d: sum(eta[a, c]*R4[(a, bb, c, d)] for a in range(n) for c in range(n)))
Rs = sum(eta[a, c]*Ric[a, c] for a in range(n) for c in range(n))
C = {}
for (a, bb, c, d), v in R4.items():
    C[(a, bb, c, d)] = sp.expand(v - (eta[a, c]*Ric[bb, d] - eta[a, d]*Ric[bb, c] - eta[bb, c]*Ric[a, d] + eta[bb, d]*Ric[a, c])/2
                                 + Rs/6*(eta[a, c]*eta[bb, d] - eta[a, d]*eta[bb, c]))
# verification Weyl sans trace
print("   Weyl sans trace :", all(sp.simplify(sum(eta[a, c]*C[(a, bb, c, d)] for a in range(n) for c in range(n))) == 0 for bb in range(n) for d in range(n)))
def Tphi(phi):
    T = sp.zeros(n, n)
    for a in range(n):
        for bb in range(n):
            T[a, bb] = 8*b*sum(eta[c, c]*eta[d, d]*dd_(phi*C[(a, c, bb, d)], c, d) for c in range(n) for d in range(n))
    return (s**2*T).applyfunc(sp.expand)
c1, c2, c3, c4 = sp.symbols('c1:5')
cands = {
  "polynome du script (c1 s + c2 s^2 + c3 s^3 + c4(x^2+s^2))": c1*s + c2*s**2 + c3*s**3 + c4*(x**2 + s**2),
  "onde [(c1+c2 s)cos qs + (c3+c4 s) sin qs] cos qy": ((c1 + c2*s)*sp.cos(q*s) + (c3 + c4*s)*sp.sin(q*s))*sp.cos(q*y),
  "s^2 ln s (non solution)": s**2*sp.log(s),
  "s^3 ln s (non solution)": s**3*sp.log(s),
  "ln s (= -sigma, non solution)": sp.log(s),
}
for nom, phi in cands.items():
    print(f"   -- phi = {nom} : box^2 phi = {sp.simplify(box(box(phi)))}")
    rapport(f"T_hat(phi = {nom})", Tphi(phi))
print("EXIT 0")
