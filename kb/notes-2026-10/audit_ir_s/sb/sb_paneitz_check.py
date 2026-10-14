# Verifie : ghat = e^{2 sig} eta  =>  sqrt(ghat)(Ehat - 2/3 box_hat Rhat) = 4 box^2 sig (Delta_4 = box^2 sur fond plat)
import sympy as sp
from sb_geom import *
sig = sp.Function('sig')(s, x)
g = sp.exp(2*sig)*sp.diag(-1, 1, 1, 1)
gi, G, Rup, Ric, Rs = geom(g, sp.simplify)
E, C2, _ = invariants(g, gi, Rup, Ric, Rs, sp.simplify)
sq = sp.exp(4*sig)
lhs = sp.simplify(sq*(E - sp.Rational(2, 3)*box(Rs, g, gi, sq, sp.simplify)))
eta = sp.diag(-1, 1, 1, 1)
boxf = lambda f: sum(eta[a, a]*sp.diff(f, X[a], 2) for a in range(n))
print("C^2 de e^{2sig} eta :", sp.simplify(C2))
print("sqrt(g)(E - 2/3 box R) - 4 box^2 sig =", sp.simplify(lhs - 4*boxf(boxf(sig))))
