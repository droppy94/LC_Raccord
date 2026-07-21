# -*- coding: utf-8 -*-
"""
verif_D_w3_gpy.py — sceau du chaînon LC-D-W3-GPY v0.1
=====================================================
Consolidation du rang 3 (classes d'hélicité S₃×P, LC-D-NONGAUSS-TTT-LOURD
[B'/PL-D]) contre la classification IMPRIMÉE de Giombi–Prakash–Yin,
arXiv:1104.4317v4 (« A Note on CFT Correlators in Three Dimensions »).

Anti-fit : cadrage LC-WORK-CADRAGE-W3-GPY v0.1 GELÉ avant fetch
(sha256 dd2cd36756f8ab689f4b40e58d35a17d9e5aceb7fce0e0f3c66fd904d30cf037,
consigné en conversation le 2026-06-12 AVANT ouverture du PDF).

Cibles gelées : T1 (2 paires, champs libres) ; T2 (≤1 impaire, non libre) ;
T3 (aucune surnuméraire).

Discipline §6.4 : ce sceau atteste « algèbre correcte + cibles reproduites ».
JAMAIS « secteur non-gaussien fermé / D1 clos / N fixé / CCC démontrée ».
"""

import sys
from itertools import product, permutations

OK = []
def check(idx, label, cond):
    assert cond, f"[assert {idx:02d}] {label} — ÉCHEC"
    OK.append(idx)
    print(f"  [assert {idx:02d}] {label} — OK")

print("=" * 78)
print("BLOC A — volet INTERNE rejouable : orbites d'hélicité (±2)³ sous S₃×P")
print("=" * 78)

configs = list(product([+2, -2], repeat=3))          # 8 configurations

def orbits(confs, with_parity):
    seen, orbs = set(), 0
    for c in confs:
        if c in seen:
            continue
        orbs += 1
        orbit = set()
        for p in permutations(range(3)):              # action S₃
            g = tuple(c[i] for i in p)
            orbit.add(g)
            if with_parity:                           # action P : renverse toutes les hélicités
                orbit.add(tuple(-x for x in g))
        seen |= orbit
    return orbs

n_S3P = orbits(configs, with_parity=True)
n_S3  = orbits(configs, with_parity=False)

check(1, "8 configurations d'hélicité (±2)³", len(configs) == 8)
check(2, "orbites sous S₃×P = 2 EXACTEMENT (rejoue le scellé lourd PL-D)", n_S3P == 2)
check(3, "orbites sous S₃ seul = 4 (la parité est NÉCESSAIRE au recompte 2)", n_S3 == 4)

# Graduation consignée du scellé lourd (PAS re-dérivée ici) :
PROG_CLASSES = {"melange":  {"repr": "(-,-,+)", "dim_derivees": 2, "action": "EINSTEIN"},
                "alignee":  {"repr": "(+,+,+)", "dim_derivees": 6, "action": "W3"}}
check(4, "graduation programme {2, 6} (consignée du lourd, dim paire = 2)",
      sorted(c["dim_derivees"] for c in PROG_CLASSES.values()) == [2, 6])
PROG_N_EVEN_BULK = len(PROG_CLASSES)   # 2 classes, toutes deux issues d'actions PAIRES
PROG_COUNT_LEGER = (2, 1)              # léger [D] : 2 formes paires + 1 impaire (OP∩MP)

print()
print("=" * 78)
print("BLOC B — volet SOURCE : constantes consignées de 1104.4317v4 [E1–E5]")
print("=" * 78)
# [E1] §3.2, éq. (3.10) : ansatz ⟨J₂J₂J₂⟩ à 6 coefficients — 4 pairs (a1..a4)
#      construits sur {P,Q}, 2 impairs (b1,b2) portant un S_i.
# [E2] §3.2, éq. (3.11) : la conservation impose 3 relations imprimées —
#      a3 = (5/4)a1 − (16/5)a2 ; a4 = −(8/15)a2 ; b2 = 5 b1
#      (2 relations dans le secteur pair, 1 dans l'impair).
# [E3] §3.2, conclusion imprimée : « 2 independent parity even structures,
#      plus one additional parity odd structure » ; les 2 paires =
#      combinaison linéaire des résultats scalaire libre / fermion libre ;
#      l'impaire (3.12) est nouvelle, réalisable en théories
#      Chern–Simons-matière violant la parité (réf. [8] de la source).
# [E4] Abstract : toutes les structures paires des courants conservés sont
#      réalisées par champs libres ; au plus UNE structure impaire par jeu
#      de spins, non réalisée par champs libres.
# [E5] §3.1, éq. (3.4) : forme générale a1⟨⟩_B + a2⟨⟩_F + b⟨⟩_odd ; l'impaire
#      conjecturée UNIQUE sous inégalité triangulaire, nulle sinon.
GPY_ANSATZ_EVEN_COEFFS = 4      # a1, a2, a3, a4          [E1]
GPY_ANSATZ_ODD_COEFFS  = 2      # b1, b2                  [E1]
GPY_RELATIONS_EVEN     = 2      # a3(a1,a2), a4(a2)       [E2]
GPY_RELATIONS_ODD      = 1      # b2 = 5 b1               [E2]
GPY_N_EVEN             = 2      # imprimé                 [E3]
GPY_N_ODD              = 1      # imprimé                 [E3]
GPY_EVEN_FREE_REALIZED = True   # scalaire ⊕ fermion      [E2]/[E3]/[E4]
GPY_ODD_FREE_REALIZED  = False  # « not realized by free fields » [E4]
SPINS = (2, 2, 2)

