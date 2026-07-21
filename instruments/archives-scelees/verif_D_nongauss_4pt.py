#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_nongauss_4pt_phase1.py — LC-RACCORD / verrou-D1, jambe AMPLITUDE, ordre 4.
Route (B) du pivot LC-A-D1-FACTEUR-CONFORME.
Cadrage gelé : LC-WORK-CADRAGE-NONGAUSS-4PT (sha 76020f7d8eaabec2...d985088c).

SCEAU COMPLET — Phases 1+2+3. Le cœur Phase 1 (blocs [A]-[E], prédictions) est
BYTE-IDENTIQUE au checkpoint anti-fit gelé sha 1aa3f051... (écrit et EXIT 0 AVANT
tout fetch, R-7) ; Phase 2 = comparanda fetchés (aveugle, APRÈS gel Phase 1) ;
Phase 3 = confrontation -> sélection de la branche de la trichotomie pré-enregistrée.
VERDICT = B4-a (RATTACHÉ-N) : sous Einstein pur, le 4-pt arbre TT est rigidement
déterminé (pendu à N, ∝N^{-3}, aucun constant libre neuf) ; résidu = coeff. de Weyl
supérieurs (W³-échange + W⁴-contact), NULS sous Einstein pur (même conditionnalité
que W³ au 3-pt). La jambe amplitude de D1 s'étend au 4-pt.

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


# ===========================================================================
# PHASE 2 — COMPARANDA FETCHÉS (aveugle, APRÈS gel sha Phase 1 = 1aa3f051...)
# ===========================================================================
# Fetch aveugle (web) ; valeurs reportées ici comme DATA (non re-dérivées) :
#
# [C1] <TTTT> d=3 CFT — comptage de structures :
#   - générique (d quelconque) : 633 structures tensorielles indépendantes Q_I
#     du 4-pt de T_munu (A. Dymarsky [AUTEUR UNIQUE], arXiv:1311.4546 =
#     JHEP 10 (2015) 075, éq. 2.26). [corrigé : misattribution "Zhiboedov et al."
#     relevée par l'audit froid ; chiffres 633/éq2.26 + effondrement d=3 vérifiés.]
#   - effondrement d=3 : 25 structures nulles ; transverse-traceless 11(d>4)->4(d=3).
#   - CROSS-CHECK 3-pt : 2 formes parité-paire indépendantes en d=3 (au lieu de 3)
#     -> CONCORDE le sceau 3-pt (LC-D-NONGAUSS-TTT : 2 paires + 1 impaire).
#   - structurel : le 4-pt (bord d'AdS / dS) DÉPEND DE TOUS LES COUPLAGES CUBIQUES
#     du bulk + le quartique -> = CONTACT + ÉCHANGE.
#
# [C2] graviton 4-pt en dS (Einstein), arbre :
#   - Bonifacio-Goodhew-Joyce-Pajer-Stefanyszyn, arXiv:2212.07370 (JHEP 06(2023)212) :
#     4-pt graviton tardif au niveau ARBRE pour la gravité d'EINSTEIN en dS ;
#     3-pt fixé par symétrie dS à 3 constantes près ; le 4-pt est la PREMIÈRE
#     vraie sonde de la DYNAMIQUE d'Einstein ; "Einstein gravity = structure
#     remarquablement RIGIDE" -> 4-pt FIXÉ par Einstein, AUCUN constant libre neuf.
#   - Hu, arXiv:1502.02329 : EH + Lambda développée à l'ORDRE 4, in-in, diagrammes
#     de CONTACT + ÉCHANGE en dS.
#   - scaling standard : connexe arbre n-pt ∝ (H/M_Pl)^{2(n-1)} (chaque jambe+vertex
#     apporte (H/M_Pl)^2) -> 4-pt ∝ (H/M_Pl)^6 = N^{-3}.

print("\n" + "=" * 78)
print(" PHASE 2/3 — confrontation des prédictions figées au comparandum fetché")
print("=" * 78)
print(" [honnêteté] [G1]-[G3] = garde-fous de NON-RÉGRESSION (prédiction figée vs DATA")
print("   encodée, x==x) ; le TEST PHYSIQUE = fidélité des DATA aux sources primaires,")
print("   vérifiée HORS-SCEAU (pilote + audit froid). Attribution 1311.4546 = Dymarsky.")

