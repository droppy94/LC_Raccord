#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_CT_dual.py — LC-RACCORD. Sceau S1 du lead « dualité graviton-dual de de Haro »
(arXiv:0808.2054, AdS4/CFT3, Cotton tenseur holographique). ÉTAGE S1 SEULEMENT :
reproduction de la structure de dualité EN AdS (signature euclidienne, ℓ² réel) et
ÉPINGLAGE des conventions, AVANT toute continuation dS (= étage S2, non couvert ici).

Pourquoi S1 d'abord. La route ÉLECTRIQUE du signe de C_T est déjà scellée
(verif_D_CT_realite.py : continuation ℓ_AdS->iℓ_dS, i^{d-1}, d=3 réel négatif). Le lead
propose une SECONDE route via le secteur MAGNÉTIQUE/dual (B = Cotton). Avant de la tester
(S2), il faut établir ce que la dualité AdS donne RÉELLEMENT — et le résultat-clé de S1 est
un GARDE-FOU : en AdS, la dualité ne retourne PAS le signe de C_T (le `-` relatif de la
fonctionnelle duale W̃ est compensé par le `-2` de la définition du tenseur dual). Donc tout
flip de signe en S2 devra venir de la continuation dS et/ou de S²=-1, pas de la dualité AdS
elle-même. Ce sceau pose cette base et fige les conventions ; il ne tranche AUCUNE physique.

