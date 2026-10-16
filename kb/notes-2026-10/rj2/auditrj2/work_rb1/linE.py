# Operateur d'Einstein linearise autour de de Sitter (H=1, lambda=3, kappa=1)
# g = Omega^{-2} (eta + eps h),  Omega = -t,  h_ab = H_ab Omega^s exp(i q.x)
# E_ab[h] = d/deps ( G_ab + 3 g_ab ) |_{eps=0}
import sympy as sp, pickle, os
from conv import eta

t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
s = sp.Symbol('s')
q = sp.symbols('q1:4', real=True)
Om = sp.Symbol('Omega', positive=True)

def build():
    Hs = sp.Matrix(4, 4, lambda a, b: sp.Symbol('H%d%d' % (min(a, b), max(a, b))))
    ph = (-t)**s*sp.exp(I*(q[0]*x + q[1]*y + q[2]*z))
    g0 = eta/t**2
    g1 = Hs*ph/t**2
    g0i = t**2*eta
    g1i = -g0i*g1*g0i
    def Gam(gi, gl_):  # Christoffel avec inverse donnee
        return [[[sum(gi[l, m]*(sp.diff(gl_[m, a], X[b]) + sp.diff(gl_[m, b], X[a]) - sp.diff(gl_[a, b], X[m])) for m in range(4))/2
                  for b in range(4)] for a in range(4)] for l in range(4)]
    G0 = Gam(g0i, g0)
    # Gamma1 = (1/2) g0^{-1}(d g1 ...) + (1/2) g1^{-1}(d g0 ...)
    A1 = Gam(g0i, g1); B1 = Gam(g1i, g0)
    G1 = [[[A1[l][a][b] + B1[l][a][b] for b in range(4)] for a in range(4)] for l in range(4)]
    def ric_lin(G0, G1):
        R = sp.zeros(4)
        for b in range(4):
            for d in range(4):
                v = 0
                for a in range(4):
                    v += sp.diff(G1[a][b][d], X[a]) - sp.diff(G1[a][b][a], X[d])
                    for e in range(4):
                        v += G0[a][a][e]*G1[e][b][d] + G1[a][a][e]*G0[e][b][d] - G0[a][d][e]*G1[e][b][a] - G1[a][d][e]*G0[e][b][a]
                R[b, d] = v
        return R
    R1 = ric_lin(G0, G1)
    # R0 = 3 g0 (de Sitter H=1) ; scalaire : R = g^{ab}R_ab ; R1s = g0i.R1 + g1i.R0
    R0 = 3*g0
    Rs0 = 12
    Rs1 = sum(g0i[a, b]*R1[a, b] + g1i[a, b]*R0[a, b] for a in range(4) for b in range(4))
    # G_ab + 3 g_ab linearise : R1 - (1/2)(Rs1 g0 + Rs0 g1) + 3 g1
    E = R1 - sp.Rational(1, 2)*(Rs1*g0 + Rs0*g1) + 3*g1
    # normalisation : diviser par Omega^{s-2} exp(i q x)
    E = (E/(ph*t**2)).applyfunc(lambda e: sp.expand(sp.simplify(e)))
    E = E.subs(t, -Om).applyfunc(sp.expand)
    return Hs, E

I = sp.I
if __name__ == "__main__":
    Hs, E = build()
    # E est polynomial en Omega : E = M0 + Omega M1 + Omega^2 M2
    for a in range(4):
        for b in range(a, 4):
            print(a, b, sp.collect(E[a, b], Om))
    pickle.dump((Hs, E), open('linE.pkl', 'wb'))
