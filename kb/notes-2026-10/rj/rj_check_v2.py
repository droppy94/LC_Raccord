# rj_check_v2.py  (chantier RJ, gel NOTE-206) : v2 apres audit (NOTE-209) : signe de tau_0a corrige (RA-2), test de la classe pure (RA-1, RA-2)
# P0 : identite exacte (Minkowski conforme g = eta, hat g = Omega^-2 eta, T-hat arbitraire) :
#      2 Omega^-1 nabla-hat_[k L-hat_l]j  =  1/2 (d_k tau'_lj - d_l tau'_kj)  +  Omega^-1 S_jkl(tau, n)
#      tau = Omega^-3 T-hat(e-hat, e-hat) = T-hat_jk / Omega (coordonnees), tau' = tau - (1/3) tr_g(tau) g, n = dOmega,
#      S_jkl = 1/2 [ 2(n_k tau'_lj - n_l tau'_kj) - g_kj n^m tau'_lm + g_lj n^m tau'_km ]   (kappa = 1)
# P1 : noyau de S pour n de genre temps : quels tau annulent S (poussiere tau = rho U U, U || n).
# P2 : champ de Dirac test sur de Sitter (carte plate, Omega = -H eta) : tau de Dirac, S/Omega le long des solutions
#      (generique, particule pure a la limite, k = 0), conservation, phase du coefficient de l'equation pour chi.
import sympy as sp, numpy as np
from scipy.integrate import solve_ivp

print("=== P0 : identite (sympy exact) ===")
t,x,y,z = sp.symbols('t x y z', real=True); X=[t,x,y,z]
lam = sp.Symbol('lambda', positive=True)
eta = sp.diag(-1,1,1,1)
Om = -t + sp.Rational(1,5)*x**2 + sp.Rational(1,7)*y*z + sp.Rational(1,3)*t*x   # Omega generique (polynomial)
# T-hat symetrique arbitraire (polynomes)
import itertools, random
random.seed(1)
That = sp.zeros(4,4)
for a in range(4):
    for b in range(a,4):
        e = sum(sp.Rational(random.randint(-3,3),random.randint(1,4))*m for m in [1,t,x,y,z,t*x,y**2,x*z,t**2])
        That[a,b]=e; That[b,a]=e
gh = eta/Om**2; ghi = eta*Om**2
# Christoffel de hat g
Gam = [[[sum(ghi[a,d]*(sp.diff(gh[d,b],X[c])+sp.diff(gh[d,c],X[b])-sp.diff(gh[b,c],X[d])) for d in range(4))/2
         for c in range(4)] for b in range(4)] for a in range(4)]
trT = sum(ghi[a,b]*That[a,b] for a in range(4) for b in range(4))
Lh = (That - trT*gh/3)/2 + lam*gh/6
def covd(Tm,k,l,j):  # nabla-hat_k T_lj
    return sp.diff(Tm[l,j],X[k]) - sum(Gam[m][k][l]*Tm[m,j] for m in range(4)) - sum(Gam[m][k][j]*Tm[l,m] for m in range(4))
tau = That/Om
trtau = sum(eta[a,a]*tau[a,a] for a in range(4))
taup = tau - trtau*eta/3
n = [sp.diff(Om,v) for v in X]; nup = [eta[m,m]*n[m] for m in range(4)]
maxres = 0
for j in range(4):
    for k in range(4):
        for l in range(k+1,4):
            lhs = 2/Om*(covd(Lh,k,l,j)-covd(Lh,l,k,j))/2
            S = sp.Rational(1,2)*(2*(n[k]*taup[l,j]-n[l]*taup[k,j]) - eta[k,j]*sum(nup[m]*taup[l,m] for m in range(4))
                                  + eta[l,j]*sum(nup[m]*taup[k,m] for m in range(4)))
            rhs = sp.Rational(1,2)*(sp.diff(taup[l,j],X[k])-sp.diff(taup[k,j],X[l])) + S/Om
            d = sp.simplify(sp.together(lhs-rhs))
            if d != 0:
                maxres += 1
