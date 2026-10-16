"""Controle de dirac_lin (forme lineaire directe utilisee par rj2_test.py) par deux identites exactes :
(1) covariance conforme : h = 2 phi eta  => delta D chi = -phi D0 chi + (3/2) i gamma^a (d_a phi) chi ;
(2) diffeomorphisme : h = L_xi eta  => delta D chi = L_xi(D0 chi) - D0(L_xi chi), L_xi de Kosmann (coefficient -1/4).
(3) comparaison directe avec d/deps dirac_op (forme complete) sur un h polynomial de degre 1."""
import sympy as sp
from rj2_ops import *
t,x,y,z=X; eps=sp.symbols('epsilon')
def D0op(v): return sum((I*gu[a]*sp.diff(v,X[a]) for a in range(4)),sp.zeros(4,1))
# (1) fonctions generiques
phi=sp.Function('phi')(*X); chi=sp.Matrix([sp.Function('c%d'%i)(*X) for i in range(4)])
d1=dirac_lin(2*phi*eta,chi)
pred=-phi*D0op(chi)+sp.Rational(3,2)*I*sum((gu[a]*sp.diff(phi,X[a]) for a in range(4)),sp.zeros(4))*chi
print("(1) covariance conforme, phi et chi generiques :",(d1-pred).applyfunc(sp.expand).is_zero_matrix)
# (2) xi et chi generiques
xi=[sp.Function('xi%d'%i)(*X) for i in range(4)]; xil=[eta[a,a]*xi[a] for a in range(4)]
hL=sp.Matrix(4,4,lambda m,n: sp.diff(xil[n],X[m])+sp.diff(xil[m],X[n]))
def Lk(v): return sum((xi[mu]*sp.diff(v,X[mu]) for mu in range(4)),sp.zeros(4,1))-sp.Rational(1,4)*sum(((sp.diff(xil[b],X[a])-sp.diff(xil[a],X[b]))/2*gu[a]*gu[b] for a in range(4) for b in range(4)),sp.zeros(4))*v
d2=dirac_lin(hL,chi)
print("(2) diffeomorphisme, xi et chi generiques :",(d2-(Lk(D0op(chi))-D0op(Lk(chi)))).applyfunc(sp.expand).is_zero_matrix)
# (3) degre 1
vals=[t+2*x, y-z, 3*t-y, x+z, 2*y+t, z-x, t+x+y, 2*z, x-3*t, y+z+t]
idx=[[0,1,2,3],[1,4,5,6],[2,5,7,8],[3,6,8,9]]
h=sp.Matrix(4,4,lambda i,j: vals[idx[i][j]])
psi=sp.Matrix([1+t*y, x-2*I*z+t*t, y*z+I, t-x*y])
a1=sp.diff(dirac_op(h,eps,psi,0),eps).subs(eps,0).applyfunc(sp.expand)
print("(3) dirac_lin = d/deps dirac_op, h de degre 1 :",(a1-dirac_lin(h,psi)).applyfunc(sp.expand).is_zero_matrix)
