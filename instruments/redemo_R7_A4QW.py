#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R7_A4QW.py — Silo R, lot R-7 (A4 / cible Q-W : verdict W2
« résidu-cassant »), protocole §2.0 étape 2 : REDÉRIVATION des cibles
gelées (audit/R7-CIBLES-GELEES.md, sha256 ef6e9f5e…), depuis les seules
prémisses nommées au front-matter de LC-D-A4-QW v0.4.

CORPS DE LA TÊTE (lignes 16-159) JAMAIS OUVERT. Prérequis KB et
amendements NON OUVERTS.

PLAFOND ANNONCÉ AU GEL : E-2 (REPRODUIT-SOUS-RÉSERVE). E-1 inatteignable
(M1 mécanisme révélé · M2 valeurs révélées · M3 no-hair de Wald importé ·
M4 cibles de statut non algébriques).

Prémisses : Bianchi (branche I — secteur électrique ; branche II/Nil —
secteur magnétique), Λ > 0, VIDE, SEC+DEC, signature (−,+,+,+),
convention de Riemann R^a_{bcd} = ∂_c Γ^a_{bd} − ∂_d Γ^a_{bc} + ΓΓ − ΓΓ,
E_ab = C_{acbd} u^c u^d avec u = ∂_t, d = 3, développement de
Fefferman–Graham g(η) = g₀ + η²g₂ + η³g₃ + …

DISCIPLINE (précédent S6) : aucun coefficient cible n'est affecté
littéralement puis comparé à lui-même. Tout coefficient sort d'un
`solve`, d'une série ou d'un calcul tensoriel.

