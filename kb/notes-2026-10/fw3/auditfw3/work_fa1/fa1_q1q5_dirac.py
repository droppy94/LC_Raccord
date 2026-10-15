#!/usr/bin/env python3
# FA-1 : verifications pour Q1 (poids de la densite de Yang-Mills, courant de Dirac)
# et Q5 (covariance conforme de l operateur de Dirac, coefficient de masse rescale,
# ordre du terme ghat_ab Lag_D, poids du tenseur energie-impulsion de Dirac).
# Metrique physique ghat = Om^-2 eta, tetrade ehat^A_mu = Om^-1 delta^A_mu.
import itertools, sympy as sp

idx = range(4)
eta = sp.diag(-1, 1, 1, 1)
Om = sp.Symbol('Omega', positive=True)
y, e, m = sp.symbols('y e m', real=True)

# jets d ordre 1 pour Omega, 1 pour les composantes du spineur, 0 pour A_a
dOm = [sp.Symbol(f'Om_{c}', real=True) for c in idx]
ddOm = {t: sp.Symbol('Om_' + ''.join(map(str, t)), real=True) for t in itertools.combinations_with_replacement(idx, 2)}
u = [sp.Symbol(f'u{k}') for k in range(4)]                       # psi_r (complexes)
du = [[sp.Symbol(f'u{k}_{c}') for c in idx] for k in range(4)]  # d_c psi_r
A = [sp.Symbol(f'A_{c}', real=True) for c in idx]
p1, p2 = sp.symbols('p1 p2', real=True)
Hr = (p1 + sp.I * p2) / sp.sqrt(2)

jetD = {Om: dOm}
for c in idx:
    jetD[dOm[c]] = [ddOm[tuple(sorted((c, d)))] for d in idx]
uc = [sp.Symbol(f'uc{k}') for k in range(4)]                     # conjugues de psi_r (symboles independants)
duc = [[sp.Symbol(f'uc{k}_{c}') for c in idx] for k in range(4)]
for k in range(4):
    jetD[u[k]] = du[k]
    jetD[uc[k]] = duc[k]

def D(expr, c):
    expr = sp.sympify(expr)
    out = 0
    for sym in expr.atoms(sp.Symbol):
        if sym in jetD:
            out += sp.diff(expr, sym) * jetD[sym][c]
    return out

# ---------- Q1 : poids de sqrt(-ghat) ghat^{ma} ghat^{nb} ----------
ghat = eta / Om**2
ghat_inv = eta * Om**2
sqrtg_hat = sp.sqrt(-ghat.det())
for mm in idx:
    for a in idx:
        for n in idx:
            for b in idx:
                assert sp.simplify(sqrtg_hat * ghat_inv[mm, a] * ghat_inv[n, b]
                                   - sp.sqrt(-eta.det()) * eta[mm, a] * eta[n, b]) == 0
print('Q1 : sqrt(-ghat) ghat^{ma} ghat^{nb} = sqrt(-g) g^{ma} g^{nb} (poids Om^0) : verifie')

# ---------- matrices gamma, signature (-,+,+,+) : {gamma^A, gamma^B} = 2 eta^{AB} ----------
I2, Z2 = sp.eye(2), sp.zeros(2)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
g0_std = sp.Matrix(sp.BlockMatrix([[I2, Z2], [Z2, -I2]]))
gi_std = [sp.Matrix(sp.BlockMatrix([[Z2, sg], [-sg, Z2]])) for sg in sig]
gam = [sp.I * g0_std] + [sp.I * gi for gi in gi_std]     # gamma^A, indice tetrade en haut
for a in idx:
    for b in idx:
        assert (gam[a] * gam[b] + gam[b] * gam[a]) == 2 * eta[a, b] * sp.eye(4)
beta = g0_std   # psibar = psi^dagger beta  (beta = gamma^0_std, hermitien, beta gamma^A beta = -(gamma^A)^dagger ... verifie ci-dessous)
for a in idx:
    assert sp.simplify(beta * gam[a].H * beta - (-gam[a])) == sp.zeros(4) or sp.simplify(beta * gam[a].H * beta + gam[a]) == sp.zeros(4)

