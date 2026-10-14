"""Q2 : variation metrique de S_b = int J phi + int sqrt(g) psi (Delta4 phi - F4/4), famille diagonale.
Delta4 phi = box^2 phi + 2 R^{mn} nabla_m nabla_n phi - (2/3) R box phi + (1/3) nabla^m R nabla_m phi
F4 = E - (2/3) box R + b C^2,  E = Riem^2 - 4 Ric^2 + R^2,  C^2 = Riem^2 - 2 Ric^2 + R^2/3 (4D)
"""
import sympy as sp

s, x, y, z, eps, b = sp.symbols('s x y z epsilon b')
X = [s, x, y, z]
h = [sp.Function('h%d' % i)(s, x) for i in (1, 2, 3)]
psi = sp.Function('psi')(s, x)
phi = -sp.log(s)

def tr(e):
    e = sp.expand(e)
    return e.coeff(eps, 0) + eps*e.coeff(eps, 1)

def build(gdiag):
    g = sp.diag(*gdiag)
    gi = sp.diag(*[tr(sp.series(1/d, eps, 0, 2).removeO()) for d in gdiag])
    sqrtg = tr(sp.series(sp.sqrt(-sp.prod(gdiag)), eps, 0, 2).removeO())
    return g, gi, sqrtg

def geometry(g, gi):
    Gam = [[[tr(sum(gi[l, a]*(sp.diff(g[a, m], X[n]) + sp.diff(g[a, n], X[m]) - sp.diff(g[m, n], X[a]))
                    for a in range(4))/2) for n in range(4)] for m in range(4)] for l in range(4)]
    # R^r_{s m n}
    Riem = {}
    for r in range(4):
        for q in range(4):
            for m in range(4):
                for n in range(m+1, 4):
                    v = sp.diff(Gam[r][n][q], X[m]) - sp.diff(Gam[r][m][q], X[n]) \
                        + sum(Gam[r][m][l]*Gam[l][n][q] - Gam[r][n][l]*Gam[l][m][q] for l in range(4))
                    v = tr(v)
                    Riem[(r, q, m, n)] = v
                    Riem[(r, q, n, m)] = -v
                Riem[(r, q, m, m)] = 0
    Ric = sp.Matrix(4, 4, lambda q, n: tr(sum(Riem[(r, q, r, n)] for r in range(4))))
    R = tr(sum(gi[a, c]*Ric[a, c] for a in range(4) for c in range(4)))
    # Riem lower R_{r q m n} and upper (metric diagonal)
    Riem2 = 0
    for r in range(4):
        for q in range(4):
            for m in range(4):
                for n in range(4):
                    v = Riem[(r, q, m, n)]
                    if v == 0:
                        continue
                    # R^r_{qmn} R_r^{qmn} = R^r_{qmn} * g_rr g^qq g^mm g^nn R^r_{qmn}
                    Riem2 += tr(v*v*g[r, r]*gi[q, q]*gi[m, m]*gi[n, n])
    Riem2 = tr(Riem2)
    Ric2 = tr(sum(Ric[a, c]**2*gi[a, a]*gi[c, c] for a in range(4) for c in range(4)))
    return Gam, Ric, R, Riem2, Ric2

def box(f, gi, sqrtg):
    return tr(sum(sp.diff(tr(sqrtg*gi[m, m]*sp.diff(f, X[m])), X[m]) for m in range(4))
              * tr(sp.series(1/sqrtg, eps, 0, 2).removeO()))

def riegert(gdiag):
    g, gi, sqrtg = build(gdiag)
    Gam, Ric, R, Riem2, Ric2 = geometry(g, gi)
    boxphi = box(phi, gi, sqrtg)
    box2phi = box(boxphi, gi, sqrtg)
    hess = sp.Matrix(4, 4, lambda m, n: tr(sp.diff(phi, X[m], X[n]) - sum(Gam[l][m][n]*sp.diff(phi, X[l]) for l in range(4))))
    RicUp = sp.Matrix(4, 4, lambda m, n: tr(gi[m, m]*gi[n, n]*Ric[m, n]))
    D4 = tr(box2phi + 2*sum(RicUp[m, n]*hess[m, n] for m in range(4) for n in range(4))
            - sp.Rational(2, 3)*R*boxphi
            + sp.Rational(1, 3)*sum(gi[m, m]*sp.diff(R, X[m])*sp.diff(phi, X[m]) for m in range(4)))
    E = tr(Riem2 - 4*Ric2 + R**2)
    C2 = tr(Riem2 - 2*Ric2 + R**2/3)
    F4 = tr(E - sp.Rational(2, 3)*box(R, gi, sqrtg) + b*C2)
    dens = tr(sqrtg*(D4 - F4/4))
    return dens, D4, F4, E, C2, R

