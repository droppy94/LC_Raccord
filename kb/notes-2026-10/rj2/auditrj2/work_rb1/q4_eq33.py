# Q4 : verification de (3.3) de Friedrich :  6 Omega s - 3 g(dOmega,dOmega) - lambda = -(1/4) That
# avec s = (1/4) box_g Omega + Omega R[g]/24,  ghat = Omega^{-2} g,  G^ + lambda g^ = T^ (kappa = 1)
import sympy as sp
from dirac_curved import christoffel
t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
A = sp.Function('A')(t, x); B = sp.Function('B')(t, y); w = sp.Function('w')(t, x, y)
g = sp.diag(-A**2, B**2, 1, A*B)
Om = sp.exp(w)
def ricci_scalar(g):
    G = christoffel(g, X); gi = g.inv()
    Ric = sp.zeros(4)
    for b in range(4):
        for d in range(4):
            Ric[b, d] = sum(sp.diff(G[a][b][d], X[a]) - sp.diff(G[a][b][a], X[d]) + sum(G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a] for e in range(4)) for a in range(4))
    return sp.simplify(sum(gi[b, d]*Ric[b, d] for b in range(4) for d in range(4))), G
R, G = ricci_scalar(g)
Rh, _ = ricci_scalar(Om**-2*g)
gi = g.inv()
grad2 = sum(gi[a, b]*sp.diff(Om, X[a])*sp.diff(Om, X[b]) for a in range(4) for b in range(4))
box = sum(gi[a, b]*(sp.diff(Om, X[a], X[b]) - sum(G[c][a][b]*sp.diff(Om, X[c]) for c in range(4))) for a in range(4) for b in range(4))
print("Rhat = Omega^2 R + 6 Omega box Omega - 12 |dOmega|^2 :", sp.simplify(Rh - (Om**2*R + 6*Om*box - 12*grad2)) == 0)
lam, That = sp.symbols('lambda That')
s = box/4 + Om*R/24
# trace de l'equation d'Einstein : Rhat = 4 lambda - That
lhs = 6*Om*s - 3*grad2 - lam
print("6 Omega s - 3|dOmega|^2 - lambda - (Rhat/4 - lambda) = 0 :", sp.simplify(lhs - (Rh/4 - lam)) == 0,
      "  => avec Rhat = 4 lambda - That : 6 Omega s - 3|dOmega|^2 - lambda = -That/4  [(3.3) verifiee]")
