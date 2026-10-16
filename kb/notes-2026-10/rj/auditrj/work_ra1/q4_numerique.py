"""Q4/Q5/Q6 : verification numerique sur de Sitter, carte plate, g = Minkowski (-,+,+,+), Omega = -H eta,
n = dOmega = (-H, 0, 0, 0).
tau_jk = Omega * Tflat_jk[u] :
   tau_00 = Omega u^+ H u,  tau_0a = -Omega k_a u^+u,  tau_ab = Omega (k_a J_b + k_b J_a)/2,  J_a = u^+ alpha_a u.
Singulier : Sing = Omega^{-1} A(tau, n) ;  Regulier : R_{jkl} = (1/2)(d_k S_lj - d_l S_kj).
Variable s = ln Omega ; chi defini par u = exp(i beta mu s) chi, mu = m/H :
   d chi/ds = (i/H) Omega (alpha.k) Omega^{2 i mu beta} chi    (forme reguliere en s).
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

# ---------- forme symbolique de A pour n = (-H,0,0,0) ----------
Hs = sp.Symbol('H', positive=True)
ts = sp.symbols('tau00 tau01 tau02 tau03 tau11 tau12 tau13 tau22 tau23 tau33')
g = sp.diag(-1, 1, 1, 1)
T = sp.zeros(4); it = iter(ts)
for a_ in range(4):
    for b_ in range(a_, 4):
        T[a_, b_] = T[b_, a_] = next(it)
nl = [-Hs, 0, 0, 0]; nu = [g[i, i] * nl[i] for i in range(4)]
tr = sum(g[i, i] * T[i, i] for i in range(4))
S = T - tr * g / 3
Sn = [sum(S[l, m] * nu[m] for m in range(4)) for l in range(4)]
def Asym(k, l, j):
    return sp.expand(nl[k] * S[l, j] - nl[l] * S[k, j] - (g[j, k] * Sn[l] - g[j, l] * Sn[k]) / 2)
print('Composantes de A_{klj} (n = -H d eta), k<l :')
for k in range(4):
    for l in range(k + 1, 4):
        for j in range(4):
            e = Asym(k, l, j)
            if e != 0:
                print(f'  A_[{k}{l}]{j} =', e)
Afun = sp.lambdify([ts, Hs], [[[Asym(k, l, j) for j in range(4)] for l in range(4)] for k in range(4)], 'numpy')

# ---------- Dirac ----------
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.])
Z = np.zeros((2, 2))
beta = np.block([[s0, Z], [Z, -s0]]).astype(complex)
alph = [np.block([[Z, s], [s, Z]]).astype(complex) for s in (s1, s2, s3)]
Pp = (np.eye(4) + beta) / 2; Pm = (np.eye(4) - beta) / 2

H = 1.0
def run(kvec, m, chi_init, Om0, Om1, npts=4000):
    ak = sum(kvec[i] * alph[i] for i in range(3))
    mu = m / H
    def rhs(s, y):
        chi = y[:4] + 1j * y[4:]
        Om = np.exp(s)
        ph = np.diag(np.exp(2j * mu * s * np.diag(beta).real))
        d = (1j / H) * Om * ak @ ph @ chi
        return np.concatenate([d.real, d.imag])
    s_eval = np.linspace(np.log(Om0), np.log(Om1), npts)
    sol = solve_ivp(rhs, (s_eval[0], s_eval[-1]), np.concatenate([chi_init.real, chi_init.imag]),
                    t_eval=s_eval, rtol=1e-12, atol=1e-14, method='DOP853')
    chi = sol.y[:4] + 1j * sol.y[4:]
    out = []
    for i, s in enumerate(sol.t):
        Om = np.exp(s)
        u = np.exp(1j * mu * s * np.diag(beta).real) * chi[:, i]
        Hm = ak + beta * m / Om
        uu = np.vdot(u, u).real
        J = np.array([np.vdot(u, al @ u).real for al in alph])
        t00 = Om * np.vdot(u, Hm @ u).real
        t0 = [-Om * kvec[i_] * uu for i_ in range(3)]
        tab = [[Om * (kvec[i_] * J[j_] + kvec[j_] * J[i_]) / 2 for j_ in range(3)] for i_ in range(3)]
        tv = [t00, t0[0], t0[1], t0[2], tab[0][0], tab[0][1], tab[0][2], tab[1][1], tab[1][2], tab[2][2]]
        A = np.array(Afun(tv, H), dtype=float)
        # derivees temporelles (analytiques via u' = -i H u) pour la partie reguliere
        dt00 = -H * np.dot(kvec, J)                                   # d tau00 / d eta
        Jp = np.array([np.vdot(u, 1j * (Hm @ al - al @ Hm) @ u).real for al in alph])  # dJ/d eta
        dtab = [[(-H) * (kvec[i_] * J[j_] + kvec[j_] * J[i_]) / 2 + Om * (kvec[i_] * Jp[j_] + kvec[j_] * Jp[i_]) / 2
                 for j_ in range(3)] for i_ in range(3)]
        dt0 = [(-H) * (-kvec[i_] * uu) for i_ in range(3)]
        out.append(dict(Om=Om, s=s, t00=t00, t0=np.array(t0), tab=np.array(tab), A=A,
                        sing=A / Om, dt00=dt00, dtab=np.array(dtab), dt0=np.array(dt0),
                        chi=chi[:, i], J=J))
    return out

rng = np.random.default_rng(7)
kvec = np.array([0.7, -0.4, 0.5]); m = 1.3; mu = m / H
print(f'\nParametres : H={H}, m={m}, mu=m/H={mu}, k={kvec}, c attendu = 2 mu = {2*mu}')

def polyres(Om, Y, deg=4):
    """residu max d'un ajustement polynomial en Omega (test de serie entiere) sur la fenetre."""
    x = Om / Om.max()
    V = np.vander(x, deg + 1)
    coef, *_ = np.linalg.lstsq(V, Y, rcond=None)
    return np.abs(V @ coef - Y).max()

