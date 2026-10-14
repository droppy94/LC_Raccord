"""indep_K.py -- audit M-b, bloc K-B, controles independants.
(a) Identite de covariance de Weyl (derivee) : pour g = e^{2 sigma} gbar, sqrt(g) Delta4 = sqrt(gbar) Delta4bar et sqrt(g) F4 = sqrt(gbar)(F4bar + 4 Delta4bar sigma).
    Avec g = s^-2 (eta + eps H), sigma = -ln s = phi : sqrt(g)(Delta4 phi - F4/4) = -1/4 sqrt(gbar) F4bar  (phi disparait identiquement).
    Au premier ordre : = (1/6) box_eta R1[H], R1[H] = d_m d_n H^{mn} - box_eta tr H.
(b) Verification brute de (a), point par point, pour une famille NON diagonale dependant de (s, x, y) :
    H_sx = p(s,x,y), H_xy = h(s,x,y), H_zz = q(s,x,y).
(c) Formules T_1, T_2 du bloc K redonnees par (a) pour la famille diagonale (s,x).
"""
import sympy as sp, time
t0=time.time()
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True); eps=sp.Symbol('epsilon')
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1)
p=sp.Function('p')(s,x,y); h=sp.Function('h')(s,x,y); q=sp.Function('q')(s,x,y)
H=sp.zeros(4,4); H[0,1]=H[1,0]=p; H[1,2]=H[2,1]=h; H[3,3]=q
def tr1(ex):
    ex=sp.expand(ex); return sp.expand(ex.subs(eps,0)+eps*sp.diff(ex,eps).subs(eps,0))
g=(eta+eps*H)/s**2
gi=(s**2*(eta-eps*eta*H*eta)).applyfunc(tr1)          # inverse au premier ordre
assert (g*gi).applyfunc(tr1)==sp.eye(4)
sqrtg=tr1(s**-4*(1+eps*sum(eta[i,i]*H[i,i] for i in range(n))/2))
dg=[[[sp.diff(g[a,b],X[c]) for c in range(n)] for b in range(n)] for a in range(n)]
Gm=[[[tr1(sum(gi[l,m]*(dg[m][a][b]+dg[m][b][a]-dg[a][b][m]) for m in range(n))/2) for b in range(n)] for a in range(n)] for l in range(n)]
print("Christoffel",round(time.time()-t0),"s")
# Gm[l][a][b] = Gamma^l_{ab}  (dg[m][a][b] = d_b g_{ma})
Rup={}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(c+1,n):
                v=tr1(sp.diff(Gm[a][d][b],X[c])-sp.diff(Gm[a][c][b],X[d])+sum(Gm[a][c][e]*Gm[e][d][b]-Gm[a][d][e]*Gm[e][c][b] for e in range(n)))
                Rup[(a,b,c,d)]=v; Rup[(a,b,d,c)]=-v
            Rup[(a,b,c,c)]=0
print("Riemann",round(time.time()-t0),"s")
Ric=sp.Matrix(n,n,lambda b,d: tr1(sum(Rup[(a,b,a,d)] for a in range(n))))
Rs=tr1(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
# Riem^2 = R^a_{bcd} R^e_{fgh} g_{ae} g^{bf} g^{cg} g^{dh}
Rlow={(a,b,c,d): tr1(sum(g[a,e]*Rup[(e,b,c,d)] for e in range(n))) for a in range(n) for b in range(n) for c in range(n) for d in range(n)}
def raise3(a,b,c,d):
    return sum(gi[b,f]*gi[c,gg]*gi[d,hh]*Rup[(a,f,gg,hh)] for f in range(n) for gg in range(n) for hh in range(n) if gi[b,f]!=0 and gi[c,gg]!=0 and gi[d,hh]!=0)
Riem2=tr1(sum(Rlow[(a,b,c,d)]*raise3(a,b,c,d) for a in range(n) for b in range(n) for c in range(n) for d in range(n) if Rlow[(a,b,c,d)]!=0))
Ricup=(gi*Ric*gi).applyfunc(tr1)
Ric2=tr1(sum(Ric[a,b]*Ricup[a,b] for a in range(n) for b in range(n)))
print("invariants",round(time.time()-t0),"s ; R fond =",sp.simplify(Rs.subs(eps,0))," ; Riem2 fond =",sp.simplify(Riem2.subs(eps,0)))
def box(f): return tr1(sum(sp.diff(tr1(sqrtg*gi[m,nn]*sp.diff(f,X[nn])),X[m]) for m in range(n) for nn in range(n))*s**4*(1-eps*sum(eta[i,i]*H[i,i] for i in range(n))/2))
phi=-sp.log(s)
Hess=sp.Matrix(n,n,lambda a,b: tr1(sp.diff(phi,X[a],X[b])-sum(Gm[l][a][b]*sp.diff(phi,X[l]) for l in range(n))))
bphi=box(phi)
D4=tr1(box(bphi)+2*sum(Ricup[a,b]*Hess[a,b] for a in range(n) for b in range(n))-sp.Rational(2,3)*Rs*bphi
       +sp.Rational(1,3)*sum(gi[a,b]*sp.diff(Rs,X[a])*sp.diff(phi,X[b]) for a in range(n) for b in range(n)))
F4=tr1(Riem2-4*Ric2+Rs**2-sp.Rational(2,3)*box(Rs))
print("Delta4, F4",round(time.time()-t0),"s ; F4 fond =",sp.simplify(F4.subs(eps,0)))
dens=tr1(sqrtg*(D4-F4/4))
d0=sp.simplify(dens.subs(eps,0)); d1=sp.expand(sp.diff(dens,eps))
print("densite sqrt(g)(Delta4 phi - F4/4) : ordre 0 =",d0," ; ordre 1 contient log(s) :",d1.has(sp.log))
# prediction (a)
Hup=eta*H*eta; trH=sum(eta[i,i]*H[i,i] for i in range(n))
boxe=lambda f: sum(eta[m,m]*sp.diff(f,X[m],2) for m in range(n))
R1=sum(sp.diff(Hup[m,nn],X[m],X[nn]) for m in range(n) for nn in range(n))-boxe(trH)
pred=sp.Rational(1,6)*boxe(R1)
print("ecart densite ordre 1 - (1/6) box_eta R1[H] :",sp.simplify(d1-sp.expand(pred)))
print("   (temps",round(time.time()-t0),"s)")
# (c) famille diagonale (s,x) : S1 = (1/6) int psi box R1 ; T_i = delta S1/delta h_i
from sympy.calculus.euler import euler_equations
h1,h2,h3=[sp.Function(f'h{i}')(s,x) for i in (1,2,3)]; psi=sp.Function('psi')(s,x)
Hd=sp.diag(0,h1,h2,h3); trd=h1+h2+h3
bx=lambda f: -sp.diff(f,s,2)+sp.diff(f,x,2)
R1d=sp.diff(h1,x,2)-bx(trd)
EL=euler_equations(sp.Rational(1,6)*psi*bx(R1d),[h1,h2,h3],[s,x])
T=[sp.expand(e.lhs) for e in EL]
T1c=-sp.diff(psi,s,4)/6+sp.diff(psi,s,2,x,2)/6
T2c=-sp.diff(psi,s,4)/6-sp.diff(psi,x,4)/6+sp.diff(psi,s,2,x,2)/3
print("(c) T_1 - formule du bloc K :",sp.simplify(T[0]-T1c)," ; T_2 - formule :",sp.simplify(T[1]-T2c)," ; T_3 - T_2 :",sp.simplify(T[2]-T[1]))
print("EXIT 0")
