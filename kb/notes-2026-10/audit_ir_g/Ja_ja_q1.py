# Q1 : mode unique k||x, eps||y ; coefficient de beta ln s a l'ordre s^2 dans X^M non moyenne
import sympy as sp
from ja_core import *

u0, c, k = sp.symbols('u0 c k', positive=True)
u = mode_u(u0, c, k)
print('u1 (premiers termes) =', sp.expand(trunc(sp.expand(u).coeff(beta, 1), 3)))
# verif equation de mode a O(beta)
res = sp.diff(I2*sp.diff(u, s), s) + k**2*I2*u
res1 = sp.expand(sp.expand(res*e**2).coeff(beta, 1))
print('residu O(beta) jusqu a s^4 :', trunc(res1, 4))
A = sp.Matrix([0, 0, u*sp.cos(k*x), 0])  # A_mu en (s,x,y,z)
F = sp.zeros(4)
for m in range(4):
    for n in range(4):
        F[m, n] = sp.diff(A[n], X[m]) - sp.diff(A[m], X[n])
XM, FF = XM_from_Fpair(F, F)
names = ['s', 'x', 'y', 'z']
Ex, Bz = sp.symbols('E B')  # E = E_y(x) = c cos kx , B = B_z(x) = -k u0 sin kx
sub = {c: Ex/sp.cos(k*x), u0: -Bz/(k*sp.sin(k*x))}
print('\nChamps a scri : E_y = c cos(kx), B_z = -k u0 sin(kx)')
print('E_y(s) ordre s^0, coefficient de beta ln s :', coeff_sp_ln(sp.expand(sp.diff(u, s)).coeff(beta, 1), 0, 1), '(x c)')
for m in range(4):
    for n in range(m, 4):
        cf = coeff_sp_ln(sp.expand(XM[m, n]).coeff(beta, 1), 2, 1)
        if cf != 0 or (m, n) == (0, 1):
            print('X^M_%s%s : [s^2 beta ln s] =' % (names[m], names[n]), sp.factor(cf), '  =', sp.simplify(sp.factor(cf.subs(sub))))
        c0 = coeff_sp_ln(sp.expand(XM[m, n]).coeff(beta, 0), 2, 0)
        if c0 != 0:
            print('      (ordre beta^0, s^2 :', sp.simplify(c0.subs(sub)), ')')
