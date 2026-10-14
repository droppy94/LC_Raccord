"""irr_c.py -- IR-r (NOTE-124/125). Terme de charge de Weyl b*Int sqrt(g) phi C^2, phi = -ln s, sur ghat = s^-2 (eta + eps h).
Partie 0 : controle de la forme fermee T_ab = c0 * d^c d^d (phi C_acbd[h]) contre Euler-Lagrange brut (famille diagonale de M-b).
Partie 1 : mode tensoriel de de Sitter h_yy = -h_zz = u(s) cos kx ; T, That = s^2 T, conservation, trace ; R de (2.17).
"""
import sympy as sp
from sympy.calculus.euler import euler_equations
s = sp.symbols('s', positive=True)
x, y, z = sp.symbols('x y z', real=True)
k, A, B, kap, b, eps = sp.symbols('k A B kappa b epsilon', positive=True)
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1)
phi = -sp.log(s)

def d(f, *ix):
    return sp.diff(f, *[X[i] for i in ix])

def weyl_lin(H):
    """Weyl lineaire (indices bas) de g = eta + H, H d'ordre 1 (on garde l'ordre lineaire)."""
    R4 = {}
    for a in range(n):
        for bb in range(n):
            for c in range(n):
                for dd in range(n):
                    R4[(a, bb, c, dd)] = (d(H[a, dd], bb, c) + d(H[bb, c], a, dd) - d(H[bb, dd], a, c) - d(H[a, c], bb, dd))/2
    Ric = sp.Matrix(n, n, lambda bb, dd: sum(eta[a, a]*R4[(a, bb, a, dd)] for a in range(n)))
    Rs = sum(eta[a, a]*Ric[a, a] for a in range(n))
    C = {}
    for (a, bb, c, dd), v in R4.items():
        C[(a, bb, c, dd)] = sp.expand(v - (eta[a, c]*Ric[bb, dd] - eta[a, dd]*Ric[bb, c] - eta[bb, c]*Ric[a, dd] + eta[bb, dd]*Ric[a, c])/2
                                       + Rs/6*(eta[a, c]*eta[bb, dd] - eta[a, dd]*eta[bb, c]))
    return C

def T_closed(C, c0=1):
    T = sp.zeros(n, n)
    for a in range(n):
        for bb in range(n):
            T[a, bb] = c0*sp.expand(sum(eta[c, c]*eta[dd, dd]*d(phi*C[(a, c, bb, dd)], c, dd) for c in range(n) for dd in range(n)))
    return T

# ---------- Partie 0 : controle
h1, h2, h3 = [sp.Function(f'h{i}')(s, x) for i in (1, 2, 3)]
H0 = sp.diag(0, h1, h2, h3)
C0 = weyl_lin(H0)
C2 = sp.expand(sum(eta[a, a]*eta[bb, bb]*eta[c, c]*eta[dd, dd]*C0[(a, bb, c, dd)]**2
                   for a in range(n) for bb in range(n) for c in range(n) for dd in range(n)))
EL = euler_equations(phi*C2, [h1, h2, h3], [s, x])
ELs = [sp.expand(e.lhs) for e in EL]          # delta S / delta h_i (densite phi*C^2 quadratique)
Tc = T_closed(C0)
# relation attendue : T_ii = 2 dS/dg_ii = 2 dS/dh_i  (eta_ii = +1 pour i spatial) -> T_ii = lambda * EL_i
lam = sp.symbols('lam')
sols = []
for i in (1, 2, 3):
    r = sp.simplify(Tc[i, i] - lam*ELs[i-1])
    sols.append(r)
lam_val = sp.solve(sp.expand(sols[0]).coeff(sp.Derivative(h1, (s, 4))), lam)
print("Partie 0 : facteur lambda tel que T_closed_ii = lambda * EL_i :", lam_val)
ok = all(sp.simplify(sols[i].subs(lam, lam_val[0])) == 0 for i in range(3))
print("   forme fermee = lambda * Euler-Lagrange brut, composantes 1,2,3 :", ok)
# normalisation physique : T_ab(phys. convention) = 2 dS/dg^ab ; dS/dh_i = dS/dg_ii = -dS/dg^ii (au premier ordre) ; on prend T = 2*EL/eps... on fixe c0 = 2/lambda
c0 = sp.Rational(2, 1)/lam_val[0]
print("   c0 retenu (T_ab = c0 * d^c d^d (phi C_acbd)) :", c0, " ; le coefficient b multiplie l'ensemble")

# ---------- Partie 1 : mode tensoriel
u = sp.Function('u')(s)
H = sp.zeros(n, n); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
C = weyl_lin(H)
T = (b*T_closed(C, c0)).applyfunc(sp.expand)
That = (s**2*T).applyfunc(sp.expand)
# conservation physique : nabla_hat^a That_ab, Christoffel de ghat = e^{2 sigma} eta, sigma = -ln s
sig = sp.log(1/s); ds_ = [sp.diff(sig, X[i]) for i in range(n)]
ghat = s**-2*eta; ghi = s**2*eta
Gam = [[[ (1 if a == bb else 0)*ds_[c] + (1 if a == c else 0)*ds_[bb] - eta[bb, c]*sum(eta[a, e]*ds_[e] for e in range(n))
          for c in range(n)] for bb in range(n)] for a in range(n)]
def cov(Tm, a, bb, c):   # nabla_c T_ab
    return sp.diff(Tm[a, bb], X[c]) - sum(Gam[e][c][a]*Tm[e, bb] + Gam[e][c][bb]*Tm[a, e] for e in range(n))
div = [sp.simplify(sum(ghi[a, c]*cov(That, a, bb, c) for a in range(n) for c in range(n))) for bb in range(n)]
tr = sp.simplify(sum(ghi[a, a]*That[a, a] for a in range(n)))
print("Partie 1 : trace ghat^ab That_ab =", tr)
print("   divergence nabla_hat^a That_ab (u quelconque) :", div)
# equation de mode de de Sitter pour u : u'' - (2/s) u' + k^2 u = 0 (en temps conforme, signe sans effet)
modeq = sp.diff(u, s, 2) - 2/s*sp.diff(u, s) + k**2*u
usol = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
print("   controle : u_sol solution de l'equation de mode :", sp.simplify(modeq.subs(u, usol).doit()))
L = (kap/2*(That - ghat*tr/3)).applyfunc(sp.expand)
def Rcomp(r, nu, la):
    return (cov(L, la, r, nu) - cov(L, nu, r, la))/s
def ser(e, N=3):
    e = sp.simplify(e.subs(u, usol).doit())
    return sp.expand(sp.series(e, s, 0, N).removeO())
names = 'sxyz'
print("   That (u = mode de de Sitter), developpement en s :")
for (a, bb) in [(0, 0), (0, 1), (1, 1), (2, 2), (3, 3), (0, 2), (1, 2)]:
    print(f"     That_{names[a]}{names[bb]} =", ser(That[a, bb], 3))
print("   R de (2.17), developpement en s (termes jusqu'a s^1) :")
seen = set()
for r in range(n):
    for nu in range(n):
        for la in range(nu+1, n):
            e = ser(Rcomp(r, nu, la), 2)
            if e != 0:
                print(f"     R_{names[r]}{names[nu]}{names[la]} =", e)
print("EXIT 0")
