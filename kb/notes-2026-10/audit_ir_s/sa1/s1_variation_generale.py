# S-a1 script 1 : variation brute d'Euler-Lagrange de S2 = b*Int phi * C1.C1 (ordre eps^2 autour de eta)
# et comparaison a la forme fermee T_ab = lam * b * d^c d^d (phi C1_acbd), h generique.
import sympy as sp
from sympy.calculus.euler import euler_equations
s,x,y,z = sp.symbols('s x y z', real=True)
X = [s,x,y,z]
b = sp.symbols('b')
eta = sp.diag(-1,1,1,1)
phi = sp.Function('phi')(s,x,y,z)   # phi generique (on specialisera)
H = {}
for m in range(4):
    for n in range(m,4):
        H[(m,n)] = sp.Function(f'h{m}{n}')(*X)
def h(m,n): return H[(min(m,n),max(m,n))]
d = sp.diff
# Riemann linearise R1_abcd
def R1(a,b_,c,e):
    return sp.Rational(1,2)*(d(h(a,e),X[b_],X[c]) + d(h(b_,c),X[a],X[e]) - d(h(b_,e),X[a],X[c]) - d(h(a,c),X[b_],X[e]))
Rm = [[[[R1(a,b_,c,e) for e in range(4)] for c in range(4)] for b_ in range(4)] for a in range(4)]
Ric = [[sum(eta[c,c]*Rm[c][a][c][b_] for c in range(4)) for b_ in range(4)] for a in range(4)]
Rs = sum(eta[a,a]*Ric[a][a] for a in range(4))
def C1(a,b_,c,e):
    return (Rm[a][b_][c][e] - sp.Rational(1,2)*(eta[a,c]*Ric[b_][e] - eta[a,e]*Ric[b_][c] - eta[b_,c]*Ric[a][e] + eta[b_,e]*Ric[a][c])
            + Rs/6*(eta[a,c]*eta[b_,e]-eta[a,e]*eta[b_,c]))
C = {}
for a in range(4):
    for b_ in range(4):
        for c in range(4):
            for e in range(4):
                C[(a,b_,c,e)] = C1(a,b_,c,e)
C2 = sp.expand(sum(eta[a,a]*eta[b_,b_]*eta[c,c]*eta[e,e]*C[(a,b_,c,e)]**2
               for a in range(4) for b_ in range(4) for c in range(4) for e in range(4)))
L = b*phi*C2
funcs = [H[k] for k in sorted(H)]
eqs = euler_equations(L, funcs, X)
# dS/dg_{mn} symetrique : EL wrt h_mn (m<n) = 2 dS/dg_mn
dSdg = sp.zeros(4,4)
for k,eq in zip(sorted(H), eqs):
    m,n = k
    val = eq.lhs
    if m==n: dSdg[m,n] = val
    else:
        dSdg[m,n] = val/2; dSdg[n,m] = val/2
# T_ab = (2/sqrt g) dS/dg^{ab} = -2 eta_ac eta_bd dS/dg_cd  (ordre lineaire)
Tbrute = sp.zeros(4,4)
for a in range(4):
    for b_ in range(4):
        Tbrute[a,b_] = -2*eta[a,a]*eta[b_,b_]*dSdg[a,b_]
# forme fermee candidate
Xf = sp.zeros(4,4)
for a in range(4):
    for b_ in range(4):
        Xf[a,b_] = sum(eta[c,c]*eta[e,e]*d(phi*C[(a,c,b_,e)], X[c], X[e]) for c in range(4) for e in range(4))
lam = sp.symbols('lam')
# determiner lam sur une composante, puis verifier toutes
r = sp.expand(Tbrute[1,2] - lam*b*Xf[1,2])
sol = sp.solve(sp.Poly(r, *[t for t in r.atoms(sp.Derivative)]).coeffs(), lam)
print('lam =', sol)
lamv = sol[lam] if isinstance(sol, dict) else sol[0][0] if isinstance(sol[0], tuple) else sol[0]
ok = all(sp.expand(Tbrute[a,b_] - lamv*b*Xf[a,b_]) == 0 for a in range(4) for b_ in range(4))
print('[calcule] T_brute == lam*b*d^c d^d(phi C_acbd) pour toutes composantes, h et phi generiques :', ok)
