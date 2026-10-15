#!/usr/bin/env python3
"""
cal_f.py -- NOTE-176 (CAL-F). Calibration of the use of Friedrich's (2.17) on known cases.
Physical de Sitter metric (Friedrich's hatted metric) ghat = eta^{-2}(-d eta^2 + dx^2), H = 1,
eta < 0, Omega = -eta. Source of (2.17): S_{rho nu lambda} = 2 Omega^{-1} nablahat_[nu Lhat_lambda] rho,
Lhat = (kappa/2)(That - (1/3) That_trace ghat)  (+ lambda/6 ghat, annihilated by nablahat).
Checks:
 (1) any homogeneous isotropic test fluid (rho(eta), p(eta)) : S = -(A H + Bdot)-type term,
     zero iff conservation holds;
 (2) homogeneous minimally coupled scalar of arbitrary mass, on shell: S = 0 identically;
 (3) the same scalar with PARTIAL derivatives (no Christoffel terms): non-zero, with an s^-1
     term at Friedrich's mass m^2 = 2 -- the error made by head computation before the freeze;
 (4) homogeneous dust (rho ~ m n0 a^-3, p = 0): S = 0.
"""
import sympy as sp

eta = sp.symbols('eta', negative=True)
x, y, z = sp.symbols('x y z', real=True)
X = [eta, x, y, z]; n = 4
kap, m = sp.symbols('kappa m', positive=True)
etaM = sp.diag(-1, 1, 1, 1)
g = etaM/eta**2
gi = g.inv()

Gam = [[[sp.simplify(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                       for e in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]

def cov(T, a, b, c):        # nabla_c T_ab
    return sp.diff(T[a, b], X[c]) - sum(Gam[e][c][a]*T[e, b] + Gam[e][c][b]*T[a, e] for e in range(n))

def part(T, a, b, c):
    return sp.diff(T[a, b], X[c])

def Lhat(T):
    tr = sp.simplify(sum(gi[a, b]*T[a, b] for a in range(n) for b in range(n)))
    return (kap/2)*(T - tr*g/3)

def S(T, D=cov):
    L = Lhat(T); Om = -eta
    out = {}
    for r in range(n):
        for nu in range(n):
            for la in range(nu+1, n):
                v = sp.simplify((D(L, la, r, nu) - D(L, nu, r, la))/Om)
                if v != 0:
                    out[(r, nu, la)] = v
    return out

def fluid(rho, p):
    u_low = sp.Matrix([-1/(-eta), 0, 0, 0])      # u_a = g_ab u^b, u^eta = 1/a = -eta ; u_eta = -a
    u_low = sp.Matrix([1/eta, 0, 0, 0])           # a = -1/eta, u_eta = -a = 1/eta
    return sp.Matrix(n, n, lambda a, b: (rho + p)*u_low[a]*u_low[b] + p*g[a, b])

print("=== CAL-F checks (H = 1, physical dS metric eta^-2 (-deta^2 + dx^2)) ===\n")

# (1) generic homogeneous fluid
rho = sp.Function('rho')(eta); p = sp.Function('p')(eta)
S1 = S(fluid(rho, p))
print("(1) generic homogeneous fluid, non-zero components of S:")
for k_, v in S1.items():
    print("   ", k_, sp.factor(v))
# conservation in conformal time: rho' = -3 (a'/a)(rho+p) = (3/eta)(rho + p)   (a = -1/eta, a'/a = -1/eta)
cons = {sp.diff(rho, eta): 3*(rho + p)/eta}
print("   after imposing conservation rho' = 3(rho+p)/eta :",
      {k_: sp.simplify(v.subs(cons)) for k_, v in S1.items()})

# (2)-(3) homogeneous scalar of arbitrary mass, on shell
h = sp.Function('h')(eta)
hp = sp.diff(h, eta)
dphi = [hp, 0, 0, 0]
T_sc = sp.Matrix(n, n, lambda a, b: dphi[a]*dphi[b]) - (sum(gi[c, c]*dphi[c]**2 for c in range(n))/2 + m**2*h**2/2)*g
# KG on dS, homogeneous: h'' - (2/eta) h' + m^2 h/eta^2 = 0
kg = {sp.diff(h, eta, 2): (2/eta)*hp - m**2*h/eta**2}
S2 = S(T_sc)
print("\n(2) homogeneous scalar, arbitrary m, covariant derivative, on shell:")
res2 = {k_: sp.simplify(v.subs(kg)) for k_, v in S2.items()}
print("   ", res2 if any(v != 0 for v in res2.values()) else "S = 0 identically")

S3 = S(T_sc, D=part)
print("\n(3) same scalar with PARTIAL derivatives only (the head-computation error), on shell, m^2 = 2:")
phi0, phi1, sv = sp.symbols('phi0 phi1 s', real=True)
for k_, v in S3.items():
    vv = sp.simplify(v.subs(kg).subs(m, sp.sqrt(2)))
    vv = sp.simplify(vv.subs(h, -phi0*eta + phi1*eta**2).doit())   # h = phi0 s + phi1 s^2, s = -eta
    print("   ", k_, sp.series(sp.simplify(vv.subs(eta, -sv)), sv, 0, 1).removeO())

# (4) dust
m_n0 = sp.symbols('mn0', positive=True)
S4 = S(fluid(m_n0*(-eta)**3, 0))
print("\n(4) homogeneous dust rho = m n0 Omega^3 :", S4 if S4 else "S = 0 identically")
