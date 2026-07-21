#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# RETIRÉ (R-7, 2026-06-15) — SCEAU INVALIDE. NE PAS rejouer comme sceau de
# continuité. Audit froid (2 passes convergentes) : ce script encode un PAS
# ILLÉGITIME — il importe le signe (−1)^Δ de l'inversion Δ↦−Δ (qui N'échange
# PAS les modes) et l'agrafe à la matrice du swap (réalisé par Δ↦d−Δ, sign-neutre).
# Sous la vraie opération d'échange : s=+1 ∀d. s=(−1)^d est un ARTEFACT.
# Conservé comme mémoire d'erreur. cf. LC-D-O2-BPRIME §R-7.
# ============================================================================
"""
verif_O2_bprime.py — LC-RACCORD. Sceau du chaînon LC-D-O2-BPRIME v0.1 (pivot O₂, étape b′).

OBJET (cadrage gelé LC-WORK-CADRAGE-O2-BPRIME v0.1, sha 0bd33386f6bb…) :
  trancher le signe résiduel s=(−1)^w isolé en (b) (LC-D-O2-P1), en DÉTERMINANT la
  PARITÉ du poids conforme w porté par la patte VEV→source de la map induite
  P=[[0,s],[1,0]] sous le facteur conforme NÉGATIF ω<0 de la réciprocité de Penrose Ω·ω=−1.

ENTRÉES KB-LOCAL (non re-dérivées, sourcées) :
  * Exposants radiaux FG du mode TT : équation indicielle z²H'' + (1−d)zH' = 0
    ⟹ racines {0, d} ⟹ Δ_-=0 (source g₀), Δ_+=d (VEV g₃=⟨T⟩).  [HOLOGRAPHIE-G3, verif_D_g3]
  * S-map scellée S=[[0,−1],[1,0]], S²=−𝟙, vp ±i.  [CT-DUAL S1/S2 ; de Haro 0808.2054 eq.50-51]
  * Réciprocité NÉGATIVE de Penrose Ω̂·Ω̌=−1.  [LC-A-D1-FACTEUR-CONFORME ; Cycles of Time, KB]
  * (b) : swap g₀↔g₃ ÉTABLI ; P=[[0,s],[1,0]], P²=s·𝟙, P=S ⟺ s=−1 ; involution NUE ⟹ s=+1.
    [LC-D-O2-P1 §2]

ARGUMENT (b′) — descente du signe via le GAP, INDÉPENDANTE du placement d'indices :
  s est un coefficient RELATIF entre les deux branches FG (Ω^{Δ_-} et Ω^{Δ_+}).
  Sous l'inversion de Penrose Ω ↦ ω = −1/Ω, une branche Ω^Δ devient
        ω^Δ = (−1/Ω)^Δ = (−1)^Δ · Ω^{−Δ},
  donc prend le facteur de signe (−1)^Δ. Le poids GLOBAL (placement d'indices, facteur a²
  d'ensemble) multiplie les DEUX pattes à l'identique ⟹ il se SIMPLIFIE dans le signe de s.
  Seul survit le signe RELATIF entre branches :
        s = (−1)^{Δ_+ − Δ_-} = (−1)^d            (car Δ_-=0).
  ⟹ w = Δ_+ − Δ_- = d   (parité = parité de d).

VERDICT GELÉ (cadrage §3) : d impair ⟹ s=−1 (P=S, concordance, gate P1 franchie) ;
  d pair ⟹ s=+1 (involution, discordance). Cas physique CCC : d=3 (impair) ⟹ s=−1.

FIREWALL (3 mutations cassantes obligatoires) :
  (m1) parité inversée  : (−1)^d ↦ (−1)^{d+1}  doit FAIRE BASCULER s à d=3.
  (m2) descente triviale : w forcé à 0 (s=(−1)^0=+1 ∀d) doit casser la concordance d=3.
  (m3) inversion POSITIVE : Ω·ω=+1 (branche Ω^Δ ↦ (+1)^Δ) ⟹ s=+1 ∀d, signe NON descendu.

SANS SURCLASSEMENT (§6.4) : s=−1 (d=3) franchit la SEULE gate P1 ; P2 reste `à inventer` ;
  A4 NON réduit ; D1 non clos ; N non fixé (≡Λ) ; {A4 ; A2★ ; N} INCHANGÉ.
"""

import sympy as sp

n_assert = 0
def check(cond, msg):
    global n_assert
    assert cond, "ÉCHEC : " + msg
    n_assert += 1

d, r, c, Omega, Delta = sp.symbols('d r c Omega Delta', positive=False)
print("=" * 78)
print("verif_O2_bprime.py — (b′) parité du poids conforme w ⟹ s=(−1)^d")
print("=" * 78)

