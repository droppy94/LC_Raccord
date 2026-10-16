"""RJ2-3 : test explicite perturbatif (NOTE-216). De Sitter H=1, Omega=-eta, kappa=1, Lambda=3.
Ordre eps : quatre modes de Dirac +-k1, +-k2 (k1, k2 non colineaires), coefficients c+- donnes.
Ordre eps^2 : reponse metrique dans chaque secteur de Fourier q (jauge longitudinale : Phi, Psi, S_i transverse, H_ij TT ;
              secteur q=0 : Psi0 = 0 (Omega = 1/a exact), S = 0, Phi0 et H_ij sans trace).
Ordre eps^3 : source F de l'equation du spineur ; detection des resonances (termes Omega^{-1 +- i mu} projetes)
              et resolution formelle dans la classe K.
Usage : python3 rj2_test.py MU CAS   (CAS = generique | unexposant)"""
import sys, itertools, time
import sympy as sp
from rj2_series import Ser, mul, dOm, conjS, dag, show
from rj2_ops import gu, gl, g0, beta, alpha, eta, SGN, X, et, lin_einstein, dirac_op, dirac_lin
I=sp.I
MU=sp.Rational(sys.argv[1]) if len(sys.argv)>1 else sp.Rational(13,10)
CAS=sys.argv[2] if len(sys.argv)>2 else 'generique'
LIBRE=sp.Integer(1) if (len(sys.argv)>3 and sys.argv[3]=='libre') else sp.Integer(0)   # valeur des parametres libres (solutions homogenes)
NU=9            # ordre des series de Dirac
NG=6            # ordre de confiance de la geometrie
t0=time.time()
import functools; print=functools.partial(print,flush=True)
print(f"mu = {MU}, cas = {CAS}, NU = {NU}, NG = {NG}, parametres libres = {LIBRE}")

# ---------- ordre eps : modes
k1=sp.Matrix([1,0,1]); k2=sp.Matrix([1,0,-1])
modes={'+k1':k1,'-k1':-k1,'+k2':k2,'-k2':-k2}
def ak(k): return sum((alpha[j]*k[j] for j in range(3)),sp.zeros(4))
# donnees : c+ dans beta=+1 (composantes 0,1), c- dans beta=-1 (2,3) ; normes N(k) = N(-k) (impulsion totale nulle)
data={'+k1':([1,I],[sp.Rational(1,2),-1]),'-k1':([I,1],[1,sp.Rational(1,2)]),
      '+k2':([2,0],[0,1]),'-k2':([0,2],[1,0])}
def Nrm(cp,cm,cas): return sum(abs(z)**2 for z in cp)+(sum(abs(z)**2 for z in cm) if cas=='generique' else 0)
def mode_series(k,cp,cm,cas):
    out={}
    for j,c in ((1,sp.Matrix([cp[0],cp[1],0,0])),(-1,sp.Matrix([0,0,cm[0],cm[1]]))):
        if j==-1 and cas!='generique': continue
        w=c; out[(0,j)]=w
        for n in range(1,NU+1):
            w=(( (n+I*j*MU)*sp.eye(4)-I*MU*beta).inv())*(I*ak(k)*w)
            out[(n,j)]=w.applyfunc(sp.expand)
    return Ser(out,NU).clean()
U={m:mode_series(modes[m],*data[m],CAS) for m in modes}
for m in modes: assert sp.simplify(Nrm(*data[m],CAS)-Nrm(*data[{'+k1':'-k1','-k1':'+k1','+k2':'-k2','-k2':'+k2'}[m]],CAS))==0
# controle : u satisfait du/dOmega = i(alpha.k + beta mu/Omega) u
for m in modes:
    lhs=dOm(U[m],MU); rhs=Ser({(n,j):I*ak(modes[m])*v for (n,j),v in U[m].d.items()},U[m].N)+Ser({(n-1,j):I*MU*beta*v for (n,j),v in U[m].d.items()},U[m].N-1)
    r=(lhs-rhs); r.N=NU-1; r.clean()
    assert not r.d, ("equation de Dirac non satisfaite",m,show(r))
print("ordre eps : 4 modes, equation de Dirac verifiee jusqu'a l'ordre",NU-1)

