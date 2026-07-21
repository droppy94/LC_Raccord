#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
#  verif_naction_gamma_dHSS.py
#  LC-RACCORD — front « verrou M_Pl^2/4 », RESSERRÉ à la map opérateur gamma.
#  Exécute R-2 « dérivation ab initio de la map opérateur » (formalisable, dHSS).
#
#  OBJET. Trancher si gamma=1 (=> N_action=1/4) est FORCÉ ou CONVENTIONNEL, en
#  dérivant la map opérateur <TT> = gamma * psi2 depuis l'action holographique
#  renormalisée (de Haro 0808.2054, éq. 61/63/90) + variation seconde.
#
#  RÉSULTAT (établi, algèbre ; cf. LC-AUDIT-LOG-NACTION-ALPHA §AF, DUAL §4 v0.4) :
#    - SÉPARATION beta/gamma : le spectre P=1/(2|Im F|)=2H^2/(M_Pl^2 k^3) FORCE
#      la magnitude beta=M_Pl^2/4, INDÉPENDAMMENT de gamma (spectre aveugle à gamma).
#    - MAP CANONIQUE FORCÉE : la définition universelle T_ij=(2/√g) δW/δg^ij,
#      appliquée DEUX fois (éq. 63), donne <TT>_canon = 4 * psi2 (psi2 = δ²W = coeff.
#      nu de fonction d'onde) => gamma_canon = 4. Les deux « 2 » sont la définition
#      de T (Brown-York), PAS un choix => reproduit éq. 90 <TT>=ell^2/kappa^2=8 c_W.
#    - N_action = gamma/4. gamma=4 => N_action=1 => C_T^prog = C_T^dH (même objet).
#                           gamma=1 => N_action=1/4 => C_T^prog = (1/4) C_T^dH (nu).
#    - VERDICT : gamma=1 n'est PAS forcé ; c'est la normalisation NU (O=T/2),
#      un CHOIX d'opérateur. Le canonique forcé est gamma=4. N_action=1/4 = étiquette
#      de convention « opérateur nu », à libeller comme telle.
#
#  FIREWALL. gamma=4 est l'UNIQUE valeur reproduisant l'éq. 90 (ell^2/kappa^2) :
#    une définition fausse de T (1 ou 3 facteurs δW/δg au lieu de 2) casse éq. 90.
#    => le résultat est SENSIBLE (non tautologique).
#
#  §6.4. « gamma=4 (canonique) / gamma=1 (convention nue) » ≠ « D1 fermé / N fixé /
#  CCC démontrée ». Aucune contradiction, PAS de NO-GO. {A4 ; A2★ ; N} INCHANGÉ ;
#  D1 non clos ; N non fixé ; CCC non démontrée.
#
#  Stack : Python 3.12 / sympy 1.14.
# =============================================================================

import sympy as sp

OK = 0
def must(cond, label):
    global OK
    assert cond, f"ÉCHEC : {label}"
    OK += 1
    print(f"  [ok] {label}")

def section(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74)

pi = sp.pi
# symboles strictement positifs / réels
ell, kappa, k, H, M_Pl2, h = sp.symbols('ell kappa k H M_Pl2 h', positive=True)
beta, gamma = sp.symbols('beta gamma', positive=True)   # magnitude et map, LIBRES

# -----------------------------------------------------------------------------
section("[A]  CHAÎNE DE HARO (éq. 61->63->90) — variation seconde de l'action")
# -----------------------------------------------------------------------------
# éq. 61 : W = c_W ∫ h □^{3/2} h   (action holographique renormalisée de bord).
#          en impulsion, □^{3/2} -> k^3 ; on travaille avec le COEFFICIENT.
c_W = ell**2 / (8 * kappa**2)
print(f"  c_W = ell^2/(8 kappa^2) = {c_W}   (coeff. de h k^3 h dans W, éq. 61)")

# La forme quadratique W = c_W * h^2 * k^3 (coeff.). Variation seconde NUE :
W_quad = c_W * h**2          # le k^3 est porté à part (structure), on suit le coeff.
psi2 = sp.diff(W_quad, h, 2) # δ²W/δh² = 2 c_W  ==> coeff. NU de fonction d'onde
must(sp.simplify(psi2 - 2*c_W) == 0,
     "psi2 = δ²W/δh² = 2 c_W   (coeff. NU de fonction d'onde = lecture programme)")

