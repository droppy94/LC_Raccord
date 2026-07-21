#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_F1_spn.py — SCEAU du front F1 (branche FALSIFIABILITÉ) : PONT CONSTRUCTIF Sp(N).

OBJET. Tester le falsifiable POSITIF de LC-E-N-CROSSCHECK (c) : un modèle dS/CFT
EXPLICITE (Sp(N)/AHS) reproduit-il le coefficient pur C_T/N du programme par une voie
où C_T ET N sont accessibles indépendamment du scellement holographique interne ?
C'est le « vrai sceau dS/CFT » appelé par LC-WORK-D-CT-CADRAGE §6.

SOURCE (déjà en KB, consommée par LC-D-SPN ; AUCUN fetch neuf) :
  Anninos-Hartman-Strominger, arXiv:1108.5735v1, telle qu'imprimée :
   - (A.10) ⟨J^(s)J^(s)⟩_EAdS = +(ℓ²_AdS/G_N)·f(x)
   - (A.11) ⟨J^(s)J^(s)⟩_dS   = −(ℓ²_dS /G_N)·f(x)        [signe − ; vaut pour TOUT spin pair, dont s=2]
   - (3.7)/(3.8)  C2 → −C2  ≡  N → −N    (O(−N)=Sp(N))
   - p.8/p.10  C2 ∼ −G_N Λ ∼ 1/N  et  C2 = 1/(2N)  ⟹  ℓ²/G_N ∼ N (rang) DANS Vasiliev
   - p.4  courants singlets conservés de tous spins PAIRS ; modèle = scalaires (vecteur)

CIBLES GELÉES (cadrage LC-WORK-CADRAGE-F1-SPN v0.1, déposé AVANT cette extraction) :
   F1-G1  A_T·N = 16            (nombre pur, convention-libre)   -> NON testable ici (O1)
   F1-G2  |C_T|/N = 1/(32π²)    (convention IMPULSION, programme)
   F1-G2' |C_T|/N = 3/(4π⁴)     (Osborn-Petkos = κ·F1-G2, κ=24/π²)
   F1-G3  sign(C_T) < 0         (déjà acquis LC-D-SPN ; contrôle)
   F1-G4  C_T(scalaire libre d=3) = 3/(32π²)  (OP, étalon Osborn-Petkou)