print("composantes (j,k<l) testees : 24 ; residus non nuls :", maxres)

print("\n=== P1 : noyau de S pour n = -nu e0 ===")
nu = sp.Symbol('nu', positive=True)
ts = sp.symbols('t00 t01 t02 t03 t11 t12 t13 t22 t23 t33')
T = sp.Matrix([[ts[0],ts[1],ts[2],ts[3]],[ts[1],ts[4],ts[5],ts[6]],[ts[2],ts[5],ts[7],ts[8]],[ts[3],ts[6],ts[8],ts[9]]])
trt = sum(eta[a,a]*T[a,a] for a in range(4)); Tp = T - trt*eta/3
nn = [-nu,0,0,0]; nnu=[eta[m,m]*nn[m] for m in range(4)]
eqs=[]
for j in range(4):
    for k in range(4):
        for l in range(k+1,4):
            eqs.append(sp.expand(sp.Rational(1,2)*(2*(nn[k]*Tp[l,j]-nn[l]*Tp[k,j]) - eta[k,j]*sum(nnu[m]*Tp[l,m] for m in range(4))
                                  + eta[l,j]*sum(nnu[m]*Tp[k,m] for m in range(4)))))
sol = sp.solve(eqs, ts, dict=True)
print("solution generale de S = 0 :", sol)
M = sp.Matrix([[sp.diff(e,v) for v in ts] for e in eqs])
print("rang de l'application tau -> S :", M.rank(), "sur 10 composantes ; noyau de dimension", 10-M.rank())

print("\n=== P2 : Dirac test sur de Sitter ===")
s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]],complex)
Z=np.zeros((2,2)); I2=np.eye(2)
beta=np.block([[I2,Z],[Z,-I2]]).astype(complex)
alph=[np.block([[Z,s],[s,Z]]) for s in (s1,s2,s3)]
Hh=1.0; m=0.7
def run(kvec, eta0, eta1, u0, rtol=1e-11, atol=1e-13):
    ak=sum(k*a for k,a in zip(kvec,alph))
    def f(e,u):
        a=-1/(Hh*e); return -1j*(ak+beta*m*a)@u
    return solve_ivp(f,(eta0,eta1),u0,method='DOP853',rtol=rtol,atol=atol,dense_output=True)
def bil(u,kvec,e):
    Om=-Hh*e; a=1/Om
    B=np.vdot(u,beta@u).real; N=np.vdot(u,u).real; J=np.array([np.vdot(u,al@u).real for al in alph]); kv=np.array(kvec)
    tau=np.zeros((4,4))
    tau[0,0]=Om*kv@J + m*B
    tau[0,1:]=tau[1:,0]=-Om*kv*N   # signe physique (RA-2 E2)
    tau[1:,1:]=0.5*Om*(np.outer(kv,J)+np.outer(J,kv))
    return tau,B,N,J,Om
etaM=np.diag([-1,1,1,1.])
def Sover(tau,Om):
    n=np.array([-Hh,0,0,0]); nup=etaM@n
    tr=np.trace(etaM@tau); tp=tau-tr*etaM/3
    out=[]
    for j in range(4):
        for k in range(4):
            for l in range(k+1,4):
                out.append(0.5*(2*(n[k]*tp[l,j]-n[l]*tp[k,j]) - etaM[k,j]*(nup@tp[l]) + etaM[l,j]*(nup@tp[k]))/Om)
    return np.array(out)

# conservation : d/dt rho + H (3 rho + sum p) = 0 avec rho = a^-4 (k.J + m a B), sum p = a^-4 k.J
kvec=[0.6,0.0,0.8]
rng=np.random.default_rng(3); u0=rng.normal(size=4)+1j*rng.normal(size=4); u0/=np.linalg.norm(u0)
sol=run(kvec,-10.0,-1e-7,u0)
es=-np.logspace(1,-7,400)
def rho_sp(e):
    u=sol.sol(e); tau,B,N,J,Om=bil(u,kvec,e); a=1/Om; kv=np.array(kvec)
    return a**-4*(kv@J+m*a*B), a**-4*(kv@J)
