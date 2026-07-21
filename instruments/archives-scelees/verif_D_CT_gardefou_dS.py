#!/usr/bin/env python3
# =============================================================================
# verif_D_CT_gardefou_dS.py
# S2 / ETAPE 3 de LC-WORK-CADRAGE-S2 §5 : PERSISTANCE du garde-fou de signe
# sous continuation dS  =  leve l'incertitude (ii) du cadrage.
#
# Question (cadrage §4 etape 3, SEUL vrai calcul ouvert) : en AdS, C̃_T=+C_T
# car le `-` relatif de W̃=-W (eq.61-62) est compense par le `-2` de
# ⟨T̃⟩=-2 δW̃/δh̃ (eq.63). Cette compensation SURVIT-elle a la continuation dS ?
#   - si OUI  -> branche 1 (α de §3), source UNIQUE du signe, dual confirmatoire
#               => CONSOLIDATION (PAS de seconde route, PAS de reduction du compte) ;
#   - si NON (break non prevu) -> une route pourrait exister (espace non clos par decret).
#
# RESULTAT : PERSISTANCE. Le garde-fou survit (branche 1). Etabli SOUS DEUX INTRANTS :
#   (1) regle de continuation de REALITE : i^{d-1} agit SEULEMENT sur le prefacteur
#       ℓ^{d-1} de C_T (etabli, scelle LC-D-CT-REALITE) ;
#   (2) ℓ-INDEPENDANCE des facteurs de dictionnaire dual : le `-2` (eq.63) et le `-`
#       relatif (eq.61-62) viennent de la structure de Legendre (eq.66), SANS ℓ
#       => non continues. (Lecture de de Haro eq.61-63/66.)
# GIVEN (1)+(2), la persistance est une CONSEQUENCE ALGEBRIQUE (ce sceau la prouve),
# avec firewall par injection d'erreur montrant qu'elle est SENSIBLE (peut echouer).
#
# DISCIPLINE §6.4 (SANS SURCLASSEMENT) : `etabli (algebre)` de la persistance GIVEN
# (1)+(2) ; la validite PHYSIQUE de (2) sous continuation dS complete (structure de
# Legendre eq.66 en dS) reste `decision ouverte` / `a inventer` -- residu delimite.
# NE PROUVE PAS : seconde route ; D1 ferme ; CCC. Stack : Python 3.12 / sympy 1.14.
# =============================================================================

import sympy as sp

I = sp.I
n_ok = 0
def check(cond, msg):
    global n_ok
    assert bool(cond), "ECHEC: " + msg
    print("  [OK] " + msg)
    n_ok += 1

print("=" * 78)
print("verif_D_CT_gardefou_dS.py — S2 etape 3 : persistance du garde-fou en dS (leve (ii))")
print("=" * 78)

d = sp.Integer(3)  # S2 reste en d=3 (toujours citer la dimension)

# ----------------------------------------------------------------------------
# [A] Structure de signe du garde-fou EN AdS (rappel S1, deja scelle dual.py)
# ----------------------------------------------------------------------------
print("\n[A] Garde-fou EN AdS (rappel S1) : C̃_T = +C_T")
cW   = sp.Integer(+1)   # signe du coeff ℓ²/κ² de W  (eq.61)
cWt  = sp.Integer(-1)   # signe du coeff ℓ²/κ² de W̃ (eq.62) : `-` RELATIF (W̃=-W)
defT  = sp.Integer(+2)  # ⟨T⟩  = +2 δW/δh   (definition standard)
defTt = sp.Integer(-2)  # ⟨T̃⟩ = -2 δW̃/δh̃ (eq.63) : le `-2` du dictionnaire dual

CTT_AdS   = defT  * cW    # signe de ⟨TT⟩   ∝ +2·(+) = +
CTtTt_AdS = defTt * cWt   # signe de ⟨T̃T̃⟩ ∝ -2·(-) = +
check(CTT_AdS  > 0, "⟨TT⟩  coeff > 0 en AdS (C_T electrique)")
check(CTtTt_AdS > 0, "⟨T̃T̃⟩ coeff > 0 en AdS (C̃_T dual) : le `-` de W̃ compense par le `-2`")
check(sp.sign(CTtTt_AdS) == sp.sign(CTT_AdS), "garde-fou S1 : sign(C̃_T)=sign(C_T) en AdS")
ratio_AdS = sp.Rational(CTtTt_AdS, CTT_AdS)
check(ratio_AdS == 1, "rapport C̃_T/C_T = +1 en AdS")

# ----------------------------------------------------------------------------
# [B] Regle de continuation de REALITE : i^{d-1} agit SEULEMENT sur ℓ^{d-1}
# ----------------------------------------------------------------------------
print("\n[B] Continuation REALITE : facteur i^{d-1} sur le prefacteur ℓ^{d-1} (et lui seul)")
fcont = I**(d - 1)                      # i^{d-1}
check(fcont == -1, "i^{d-1} = i^2 = -1 en d=3 (REALITE : C_T -> reel negatif)")
# branche 1 (dualite standard, dual 'meme forme' eq.90) : C̃_T porte le MEME ℓ^{d-1}
pow_CT  = d - 1     # C_T  ∝ ℓ^{d-1}        (REALITE)
pow_CTt = d - 1     # C̃_T ∝ ℓ^{d-1} aussi  (branche 1, eq.90 'same form')
check(pow_CT == pow_CTt, "branche 1 : C_T et C̃_T portent la MEME puissance ℓ^{d-1} => MEME i^{d-1}")
# les facteurs de dictionnaire dual ne portent AUCUNE puissance de ℓ :
pow_defTt = sp.Integer(0)   # le `-2` (eq.63)  : facteur de dictionnaire, 0 puissance de ℓ
pow_cWt   = sp.Integer(0)   # le `-` relatif (eq.61-62) : idem, 0 puissance de ℓ
check(pow_defTt == 0 and pow_cWt == 0, "`-2` (eq.63) et `-` relatif (eq.61-62) : 0 puissance de ℓ => NON continues")

