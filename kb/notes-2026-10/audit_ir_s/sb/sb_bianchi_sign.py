# Controle du signe de l'identite de Bianchi contractee : d^a C_abcd = +/- (d_c P_db - d_d P_cb), h generique lineaire
import sympy as sp
from sb_lib import *
H = sp.Matrix(4, 4, lambda i, j: sp.Function(f'h{min(i,j)}{max(i,j)}')(*X))
Rd, Ric, Rs, P, C = lin_curv(H)
bad = 0
for b in range(4):
    for c in range(4):
        for d in range(4):
            lhs = sum(eta[a, a]*sp.diff(C[(a, b, c, d)], X[a]) for a in range(4))
            rhs = sp.diff(P[d, b], X[c]) - sp.diff(P[c, b], X[d])
            if sp.expand(lhs - rhs) != 0: bad += 1
print("d^a C_abcd - (d_c P_db - d_d P_cb) non nul pour", bad, "composantes sur 64")
