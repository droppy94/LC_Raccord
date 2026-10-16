# RA-2, partie C : verifications numeriques independantes
#  C1 conservation COMPLETE (4 composantes) pour une superposition de deux modes (champ non homogene),
#     avec le signe physique de tau_0a et avec le signe du script
#  C2 particule pure : tau est-il une serie entiere en Omega (Frobenius) ou oscille-t-il a l'ordre Omega ?
#  C3 terme derivee de P0 (absent du rapport du script), generique vs particule pure
#  C4 paquet d'ondes : particule pure (2 modes) vs melange
#  C5 sensibilite m/H, k, tolerances
import numpy as np
from scipy.integrate import solve_ivp
s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]],complex)
Z=np.zeros((2,2)); I2=np.eye(2)
beta=np.block([[I2,Z],[Z,-I2]]).astype(complex)
alph=[np.block([[Z,s],[s,Z]]) for s in (s1,s2,s3)]
gup=[beta]+[beta@a for a in alph]; etaf=np.diag([1.,-1,-1,-1]); glo=[etaf[A,A]*gup[A] for A in range(4)]
H=1.0

def make(m):
    def run(kvec,e0,e1,u0,rtol=1e-12,atol=1e-14):
        ak=sum(k*a for k,a in zip(kvec,alph))
        f=lambda e,u: -1j*(ak+beta*m*(-1/(H*e)))@u
        return solve_ivp(f,(e0,e1),u0,method='DOP853',rtol=rtol,atol=atol,dense_output=True)
    return run

def Tflat_modes(modes, e, xpt, m):
    """modes = liste (kvec, sol). Renvoie T^flat_{mu nu}(eta,x) (indices bas, +---) pour psi = sum u_k e^{ik.x}"""
    a=-1/(H*e)
    u=np.zeros(4,complex); du=[np.zeros(4,complex) for _ in range(4)]
    for kvec,sol in modes:
        kv=np.array(kvec,float); ph=np.exp(1j*kv@xpt); uk=sol.sol(e)*ph
        Hk=sum(k*al for k,al in zip(kv,alph))+beta*m*a
        u+=uk; du[0]+=-1j*Hk@uk
        for i in range(3): du[i+1]+=1j*kv[i]*uk
    ub=u.conj()@beta
    T=np.zeros((4,4))
    for mu in range(4):
        for nu in range(4):
            t1=ub@glo[mu]@du[nu]; t2=ub@glo[nu]@du[mu]
            T[mu,nu]=(1j/4*(t1+t2-np.conj(t1)-np.conj(t2))).real
    return T

def conservation(modes,e,xpt,m,flip0a=False):
    a=-1/(H*e); ap=a*a*H  # da/deta = H a^2
    def That(e_,x_):
        T=Tflat_modes(modes,e_,x_,m)/(-1/(H*e_))**2
        if flip0a: T[0,1:]*=-1; T[1:,0]*=-1
        return T
    T0=That(e,xpt)
    dT=[]
    h=1e-5*abs(e); dT.append((That(e+h,xpt)-That(e-h,xpt))/(2*h))
    for i in range(3):
        dx=np.zeros(3); dx[i]=1e-5; dT.append((That(e,xpt+dx)-That(e,xpt-dx))/(2e-5))
    gi=etaf/a**2
    Gam=np.zeros((4,4,4))  # Gam[l,mu,nu]
    for l in range(4):
        for mu in range(4):
            for nu in range(4):
                Gam[l,mu,nu]=(ap/a)*((l==mu)*(nu==0)+(l==nu)*(mu==0)-etaf[mu,nu]*etaf[l,0])
    div=np.zeros(4)
    for nu in range(4):
        sacc=0
        for mu in range(4):
            for r in range(4):
                if gi[mu,r]==0: continue
                term=dT[r][mu,nu]-sum(Gam[l,r,mu]*T0[l,nu] for l in range(4))-sum(Gam[l,r,nu]*T0[mu,l] for l in range(4))
                sacc+=gi[mu,r]*term
        div[nu]=sacc
    scale=np.max(np.abs(T0))*a**-2 /abs(e)  # echelle typique d'un terme de la divergence
    return np.abs(div)/scale

