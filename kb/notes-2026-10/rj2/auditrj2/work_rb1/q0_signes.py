# Fixe par calcul : (i) le signe c de la connexion spinorielle, (ii) le signe global de T (T_00>0), (iii) trace = -m psibar psi
import sympy as sp
from conv import gu, gl, eta, E4, I, g0
from dirac_curved import Geo

t, x, y, z = sp.symbols('t x y z', real=True)
X = (t, x, y, z)
A = sp.Function('A')(t, x); B = sp.Function('B')(t, x); C = sp.Function('C')(t, y)
E = sp.diag(1/A, 1/B, 1/C, 1)   # repere non conforme, test generique
geo = Geo(E, X)
c = sp.Symbol('c')
eqs = []
for mu in range(4):
    for nu in range(4):
        M = sp.simplify(geo.nabla_gamma(mu, nu, c))
        eqs += [e for e in M if e != 0]
sol = sp.solve(eqs, c, dict=True)
print("(i) nabla_mu gamma^nu = 0 impose c =", sol)

# (ii) onde plane d'energie positive en espace plat
m, p = sp.symbols('m p', positive=True)
Ep = sp.sqrt(p**2 + m**2)
geo0 = Geo(E4, X, c=sp.Rational(-1, 4) if not sol else sol[0][c])
# solution : (i gamma^a d_a - m) psi = 0, psi = u exp(-i E t + i p x)
u = sp.Matrix(sp.symbols('u0:4'))
M = I*(gu[0]*(-I*Ep) + gu[1]*(I*p)) - m*E4
ns = M.nullspace()
uu = ns[0]
psi = uu*sp.exp(-I*Ep*t + I*p*x)
chi = (psi.H*g0)
print("    verif. equation de Dirac :", sp.simplify(I*geo0.slashD(psi) - m*psi).T)
T = geo0.T(psi, chi)
T00 = sp.simplify(T[0, 0]); dens = sp.simplify((psi.H*psi)[0, 0])
print("(ii) T_00 / (psi^dag psi) =", sp.simplify(T00/dens), " (attendu +E>0)")
tr = sp.simplify(sum(eta[a, a]*T[a, a] for a in range(4)))
pbp = sp.simplify((chi*psi)[0, 0])
print("(iii) trace T / (psibar psi) =", sp.simplify(tr/pbp), " (attendu -m)")
