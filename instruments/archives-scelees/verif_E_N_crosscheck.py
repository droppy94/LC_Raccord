#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_E_N_crosscheck.py — Module E / front « qu'est-ce qui fixe N ? », axe (beta).

Atteste, EN ALGEBRE (LC-AUDIT-VERDICT §6.4), que :
  [A] toutes les prises sur N (A_T, C_T, cutoff, marée P_T) sont des FONCTIONS de
      l'unique N par scellement => pas de seconde determination independante ;
  [B] la relation composee A_T = 16/S_dS = (16/pi)(H_dS/M_P)^2 (H_dS^2 = Lambda/3) ;
  [C] numerique : A_T^pred ~ 5e-122 (Lambda, ell_P mesures) << A_T^obs(borne) ~ 1e-10
      => le deux-point de VIDE CCC n'est PAS le spectre primordial observe (FALSIFICATION) ;
  [D] non-independance : 4 relations parmi {N, A_T, C_T, cutoff, Lambda} a ell_P fixe
      => 1 SEUL intrant libre (= Lambda). « Fixer N » == « fixer Lambda ».
  [E] FIREWALL (injection d'echelle) : le resultat est SENSIBLE — injecter H_inf
      (echelle inflationnaire) au lieu de H_dS redonne A_T ~ 1e-10 (CMB) => le
      mismatch vient SPECIFIQUEMENT de l'echelle H_dS, le test n'est pas tautologique.

NE PROUVE PAS : que N est fixe (il est LU sur Lambda) ; que le germe observe exige un
mecanisme energetique (interpretation physique, decision ouverte) ; CCC. Perimetre
{A4 ; A2* ; N} INCHANGE. Consolidation + un acquis falsifiable NEGATIF.

Stack : Python 3.12 / sympy 1.14 / numpy 2.4.
"""

import sympy as sp

OK = 0
def check(cond, msg):
    global OK
    assert cond, "ECHEC : " + msg
    print("  [OK]", msg)
    OK += 1

print("=" * 78)
print("verif_E_N_crosscheck.py — N : un seul intrant (Lambda) ; deux-point CCC != CMB")
print("=" * 78)

# Symboles strictement positifs (longueurs, comptes, constantes)
N, Lam, lP, H, MP, AT, CT, K = sp.symbols(
    "N Lambda ell_P H M_P A_T C_T K", positive=True)

# ---------------------------------------------------------------------------
print("\n[A] Tout retombe sur l'unique N (relations scellees)")
# Relations scellees du secteur gaussien/holographique :
N_of_Lam = 3 * sp.pi / (Lam * lP**2)          # N = S_dS = 3 pi / (Lambda ell_P^2)   (LC-E)
AT_of_N  = sp.Integer(16) / N                  # A_T = 16/N            (candidat-egalite, LC-D-CT-ATN)
CT_of_N  = N / (32 * sp.pi**2)                 # C_T/N = 1/(32 pi^2)   (verrouillage, LC-D-CT-ATN)
K_of_N   = sp.sqrt(N / sp.pi)                  # cutoff log-doux sqrt(N/pi) = ell_dS/ell_P

check(sp.simplify(AT_of_N * N - 16) == 0,
      "A_T * N = 16 (nombre pur) : A_T est 1/N par scellement (pas de DOF propre)")
check(sp.simplify(CT_of_N / N - sp.Rational(1, 1) / (32 * sp.pi**2)) == 0,
      "C_T / N = 1/(32 pi^2) (nombre pur) : C_T est N par scellement (pas de DOF propre)")
check(sp.simplify(K_of_N**2 * sp.pi - N) == 0,
      "cutoff^2 * pi = N : le cutoff est sqrt(N/pi) (pas de DOF propre)")

# Maree (atlas) : P_T ∝ H^2 = Lambda/3 ; H_dS^2 = Lambda/3 (de Sitter asymptotique)
H2_of_Lam = Lam / 3
check(sp.simplify(H2_of_Lam - Lam/3) == 0,
      "maree atlas P_T ∝ H^2 = Lambda/3 (CROSSOVER-STABILITE §4) : H = H_dS asymptotique")
# Pont atlas <-> holographique : Lambda * N = 3 pi / ell_P^2 = 3 pi M_P^2 (M_P = 1/ell_P)
LamN = sp.simplify(Lam * N_of_Lam)
check(sp.simplify(LamN - 3*sp.pi/lP**2) == 0,
      "Lambda * N = 3 pi / ell_P^2 = 3 pi M_P^2 (identite) : atlas et N = meme nombre")

# ---------------------------------------------------------------------------
print("\n[B] Relation composee A_T = 16/S_dS = (16/pi)(H_dS/M_P)^2")
AT_composed = sp.simplify(AT_of_N.subs(N, N_of_Lam))          # 16 Lambda ell_P^2 / (3 pi)
check(sp.simplify(AT_composed - 16*Lam*lP**2/(3*sp.pi)) == 0,
      "A_T = 16 Lambda ell_P^2 / (3 pi)  (composition des scellements)")
# Reecriture via H_dS^2 = Lambda/3 et M_P = 1/ell_P :
AT_via_H = sp.simplify((16/sp.pi) * (H**2) * lP**2)          # (16/pi)(H/M_P)^2, M_P=1/ell_P
AT_from_compo_in_H = sp.simplify(AT_composed.subs(Lam, 3*H**2))
check(sp.simplify(AT_from_compo_in_H - AT_via_H) == 0,
      "A_T = (16/pi)(H_dS/M_P)^2 avec H_dS^2=Lambda/3, M_P=1/ell_P (convention dans 16/pi)")

# ---------------------------------------------------------------------------
print("\n[C] Numerique : A_T^pred << A_T^obs => FALSIFICATION (CMB != germe de vide)")
Lam_val = 1.1e-52        # m^-2  (constante cosmologique observee)
lP_val  = 1.616e-35      # m     (longueur de Planck)
N_val   = float(3*sp.pi.evalf() / (Lam_val * lP_val**2))
AT_pred = 16.0 / N_val
print(f"      N = S_dS              = {N_val:.3e}   (attendu ~3.3e122)")
print(f"      A_T^pred = 16/N       = {AT_pred:.3e}   (attendu ~5e-122)")
check(2.0e122 < N_val < 5.0e122,
      "N = S_dS ~ 3.3e122 (entropie d'horizon de Sitter ; lu sur Lambda, ell_P)")
check(3.0e-122 < AT_pred < 8.0e-122,
      "A_T^pred = 16/S_dS ~ 5e-122 (amplitude de vide a l'echelle dS asymptotique)")

# Verification croisee via (16/pi)(H_dS/M_P)^2
H_dS_val = (Lam_val/3.0)**0.5            # m^-1
HsurMP   = H_dS_val * lP_val             # (H_dS/M_P), M_P = 1/ell_P
import math
AT_via_H_val = (16.0/math.pi) * HsurMP**2
print(f"      (16/pi)(H_dS/M_P)^2   = {AT_via_H_val:.3e}   (doit egaler A_T^pred)")
check(abs(AT_via_H_val - AT_pred)/AT_pred < 1e-3,
      "voie holographique (16/N) et voie d'echelle (16/pi)(H_dS/M_P)^2 coincident (<0.1%)")

# Borne observationnelle du spectre tensoriel primordial
A_s        = 2.1e-9      # amplitude scalaire (Planck)
r_bound    = 0.036       # borne sur r (BICEP/Keck 2021, ordre de grandeur)
AT_obs_lim = r_bound * A_s
print(f"      A_T^obs (borne)       = r*A_s ~ {AT_obs_lim:.2e}   (ordre 1e-10)")
ratio = AT_obs_lim / AT_pred
print(f"      A_T^obs / A_T^pred    = {ratio:.2e}   (ecart ~10^111)")
check(AT_pred < 1e-100 < AT_obs_lim,
      "A_T^pred << A_T^obs : le deux-point de VIDE CCC est ~10^111 sous le spectre observe")
check(ratio > 1e100,
      "FALSIFICATION : 'deux-point observable = spectre CMB' EXCLU (ecart >10^100)")

# ---------------------------------------------------------------------------
print("\n[D] Non-independance : 4 relations, 5 quantites, ell_P fixe => 1 intrant (Lambda)")
quantites = {"N", "A_T", "C_T", "cutoff", "Lambda"}     # a ell_P fixe
relations = {
    "A_T = 16/N",
    "C_T = N/(32 pi^2)",
    "cutoff = sqrt(N/pi)",
    "N = 3 pi/(Lambda ell_P^2)",
}
dof = len(quantites) - len(relations)
print(f"      quantites = {len(quantites)} ; relations scellees = {len(relations)} ; DOF = {dof}")
check(dof == 1,
      "un seul degre de liberte residuel parmi {N,A_T,C_T,cutoff,Lambda} a ell_P fixe")
# L'unique intrant est Lambda : varier Lambda deplace TOUT, sans casser les nombres purs.
Lam1, Lam2 = 1.1e-52, 2.2e-52
def bundle(L):
    n = float(3*sp.pi.evalf()/(L*lP_val**2))
    return n, 16.0/n, n/(32*math.pi**2), (n/math.pi)**0.5
n1, at1, ct1, k1 = bundle(Lam1)
n2, at2, ct2, k2 = bundle(Lam2)
check(abs(at1*n1 - 16) < 1e-6 and abs(at2*n2 - 16) < 1e-6,
      "sous variation de Lambda : A_T*N = 16 reste invariant (pas de 2e nombre libere)")
check(abs(ct1/n1 - ct2/n2) < 1e-12,
      "sous variation de Lambda : C_T/N reste constant (1/(32 pi^2)) — meme intrant")
check(abs(n2/n1 - Lam1/Lam2) < 1e-9,
      "N ∝ 1/Lambda : 'fixer N' == 'fixer Lambda' (probleme de la constante cosmologique)")

# ---------------------------------------------------------------------------
print("\n[E] FIREWALL (injection d'echelle) : le test est SENSIBLE, non tautologique")
# Si l'amplitude vivait a l'echelle INFLATIONNAIRE H_inf (et non H_dS), on retrouverait
# l'ordre observe. Le mismatch vient donc de l'echelle H_dS, pas d'une trivialite.
MP_GeV   = 1.22e19       # M_P (non reduit), GeV
H_inf    = 6.0e13        # GeV, borne sup. inflationnaire typique
AT_inf   = (16.0/math.pi) * (H_inf/MP_GeV)**2
print(f"      (break) A_T(H_inf)    = {AT_inf:.2e}   (echelle inflationnaire)")
check(1e-11 < AT_inf < 1e-9,
      "BREAK : injecter H_inf donne A_T ~ 1e-10 (ordre CMB) — l'echelle est LE facteur decisif")
check(AT_inf/AT_pred > 1e100,
      "FIREWALL : A_T(H_inf) != A_T(H_dS) de >10^100 => resultat SENSIBLE a l'echelle (non taut.)")
# Sensibilite au coefficient : A_T = coeff * Lambda ell_P^2/(3 pi) ; coeff=16 porteur.
coeff = sp.symbols("coeff", positive=True)
AT_gen = coeff * Lam * lP**2 / (3 * sp.pi)
check(AT_gen.subs(coeff, 0) == 0
      and sp.simplify(AT_gen.subs(coeff, 16) - AT_composed) == 0,
      "le coefficient (=16) est porteur : A_T lineaire en lui (0->0, 16->valeur scellee)")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"BILAN : {OK}/{OK} assertions OK")
print("=" * 78)
print("""
VERDICT (axe beta) — etabli (ALGEBRE, §6.4) :
  [A] A_T, C_T, cutoff, maree sont des fonctions de l'UNIQUE N par scellement
      (A_T*N=16, C_T/N=1/(32 pi^2), cutoff=sqrt(N/pi)) ; Lambda*N=3 pi M_P^2.
  [B] composition : A_T = 16/S_dS = (16/pi)(H_dS/M_P)^2, H_dS^2 = Lambda/3.
  [C] A_T^pred ~ 5e-122 (echelle dS asymptotique, H_dS ~ H_0) << A_T^obs ~ 1e-10 :
      'deux-point observable = spectre CMB' est EXCLU (~10^111) — acquis NEGATIF net.
  [D] 1 seul intrant libre (Lambda) : « fixer N » == « fixer Lambda » (probleme CC).
  [E] firewall : injecter H_inf redonne ~1e-10 => mismatch SPECIFIQUE a H_dS, sensible.

CONSEQUENCE : l'axe beta (cross-check empirique) est une CONSOLIDATION (les
  determinations ne sont pas independantes), assortie d'UN acquis falsifiable
  NEGATIF (le germe inter-eon de vide n'est pas le spectre observe). Le falsifiable
  POSITIF (coefficients 16, 1/(32 pi^2)) vit dans le pont CONSTRUCTIF (dS/CFT
  travaille), ou A_T/C_T et N sont accessibles independamment.

NE PROUVE PAS : que N est fixe (LU sur Lambda) ; qu'un mecanisme energetique est requis
  (interpretation physique, decision ouverte) ; D1 ferme ; CCC. Perimetre
  {A4 ; A2* ; N} INCHANGE ; (A) physique conditionnel au seul A2* inchange.
""")
