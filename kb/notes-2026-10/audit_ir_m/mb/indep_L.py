"""indep_L.py -- audit M-b, bloc L, controles independants (numpy, quadrature numerique sur la sphere, pas de moments exacts).
1. L-A/L-B : Q_k = Re(B B^dag - E E^dag) en 3D pour J+, J- complexes aleatoires et k quelconque, contre la formule ;
   Green retardee pour une source differente de celle du script.
2. L-D : <L> pour les sources du script.
3. Contre-exemples : dipoles p // m, |p| = |m|, phase relative quelconque ; loi generale des dipoles <L> = (2/5)[tf Re pp^dag - tf Re mm^dag].
4. Interference : facteur de suppression pour une enveloppe lisse et pour une source a composante statique.
"""
import numpy as np
rng=np.random.default_rng(2026)
def cvec(n=3): return rng.normal(size=n)+1j*rng.normal(size=n)
def L3(v,nv):
    P=np.eye(3)-np.outer(nv,nv); M=np.real(np.outer(v,v.conj())); return M-P*np.trace(M)/2
# 1. identite
worst=0
for trial in range(200):
    kh=rng.normal(size=3); kh/=np.linalg.norm(kh); k=abs(rng.normal())+0.1
    P=np.eye(3)-np.outer(kh,kh)
    Jp=P@cvec(); Jm=P@cvec()
    a=1j*(Jp-Jm)/(2*k); b=-(Jp+Jm)/2          # A(0) et E = -dA/dt
    B=1j*k*np.cross(kh,a)
    Q=np.real(np.outer(B,B.conj())-np.outer(b,b.conj()))
    pred=-0.5*(L3(Jp,kh)+L3(Jm,kh))-0.5*np.real(Jp@Jm.conj())*P
    worst=max(worst,np.abs(Q-pred).max())
print("1. L-A en 3D, 200 tirages : max |Q_k - formule| =",worst)
# Green retardee : source J(t) = t^2 exp(-(t+5)^2) (differente du script), k = 0.9
from numpy.polynomial.legendre import leggauss
tg,wg=leggauss(400); T=-5+6*tg; W=6*wg          # t dans [-11, 1] -> on coupe a t <= 0
mask=T<=0; T=T[mask]; W=W[mask]
J=T**2*np.exp(-(T+5)**2); k=0.9
aG=np.sum(W*np.sin(k*(0-T))/k*J); dAG=np.sum(W*np.cos(k*(0-T))*J)
Jp=np.sum(W*np.exp(1j*k*T)*J); Jm=np.sum(W*np.exp(-1j*k*T)*J)
print("   Green : a =",aG," formule :",(1j*(Jp-Jm)/(2*k)).real," ; -dA/dt =",-dAG," formule :",(-(Jp+Jm)/2).real)
# 2. moyennes angulaires numeriques
xg,wq=leggauss(48); phs=np.linspace(0,2*np.pi,96,endpoint=False)
dirs=[];wts=[]
for c,wc in zip(xg,wq):
    sn=np.sqrt(1-c*c)
    for p in phs: dirs.append(np.array([sn*np.cos(p),sn*np.sin(p),c])); wts.append(wc/2/len(phs))
def avgL(Jfun):
    return sum(w*L3(Jfun(nv),nv) for nv,w in zip(dirs,wts))
P_=lambda nv: np.eye(3)-np.outer(nv,nv)
tf=lambda M: M-np.eye(3)*np.trace(M)/3
m=rng.normal(size=3); p=rng.normal(size=3)
Lm=avgL(lambda nv: np.cross(nv,m)); Lp=avgL(lambda nv: P_(nv)@p)
print("\n2. dipole magnetique lineaire : |<L> + (2/5) tf(mm)| =",np.abs(Lm+0.4*tf(np.outer(m,m))).max())
print("   dipole electrique lineaire : |<L> - (2/5) tf(pp)| =",np.abs(Lp-0.4*tf(np.outer(p,p))).max())
ex,ey,ez=np.eye(3)
print("   magnetique tournant x - i y : <L> =",np.round(avgL(lambda nv: np.cross(nv,ex-1j*ey)),12).diagonal()," (attendu -2/15,-2/15,4/15)")
Jch=lambda nv: P_(nv)@ez-np.cross(nv,-1j*ez)
print("   chiral (p = z, m = -i z) : max_n |L(n)| =",max(np.abs(L3(Jch(nv),nv)).max() for nv in dirs[::37]))
A=np.array([[1,2,0],[2,-3,1],[0,1,2.]])
def LE(nv): Pn=P_(nv); M=Pn@A@Pn; return M-Pn*np.trace(M)/2
def LB(nv): Rn=np.array([[0,-nv[2],nv[1]],[nv[2],0,-nv[0]],[-nv[1],nv[0],0]]); M=Rn@LE(nv); return (M+M.T)/2
print("   E pur l=2 : |<L_E> - (2/5)A| =",np.abs(sum(w*LE(nv) for nv,w in zip(dirs,wts))-0.4*A).max()," ; B pur l=2 : |<L_B>| =",np.abs(sum(w*LB(nv) for nv,w in zip(dirs,wts))).max())
# isotrope : moyenne de -(2/5) tf(mm) sur m uniforme -> 0 (trivial) ; controle numerique
iso=sum(w*(-0.4)*tf(np.outer(nv,nv)) for nv,w in zip(dirs,wts)); print("   ensemble isotrope : |<L>| =",np.abs(iso).max())
# 3. contre-exemples
print("\n3. dipoles p // m, |p| = |m| = 1 (axe z), phase relative phi :")
for phi in (0,np.pi/4,np.pi/2,np.pi):
    Jf=lambda nv,phi=phi: P_(nv)@ez-np.cross(nv,np.exp(1j*phi)*ez)
    La=avgL(Jf); loc=max(np.abs(L3(Jf(nv),nv)).max() for nv in dirs[::37])
    print(f"   phi = {phi:.4f} : |<L>| = {np.abs(La).max():.2e} ; max_n |L(n)| (polarisation lineaire locale) = {loc:.3f}")