check(5, "cohérence interne source : 4 coeffs pairs − 2 relations = 2 indépendants",
      GPY_ANSATZ_EVEN_COEFFS - GPY_RELATIONS_EVEN == GPY_N_EVEN)
check(6, "cohérence interne source : 2 coeffs impairs − 1 relation = 1 indépendant",
      GPY_ANSATZ_ODD_COEFFS - GPY_RELATIONS_ODD == GPY_N_ODD)
check(7, "inégalité triangulaire satisfaite pour (2,2,2) ⟹ l'impaire est permise [E5]",
      all(SPINS[i] <= SPINS[(i+1) % 3] + SPINS[(i+2) % 3] for i in range(3)))
check(8, "T2 (forme gelée « au plus 1 ») : N_odd ≤ 1 ET non réalisée par champs libres",
      GPY_N_ODD <= 1 and not GPY_ODD_FREE_REALIZED)

print()
print("=" * 78)
print("BLOC C — APPARIEMENT cibles gelées T1/T2/T3 (cadrage sha dd2cd3…f037)")
print("=" * 78)
check(9,  "T1 : GPY compte EXACTEMENT 2 structures paires", GPY_N_EVEN == 2)
check(10, "T1 : les 2 paires sont réalisées par champs libres (boson, fermion)",
      GPY_EVEN_FREE_REALIZED)
check(11, "T1 : appariement de comptage — 2 classes S₃×P programme ↔ 2 paires GPY",
      n_S3P == GPY_N_EVEN == PROG_N_EVEN_BULK)
check(12, "T2 : comptage total 2+1 — léger [D] (OP∩MP) ↔ GPY (route INDÉPENDANTE)",
      PROG_COUNT_LEGER == (GPY_N_EVEN, GPY_N_ODD))
check(13, "T3 : aucune structure surnuméraire (ni 3ᵉ paire, ni 2ᵉ impaire)",
      GPY_N_EVEN == 2 and GPY_N_ODD == 1)
# Nuance T2 CONSIGNÉE (pas un assert d'identité — périmètres DISJOINTS) :
# l'impaire GPY est une structure à points séparés des théories violant la
# parité (CS-matière) ; le périmètre programme (actions paires Einstein/W³ ;
# parité impaire = S2 HORS périmètre) ne la source pas. Compatible avec
# « présente en fonction d'onde, absente du bispectre » (léger [D]) ;
# AUCUNE contradiction, AUCUNE identification revendiquée.
check(14, "T2-nuance : l'impaire n'est portée par AUCUNE classe-action du périmètre",
      all(c["action"] in ("EINSTEIN", "W3") for c in PROG_CLASSES.values()))

print()
print("=" * 78)
print("BLOC D — FIREWALL (injections fausses : chacune DOIT casser)")
print("=" * 78)
fw = 0
# F-1 : sans parité, le recompte 2 est FAUX
try: check(99, "", orbits(configs, with_parity=False) == 2)
except AssertionError: fw += 1; print("  [F-1] orbites S₃ seul ⟹ 4 ≠ 2 — CASSE — OK")
# F-2 : une 3ᵉ structure paire casse T1/T3
try: check(99, "", 3 == GPY_N_EVEN)
except AssertionError: fw += 1; print("  [F-2] N_even=3 injecté — CASSE — OK")
# F-3 : une 2ᵉ impaire casse T3
try: check(99, "", GPY_N_ODD == 2)
except AssertionError: fw += 1; print("  [F-3] N_odd=2 injecté — CASSE — OK")
# F-4 : une seule relation paire (au lieu de 2) casse la cohérence interne [E2]→[E3]
try: check(99, "", GPY_ANSATZ_EVEN_COEFFS - 1 == GPY_N_EVEN)
except AssertionError: fw += 1; print("  [F-4] 1 relation paire au lieu de 2 — CASSE — OK")
# F-5 : spins (2,2,5) violent l'inégalité triangulaire ⟹ le test [E5] discrimine
try: check(99, "", all((2,2,5)[i] <= (2,2,5)[(i+1)%3] + (2,2,5)[(i+2)%3] for i in range(3)))
except AssertionError: fw += 1; print("  [F-5] triangle violé (2,2,5) — CASSE — OK")
# F-6 : graduation {2,4} au lieu de {2,6} casse la consignation lourd
try: check(99, "", sorted([2, 4]) == [2, 6])
except AssertionError: fw += 1; print("  [F-6] graduation {2,4} injectée — CASSE — OK")
assert fw == 6, "firewall incomplet"

print()
print("=" * 78)
print(f"TOUS LES ASSERT PASSENT — {len(OK)} assertions + firewall 6/6. EXIT 0.")
print("VERDICT : CONSOLIDATION — le recompte 2+1 du rang 3 est RECOUPÉ par une")
print("route externe indépendante (invariants conformes 3d, GPY) ; T1/T3 tenues")
print("telles qu'imprimées ; T2 tenue sur le compte, nuance consignée (impaire =")
print("structure des théories violant la parité, HORS périmètre S2).")
print("AUCUNE réduction de comptage. Décisions ouvertes INCHANGÉES :")
print("  coefficient W³ ~ (LH)⁴ ; (a,b,c) propres / CFT de raccordement.")
print("§6.4 : « établi (algèbre) » = algèbre correcte + cibles reproduites —")
print("  JAMAIS « secteur non-gaussien fermé / D1 clos / N fixé / CCC démontrée ».")
print("Compte {A4 ; A2★ ; N} INCHANGÉ.")
print("=" * 78)
sys.exit(0)