# ---------- connexion de spin de ghat ----------
# Christoffel de ghat = Om^-2 eta
Gam = [[[sp.simplify(sum(ghat_inv[c, d] * (D(ghat[d, b], a) + D(ghat[d, a], b) - D(ghat[a, b], d)) for d in idx) / 2)
         for b in idx] for a in idx] for c in idx]
E_up = [[Om * (1 if A_ == mu else 0) for mu in idx] for A_ in idx]        # ehat_A^mu
E_dn = [[(1 if A_ == mu else 0) / Om for mu in idx] for A_ in idx]       # ehat^A_mu
# omega_mu^A_B = ehat^A_nu (d_mu ehat_B^nu + Gam^nu_{mu lam} ehat_B^lam)
def om_AB(mu, A_, B_):
    return sp.simplify(sum(E_dn[A_][nu] * (D(E_up[B_][nu], mu) + sum(Gam[nu][mu][la] * E_up[B_][la] for la in idx)) for nu in idx))
omega = [[[sum(eta[A_, C] * om_AB(mu, C, B_) for C in idx) for B_ in idx] for A_ in idx] for mu in idx]  # omega_{mu A B}
for mu in idx:
    for A_ in idx:
        for B_ in idx:
            assert sp.simplify(omega[mu][A_][B_] + omega[mu][B_][A_]) == 0   # antisymetrie

gam_hat_up = [Om * gam[mu] for mu in idx]      # gammahat^mu = ehat_A^mu gamma^A
# determination du signe de Sigma_mu par le postulat de la tetrade : nablahat_mu gammahat^nu = 0
def tetrad_postulate(sign):
    for mu in idx:
        Sig = sign * sp.Rational(1, 4) * sum((omega[mu][A_][B_] * gam[A_] * gam[B_] for A_ in idx for B_ in idx), sp.zeros(4))
        for nu in idx:
            expr = gam_hat_up[nu].applyfunc(lambda z: D(z, mu)) + sum((Gam[nu][mu][la] * gam_hat_up[la] for la in idx), sp.zeros(4)) \
                   + Sig * gam_hat_up[nu] - gam_hat_up[nu] * Sig
            if sp.simplify(expr) != sp.zeros(4):
                return False
    return True
signs = [sg for sg in (+1, -1) if tetrad_postulate(sg)]
assert len(signs) == 1, signs
sign = signs[0]
print('Connexion de spin : signe fixe par le postulat de la tetrade, sign =', sign)
Sigma = [sign * sp.Rational(1, 4) * sum((omega[mu][A_][B_] * gam[A_] * gam[B_] for A_ in idx for B_ in idx), sp.zeros(4)) for mu in idx]

# ---------- Q5 : covariance conforme de l operateur de Dirac (avec jauge) ----------
psi_r = sp.Matrix(u)
psi = Om ** sp.Rational(3, 2) * psi_r
def Dhat(mu, chi):   # nablahat_mu chi - i e A_mu chi
    return chi.applyfunc(lambda z: D(z, mu)) + Sigma[mu] * chi - sp.I * e * A[mu] * chi
Dirac_hat = sum((gam_hat_up[mu] * Dhat(mu, psi) for mu in idx), sp.zeros(4, 1))
Dirac_flat_r = sum((gam[mu] * (psi_r.applyfunc(lambda z: D(z, mu)) - sp.I * e * A[mu] * psi_r) for mu in idx), sp.zeros(4, 1))
assert sp.simplify(Dirac_hat - Om ** sp.Rational(5, 2) * Dirac_flat_r) == sp.zeros(4, 1)
print('Q5 : gammahat^mu Dhat_mu (Om^{3/2} psi_r) = Om^{5/2} gamma^mu D_mu psi_r : verifie')

