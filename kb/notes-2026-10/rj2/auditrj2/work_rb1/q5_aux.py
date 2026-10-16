# Verifications auxiliaires :
# (1) operateur indiciel du spineur : det(i s g0 + m) et noyau a s = +-i mu
# (2) operateur indiciel metrique (jauge h_0i = 0, trace nulle) : racines
# (3) transformations de jauge residuelles : delta h_ab = Omega^2 L_xi ghat
import sympy as sp, pickle
from conv import gu, eta, E4, I, g0
s, m, mu = sp.symbols('s m mu')
M = I*s*g0 + m*E4
print("(1) det(i s gamma^0 + m) =", sp.factor(M.det()))
print("    racines en s :", sp.solve(M.det(), s), " => pour s = N + i j mu (N entier >= 0, j entier) : singulier ssi N = 0 et j = +-1 (m = mu)")
Mp = M.subs({s: I*m})
print("    a s = +i mu : i s g0 + m =", list(Mp.subs(m, mu)), " ; image = P- , noyau = P+  => condition de resonance : P+ S != 0")
Hs, E = pickle.load(open('linE.pkl', 'rb'))
Om = sp.Symbol('Omega', positive=True)
sS = sp.Symbol('s')
A = E.applyfunc(lambda e: sp.expand(e).coeff(Om, -4))
H = sp.symbols('H00 H11 H22 H12 H13 H23')
sub = {sp.Symbol('H33'): -H[1]-H[2], sp.Symbol('H01'): 0, sp.Symbol('H02'): 0, sp.Symbol('H03'): 0}
rows = [(0, 0), (1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]
Mat = sp.Matrix([[sp.diff(A[a, b].subs(sub), h) for h in H] for (a, b) in rows])
print("(2) operateur indiciel metrique (composantes 00, 11, 22, 12, 13, 23) : det =", sp.factor(Mat.det().subs(sp.Symbol('s'), sS)))
print("    composantes 0i : partie Omega^{s-2} =", [sp.simplify(A[0, i].subs(sub)) for i in (1, 2, 3)], "(contraintes : apparaissent a l'ordre suivant)")
# (3) jauge
t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
xi = [sp.Function('xi%d' % a)(*X) for a in range(4)]
g = eta/t**2
Lg = sp.Matrix(4, 4, lambda a, b: sum(xi[c]*sp.diff(g[a, b], X[c]) + g[c, b]*sp.diff(xi[c], X[a]) + g[a, c]*sp.diff(xi[c], X[b]) for c in range(4)))
dh = (t**2*Lg).applyfunc(sp.simplify)
print("(3) delta h_00 =", dh[0, 0], " ; delta h_11 =", dh[1, 1])
f = sp.Function('f')(x, y, z); ss = sp.Symbol('sigma')
for lab, x0 in (("xi^0 = c(x) (translation de scri)", sp.Function('c')(x, y, z)), ("xi^0 = t f(x)", t*f), ("xi^0 = (-t)^{1+sigma} f(x)", (-t)**(1+ss)*f)):
    v = sp.simplify(dh[0, 0].subs(xi[0], x0).doit())
    print("    ", lab, ": delta h_00 =", sp.simplify(v))
