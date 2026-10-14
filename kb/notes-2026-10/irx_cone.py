"""irx_cone.py -- IR-x (NOTE-139/140). Solutions de cone de box^2 pour phi_h, sigma = r^2 - s^2.
x-1 : box^2 = 0 hors cone pour ln sigma, 1/sigma, s/sigma (4D, box = -d_s^2 + Laplacien).
x-2 : phi_h = ln sigma (sommet a l'origine de scri+) ; T = -8b d^c d^d(phi_h C_acbd) (convention physique NOTE-138), T_hat = s^2 T ;
      R de (2.17) : (i) en un point de scri+ distinct du sommet (x,y,z) = (X0,Y0,0), coefficient de 1/s ; (ii) ordre de singularite sur le cone.
x-3 : ansatz phi = sum_n (a_n(x,y,z) + c_n(x,y,z) ln s) s^n, n = 0..7 ; box^2 phi = 0 ordre par ordre : les c_n sont-ils forces a 0 ?
x-4 : phi = f(s) seule : box^2 f = f'''' = 0 => cubique.
"""
import sympy as sp
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
k, A, B, kap, b = sp.symbols('k A B kappa b', positive=True)
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1)
box = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
sig = x**2 + y**2 + z**2 - s**2
# ---------------- x-1
print("x-1 :")
for nom, f in (("ln sigma", sp.log(sig)), ("1/sigma", 1/sig), ("s/sigma", s/sig), ("controle ln s", sp.log(s))):
    print(f"   box^2({nom}) =", sp.simplify(box(box(f))))
# ---------------- x-2
print("x-2 :")
phih = sp.log(sig)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(n, n); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
d = lambda f, *ix: sp.diff(f, *[X[i] for i in ix])
R4 = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for q in range(n):
                R4[(a, bb, c, q)] = (d(H[a, q], bb, c) + d(H[bb, c], a, q) - d(H[bb, q], a, c) - d(H[a, c], bb, q))/2
Ric = sp.Matrix(n, n, lambda bb, q: sum(eta[a, a]*R4[(a, bb, a, q)] for a in range(n)))
Rs = sum(eta[a, a]*Ric[a, a] for a in range(n))
C = {kk: v - (eta[kk[0], kk[2]]*Ric[kk[1], kk[3]] - eta[kk[0], kk[3]]*Ric[kk[1], kk[2]] - eta[kk[1], kk[2]]*Ric[kk[0], kk[3]] + eta[kk[1], kk[3]]*Ric[kk[0], kk[2]])/2
     + Rs/6*(eta[kk[0], kk[2]]*eta[kk[1], kk[3]] - eta[kk[0], kk[3]]*eta[kk[1], kk[2]]) for kk, v in R4.items()}
T = sp.zeros(n, n)
for a in range(n):
    for bb in range(a, n):
        T[a, bb] = -8*b*sum(eta[c, c]*eta[q, q]*d(phih*C[(a, c, bb, q)], c, q) for c in range(n) for q in range(n))
        T[bb, a] = T[a, bb]
That = s**2*T
ghat = s**-2*eta; ghi = s**2*eta
ds_ = [sp.diff(-sp.log(s), X[i]) for i in range(n)]
Gam = [[[(1 if a == bb else 0)*ds_[c] + (1 if a == c else 0)*ds_[bb] - eta[bb, c]*sum(eta[a, m]*ds_[m] for m in range(n))
         for c in range(n)] for bb in range(n)] for a in range(n)]
tr = sum(ghi[a, a]*That[a, a] for a in range(n))
print("   trace T_hat (simplifiee) =", sp.simplify(tr))
L = kap/2*(That - ghat*tr/3)
def cov(Tm, a, bb, c):
    return sp.diff(Tm[a, bb], X[c]) - sum(Gam[m][c][a]*Tm[m, bb] + Gam[m][c][bb]*Tm[a, m] for m in range(n))
X0, Y0 = sp.Rational(3, 2), sp.Rational(1, 2)
names = 'sxyz'
pole_hors_sommet = False
comps = {}
for r in range(n):
    for nu in range(n):
        for la in range(nu+1, n):
            v = (cov(L, la, r, nu) - cov(L, nu, r, la))/s
            comps[(r, nu, la)] = v
            vp = v.subs({x: X0, y: Y0, z: 0})
            ser = sp.series(sp.simplify(vp*s), s, 0, 2).removeO()
            co = sp.simplify(ser.subs(s, 0))
            if co != 0:
                pole_hors_sommet = True
            print(f"   R_{names[r]}{names[nu]}{names[la]} en (x,y,z) = ({X0},{Y0},0) : coefficient de 1/s = {co}")
print("   pole en un point de scri+ distinct du sommet :", pole_hors_sommet)
# ordre de singularite sur le cone : le long de la droite y = z = 0, x = s + e, s = 1/2 fixe, e -> 0+
e = sp.symbols('e', positive=True)
vmax = None
for key, v in comps.items():
    ve = sp.simplify(v.subs({y: 0, z: 0, s: sp.Rational(1, 2), x: sp.Rational(1, 2) + e, k: 1, A: 0, B: 1}))
    if ve == 0:
        continue
    lead = sp.series(ve, e, 0, 0).removeO()
    order = min(sp.Poly(sp.expand(lead*e**6), e).monoms())[0] - 6 if lead != 0 else None
    print(f"   R_{''.join(names[i] for i in key)} pres du cone (x = s + e) : terme dominant ~ e^{order}")
# ---------------- x-3
print("x-3 :")
N = 8
a_ = [sp.Function(f'a{i}')(x, y, z) for i in range(N)]
c_ = [sp.Function(f'c{i}')(x, y, z) for i in range(N)]
Ls = sp.log(s)
phi = sum(a_[i]*s**i + c_[i]*s**i*Ls for i in range(N))
eq = sp.expand(box(box(phi))*s**4)
sol = {}
for p in range(0, N):
    for lp in (1, 0):
        co = sp.expand(eq).coeff(s, p)
        co = sp.expand(co).coeff(Ls, 1) if lp else sp.expand(co).subs(Ls, 0)
        co = sp.simplify(co.subs(sol).doit())
        if co == 0:
            continue
        # resoudre pour le c_n de plus bas indice non encore fixe
        for i in range(N):
            if c_[i] not in sol and co.has(c_[i]):
                si = sp.solve(co, c_[i])
                if si:
                    sol[c_[i]] = sp.simplify(si[0])
                    print(f"   ordre s^{p-4}{' ln s' if lp else ''} : c{i} = {sol[c_[i]]}")
                break
print("   conclusion : c0..c4 forces a zero ->", all(sol.get(c_[i], None) == 0 for i in range(5)))
# ---------------- x-4
print("x-4 :")
f = sp.Function('f')
print("   box^2 f(s) =", sp.simplify(box(box(f(s)))), " ; solution generale :", sp.dsolve(sp.diff(f(s), s, 4), f(s)))
print("EXIT 0")
