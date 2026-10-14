"""indep_I_ferm.py -- audit M-b. Structure de la fermeture H-loc et contre-exemple hors classe.
1. divergence d'un X^R = diag(r0,r1,r1,r1) + q (s,x), trace That, sous forme fermee ;
2. compensation exacte des sources : div X^M |_0 + That/s = 0 au premier ordre ;
3. tenseur TT conserve sans trace X' = s^2 ln s diag(0,0,f(x),-f(x)) : log dans R a s^0 (hors H-loc, flat tensor non lisse).
"""
import sympy as sp
s=sp.symbols('s',positive=True); x=sp.symbols('x',real=True); kap=sp.symbols('kappa',positive=True)
X=[s,x,sp.Symbol('y'),sp.Symbol('z')]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=s**2*eta
L=sp.Symbol('L')
def Gam(a,b,c):
    d=lambda i,j: 1 if i==j else 0
    return -(d(a,b)*d(c,0)+d(a,c)*d(b,0)+eta[b,c]*d(a,0))/s
G=[[[Gam(a,b,c) for c in range(n)] for b in range(n)] for a in range(n)]
def cov(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
def div(T):
    D=cov(T); return [sp.expand(sum(gi[m,m]*D[(m,m,nu)] for m in range(n))) for nu in range(n)]
r0=sp.Function('r0')(s,x); q=sp.Function('q')(s,x); Th=sp.Function('That')(s,x)
r1=(r0+Th/s**2)/3
XR=sp.diag(r0,r1,r1,r1); XR[0,1]=q; XR[1,0]=q
print("trace de X^R :",sp.simplify(sum(gi[i,i]*XR[i,i] for i in range(n))))
dv=div(XR)
f0=-s**4*sp.diff(r0/s**2,s)+s**2*sp.diff(q,x)+Th/s
f1=-s**4*sp.diff(q/s**2,s)+s**2*sp.diff(r1,x)
print("div X^R nu=0 - [-s^4 d_s(r0/s^2) + s^2 d_x q + That/s] :",sp.simplify(dv[0]-f0))
print("div X^R nu=1 - [-s^4 d_s(q/s^2) + s^2 d_x r1] :",sp.simplify(dv[1]-f1)," ; nu=2,3 :",sp.simplify(dv[2]),sp.simplify(dv[3]))
# 2. compensation : div X^M = -1/4 d(I^2) F^2 = (beta/(2 e^2 s)) F^2_g delta_nu^0 ; That = -(beta/(2 e^2)) s^4 F^2_eta = -(beta/(2e^2)) F^2_g
beta,e=sp.symbols('beta e',positive=True); F2g=sp.Symbol('F2g')
I2=(1+2*beta*(sp.Symbol('lambda')-sp.log(s)))/e**2
src0=-sp.Rational(1,4)*sp.diff(I2,s)*F2g
That_=-(beta/(2*e**2))*F2g
print("div X^M_0 + That/s (identite + definition de That) :",sp.simplify(src0+That_/s))
print("   => X^R obeit au systeme homogene : d_s rho = d_x chi, d_s chi = d_x rho/3 + d_x(That/s^4)/3, rho=r0/s^2, chi=q/s^2 :")
rho=sp.Function('rho')(s,x); chi=sp.Function('chi')(s,x)
e0=sp.simplify((f0.subs({r0:s**2*rho,q:s**2*chi})-Th/s)/s**4); e1=sp.simplify(f1.subs({r0:s**2*rho,q:s**2*chi})/s**4)
print("   nu=0 / s^4 :",e0," ; nu=1 / s^4 :",e1)
print("   (systeme hyperbolique a coefficients constants, source lisse That/s^4 : solution lisse en s a donnees lisses, aucun ln)")
# 3. contre-exemple hors classe
f=sp.Function('f')(x)
Xp=sp.zeros(4,4); Xp[2,2]=s**2*sp.log(s)*f; Xp[3,3]=-s**2*sp.log(s)*f
print("\n3. X' = s^2 ln s diag(0,0,f,-f) : trace =",sp.simplify(sum(gi[i,i]*Xp[i,i] for i in range(n)))," ; divergence =",[sp.simplify(w) for w in div(Xp)])
Lh=kap/2*Xp; DL=cov(Lh)
for rho_,nu,la in ((2,0,2),(3,0,3),(1,0,1),(2,1,2)):
    w=sp.expand(((DL[(nu,la,rho_)]-DL[(la,nu,rho_)])/s).subs(sp.log(s),L))
    print(f"   R_{(rho_,nu,la)} = {sp.collect(w,L)}")
print("EXIT 0")
