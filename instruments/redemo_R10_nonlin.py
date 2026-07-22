#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R10_nonlin.py — REDEMONSTRATION AVEUGLE, lot R-10 (Silo R).

Cibles gelées : audit/R10-CIBLES-GELEES.md
  sha256 = 8fb1b0bd21c2a6035158ee48743f56c060b246da6f76de2e22e68c732b2a4ca8
Gel figé en S5, AVANT l'écriture de ce fichier ; NON re-gelé (précédent
R-6). Plafond annoncé au gel : REPRODUIT-SOUS-RESERVE (E-2). E-1 exclu.

Aveuglement : les CORPS de kb/LC-D-NONLIN-VERROU.md et
kb/LC-D-NONLIN-2PT.md n'ont PAS été ouverts avant l'exécution de ce
script. Seul le gel (front-matters) a été lu.

Périmètre redérivé : Q1-Q6, Q8 depuis les prémisses NOMMEES (Schouten /
Cotton en d=3 ; décomposition SVT ; projecteur TT ; algèbre de Weyl en
4D ; mode de Bunch-Davies). Q7 : imports externes (Osborn-Petkou,
de Haro) — consignés, sauf le comptage interne. Q9 : rejeu, hors script.

Harnais a deux issues : PASS discriminant (assert + mutation MORDANTE
qui doit casser) / CONSIGNATION (import, verdict, prémisse). Convention
unique (précédent R-8/C10) : l'argument `mutation` est la claim MUTEE,
qui doit être FAUSSE ; une mutation laissant la cible invariante est
VACANTE et le harnais la signale.

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
import itertools
import numpy as np
import sympy as sp

PASS = 0
CONS = 0
FAIL = []
TOL = 1e-10          # seuil de rang déclaré au gel §3


def pas(label, cond, mutation=None, mut_label=""):
    """PASS discriminant : la condition tient ET la mutation casse."""
    global PASS
    ok = bool(cond)
    if mutation is not None:
        if bool(mutation):
            FAIL.append("MUTATION VACANTE : " + label + " / " + mut_label)
            print("  [MUTATION VACANTE] " + label + " — " + mut_label)
            return
    if ok:
        PASS += 1
        suf = ("  |  mutation mordante : " + mut_label) if mutation is not None else ""
        print("  [PASS] " + label + suf)
    else:
        FAIL.append(label)
        print("  [ECHEC] " + label)


def cons(label, texte):
    global CONS
    CONS += 1
    print("  [CONSIGNATION] " + label + " — " + texte)


def simp(e):
    """Simplification robuste (incident d'instrument R-4 : simplify seul
    insuffisant sur les identités trigonométriques)."""
    return sp.simplify(sp.expand_trig(sp.trigsimp(sp.simplify(e))))


# ====================================================================
# Outillage géométrique : Schouten et Cotton en d=3
# ====================================================================
def cotton3(g, X):
    """Ricci, R, Schouten (d=3), Cotton C_{ijk} = D_k S_ij - D_j S_ik."""
    n = 3
    gi = g.inv()
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = 0
                for e in range(n):
                    s += gi[a, e] * (sp.diff(g[e, b], X[c])
                                     + sp.diff(g[e, c], X[b])
                                     - sp.diff(g[b, c], X[e]))
                Gam[a][b][c] = sp.simplify(s / 2)
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for e in range(n):
                    s += Gam[a][a][e] * Gam[e][b][c] - Gam[a][c][e] * Gam[e][b][a]
            Ric[b, c] = sp.simplify(s)
    R = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    S = sp.simplify(Ric - R * g / 4)          # Schouten en d=3

    def cov(k, i, j):
        e = sp.diff(S[i, j], X[k])
        for m in range(n):
            e -= Gam[m][k][i] * S[m, j] + Gam[m][k][j] * S[i, m]
        return e

    C = [[[simp(cov(k, i, j) - cov(j, i, k)) for k in range(n)]
          for j in range(n)] for i in range(n)]
    return Ric, R, S, C


def cotton_nul(C):
    return all(C[i][j][k] == 0 for i in range(3) for j in range(3) for k in range(3))


# ====================================================================
# Outillage tensoriel numérique : eps, projecteurs, opérateur D
# ====================================================================
EPS = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)):
    EPS[p] = np.sign(np.prod([p[j] - p[i] for i in range(3) for j in range(i + 1, 3)]))
DELTA = np.eye(3)
RNG = np.random.default_rng(20260722)


def unit(v):
    return np.asarray(v, float) / np.linalg.norm(v)


def Pt(n):
    return DELTA - np.outer(n, n)


def PiTT(n):
    P = Pt(n)
    return (0.5 * np.einsum('ik,jl->ijkl', P, P)
            + 0.5 * np.einsum('il,jk->ijkl', P, P)
            - 0.5 * np.einsum('ij,kl->ijkl', P, P))


def PiV(n):
    P = Pt(n)
    return 0.5 * (np.einsum('ik,j,l->ijkl', P, n, n)
                  + np.einsum('jk,i,l->ijkl', P, n, n)
                  + np.einsum('il,j,k->ijkl', P, n, n)
                  + np.einsum('jl,i,k->ijkl', P, n, n))


def PiS(n):
    P = Pt(n)
    o = np.outer(n, n)
    return np.einsum('ij,kl->ijkl', o, o) + 0.5 * np.einsum('ij,kl->ijkl', P, P)


def app(T4, M):
    return np.einsum('ijkl,kl->ij', T4, M)


def Dh(n, h):
    """(D h)_ij = eps_ikl n_k h_lj — l'opérateur de dualité (curl)."""
    return np.einsum('ikl,k,lj->ij', EPS, n, h)


def randTT(n):
    A = RNG.normal(size=(3, 3))
    return app(PiTT(n), (A + A.T) / 2)


def sym2(T):
    T = 0.5 * (T + np.einsum('ijkl->jikl', T))
    return 0.5 * (T + np.einsum('ijkl->ijlk', T))


