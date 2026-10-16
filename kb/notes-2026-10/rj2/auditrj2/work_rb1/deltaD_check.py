# verification de deltaD : (a) cas conforme h = 2 f eta (formule analytique), (b) h explicite non conforme vs calcul exact (Geo)
import sympy as sp
from conv import gu, eta, E4, I
from deltaD import deltaD
from dirac_curved import Geo
t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
eps = sp.Symbol('epsilon')
psi = sp.Matrix([sp.Function('p%d' % i)(t, x) for i in range(4)])
# (a) conforme : g = (1+2 eps f) eta = e^{2 phi} eta + O(eps^2), phi = eps f ; Dslash = e^{-phi}(gamma.d + 3/2 gamma^a d_a phi)
f = sp.Function('f')(t, x)
h = 2*f*eta
ref = -f*sum((gu[a]*psi.diff(X[a]) for a in range(4)), sp.zeros(4, 1)) + sp.Rational(3, 2)*sum((gu[a]*f.diff(X[a]) for a in range(4)), sp.zeros(4))*psi
print("(a) cas conforme : deltaD = formule analytique :", sp.simplify(deltaD(h, psi, X) - ref) == sp.zeros(4, 1), flush=True)
# (b) h explicite non conforme
hb = sp.Matrix([[t*x, sp.sin(x), 0, 0], [sp.sin(x), t**2, x, 0], [0, x, 0, 0], [0, 0, 0, t]])
hud = sp.Matrix(4, 4, lambda mu_, a: sum(eta[mu_, n]*hb[n, a] for n in range(4)))
Emat = sp.Matrix(4, 4, lambda a, mu_: (1 if a == mu_ else 0) - eps/2*hud[mu_, a])
geo = Geo(Emat, X, c=sp.Rational(-1, 4))
full = geo.slashD(psi)
first = full.applyfunc(lambda e: sp.simplify(sp.diff(e, eps).subs(eps, 0)))
print("(b) h explicite non conforme : deltaD = d/deps Dslash|_0 (calcul exact) :", sp.simplify(first - deltaD(hb, psi, X)) == sp.zeros(4, 1))
