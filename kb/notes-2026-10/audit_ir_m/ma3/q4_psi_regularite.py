"""Q4 : regularite de psi, solution de box_eta^2 psi = -J, J = sqrt(g) F^2 a l'ordre beta^0 pour le mode.
Decomposition psi = psi0(s) + psi2(s) cos(2kx). On montre que toute solution est analytique en s (pas de ln s)."""
import sympy as sp
s, x, k, u0, c = sp.symbols('s x k u0 c', positive=True)
U0 = u0*sp.cos(k*s) + c/k*sp.sin(k*s)
J = sp.expand(sp.simplify(2*(k**2*U0**2*sp.sin(k*x)**2 - sp.diff(U0, s)**2*sp.cos(k*x)**2)))
J = sp.expand(sp.fu(J.rewrite(sp.exp)).rewrite(sp.cos)) if False else J
# projections en x
J0 = sp.simplify(sp.integrate(J, (x, 0, sp.pi/k))*k/sp.pi)
J2 = sp.simplify(sp.integrate(J*sp.cos(2*k*x), (x, 0, sp.pi/k))*2*k/sp.pi)
print('[calcule] J0(s) =', J0)
print('[calcule] J2(s) =', J2)
print('[calcule] reconstruction J - J0 - J2 cos2kx =', sp.simplify(J - J0 - J2*sp.cos(2*k*x)))
p0 = sp.Function('p0'); p2 = sp.Function('p2')
# box_eta = -d_s^2 + d_x^2 ; sur cos(2kx) : box = -(d_s^2 + 4k^2)
sol0 = sp.dsolve(sp.Eq(sp.diff(p0(s), s, 4), -J0), p0(s))
op2 = lambda f: sp.diff(f, s, 4) + 8*k**2*sp.diff(f, s, 2) + 16*k**4*f
sol2 = sp.dsolve(sp.Eq(op2(p2(s)), -J2), p2(s))
print('[calcule] psi0 general =', sol0.rhs)
print('[calcule] psi2 general =', sp.simplify(sol2.rhs))
print('[calcule] ln s present ?', sol0.rhs.has(sp.log(s)) or sol2.rhs.has(sp.log(s)))
# consequence pour T^(b) : dS/dh_y = dS/dh_z = J/6 ; dS/dh_x = -(1/6) d_s^2 box psi