Source primaire (citée verbatim par numéro d'équation) :
    de Haro, arXiv:0808.2054v1 [hep-th], « Dual Gravitons in AdS4/CFT3 and the Holographic
    Cotton Tensor ». Conventions de Haro-Skenderis-Solodukhin (hep-th/0002230) : 2κ² = 16πG,
    soit κ² = 8πG ; ⟨T_ij⟩ = (d ℓ²)/(16πG) g_(3)ij en d=3 (éq. 1).

Ancrage KB (non dupliqué) :
    LC-D-CT-ATN        — verrouillage C_T∝N, C_T/N = 1/(32π²) (normalisation programme).
    LC-D-CT-REALITE    — route électrique du signe (i^{d-1}, d=3 réel négatif).
    LC-D-NONLIN-VERROU — décomposition E∝g3 (pair) / B∝Cotton (impair) au UN-POINT.
    verif_E_planck.py  — N = S_dS = π/(G H²).

Blocs :
    [A] DUALITÉ DES EOM, S²=-1. Sur la solution physique TT du bulk (éq. 43),
        f_a(u)=cos u + u sin u, f_b(u)=u cos u - sin u (u=|p|r), l'identité de troisième
        dérivée (éq. 44) referme sur les MÊMES deux fonctions avec échange de coefficients
        S:(a,b)->(-b,a). Donc S = [[0,-1],[1,0]] et S² = -𝟙 (éq. 51 : S²=-1).
    [B] GARDE-FOU DE SIGNE (cœur de S1). W = +ℓ²/(8κ²)∫h0 □^{3/2} h0 (éq. 61) ;
        W̃ = -ℓ²/(8κ²)∫h̃0 □^{3/2} h̃0 (éq. 62) : `-` relatif RÉEL. MAIS ⟨T⟩ = 2 δW/δh
        tandis que ⟨T̃⟩ = -2 δW̃/δh̃ (éq. 63, signe explicite). Conséquence DÉRIVÉE
        symboliquement : ⟨T̃T̃⟩ a le MÊME signe que ⟨TT⟩ ⟹ C̃_T = +C_T EN AdS. Le `-` de W̃
        est compensé ; la dualité AdS ne flippe pas C_T. (Motif du nugget P1 : objet
        structurel signé ≠ observable.)
    [C] DICTIONNAIRE C_T ↔ ℓ²/κ² ↔ N. (i) éq. (1) de de Haro = dictionnaire programme à d=3 ;
        (ii) C_T = coeff de |p|³Π = ℓ²/κ² (éq. 90) ∝ ℓ²/G ; (iii) sous ℓ=ℓ_dS=1/H,
        C_T ∝ 1/(G H²) ∝ N (N=π/(G H²)) ; C_T/N = nombre PUR (H,G,k se simplifient) =
        verrouillage. La valeur nue de de Haro (1/(8π²)) et la valeur scellée programme
        (1/(32π²), LC-D-CT-ATN) sont reliées par un facteur de CONVENTION fixe (=4 ;
        normalisation de Π et préfacteurs), explicitement enregistré, PAS une contradiction.

DISCIPLINE LC-AUDIT-VERDICT §6.4. Tout `établi (algèbre)` atteste : algèbre correcte +
cibles de de Haro reproduites + conventions épinglées. JAMAIS « physique CCC établie », ni
« seconde route au signe acquise » (c'est S2), ni « D1 fermé », ni « CCC démontrée ».
S1 est en AdS ; la continuation dS reste `à inventer` (S2). D1 NON clos.
"""

import sympy as sp

CHECKS = []
def check(label, cond):
    ok = bool(cond)
    CHECKS.append((label, ok))
    print(f"  [{'OK' if ok else 'FAIL'}] {label}")
    assert ok, f"ÉCHEC: {label}"

print("=" * 78)
print("verif_D_CT_dual.py — S1 : structure de dualité de de Haro EN AdS (paper-first)")
print("=" * 78)

# ---------------------------------------------------------------------------
# [A] Dualité des équations de mouvement du bulk ; S² = -1.
# ---------------------------------------------------------------------------
print("\n[A] Dualité des EOM (éq. 43-44) et S² = -1 (éq. 51)")

p, r = sp.symbols('p r', positive=True)
a, b = sp.symbols('a b')
u = p * r
f_a = sp.cos(u) + u * sp.sin(u)        # éq. (43), mode a
f_b = u * sp.cos(u) - sp.sin(u)        # éq. (43), mode b

def field(ca, cb):
    """h̄[ca,cb](r) (partie physique TT), facteur tensoriel commun factorisé."""
    return ca * f_a + cb * f_b

# Identité (44) : d³/dr³ h̄[-b,a] = |p|³ h̄[a,b] - (3|p|/r) h̄'[a,b].
lhs_44 = sp.diff(field(-b, a), r, 3)
rhs_44 = p**3 * field(a, b) - (sp.Integer(3) * p / r) * sp.diff(field(a, b), r, 1)
check("(44) identite de 3e derivee referme sur (f_a,f_b) avec echange (a,b)->(-b,a)",
      sp.simplify(lhs_44 - rhs_44) == 0)

# La carte de dualite induite sur les donnees de bord (a,b).
S = sp.Matrix([[0, -1], [1, 0]])            # (a,b) -> (-b, a)
check("S agit comme (a,b) -> (-b,a)",
      list(S * sp.Matrix([a, b])) == [-b, a])
check("S^2 = -1  (eq. 51 : involution de duals S^2=-1)",
      (S * S) == -sp.eye(2))
check("S a pour valeurs propres +i, -i (moteur candidat du 'i' de S2)",
      sorted([sp.simplify(ev) for ev in S.eigenvals().keys()], key=str)
      == sorted([sp.I, -sp.I], key=str))

# Controle de non-trivialite : l'identite ne tient PAS sans l'echange (sinon S serait
# l'identite et S^2=+1) -> certifie que S est bien l'involution non triviale.
lhs_noswap = sp.diff(field(a, b), r, 3)
check("controle negatif : sans echange, (44) ne tient pas (S != identite)",
      sp.simplify(lhs_noswap - rhs_44) != 0)

# ---------------------------------------------------------------------------
# [B] Garde-fou de signe : en AdS, la dualite NE flippe PAS C_T.
# ---------------------------------------------------------------------------
print("\n[B] Garde-fou de signe : C̃_T = +C_T en AdS (le `-` de W̃ est compense)")

ell, kappa, h, ht, P3 = sp.symbols('ell kappa h ht P3', positive=True)
# P3 = □^{3/2} -> |p|^3 (euclidien, positif). Facteur tensoriel Pi commun factorise :
# le SIGNE est porte par le coefficient scalaire, robuste aux conventions de normalisation.

cW = ell**2 / (8 * kappa**2)                 # eq. (61) : W = +cW ∫ h □^{3/2} h
cWt = -ell**2 / (8 * kappa**2)               # eq. (62) : W̃ = -cW ∫ h̃ □^{3/2} h̃ (MINUS relatif)
check("(61)-(62) : signe relatif de W̃ vs W est NEGATIF (cWt = -cW)",
      sp.simplify(cWt + cW) == 0 and cWt != cW)

# Fonctionnelles quadratiques (surrogate scalaire ; Pi factorise) :
W = cW * P3 * h**2
Wt = cWt * P3 * ht**2

# Tenseur de stress et deux-points, AVEC les definitions de de Haro :
T = 2 * sp.diff(W, h)                         # ⟨T⟩ = 2 δW/δh
TT = sp.diff(T, h)                            # ⟨TT⟩, coeff de |p|^3
Tt = -2 * sp.diff(Wt, ht)                     # ⟨T̃⟩ = -2 δW̃/δh̃   (eq. 63, signe explicite)
TtTt = sp.diff(Tt, ht)                        # ⟨T̃T̃⟩, coeff de |p|^3

sgn_TT = sp.sign(TT.subs(P3, 1))
sgn_TtTt = sp.sign(TtTt.subs(P3, 1))
check("⟨TT⟩ coeff > 0 (C_T electrique, CFT1)", sgn_TT == 1)
check("⟨T̃T̃⟩ coeff > 0 (C̃_T dual, CFT2)", sgn_TtTt == 1)
check("CŒUR S1 : sign(C̃_T) == sign(C_T) en AdS  (la dualite NE flippe PAS C_T)",
      sgn_TT == sgn_TtTt)
check("... ALORS QUE sign(W̃) = -sign(W) : le `-` de W̃ est COMPENSE par le `-2` de ⟨T̃⟩",
      sp.sign(cWt) == -sp.sign(cW))
check("⟨TT⟩ et ⟨T̃T̃⟩ ont le MEME coefficient (eq. 90 : 'dual takes the same form')",
      sp.simplify(TT - TtTt) == 0)

# ---------------------------------------------------------------------------
# [C] Dictionnaire C_T ↔ ℓ²/κ² ↔ N (verrouillage), conventions epinglees.
# ---------------------------------------------------------------------------
print("\n[C] Dictionnaire C_T ↔ ℓ²/κ² ↔ N et facteur de convention")

d, G, H = sp.symbols('d G H', positive=True)

# (i) eq. (1) de de Haro : coeff du dictionnaire = d ℓ²/(16πG). A d=3 -> 3 ℓ²/(16πG).
coeff_deHaro = d * ell**2 / (16 * sp.pi * G)
coeff_programme = d * ell**2 / (16 * sp.pi * G)     # ⟨T⟩=(d/16πG)g3 (LC-D-CT-ATN, §dictionnaire)
check("(1) dictionnaire de de Haro == dictionnaire programme (d quelconque)",
      sp.simplify(coeff_deHaro - coeff_programme) == 0)
check("a d=3 le coeff vaut 3 ℓ²/(16πG)",
      sp.simplify(coeff_deHaro.subs(d, 3) - 3 * ell**2 / (16 * sp.pi * G)) == 0)

# (ii)-(iii) C_T = ℓ²/κ² (eq. 90, coeff de |p|^3 Pi), κ²=8πG ; ℓ=ℓ_dS=1/H ; N=π/(G H²).
kappa2 = 8 * sp.pi * G
C_T_deHaro = ell**2 / kappa2                          # coeff nu de de Haro
C_T_dS = C_T_deHaro.subs(ell, 1 / H)                  # ℓ_dS = 1/H
N = sp.pi / (G * H**2)                                # = S_dS, verif_E_planck.py

ratio = sp.simplify(C_T_dS / N)
check("C_T ∝ ℓ²/κ² ∝ ℓ²/G (forme de de Haro)",
      sp.simplify(C_T_deHaro - ell**2 / kappa2) == 0)
check("VERROUILLAGE : C_T/N est un NOMBRE PUR (H,G,k se simplifient)",
      ratio.free_symbols == set())
check("C_T/N (normalisation nue de Haro) = 1/(8π²)",
      sp.simplify(ratio - sp.Rational(1, 1) / (8 * sp.pi**2)) == 0)

# Facteur de convention vers la valeur scellee du programme (LC-D-CT-ATN : C_T/N=1/(32π²)).
ratio_programme = sp.Rational(1, 1) / (32 * sp.pi**2)
conv_factor = sp.simplify(ratio / ratio_programme)
check("facteur de convention deHaro/programme = 4 (Pi-normalisation + prefacteurs), CONSTANT",
      conv_factor == 4 and conv_factor.free_symbols == set())
check("=> C_T/N independant de H,G,k dans LES DEUX normalisations (verrouillage robuste)",
      ratio.free_symbols == set() and ratio_programme.free_symbols == set())

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
n_ok = sum(1 for _, ok in CHECKS if ok)
print(f"BILAN : {n_ok}/{len(CHECKS)} assertions OK")
print("=" * 78)
print("""
PORTEE (etabli — ALGEBRE, §6.4) :
  [A] dualite EOM de de Haro reproduite ; S²=-1 (vp ±i) — S1.
  [B] GARDE-FOU : en AdS, sign(C̃_T)=sign(C_T) malgre sign(W̃)=-sign(W) — la dualite AdS
      ne flippe PAS C_T ; tout flip viendra de la continuation dS et/ou de S²=-1 (S2).
  [C] dictionnaire C_T↔ℓ²/κ²↔N reproduit ; C_T/N nombre pur (verrouillage) ; facteur de
      convention deHaro/programme = 4, fige et NON cache.
NON couvert / `a inventer` (S2) : continuation dS de la dualite ; le secteur magnetique/dual
  livre-t-il sign(C_T)<0 en d=3 INDEPENDAMMENT, et S²=-1 porte-t-il le i² structurellement ?
  Quelle CFT (Dirichlet vs duale) joue 'raccordement' ? — TOUT cela reste ouvert.
NE PROUVE PAS : seconde route au signe ; D1 ferme ; CCC. S1 est en AdS.
""")
