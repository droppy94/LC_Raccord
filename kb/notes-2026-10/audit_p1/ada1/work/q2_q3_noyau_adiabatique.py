#!/usr/bin/env python3
# ADA-1, questions 2 et 3.
# Q2 : verification numerique du noyau retarde
#      K_k(T) = -2 Pf_{T0}[ theta(T) cos(kT)/T ] - 2 ln(mu T0 e^gamma) delta(T)
#      contre L(omega) = ln((k^2 - (omega+i0)^2)/mu^2), via la transformee de Laplace-Fourier
#      L(omega) = Int_0^inf e^{i omega T} K(T) dT evaluee en omega complexe (Im omega = a > 0).
# Q3 : reponse retardee R_eps(0) = Int_0^inf K(T) B_eps(-T) dT, numerique (mpmath) et forme fermee.
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
out = []

def pf_integral(F, F0, T0, Tmax, period):
    """Partie finie de Hadamard (echelle T0) de Int_0^inf F(T)/T dT, avec F(0) = F0.
    Pf := Int_0^{T0} (F(T) - F0)/T dT + Int_{T0}^{Tmax} F(T)/T dT  (F supposee decroissante au-dela de Tmax)."""
    reg = mp.quad(lambda T: (F(T) - F0) / T, [0, T0])
    # decoupage de la queue oscillante en sous-intervalles de longueur 'period'
    pts = [T0]
    t = T0
    while t < Tmax:
        t = min(t + period, Tmax)
        pts.append(t)
    tail = mp.quad(lambda T: F(T) / T, pts)
    return reg + tail

# ---------------- Q2 : test du noyau ----------------
k = mp.mpf(1); mu = mp.mpf(1); T0 = mp.mpf(1)
gam = mp.euler
Cdelta = -2 * mp.log(mu * T0 * mp.e**gam)   # coefficient de delta(T)

def L_exact(om):
    # ln((k^2 - omega^2)/mu^2) pour Im omega > 0 (branche principale, continue dans le demi-plan superieur)
    return mp.log((k**2 - om**2) / mu**2)

def L_from_kernel(om, Tmax=400):
    # Int_0^inf e^{i om T} K(T) dT, avec K = -2 Pf[cos(kT)/T] + Cdelta delta
    F = lambda T: mp.cos(k * T) * mp.exp(1j * om * T)
    val = -2 * pf_integral(F, mp.mpf(1), T0, Tmax, mp.pi / k) + Cdelta
    return val

out.append("Q2 : test numerique du noyau K_k(T) (k = mu = 1, T0 = 1, C_delta = %s)" % mp.nstr(Cdelta, 12))
out.append("     omega complexe         L exact                        L reconstruit depuis K          |diff|")
for om in [mp.mpc(0, 1), mp.mpc(0, 0.5), mp.mpc(0.5, 0.3), mp.mpc(2, 0.3), mp.mpc(3, 0.1), mp.mpc(-3, 0.1), mp.mpc(0.3, 0.05)]:
    Tmax = 60 / float(om.imag)
    Lk = L_from_kernel(om, Tmax=Tmax)
    Le = L_exact(om)
    out.append("     %-22s %-30s %-30s %s" % (mp.nstr(om, 6), mp.nstr(Le, 12), mp.nstr(Lk, 12), mp.nstr(abs(Lk - Le), 3)))
# dependance en T0 : le resultat ne doit pas en dependre (le terme delta compense)
for T0try in [mp.mpf('0.5'), mp.mpf(2), mp.mpf(5)]:
    T0 = T0try
    Cdelta = -2 * mp.log(mu * T0 * mp.e**gam)
    om = mp.mpc(2, 0.3)
    out.append("     T0 = %s : L reconstruit = %s (exact %s)" % (mp.nstr(T0, 3), mp.nstr(L_from_kernel(om, Tmax=200), 12), mp.nstr(L_exact(om), 12)))
T0 = mp.mpf(1); Cdelta = -2 * mp.log(mu * T0 * mp.e**gam)
# signe retarde : Im L(omega + i0) pour omega > k doit tendre vers -pi
for a in [mp.mpf('0.1'), mp.mpf('0.02')]:
    om = mp.mpc(3, a)
    out.append("     omega = 3 + %s i : Im L exact = %s, Im L depuis K = %s (attendu -> -pi = %s)" %
               (mp.nstr(a, 3), mp.nstr(L_exact(om).imag, 8), mp.nstr(L_from_kernel(om, Tmax=60 / float(a)).imag, 8), mp.nstr(-mp.pi, 8)))

