#!/usr/bin/env python3
# FA-1 : verification independante des points Q1 (courant de Higgs), Q2 (covariance
# conforme de box - R/6 et coefficient Omega^-2), Q3 et Q4 (second membre de (2.17)).
#
# Methode : calcul en composantes sur g = eta (Minkowski, signature -+++), avec des
# "variables de jet" : Omega et ses derivees (ordre 0..3), phi1, phi2 (ordre 0..3),
# A_a (ordre 0..2) sont des symboles independants ; l'operateur D(expr, c) applique
# la regle de la chaine sur la table de jets. Ainsi toute expression est un polynome
# de Laurent en Omega, ce qui permet d'extraire les coefficients de Omega^-2, Omega^-1.
# Les substitutions (2.14) et (3.8) sont faites a la fin (a l'ordre dominant,
# suffisant pour Omega^-2 et Omega^-1, voir rapport).

import itertools, sys, time
import sympy as sp

t0 = time.time()
idx = range(4)
eta = sp.diag(-1, 1, 1, 1)
Om = sp.Symbol('Omega', positive=True)
kappa, lam, m2, xi, lh, e, s = sp.symbols('kappa lambda m2 xi lambda_h e s', real=True)
ds = [sp.Symbol(f's_{c}', real=True) for c in idx]

# ---------- jets ----------
def jet(name, order):
    return {t: sp.Symbol(name + '_' + ''.join(map(str, t)), real=True)
            for t in itertools.combinations_with_replacement(idx, order)}

jetD = {}   # symbole -> [derivee selon c, c=0..3]
TOP = set()

def make_scalar_jets(name, maxorder):
    levels = [{(): sp.Symbol(name, real=True)}]
    for k in range(1, maxorder + 2):
        levels.append(jet(name, k))
    for k in range(0, maxorder + 1):
        for t, sym in levels[k].items():
            jetD[sym] = [levels[k + 1][tuple(sorted(t + (c,)))] for c in idx]
    for sym in levels[maxorder + 1].values():
        TOP.add(sym)
    return levels

OmJ = make_scalar_jets('Om', 3)
P1J = make_scalar_jets('p1', 3)
P2J = make_scalar_jets('p2', 3)
# on identifie OmJ[0][()] a Om
OmJ[0][()] = Om
# il faut que la derivee de Om soit Om_a : on reconstruit la table pour Om
jetD[Om] = [OmJ[1][(c,)] for c in idx]

dOm = [OmJ[1][(c,)] for c in idx]
ddOm = OmJ[2]
dddOm = OmJ[3]

# A_a avec jets d'ordre 0..2 (cle : (a, tuple trie des indices de derivation))
AJ = {}
for a in idx:
    for k in range(0, 4):
        for t in itertools.combinations_with_replacement(idx, k):
            AJ[(a, t)] = sp.Symbol(f'A{a}_' + ''.join(map(str, t)), real=True)
for a in idx:
    for k in range(0, 3):
        for t in itertools.combinations_with_replacement(idx, k):
            jetD[AJ[(a, t)]] = [AJ[(a, tuple(sorted(t + (c,))))] for c in idx]
    for t in itertools.combinations_with_replacement(idx, 3):
        TOP.add(AJ[(a, t)])
A = [AJ[(a, ())] for a in idx]

for c in idx:
    jetD[s] = [ds[cc] for cc in idx]
# les derivees de s_c et des constantes ne sont jamais requises

def D(expr, c):
    expr = sp.sympify(expr)
    out = 0
    for sym in expr.free_symbols:
        if sym in jetD:
            out += sp.diff(expr, sym) * jetD[sym][c]
        elif sym in TOP:
            raise RuntimeError('derivee d ordre trop eleve requise : ' + str(sym))
    return out

# ---------- metrique physique ghat = Om^-2 eta ----------
ghat = eta / Om**2
ghat_inv = eta * Om**2

