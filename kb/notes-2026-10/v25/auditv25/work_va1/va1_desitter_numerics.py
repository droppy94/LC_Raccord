# VA-1 : verifications numeriques sur de Sitter (H=1)
# Mode : i u' = (alpha.k + beta*mu/(-eta)) u ; variable s = ln(-eta) : du/ds = i( e^s alpha.k + mu beta ) u
import numpy as np
from scipy.integrate import solve_ivp
from math import factorial

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2)); E = np.eye(2)
beta = np.block([[E, Z], [Z, -E]]).astype(complex)
alpha = [np.block([[Z, s], [s, Z]]) for s in (s1, s2, s3)]
Pp = (np.eye(4) + beta) / 2; Pm = (np.eye(4) - beta) / 2

def adk(kvec):
    return sum(kvec[i] * alpha[i] for i in range(3))

def rhs_s(s, y, K, mu):
    u = y[:4] + 1j * y[4:]
    du = 1j * (np.exp(s) * (K @ u) + mu * (beta @ u))
    return np.concatenate([du.real, du.imag])

def evolve(u0, eta0, etas, kvec, mu, rtol=1e-11, atol=1e-13):
    K = adk(kvec)
    s_eval = np.log(-np.asarray(etas))
    sol = solve_ivp(rhs_s, (np.log(-eta0), s_eval[-1]), np.concatenate([u0.real, u0.imag]),
                    t_eval=s_eval, method='DOP853', rtol=rtol, atol=atol, args=(K, mu))
    return (sol.y[:4] + 1j * sol.y[4:]).T

def chi_of(u, eta, mu):
    # chi = Omega^{-i mu beta} u, Omega = -eta (theta = -mu ln Omega exactement)
    Om = -eta
    return np.array([Om ** (-1j * mu) * u[0], Om ** (-1j * mu) * u[1], Om ** (1j * mu) * u[2], Om ** (1j * mu) * u[3]])

rng = np.random.default_rng(1)
print("=== V2 : Proposition 1 (norme, borne ||chi-chi0|| <= k|eta| ||chi0||, absence de limite) ===")
for (mu, kvec) in [(1.0, [0.0, 0.0, 0.5]), (3.0, [1.2, -0.7, 1.4]), (0.3, [0.0, 2.0, 0.0])]:
    k = np.linalg.norm(kvec)
    u0 = rng.normal(size=4) + 1j * rng.normal(size=4); u0 /= np.linalg.norm(u0)
    etas = -np.logspace(0, -9, 400)
    U = evolve(u0, -1.0, etas, kvec, mu)
    chis = np.array([chi_of(U[i], etas[i], mu) for i in range(len(etas))])
    chi0 = chis[-1]
    normdev = np.max(np.abs(np.linalg.norm(U, axis=1) - 1))
    ratio = np.max(np.linalg.norm(chis[:-50] - chi0, axis=1) / (k * np.abs(etas[:-50]) * np.linalg.norm(chi0)))
    comp = U[:, 0]
    print(f"mu={mu}, k={k:.3f}: max|  ||u||-1 | = {normdev:.1e} ; max ||chi-chi0||/(k|eta|||chi0||) = {ratio:.3f} (<=1 attendu) ;"
          f" Re u_0 sur la derniere decade : min {comp.real[-45:].min():+.3f} max {comp.real[-45:].max():+.3f}")

print("\n=== V2 : Remarque 1 (Frobenius, P_+- entieres, P_+-(0)=chi0^+-) ===")
mu = 1.3; kvec = np.array([0.4, -0.9, 0.6]); K = adk(kvec)
# u = Omega^{i mu beta} sum_n c_n Omega^n ; recurrence (n + i mu beta - i mu beta_ad) ... :
# d/dOmega u = (i mu beta/Omega + i K) u  (H=1) ; avec u = sum_n Omega^n Omega^{i mu beta} ... on construit la matrice P :
# Y(Omega) = P(Omega) Omega^{i mu beta},  P' = i mu [beta,P]/Omega + i K P ... on resout coefficient par coefficient
N = 60
Pn = [np.eye(4, dtype=complex)]
for n in range(1, N):
    rhs = 1j * K @ Pn[n - 1]
    X = np.zeros((4, 4), complex)
    # n X - i mu (beta X - X beta) = rhs  ; resolution element par element (beta diagonal)
    b = np.diag(beta).real
    for i in range(4):
        for j in range(4):
            X[i, j] = rhs[i, j] / (n - 1j * mu * (b[i] - b[j]))
    Pn.append(X)
norms = [np.linalg.norm(X, 2) for X in Pn]
kk = np.linalg.norm(kvec)
print("||P_n|| * n! / k^n pour n=5,10,20,40 :", [f"{norms[n]*factorial(n)/kk**n:.3f}" for n in (5, 10, 20, 40)], "(borne => serie entiere)")
# comparaison avec integration numerique
chi0 = rng.normal(size=4) + 1j * rng.normal(size=4); chi0 /= np.linalg.norm(chi0)
def useries(Om):
    P = sum(Pn[n] * Om ** n for n in range(N))
    return P @ (np.array([Om ** (1j * mu)] * 2 + [Om ** (-1j * mu)] * 2) * chi0)