# ----------------------------------------------------------------------------
# [C] PERSISTANCE : appliquer i^{d-1} aux DEUX (meme puissance ℓ^{d-1})
# ----------------------------------------------------------------------------
print("\n[C] Persistance du garde-fou sous continuation dS")
CTT_dS   = fcont * CTT_AdS     # ⟨TT⟩   continue
CTtTt_dS = fcont * CTtTt_AdS   # ⟨T̃T̃⟩ continue (MEME fcont, branche 1)
check(CTT_dS   < 0, "C_T  reel negatif en dS (d=3) : coherent REALITE")
check(CTtTt_dS < 0, "C̃_T reel negatif en dS (d=3)")
check(sp.sign(CTtTt_dS) == sp.sign(CTT_dS), "GARDE-FOU PERSISTE : sign(C̃_T)=sign(C_T) en dS")
ratio_dS = sp.simplify(CTtTt_dS / CTT_dS)
check(ratio_dS == ratio_AdS, "rapport C̃_T/C_T = +1 en dS == AdS (i^{d-1} se simplifie : rapport INVARIANT)")
# MECANISME : le rapport = (defTt·cWt)/(defT·cW), independant de fcont
ratio_mech = sp.Rational(defTt * cWt, defT * cW)
check(ratio_mech == ratio_dS, "MECANISME : rapport = (defTt·cWt)/(defT·cW), independant de i^{d-1}")

# ----------------------------------------------------------------------------
# [D] FIREWALL par injection d'erreur : un break exigerait un i sur le `-2`/relatif
# ----------------------------------------------------------------------------
print("\n[D] Firewall (injection d'erreur) : la persistance est SENSIBLE (peut echouer)")
# scenario errone : on continue (a tort) le `-2` (ou le `-` relatif) avec un i^{d-1}
ratio_spurious = sp.simplify(fcont * ratio_dS)   # = -1 : C̃_T = -C_T (BREAK)
check(ratio_spurious == -1, "scenario break (i errone sur le `-2`) : rapport -> -1 (C̃_T=-C_T)")
check(ratio_spurious != ratio_dS, "FIREWALL : break (-1) != persistance (+1) => resultat SENSIBLE, non tautologique")

# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"BILAN : {n_ok}/{n_ok} assertions OK")
print("=" * 78)
print("""
VERDICT (etape 3, leve (ii)) : PERSISTANCE.
  Le garde-fou de signe SURVIT a la continuation dS (branche 1) : C̃_T=+C_T reste
  vrai (les deux reels negatifs en d=3). Le facteur i^{d-1} agit identiquement sur
  C_T et C̃_T (meme puissance ℓ^{d-1}) et se simplifie dans le rapport ; le `-2`
  (eq.63) et le `-` relatif (eq.61-62), sans ℓ, ne sont PAS continues.
  => branche (α) du cadrage §3 : SOURCE UNIQUE du signe, dual CONFIRMATOIRE,
     PAS de seconde route independante => CONSOLIDATION.
  Firewall : injecter un i sur le `-2` basculerait a C̃_T=-C_T (break) => le
  resultat est SENSIBLE et pourrait echouer ; il ne le fait pas car le `-2` vient
  du dictionnaire de Legendre (eq.66), sans ℓ.

PORTEE (etabli — ALGEBRE, §6.4) GIVEN deux intrants :
  (1) regle de continuation de REALITE (i^{d-1} sur ℓ^{d-1} seul) — ETABLI, scelle ;
  (2) ℓ-independance des facteurs de dictionnaire dual (`-2` eq.63 ; `-` relatif
      eq.61-62) — LECTURE de de Haro eq.61-63/66.
  GIVEN (1)+(2), la persistance du garde-fou est une CONSEQUENCE algebrique (prouvee).

RESIDU `a inventer` / `decision ouverte` (NON scelle) :
  la validite PHYSIQUE de (2) sous continuation dS COMPLETE — i.e. la structure de
  Legendre (eq.66) se continue-t-elle sans injecter de ℓ-dependance dans le `-2`/
  le `-` relatif ? Aucune indication de break ; mais ce n'est pas scelle.

COHERENCE : aucune contradiction avec REALITE (C_T(d=3)=-N/(32π²) reel negatif) ni
  avec LECTURE-EQ65 (branche 2 ∝ℓ^{-2} -> i^{-2}=-1, aussi reel negatif, non
  independante). Les deux branches retombent sur la source unique du signe.

NE PROUVE PAS : seconde route INDEPENDANTE ; D1 ferme ; CCC. Perimetre {A4 ; A2★ ; N}
  INCHANGE. (A) physique conditionnel au seul A2★ inchange. Le pronostic §3
  (consolidation) est CONFIRME, pas dementi.
""")
