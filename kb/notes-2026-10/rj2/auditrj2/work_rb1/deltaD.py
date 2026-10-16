# Perturbation au 1er ordre de l'operateur de Dirac pour g_c = eta + eps h (repere symetrique e_a^mu = delta - eps/2 h^mu_a)
import sympy as sp
from conv import gu, gl, eta, E4, I

def deltaD(h, psi, X):
    """h : matrice 4x4 h_{mu nu} (expressions), psi : colonne. Renvoie delta(gamma^mu nabla_mu) psi au 1er ordre."""
    hud = sp.Matrix(4, 4, lambda mu_, a: sum(eta[mu_, n]*h[n, a] for n in range(4)))   # h^mu_a
    # delta Gamma^nu_{mu lam} = 1/2 eta^{nu rho}(d_mu h_{rho lam} + d_lam h_{rho mu} - d_rho h_{mu lam})
    dG = lambda nu, mu_, lam: sum(eta[nu, r]*(sp.diff(h[r, lam], X[mu_]) + sp.diff(h[r, mu_], X[lam]) - sp.diff(h[mu_, lam], X[r])) for r in range(4))/2
    # omega_mu^a_b (1er ordre) = -1/2 d_mu h^a_b + dGamma^a_{mu b}
    om = lambda mu_, a, b: -sp.Rational(1, 2)*sp.diff(hud[a, b], X[mu_]) + dG(a, mu_, b)
    out = sp.zeros(4, 1)
    for mu_ in range(4):
        Gm = -sp.Rational(1, 4)*sum((om(mu_, a, d)*eta[d, b]*gl[a]*gl[b] for a in range(4) for b in range(4) for d in range(4)), sp.zeros(4))
        out += gu[mu_]*Gm*psi
        out += -sp.Rational(1, 2)*sum((hud[mu_, a]*gu[a] for a in range(4)), sp.zeros(4))*sp.diff(psi, X[mu_])
    return out

if __name__ == "__main__":
    # verification contre le calcul exact (classe Geo) sur un exemple
    from dirac_curved import Geo
    t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
    eps = sp.Symbol('epsilon')
    f = [sp.Function('f%d' % i)(t, x) for i in range(5)]
    h = sp.Matrix([[f[0], f[1], 0, 0], [f[1], f[2], f[3], 0], [0, f[3], f[4], 0], [0, 0, 0, 0]])
    hud = sp.Matrix(4, 4, lambda mu_, a: sum(eta[mu_, n]*h[n, a] for n in range(4)))
    Emat = sp.Matrix(4, 4, lambda a, mu_: (1 if a == mu_ else 0) - eps/2*hud[mu_, a])
    psi = sp.Matrix([sp.Function('p%d' % i)(t, x) for i in range(4)])
    geo = Geo(Emat, X, c=sp.Rational(-1, 4))
    full = geo.slashD(psi)
    first = full.applyfunc(lambda e: sp.simplify(sp.diff(e, eps).subs(eps, 0)))
    print("metrique du repere = eta + eps h + O(eps^2) :", sp.simplify((geo.g - eta - eps*h).applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0))) == sp.zeros(4))
    print("deltaD (formule) = d/deps Dslash|_0 (calcul exact) :", sp.simplify(first - deltaD(h, psi, X)) == sp.zeros(4, 1))
