"""ctrl_etat.py -- controle independant (NOTE-106) de la reserve d'etat de D-b : mode mixte u = u0 cos ks + (c/k) sin ks + beta U1,
coefficient de beta ln s dans <X^M> a l'ordre dominant en s, et trace anomale <F^2>_eta."""
import sympy as sp
s=sp.symbols('s',positive=True); x=sp.symbols('x',real=True); k,e,beta,u0,c,lam=sp.symbols('k e beta u0 c lambda',positive=True); L=sp.symbols('L')
eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv(); n=4
I2=(1+2*beta*(lam-sp.log(s)))/e**2
# corrections d'ordre beta (Green, a0=a1=0), resolues ici independamment par variation des constantes
t=sp.symbols('t',positive=True)
def U1(src):  # U1''+k^2 U1 = src, solution particuliere nulle en 0 au sens de Green
    return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
srcm=ser(2/s*sp.diff(U0m,s),N+2); U1m=ser(U1(srcm),N+2)
# branche electrique : source 2c cos(ks)/s ; on prend la serie de cos et integre terme a terme avec la partie singuliere 2c/s
U1e_sing=2*c*(s*sp.log(s)-s)  # solution de U''=2c/s (ordre dominant), corrections k^2 incluses ci-dessous par serie
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(U1e_sing + U1(rest) - k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
res=sp.expand(sp.series(sp.expand((sp.diff(I2*sp.diff(u,s),s)+k**2*I2*u)*e**2),s,0,3).removeO())
res1=sp.expand(sp.diff(res,beta).subs(beta,0).subs(sp.log(s),L))
print("residu O(beta) jusqu'a s^2 :", sp.simplify(res1))
A=u*sp.cos(k*x); F=sp.zeros(4,4); F[1,2]=sp.diff(A,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A,s); F[2,0]=-F[0,2]
F2g=sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
XM=I2*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)
avg=lambda v: sp.integrate(sp.expand(v),(x,0,2*sp.pi/k))*k/(2*sp.pi)
out=[]
for i in range(4):
    v=ser(avg(XM[i,i]),4); v=sp.expand(sp.expand_log(v,force=True).subs(sp.log(s),L))
    v1=sp.expand(sp.diff(v,beta).subs(beta,0)); cL=sp.expand(sp.diff(v1,L)); lead=sp.limit(cL/s**2,s,0)
    out.append(sp.factor(lead))
print("coef de beta ln s dans <X^M>_ii / s^2 (s->0), i=s,x,y,z :", out)
F2eta=sum(eta[i,a]*eta[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
print("<F^2>_eta a l'ordre 0, s->0 :", sp.factor(sp.limit(avg(F2eta).subs(beta,0),s,0)))
print("EXIT 0")
