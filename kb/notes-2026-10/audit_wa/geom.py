# Outils geometriques communs (audit W-a). Signature (-,+,+,+), coordonnees (s,x,y,z).
import sympy as sp

s, x, y, z = sp.symbols('s x y z', real=True)
X = [s, x, y, z]
eps = sp.Symbol('epsilon')
eta = sp.diag(-1, 1, 1, 1)


def truncate(e, n):
    """garde les ordres eps^0..eps^n"""
    e = sp.expand(e)
    return sum(e.coeff(eps, i) * eps**i for i in range(n + 1))


def curvature(g, order):
    """Riemann R_abcd (convention R^a_bcd = d_c Gamma^a_bd - ...), Ricci R_bd = R^a_bad,
    scalaire, Weyl C_abcd ; tout tronque a l'ordre eps^order."""
    n = 4
    gi = g.inv() if order is None else sp.Matrix(4, 4, lambda i, j: truncate(sp.series(g.inv()[i, j], eps, 0, order + 1).removeO(), order))
    tr = (lambda e: sp.simplify(e)) if order is None else (lambda e: truncate(e, order))
    Gam = [[[tr(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Rup = [[[[tr(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                 + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
              for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    R = [[[[tr(sum(g[a, e] * Rup[e][b][c][d] for e in range(n))) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(4, 4, lambda b, d: tr(sum(Rup[a][b][a][d] for a in range(n))))
    Rs = tr(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    C = [[[[tr(R[a][b][c][d]
               - sp.Rational(1, 2) * (g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c] - g[b, c] * Ric[a, d] + g[b, d] * Ric[a, c])
               + Rs / 6 * (g[a, c] * g[b, d] - g[a, d] * g[b, c]))
            for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    return dict(gi=gi, R=R, Ric=Ric, Rs=Rs, C=C)