def report(name, out):
    Om = np.array([o['Om'] for o in out]); s = np.log(Om)
    sing = np.array([o['sing'].ravel() for o in out])
    tabO = np.array([(o['tab'] / o['Om']).ravel() for o in out]); t0O = np.array([o['t0'] / o['Om'] for o in out])
    t00 = np.array([o['t00'] for o in out])
    dt00 = np.array([o['dt00'] for o in out]); dtab = np.array([o['dtab'].ravel() for o in out])
    print(f'\n=== {name} ===')
    for lo in [1e-8, 1e-6, 1e-4, 1e-2]:
        w = (Om >= lo) & (Om <= 10 * lo)
        if w.sum() < 20:
            continue
        print(f'  Omega in [{lo:.0e},{10*lo:.0e}] : max|Sing| = {np.abs(sing[w]).max():.4e} '
              f'(residu fit polyn. en Omega {polyres(Om[w], sing[w]):.2e}) ; max|tau_ab/Omega| = {np.abs(tabO[w]).max():.3e} '
              f'(residu {polyres(Om[w], tabO[w]):.2e}) ; tau_0a/Omega = {t0O[w][-1]} ; '
              f'tau00 in [{t00[w].min():.6f},{t00[w].max():.6f}] ; max|d tau00/d eta| = {np.abs(dt00[w]).max():.3e} '
              f'(residu {polyres(Om[w], dt00[w]):.2e}) ; max|d tau_ab/d eta| = {np.abs(dtab[w]).max():.3e} '
              f'(residu {polyres(Om[w], dtab[w]):.2e})')
    w = Om <= 1e-4
    sig = sing[w][:, np.argmax(np.ptp(sing[w], axis=0))]
    res = polyres(Om[w], sig)
    if res > 1e-6:
        sig = sig - sig.mean()
        ss = s[w]; freqs = np.linspace(0.1, 6, 6000)
        pw = [abs(np.sum(sig * np.exp(-1j * f * ss))) for f in freqs]
        print(f'  frequence dominante de Sing en ln Omega (Omega <= 1e-4) : c = {freqs[int(np.argmax(pw))]:.4f}')
    else:
        print(f'  Sing compatible avec une serie entiere en Omega sur Omega <= 1e-4 (residu {res:.1e}) : pas d\'oscillation')
    return Om, sing

# (a) generique
chi_a = rng.normal(size=4) + 1j * rng.normal(size=4)
out_a = run(kvec, m, chi_a, 1.0, 1e-8, 20000)
Om_a, sing_a = report('(a) solution generique (chi(Omega=1) aleatoire)', out_a)
c0 = out_a[-1]['chi']
print('  chi0 approx (Omega=1e-8) : |P+ chi0| =', np.linalg.norm(Pp @ c0), ' |P- chi0| =', np.linalg.norm(Pm @ c0))

# (b) chi0 dans beta=+1 : integration montante depuis Omega = 1e-12 avec chi = chi0+ (erreur O(1e-12))
chi_b = Pp @ (rng.normal(size=4) + 1j * rng.normal(size=4))
out_b = run(kvec, m, chi_b, 1e-12, 1.0, 20000)
Om_b, sing_b = report('(b) chi0 dans l\'espace propre beta = +1', out_b)
# limite predite : Sing -> contribution de tau_0a/Omega = -k_a |chi0|^2
sing_pred = np.array(Afun([0, *(-kvec * np.vdot(chi_b, chi_b).real), 0, 0, 0, 0, 0, 0], H)).ravel()
i0 = np.argmin(abs(Om_b - 1e-6))
print('  ecart Sing(1e-6) - limite predite (contribution tau_0a seule) :', np.abs(sing_b[i0] - sing_pred).max())
# controle de la serie entiere : (Sing - limite)/Omega doit tendre vers une constante
for O in [1e-6, 1e-5, 1e-4, 1e-3]:
    i = np.argmin(abs(Om_b - O))
    print(f'    Omega={Om_b[i]:.2e} : max|(Sing - lim)/Omega| = {np.abs((sing_b[i]-sing_pred)/Om_b[i]).max():.6f}')
# (b') beta = -1
chi_bm = Pm @ (rng.normal(size=4) + 1j * rng.normal(size=4))
report('(b\') chi0 dans l\'espace propre beta = -1', run(kvec, m, chi_bm, 1e-12, 1.0, 20000))

# (c) k = 0
out_c = run(np.zeros(3), m, chi_a, 1.0, 1e-8, 4000)
report('(c) k = 0', out_c)
print('  max|A| sur toute la trajectoire k=0 :', max(np.abs(o['A']).max() for o in out_c))

# (d) controle m = 0 (conforme) : tout est serie entiere
report('(d) controle m = 0, solution generique', run(kvec, 0.0, chi_a, 1.0, 1e-8, 20000))

# Q5 : coefficient de l'equation pour chi, i dchi/deta = (alpha.k) Omega^{2 i mu beta} chi
ak = sum(kvec[i] * alph[i] for i in range(3))
print('\nQ5 : element (1,3) du coefficient C(Omega) = (alpha.k) Omega^{2 i mu beta} :')
for O in [1e-2, 1e-4, 1e-6, 1e-8]:
    C = ak @ np.diag(np.exp(2j * mu * np.log(O) * np.diag(beta).real))
    print(f'   Omega={O:.0e} : C[0,2] = {C[0,2]:.6f}')
