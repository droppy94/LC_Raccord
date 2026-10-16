"""RJ2, lemmes algebriques (NOTE-216, RJ2-1).
Conventions (FW-2) : signature (-,+,+,+), eta=diag(-1,1,1,1), {g^a,g^b} = -2 eta^{ab},
representation de Dirac : g0 = diag(1,1,-1,-1), g^i = [[0,s_i],[-s_i,0]] ; beta = g0 ; psibar = psi^dag g0.
Dirac : (i g^a nabla_a - M) psi = 0.  Tenseur cinetique : T_ab = sgn*(i/4)[psibar g_a nab_b psi + (a<->b) - h.c.],
g_a = eta_ab g^b ; sgn fixe par T_00 = +m psi^dag psi pour une particule au repos (lu a l'execution).
"""
import sympy as sp
I=sp.I
s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-I],[I,0]]); s3=sp.Matrix([[1,0],[0,-1]])
Z2=sp.zeros(2); E2=sp.eye(2)
def blk(a,b,c,d): return sp.Matrix(sp.BlockMatrix([[a,b],[c,d]]))
g0=blk(E2,Z2,Z2,-E2); gs=[blk(Z2,s,-s,Z2) for s in (s1,s2,s3)]
gu=[g0]+gs                                  # gamma^a
eta=sp.diag(-1,1,1,1)
gl=[sum((eta[a,b]*gu[b] for b in range(4)),sp.zeros(4)) for a in range(4)]  # gamma_a
for a in range(4):
    for b in range(4):
        assert sp.simplify(gu[a]*gu[b]+gu[b]*gu[a]+2*eta[a,b]*sp.eye(4))==sp.zeros(4)
print("Clifford {g^a,g^b} = -2 eta^{ab} : ok")
def bar(M): return g0*M.H*g0

# ---- signe du tenseur : particule au repos, psi = exp(-i m t) v, beta v = v
m=sp.symbols('m',positive=True)
v=sp.Matrix([1,0,0,0]); 
def Tab(psi,dpsi,a,b,sgn=1):
    pb=(psi.H*g0); 
    t=pb*gl[a]*dpsi[b]+pb*gl[b]*dpsi[a]
    t=t[0]; return sgn*sp.Rational(1,4)*I*(t-sp.conjugate(t))
dpsi=[-I*m*v,sp.zeros(4,1),sp.zeros(4,1),sp.zeros(4,1)]
T00=sp.simplify(Tab(v,dpsi,0,0))
sgn=sp.sign(T00/m)
print("T_00 avec sgn=+1 :",T00," -> sgn retenu =",sgn)

# ---- Lemme (b) : partie singuliere de T, n generique de genre temps, repere quelconque
n=sp.symbols('n0:4',real=True)
nl=sp.Matrix(n)                                 # n_a (indice bas)
nsl=sum((gu[a]*nl[a] for a in range(4)),sp.zeros(4))   # n-slash = g^a n_a
nn=sum(eta[a,a]*nl[a]**2 for a in range(4))           # eta^{ab} n_a n_b (< 0)
print("nslash^2 + (n.n) Id = 0 :", sp.simplify(nsl*nsl+nn*sp.eye(4))==sp.zeros(4))
absn2=-nn
K=-I*m*nsl/absn2
print("i nslash K = m Id :", sp.simplify(I*nsl*K-m*sp.eye(4))==sp.zeros(4))
print("nbar(nslash) = nslash :", sp.simplify(bar(nsl)-nsl)==sp.zeros(4))
x=sp.symbols('x0:4',real=True); y=sp.symbols('y0:4',real=True)
psi=sp.Matrix([x[i]+I*y[i] for i in range(4)])
Om=sp.symbols('Omega',positive=True)
dsing=[nl[b]/Om*K*psi for b in range(4)]
pbp=sp.expand((psi.H*g0*psi)[0])
ok=True
for a in range(4):
    for b in range(a,4):
        Ts=sp.expand(Tab(psi,dsing,a,b,sgn))
        target=sp.expand(m/Om*pbp*nl[a]*nl[b]/absn2)
        if sp.simplify(Ts-target)!=0: ok=False; print("ecart",a,b,sp.simplify(Ts-target))
print("Lemme (b) : T_sing_ab = (m/Omega) (psibar psi) n_a n_b / |n|^2, 10 composantes :",ok)

# ---- Lemme (c) : orthogonalite des sous-espaces propres de nslash pour l'adjoint de Dirac
r=sp.symbols('r',positive=True)
n0sub={n[0]:sp.sqrt(r**2+n[1]**2+n[2]**2+n[3]**2)}
absn=r
nsl_r=nsl.subs(n0sub)
print("|n| = r : nslash^2 = r^2 Id :", sp.simplify(nsl_r*nsl_r-r**2*sp.eye(4))==sp.zeros(4))
nsl=nsl_r
Pp=(sp.eye(4)+nsl/absn)/2; Pm=(sp.eye(4)-nsl/absn)/2
print("P+ P- = 0 :", sp.simplify(Pp*Pm)==sp.zeros(4), "; bar(P+) = P+ :", sp.simplify(bar(Pp)-Pp)==sp.zeros(4))
phi=sp.Matrix(sp.symbols('z0:4'))
cross=sp.simplify(((Pp*psi).H*g0*(Pm*phi))[0])
print("Lemme (c) : (P+ psi)bar (P- phi) =",cross)
print("valeurs propres de K :",sp.simplify(sp.Matrix(list(K.subs({n[1]:0,n[2]:0,n[3]:0}).eigenvals().keys()))).T, "(n = n0 e^0 ; mu = m/|n|)")

