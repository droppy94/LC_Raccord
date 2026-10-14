"""ir_i.py -- NOTE-BORD-EON-111, sous le gel de NOTE-110.
A : loi locale. Mode mixte non moyenne, fermeture locale isotrope X^R = diag(r0,r1,r1,r1)(s,x) + q (s,x), trace locale, conservation ;
    coefficient de ln s a s^0 dans toutes les composantes de R, contre (3 beta kappa/e^2) Q_tf(x) local ; role des coefficients libres.
B : dipole magnetique eteint : champs exacts a t = 0 (A = rot(m(t-r)/r)), controle de Maxwell, carte de Q_tf, integrales par region.
"""
import sympy as sp, mpmath as mp
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True)
k,e,beta,kap,u0,c,lam=sp.symbols('k e beta kappa u0 c lambda',positive=True); L=sp.symbols('L'); t=sp.symbols('t',positive=True)
W=sp.symbols('W',positive=True)
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv()
G=[[[sp.simplify(sum(gi[l,q]*(sp.diff(gh[q,m],X[r])+sp.diff(gh[q,r],X[m])-sp.diff(gh[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
def tolog(ex): return sp.expand(sp.expand(sp.expand_log(sp.expand(ex),force=True)).subs(sp.log(s),L))
def toW(ex):  # x -> W = exp(i k x)
    ex=sp.expand(sp.expand(ex).rewrite(sp.exp)); ex=ex.subs(x,sp.log(W)/(sp.I*k)); return sp.expand(sp.powsimp(sp.expand(ex)))
I2=(1+2*beta*(lam-sp.log(s)))/e**2
def green(src): return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
U1m=ser(green(ser(2/s*sp.diff(U0m,s),N+2)),N+2)
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(2*c*(s*sp.log(s)-s)+green(rest)-k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
F=sp.zeros(4,4); A_y=u*sp.cos(k*x); F[1,2]=sp.diff(A_y,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A_y,s); F[2,0]=-F[0,2]
F2g=sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
first=lambda v: sp.expand(v.subs(beta,0)+beta*sp.diff(v,beta).subs(beta,0))
XM=(I2*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)).applyfunc(lambda v: first(ser(v,6)))
F2eta=sum(eta[i,a]*eta[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
That=first(ser(-(beta/(2*e**2))*F2eta*s**4,8)); That=sp.expand(beta*sp.diff(That,beta).subs(beta,0))
# ansatz X^R
P=5
harm=lambda name: [sp.Symbol(f'{name}_{h}') for h in ('0','c','s')]
coef={}
def field(name):
    ex=0
    for j in range(0,P+1):
        for l in range(0,3):
            a0,ac,as_=harm(f'{name}{j}{l}'); coef.update({str(v):v for v in (a0,ac,as_)})
            ex+=s**j*sp.log(s)**l*(a0+ac*sp.cos(2*k*x)+as_*sp.sin(2*k*x))
    return ex
r0=field('r'); qf=field('q')
r1=(r0+That/s**2)/3
XR=sp.diag(r0,r1,r1,r1); XR[0,1]=qf; XR[1,0]=qf
def D(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
def div(T):
    DT=D(T); return [sp.expand(sum(gi[m,r]*DT[(r,m,nu)] for m in range(n) for r in range(n))) for nu in range(n)]
tot=XM+XR
dv=div(tot)
eqs=[]
pmax=3   # ordres controles : s^p, p <= pmax, pour div (X ~ s^2, div ~ s^3 apres multiplication)
for nu in (0,1):
    ex=toW(tolog(sp.expand(dv[nu])))
    ex=sp.expand(ex)
    for p in range(-1,pmax+1):
        cp=sp.expand(ex.coeff(s,p)) if p!=0 else sp.expand(ex.subs(s,0)) if False else sp.expand(ex.coeff(s,p))
        for lpow in range(0,4):
            cl=sp.expand(cp.coeff(L,lpow))
            for wp in range(-4,5):
                cw=sp.expand(cl.coeff(W,wp))
                if cw!=0: eqs.append(cw)
unk=list(coef.values())
print("A0. equations de conservation (ordres s^p, p <=",pmax,") :",len(eqs)," ; inconnues :",len(unk))
sol=sp.solve(eqs,unk,dict=True)
assert sol, "fermeture locale : systeme sans solution aux ordres controles"
sol=sol[0]
free=[v for v in unk if v not in sol]
print("    solution trouvee ; coefficients libres :",len(free))
totS=tot.applyfunc(lambda v: sp.expand(v.subs(sol)))
def tr(T): return sp.expand(sum(gi[i,j]*T[i,j] for i in range(n) for j in range(n)))
Lh=kap/2*(totS-sp.Rational(1,3)*tr(totS)*gh); DL=D(Lh)
B2=(k*u0*sp.sin(k*x))**2; E2=(c*sp.cos(k*x))**2
Q=sp.diag(0,-E2,B2); Qtf=Q-sp.eye(3)*Q.trace()/3
print("A1. coefficient de ln s a s^0 dans R_{rho nu la} (local) ; reference (3 beta kappa/e^2) Q_tf pour (i,s,i) :")
ok=True; freeL=set()
for rho in range(n):
    for nu in range(n):
        for la in range(nu+1,n):
            v=(DL[(nu,la,rho)]-DL[(la,nu,rho)])/s
            v=tolog(ser(sp.expand(v),1))
            v=sp.expand(sp.diff(v,beta).subs(beta,0))
            cl=sp.expand(sp.diff(v,L).subs(s,0))
            cl0=sp.expand(sp.diff(v,L))   # garde d'eventuels termes s^(-1) L
            neg=sp.expand(cl0-cl)
            ref=0
            if nu==0 and rho==la and rho>=1: ref=sp.expand(-3*kap/e**2*Qtf[rho-1,rho-1])  # R_{rho,0,rho} = -(R_{rho,rho,0}) convention ci-dessous
            if nu==0 and rho==la and rho>=1:
                d1=sp.simplify(cl-sp.expand(3*kap/e**2*Qtf[rho-1,rho-1])); d2=sp.simplify(cl+sp.expand(3*kap/e**2*Qtf[rho-1,rho-1]))
                print("   ",(rho,nu,la),": coef =",sp.factor(sp.trigsimp(cl))," ; ecart a +ref :",sp.trigsimp(d1)," ; a -ref :",sp.trigsimp(d2))
                ok=ok and (d1==0 or d2==0)
            elif cl!=0 or neg!=0:
                print("   ",(rho,nu,la),": coef ln s a s^0 =",sp.trigsimp(cl)," ; termes negatifs en s :",neg)
                ok=False
            fs=set(map(str,sp.sympify(cl0).free_symbols)) & set(map(str,free))
            freeL|=fs
print("   loi locale verifiee (diagonales (i,s,i)) et aucun autre ln a s^0 :",ok)
print("   coefficients libres de la fermeture presents dans un coefficient de ln :",sorted(freeL) if freeL else "aucun")
# gradients : ordre du premier terme ln dependant de k au-dela de Q_tf
v=(DL[(0,1,1)]-DL[(1,0,1)])/s; v=tolog(ser(sp.expand(v),3)); v=sp.expand(sp.diff(v,beta).subs(beta,0)); v=sp.expand(sp.diff(v,L))
print("A2. coefficient de ln s dans R_(1,0,1) jusqu'a s^2 (structure des corrections) :",sp.collect(sp.expand(sp.trigsimp(v)),s))
# ---------------- B : dipole ----------------
rr,th,ph=sp.symbols('r theta phi',positive=True); tt=sp.symbols('t',real=True); D_,w,m0=sp.symbols('D w m0',positive=True)
xs,ys,zs=sp.symbols('xs ys zs',real=True)
R_=sp.sqrt(xs**2+ys**2+zs**2)
f=lambda tv: (1-sp.tanh((tv+D_)/w))/2
Pi=sp.Matrix([0,0,m0*f(tt-R_)/R_])
def curl(V): return sp.Matrix([sp.diff(V[2],ys)-sp.diff(V[1],zs),sp.diff(V[0],zs)-sp.diff(V[2],xs),sp.diff(V[1],xs)-sp.diff(V[0],ys)])
Avec=curl(Pi); Bv=curl(Avec); Ev=-sp.diff(Avec,tt)
vals={D_:10,w:sp.Rational(1,2),m0:1}
pt={xs:sp.Rational(3,1),ys:sp.Rational(-2,1),zs:sp.Rational(5,1),tt:sp.Rational(-1,3)}
divB=sp.N(sum(sp.diff(Bv[i],v) for i,v in enumerate((xs,ys,zs))).subs(vals).subs(pt))
far=curl(Ev)+sp.diff(Bv,tt); amp=curl(Bv)-sp.diff(Ev,tt)
print("\nB0. controle Maxwell en un point generique (D=10, w=1/2) : div B =",divB," ; |rot E + dB/dt| =",sp.N(far.subs(vals).subs(pt).norm())," ; |rot B - dE/dt| =",sp.N(amp.subs(vals).subs(pt).norm()))
Bt=Bv.subs(tt,0); Et=Ev.subs(tt,0)
def BE_at(px,py,pz): 
    sub={xs:px,ys:py,zs:pz}; sub.update(vals)
    return sp.Matrix([sp.N(b.subs(sub)) for b in Bt]), sp.Matrix([sp.N(q.subs(sub)) for q in Et])
def Qtf_at(px,py,pz):
    Bn,En=BE_at(px,py,pz); Qm=Bn*Bn.T-En*En.T; return Qm-sp.eye(3)*Qm.trace()/3, Bn, En
print("B1. carte de Q_tf a scri+ (t = 0), D = 10, w = 1/2, m0 = 1 :")
for lab,p in (("r=3 (boule deja traversee)",(sp.Rational(3)/sp.sqrt(2),0,sp.Rational(3)/sp.sqrt(2))),("r=10 (coquille)",(sp.Rational(10)/sp.sqrt(2),0,sp.Rational(10)/sp.sqrt(2))),("r=10, equateur",(10,0,0)),("r=20 (reliquat statique)",(sp.Rational(20)/sp.sqrt(2),0,sp.Rational(20)/sp.sqrt(2)))):
    Qt,Bn,En=Qtf_at(*p)
    print(f"   {lab} : |B| = {sp.N(Bn.norm(),4)}, |E| = {sp.N(En.norm(),4)}, B.E = {sp.N(Bn.dot(En),3)}, norme de Q_tf = {sp.N(sp.sqrt(sum(v**2 for v in Qt)),4)}")
# forme radiale : B = alpha(r)(3 n n.z - z) + gamma(r)(n n.z - z) ; E = eps(r) n x z
Bz_axis=sp.simplify(Bt[2].subs({xs:0,ys:0,zs:rr})); Bz_eq=sp.simplify(Bt[2].subs({xs:rr,ys:0,zs:0})); Ey_eq=sp.simplify(Et[1].subs({xs:rr,ys:0,zs:0}))
alpha=Bz_axis/2; gamma=-Bz_eq-alpha; eps=-Ey_eq
# controle de la forme en un point generique
nvec=sp.Matrix([xs,ys,zs])/R_; ez=sp.Matrix([0,0,1])
Bform=alpha.subs(rr,R_)*(3*nvec*nvec[2]-ez)+gamma.subs(rr,R_)*(nvec*nvec[2]-ez); Eform=eps.subs(rr,R_)*nvec.cross(ez)
gp={xs:sp.Rational(2),ys:sp.Rational(3),zs:sp.Rational(-7)}; gp.update(vals)
print("B2. forme radiale controlee en un point generique : |B - forme| =",sp.N((Bt-Bform).subs(gp).norm())," ; |E - forme| =",sp.N((Et-Eform).subs(gp).norm()))
# moyennes angulaires des structures
thv,phv=sp.symbols('thv phv',real=True)
nn=sp.Matrix([sp.sin(thv)*sp.cos(phv),sp.sin(thv)*sp.sin(phv),sp.cos(thv)])
def aavg(M): return M.applyfunc(lambda v: sp.simplify(sp.integrate(sp.integrate(sp.expand(v)*sp.sin(thv),(thv,0,sp.pi)),(phv,0,2*sp.pi))/(4*sp.pi)))
Sa=3*nn*nn[2]-ez; Sg=nn*nn[2]-ez; Se=nn.cross(ez)
tf=lambda M: M-sp.eye(3)*M.trace()/3
AA=tf(aavg(Sa*Sa.T)); GG=tf(aavg(Sg*Sg.T)); AG=tf(aavg(Sa*Sg.T+Sg*Sa.T)); EE=tf(aavg(Se*Se.T))
P0=sp.diag(-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(2,3))
cA,cG,cAG,cE=[sp.simplify(M[2,2]/P0[2,2]) for M in (AA,GG,AG,EE)]
print("B3. moyennes angulaires (parties sans trace, en unites de diag(-1/3,-1/3,2/3)) : <SaSa> =",cA,", <SgSg> =",cG,", <SaSg+SgSa> =",cAG,", <SeSe> =",cE)
qrad=sp.lambdify(rr,(cA*alpha**2+cG*gamma**2+cAG*alpha*gamma-cE*eps**2).subs(vals),'mpmath')
def integ(a,b): return mp.quad(lambda r: 4*mp.pi*r**2*qrad(r),[a,b])
mp.mp.dps=20
Iin=integ(0.05,10-6*0.5); Ishell=integ(10-6*0.5,10+6*0.5); Iout=integ(10+6*0.5,mp.inf)
print("B4. integrale de Q_tf (composante zz, unites de 2/3) par region : boule r<D-3w :",mp.nstr(Iin,6)," ; coquille |r-D|<3w :",mp.nstr(Ishell,6)," ; reliquat r>D+3w :",mp.nstr(Iout,6))
Iout_th=cA*4*sp.pi/(3*(10+3)**3)
print("    reliquat, prediction statique pure cA * 4 pi/(3 r_min^3) :",sp.N(Iout_th,6))
mdd2=mp.quad(lambda tv: mp.diff(lambda u: (1-mp.tanh((u+10)/0.5))/2, tv, 2)**2, [-mp.inf,mp.inf])
print("    coquille, prediction rayonnee (4/5)*... : 4 pi * <(eB eB - eE eE)>_zz * int mdd^2 ; <SgSg - SeSe> zz/(2/3) =",sp.simplify(cG-cE)," ; 4 pi (cG - cE) int mdd^2 =",mp.nstr(4*mp.pi*float(cG-cE)*mdd2,6))
# domaine de l'action plate : |F| << 1/r^2 en unites ou e est absorbe (m0 = 1)
print("B5. domaine : |B| r^2 au reliquat (r=20) =",sp.N((BE_at(sp.Rational(20)/sp.sqrt(2),0,sp.Rational(20)/sp.sqrt(2))[0].norm())*400,4)," (doit etre << 1 : ici m0/r ; condition r >> m0)")
print("\nEXIT 0")
