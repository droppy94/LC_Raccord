"""VA-3 : verifications symboliques des corrections de la v2.5 corrigee."""
import sympy as sp
I=sp.I
s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-I],[I,0]]); s3=sp.Matrix([[1,0],[0,-1]])
Z=sp.zeros(2); E=sp.eye(2)
def blk(a,b,c,d): return sp.Matrix(sp.BlockMatrix([[a,b],[c,d]]))
g0=blk(E,Z,Z,-E); gs=[blk(Z,s,-s,Z) for s in (s1,s2,s3)]; G=[g0]+gs
eta=sp.diag(-1,1,1,1)
assert all(sp.simplify(G[a]*G[b]+G[b]*G[a]+2*eta[a,b]*sp.eye(4))==sp.zeros(4) for a in range(4) for b in range(4))
g5=I*G[0]*G[1]*G[2]*G[3]; assert g5*g5==sp.eye(4)
alpha=[g0*g for g in gs]; beta=g0
print("[0] Clifford {g,g}=-2eta OK ; g5^2=1 ; alpha hermitiens:", all(a==a.H for a in alpha))

# ---------- [1] Lemme 2 : relation de dispersion
Z1,Z2,m,m5,p0,p1,p2,p3=sp.symbols('Z1 Z2 m m5 p0 p1 p2 p3',real=True)
pl=[-p0,p1,p2,p3]
slp=sum((G[a]*pl[a] for a in range(4)),sp.zeros(4))
Mop=(Z1*sp.eye(4)+Z2*g5)*slp-(m*sp.eye(4)+I*m5*g5)
target=((Z1**2-Z2**2)*(p0**2-p1**2-p2**2-p3**2)-(m**2+m5**2))**2
print("[1a] det = [(Z1^2-Z2^2)(p0^2-p^2)-(m^2+m5^2)]^2 :", sp.expand(Mop.det()-target)==0)

# ---------- [1b] remise a l'echelle chirale psi_L -> s psi_L
s=sp.symbols('s',positive=True); cR,cL=sp.symbols('cR cL')
PL=(sp.eye(4)-g5)/2; PR=(sp.eye(4)+g5)/2
S=s*PL+PR; T=cR*PR+cL*PL
K=(Z1*sp.eye(4)+Z2*g5)*slp*S
sol=sp.solve(list(sp.expand(T*K-slp)),[cR,cL],dict=True)[0]
Mm=sp.expand((T*(m*sp.eye(4)+I*m5*g5)*S).subs(sol))
MR=sp.simplify((Mm*PR).trace()/2); ML=sp.simplify((Mm*PL).trace()/2)
print("[1b] normalisation T :",sol)
print("     masse apres normalisation : M_R =",MR,"; M_L =",ML)
ssq=sp.solve(sp.Eq(sp.simplify(ML*sp.conjugate(ML)),sp.simplify(MR*sp.conjugate(MR))),s)
print("     |M_L|=|M_R| (masse hermitienne a rotation chirale pres) pour s =",ssq)
sv=sp.sqrt((Z1-Z2)/(Z1+Z2))
print("     s^2 = (Z1-Z2)/(Z1+Z2) ? ",[sp.simplify(x**2-(Z1-Z2)/(Z1+Z2)) for x in ssq])
print("     |M|^2 =",sp.simplify((MR*sp.conjugate(MR)).subs(s,sv)))
# courant conserve: psibar (Z1+Z2 g5) gamma^a psi, avec psibar = psi^dag g0
phi=sp.Matrix(sp.symbols('f0:4'))
phic=sp.Matrix([sp.conjugate(x) for x in phi])
psi=S*phi
Jorig=[sp.expand((psi.H*g0*(Z1*sp.eye(4)+Z2*g5)*G[a]*psi)[0]) for a in range(4)]
Jphi=[sp.expand((phi.H*g0*G[a]*phi)[0]) for a in range(4)]
rat=[sp.simplify((Jorig[a]-(Z1-Z2)*Jphi[a]).subs(s,sv)) for a in range(4)]
print("[1c] courant original = (Z1-Z2) x courant standard de phi :",all(r==0 for r in rat),
      "(convention P_L=(1-g5)/2)")

# ---------- [2] termes sigma : sigma^{ab} R_abcd sigma^{cd} sur de Sitter
H=sp.symbols('H',positive=True)
ginv=eta  # repere orthonorme
sig=[[I/2*(G[a]*G[b]-G[b]*G[a]) for b in range(4)] for a in range(4)]
def R(a,b,c,d): return H**2*(eta[a,c]*eta[b,d]-eta[a,d]*eta[b,c])
# indices bas en repere orthonorme: sigma_ab = eta_aa eta_bb sigma^ab
acc=sp.zeros(4); acc2=sp.zeros(4)
for a in range(4):
 for b in range(4):
  acc2+=sig[a][b]*sig[a][b]*eta[a,a]*eta[b,b]
  for c in range(4):
   for d in range(4):
    r=R(a,b,c,d)
    if r!=0: acc+=sig[a][b]*r*sig[c][d]
