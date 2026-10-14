"""ir_l.py -- NOTE-BORD-EON-116, sous le gel de NOTE-115.
A : champ a eta = 0 d'une source eteinte (Green retardee) : a = i(J+ - J-)/(2k), b = -(J+ + J-)/2 ; controle numerique.
B : decomposition exacte de Q_k : -1/2 L(J+J+^dag + J-J-^dag) - 1/2 Re(J+.J-^*) (delta - k k) ; identite R M R^T - M = -2 L(M).
C : integrales angulaires de L pour : dipole magnetique lineaire, dipole electrique lineaire, dipole magnetique tournant, dipole chiral (p, m en quadrature),
    ensemble isotrope, motifs E et B purs l = 2, combinaison generique.
D : terme d'interference : phase e^{2ik t0} ; moyenne sur une bande de k.
"""
import sympy as sp, mpmath as mp, random
# ---------- A ----------
mp.mp.dps=30
k0=mp.mpf('1.7'); t0=mp.mpf(-6); sig=mp.mpf('0.8')
J=lambda t: mp.exp(-((t-t0)/sig)**2)*(1+mp.mpf('0.3')*mp.sin(3*t))
a_num=mp.quad(lambda t: mp.sin(k0*(0-t))/k0*J(t),[-mp.inf,t0,0])
dA_num=mp.quad(lambda t: mp.cos(k0*(0-t))*J(t),[-mp.inf,t0,0])
Jp=mp.quad(lambda t: mp.exp(1j*k0*t)*J(t),[-mp.inf,t0,0]); Jm=mp.quad(lambda t: mp.exp(-1j*k0*t)*J(t),[-mp.inf,t0,0])
a_f=1j*(Jp-Jm)/(2*k0); b_f=-(Jp+Jm)/2
print("A. a (Green) =",mp.nstr(a_num,12)," ; a (formule) =",mp.nstr(a_f,12))
print("   b = -dA/dt (Green) =",mp.nstr(-dA_num,12)," ; b (formule) =",mp.nstr(b_f,12))
# ---------- B ----------
m11,m22=sp.symbols('m11 m22',real=True); m12=sp.symbols('m12')
M=sp.Matrix([[m11,m12],[sp.conjugate(m12),m22]]); R=sp.Matrix([[0,-1],[1,0]])
Lm=sp.Matrix([[(m11-m22)/2,sp.re(m12)],[sp.re(m12),(m22-m11)/2]])
lhs=(R*M*R.T-M); real_lhs=lhs.applyfunc(lambda v: sp.simplify((v+sp.conjugate(v))/2))
print("\nB1. Re(R M R^T - M) + 2 L(M) =",sp.simplify(real_lhs+2*Lm))
C=M  # meme forme pour C hermitienne
print("    Re(R C R^T + C) - tr(C) 1 =",(R*C*R.T+C).applyfunc(lambda v: sp.simplify((v+sp.conjugate(v))/2))-sp.eye(2)*(m11+m22))
# controle direct de la decomposition sur des J+ J- complexes aleatoires
random.seed(3)
def cvec(): return sp.Matrix([sp.Rational(random.randint(-5,5),3)+sp.I*sp.Rational(random.randint(-5,5),3) for _ in range(2)])
Jp_,Jm_=cvec(),cvec(); kk=sp.Rational(7,5)
a_=sp.I*(Jp_-Jm_)/(2*kk); b_=-(Jp_+Jm_)/2
Bv=sp.I*kk*(R*a_)
Qk=(Bv*Bv.H-b_*b_.H).applyfunc(lambda v: sp.simplify((v+sp.conjugate(v))/2))
def L2(Mx): 
    Mr=Mx.applyfunc(lambda v: sp.simplify((v+sp.conjugate(v))/2)); return Mr-sp.eye(2)*Mr.trace()/2
pred=-L2(Jp_*Jp_.H+Jm_*Jm_.H)/2 - sp.re(sp.expand((Jp_.H*Jm_)[0]))*sp.eye(2)/2
print("B2. Q_k (plan transverse) - [-1/2 L(J+J+^dag + J-J-^dag) - 1/2 Re(J+.J-^*) 1] =",sp.simplify(Qk-pred))
# ---------- C ----------
th,ph=sp.symbols('theta phi',real=True)
n=sp.Matrix([sp.sin(th)*sp.cos(ph),sp.sin(th)*sp.sin(ph),sp.cos(th)])
P3=sp.eye(3)-n*n.T
def cross(u,v): return u.cross(v)
def L3(v):  # tenseur de polarisation lineaire 3D (transverse, sans trace) de v v^dag
    M=v*v.H; Mr=M.applyfunc(lambda z: sp.simplify(sp.re(sp.expand(z)))); return Mr-P3*Mr.trace()/2
