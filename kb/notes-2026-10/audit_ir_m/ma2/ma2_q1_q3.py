# M-a2, questions 1-3 : a, b en fonction de J+, J- ; Q_k ; interference vs t0.
# Conventions : J^(omega,k) = int dt d3x exp(+i omega t - i k.x) J(t,x)
#               A_k(t) = int d3x exp(-i k.x) A(t,x) ; jauge de Coulomb, J transverse
#               A'' - lap A = J  ->  A_k'' + k^2 A_k = J_k(t) ; E = -dA/dt ; B = curl A
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp, quad
rng = np.random.default_rng(1)

print("=== Q1 : controle numerique (ODE du mode, source impulsionnelle) ===")
k = 2.3
v1 = rng.normal(size=2) + 1j*rng.normal(size=2)   # composantes transverses complexes
v2 = rng.normal(size=2) + 1j*rng.normal(size=2)
def Jk(t):  # deux impulsions a support quasi compact, eteintes bien avant 0
    return v1*np.exp(-((t+12)/1.1)**2)*np.cos(1.7*t) + v2*np.exp(-((t+7)/0.6)**2)
def rhs(t, y):
    A = y[0:2] + 1j*y[2:4]; Ad = y[4:6] + 1j*y[6:8]
    Add = Jk(t) - k**2*A
    return np.concatenate([Ad.real, Ad.imag, Add.real, Add.imag])
sol = solve_ivp(rhs, [-25, 0], np.zeros(8), rtol=1e-11, atol=1e-13)
y = sol.y[:, -1]
a_ode = y[0:2] + 1j*y[2:4]; b_ode = -(y[4:6] + 1j*y[6:8])
def Jhat(w):
    re = [quad(lambda t: (np.exp(1j*w*t)*Jk(t))[c].real, -25, 0, limit=400)[0] for c in range(2)]
    im = [quad(lambda t: (np.exp(1j*w*t)*Jk(t))[c].imag, -25, 0, limit=400)[0] for c in range(2)]
    return np.array(re) + 1j*np.array(im)
Jp, Jm = Jhat(+k), Jhat(-k)
a_f = 1j*(Jp - Jm)/(2*k); b_f = -(Jp + Jm)/2
print("a ODE    =", a_ode); print("a formule=", a_f, " |ecart| =", np.abs(a_ode-a_f).max())
print("b ODE    =", b_ode); print("b formule=", b_f, " |ecart| =", np.abs(b_ode-b_f).max())

print("\n=== Q2 : Q_k exact (symbolique, plan transverse, k^ = e3) ===")
p1,p2,m1,m2 = sp.symbols('p1 p2 m1 m2')  # J+ et J- complexes
Jpv = sp.Matrix(sp.symbols('jp1r jp2r', real=True)) + sp.I*sp.Matrix(sp.symbols('jp1i jp2i', real=True))
Jmv = sp.Matrix(sp.symbols('jm1r jm2r', real=True)) + sp.I*sp.Matrix(sp.symbols('jm1i jm2i', real=True))
kk = sp.symbols('k', positive=True)
R = sp.Matrix([[0,-1],[1,0]])   # k^ x (.) dans le plan transverse
a = sp.I*(Jpv - Jmv)/(2*kk); b = -(Jpv + Jmv)/2
H = lambda M: M.conjugate().T
re = lambda M: M.applyfunc(lambda z: sp.re(sp.expand(z)))
Qk = re(kk**2*(R*a)*H(R*a) - b*H(b))
def Lof(M):  # partie lineaire (sym. sans trace) de Re(M)
    Mr = re(M); return (Mr + Mr.T)/2 - sp.eye(2)*Mr.trace()/2
Mdiag = Jpv*H(Jpv) + Jmv*H(Jmv)
diag_pred = -Lof(Mdiag)/2
interf_pred = -sp.re(sp.expand((H(Jmv)*Jpv)[0]))/2*sp.eye(2)
print("Q_k - [ -L(J+J+^dag + J-J-^dag)/2  - Re(J-^dag J+)/2 * P_perp ] =",
      sp.simplify(Qk - diag_pred - interf_pred))
# V (partie antisymetrique imaginaire) et intensite ne contribuent pas a la partie diagonale :
I_, Qs, Us, V = sp.symbols('I Q U V', real=True)
Mst = sp.Matrix([[I_+Qs, Us - sp.I*V],[Us + sp.I*V, I_-Qs]])/2
print("Partie diagonale pour une matrice de Stokes generique:",
      sp.simplify(re(R*Mst*R.T - Mst)/4).tolist(), " (pas de I, pas de V)")

print("\n=== Q3 : dependance en t0 et moyenne de bande ===")
# impulsion J(t) = f(t - t0) eps : J+- = exp(+- i k t0) f^(+-k) eps
t0 = sp.symbols('t0', real=True); fp, fm = sp.symbols('fp fm')
Jp_t0 = sp.exp(sp.I*kk*t0)*fp; Jm_t0 = sp.exp(-sp.I*kk*t0)*fm
print("J-^* J+ =", sp.simplify(sp.conjugate(Jm_t0)*Jp_t0), " (phase exp(2 i k t0))")
# moyenne numerique sur une bande, profil gaussien f(t)=exp(-t^2/(2 s^2)) cos(w0 t)
s, w0 = 0.5, 3.0
fh = lambda w: np.sqrt(2*np.pi)*s*0.5*(np.exp(-s**2*(w-w0)**2/2)+np.exp(-s**2*(w+w0)**2/2))
ks = np.linspace(2.0, 4.0, 20001)
for T in [0, -2, -5, -10, -20, -40]:
    interf = np.trapezoid(np.real(np.exp(2j*ks*T)*fh(ks)*fh(-ks)), ks)
    diag = np.trapezoid(np.abs(fh(ks))**2 + np.abs(fh(-ks))**2, ks)
    print(f"t0={T:6.1f}  bande[2,4] : interf/diag = {interf/diag: .3e}")
print("fenetre lisse (bande gaussienne centree 3, largeur 0.5) :")
wnd = np.exp(-((ks-3.0)/0.25)**2)
for T in [0, -2, -5, -10, -20, -40]:
    interf = np.trapezoid(wnd*np.real(np.exp(2j*ks*T)*fh(ks)*fh(-ks)), ks)
    diag = np.trapezoid(wnd*(np.abs(fh(ks))**2 + np.abs(fh(-ks))**2), ks)
    print(f"t0={T:6.1f}  interf/diag = {interf/diag: .3e}")
