"""ir_g.py -- NOTE-BORD-EON-108, sous le gel de NOTE-107.
A : structure du terme beta ln s de X^M pour un mode mixte (u0, c) : comparaison a -2 (T_B - T_E), Poynting.
B : (2.17), partie homogene, C-iso, mode mixte : coefficients de ln s de R en fonction de <B^2>, <E^2> ; test R_ln = (3 beta kappa/e^2) * Q_sans_trace.
C : coupure de source (magnetostatique a eta_off, D = |eta_off|) : Q par mode, moyenne spectrale k^n e^{-k/k*}.
D : dipole magnetique coherent : moyenne angulaire de la partie survivante ; ensemble isotrope d'orientations.
"""
import sympy as sp
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True)
k,e,beta,kap,u0,c,lam,Cr=sp.symbols('k e beta kappa u0 c lambda C_r',positive=True); L=sp.symbols('L'); t=sp.symbols('t',positive=True)
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv()
G=[[[sp.simplify(sum(gi[l,q]*(sp.diff(gh[q,m],X[r])+sp.diff(gh[q,r],X[m])-sp.diff(gh[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
def tolog(ex): return sp.expand(sp.expand(sp.expand_log(sp.expand(ex),force=True)).subs(sp.log(s),L))
I2=(1+2*beta*(lam-sp.log(s)))/e**2
def green(src): return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
U1m=ser(green(ser(2/s*sp.diff(U0m,s),N+2)),N+2)
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(2*c*(s*sp.log(s)-s)+green(rest)-k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
r1=sp.expand(sp.series(sp.expand((sp.diff(I2*sp.diff(u,s),s)+k**2*I2*u)*e**2),s,0,3).removeO())
print("A0. residu de l'equation de mode, ordre beta, jusqu'a s^2 :", sp.simplify(tolog(sp.diff(r1,beta).subs(beta,0))))
def Fof(A_y):
    F=sp.zeros(4,4); F[1,2]=sp.diff(A_y,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A_y,s); F[2,0]=-F[0,2]; return F
def XM_of(F,I2f):
    F2g=sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
    return I2f*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)
XM=XM_of(Fof(u*sp.cos(k*x)),I2)
# T_B, T_E : Maxwell de la seule partie magnetique (u -> u0 constant) ou electrique (A_y -> c s cos kx), I^2 = 1/e^2
TB=XM_of(Fof(u0*sp.cos(k*x)),1/e**2); TE=XM_of(Fof(c*s*sp.cos(k*x)),1/e**2)
print("A1. coefficient de beta ln s dans X^M (ordre dominant s^2) compare a -2 (T_B - T_E) :")
okA=True
for i in range(4):
    for j in range(i,4):
        v=tolog(ser(XM[i,j],4)); cl=sp.expand(sp.diff(sp.diff(v,beta).subs(beta,0),L))
        lead=sp.simplify(sp.limit(cl/s**2,s,0))
        ref=sp.simplify(sp.limit(sp.expand(-2*(TB[i,j]-TE[i,j]))/s**2,s,0))
        d=sp.simplify(lead-ref); okA=okA and d==0
        if lead!=0 or ref!=0: print("   ",(i,j),": log =",sp.factor(lead)," ; -2(TB-TE) =",sp.factor(ref)," ; ecart",d)
print("   accord sur toutes les composantes :",okA, " (composante (0,1) = Poynting)")
# ---------- B ----------
def D(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
def div(T):
    DT=D(T); return [sp.expand(sum(gi[m,r]*DT[(r,m,nu)] for m in range(n) for r in range(n))) for nu in range(n)]
def tr(T): return sp.expand(sum(gi[i,j]*T[i,j] for i in range(n) for j in range(n)))
avg=lambda v: sp.integrate(sp.expand(v),(x,0,2*sp.pi/k))*k/(2*sp.pi)
XMh=XM.applyfunc(lambda v: ser(avg(v),6)); XMh=XMh.applyfunc(lambda v: sp.expand(v.subs(beta,0)+beta*sp.diff(v,beta).subs(beta,0)))
F=Fof(u*sp.cos(k*x)); F2eta=sum(eta[i,a]*eta[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
That=sp.expand(ser(-(beta/(2*e**2))*avg(F2eta)*s**4,7)); That=sp.expand(beta*sp.diff(That,beta).subs(beta,0))
r0=sp.Function('r0')(s); r1f=(r0+That/s**2)/3; XR=sp.diag(r0,r1f,r1f,r1f)
sol=sp.dsolve(sp.Eq(div(XMh+XR)[0],0),r0); r0s=sol.rhs.subs(sp.Symbol('C1'),Cr)
tot=(XMh+XR.subs(r0,r0s)).applyfunc(lambda v: sp.expand(v.doit()))
print("\nB0. conservation totale (ordre tronque) :",[sp.simplify(tolog(ser(v,5))) for v in div(tot)])
Lh=kap/2*(tot-sp.Rational(1,3)*tr(tot)*gh); DL=D(Lh)
Bsq=k**2*u0**2/2; Esq=c**2/2
Q=sp.diag(0,-Esq,Bsq)   # <B_iB_j - E_iE_j>, axes x,y,z (B selon z, E selon y)
Qtf=Q-sp.eye(3)*Q.trace()/3
print("B1. coefficient de ln s dans R_{i s i} (s -> 0) compare a (3 beta kappa/e^2) Q_sans_trace_ii :")
okB=True
for i in (1,2,3):
    v=(DL[(0,i,i)]-DL[(i,0,i)])/s
    v=tolog(ser(sp.expand(v),1)); v=sp.expand(sp.diff(v,beta).subs(beta,0)); cl=sp.expand(sp.diff(v,L).subs(s,0))
    ref=sp.expand(3*kap/e**2*Qtf[i-1,i-1]); d=sp.simplify(cl-ref); okB=okB and d==0
    print("   i =",i,": coef ln s =",sp.factor(cl)," ; reference =",sp.factor(ref)," ; ecart",d)
print("   accord :",okB)
print("   trace : coefficient de ln s dans la partie isotrope de R :", sp.simplify(sum(sp.expand(sp.diff(sp.expand(sp.diff(tolog(ser(sp.expand((DL[(0,i,i)]-DL[(i,0,i)])/s),1)),beta).subs(beta,0)),L).subs(s,0)) for i in (1,2,3))))
# ---------- C ----------
kk,Dd,a,ks,nn=sp.symbols('k D a k_star n',positive=True); eta_=sp.symbols('eta',real=True)
uf=a*sp.cos(kk*(eta_+Dd))           # libre apres eta_off = -D, magnetostatique : u(-D)=a, u'(-D)=0
B0=sp.simplify(kk*uf.subs(eta_,0)); E0=sp.simplify(-sp.diff(uf,eta_).subs(eta_,0))
print("\nC1. a eta = 0 : amplitude B =",B0," ; amplitude E =",E0," ; B^2 - E^2 =",sp.simplify(sp.trigsimp(B0**2-E0**2)))
# Q par mode (repere transverse, eps_B et eps_E unitaires orthogonaux) : B^2 eB eB - E^2 eE eE
# = (B^2+E^2)/2 (eB eB - eE eE) + (B^2-E^2)/2 (eB eB + eE eE)
print("    partie (eB eB - eE eE) : (B^2+E^2)/2 =",sp.simplify((B0**2+E0**2)/2)," (independante de D)")
print("    partie (eB eB + eE eE) : (B^2-E^2)/2 =",sp.simplify(sp.trigsimp((B0**2-E0**2)/2)))
x_=sp.symbols('x',positive=True)
for nv in (2,4,5):
    I0=sp.integrate(kk**nv*sp.exp(-kk/ks),(kk,0,sp.oo)); Ic=sp.simplify(sp.integrate(kk**nv*sp.exp(-kk/ks)*sp.cos(2*kk*Dd),(kk,0,sp.oo)))
    r=sp.simplify((Ic/I0).subs(Dd,x_/(2*ks)))
    asym=sp.limit(r*x_**(nv+1),x_,sp.oo)
    print(f"C2. n = {nv} : <cos 2kD> spectral = {sp.simplify(sp.re(sp.expand_complex(r)))} ; x = 2 k* D ; x^(n+1) * <cos 2kD> -> {asym} ; valeur a x = 0 : {r.subs(x_,0)}")
# ---------- D ----------
th,ph=sp.symbols('theta phi',real=True); mx,my,mz=sp.symbols('m_x m_y m_z',real=True)
kh=sp.Matrix([sp.sin(th)*sp.cos(ph),sp.sin(th)*sp.sin(ph),sp.cos(th)]); m=sp.Matrix([mx,my,mz])
eE=kh.cross(m)                      # direction de A (et de E) : transverse, prop. a k x m
eB=kh.cross(eE)                     # direction de B : k^ x eE = -m_perp
def angavg(M): return M.applyfunc(lambda v: sp.simplify(sp.integrate(sp.integrate(sp.expand(v)*sp.sin(th),(th,0,sp.pi)),(ph,0,2*sp.pi))/(4*sp.pi)))
Sm=angavg(eB*eB.T-eE*eE.T); Sp=angavg(eB*eB.T+eE*eE.T)
print("\nD1. dipole magnetique : <eB eB - eE eE>_angles =",Sm)
print("    attendu (4/5)(m m - m^2 1/3) :",sp.simplify(Sm-sp.Rational(4,5)*(m*m.T-(m.dot(m))*sp.eye(3)/3))==sp.zeros(3,3))
print("    <eB eB + eE eE>_angles =",Sp)
# ensemble isotrope d'orientations : moyenne de m m -> m^2 1/3
Smiso=Sm.subs({mx*my:0}).applyfunc(lambda v: v)  # placeholder
al,bt=sp.symbols('alpha beta_o',real=True)
mrot=sp.Matrix([sp.sin(al)*sp.cos(bt),sp.sin(al)*sp.sin(bt),sp.cos(al)])
Smr=(sp.Rational(4,5)*(mrot*mrot.T-sp.eye(3)/3)).applyfunc(lambda v: sp.simplify(sp.integrate(sp.integrate(v*sp.sin(al),(al,0,sp.pi)),(bt,0,2*sp.pi))/(4*sp.pi)))
print("D2. ensemble isotrope d'orientations (|m| = 1) : <(4/5)(m m - 1/3)> =",Smr)
print("\nEXIT 0")
