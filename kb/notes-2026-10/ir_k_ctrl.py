"""ir_k_ctrl.py -- NOTE-118, partie C : le ln de R a s^0 ne depend que de la partie logarithmique de T.
R calcule avec T = X^M seul (mode mixte non moyenne, aucun secteur non Maxwell) : coefficient de ln s a s^0 contre (3 beta kappa/e^2) Q_tf(x) local."""
import sympy as sp
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True)
k,e_,beta,kap,u0,c,lam=sp.symbols('k e beta kappa u0 c lambda',positive=True); L=sp.symbols('L'); t=sp.symbols('t',positive=True)
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv()
G=[[[sp.simplify(sum(gi[l,q]*(sp.diff(gh[q,m],X[r])+sp.diff(gh[q,r],X[m])-sp.diff(gh[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
tolog=lambda ex: sp.expand(sp.expand(sp.expand_log(sp.expand(ex),force=True)).subs(sp.log(s),L))
first=lambda v: sp.expand(v.subs(beta,0)+beta*sp.diff(v,beta).subs(beta,0))
I2=(1+2*beta*(lam-sp.log(s)))/e_**2
def green(src): return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
U1m=ser(green(ser(2/s*sp.diff(U0m,s),N+2)),N+2)
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(2*c*(s*sp.log(s)-s)+green(rest)-k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
F=sp.zeros(4,4); A_y=u*sp.cos(k*x); F[1,2]=sp.diff(A_y,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A_y,s); F[2,0]=-F[0,2]
F2g=sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
XM=(I2*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)).applyfunc(lambda v: first(ser(v,5)))
tr=lambda T: sp.expand(sum(gi[i,j]*T[i,j] for i in range(n) for j in range(n)))
def D(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
Lh=kap/2*(XM-sp.Rational(1,3)*tr(XM)*gh); DL=D(Lh)
B2=(k*u0*sp.sin(k*x))**2; E2=(c*sp.cos(k*x))**2; Q=sp.diag(0,-E2,B2); Qtf=Q-sp.eye(3)*Q.trace()/3
ok=True
for rho in range(n):
    for nu in range(n):
        for la in range(nu+1,n):
            v=tolog(ser(sp.expand((DL[(nu,la,rho)]-DL[(la,nu,rho)])/s),1)); v=sp.expand(sp.diff(v,beta).subs(beta,0))
            cl=sp.expand(sp.diff(v,L).subs(s,0))
            ref=sp.expand(3*kap/e_**2*Qtf[rho-1,rho-1]) if (nu==0 and rho==la and rho>=1) else 0
            d=sp.simplify(sp.trigsimp(cl-ref))
            if cl!=0 or ref!=0: print("  ",(rho,nu,la),": coef ln s a s^0 (X^M seul) =",sp.factor(sp.trigsimp(cl))," ; ecart a la loi :",d)
            ok=ok and d==0
print("loi R_ln = (3 beta kappa/e^2) Q_tf(x) retrouvee avec X^M seul, sans secteur non Maxwell :",ok)
print("EXIT 0")