res=[]
for e in es[5:-5]:
    h=1e-6*abs(e)
    r1,_=rho_sp(e-h); r2,_=rho_sp(e+h); r,sp_=rho_sp(e)
    a=-1/(Hh*e); dt_de=a  # dt = a d eta
    drdt=(r2-r1)/(2*h)/a
    res.append(abs(drdt+Hh*(3*r+sp_))/abs(Hh*3*r))
print("conservation (residu relatif max) :", max(res))

def report(label,sol,kvec,es):
    vals=[];
    for e in es:
        tau,B,N,J,Om=bil(sol.sol(e),kvec,e); vals.append((Om,Sover(tau,Om),tau))
    print(label)
    for Om,S,tau in vals[::len(vals)//8]:
        print(f"  Omega={Om:9.2e}  max|S/Omega|={np.max(np.abs(S)):.5f}  tau00={tau[0,0]:+.5f}  |tau_0a|/Om={np.linalg.norm(tau[0,1:])/Om:.5f}  |tau_ab|/Om={np.linalg.norm(tau[1:,1:])/Om:.6f}")
    # oscillation a la fin : etendue de S/Omega sur la derniere decade
    last=[v[1] for v in vals if v[0]<1e-5]
    if last:
        A=np.array(last); print("  derniere decade (Omega<1e-5) : max - min de S/Omega par composante (max) =", np.max(A.max(0)-A.min(0)))
    return vals

es2=-np.logspace(-1,-8,1500)/Hh
print("\n-- (a) solution generique (melange particule/antiparticule) --")
sol_a=run(kvec,-10.0,-1e-8,u0); report("generique",sol_a,kvec,es2)
print("\n-- (b) particule pure a la limite : chi = (1,0,0,0) impose en eta = -1e-8 (integration a rebours) --")
ub=np.array([1,0,0,0],complex)
# u = U0 chi, U0 = exp(i beta (m/H) ln Omega)
Omf=1e-8; U0=np.diag(np.exp(1j*np.diag(beta).real*(m/Hh)*np.log(Omf)))
sol_b=run(kvec,-1e-8,-10.0,U0@ub)
report("particule pure",sol_b,kvec,es2)
print("\n-- (c) k = 0 (homogene) --")
sol_c=run([0,0,0],-10.0,-1e-8,u0); report("k=0",sol_c,[0,0,0],es2)

print("\n=== P3 : equation pour chi = U0^dagger u ===")
# i chi' = U0^dag (alpha.k) U0 chi ; U0^dag alpha_i U0 = alpha_i exp(2 i beta (m/H) ln Omega)
for Om in [1e-2,1e-4,1e-6]:
    U0=np.diag(np.exp(1j*np.diag(beta).real*(m/Hh)*np.log(Om)))
    C=U0.conj().T@alph[0]@U0
    print(f"  Omega={Om:.0e}  element (0,3) du coefficient (alpha_1 conjugue) = {C[0,3]:.4f}  (module {abs(C[0,3]):.3f})")
print("  identite U0^dag alpha_1 U0 = alpha_1 exp(2 i beta theta) :",
      np.allclose(U0.conj().T@alph[0]@U0, alph[0]@np.diag(np.exp(2j*np.diag(beta).real*(m/Hh)*np.log(1e-6)))))

print("\n=== P4 (v2) : classe pure, bilineaires analytiques en Omega ===")
for e in [-1e-1,-1e-2,-1e-3,-1e-4,-1e-5]:
    tau,B,N,J,Om=bil(sol_b.sol(e),kvec,e)
    print(f"  Omega={Om:.0e}  |tau_ab|/Omega^2={np.linalg.norm(tau[1:,1:])/Om**2:.5f}  (tau00-m)/Omega={(tau[0,0]-m)/Om:+.6f}")
print("  (convergence sans oscillation : tau_ab = O(Omega^2), tau_00 = m + O(Omega^2) ; seule l'inconnue chi porte la phase)")
