# Modes de Dirac conformes sur de Sitter plat (g_c = eta, Omega = -t) et tenseur source
# Equation : i gamma^a d_a psi_c - (m/Omega) psi_c = 0, m = mu (H=1)
# Mode : psi_c = exp(i k.x) sum_{n,j} Omega^{n + i j mu} c_{n,j},  j = +1 (c_0 dans P+ = (1+g0)/2), j = -1 (c_0 dans P- = (1-g0)/2)
import sympy as sp
from conv import gu, gl, eta, E4, I, g0

mu = sp.Symbol('mu', positive=True)
Om = sp.Symbol('Omega', positive=True)
Pp = (E4 + g0)/2; Pm = (E4 - g0)/2

def mode(k, a0, b0, N, m=mu):
    """renvoie dict (n,j) -> vecteur colonne ; k = (k1,k2,k3)"""
    gk = sum((gu[i+1]*k[i] for i in range(3)), sp.zeros(4))
    d = {}
    for j, c0 in ((1, a0), (-1, b0)):
        if c0 is None:
            continue
        c = sp.Matrix(c0)
        for n in range(N+1):
            if n > 0:
                sv = n + I*j*m
                M = I*sv*g0 + m*E4
                c = (-M.inv()*gk*c).applyfunc(sp.simplify)
            d[(n, j)] = c
    return d

def dirac_residual(k, d, m=mu):
    """coefficients de Omega^{p + i j mu} dans i g^a d_a psi - (m/Omega) psi (sans l'exponentielle)"""
    gk = sum((gu[i+1]*k[i] for i in range(3)), sp.zeros(4))
    res = {}
    for (n, j), c in d.items():
        sv = n + I*j*m
        # i g0 d_t (Omega^s) = i g0 (-s) Omega^{s-1}
        res[(n-1, j)] = res.get((n-1, j), sp.zeros(4, 1)) + (-I*sv*g0 - m*E4)*c
        res[(n, j)] = res.get((n, j), sp.zeros(4, 1)) + (-gk)*c  # i g^j (i k_j) = -g.k
    return {key: v.applyfunc(sp.simplify) for key, v in res.items()}

def conj_series(d):
    return {(n, -j): v.applyfunc(sp.conjugate) for (n, j), v in d.items()}

def T_phys_pair(p, dp, r, dr, nmax):
    """contribution a T_{mu nu} physique (coordonnees) de psibar_p psi_r, facteur exp(i (r-p).x) omis.
    T^c_ab = -(i/4)[pb g_a d_b ps + pb g_b d_a ps - d_a pb g_b ps - d_b pb g_a ps] ; T = Omega^2 T^c
    renvoie dict (n,j) -> 4x4 pour Omega^{n + i j mu}"""
    cb = conj_series(dp)
    out = {}
    for (n1, j1), v1 in cb.items():
        row = v1.T*g0          # psibar coefficient (ligne)
        s1 = n1 + I*j1*mu       # exposant du psibar (deja conjugue)
        for (n2, j2), v2 in dr.items():
            s2 = n2 + I*j2*mu
            # derivees : d_0 -> -d_Omega ; d_0 Omega^s = -s Omega^{s-1}
            # facteur Omega^{s1+s2}; termes d_0 donnent Omega^{s1+s2-1}
            for a in range(4):
                for b in range(a, 4):
                    def dpsi(c_, sv, kk, idx):  # renvoie (coef, decalage de puissance)
                        if idx == 0:
                            return (-sv)*c_, -1
                        return I*kk[idx-1]*c_, 0
                    terms = []
                    # pb g_a d_b ps
                    for (A_, B_) in ((a, b), (b, a)):
                        cc, sh = dpsi(v2, s2, r, B_)
                        terms.append(((row*gl[A_]*cc)[0, 0], sh))
                        # - d_A pb g_B ps : d_A psibar
                        if A_ == 0:
                            cpb, sh2 = (-s1)*row, -1
                        else:
                            cpb, sh2 = (-I*p[A_-1])*row, 0
                        terms.append((-(cpb*gl[B_]*v2)[0, 0], sh2))
                    for val, sh in terms:
                        if val == 0:
                            continue
                        key = (n1+n2+sh+2, j1+j2)   # + 2 : T = Omega^2 T^c
                        if key[0] > nmax:
                            continue
                        out.setdefault(key, sp.zeros(4))
                        out[key][a, b] += -I/4*val
                        if a != b:
                            out[key][b, a] += -I/4*val
    return out
