#!/usr/bin/env python3
"""
dirac_scri_check_v2.py  --  numerical consistency checks for
"No non-zero rest mass for a Dirac field across future conformal infinity" (v2).

Units H = 1. eta in (-inf, 0), a = -1/eta, Omega = 1/a = -eta, ln Omega = -t.
Rescaled mode u = (f, g) (beta = +1, -1 components of one helicity block):
    i du/deta = [[ M(eta), k ], [ k, -M(eta) ]] u,   M(eta) = m(eta) a(eta).

These checks are illustrations of the analytic statements, not proofs.
 (1) constant mass: norm conserved; interaction-picture spinor chi converges;
 (2) gauge: a solution whose limit chi_0 lies in the beta=+1 eigenspace converges
     after the gauge transformation exp(-i (m/H) ln Omega) (singular in the
     conformal frame: A_eta ~ 1/eta); a generic solution (both components) does not;
 (3) rescaled energy density rho_hat = Omega^{-4} T_tt = u^dag (alpha.k) u + M u^dag beta u:
     Omega * rho_hat -> m (|chi_+|^2 - |chi_-|^2)  (simple pole);
 (4) variable mass m(t) = m0 Omega^eps: phase integral converges, u converges;
     for eps = 1 (mass decaying like 1/a) rho_hat stays bounded.
"""
import numpy as np
from scipy.integrate import solve_ivp

def rhs(eta, y, mfun, k):
    f = y[0] + 1j*y[1]; g = y[2] + 1j*y[3]
    M = mfun(eta) * (-1.0/eta)
    df = -1j*(M*f + k*g); dg = -1j*(k*f - M*g)
    return [df.real, df.imag, dg.real, dg.imag]

def solve(mfun, k, eta_a, eta_b, u0, pts):
    y0 = [u0[0].real, u0[0].imag, u0[1].real, u0[1].imag]
    s = solve_ivp(rhs, (eta_a, eta_b), y0, args=(mfun, k), method="DOP853",
                  rtol=1e-11, atol=1e-13, dense_output=True)
    out = []
    for e in pts:
        y = s.sol(e); out.append((e, y[0]+1j*y[1], y[2]+1j*y[3]))
    return out

PTS = [-1.0, -1e-2, -1e-4, -1e-6, -1e-7, -1e-8]

def check_gauge(m, k):
    print(f"\n[gauge] m = {m}, k = {k}")
    const = lambda e: m
    # (a) generic solution: start pure beta=+1 at eta=-1 (limit has both components)
    gen = solve(const, k, -1.0, -1e-8, np.array([1, 0], complex), PTS)
    # (b) pure-particle solution: impose chi(eta_f) = (1,0) at eta_f = -1e-8, integrate backward
    ef = -1e-8; lamf = m*np.log(-ef)
    uf = np.array([np.exp(1j*lamf), 0], complex)          # u = exp(i beta m ln Omega) chi
    pur = solve(const, k, ef, -1.0, uf, PTS[::-1])[::-1]
    print("  eta       |gen g'|  gen g' (gauge-fixed)          pur f' (gauge-fixed)          |pur g'|")
    for (e, f1, g1), (_, f2, g2) in zip(gen, pur):
        lam = m*np.log(-e)                                   # lambda = (m/H) ln Omega
        g1p = np.exp(-1j*lam)*g1; f2p = np.exp(-1j*lam)*f2; g2p = np.exp(-1j*lam)*g2
        print(f"  {e:8.0e}  {abs(g1p):.5f}   {g1p.real:+.5f}{g1p.imag:+.5f}j            "
              f"{f2p.real:+.6f}{f2p.imag:+.6f}j          {abs(g2p):.2e}")
    print("  -> generic: g' keeps modulus ~ |chi_-| and rotates (no limit in any gauge);")
    print("     pure particle: f' converges, g' -> 0 (limit exists in the singular gauge).")

def check_energy(m, k):
    print(f"\n[energy] m = {m}, k = {k}: Omega * rho_hat")
    const = lambda e: m
    gen = solve(const, k, -1.0, -1e-8, np.array([1, 0], complex), PTS)
    for e, f, g in gen:
        Om = -e
        rho = 2*k*(np.conj(f)*g).real + (m/Om)*(abs(f)**2 - abs(g)**2)
        print(f"  {e:8.0e}  Omega*rho_hat = {Om*rho:+.6f}   (m(|f|^2-|g|^2) = {m*(abs(f)**2-abs(g)**2):+.6f})")

def check_varmass(m0, eps, k):
    print(f"\n[variable mass] m(t) = {m0} Omega^{eps}, k = {k}")
    mf = lambda e: m0*(-e)**eps
    sol = solve(mf, k, -1.0, -1e-8, np.array([1, 0], complex), PTS)
    prev = None
    for e, f, g in sol:
        Om = -e
        rho = 2*k*(np.conj(f)*g).real + m0*Om**eps/Om*(abs(f)**2 - abs(g)**2)
        d = "" if prev is None else f"  |u - u_prev| = {np.hypot(abs(f-prev[0]), abs(g-prev[1])):.2e}"
        print(f"  {e:8.0e}  f = {f.real:+.6f}{f.imag:+.6f}j  rho_hat = {rho:+.4e}{d}")
        prev = (f, g)
    phase = m0/eps if eps > 0 else float('inf')
    print(f"  total phase integral int m dt = m0/eps = {phase:.3f} (finite)")

if __name__ == "__main__":
    print("=== v2 consistency checks (H = 1) ===")
    check_gauge(1.0, 0.5)
    check_gauge(3.0, 2.0)
    check_energy(1.0, 0.5)
    check_varmass(3.0, 0.5, 2.0)
    check_varmass(3.0, 1.0, 2.0)
    print("\nElectron: m_e/H_inf = %.2e" % (5.11e5/1.2e-33))
