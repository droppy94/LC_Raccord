# Taches 3-5 : equation d'Einstein linearisee completee (yy), reduction d'ordre, Weyl electrique.
import pickle
import sympy as sp
from geom import *

b = sp.Symbol('b', positive=True)
k = sp.Symbol('k', positive=True)
G = sp.Symbol('G', positive=True)
A, B = sp.symbols('A B', real=True)
Lam = 3
d = pickle.load(open('/home/claude/audit_wa/work/t2_out.pkl', 'rb'))
That_mode, C_sysy = d['That_mode'], d['C_sysy']

u = sp.Function('u')(s)
h = sp.zeros(4); h[2, 2] = u * sp.cos(k * x); h[3, 3] = -u * sp.cos(k * x)
ghat = (eta + eps * h) / s**2
c = curvature(ghat, 1)
Ein = (c["Ric"] - c["Rs"] * ghat / 2 + Lam * ghat).applyfunc(sp.expand)
E0 = sp.simplify(Ein.applyfunc(lambda e: e.coeff(eps, 0)))
print('fond : G+Lambda g a l ordre 0 =', E0 == sp.zeros(4))
Eyy = sp.simplify(Ein[2, 2].coeff(eps, 1) / sp.cos(k * x))
print('delta(G+Lg)_yy / (eps cos kx) =', sp.factor(Eyy))
# autres composantes a l ordre eps (coherence du mode TT)
for (i, j) in [(0, 0), (0, 1), (1, 1), (0, 2), (2, 3), (3, 3)]:
    print('  comp', (i, j), sp.simplify(Ein[i, j].coeff(eps, 1) + (Ein[2, 2].coeff(eps, 1) if (i, j) == (3, 3) else 0)))

u0 = A * (sp.cos(k * s) + k * s * sp.sin(k * s)) + B * (sp.sin(k * s) - k * s * sp.cos(k * s))
print('u0 solution du vide :', sp.simplify(Eyy.subs(u, u0).doit()))

# --- source : 8 pi G T^_yy evaluee sur u0
src = sp.simplify((That_mode.subs(u, u0).doit()))
print('T^_yy[u0]/cos kx =', sp.simplify(src))
# Equation : Eyy[u0 + G u1] = 8 pi G T^_yy[u0]  => Eyy[u1] = 8 pi T^_yy[u0]
# Eyy est lineaire : Eyy = alpha(s) (u'' - 2u'/s + k^2 u) a verifier
alpha = sp.simplify(Eyy / (sp.diff(u, s, 2) - 2 * sp.diff(u, s) / s + k**2 * u))
print('alpha(s) =', alpha)
F = sp.simplify(8 * sp.pi * src / alpha)    # u1 - 2u1/s + k^2 u1 = F
print('F(s) =', sp.simplify(F))

# --- resolution exacte par variation des constantes
y1 = sp.cos(k * s) + k * s * sp.sin(k * s)
y2 = sp.sin(k * s) - k * s * sp.cos(k * s)
Wr = sp.simplify(y1 * sp.diff(y2, s) - y2 * sp.diff(y1, s))
print('Wronskien =', Wr)

# --- resolution en serie pres de s=0 (ansatz avec log), ordre N
N = 7
L = sp.log(s)
a = sp.symbols('a0:%d' % (N + 1)); cc = sp.symbols('c0:%d' % (N + 1))
u1 = sum((a[n] + cc[n] * L) * s**n for n in range(N + 1))
Fser = sp.expand(sp.series(F, s, 0, N - 1).removeO())
res = sp.expand((sp.diff(u1, s, 2) - 2 * sp.diff(u1, s) / s + k**2 * u1 - Fser) * s**2)
eqs = []
for n in range(0, N):
    for lp in range(0, 3):
        eqs.append(res.coeff(s, n).coeff(L, lp) if lp > 0 else res.coeff(s, n).subs(L, 0))
sol = sp.solve(eqs, list(a) + list(cc), dict=True)
print('nb solutions serie :', len(sol))
sol = sol[0]
u1s = sp.expand(u1.subs(sol))
print('u1 (serie) =', sp.collect(u1s, [L, s]))
# libertes residuelles (homogenes) : on les note
free = [v for v in list(a) + list(cc) if v in u1s.free_symbols]
print('parametres libres (solutions homogenes absorbables dans A,B) :', free)
# verification directe du residu
chk = sp.series(sp.expand((sp.diff(u1s, s, 2) - 2 * sp.diff(u1s, s) / s + k**2 * u1s - F)), s, 0, N - 3).removeO()
print('residu ODE (doit etre 0 jusqu a s^%d) :' % (N - 4), sp.simplify(chk))

# --- Weyl electrique rescale W_E = C_sysy/s, en unites eps cos kx
utot = u0 + G * u1s
WE = sp.expand(C_sysy.subs(u, utot).doit() / s)
WE_ser = sp.expand(sp.series(WE, s, 0, 3).removeO())
print('W_E (serie, ordre G^1) =', sp.collect(sp.expand(WE_ser), [G, L, s]))
WE0 = sp.expand(sp.series(C_sysy.subs(u, u0).doit() / s, s, 0, 3).removeO())
WE1 = sp.expand(sp.series(C_sysy.subs(u, u1s).doit() / s, s, 0, 3).removeO())
print('W_E0 =', sp.collect(WE0, s))
print('W_E1 =', sp.collect(WE1, [L, s]))
pickle.dump(dict(Eyy=Eyy, src=src, F=F, u1s=u1s, WE0=WE0, WE1=WE1, alpha=alpha), open('/home/claude/audit_wa/work/t3_out.pkl', 'wb'))
