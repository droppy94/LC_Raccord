"""Q3 : tenseur d'energie-impulsion de Dirac sur FLRW conforme (puis de Sitter).
Derivation (rapport, section Q3) en signature (+,-,-,-) ; les composantes T_mn a deux indices
bas sont identiques en (-,+,+,+) (T^{mn} est le meme objet physique, deux abaissements).
Action : L = sqrt(-g) [ (i/2)(psibar g^m D_m psi - D_m psibar g^m psi) - m psibar psi ]
Variation de tetrade : T_mn = (i/4)[psibar g_(m D_n) psi - D_(m psibar g_n) psi]*2/2 - g_mn L
(L = 0 sur couche).
Verifications :
 (1) l'equation de Dirac courbe pour psi = a^{-3/2} u e^{ik.x} equivaut a i u' = (alpha.k + beta m a) u
 (2) T_hat_mn = a^{-2} T^flat_mn[u]  (meme formule, gamma plates, d ordinaire)
 (3) nabla-hat^m T_hat_mn = 0 sur couche, a(eta) quelconque
 (4) forme explicite : T00 = u^+ H u, T0a = -k_a u^+u (en composantes k^a du vecteur k), Tab = (k_a J_b + k_b J_a)/2
"""
import sympy as sp

I = sp.I
eta_, x, y, z = sp.symbols('eta x y z', real=True)
X = [eta_, x, y, z]
m = sp.Symbol('m', positive=True)
kv = sp.symbols('k1:4', real=True)
a = sp.Function('a', positive=True)(eta_)

s0 = sp.eye(2); s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
def blk(A, B, C, D):
    return sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))
Z = sp.zeros(2)
beta = blk(s0, Z, Z, -s0)
alph = [blk(Z, s, s, Z) for s in (s1, s2, s3)]
gam = [beta] + [beta * al for al in alph]          # gamma^A standard, (+,-,-,-)
etaM = sp.diag(1, -1, -1, -1)
gl = [sum((etaM[A, B] * gam[B] for B in range(4)), sp.zeros(4)) for A in range(4)]  # gamma_A

# metrique physique, tetrade
g = a**2 * etaM; ginv = g.inv()
E = [[(1 / a if mu == A else 0) for A in range(4)] for mu in range(4)]  # e^mu_A
Ed = [[(a if mu == A else 0) for mu in range(4)] for A in range(4)]    # e^A_mu
Gam = [[[sp.simplify(sum(ginv[l, s] * (sp.diff(g[s, mu], X[nu]) + sp.diff(g[s, nu], X[mu]) - sp.diff(g[mu, nu], X[s]))
                        for s in range(4)) / 2) for nu in range(4)] for mu in range(4)] for l in range(4)]
# omega_mu^A_B = e^A_nu (d_mu e^nu_B + Gamma^nu_{mu lam} e^lam_B)
def omega(mu, A, B):
    return sp.simplify(sum(Ed[A][nu] * (sp.diff(E[nu][B], X[mu]) + sum(Gam[nu][mu][l] * E[l][B] for l in range(4)))
                           for nu in range(4)))
SpinC = []
for mu in range(4):
    Gm = sp.zeros(4)
    for A in range(4):
        for B in range(4):
            wAB = etaM[A, A] * omega(mu, A, B)
            Gm += wAB * (gam[A] * gam[B] - gam[B] * gam[A]) / 8
    SpinC.append(sp.simplify(Gm))
gup = [sum((E[mu][A] * gam[A] for A in range(4)), sp.zeros(4)) for mu in range(4)]   # gamma^mu courbe
gdn = [sum((g[mu, nu] * gup[nu] for nu in range(4)), sp.zeros(4)) for mu in range(4)]