# DÉFINITION UNIVERSELLE du tenseur de stress (éq. 63) : T = 2 δW/δh, appliquée 2x.
# <T>  = 2 δW/δh
# <TT> = 2 δ<T>/δh = 2 * 2 * δ²W/δh²
T1   = 2 * sp.diff(W_quad, h)            # <T>  = 2 δW/δh = 4 c_W h
TT   = 2 * sp.diff(T1, h)                # <TT> = 2 δ<T>/δh = 8 c_W
C_T_dH = sp.simplify(TT)
must(sp.simplify(C_T_dH - 8*c_W) == 0,
     "<TT>_canon = 2 δ(2 δW/δh)/δh = 8 c_W   (chaîne 2x2x2, éq. 63 deux fois)")
must(sp.simplify(C_T_dH - ell**2/kappa**2) == 0,
     "<TT>_canon = ell^2/kappa^2   (= éq. 90 de de Haro, reproduite)")

# -----------------------------------------------------------------------------
section("[B]  MAP OPÉRATEUR gamma = <TT>_canon / psi2   (FORCÉE par éq. 63)")
# -----------------------------------------------------------------------------
gamma_canon = sp.simplify(C_T_dH / psi2)
must(gamma_canon == 4,
     "gamma_canon = <TT>_canon / psi2 = 8c_W / 2c_W = 4   (FORCÉ : les deux 2 de éq.63)")
# Les deux 2 sont la DÉFINITION de T (Brown-York), pas une convention.
# (Le 2 de la dérivée seconde de la forme quadratique est COMMUN aux deux côtés.)
print("  -> les deux facteurs 2 (T=2δW/δg appliqué deux fois) = définition de T,")
print("     PAS un choix => gamma=4 reproduit éq.90 ; c'est la map CANONIQUE.")

# -----------------------------------------------------------------------------
section("[C]  N_action = gamma/4  ;  lecture canonique vs lecture nue")
# -----------------------------------------------------------------------------
# Relation de la sonde (LC-WORK-REPRISE-POST-AUDIT-FROID §3) :
#   <TT> = gamma * psi2 ;  C_T^prog = gamma * (psi2/N)  ;  f_W = C_T^dH/C_T^prog = 4/gamma
#   N_action = 1/f_W = gamma/4.
C_T_prog = gamma * psi2                       # map programme générale
f_W = sp.simplify(C_T_dH / C_T_prog)
must(sp.simplify(f_W - 4/gamma) == 0,
     "f_W = C_T^dH/C_T^prog = 4/gamma   (symbolique)")
N_action = sp.simplify(1/f_W)
must(sp.simplify(N_action - gamma/4) == 0,
     "N_action = 1/f_W = gamma/4   (re-vérifié symboliquement)")

# Canonique gamma=4 :
must(sp.simplify(N_action.subs(gamma, 4) - 1) == 0,
     "gamma=4 (canonique) => N_action=1   (C_T^prog = C_T^dH : MÊME objet)")
must(sp.simplify((C_T_prog.subs(gamma, 4)) - C_T_dH) == 0,
     "gamma=4 => C_T^prog = C_T^dH = ell^2/kappa^2   (cohérence, f_W=1)")
# Nu gamma=1 (posé par le programme) :
must(sp.simplify(N_action.subs(gamma, 1) - sp.Rational(1, 4)) == 0,
     "gamma=1 (opérateur nu O=T/2) => N_action=1/4   (étiquette de CONVENTION)")
must(sp.simplify((C_T_prog.subs(gamma, 1)) - C_T_dH/4) == 0,
     "gamma=1 => C_T^prog = (1/4) C_T^dH   (lecture NU, non-canonique)")

# Recoupement valeurs scellées /N (1/(8pi^2) canonique ; 1/(32pi^2) nu) :
CTdH_over_N = sp.Rational(1, 8) / pi**2
must(sp.simplify(CTdH_over_N*4 - sp.Rational(1, 8)/pi**2*4) == 0, "garde de cohérence triviale")
ratio_seale = sp.simplify((sp.Rational(1,8)/pi**2) / (sp.Rational(1,32)/pi**2))
must(ratio_seale == 4,
     "(1/8pi^2)/(1/32pi^2) = 4   (de Haro/programme = 4 = f_W à gamma=1, recoupe CT-ATN/DUAL)")

# -----------------------------------------------------------------------------
section("[D]  SÉPARATION beta/gamma — le spectre FORCE beta, AVEUGLE à gamma")
# -----------------------------------------------------------------------------
# Partie finie de F : |Im F|/k^3 = beta/H^2 (beta = magnitude, LIBRE).
# Prescription dS/CFT du programme : P = 1/(2 |Im F|).
ImF = beta * k**3 / H**2                       # |Im F| = beta k^3 / H^2 (structure k^3)
P_T = sp.simplify(1/(2*ImF))
must(sp.simplify(P_T - H**2/(2*beta*k**3)) == 0,
     "P = 1/(2|Im F|) = H^2/(2 beta k^3)   (prescription programme)")
