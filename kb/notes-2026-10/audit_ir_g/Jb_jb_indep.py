"""jb_indep.py -- audit J-b, chaine independante de ir_g.py.
Representation : dependance spatiale en polynomes de Laurent (zx,zy,zz) avec d/dx = i zx d/dzx ;
ln s = symbole L avec d/ds L = 1/s ; mode beta par Frobenius (ansatz polynome en s et L) ;
Christoffel par la formule conforme ; moyenne spatiale = terme constant en (zx,zy,zz).
"""
import sympy as sp, sys
s=sp.symbols('s',positive=True); L=sp.symbols('L')
e,beta,kap,lam,Cr=sp.symbols('e beta kappa lambda C_r',positive=True)
zx,zy,zz=sp.symbols('zx zy zz'); Z=[zx,zy,zz]; I=sp.I
NS=6  # ordre de troncature en s

def dS(f): return sp.expand(sp.diff(f,s)+sp.diff(f,L)/s)
def dX(f,j): return sp.expand(I*Z[j]*sp.diff(f,Z[j]))
def sdeg(t):
    return sp.Mul.make_args(t) and sum(sp.Integer(q.as_base_exp()[1]) for q in sp.Mul.make_args(t) if q.as_base_exp()[0]==s)
def trunc(f,o=NS,b=True):
    f=sp.expand(f)
    if b: f=sp.expand(f.subs(beta,0)+beta*sp.diff(f,beta).subs(beta,0))
    return sp.expand(sum(t for t in sp.Add.make_args(f) if sdeg(t)<=o)) if f!=0 else 0
def const_term(f):
    f=sp.expand(f); out=0
    for t in sp.Add.make_args(f):
        if not any(t.has(zv) for zv in Z): out+=t
    return sp.expand(out)

# ---------- mode : u'' + k^2 u - (2 beta/s) u' = 0 au premier ordre, Frobenius ----------
_cache={}
def mode(k2,u0,c):
    """renvoie U0+beta U1 tronque, k2 = |k|^2 ; U1 particuliere sans homogene."""
    k=sp.sqrt(k2)
    U0=sp.expand(sp.series(u0*sp.cos(k*s)+c/k*sp.sin(k*s),s,0,NS+3).removeO())
    M=NS+2; b=sp.symbols('b0:%d'%(M+1)); d=sp.symbols('d0:%d'%(M+1))
    U1=sum((b[n]+d[n]*L)*s**n for n in range(M+1))
    eq=sp.expand((dS(dS(U1))+k2*U1-2/s*dS(U0))*s**2)
    eqs=[]
    for n in range(0,M+1):
        for lp in (0,1):
            eqs.append(eq.coeff(s,n).coeff(L,lp))
    sol=sp.solve(eqs+[b[0],b[1]],list(b)+list(d),dict=True)
    assert len(sol)==1, sol
    U1s=sp.expand(U1.subs(sol[0]))
    # residu de controle
    res=sp.expand((dS(dS(U1s))+k2*U1s-2/s*dS(U0))*s**2)
    resl=sum(res.coeff(s,n) for n in range(0,M))
    assert sp.simplify(resl)==0
    return sp.expand(U0+beta*U1s), sp.expand(U0)

def build(modes):
    """modes : liste de (n=(n1,n2,n3) entiers, eps_cos (3), u0c, cc, eps_sin (3), u0s, cs).
    A_i = sum eps_cos_i u_c(s) cos(n.x) + eps_sin_i u_s(s) sin(n.x)."""
    A=[0,0,0]; A0=[0,0,0]; Abd_B=[0,0,0]; Abd_E=[0,0,0]
    for (nv,ec,u0c,cc,es,u0s,cs) in modes:
        k2=sum(q**2 for q in nv); P=zx**nv[0]*zy**nv[1]*zz**nv[2]
        cosP=(P+1/P)/2; sinP=(P-1/P)/(2*I)
        uc,uc0=mode(k2,u0c,cc); us,us0=mode(k2,u0s,cs)
        for i in range(3):
            A[i]+=ec[i]*uc*cosP+es[i]*us*sinP
            A0[i]+=ec[i]*uc0*cosP+es[i]*us0*sinP
            Abd_B[i]+=ec[i]*u0c*cosP+es[i]*u0s*sinP          # partie magnetique pure (A constant en s)
            Abd_E[i]+=ec[i]*cc*s*cosP+es[i]*cs*s*sinP        # partie electrique pure (A = c s)
    return [sp.expand(a) for a in A],[sp.expand(a) for a in A0],Abd_B,Abd_E

def Fmat(A):
    # coordonnees (s,x,y,z), A_s = 0
    Af=[0]+list(A); F=sp.zeros(4,4)
    def d(f,mu): return dS(f) if mu==0 else dX(f,mu-1)
    for m in range(4):
        for nn in range(4):
            if m<nn:
                F[m,nn]=sp.expand(d(Af[nn],m)-d(Af[m],nn)); F[nn,m]=-F[m,nn]
    return F
eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=eta*s**2
def Tmax(F,I2):
    F2=sp.expand(sum(gi[a,a]*gi[b,b]*F[a,b]**2 for a in range(4) for b in range(4)))
    T=sp.zeros(4,4)
    for m in range(4):
        for nn in range(4):
            T[m,nn]=sp.expand(I2*(sum(F[m,a]*F[nn,a]*gi[a,a] for a in range(4))-sp.Rational(1,4)*gh[m,nn]*F2))
    return T

# Christoffel conformes : g = Omega^2 eta, Omega = 1/s, d ln Omega = -ds/s
def Gam(l,m,nn):
    dl=[-1/s,0,0,0]
    return (int(l==m)*dl[nn]+int(l==nn)*dl[m]-eta[m,nn]*eta[l,l]*dl[l])
GG=[[[Gam(l,m,nn) for nn in range(4)] for m in range(4)] for l in range(4)]
# controle contre la formule metrique
X4=[s]+list(sp.symbols('x y z'))
for l in range(4):
    for m in range(4):
        for nn in range(4):
            ref=sum(gi[l,q]*(sp.diff(gh[q,m],X4[nn])+sp.diff(gh[q,nn],X4[m])-sp.diff(gh[m,nn],X4[q])) for q in range(4))/2
            assert sp.simplify(ref-GG[l][m][nn])==0

def cov(T):  # T homogene (fonction de s, L) ; nabla_r T_{mq}
    out={}
    for r in range(4):
        for m in range(4):
            for q in range(4):
                v=(dS(T[m,q]) if r==0 else 0)-sum(GG[p][r][m]*T[p,q]+GG[p][r][q]*T[m,p] for p in range(4))
                out[(r,m,q)]=sp.expand(v)
    return out
def div(T):
    DT=cov(T); return [sp.expand(sum(gi[m,m]*DT[(m,m,nn)] for m in range(4))) for nn in range(4)]
def trg(T): return sp.expand(sum(gi[i,i]*T[i,i] for i in range(4)))

