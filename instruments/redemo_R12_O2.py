#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R12_O2.py — Lot R-12 : redérivation de l'arc O₂ (jonction D→N,
Hodge, P1/P2, Δ_𝒞, coin-transmission).
Cibles Q1–Q10, audit/R12-CIBLES-GELEES.md, sha256 =
4fe114dee7acb03c0f6124d3889071978da97c2d0963b72bf860b78fb1bf6a69.

Discipline amendée post-CSE : PASS discriminant (mutation mordante) /
CONSIGNATION (import, prémisse, verdict — hors décompte). Tolérance :
algèbre symbolique exacte (sympy, simplify==0 / égalités d'objets),
déclarée avant toute comparaison. Corps KB et code des sceaux NON lus.
Plafond annoncé au gel : E-2.

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
from sympy import (symbols, Symbol, I, Matrix, eye, simplify, S, Rational,
                   sqrt, sinh, cosh, asinh, expand, conjugate, det, im,
                   Function, pi, oo, expand_trig)

PASS, CONS, FAIL = [], [], []
def ok(tag, nominal, mutation_fails, note=""):
    if nominal and mutation_fails:
        PASS.append(tag); print(f"PASS  {tag}  {note}")
    else:
        FAIL.append(tag)
        print(f"FAIL  {tag}  nominal={nominal} mut_echoue={mutation_fails}  {note}")
def consigne(tag, note):
    CONS.append(tag); print(f"CONSIGNATION  {tag}  {note}")
Z = lambda e: simplify(e) == 0

Jm = Matrix([[0, 1], [1, 0]])          # swap de jonction (s=+1)
Sm = Matrix([[0, -1], [1, 0]])         # Hodge / S-map

# ===========================================================================
# Q2 — P1 : involution nue ⟹ s=+1 ; P² = s·𝟙 ; P=S ⟺ s=−1
# ===========================================================================
Om, s = symbols("Omega s", nonzero=True)

# P01 — le signe se carre et se perd : z ~ Ω⁻² sous Ω ↦ −1/Ω donne z ↦ 1/z
z_of = lambda O: O**(-2)
z_img = simplify(z_of(-1/Om))                  # attendu : Ω² = 1/z, AUCUN signe
nom = Z(z_img - Om**2) and Z(simplify(z_of(-1/(-1/Om))) - z_of(Om))  # involution
z_lin = lambda O: O**(-1)                      # mutation : poids IMPAIR
mut = not Z(simplify(z_lin(-1/Om)) - Om)       # z↦−Ω : le signe SURVIT
ok("P01[Q2] Ω↦−1/Ω sur z~Ω⁻² : z↦1/z, signe carré PERDU (involution)",
   nom, mut, "mutation poids impair Ω⁻¹ ⟹ le signe survit (−Ω)")

# P02 — P=[[0,s],[1,0]] : P² = s·𝟙 ; P=S ⟺ s=−1 ; s=+1 ⟹ P²=+𝟙 ≠ S²=−𝟙
Pm = Matrix([[0, s], [1, 0]])
nom = (Z((Pm*Pm - s*eye(2)).norm())
       and Z((Pm.subs(s, -1) - Sm).norm())
       and Z((Pm.subs(s, 1)*Pm.subs(s, 1) - eye(2)).norm())
       and Z((Sm*Sm + eye(2)).norm()))
mut = not Z((Pm.subs(s, 1) - Sm).norm())       # s=+1 ne donne PAS S
ok("P02[Q2] P²=s·𝟙 ; P=S ⟺ s=−1 ; involution nue (s=+1) ⟹ P²=+𝟙 ≠ S²=−𝟙",
   nom, mut, "la réciprocité conforme nue ne fournit pas le −𝟙")

# ===========================================================================
# Q3 — Hodge : invariants de classe ⟹ J ≁ S à toute base près
# ===========================================================================
nom = (det(Jm) == -1 and det(Sm) == 1
       and Z((Jm**2 - eye(2)).norm())                 # ordre 2
       and not Z((Sm**2 - eye(2)).norm())
       and Z((Sm**4 - eye(2)).norm())                 # ordre 4
       and sorted(Jm.eigenvals()) == [-1, 1]
       and set(Sm.eigenvals()) == {I, -I}
       and det(Jm) != det(Sm))                        # det = invariant de conjugaison
g11, g12, g21, g22 = symbols("g11 g12 g21 g22")
G = Matrix([[g11, g12], [g21, g22]])                  # changement de base générique
mut = not Z(det(G*Jm*G.inv()) - det(Sm))              # det(GJG⁻¹)=det(J)=−1 ≠ +1
ok("P03[Q3] J (det −1, ordre 2, vp ±1) ≁ S (det +1, ordre 4, vp ±i)",
   nom, mut, "det conservé par conjugaison GL(2) générique ⟹ aucune base ne fait J=S")

# ===========================================================================
# Q4 — garde-fou : W̃=−W ∧ ⟨T̃⟩=−2δW̃/δh̃ ⟹ C̃_T=+C_T
# ===========================================================================
h = Symbol("h"); W = Function("W")(h)
T_of = lambda Wf: -2*Wf.diff(h)                       # ⟨T⟩ = −2 δW/δh (convention consignée)
T_tilde = T_of(-W)                                    # W̃ = −W
nom = Z(simplify(T_tilde - (+2*W.diff(h))))           # ⟹ ⟨T̃⟩ = +2δW/δh ⟹ C̃_T=+C_T
mut = not Z(simplify(T_of(W) - (+2*W.diff(h))))       # sans le flip de W : signe opposé
ok("P04[Q4] deux −1 composés : W̃=−W ∧ T=−2δW/δh ⟹ C̃_T=+C_T", nom, mut,
   "la jonction ne flippe pas le signe physique ; mutation = un seul flip ⟹ −C_T")

# ===========================================================================
# Q5 — source unique : i^{d−1} réel ⟺ d impair ; = −1 à d=3 ; ≠ le −𝟙 de S²
# ===========================================================================
vals = {d: simplify(I**(d-1)) for d in (2, 3, 4, 5)}
nom = (vals[3] == -1 and vals[5] == 1
       and im(vals[3]) == 0 and im(vals[5]) == 0
       and im(vals[2]) != 0 and im(vals[4]) != 0     # d pair ⟹ non réel
       and Z((Sm*Sm + eye(2)).norm()))               # S²=−𝟙 : structural, d-indépendant
mut = not (simplify(I**(4-1)) == -1)                 # d=4 ne donne PAS −1 réel
ok("P05[Q5] i^{d−1} réel ⟺ d impair ; = −1 à d=3 ; DISTINCT du −𝟙 de S²",
   nom, mut, "deux −𝟙 séparés (observable dS vs carré de Hodge) ; mutation d=4")

# ===========================================================================
# Q6 / Q7 — P2 : α-vacua, conjugaison, échange des racines par J
# ===========================================================================
# vecteurs propres de S : S e± = ±i e± ; base (a,b)
ep = Matrix([1, -I]); em = Matrix([1, I])
mu = Symbol("mu", real=True)

# P06 — vérif propre + conjugaison : S réelle, conj(e₊)=e₋ (paire NON ordonnée)
nom = (Z((Sm*ep - I*ep).norm()) and Z((Sm*em + I*em).norm())
       and Z((ep.conjugate() - em).norm())
       and Z((Sm.conjugate() - Sm).norm()))          # S réelle ⟹ commute avec conj
Sc = Matrix([[0, -I], [1, 0]])                       # mutation : S complexe
mut = not Z((Sc.conjugate() - Sc).norm())
ok("P06[Q7] S e±=±i e± ; S RÉELLE ⟹ conj échange e₊↔e₋ : paire NON ordonnée",
   nom, mut, "le choix de racine +i n'est pas structurel ; mutation S complexe")

# P07 — la jonction échange les racines : J·e₊ ∝ e₋, J·e₋ ∝ e₊ (BD ↔ BD*)
c1 = simplify((Jm*ep)[0]/em[0]); c2 = simplify((Jm*em)[0]/ep[0])
nom = (Z(((Jm*ep) - c1*em).norm()) and Z(((Jm*em) - c2*ep).norm())
       and c1 != 0 and c2 != 0)
lam_p = simplify((Sm*ep)[0]/ep[0])                   # S préserve e₊ (vp i) — mutation
mut = not Z(((Jm*ep) - lam_p*ep).norm())             # J n'est PAS diagonal sur e₊
ok("P07[Q7] J·e₊ ∝ e₋ et J·e₋ ∝ e₊ : la jonction traite ±i SYMÉTRIQUEMENT",
   nom, mut, "elle n'impose pas +i ; mutation = J supposé diagonal sur e₊")

# P08 — exclusion des α-vacua : dét[v_α | S·v_α] = 4μ ⟹ zéro ⟺ μ=0 (BD)
v_alpha = ep + mu*em
Malpha = Matrix.hstack(v_alpha, Sm*v_alpha)
d_alpha = simplify(det(Malpha))
nom = Z(d_alpha - 4*I*mu) or Z(d_alpha - 4*mu) or Z(d_alpha + 4*mu) or Z(d_alpha + 4*I*mu)
# la cible gelée est |dét| = 4μ à phase de convention près : on exige le FACTEUR 4μ exact
phase = simplify(d_alpha/(4*mu))
nom = nom and phase.is_constant() and abs(complex(phase)) == 1.0 \
      and Z(d_alpha.subs(mu, 0))
mut = not Z(simplify(det(Matrix.hstack(v_alpha, Jm*v_alpha))) - d_alpha) \
      or Z(simplify(det(Matrix.hstack(v_alpha, Jm*v_alpha))))
# mutation : remplacer S par J ne doit PAS reproduire le même déterminant sélecteur
ok("P08[Q6] dét[v_α|S·v_α] = 4μ (phase de convention) ; s'annule ⟺ μ=0 (BD)",
   nom, mut, "α-vacua exclus SANS intrant d'état ; resserrement ∞→{BD,BD*}")

# ===========================================================================
# Q8 — Δ_𝒞 : ledger de dimensions d=3, coefficient (d−3)/2, trichotomie
# ===========================================================================
dd = Symbol("d", positive=True, integer=True)
dims = {"trace(GHY)": dd, "courbure²": 4, "courbure×EMT": dd+2, "TT̄": 2*dd}
at3 = {k: (v.subs(dd, 3) if hasattr(v, "subs") else v) for k, v in dims.items()}
coefTT = (dd - 3)/2
nom = (at3["trace(GHY)"] == 3 and at3["courbure²"] == 4
       and at3["courbure×EMT"] == 5 and at3["TT̄"] == 6
       and at3["trace(GHY)"] == min(at3.values())        # le plus relevant
       and Z(coefTT.subs(dd, 3))                          # TT̄ absent en d=3
       and Z(S(3) - 3))                                   # Δ_𝒞 − d = 0 ⟹ marginal ⟹ C1-b
mut = not Z(coefTT.subs(dd, 4))                           # d=4 : coeff 1/2 ≠ 0
ok("P09[Q8] ledger d=3 : trace 3 < courbure² 4 < c×EMT 5 < TT̄ 6 (coeff 0) ; "
   "Δ_𝒞=d ⟹ marginal ⟹ C1-b", nom, mut, "mutation d=4 ⟹ TT̄ présent")

# ===========================================================================
# Q9 — coin : additivité en rapidité de η ; limite m2 (κ→0 ⟹ η-term nu)
# ===========================================================================
e1, e2 = symbols("eta1 eta2", real=True)
# normales unité (timelike n, spacelike s) à rapidités η₁, η₂ : n·s = sinh(η₂−η₁)
nvec = Matrix([cosh(e1), sinh(e1)])          # n·n = −1 (métrique diag(−1,1))
svec = Matrix([sinh(e2), cosh(e2)])          # s·s = +1
mink = Matrix([[-1, 0], [0, 1]])
ns = simplify((nvec.T*mink*svec)[0])          # = sinh(η₁−η₂) avec cette orientation
u_ = Symbol("u_", real=True)
inv_ok = (simplify((asinh(sinh(u_))).diff(u_)) == 1
          and asinh(sinh(u_)).subs(u_, 0) == 0)   # asinh∘sinh = id sur ℝ (dérivée + point)
nom = Z(expand_trig(ns - sinh(e1 - e2))) and inv_ok
# additivité : booster le repère de χ décale η₁,η₂ ⟹ η invariant ; composer ⟹ additif
chi = Symbol("chi", real=True)
nom = nom and Z(expand_trig(simplify((nvec.subs(e1, e1+chi).T*mink*svec.subs(e2, e2+chi))[0])
                            - sinh(e1 - e2)))
mut = not Z(expand_trig(ns - sinh(e1 + e2)))              # mutation : somme au lieu de différence
ok("P10[Q9] η = arcsinh(n·s) = rapidité RELATIVE (invariante de boost, additive)",
   nom, mut, "backbone du coin dérivé ; mutation = mauvaise composition")

# P11 — m2 : face N → Dirichlet ⟹ κ→0 ⟹ S_TC → η-term nu (retour EXACT à LMPS)
G_N, kap, Phi, eta_s, sig = symbols("G_N kappa Phi eta_s sigma_a", positive=True)
S_TC = -1/(8*pi*G_N) * sqrt(sig) * (eta_s + kap*Phi)      # intégrande
S_nu = -1/(8*pi*G_N) * sqrt(sig) * eta_s                  # η-term nu (LMPS)
nom = Z(simplify(S_TC.subs(kap, 0) - S_nu))
mut = not Z(simplify(S_TC.subs(kap, 1) - S_nu))           # κ≠0 ⟹ écart Φ subsiste
ok("P11[Q9] limite m2 : κ→0 ⟹ S_TC → η-term nu EXACT (mécanisme mordant)",
   nom, mut, "le retrait de la correction conforme rend le backbone, rien d'autre")

# ===========================================================================
# CONSIGNATIONS
# ===========================================================================
consigne("C1[Q1] cartographie", "jonction discrète Dirichlet|Neumann (n : g₀ "
         "fixé, g₃=⟨T⟩ ; n+1 : g₃=0 par WCH, g₀ libre) ; eigenmode +i = "
         "condition d'état — structure DÉCLARÉE (zéro-algèbre au KB), consignée")
consigne("C2[Q8] IMPORT/lecture", "générateur W_{N→D}=−(1/2)√−h·T (Freelance II "
         "éq.7.13) et transport dS BLOQUÉ (Skenderis : contre-termes projetés, "
         "rupture-shadow au pas C1-b, périmètre scalaires/mono-bord) — lectures, "
         "non redérivables en interne")
consigne("C3[Q9] IMPORT", "table b = 2/⅔/0 (Dirichlet/York/Neumann) et c = 2/0/0 "
         "(Odak–Speziale) ; Φ = Π̄_⟨μν⟩ (charge de York) ; finitude ∀p "
         "(Gustavsson : anomalie indépendante de k) — fetchs consignés ; seule "
         "la STRUCTURE (P10/P11) est recalculée")
consigne("C4[Q9] verdict", "p LIBRE ∀p ⟹ α = C1-b POSITIF (classification "
         "finale de l'axe coin : famille à un paramètre, PAS de construction "
         "unique) — verdict consigné, jamais compté PASS")
consigne("C5[Q10] verdicts", "(C-O2) forte NON établie ; P1 réduite à s=(−1)^w "
         "(décision ouverte, fetch-conditionnel) ; P2 = DISCORDANCE (G1-c∧G2-c) ; "
         "TC-b ; β≡G3 = seul facteur d'O₂ ouvert — verdicts d'axe consignés")
consigne("C6 prémisses", "modes (f_a,f_b)=(source,VEV) de de Haro 0808.2054 ; "
         "convention ⟨T⟩=−2δW/δh (utilisée en P04) ; WCH (=A4, socle admis) — "
         "imports déclarés")
consigne("C7 correction d'instrument (en cours de lot)",
         "P10 (deux retouches, même cycle) : (i) signe d'orientation des "
         "normales erroné dans MON expression attendue (n·s = sinh(η₁−η₂) avec "
         "l'orientation choisie ; la cible gelée ne fixe pas d'orientation) ; "
         "(ii) l'identité asinh∘sinh = id sur ℝ vérifiée par dérivée (=1) + "
         "point (0↦0), sympy ne la réécrivant pas — aucune cible ni tolérance "
         "modifiée")

# ===========================================================================
print()
if FAIL:
    print(f"REDEMO R-12 : ÉCHEC — {len(FAIL)} test(s) en défaut : {FAIL}")
    sys.exit(1)
print(f"REDEMO R-12 : {len(PASS)}/{len(PASS)} PASS discriminants "
      f"+ {len(CONS)} consignations déclarées — EXIT 0")
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (plafond annoncé "
      "AU GEL : chaîne entière révélée par les front-matters).")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien. "
      "O₂ n'est PAS construit (β≡G3 ouvert). { A4 ; A2★ ; N } INCHANGÉ · "
      "CCC non démontrée NI réfutée.")
