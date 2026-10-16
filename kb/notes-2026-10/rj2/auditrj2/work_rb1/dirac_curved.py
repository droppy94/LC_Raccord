# Operateur de Dirac et tenseur cinetique en espace courbe, a partir d'un repere e_a^mu
import sympy as sp
from conv import gu, gl, eta, E4, I

def christoffel(g, X):
    gi = sp.simplify(g.inv())
    n = 4
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for k in range(n):
                G[l][m][k] = sp.simplify(sum(gi[l, s]*(sp.diff(g[s, m], X[k]) + sp.diff(g[s, k], X[m]) - sp.diff(g[m, k], X[s])) for s in range(n))/2)
    return G  # G[l][m][k] = Gamma^l_{mk}

class Geo:
    def __init__(self, E, X, c=None):
        """E[a,mu] = e_a^mu (repere orthonorme)"""
        self.E = E; self.X = X
        self.Einv = sp.simplify(E.inv())  # Einv[mu,a] = e^a_mu  (E*Einv = 1 : sum_mu e_a^mu e^b_mu)
        # coframe e^a_mu = Einv[mu, a]
        self.g = sp.simplify(sp.Matrix(4, 4, lambda m, n: sum(eta[a, b]*self.Einv[m, a]*self.Einv[n, b] for a in range(4) for b in range(4))))
        self.G = christoffel(self.g, X)
        # omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_{mu lam} e_b^lam)
        om = [[[sp.simplify(sum(self.Einv[nu, a]*(sp.diff(E[b, nu], X[mu]) + sum(self.G[nu][mu][lam]*E[b, lam] for lam in range(4))) for nu in range(4)))
                for b in range(4)] for a in range(4)] for mu in range(4)]
        self.om = om
        self.c = c
    def Gam(self, mu, c):
        # Gamma_mu = c * omega_mu^{ab} gamma_a gamma_b, omega_mu^{ab} = omega_mu^a_d eta^{db}
        return c*sum((self.om[mu][a][d]*eta[d, b]*gl[a]*gl[b] for a in range(4) for b in range(4) for d in range(4)), sp.zeros(4))
    def gamma_up(self, mu):
        return sum((self.E[a, mu]*gu[a] for a in range(4)), sp.zeros(4))
    def gamma_dn(self, mu):
        return sum((self.Einv[mu, a]*gl[a] for a in range(4)), sp.zeros(4))
    def nabla_gamma(self, mu, nu, c):
        X = self.X
        gnu = self.gamma_up(nu)
        Gm = self.Gam(mu, c)
        return (gnu.diff(X[mu]) + sum((self.G[nu][mu][l]*self.gamma_up(l) for l in range(4)), sp.zeros(4)) + Gm*gnu - gnu*Gm)
    def Dpsi(self, mu, psi):
        return psi.diff(self.X[mu]) + self.Gam(mu, self.c)*psi
    def Dchi(self, mu, chi):  # chi = ligne (adjoint de Dirac)
        return chi.diff(self.X[mu]) - chi*self.Gam(mu, self.c)
    def slashD(self, psi):
        return sum((self.gamma_up(mu)*self.Dpsi(mu, psi) for mu in range(4)), sp.zeros(4, 1))
    def T(self, psi, chi):
        """T_{mu nu} = -(i/2) * sym[ chi gamma_mu D_nu psi - D_mu chi gamma_nu psi ]"""
        D = [self.Dpsi(m, psi) for m in range(4)]
        Dc = [self.Dchi(m, chi) for m in range(4)]
        gd = [self.gamma_dn(m) for m in range(4)]
        T = sp.zeros(4)
        for m in range(4):
            for n in range(m, 4):
                v = (chi*gd[m]*D[n] + chi*gd[n]*D[m] - Dc[m]*gd[n]*psi - Dc[n]*gd[m]*psi)[0, 0]
                T[m, n] = -I/4*v
                T[n, m] = T[m, n]
        return T
