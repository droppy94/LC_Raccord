#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_crossover_attracteur.py — PORTE (ii) : la sélection WCH (P=9k²/4) devient-elle
un ATTRACTEUR dynamique sous la back-réaction du bain de gravitons de Bunch-Davies ?

Compagnon proposé de LC-D3-CROSSOVER-ATTRACTEUR (à enregistrer si validé).
Étend verif_D3_crossover_stabilite.py (a3) + verif_D3_backreaction.py (a2) + verif_E_planck.py (N).

Squelette ÉTABLI (a3, sceau ré-exécuté PASS) :
    m' = 9k²/(4λ),  λ' = 4λ²m/(9k²)  ⟹  P=mλ conservé ; λ'=(P/P*)λ, P*=9k²/4.
    Point fixe NON-HYPERBOLIQUE : J → vp 1 double, défective (= candidat #5). SÉLECTION, pas attracteur.

Canal de back-réaction ÉTABLI (a2) :
    BR de Bunch-Davies ISOTROPE → part traceless nulle (⟨g₃^(2)⟩=0, pas de marée induite),
    part isotrope (ρ,p) RENORMALISE le fond λ(=Λ). Scaling ÉTABLI : δλ ~ H⁴ ~ λ².
    Coefficient/signe OUVERTS → régularisation UV ρ~∫dk k³ par coupure holographique N (LC-E).

Source paramétrée (Tâche 1) :   δλ_i = c(λ_i ; N) · λ_i²   (N = S_dS = 3π/(Λ ℓ_P²), Λ=λ).
Récurrence MODIFIÉE :
    m_{i+1} = 9k²/(4 λ_i) = P*/λ_i
    λ_{i+1} = (P_i/P*) λ_i + δλ(λ_i)
    P_{i+1} = m_{i+1} λ_{i+1} = P_i + (P*/λ_i) δλ(λ_i)     ← l'incrément qui pilote tout.
"""

import numpy as np

# =====================================================================================
#  CRITÈRE PRÉ-ENREGISTRÉ (CONSORT / LC-AUDIT-VERDICT §9) — FIGÉ AVANT TOUTE EXÉCUTION
# =====================================================================================
PRE_REGISTERED = """
CRITÈRE PRÉ-ENREGISTRÉ (figé 2026-06-08, AVANT exécution — non révisable après lecture des sorties) :

  Soit le point fixe candidat (m*,λ*) avec m*λ* = P* = 9k²/4. Il N'EST un point fixe
  de la récurrence modifiée QUE SI δλ(λ*)=0 (sinon P* n'est pas conservé : pas de fixe).

  VERDICT (sur la linéarisation 2D au point fixe, valeurs propres μ de J*) :
    • ATTRACTEUR  ⟺  P* est un point fixe ET max|μ| < 1
                     (équivaut à : sign(dP/déon) change +→− en traversant P*).
    • RÉPULSEUR   ⟺  max|μ| > 1   (ou P* n'est pas un point fixe et P dérive en s'éloignant).
    • NEUTRE      ⟺  max|μ| = 1   (marginal/centre : P orbite, ne converge pas — sélection
                     reste POSÉE, non dérivée).

  Les trois verdicts sont publiables (cf. LC-WORK-REPRISE-POST-FRONT-A §5).
  DISCIPLINE §6.4 : un 'attracteur' = la récurrence numérique converge, JAMAIS 'la WCH est prouvée'.
  Toute conclusion est CONDITIONNELLE à l'hypothèse N (holographique, 'à inventer' en l'état).
"""

# ---- paramètres fixes ----
k     = 1.0
Pstar = 9*k**2/4          # = 2.25
lam_s = 1.5               # λ* de référence (cohérent avec les exemples du sceau a3)
m_s   = Pstar/lam_s       # m* tel que m*λ* = P*
c0    = 0.05              # amplitude de back-réaction (perturbative, δλ/λ ~ c0·λ « petit »)

def banner(t): print("\n" + "="*86 + "\n " + t + "\n" + "="*86)

# =====================================================================================
#  Les TROIS closures pour c(λ;N).  N = S_dS = 3π/(Λ ℓ_P²), Λ=λ  ⟹  N ∝ 1/λ.
# =====================================================================================
#  douce   : coupure de Hubble (dark-energy holographique) ρ~Λ²  ⟹  c ≈ const (>0).
#  dure    : Cohen-Kaplan-Nelson ρ~M_P²Λ~Λ²N, N∝1/λ amplifie le bain  ⟹  c CROÎT avec λ.
#  balance : COMPÉTITION bain (λ↑) vs reset d'entropie de Weyl au crossover (λ↓ ; LC-E §5),
#            point d'équilibre en λ*  ⟹  c(λ)=c0(1−λ/λ*) change de signe en λ*.  [à inventer]
def dlam_douce  (lam): return c0 * lam**2
def dlam_dure   (lam): return c0 * (lam/lam_s) * lam**2          # c ∝ λ
def dlam_balance(lam): return c0 * (1.0 - lam/lam_s) * lam**2    # c s'annule en λ*

CLOSURES = [("douce  (coupure Hubble, ρ~Λ²)",            dlam_douce),
            ("dure   (CKN, ρ~Λ²N, N∝1/λ)",               dlam_dure),
            ("balance(bain vs reset Weyl, zéro en λ*)",   dlam_balance)]

# =====================================================================================
#  Récurrence (un pas) et Jacobien numérique 2D en variables (m,λ).
# =====================================================================================
def step(m, lam, dlam):
    mp  = Pstar/lam
    lp  = (m*lam/Pstar)*lam + dlam(lam)     # = (P/P*)λ + δλ,  P=mλ
    return mp, lp

def jacobian(m, lam, dlam, h=1e-6):
    # Jacobien ANALYTIQUE de  m'=P*/λ , λ'=mλ²/P*+δλ(λ).  δλ'(λ) par diff. centrée (scalaire, lisse).
    dprime = (dlam(lam+h) - dlam(lam-h))/(2*h)
    return np.array([[0.0,              -Pstar/lam**2],
                     [lam**2/Pstar,      2*m*lam/Pstar + dprime]])

def eig_trdet(J):
    """Valeurs propres d'une 2x2 via tr/det ; snap du discriminant quasi-nul (vp défective/Jordan)."""
    tr, dt = np.trace(J), np.linalg.det(J)
    disc = tr*tr - 4*dt
    if abs(disc) < 1e-9: disc = 0.0          # point de Jordan : μ = tr/2 double
    if disc >= 0:
        s = np.sqrt(disc);  return np.array([(tr+s)/2, (tr-s)/2])
    s = np.sqrt(-disc);     return np.array([(tr+1j*s)/2, (tr-1j*s)/2])

def classify(J):
    mu = eig_trdet(J)
    a  = np.max(np.abs(mu))
    if a > 1 + 1e-6:  lab = "RÉPULSEUR"
    elif a < 1 - 1e-6: lab = "ATTRACTEUR"
    else:             lab = "NEUTRE (marginal/centre)"
    return mu, a, lab

# =====================================================================================
#  EXÉCUTION
# =====================================================================================
print(PRE_REGISTERED)
print(f" Paramètres : k={k}, P*=9k²/4={Pstar}, λ*={lam_s}, m*={m_s}, c0={c0}")

# ---- [0] BASELINE conservatif (δλ=0) : doit reproduire a3 (det=1, μ=1 double) ----
banner("[0] BASELINE conservatif (δλ=0) — doit reproduire a3 : det=1, μ=1 double, NON-HYPERBOLIQUE")
J0 = jacobian(m_s, lam_s, lambda lam: 0.0)
mu0, a0, lab0 = classify(J0)
print(f"    J* =\n{J0}")
print(f"    det J* = {np.linalg.det(J0):.6f}   tr J* = {np.trace(J0):.6f}")
print(f"    valeurs propres μ = {np.round(mu0,6)}   |μ|max = {a0:.6f}  ⟹  {lab0}")
print("    ✓ cohérent avec LC-D3-CROSSOVER-STABILITE [3] (vp 1 double défective = candidat #5,")
print("      non-hyperbolique ⟹ NEUTRE : c'est bien une SÉLECTION, pas un attracteur).")

# ---- [1] OBSTRUCTION STRUCTURELLE : det J* = 1 pour TOUTE back-réaction sur λ seul ----
banner("[1] OBSTRUCTION STRUCTURELLE — det J* est-il modifié par δλ ?")
print("    m' = P*/λ ne dépend PAS de m  ⟹  ∂m'/∂m = 0, et det J* = −(∂m'/∂λ)(∂λ'/∂m) = 1")
print("    INDÉPENDAMMENT de δλ. Une BR isotrope ajoutée à λ' seul PRÉSERVE l'aire (det=1).")
print("    Conséquence : aucune valeur propre |μ|<1 possible ⟹ ATTRACTEUR linéaire IMPOSSIBLE")
print("    sans BRISER det=1 (il faudrait une BR DISSIPATIVE touchant aussi m'). [voir §[3]]")

# ---- [2] Les trois closures : point fixe ? Jacobien ? verdict ? itération directe ? ----
banner("[2] LES TROIS CLOSURES — application du critère pré-enregistré")
results = {}
for name, dlam in CLOSURES:
    print("\n  ----------------------------------------------------------------------------")
    print(f"  CLOSURE : {name}")
    fixe = abs(dlam(lam_s)) < 1e-12
    print(f"    δλ(λ*) = {dlam(lam_s):+.6e}  ⟹  P* est-il un point fixe ? {'OUI' if fixe else 'NON'}")
    if not fixe:
        # P* pas fixe : on regarde la dérive de P sur un pas, depuis (m*,λ*)
        mp, lp = step(m_s, lam_s, dlam)
        dP = mp*lp - Pstar
        verdict = "RÉPULSEUR (P* non fixe — P dérive)"
        print(f"    pas depuis (m*,λ*) : ΔP = {dP:+.4e}  (P s'éloigne de P* ⟹ pas d'attracteur)")
    else:
        J  = jacobian(m_s, lam_s, dlam)
        mu, a, verdict = classify(J)
        print(f"    det J* = {np.linalg.det(J):.6f}   tr J* = {np.trace(J):.6f}")
        print(f"    μ = {np.round(mu,6)}   |μ|max = {a:.6f}  ⟹  {verdict}")
    results[name] = verdict

    # itération directe (test 'sign(dP/déon) de part et d'autre de P*')
    print("    itération directe (200 éons), P0 = P*±0.1, λ0 = λ* :")
    for sgn, tag in [(+1, "P0>P*"), (-1, "P0<P*")]:
        P0 = Pstar + sgn*0.10
        m, lam = P0/lam_s, lam_s
        Ps = [P0]
        for _ in range(200):
            m, lam = step(m, lam, dlam)
            if not np.isfinite(lam) or lam > 1e12 or lam < 1e-12:
                Ps.append(np.nan); break
            Ps.append(m*lam)
        Pend = Ps[-1]
        if not np.isfinite(Pend):
            beh = "DIVERGE (runaway)"
        elif abs(Pend - Pstar) < 0.5*abs(P0-Pstar):
            beh = f"→ se rapproche de P* (P_fin={Pend:.4f})"
        elif abs(Pend - Pstar) > 2*abs(P0-Pstar):
            beh = f"→ s'éloigne de P* (P_fin={Pend:.4f})"
        else:
            beh = f"→ orbite/borné près de P* (P_fin={Pend:.4f})"
        print(f"        {tag} : {beh}")

# ---- [3] DIAGNOSTIC : ce qu'il faudrait pour un VRAI attracteur (triangle de stabilité) ----
banner("[3] DIAGNOSTIC — que faudrait-il pour un attracteur ? (condition de Schur 2D)")
print("    Pour |μ₁|,|μ₂|<1 (2x2) il faut le TRIANGLE de stabilité :  |tr|<1+det  ET  det<1.")
print(f"    Or au point fixe NON modifié : tr=2 (du bloc de Jordan : ∂λ'/∂λ=2mλ/P*=2), det=1.")
print("    ⟹ on est au SOMMET du triangle (tr=2=1+det). Il faut DESCENDRE tr ET det.")
print()
print("    (3a) un seul terme dissipatif sur m' :  m'=(P*/λ)(1+g(λ−λ*)/λ*)  ⟹ det=1−g, mais tr≈2.")
g = 0.30
def step_3a(m, lam):
    return (Pstar/lam)*(1 + g*(lam-lam_s)/lam_s), (m*lam/Pstar)*lam + dlam_balance(lam)
def jac(stepf, m, lam, h=1e-7):
    fm = (np.array(stepf(m+h,lam)) - np.array(stepf(m-h,lam)))/(2*h)
    fl = (np.array(stepf(m,lam+h)) - np.array(stepf(m,lam-h)))/(2*h)
    return np.array([[fm[0],fl[0]],[fm[1],fl[1]]])
J3a = jac(step_3a, m_s, lam_s); mu3a, a3a, lab3a = classify(J3a)
print(f"         g={g} : det={np.linalg.det(J3a):.3f}, tr={np.trace(J3a):.3f}, |μ|max={a3a:.3f} ⟹ {lab3a}")
print("         ⟹ INSUFFISANT : tr≈2 reste hors du triangle (saddle). Un δm seul ne dérive PAS A4.")
print()
print("    (3b) déformer AUSSI ∂λ'/∂λ (back-réaction freinant la croissance de λ) : tr ET det.")
# il faut q tel que ∂λ'/∂λ baisse : λ' = (P/P*)λ(1 − q(λ−λ*)/λ*) + δλ_balance
g2, q2 = 0.30, 0.60
def step_3b(m, lam):
    mp = (Pstar/lam)*(1 + g2*(lam-lam_s)/lam_s)
    lp = (m*lam/Pstar)*lam*(1 - q2*(lam-lam_s)/lam_s) + dlam_balance(lam)
    return mp, lp
J3b = jac(step_3b, m_s, lam_s); mu3b, a3b, lab3b = classify(J3b)
print(f"         g={g2}, q={q2} : det={np.linalg.det(J3b):.3f}, tr={np.trace(J3b):.3f}, |μ|max={a3b:.3f} ⟹ {lab3b}")
print("    ⟹ un attracteur EST atteignable EN PRINCIPE, mais SEULEMENT en déformant DEUX invariants")
print("       (det ET tr) du point fixe de Jordan — DEUX ingrédients holographiques NON fournis")
print("       par a2/a3/E. Conjecture pure, aucune dérivation. C'est le cœur du 'à inventer'.")

# ---- VERDICT ----
banner("VERDICT (porte ii) — selon le critère pré-enregistré, sans surclassement (§6.4)")
for name, v in results.items():
    print(f"    closure {name.split('(')[0].strip():9s} : {v}")
print("""
    SYNTHÈSE. Aucune des trois closures NATURELLES sur λ ne dérive A4 :
      • la structure de l'atlas est PRÉSERVATRICE D'AIRE (det J*=1) pour toute BR isotrope sur λ ;
      • douce/dure (BR de signe constant) ⟹ RÉPULSEUR / runaway (P* pas même un point fixe) ;
      • balance (compétition, zéro en λ*) ⟹ NEUTRE (centre marginal, |μ|=1 : P orbite, ne converge pas).
    La sélection P=9k²/4 RESTE POSÉE : la porte (ii) MINIMALE ne promeut pas la WCH en attracteur.
    A4 demeure un SOCLE. (A) reste 'formalisable' conditionnel à A2 — INCHANGÉ.
    Un attracteur exigerait de quitter le SOMMET du triangle de stabilité (tr=2, det=1) en
    déformant DEUX invariants (BR dissipative sur m' ET frein sur λ', §[3b]) : DEUX ingrédients
    'à inventer / hors de portée' (circularité N de LC-E non brisée). Résultat HONNÊTE et publiable.
""")
print("="*86)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
# Critere PRE-ENREGISTRE : baseline area-preserving (det J0=1) ; aucune closure naturelle
# sur λ ne derive A4 (aucun ATTRACTEUR). Encode le verdict CALCULE (porte ii).
assert np.isclose(np.linalg.det(J0), 1.0), "crossover_attracteur: baseline det J0=1 (area-preserving, a3)"
assert all("ATTRACTEUR" not in str(v).upper() for v in results.values()), "crossover_attracteur: aucune closure naturelle ne derive A4 (pas d'attracteur)"
print("EXIT 0 (F1: 2 assertions baseline+verdict verifiees)")