# Christoffel de ghat calcules directement
Gam = [[[0]*4 for _ in idx] for _ in idx]   # Gam[c][a][b] = Gamhat^c_ab
for c in idx:
    for a in idx:
        for b in idx:
            Gam[c][a][b] = sp.simplify(sum(ghat_inv[c, d] * (D(ghat[d, b], a) + D(ghat[d, a], b) - D(ghat[a, b], d))
                                          for d in idx) / 2)
# verification de la forme attendue
for c in idx:
    for a in idx:
        for b in idx:
            expected = -(1/Om) * ((1 if c == a else 0) * dOm[b] + (1 if c == b else 0) * dOm[a]
                                  - eta[a, b] * sum(eta[c, d] * dOm[d] for d in idx))
            assert sp.simplify(Gam[c][a][b] - expected) == 0
print('Christoffel de ghat : forme -Om^-1(delta dOm + delta dOm - eta dOm) verifiee')

# Riemann, Ricci, scalaire de ghat
def Riem(r, sg, mu, nu):
    return (D(Gam[r][nu][sg], mu) - D(Gam[r][mu][sg], nu)
            + sum(Gam[r][mu][l] * Gam[l][nu][sg] - Gam[r][nu][l] * Gam[l][mu][sg] for l in idx))
Ric = sp.zeros(4, 4)
for sg in idx:
    for nu in idx:
        Ric[sg, nu] = sp.expand(sum(Riem(r, sg, r, nu) for r in idx))
Rhat = sp.expand(sum(ghat_inv[a, b] * Ric[a, b] for a in idx for b in idx))
boxOm = sum(eta[a, b] * ddOm[tuple(sorted((a, b)))] for a in idx for b in idx)
dOm2 = sum(eta[a, b] * dOm[a] * dOm[b] for a in idx for b in idx)
for a in idx:
    for b in idx:
        exp_ab = 2/Om * ddOm[tuple(sorted((a, b)))] + (boxOm/Om - 3*dOm2/Om**2) * eta[a, b]
        assert sp.expand(Ric[a, b] - exp_ab) == 0
assert sp.expand(Rhat - Om**2 * (6*boxOm/Om - 12*dOm2/Om**2)) == 0
print('Formules de Friedrich pour Rhat_ab et Rhat : verifiees')
Ghat = Ric - Rhat * ghat / 2

# ---------- champs de matiere rescales ----------
p1, p2 = P1J[0][()], P2J[0][()]
Hr = (p1 + sp.I * p2) / sp.sqrt(2)
Hrc = (p1 - sp.I * p2) / sp.sqrt(2)
def DHr(a):   # D_a H_r = d_a H_r - i e A_a H_r
    return D(Hr, a) - sp.I * e * A[a] * Hr
def DHrc(a):
    return D(Hrc, a) + sp.I * e * A[a] * Hrc
H = Om * Hr
Hc = Om * Hrc
def DH(a):
    return D(H, a) - sp.I * e * A[a] * H
def DHc(a):
    return D(Hc, a) + sp.I * e * A[a] * Hc
Hr2 = (p1**2 + p2**2) / 2       # |H_r|^2
H2 = Om**2 * Hr2                # |H|^2

# ----- Q1 : courant de Higgs -----
for n in idx:
    Jn = sp.expand(sum(ghat_inv[n, b] * sp.I * e * (Hc * DH(b) - DHc(b) * H) for b in idx))
    jr = sp.expand(sum(eta[n, b] * sp.I * e * (Hrc * DHr(b) - DHrc(b) * Hr) for b in idx))
    assert sp.expand(Jn - Om**4 * jr) == 0
print('Q1 : J^n_Higgs = Om^4 j_r^n, sans terme en dOm : verifie')