# ---------- bilineaires par secteur : X_ab^(q) = sum_{k-k'=q} u_k'^dag g0 g_a D_b u_k
def Dser(u,k,b):
    if b==0: return dOm(u,MU).scale(-1)          # d/deta = -d/dOmega
    return u.scale(I*k[b-1])
sectors={}
for m,mp in itertools.product(modes,modes):
    q=tuple(modes[m]-modes[mp]); sectors.setdefault(q,[]).append((m,mp))
def Xab(q,a,b):
    tot=Ser({},NU)
    for (m,mp) in sectors[q]:
        tot=tot+mul(dag(U[mp]),Dser(U[m],modes[m],b),lambda A,B: (A*g0*gl[a]*B)[0])
    return tot
Tc={}
for q in sectors:
    mq=tuple(-x for x in q)
    for a in range(4):
        for b in range(a,4):
            T=(Xab(q,a,b)+Xab(q,b,a)-conjS(Xab(mq,a,b))-conjS(Xab(mq,b,a))).scale(SGN*I/4)
            Tc[(q,a,b)]=T; Tc[(q,b,a)]=T
print(f"bilineaires : {len(sectors)} secteurs ({time.time()-t0:.0f} s)")
# controle RJ : tau = Omega T_c ; tau_00 du secteur 0 = m B + Omega k.J somme sur les modes
def tau(q,a,b): return Tc[(q,a,b)].shift(1)
q0=(0,0,0)
B=Ser({},NU); kJ=Ser({},NU)
for m in modes:
    B=B+mul(dag(U[m]),U[m],lambda A,C:(A*beta*C)[0])
    kJ=kJ+mul(dag(U[m]),U[m],lambda A,C:(A*ak(modes[m])*C)[0])
r=tau(q0,0,0)-(B.scale(MU)+kJ.shift(1)); r.N=NU-2; r.clean()
print("controle RJ : tau_00(q=0) = mu B + Omega k.J :", not r.d)
print("impulsion totale : T_c,0a(q=0) =", [show(Tc[(q0,0,a)]) or '0' for a in (1,2,3)])

# ---------- ordre eps^2 : geometrie
fn={nm:sp.Function(nm)(et) for nm in ['Phi','Psi','S1','S2','S3','H11','H12','H13','H22','H23','H33']}
def hmat(q):
    E=sp.exp(I*(q[0]*X[1]+q[1]*X[2]+q[2]*X[3]))
    S=[fn['S1'],fn['S2'],fn['S3']]
    H=sp.Matrix([[fn['H11'],fn['H12'],fn['H13']],[fn['H12'],fn['H22'],fn['H23']],[fn['H13'],fn['H23'],fn['H33']]])
    h=sp.zeros(4)
    h[0,0]=-2*fn['Phi']
    for i in range(3):
        h[0,i+1]=h[i+1,0]=S[i]
        for j in range(3):
            h[i+1,j+1]=-2*fn['Psi']*(1 if i==j else 0)+H[i,j]
    return h*E, E
_cacheE={}
def lin_ops(q):
    if q in _cacheE: return _cacheE[q]
    h,E=hmat(q)
    dE,_=lin_einstein(h)
    dE=(dE/E).applyfunc(sp.expand)
    _cacheE[q]=dE; return dE
def to_series_expr(expr,vals):
    """expr lineaire en fn et leurs derivees en eta, coefficients fonctions rationnelles de eta ; vals : nom -> Ser (en Omega)."""
    expr=sp.expand(expr)
    tot=Ser({},None)
    if expr==0: return Ser({},10**6)
    derivs={}
    for nm,f in fn.items():
        for d in range(3):
            derivs[sp.diff(f,et,d) if d else f]=(nm,d)
    poly=sp.Poly(expr,*derivs.keys())
    for mon,coef in poly.terms():
        if sum(mon)==0:
            raise ValueError("terme sans inconnue")
        idx=[i for i,p in enumerate(mon) if p][0]
        key=list(derivs.keys())[idx]; nm,d=derivs[key]
        s=vals[nm]
        for _ in range(d): s=dOm(s,MU).scale(-1)
        c=sp.expand(sp.together(coef).subs(et,-sp.Symbol('Om')))
        Om=sp.Symbol('Om')
        cp=sp.Poly(sp.expand(c*Om**6),Om)   # Laurent : multiplier par Om^6
        for (pw,),cc in cp.terms():
            tot=tot+s.shift(pw-6).scale(cc)
    return tot
