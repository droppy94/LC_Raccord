#!/usr/bin/env python3
"""HA-2 : variantes independantes de hx_check.py"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

s, M2, k, xi, m2 = sp.symbols('s M2 k xi m2', real=True); al = sp.symbols('alpha')
eta = sp.symbols('eta', negative=True)

print("V1. KG derive de la metrique dS (conformal time), non tape a la main")
a = -1/eta                       # H = 1
phi = sp.Function('phi')
# box phi = (1/sqrt g) d_mu (sqrt g g^{mu nu} d_nu phi), g = a^2 (-deta^2 + dx^2), homogene
sqrtg = a**4
box = (1/sqrtg)*sp.diff(sqrtg*(-1/a**2)*sp.diff(phi(eta), eta), eta)
R = sp.simplify(6*sp.diff(a, eta, 2)/a**3)
print("   R =", R)
eq = sp.expand(box - (m2 + xi*R)*phi(eta))
eqs = eq.subs(phi(eta), (-eta)**al).doit()
ind = sp.simplify(eqs/(-eta)**al*eta**2*(-1))   # normalise
print("   indicielle (doit etre alpha(alpha-3)+m2+12xi au signe pres):", sp.factor(sp.simplify(eqs*eta**2/(-eta)**al)))

print("\nV2. Poids conformes calcules symboliquement (Omega explicite)")
Om, Hr, psr, A, y, g, mm, lam = sp.symbols('Omega H_r psibarpsi_r A y g m lambda', positive=True)
sqrtghat = Om**-4; ghat_inv = Om**2
H = Om*Hr; psibarpsi = Om**3*psr
terms = {
 'Yukawa y H psibar psi (et h.c.)': sqrtghat*y*H*psibarpsi,
 'masse de jauge g^2 |H|^2 ghat^mn A A': sqrtghat*ghat_inv*g**2*H**2*A**2,
 'masse Higgs m^2 |H|^2': sqrtghat*mm**2*H**2,
 'quartique lambda |H|^4': sqrtghat*lam*H**4,
 'cubique mu H^3 (absent du SM)': sqrtghat*H**3,
 'Weinberg (L H)(L H)/M': sqrtghat*psibarpsi*H**2,
}
for n, t in terms.items():
    print(f"   {n:40s} poids Omega = {sp.degree(sp.expand(t*Om**10), Om) - 10}")

print("\nV3. Identite conforme : (box_hat - Rhat/6)(Omega phir) = Omega^3 (box - R/6) phir ; terme singulier")
phir = sp.Function('phir')
# physique : box_hat phi - m2 phi = 0 avec phi = s * phir (Omega = s = -eta), metrique rescalee plate
sv = sp.symbols('s', positive=True)
physeq = lambda f: sp.diff(f, sv, 2) - 2/sv*sp.diff(f, sv) + m2*f/sv**2   # homogene, s=-eta
expr = sp.simplify(physeq(sv*phir(sv))/sv)
print("   (eq physique)/Omega  =", sp.collect(sp.expand(expr), phir(sv)))
print("   -> terme singulier (m2 - 2)/s^2 * phir : nul ssi m2 + 12 xi = 2 (= Rhat/6)")

print("\nV4. Balayage dense du critere (c) (donnees generiques) sur M2 rationnels p/q, q<=40, -20<=M2<=20")
hits = set()
for q in range(1, 41):
    for p in range(-20*q, 20*q+1):
        M = sp.Rational(p, q)
        disc = sp.Rational(9, 4) - M
        if disc <= 0: continue
        mu = sp.sqrt(disc)
        r1, r2 = sp.Rational(3, 2) - mu, sp.Rational(3, 2) + mu
        if (r1 - 1).is_integer and (r2 - 1).is_integer and r1 >= 1:
            hits.add(M)
print("   M2 satisfaisant (c) :", sorted(hits))
print("   preuve : (a1-1)+(a2-1) = 1, entiers >= 0 -> {0,1} -> M2 = 1*2 = 2")

print("\nV5. Role de c1 = 0 (donnees fines) : on ne garde que s^alpha_max")
for M in [-10, -4, 0, sp.Rational(5,4), 2, sp.Rational(21,10), 3]:
    r = sorted(sp.solve(al*(al-3)+M, al), key=lambda z: sp.re(z))
    amax = r[-1]
    smooth = sp.im(amax) == 0 and (amax - 1).is_integer and amax - 1 >= 0
    print(f"   M2={str(M):5s} alpha_max={str(amax):18s} (a):{bool(sp.re(amax)>0)} (b):{bool(sp.re(amax)>=1)} (c):{bool(smooth)}")
print("   -> avec c1=0, (c) vaut pour M2 = -(n+1)(n-2), n entier>=1 : 2, 0, -4, -10, ...")

print("\nV6. Inhomogene k != 0, donnees fines c1=0 a M2=0 : h = sin(ks) - ks cos(ks) (sans log ?)")
hk = sp.sin(k*sv) - k*sv*sp.cos(k*sv)
print("   residu KG(M2=0) :", sp.simplify(sp.diff(hk, sv, 2) - 2/sv*sp.diff(hk, sv) + k**2*hk))
print("   h/Omega serie :", sp.series(hk/sv, sv, 0, 6))
print("   M2=2 general : h = s*(c1 cos ks + c2 sin ks), residu :",
      sp.simplify((lambda f: sp.diff(f, sv, 2) - 2/sv*sp.diff(f, sv) + (k**2 + 2/sv**2)*f)(sv*(sp.cos(k*sv)+sp.sin(k*sv)))))

print("\nV7. Neutrinos (Weinberg) : coefficient m_nu/Omega ~ h^2/s ; seuils propres")
def nu_class(M):
    r = sorted(sp.solve(al*(al-3)+M, al), key=lambda z: sp.re(z))
    if len(r) == 1: return None
    a1, a2 = r
    exps = [2*a1-1, a1+a2-1, 2*a2-1]
    A = all(sp.re(e) > -1 for e in exps)
    B = all(sp.re(e) >= 0 for e in exps)
    C = all(sp.im(e) == 0 and e.is_integer and e >= 0 for e in exps)
    return bool(A), bool(B), bool(C)
for M in [sp.Rational(1,2), 1, sp.Rational(5,4), sp.Rational(3,2), 2, sp.Rational(21,10), 3]:
    print(f"   M2={str(M):5s} (a,b,c)_nu = {nu_class(M)}")
print("   -> (b)_nu ssi M2 >= 5/4 ; (c)_nu en M2 = 5/4 ET M2 = 2")

print("\nV8. W,Z : coefficient g^2|H_r|^2 ~ s^(2 alpha - 2) (poids 0, sans 1/Omega)")
for M in [sp.Rational(1,2), 1, sp.Rational(5,4), sp.Rational(3,2), 2, sp.Rational(21,10)]:
    r = sorted(sp.solve(al*(al-3)+M, al), key=lambda z: sp.re(z))
    e = 2*r[0]-2
    print(f"   M2={str(M):5s} exposant {str(sp.nsimplify(e)):18s} borne:{bool(sp.re(e)>=0)}  integrable(ds):{bool(sp.re(e)>-1)}  s*q integrable:{bool(sp.re(e)>-2)}")

print("\nV9. Dirac homogene numerique k != 0, zone 0<M2<2 : psi_r continu, (m/Omega) psibar psi diverge ?")
def dirac(M, kk=1.0, c1=1.0, c2=0.7):
    mu = np.sqrt(9/4 - M); a1, a2 = 1.5 - mu, 1.5 + mu
    q = lambda S: (c1*S**(a1-1) + c2*S**(a2-1))     # m/Omega
    # 2-composantes (helicite fixee) : i d/ds u = [[ -q, k],[k, q]] u  (forme standard, s = -eta, signe sans importance)
    def f(S, u):
        U = u[:2] + 1j*u[2:]
        Mx = np.array([[-q(S), kk], [kk, q(S)]])
        dU = 1j*Mx @ U
        return np.concatenate([dU.real, dU.imag])
    sol = solve_ivp(f, [1.0, 1e-9], [1, 0, 0, 0], rtol=1e-10, atol=1e-12, dense_output=True, method='LSODA')
    out = []
    for S in [1e-3, 1e-5, 1e-7, 1e-9]:
        u = sol.sol(S); U = u[:2]+1j*u[2:]
        out.append((S, np.round(U, 5), q(S)*(abs(U[0])**2 - abs(U[1])**2)))
    return out
for M in [0.5, 1.5, 1.99]:
    print(f"   M2={M}")
    for S, U, rho in dirac(M):
        print(f"      s={S:.0e}  psi_r={U}  (m/Omega)*psibar psi = {rho:.3e}")

print("\nV10. Robustesse de classify() : is_integer peut renvoyer None")
for z in [sp.Rational(1,2)-sp.sqrt(7)/2, sp.sqrt(4)-1, sp.nsimplify(1.0000000001)]:
    print("   ", z, "is_integer ->", z.is_integer)
import importlib.util, sys
spec = importlib.util.spec_from_file_location('hx', '/tmp/claude-0/ha2/hx_check.py')
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    hx = importlib.util.module_from_spec(spec); spec.loader.exec_module(hx)
for M in [2.0, 1.9999999, -4, 0.0, sp.Rational(9,4), 2.25]:
    try:
        print(f"    classify({M}) ->", hx.classify(M))
    except Exception as e:
        print(f"    classify({M}) -> EXCEPTION {type(e).__name__}: {e}")
