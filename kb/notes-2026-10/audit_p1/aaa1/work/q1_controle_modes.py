#!/usr/bin/env python3
"""Controle independant de Q1 : calcul direct par la forme bilineaire symetrisee
T_{mu nu}(phi, phibar) sur le mode phi_k = (alpha e^{-ik eta} + beta e^{ik eta}) e^{ik.x}/sqrt(2k(2pi)^3),
puis soustraction du vide (alpha=1, beta=0), avec |alpha|^2 = 1 + |beta|^2.
On verifie aussi l'effet du terme d'amelioration (xi = 0 vs xi = 1/6) sur la structure P3.
"""
import sympy as sp

eta = sp.symbols('eta', real=True)
x = sp.symbols('x1:4', real=True)
k = sp.symbols('k', positive=True)
kv = sp.symbols('k1:4', real=True)
X = [eta] + list(x)
g = sp.diag(-1, 1, 1, 1); ginv = g.inv()
al, be = sp.symbols('alpha beta')
alc, bec = sp.symbols('alphac betac')  # conjugues traites comme symboles independants
ksq = {kv[0]**2: k**2 - kv[1]**2 - kv[2]**2}

def bilin(phi, psi, xi):
    d = lambda f, mu: sp.diff(f, X[mu])
    kin = sum(ginv[a, b] * d(phi, a) * d(psi, b) for a in range(4) for b in range(4))
    pp = phi * psi
    box = sum(ginv[a, b] * d(d(pp, b), a) for a in range(4) for b in range(4))
    T = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            T[mu, nu] = (sp.Rational(1, 2) * (d(phi, mu) * d(psi, nu) + d(phi, nu) * d(psi, mu))
                         - sp.Rational(1, 2) * g[mu, nu] * kin
                         - xi * (d(d(pp, nu), mu) - g[mu, nu] * box))
    return T

kx = sum(kv[i] * x[i] for i in range(3))
norm = 1 / sp.sqrt(2 * k * (2 * sp.pi) ** 3)
phi = (al * sp.exp(-sp.I * k * eta) + be * sp.exp(sp.I * k * eta)) * sp.exp(sp.I * kx) * norm
phib = (alc * sp.exp(sp.I * k * eta) + bec * sp.exp(-sp.I * k * eta)) * sp.exp(-sp.I * kx) * norm

for xi in (sp.Rational(1, 6), 0):
    print('=' * 70)
    print('xi =', xi)
    T = bilin(phi, phib, xi)
    Tv = bilin(phi.subs({al: 1, be: 0}), phib.subs({alc: 1, bec: 0}), xi)
    Ts = (T - Tv).applyfunc(lambda e: sp.expand(e))
    # |alpha|^2 -> 1 + |beta|^2 ; on garde alpha*betac et alphac*beta comme structures
    b2 = sp.symbols('b2', positive=True)
    Ts = Ts.applyfunc(lambda e: sp.expand(e.subs(al * alc, 1 + b2).subs(be * bec, b2)))
    Ts = Ts.applyfunc(lambda e: sp.simplify(sp.expand(e).subs(ksq)))
    # extraction des coefficients
    for name, mono in (('|beta|^2', b2), ('alpha beta*', al * bec), ('alpha* beta', alc * be)):
        C = Ts.applyfunc(lambda e: sp.simplify(sp.expand(e).coeff(mono)))
        print('--- structure', name)
        print('T_00 =', C[0, 0], ' T_0i =', [C[0, i] for i in (1, 2, 3)])
        print('T_ij (composantes 11, 12, 22) =', C[1, 1], '|', C[1, 2], '|', C[2, 2])
        tr = sp.simplify(sum(ginv[a, b] * C[a, b] for a in range(4) for b in range(4)).subs(ksq))
        print('trace =', tr)
        trsp = sp.simplify((C[1, 1] + C[2, 2] + C[3, 3]).subs(ksq))
        print('trace spatiale T_ii =', trsp)
    # controle : il ne reste rien d'autre
    reste = Ts.applyfunc(lambda e: sp.simplify(sp.expand(e).subs({b2: 0, al: 0, alc: 0, be: 0, bec: 0})))
    print('reste (doit etre nul) :', reste)