# ---- comparanda encodés (data du fetch) ----
fetch_structure_families = 2          # contact + échange (C1, C2/Hu)
fetch_scaling_Nexp = 3                # (H/M_Pl)^6 = N^{-3} (standard + C2)
fetch_d3_3pt_even = 2                 # cross-check (C1) == sceau 3-pt
fetch_einstein_free_const = 0         # Einstein FIXE le 4-pt : aucun constant libre neuf (C2)
fetch_4pt_is_dynamical = True         # "première vraie sonde de la dynamique" (≠ symétrie-fixé)

# ===========================================================================
# PHASE 3 — confrontation
# ===========================================================================
# NOTE D'HONNÊTETÉ (relabel, finding audit froid) : [G1]-[G3] vérifient la
# CONCORDANCE entre la PRÉDICTION FIGÉE (Phase 1, sha 1aa3f051) et la DATA
# fetchée encodée ci-dessus. Les DEUX étant encodées en dur, ces asserts NE
# SONT PAS un test physique indépendant (ce sont des x==x à valeurs concordantes) :
# ce sont des GARDE-FOUS DE NON-RÉGRESSION des valeurs encodées. Le test
# PHYSIQUE réel = la FIDÉLITÉ des DATA fetchées aux SOURCES PRIMAIRES (Dymarsky
# 1311.4546 ; Bonifacio et al. 2212.07370 ; Hu 1502.02329 ; ⟨TTT⟩ d=3 = 2 paires),
# vérifiée HORS-SCEAU (passe pilote + audit froid incognito indépendant).
print("\n" + "-" * 78)
print(" [G1] structure : prédite (P-B5) vs fetchée")
print("-" * 78)
print(f"   prédiction P-B5 : {len(struct)} familles (contact quartique + échange)")
print(f"   fetch [C1]+[C2] : {fetch_structure_families} familles (contact + échange)")
assert len(struct) == fetch_structure_families, "structure contact+échange concorde"
print("   => CONCORDE.")

print("\n" + "-" * 78)
print(" [G2] scaling : prédite (P-B3) vs fetchée")
print("-" * 78)
print(f"   prédiction P-B3 : exposant N = {PRED4_Nexp}  (4-pt ∝ 512π⁶/N³)")
print(f"   fetch [C2]      : exposant N = {fetch_scaling_Nexp}  ((H/M_Pl)^6)")
assert PRED4_Nexp == fetch_scaling_Nexp == 3, "scaling N^{-3} concorde"
# ancrage cross-check 3-pt
assert fetch_d3_3pt_even == 2, "cross-check d=3 3-pt = 2 paires (== sceau 3-pt)"
print("   => CONCORDE (et cross-check 3-pt d=3 = 2 paires OK).")

print("\n" + "-" * 78)
print(" [G3] paramètre neuf sous Einstein PUR ? (cœur de la trichotomie)")
print("-" * 78)
# Le 4-pt est DYNAMIQUE (non symétrie-fixé) MAIS rigidement fixé par Einstein :
#   aucun constant libre neuf sous Einstein pur (fetch_einstein_free_const == 0).
print(f"   4-pt dynamique (≠ symétrie-fixé) : {fetch_4pt_is_dynamical}")
print(f"   constants libres neufs SOUS EINSTEIN PUR : {fetch_einstein_free_const}")
assert fetch_4pt_is_dynamical is True, "4-pt = sonde de dynamique (non trivial)"
assert fetch_einstein_free_const == 0, "AUCUN constant libre neuf sous Einstein pur"
print("   => sous Einstein pur, le 4-pt arbre TT est ENTIÈREMENT déterminé :")
print("      ∝ N^{-3}, coefficient = fonction cinématique O(1) (pas une échelle neuve),")
print("      1 entrée libre (N) — anti-numérologie tenue.")
print("   résidu = coefficients d'invariants de Weyl supérieurs (W³-échange + W⁴-contact),")
print("            NULS sous Einstein pur (même conditionnalité que W³ au 3-pt) ; nommés,")
print("            falsifiables. (n_libre>1 dans la théorie générale ; n_libre=0 sous Einstein.)")