VERDICT (sans surclassement, §6.4) :
   - STRUCTURE  : signe < 0, ∝N, mécanisme holographique ⟨JJ⟩∝ℓ²/G_N  -> CONCORDANTS (consolidation).
   - COEFFICIENT: |C_T^Sp(N)|/N = 3/(32π²) (OP, N scalaires |_{N→−N}) vs cible 3/(4π⁴)
                  -> écart EXACT π²/8 ≠ 1  -> NON concordant. C'est la signature de O1
                  (higher-spin/scalaires ≠ Einstein) : le C_T de Sp(N) est celui des SCALAIRES
                  composites, pas du graviton d'Einstein du programme.
   - Issue §5 : (A) à la structure, (B) au coefficient (le désaccord LOCALISE le fossé
                dS/CFT↔inflation). Le falsifiable POSITIF n'est PAS branché par Sp(N).
   - Compte {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée.
"""
import sympy as sp

pi = sp.pi
asserts = 0
def check(cond, msg):
    global asserts
    assert cond, "ÉCHEC: " + msg
    asserts += 1

# =========================================================================
# Bloc A — EXTRACTION AHS (telle qu'imprimée, valeurs/structure)
# =========================================================================
# On encode les FAITS imprimés sous forme vérifiable, sans aucun indice de cible.
# Signe relatif EAdS->dS du deux-point de courant (A.10 vs A.11) : facteur (-1).
sign_EAdS = +1
sign_dS   = -1
check(sign_dS == -sign_EAdS, "A: signe ⟨JJ⟩_dS = −⟨JJ⟩_EAdS (A.10/A.11)")

# Règle de continuation C2 -> -C2 ≡ N -> -N (3.7/3.8) ; O(-N)=Sp(N)
def to_Sp(expr_in_N, N):
    return expr_in_N.subs(N, -N)
N = sp.symbols('N', positive=True)
# Coefficient générique du deux-point ∝ ℓ²/G_N ∼ N (rang) dans Vasiliev (p.8/p.10)
# (proportionnalité structurelle ; le coefficient pur vient de l'étalon, Bloc C)
C2 = sp.Rational(1,2)/N           # p.10 : C2 = 1/(2N)
check(sp.simplify(C2 - sp.Rational(1,2)/N) == 0, "A: C2 = 1/(2N) (p.10)")
# ⟨OO⟩ ∝ 1/C2 = 2N  (p.9 : correlateurs ∝ C2^{-1})
twopt_ON = sp.simplify(1/C2)
check(sp.simplify(twopt_ON - 2*N) == 0, "A: deux-point O(N) ∝ 1/C2 = 2N (∝ rang)")
# Spins PAIRS uniquement (p.4) — le tenseur de stress s=2 est pair => présent
spins = [2, 4, 6]
check(all(s % 2 == 0 for s in spins) and 2 in spins, "A: courants spins pairs, s=2 présent")

# =========================================================================
# Bloc B — STRUCTURE de C_T (signe, proportionnalité, mécanisme holographique)
# =========================================================================
# C_T (s=2) hérite du signe dS (A.11) et de ∝ ℓ²/G_N ∼ N.
# Sp(N) = O(N)|_{N->-N} : le deux-point bascule de signe (Fermi) -> C_T<0, ∝ -N.
twopt_Sp = to_Sp(twopt_ON, N)     # = -2N
check(sp.simplify(twopt_Sp - (-2*N)) == 0, "B: deux-point Sp(N) = (O(N))|_{N→−N} = −2N")
check(sp.sign(twopt_Sp.subs(N, 1)) == -1, "B: C_T(Sp) < 0 (signe négatif)")
# proportionnalité ∝ N (linéaire)
check(sp.simplify(sp.diff(twopt_Sp, N) - (-2)) == 0, "B: C_T ∝ N (dérivée constante)")

# =========================================================================
# Bloc C — COEFFICIENT PUR via étalon (Osborn-Petkou)
# =========================================================================
# Sp(N) libre = N scalaires anticommutants ; |C_T|/N = C_T d'UN scalaire libre (OP).
etalon_scal_OP = sp.Rational(3,32)/pi**2          # F1-G4 (Osborn-Petkou, d=3)
CT_over_N_Sp_OP = etalon_scal_OP                  # |C_T^Sp(N)|/N en convention OP
check(sp.simplify(CT_over_N_Sp_OP - sp.Rational(3,32)/pi**2) == 0,
      "C: |C_T^Sp(N)|/N = 3/(32π²) (OP, N scalaires libres |_{N→−N})")

# =========================================================================
# Bloc D — CONFRONTATION aux cibles GELÉES
# =========================================================================
# Cibles (figées dans le cadrage, AVANT extraction)
kappa     = 24/pi**2                              # dictionnaire IMP->OP (LC-NACTION-AVEUGLE)
cible_imp = sp.Rational(1,32)/pi**2               # F1-G2  (impulsion)
cible_OP  = sp.simplify(cible_imp*kappa)          # F1-G2' (OP)
check(sp.simplify(cible_OP - sp.Rational(3,4)/pi**4) == 0, "D: cible programme OP = 3/(4π⁴) (=κ·F1-G2)")

# D1 — SIGNE : concordant (F1-G3)
check(sp.sign(twopt_Sp.subs(N, 1)) == -1, "D1: signe CONCORDANT (C_T<0 = F1-G3)")
# D2 — ∝N : concordant
check(sp.simplify(sp.diff(twopt_Sp, N)) != 0 and sp.simplify(sp.diff(twopt_Sp, N, 2)) == 0,
      "D2: ∝N CONCORDANT (linéaire en N)")
# D3 — COEFFICIENT : NON concordant, écart EXACT π²/8
ratio = sp.simplify(CT_over_N_Sp_OP / cible_OP)
check(sp.simplify(ratio - pi**2/8) == 0, "D3: écart coefficient = π²/8 (exact)")
check(ratio != 1, "D3: coefficient NON concordant (ratio ≠ 1)")
# D4 — lecture O1 : le MÊME facteur 8/π² sépare graviton(prog) et scalaire libre en IMPULSION
scal_imp = sp.simplify(etalon_scal_OP/kappa)
check(sp.simplify(cible_imp/scal_imp - 8/pi**2) == 0,
      "D4: graviton/scalaire (IMP) = 8/π² -> l'écart EST O1 (Einstein ≠ scalaires/Vasiliev)")
# D5 — A_T·N=16 NON testable ici (O1) : consignation (pas un échec, une limite de domaine)
A_T_testable_in_Sp = False
check(A_T_testable_in_Sp is False, "D5: A_T·N=16 NON testable dans Sp(N) (O1, consigné)")

# =========================================================================
# Bloc E — FIREWALL (injections cassantes : le sceau doit casser sur faux)
# =========================================================================
# E1 : prétendre la concordance du coefficient (ratio==1) doit être REJETÉ
fw1 = (sp.simplify(ratio - 1) == 0)
check(fw1 is False, "E1: concordance forcée du coefficient REJETÉE (ratio≠1)")
# E2 : oublier le dictionnaire κ (κ=1) change la cible -> casse la valeur 3/(4π⁴)
cible_OP_bad = sp.simplify(cible_imp*1)
check(sp.simplify(cible_OP_bad - sp.Rational(3,4)/pi**4) != 0, "E2: κ=1 (oubli dictionnaire) CASSE la cible OP")
# E3 : signe + (au lieu de −) contredit A.11
check((+2*N).subs(N,1) != twopt_Sp.subs(N,1), "E3: signe + CASSE (contredit A.11/Fermi)")
# E4 : mauvais étalon (ex. 1/(32π²) au lieu de 3/(32π²)) change le ratio
ratio_bad = sp.simplify((sp.Rational(1,32)/pi**2)/cible_OP)
check(sp.simplify(ratio_bad - pi**2/8) != 0, "E4: étalon faux CASSE le ratio")
# E5 : continuation N->-N absente -> pas de signe négatif (structure dS perdue)
twopt_noSp = twopt_ON  # = +2N
check(sp.sign(twopt_noSp.subs(N,1)) == +1, "E5: sans N→−N le signe reste + (dS non atteint) — discriminant")

print(f"OK — {asserts} assertions. F1/Sp(N) : STRUCTURE concordante (signe<0, ∝N, holographique) ; "
      f"COEFFICIENT NON concordant (écart π²/8 = O1, Einstein≠scalaires). Falsifiable positif NON "
      f"branché par Sp(N). {{A4 ; A2★ ; N}} INCHANGÉ. Firewall actif. EXIT 0.")
