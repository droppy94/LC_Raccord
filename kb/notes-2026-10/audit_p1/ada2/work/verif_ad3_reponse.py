# ad-3 : reponse retardee R_eps(tau0) = Int_0^inf K(T) B_eps(tau0 - T) dT, mode A, k = 1.
# (1) Reproduction par une autre methode : partie [1, inf) en forme fermee (fonctions gamma incompletes de
#     argument complexe), partie [0, L] par quadrature a haute precision.
# (2) Dependance en l'echelle L de Hadamard (L = 0.1, 1, 10) et autre regularisation (soustraction lisse f0 e^{-T/L}).
# (3) Comparaison a la prediction asymptotique 8 eps k^3 sin(k tau0) E1(eps) + O(eps).
import sympy as sp
from mpmath import mp, mpf, mpc, quad, quadosc, cos, sin, exp, log, inf, gammainc, e1, ci, euler, pi, nstr

mp.dps = 25
t, T = sp.symbols('tau T', real=True)
k = sp.symbols('k', positive=True)
eps = sp.symbols('epsilon', positive=True)
uA = sp.cos(k*t) + k*t*sp.sin(k*t)
P2 = lambda f: sp.diff(f, t, 2) + k**2*f
B_exact = sp.simplify(P2(P2(sp.exp(eps*t)*uA)))           # B_eps(tau)
poly = sp.collect(sp.expand(sp.simplify(B_exact*sp.exp(-eps*t))), eps)  # polynome trig en tau
print("e^(-eps tau) B_eps =", poly)

kv = mpf(1)

def B_num(tv, ev):
    return mpf(sp.N(B_exact.subs({k: 1, eps: ev, t: tv}), 30))

# Decomposition exponentielle de B_eps(tau0 - T) cos(kT) : termes c * T^m * e^{s T}, s complexe.
# Int_L^inf T^(m-1) e^{-sT} dT = s^{-m} Gamma(m, s L)  (m >= 1) ; m = 0 : E1(sL).
def closed_tail(tau0, ev, L):
    expr = sp.expand(sp.expand_complex(sp.expand((B_exact.subs({k: 1, eps: ev, t: tau0 - T})*sp.cos(T)).rewrite(sp.exp))))
    # on remplace sin/cos par exponentielles complexes, puis collecte en T^m e^{a T}
    expr = sp.expand(expr.rewrite(sp.exp))
    assert not expr.has(sp.sin) and not expr.has(sp.cos)
    total = mpc(0)
    for term in sp.Add.make_args(expr):
        coeff, rest = term.as_independent(T)
        # rest = T^m * exp(a T) (ou 1)
        m = 0
        a = 0
        for fac in sp.Mul.make_args(rest):
            if fac.is_Pow and fac.base == T:
                m = int(fac.exp)
            elif fac == T:
                m = 1
            elif isinstance(fac, sp.exp):
                a = a + sp.simplify(fac.args[0]/T)   # plusieurs facteurs exp possibles : on additionne
            elif fac == 1:
                pass
            else:
                raise ValueError(str(fac))
        s = -mpc(complex(sp.N(a, 30)))
        c = mpc(complex(sp.N(coeff, 30)))
        # Int_L^inf T^(m-1) e^{-sT} dT, avec le facteur -2 du noyau
        if m == 0:
            I = e1(s*L)
        else:
            I = gammainc(m, s*L)/s**m
        total += -2*c*I
    return total

def R_eps(tau0, ev, L=mpf(1), scheme="hadamard"):
    f = lambda TT: B_num(tau0 - TT, ev)
    f0 = B_num(tau0, ev)
    if scheme == "hadamard":
        I1 = quad(lambda TT: (f(TT) - f0)*(-2*cos(kv*TT)/TT), [0, L/4, L/2, L])
        I2 = closed_tail(tau0, ev, L)
        return I1 + I2.real, f0
    elif scheme == "lisse":
        # Int_0^inf (f(T) - f0 e^{-T/L}) K(T) dT = Hadamard(L) + f0 * [ Int_0^L (1 - e^{-T/L}) ... ] : calcule directement
        I1 = quad(lambda TT: (f(TT) - f0*exp(-TT/L))*(-2*cos(kv*TT)/TT), [0, L/4, L/2, L])
        I2 = closed_tail(tau0, ev, L) - f0*(-2)*quadosc(lambda TT: exp(-TT/L)*cos(kv*TT)/TT, [L, inf], omega=kv)
        return I1 + I2.real, f0

print("\n(1) Reproduction, Hadamard echelle 1 (a comparer au script) :")
for tau0 in (mpf(0), mpf(-1)):
    for ev in (mpf('0.1'), mpf('0.01'), mpf('0.001')):
        Rv, f0 = R_eps(tau0, ev)
        pred = 8*ev*sin(kv*tau0)*e1(ev)
        print(f"  tau0 = {tau0}, eps = {ev} : R = {nstr(Rv, 12)} ; R/eps = {nstr(Rv/ev, 8)} ; R/(eps ln 1/eps) = {nstr(Rv/(ev*log(1/ev)), 8)} ; terme dominant 8 eps sin(tau0) E1(eps) = {nstr(pred, 8)} ; B_eps(tau0) = {nstr(f0, 8)}")

print("\n(2) Dependance en l'echelle L et autre regularisation ; prediction : R(L) - R(1) = 2 B_eps(tau0) [Ci(kL) - Ci(k)]")
for tau0 in (mpf(0), mpf(-1)):
    for ev in (mpf('0.1'), mpf('0.01'), mpf('0.001')):
        R1, f0 = R_eps(tau0, ev, mpf(1))
        line = f"  tau0 = {tau0}, eps = {ev} : R(L=1) = {nstr(R1, 10)}"
        for L in (mpf('0.1'), mpf(10), mpf(100)):
            RL, _ = R_eps(tau0, ev, L)
            line += f" | L={L}: R = {nstr(RL, 10)}, ecart = {nstr(RL - R1, 6)}, predit = {nstr(2*f0*(ci(kv*L) - ci(kv)), 6)}"
        Rs, _ = R_eps(tau0, ev, mpf(1), "lisse")
        line += f" | lisse(L=1): R = {nstr(Rs, 10)}, ecart = {nstr(Rs - R1, 6)}"
        print(line)

print("\n(3) Petits eps supplementaires (Hadamard L = 1) pour la tendance :")
for tau0 in (mpf(0), mpf(-1)):
    for ev in (mpf('1e-4'), mpf('1e-5')):
        Rv, f0 = R_eps(tau0, ev)
        print(f"  tau0 = {tau0}, eps = {ev} : R = {nstr(Rv, 10)} ; R/eps = {nstr(Rv/ev, 8)} ; R/(eps ln 1/eps) = {nstr(Rv/(ev*log(1/ev)), 8)} ; 8 sin(tau0) E1(eps) = {nstr(8*sin(tau0)*e1(ev), 8)}")
