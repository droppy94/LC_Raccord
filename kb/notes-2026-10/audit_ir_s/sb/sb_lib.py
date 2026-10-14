"""Bibliotheque independante (auditeur S-b). Courbure lineaire via Christoffel tronques, conventions:
R^a_{bcd} = d_c Gam^a_{bd} - d_d Gam^a_{bc} + ..., Ric_bd = R^a_{bad}, P = (Ric - R g/6)/2, C = Riem - (g ^ P)."""
import sympy as sp
s = sp.symbols('s', positive=True)
x, y, z = sp.symbols('x y z', real=True)
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1)

def lin_curv(H):
    """Riemann (indices bas), Ricci, Schouten, Weyl lineaires de g = eta + H via Gamma lineaires."""
    Gl = [[[sum(eta[a, a]*0 for _ in [0]) for c in range(n)] for b in range(n)] for a in range(n)]
    # Gamma_{a b c} (indice bas) lineaire
    Gd = [[[ (sp.diff(H[a, b], X[c]) + sp.diff(H[a, c], X[b]) - sp.diff(H[b, c], X[a]))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    Gu = [[[eta[a, a]*Gd[a][b][c] for c in range(n)] for b in range(n)] for a in range(n)]
    Rup = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Rup[(a, b, c, d)] = sp.diff(Gu[a][b][d], X[c]) - sp.diff(Gu[a][b][c], X[d])
    Rd = {k: eta[k[0], k[0]]*v for k, v in Rup.items()}
    Ric = sp.Matrix(n, n, lambda b, d: sum(Rup[(a, b, a, d)] for a in range(n)))
    Rs = sum(eta[a, a]*Ric[a, a] for a in range(n))
    P = (Ric - Rs*eta/6)/2
    C = {}
    for (a, b, c, d), v in Rd.items():
        C[(a, b, c, d)] = sp.expand(v - (eta[a, c]*P[b, d] - eta[a, d]*P[b, c] - eta[b, c]*P[a, d] + eta[b, d]*P[a, c]))
    return Rd, Ric, Rs, P, C

def christoffel_full(g):
    gi = g.inv()
    return [[[sp.simplify(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) for e in range(n))/2)
              for c in range(n)] for b in range(n)] for a in range(n)]

def covd2(Tm, Gam, a, b, c):
    """nabla_c T_ab"""
    return sp.diff(Tm[a, b], X[c]) - sum(Gam[e][c][a]*Tm[e, b] + Gam[e][c][b]*Tm[a, e] for e in range(n))