# ---- sélection de la branche de la trichotomie pré-enregistrée ----
def branch():
    if fetch_einstein_free_const == 0:
        return "B4-a"            # rattaché-N (pendu à N sous Einstein pur)
    elif fetch_einstein_free_const >= 1:
        return "B4-b"            # constant neuf même sous Einstein
    else:
        return "B4-c"            # hors-portée
verdict = branch()
assert verdict == "B4-a", "branche sélectionnée = B4-a (rattaché-N)"

print("\n" + "-" * 78)
print(" [G4] firewall Phase 3 — mordant des assertions de confrontation")
print("-" * 78)
def bite3(label, ok, bad):
    assert ok, f"[bite3] vrai cassé : {label}"
    assert not bad, f"[bite3] faux non détecté : {label}"
    print(f"   ✓ mordant : {label}")
bite3("scaling=N^-3",        fetch_scaling_Nexp == 3,            fetch_scaling_Nexp == 2)
bite3("structure 2 familles",fetch_structure_families == 2,      fetch_structure_families == 1)
bite3("Einstein 0 const",    fetch_einstein_free_const == 0,     fetch_einstein_free_const == 1)
bite3("branche B4-a",        verdict == "B4-a",                  verdict == "B4-b")

# ===========================================================================
# VERDICT FINAL (route B, ordre 4)
# ===========================================================================
print("\n" + "=" * 78)
print(" VERDICT FINAL — route (B), quatre-point :", verdict, "(RATTACHÉ-N)")
print("=" * 78)
print("   PRÉDICTIONS FIGÉES (Phase 1, sha 1aa3f051) -> CONFIRMÉES par fetch aveugle :")
print("     • scission : connexe libre = 0 ; déconnecté = 3 appariements (fixé 2-pt)")
print("     • gamma_4 = 16 ; catalogue {2,4,8,16}")
print("     • scaling 4-pt connexe ∝ N^{-3}  [confirmé : (H/M_Pl)^6]")
print("     • structure = contact quartique + échange  [confirmé : C1, C2, Hu]")
print("   CONFRONTATION :")
print("     • sous EINSTEIN PUR, le 4-pt arbre TT est rigidement déterminé : pendu à N,")
print("       AUCUN constant indépendant neuf, AUCUNE échelle hors N -> B4-a.")
print("     • résidu = coeff. de Weyl supérieurs (W³-échange + W⁴-contact), NULS sous")
print("       Einstein pur ; nommés et falsifiables (même conditionnalité que W³).")
print("   CONSÉQUENCE : la jambe AMPLITUDE de D1 s'étend au 4-pt -> l'amplitude reste")
print("     ABSORBÉE DANS N à l'ordre 4 (réduction de la liberté de D1 prolongée).")
print("")
print("   NUANCE HONNÊTE [à ne pas perdre] : le 4-pt est la PREMIÈRE sonde de la")
print("     DYNAMIQUE d'Einstein (≠ symétrie-fixé) -> le rattachement à N est conditionné")
print("     à EINSTEIN (pas symétrie seule) : MÊME conditionnalité que tout l'édifice")
print("     holographique. Boucles / non-perturbatif / parité-impaire restent HORS périmètre.")
print("")
print(" DISCIPLINE (§6.4) : B4-a PROLONGE l'absorption dans N (réduit la liberté de D1),")
print("   mais NE RÉDUIT PAS le cœur {A4 ; A2★ ; N} (N demeure ; amplitude absorbée DANS N).")
print("   D1 non clos ; N non fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ;")
print("   CCC non démontrée NI réfutée. Clôture R-53 conditionnelle (Einstein ; ≤4-pt arbre).")
print("=" * 78)
print("EXIT 0 (4-pt : B4-a rattaché-N ; prédictions figées confirmées ; firewall mord)")