def solve_sector(q,jset):
    qv=sp.Matrix(q); qq=(qv.T*qv)[0]
    dE=lin_ops(q)
    names=list(fn.keys())
    if qq==0: names=['Phi','H11','H12','H13','H22','H23','H33']   # Psi0 = 0, S = 0
    sol_all={nm:Ser({},NG) for nm in fn}; report=[]
    for j in jset:
        nlo=-2; nhi=NG+3
        cs={nm:[sp.Symbol(f'c_{nm}_{n}') for n in range(nlo,nhi+1)] for nm in names}
        vals={nm:(Ser({(n,j):cs[nm][n-nlo] for n in range(nlo,nhi+1)},nhi) if nm in names else Ser({},nhi+10)) for nm in fn}
        eqs=[]
        for a in range(4):
            for b in range(a,4):
                lhs=to_series_expr(dE[a,b],vals)
                src=Tc[(q,a,b)].shift(2)          # kappa Omega^2 T_c
                res=lhs-Ser({k:v for k,v in src.d.items() if k[1]==j},src.N)
                for (n,jj),v in res.d.items():
                    if jj==j and n<=NG: eqs.append(v)
        # jauge
        if qq!=0:
            for n in range(nlo,nhi+1):
                k=n-nlo
                eqs.append(sum(qv[i]*cs['S%d'%(i+1)][k] for i in range(3)))
                Hm=sp.Matrix([[cs['H11'][k],cs['H12'][k],cs['H13'][k]],[cs['H12'][k],cs['H22'][k],cs['H23'][k]],[cs['H13'][k],cs['H23'][k],cs['H33'][k]]])
                eqs+=list(Hm*qv); eqs.append(Hm.trace())
        else:
            for n in range(nlo,nhi+1):
                k=n-nlo; eqs.append(cs['H11'][k]+cs['H22'][k]+cs['H33'][k])
        unknowns=[c for nm in names for c in cs[nm]]
        S=sp.linsolve(eqs,unknowns)
        if S==sp.EmptySet:
            report.append((j,'INCOMPATIBLE (resonance ou violation de contrainte)')); continue
        s=list(S)[0]; free=set().union(*[e.free_symbols for e in s])&set(unknowns)
        sub={u:LIBRE for u in free}
        for nm in names:
            d={}
            for n in range(nlo,nhi+1):
                v=sp.simplify(s[unknowns.index(cs[nm][n-nlo])].subs(sub))
                if v!=0 and n<=NG: d[(n,j)]=v
            sol_all[nm]=sol_all[nm]+Ser(d,NG)
        # parametres libres : exposants des solutions homogenes
        low=set()
        for nm in names:
            for n in range(nlo,NG+1):
                low|=s[unknowns.index(cs[nm][n-nlo])].free_symbols&free
        report.append((j,f"ok ; parametres libres : {len(free)}, dont atteignant un coefficient d'ordre <= NG : {len(low)}"))
    return sol_all,report
geo={}
for q in sorted(sectors):
    jset=sorted({k[1] for (qq,a,b),T in Tc.items() if qq==q for k in T.d})
    if not jset: jset=[0]
    sol,rep=solve_sector(q,jset)
    geo[q]=sol
    print(f"secteur q={q} : j={jset}")
    for r_ in rep: print("   j =",r_[0],":",r_[1])
    for nm in fn:
        if sol[nm].d: print(f"   {nm:4s}: nmin = {sol[nm].nmin()} ; termes : {show(sol[nm],8)}")
    osc=[(nm,min(n for (n,j) in sol[nm].d if j!=0)) for nm in fn if any(j!=0 for (n,j) in sol[nm].d)]
    print("   ordre minimal des termes oscillants :",osc if osc else "aucun")
print(f"geometrie : fin ({time.time()-t0:.0f} s)")

