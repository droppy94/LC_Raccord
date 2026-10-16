# VA-1 : FLRW non de Sitter (a = t^p, p>1 : temps conforme fini, H -> 0) et masse variable sur de Sitter.
# En temps physique : i du/dt = (alpha.k / a(t) + beta m(t)) u , u = composantes de hat psi (meme u que (3)).
import numpy as np
from scipy.integrate import solve_ivp

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2)); E = np.eye(2)
beta = np.block([[E, Z], [Z, -E]]).astype(complex)
alpha = [np.block([[Z, s], [s, Z]]) for s in (s1, s2, s3)]

def run(afun, mfun, kvec, t0, t1, n=4000, rtol=1e-11, atol=1e-13):
    K = sum(kvec[i] * alpha[i] for i in range(3))
    def f(t, y):
        u = y[:4] + 1j * y[4:]
        du = -1j * ((K / afun(t)) @ u + mfun(t) * (beta @ u))
        return np.concatenate([du.real, du.imag])
    ts = np.geomspace(t0, t1, n)
    Ufund = []
    for j in range(4):
        e = np.zeros(4, complex); e[j] = 1
        sol = solve_ivp(f, (t0, t1), np.concatenate([e.real, e.imag]), t_eval=ts, method='DOP853', rtol=rtol, atol=atol)
        Ufund.append((sol.y[:4] + 1j * sol.y[4:]).T)
    return ts, np.stack(Ufund, axis=2)   # (temps, 4, 4)

print("=== V2/V3 : FLRW a = t^p (hypotheses du par.2 satisfaites, H -> 0) ; solution a coefficient c = 0 ===")
m = 1.0; kvec = np.array([0.0, 0.0, 1.0]); K = kvec[2] * alpha[2]
for p in (1.5, 2.0, 3.0):
    a = lambda t, p=p: t ** p
    ts, F = run(a, lambda t: m, kvec, 1.0, 3000.0)
    theta = m * ts
    # chi = e^{i beta theta} u ; chi0 estime au dernier instant
    Ph = lambda th: np.diag([np.exp(1j * th)] * 2 + [np.exp(-1j * th)] * 2)
    chiF_end = Ph(theta[-1]) @ F[-1]
    target = np.array([1, 0, 1, 0], complex) / np.sqrt(2)     # |chi0+| = |chi0-|  -> c = 0
    c = np.linalg.solve(chiF_end, target)
    U = np.einsum('tij,j->ti', F, c)
    rho = np.array([np.real(np.vdot(U[i], (K + beta * m * a(ts[i])) @ U[i])) for i in range(len(ts))])
    eta_abs = ts ** (1 - p) / (p - 1)
    print(f"p={p}: a|eta| final = {a(ts[-1])*eta_abs[-1]:.1f} ; max|rho_hat| sur t in [100,3000] = {np.max(np.abs(rho[ts>100])):.3f} ;"
          f" max|Omega rho_hat| fin = {np.max(np.abs(rho[-200:]/a(ts[-200:]))):.1e}")
    # solution generique : Omega rho_hat -> c
    cg = np.array([0.9, 0.2, 0.3, 0.1], complex); cg /= np.linalg.norm(Ph(theta[-1]) @ F[-1] @ cg)
    Ug = np.einsum('tij,j->ti', F, cg)
    chi_end = Ph(theta[-1]) @ Ug[-1]
    cc = m * np.real(np.vdot(chi_end, beta @ chi_end))
    rg = np.array([np.real(np.vdot(Ug[i], (K + beta * m * a(ts[i])) @ Ug[i])) for i in range(len(ts))])
    print(f"      generique : coefficient c = {cc:+.6f} ; rho_hat - c/Omega sur la fin : [{np.min(rg[-300:]-cc*a(ts[-300:])):+.3f}, {np.max(rg[-300:]-cc*a(ts[-300:])):+.3f}]")

print("\n=== V7 : Proposition 4, exemples d'ordre strict (de Sitter, H=1, Omega = e^{-t}) ===")
a = lambda t: np.exp(t)
for name, mfun, expect in [("m=3 Omega^{1/2}", lambda t: 3 * np.exp(-t / 2), "champ convergent, m a ~ Omega^{-1/2}"),
                           ("m=3 Omega", lambda t: 3 * np.exp(-t), "champ convergent, m a = 3"),
                           ("m=3 Omega(1+Omega^{1/2})", lambda t: 3 * np.exp(-t) * (1 + np.exp(-t / 2)), "m a borne, non lisse"),
                           ("m=1/(1+t)", lambda t: 1 / (1 + t), "phase divergente en log")]:
    ts, F = run(a, mfun, np.array([0, 0, 2.0]), 1.0, 22.0, n=2)
    u_end = F[-1][:, 0]
    ts2, F2 = run(a, mfun, np.array([0, 0, 2.0]), 1.0, 19.0, n=2)
    dv = np.linalg.norm(u_end - F2[-1][:, 0])
    tq = np.linspace(19, 22, 30001); th = np.trapezoid(mfun(tq), tq)
    ma = mfun(22.0) * a(22.0)
    print(f"{name:26s}: |u(t=22)-u(t=19)| = {dv:.2e} ; increment de theta sur [19,22] = {th:.2e} ; m a(22) = {ma:.3e} ; ({expect})")
print("Pour m = 1/(1+t) : theta(t) = ln(1+t) -> infini (log) ; le champ ne converge pas mais tres lentement.")

print("\n=== V7 : contre-exemple FLRW a = t^{1.5} pour m ~ Omega^{1/2} ===")
p = 1.5
I_conv = lambda T: np.trapezoid(T ** (-p / 2), T)
for T in (1e2, 1e4, 1e6):
    tt = np.geomspace(1, T, 200000)
    print(f"int_1^{T:.0e} m dt avec m = a^(-1/2) = t^(-0.75) : {I_conv(tt):.2f} (diverge comme t^0.25)")

print("\n=== V9 : ordres de grandeur ===")
hbar = 6.582119569e-16      # eV s
Mpc = 3.0856775814913673e22  # m
for H0, OL in [(67.4, 0.685), (70.0, 0.7), (73.0, 0.69)]:
    H0s = H0 * 1e3 / Mpc
    Hinf = hbar * H0s * np.sqrt(OL)
    r = 5.10999e5 / Hinf
    print(f"H0={H0}, Omega_L={OL}: H_inf = {Hinf:.3e} eV ; m_e/H_inf = {r:.3e} ; log10 poids antiparticule ~ -2 pi r / ln 10 = {-2*np.pi*r/np.log(10):.3e} (exposant naturel {-2*np.pi*r:.2e})")