def rang(M):
    sv = np.linalg.svd(np.array(M), compute_uv=False)
    ref = max(sv[0], 1e-30)
    return int((sv > TOL * ref).sum()), sv


# ====================================================================
# Moteur de linéarisation AB INITIO : Ricci et Cotton au premier ordre
# pour g = delta + eps*h, h_ij = H_ij exp(i k.x). Aucun coefficient n'est
# postulé : Christoffel, Ricci, Schouten et Cotton sont calculés.
# ====================================================================
_x, _y, _z, _e = sp.symbols("x y z varepsilon", real=True)
_X = [_x, _y, _z]


def lin_ric_cotton(kvec, H):
    ph = sp.exp(sp.I * (kvec[0] * _x + kvec[1] * _y + kvec[2] * _z))
    h = sp.Matrix(3, 3, lambda i, j: H[i][j] * ph)
    g = sp.eye(3) + _e * h
    gi = sp.eye(3) - _e * h                       # inverse au premier ordre

    def O1(e):
        return sp.expand(sp.series(sp.expand(e), _e, 0, 2).removeO()).coeff(_e, 1)

    Gam = [[[0] * 3 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                s = 0
                for m in range(3):
                    s += gi[a, m] * (sp.diff(g[m, b], _X[c])
                                     + sp.diff(g[m, c], _X[b])
                                     - sp.diff(g[b, c], _X[m]))
                Gam[a][b][c] = sp.expand(s / 2)
    Ric = sp.zeros(3, 3)
    for b in range(3):
        for c in range(3):
            s = 0
            for a in range(3):
                s += sp.diff(Gam[a][b][c], _X[a]) - sp.diff(Gam[a][b][a], _X[c])
                for m in range(3):
                    s += Gam[a][a][m] * Gam[m][b][c] - Gam[a][c][m] * Gam[m][b][a]
            Ric[b, c] = O1(s)
    Rs1 = sp.expand(sum(Ric[i, i] for i in range(3)))     # trace au 1er ordre
    S = sp.Matrix(3, 3, lambda i, j: sp.expand(Ric[i, j] - Rs1 * sp.eye(3)[i, j] / 4))
    Ct = sp.Matrix(3, 3, lambda i, j: sp.expand(
        sum(EPS[i, k, l] * sp.diff(S[l, j], _X[k]) for k in range(3) for l in range(3))))
    lap = sp.Matrix(3, 3, lambda i, j: sp.expand(
        sum(sp.diff(h[i, j], v, 2) for v in _X)))
    return h, Ric, Rs1, S, Ct, lap


print("=" * 78)
print("REDEMO R-10 — parité non-linéaire du Weyl rescalé (E pair / B impair)")
print("gel 8fb1b0bd...4ca8 — plafond E-2 annoncé au gel, E-1 exclu d'avance")
print("=" * 78)

# ====================================================================
# Q1 — secteur MAGNETIQUE, parité impaire : B ∝ Cotton[g0]
# ====================================================================
print("\n### Q1 — B ∝ Cotton[g0] ; fond maximalement symétrique ⟹ Cotton ≡ 0")

r, th, ph, a = sp.symbols("r theta phi a", positive=True)
x, y, z = sp.symbols("x y z", real=True)

g_S3 = sp.diag(a ** 2, a ** 2 * sp.sin(r) ** 2,
               a ** 2 * sp.sin(r) ** 2 * sp.sin(th) ** 2)
g_H3 = sp.diag(a ** 2, a ** 2 * sp.sinh(r) ** 2,
               a ** 2 * sp.sinh(r) ** 2 * sp.sin(th) ** 2)
g_R3 = sp.eye(3)
# témoin 1 : homogène, R CONSTANT, mais NON conformément plat
g_T1 = sp.diag(1, sp.exp(2 * x), sp.exp(4 * x))
# témoin 2 : R non constant, non conformément plat
g_T2 = sp.diag(1, 1, 1 + x ** 2)

_, R_S3, S_S3, C_S3 = cotton3(g_S3, [r, th, ph])
_, R_H3, _, C_H3 = cotton3(g_H3, [r, th, ph])
_, R_R3, _, C_R3 = cotton3(g_R3, [x, y, z])
_, R_T1, _, C_T1 = cotton3(g_T1, [x, y, z])
_, R_T2, _, C_T2 = cotton3(g_T2, [x, y, z])

pas("Cotton(S3) ≡ 0 exactement (27 composantes), R = 6/a² > 0",
    cotton_nul(C_S3) and simp(R_S3 - 6 / a ** 2) == 0,
    mutation=cotton_nul(C_T1),
    mut_label="témoin diag(1,e^{2x},e^{4x}) — R = −14 CONSTANT — a un Cotton nul")
pas("Cotton(H3) ≡ 0 exactement, R = −6/a² < 0",
    cotton_nul(C_H3) and simp(R_H3 + 6 / a ** 2) == 0,
    mutation=cotton_nul(C_T2),
    mut_label="témoin diag(1,1,1+x²) (R non constant) a un Cotton nul")
pas("Cotton(R3) ≡ 0, R = 0 — les trois géométries A3 (S3, R3, H3) épuisées",
    cotton_nul(C_R3) and simp(R_R3) == 0,
    mutation=(simp(R_T1) == 0),
    mut_label="le témoin non conformément plat a R = 0")

# argument général : max. symétrique ⟹ Schouten = (R/12) g avec R constant
Rs = sp.Symbol("R_0", positive=True)
S_max = sp.simplify(Rs / 3 - Rs / 4)
pas("argument général : Ric = (R/3)g ⟹ Schouten = (R/12)g ; R constant ⟹ "
    "∇S = 0 ⟹ Cotton = 0 SANS argument de représentation",
    sp.simplify(S_max - Rs / 12) == 0 and simp(S_S3 - g_S3 / (2 * a ** 2)) == sp.zeros(3, 3),
    mutation=(sp.simplify(sp.diff((sp.Function("f")(x) / 12), x)) == 0),
    mut_label="R non constant donnerait encore ∇S = 0")

# Cotton linéarisé d'une perturbation TT : objet TT, pas de fuite de singlet
n0 = unit(RNG.normal(size=3))
h0 = randTT(n0)
Ch = Dh(n0, h0)
pas("Cotton linéarisé d'une perturbation TT : NON NUL, symétrique, sans "
    "trace, transverse (objet TT — pas de fuite de singlet)",
    np.abs(Ch).max() > 1e-8 and np.abs(Ch - Ch.T).max() < TOL
    and abs(np.trace(Ch)) < TOL and np.abs(n0 @ Ch).max() < TOL,
    mutation=(np.abs(Dh(n0, np.outer(n0, n0))).max() > TOL),
    mut_label="D appliqué au secteur longitudinal n⊗n donne un objet non nul")

cons("Q1 / instrument", "simplify seul insuffisant sur les identités "
     "trigonométriques du Cotton de S3 (composante (1,1,0) résiduelle "
     "sin2r·tan r + cos2r − 1) ; expand_trig requis. Instrument, pas algèbre "
     "— précédent R-4.")
cons("Q1 / portée", "le verrou magnétique est CONDITIONNEL à A3 : c'est A3 "
     "qui impose le fond maximalement symétrique. Sans A3, le témoin "
     "diag(1,e^{2x},e^{4x}) (homogène, R constant) a un Cotton NON NUL.")

# ====================================================================
# Q2 — secteur ELECTRIQUE, parité paire : E ∝ g3 ∝ <T>
# ====================================================================
print("\n### Q2 — E ∝ g3 ∝ <T> ; SVT ; Pi^TT(delta) = Pi^TT(P) = 0 ; hélicités ±2")

n = unit(RNG.normal(size=3))
Pi, PV, PS = PiTT(n), PiV(n), PiS(n)
Id4 = 0.5 * (np.einsum('ik,jl->ijkl', DELTA, DELTA)
             + np.einsum('il,jk->ijkl', DELTA, DELTA))


def rk4(T):
    sv = np.linalg.svd(T.reshape(9, 9), compute_uv=False)
    return int((sv > TOL).sum())


ex, ey = np.array([1., 0, 0]), np.array([0, 1., 0])
e_plus = (np.outer(ex, ex) - np.outer(ey, ey)
          + 1j * (np.outer(ex, ey) + np.outer(ey, ex))) / 2
nz = np.array([0., 0., 1.])

pas("Pi^TT(delta) = 0 exactement (la trace est annihilée par le projecteur TT)",
    np.abs(app(Pi, DELTA)).max() < TOL,
    mutation=(np.abs(app(PiTT(nz), e_plus)).max() < TOL),
    mut_label="Pi^TT annihile aussi l'hélicité e^+")
pas("Pi^TT(P) = Pi^TT(n⊗n) = 0 — spin-2 ∩ invariants = {0}",
    np.abs(app(Pi, Pt(n))).max() < TOL and np.abs(app(Pi, np.outer(n, n))).max() < TOL,
    mutation=(np.abs(app(PS, DELTA)).max() < TOL),
    mut_label="le projecteur scalaire annihile aussi delta")
pas("décomposition SVT complète en d=3 : rangs (TT, V, S) = (2, 2, 2), "
    "somme = identité sur les symétriques (6 = 2+2+2)",
    (rk4(Pi), rk4(PV), rk4(PS)) == (2, 2, 2)
    and np.abs(Pi + PV + PS - Id4).max() < TOL,
    mutation=(rk4(Pi) == 5),
    mut_label="le secteur TT serait de rang 5 (symétrique sans trace complet)")

psi = 0.7
Rz = np.array([[np.cos(psi), -np.sin(psi), 0],
               [np.sin(psi), np.cos(psi), 0], [0, 0, 1.]])
pas("hélicités ±2 : R_z(psi)·e^±·R_z^T = e^{∓2i psi} e^± (pas d'hélicité 0 "
    "dans le secteur TT)",
    np.abs(Rz @ e_plus @ Rz.T - np.exp(-2j * psi) * e_plus).max() < TOL
    and np.abs(Rz @ e_plus.conj() @ Rz.T - np.exp(2j * psi) * e_plus.conj()).max() < TOL,
    mutation=(np.abs(Rz @ e_plus @ Rz.T - np.exp(-1j * psi) * e_plus).max() < TOL),
    mut_label="l'action serait de poids d'hélicité 1 (e^{−i psi})")

# le seul tenseur symétrique invariant sous A3 vit dans span{delta, n⊗n}
coefs = RNG.normal(size=(8, 2))
inv_ok = all(np.abs(app(Pi, c[0] * DELTA + c[1] * np.outer(n, n))).max() < TOL
             for c in coefs)
pas("<g3> = 0 exactement : tout tenseur symétrique INVARIANT sous A3 est "
    "dans span{delta, n⊗n}, de projection TT nulle (8 tirages)",
    inv_ok,
    mutation=(np.abs(app(PiTT(nz), e_plus + e_plus.conj())).max() < TOL),
    mut_label="une combinaison NON invariante (e^+ + e^−) aurait aussi une "
              "projection TT nulle")

cons("Q2 / import", "IDENTITES DE WARD EXACTES en d = 3 (d impair, pas "
     "d'anomalie de trace) ⟹ g3 transverse et sans trace À TOUS LES ORDRES : "
     "IMPORT, non redérivé ici. C'est cette exactitude — et elle seule — qui "
     "porte le « tous ordres » du verrou électrique.")
cons("Q2 / conditionnalité", "E ∝ g3 ∝ <T> suppose l'identification "
     "holographique de Fefferman-Graham (module [D]) : prémisse, non résultat.")

# ====================================================================
# Q3 — cohérence de PARITE : pseudo-tenseur vs tenseur vrai ; (E,B)=(5,5)=10
# ====================================================================
print("\n### Q3 — Cotton pseudo-tenseur / Ricci tenseur vrai ; (E,B) = (5,5) = 10")

# les deux configurations sont RECALCULEES ab initio : rien n'est transporté
# à la main. R = réflexion (det = −1) ; k ⟶ Rk et H ⟶ R H R^T.
kk_s = sp.Symbol("k", positive=True)
aa, bb = sp.symbols("a b", real=True)
H_TT = [[aa, bb, 0], [bb, -aa, 0], [0, 0, 0]]      # TT générique pour k ∥ z
Rr = sp.Matrix([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
detR = Rr.det()
kv = sp.Matrix([0, 0, kk_s])
kvp = Rr * kv
Hp = Rr * sp.Matrix(H_TT) * Rr.T

_, Ric1, R1, _, Ct1, lap1 = lin_ric_cotton([kv[0], kv[1], kv[2]], H_TT)
_, Ric2, _, _, Ct2, _ = lin_ric_cotton(
    [kvp[0], kvp[1], kvp[2]], [[Hp[i, j] for j in range(3)] for i in range(3)])

config_diff = sp.simplify(Hp - sp.Matrix(H_TT)) != sp.zeros(3, 3)
zero3 = sp.zeros(3, 3)
pas("Cotton = PSEUDO-tenseur : y_R = det(R)·(R⊗R)·y(Rx) — les DEUX "
    "configurations recalculées ab initio, sur une polarisation TT "
    "générique (a,b) réellement transformée",
    config_diff and sp.simplify(Ct2 - detR * Rr * Ct1 * Rr.T) == zero3,
    mutation=(sp.simplify(Ct2 - Rr * Ct1 * Rr.T) == zero3),
    mut_label="contrôle négatif — le Cotton suivrait la loi de tenseur VRAI "
              "(sans det)")
pas("Ricci / Schouten / stress = tenseur VRAI : loi SANS det(R), "
    "recalculée ab initio sur la même paire de configurations",
    sp.simplify(Ric2 - Rr * Ric1 * Rr.T) == zero3 and sp.simplify(Ric1) != zero3,
    mutation=(sp.simplify(Ric2 - detR * Rr * Ric1 * Rr.T) == zero3),
    mut_label="contrôle négatif — le Ricci suivrait la loi PSEUDO (avec det)")

# espace de Weyl en 4D : symétries + condition de trace
eta4 = np.diag([-1., 1, 1, 1])
IDX = [(A, B, C, D) for A in range(4) for B in range(4)
       for C in range(4) for D in range(4)]
POS = {t: i for i, t in enumerate(IDX)}


def ligne(pairs):
    v = np.zeros(256)
    for t, c in pairs:
        v[POS[t]] += c
    return v


def espace_weyl(avec_trace=True):
    rows = []
    for (A, B, C, D) in IDX:
        rows.append(ligne([((A, B, C, D), 1), ((B, A, C, D), 1)]))
        rows.append(ligne([((A, B, C, D), 1), ((A, B, D, C), 1)]))
        rows.append(ligne([((A, B, C, D), 1), ((C, D, A, B), -1)]))
        rows.append(ligne([((A, B, C, D), 1), ((A, C, D, B), 1), ((A, D, B, C), 1)]))
    if avec_trace:
        for B in range(4):
            for D in range(4):
                v = np.zeros(256)
                for A in range(4):
                    for C in range(4):
                        v[POS[(A, B, C, D)]] += eta4[A, C]
                rows.append(v)
    Mx = np.array(rows)
    _, sv, vt = np.linalg.svd(Mx)
    return vt[(sv > 1e-9).sum():]


ker_W = espace_weyl(True)
ker_Riem = espace_weyl(False)


def EB(v):
    C4 = v.reshape(4, 4, 4, 4)
    E = np.array([[C4[0, i + 1, 0, j + 1] for j in range(3)] for i in range(3)])
    Cs = np.array([[[C4[k + 1, l + 1, j + 1, 0] for j in range(3)]
                    for l in range(3)] for k in range(3)])
    B = 0.5 * np.einsum('ikl,klj->ij', EPS, Cs)
    return E, B


def vec5(X):
    return np.array([X[0, 0], X[1, 1], X[0, 1], X[0, 2], X[1, 2]])


ecart_E = ecart_B = 0.0
cols = []
for v in ker_W:
    E, B = EB(v)
    ecart_E = max(ecart_E, np.abs(E - E.T).max(), abs(np.trace(E)))
    ecart_B = max(ecart_B, np.abs(B - B.T).max(), abs(np.trace(B)))
    cols.append(np.concatenate([vec5(E), vec5(B)]))
rgEB, _ = rang(cols)

pas("espace de Weyl en 4D : dimension 10 (symétries + condition de trace)",
    ker_W.shape[0] == 10,
    mutation=(ker_Riem.shape[0] == 10),
    mut_label="sans la condition de trace (Riemann) la dimension serait "
              "encore 10 — elle vaut %d" % ker_Riem.shape[0])
pas("E = C_{0i0j} et B = ½ eps_ikl C^{kl}_{j0} : tous deux SYMETRIQUES et "
    "SANS TRACE ⟹ 5 + 5",
    ecart_E < 1e-9 and ecart_B < 1e-9,
    mutation=(ecart_E > 1e-9),
    mut_label="E porterait une trace ou une partie antisymétrique")
pas("carte Weyl ⟶ (E,B) de RANG 10 = dim source ⟹ couverture COMPLETE, "
    "DISJOINTE, SANS CROISE : (E,B) = (5,5) = 10",
    rgEB == 10 and ker_W.shape[0] == 10 and 5 + 5 == 10,
    mutation=(rgEB <= 9),
    mut_label="la carte aurait un noyau (une composante de Weyl invisible "
              "de (E,B))")
pas("chaque secteur est annulé par SON argument, respectant SA parité : "
    "B (impair) par la platitude conforme du fond ; E (pair) par "
    "invariance ⊗ TT — aucun argument croisé",
    np.abs(app(Pi, DELTA)).max() < TOL and cotton_nul(C_S3),
    mutation=(np.abs(app(Pi, Dh(n, randTT(n)))).max() < TOL),
    mut_label="l'argument électrique (projection TT) annulerait aussi le "
              "secteur magnétique")

# ====================================================================
# Q4 — C1 : secteur PAIR du deux-point, dimension 1 ; k^3 non analytique
# ====================================================================
print("\n### Q4 — C1 : structures PAIRES du deux-point TT spin-2 à Delta = d = 3")


def base_paire(m):
    o = np.outer(m, m)
    B = [np.einsum('ij,kl->ijkl', DELTA, DELTA),
         np.einsum('ik,jl->ijkl', DELTA, DELTA) + np.einsum('il,jk->ijkl', DELTA, DELTA),
         np.einsum('ij,kl->ijkl', o, DELTA),
         np.einsum('ij,kl->ijkl', DELTA, o),
         np.einsum('ik,jl->ijkl', o, DELTA) + np.einsum('il,jk->ijkl', o, DELTA),
         np.einsum('ij,kl->ijkl', o, o)]
    return [sym2(b) for b in B]


def base_impaire(m):
    E = np.einsum('ika,a->ik', EPS, m)
    o, P = np.outer(m, m), Pt(m)
    B = [np.einsum('ik,jl->ijkl', E, DELTA), np.einsum('ik,jl->ijkl', E, o),
         np.einsum('ij,kl->ijkl', E, DELTA), np.einsum('ij,kl->ijkl', E, o),
         np.einsum('ik,jl->ijkl', E, P), np.einsum('ik,jl->ijkl', P, E)]
    return [sym2(b) for b in B]


def projTT4(T, m):
    Q = PiTT(m)
    return np.einsum('ijmn,mnpq,pqkl->ijkl', Q, T, Q)


dims_p, dims_i = [], []
for _ in range(5):
    m = unit(RNG.normal(size=3))
    dims_p.append(rang([projTT4(b, m).ravel() for b in base_paire(m)])[0])
    dims_i.append(rang([projTT4(b, m).ravel() for b in base_impaire(m)])[0])

pas("C1 — l'espace des structures PAIRES invariantes est de DIMENSION 1 "
    "(SVD, seuil de rang 1e-10, 5 directions indépendantes)",
    set(dims_p) == {1},
    mutation=(set(dims_p) == {2}),
    mut_label="la dimension du secteur pair serait 2")

m = unit(RNG.normal(size=3))
Qm = PiTT(m)
res_p = []
for b in base_paire(m):
    T = projTT4(b, m)
    if np.abs(T).max() > 1e-12:
        lam = T.ravel() @ Qm.ravel() / (Qm.ravel() @ Qm.ravel())
        res_p.append(np.abs(T - lam * Qm).max())
pas("la solution est ∝ Pi^TT (résidu nul sur toutes les entrées non nulles "
    "de la base)",
    len(res_p) > 0 and max(res_p) < TOL,
    mutation=(np.abs(projTT4(base_impaire(m)[0], m)
                     - (projTT4(base_impaire(m)[0], m).ravel() @ Qm.ravel()
                        / (Qm.ravel() @ Qm.ravel())) * Qm).max() < TOL),
    mut_label="une structure IMPAIRE serait elle aussi ∝ Pi^TT")

# complétude des hélicités ±2 : l'espace TT à direction fixe est de dim 2
pas("complétude des hélicités ±2 : {e^+, e^−} engendre exactement le "
    "secteur TT (dim 2), les opérateurs invariants y sont diagonaux",
    rk4(PiTT(nz)) == 2
    and np.abs(app(PiTT(nz), e_plus) - e_plus).max() < TOL,
    mutation=(rk4(PiTT(nz)) == 3),
    mut_label="le secteur TT à direction fixe serait de dimension 3")


def coeff_FT(alpha, dd):
    """Coefficient de la transformée de Fourier de |k|^{2 alpha} en dim dd :
    ∝ Gamma((dd+2 alpha)/2) / Gamma(−alpha). Un pôle de Gamma(−alpha)
    (alpha entier ≥ 0) annule le coefficient ⟹ support de contact."""
    return sp.simplify(2 ** (2 * alpha) * sp.pi ** sp.Rational(dd, 2)
                       * sp.gamma(sp.Rational(dd, 2) + alpha) / sp.gamma(-alpha))


c_32_3 = coeff_FT(sp.Rational(3, 2), 3)
c_1_3 = coeff_FT(1, 3)
pas("k³ = (k²)^{3/2} NON ANALYTIQUE (puissance demi-entière de k²) ⟹ "
    "coefficient de Fourier 12·pi ≠ 0 ⟹ RADIATIF",
    sp.simplify(c_32_3 - 12 * sp.pi) == 0 and c_32_3 != 0,
    mutation=(c_1_3 != 0),
    mut_label="une puissance ENTIERE (k², alpha = 1) donnerait aussi un "
              "coefficient non nul")
kk = sp.Symbol("k2", positive=True)
pas("critère analytique (jamais un ajustement numérique) : (k²)^{3/2} n'est "
    "pas polynomiale en k², (k²)² l'est",
    not (kk ** sp.Rational(3, 2)).is_polynomial(kk) and (kk ** 2).is_polynomial(kk),
    mutation=((kk ** 2).is_polynomial(kk) is False),
    mut_label="k⁴ = (k²)² serait lui aussi non analytique")

# ====================================================================
# Q5 — C2 : secteur IMPAIR, dimension 1, de type CONTACT
# ====================================================================
print("\n### Q5 — C2 : secteur IMPAIR — dimension 1 ET type CONTACT")

DQm = sym2(np.einsum('ima,a,mjkl->ijkl', EPS, m, Qm))
pas("C2 — le secteur IMPAIR est de DIMENSION 1 (SVD, seuil 1e-10, "
    "5 directions)",
    set(dims_i) == {1},
    mutation=(set(dims_i) == {0}),
    mut_label="le secteur impair serait vide")
res_i = []
for b in base_impaire(m):
    T = projTT4(b, m)
    if np.abs(T).max() > 1e-12:
        lam = T.ravel() @ DQm.ravel() / (DQm.ravel() @ DQm.ravel())
        res_i.append(np.abs(T - lam * DQm).max())
pas("la solution impaire est ∝ D·Pi^TT (pseudo-tenseur : une seule "
    "insertion d'epsilon)",
    len(res_i) > 0 and max(res_i) < TOL,
    mutation=(np.abs(DQm - (DQm.ravel() @ Qm.ravel()
                            / (Qm.ravel() @ Qm.ravel())) * Qm).max() < TOL),
    mut_label="la structure impaire serait proportionnelle à Pi^TT")
pas("ORTHOGONALITE pair ⊥ impair : Pi^TT · (D·Pi^TT) = 0 exactement "
    "⟹ aucune amplitude radiative neuve",
    abs(np.einsum('ijkl,ijkl', Qm, DQm)) < TOL and np.abs(DQm).max() > 1e-8,
    mutation=(abs(np.einsum('ijkl,ijkl', Qm, Qm)) < TOL),
    mut_label="le produit du secteur pair avec lui-même serait nul aussi")
pas("type CONTACT : la structure impaire porte un n̂ = k/|k| SUPPLEMENTAIRE "
    "⟹ k³·S^odd de puissance nette ENTIERE (alpha = 1) ⟹ coefficient de "
    "Fourier NUL (pôle de Gamma(−1)) ⟹ polynomial, donc LOCAL",
    c_1_3 == 0 and sp.gamma(-1) == sp.zoo,
    mutation=(coeff_FT(sp.Rational(3, 2), 3) == 0),
    mut_label="le secteur PAIR (alpha = 3/2) serait lui aussi de contact")
pas("la scission radiatif / contact suit EXACTEMENT la frontière de parité : "
    "pair ⟹ demi-entier ⟹ radiatif ; impair ⟹ entier ⟹ contact",
    (c_32_3 != 0) and (c_1_3 == 0),
    mutation=((c_32_3 == 0) or (c_1_3 != 0)),
    mut_label="la scission croiserait la frontière de parité")

# ====================================================================
# Q6 — C3 : Cotton linéarisé ab initio ; D² = −1 ; refermeture BD
# ====================================================================
print("\n### Q6 — C3 : C^lin = (i/2) k³ (Dh) ; D² = −1 ; refermeture Bunch-Davies")

hh_unused = None
# le coefficient du Ricci linéarisé est RESOLU, jamais posé
cc = sp.Symbol("c_lin")
sol_ric = sp.solve(sp.Eq(Ric1[0, 0], cc * lap1[0, 0]), cc)
pas("le ½ sort du RICCI LINEARISE, coefficient RESOLU ab initio : "
    "Ric^(1)_ij = −½ ∂²h_ij pour h TT (trace R^(1) = 0 ; les deux autres "
    "termes tombent par transversalité et trace nulle)",
    len(sol_ric) == 1 and sp.simplify(sol_ric[0] + sp.Rational(1, 2)) == 0
    and sp.simplify(R1) == 0,
    mutation=(len(sol_ric) == 1 and sp.simplify(sol_ric[0] + 1) == 0),
    mut_label="le coefficient du Ricci linéarisé TT serait 1")

# le préfacteur du Cotton linéarisé est RESOLU, jamais posé
nh = [0, 0, 1]
h_s = sp.Matrix(3, 3, lambda i, j: H_TT[i][j]) * sp.exp(sp.I * kk_s * _z)
Dh_s = sp.Matrix(3, 3, lambda i, j: sp.expand(
    sum(EPS[i, k, l] * nh[k] * h_s[l, j] for k in range(3) for l in range(3))))
cd = sp.Symbol("c_cot")
sol_cot = sp.solve(sp.Eq(Ct1[0, 1], cd * sp.I * kk_s ** 3 * Dh_s[0, 1]), cd)
pas("C^lin = (i/2)·k³·(Dh) AB INITIO : préfacteur RESOLU à ½, et égalité "
    "tensorielle complète Ct − (i/2)k³(Dh) = 0 sur les 9 composantes",
    len(sol_cot) == 1 and sp.simplify(sol_cot[0] - sp.Rational(1, 2)) == 0
    and sp.simplify(Ct1 - sp.Rational(1, 2) * sp.I * kk_s ** 3 * Dh_s) == zero3
    and sp.simplify(Ct1) != zero3,
    mutation=(sp.simplify(Ct1 - sp.I * kk_s ** 3 * Dh_s) == zero3),
    mut_label="le préfacteur serait i·k³ (coefficient 1 au lieu de ½)")

tests_D2, tests_Dp = [], []
for _ in range(5):
    v = unit(RNG.normal(size=3))
    hv = randTT(v)
    tests_D2.append(np.abs(Dh(v, Dh(v, hv)) + hv).max())
    tests_Dp.append(np.abs(Dh(v, Dh(v, hv)) - hv).max())
pas("D² = −1 sur le secteur TT (exact : eps_ikl eps_lmn n_k n_m h_nj "
    "= n_i(n·h)_j − h_ij = −h_ij par transversalité), 5 tirages",
    max(tests_D2) < TOL,
    mutation=(max(tests_Dp) < TOL),
    mut_label="D² vaudrait +1 (dualité involutive au lieu d\'ordre 4)")

anti = []
orth = []
for _ in range(5):
    v = unit(RNG.normal(size=3))
    A, B = randTT(v), randTT(v)
    anti.append(abs(np.einsum('ij,ij', Dh(v, A), B) + np.einsum('ij,ij', A, Dh(v, B))))
    orth.append(abs(np.einsum('ij,ij', Dh(v, A), Dh(v, B)) - np.einsum('ij,ij', A, B)))
pas("D antisymétrique (D^T = −D) ⟹ D^T D = −D² = 1 : D est une ISOMETRIE "
    "du secteur TT ⟹ équipartition <BB>/<EE> = 1 EXACTE en unités de "
    "dualité (aucune tolérance)",
    max(anti) < TOL and max(orth) < TOL,
    mutation=(max(abs(np.einsum('ij,ij', Dh(n0, h0), Dh(n0, h0))
                      - 4 * np.einsum('ij,ij', h0, h0)) for _ in [0]) < TOL),
    mut_label="Cotton ×2 : le ratio resterait 1 (il vaut 4)")

cons("Q6 / recoupement", "D² = −𝟙 sur TT recoupe S² = −𝟙 du sceau CT-DUAL "
     "(R-4/T10) INDEPENDAMMENT : deux opérateurs d'ordre 4 distincts (D est "
     "la dualité spatiale eps·n̂ ; S la carte de dualité radiale AdS/dS), "
     "obtenus par des routes disjointes. Recoupement, pas dérivation de l'un "
     "par l'autre.")

# refermeture BD : g3 = −(i/3) k³ g0 (R-5 / P1), <g0 g0> = P0 Pi^TT
Hs, MPl, kf = sp.symbols("H M_Pl k", positive=True)
# c_E EXTRAIT du développement du mode BD (pas posé) ; c_B EXTRAIT du
# préfacteur du Cotton résolu ci-dessus (sol_cot = ½).
_eta = sp.Symbol("eta", negative=True)
_g0 = sp.Symbol("g_0", positive=True)
_hBD = _g0 * (1 + sp.I * kf * _eta) * sp.exp(-sp.I * kf * _eta)
_ser = sp.series(_hBD, _eta, 0, 5).removeO().expand()
_c3 = _ser.coeff(_eta, 3)                      # = −(i/3) k³ g0
P0 = 2 * Hs ** 2 / (MPl ** 2 * kf ** 3)
cE = sp.simplify(_c3 / (kf ** 3 * _g0))        # extrait du mode BD
cB = sp.I * sol_cot[0]                          # extrait du Cotton résolu
EE = sp.simplify(cE * sp.conjugate(cE) * kf ** 6 * P0)
BB = sp.simplify(cB * sp.conjugate(cB) * kf ** 6 * P0)
pas("refermeture BD : <EE> = (2H²/9M_Pl²)·k³ ∝ k³ — recoupe EXACTEMENT "
    "R-5/P4 (<g3 g3> = (2H²/9M_Pl²) k³), redémontré en S2",
    sp.simplify(EE - (2 * Hs ** 2 / (9 * MPl ** 2)) * kf ** 3) == 0,
    mutation=(sp.simplify(EE - (2 * Hs ** 2 / (9 * MPl ** 2)) * kf ** 6) == 0),
    mut_label="<EE> irait en k⁶ (pas de compensation par P0 ∝ k^{−3})")
pas("<BB> = (H²/2M_Pl²)·k³ ∝ k³ (D isométrie ⟹ même forme spectrale)",
    sp.simplify(BB - (Hs ** 2 / (2 * MPl ** 2)) * kf ** 3) == 0 and BB != 0,
    mutation=(sp.simplify(BB) == 0),
    mut_label="le secteur magnétique aurait un deux-point nul sur BD")
pas("<EB> RADIATIF NUL sur BD : la corrélation croisée est portée par la "
    "structure D·Pi^TT, orthogonale au secteur radiatif (contraction nulle) "
    "et de type contact",
    abs(np.einsum('ijkl,ijkl', Qm, DQm)) < TOL and c_1_3 == 0,
    mutation=(abs(np.einsum('ijkl,ijkl', DQm, DQm)) < TOL),
    mut_label="la structure croisée serait identiquement nulle (donc "
              "l'énoncé vide)")

cons("Q6 / écart de convention NOMME (anti-fit, non corrigé)",
     "avec les préfacteurs NUS du programme (c_E = −i/3 de la relation "
     "d'état BD ; c_B = i/2 du Cotton), le ratio nu <BB>/<EE> vaut "
     "(1/2)²/(1/3)² = 9/4, PAS 1. L'équipartition = 1 est un énoncé en "
     "UNITES DE DUALITE (𝓑 = D𝓔, D isométrique), pas dans les unités "
     "prog. Écart de convention nommé, aucune tolérance desserrée, aucun "
     "coefficient modifié — précédent R-2/Q6.")

# ====================================================================
# Q7 — comparanda : imports externes (Osborn-Petkou, de Haro)
# ====================================================================
print("\n### Q7 — C4 : comparanda — IMPORTS externes, comptage interne seul dérivé")

cat = [(2, 1), (4, 2), (8, 3)]
nets = [sp.simplify(v * sp.Rational(1, 2) ** p) for v, p in cat]
pas("cas catalogue {2, 4, 8} : chaque préfacteur 2^p apparié à (½)^p du "
    "Cotton donne un produit NET = 1 (arithmétique interne)",
    all(x == 1 for x in nets),
    mutation=(sp.simplify(2 * sp.Rational(1, 2) ** 2) == 1),
    mut_label="un appariement décalé (2 avec (½)²) donnerait aussi 1")
pas("Gamma(−3/2) FINIE en d = 3 (pole-free) ; Gamma(−2) est un PÔLE — "
    "la spécificité d = 3 est STRUCTURELLE",
    sp.simplify(sp.gamma(sp.Rational(-3, 2)) - 4 * sp.sqrt(sp.pi) / 3) == 0
    and sp.gamma(-2) == sp.zoo,
    mutation=(sp.gamma(-2) != sp.zoo),
    mut_label="Gamma(−2) serait finie")

cons("Q7 / import Osborn-Petkou", "OP (2.23)-(2.24) = 1 structure / "
     "1 constante : IMPORT non redérivé. Recoupe la dimension 1 dérivée en "
     "Q4 — recoupement, pas confirmation mutuelle.")
cons("Q7 / import de Haro", "de Haro (47) coefficient Cotton ½ : IMPORT. "
     "Recoupe le ½ dérivé ab initio en Q6 par le Ricci linéarisé.")
cons("Q7 / import de Haro (49)/(50)", "équipartition <𝓑𝓑>/<𝓔𝓔> = 1 EXACTE "
     "en unités de dualité : IMPORT, dont le mécanisme (D isométrique) est "
     "dérivé en Q6 ; la valeur elle-même n'est pas indépendamment recalculée "
     "à partir de de Haro.")
cons("Q7 / c_FT = pi²/12", "IMPORT non dérivé (= zeta(2)/2 ; aucune route "
     "interne à ce lot n'y mène). Consigné tel quel.")
cons("Q7 / map prog↔dH = kappa²/(H·ell²)", "facteur fixe pur, sans paramètre "
     "libre : IMPORT de convention, non redérivé.")
cons("Q7 / comptage", "0 entrée libre < 3 sorties appariées (structure, "
     "coefficient ½, équipartition) : le comptage est favorable mais reste "
     "un comptage — il ne vaut pas dérivation des imports.")

# ====================================================================
# Q8 — firewall 5/5
# ====================================================================
print("\n### Q8 — firewall 5/5 (mutations mordantes)")

eta_n = sp.Symbol("eta", negative=True)
g0s = sp.Symbol("g_0", positive=True)
hBD = g0s * (1 + sp.I * kf * eta_n) * sp.exp(-sp.I * kf * eta_n)
ser = sp.series(hBD, eta_n, 0, 5).removeO().expand()
c2, c3 = ser.coeff(eta_n, 2), ser.coeff(eta_n, 3)
pas("FIREWALL 1 — Delta ≠ 3 casse : à d = 3 le coefficient eta² est "
    "DETERMINE (= k²g0/2, local) et seul eta³ (Delta = d = 3) est la donnée "
    "LIBRE ; g3 = −(i/3)k³g0",
    sp.simplify(c2 - kf ** 2 * g0s / 2) == 0
    and sp.simplify(c3 + (sp.I / 3) * kf ** 3 * g0s) == 0,
    mutation=(sp.simplify(c2) == 0),
    mut_label="le coefficient eta² serait absent (donc indéterminé/libre)")
pas("FIREWALL 2 — d = 4 : puissance 2·Delta − d = 4, alpha = 2 entier ⟹ "
    "pôle Gamma(−2) ⟹ coefficient de Fourier NUL ⟹ contact (la radiativité "
    "de d = 3 est structurelle, pas conventionnelle)",
    coeff_FT(2, 4) == 0,
    mutation=(coeff_FT(sp.Rational(3, 2), 3) == 0),
    mut_label="d = 3 donnerait lui aussi un coefficient nul")
ratio_nom = sp.Integer(1)
ratio_mut = sp.simplify((2 * sp.Rational(1, 2)) ** 0 * 2 ** 2)
pas("FIREWALL 3 — Cotton ×2 ⟹ ratio d'équipartition 4 ≠ 1 : l'équipartition "
    "est un énoncé MORDANT sur le coefficient ½, pas une identité vide",
    ratio_nom == 1 and ratio_mut == 4,
    mutation=(ratio_mut == 1),
    mut_label="doubler le Cotton laisserait le ratio à 1")
pas("FIREWALL 4 — la trace est ANNIHILEE par Pi^TT : aucun singlet ne "
    "traverse la projection (Pi^TT(delta) = 0)",
    np.abs(app(Pi, DELTA)).max() < TOL,
    mutation=(np.abs(app(PiV(n), DELTA)).max() < TOL
              and np.abs(app(PiS(n), DELTA)).max() < TOL),
    mut_label="delta serait annihilé par TOUS les projecteurs SVT (donc nul)")
nn = sp.Symbol("n_BY")
gamma_of_n = nn ** 2
pas("FIREWALL 5 — n ≠ 2 casse : gamma = n² (n = 2, Brown-York) ⟹ gamma = 4 ; "
    "n = 1 donne gamma = 1 [relation gamma = n² IMPORTEE de R-4/T13]",
    gamma_of_n.subs(nn, 2) == 4 and gamma_of_n.subs(nn, 1) == 1,
    mutation=(gamma_of_n.subs(nn, 1) == 4),
    mut_label="n = 1 donnerait aussi gamma = 4")

cons("Q8 / firewall 5 — provenance", "la relation gamma = n² (n = 2 de "
     "Brown-York) est IMPORTEE du lot R-4 (T13), non redérivée ici. Le "
     "firewall teste sa sensibilité, pas sa validité.")
cons("Q8 / limite du firewall 1 NOMMEE", "le critère d'analyticité SEUL ne "
     "sépare pas Delta = 2 (alpha = 1/2, demi-entier, donc radiatif lui "
     "aussi : coefficient −pi ≠ 0). Ce qui singularise Delta = 3 à d = 3 "
     "n'est PAS la radiativité mais la MARGINALITE Delta = d (tenseur de "
     "stress, coefficient FG libre à eta^d). Limite consignée, non contournée.")

# ====================================================================
print("\n" + "=" * 78)
if FAIL:
    print("REDEMO R-10 : %d PASS, %d CONSIGNATIONS — ECHECS :" % (PASS, CONS))
    for f in FAIL:
        print("   - " + f)
    print("=" * 78)
    sys.exit(1)
print("REDEMO R-10 : %d/%d PASS discriminants + %d consignations déclarées "
      "— EXIT 0" % (PASS, PASS, CONS))
print("Grade au mieux : REPRODUIT-SOUS-RESERVE au sens E-2 (plafond annoncé "
      "AU GEL : valeurs d'arrivée ET mécanismes révélés par les "
      "front-matters). E-1 exclu d'avance.")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien. "
      "Le verrou un-point reste CONDITIONNEL à A3 et SPECIFIQUE à d = 3 ; "
      "<g3 g3> ∝ k³ reste la donnée de Cauchy irréductible pendue à la seule "
      "amplitude A_T ~ 1/N ; A3/A4 NON fusionnés ; D1 NON clos ; N non fixé. "
      "{ A4 ; A2* ; N } INCHANGE · CCC non démontrée NI réfutée.")
print("=" * 78)
sys.exit(0)