# ---- Noyau P1 avec n generique : S(nu nu, n) = 0
def S_of(tau,nl,g):
    gi=g.inv(); nu_=gi*nl
    tr=sum(gi[i,j]*tau[i,j] for i in range(4) for j in range(4))
    tp=tau-tr*g/3
    S={}
    for j in range(4):
        for k in range(4):
            for l in range(4):
                nt_l=sum(nu_[mm]*tp[l,mm] for mm in range(4)); nt_k=sum(nu_[mm]*tp[k,mm] for mm in range(4))
                S[(j,k,l)]=sp.Rational(1,2)*(2*(nl[k]*tp[l,j]-nl[l]*tp[k,j])-g[k,j]*nt_l+g[l,j]*nt_k)
    return S
rho=sp.symbols('rho')
tau_nn=rho*nl*nl.T/absn2
S=S_of(tau_nn,nl,eta)
print("Noyau : S(rho nu nu, n) = 0 pour n generique :", all(sp.simplify(v_)==0 for v_ in S.values()))

# ---- Lemme (a) : tau = Omega * T_c, metrique conforme generique g = Omega^{-2} eta, Omega(x^mu) quelconque
X=sp.symbols('t x y z',real=True)
W=sp.Function('W',positive=True)(*X)          # facteur conforme Omega(x)
u=[sp.Function('u%d'%i)(*X) for i in range(4)]; ub=[sp.Function('ub%d'%i)(*X) for i in range(4)]
uc=sp.Matrix(u); ucb=sp.Matrix(ub)   # ub = conjugue de u (traite comme independant)
# connexion de spin : nabla_mu psi = d_mu psi + c * omega_{mu a b} g^a g^b psi, c fixe par [c w_ab g^a g^b, g^d] = -w^d_b g^b (antisym. w)
cc=sp.symbols('cc'); wab=sp.Matrix(4,4,lambda i,j: sp.Symbol('w%d%d'%(min(i,j),max(i,j)))*(1 if i<j else (-1 if i>j else 0)))
L=sum((wab[a,b]*gu[a]*gu[b] for a in range(4) for b in range(4)),sp.zeros(4))
eqs=[]
for d_ in range(4):
    lhs=cc*(L*gu[d_]-gu[d_]*L)
    rhs=-sum((eta[d_,d_]*wab[d_,b]*gu[b] for b in range(4)),sp.zeros(4))   # w^d_b = eta^{dd} w_{db}
    eqs+=list(sp.expand(lhs-rhs))
sol=sp.solve([e for e in eqs if e!=0],cc,dict=True); cval=sol[0][cc]
print("coefficient de spin c =",cval," (nabla gamma = 0)")
def spin_conn(F):
    """g = F^2 eta, vierbein e_a^mu = F^{-1} delta_a^mu ; renvoie liste mu -> matrice c*omega_{mu ab} g^a g^b"""
    g=F**2*eta; gi=g.inv()
    Gam=[[[sum(gi[l,s_]*(sp.diff(g[s_,m_],X[n_])+sp.diff(g[s_,n_],X[m_])-sp.diff(g[m_,n_],X[s_])) for s_ in range(4))/2 for n_ in range(4)] for m_ in range(4)] for l in range(4)]
    e=lambda mu,a: (1/F if mu==a else 0)          # e_a^mu
    ed=lambda a,mu: (F if mu==a else 0)           # e^a_mu
    out=[]
    for mu in range(4):
        M=sp.zeros(4)
        for a in range(4):
            for b in range(4):
                # omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_{mu lam} e_b^lam)
                w=sum(ed(a,nu)*(sp.diff(e(nu,b),X[mu])+sum(Gam[nu][mu][lm]*e(lm,b) for lm in range(4))) for nu in range(4))
                w_low=eta[a,a]*w                  # omega_{mu a b}
                M+=cval*w_low*gu[a]*gu[b]
        out.append(sp.simplify(M))
    return out
def Tkin(psi,psic,F,a,b):
    SC=spin_conn(F)
    def D(c):   # e_c^mu nabla_mu psi
        return (sp.diff(psi,X[c])+SC[c]*psi)/F
    def Dc(c):
        return (sp.diff(psic,X[c])+SC[c].conjugate()*psic)/F
    pbar=psic.T*g0
    term=lambda a_,b_: (pbar*gl[a_]*D(b_))[0]
    termc=lambda a_,b_: (psi.T*g0*gl[a_].conjugate()*Dc(b_))[0]
    return sgn*sp.Rational(1,4)*I*(term(a,b)+term(b,a)-termc(a,b)-termc(b,a))
# physique : g = Omega^{-2} eta, psi = Omega^{3/2} psi_c ; conforme : eta, psi_c
okA=True
for (a,b) in [(a_,b_) for a_ in range(4) for b_ in range(a_,4)]:
    Tphys=Tkin(W**sp.Rational(3,2)*uc,W**sp.Rational(3,2)*ucb,1/W,a,b)
    Tc=Tkin(uc,ucb,sp.Integer(1),a,b)
    tau=Tphys/W**3
    e_=sp.expand(tau-W*Tc)
    e_=e_.replace(lambda q: isinstance(q,sp.conjugate) and q.args[0].has(W), lambda q: q.args[0])   # Omega reel
    diff_=sp.simplify(e_)
    if diff_!=0: okA=False; print("ecart (a)",a,b,diff_)
print("Lemme (a) : Omega^{-3} T_phys(e,e) = Omega T_c(e_c,e_c), Omega(x) quelconque, 10 composantes :",okA)
