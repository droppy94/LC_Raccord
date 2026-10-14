import sympy as sp
from sb_lib import *
b, kap, k, gam, al, be = sp.symbols('b kappa k gamma alpha beta', positive=True)
A, B = sp.symbols('A B', real=True)
phi = -sp.log(s); c0 = -8
ghat = s**-2*eta; ghi = s**2*eta; Gam = christoffel_full(ghat)
def Tclosed(C, ph):
    return sp.Matrix(4, 4, lambda a, bb: c0*b*sp.expand(sum(eta[c,c]*eta[d,d]*sp.diff(ph*C[(a,c,bb,d)], X[c], X[d]) for c in range(4) for d in range(4))))
def Rysy(Th):
    tr = sp.simplify(sum(ghi[a,bb]*Th[a,bb] for a in range(4) for bb in range(4)))
    L = (kap/2*(Th - ghat*tr/3)).applyfunc(sp.expand)
    return sp.simplify((covd2(L, Gam, 2, 2, 0) - covd2(L, Gam, 0, 2, 2))/s)
# 1) jauge : h -> h + d_a xi_b + d_b xi_a - (2 xi^s/s) eta  (diffeo de ghat = s^-2(eta+h)) : C lineaire inchange ?
xi = [sp.Function(f'xi{i}')(*X) for i in range(4)]
f = sp.Function('f')(*X)
Hg = sp.Matrix(4, 4, lambda a, c: sp.diff(xi[a], X[c]) + sp.diff(xi[c], X[a])) + f*eta
_, _, _, _, Cg = lin_curv(Hg)
print("1) Weyl lineaire de (d xi + d xi + f eta) identiquement nul :", all(sp.simplify(v) == 0 for v in Cg.values()))
# 2) changement de reference g -> theta^2 g, phi -> phi - ln theta, theta = exp(alpha x + beta s) : contribution polaire de R ?
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(4, 4); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
_, _, _, _, C = lin_curv(H)
Tex = Tclosed(C, -(al*x + be*s))
Rex = Rysy((s**2*Tex).applyfunc(sp.expand))
print("2) residu polaire de R_ysy du terme -b Int ln(theta) C^2 :", sp.limit(s*Rex, s, 0))
# 3) R-E hors vide : u generique
U = sp.Function('U')(s)
H = sp.zeros(4, 4); H[2, 2] = U*sp.cos(k*x); H[3, 3] = -U*sp.cos(k*x)
Rd, Ric, Rs, P, C = lin_curv(H)
Bach = sp.simplify(sum(eta[c,c]*eta[d,d]*sp.diff(C[(2,c,2,d)], X[c], X[d]) for c in range(4) for d in range(4)))
print("3) Bach lineaire de g, composante yy (u generique) :", sp.factor(Bach))
S = sp.diff(U, s, 2) - 2*sp.diff(U, s)/s + k**2*U     # 'source' : ecart a l'equation de mode de Sitter
v = sp.diff(U, s)/s
print("   Bach_yy + (1/4)(2S'/s + S'' + k^2 S) cos kx (S = u''-2u'/s+k^2u) :", sp.simplify(Bach + sp.Rational(1,4)*(2*sp.diff(S, s)/s + sp.diff(S, s, 2) + k**2*S)*sp.cos(k*x)))
T = Tclosed(C, phi); Th = (s**2*T).applyfunc(sp.expand)
lncoef = sp.simplify(sp.expand(Th[2, 2]).coeff(sp.log(s)))
print("   coefficient de ln s dans That_yy :", sp.factor(lncoef), " = -c0 b s^2 Bach_yy ?", sp.simplify(lncoef - (-c0)*b*s**2*Bach) == 0)
# exemple : u = mode B + gamma s^4 (source S = gamma(4 s^2 + k^2 s^4))
ue = B*(sp.sin(k*s) - k*s*sp.cos(k*s)) + gam*s**4
Re = sp.simplify(Rysy(Th).subs(U, ue).doit())
print("   exemple u = mode_B + gamma s^4 : S =", sp.factor(S.subs(U, ue).doit()))
print("     That_yy =", sp.expand(sp.series(sp.simplify(Th[2,2].subs(U, ue).doit()), s, 0, 3).removeO()))
print("     R_ysy  =", sp.expand(sp.series(Re, s, 0, 1).removeO()))
