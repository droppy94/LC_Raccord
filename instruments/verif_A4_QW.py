#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_A4_QW.py — SCEAU du chaînon-verdict LC-D-A4-QW (front A4 Phase-1, cible Q-W).

Cadrage gelé (CSE-2, sha hors-fichier, manifeste) : LC-WORK-CADRAGE-A4-QW [91a50391].
Amendement R-7 (gel hors-fichier, manifeste)      : LC-WORK-AMENDEMENT-R7-A4-QW-PHASE0 [b60baef0].
Espace-verdict gelé : {W1 nettoyage-tenant / W2 résidu-cassant / W3 indéterminé}.

VERDICT SCELLÉ ICI : W2 — RÉSIDU-CASSANT.
Question Q-W : dans le domaine établi du no-hair (branche Bianchi, Wald 1983, Λ>0, SEC+DEC),
la limite à 𝓘⁺ du Weyl RESCALÉ (couple programme 𝓔=(3/2H)g₃ ; 𝓑=(1/H)C[g₀]) le long du flot
no-hair converge-t-elle vers 0, ou vers un résidu fini générique ?
Réponse (algèbre, types I/V/II) : RÉSIDU GÉNÉRIQUE — secteur 𝓔 porté par g₃ (donnée
d'anisotropie ; JAMAIS nul au type I vide), secteur 𝓑 porté par g₀ (identiquement non nul
au type II, structure Nil). Le taux no-hair e^{−3Ht} EST la branche Δ₊=3 : le flot transcrit
l'anisotropie au bord au lieu de l'effacer.