# ----------------------------------------------------------------------
# [A] Exposants radiaux FG (mode TT) : équation indicielle ⟹ {0, d}.   [KB]
# ----------------------------------------------------------------------
dd = sp.symbols('dd')                       # d symbolique (positif entier en usage)
H = Omega**r                                 # essai de branche (Ω ~ 1/z)
# équation indicielle du mode TT : z²H'' + (1−d)zH' = 0  (verif_D_g3)
zz = sp.symbols('zz', positive=True)
Hz = zz**r
indicielle = sp.simplify((zz**2*sp.diff(Hz, zz, 2) + (1 - dd)*zz*sp.diff(Hz, zz)) / Hz)
racines = sp.solve(sp.Eq(indicielle, 0), r)
print("\n[A] indicielle FG :", sp.expand(indicielle), " ⟹ racines r =", racines)
check(set(racines) == {0, dd}, "racines FG doivent être {0, d}")
Delta_minus, Delta_plus = 0, dd
check(Delta_minus == 0, "Δ_- = 0 (source g₀)")
check(Delta_plus == dd, "Δ_+ = d (VEV g₃=⟨T⟩)")
print("    Δ_- =", Delta_minus, "(source) ; Δ_+ =", Delta_plus, "(VEV) ; gap =", Delta_plus - Delta_minus)

# ----------------------------------------------------------------------
# [B] Descente de Penrose : branche Ω^Δ ↦ (−1)^Δ Ω^{−Δ} sous Ω ↦ −1/Ω.
# ----------------------------------------------------------------------
def penrose_branch(D, sign_recip=-1):
    """Sous Ω ↦ sign_recip/Ω, la branche Ω^D devient (sign_recip)^D · Ω^{-D}.
       Renvoie le facteur de signe (sign_recip)^D."""
    return sp.Integer(sign_recip)**D

sig_minus = penrose_branch(Delta_minus, -1)          # branche source
sig_plus  = penrose_branch(Delta_plus,  -1)          # branche VEV
print("\n[B] sous Ω↦−1/Ω : branche Δ_- prend", sig_minus, "; branche Δ_+ prend (−1)^d")
# signe RELATIF (= s) : (−1)^{Δ_+} / (−1)^{Δ_-}
s_sign = sp.simplify(sig_plus / sig_minus)
check(sp.simplify(s_sign - (-1)**(Delta_plus - Delta_minus)) == 0,
      "signe relatif s = (−1)^{Δ_+−Δ_-}")
check(sp.simplify(s_sign - (-1)**dd) == 0, "s = (−1)^d (car Δ_-=0)")
w = Delta_plus - Delta_minus
print("    w = Δ_+ − Δ_- =", w, "  ⟹  s = (−1)^w = (−1)^d")

# ----------------------------------------------------------------------
# [C] Indépendance au placement d'indices : un poids GLOBAL c·(…) ne change pas sign(s).
#     Les deux pattes de P sont multipliées par le MÊME facteur d'ensemble (a², indices).
# ----------------------------------------------------------------------
cpos = sp.symbols('cpos', positive=True)
sig_plus_scaled  = cpos * sig_plus
sig_minus_scaled = cpos * sig_minus
s_sign_scaled = sp.simplify(sig_plus_scaled / sig_minus_scaled)
print("\n[C] poids global cpos>0 appliqué aux deux branches : s_scaled =", s_sign_scaled)
check(sp.simplify(s_sign_scaled - s_sign) == 0,
      "le poids global se simplifie : sign(s) inchangé (s relatif au gap)")

# ----------------------------------------------------------------------
# [D] Map induite P=[[0,s],[1,0]] ; carré ; comparaison à S.
# ----------------------------------------------------------------------
s = sp.symbols('s')                                  # gardé symbolique d'abord
P = sp.Matrix([[0, s], [1, 0]])
S = sp.Matrix([[0, -1], [1, 0]])
print("\n[D] P =", P.tolist(), " ; P² =", (P*P).tolist())
check(sp.simplify(P*P - s*sp.eye(2)) == sp.zeros(2), "P² = s·𝟙")
check(sp.simplify(S*S + sp.eye(2)) == sp.zeros(2), "S² = −𝟙 (référence scellée)")
# P = S  ⟺  s = −1
PmS = sp.simplify(P - S)
check(PmS == sp.Matrix([[0, s + 1], [0, 0]]), "P − S = [[0, s+1],[0,0]]")
check(sp.simplify((P - S).subs(s, -1)) == sp.zeros(2), "P = S ⟺ s = −1")
check(sp.simplify((P*P).subs(s, -1) + sp.eye(2)) == sp.zeros(2), "s=−1 ⟹ P² = −𝟙 = S²")

