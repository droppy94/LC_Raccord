"""Controles des operateurs (FW-1) : fond de Sitter, invariance de jauge de l'Einstein linearise, transformation conforme de Dirac."""
import sympy as sp
from rj2_ops import *
eps=sp.symbols('epsilon')
# 1) fond : E_b = 0 ; 2) jauge : h = L_xi(gb)/a^2 avec xi generique => delta E = 0
xi=[sp.Function('xi%d'%i)(*X) for i in range(4)]
a=-1/et; gb=a**2*eta
Lg=sp.zeros(4)
for m in range(4):
    for n in range(4):
        Lg[m,n]=sum(xi[l]*sp.diff(gb[m,n],X[l])+gb[l,n]*sp.diff(xi[l],X[m])+gb[m,l]*sp.diff(xi[l],X[n]) for l in range(4))
hg=(Lg/a**2).applyfunc(sp.simplify)
dE,Eb=lin_einstein(hg)
print("fond de Sitter (H=1, Lambda=3) : E_b = 0 :", Eb.is_zero_matrix)
print("jauge : delta E[L_xi g_b] = 0 (10 comp.) :", all(sp.simplify(dE[m,n])==0 for m in range(4) for n in range(m,4)))
# 3) Dirac : h = 2 phi eta  => delta D chi = -phi D0 chi + (3/2) i gamma^a (d_a phi) chi  (partie sans masse)
phi=sp.Function('phi')(*X)
chi=sp.Matrix([sp.Function('c%d'%i)(*X) for i in range(4)])
D=dirac_op(2*phi*eta,eps,chi,0)
dD=sp.diff(D,eps).subs(eps,0)
D0=sum((I*gu[a]*sp.diff(chi,X[a]) for a in range(4)),sp.zeros(4,1))
pred=-phi*D0+sp.Rational(3,2)*I*sum((gu[a]*sp.diff(phi,X[a]) for a in range(4)),sp.zeros(4))*chi
print("Dirac : covariance conforme au premier ordre :", (dD-pred).applyfunc(sp.simplify).is_zero_matrix)
# 4) Dirac : diffeomorphisme h = L_xi eta  => delta D chi = - xi^mu d_mu (D0 chi) + D0(xi^mu d_mu chi) + rotation de Lorentz locale
#    controle plus simple : xi constant (translation) => delta D chi = -(xi.d)D0 chi + D0((xi.d)chi) = 0 trivialement ; on teste xi lineaire (Lorentz global)
# 4) diffeomorphisme : h = L_xi eta. Prediction : delta D chi = s*(D0(Lk chi) - Lk(D0 chi)),
#    Lk = derivee de Lie spinorielle (Kosmann) : xi.d chi + cK d_[a xi_b] g^a g^b chi + c2 (div xi) chi (c2 : poids, attendu nul ou non selon la forme).
#    Champs explicites polynomiaux (identite lineaire en xi et chi : un cas generique de degre 2 suffit a tester les coefficients).
t,x,y,z=X
xi=[t*x+y**2, x*z-t**2+3*y, y*t+2*z*x, x**2-y*z+t]
xil=[eta[a,a]*xi[a] for a in range(4)]
chi=sp.Matrix([1+t*y, x-2*I*z+t*t, y*z+I, t-x*y])
hL=sp.zeros(4)
for m in range(4):
    for n in range(4):
        hL[m,n]=sp.diff(xil[n],X[m])+sp.diff(xil[m],X[n])
cK,c2=sp.symbols('cK c2')
divxi=sum(sp.diff(xi[a],X[a]) for a in range(4))
def Lk(v): return sum((xi[mu]*sp.diff(v,X[mu]) for mu in range(4)),sp.zeros(4,1))+cK*sum(((sp.diff(xil[b],X[a])-sp.diff(xil[a],X[b]))/2*gu[a]*gu[b] for a in range(4) for b in range(4)),sp.zeros(4))*v+c2*divxi*v
def D0op(v): return sum((I*gu[a]*sp.diff(v,X[a]) for a in range(4)),sp.zeros(4,1))
D=dirac_op(hL,eps,chi,0); dD=sp.diff(D,eps).subs(eps,0).applyfunc(sp.expand)
found=False
for sgn_ in (1,-1):
    res=(dD-sgn_*(D0op(Lk(chi))-Lk(D0op(chi)))).applyfunc(sp.expand)
    eqs=[sp.Poly(c,*X).coeffs() for c in res if c!=0]
    eqs=[e for l in eqs for e in l]
    so=sp.solve(eqs,[cK,c2],dict=True)
    if so:
        found=True
        print("diffeomorphisme : signe",sgn_,", (cK, c2) =",(so[0].get(cK),so[0].get(c2)),", identite exacte (toutes composantes, tous monomes) :",(res.subs(so[0])).applyfunc(sp.expand).is_zero_matrix)
if not found: print("diffeomorphisme : aucune valeur de cK ne convient")
