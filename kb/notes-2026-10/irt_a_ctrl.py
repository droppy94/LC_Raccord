"""irt_a_ctrl.py (controle : coefficient non integrable -1/2 au lieu de 2) -- IR-t (NOTE-130/131), t-1 : partie a (Euler) de l'action de Wess-Zumino integrable,
S_a = Int sqrt(g) [ sigma (E - 2/3 box R) + 2 sigma Delta4 sigma ],  sigma = -ln s,
sur g = diag(-1, 1, 1+eP, 1+eQ)(s,x). Variation brute (Euler-Lagrange) par rapport a P ; T^yy = sgn*(2/sqrt g) dS/dg_yy.
Tests : fond T_hat = 6 ghat (a = 1) ; ordre e : delta T_hat_yy == 6 * delta ghat_yy ?  (u = mode tensoriel de de Sitter, P = -Q = u cos kx)
Calcul independant de celui de l'audit S-b (pas de reprise de code).
"""
import sympy as sp
from sympy.calculus.euler import euler_equations
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True); e = sp.symbols('e')
k, A, B = sp.symbols('k A B', positive=True)
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]; n = 4
P = sp.Function('P')(s, x); Q = sp.Function('Q')(s, x)
N2 = 2
def tr(ex):
    ex = sp.expand(ex)
    return sum(ex.coeff(e, i)*e**i for i in range(N2+1))
g = sp.diag(-1, 1, 1 + e*P, 1 + e*Q)
ginv = sp.diag(-1, 1, tr(1 - e*P + e**2*P**2), tr(1 - e*Q + e**2*Q**2))
sqg = tr(1 + e*(P+Q)/2 + e**2*(P*Q/4 - (P**2+Q**2)/8))
d = lambda f, i: sp.diff(f, X[i])
Gam = [[[tr(sum(ginv[a, m]*(d(g[m, b], c) + d(g[m, c], b) - d(g[b, c], m)) for m in range(n))/2)
         for c in range(n)] for b in range(n)] for a in range(n)]
# Riemann R^a_{bcd}
Rud = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for dd in range(n):
                Rud[(a, b, c, dd)] = tr(d(Gam[a][b][dd], c) - d(Gam[a][b][c], dd)
                                       + sum(Gam[a][c][m]*Gam[m][b][dd] - Gam[a][dd][m]*Gam[m][b][c] for m in range(n)))
Ric = sp.Matrix(n, n, lambda b, dd: tr(sum(Rud[(a, b, a, dd)] for a in range(n))))
Rs = tr(sum(ginv[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
# Riem^2 = R^a_bcd R_a^bcd ; metric diagonale
Riem2 = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for dd in range(n):
                v = Rud[(a, b, c, dd)]
                if v != 0:
                    Riem2 += v*v*g[a, a]*ginv[b, b]*ginv[c, c]*ginv[dd, dd]
Riem2 = tr(Riem2)
Ric2 = tr(sum(Ric[a, b]**2*ginv[a, a]*ginv[b, b] for a in range(n) for b in range(n)))
E = tr(Riem2 - 4*Ric2 + Rs**2)
def box(f):
    return tr(sum(ginv[a, a]*(sp.diff(f, X[a], 2) - sum(Gam[m][a][a]*d(f, m) for m in range(n))) for a in range(n)))
boxR = box(Rs)
sig = -sp.log(s)
def hess(f, a, b):
    return sp.diff(f, X[a], X[b]) - sum(Gam[m][a][b]*d(f, m) for m in range(n))
bs = box(sig)
D4 = tr(box(bs) + 2*sum(Ric[a, b]*ginv[a, a]*ginv[b, b]*hess(sig, a, b) for a in range(n) for b in range(n))
        - sp.Rational(2, 3)*Rs*bs + sp.Rational(1, 3)*sum(ginv[a, a]*d(Rs, a)*d(sig, a) for a in range(n)))
dens = tr(sqg*(sig*(E - sp.Rational(2, 3)*boxR) - sp.Rational(1, 2)*sig*D4))
print("densite construite ; termes :", len(sp.Add.make_args(dens)))
EL = euler_equations(dens, [P], [s, x])[0].lhs
EL = tr(EL)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
sub = {P: u*sp.cos(k*x), Q: -u*sp.cos(k*x)}
ELs = sp.simplify(EL.subs(sub).doit())
E0 = sp.simplify(ELs.coeff(e, 0)); E1 = sp.simplify(ELs.coeff(e, 1))
# T^yy = sgn * 2/sqrt(g) * (EL/e) ; T_yy = g_yy^2 T^yy ; T_hat = s^2 T ; ordre 0 et 1 en e (EL est d'ordre e : EL = e*E0' + e^2*E1')
# note : euler sur dens donne EL = dS/dP = e * dS/dg_yy
Tyy_up = 2*tr(ELs/e if False else 0)
sqgs = sqg.subs(sub).doit(); gyy = (1 + e*P).subs(sub).doit()
EL_P = ELs                   # = e * dS/dg_yy
dS_dgyy0 = sp.simplify(EL_P.coeff(e, 1))   # dS/dg_yy ordre 0
dS_dgyy1 = sp.simplify(EL_P.coeff(e, 2))   # ordre 1
print("verification : EL ordre e^0 (doit etre 0) :", sp.simplify(EL_P.coeff(e, 0)))
for sgn in (1, -1):
    Tup = sp.expand(sgn*2*(dS_dgyy0 + e*dS_dgyy1)*tr(1 - e*(sqgs - 1)))   # 1/sqrt g ~ 1 - (sqrt g - 1) a l'ordre 1
    Tlow = tr(sp.expand(gyy**2*Tup))
    That = sp.expand(s**2*Tlow)
    T0 = sp.simplify(That.coeff(e, 0)); T1 = sp.simplify(That.coeff(e, 1))
    print(f"sgn={sgn} : That_yy fond = {T0} ; attendu 6*ghat_yy = {sp.simplify(6/s**2)}")
    print(f"   That_yy ordre e = {sp.simplify(T1)}")
    print(f"   That_yy ordre e - 6*delta ghat_yy = {sp.simplify(T1 - 6*u*sp.cos(k*x)/s**2)}")
print("EXIT 0")
