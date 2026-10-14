"""indep_I.py -- audit M-b, controle independant des blocs I-A et K-A / K-C.
Methode differente des scripts audites :
 - solution de mode par ansatz de serie s^n, s^n ln s (pas de fonction de Green) ;
 - deux polarisations A_y = u(s) cos(kx), A_z = v(s) sin(kx) (Q a une composante hors diagonale yz) ;
 - Christoffel de g = s^-2 eta ecrits sous forme fermee (conformement plat) ;
 - toutes les composantes R_{rho nu lambda} comparees a (3 kappa/e^2) Q_tf, y compris hors diagonale.
"""
import sympy as sp
s=sp.symbols('s',positive=True); x=sp.symbols('x',real=True)
k,e,beta,kap,lam=sp.symbols('k e beta kappa lambda',positive=True)
a1,b1,a2,b2=sp.symbols('a1 b1 a2 b2',real=True)   # u(0)=a1, u'(0)=b1 ; v(0)=a2, v'(0)=b2
L=sp.Symbol('L')
X=[s,x,sp.Symbol('y'),sp.Symbol('z')]; n=4
eta=sp.diag(-1,1,1,1)
NS=6
def mode(a,b):
    """u'' - (2 beta/s) u' + k^2 u = 0 au premier ordre en beta ; u = u0 + beta u1, u1 = sum (p_n + q_n ln s) s^n, p0=p1=0."""
    u0=a*sp.cos(k*s)+b/k*sp.sin(k*s)
    u0s=sp.expand(sp.series(u0,s,0,NS+3).removeO())
    p=sp.symbols(f'p0:{NS+3}'); q=sp.symbols(f'q0:{NS+3}')
    u1=sum((p[j]+q[j]*sp.log(s))*s**j for j in range(NS+3))
    res=sp.expand(sp.diff(u1,s,2)+k**2*u1-2/s*sp.diff(u0s,s))
    res=sp.expand(res.subs(sp.log(s),L))
    eqs=[]
    for j in range(-2,NS+1):
        cj=res.coeff(s,j) if j!=0 else res.subs(s,0) if False else res.coeff(s,j)
        cj=sp.expand(cj)
        for l in range(0,3):
            c=cj.coeff(L,l)
            if c!=0: eqs.append(c)
    unk=[v for v in list(p)+list(q) if v not in (p[0],p[1])]
    sol=sp.solve(eqs+[p[0],p[1]],unk+[p[0],p[1]],dict=True)[0]
    u1s=sp.expand(u1.subs(sol))
    # inconnues restees libres (ordres non contraints au-dela de la troncature) : on les met a 0
    u1s=u1s.subs({v:0 for v in list(p)+list(q)})
    # tronque a s^NS
    u1s=sp.expand(u1s)
    keep=sum(t for t in sp.Add.make_args(u1s) if sp.degree(t.subs(sp.log(s),1),s)<=NS)
    return sp.expand(u0s+beta*keep), sp.expand(keep)
u,u1=mode(a1,b1); v,v1=mode(a2,b2)
print("u1 (debut) :",sp.collect(sp.expand(sum(t for t in sp.Add.make_args(u1) if sp.degree(t.subs(sp.log(s),1),s)<=3)),s))
# controle on-shell de l'equation de mode (premier ordre, ordres bas)
ode=sp.expand(sp.diff(u,s,2)-2*beta/s*sp.diff(u,s)+k**2*u)
ode1=sp.expand(sp.diff(ode,beta).subs(beta,0)).subs(sp.log(s),L)
print("residu de l'equation de mode (ordre beta), ordres s^-1..s^3 :",[sp.simplify(sp.expand(ode1).coeff(s,j)) for j in range(-1,4)])
Ay=u*sp.cos(k*x); Az=v*sp.sin(k*x)
A=[0,0,Ay,Az]
F=sp.Matrix(n,n,lambda i,j: sp.diff(A[j],X[i])-sp.diff(A[i],X[j]))
I2=(1+2*beta*(lam-sp.log(s)))/e**2
first=lambda w: sp.expand(sp.expand(w).subs(beta,0)+beta*sp.diff(sp.expand(w),beta).subs(beta,0))
F2eta=sp.expand(sum(eta[i,i]*eta[j,j]*F[i,j]**2 for i in range(n) for j in range(n)))
# X^M = I^2 (F g^-1 F^T - 1/4 g F.F) avec g = eta/s^2, g^-1 = s^2 eta : X^M = s^2 I^2 (F eta F^T - 1/4 eta F2eta)
XM=(s**2*I2*(F*eta*F.T-sp.Rational(1,4)*eta*F2eta)).applyfunc(first)
gh=eta/s**2; gi=s**2*eta
def Gam(a,b,c):
    d=lambda i,j: 1 if i==j else 0
    return -(d(a,b)*d(c,0)+d(a,c)*d(b,0)+eta[b,c]*d(a,0))/s