# ----------------------------------------------------------------------
# [E] Branchement parité de d : s=(−1)^d ⟹ d impair: concordance / d pair: discordance.
# ----------------------------------------------------------------------
print("\n[E] s(d) = (−1)^d :")
res = {}
for dv in [2, 3, 4, 5]:
    sval = int((-1)**dv)
    Pv = P.subs(s, sval)
    concordance = (sp.simplify(Pv - S) == sp.zeros(2))
    res[dv] = (sval, concordance)
    print(f"    d={dv} ({'impair' if dv%2 else 'pair'})  s={sval:+d}  P=S ? {concordance}")
check(res[3][0] == -1 and res[3][1] is True,  "d=3 ⟹ s=−1 ⟹ P=S (CONCORDANCE)")
check(res[5][0] == -1 and res[5][1] is True,  "d=5 (impair) ⟹ s=−1 ⟹ P=S")
check(res[2][0] == +1 and res[2][1] is False, "d=2 (pair) ⟹ s=+1 ⟹ P≠S (discordance)")
check(res[4][0] == +1 and res[4][1] is False, "d=4 (pair) ⟹ s=+1 ⟹ P≠S")

# cas physique CCC : d=3
s_phys = int((-1)**3)
print(f"\n    CAS PHYSIQUE CCC : d=3 ⟹ s={s_phys:+d} ⟹ P=S, P²=−𝟙=S² ⟹ (C-O2) forte ÉTABLIE (gate P1).")
check(s_phys == -1, "d=3 ⟹ s=−1")

# ======================================================================
# FIREWALL — 3 mutations cassantes
# ======================================================================
print("\n" + "=" * 78)
print("FIREWALL — 3 mutations cassantes")
print("=" * 78)
fw = 0

# (m1) parité inversée : (−1)^d ↦ (−1)^{d+1}
s_m1_d3 = int((-1)**(3 + 1))
P_m1 = P.subs(s, s_m1_d3)
broken_m1 = (sp.simplify(P_m1 - S) != sp.zeros(2))
print(f"  (m1) parité inversée (−1)^(d+1) : d=3 ⟹ s={s_m1_d3:+d}, P=S ? {not broken_m1}")
check(broken_m1, "(m1) parité inversée DOIT casser la concordance à d=3")
fw += 1

# (m2) descente triviale : w forcé à 0 ⟹ s=(−1)^0=+1 ∀d
s_m2 = int((-1)**0)
P_m2 = P.subs(s, s_m2)
broken_m2 = (sp.simplify((P_m2*P_m2) + sp.eye(2)) != sp.zeros(2))  # P²=+𝟙 ≠ −𝟙
print(f"  (m2) descente triviale w=0 : s={s_m2:+d}, P²=−𝟙 ? {not broken_m2}")
check(broken_m2, "(m2) descente triviale (w=0) DOIT donner P²=+𝟙 ≠ S²")
fw += 1

# (m3) inversion POSITIVE Ω·ω=+1 : branche Ω^Δ ↦ (+1)^Δ ⟹ s=+1 ∀d
sig_plus_pos  = penrose_branch(Delta_plus,  +1)
sig_minus_pos = penrose_branch(Delta_minus, +1)
s_m3 = sp.simplify(sig_plus_pos / sig_minus_pos)
print(f"  (m3) inversion positive Ω·ω=+1 : s = (+1)^d =", s_m3, "(signe NON descendu)")
check(sp.simplify(s_m3 - 1) == 0, "(m3) inversion positive ⟹ s=+1 ∀d (pas de descente du signe)")
# et à d=3 : casse la concordance
broken_m3 = (sp.simplify(P.subs(s, 1) - S) != sp.zeros(2))
check(broken_m3, "(m3) ⟹ P≠S à d=3 (concordance détruite si la réciprocité n'est pas négative)")
fw += 1

print(f"\n  Firewall : {fw}/3 mutations cassent comme attendu.")
check(fw == 3, "les 3 mutations firewall doivent casser")

# ======================================================================
print("\n" + "=" * 78)
print(f"OK — {n_assert} assertions. (b′) : w = Δ_+−Δ_- = d ⟹ s = (−1)^d.")
print("  Descente du signe via le GAP (poids global simplifié) ; réciprocité NÉGATIVE de Penrose.")
print("  d=3 (CCC, impair) ⟹ s=−1 ⟹ P=S, P²=−𝟙=S² ⟹ (C-O2) forte ÉTABLIE au niveau P1 (gate franchie).")
print("  SANS SURCLASSEMENT (§6.4) : franchit la SEULE gate P1 ; P2 reste `à inventer` ;")
print("  A4 NON réduit ; D1 non clos ; N non fixé ; {A4 ; A2★ ; N} INCHANGÉ. EXIT 0.")
print("=" * 78)