# ----- Q2 : covariance conforme de box_D - R/6 -----
def boxhat_D(F, Fdagger=False):
    # ghat^{ab} (D_a D_b F) avec D_a = nabla_a - i e A_a (ou + pour le conjugue)
    sgn = 1 if Fdagger else -1
    out = 0
    for a in idx:
        for b in idx:
            DbF = D(F, b) + sgn * sp.I * e * A[b] * F
            DaDbF = D(DbF, a) + sgn * sp.I * e * A[a] * DbF - sum(Gam[c][a][b] * (D(F, c) + sgn * sp.I * e * A[c] * F) for c in idx)
            out += ghat_inv[a, b] * DaDbF
    return sp.expand(out)
lhs = sp.expand(boxhat_D(H) - Rhat / 6 * H)
box_flat_Hr = sp.expand(sum(eta[a, b] * (D(DHr(b), a) - sp.I * e * A[a] * DHr(b)) for a in idx for b in idx))
assert sp.expand(lhs - Om**3 * box_flat_Hr) == 0
print('Q2 : (boxhat_D - Rhat/6)(Om H_r) = Om^3 box_D H_r (g plat) : verifie')

# ---------- tenseur energie-impulsion physique ----------
def nabhat2(f, a, b):   # nablahat_a nablahat_b f, f scalaire
    return D(D(f, b), a) - sum(Gam[c][a][b] * D(f, c) for c in idx)
nn_H2 = [[sp.expand(nabhat2(H2, a, b)) for b in idx] for a in idx]
box_H2 = sp.expand(sum(ghat_inv[a, b] * nn_H2[a][b] for a in idx for b in idx))
DHl = [DH(a) for a in idx]
DHcl = [DHc(a) for a in idx]
L0 = -sum(ghat_inv[c, d] * DHcl[c] * DHl[d] for c in idx for d in idx) - m2 * H2 - lh * H2**2

T = sp.zeros(4, 4)   # Higgs (avec xi)
for a in idx:
    for b in idx:
        T[a, b] = sp.expand(DHcl[a] * DHl[b] + DHcl[b] * DHl[a] + ghat[a, b] * L0
                            + 2 * xi * (Ghat[a, b] * H2 + ghat[a, b] * box_H2 - nn_H2[a][b]))
# Maxwell
F = [[sp.expand(D(A[b], a) - D(A[a], b)) for b in idx] for a in idx]
F2 = sum(F[c][d] * F[ee][f] * ghat_inv[c, ee] * ghat_inv[d, f] for c in idx for d in idx for ee in idx for f in idx)
TF = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        TF[a, b] = sp.expand(sum(F[a][c] * F[b][d] * ghat_inv[c, d] for c in idx for d in idx) - ghat[a, b] * F2 / 4)
Ttot = T + TF
Ttr = sp.expand(sum(ghat_inv[a, b] * Ttot[a, b] for a in idx for b in idx))
print('T_ab et trace construits  (t = %.0f s)' % (time.time() - t0))

# verification : T_ab en variables de jet n'a pas de puissance negative de Om
for a in idx:
    for b in idx:
        assert sp.Poly(sp.expand(Ttot[a, b]), Om).degree() >= 0  # polynome en Om
print('T_ab est un polynome (puissances >= 0) en Om dans les variables rescalees')
Tt_poly = sp.Poly(Ttr, Om)
print('Trace That : plus basse puissance de Om =', min(m[0] for m in Tt_poly.monoms()))

# ---------- L hat et second membre de (2.17) ----------
Lh = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        Lh[a, b] = sp.expand(kappa / 2 * (Ttot[a, b] - Ttr * ghat[a, b] / 3) + lam / 6 * ghat[a, b])

def nabhatL(nu, la, rho):
    return D(Lh[la, rho], nu) - sum(Gam[c][nu][la] * Lh[c, rho] + Gam[c][nu][rho] * Lh[la, c] for c in idx)