G=[[[Gam(a,b,c) for c in range(n)] for b in range(n)] for a in range(n)]
def cov(T):
    return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
# K-A independant : div X^M + 1/4 d(I^2) F^2 (F^2 = g g F F = s^4 F2eta)
DX=cov(XM)
print("\nK-A (independant) :")
for nu in range(n):
    dv=sp.expand(sum(gi[m,m]*DX[(m,m,nu)] for m in range(n)))
    res=first(dv+sp.Rational(1,4)*sp.diff(I2,X[nu])*s**4*F2eta)
    res=sp.expand(res.subs(sp.log(s),L))
    lo=[sp.simplify(res.coeff(s,j)) for j in range(0,6)]
    dvL=sp.expand(first(dv).subs(sp.log(s),L))
    print(f"   nu={nu} : residu, coefficients s^0..s^5 :",lo," ; coefficient de beta*L dans div X^M (s^0..s^5) :",[sp.simplify(sp.diff(dvL,L).coeff(s,j)) for j in range(0,6)])
# R
trX=sp.expand(sum(gi[i,i]*XM[i,i] for i in range(n)))
print("\ntrace de X^M :",sp.simplify(trX))
Lh=(kap/2*(XM-sp.Rational(1,3)*trX*gh)).applyfunc(sp.expand)
DL=cov(Lh)
# Q a scri+ (ordre 0) : B_i = 1/2 eps_ijk F_jk, E_i = F_{0 i} ; s = 0
F0=F.applyfunc(lambda w: sp.expand(w.subs(beta,0)))
Fs0=F0.applyfunc(lambda w: sp.limit(w,s,0))
Bv=sp.Matrix([Fs0[2,3],Fs0[3,1],Fs0[1,2]]); Ev=sp.Matrix([Fs0[0,1],Fs0[0,2],Fs0[0,3]])
Q=Bv*Bv.T-Ev*Ev.T; Qtf=(Q-sp.eye(3)*Q.trace()/3).applyfunc(sp.expand)
print("Q (a scri+) =",Q.applyfunc(sp.factor))
print("\nI-A / K-C (independant) : coefficient de beta*ln s dans R_{rho nu lambda}, ordres s^0 et s^1 :")
okA=True; maxbad=[]
for rho in range(n):
    for nu in range(n):
        for la in range(nu+1,n):
            w=sp.expand((DL[(nu,la,rho)]-DL[(la,nu,rho)])/s)
            w=sp.expand(sp.diff(w,beta).subs(beta,0))
            w=sp.expand(w.subs(sp.log(s),L))
            cL=sp.expand(sp.diff(w,L))
            neg=[sp.simplify(cL.coeff(s,j)) for j in (-3,-2,-1)]
            c0=sp.expand(cL.coeff(s,0)); c1=sp.expand(cL.coeff(s,1))
            cL2=sp.simplify(sp.expand(sp.diff(w,L,2)).coeff(s,0))
            ref=0
            if nu==0 and la>=1 and rho>=1: ref=3*kap/e**2*Qtf[rho-1,la-1]
            d=sp.simplify(sp.trigsimp(c0-ref))
            if c0!=0 or ref!=0 or c1!=0 or any(neg) or cL2!=0:
                print(f"   {(rho,nu,la)} : s^0 : {sp.factor(sp.trigsimp(c0))} ; ecart a (3 kappa/e^2) Q_tf[{rho-1},{la-1}] : {d} ; s^1 : {sp.factor(sp.trigsimp(c1))} ; s^-k : {neg} ; ln^2 a s^0 : {cL2}")
            okA=okA and d==0 and not any(neg) and cL2==0
print("   loi R_ln(s^0) = (3 beta kappa/e^2) Q_tf pour toutes les composantes (rho,0,lambda), zero ailleurs, pas de ln^2 :",okA)
print("EXIT 0")
