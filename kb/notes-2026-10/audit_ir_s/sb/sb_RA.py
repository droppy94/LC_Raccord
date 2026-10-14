# R-A independant : variation brute de S = Int phi C^2 (phi=-ln s) vs forme fermee d^c d^d(phi C_acbd), 10 composantes h_ab(s,x)
import sympy as sp
from sympy.calculus.euler import euler_equations
from sb_lib import *
phi = -sp.log(s)
names = {}
H = sp.zeros(4, 4); funcs = []
for i in range(4):
    for j in range(i, 4):
        f = sp.Function(f'h{i}{j}')(s, x); funcs.append((i, j, f)); H[i, j] = f; H[j, i] = f
Rd, Ric, Rs, P, C = lin_curv(H)
C2 = sp.expand(sum(eta[a,a]*eta[b,b]*eta[c,c]*eta[d,d]*C[(a,b,c,d)]**2 for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
EL = euler_equations(phi*C2, [f for (_, _, f) in funcs], [s, x])
closed = lambda a, b: sp.expand(sum(eta[c,c]*eta[d,d]*sp.diff(phi*C[(a,c,b,d)], X[c], X[d]) for c in range(4) for d in range(4)))
ok = True
for (i, j, f), e in zip(funcs, EL):
    # dS/dh_ij (une seule fonction pour (ij) et (ji)) = (2 - delta_ij) dS/dg_ij ; attendu dS/dg_ij = -4 d_c d_d(phi C^icjd) (indices hauts)
    mult = 1 if i == j else 2
    r = sp.simplify(sp.expand(e.lhs) - mult*(-4)*eta[i,i]*eta[j,j]*closed(i, j))
    if r != 0: ok = False; print("ecart", i, j, r)
print("dS/dg_ab = -4 d_c d_d(phi C^acbd) pour les 10 composantes :", ok)
print("=> T^ab = 2 dS/dg_ab donne c0 = -8 ; T_ab = 2 dS/dg^ab (= -2 dS/dg_ab) donne c0 = +8")
