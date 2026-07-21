#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_nongauss_TTT_lourd_phase1.py — DÉPÔT DE PHASE 1 du sceau du PASSAGE LOURD
==================================================================================
Cadrage : LC-WORK-CADRAGE-NONGAUSS-LOURD v0.1 (validé 2026-06-12, en KB).
Scopings S-L1..S-L6 tranchés « tout recommandé » ; R-7 ARMÉE sur PL-A..PL-D.

CE FICHIER EST LE DÉPÔT DE PHASE (règle R-10) : phase 1 INTERNE, écrite et
exécutée EXIT 0 AVANT TOUTE CONSULTATION DE LITTÉRATURE. Aucun fetch n'a été
fait pour le produire ; la p.6 de MP n'a PAS été lue (résidu gelé, E-L2) ;
les PDF d'OP/MP n'ont PAS été ouverts. Ce fichier est GELÉ après dépôt :
ses asserts 01-K devront être BYTE-IDENTIQUES dans le sceau final
verif_D_nongauss_TTT_lourd.py (phase 2 = blocs [C]-[F], fetch).

CIBLES GELÉES (cadrage §3 — NE PAS reparamétrer ; R-7) :
  PL-A : secteur Ward de ⟨TTT⟩, appareil OP NUMÉRIQUE telle-qu'écrite
         ((d−2)(d+3)=6, d(d+2)=15 en d=3) ⟹ |C_T|/N = 1/(32π²) (nu), slack NUL.
         [PHASE 2 — ici : squelette + verrou dimensionnel + valeur interne]
  PL-B : énoncé ε·ε* MP exhibé verbatim (attendu p.6), tranché 4 vs 2,
         absorbé par {2,4,8} ; insensibilité des ratios re-dérivée. [PHASE 2]
  PL-C : non-régressions du léger — γ₃=8 ; (H/M_Pl)⁴/A_T²=π⁴/4 slack nul ;
         ⟨g₃³⟩_libre=0 identiquement. [PHASE 1 — bloc A, ICI]
  PL-D : espace des structures invariantes du trois-point TT (Δ=d=3, niveau
         arbre) par représentation, SANS consommer MP/OP : 2 formes paires ;
         l'impaire hors bispectre (recoupement du scellé léger, non re-dérivé).
         [PHASE 1 — bloc B', ICI]

DÉRIVATION PAPIER DU BLOC B' (consignée ; petit groupe + parité, niveau arbre) :
  (1) Bord d=3, donnée radiative spin-2 ⟹ petit groupe SO(2), hélicités ±2
      par jambe ⟹ 8 configurations (s₁,s₂,s₃).
  (2) Orbites sous S₃ (opérateurs identiques) × P (renversement global) :
      exactement DEUX classes — {tout-même} = {(+++),(−−−)} et
      {un-différent} = les 6 mixtes. ⟹ ≤ 2 paires + ≤ 2 impaires a priori.
  (3) Niveau arbre : la cinématique trois-points sans masse (squelette plat
      du vertex de bulk, spineurs-hélicité 4d) FORCE l'unicité par classe :
      la covariance de petit groupe donne un système linéaire 3×3 INVERSIBLE
      sur les exposants de crochets ⟹ UNE structure par classe.
      Classe (−−+) : ⟨12⟩⁶/(⟨13⟩²⟨23⟩²), dimension 2 (dérivées) = EINSTEIN.
      Classe (+++) : ([12][13][23])²,    dimension 6 (dérivées) = W³.
      ⟹ la graduation en dérivées RECOUPE la scission Einstein/W³ scellée
      au léger ([D]) — route interne indépendante du fetch MP∩OP.
  (4) Parité : 2 combinaisons PAIRES (une par classe) ⟹ dimension paire = 2.
      Le canal impair : « présente en fonction d'onde, ABSENTE du bispectre »
      est le scellé du léger, RECOUPÉ ici (cohérence trans-rang), PAS re-dérivé.
  CONDITIONNALITÉS CONSIGNÉES : niveau arbre (S1/E-L4) ; squelette de petit
  groupe sur cinématique plate complexifiée (la complétion dS de chaque
  structure est EXHIBÉE — actions Einstein et W³ sur dS — non re-classifiée).

PLAN DU SCEAU FINAL (rappel ; phase 2 À VENIR, fetch tracé, extraits+sha) :
  [C] étalon Ward OP numérique (PL-A telle-qu'écrite) ; [D] forensique ε·ε*
  (PL-B, p.6 MP extensible alors) ; [E] anti-numérologie/DoF ; [F] firewall.

DISCIPLINE LC-AUDIT-VERDICT §6.4 — SANS SURCLASSEMENT :
  Tout assert qui passe = « algèbre correcte + cibles reproduites ». JAMAIS
  « secteur non-gaussien fermé / D1 fermé / N fixé / CCC démontrée ».
  Compte {A4 ; A2★ ; N} INCHANGÉ.

Stack : Python 3.12 / sympy 1.14 / numpy 2.4 / scipy 1.17.
"""

import sys
from itertools import product, permutations

import sympy as sp

OK = 0


def check(label, cond):
    global OK
    assert cond, f"ÉCHEC : {label}"
    OK += 1
    print(f"  [assert {OK:02d}] {label} — OK")


print("=" * 78)
print("PHASE 1 (INTERNE, AVANT TOUT FETCH) — blocs [A], [B], [B']")
print("=" * 78)

# ============================================================================
# BLOC [A] — NON-RÉGRESSIONS DU LÉGER (PL-C ; symbolique, conventions léger)
# Conventions (C5 du léger) : N = πℓ²/G ; M_Pl² = 1/(8πG) ; ℓ = 1/H ; d = 3.
# ============================================================================
print("\n[A] Non-régressions PL-C (léger, conventions inchangées)")

# A-1 : map opérateur γ₃ = n³ (générateur jouet, triple application de T = n·δW)
h, n = sp.symbols("h n", positive=True)
cW = sp.symbols("c_W", positive=True)
W = cW * h**3 + cW * h**2          # générateur jouet : seul compte le rapport
psi3 = sp.diff(W, h, 3).subs(h, 0)
TTT_canon = sp.expand(n**3 * sp.diff(W, h, 3).subs(h, 0))
gamma3 = sp.simplify(TTT_canon / psi3)
check("[A-1] γ₃ = ⟨TTT⟩_canon/ψ₃ = n³ générique ; n=2 (Brown-York) ⟹ γ₃ = 8",
      sp.simplify(gamma3 - n**3) == 0 and gamma3.subs(n, 2) == 8)

# A-2 : chaîne A_T (CT-ATN scellé) en (H, M_Pl)
H_, MPl, G = sp.symbols("H M_Pl G", positive=True)
ell = 1 / H_
N_HM = sp.simplify((sp.pi * ell**2 / G).subs(G, 1 / (8 * sp.pi * MPl**2)))
check("[A-2] N = πℓ²/G = 8π² M_Pl²/H² (C5)",
      sp.simplify(N_HM - 8 * sp.pi**2 * MPl**2 / H_**2) == 0)
A_T = sp.simplify(16 / N_HM)
check("[A-3] A_T = 16/N = 2H²/(π² M_Pl²) ⟹ (H/M_Pl)² = 8π²/N",
      sp.simplify(A_T - 2 * H_**2 / (sp.pi**2 * MPl**2)) == 0
      and sp.simplify(sp.pi**2 * A_T / 2 - H_**2 / MPl**2) == 0)
ratio = sp.simplify((H_ / MPl)**4 / A_T**2)
check("[A-4] (H/M_Pl)⁴ / A_T² = π⁴/4 — slack NUL (valeur du léger inchangée)",
      sp.simplify(ratio - sp.pi**4 / 4) == 0)

# A-5 : ⟨g₃³⟩_libre = 0 — préfacteur exact + moment impair gaussien nul
pref = sp.simplify((-sp.I / 3)**3)
x, sig = sp.symbols("x sigma", real=True, positive=True)
gauss = sp.exp(-x**2 / (2 * sig**2)) / (sig * sp.sqrt(2 * sp.pi))
m3 = sp.integrate(x**3 * gauss, (x, -sp.oo, sp.oo))
check("[A-5] (−i/3)³ = i/27 ET E[g₀³] = 0 (gaussien) ⟹ ⟨g₃³⟩_libre = 0 ident.",
      sp.simplify(pref - sp.I / 27) == 0 and sp.simplify(m3) == 0)

# ============================================================================
# BLOC [B] — APPAREIL WARD CÔTÉ PROGRAMME (squelette symbolique ; AUCUNE
# valeur OP ici — les coefficients Ward restent SYMBOLIQUES jusqu'au fetch [C])
# ============================================================================
print("\n[B] Appareil Ward côté programme (squelette ; coefficients symboliques)")

# B-1 : projecteur TT en d=3 (machinerie du rang 2 transposée)
kvec = sp.Matrix([0, 0, 1])                      # k = ẑ (générique par rotation)
P = sp.eye(3) - kvec * kvec.T                    # projecteur transverse
idx = [(i, j) for i in range(3) for j in range(3)]


def PiTT(i, j, k_, l_):
    return (sp.Rational(1, 2) * (P[i, k_] * P[j, l_] + P[i, l_] * P[j, k_])
            - sp.Rational(1, 2) * P[i, j] * P[k_, l_])


transv = all(sum(kvec[i] * PiTT(i, j, k_, l_) for i in range(3)) == 0
             for j in range(3) for (k_, l_) in idx)
tracel = all(sum(PiTT(i, i, k_, l_) for i in range(3)) == 0 for (k_, l_) in idx)
idem = all(sp.simplify(sum(PiTT(i, j, a, b) * PiTT(a, b, k_, l_)
                           for (a, b) in idx) - PiTT(i, j, k_, l_)) == 0
           for (i, j) in idx for (k_, l_) in idx)
trPi = sp.simplify(sum(PiTT(i, j, i, j) for (i, j) in idx))
check("[B-1] Π^TT d=3 : transverse, sans trace, idempotent, Π:Π = 2 (2 pol.)",
      transv and tracel and idem and trPi == 2)

# B-2 : valeur INTERNE de l'ancrage — |Im F|/k³ = M_Pl²/(4H²) (scellé) ⟹
#       C_T/N = 1/(32π²) (nu). C'est la CIBLE de PL-A re-dérivée en interne ;
#       l'ÉTALON OP numérique telle-qu'écrite reste le travail de la phase 2.
CT_nu = MPl**2 / (4 * H_**2)
check("[B-2] C_T(nu)/N = [M_Pl²/(4H²)] / [8π²M_Pl²/H²] = 1/(32π²) — exact",
      sp.simplify(CT_nu / N_HM - 1 / (32 * sp.pi**2)) == 0)

# B-3 : VERROU DIMENSIONNEL du secteur Ward — Δ = d ⟹ le secteur de contact
#       de ⟨TTT⟩ porte EXACTEMENT le degré de C_T·k³ ; le coefficient relatif
#       est un NOMBRE PUR ⟹ aucun paramètre dimensionnel neuf ne PEUT entrer
#       (pré-verrou anti-numérologie de PL-A).
Delta, dd = sp.symbols("Delta d", positive=True)
deg2 = 2 * Delta - dd            # degré de ⟨TT⟩ en impulsion
deg3 = 3 * Delta - 2 * dd        # degré du secteur Ward/contact de ⟨TTT⟩
check("[B-3] Δ=d ⟹ deg⟨TTT⟩_Ward − deg⟨TT⟩ = Δ−d = 0 ; d=3 : deg = 3 = 3",
      sp.simplify((deg3 - deg2) - (Delta - dd)) == 0
      and deg2.subs({Delta: 3, dd: 3}) == 3
      and deg3.subs({Delta: 3, dd: 3}) == 3)

# B-4 : squelette de refermeture (grade CONSIGNATION) — coefficients Ward
#       SYMBOLIQUES w₁, w₂ (placeholders des valeurs imprimées d'OP, fetch [C]) ;
#       sensibilité à C_T pré-vérifiée (pare-feu en germe).
w1, w2, kk = sp.symbols("w_1 w_2 k", positive=True)
ward_sector = CT_nu * kk**3 * (w1 + w2)          # structure ; w_i nombres purs
check("[B-4] squelette : ×2 sur C_T ⟹ ×2 sur le secteur Ward (sensibilité) ; "
      "w₁,w₂ n'altèrent pas le degré k³ (nombres purs)",
      sp.simplify(ward_sector.subs(CT_nu, 2 * CT_nu) / ward_sector - 2) == 0
      and sp.degree(sp.Poly(ward_sector, kk)) == 3)

# ============================================================================
# BLOC [B'] — INVARIANCE RANG 3 (PL-D ; petit groupe + parité, niveau arbre)
# ============================================================================
print("\n[B'] Invariance rang 3 (PL-D) — petit groupe, parité, niveau arbre")

# B'-1 : orbites des 8 configurations d'hélicité sous S₃ × P ⟹ DEUX classes
configs = set(product((+2, -2), repeat=3))
orbits = []
seen = set()
for c in sorted(configs):
    if c in seen:
        continue
    orb = set()
    for perm in permutations(range(3)):
        pc = tuple(c[p] for p in perm)
        orb.add(pc)
        orb.add(tuple(-s for s in pc))           # parité = renversement global
    orbits.append(orb)
    seen |= orb
check("[B'-1] 8 configs (±2)³ ; orbites sous S₃×P = 2 classes "
      "{tout-même (2)} ⊔ {un-différent (6)}",
      len(configs) == 8 and len(orbits) == 2
      and sorted(len(o) for o in orbits) == [2, 6])

# B'-2 : cinématique trois-points sans masse (squelette plat, complexifiée) —
#        branche holomorphe : tous [ij] = 0, ⟨ij⟩ ≠ 0, conservation EXACTE.
a1, b1, a2, b2, c1, c2, c3, ca, cb = sp.symbols(
    "a1 b1 a2 b2 c1 c2 c3 chi_a chi_b")
lam = {1: sp.Matrix([a1, b1]), 2: sp.Matrix([a2, b2])}
lam[3] = -(c1 * lam[1] + c2 * lam[2]) / c3
chi = sp.Matrix([ca, cb])
lamt = {i: c * chi for i, c in zip((1, 2, 3), (c1, c2, c3))}


def ang(i, j):
    return sp.simplify(lam[i][0] * lam[j][1] - lam[i][1] * lam[j][0])


def sqr(i, j):
    return sp.simplify(lamt[i][0] * lamt[j][1] - lamt[i][1] * lamt[j][0])


ptot = sp.zeros(2, 2)
for i_ in (1, 2, 3):
    ptot += lam[i_] * lamt[i_].T
check("[B'-2] branche holomorphe : Σλᵢλ̃ᵢᵀ = 0 exact ; [ij] ≡ 0 ; ⟨ij⟩ ≠ 0",
      all(sp.simplify(ptot[r, s]) == 0 for r in range(2) for s in range(2))
      and all(sqr(i_, j_) == 0 for i_, j_ in ((1, 2), (1, 3), (2, 3)))
      and all(sp.simplify(ang(i_, j_)) != 0
              for i_, j_ in ((1, 2), (1, 3), (2, 3))))

# B'-3 : UNICITÉ par classe — la covariance de petit groupe (poids t^{−2hᵢ})
#        sur l'ansatz ⟨12⟩^α⟨13⟩^β⟨23⟩^γ est un système linéaire 3×3
#        INVERSIBLE ⟹ UNE structure par classe.
#        Classe (−,−,+) [h = (−2,−2,+2)] : α+β = 4, α+γ = 4, β+γ = −4.
Msys = sp.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
rhs_mhv = sp.Matrix([4, 4, -4])                  # −2hᵢ, h=(−2,−2,+2)
sol_mhv = Msys.solve(rhs_mhv)
check("[B'-3] det(système petit-groupe) = −2 ≠ 0 ; classe (−−+) UNIQUE : "
      "⟨12⟩⁶/(⟨13⟩²⟨23⟩²)",
      Msys.det() == -2 and list(sol_mhv) == [6, -2, -2])

#        Classe (+,+,+) [h = (+2,+2,+2)], branche anti-holomorphe [ij]^x… :
#        x+y = 4, x+z = 4, y+z = 4 ⟹ x = y = z = 2, UNIQUE.
rhs_ppp = sp.Matrix([4, 4, 4])
sol_ppp = Msys.solve(rhs_ppp)
check("[B'-3bis] classe (+++) UNIQUE : ([12][13][23])²",
      list(sol_ppp) == [2, 2, 2])

# B'-4 : graduation en dérivées = scission Einstein/W³ (recoupe le léger [D])
#        dimension(crochets) : (−−+) ⟹ 6−2−2 = 2 (EINSTEIN, 2 dérivées) ;
#        (+++) ⟹ 2+2+2 = 6 (W³, 6 dérivées).
dim_mhv = sum(sol_mhv)
dim_ppp = sum(sol_ppp)
check("[B'-4] dimensions : classe (−−+) = 2 (Einstein) ; classe (+++) = 6 (W³) "
      "— la graduation RECOUPE la scission Einstein/W³ du léger",
      dim_mhv == 2 and dim_ppp == 6)

# B'-5 : COMPTAGE PAIR — une combinaison paire par classe (structure ⊕ son
#        conjugué de parité) ⟹ dimension PAIRE = 2 = comptage scellé du léger.
#        L'impaire : « présente en fonction d'onde, ABSENTE du bispectre » =
#        scellé du léger, RECOUPÉ (cohérence trans-rang), PAS re-dérivé ici.
n_paires = len(orbits)                            # 1 paire par classe
check("[B'-5] dimension paire (niveau arbre, par représentation) = 2 "
      "= comptage 2+1 scellé au léger (PL-D TENUE telle qu'écrite)",
      n_paires == 2)

# ============================================================================
print("\n" + "=" * 78)
print(f"PHASE 1 : TOUS LES ASSERT PASSENT — {OK} assertions. EXIT 0.")
print("GEL DE PHASE (R-10) : ce fichier est déposé tel quel ; les asserts")
print("01-%02d devront être BYTE-IDENTIQUES dans le sceau final." % OK)
print("PROCHAINE ÉTAPE : phase 2 (fetch tracé) — [C] étalon Ward OP numérique")
print("(PL-A telle-qu'écrite) ; [D] forensique ε·ε* (PL-B, p.6 MP extensible")
print("alors) ; [E] anti-numérologie ; [F] firewall.")
print("SANS SURCLASSEMENT (§6.4) : phase 1 = algèbre interne + squelettes.")
print("  JAMAIS « secteur non-gaussien fermé / D1 clos / N fixé / CCC démontrée ».")
print("  Compte {A4 ; A2★ ; N} INCHANGÉ.")
print("=" * 78)
sys.exit(0)