etaA, etaB = -2.5, -1e-7
UB = evolve(useries(-etaA), etaA, [etaB], kvec, mu)[0]
print("ecart serie de Frobenius / integration (eta de -2.5 a -1e-7) :", f"{np.linalg.norm(UB-useries(-etaB)):.2e}")
# interference pour X = 1 : coefficients de P_+^dag P_- doivent etre nuls
Pp_ser = [X @ (Pp @ chi0) for X in Pn]; Pm_ser = [X @ (Pm @ chi0) for X in Pn]
for name, Xop in [("1", np.eye(4)), ("beta", beta), ("alpha_1", alpha[0])]:
    coefs = [sum(np.vdot(Pp_ser[i], Xop @ Pm_ser[n - i]) for i in range(n + 1)) for n in range(6)]
    print(f"X={name:8s}: coefficients Omega^0..5 de P_+^dag X P_- :", " ".join(f"{abs(c):.1e}" for c in coefs))

print("\n=== V5 : poids d'antiparticule du mode Bunch-Davies a scri ===")
def bd_weight(mu, kvec, X=4000.0, eta_end=1e-8):
    k = np.linalg.norm(kvec); K = adk(kvec)
    eta0 = -X / k
    Hm = K + beta * mu / (-eta0)
    w, v = np.linalg.eigh(Hm)
    out = []
    for idx in np.where(w > 0)[0]:          # les deux helicites d'energie positive
        u = evolve(v[:, idx], eta0, [-eta_end / k], kvec, mu)[0]
        ch = chi_of(u, -eta_end / k, mu)
        out.append((np.linalg.norm(Pm @ ch) ** 2 / np.linalg.norm(ch) ** 2, ch))
    return out
for mu in (0.2, 0.5, 1.0, 2.0):
    th = 1 / (np.exp(2 * np.pi * mu) + 1)
    vals = []
    for kvec in ([0, 0, 0.7], [1.5, -2.0, 0.3], [0, 4.0, 0]):
        res = bd_weight(mu, np.array(kvec, float))
        vals += [r[0] for r in res]
        # terme croise de beta entre les deux helicites (meme k) a scri
        cross = abs(np.vdot(res[0][1], beta @ res[1][1]))
    print(f"mu={mu}: poids numeriques {['%.6e' % x for x in vals]} ; 1/(e^(2 pi mu)+1) = {th:.6e} ; "
          f"ecart relatif max {max(abs(x-th)/th for x in vals):.1e} ; |croise beta helicites| (dernier k) = {cross:.1e}")
    print(f"      1-2w = {1-2*np.mean(vals):.6f} ; tanh(pi mu) = {np.tanh(np.pi*mu):.6f}")

print("\n=== V5 : paquet d'ondes (Plancherel discretise) : Omega * int rho_hat -> m tanh(pi m/H) ||f||^2 ===")
mu = 0.5
rng2 = np.random.default_rng(7)
ks = [rng2.normal(size=3) for _ in range(5)]
tot_norm = 0; tot_E = 0
for kvec in ks:
    res = bd_weight(mu, kvec, eta_end=1e-7)
    for (w_, ch) in res:
        c = rng2.normal() + 1j * rng2.normal()
        # au lieu de evaluer a eta fixe pour tous les k on utilise la limite Omega*rho_hat -> m chi^dag beta chi
        tot_norm += abs(c) ** 2 * np.linalg.norm(ch) ** 2
        tot_E += abs(c) ** 2 * mu * np.real(np.vdot(ch, beta @ ch))
print(f"Omega*E/||f||^2 = {tot_E/tot_norm:.6f} ; m tanh(pi m) = {mu*np.tanh(np.pi*mu):.6f}")
# signe ponctuel : croise entre deux k distincts
res1 = bd_weight(mu, ks[0])[0][1]; res2 = bd_weight(mu, ks[1])[0][1]
print("terme croise ponctuel chi_k^dag beta chi_k' (complexe, module/phase quelconques) :", np.round(np.vdot(res1, beta @ res2), 4))

print("\n=== V4 : composantes du tenseur en poids poussiere, solution a deux exposants ===")
mu = 1.0; kvec = np.array([0.0, 0.0, 0.8]); k = 0.8
u0 = rng.normal(size=4) + 1j * rng.normal(size=4); u0 /= np.linalg.norm(u0)
etas = -np.logspace(0, -8, 2000)
U = evolve(u0, -1.0, etas, kvec, mu)
Om = -etas
T33 = np.array([k * np.real(np.vdot(x, alpha[2] @ x)) for x in U])     # T_33 = k u^dag alpha_3 u (k selon z)
T03 = k * np.linalg.norm(U, axis=1) ** 2
rho = np.array([np.real(np.vdot(U[i], (adk(kvec) + beta * mu / Om[i]) @ U[i])) for i in range(len(Om))])
print("T_eta3 = k|u|^2 : constant ? ecart max", f"{np.ptp(T03):.1e}")
print("T_33 = k u^dag alpha_3 u sur la derniere decade : min", f"{T33[-250:].min():+.4f}", "max", f"{T33[-250:].max():+.4f}", "(oscille sans limite -> Omega*T_33 = O(Omega) avec interference)")
print("Omega*rho_hat (poids poussiere) en eta=-1e-6,-1e-7,-1e-8 :", [f"{(Om*rho)[np.argmin(abs(etas+e))]:+.6f}" for e in (1e-6, 1e-7, 1e-8)],
      "; limite m(|chi0+|^2-|chi0-|^2) =", f"{mu*np.real(np.vdot(chi_of(U[-1],etas[-1],mu), beta@chi_of(U[-1],etas[-1],mu))):+.6f}")