def analyse(name,modes,verbose=True):
    print("\n=== cas",name,"===")
    A,A0,AB,AE=build(modes)
    I2=(1+2*beta*(lam-L))/e**2
    F=Fmat(A); XM=Tmax(F,I2).applyfunc(lambda v: trunc(v))
    # G1 : coefficient de beta L a l'ordre s^2, non moyenne
    TB=Tmax(Fmat(AB),1/e**2); TE=Tmax(Fmat(AE),1/e**2)
    okG1=True; logs_low=True
    for i in range(4):
        for j in range(i,4):
            v=sp.diff(XM[i,j],beta)
            cl=sp.expand(sp.diff(v,L))
            for o in (0,1): logs_low = logs_low and sp.expand(cl.coeff(s,o))==0
            lead=sp.expand(cl.coeff(s,2))
            ref=sp.expand((-2*(TB[i,j]-TE[i,j])).coeff(s,2))
            if sp.expand(lead-ref)!=0: okG1=False; print("   G1 ecart",(i,j),sp.factor(lead-ref))
    pt=sp.expand(sp.diff(sp.diff(XM[0,1],beta),L))+sp.expand(sp.diff(sp.diff(XM[0,2],beta),L))+sp.expand(sp.diff(sp.diff(XM[0,3],beta),L))
    print("G1 (non moyenne, s^2) : accord -2(T_B - T_E) :",okG1," ; pas de log aux ordres s^0,s^1 :",logs_low,
          " ; log dans X_{s i} a l'ordre s^2 :",[sp.expand(sp.diff(sp.diff(XM[0,i],beta),L)).coeff(s,2) for i in (1,2,3)])
    # moyenne spatiale
    XMh=XM.applyfunc(const_term)
    F0=Fmat(A0); F2eta=sp.expand(sum(eta[a,a]*eta[b,b]*F0[a,b]**2 for a in range(4) for b in range(4)))
    That=trunc(-(beta/(2*e**2))*const_term(F2eta)*s**4,NS+1)
    # Q = <B_i B_j - E_i E_j> au bord (ordre zero, s -> 0)
    Fb=F0.applyfunc(lambda v: sp.expand(v).subs(s,0))
    E=[Fb[0,i] for i in (1,2,3)]        # E_i ~ d_s A_i (signe sans effet sur Q)
    B=[Fb[2,3],Fb[3,1],Fb[1,2]]
    Q=sp.Matrix(3,3,lambda i,j: const_term(B[i]*B[j]-E[i]*E[j]))
    Qtf=Q-sp.eye(3)*Q.trace()/3
    # conservation de X^M seul (composantes spatiales) ; Poynting moyen
    dvM=div(XMh)
    print("Poynting moyen <X_{s i}> :",[sp.factor(XMh[0,i]) for i in (1,2,3)])
    print("div X^M spatiale (doit etre 0 a l'ordre tronque) :",[sp.expand(sum(t for t in sp.Add.make_args(v) if sdeg(t)<=NS-2)) for v in dvM[1:]])
    # fermeture C-iso
    r0=sp.Function('r0')(s)
    r1=(r0+That/s**2)/3; XR=sp.diag(r0,r1,r1,r1)
    # equation pour r0 : div_0 = 0 ; on resout par ansatz polynome en s, L, plus homogene Cr s^p
    eq0=sp.expand(div(XMh+XR)[0])
    # forme : a r0' + b r0/s + source ; determination de l'exposant homogene
    p=sp.symbols('p'); hom=sp.expand(eq0.subs(r0,0)) ;
    ode=sp.expand(eq0-hom)
    pe=sp.solve(sp.simplify(ode.subs(r0,s**p).doit()/s**(p-1)),p) if False else None
    sol=sp.dsolve(sp.Eq(eq0,0),r0)
    r0s=sp.expand(sol.rhs.subs(sp.Symbol('C1'),Cr))
    r0s=sp.expand(r0s.subs(sp.log(s),L))
    tot=(XMh+XR.subs(r0,r0s)).applyfunc(lambda v: sp.expand(sp.expand(v.doit()).subs(sp.log(s),L)))
    dv=[trunc(v,NS-3) for v in div(tot)]
    print("conservation totale (tronquee) :",dv, " ; r0 =",sp.factor(sp.expand(r0s)))
    trT=trg(tot)
    Lh=(kap/2*(tot-sp.Rational(1,3)*trT*gh)).applyfunc(sp.expand)
    DL=cov(Lh)
    # toutes les composantes R_{rho nu lam}, coefficient de beta L a l'ordre s^0, et termes singuliers
    res={}
    sing=[]
    for rho in range(4):
        for nu in range(4):
            for la in range(nu+1,4):
                v=sp.expand((DL[(nu,la,rho)]-DL[(la,nu,rho)])/s)   # Omega^{-1} = 1/s (Omega = s)
                vb=sp.expand(sp.diff(v,beta).subs(beta,0)); v0=sp.expand(v.subs(beta,0))
                lnc=sp.expand(sp.diff(vb,L))
                for t in sp.Add.make_args(sp.expand(vb)):
                    if t!=0 and sdeg(t)<0 and t.has(L): sing.append(((rho,nu,la),t))
                res[(rho,nu,la)]=sp.expand(lnc.coeff(s,0)) if lnc!=0 else 0
    ok=True
    for key,v in res.items():
        rho,nu,la=key
        if nu==0 and rho>0:
            ref=sp.expand(3*kap/e**2*Qtf[rho-1,la-1])
        else:
            ref=0
        d=sp.simplify(v-ref)
        if d!=0: ok=False; print("   ECART",key,": ln =",sp.factor(v)," ref =",sp.factor(ref))
        elif verbose and v!=0: print("   R",key,"ln-coef =",sp.factor(v))
    print("termes log singuliers (puissances negatives de s) a l'ordre beta :",sing[:3])
    print("Q =",Q.applyfunc(sp.factor).tolist())
    print("G2 tensoriel R_{i s j}|ln = (3 beta kappa/e^2) Qtf_ij, autres composantes sans log :",ok)
    fs=set().union(*[sp.sympify(v).free_symbols for v in res.values()])
    print("symboles dans les coefficients ln :",fs, " ; lambda ou C_r present :",(lam in fs) or (Cr in fs))
    return Q,res,ok

if __name__=="__main__":
    u0,c=sp.symbols('u0 c',real=True)
    a1,a2,b1,b2,c1,c2,d1,d2=sp.symbols('a1 a2 b1 b2 c1 c2 d1 d2',real=True)
    which=sys.argv[1] if len(sys.argv)>1 else 'all'
    cases={
     'T1_script':[((1,0,0),(0,1,0),u0,c,(0,0,0),0,0)],
     'T2_oblique':[((1,1,0),(1,-1,1),a1,b1,(0,0,0),0,0)],
     'T3_deux_modes':[((1,0,0),(0,1,1),a1,b1,(0,0,0),0,0),((0,1,0),(1,0,2),a2,b2,(0,0,0),0,0)],
     'T4_helicoidal':[((1,0,0),(0,1,0),a1,b1,(0,0,1),a2,b2)],
     'T5_meme_k_secteurs_croises':[((0,1,1),(1,0,0),a1,b1,(0,1,-1),a2,b2)],
    }
    for nm,md in cases.items():
        if which in ('all',nm): analyse(nm,md)
    print("\nEXIT 0")
