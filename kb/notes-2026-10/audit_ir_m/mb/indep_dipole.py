"""indep_dipole.py -- audit M-b, bloc I-B, controle independant.
Champs du dipole magnetique m(t) z (Gauss, c = 1), formules standard :
 B = (3n n.z - z)(m/r^3 + mdot/r^2) + (n n.z - z) mddot/r ,  E = -(n x z)(mdot/r^2 + mddot/r) , m evalue en u = t - r.
m(u) = (1 - tanh((u + D)/w))/2, D = 10, w = 1/2, t = 0.
Moyennes angulaires par quadrature numerique (Gauss-Legendre x trapezes), sans formule de moments.
"""
import numpy as np, mpmath as mp
mp.mp.dps=25
D=mp.mpf(10); w=mp.mpf(1)/2
f=lambda u: (1-mp.tanh((u+D)/w))/2
fd=lambda u: mp.diff(f,u,1); fdd=lambda u: mp.diff(f,u,2)
# moyennes angulaires numeriques des structures
xg,wg=np.polynomial.legendre.leggauss(40); ph=np.linspace(0,2*np.pi,64,endpoint=False)
def avg(fun):
    acc=np.zeros((3,3))
    for c,wc in zip(xg,wg):
        sn=np.sqrt(1-c*c)
        for p in ph:
            nv=np.array([sn*np.cos(p),sn*np.sin(p),c]); acc+=fun(nv)*wc/2/len(ph)
    return acc
ez=np.array([0,0,1.])
Sa=lambda nv: 3*nv*nv[2]-ez; Sg=lambda nv: nv*nv[2]-ez; Se=lambda nv: np.cross(nv,ez)
tf=lambda M: M-np.eye(3)*np.trace(M)/3
P0zz=2/3
cA=tf(avg(lambda nv: np.outer(Sa(nv),Sa(nv))))[2,2]/P0zz
cG=tf(avg(lambda nv: np.outer(Sg(nv),Sg(nv))))[2,2]/P0zz
cAG=tf(avg(lambda nv: np.outer(Sa(nv),Sg(nv))+np.outer(Sg(nv),Sa(nv))))[2,2]/P0zz
cE=tf(avg(lambda nv: np.outer(Se(nv),Se(nv))))[2,2]/P0zz
MS=tf(avg(lambda nv: np.outer(Sa(nv),Sa(nv))))
print("moyennes numeriques (unites de diag(-1/3,-1/3,2/3)) : SaSa =",round(cA,12),", SgSg =",round(cG,12),", SaSg+SgSa =",round(cAG,12),", SeSe =",round(cE,12))
print("   forme de <SaSa>_tf (doit etre prop. a diag(-1/3,-1/3,2/3)) :",np.round(MS,12).tolist())
print("   statique : 1/5 ?",abs(cA-0.2)<1e-12," ; rayonne SgSg - SeSe = 4/5 ?",abs(cG-cE-0.8)<1e-12)
def coefs(r):
    u=-r; m=f(u); md=fd(u); mdd=fdd(u)
    al=m/r**3+md/r**2; ga=mdd/r; ep=md/r**2+mdd/r
    return al,ga,ep
def q(r,mode='full'):
    al,ga,ep=coefs(r)
    if mode=='rad': al=0; ep=ga   # partie rayonnee seule : B = (n n.z - z) mddot/r, E = (n x z) mddot/r
    return cA*al**2+cG*ga**2+cAG*al*ga-cE*ep**2
for r in (3,10,20):
    al,ga,ep=coefs(mp.mpf(r))
    print(f"r = {r} : alpha = {mp.nstr(al,4)}, gamma = {mp.nstr(ga,4)}, epsilon = {mp.nstr(ep,4)}")
I=lambda a,b,mode='full': mp.quad(lambda r: 4*mp.pi*r**2*q(r,mode),[a,(a+b)/2,b] if b!=mp.inf else [a,b])
Iin=I(mp.mpf('0.05'),D-3*w); Ish=I(D-3*w,D+3*w); Iout=I(D+3*w,mp.inf)
print("integrales radiales : boule",mp.nstr(Iin,6)," ; coquille",mp.nstr(Ish,6)," ; reliquat",mp.nstr(Iout,6))
print("   reliquat statique pur (1/5) 4 pi/(3 r^3), r = 13 :",mp.nstr(mp.mpf(1)/5*4*mp.pi/(3*13**3),6))
Ishr=I(D-3*w,D+3*w,'rad')
print("   coquille, partie rayonnee seule :",mp.nstr(Ishr,6)," ; prediction (4/5) 4 pi int mddot^2 du :",mp.nstr(mp.mpf(4)/5*4*mp.pi*mp.quad(lambda u: fdd(u)**2,[-mp.inf,-D,mp.inf]),6))
# decomposition de l'ecart : termes d'induction
def q_parts(r):
    u=-r; m=f(u); md=fd(u); mdd=fdd(u)
    al=m/r**3+md/r**2; ga=mdd/r; ep=md/r**2+mdd/r
    stat=cA*al**2
    cross=cAG*al*ga
    Eind=-cE*(ep**2-(mdd/r)**2)
    return stat,cross,Eind
for idx,lab in enumerate(("alpha^2 (statique+induction)","alpha*gamma","E : (eps^2 - (mddot/r)^2)")):
    print(f"   contribution coquille {lab} :",mp.nstr(mp.quad(lambda r: 4*mp.pi*r**2*q_parts(r)[idx],[D-3*w,D,D+3*w]),6))
print("EXIT 0")