# ---------- ordre eps^3 : source du spineur
eps=sp.symbols('epsilon')
hgen=sp.Matrix(4,4,lambda i,j: sp.Function('h%d%d'%(min(i,j),max(i,j)))(*X))
psig=sp.Matrix([sp.Function('p%d'%i)(*X) for i in range(4)])
Om_=sp.Symbol('Om')
dD=dirac_lin(hgen,psig).applyfunc(sp.expand)   # masse non perturbee (Omega fixe) : seul le terme cinetique varie ; cf. rj2_lin_check
print(f"operateur de Dirac perturbe derive ({time.time()-t0:.0f} s)")
def hval(q,i,j_):
    s=geo[q]
    if i==0 and j_==0: return s['Phi'].scale(-2)
    if i==0 or j_==0:
        return s['S%d'%(max(i,j_))]
    H=s['H%d%d'%(min(i,j_),max(i,j_))]
    return (H+s['Psi'].scale(-2)) if i==j_ else H
results=[]
for q in sorted(sectors):
    qv=sp.Matrix(q)
    for m in modes:
        k=modes[m]; kt=k+qv
        # substitution : h_ab = hval * e^{iqx}, psi = u * e^{ikx} ; derivee spatiale -> i q / i k ; derivee en eta -> -d/dOmega
        F=Ser({},None)
        for comp in range(4):
            ex=dD[comp]
            # decomposer ex en sommes de produits (derivee de h) * (derivee de psi)
            for term in sp.Add.make_args(ex):
                hf=[f for f in term.atoms(sp.Function, sp.Derivative) if (isinstance(f,sp.Derivative) and str(f.expr.func).startswith('h')) or (isinstance(f,sp.Function) and str(f.func).startswith('h'))]
                pf=[f for f in term.atoms(sp.Function, sp.Derivative) if (isinstance(f,sp.Derivative) and str(f.expr.func).startswith('p')) or (isinstance(f,sp.Function) and str(f.func).startswith('p'))]
                # garder les atomes maximaux (derivees)
                hf=[f for f in hf if not any(f!=g and f in g.atoms(sp.Function) for g in hf)]
                pf=[f for f in pf if not any(f!=g and f in g.atoms(sp.Function) for g in pf)]
                assert len(hf)==1 and len(pf)==1, term
                coef=sp.simplify(term/(hf[0]*pf[0]))
                def ser_h(f):
                    base=f.expr if isinstance(f,sp.Derivative) else f
                    nm=str(base.func); i,j_=int(nm[1]),int(nm[2]); s=hval(q,i,j_)
                    vs=f.variables if isinstance(f,sp.Derivative) else ()
                    for v_ in vs:
                        s=dOm(s,MU).scale(-1) if v_==et else s.scale(I*q[X.index(v_)-1])
                    return s
                def ser_p(f):
                    base=f.expr if isinstance(f,sp.Derivative) else f
                    c_=int(str(base.func)[1]); s=Ser({kk:v[c_] for kk,v in U[m].d.items()},U[m].N)
                    vs=f.variables if isinstance(f,sp.Derivative) else ()
                    for v_ in vs:
                        s=dOm(s,MU).scale(-1) if v_==et else s.scale(I*k[X.index(v_)-1])
                    return s
                prod=mul(ser_h(hf[0]),ser_p(pf[0])).scale(coef)
                F=F+Ser({kk:sp.Matrix([v if r==comp else 0 for r in range(4)]) for kk,v in prod.d.items()},prod.N)
        # equation : du1/dOmega - i(alpha.k' + beta mu/Omega) u1 = -i g0 (dD u0)
        Fs=Ser({kk:-I*g0*v for kk,v in F.d.items()},F.N).clean()
        if not Fs.d: continue
        nmin=Fs.nmin()
        reson=[]
        for (n,j),v in Fs.d.items():
            if n==-1 and j in (1,-1):
                proj=((sp.eye(4)+j*beta)/2)*v
                if not proj.applyfunc(sp.simplify).is_zero_matrix: reson.append((n,j))
        neg=[(n,j) for (n,j) in Fs.d if n<-1]
        results.append((q,m,nmin,reson,neg))
        print(f"q={q} mode {m} -> k'={tuple(kt)} : F commence a Omega^{nmin} (+i j mu) ; resonances : {reson or 'aucune'} ; puissances < -1 : {neg or 'aucune'} ; N_F={Fs.N}")
print(f"BILAN eps^3 : {len(results)} couples (secteur, mode) ; resonances : {sum(1 for r in results if r[3])} ; puissances < -1 : {sum(1 for r in results if r[4])} ; nmin global = {min(r[2] for r in results)}")
print(f"fin ({time.time()-t0:.0f} s)")