# ---------------- Q3 : reponse adiabatique ----------------
out.append("")
out.append("Q3 : R_eps(0) = Int_0^inf K(T) B_eps(-T) dT, k = mu = 1, Pf de Hadamard a l'echelle T0 = 1")
ks = sp.symbols('k', positive=True); eps_s = sp.symbols('epsilon', positive=True); tau_s = sp.symbols('tau', real=True)
uA = sp.cos(ks * tau_s) + ks * tau_s * sp.sin(ks * tau_s)
Dop = lambda f: sp.diff(f, tau_s, 2) + ks**2 * f
Beps = sp.simplify(Dop(Dop(sp.exp(eps_s * tau_s) * uA)))
Beps_f = sp.lambdify((tau_s, ks, eps_s), Beps, 'mpmath')
out.append("     B_eps(tau) = %s" % Beps)

def R_eps_numeric(epsv, T0=mp.mpf(1)):
    Cd = -2 * mp.log(mu * T0 * mp.e**gam)
    F = lambda T: mp.cos(k * T) * Beps_f(-T, k, epsv)
    F0 = Beps_f(mp.mpf(0), k, epsv)
    Tmax = 60 / epsv  # e^{-60} negligeable
    return -2 * pf_integral(F, F0, T0, Tmax, mp.pi / k) + Cd * F0

# forme fermee (derivee a la main a partir des integrales elementaires et de la Pf, voir rapport)
def R_eps_closed(e, kk=1, mm=1):
    e = mp.mpf(e); kk = mp.mpf(kk); mm = mp.mpf(mm)
    s = e**2 + 4 * kk**2
    val = (-8 * e * kk**3 * mp.atan(2 * kk / e)
           + 8 * e**2 * kk**4 / s + 4 * e**2 * kk**2 + 2 * e**4 * kk**2 / s
           + (8 * e**2 * kk**2 + e**4) * (mp.log(e / mm) + mp.log(mp.sqrt(s) / mm)))
    return val

out.append("     eps        R_eps(0) numerique (T0=1)      R_eps(0) numerique (T0=3)      forme fermee                 -4 pi k^3 eps         R/eps")
for e in ['0.1', '0.01', '0.001']:
    ev = mp.mpf(e)
    Rn1 = R_eps_numeric(ev, T0=mp.mpf(1))
    Rn3 = R_eps_numeric(ev, T0=mp.mpf(3))
    Rc = R_eps_closed(ev)
    out.append("     %-8s %-30s %-30s %-28s %-20s %s" % (e, mp.nstr(Rn1, 14), mp.nstr(Rn3, 14), mp.nstr(Rc, 14), mp.nstr(-4 * mp.pi * ev, 10), mp.nstr(Rn1 / ev, 10)))
out.append("     developpement de la forme fermee en eps (k = mu = 1) :")
e_s = sp.symbols('epsilon', positive=True)
Rc_s = (-8 * e_s * sp.atan(2 / e_s) + 8 * e_s**2 / (e_s**2 + 4) + 4 * e_s**2 + 2 * e_s**4 / (e_s**2 + 4)
        + (8 * e_s**2 + e_s**4) * (sp.log(e_s) + sp.log(sp.sqrt(e_s**2 + 4))))
out.append("     R_eps(0) = %s" % sp.series(Rc_s, e_s, 0, 4))
# borne : sup_{0<eps<=1} |R_eps(0)|/eps et |R_eps(0) + 4 pi eps| / (eps^2 |ln eps|)
grid = [mp.mpf(10)**(-mp.mpf(j) / 4) for j in range(1, 41)]
m1 = max(abs(R_eps_closed(e)) / e for e in grid)
m2 = max(abs(R_eps_closed(e) + 4 * mp.pi * e) / (e**2 * abs(mp.log(e))) for e in grid if e < 0.5)
out.append("     sup_{1e-10<=eps<=0.56} |R_eps(0)|/eps = %s ; sup |R_eps(0)+4 pi eps|/(eps^2 |ln eps|) (eps<0.5) = %s" % (mp.nstr(m1, 8), mp.nstr(m2, 8)))

txt = "\n".join(out)
print(txt)
open('/home/claude/audit_p1/ada1/work/q2_q3_noyau_adiabatique.out', 'w').write(txt + "\n")
