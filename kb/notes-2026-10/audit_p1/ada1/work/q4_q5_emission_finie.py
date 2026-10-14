#!/usr/bin/env python3
# ADA-1, questions 4 et 5 : histoire a emission finie u = S(tau) u_A(tau),
# S transition C^infini de 0 (tau < tau0) a 1 (tau > tau0 + delta). k = 1, tau0 = -6, delta = 2.
# R(tau) = Int_{-inf}^{tau} K(tau - tau') B(tau') dtau' avec K(T) = -2 theta(T) cos(kT)/T (+ delta locale),
# B(tau') = (d^2+k^2)^2 (S u_A) a support dans [tau0, tau0+delta].
# Methode : B est tabulee une fois sur une quadrature de Gauss-Legendre composite ; R(tau) et ses derivees
# s'obtiennent par sommation avec le noyau (et ses derivees analytiques en tau), qui est analytique pour tau > tau0+delta.
import mpmath as mp
import sympy as sp

mp.mp.dps = 20
out = []
k_s, tau_s, t0_s, d_s = sp.symbols('k tau tau0 delta', real=True)
xi = (tau_s - t0_s) / d_s
def gfun(x):
    return sp.exp(-1 / x)
S_expr = gfun(xi) / (gfun(xi) + gfun(1 - xi))      # fonction de transition C^infini, valable pour 0 < xi < 1
uA = sp.cos(k_s * tau_s) + k_s * tau_s * sp.sin(k_s * tau_s)
Dop = lambda f: sp.diff(f, tau_s, 2) + k_s**2 * f
B_expr = Dop(Dop(S_expr * uA))
B_f = sp.lambdify((tau_s, k_s, t0_s, d_s), B_expr, 'mpmath')
S_f = sp.lambdify((tau_s, k_s, t0_s, d_s), S_expr, 'mpmath')

def B(tp, k, t0, d):
    if tp <= t0 or tp >= t0 + d:
        return mp.mpf(0)
    return B_f(tp, k, t0, d)

def gl_table(k, t0, d, nsub=16, deg=24):
    """noeuds, poids et valeurs de B sur [t0, t0+d] (Gauss-Legendre composite)."""
    xs, ws = mp.gauss_legendre(deg) if hasattr(mp, 'gauss_legendre') else (None, None)
    nodes = []; weights = []
    # construction manuelle des noeuds de Gauss-Legendre via mpmath (polyroots de Legendre)
    import mpmath.calculus.quadrature as q
    GL = mp.calculus.quadrature.GaussLegendre(mp.mp)
    pts = GL.calc_nodes(5, mp.mp.prec)  # degre 5 -> 3*2^4 = 48 noeuds environ sur [-1,1]
    for j in range(nsub):
        a = t0 + d * j / nsub; b = t0 + d * (j + 1) / nsub
        for (x, w) in pts:
            tp = (a + b) / 2 + (b - a) / 2 * x
            nodes.append(tp); weights.append(w * (b - a) / 2)
    Bv = [B(tp, k, t0, d) for tp in nodes]
    return nodes, weights, Bv

def kernel_deriv(T, k, n):
    """d^n/dT^n [cos(kT)/T] par formule de Leibniz."""
    s = mp.mpf(0)
    for j in range(n + 1):
        # d^j cos(kT) = k^j cos(kT + j pi/2) ; d^{n-j} (1/T) = (-1)^{n-j} (n-j)! / T^{n-j+1}
        s += mp.binomial(n, j) * k**j * mp.cos(k * T + j * mp.pi / 2) * (-1)**(n - j) * mp.factorial(n - j) / T**(n - j + 1)
    return s

def R(tau, tab, k, n=0):
    nodes, weights, Bv = tab
    return -2 * mp.fsum(w * kernel_deriv(tau - tp, k, n) * b for tp, w, b in zip(nodes, weights, Bv))