# ---------- substitutions (2.14) a l'ordre dominant et (3.8) ----------
sub214 = {ddOm[t]: s * eta[t[0], t[1]] for t in ddOm}
for t in dddOm:
    a, b, c = t
    sub214[dddOm[t]] = (ds[c] * eta[a, b] + ds[b] * eta[a, c] + ds[a] * eta[b, c]) / 3
R38 = dOm[1]**2 + dOm[2]**2 + dOm[3]**2 + lam / 3 - 2 * Om * s   # = Om_0^2 d'apres (3.8) a l'ordre Om^1

def reduce38(expr):
    # remplace Om_0^2 par R38 (reduction polynomiale en Om_0)
    P = sp.Poly(sp.expand(expr), dOm[0])
    out = 0
    for (k,), coeff in P.terms():
        q, r = divmod(k, 2)
        out += coeff * R38**q * dOm[0]**r
    return sp.expand(out)

def laurent(expr, name):
    P = sp.Poly(sp.expand(expr * Om**4), Om)
    d = {}
    for (k,), coeff in P.terms():
        d[k - 4] = coeff
    return d

# coefficient attendu (K-3)
def K3(rho, nu, la):
    return kappa / 3 * (m2 + 4 * lam * xi - 2 * lam / 3) * (p1**2 + p2**2) * (dOm[nu] * eta[la, rho] - dOm[la] * eta[nu, rho]) / 2

results = {}
coef_m1 = {}
pairs = [(nu, la) for nu in idx for la in idx if nu < la]
for rho in idx:
    for (nu, la) in pairs:
        rhs = sp.expand((nabhatL(nu, la, rho) - nabhatL(la, nu, rho)) / Om)   # 2 Om^-1 nablahat_[nu L_lambda]rho
        rhs = rhs.subs(sub214)
        rhs = reduce38(rhs)
        d = laurent(rhs, f'rhs_{rho}{nu}{la}')
        lowest = min(d)
        assert lowest >= -2, (rho, nu, la, lowest)
        c2 = sp.factor(reduce38(d.get(-2, 0)))
        diff = sp.expand(reduce38(d.get(-2, 0) - K3(rho, nu, la)))
        results[(rho, nu, la)] = (lowest, c2, diff)
        coef_m1[(rho, nu, la)] = sp.expand(reduce38(d.get(-1, 0)))
        print(f'composante rho={rho} nu={nu} la={la}: plus basse puissance Om^{lowest}; '
              f'coeff Om^-2 - K3 = {diff}')
print('temps : %.0f s' % (time.time() - t0))

# affichage de quelques coefficients Om^-2 factorises
for key in [(0, 0, 1), (1, 0, 1), (2, 0, 1), (1, 1, 2), (3, 2, 3)]:
    print('coeff Om^-2', key, ':', results[key][1])

# ---------- Q4 : coefficient de Om^-1 ----------
print('\n=== Q4 : coefficient de Om^-1 ===')
cond = m2 + 4 * lam * xi - 2 * lam / 3
allzero_cond = True
for key, c1 in coef_m1.items():
    c1_cond = sp.expand(c1.subs(m2, 2 * lam / 3 - 4 * lam * xi))
    if c1_cond != 0:
        allzero_cond = False
    print(key, ' valeur du coeff Om^-1 sous la condition =', sp.factor(c1_cond))
for key in [(0, 0, 1), (1, 0, 1), (2, 0, 1), (1, 1, 2)]:
    print('coeff Om^-1', key, ':', sp.factor(coef_m1[key]))
print('Le coefficient de Om^-1 s annule identiquement sous la condition :', allzero_cond)

# ---------- Variante "sur couche" : on remplace, dans le terme xi ghat_ab boxhat|H|^2,
# H^dagger boxhat_D H par l equation de Higgs (sans Yukawa) ----------
print('\n=== Variante : elimination de boxhat_D H par l equation de Higgs ===')
E = sp.expand(Hc * (boxhat_D(H) - (m2 + xi * Rhat + 2 * lh * H2) * H)
              + H * (boxhat_D(Hc, True) - (m2 + xi * Rhat + 2 * lh * H2) * Hc))   # = 0 sur couche
