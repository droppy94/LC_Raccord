"""jb_g34.py -- controles independants de G3, G4 et du faisceau non polarise equilibre."""
import sympy as sp
from jb_indep import analyse
# ---- G3 : evolution libre depuis u(-D)=a, u'(-D)=0, puis moyenne spatiale du mode A_y = u cos kx
k,D,a,ks,x=sp.symbols('k D a k_star x',positive=True); tau,X=sp.symbols('tau X',real=True)
u=a*sp.cos(k*(tau+D))
assert sp.simplify(sp.diff(u,tau,2)+k**2*u)==0 and u.subs(tau,-D)==a and sp.diff(u,tau).subs(tau,-D)==0
By=0; Bz=sp.diff(u*sp.cos(k*X),X); Ey=-sp.diff(u*sp.cos(k*X),tau)
avg=lambda f: sp.simplify(sp.integrate(f.subs(tau,0),(X,0,2*sp.pi/k))*k/(2*sp.pi))
QB=avg(Bz**2); QE=avg(Ey**2)
print("G3 amplitudes a tau=0 : |B| =",sp.simplify(sp.diff(u,tau,0).subs(tau,0)*k)," |E| =",sp.simplify(-sp.diff(u,tau).subs(tau,0)))
print("G3 Q moyen (spatial) : Q_zz = <B^2> =",sp.trigsimp(QB)," ; Q_yy = -<E^2> =",sp.trigsimp(-QE))
print("   decomposition : (QB+QE)/2 =",sp.simplify(sp.trigsimp((QB+QE)/2))," ; (QB-QE)/2 =",sp.simplify(sp.trigsimp((QB-QE)/2)))
# partie sans trace : Q = S (eBeB - eEeE) + C (eBeB + eEeE), eBeB+eEeE = 1 - kk
eB=sp.Matrix([0,0,1]); eE=sp.Matrix([0,1,0]); kh=sp.Matrix([1,0,0]); Sm,Cm=sp.symbols('S C')
Qm=Sm*(eB*eB.T-eE*eE.T)+Cm*(eB*eB.T+eE*eE.T); Qtf=Qm-sp.eye(3)*Qm.trace()/3
print("   Qtf =",Qtf.tolist()," ; part du terme cos 2kD dans Qtf = C (1/3 - k k) :",sp.simplify(Qtf-Sm*(eB*eB.T-eE*eE.T)-Cm*(sp.eye(3)/3-kh*kh.T))==sp.zeros(3,3))
# moyenne spectrale : forme fermee Re (1 - i x)^{-(n+1)}
for n in (0,1,2,3,4,5):
    r=sp.integrate(k**n*sp.exp(-k/ks)*sp.cos(2*k*D),(k,0,sp.oo))/sp.integrate(k**n*sp.exp(-k/ks),(k,0,sp.oo))
    r=sp.simplify(r.subs(D,x/(2*ks)))
    cf=sp.simplify(sp.re(sp.expand_complex((1-sp.I*x)**(-(n+1)))))
    lead=sp.limit(r*x**(n+2 if (n%2==0) else n+1),x,sp.oo)
    print(f"   n={n}: <cos2kD> = {sp.factor(r)} ; = Re(1-ix)^-(n+1) : {sp.simplify(r-cf)==0} ; equivalent grand x : {lead} x^-{n+2 if n%2==0 else n+1}")
# ponderation alternative : spectre de Q (facteur a^2 k^2 deja dans le poids) -- remarque seulement
# ---- G4 : dipole, controle par identites tensorielles isotropes <n_i n_j> = d/3, <n_i n_j n_k n_l> = (dd+dd+dd)/15
mx,my,mz=sp.symbols('m_x m_y m_z',real=True); m=sp.Matrix([mx,my,mz]); d=sp.eye(3)
N2=d/3
def N4(i,j,k_,l): return (d[i,j]*d[k_,l]+d[i,k_]*d[j,l]+d[i,l]*d[j,k_])/15
# eB = -(m - n (n.m)), eE = n x m ; eB eB - eE eE = 2 m_perp m_perp - |m_perp|^2 (1 - n n)
mm=m*m.T; m2=m.dot(m)
# <m_perp m_perp>_ij = m_i m_j - <n_i n_k> m_k m_j - m_i m_k <n_k n_j> + <n_i n_j n_k n_l> m_k m_l
Mpp=sp.Matrix(3,3,lambda i,j: mm[i,j]-sum(N2[i,q]*m[q]*m[j]+m[i]*m[q]*N2[q,j] for q in range(3))+sum(N4(i,j,p,q)*m[p]*m[q] for p in range(3) for q in range(3)))
# <|m_perp|^2 (d - n n)> = m2 d - m2 N2 - <(n.m)^2> d + <(n.m)^2 n n>
nm2=sum(N2[p,q]*m[p]*m[q] for p in range(3) for q in range(3))
Wpp=sp.Matrix(3,3,lambda i,j: m2*d[i,j]-m2*N2[i,j]-nm2*d[i,j]+sum(N4(i,j,p,q)*m[p]*m[q] for p in range(3) for q in range(3)))
Sminus=(2*Mpp-Wpp).applyfunc(sp.expand); Splus=Wpp.applyfunc(sp.expand)
print("\nG4 <eBeB - eEeE> - (4/5)(mm - m^2/3) =",sp.simplify(Sminus-sp.Rational(4,5)*(mm-m2*d/3)))
Sp_tf=Splus-d*Splus.trace()/3
print("   <eBeB + eEeE> sans trace =",sp.simplify(Sp_tf-sp.Rational(2,15)*(mm-m2*d/3))," (attendu 0 si = (2/15)(mm - m^2/3))")
# ---- faisceau non polarise EQUILIBRE (meme direction, deux polarisations, E = B, intensites egales)
print("\n##### faisceau non polarise equilibre")
analyse('T11_faisceau_non_polarise_equilibre',[((1,0,0),(0,1,0),1,0,(0,1,0),0,1),((2,0,0),(0,0,1),sp.Rational(1,2),0,(0,0,1),0,1)])
print("\nEXIT 0")
