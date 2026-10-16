"""Q1/Q2 : 2 Omega^{-1} nabla-hat_[k Lhat_l]j  pour That symetrique quelconque.
Formule analytique (derivee a la main, voir rapport) :
  RHS_{jkl} = nabla_[k S_l]j + Omega^{-1} A_{klj},
  S = tau - (1/3) tr(tau) g,
  A_{klj} = n_k S_lj - n_l S_kj - (1/2)( g_jk (S n)_l - g_jl (S n)_k ),  (S n)_l = S_lm n^m.
Verification exacte independante : g = Minkowski (-,+,+,+), Omega et tau polynomiaux
explicites, ghat = Omega^{-2} g, That_ab = Omega tau_ab, calcul direct de nabla-hat avec les
Christoffel de ghat.
"""
import sympy as sp
import itertools, random

X = sp.symbols('t x y z')
t, x, y, z = X
lam = sp.Symbol('lambda')
eta = sp.diag(-1, 1, 1, 1)
N = 4

random.seed(1)
def rpoly():
    return sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4)) * m
               for m in [1, t, x, y, z, t*x, y*z, t**2, x*z, t*y])

Om = 2 + t/3 + x**2/5 - y*z/7 + t*x/11
tau = sp.zeros(4)
for a in range(4):
    for b in range(a, 4):
        tau[a, b] = tau[b, a] = rpoly()

g = eta
ginv = eta.inv()
gh = g / Om**2
ghinv = g.inv() * Om**2

def christoffel(G, Ginv):
    return [[[sp.simplify(sum(Ginv[m, s] * (sp.diff(G[s, a], X[b]) + sp.diff(G[s, b], X[a])
                                              - sp.diff(G[a, b], X[s])) for s in range(N)) / 2)
              for b in range(N)] for a in range(N)] for m in range(N)]

Gh = christoffel(gh, ghinv)

That = Om * tau                     # composantes coordonnees, cf. rapport
trT = sum(ghinv[a, b] * That[a, b] for a in range(N) for b in range(N))
Lh = (That - trT * gh / 3) / 2 + lam * gh / 6

def cov_hat(L, k, l, j):  # nabla-hat_k L_lj
    return sp.diff(L[l, j], X[k]) - sum(Gh[m][k][l] * L[m, j] + Gh[m][k][j] * L[l, m] for m in range(N))

n = [sp.diff(Om, v) for v in X]
nup = [sum(ginv[a, b] * n[b] for b in range(N)) for a in range(N)]
trtau = sum(ginv[a, b] * tau[a, b] for a in range(N) for b in range(N))
S = tau - trtau * g / 3
Sn = [sum(S[l, m] * nup[m] for m in range(N)) for l in range(N)]

ok = True
for k, l, j in itertools.product(range(N), repeat=3):
    if k >= l:
        continue
    direct = 2 / Om * (cov_hat(Lh, k, l, j) - cov_hat(Lh, l, k, j)) / 2
    reg = (sp.diff(S[l, j], X[k]) - sp.diff(S[k, j], X[l])) / 2   # g plate : nabla = d
    A = n[k] * S[l, j] - n[l] * S[k, j] - (g[j, k] * Sn[l] - g[j, l] * Sn[k]) / 2
    diff = sp.simplify(sp.together(direct - reg - A / Om))
    if diff != 0:
        ok = False
        print('ECHEC', k, l, j, diff)
print('Q1 verification exacte (Minkowski, Omega et tau explicites, lambda symbolique) :', ok)

# ---------- Q2 : noyau de tau -> A(tau, n) pour n de genre temps ----------
# On travaille dans un repere ou n = N0 * (dt) (n_a = (-N0? ) ) : n_a = (nn,0,0,0), n timelike.
nn = sp.Symbol('n0', nonzero=True)
nvec = [nn, 0, 0, 0]
nvu = [ginv[a, a] * nvec[a] for a in range(N)]
tv = sp.symbols('t0:10')
T = sp.zeros(4)
idx = [(a, b) for a in range(4) for b in range(a, 4)]
for s, (a, b) in zip(tv, idx):
    T[a, b] = T[b, a] = s
trT2 = sum(ginv[a, a] * T[a, a] for a in range(N))
S2 = T - trT2 * g / 3
Sn2 = [sum(S2[l, m] * nvu[m] for m in range(N)) for l in range(N)]
eqs = []
for k, l, j in itertools.product(range(N), repeat=3):
    eqs.append(sp.expand(nvec[k] * S2[l, j] - nvec[l] * S2[k, j]
                         - (g[j, k] * Sn2[l] - g[j, l] * Sn2[k]) / 2))
M = sp.Matrix([[sp.diff(e, s) for s in tv] for e in eqs])
print('rang de tau -> A :', M.rank(), ' (dim tau = 10) ; noyau :', M.nullspace())
# Verification generale (n quelconque timelike, symbolique) : tau = rho nu nu annule A
n_s = sp.symbols('m0:4')
rho = sp.Symbol('rho')
nvec = list(n_s)
nvu = [ginv[a, a] * nvec[a] for a in range(N)]
n2 = sum(nvec[a] * nvu[a] for a in range(N))
Td = sp.Matrix(4, 4, lambda a, b: -rho * nvec[a] * nvec[b] / n2)  # = rho nu_a nu_b, nu = n/sqrt(-n^2)
trd = sum(ginv[a, a] * Td[a, a] for a in range(N))
Sd = Td - trd * g / 3
Snd = [sum(Sd[l, m] * nvu[m] for m in range(N)) for l in range(N)]
allz = all(sp.simplify(nvec[k] * Sd[l, j] - nvec[l] * Sd[k, j] - (g[j, k] * Snd[l] - g[j, l] * Snd[k]) / 2) == 0
           for k, l, j in itertools.product(range(N), repeat=3))
print('tau = rho nu nu annule A pour n generique :', allz)