print("=== C1 : conservation complete, superposition de deux modes ===")
m=0.7; run=make(m)
rng=np.random.default_rng(11)
k1=[0.6,0.0,0.8]; k2=[-0.3,0.5,0.2]
u1=rng.normal(size=4)+1j*rng.normal(size=4); u2=rng.normal(size=4)+1j*rng.normal(size=4)
sA=run(k1,-10.0,-1e-6,u1/np.linalg.norm(u1)); sB=run(k2,-10.0,-1e-6,u2/np.linalg.norm(u2))
modes=[(k1,sA),(k2,sB)]; xpt=np.array([0.3,-0.7,1.1])
for e in [-3.0,-0.5,-0.05,-0.005]:
    r_ok=conservation(modes,e,xpt,m); r_scr=conservation(modes,e,xpt,m,flip0a=True)
    print(f"  eta={e:7.3f}  residus relatifs (nu=0..3) signe physique : {np.array2string(r_ok,precision=1)}   signe du script : {np.array2string(r_scr,precision=1)}")
print("  mode unique (signe du script), test trace/nu=0 seul :", np.array2string(conservation([(k1,sA)],-0.5,xpt,m,flip0a=True),precision=1))

def tau_dust(T,e):
    Om=-H*e; a=1/Om
    return Om*T   # tau_jk = Omega^-3 T-hat(e-hat,e-hat) = Omega^-1 T-hat_coord = Omega^-1 a^-2 T^flat = Omega T^flat

print("\n=== C2 : particule pure a la limite = solution de Frobenius u_+ = Omega^{i m/H} (serie entiere) ===")
def pure_solution(run,kvec,m,Omf=1e-10,sign=+1):
    c=np.array([1,0,0,0],complex) if sign>0 else np.array([0,0,1,0],complex)
    U0=np.diag(np.exp(1j*np.diag(beta).real*(m/H)*np.log(Omf)))
    return run(kvec,-Omf/H,-10.0,U0@c)
for mH in [0.7]:
    run=make(mH); sp_=pure_solution(run,k1,mH)
    print("  Omega       |tau_ab|/Omega^2   tau00           (tau00-m)/Omega    |chi_-|/Omega   phase(chi_-) ")
    for Om in [1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]:
        e=-Om/H; T=Tflat_modes([(k1,sp_)],e,np.zeros(3),mH); tau=tau_dust(T,e)
        U0=np.diag(np.exp(1j*np.diag(beta).real*(mH/H)*np.log(Om))); chi=U0.conj().T@sp_.sol(e)
        print(f"  {Om:8.0e}   {np.linalg.norm(tau[1:,1:])/Om**2:.8f}       {tau[0,0]:+.8f}    {(tau[0,0]-mH)/Om:+.6f}        {np.linalg.norm(chi[2:])/Om:.6f}      {np.angle(chi[2]):+.4f}")
    # prediction Frobenius a l'ordre dominant : chi_- = (i/H) sigma.k chi0+ Omega e^{2 i theta}/(1+2 i m/H)  => J = 2 Omega Re(...) non oscillant
    sk=sum(k*s for k,s in zip(k1,(s1,s2,s3))); c0=np.array([1,0],complex)
    Cm=(1j/H)*sk@c0/(1+2j*mH/H)
    Jpred=np.array([2*np.real(c0.conj()@s@Cm) for s in (s1,s2,s3)])
    e=-1e-6/H; T=Tflat_modes([(k1,sp_)],e,np.zeros(3),mH); J=np.array([np.vdot(sp_.sol(e),al@sp_.sol(e)).real for al in alph])
    print("  J/Omega numerique (Omega=1e-6) :", np.round(J/1e-6,6), " prediction Frobenius 2Re(chi0+^dag sigma C) :", np.round(Jpred,6))

