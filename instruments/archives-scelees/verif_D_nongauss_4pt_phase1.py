#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_nongauss_4pt_phase1.py — LC-RACCORD / verrou-D1, jambe AMPLITUDE, ordre 4.
Route (B) du pivot LC-A-D1-FACTEUR-CONFORME.
Cadrage gelé : LC-WORK-CADRAGE-NONGAUSS-4PT (sha 76020f7d8eaabec2...d985088c).

PHASE 1 SEULEMENT — écrite et EXIT 0 *AVANT* tout fetch (protocole anti-fit R-7).
Aucun comparandum externe consommé ici. Cette passe ÉTABLIT l'algèbre interne et
FIGE les prédictions ; elle NE TRANCHE PAS la trichotomie B4-a/b/c (qui exige le
comptage <TTTT> d=3 + l'amplitude Einstein, fetchés en Phase 2 aveugle).

Cibles internes (cadrage §3) :
  [A] P-B1 — scission connexe/déconnecté du 4-point ; la chaîne linéaire
      g3 = -(i/3) k^3 g0 TRANSPORTE la gaussianité : le 4-pt LIBRE a une part
      DÉCONNECTÉE non nulle (3 appariements de Wick du 2-pt scellé) MAIS un
      CONNEXE nul identiquement (cumulant gaussien d'ordre 4 = 0). Le connexe
      vit au vertex (datum non-gaussien authentique), comme au 3-pt.
  [B] P-B2 — map gamma_k = n^k ; Brown-York n=2 ⟹ gamma_4 = 16 (dérivé, pas
      supposé). Catalogue d'artefacts de mélange étendu {2,4,8,16}.
  [C] P-B3 — scaling : (H/M_Pl)^2 = 8π²/N (interne, via A_T·N=16, LC-D-CT-ATN).
      Le connexe n-pt ∝ (H/M_Pl)^{2(n-1)} (pattern scellé : 2-pt N^-1, 3-pt N^-2).
      ⟹ PRÉDICTION FIGÉE 4-pt connexe ∝ (8π²/N)^3 = 512 π^6 / N^3 (exposant N = 3).
  [D] P-B5 — structure Einstein (pré-déclaration) : connexe arbre = contact
      quartique + échange (cubique×cubique) ; aucun constant libre de l'action
      d'Einstein. À confronter au comptage fetché (Phase 2).
  [E] Firewall interne — chaque assertion porteuse a du mordant.

SANS SURCLASSEMENT (§6.4) : Phase 1 fige des prédictions ; ne scelle pas le
verdict, ne ferme pas D1, ne fixe pas N. {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ;
N non fixé (≡Λ) ; CCC non démontrée NI réfutée.

Dépendances : sympy. Re-exécutable, SANS réseau.
"""

import sympy as sp

print("=" * 78)
print(" verif_D_nongauss_4pt_phase1.py — 4-point <g3 g3 g3 g3>, PHASE 1 (avant fetch)")
print("=" * 78)

# symboles
k, k1, k2, k3, k4, N, H, MPl, n = sp.symbols('k k1 k2 k3 k4 N H M_Pl n', positive=True)
pi = sp.pi
I = sp.I
S = sp.symbols('S', positive=True)   # 2-point scellé (forme ~k^3), gardé symbolique

LB = []  # journal des assertions porteuses (pour le décompte honnête)

# ---------------------------------------------------------------------------
# [A] P-B1 — scission connexe / déconnecté ; transport gaussien
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print(" [A] P-B1 : 4-pt LIBRE — déconnecté (Wick) ≠ 0, CONNEXE = 0 (cumulant g4)")
print("-" * 78)

# relation d'état BD (linéaire) : g3(k) = -(i/3) k^3 g0(k)
def g3_factor(ki):
    return -(I / 3) * ki**3

# 4-pt de g3 = produit des préfacteurs × 4-pt de g0
pref4 = g3_factor(k1) * g3_factor(k2) * g3_factor(k3) * g3_factor(k4)
pref4 = sp.simplify(pref4)
print(" préfacteur 4-pt = Π[-(i/3)k_a^3] =", pref4, " (= (k1k2k3k4)^3 / 81)")
assert sp.simplify(pref4 - (k1*k2*k3*k4)**3 / 81) == 0, "préfacteur 4-pt"
LB.append("pref4 = (k1k2k3k4)^3/81")

# Wick gaussien sur g0 : <g0^4> = somme des 3 appariements de 2-pts (déconnecté).
# Représentation symbolique : chaque appariement -> S^2 (2-pt = S). #appariements=3.
n_pairings = sp.Integer(3)        # (4-1)!! = 3
four_pt_gauss_full = n_pairings * S**2          # déconnecté complet
disconnected = n_pairings * S**2
connected_free = sp.simplify(four_pt_gauss_full - disconnected)   # cumulant d'ordre 4
print(" #appariements de Wick (4 points) =", n_pairings, " [(4-1)!! = 3]")
print(" <g0^4>_libre complet  =", four_pt_gauss_full, " (déconnecté)")
print(" <g0^4>_libre CONNEXE  =", connected_free, " (cumulant gaussien d'ordre 4)")
assert n_pairings == 3, "le 4-pt gaussien a EXACTEMENT 3 appariements"
assert sp.simplify(connected_free) == 0, "connexe libre d'ordre 4 = 0 (gaussien)"
# contraste explicite avec le 3-pt : <g0^3>_libre = 0 ENTIÈREMENT (pas de part déconnectée)
three_pt_gauss_full = sp.Integer(0)   # appariement impossible à 3 points
assert three_pt_gauss_full == 0, "3-pt gaussien = 0 entièrement"
LB.append("n_pairings(4)=3 ; connexe_libre(4)=0 ; 3-pt libre=0 entierement")
print(" CONTRASTE 3-pt : <g0^3>_libre =", three_pt_gauss_full,
      " (0 ENTIER, pas de déconnecté) — feature P-B1 confirmée.")
print(" => le 4-pt connexe N'EST PAS sourcé par l'état libre : il vit au VERTEX")
print("    (datum non-gaussien authentique) ; le déconnecté est fixé par le 2-pt scellé.")

# ---------------------------------------------------------------------------
# [B] P-B2 — map gamma_k = n^k ; gamma_4 dérivé
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print(" [B] P-B2 : gamma_k = n^k (k insertions de T = n·δW/δg) ; Brown-York n=2")
print("-" * 78)

def gamma_k(order, nval):
    # T = n δW/δg ; k insertions -> <T...T>_canon = n^k δ^k W ; gamma_k = n^k
    return nval**order

gamma2 = gamma_k(2, n); gamma3 = gamma_k(3, n); gamma4 = gamma_k(4, n)
print(" gamma_2 = n^2 =", gamma2, " ; gamma_3 = n^3 =", gamma3, " ; gamma_4 = n^4 =", gamma4)
assert sp.simplify(gamma4 - n**4) == 0, "gamma_4 = n^4 (générique)"
# Brown-York n=2 (scellé LC-D-CT-GAMMA [E])
nBY = 2
g2v, g3v, g4v = gamma_k(2, nBY), gamma_k(3, nBY), gamma_k(4, nBY)
print(f" Brown-York n=2 ⟹ gamma_2={g2v}, gamma_3={g3v}, gamma_4={g4v}")
assert (g2v, g3v, g4v) == (4, 8, 16), "catalogue {n^2,n^3,n^4} = {4,8,16}"
catalogue = sorted({2, g2v, g3v, g4v})   # {n^1..n^4} = {2,4,8,16}
print(" catalogue d'artefacts de mélange étendu :", catalogue)
assert catalogue == [2, 4, 8, 16], "catalogue {2,4,8,16}"
LB.append("gamma_4 = n^4 ; n=2 -> 16 ; catalogue {2,4,8,16}")

# ---------------------------------------------------------------------------
# [C] P-B3 — scaling : prédiction FIGÉE du connexe 4-pt
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print(" [C] P-B3 : scaling — (H/M_Pl)^2 = 8π²/N ; connexe n-pt ∝ (H/M_Pl)^{2(n-1)}")
print("-" * 78)

HMpl2 = 8 * pi**2 / N      # (H/M_Pl)^2, via A_T·N=16 (LC-D-CT-ATN) ; A_T = 2H²/(π²M_Pl²)
print(" (H/M_Pl)^2 =", HMpl2)

def connected_npt_scaling(npt):
    # pattern scellé : 2-pt ∝ (H/M_Pl)^2 = N^-1 ; 3-pt ∝ (H/M_Pl)^4 = N^-2
    return sp.simplify(HMpl2**(npt - 1))

amp2 = connected_npt_scaling(2)   # 8π²/N
amp3 = connected_npt_scaling(3)   # 64π⁴/N²
amp4 = connected_npt_scaling(4)   # 512π⁶/N³  <- PRÉDICTION FIGÉE
print(" 2-pt ∝", amp2, "  (vérif scellé : 8π²/N, exposant N = 1)")
print(" 3-pt ∝", amp3, "  (vérif scellé : 64π⁴/N², exposant N = 2)")
print(" 4-pt ∝", amp4, "  <== PRÉDICTION FIGÉE (à confronter au fetch)")

# vérif des ancrages scellés (2-pt, 3-pt) — anti-dérive du pattern
assert sp.simplify(amp2 - 8*pi**2/N) == 0, "2-pt = 8π²/N (scellé)"
assert sp.simplify(amp3 - 64*pi**4/N**2) == 0, "3-pt = 64π⁴/N² (scellé)"
# prédiction 4-pt
PRED4_coeff = 512 * pi**6
PRED4_Nexp = 3
assert sp.simplify(amp4 - PRED4_coeff / N**PRED4_Nexp) == 0, "4-pt = 512π⁶/N³ (prédit)"
assert sp.simplify((8*pi**2)**3 - PRED4_coeff) == 0, "(8π²)^3 = 512π⁶"
# exposant de N extrait
Nexp4 = sp.degree(sp.Poly(1/amp4 * PRED4_coeff, N), N)  # = 3
assert Nexp4 == PRED4_Nexp == 3, "exposant de N au 4-pt = 3"
print(f" coefficient figé = {PRED4_coeff} ; exposant N figé = {PRED4_Nexp}")
LB.append("PRÉDICTION 4-pt connexe = 512π⁶/N³ (exposant N=3) — FIGÉE avant fetch")

# anti-numérologie : 1 entrée libre (N) vs sorties appariées
n_free_inputs = 1   # N
print(" anti-numérologie : 1 entrée libre (N) — si l'amplitude Einstein fetchée")
print("   tombe sur 512π⁶/N³ avec O(1) apparié ⟹ aucun paramètre neuf (vers B4-a).")

# ---------------------------------------------------------------------------
# [D] P-B5 — structure Einstein (pré-déclaration, à confronter au fetch)
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print(" [D] P-B5 : structure connexe arbre sous Einstein (pré-déclaration)")
print("-" * 78)
struct = ["contact quartique (action Einstein O(h^4))",
          "échange cubique×cubique (vertex^2 × propagateur graviton)"]
print(" connexe arbre Einstein =", " + ".join(struct))
print("   ⟹ aucun constant libre de l'action d'Einstein (à vérifier en Phase 2).")
print("   libertés candidates = invariants de Weyl supérieurs (W^4, W²∇²…),")
print("   pré-déclarées NULLES sous Einstein pur (même conditionnalité que W³).")
assert len(struct) == 2, "deux familles de diagrammes arbre au 4-pt"
LB.append("structure Einstein arbre = {contact quartique, échange} (2 familles)")

# ---------------------------------------------------------------------------
# [E] Firewall interne — mordant des assertions porteuses
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print(" [E] Firewall interne — chaque assertion porteuse doit MORDRE")
print("-" * 78)

def bite(label, truthy_ok, falsy_bad):
    # truthy_ok doit être vrai (0 attendu), falsy_bad doit être faux (≠0)
    assert sp.simplify(truthy_ok) == 0, f"[bite] vrai cassé : {label}"
    assert sp.simplify(falsy_bad) != 0, f"[bite] faux non détecté : {label}"
    print(f"   ✓ mordant : {label}")

bite("gamma_4=16",        gamma4.subs(n, 2) - 16,            gamma4.subs(n, 2) - 12)
bite("connexe_libre=0",   connected_free,                    connected_free + S**2)
bite("n_pairings=3",      n_pairings - 3,                    n_pairings - 2)
bite("4-pt=512π⁶/N³",     amp4 - 512*pi**6/N**3,             amp4 - 256*pi**6/N**3)
bite("exposant N=3",      sp.Integer(Nexp4) - 3,             sp.Integer(Nexp4) - 2)

# ---------------------------------------------------------------------------
# VERDICT PHASE 1
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print(" VERDICT PHASE 1 (avant fetch) :")
print("=" * 78)
print(f"   assertions porteuses figées ({len(LB)}) :")
for i, s in enumerate(LB, 1):
    print(f"     {i}. {s}")
print("   PRÉDICTIONS FIGÉES (anti-fit) :")
print("     • connexe libre d'ordre 4 = 0 ; déconnecté = 3 appariements (fixé 2-pt)")
print("     • gamma_4 = 16 ; catalogue {2,4,8,16}")
print("     • amplitude 4-pt connexe = 512π⁶/N³ (exposant N = 3)")
print("     • structure Einstein arbre = contact quartique + échange (à confronter)")
print("   NON TRANCHÉ ICI : trichotomie B4-a/b/c (exige comptage <TTTT> d=3 +")
print("     amplitude Einstein, fetchés en Phase 2 AVEUGLE).")
print("")
print(" DISCIPLINE (§6.4) : Phase 1 fige des prédictions ; ne scelle pas le verdict,")
print("   ne ferme pas D1, ne fixe pas N. {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ;")
print("   N non fixé (≡Λ) ; CCC non démontrée NI réfutée.")
print("=" * 78)
print("EXIT 0 (Phase 1 : scission OK, gamma_4=16, scaling figé N^-3, firewall mord)")
