# d_a (s^-1 C^a_bcd) [g = eta + h, ordre lineaire] = s^-1 nablahat_a C^a_bcd [ghat = s^-2 g, Christoffel de fond]
import sympy as sp
from sb_lib import *
H = sp.Matrix(4, 4, lambda i, j: sp.Function(f'h{min(i,j)}{max(i,j)}')(*X))
_, _, _, _, C = lin_curv(H)
Cm = {(a, b, c, d): eta[a, a]*C[(a, b, c, d)] for (a, b, c, d) in C}   # C^a_bcd (mixte, invariant conforme)
Gam = christoffel_full(s**-2*eta)
bad = 0
for b in range(4):
    for c in range(4):
        for d in range(4):
            lhs = sum(sp.diff(Cm[(a, b, c, d)]/s, X[a]) for a in range(4))
            nab = sum(sp.diff(Cm[(a, b, c, d)], X[a]) + sum(Gam[a][a][e]*Cm[(e, b, c, d)] - Gam[e][a][b]*Cm[(a, e, c, d)]
                      - Gam[e][a][c]*Cm[(a, b, e, d)] - Gam[e][a][d]*Cm[(a, b, c, e)] for e in range(4)) for a in range(4))
            if sp.simplify(lhs - nab/s) != 0: bad += 1
print("identite conforme de la divergence de Weyl : composantes en defaut =", bad, "/ 64")
