# Tache 1 (controle) et tache 2 : tenseur du terme local b * int sqrt(-g) sigma C^2.
import sympy as sp
from sympy.calculus.euler import euler_equations
from geom import *

b = sp.Symbol('b', positive=True)
k = sp.Symbol('k', positive=True)
p = sp.Function('p')(s, x)
q = sp.Function('q')(s, x)
sig = -sp.log(s)

# --- metrique de reference g = eta + eps h, h_yy = p, h_zz = q (generiques)
h = sp.zeros(4); h[2, 2] = p; h[3, 3] = q
g = eta + eps * h
cg = curvature(g, 1)
C1 = [[[[cg['C'][a][bb][c][d].coeff(eps, 1) for d in range(4)] for c in range(4)] for bb in range(4)] for a in range(4)]
# C^2 a l'ordre eps^2 (indices leves par eta)
C2 = sp.expand(sum(C1[a][bb][c][d]**2 * eta[a, a] * eta[bb, bb] * eta[c, c] * eta[d, d]
                   for a in range(4) for bb in range(4) for c in range(4) for d in range(4)))

# --- controle conforme : sqrt(-ghat) Chat^2 = sqrt(-g) C^2 pour ghat = s^-2 g, a l'ordre eps^2
ghat = g / s**2
ch = curvature(ghat, 1)
Ch1 = [[[[ch['C'][a][bb][c][d].coeff(eps, 1) for d in range(4)] for c in range(4)] for bb in range(4)] for a in range(4)]
Ch0 = [[[[ch['C'][a][bb][c][d].coeff(eps, 0) for d in range(4)] for c in range(4)] for bb in range(4)] for a in range(4)]
gi0 = s**2 * eta
Chat2 = sp.expand(sum(Ch1[a][bb][c][d]**2 * gi0[a, a] * gi0[bb, bb] * gi0[c, c] * gi0[d, d]
                      for a in range(4) for bb in range(4) for c in range(4) for d in range(4)))
print('Weyl de dS plat nul (ordre 0) :', all(sp.simplify(Ch0[a][bb][c][d]) == 0 for a in range(4) for bb in range(4) for c in range(4) for d in range(4)))
print('sqrt(-ghat)Chat^2 - sqrt(-g)C^2 (ordre eps^2) :', sp.simplify(s**-4 * Chat2 - C2))

# --- Euler-Lagrange brut sur g de reference : T^{yy} = 2 dS/dg_yy, dg_yy = eps dp
Lag = b * sig * C2           # sqrt(-g) = 1 + O(eps), C^2 = O(eps^2)
EL = euler_equations(Lag, [p, q], [s, x])
dS_dp = EL[0].lhs            # variationnelle dL/dp
T_yy_ref = sp.expand(2 * dS_dp)   # T_yy[g] a l'ordre eps (eps factorise)

# --- Euler-Lagrange brut directement sur ghat (controle independant de T_hat = s^2 T[g])
Lagh = b * sig * s**-4 * Chat2
ELh = euler_equations(Lagh, [p, q], [s, x])
That_yy_direct = sp.expand(2 * s**2 * ELh[0].lhs)   # T^_yy = 2 s^2/eps dS/dp
print('T^_yy(direct sur ghat) - s^2 T_yy[g] :', sp.simplify(That_yy_direct - s**2 * T_yy_ref))

# --- forme fermee candidate : T_ab = c * b * d^c d^d (sigma C_acbd) (indices eta), c a determiner
cand = sp.expand(sum(eta[c, c] * eta[d, d] * sp.diff(sig * C1[2][c][2][d], X[c], X[d]) for c in range(4) for d in range(4)))
cst = sp.simplify(T_yy_ref / (b * cand))
print('rapport T_yy / (b d^c d^d(sigma C_ycyd)) =', cst)

# --- specialisation au mode tensoriel h_yy = -h_zz = u(s) cos kx
u = sp.Function('u')(s)
sub = {p: u * sp.cos(k * x), q: -u * sp.cos(k * x)}
Tyy_mode = sp.simplify(T_yy_ref.subs(sub).doit())
That_mode = sp.simplify(s**2 * Tyy_mode / sp.cos(k * x))
print('T^_yy / cos kx =', sp.collect(sp.expand(That_mode), [b]))
C_sysy = sp.simplify(C1[0][2][0][2].subs(sub).doit() / sp.cos(k * x))
print('C_sysy[eta+eps h]/(eps cos kx) =', sp.expand(C_sysy))

import pickle
pickle.dump(dict(That_mode=That_mode, C_sysy=C_sysy, cst=cst), open('/home/claude/audit_wa/work/t2_out.pkl', 'wb'))
