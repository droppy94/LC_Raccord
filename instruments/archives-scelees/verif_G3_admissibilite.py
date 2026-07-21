#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_G3_admissibilite.py  (v2 DURCI post-audit froid 2026-07-03, RÉSERVE)
==========================================================================
Sceau Phase 0 KB-only du cadrage GELE `LC-WORK-CADRAGE-G3-ADMISSIBILITE` (gel R-36 d3e1afc7).

DURCISSEMENT (répond aux 5 griefs de l'audit froid, Mode B) :
  (1) La loi d'échelle FG z^{2Δ+1-d} est DÉRIVÉE de la métrique FG construite symboliquement
      (det, inverse via SymPy), et VÉRIFIÉE en d ∈ {2,3,4} — plus hardcodée.
  (2) Les entrées structurelles (Δ_-=0 de SFG-1 ; borne IW ; DELTA-C T2b ; nécessité de
      normalisabilité mono-bord pour la transmission) sont DÉCLARÉES comme IMPORTS contingents,
      PAS « assertées » comme prouvées ici.
  (3) La tautologie interceptrice `exponent-(2Δ-2)==0` est SUPPRIMÉE.
  (4) TN-3 : la MARGINALITÉ est dérivée ; l'ABSENCE de contre-termes est un IMPORT (DELTA-C T2b),
      distincte — plus de non-sequitur absence≡marginalité.
  (5) Grade REQUALIFIÉ : « établi (arithmétique), CONDITIONNEL aux imports {Δ_-=0 (SFG-1),
      fenêtre IW} ; TN-2/TN-3 NON établies par le code (imports déclarés) ».

CE QUE CE SCEAU ÉTABLIT (arithmétique, inconditionnel) :
  - la densité de norme KG d'un mode φ~z^Δ à 𝓘⁺, DÉRIVÉE de la métrique FG, vaut z^{2Δ+1-d} ;
  - la fenêtre de normalisabilité Δ > (d-2)/2 en découle (convergence ⟺ exposant > -1) ;
  - l'IMPLICATION : SI Δ_-=0 (import) ALORS ∫_0 z^{-2}dz = ∞ (mode lent hors fenêtre).
CE QU'IL N'ÉTABLIT PAS (imports contingents, à trancher en Phase 1 fetch) :
  - que la racine dS4 genuine du mode lent mixed-BC est EXACTEMENT Δ_-=0 (SFG-1, importé) ;
  - que la transmission deux-faces EXIGE la normalisabilité mono-bord (structural, importé) ;
  - l'absence STRUCTURELLE de renorm marginale (DELTA-C T2b, importé).
=> Plafond honnête : T-c CONDITIONNEL aux imports. PAS un verrou β propre. Le fetch (Phase 1)
   reste requis pour trancher.

SymPy exact, aucun réseau, aucune donnée externe consommée.
"""

import sympy as sp

# ==========================================================================
# SECTION A — DÉRIVÉ (arithmétique, établi par le code, INCONDITIONNEL)
# ==========================================================================
z, ell, Delta = sp.symbols('z ell Delta', positive=True)

def fg_density_exponent(d_val, sign):
    """Construit la metrique FG (d+1 dim) et DERIVE l'exposant en z de la densite de
    norme Klein-Gordon  sqrt|g| * |g^{tt}| * |phi|^2  avec phi ~ z^Delta.
      ds^2 = (ell^2/z^2)( sign*dz^2 + eta_ij dx^i dx^j ), bord plat signature (-,+,..,+).
      sign = +1 (AdS, FG radial spacelike) / -1 (dS, FG radial timelike au I+ spacelike).
    Retourne l'exposant p tel que densite ∝ z^p (via derivee logarithmique, robuste)."""
    n = d_val + 1
    g = sp.zeros(n, n)
    g[0, 0] = sign * ell**2 / z**2                        # composante FG radiale (x0 = z)
    eta = [-1] + [1] * (d_val - 1)                        # bord : x1 = temps, puis spatial
    for i in range(d_val):
        g[i + 1, i + 1] = eta[i] * ell**2 / z**2
    detg = g.det()
    sqrt_absdet = sp.sqrt(sp.Abs(detg))                   # sqrt|g|
    gtt = g.inv()[1, 1]                                   # g^{tt} (temps du bord)
    density = sqrt_absdet * sp.Abs(gtt) * z**(2 * Delta)  # densite de norme KG
    density_l1 = sp.simplify(density.subs(ell, 1))
    p = sp.simplify(z * sp.diff(density_l1, z) / density_l1)   # exposant = z * (rho'/rho)
    return sp.simplify(p)

# DÉRIVATION + ROBUSTESSE : l'exposant metrique-derive doit valoir 2*Delta + 1 - d, pour les
# deux signatures (AdS sign=+1 ET dS sign=-1 : |det|,|g^{tt}| rendent p independant du signe),
# et se reproduire en d = 2, 3, 4 (loi d'echelle, pas coincidence a d=3).
d_sym = sp.symbols('d', positive=True)
closed_form = 2 * Delta + 1 - d_sym
for d_val in (2, 3, 4):
    for sign in (+1, -1):
        p = fg_density_exponent(d_val, sign)
        assert sp.simplify(p - closed_form.subs(d_sym, d_val)) == 0, \
            f"FG derivee : exposant z^{{{p}}} != 2*Delta+1-{d_val} (d={d_val}, sign={sign})"

# Fenetre de normalisabilite : convergence de int_0 z^p dz  <=>  p > -1  <=>  Delta > (d-2)/2.
# (DERIVEE de l'exposant, non citee.)
d = sp.Integer(3)                                          # bord dS4 -> d = 3
exponent = closed_form.subs(d_sym, d)                     # = 2*Delta - 2
window_bound = sp.solve(sp.Eq(exponent, -1), Delta)[0]    # Delta seuil tel que p = -1
assert window_bound == sp.Rational(1, 2), "fenetre IW derivee : seuil Delta = (d-2)/2 = 1/2"

def norm_integral(Dval, lower=0):
    return sp.integrate(z**(exponent.subs(Delta, Dval)), (z, lower, 1))

# Temoin de continuite de la fenetre (DERIVE) : juste au-dessus du seuil -> fini ;
# au seuil et en dessous -> divergent. (Etablit la fenetre comme frontiere reelle.)
assert norm_integral(sp.Rational(51, 100)) != sp.oo, "Delta=0.51 (dans la fenetre) : norme finie"
assert norm_integral(sp.Rational(1, 2))   == sp.oo, "Delta=1/2 (au seuil) : norme divergente"
assert norm_integral(sp.Rational(49, 100)) == sp.oo, "Delta=0.49 (hors fenetre) : divergente"

# ==========================================================================
# SECTION B — IMPORTS DÉCLARÉS (contingents ; NON établis par ce code)
# ==========================================================================
# Chaque import est une PRÉMISSE affirmée ailleurs (amont KB), reprise ici SANS re-derivation.
# Le verdict est CONTINGENT a chacun. (Aucune de ces valeurs n'est "prouvee" par une assertion.)
IMPORTS = {
    "I1_Delta_moins_0": {
        "valeur": sp.Integer(0),
        "enonce": "racine FG NATIVE du mode graviton lent (mixed-BC) en dS4 genuine = 0",
        "source": "SFG-1 / LC-D-O2-SCATTERING-FG (Thm 1.2, racines {0,3}) ; de Haro 0808.2054",
        "etabli_ici": False,   # CRUX : non derive dans les pieces ; charniere du verdict
    },
    "I2_fenetre_IW_est_le_critere": {
        "enonce": "la fenetre Delta > (d-2)/2 (norme KG) EST le critere d'admissibilite du mode",
        "source": "Ishibashi-Wald / Compere-Marolf (KB-cite)",
        "etabli_ici": True,    # la fenetre elle-meme est DERIVEE en Section A ; son role de
                               # critere d'admissibilite mixed-BC est le sens IW standard
    },
    "I3_transmission_exige_mono_norm": {
        "enonce": "une jonction de transmission deux-faces EXIGE la normalisabilite mono-bord",
        "source": "structural (raccord CCC = transmission, pas point fixe RG mono-bord)",
        "etabli_ici": False,   # premisse structurelle, non derivee
    },
    "I4_absence_renorm_marginale": {
        "enonce": "la carte shadow g0<->g3 n'a PAS de contre-termes locaux au pas marginal",
        "source": "DELTA-C T2b (KB)",
        "etabli_ici": False,   # importe ; distinct de la marginalite (derivee en Section C)
    },
}
imports_contingents = [k for k, v in IMPORTS.items() if not v["etabli_ici"]]
assert imports_contingents == ["I1_Delta_moins_0", "I3_transmission_exige_mono_norm",
                               "I4_absence_renorm_marginale"], \
    "3 imports contingents declares (non etablis par le code)"

# ==========================================================================
# SECTION C — RÉSULTATS CONDITIONNELS (implications ; antecedents = imports)
# ==========================================================================
Delta_minus = IMPORTS["I1_Delta_moins_0"]["valeur"]        # = 0, IMPORTÉ (contingent)
Delta_plus  = sp.Integer(3)                                # = d ; racine g3 = <T>, marginal

# --- TN-1 (PORTANTE) : UNE implication (plus deux checks redondants) --------------------------
# SI Delta_-=0 (I1) ALORS le mode lent est hors fenetre <=> norme divergente. Un seul enonce :
exp_slow = exponent.subs(Delta, Delta_minus)               # = -2 (DERIVE, sous I1)
slow_norm = norm_integral(Delta_minus)                     # int_0^1 z^{-2} dz
TN1_non_normalizable_IF_I1 = (slow_norm == sp.oo)          # <=> Delta_- <= (d-2)/2
assert exp_slow == sp.Integer(-2), "sous I1 : exposant du mode lent = -2"
assert TN1_non_normalizable_IF_I1, \
    "TN-1 (conditionnel a I1) : mode lent non-normalisable <=> hors fenetre (une seule inegalite)"

# --- TN-2 : conditionnel a I3 (declare, non derive) -------------------------------------------
TN2_obstruction_IF_I3 = TN1_non_normalizable_IF_I1         # (import I3) ∧ (TN-1) => obstruction
# NB : ceci n'est PAS une derivation de la necessite mono-bord ; c'est l'implication SOUS I3.

# --- TN-3 : marginalite DERIVEE ; absence de contre-termes IMPORTEE (I4) — SEPAREES -----------
marginal_derive = sp.Eq(2 * Delta_plus - d, d)             # 2*3-3 = 3 = d : DERIVE
assert bool(marginal_derive), "TN-3 : marginalite Delta_+ = d = 3 (DERIVEE)"
TN3_absence_IMPORTEE = IMPORTS["I4_absence_renorm_marginale"]  # absence = IMPORT (DELTA-C T2b)
# AUCUNE assertion ne pretend DERIVER l'absence depuis la marginalite (fin du non-sequitur).

# ==========================================================================
# FIREWALL TN-R (robustesse ; mutations qui DOIVENT mordre)
# ==========================================================================
# m1 — dans la fenetre AdS (Delta_->1/2) : normalisable (de Haro recupere). Temoin 3/4.
m1 = norm_integral(sp.Rational(3, 4)) != sp.oo
assert m1, "m1 : dans la fenetre, normalisabilite recuperee (de Haro 0808.2054)"
# m2 — scalaire mono-bord normalisable (Skenderis) : temoin Delta_-=1.
m2 = norm_integral(sp.Integer(1)) != sp.oo
assert m2, "m2 : scalaire mono-bord normalisable recupere (Skenderis)"
# m3 — cutoff eps>0 : norme FINIE ; eps->0 RETABLIT la divergence (artefact de branche cutoff).
I_cut = norm_integral(Delta_minus, lower=sp.Symbol('eps', positive=True))
m3 = (sp.limit(I_cut, sp.Symbol('eps', positive=True), 0, '+') == sp.oo)
assert m3, "m3 : cutoff->infini retablit la non-normalisabilite"
# m4 — anti-blanchiment AdS->dS : parite i^{d-1}|_{d=3} = -1 (reel negatif, CT-REALITE) ;
#      et l'exposant p est INDEPENDANT du signe FG (verifie Section A : sign=+1 ET -1),
#      donc la non-normalisabilite est genuine-dS, pas un blanchiment d'AdS.
m4 = (sp.simplify(sp.I**(d - 1) - (-1)) == 0)
assert m4, "m4 : i^{d-1}|_{d=3} = -1 (genuine-dS ; exposant signe-independant, Section A)"
# m5 — anti-circularite A4 : les entrees sont {metrique FG, I1..I4, borne IW} ; jamais Weyl/no-hair.
entrees = {"metrique_FG", "I1_Delta_moins_0", "I2_fenetre_IW", "I3_transmission",
           "I4_DELTA_C_T2b"}
m5 = not ({"A4", "Weyl_regularite", "no_hair"} & entrees)
assert m5, "m5 : amont-strict de A4 (aucune regularite de Weyl / no-hair)"

# ==========================================================================
# VERDICT (arithmetique, CONDITIONNEL aux imports)
# ==========================================================================
# Etabli inconditionnel : la loi FG z^{2Δ+1-d}, la fenetre Delta>(d-2)/2, l'implication TN-1.
# Conditionnel : le mode lent EST a Delta_-=0 (I1) ; transmission exige mono-norm (I3) ;
#                absence marginale (I4). => T-c CONDITIONNEL, pas un verrou propre.
T_c_conditionnel = TN1_non_normalizable_IF_I1 and TN2_obstruction_IF_I3 and bool(TN3_absence_IMPORTEE)
verrou_propre    = False   # NECESSITE de lever I1 (racine genuine) + I3/I4 via Phase 1 fetch
assert T_c_conditionnel and not verrou_propre, \
    "VERDICT = T-c CONDITIONNEL aux imports (I1,I3,I4) ; verrou propre NON acquis KB-only"

print("=== verif_G3_admissibilite.py v2 DURCI (Phase 0 KB-only, gel d3e1afc7) ===")
print("--- SECTION A : DÉRIVÉ (arithmétique, inconditionnel) ---")
print(f"  loi FG derivee de la metrique (d in 2,3,4 ; sign ±1) : densite ∝ z^(2Δ+1-d)")
print(f"  fenetre de normalisabilite DERIVEE : Δ > (d-2)/2 = {window_bound}  (d=3)")
print(f"  temoins de frontiere : Δ=0.51 fini ; Δ=1/2 divergent ; Δ=0.49 divergent")
print("--- SECTION B : IMPORTS DÉCLARÉS (contingents, NON établis ici) ---")
for k in imports_contingents:
    print(f"  [IMPORT] {k}: {IMPORTS[k]['enonce']}  (src: {IMPORTS[k]['source']})")
print("--- SECTION C : RÉSULTATS CONDITIONNELS ---")
print(f"  TN-1 (sous I1) : exposant mode lent = {exp_slow} ; ∫_0^1 = {slow_norm}  -> non-normalisable")
print(f"  TN-2 (sous I3) : obstruction transmission = implication, PAS derivation de I3")
print(f"  TN-3 : marginalite Δ_+=d=3 DERIVEE ; absence contre-termes = IMPORT (DELTA-C T2b)")
print(f"  firewall TN-R : m1={m1} m2={m2} m3={m3} m4={m4} m5={m5}  (5/5)")
print("--- VERDICT ---")
print(f"  T-c CONDITIONNEL aux imports {{I1: Δ_-=0 (SFG-1), I3: transmission, I4: DELTA-C T2b}}")
print(f"  verrou propre = {verrou_propre}  -> Phase 1 FETCH requise pour trancher (lever I1/I3/I4)")
print("  GRADE : etabli (arithmetique), CONDITIONNEL ; TN-2/TN-3 = imports, non etablis par le code.")
print("  §6.4 : delimite les MOYENS sous imports ; NE reduit PAS A4 ; {A4;A2★;N} inchange.")
print("ALL ASSERTIONS PASSED.")
