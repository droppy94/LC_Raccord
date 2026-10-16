"""RB-2 : les controles de dirac_lin sont-ils aveugles a une erreur sur le coefficient de spin ?
On remplace CSPIN par une valeur fausse et on cherche cK libre dans l'identite de diffeomorphisme."""
import sympy as sp, sys
sys.path.insert(0,'.')
import rj2_ops as R
from rj2_ops import X, eta, gu, I
t,x,y,z=X
def D0op(v): return sum((I*gu[a]*sp.diff(v,X[a]) for a in range(4)),sp.zeros(4,1))
xi=[t*x+y**2, x*z-t**2+3*y, y*t+2*z*x, x**2-y*z+t]
xil=[eta[a,a]*xi[a] for a in range(4)]
chi=sp.Matrix([1+t*y, x-2*I*z+t*t, y*z+I, t-x*y])
hL=sp.Matrix(4,4,lambda m,n: sp.diff(xil[n],X[m])+sp.diff(xil[m],X[n]))
phi=t*x+y*z-2*t**2
cK,c2=sp.symbols('cK c2')
def Lk(v): return sum((xi[mu]*sp.diff(v,X[mu]) for mu in range(4)),sp.zeros(4,1))+cK*sum(((sp.diff(xil[b],X[a])-sp.diff(xil[a],X[b]))/2*gu[a]*gu[b] for a in range(4) for b in range(4)),sp.zeros(4))*v+c2*sum(sp.diff(xi[a],X[a]) for a in range(4))*v
for cs in (sp.Rational(-1,4),sp.Rational(1,4),sp.Rational(-1,2),sp.Integer(0)):
    R.CSPIN=cs
    d2=R.dirac_lin(hL,chi)
    found=[]
    for s in (1,-1):
        res=(d2-s*(Lk(D0op(chi))-D0op(Lk(chi)))).applyfunc(sp.expand)
        eqs=[c for e in res if e!=0 for c in sp.Poly(e,*X).coeffs()]
        so=sp.solve(eqs,[cK,c2],dict=True)
        if so: found.append((s,so))
    d1=R.dirac_lin(2*phi*eta,chi)
    pred=-phi*D0op(chi)+sp.Rational(3,2)*I*sum((gu[a]*sp.diff(phi,X[a]) for a in range(4)),sp.zeros(4))*chi
    cc=(d1-pred).applyfunc(sp.expand).is_zero_matrix
    print(f"CSPIN={cs} : diffeo (signe, cK, c2) ajustables : {found or 'aucun'} ; covariance conforme : {cc}")
