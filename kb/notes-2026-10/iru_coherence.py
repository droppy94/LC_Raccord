"""iru_coherence.py -- IR-u (NOTE-133), sous-question u-3 (ajoute apres iru_transport, prevu au gel §1 'controle de coherence').
Compare (i) le residu du pole de R_rho nu lambda (Friedrich 2.17) calcule avec That[u0] (c0 = +8) et
(ii) la derivee s d/ds du terme log de W_E,yy obtenu par iru_transport (W_E ~ W0 (1 + 8 b kappa ln s)), en unites de W0 = -B k^3 cos(kx)/2.
"""
import sympy as sp
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True)
k, A, B, kap, b = sp.symbols('k A B kappa b', positive=True)
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]; n = 4
eta = sp.diag(-1, 1, 1, 1); ghat = s**-2*eta; ghi = s**2*eta
sig = sp.log(1/s); ds_ = [sp.diff(sig, X[i]) for i in range(n)]
Gam = [[[(1 if a == bb else 0)*ds_[c] + (1 if a == c else 0)*ds_[bb] - eta[bb, c]*sum(eta[a, m]*ds_[m] for m in range(n))
         for c in range(n)] for bb in range(n)] for a in range(n)]
def cov(Tm, a, bb, c):
    return sp.diff(Tm[a, bb], X[c]) - sum(Gam[m][c][a]*Tm[m, bb] + Gam[m][c][bb]*Tm[a, m] for m in range(n))
u0 = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(n, n); H[2, 2] = u0*sp.cos(k*x); H[3, 3] = -u0*sp.cos(k*x)
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
    for bb in range(n):
        T[a, bb] = 8*b*sum(eta[c, c]*eta[q, q]*d(-sp.log(s)*C[(a, c, bb, q)], c, q) for c in range(n) for q in range(n))
That = (s**2*T).applyfunc(sp.expand)
tr = sp.simplify(sum(ghi[a, a]*That[a, a] for a in range(n)))
L = (kap/2*(That - ghat*tr/3)).applyfunc(sp.expand)
W0 = -B*k**3*sp.cos(k*x)/2
names = 'sxyz'
print("trace That =", tr)
for r in range(n):
    for nu in range(n):
        for la in range(nu+1, n):
            v = sp.expand((cov(L, la, r, nu) - cov(L, nu, r, la))/s)
            if v == 0: continue
            co = sp.simplify(sp.series(v*s, s, 0, 1).removeO().subs(s, 0))
            if co != 0:
                print(f"R_{names[r]}{names[nu]}{names[la]} : residu de 1/s = {sp.factor(co)} ; en unites de b kappa W0 : {sp.simplify(co/(b*kap*W0))}")
# cote W : s dW_E/ds du terme log = 8 b kappa W0 (iru_transport) ; Weyl electrique : C_sysy/s, magnetique C_sxyz... pour reference :
CB = sp.simplify(C[(0, 2, 1, 2)])
print("C_syxy (partie magnetique, controle) =", sp.factor(CB))
print("s d/ds [8 b kappa W0 ln s] =", sp.simplify(s*sp.diff(8*b*kap*W0*sp.log(s), s)), "= 8 b kappa W0")
print("EXIT 0")