print("[2] sigma^ab sigma_ab =",sp.simplify(acc2)[0,0],"x 1 ; sigma^ab R_abcd sigma^cd =",sp.simplify(acc)[0,0],"x 1 ; diagonal:",sp.simplify(acc-acc[0,0]*sp.eye(4))==sp.zeros(4))
# commutateur [nabla_a,nabla_b] psi = (1/4) R_abcd gamma^c gamma^d psi (convention), -> sigma^ab[.,.] propto sigma R sigma
acc3=sp.zeros(4)
for a in range(4):
 for b in range(4):
  for c in range(4):
   for d in range(4):
    r=R(a,b,c,d)
    if r!=0: acc3+=sig[a][b]*sp.Rational(1,4)*r*G[c]*G[d]
print("    sigma^ab (1/4)R_abcd g^c g^d =",sp.simplify(acc3)[0,0],"x 1 ; diag:",sp.simplify(acc3-acc3[0,0]*sp.eye(4))==sp.zeros(4))
print("    meme chose avec g5 : sigma^ab R sigma^cd g5 commute :",sp.simplify(g5*acc-acc*g5)==sp.zeros(4))

# ---------- [3] Remarque 1 : V^{-1} alpha_j V avec V = Omega^{i mu beta} M
Om,mu=sp.symbols('Omega mu',positive=True)
Pw=sp.diag(Om**(I*mu),Om**(I*mu),Om**(-I*mu),Om**(-I*mu))  # Omega^{i mu beta}
Pw2=sp.diag(Om**(2*I*mu),Om**(2*I*mu),Om**(-2*I*mu),Om**(-2*I*mu))
ok=all(sp.simplify(Pw.inv()*a*Pw-a*Pw2)==sp.zeros(4) for a in alpha)
print("[3] Omega^{-i mu beta} alpha_j Omega^{i mu beta} = alpha_j Omega^{2 i mu beta} :",ok)
# k=0 : u' = (i mu beta/Omega) u ; V = Omega^{i mu beta} M => B0 = -M^{-1} M'
print("    d/dOmega Omega^{i mu beta} = (i mu beta/Omega) Omega^{i mu beta} :",
      sp.simplify(sp.diff(Pw,Om)-(I*mu*beta/Om)*Pw)==sp.zeros(4))
# forme de Fuchs depuis (3) sur de Sitter: a=1/Omega, d/deta = -H d/dOmega
k1,k2,k3=sp.symbols('k1 k2 k3',real=True)
ak=k1*alpha[0]+k2*alpha[1]+k3*alpha[2]
Hk=ak+beta*m/Om
rhs_fuchs=(I*m/H)*beta/Om+(I/H)*ak
# i d_eta u = Hk u  -> d_Omega u = -(1/H) d_eta u = -(1/H)(-i Hk u) = (i/H) Hk u
print("    forme de Fuchs (i/H)(alpha.k + beta m/Omega) == annoncee :",sp.simplify((I/H)*Hk-rhs_fuchs)==sp.zeros(4))
# chi0+^dag beta chi0- = 0
a_,b_=sp.symbols('a0:2'),sp.symbols('b0:2')
cp=sp.Matrix([a_[0],a_[1],0,0]); cm=sp.Matrix([0,0,b_[0],b_[1]])
print("    chi0+^dag beta chi0- =",sp.simplify((cp.H*beta*cm)[0]))

# ---------- [4] Prop. 2(c), signes
e,eta_s=sp.symbols('e eta',real=True)
Hs=sp.symbols('H',positive=True)
a_dS=-1/(Hs*eta_s); Om_dS=-Hs*eta_s
theta_eta=m*a_dS  # d theta/d eta
A_eta=theta_eta/e  # A' = e^{-1} d theta
# en Omega : dOmega = -H d eta => A_Omega = A_eta * deta/dOmega = A_eta*(-1/H)
A_Om=sp.simplify((A_eta*(-1/Hs)).subs(eta_s,-Om/Hs))
print("[4] A_Omega =",A_Om," (attendu -m/(e H Omega))")

# ---------- [5] Lambda-CDM : m_eff = m(1 - R/(12 Hinf^2))
Gn,rho_m,Lam=sp.symbols('G rho_m Lambda',positive=True)
Rsc=8*sp.pi*Gn*rho_m+4*Lam   # (-,+,+,+), poussiere + Lambda, R = 8piG(rho-3p)+4Lambda
Hinf2=Lam/3
meff=sp.simplify(m*(1-Rsc/(12*Hinf2)))
print("[5] m_eff (LambdaCDM) =",meff," ; rho_Lambda = Lambda/(8 pi G) =>",sp.simplify(meff.subs(Lam,8*sp.pi*Gn*sp.Symbol('rho_L'))))
print("    sur de Sitter (rho_m=0): m_eff =",meff.subs(rho_m,0))