U = sp.Matrix([sp.Function(f'u{i}')(eta_) for i in range(4)])
W = sp.Matrix([sp.Function(f'w{i}')(eta_) for i in range(4)])   # w = conj(u)
ph = sp.exp(I * (kv[0] * x + kv[1] * y + kv[2] * z))
psi = a**sp.Rational(-3, 2) * U * ph
psid = (a**sp.Rational(-3, 2) * W * sp.conjugate(ph)).T            # psi^dagger (ligne)
psib = psid * beta
Hm = sum((kv[i] * alph[i] for i in range(3)), sp.zeros(4)) + beta * m * a
Hc = Hm.conjugate()
subsd = {sp.Derivative(U[i], eta_): (-I * Hm * U)[i] for i in range(4)}
subsd.update({sp.Derivative(W[i], eta_): (I * Hc * W)[i] for i in range(4)})

D = [sp.diff(psi, X[mu]) + SpinC[mu] * psi for mu in range(4)]
Db = [sp.diff(psib, X[mu]) - psib * SpinC[mu] for mu in range(4)]

# (1) equation de Dirac
dir_eq = sum((I * gup[mu] * D[mu] for mu in range(4)), sp.zeros(4, 1)) - m * psi
dir_eq = sp.simplify((dir_eq.subs(subsd)) / ph)
print('(1) Dirac courbe <=> i u\' = (alpha.k + beta m a) u :', dir_eq == sp.zeros(4, 1))

# T hat
That = sp.zeros(4)
for mu in range(4):
    for nu in range(4):
        e = (psib * gdn[mu] * D[nu] + psib * gdn[nu] * D[mu] - Db[mu] * gdn[nu] * psi - Db[nu] * gdn[mu] * psi)[0, 0]
        That[mu, nu] = sp.simplify(sp.expand(I * e / 4))
That = That.applyfunc(lambda e: sp.simplify(e))

# T flat de u (gamma plats, derivees ordinaires, phase e^{ikx})
psic = U * ph; psicb = (W * sp.conjugate(ph)).T * beta
Tfl = sp.zeros(4)
for mu in range(4):
    for nu in range(4):
        e = (psicb * gl[mu] * sp.diff(psic, X[nu]) + psicb * gl[nu] * sp.diff(psic, X[mu])
             - sp.diff(psicb, X[mu]) * gl[nu] * psic - sp.diff(psicb, X[nu]) * gl[mu] * psic)[0, 0]
        Tfl[mu, nu] = sp.simplify(sp.expand(I * e / 4))
print('(2) That_mn = a^-2 Tflat_mn[u] :', sp.simplify((That - Tfl / a**2).subs(subsd)) == sp.zeros(4))

# (3) conservation : nabla_mu T^mu_nu
Tmix = (ginv * That)   # T^mu_nu
sqrtg = a**4
cons = []
for nu in range(4):
    e = sum(sp.diff(sqrtg * Tmix[mu, nu], X[mu]) for mu in range(4)) / sqrtg \
        - sum(Gam[l][mu][nu] * Tmix[mu, l] for mu in range(4) for l in range(4))
    e = e.doit()
    for _ in range(3):   # second derivees : substitutions iterees
        e = e.subs(subsd).doit()
    cons.append(sp.simplify(sp.expand(e)))
print('(3) conservation nabla-hat_mu T^mu_nu = 0 :', all(c == 0 for c in cons))

# (4) forme explicite
uu = (W.T * U)[0, 0]
Jv = [(W.T * al * U)[0, 0] for al in alph]
T00 = (W.T * Hm * U)[0, 0]
chk = [sp.simplify((Tfl[0, 0] - T00).subs(subsd)) == 0]
for i in range(3):
    chk.append(sp.simplify((Tfl[0, i + 1] + kv[i] * uu).subs(subsd)) == 0)
    for j in range(3):
        chk.append(sp.simplify((Tfl[i + 1, j + 1] - (kv[i] * Jv[j] + kv[j] * Jv[i]) / 2).subs(subsd)) == 0)
print('(4) T00 = u+Hu, T0a = -k_a u+u, Tab = (k_a J_b + k_b J_a)/2 :', all(chk))
trace = sp.simplify((Tfl[0, 0] - Tfl[1, 1] - Tfl[2, 2] - Tfl[3, 3] - m * a * (W.T * beta * U)[0, 0]).subs(subsd))
print('    trace (+---) de Tflat = m a ubar u :', trace == 0)
