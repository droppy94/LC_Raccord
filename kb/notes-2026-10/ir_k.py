"""ir_k.py -- NOTE-BORD-EON-118, sous le gel de NOTE-117.
A : identite de divergence du secteur Maxwell sur couche, absence de log au premier ordre (mode mixte non moyenne).
B : variation metrique de la partie (b) de Riegert, S_b = int sqrt(g) psi (Delta4 phi - F4/4), famille g = s^-2 diag(-1, 1+e h1, 1+e h2, 1+e h3)(s,x),
    phi = -ln s, psi(s,x) quelconque ; T_i = delta S_b / delta h_i (Euler-Lagrange) ; logs ; symetrie y-z ; puissances de s.
"""
import sympy as sp, time
from sympy.calculus.euler import euler_equations
t0=time.time()
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True)
k,e_,beta,u0,c,lam=sp.symbols('k e beta u0 c lambda',positive=True); L=sp.symbols('L'); t=sp.symbols('t',positive=True)
X=[s,x,y,z]; n=4
def christ(g):
    gi=g.inv()
    return [[[sp.expand(sum(gi[l,q]*(sp.diff(g[q,m],X[r])+sp.diff(g[q,r],X[m])-sp.diff(g[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)], gi
# ---------- A ----------
eta=sp.diag(-1,1,1,1); gh=eta/s**2; G,gi=christ(gh); G=[[[sp.simplify(v) for v in row] for row in M] for M in G]
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
I2=(1+2*beta*(lam-sp.log(s)))/e_**2
def green(src): return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
U1m=ser(green(ser(2/s*sp.diff(U0m,s),N+2)),N+2)
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(2*c*(s*sp.log(s)-s)+green(rest)-k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
F=sp.zeros(4,4); A_y=u*sp.cos(k*x); F[1,2]=sp.diff(A_y,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A_y,s); F[2,0]=-F[0,2]
F2g=sp.expand(sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n)))
XM=I2*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)
def D(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
DT=D(XM)
first=lambda v: sp.expand(v.subs(beta,0)+beta*sp.diff(v,beta).subs(beta,0))
tolog=lambda ex: sp.expand(sp.expand(sp.expand_log(sp.expand(ex),force=True)).subs(sp.log(s),L))
print("A. divergence de X^M + (1/4) d_nu(I^2) F^2 (premier ordre, ordre tronque) et log dans div X^M :")
for nu in range(n):
    dv=sp.expand(sum(gi[m,r]*DT[(r,m,nu)] for m in range(n) for r in range(n)))
    resid=first(ser(dv+sp.Rational(1,4)*sp.diff(I2,X[nu])*F2g,5))
    dvl=tolog(first(ser(dv,5)))
    print("   nu =",nu,": residu =",sp.simplify(tolog(resid))," ; coefficient de L dans div X^M =",sp.simplify(sp.diff(dvl,L)))
print("   (temps",round(time.time()-t0),"s)")
# ---------- B ----------
eps=sp.symbols('epsilon')
h=[sp.Function(f'h{i}')(s,x) for i in (1,2,3)]
psi=sp.Function('psi')(s,x)
g=sp.diag(-1,1+eps*h[0],1+eps*h[1],1+eps*h[2])/s**2
def tr1(ex):  # tronque au premier ordre en eps
    ex=sp.expand(ex); return sp.expand(ex.subs(eps,0)+eps*sp.diff(ex,eps).subs(eps,0))
gi=g.inv().applyfunc(lambda v: tr1(sp.series(v,eps,0,2).removeO()))
Gm=[[[tr1(sum(gi[l,q]*(sp.diff(g[q,m],X[r])+sp.diff(g[q,r],X[m])-sp.diff(g[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
print("B0. Christoffel (",round(time.time()-t0),"s)")
def Riem(a,b,c_,d):  # R^a_{bcd}
    return tr1(sp.diff(Gm[a][d][b],X[c_])-sp.diff(Gm[a][c_][b],X[d])+sum(Gm[a][c_][e]*Gm[e][d][b]-Gm[a][d][e]*Gm[e][c_][b] for e in range(n)))
Rup={}
for a in range(n):
    for b in range(n):
        for c_ in range(n):
            for d in range(c_+1,n):
                v=Riem(a,b,c_,d); Rup[(a,b,c_,d)]=v; Rup[(a,b,d,c_)]=-v
            Rup[(a,b,c_,c_)]=0
print("B1. Riemann (",round(time.time()-t0),"s)")
Ric=sp.Matrix(n,n,lambda b,d: tr1(sum(Rup[(a,b,a,d)] for a in range(n))))
Rs=tr1(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
# Riemann^2 : R_{abcd}R^{abcd} = R^a_{bcd} R^{b'}_{a'c'd'} g_{a a'} g^{b b'} g^{c c'} g^{d d'} ; metriques diagonales
gd=[g[i,i] for i in range(n)]; gid=[gi[i,i] for i in range(n)]
Riem2=tr1(sum(Rup[(a,b,c_,d)]**2*gd[a]*gid[b]*gid[c_]*gid[d] for a in range(n) for b in range(n) for c_ in range(n) for d in range(n) if Rup[(a,b,c_,d)]!=0))
Ric2=tr1(sum(Ric[a,b]**2*gid[a]*gid[b] for a in range(n) for b in range(n)))
sqrtg=tr1(sp.series(sp.sqrt(-g.det()),eps,0,2).removeO())
def box(f): return tr1(sum(sp.diff(tr1(sqrtg*gid[m]*sp.diff(f,X[m])),X[m]) for m in range(n))/sqrtg) if False else tr1(sp.series(sum(sp.diff(sqrtg*gid[m]*sp.diff(f,X[m]),X[m]) for m in range(n))/sqrtg,eps,0,2).removeO())
print("B2. courbures (",round(time.time()-t0),"s)")
phi=-sp.log(s)
def hess(f):
    return sp.Matrix(n,n,lambda a,b: tr1(sp.diff(f,X[a],X[b])-sum(Gm[l][a][b]*sp.diff(f,X[l]) for l in range(n))))
Hphi=hess(phi)
boxphi=box(phi)
F4=tr1(Riem2-4*Ric2+Rs**2-sp.Rational(2,3)*box(Rs))
D4phi=tr1(box(boxphi)+2*sum(gi[a,a]*gi[b,b]*Ric[a,b]*Hphi[a,b] for a in range(n) for b in range(n))+sp.Rational(1,3)*sum(gid[m]*sp.diff(Rs,X[m])*sp.diff(phi,X[m]) for m in range(n))-sp.Rational(2,3)*Rs*boxphi)
print("B3. Delta4 phi et F4 (",round(time.time()-t0),"s)")
bg=sp.simplify((D4phi-F4/4).subs(eps,0)); print("    fond : Delta4(-ln s) - F4/4 =",bg," ; F4 fond =",sp.simplify(F4.subs(eps,0)))
Lag=tr1(sqrtg*psi*(D4phi-F4/4))
L1=sp.expand(sp.diff(Lag,eps).subs(eps,0))
print("B4. densite au premier ordre construite (",round(time.time()-t0),"s), nombre de termes :",len(L1.args))
EL=euler_equations(L1,h,[s,x])
T=[sp.expand(eq.lhs) for eq in EL]
print("B5. Euler-Lagrange (",round(time.time()-t0),"s)")
for i,Ti in enumerate(T):
    print(f"   T_{i+1} contient log(s) : {Ti.has(sp.log)} ; nombre de termes : {len(sp.Add.make_args(Ti))}")
print("   T_2 - T_3 =",sp.simplify(T[1]-T[2]))
# puissances de s : psi lisse = a0(x) + s a1(x) + s^2 a2(x) + s^3 a3(x) + s^4 a4(x)
a=[sp.Function(f'a{j}')(x) for j in range(6)]
psis=sum(a[j]*s**j for j in range(6))
for i,lab in ((0,'T_1 (x)'),(1,'T_2 (y)')):
    v=sp.expand(T[i].subs(psi,psis).doit())
    pw=sorted(set(sp.Poly(sp.expand(v*s**8),s).monoms()))
    lead=min(p[0] for p in pw)-8
    print(f"B6. {lab} avec psi lisse : plus basse puissance de s = {lead} ; coefficient : {sp.factor(sp.expand(v*s**(-lead)).subs(s,0))}")
d12=sp.expand((T[0]-T[1]).subs(psi,psis).doit())
pw=sorted(set(sp.Poly(sp.expand(d12*s**8),s).monoms())); lead=min(p[0] for p in pw)-8
print(f"B7. anisotropie T_1 - T_2 : plus basse puissance de s = {lead} ; coefficient : {sp.factor(sp.expand(d12*s**(-lead)).subs(s,0))}")
print("\nEXIT 0 (",round(time.time()-t0),"s)")
