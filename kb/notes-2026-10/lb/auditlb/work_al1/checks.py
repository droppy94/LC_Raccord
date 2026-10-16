import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
rng = np.random.default_rng(1)

# ---------- Q5 : CAR, etat quasi-libre pur, a*(f) Omega ----------
n = 4
I2 = np.eye(2); Z = np.diag([1., -1.]); a1 = np.array([[0, 1], [0, 0]], dtype=complex)  # a|1>=|0>
def kron_all(ms):
    out = np.array([[1.0+0j]])
    for m in ms: out = np.kron(out, m)
    return out
A = [kron_all([Z]*j + [a1] + [I2]*(n-j-1)) for j in range(n)]   # Jordan-Wigner
def a(f):  return sum(np.conj(f[j])*A[j] for j in range(n))      # a(f) antilineaire
def ad(f): return a(f).conj().T
# projecteur P de rang 2 (modes occupes) dans une base aleatoire
U, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))
P = U[:, :2] @ U[:, :2].conj().T
# vecteur de Fock : Slater des 2 premieres colonnes de U appliquees au vide
vac = np.zeros(2**n, dtype=complex); vac[0] = 1.0   # |00..0> : a_j vac = 0 avec convention a1|1>=|0>
# avec a1=[[0,1],[0,0]], etat |0>=(1,0) est annule par a1 ? a1 (1,0) = (0,0) oui
Om = ad(U[:, 1]) @ ad(U[:, 0]) @ vac; Om /= np.linalg.norm(Om)
def twopt(psi):  # G[i,j] = <psi| a*(e_j) a(e_i) |psi> ; omega(a*(u)a(v)) = <v, G u>
    E = np.eye(n)
    return np.array([[np.vdot(psi, ad(E[j]) @ a(E[i]) @ psi) for j in range(n)] for i in range(n)])
G = twopt(Om)
print("Q5 omega(a*a) == P :", np.allclose(G, P))
f = (np.eye(n) - P) @ (rng.normal(size=n) + 1j*rng.normal(size=n)); f /= np.linalg.norm(f)
Phi = ad(f) @ Om
print("Q5 norme a*(f)Omega :", np.linalg.norm(Phi))
Gf = twopt(Phi)
print("Q5 omega_f(a*a) == P + |f><f| :", np.allclose(Gf, P + np.outer(f, f.conj())))
# quasi-liberte : verif. Wick sur 4 points aleatoires
def wick4(psi, Gm):
    us = [rng.normal(size=n)+1j*rng.normal(size=n) for _ in range(4)]
    lhs = np.vdot(psi, ad(us[0]) @ ad(us[1]) @ a(us[2]) @ a(us[3]) @ psi)
    w = lambda u, v: np.vdot(v, Gm @ u)   # omega(a*(u) a(v))
    rhs = w(us[1], us[2])*w(us[0], us[3]) - w(us[0], us[2])*w(us[1], us[3])
    return np.isclose(lhs, rhs)
print("Q5 Wick 4 points pour omega_f :", all(wick4(Phi, Gf) for _ in range(5)))
# purete : Gf projecteur
print("Q5 Gf projecteur :", np.allclose(Gf @ Gf, Gf))

# ---------- Q1 : borne de structure vs Lemme 3.1 ----------
# i du/deta = (alpha.k + beta m a) u, a=-1/(H eta). Rep. 2x2 par helicite : beta=diag(1,-1), alpha.k = k sigma_x
H, m, k = 1.0, 3.0, 2.0
sx = np.array([[0, 1], [1, 0]], complex); b = np.diag([1., -1.]).astype(complex)
def rhs(eta, u):
    a_ = -1/(H*eta); return -1j*((k*sx + b*m*a_) @ u)
eta0 = -5.0
u0 = np.array([1, 0.3j]); u0 = u0/np.linalg.norm(u0)
etas = np.clip(-np.logspace(np.log10(5), -7, 400), -5.0, -1e-7)
def rhs_r(eta, y):
    u = y[:2] + 1j*y[2:]; du = rhs(eta, u); return np.r_[du.real, du.imag]
sol = solve_ivp(rhs_r, [eta0, -1e-7], np.r_[u0.real, u0.imag], t_eval=etas, rtol=1e-11, atol=1e-13, method="DOP853")
U_ = sol.y[:2] + 1j*sol.y[2:]
Om_ = -H*sol.t   # Omega = 1/a = -H eta
chi = np.array([expm(-1j*b*(m/H)*np.log(Om_[i])) @ U_[:, i] for i in range(len(sol.t))]).T
chi0 = chi[:, -1]
err = np.linalg.norm(chi - chi0[:, None], axis=0)
bound_extract = k*np.abs(sol.t)*np.linalg.norm(chi0)
bound_dfmr_corr = (np.exp(k*np.abs(sol.t)*H) - 1)*np.linalg.norm(chi0)   # (exp(|lam| e^{-t})-1), H=1
print("Q1 borne extrait respectee :", np.all(err <= bound_extract*(1+1e-6) + 1e-9))
print("Q1 borne DFMR corrigee respectee :", np.all(err <= bound_dfmr_corr*(1+1e-6) + 1e-9))
print("Q1 norme conservee :", np.ptp(np.linalg.norm(U_, axis=0)))
print("Q1 ratio max err/(k|eta|) :", np.max(err/bound_extract))

# ---------- tanh ----------
nu = 0.7
print("tanh check :", np.isclose(1 - 2/(np.exp(2*np.pi*nu)+1), np.tanh(np.pi*nu)))
