# RA-2, partie B : tenseur de Dirac covariant (connexion de spin incluse) sur g-hat = a(eta)^2 * Minkowski
# Verifie : T-hat_{mu nu}[psi = a^{-3/2} u] = a^{-2} T^flat_{mu nu}[u]  (hors couche, u arbitraire)
# puis signes sur une onde plane.  Convention interne (+,-,-,-) ; T avec indices bas est le meme en (-,+,+,+).
import sympy as sp
e,x,y,z = sp.symbols('eta x y z', real=True); X=[e,x,y,z]
a = sp.Function('a', positive=True)(e)
I2=sp.eye(2); Z2=sp.zeros(2)
s=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
beta=sp.diag(1,1,-1,-1)
alpha=[sp.Matrix(sp.BlockMatrix([[Z2,si],[si,Z2]])) for si in s]
gup=[beta]+[beta*al for al in alpha]          # gamma^a, {g^a,g^b}=2 eta^{ab}, eta=diag(1,-1,-1,-1)
etaf=sp.diag(1,-1,-1,-1)
glo=[etaf[A,A]*gup[A] for A in range(4)]     # gamma_a
# tetrade e^a_mu = a delta, E_a^mu = delta/a
G = a**2*etaf; Gi = etaf/a**2
Chr=[[[sp.simplify(sum(Gi[l,d]*(sp.diff(G[d,m],X[n])+sp.diff(G[d,n],X[m])-sp.diff(G[m,n],X[d])) for d in range(4))/2)
       for n in range(4)] for m in range(4)] for l in range(4)]
# omega_mu^a_b = e^a_nu (d_mu E_b^nu + Chr^nu_{mu lam} E_b^lam)
om=[[[sp.simplify(a*(sp.diff((1/a) if nu==b else 0, X[mu]) + Chr[nu][mu][b]/a)) for b in range(4)] for nu in range(4)] for mu in range(4)]
# om[mu][A][B] = omega_mu^A_B ; omega_mu AB = eta_AC omega^C_B
Gam=[sp.zeros(4) for _ in range(4)]
for mu in range(4):
    for A in range(4):
        for B in range(4):
            Gam[mu]+= sp.Rational(1,8)*etaf[A,A]*om[mu][A][B]*(gup[A]*gup[B]-gup[B]*gup[A])
# test : nabla_mu gamma^nu = d_mu gamma^nu + Chr^nu_{mu l} gamma^l + [Gam_mu, gamma^nu] = 0
gcurv=[gup[A]/a for A in range(4)]   # gamma^mu = E_a^mu gamma^a
bad=0
for mu in range(4):
    for nu in range(4):
        M = gcurv[nu].diff(X[mu]) + sum((Chr[nu][mu][l]*gcurv[l] for l in range(4)), sp.zeros(4)) + Gam[mu]*gcurv[nu]-gcurv[nu]*Gam[mu]
        if sp.simplify(M)!=sp.zeros(4): bad+=1
print("connexion de spin : nabla gamma = 0 echoue sur", bad, "composantes sur 16")
# spineur arbitraire u = p + i q
p=[sp.Function(f'p{i}', real=True)(*X) for i in range(4)]; q=[sp.Function(f'q{i}', real=True)(*X) for i in range(4)]
u=sp.Matrix([p[i]+sp.I*q[i] for i in range(4)])
psi=a**sp.Rational(-3,2)*u
def bar(v): return v.conjugate().T*beta
gmu_lo=[a*glo[A] for A in range(4)]   # gamma_mu = e^a_mu gamma_a
def Dpsi(mu): return psi.diff(X[mu]) + Gam[mu]*psi
def Tcurv(m,n):
    t1=(bar(psi)*gmu_lo[m]*Dpsi(n))[0]; t2=(bar(psi)*gmu_lo[n]*Dpsi(m))[0]
    return sp.I/4*(t1+t2 - sp.conjugate(t1) - sp.conjugate(t2))
def Tflat(m,n):
    t1=(bar(u)*glo[m]*u.diff(X[n]))[0]; t2=(bar(u)*glo[n]*u.diff(X[m]))[0]
    return sp.I/4*(t1+t2 - sp.conjugate(t1) - sp.conjugate(t2))
bad=0
for m in range(4):
    for n in range(m,4):
        d=sp.expand(Tcurv(m,n) - Tflat(m,n)/a**2); d=sp.simplify(d.subs(sp.conjugate(sp.diff(a,e)), sp.diff(a,e)))  # a' reel
        if d!=0: bad+=1; print("  ecart",m,n,d)
print("T-hat_{mu nu}[a^-3/2 u] - a^-2 T^flat[u] : composantes non nulles :", bad, "sur 10 (hors couche, u arbitraire)")

# signes sur un mode : u(eta) e^{i k.x}, i u' = (alpha.k + beta M) u  (M = m a)
k1,k2,k3,M=sp.symbols('k1 k2 k3 M', real=True)
c=sp.Matrix([sp.Symbol(f'r{i}',real=True)+sp.I*sp.Symbol(f's{i}',real=True) for i in range(4)])
kv=[k1,k2,k3]
Hm=sum((kv[i]*alpha[i] for i in range(3)),sp.zeros(4))+beta*M
uc=c  # valeur instantanee ; u' = -i H u ; d_i u = i k_i u
du=[-sp.I*Hm*uc]+[sp.I*kv[i]*uc for i in range(3)]
def Tmode(m,n):
    t1=(bar(uc)*glo[m]*du[n])[0]; t2=(bar(uc)*glo[n]*du[m])[0]
    return sp.expand(sp.I/4*(t1+t2 - sp.conjugate(t1) - sp.conjugate(t2)))
N=(uc.conjugate().T*uc)[0]; B=(uc.conjugate().T*beta*uc)[0]; J=[(uc.conjugate().T*al*uc)[0] for al in alpha]
print("T00 - (k.J + M B) =", sp.simplify(Tmode(0,0)-(sum(kv[i]*J[i] for i in range(3))+M*B)))
print("T0i + k_i N (signe physique attendu T_0i = -k_i N) :", [sp.simplify(Tmode(0,i+1)+kv[i]*N) for i in range(3)])
print("T0i - k_i N (signe du script) :", [sp.simplify(Tmode(0,i+1)-kv[i]*N)==0 for i in range(3)])
print("Tij - (k_i J_j + k_j J_i)/2 :", [sp.simplify(Tmode(i+1,j+1)-(kv[i]*J[j]+kv[j]*J[i])/2) for i in range(3) for j in range(i,3)])