gdiag = [-1/s**2] + [(1 + eps*h[i])/s**2 for i in range(3)]
dens, D4, F4, E, C2, R = riegert(gdiag)

print('[calcule] fond : Delta4(-ln s) =', sp.simplify(D4.coeff(eps, 0)))
print('[calcule] fond : F4 =', sp.simplify(F4.coeff(eps, 0)), ' E =', sp.simplify(E.coeff(eps, 0)),
      ' R =', sp.simplify(R.coeff(eps, 0)), ' C2 =', sp.simplify(C2.coeff(eps, 0)))
d0 = sp.simplify(dens.coeff(eps, 0))
print('[calcule] fond : sqrt(g)(Delta4 phi - F4/4) =', d0)

d1 = sp.expand(dens.coeff(eps, 1))
print('[calcule] ordre eps : depend de b (terme C^2) ?', sp.simplify(sp.diff(d1, b)) != 0)
print('[calcule] ordre eps : contient log(s) ?', d1.has(sp.log(s)))

# prediction par covariance de Weyl : g = e^{2 sigma} gbar, sigma = -ln s = phi
# => sqrt(g)(Delta4 phi - F4/4) = -1/4 sqrt(gbar) Fbar4 ; lineaire : (1/6) box_eta R1[h]
boxeta = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2)
R1 = sp.diff(h[0], x, 2) - boxeta(h[0] + h[1] + h[2])
pred = sp.expand(boxeta(R1)/6)
print('[calcule] identite ponctuelle eps-coeff == (1/6) box_eta R^(1)[h] :', sp.simplify(d1 - pred) == 0)

# Euler-Lagrange de psi * d1 par rapport a h_i
Lag = sp.expand(psi*d1)
def EL(Lag, f):
    out = 0
    for D in Lag.atoms(sp.Derivative):
        if D.expr != f:
            continue
        coef = Lag.coeff(D)
        out += (-1)**D.derivative_count * sp.diff(coef, *D.variable_count)
    # terme sans derivee
    Lag0 = Lag.subs({d: 0 for d in Lag.atoms(sp.Derivative) if d.expr in h})
    out += sp.diff(Lag0, f)
    return sp.simplify(sp.expand(out))

T = [EL(Lag, h[i]) for i in range(3)]
for i in range(3):
    print('[calcule] dS_b/dh_%d =' % (i+1), T[i])
    _sub = T[i].subs({d: sp.Symbol('D%d' % j) for j, d in enumerate(T[i].atoms(sp.Derivative))})
    print('          contient log(s) ?', T[i].has(sp.log(s)), '; facteur s explicite (hors derivees de psi) ?', _sub.has(s))
predT = [sp.diff(boxeta(psi), x, 2)/6 - boxeta(boxeta(psi))/6, -boxeta(boxeta(psi))/6, -boxeta(boxeta(psi))/6]
for i in range(3):
    print('[calcule] ecart a la prediction covariante, i=%d :' % (i+1), sp.simplify(T[i] - predT[i]))
print('[calcule] T_y - T_z =', sp.simplify(T[1] - T[2]))
print('[calcule] dS_b/dh_2 + (1/6) box_eta^2 psi =', sp.simplify(T[1] + boxeta(boxeta(psi))/6), ' (donc dS_b/dh_y = dS_b/dh_z = J/6 sur couche box^2 psi = -J)')
# composantes coordonnees T_ii = 2 s^2 dS/dh_i (T_{mu nu} = (2/sqrt g) delta S / delta g^{mu nu}, signe conventionnel)
print('[derive] T^(b)_ii (coord.) = 2 s^2 dS_b/dh_i  =>  plus basse puissance s^2 pour psi lisse generique')