print("   loi generale des dipoles (p, m complexes aleatoires) :")
for trial in range(3):
    p=cvec(); m=cvec()
    La=avgL(lambda nv: P_(nv)@p-np.cross(nv,m))
    pred=0.4*(tf(np.real(np.outer(p,p.conj())))-tf(np.real(np.outer(m,m.conj()))))
    print("     |<L> - (2/5)[tf Re pp^dag - tf Re mm^dag]| =",np.abs(La-pred).max())
# famille hors des trois classes : p reel, m = R p avec R rotation et |m| = |p| ? -> tf(pp) = tf(mm) exige m = +- p (vecteurs reels)
p=np.array([1.,0,0]); m=np.array([0,1.,0])
print("   p = x, m = y (source de Huygens) : <L> diag =",np.round(avgL(lambda nv: P_(nv)@p-np.cross(nv,m)).diagonal(),12))
# p complexe, m complexe distincts avec tf Re pp^dag = tf Re mm^dag : p = x + i y, m = x - i y (meme Re pp^dag), pas parallele
p=ex+1j*ey; m=ex-1j*ey
La=avgL(lambda nv: P_(nv)@p-np.cross(nv,m)); loc=max(np.abs(L3(P_(nv)@p-np.cross(nv,m),nv)).max() for nv in dirs[::37])
print("   p = x + i y (tournant electrique), m = x - i y (tournant magnetique oppose) : |<L>| =",f"{np.abs(La).max():.2e}"," ; max_n |L(n)| =",round(loc,3))
# 4. interference (transformees analytiques ; poids k^4 = d^3k x |k x m|^2 d'un dipole magnetique)
print("\n4. rapport interference/intensite  R = int k^4 Re(J+.J-^*) dk / int k^4 |J+|^2 dk  (J reel : J- = conj(J+)) :")
import mpmath as mp
def R(Jp):
    num=mp.quad(lambda k: k**4*mp.re(Jp(k)**2),[0,1,2,3,4,6,10,20,mp.inf]); den=mp.quad(lambda k: k**4*abs(Jp(k))**2,[0,1,2,3,4,6,10,20,mp.inf]); return num/den
for sig,t0 in ((2,-10),(2,-20),(5,-10),(10,-10)):
    w0=3
    Jp=lambda k,sig=sig,t0=t0: mp.sqrt(mp.pi)*sig/2*(mp.exp(1j*(k+w0)*t0-(k+w0)**2*sig**2/4)+mp.exp(1j*(k-w0)*t0-(k-w0)**2*sig**2/4))
    print(f"   enveloppe gaussienne sigma = {sig}, t0 = {t0}, w0 = 3 : R = {mp.nstr(R(Jp),3)}  (estimation exp(-2 t0^2/sigma^2) = {mp.nstr(mp.exp(-2*t0**2/sig**2),3)})")
for t0 in (-2,-5,-10):
    w=mp.mpf(1)/2
    Jp=lambda k,t0=t0: mp.exp(1j*k*t0)*1j*mp.pi*w/(2*mp.sinh(mp.pi*k*w/2))   # TF de (1 - tanh((t - t0)/w))/2 (hors delta en k = 0)
    print(f"   aimant eteint (marche tanh, w = 1/2, allume depuis -inf), t0 = {t0} : R = {mp.nstr(R(Jp),3)}")
print("EXIT 0")