def angavg(T): return T.applyfunc(lambda z: sp.simplify(sp.integrate(sp.integrate(sp.expand(sp.simplify(z))*sp.sin(th),(th,0,sp.pi)),(ph,0,2*sp.pi))/(4*sp.pi)))
mx,my,mz=sp.symbols('m_x m_y m_z',real=True); mv=sp.Matrix([mx,my,mz])
tf=lambda T: sp.simplify(T-sp.eye(3)*T.trace()/3)
# dipole magnetique lineaire : J_perp ∝ n x m ; dipole electrique : J_perp ∝ P p
Lm_lin=angavg(L3(cross(n,mv))); Lp_lin=angavg(L3(P3*mv))
print("\nC1. dipole magnetique lineaire : <L> =",Lm_lin," ; -(2/5)(mm - m^2/3) ? ",sp.simplify(Lm_lin+sp.Rational(2,5)*(mv*mv.T-mv.dot(mv)*sp.eye(3)/3))==sp.zeros(3,3))
print("    dipole electrique lineaire : <L> =",Lp_lin," ; +(2/5)(pp - p^2/3) ? ",sp.simplify(Lp_lin-sp.Rational(2,5)*(mv*mv.T-mv.dot(mv)*sp.eye(3)/3))==sp.zeros(3,3))
x_,y_,z_=sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([0,0,1])
Lrot=angavg(L3(cross(n,x_-sp.I*y_)))   # m tournant dans le plan (x,y) : composante a +omega
print("C2. dipole magnetique tournant (x - i y) : <L> =",Lrot)
# dipole chiral : p et m colineaires (axe z), en quadrature : J_perp ∝ P p - n x m avec m = -i p (a +omega)
pz=z_; Jch=P3*pz - cross(n,-sp.I*pz)
Lch=angavg(L3(Jch)); print("C3. dipole chiral (p = z, m = -i z) : L par direction =",sp.simplify(L3(Jch))," ; <L> =",Lch)
Jch2=P3*pz - cross(n,sp.I*pz); print("    meme helicite opposee (m = +i z) : L par direction =",sp.simplify(L3(Jch2)))
# ensemble isotrope d'orientations : moyenne de -(2/5)(mm - 1/3) sur m unitaire isotrope
al,bt=sp.symbols('alpha beta_o',real=True)
mu=sp.Matrix([sp.sin(al)*sp.cos(bt),sp.sin(al)*sp.sin(bt),sp.cos(al)])
iso=(-sp.Rational(2,5)*(mu*mu.T-sp.eye(3)/3)).applyfunc(lambda z: sp.simplify(sp.integrate(sp.integrate(z*sp.sin(al),(al,0,sp.pi)),(bt,0,2*sp.pi))/(4*sp.pi)))
print("C4. ensemble isotrope d'orientations :",iso)
# motifs l = 2 purs E et B : L_E = P A P - 1/2 tr(PAP) P ; L_B = Rn L_E (Rn = produit vectoriel par n)
A=sp.Matrix([[1,2,0],[2,-3,1],[0,1,2]])
LE=P3*A*P3; LE=LE-P3*LE.trace()/2
Rn=sp.Matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
LB=Rn*LE; LB=(LB+LB.T)/2
print("C5. motif E pur l = 2 : <L_E> =",angavg(LE)," ; motif B pur l = 2 : <L_B> =",angavg(LB))
# combinaison generique : p, m complexes aleatoires + quadrupole electrique Q_e (J_perp ∝ P Q_e n)
random.seed(11)
rc=lambda: sp.Rational(random.randint(-4,4),2)+sp.I*sp.Rational(random.randint(-4,4),2)
pg=sp.Matrix([rc() for _ in range(3)]); mg=sp.Matrix([rc() for _ in range(3)])
Qe=sp.Matrix(3,3,lambda i,j: 0); 
for i in range(3):
    for j in range(i,3):
        v=rc(); Qe[i,j]=v; Qe[j,i]=v
Qe=Qe-sp.eye(3)*Qe.trace()/3
Jg=P3*(pg+sp.I*Qe*n)-cross(n,mg)
Lg=angavg(L3(Jg)); print("C6. combinaison generique (p, m, quadrupole) : <L> =",Lg," ; nul ? ",Lg==sp.zeros(3,3))
# ---------- D ----------
kk_,tt0=sp.symbols('k t0',real=True)
print("\nD1. pulse en t0 : J+ . J-^* ∝ exp(2 i k t0) ; Re -> cos(2 k t0) ; moyenne sur une bande k in [k1, k1 + dk] :",
      sp.simplify(sp.integrate(sp.cos(2*kk_*tt0),(kk_,sp.Symbol('k1'),sp.Symbol('k1')+sp.Symbol('dk')))/sp.Symbol('dk')))
print("\nEXIT 0")