k = mp.mpf(1); t0 = mp.mpf(-6); d = mp.mpf(2)
tab = gl_table(k, t0, d)
tab2 = gl_table(k, t0, d, nsub=32)
out.append("Q4 : u = S(tau) u_A, k = 1, tau0 = -6, delta = 2, S(xi) = g(xi)/(g(xi)+g(1-xi)), g(x) = exp(-1/x)")
out.append("     S(-5.9) = %s, S(-5) = %s, S(-4.1) = %s" % (mp.nstr(S_f(mp.mpf(-5.9), k, t0, d), 6), mp.nstr(S_f(mp.mpf(-5), k, t0, d), 6), mp.nstr(S_f(mp.mpf(-4.1), k, t0, d), 6)))
out.append("     support de B : B est nul pour tau < -6 (S = 0) et pour tau > -4 (S = 1 et (d^2+k^2)^2 u_A = 0).")
out.append("     valeurs de B dans la fenetre : " + ", ".join("B(%s)=%s" % (mp.nstr(tp, 3), mp.nstr(B(tp, k, t0, d), 6)) for tp in [mp.mpf(-5.9), mp.mpf(-5.5), mp.mpf(-5), mp.mpf(-4.5), mp.mpf(-4.1)]))
nodes, weights, Bv = tab
out.append("     Int B = %s ; Int cos(k tau') B = %s ; Int sin(k tau') B = %s ; Int tau' cos(k tau') B = %s  (attendu : concomitant bilineaire J[g,u_A] au bord superieur, J = 0 pour g = cos, tau cos, tau sin et J = -2 k^3 pour g = sin)" % (
    mp.nstr(mp.fsum(w * b for w, b in zip(weights, Bv)), 6),
    mp.nstr(mp.fsum(w * mp.cos(k * tp) * b for tp, w, b in zip(nodes, weights, Bv)), 6),
    mp.nstr(mp.fsum(w * mp.sin(k * tp) * b for tp, w, b in zip(nodes, weights, Bv)), 6),
    mp.nstr(mp.fsum(w * tp * mp.cos(k * tp) * b for tp, w, b in zip(nodes, weights, Bv)), 6)))
out.append("     controle de quadrature : R(0) avec 16 sous-intervalles = %s, avec 32 = %s" % (mp.nstr(R(mp.mpf(0), tab, k), 15), mp.nstr(R(mp.mpf(0), tab2, k), 15)))
out.append("     tau        R(tau)")
for tau in ['-2', '-1', '-0.5', '-0.1', '0']:
    out.append("     %-8s %s" % (tau, mp.nstr(R(mp.mpf(tau), tab2, k), 15)))
out.append("     derivees en tau = 0 (noyau derive analytiquement) :")
for n in range(0, 5):
    out.append("       R^(%d)(0) = %s" % (n, mp.nstr(R(mp.mpf(0), tab2, k, n), 12)))
out.append("     controle : R(-0.1) par Taylor a l'ordre 4 autour de 0 = %s" % mp.nstr(mp.fsum(R(mp.mpf(0), tab2, k, n) * mp.mpf('-0.1')**n / mp.factorial(n) for n in range(5)), 12))
out.append("     R(0) = 2 Int cos(k tau') B(tau')/tau' dtau' = %s" % mp.nstr(2 * mp.fsum(w * mp.cos(k * tp) / tp * b for tp, w, b in zip(nodes, weights, Bv)), 15))
# dependance en tau0
out.append("     dependance en tau0 (delta = 2) :")
for t0try in ['-5', '-6', '-8', '-12', '-20', '-40', '-80']:
    t0v = mp.mpf(t0try)
    tb = gl_table(k, t0v, d)
    R0v = R(mp.mpf(0), tb, k)
    out.append("       tau0 = %-5s : R(0) = %-22s  tau0*R(0) = %s" % (t0try, mp.nstr(R0v, 12), mp.nstr(t0v * R0v, 8)))
out.append("     dependance en delta (tau0 = -6) :")
for dtry in ['1', '2', '3']:
    tb = gl_table(k, t0, mp.mpf(dtry))
    out.append("       delta = %s : R(0) = %s" % (dtry, mp.nstr(R(mp.mpf(0), tb, k), 12)))

# ---------------- Q5 : T-hat = s^2 R(-s) ----------------
out.append("")
out.append("Q5 : T-hat(s) = s^2 R(-s), tau0 = -6, delta = 2")
out.append("     s          R(-s)                 T-hat(s)              T-hat/s               T-hat/s^2")
for s in ['1', '0.3', '0.1', '0.03', '0.01', '0.001']:
    sv = mp.mpf(s)
    Rv = R(-sv, tab2, k)
    out.append("     %-8s %-22s %-22s %-22s %s" % (s, mp.nstr(Rv, 12), mp.nstr(sv**2 * Rv, 12), mp.nstr(sv * Rv, 12), mp.nstr(Rv, 12)))
R0 = R(mp.mpf(0), tab2, k); R1 = R(mp.mpf(0), tab2, k, 1)
out.append("     Taylor : T-hat(s) = R(0) s^2 - R'(0) s^3 + O(s^4) avec R(0) = %s, R'(0) = %s" % (mp.nstr(R0, 12), mp.nstr(R1, 12)))
out.append("     coefficient lineaire en s : T-hat/s en s = 0.001 vaut %s -> 0 (pas de terme lineaire)" % mp.nstr(mp.mpf('0.001') * R(mp.mpf('-0.001'), tab2, k), 6))

txt = "\n".join(out)
print(txt)
open('/home/claude/audit_p1/ada1/work/q4_q5_emission_finie.out', 'w').write(txt + "\n")
