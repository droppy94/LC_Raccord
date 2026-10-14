# test de l'operateur EL maison contre euler_equations sur un cas non lineaire
import sympy as sp
from sympy.calculus.euler import euler_equations
from sb_geom import EL, s, x
f = sp.Function('f')(s, x)
L = sp.log(s)*sp.diff(f, s, 2)**2 + s*f*sp.diff(f, x)**2 + sp.diff(f, s, x)*sp.diff(f, x, 2)
print("EL maison - euler_equations :", sp.simplify(EL(L, f, [s, x]) - euler_equations(L, [f], [s, x])[0].lhs))