# equation de Dirac avec masse de Yukawa : (i gammahat.Dhat - y H) psi = 0, H = Om H_r
eqY = sp.I * Dirac_hat - y * Om * Hr * psi
eqY_r = sp.I * Dirac_flat_r - y * Hr * psi_r
assert sp.simplify(eqY - Om ** sp.Rational(5, 2) * eqY_r) == sp.zeros(4, 1)
print('Q5 : equation de Dirac rescalee = Om^{5/2} [ (i gamma.D - y H_r) psi_r ] : coefficient de masse y H_r (regulier)')
eqm = sp.I * Dirac_hat - m * psi
eqm_r = sp.I * Dirac_flat_r - m / Om * psi_r
assert sp.simplify(eqm - Om ** sp.Rational(5, 2) * eqm_r) == sp.zeros(4, 1)
print('Q5 : avec masse constante m : coefficient de masse rescale = m/Om (singulier)')

# ---------- Q5 : le terme ghat_ab Lag_D ----------
psibar = Om ** sp.Rational(3, 2) * sp.Matrix([uc]) * beta
psibar_r = sp.Matrix([uc]) * beta
LagD_Y = (psibar * (sp.I * Dirac_hat - y * Om * Hr * psi))[0, 0]
LagD_Y_r = (psibar_r * (sp.I * Dirac_flat_r - y * Hr * psi_r))[0, 0]
assert sp.simplify(LagD_Y - Om**4 * LagD_Y_r) == 0
print('Q5 : Lag_D (Yukawa) = Om^4 Lag_D^r  =>  ghat_ab Lag_D = Om^2 eta_ab Lag_D^r (ordre Om^2)')
LagD_m = (psibar * (sp.I * Dirac_hat - m * psi))[0, 0]
mass_part = sp.simplify(LagD_m - Om**4 * (psibar_r * sp.I * Dirac_flat_r)[0, 0])
assert sp.simplify(mass_part + m * Om**3 * (psibar_r * psi_r)[0, 0]) == 0
print('Q5 : avec masse constante : ghat_ab (-m psibar psi) = -m Om eta_ab psibar_r psi_r (ordre Om^1)')

# ---------- Q1 : courant de Dirac ----------
for n in idx:
    Jn = (psibar * gam_hat_up[n] * psi)[0, 0] * e
    jr = (psibar_r * gam[n] * psi_r)[0, 0] * e
    assert sp.simplify(Jn - Om**4 * jr) == 0
print('Q1 : J^n_Dirac = Om^4 j_r^n : verifie')

# ---------- Q3/Q5 : poids du tenseur energie-impulsion de Dirac (partie cinetique symetrisee) ----------
def T_dirac_hat(mu, nu):
    gam_hat_dn = [sum((ghat[mu2, la] * gam_hat_up[la] for la in idx), sp.zeros(4)) for mu2 in idx]
    def term(a, b):
        Dpsi = Dhat(b, psi)
        Dpsibar = psibar.applyfunc(lambda z: D(z, b)) - psibar * Sigma[b] + sp.I * e * A[b] * psibar
        return (psibar * gam_hat_dn[a] * Dpsi)[0, 0] - (Dpsibar * gam_hat_dn[a] * psi)[0, 0]
    return sp.I / 4 * (term(mu, nu) + term(nu, mu))
def T_dirac_flat(mu, nu):
    gam_dn = [sum((eta[mu2, la] * gam[la] for la in idx), sp.zeros(4)) for mu2 in idx]
    def term(a, b):
        Dpsi = psi_r.applyfunc(lambda z: D(z, b)) - sp.I * e * A[b] * psi_r
        Dpsibar = psibar_r.applyfunc(lambda z: D(z, b)) + sp.I * e * A[b] * psibar_r
        return (psibar_r * gam_dn[a] * Dpsi)[0, 0] - (Dpsibar * gam_dn[a] * psi_r)[0, 0]
    return sp.I / 4 * (term(mu, nu) + term(nu, mu))
for mu in idx:
    for nu in idx:
        if mu <= nu:
            assert sp.simplify(sp.expand(T_dirac_hat(mu, nu) - Om**2 * T_dirac_flat(mu, nu))) == 0
print('Q3/Q5 : T^D_ab (partie cinetique symetrisee, avec jauge) = Om^2 T^D_ab[psi_r] exactement : verifie')
print('       (les termes en dOm issus de la connexion de spin et du poids 3/2 se compensent)')