print("\n=== C3 : membre de droite COMPLET de (3.7) (terme derivee + S/Omega), un mode ===")
def rhs37(modes,e,m):
    def taup(e_):
        T=Tflat_modes(modes,e_,np.zeros(3),m); tau=tau_dust(T,e_)
        etaM=np.diag([-1.,1,1,1]); tau=tau.copy(); tau[0,1:]*=1; tr=np.trace(etaM@tau)
        return tau-tr*etaM/3
    h=1e-6*abs(e); dtp=(taup(e+h)-taup(e-h))/(2*h)   # d/deta ; n_0 = dOmega/deta = -H ; conformal metric plate
    tp=taup(e); Om=-H*e; n=np.array([-H,0,0,0]); etaM=np.diag([-1.,1,1,1]); nup=etaM@n
    out=[]
    for j in range(4):
        for k in range(4):
            for l in range(k+1,4):
                der=0.5*((dtp[l,j] if k==0 else 0)-(dtp[k,j] if l==0 else 0))
                S=0.5*(2*(n[k]*tp[l,j]-n[l]*tp[k,j]) - etaM[k,j]*(nup@tp[l]) + etaM[l,j]*(nup@tp[k]))/Om
                out.append((der,S))
    return np.array(out)
run=make(0.7)
sgen=run(k1,-10.0,-1e-9,u1/np.linalg.norm(u1)); spur=pure_solution(run,k1,0.7)
for lab,sol in [("generique",sgen),("particule pure",spur)]:
    D=[];S=[]
    for Om in np.logspace(-3,-8,300):
        r=rhs37([(k1,sol)],-Om/H,0.7); D.append(r[:,0]); S.append(r[:,1])
    D=np.array(D); S=np.array(S)
    print(f"  {lab:15s} terme derivee : max|.| = {np.abs(D).max():.4f}, etendue (max-min) sur Omega in [1e-8,1e-3] = {np.max(D.max(0)-D.min(0)):.4f} ;  S/Omega etendue = {np.max(S.max(0)-S.min(0)):.2e}")

print("\n=== C4 : paquet d'ondes (deux modes) ; termes croises de tau en x fixe ===")
for lab,signs in [("deux particules pures",(+1,+1)),("particule + antiparticule pures",(+1,-1))]:
    sa=pure_solution(run,k1,0.7,sign=signs[0]); sb=pure_solution(run,k2,0.7,sign=signs[1])
    vals=[]
    for Om in np.logspace(-2,-8,400):
        e=-Om/H; T=Tflat_modes([(k1,sa),(k2,sb)],e,xpt,0.7); tau=tau_dust(T,e); vals.append((Om,tau))
    t00=np.array([v[1][0,0] for v in vals]); t0a=np.array([np.linalg.norm(v[1][0,1:])/v[0] for v in vals]); tab=np.array([np.linalg.norm(v[1][1:,1:])/v[0] for v in vals])
    last=np.array([v[0] for v in vals])<1e-5
    print(f"  {lab:32s} tau00 etendue (Omega<1e-5) = {np.ptp(t00[last]):.2e} ; |tau_0a|/Omega max = {t0a.max():.3f} ; |tau_ab|/Omega etendue = {np.ptp(tab[last]):.3e} ; max = {tab.max():.3f}")

print("\n=== C5 : sensibilite (generique ; etendue de |tau_ab|/Omega et de S/Omega sur Omega in [1e-8,1e-2]) ===")
for mH in [0.05,0.3,0.7,2.0,5.0]:
    for kvec in [[0.6,0,0.8],[0.06,0,0.08],[6.,0,8.]]:
        for rtol in [1e-9,1e-12]:
            r=make(mH); sol=r(kvec,-10.0,-1e-9,u1/np.linalg.norm(u1),rtol=rtol,atol=rtol*1e-2)
            Oms=np.logspace(-2,-8,600); tab=[];Smax=[];t00=[]
            for Om in Oms:
                e=-Om/H; T=Tflat_modes([(kvec,sol)],e,np.zeros(3),mH); tau=tau_dust(T,e)
                tab.append(np.linalg.norm(tau[1:,1:])/Om); t00.append(tau[0,0])
                Smax.append(np.abs(tau[0,1:]).max()/Om)
            tab=np.array(tab); t00=np.array(t00)
            per=np.pi/mH/np.log(10)
            print(f"  m/H={mH:4.2f} |k|={np.linalg.norm(kvec):5.2f} rtol={rtol:.0e} : |tau_ab|/Om in [{tab.min():.3f},{tab.max():.3f}] ; tau00 final {t00[-1]:+.4f} ; |tau_0a|/Om max {max(Smax):.3f} ; periode de l'oscillation = {per:.1f} decades")