Ton = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        Ton[a, b] = sp.expand(Ttot[a, b] - 2 * xi * ghat[a, b] * E)
Ttr_on = sp.expand(sum(ghat_inv[a, b] * Ton[a, b] for a in idx for b in idx))
Lh_on = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        Lh_on[a, b] = sp.expand(kappa / 2 * (Ton[a, b] - Ttr_on * ghat[a, b] / 3) + lam / 6 * ghat[a, b])
def nabhatL_on(nu, la, rho):
    return D(Lh_on[la, rho], nu) - sum(Gam[c][nu][la] * Lh_on[c, rho] + Gam[c][nu][rho] * Lh_on[la, c] for c in idx)
for key in [(0, 0, 1), (1, 0, 1), (2, 1, 2)]:
    rho, nu, la = key
    rhs = sp.expand((nabhatL_on(nu, la, rho) - nabhatL_on(la, nu, rho)) / Om).subs(sub214)
    rhs = reduce38(rhs)
    d = laurent(rhs, 'on')
    c2 = reduce38(d.get(-2, 0))
    c1 = reduce38(d.get(-1, 0))
    ratio = sp.simplify(c2 / K3(rho, nu, la)) if K3(rho, nu, la) != 0 else None
    print(key, 'plus basse puissance', min(d), '; coeff Om^-2 / K3 =', ratio,
          '; coeff Om^-1 sous la condition =', sp.factor(sp.expand(c1.subs(m2, 2 * lam / 3 - 4 * lam * xi))))
print('temps total : %.0f s' % (time.time() - t0))

# ---------- Robustesse : substitution (2.14) et (3.8) a l ordre suivant ----------
print('\n=== Robustesse : (2.14) avec le terme (kappa/2) Om T*_ab et (3.8) avec (kappa/12) That ===')
Tstar = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        Tstar[a, b] = sp.expand(Ttot[a, b] - Ttr * ghat[a, b] / 4)
# partie d ordre Om^0 de T*_ab (suffisante : le reste est O(Om^2) dans (2.14) et O(Om^3) dans (3.8))
def part0(expr):
    return sp.Poly(sp.expand(expr), Om).coeff_monomial(1)
sub214b = {ddOm[t]: s * eta[t[0], t[1]] + kappa / 2 * Om * part0(Tstar[t[0], t[1]]) for t in ddOm}
for t in dddOm:
    a, b, c = t
    sub214b[dddOm[t]] = sub214[dddOm[t]]
tau0 = part0(sp.expand(Ttr / Om**2))
R38b = dOm[1]**2 + dOm[2]**2 + dOm[3]**2 + lam / 3 - 2 * Om * s - kappa / 12 * Om**2 * tau0
def reduce38b(expr):
    P = sp.Poly(sp.expand(expr), dOm[0])
    out = 0
    for (k,), coeff in P.terms():
        q, r = divmod(k, 2)
        out += coeff * R38b**q * dOm[0]**r
    return sp.expand(out)
for key in [(0, 0, 1), (1, 0, 1), (2, 1, 2), (3, 1, 3)]:
    rho, nu, la = key
    rhs = sp.expand((nabhatL(nu, la, rho) - nabhatL(la, nu, rho)) / Om).subs(sub214b)
    rhs = reduce38b(reduce38b(rhs))
    d = laurent(rhs, 'b')
    c2 = sp.expand(reduce38b(d.get(-2, 0)) - K3(rho, nu, la))
    c1 = sp.expand(reduce38b(d.get(-1, 0)) - coef_m1[key])
    print(key, 'plus basse puissance', min(d), '; coeff Om^-2 inchange :', c2 == 0, '; coeff Om^-1 inchange :', c1 == 0)
print('temps total : %.0f s' % (time.time() - t0))
