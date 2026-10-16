"""Precheck (precedent xiv) : equation (3.3) de Friedrich 1601.04506, recopiee
   6 Omega s - 3 nabla_eta Omega nabla^eta Omega - lambda = -(1/4) That,
   s = (1/4) Box Omega + (1/24) R Omega, That = trace physique (= -rho_hat pour la poussiere), kappa = 1.
Test sur FLRW plat Lambda + poussiere, metrique conforme plate (R = 0), Omega = 1/a(eta),
signature (-,+,+,+), Friedmann (kappa=1) : (a'/a)^2 = a^2 (lambda + rho_hat)/3, rho_hat = C/a^3."""
import sympy as sp
eta=sp.symbols('eta'); lam,C=sp.symbols('lambda C',positive=True)
a=sp.Function('a')(eta)
ap=a*sp.sqrt(a**2*(lam+C/a**3)/3)          # a' from Friedmann
app=sp.diff(ap,eta).subs(sp.Derivative(a,eta),ap)
Om=1/a
Omp=sp.diff(Om,eta).subs(sp.Derivative(a,eta),ap)
Ompp=sp.diff(Omp,eta).subs(sp.Derivative(a,eta,2),app).subs(sp.Derivative(a,eta),ap)
box=-Ompp                       # flat conformal metric, Omega depends on eta only
s=box/4
grad2=-Omp**2                   # g^{eta eta} = -1
rho=C/a**3
lhs=6*Om*s-3*grad2-lam
rhs=-sp.Rational(1,4)*(-rho)
print("residu (3.3) sur FLRW Lambda+poussiere :", sp.simplify(lhs-rhs))
print("de Sitter (C=0) : |grad Omega|^2 =", sp.simplify(grad2.subs(C,0)), " (attendu -lambda/3)")