# Exiger le spectre tensoriel standard P = 2 H^2/(M_Pl^2 k^3) :
sol_beta = sp.solve(sp.Eq(P_T, 2*H**2/(M_Pl2*k**3)), beta)
must(len(sol_beta) == 1 and sp.simplify(sol_beta[0] - M_Pl2/4) == 0,
     "P = 2H^2/(M_Pl^2 k^3) => beta = M_Pl^2/4 UNIQUEMENT (magnitude FORCÉE)")
# Le spectre ne contient pas gamma : aveugle à la map opérateur.
must(gamma not in P_T.free_symbols and gamma not in sp.Eq(P_T, 2*H**2/(M_Pl2*k**3)).free_symbols,
     "le spectre ne dépend PAS de gamma => beta et gamma sont DISJOINTS")

# -----------------------------------------------------------------------------
section("[E]  FIREWALL — gamma=4 est l'UNIQUE valeur reproduisant éq. 90")
# -----------------------------------------------------------------------------
# On injecte des définitions FAUSSES de T : n facteurs (δW/δg) au lieu de 2.
# T(n) : <TT> = n * δ(n δW/δh)/δh = n^2 δ²W/δh^2 = n^2 * psi2.
# Seule n=2 (Brown-York) reproduit 8 c_W = ell^2/kappa^2.
n = sp.symbols('n', positive=True)
TT_n = n**2 * psi2
sol_n = sp.solve(sp.Eq(TT_n, ell**2/kappa**2), n)
sol_n_pos = [s for s in sol_n if s.is_positive]
must(len(sol_n_pos) == 1 and sol_n_pos[0] == 2,
     "T = n δW/δg : SEUL n=2 (Brown-York) reproduit éq.90 => gamma=n^2=4 SENSIBLE")
# contrôle négatif : n=1 (sans le 2) casse l'éq. 90
must(sp.simplify(TT_n.subs(n, 1) - ell**2/kappa**2) != 0,
     "n=1 (T=δW/δg, sans le 2) => <TT>=2c_W != ell^2/kappa^2  (CASSE éq.90)")
must(sp.simplify(TT_n.subs(n, 1) - sp.Rational(1,4)*ell**2/kappa**2) == 0,
     "n=1 reproduit la lecture NU 2c_W = (1/4) ell^2/kappa^2  (= gamma=1)")

# -----------------------------------------------------------------------------
section("BILAN")
# -----------------------------------------------------------------------------
print(f"""
  +---------------------------------------------------------------------+
  |  SÉPARATION beta/gamma (sonde 1 + sonde 2, scellée) :               |
  |    beta = M_Pl^2/4   FORCÉ par le spectre (aveugle à gamma)         |
  |    gamma  = map opérateur, N_action = gamma/4                       |
  |                                                                     |
  |  MAP CANONIQUE (de Haro éq.63 x2, FORCÉE) :                         |
  |    <TT>_canon = 4 * psi2  =>  gamma_canon = 4                       |
  |    => N_action = 1 ; C_T^prog = C_T^dH = ell^2/kappa^2 (MÊME objet) |
  |                                                                     |
  |  LECTURE NU (programme, O=T/2, POSÉE) :                             |
  |    gamma = 1  =>  N_action = 1/4 ; C_T^prog = (1/4) C_T^dH          |
  |                                                                     |
  |  VERDICT : gamma=1 n'est PAS forcé = CONVENTION (normalisation      |
  |  d'opérateur nu). Canonique forcé = gamma=4. N_action=1/4 = étiquette|
  |  de convention, à libeller comme telle (§AF branche 2).            |
  |                                                                     |
  |  Firewall : gamma=4 = UNIQUE valeur reproduisant éq.90 (SENSIBLE).  |
  +---------------------------------------------------------------------+

  §6.4 : « gamma=4 (canonique) / gamma=1 (convention nue) » (algèbre)
  != « D1 fermé / N fixé / CCC démontrée ». PAS de NO-GO ; aucune
  contradiction. {{A4 ; A2★ ; N}} INCHANGÉ ; D1 non clos ; N non fixé ;
  CCC non démontrée.
""")
print(f"TOUS LES ASSERT PASSENT — {OK} assertions. gamma_canon=4 FORCÉ ; gamma=1 CONVENTIONNEL. EXIT 0.")
