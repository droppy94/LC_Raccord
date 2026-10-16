"""VA-3 : controles numeriques (de Sitter, H=1) : borne de la Prop. 3 quand le coefficient s'annule,
tanh du paquet (convergence dominee), exemples de la Prop. 4 et masse LambdaCDM."""
import numpy as np
from scipy.integrate import solve_ivp, quad
s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.diag([1,-1]).astype(complex)
Z=np.zeros((2,2)); E=np.eye(2)
beta=np.block([[E,Z],[Z,-E]]).astype(complex)
alph=[np.block([[Z,s],[s,Z]]) for s in (s1,s2,s3)]
def run(m,k,chi_end,eta_end=-1e-9,eta_start=-1.0):
    ak=k*alph[2]; mu=m
    def rhs(eta,chi):
        Om=-eta
        ph=np.exp(1j*mu*np.log(Om)*np.diag(beta).real)   # Omega^{i mu beta} diag
        V=(ph.conj()[:,None])*ak*(ph[None,:])
        return -1j*V@chi
    sol=solve_ivp(rhs,[eta_end,eta_start],chi_end,method='DOP853',rtol=1e-11,atol=1e-13,dense_output=True)
    etas=-np.logspace(np.log10(-eta_end),0,4000)
    out=[]
    for et in etas:
        chi=sol.sol(et); Om=-et
        ph=np.exp(1j*mu*np.log(Om)*np.diag(beta).real)
        u=ph*chi
        rho=np.real(u.conj()@(ak@u))+(m/Om)*np.real(u.conj()@(beta@u))
        out.append((Om,rho,np.real(u.conj()@u)))
    return np.array(out)
print("[P3] coefficient nul (||chi0+||=||chi0-||), de Sitter, H=1")
for m,k in [(1,0.5),(3,2),(0.3,1.0)]:
    chi=np.array([1,0,1,0],complex)/np.sqrt(2)
    o=run(m,k,chi)
    print(f"  m={m} k={k}: sup|rho_hat| = {np.max(np.abs(o[:,1])):.4f}, borne m k/H + k = {m*k+k:.4f}, norme in [{o[:,2].min():.12f},{o[:,2].max():.12f}]")
print("[P3] coefficient non nul : Omega*rho_hat -> m(|c+|^2-|c-|^2), et rho_hat - c/Omega borne")
for m,k in [(1,0.5),(3,2)]:
    chi=np.array([np.sqrt(0.8),0,np.sqrt(0.2),0],complex)
    o=run(m,k,chi); c=m*0.6
    print(f"  m={m} k={k}: Omega*rho a Omega={o[0,0]:.1e} : {o[0,0]*o[0,1]:.8f} (attendu {c}); sup|rho - c/Omega| = {np.max(np.abs(o[:,1]-c/o[:,0])):.4f}")
# paquet : Omega * int (rho) -> m tanh(pi m/H) ||f||^2 ; dominante (Omega_1 k + m)|f|^2
print("[QV] identite 1 - 2/(e^{2 pi x}+1) = tanh(pi x) :",
      max(abs(1-2/(np.exp(2*np.pi*x)+1)-np.tanh(np.pi*x)) for x in np.linspace(0.01,3,300)))
# convergence dominee : majorant |Omega rho_k| <= Omega k + m pour u normalise
f2=lambda k: k**2*np.exp(-k)           # |f^(k)|^2 d^3k radial (exemple), int k|f|^2 fini
print("    int k |f|^2 d^3k (exemple exp(-k)) =",quad(lambda k:4*np.pi*k*f2(k),0,np.inf)[0])
# Prop 4 exemples de Sitter
print("[P4] m = 3 Omega^{1/2} = 3 e^{-t/2}: int m dt =",quad(lambda t:3*np.exp(-t/2),0,np.inf)[0]," ; m a = 3 e^{t/2} non borne")
print("[P4] LambdaCDM : |m_eff| = m rho_m/(4 rho_L) ~ Omega^3 :  int_0^inf e^{-3t} dt fini, m a ~ Omega^2 -> 0, mu = Omega^2 lisse")