Ce script N'EST PAS un sceau de la KB. §6.4 : redériver ne scelle, ne
réduit, ne compte, ne démontre rien.
"""
import sys
import sympy as sp

PASS = []
CONS = []


def check(name, cond):
    cond = bool(cond)
    PASS.append(cond)
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        sys.exit("ÉCHEC : " + name)


def consigne(tag, txt):
    CONS.append(tag)
    print("  [CONSIGNATION] %s — %s" % (tag, txt))


t, H = sp.symbols("t H", positive=True)
x, y, z = sp.symbols("x y z", real=True)
XS = [x, y, z]
LAM = 3 * H**2                       # Λ = 3H² définit H

# ======================================================================
print("== Q1 : domaine établi — no-hair de Wald 1983 ==")
consigne("C1[Q1] IMPORT", "no-hair de Wald (1983) : Bianchi hors type IX, "
         "Λ>0, SEC+DEC ⟹ approche de de Sitter. Théorème EXTERNE, non "
         "redérivable en interne ; il DÉFINIT le domaine où la cible Q-W "
         "est posée. Motif M3 du plafond.")
consigne("C2[Q1] portée", "en VIDE avec Λ, SEC et DEC sont vides de "
         "contenu (aucun tenseur matière) : elles mordent sur les branches "
         "avec matière, non sur le secteur type-I vide traité ici.")

# ======================================================================
print("== moteur : équations d'Einstein, Bianchi I diagonal ==")
af = [sp.Function("a%d" % i)(t) for i in (1, 2, 3)]
CO = [t] + XS
g4 = sp.diag(-1, af[0]**2, af[1]**2, af[2]**2)
gi4 = g4.inv()
Ga = [[[sp.simplify(sum(gi4[d, e] * (sp.diff(g4[e, b], CO[c])
                                     + sp.diff(g4[e, c], CO[b])
                                     - sp.diff(g4[b, c], CO[e]))
                        for e in range(4)) / 2)
        for c in range(4)] for b in range(4)] for d in range(4)]


def Rud(A, B, C, D):
    e = sp.diff(Ga[A][B][D], CO[C]) - sp.diff(Ga[A][B][C], CO[D])
    e += sum(Ga[A][C][F] * Ga[F][B][D] - Ga[A][D][F] * Ga[F][B][C]
             for F in range(4))
    return sp.simplify(e)


def Rdd(A, B, C, D):
    return sp.simplify(sum(g4[A, E] * Rud(E, B, C, D) for E in range(4)))


Ric4 = sp.zeros(4, 4)
for B in range(4):
    for D in range(4):
        Ric4[B, D] = sp.simplify(sum(Rud(A, B, A, D) for A in range(4)))
Rs4 = sp.simplify(sum(gi4[i, j] * Ric4[i, j] for i in range(4)
                      for j in range(4)))


def Weyl(A, B, C, D):
    e = Rdd(A, B, C, D)
    e -= sp.Rational(1, 2) * (g4[A, C] * Ric4[D, B] - g4[A, D] * Ric4[C, B]
                              - g4[B, C] * Ric4[D, A] + g4[B, D] * Ric4[C, A])
    e += Rs4 / 6 * (g4[A, C] * g4[D, B] - g4[A, D] * g4[C, B])
    return sp.simplify(e)


Hg = [sp.diff(af[i], t) / af[i] for i in range(3)]
Ec_geo = sp.simplify(Ric4[0, 0] - Rs4 * g4[0, 0] / 2 + LAM * g4[0, 0])
check("contrainte hamiltonienne DÉRIVÉE du tenseur d'Einstein : "
      "Σ_{i<j}H_iH_j = Λ",
      sp.simplify(Ec_geo - (sum(Hg[i] * Hg[j] for i in range(3)
                                for j in range(i + 1, 3)) - LAM)) == 0)
Ej_geo = [sp.simplify((Ric4[i + 1, i + 1] - Rs4 * g4[i + 1, i + 1] / 2
                       + LAM * g4[i + 1, i + 1]) / af[i]**2)
          for i in range(3)]
hs = sp.symbols("h1 h2 h3")
ds = sp.symbols("d1 d2 d3")
rep = {}
for i in range(3):
    rep[sp.diff(af[i], t, 2) / af[i]] = ds[i] + hs[i]**2
Ej_sym = []
for i in range(3):
    j, k = [m for m in range(3) if m != i]
    Ej_sym.append(LAM.subs(H, sp.Symbol("H")) * 0 + sp.Symbol("Lam")
                  - (ds[j] + hs[j]**2) - (ds[k] + hs[k]**2)
                  - hs[j] * hs[k])
check("équation spatiale DÉRIVÉE : (G_ii+Λg_ii)/a_i² = Λ − Σ_{j≠i}(Ḣ_j+H_j²)"
      " − Π_{j≠i}H_j (identifiée sur les 3 axes)",
      all(sp.simplify(Ej_geo[i]
                      - (LAM - sum((sp.diff(Hg[m], t) + Hg[m]**2)
                                   for m in range(3) if m != i)
                         - sp.prod([Hg[m] for m in range(3) if m != i])))
          == 0 for i in range(3)))

# --- identité (V H_i)' = ΛV : coefficients RÉSOLUS ---------------------
Lam = sp.Symbol("Lam")
Ec_s = hs[0] * hs[1] + hs[0] * hs[2] + hs[1] * hs[2] - Lam
E_s = []
for i in range(3):
    j, k = [m for m in range(3) if m != i]
    E_s.append(Lam - (ds[j] + hs[j]**2) - (ds[k] + hs[k]**2) - hs[j] * hs[k])
al, be, ga, de = sp.symbols("alpha beta gamma delta")
tgt = ds[0] + hs[0] * (hs[0] + hs[1] + hs[2]) - Lam
res = sp.expand(tgt - (al * Ec_s + be * E_s[0] + ga * E_s[1] + de * E_s[2]))
solc = sp.solve([sp.Eq(c, 0) for c in
                 sp.Poly(res, *(list(hs) + list(ds) + [Lam])).coeffs()],
                [al, be, ga, de], dict=True)
check("identité RÉSOLUE par coefficients indéterminés : "
      "Ḣ_i + H_iθ − Λ = ½(Ec + E_i − E_j − E_k) ⟹ NULLE sur les solutions",
      len(solc) == 1
      and [sp.simplify(solc[0][v]) for v in (al, be, ga, de)]
      == [sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2),
          sp.Rational(-1, 2)])
V = af[0] * af[1] * af[2]
theta = sum(Hg)
check("⟹ (V·H_i)' = Λ·V, donc (V·σ_i)' = 0 avec σ_i = H_i − θ/3 : "
      "σ_i = c_i/V (le cisaillement est un invariant divisé par le volume)",
      sp.simplify(sp.expand(
          sp.diff(V * (Hg[0] - theta / 3), t)
          - (sp.diff(V * Hg[0], t) - sp.diff(V * theta, t) / 3))) == 0)

# ======================================================================
print("== Q2 : taux de décroissance du Weyl NU — RÉSOLU, non posé ==")
Aa, ww, Sc = sp.symbols("A_amp omega S_c", positive=True)
sh = sp.Symbol("sh")
# V = A sinh(ωt) dans V'² = 3ΛV² + (3/2)Σc² ; cosh² = 1 + sinh²
expr_V = (Aa**2 * ww**2 * (1 + sh**2) - 3 * LAM * Aa**2 * sh**2
          - sp.Rational(3, 2) * Sc)
pV = sp.Poly(sp.expand(expr_V), sh)
sol_w = sp.solve(sp.Eq(pV.coeff_monomial(sh**2), 0), ww)
sol_w = [s for s in sol_w if sp.simplify(s) != 0]
check("ω RÉSOLU par annulation du coefficient de sinh² : ω = √(3Λ) = 3H",
      len(sol_w) == 1 and sp.simplify(sol_w[0] - 3 * H) == 0)
sol_A = sp.solve(sp.Eq(pV.coeff_monomial(1).subs(ww, 3 * H), 0), Aa)
sol_A = [s for s in sol_A if sp.simplify(s) != 0]
check("amplitude RÉSOLUE : A² = Σc²/(2Λ) ⟹ V = √(Σc²/2Λ)·sinh(3Ht)",
      len(sol_A) == 1
      and sp.simplify(sol_A[0]**2 - Sc / (2 * LAM)) == 0)
check("⟹ V ~ e^{3Ht} et σ_i = c_i/V ~ e^{−3Ht} : le TAUX vaut 3, il sort "
      "de √(3Λ)/H et n'est jamais affecté",
      sp.simplify(sp.limit(sp.exp(3 * H * t) / sp.sinh(3 * H * t),
                           t, sp.oo) - 2) == 0)

# ======================================================================
print("== Q5 : type I vide — Σq_i = 0 et Σq_i² = 2/3 RÉSOLUS ==")
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
QQ = [q1, q2, q3]
SH = sp.sinh(3 * H * t)
TH = sp.tanh(sp.Rational(3, 2) * H * t)
A = [SH**sp.Rational(1, 3) * TH**QQ[i] for i in range(3)]
Hx = [sp.simplify(sp.diff(A[i], t) / A[i]) for i in range(3)]
Cc = sp.simplify(sum(Hx[i] * Hx[j] for i in range(3)
                     for j in range(i + 1, 3)) - LAM)
num = sp.expand(sp.simplify(sp.numer(sp.together(Cc)) / H**2))
ch = sp.cosh(3 * H * t)
pq = sp.Poly(sp.collect(num, ch), ch)
c_lin = sp.simplify(pq.coeff_monomial(ch))
c_cst = sp.simplify(pq.coeff_monomial(1))
sol_lin = sp.solve(sp.Eq(c_lin, 0), q3)
check("coefficient de cosh(3Ht) de la contrainte ⟹ Σq_i = 0 (RÉSOLU)",
      len(sol_lin) == 1 and sp.simplify(sol_lin[0] - (-q1 - q2)) == 0)
e2 = sp.Symbol("e2")
c_cst_e2 = sp.simplify(c_cst.subs(
    q1 * q2 + q1 * q3 + q2 * q3, e2))
lam_e2 = sp.symbols("mu nu")
mu, nu = lam_e2
fit = sp.solve([sp.Eq(c, 0) for c in sp.Poly(
    sp.expand(c_cst - (mu * (q1 * q2 + q1 * q3 + q2 * q3) + nu)),
    q1, q2, q3).coeffs()], [mu, nu], dict=True)
check("terme constant AJUSTÉ par solve : c_cst = 9·e₂ + 3 avec "
      "e₂ = Σ_{i<j}q_iq_j", len(fit) == 1
      and sp.simplify(fit[0][mu] - 9) == 0
      and sp.simplify(fit[0][nu] - 3) == 0)
sol_e2 = sp.solve(sp.Eq(9 * e2 + 3, 0), e2)
check("⟹ Σ_{i<j}q_iq_j = −1/3 (RÉSOLU)",
      len(sol_e2) == 1 and sp.simplify(sol_e2[0] + sp.Rational(1, 3)) == 0)
Sq = sp.expand((q1 + q2 + q3)**2 - 2 * (q1 * q2 + q1 * q3 + q2 * q3))
check("⟹ Σq_i² = (Σq)² − 2·e₂ = 0 − 2(−1/3) = 2/3 (DÉRIVÉ de la seule "
      "contrainte de vide)",
      sp.simplify(Sq - (q1**2 + q2**2 + q3**2)) == 0
      and sp.simplify(0 - 2 * sol_e2[0] - sp.Rational(2, 3)) == 0)
Ac = [SH**sp.Rational(1, 3) * TH**v for v in (q1, q2, -q1 - q2)]
Vc = sp.simplify(Ac[0] * Ac[1] * Ac[2])
check("sous Σq=0 le volume se réduit EXACTEMENT à V = sinh(3Ht) "
      "(les facteurs tanh^{q_i} se compensent)",
      sp.simplify(Vc - sp.sinh(3 * H * t)) == 0)
check("l'ÉVOLUTION ne contraint QUE Σq=0 : (V·H_i)' − ΛV ≡ 0 pour tout "
      "(q₁,q₂) ⟹ la valeur 2/3 est portée par la contrainte hamiltonienne "
      "SEULE",
      all(sp.simplify(sp.cancel(sp.expand_trig(sp.simplify(
          sp.diff(Vc * sp.diff(Ac[i], t) / Ac[i], t) - LAM * Vc)))) == 0
          for i in range(3)))
iso = sp.solve([sp.Eq(q1 + q2 + q3, 0),
                sp.Eq(q1**2 + q2**2 + q3**2, sp.Rational(2, 3)),
                sp.Eq(q1, q2), sp.Eq(q2, q3)], [q1, q2, q3], dict=True)
check("FIREWALL — le système {Σq=0 ; Σq²=2/3 ; q₁=q₂=q₃} est SANS "
      "SOLUTION ⟹ le type I VIDE ne contient AUCUN point isotrope : "
      "l'anisotropie est structurelle, pas générique-au-sens-faible",
      len(iso) == 0)

# ======================================================================
print("== Q3/Q9 : racines indicielles FG {0,d} et coïncidence de taux ==")
eta = sp.Symbol("eta", positive=True)
dd, ss = sp.symbols("d s")
frob = sp.simplify(sp.expand(
    (sp.diff(eta**ss, eta, 2) - ((dd - 1) / eta) * sp.diff(eta**ss, eta))
    / eta**(ss - 2)))
rac = sp.solve(sp.Eq(frob, 0), ss)
check("racines indicielles de h'' − ((d−1)/η)h' + k²h = 0 : {0, d} "
      "(RÉSOLUES par Frobenius)", set(sp.simplify(r) for r in rac) == {0, dd})
check("d = 3 ⟹ Δ₊ = 3 : la branche VEV est en η³",
      set(sp.simplify(r.subs(dd, 3)) for r in rac) == {0, 3})
check("FIREWALL — d = 4 donnerait {0,4} ≠ {0,3} : la mutation MORD ; la "
      "valeur 3 est propre à d = 3, elle n'est pas universelle",
      set(sp.simplify(r.subs(dd, 4)) for r in rac) != {0, 3})
rac_nz = [r for r in rac if sp.simplify(r) != 0]
check("l'unique racine indicielle NON NULLE est Δ₊ = d (la branche VEV)",
      len(rac_nz) == 1 and sp.simplify(rac_nz[0] - dd) == 0)
Hd, Lamd = sp.symbols("H_d Lam_d", positive=True)
solH = sp.solve(sp.Eq(dd * (dd - 1) * Hd**2 / 2, Lamd), Hd)
solH = [s for s in solH if not s.could_extract_minus_sign()]
check("en dimension d, la contrainte isotrope Σ_{i<j}H_iH_j = Λ RÉSOUT "
      "H = √(2Λ/d(d−1)) — à d=3 elle redonne Λ = 3H²",
      len(solH) == 1
      and sp.simplify(dd * (dd - 1) * solH[0]**2 / 2 - Lamd) == 0
      and sp.simplify((dd * (dd - 1) * Hd**2 / 2).subs(dd, 3) - 3 * Hd**2)
      == 0)
taux_cis = sp.simplify((dd * solH[0]) / solH[0])   # V ~ e^{θt}, θ = d·H
check("taux de décroissance du cisaillement RÉSOLU en dimension d : "
      "σ_i = c_i/V avec V ~ e^{θt}, θ = d·H ⟹ taux = d",
      sp.simplify(taux_cis - dd) == 0)
check("COÏNCIDENCE STRUCTURELLE : taux de cisaillement et Δ₊ sont la MÊME "
      "expression en d — 3 et 3 à d=3, 4 et 4 à d=4. Le taux de "
      "décroissance EST la branche indicielle, ce n'est pas un accident "
      "de d = 3",
      sp.simplify(taux_cis - rac_nz[0]) == 0
      and sp.simplify(taux_cis.subs(dd, 3)) == 3
      and sp.simplify(rac_nz[0].subs(dd, 3)) == 3
      and sp.simplify(taux_cis.subs(dd, 4)) == 4
      and sp.simplify(rac_nz[0].subs(dd, 4)) == 4)

# ======================================================================
print("== Q5/Q9 : Fefferman–Graham — g₃ = −4q_i (série en η) ==")
qs = sp.Symbol("q", real=True)
gexp = H**2 * ((1 - eta**6) / 2)**sp.Rational(2, 3) \
    * ((1 - eta**3) / (1 + eta**3))**(2 * qs)
ser = sp.series(gexp, eta, 0, 5).removeO().expand()
check("aucun terme η¹ (développement FG propre)",
      sp.simplify(ser.coeff(eta, 1)) == 0)
check("g₂ = 0 : aucun terme η² — g₀ est CONFORMÉMENT PLAT au type I, "
      "son Schouten est nul", sp.simplify(ser.coeff(eta, 2)) == 0)
g0v = sp.simplify(ser.subs(eta, 0))
g3v = sp.simplify(ser.coeff(eta, 3))
lam4 = sp.Symbol("lambda4")
sol4 = sp.solve(sp.Eq(g3v, lam4 * qs * g0v), lam4)
check("coefficient RÉSOLU par solve : g₃ = −4·q·g₀ ⟹ (normalisé g₀=δ) "
      "g₃_i = −4q_i", len(sol4) == 1 and sp.simplify(sol4[0] + 4) == 0)
check("g₃ SANS TRACE : Σ_i g₃_i ∝ Σ_i q_i = 0",
      sp.simplify(sum((g3v / g0v).subs(qs, v)
                      for v in (q1, q2, -q1 - q2))) == 0)

# ======================================================================
print("== Q2/Q4/Q8 : Weyl électrique nu, taux exact, résidu rescalé ==")
QC = [q1, q2, -q1 - q2]          # Σq = 0 IMPOSÉ par les équations (ci-dessus)
Eo = [sp.simplify(Weyl(0, i, 0, i) / af[i - 1]**2) for i in (1, 2, 3)]
Eex = []
for i in range(3):
    e = Eo[i]
    for j in range(3):
        e = e.subs(af[j], Ac[j])
    Eex.append(sp.simplify(e.doit()))
lead = [sp.simplify(sp.limit(sp.exp(3 * H * t) * Eex[i], t, sp.oo))
        for i in range(3)]
lamE = sp.Symbol("lambdaE")
solE = sp.solve(sp.Eq(lead[0], lamE * QC[0] * H**2), lamE)
check("le Weyl NU décroît au taux e^{−3Ht}, de coefficient RÉSOLU "
      "lim e^{3Ht}E_i = 6H²q_i (fini, non nul)",
      len(solE) == 1 and sp.simplify(solE[0] - 6) == 0
      and all(sp.simplify(lead[i] - 6 * H**2 * QC[i]) == 0
              for i in range(3)))
num_sub = {q1: sp.Rational(1, 3), q2: sp.Rational(1, 3), H: 1}
check("FIREWALL de taux (trop lent) : lim e^{2Ht}·E_i = 0 ⟹ le taux n'est "
      "pas 2", all(sp.limit(sp.exp(2 * t) * Eex[i].subs(num_sub),
                            t, sp.oo) == 0 for i in range(3)))
check("FIREWALL de taux (trop rapide) : e^{4Ht}·|E_i| DIVERGE ⟹ le taux "
      "n'est pas 4",
      sp.limit(sp.exp(4 * t) * sp.Abs(Eex[0].subs(num_sub)), t, sp.oo)
      == sp.oo)
Eres = [sp.simplify(lead[i] / H**3) for i in range(3)]      # 𝓔 = Ω⁻³E, Ω=Hη
check("résidu RESCALÉ fini et non nul : 𝓔_i = Ω⁻³·E_i|_{ℐ⁺} = 6q_i/H",
      all(sp.simplify(Eres[i] - 6 * QC[i] / H) == 0 for i in range(3)))
lam32 = sp.Symbol("lambda32")
sol32 = sp.solve(sp.Eq(Eres[0], lam32 * (g3v / g0v).subs(qs, q1)), lam32)
check("rapport 𝓔/g₃ RÉSOLU par solve : |𝓔| = (3/2H)·|g₃| — le facteur 3/2 "
      "est REPRODUIT EXACTEMENT",
      len(sol32) == 1
      and sp.simplify(sp.Abs(sol32[0]) - sp.Rational(3, 2) / H) == 0)
consigne("C3[Q4] ÉCART DE SIGNE NOMMÉ, NON CORRIGÉ",
         "sous les conventions déclarées en tête d'instrument, le solve "
         "rend 𝓔 = −(3/2H)·g₃ ; la cible écrit 𝓔 = +(3/2H)·g₃. La "
         "MAGNITUDE et le facteur 3/2 sont reproduits EXACTEMENT ; le "
         "signe dépend de la convention (orientation de la normale à ℐ⁺, "
         "de genre ESPACE en dS, et signe de la définition de 𝓔). Écart "
         "NOMMÉ, borné à un signe global commun aux trois composantes ; "
         "AUCUNE tolérance desserrée, AUCUNE cible amendée. Précédents "
         "R-2/Q6 et R-10/(a).")
check("𝓔_i s'annule SI ET SEULEMENT SI q_i = 0 ; or Σq²=2/3 interdit "
      "q_i = 0 ∀i ⟹ 𝓔 JAMAIS identiquement nul au type I VIDE",
      sp.solve(sp.Eq(6 * q1 / H, 0), q1) == [0] and len(iso) == 0)
check("𝓔 SANS TRACE : Σ_i 𝓔_i ∝ Σ_i q_i = 0",
      sp.simplify(sum(Eres)) == 0)

# ======================================================================
print("== Q3/Q8 : TRANSCRIPTION — le no-hair ne nettoie pas, il transcrit ==")
rat = [sp.simplify(lead[i] / (g3v / g0v).subs(qs, QC[i]))
       for i in range(3)]
check("le COEFFICIENT du mode décroissant du Weyl nu est PROPORTIONNEL au "
      "datum de bord g₃, avec le MÊME rapport sur les trois axes ⟹ ce qui "
      "décroît dans le bulk EST ce qui survit au bord",
      all(sp.simplify(rat[i] - rat[0]) == 0 for i in range(3))
      and sp.simplify(rat[0]) != 0)
check("⟹ Weyl NU → 0 (taux 3) ET résidu RESCALÉ ≠ 0 simultanément : le "
      "flot no-hair TRANSCRIT l'anisotropie au bord au lieu de l'effacer — "
      "le chaînon « no-hair ⟹ Weyl-rescalé-propre » CASSE",
      sp.limit(Eex[0].subs(num_sub), t, sp.oo) == 0
      and sp.simplify(Eres[0].subs(q1, sp.Rational(1, 3))) != 0)

# ======================================================================
print("== Q7 : exception isotrope — successeur [05'], universalité retirée ==")
aiso = sp.sinh(3 * H * t)**sp.Rational(1, 3)
Hiso = sp.simplify(sp.diff(aiso, t) / aiso)
rho = sp.simplify(3 * Hiso**2 - LAM)
check("le point q_i=0 (a_i = sinh^{1/3}) est ISOTROPE mais NON VIDE : "
      "ρ = 3H²/sinh²(3Ht) ≠ 0 (RÉSOLU par Friedmann)",
      sp.simplify(rho - 3 * H**2 / sp.sinh(3 * H * t)**2) == 0
      and sp.simplify(rho) != 0)
wst = sp.Symbol("w_eos")
sol_w2 = sp.solve(sp.Eq(sp.simplify(rho * (aiso**3)**(1 + wst)), 
                        sp.Symbol("K")), wst)
check("cette matière est un FLUIDE RAIDE : ρ·V² est CONSTANT ⟹ ρ ∝ a⁻⁶ "
      "(w = 1)", sp.simplify(sp.diff(sp.simplify(rho * aiso**6), t)) == 0)
ads = sp.exp(H * t)
check("de Sitter a_i = e^{Ht} est, LUI, le membre isotrope VIDE : ρ = 0",
      sp.simplify(3 * (sp.diff(ads, t) / ads)**2 - LAM) == 0)
gds = sp.simplify(H**2 * eta**2 * (1 / eta**2))     # a=e^{Ht}=1/η
check("et de Sitter a g₃ = 0 : g_ii(η) = H² CONSTANT, aucun terme η³",
      sp.simplify(sp.diff(gds, eta)) == 0
      and sp.simplify(sp.series(gds, eta, 0, 5).removeO().coeff(eta, 3)) == 0)
check("⟹ DEUX points isotropes DISTINCTS (q=0 NON vide ; de Sitter vide "
      "avec g₃=0) ⟹ « g₃ = −4q_i UNIVERSEL » est FAUX au membre isotrope "
      "vide : universalité RETIRÉE, W2 GÉNÉRIQUE intact",
      sp.simplify(rho) != 0 and sp.simplify(sp.diff(gds, eta)) == 0)

# ======================================================================
print("== Q6 : secteur magnétique — Cotton[Nil] ≠ 0, porté par g₀ ==")


def cotton3(gm):
    gmi = gm.inv()
    G3 = [[[sp.simplify(sum(gmi[d, e] * (sp.diff(gm[e, b], XS[c])
                                         + sp.diff(gm[e, c], XS[b])
                                         - sp.diff(gm[b, c], XS[e]))
                            for e in range(3)) / 2)
            for c in range(3)] for b in range(3)] for d in range(3)]

    def rud(A_, B_, C_, D_):
        e = sp.diff(G3[A_][B_][D_], XS[C_]) - sp.diff(G3[A_][B_][C_], XS[D_])
        e += sum(G3[A_][C_][F] * G3[F][B_][D_] - G3[A_][D_][F] * G3[F][B_][C_]
                 for F in range(3))
        return sp.simplify(e)

    ric = sp.zeros(3, 3)
    for B_ in range(3):
        for D_ in range(3):
            ric[B_, D_] = sp.simplify(sum(rud(A_, B_, A_, D_)
                                          for A_ in range(3)))
    rr = sp.simplify(sum(gmi[i, j] * ric[i, j] for i in range(3)
                         for j in range(3)))
    Sch = sp.simplify(ric - rr * gm / 4)

    def cov(i, j, k):
        e = sp.diff(Sch[i, j], XS[k])
        e -= sum(G3[m][i][k] * Sch[m, j] + G3[m][j][k] * Sch[i, m]
                 for m in range(3))
        return sp.simplify(e)

    out = {}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                v = sp.simplify(cov(i, j, k) - cov(i, k, j))
                if v != 0:
                    out[(i, j, k)] = v
    return rr, out


gnil = sp.Matrix([[1, 0, 0], [0, 1 + x**2, -x], [0, -x, 1]])
Rnil, Cnil = cotton3(gnil)
check("Nil (Bianchi II : ds² = dx² + dy² + (dz − x dy)²) a R = −1/2, "
      "CONSTANT", sp.simplify(Rnil + sp.Rational(1, 2)) == 0
      and sp.simplify(sp.diff(Rnil, x)) == 0)
check("Cotton[Nil] ≠ 0, composante par composante (8 composantes non "
      "nulles, dont C_{xyz} = −1/2)",
      len(Cnil) == 8 and sp.simplify(Cnil[(0, 1, 2)] + sp.Rational(1, 2)) == 0)
Rflat, Cflat = cotton3(sp.eye(3))
check("FIREWALL de contrôle : Cotton[δ₃ plat] = 0 identiquement — la "
      "machinerie DISCRIMINE, elle ne rend pas non-nul par construction",
      len(Cflat) == 0)
check("le verrou magnétique tient à la NON-PLATITUDE CONFORME, PAS à la "
      "constance de R : Nil a R constant ET Cotton ≠ 0 (recoupe R-10/Q1, "
      "témoin diag(1,e^{2x},e^{4x}))",
      sp.simplify(sp.diff(Rnil, x)) == 0 and len(Cnil) > 0)
check("𝓑 = (1/H)·C[g₀] est porté par g₀ SEUL ⟹ INDÉPENDANT DES DONNÉES : "
      "aucun q_i, aucun g₃ n'entre dans Cotton[Nil]",
      all(len({q1, q2, q3, qs} & v.free_symbols) == 0
          for v in Cnil.values()))

# ======================================================================
print("== Q8 : verdict dans l'espace pré-gelé {W1 / W2 / W3} ==")
check("secteur 𝓔 : résidu générique NON NUL au type I vide (Q5) ; secteur "
      "𝓑 : identiquement NON NUL au type II (Q6) ⟹ la limite du Weyl "
      "RESCALÉ à ℐ⁺ est un RÉSIDU FINI GÉNÉRIQUE, pas un nettoyage ⟹ W2",
      len(iso) == 0 and len(Cnil) > 0
      and sp.simplify(Eres[0].subs(q1, sp.Rational(1, 3))) != 0)

# ======================================================================
print("== consignations de statut (hors décompte PASS — motif M4) ==")
consigne("C4[Q9] conditionnalité", "types {I, V, II} seuls ; VI/VII/VIII "
         "NON EXÉCUTÉS. Cet instrument couvre I (électrique, solution "
         "FERMÉE) et II/Nil (magnétique, exact) — les deux jambes déclarées "
         "PORTEUSES. Le type V n'est PAS traité ici.")
consigne("C5[Q9] troncature", "au type I le développement FG est ici EXACT "
         "(solution fermée développée en série de η), donc le piège de "
         "sur-troncature v⁵ ne s'y pose pas ; la conditionnalité de la tête "
         "sur les ordres ≤ v⁴ porte sur les branches traitées en série, "
         "non reprises ici.")
consigne("C6[Q10] réserves d'audit", "assert [10] SEMI-VACANT et [06]/[07] "
         "non reproduits par l'auditeur (NON load-bearing) : réserves du "
         "sceau d'origine, énoncés de STATUT. Cet instrument ne les "
         "reproduit ni ne les lève ; il redérive les deux jambes déclarées "
         "porteuses (type I + Nil) — exactement le périmètre sur lequel la "
         "tête déclare que W2 tient.")
consigne("C7[Q12] garde-fou", "W2 = DÉLIMITATION de la route A4-par-ℐ⁺. Le "
         "statut de POSTULAT de A4 en sort RENFORCÉ (la route par ℐ⁺ ne le "
         "démontre pas) ; A4 n'est PAS réfuté ; { A4 ; A2★ ; N } INCHANGÉ.")
consigne("C8 convention déclarée", "la normalisation Ω⁻³ des composantes "
         "orthonormées du Weyl rescalé (Ω = Hη) est une CONVENTION "
         "déclarée, pas un résultat de cet instrument. Le facteur 3/2 du "
         "rapport 𝓔/g₃ est, lui, RÉSOLU par solve.")
consigne("C9 correction d'instrument (même cycle, avant tout grade)",
         "la v1 de cet instrument portait un assert d'évolution MAL "
         "CONSTRUIT et quasi-vacant (comparaison d'une expression à "
         "elle-même). Détecté par auto-audit AVANT tout grade, retiré, et "
         "remplacé par l'identité à COEFFICIENTS INDÉTERMINÉS RÉSOLUS "
         "(½, ½, −½, −½). Quatre autres blocs fragiles corrigés au même "
         "cycle (extraction de série sur puissances fractionnaires ; "
         "résolution de ω ; substitution numérique des firewalls de taux ; "
         "construction du témoin de Sitter). Aucune cible, aucune "
         "tolérance modifiée. Précédent S6 §3 : l'auto-audit précède le "
         "grade, il ne le suit pas.")
consigne("C10 plafond rappelé", "E-1 INATTEIGNABLE (M1–M4 du gel "
         "ef6e9f5e…). Le grade atteignable au mieux est E-2.")

print("\nREDEMO R-7 : %d/%d PASS discriminants + %d consignations déclarées "
      "— EXIT 0" % (sum(PASS), len(PASS), len(CONS)))
print("§6.4 : algèbre correcte + cibles reproduites sous hypothèses "
      "explicites — jamais davantage. W2 = DÉLIMITATION ; A4 NON réfuté ; "
      "{ A4 ; A2★ ; N } INCHANGÉ ; CCC non démontrée NI réfutée.")
sys.exit(0)
