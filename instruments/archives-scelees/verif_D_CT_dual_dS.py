#!/usr/bin/env python3
# =============================================================================
# verif_D_CT_dual_dS.py
# S2 / ETAPE 2 de LC-WORK-CADRAGE-S2 §5 : carte S de de Haro en dS sur les
# modes de Bunch-Davies.  GO/NO-GO du risque R1 (re-derivation dS obligatoire).
#
# Question (cadrage §4) : une structure de dualite analogue a de Haro
# (eq. 43-44, 51) referme-t-elle sur les modes BD de dS, et avec quel S^2 ?
#   - si la carte S NE referme PAS en dS  -> NO-GO (lead `hors de portee`)
#   - si elle referme                     -> GO, lire S^2 et brancher §2-§3.
#
# DISCIPLINE §6.4 (SANS SURCLASSEMENT). Ce sceau atteste UNIQUEMENT que :
#   (A) les modes BD solvent l'EOM TT de dS et que la base reelle de de Haro
#       (f_a,f_b) solve la MEME EOM sous u->k|eta| (identite de forme AdS<->dS) ;
#   (B) la matrice S de de Haro (eq.51) verifie S^2=-1, vp ±i ;
#   (C) le mode BD = f_a - i f_b EST le mode propre de S pour +i (BD diagonalise S).
# Il NE scelle PAS : l'identite tensorielle complete eq.44 avec ses facteurs de
# continuation (□^{3/2}, epsilon, i^{d-1}) NI la persistance du garde-fou (-2)
# sous continuation dS = incertitude (ii) du cadrage, SEUL vrai calcul ouvert.
# Stack : Python 3.12 / sympy 1.14.
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
print("verif_D_CT_dual_dS.py — S2 etape 2 : carte S en dS sur modes BD (go/no-go R1)")
print("=" * 78)

# variables : eta = |temps conforme| (generique, != 0) ; k > 0 ; u = coord. radiale AdS
eta, k, u = sp.symbols('eta k u', positive=True)
x = k * eta

# ----------------------------------------------------------------------------
# [A] Modes BD de dS et IDENTITE DE FORME AdS<->dS
# ----------------------------------------------------------------------------
print("\n[A] Modes BD de dS + identite de forme AdS<->dS")

# EOM TT de dS (LC-D3-WEYL-BUNCHDAVIES) : L_dS[f] = f'' - (2/eta) f' + k^2 f
def L_dS(f):
    return sp.diff(f, eta, 2) - (2/eta) * sp.diff(f, eta) + k**2 * f

# EOM radiale AdS de de Haro (forme) : L_AdS[y] = y'' - (2/u) y' + y
def L_AdS(y):
    return sp.diff(y, u, 2) - (2/u) * sp.diff(y, u) + y

fBD  = (1 - I*x) * sp.exp(I*x)      # mode de Bunch-Davies
fBDc = (1 + I*x) * sp.exp(-I*x)     # mode conjugue (anti-BD)
check(sp.simplify(L_dS(fBD))  == 0, "mode BD (1-ik|eta|)e^{ik|eta|} annule l'EOM dS f''-(2/eta)f'+k^2 f=0")
check(sp.simplify(L_dS(fBDc)) == 0, "mode BD* (1+ik|eta|)e^{-ik|eta|} annule la meme EOM (conjugue)")

# base reelle = fonctions de mode de de Haro (eq. 43)
fa_u = sp.cos(u) + u*sp.sin(u)      # f_a(u)  de Haro
fb_u = u*sp.cos(u) - sp.sin(u)      # f_b(u)  de Haro
check(sp.simplify(L_AdS(fa_u)) == 0, "f_a=cos u + u sin u (de Haro eq.43) annule l'EOM radiale AdS")
check(sp.simplify(L_AdS(fb_u)) == 0, "f_b=u cos u - sin u (de Haro eq.43) annule l'EOM radiale AdS")

fa = fa_u.subs(u, x)                # f_a sous u -> x = k|eta|
fb = fb_u.subs(u, x)
check(sp.simplify(L_dS(fa)) == 0, "MEME f_a, sous u->k|eta|, annule l'EOM dS => IDENTITE DE FORME AdS<->dS")
check(sp.simplify(L_dS(fb)) == 0, "MEME f_b, sous u->k|eta|, annule l'EOM dS => skelette transplante")