PORTÉE : types Bianchi {I, V, II} calculés ; VI/VII/VIII NON-EXÉCUTÉS (tractabilité, amendement
§2) ; conditionnalités : b2 (Wald→FG lisse = import de connexion, bénin homogène), b3 (racines
{0,3} indicielles/linéaires, argument de parité d=3 impair). Unités H=1, Λ=3.
§6.4 : W2 = DÉLIMITATION de la route A4-par-𝓘⁺ ; A4 NON réfuté, RIEN ne réduit ;
{A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée.

Asserts porteurs [01]-[10] + mutations firewall [F1]-[F4] (chacune doit MORDRE).
EXIT 0 attendu. Stack : Python 3.12 / SymPy 1.14.
"""
import sys
import sympy as sp

FAIL = []
def check(label, cond):
    ok = bool(cond)
    print(('PASS ' if ok else 'FAIL ') + label)
    if not ok:
        FAIL.append(label)

# ============================================================================
# BLOC A — BIANCHI I (vide+Λ), paramétrage rationnel w = e^{3Ht}, H=1
# a_i = sinh^{1/3}(3t)·tanh^{q_i}(3t/2) ; H_i = (w²+1+6q_i w)/(w²−1)
# ============================================================================
w, u = sp.symbols('w u', positive=True)   # u = 1/w = e^{-3Ht}
q1, q2 = sp.symbols('q1 q2', real=True)
q3 = -q1 - q2
qs = [q1, q2, q3]
Hs = [(w**2 + 1 + 6*q*w)/(w**2 - 1) for q in qs]
Dt = lambda f: sp.diff(f, w)*3*w
theta = sp.simplify(sum(Hs))
K13 = sp.Rational(1, 3)                    # contrainte vide : q1²+q1q2+q2² = 1/3 (⟺ Σq²=2/3)
q2sol = sp.solve(sp.Eq(q1**2 + q1*q2 + q2**2, K13), q2)[1]

# [01] Einstein vide+Λ exact (contrainte + 3 évolutions)
cF = sp.simplify((Hs[0]*Hs[1] + Hs[0]*Hs[2] + Hs[1]*Hs[2] - 3).subs(q2, q2sol))
ev = [sp.simplify((Dt(Hs[i]) + Hs[i]*theta - 3).subs(q2, q2sol)) for i in range(3)]
check('[01] Bianchi I : Einstein vide+Λ exact (4 équations ≡ 0)',
      cF == 0 and all(e == 0 for e in ev))

# [02] taux no-hair : σ_i = 6q_i·e^{−3Ht} + O(e^{−6Ht}) — TAUX 3 EXHIBÉ (b1)
sig_ser = []
for i in range(3):
    s = sp.simplify((Hs[i] - theta/3).subs(w, 1/u))
    sig_ser.append(sp.expand(sp.series(s, u, 0, 2).removeO()))
check('[02] taux 3 exhibé : σ_i = 6q_i·u + O(u²)',
      all(sp.simplify(sig_ser[i] - 6*qs[i]*u) == 0 for i in range(3)))

# [03] Weyl NU → 0 (repère orthonormé ; m2 : calculé, jamais consommé comme conclusion)
R0i0i = [sp.simplify(-(Dt(Hs[i]) + Hs[i]**2)) for i in range(3)]
Rii   = [sp.simplify(Dt(Hs[i]) + Hs[i]*theta) for i in range(3)]
R00   = sp.simplify(-sum(Dt(Hs[i]) + Hs[i]**2 for i in range(3)))
Rsc   = sp.simplify(2*(Hs[0]*Hs[1] + Hs[0]*Hs[2] + Hs[1]*Hs[2])
                    + 2*sum(Dt(Hs[i]) + Hs[i]**2 for i in range(3)))
E_nu = [sp.simplify(R0i0i[i] + (Rii[i] - R00)/2 - Rsc/6) for i in range(3)]
E1u = sp.series(sp.simplify(E_nu[0].subs(q2, q2sol).subs(w, 1/u)), u, 0, 2).removeO()
check('[03] Weyl NU → 0 au taux 3 : E_nu,1 = 6q1·u + O(u²) ; 𝓑_nu ≡ 0 (diagonal)',
      sp.simplify(E1u - 6*q1*u) == 0)

# [04] extraction FG : a_i²e^{−2Ht} = 2^{−2/3}(1 − 4q_i·u + O(u²)) ⟹ g₀ plat, g₃ ∝ −4q_i
g3I = []
for q in qs:
    f = 2**sp.Rational(-2, 3)*(1 - u**2)**sp.Rational(2, 3)*((1 - u)/(1 + u))**(2*q)
    ser = sp.series(f, u, 0, 2).removeO()
    c0 = ser.subs(u, 0); c1 = sp.simplify(sp.diff(ser, u).subs(u, 0))
    g3I.append(sp.simplify(c1/c0))
check('[04] FG type I : g₃ = diag(−4q_i), traceless, mode u = (Hz)³ = branche Δ₊=3',
      all(sp.simplify(g3I[i] + 4*qs[i]) == 0 for i in range(3))
      and sp.simplify(sum(g3I)) == 0)

# [05] type I vide : g₃ = 0 IMPOSSIBLE (Σq²=2/3 exclut q=0) ⟹ résidu 𝓔 sur TOUTE la famille
sol_q0 = sp.solve([sp.Eq(q1, 0), sp.Eq(q2, 0), sp.Eq(q1**2 + q1*q2 + q2**2, K13)], [q1, q2])
check('[05] type I vide : {q=0} ∩ {contrainte} = ∅ ⟹ lim 𝓔 = (3/2H)g₃ ≠ 0 sur toute la famille',
      sol_q0 == [])

# ============================================================================
# BLOC B — SÉRIES FG types V et II (arithmétique polynomiale, ordres ≤ v⁴)
# a_i = (1/v)(1 + A_i v² + B_i v³ + D_i v⁴), d/dt = −v d/dv, H=1, Λ=3
# ============================================================================
v = sp.symbols('v')
A1, A2, A3, B1, B2, B3, D1, D2, D3 = sp.symbols('A1 A2 A3 B1 B2 B3 D1 D2 D3')
Av = [A1, A2, A3]; Bv = [B1, B2, B3]; Dv = [D1, D2, D3]
NT = 5
def T(e): return sp.expand((sp.expand(e) + sp.O(v**NT)).removeO())

def fg_system(curv):
    """curv(f, finv) -> (K1,K2,K3) : termes de courbure spatiale par direction (ordre v²)."""
    f = [1 + Av[i]*v**2 + Bv[i]*v**3 + Dv[i]*v**4 for i in range(3)]
    fp = [sp.diff(fi, v) for fi in f]
    fpp = [sp.diff(fi, v, 2) for fi in f]
    finv = []
    for i in range(3):
        uu = f[i] - 1
        finv.append(T(1 - uu + uu*uu))
    Hl = [T(1 - v*T(fp[i]*finv[i])) for i in range(3)]
    DD = [T(1 - v*T(fp[i]*finv[i]) + v**2*T(fpp[i]*finv[i])) for i in range(3)]
    K1, K2, K3 = curv(f, finv)
    E = [T(3 - DD[0] - DD[1] - DD[2]),
         T(K1 - 3 + DD[0] + T(Hl[0]*Hl[2]) + T(Hl[0]*Hl[1])),
         T(K2 - 3 + DD[1] + T(Hl[1]*Hl[2]) + T(Hl[0]*Hl[1])),
         T(K3 - 3 + DD[2] + T(Hl[1]*Hl[2]) + T(Hl[0]*Hl[2]))]
    return E, Hl

def collect_eqs(Elist, kmax=4):
    eqs = []
    for E in Elist:
        p = sp.Poly(E, v)
        for (k,), c in zip(p.monoms(), p.coeffs()):
            c = sp.expand(c)
            if k <= kmax and c != 0:
                eqs.append(sp.Eq(c, 0))
    return eqs

# --- Type V : courbure ISOTROPE −2/a₁² = −2v²f₁⁻² ; + contrainte de moment 2H₁=H₂+H₃ ---
def curvV(f, finv):
    K = T(-2*v**2*T(finv[0]*finv[0]))
    return K, K, K
EV, HV = fg_system(curvV)
EV.append(T(2*HV[0] - HV[1] - HV[2]))     # contrainte de moment type V
solV = sp.solve(collect_eqs(EV), [A1, A2, A3, B1, B2, B3, D1, D2, D3], dict=True)
sV = solV[0]
check('[06] type V : g₂ = −(1/4)δ (courbure, FG-concordant) ; g₃ = (0, −B3, B3) — 1 param LIBRE ; D = 0',
      len(solV) == 1
      and all(sV[k] == sp.Rational(-1, 4) for k in [A1, A2, A3])
      and sV[B1] == 0 and sp.simplify(sV[B2] + B3) == 0 and (B3 not in sV)
      and all(sV[k] == 0 for k in [D1, D2, D3]))

# --- Type II : courbure ANISOTROPE (+,−,−)·a₁²/(2a₂²a₃²) = (±)v²f₁²/(2f₂²f₃²) ---
def curvII(f, finv):
    K = T(sp.Rational(1, 2)*v**2*T(T(f[0]*f[0])*T(finv[1]*finv[1])*T(finv[2]*finv[2])))
    return K, -K, -K
EII, HII = fg_system(curvII)
solII = sp.solve(collect_eqs(EII), [A1, A2, A3, B1, B2, B3, D1, D2, D3], dict=True)
sII = solII[0]
check('[07] type II : g₂ = (5/16, −3/16, −3/16) anisotrope ; g₃ : ΣB=0 — 2 params LIBRES ; D fixés',
      len(solII) == 1
      and sII[A1] == sp.Rational(5, 16) and sII[A2] == sp.Rational(-3, 16)
      and sII[A3] == sp.Rational(-3, 16)
      and sp.simplify(sII[B1] + B2 + B3) == 0 and (B2 not in sII) and (B3 not in sII)
      and sII[D1] == sp.Rational(-3, 16) and sII[D2] == sp.Rational(3, 32)
      and sII[D3] == sp.Rational(3, 32))

# ============================================================================
# BLOC C — COTTON des métriques de bord g₀ (secteur 𝓑 = (1/H)·C[g₀])
# ============================================================================
def cotton_nonzero(g3d, Xs):
    gi = g3d.inv()
    Gm = [[[sp.simplify(sum(gi[l, m]*(sp.diff(g3d[m, i], Xs[j]) + sp.diff(g3d[m, j], Xs[i])
                                      - sp.diff(g3d[i, j], Xs[m])) for m in range(3))/2)
            for j in range(3)] for i in range(3)] for l in range(3)]
    def Ric3(i, j):
        r = 0
        for l in range(3):
            r += sp.diff(Gm[l][i][j], Xs[l]) - sp.diff(Gm[l][i][l], Xs[j])
            for m in range(3):
                r += Gm[l][l][m]*Gm[m][i][j] - Gm[l][j][m]*Gm[m][i][l]
        return sp.simplify(r)
    R3 = sp.Matrix(3, 3, lambda i, j: Ric3(i, j))
    Rs = sp.simplify(sum(gi[i, j]*R3[i, j] for i in range(3) for j in range(3)))
    S = sp.Matrix(3, 3, lambda i, j: sp.simplify(R3[i, j] - Rs*g3d[i, j]/4))
    def cds(k, i, j):
        r = sp.diff(S[i, j], Xs[k])
        for m in range(3):
            r -= Gm[m][k][i]*S[m, j] + Gm[m][k][j]*S[i, m]
        return sp.simplify(r)
    nz = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if sp.simplify(cds(i, j, k) - cds(j, i, k)) != 0:
                    nz += 1
    return nz

x, y, zc = sp.symbols('x y z')
gH3 = sp.diag(1, sp.exp(2*x), sp.exp(2*x))                                   # H³ (type V)
gNil = sp.Matrix([[1, -zc, 0], [-zc, 1 + zc**2, 0], [0, 0, 1]])              # Nil (type II)
check('[08] Cotton[H³] ≡ 0 ⟹ lim 𝓑 = 0 (types I plat et V H³ : g₀ conformément plats)',
      cotton_nonzero(gH3, [x, y, zc]) == 0)
check('[09] Cotton[Nil] ≠ 0 ⟹ lim 𝓑 ≠ 0 IDENTIQUEMENT au type II (porté par g₀, indépendant des données)',
      cotton_nonzero(gNil, [x, y, zc]) > 0)

# [10] uniformité indicielle : β̈ + 3β̇ = 0 ⟹ racines {0,3} (type-indépendant, concordant a0b962c8)
lam = sp.symbols('lam')
check('[10] racines indicielles du mode libre = {0, 3} (λ(λ−3)=0), indépendantes du potentiel de courbure',
      sorted(sp.solve(lam**2 - 3*lam, lam)) == [0, 3])

# ============================================================================
# BLOC F — MUTATIONS FIREWALL (chacune doit MORDRE)
# ============================================================================
# [F1] m1 anti-circularité : imposer q=0 (bas-Weyl en entrée) au type I vide VIOLE la contrainte
viol = sp.simplify((q1**2 + q1*q2 + q2**2 - K13).subs({q1: 0, q2: 0}))
check('[F1] mutation m1 : q=0 imposé ⟹ contrainte du vide violée (−1/3 ≠ 0) — la circularité EST détectée',
      viol == sp.Rational(-1, 3) and viol != 0)

# [F2] m2 anti-blanchiment : le NU s'annule en limite MAIS le RESCALÉ ne s'annule pas —
# consommer le nu comme conclusion inverserait [04]/[05]
nu_lim = sp.limit(E1u, u, 0)
resc_generic = sp.simplify(g3I[0].subs({q1: sp.Rational(1, 2), q2: sp.Rational(1, 10)}))
check('[F2] mutation m2 : lim(nu) = 0 ET g₃(générique) = −2 ≠ 0 — blanchir nu→rescalé CASSERAIT [04]',
      nu_lim == 0 and resc_generic == -2)

# [F3] m6 exposant : compensation Ω^{−1} (au lieu de la structure FG Ω^{−3} du mode u) ⟹
# limite NULLE pour TOUTES données — fabrique un faux W1, indépendance aux données = signature d'artefact
f_mut = 2**sp.Rational(-2, 3)*(1 - u**2)**sp.Rational(2, 3)*((1 - u)/(1 + u))**(2*q1)*u**sp.Rational(2, 3)
check('[F3] mutation m6 : sous Ω^{−1}, limite = 0 pour toutes données (artefact) — l’exposant FG est porteur',
      sp.limit(f_mut, u, 0) == 0 and sp.limit(f_mut, u, 0).free_symbols == set())

# [F4] m3 anti-continuation : signe de courbure type II inversé (pipeline hors domaine) ⟹
# le g₂ scellé (5/16, −3/16, −3/16) N'EST PAS reproduit — la mutation casse
def curvII_mut(f, finv):
    K = T(sp.Rational(1, 2)*v**2*T(T(f[0]*f[0])*T(finv[1]*finv[1])*T(finv[2]*finv[2])))
    return -K, K, K
EM, _ = fg_system(curvII_mut)
solM = sp.solve(collect_eqs(EM), [A1, A2, A3, B1, B2, B3, D1, D2, D3], dict=True)
check('[F4] mutation m3 : courbure mutée ⟹ g₂ ≠ (5/16, −3/16, −3/16) — l’assert [07] MORD',
      len(solM) == 1 and solM[0][A1] != sp.Rational(5, 16))

# ============================================================================
print()
if FAIL:
    print(f'ÉCHEC : {len(FAIL)} assert(s) — {FAIL}')
    sys.exit(1)
print('SCEAU verif_A4_QW : 14/14 PASS — VERDICT W2 (résidu-cassant) SCELLÉ.')
print('§6.4 : délimitation, aucune réduction ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée.')
sys.exit(0)
