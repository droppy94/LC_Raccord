"""Q1 : identite nabla^mu X^M_{mu nu} = -1/4 d_nu(I^2) F^2 sur couche, mode A_y = u(s) cos(kx), fond g = s^-2 eta."""
import sympy as sp

s, x, y, z, k, beta, e, lam = sp.symbols('s x y z k beta e lambda', positive=True)
X = [s, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
g = eta / s**2
gi = g.inv()
u = sp.Function('u')(s)
I2f = sp.Function('I2')(s)          # I^2 generique d'abord

A = [0, 0, u*sp.cos(k*x), 0]
F = sp.Matrix(4, 4, lambda m, n: sp.diff(A[n], X[m]) - sp.diff(A[m], X[n]))
Fup = gi*F*gi
F2 = sp.simplify(sum(F[m, n]*Fup[m, n] for m in range(4) for n in range(4)))

Gam = [[[sp.simplify(sum(gi[l, a]*(sp.diff(g[a, m], X[n]) + sp.diff(g[a, n], X[m]) - sp.diff(g[m, n], X[a]))
                         for a in range(4))/2) for n in range(4)] for m in range(4)] for l in range(4)]

def Xm(I2):
    return sp.Matrix(4, 4, lambda m, n: I2*(sum(F[m, a]*F[n, b]*gi[a, b] for a in range(4) for b in range(4))
                                            - g[m, n]*F2/4))

def cov_div(T):
    # nabla^mu T_{mu nu} = g^{mu a} nabla_a T_{mu nu}
    out = []
    for n in range(4):
        tot = 0
        for m in range(4):
            for a in range(4):
                if gi[m, a] == 0:
                    continue
                d = sp.diff(T[m, n], X[a]) - sum(Gam[l][a][m]*T[l, n] for l in range(4)) \
                    - sum(Gam[l][a][n]*T[m, l] for l in range(4))
                tot += gi[m, a]*d
        out.append(tot)
    return out

# equation de mode : (I2 u')' + k^2 I2 u = 0  =>  u'' = -(I2' u' + k^2 I2 u)/I2
eom_upp = -(sp.diff(I2f, s)*sp.diff(u, s) + k**2*I2f*u)/I2f
# verifier que c'est bien l'equation de Maxwell nabla_mu(I2 F^{mu nu}) = 0
maxw = [sp.simplify((sum(sp.diff(sp.sqrt(-g.det())*I2f*Fup[m, n], X[m]) for m in range(4))).subs(sp.diff(u, s, 2), eom_upp))
        for n in range(4)]
print('[calcule] Maxwell sur couche (doit etre 0,0,0,0):', maxw)

div = cov_div(Xm(I2f))
rhs = [-sp.Rational(1, 4)*sp.diff(I2f, X[n])*F2 for n in range(4)]
res = [sp.simplify((div[n] - rhs[n]).subs(sp.diff(u, s, 2), eom_upp)) for n in range(4)]
print('[calcule] F^2 =', F2)
print('[calcule] div X^M - (-1/4 d(I2) F^2), composantes s,x,y,z (I2 generique):', res)

# specialisation I2 = e^-2 [1 + 2 beta (lam - ln s)]
I2 = (1 + 2*beta*(lam - sp.log(s)))/e**2
div_s = sp.simplify((-sp.Rational(1, 4)*sp.diff(I2, s)*F2))
print('[calcule] -1/4 d_s(I2) F^2 =', div_s)
L = sp.Symbol('L')
print('[calcule] contient log(s) ?', div_s.has(sp.log(s)))
print('[calcule] composante s, ordre beta^1 :', sp.simplify(sp.diff(div_s, beta)))