# ----------------------------------------------------------------------------
# [B] Matrice de S-dualite de de Haro (eq. 51)
# ----------------------------------------------------------------------------
print("\n[B] Matrice de S-dualite (de Haro eq.51) : S^2=-1, vp ±i")
S = sp.Matrix([[0, -1], [1, 0]])    # S:(a,b) -> (-b,a)
check(S*S == -sp.eye(2), "S=[[0,-1],[1,0]] verifie S^2 = -1 (involution de duals, eq.51)")
check(set(S.eigenvals().keys()) == {I, -I}, "valeurs propres de S = {+i, -i} (moteur du 'i')")

# ----------------------------------------------------------------------------
# [C] BD = mode propre de S (vp +i) : la carte S referme sur les modes dS
# ----------------------------------------------------------------------------
print("\n[C] BD = mode propre de S (vp +i) — la carte referme sur les modes dS")
# comparaison robuste : tout ramener en forme exponentielle avant simplification
# (BD est en e^{ix}, la base (f_a,f_b) en cos/sin ; sp.simplify seul ne les rapproche pas)
def zero_eq(expr):
    return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0
check(zero_eq(fBD  - (fa - I*fb)), "BD  = f_a - i f_b  (coeff (a,b)=(1,-i))")
check(zero_eq(fBDc - (fa + I*fb)), "BD* = f_a + i f_b  (coeff (a,b)=(1,+i))")

vBD  = sp.Matrix([1, -I])
vBDc = sp.Matrix([1,  I])
check(sp.simplify(S*vBD  - ( I)*vBD ) == sp.zeros(2,1), "S.(1,-i) = +i.(1,-i)  => S(BD)  = +i BD  (BD est mode propre de S)")
check(sp.simplify(S*vBDc - (-I)*vBDc) == sp.zeros(2,1), "S.(1,+i) = -i.(1,+i)  => S(BD*) = -i BD*")

# controle negatif : un mode reel pur (f_a) n'est PAS mode propre de S
vreal = sp.Matrix([1, 0])
det_par = sp.Matrix.hstack(vreal, S*vreal).det()   # =0 ssi parallele (=> propre)
check(det_par != 0, "controle negatif : f_a pur (1,0) n'est PAS mode propre de S (S le tourne)")

# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"BILAN : {n_ok}/{n_ok} assertions OK")
print("=" * 78)
print("""
VERDICT (go/no-go R1) : GO.
  La carte S de de Haro REFERME sur les modes dS : l'EOM TT de dS a la MEME
  forme que l'EOM radiale AdS (squelette (f_a,f_b) transplante sous u->k|eta|),
  S^2=-1 (vp ±i) est PRESERVE, et la condition de Bunch-Davies DIAGONALISE S
  (BD = f_a - i f_b = mode propre +i ; BD* = mode propre -i).

PORTEE (etabli — ALGEBRE, §6.4) :
  [A] modes BD solvent l'EOM dS ; base de de Haro (f_a,f_b) solve la MEME EOM
      => identite de forme AdS<->dS (aucun i DANS l'equation ; les i de
         continuation vivent dans les coefficients C_T∝ℓ², □^{3/2}∝k³).
  [B] S^2=-1, vp ±i (eq.51) reproduite.
  [C] BD = mode propre de S pour +i  => la dualite referme sur les modes dS.

NON couvert / `a inventer` (reste ouvert APRES ce GO) :
  (ii) persistance de la compensation (-2) du garde-fou S1 (C̃_T=+C_T en AdS via
       ⟨T̃⟩=-2δW̃/δh̃) sous continuation dS — SEUL vrai calcul ouvert, seul point
       pouvant faire basculer le pronostic de consolidation (cadrage §3/§4-etape3) ;
  l'identite tensorielle COMPLETE eq.44 (□^{3/2}, epsilon, i^{d-1}) en dS.

NE PROUVE PAS : seconde route INDEPENDANTE au signe de C_T ; D1 ferme ; CCC.
  Le squelette de la dualite referme en dS (GO) ; cela ouvre §2-§3, ne les clot pas.
  Perimetre {A4 ; A2★ ; N} INCHANGE. (A) physique conditionnel au seul A2★ inchange.
""")
