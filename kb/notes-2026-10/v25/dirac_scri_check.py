#!/usr/bin/env python3
"""
dirac_scri_check.py  --  numerical check for the article
"No non-zero rest mass for a Dirac field across future conformal infinity".

Units: H = 1.  Conformal time eta in (-inf, 0), a = -1/eta, Omega = 1/a = -eta.
Rescaled Dirac field psi_hat = a^{3/2} psi satisfies, for a single spatial
momentum k along z and in the Dirac representation, the 2-component system

    i d/d eta (f, g)^T = [[ m a ,  k ],
                          [ k   , -m a ]] (f, g)^T

(f = upper component, g = lower component for the helicity block).
The generator is Hermitian, so |f|^2 + |g|^2 is conserved.

Checks:
 (1) norm conservation along the integration;
 (2) for k = 0 the exact solution f = exp(-i m ln a) f0 (phase (m/H) ln Omega);
 (3) for k != 0 the phase of f still winds like m ln a as eta -> 0^-, while
     the "interaction-picture" spinor chi = exp(+i beta m ln a) psi_hat
     converges (its variation between eta and 0 is bounded by k|eta|);
 (4) the scalar comparison: rescaled minimally coupled scalar chi'' +
     (m^2 a^2 - 2/eta^2) chi = 0 has exponents 1/2 +- sqrt(9/4 - m^2).
"""
import numpy as np
from scipy.integrate import solve_ivp

def dirac_rhs(eta, y, m, k):
    f = y[0] + 1j*y[1]
    g = y[2] + 1j*y[3]
    a = -1.0/eta
    df = -1j*( m*a*f + k*g )
    dg = -1j*( k*f - m*a*g )
    return [df.real, df.imag, dg.real, dg.imag]

def run(m, k, eta0=-1.0, eta1=-1e-6):
    y0 = [1.0, 0.0, 0.0, 0.0]          # start in the beta=+1 component
    sol = solve_ivp(dirac_rhs, (eta0, eta1), y0, args=(m, k),
                    rtol=1e-10, atol=1e-12, dense_output=True,
                    method="DOP853")
    etas = -np.logspace(0, 6, 7)[::-1]*(-eta1) if False else np.array([-1.0,-1e-1,-1e-2,-1e-3,-1e-4,-1e-5,-1e-6])
    out = []
    for e in etas:
        y = sol.sol(e)
        f = y[0]+1j*y[1]; g = y[2]+1j*y[3]
        norm = abs(f)**2 + abs(g)**2
        a = -1.0/e
        # interaction picture: remove the beta-rotation exp(-i beta m ln a)
        chi_f = f*np.exp(1j*m*np.log(a))
        chi_g = g*np.exp(-1j*m*np.log(a))
        out.append((e, norm, np.angle(f), (-m*np.log(a)), chi_f, chi_g))
    return out

def main():
    np.set_printoptions(precision=6)
    print("=== Dirac rescaled field near scri+ (H = 1) ===")
    for (m, k) in [(1.0, 0.0), (1.0, 0.5), (3.0, 2.0)]:
        print(f"\n--- m = {m}, k = {k} ---")
        print(" eta        norm          arg f      -m ln a    |chi_f|   |chi_g|   chi_f")
        res = run(m, k)
        for (e, norm, argf, pred, cf, cg) in res:
            # compare phases modulo 2 pi
            d = (argf - pred + np.pi) % (2*np.pi) - np.pi
            print(f"{e:9.1e}  {norm:12.9f}  {argf:9.4f}  {pred:9.4f}   {abs(cf):8.5f} {abs(cg):8.5f}   {cf:.5f}" + ("" if k else f"   (phase diff mod 2pi = {d:+.2e})"))
        # convergence of chi: difference between last two samples
        cf1, cf2 = res[-2][4], res[-1][4]
        print(f" |chi_f(1e-5) - chi_f(1e-6)| = {abs(cf1-cf2):.2e}  (bound k*|eta| = {k*1e-5:.1e})")
        # windings of the phase between eta=-1 and eta=-1e-6
        print(f" phase of f winds by about m*ln(a) = {m*np.log(1e6):.2f} rad between eta=-1 and eta=-1e-6")

    print("\n=== Scalar comparison: exponents s of chi ~ |eta|^s, chi'' + (m^2 a^2 - 2/eta^2) chi = 0 ===")
    for m2 in [0.0, 1.0, 2.0, 2.25, 4.0, 100.0]:
        disc = 9/4 - m2
        if disc >= 0:
            s1, s2 = 0.5 + np.sqrt(disc), 0.5 - np.sqrt(disc)
            print(f" m^2/H^2 = {m2:6.2f} : s = {s1:.4f}, {s2:.4f}  -> " +
                  ("smooth (integers 0,1)" if m2 == 2.0 else ("one branch diverges" if s2 < 0 else "both -> 0, non-smooth")))
        else:
            print(f" m^2/H^2 = {m2:6.2f} : s = 1/2 +- i {np.sqrt(-disc):.4f}  -> both -> 0 with oscillation, not C^1")
    print("\nElectron: m_e = 5.11e5 eV, H_inf = 1.2e-33 eV, m_e/H_inf =", f"{5.11e5/1.2e-33:.2e}")

if __name__ == "__main__":
    main()
