"""ir_i.py -- NOTE-BORD-EON-111, sous le gel de NOTE-110.
A : loi locale. Mode mixte non moyenne, fermeture locale isotrope X^R = diag(r0,r1,r1,r1)(s,x) + q (s,x), trace locale, conservation ;
    coefficient de ln s a s^0 dans toutes les composantes de R, contre (3 beta kappa/e^2) Q_tf(x) local ; role des coefficients libres.
B : dipole magnetique eteint : champs exacts a t = 0 (A = rot(m(t-r)/r)), controle de Maxwell, carte de Q_tf, integrales par region.
"""
import sympy as sp, mpmath as mp
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True)
k,e,beta,kap,u0,c,lam=sp.symbols('k e beta kappa u0 c lambda',positive=True); L=sp.symbols('L'); t=sp.symbols('t',positive=True)
W=sp.symbols('W',positive=True)
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv()
G=[[[sp.simplify(sum(gi[l,q]*(sp.diff(gh[q,m],X[r])+sp.diff(gh[q,r],X[m])-sp.diff(gh[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
N=6
def ser(ex,o=N): return sp.expand(sp.series(ex,s,0,o).removeO())
def tolog(ex): return sp.expand(sp.expand(sp.expand_log(sp.expand(ex),force=True)).subs(sp.log(s),L))
def toW(ex):  # x -> W = exp(i k x)
    ex=sp.expand(sp.expand(ex).rewrite(sp.exp)); ex=ex.subs(x,sp.log(W)/(sp.I*k)); return sp.expand(sp.powsimp(sp.expand(ex)))
I2=(1+2*beta*(lam-sp.log(s)))/e**2
def green(src): return sp.integrate(sp.sin(k*(s-t))/k*src.subs(s,t),(t,0,s))
U0m=u0*sp.cos(k*s); U0e=c/k*sp.sin(k*s)
U1m=ser(green(ser(2/s*sp.diff(U0m,s),N+2)),N+2)
rest=ser(2*c*(sp.cos(k*s)-1)/s,N+2)
U1e=ser(2*c*(s*sp.log(s)-s)+green(rest)-k**2*sp.integrate(sp.sin(k*(s-t))/k*(2*c*(t*sp.log(t)-t)),(t,0,s)),N+2)
u=U0m+U0e+beta*(U1m+U1e)
F=sp.zeros(4,4); A_y=u*sp.cos(k*x); F[1,2]=sp.diff(A_y,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A_y,s); F[2,0]=-F[0,2]
F2g=sum(gi[i,a]*gi[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
first=lambda v: sp.expand(v.subs(beta,0)+beta*sp.diff(v,beta).subs(beta,0))
XM=(I2*(F*gi*F.T-sp.Rational(1,4)*gh*F2g)).applyfunc(lambda v: first(ser(v,6)))
F2eta=sum(eta[i,a]*eta[j,b]*F[i,j]*F[a,b] for i in range(n) for j in range(n) for a in range(n) for b in range(n))
That=first(ser(-(beta/(2*e**2))*F2eta*s**4,8)); That=sp.expand(beta*sp.diff(That,beta).subs(beta,0))
# ansatz X^R
P=5
harm=lambda name: [sp.Symbol(f'{name}_{h}') for h in ('0','c','s')]
coef={}
def field(name):
    ex=0
    for j in range(0,P+1):
        for l in range(0,3):
            a0,ac,as_=harm(f'{name}{j}{l}'); coef.update({str(v):v for v in (a0,ac,as_)})
            ex+=s**j*sp.log(s)**l*(a0+ac*sp.cos(2*k*x)+as_*sp.sin(2*k*x))
    return ex
r0=field('r'); qf=field('q')
r1=(r0+That/s**2)/3
XR=sp.diag(r0,r1,r1,r1); XR[0,1]=qf; XR[1,0]=qf
def D(T): return {(r,m,q): sp.diff(T[m,q],X[r])-sum(G[p][r][m]*T[p,q]+G[p][r][q]*T[m,p] for p in range(n)) for r in range(n) for m in range(n) for q in range(n)}
def div(T):
    DT=D(T); return [sp.expand(sum(gi[m,r]*DT[(r,m,nu)] for m in range(n) for r in range(n))) for nu in range(n)]
tot=XM+XR
dv=div(tot)
eqs=[]
pmax=3   # ordres controles : s^p, p <= pmax, pour div (X ~ s^2, div ~ s^3 apres multiplication)
for nu in (0,1):
    ex=toW(tolog(sp.expand(dv[nu])))
    ex=sp.expand(ex)
    for p in range(-1,pmax+1):
        cp=sp.expand(ex.coeff(s,p)) if p!=0 else sp.expand(ex.subs(s,0)) if False else sp.expand(ex.coeff(s,p))
        for lpow in range(0,4):
            cl=sp.expand(cp.coeff(L,lpow))
            for wp in range(-4,5):
                cw=sp.expand(cl.coeff(W,wp))
                if cw!=0: eqs.append(cw)
unk=list(coef.values())
print("A0. equations de conservation (ordres s^p, p <=",pmax,") :",len(eqs)," ; inconnues :",len(unk))
sol=sp.solve(eqs,unk,dict=True)
assert sol, "fermeture locale : systeme sans solution aux ordres controles"
sol=sol[0]
free=[v for v in unk if v not in sol]
# ---- ajouts audit ----
print("libres:", sorted(map(str,free)))
for key in ['r20','r21','r22','r30','r31','r32','q10','q11','q12','q20','q21','q22','q30','q31']:
    for h in ('0','c','s'):
        nm=f'{key}_{h}'; v=coef[nm]
        print(nm, '->', sol.get(v,'LIBRE'))
# verification : les sources du secteur nu=0 se compensent-elles ? (That/s + div XM_0)
dvM=div(XM)
chk=sp.expand(dvM[0] + That/s)   # partie XR : -s^4 d_s(r0/s^2)+s^2 d_x q + That/s
print("div XM_0 + That/s, ordre s^3 (premier ordre beta) :", sp.simplify(sp.expand(ser(chk,4)).coeff(s,3)))
