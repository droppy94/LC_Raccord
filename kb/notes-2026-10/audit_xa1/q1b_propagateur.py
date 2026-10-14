"""XA-1 Q1(b) : propagateur de Cauchy de box^2 et lissite en s a valeurs distributions.
P = d_s^2 - Delta (box = -P, box^2 = P^2). Transformee de Fourier partielle en x :
P^2 -> (d_s^2 + k^2)^2. Propagateur K(s) : K(0)=K'(0)=K''(0)=0, K'''(0)=delta."""
import sympy as sp

s, k, r, rho = sp.symbols('s k r rho', positive=True)
sr = sp.symbols('s', real=True)
Kh = (sp.sin(k*sr) - k*sr*sp.cos(k*sr))/(2*k**3)
ode = sp.simplify(sp.diff(Kh, sr, 4) + 2*k**2*sp.diff(Kh, sr, 2) + k**4*Kh)
print("(d_s^2+k^2)^2 Khat =", ode)
print("Khat(0), Khat'(0), Khat''(0), Khat'''(0) =",
      [sp.simplify(sp.diff(Kh, sr, j).subs(sr, 0)) for j in range(4)])
print("serie de Khat en s (entiere, pas de log) :", sp.series(Kh, sr, 0, 9))
# Transformee de Fourier 3D de l'indicatrice de la boule de rayon s, divisee par 8 pi
ball = sp.integrate(sp.sin(k*rho)/(k*rho)*rho**2, (rho, 0, s))*4*sp.pi/(8*sp.pi)
print("FT[ theta(s-r)/(8 pi) ](k) =", sp.simplify(ball))
print("egal a Khat(s) pour s>0 :", sp.simplify(ball - Kh.subs(sr, s)) == 0)
# Solution generale homogene en Fourier : (A + B s) cos ks + (C + D s) sin ks : entiere en s
A, B, C, D = sp.symbols('A B C D')
gen = (A + B*sr)*sp.cos(k*sr) + (C + D*sr)*sp.sin(k*sr)
print("solution generale de (d_s^2+k^2)^2 v = 0 verifiee :",
      sp.simplify(sp.diff(gen, sr, 4) + 2*k**2*sp.diff(gen, sr, 2) + k**4*gen) == 0)
# exposants indiciels de box^2 en s=0 (partie principale en s : d_s^4) : n(n-1)(n-2)(n-3)
n = sp.symbols('n')
print("polynome indiciel :", sp.factor(sp.ff(n, 4)), "-> racines 0,1,2,3 simples, aucune racine double : pas de log force")
