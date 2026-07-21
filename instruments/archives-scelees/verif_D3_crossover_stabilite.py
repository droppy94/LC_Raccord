#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_crossover_stabilite.py — LC-RACCORD, front (a) du raccord, étape (a3).
(Compagnon de LC-D3-CROSSOVER-STABILITE. Étend verif_D1_atlas.py et verif_D3_backreaction.py.)

QUESTION (a3). (a1) : la carte de crossover est homogène, ǧ₃ = M·ĝ₃, point fixe à 0 ;
le facteur M dépend du fond via c₁. (a2) : la back-réaction des fluctuations BD est
isotrope -> elle renormalise le fond (m,λ) = source de l'itération inter-éons de l'atlas.
Donc : le point fixe de marée g₃=0 est-il STABLE sous cette itération, ou le runaway
(m,λ) (LC-A-D1 §4-bis) amplifie-t-il la marée ?

MÉCANISME. La marée g₃=0 (1-point) est préservée (a1,a2). La question de (a3) est la
stabilité de l'AMPLITUDE de fluctuation (2-points ⟨g₃g₃⟩~k³, irréductible) à travers les
éons. L'amplitude physique de marée (spectre tensoriel de l'éon) scale comme le Hubble du
secteur Λ-dominé : P_T ∝ H² = λ/3, donc P_T ∝ λ. Or la récurrence de l'atlas
(classe Penrose-cohérente) CONSERVE le produit P = mλ et fait courir λ géométriquement de
raison r = P/P*, P* = 9k²/4. Conséquence :
   P > P*  ->  λ→∞  ->  marée P_T→∞     (Weyl explose : WCH violée)
   P < P*  ->  λ→0  ->  marée P_T→0      (sur-suppression)
   P = P*  ->  λ const ->  marée stable   (bornée, non nulle)
Donc EXIGER une marée gravitationnelle bornée à chaque Big Bang (= l'hypothèse de Weyl de
Penrose, D3) SÉLECTIONNE P = P* = 9k²/4 — exactement le point fixe du candidat #5
(stabilité inter-éons). D3/WCH et #5 COÏNCIDENT. Mais P étant conservé, ce n'est pas un
attracteur dynamique : c'est une SÉLECTION (le fine-tuning subsiste, désormais unifié et
physiquement motivé). Reste ouvert : la back-réaction (a2) peut-elle DRIVER P vers P* ?

Sceaux :
  [1] récurrence de l'atlas : produit P=mλ CONSERVÉ.
  [2] sur une level-set P : λ' = (P/P*) λ, P* = 9k²/4 (level-set critique = ligne de pts fixes).
  [3] point fixe NON-HYPERBOLIQUE : Jacobien -> vp 1 double, défective (Jordan) ->
      drift séculaire (reconnecte candidat #5, LC-A-D1-STABILITE-WEYL).
  [4] marée P_T ∝ λ : trois branches (explose / s'éteint / stable) selon P vs P*.
  [5] sélection : marée bornée (WCH) <=> P <= P* ; stable & non nulle <=> P = P*  = #5.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs (cf. LC-04) : Markwell–Stevens GRG 55, 93 (2023) — atlas/récurrence ; Penrose,
Cycles of Time (2010) — WCH ; Bunch–Davies (1978) ; (tensor spectrum P_T ∝ H² : standard).
"""

import sympy as sp

print("="*74)
print(" verif_D3_crossover_stabilite.py — (a3) stabilité de g₃=0 sous l'itération atlas")
print("="*74)

m, lam, k = sp.symbols('m lambda k', positive=True)

# ======================================================================
# [1] Récurrence de l'atlas (classe Penrose-cohérente, LC-A-D1 §4-bis) :
#     m' = 9k²/(4λ),  λ' = 4λ²m/(9k²).  Produit P=mλ conservé ?
# ======================================================================
print("\n[1] Récurrence Penrose-cohérente : m' = 9k²/4λ , λ' = 4λ²m/9k²")
m_n = 9*k**2/(4*lam)
lam_n = 4*lam**2*m/(9*k**2)
P  = sp.simplify(m*lam)
Pn = sp.simplify(m_n*lam_n)
print("    P = mλ =", P, "   ;   P' = m'λ' =", Pn)
print("    P' - P =", sp.simplify(Pn - P), " -> produit CONSERVÉ.")
assert sp.simplify(Pn - P) == 0

# ======================================================================
# [2] Sur une level-set P=const : λ' = (P/P*) λ, P* = 9k²/4.
# ======================================================================
print("\n[2] Réduction sur la level-set P=mλ : λ' en fonction de λ")
Pc = sp.symbols('P', positive=True)               # produit conservé
lam_n_levelset = sp.simplify(lam_n.subs(m, Pc/lam))   # m = P/λ
print("    λ' = 4λ²·(P/λ)/9k² =", lam_n_levelset, " = (4P/9k²)·λ")
Pstar = sp.Rational(9,4)*k**2
r = sp.simplify(lam_n_levelset/lam)
print("    raison r = λ'/λ =", r, " = P/P* avec P* = 9k²/4 =", Pstar)
assert sp.simplify(r - Pc/Pstar) == 0
print("    -> P=P* : r=1 (ligne de points fixes) ; P>P* : λ→∞ ; P<P* : λ→0.")

# ======================================================================
# [3] Point fixe NON-HYPERBOLIQUE : Jacobien du map 2D, valeurs propres.
# ======================================================================
print("\n[3] Stabilité linéaire au point fixe (mλ=9k²/4) : Jacobien")
F = sp.Matrix([m_n, lam_n])
J = F.jacobian(sp.Matrix([m, lam]))
J_fp = sp.simplify(J.subs(m, Pstar/lam))           # au point fixe m = 9k²/4λ
print("    J|_fp =")
sp.pprint(J_fp)
ev = J_fp.eigenvals()
print("    valeurs propres :", ev, "  (det =", sp.simplify(J_fp.det()),
      ", trace =", sp.simplify(J_fp.trace()), ")")
assert sp.simplify(J_fp.det()) == 1 and sp.simplify(J_fp.trace()) == 2
assert ev == {sp.Integer(1): 2}
# défective ? rang(J-I) = 1 => un seul vecteur propre => bloc de Jordan
defect = (J_fp - sp.eye(2))
print("    rang(J-I) =", defect.rank(), "-> vp 1 DOUBLE + DÉFECTIVE (Jordan) : drift séculaire.")
assert defect.rank() == 1
print("    (cohérent avec candidat #5 : carte non-hyperbolique, vp 1 double — LC-A-D1-STABILITE-WEYL)")

# ======================================================================
# [4] Marée : amplitude (spectre tensoriel) P_T ∝ λ. Trois branches.
# ======================================================================
print("\n[4] Amplitude de marée P_T ∝ H² = λ/3 (spectre tensoriel de l'éon Λ-dominé) :")
import math
def iterate(P0, lam0, n):
    rr = P0/2.25                      # k=1 -> P*=2.25
    return [(i, lam0*rr**i, lam0*rr**i/3.0) for i in range(n+1)]   # (éon, λ_i, P_T∝λ/3)

print("    (k=1, P*=2.25 ; on suit λ_i et P_T_i ∝ λ_i sur 6 éons)")
for label, P0, lam0 in [("P>P* (runaway up)", 2.40, 1.5),
                        ("P=P*  (steady)   ", 2.25, 1.5),
                        ("P<P* (suppression)",2.00, 1.5)]:
    seq = iterate(P0, lam0, 6)
    lams = ", ".join(f"{l:.3f}" for _, l, _ in seq)
    print(f"    {label} : λ = [{lams}]")
print("    -> P>P* : λ (donc P_T) EXPLOSE (Weyl non borné : WCH violée).")
print("       P<P* : λ→0 (marée sur-supprimée).   P=P* : λ const (marée bornée, stable).")
# vérif : r=2.40/2.25 -> m décroît de 1/r = 0.9375/éon (cohérent atlas §4-bis)
print("    [check atlas] P=2.40 -> r=", round(2.40/2.25,4),
      "; m décroît de 1/r =", round(2.25/2.40,4), "/éon (=0.9375, sceau verif_D1_atlas).")
assert abs(2.25/2.40 - 0.9375) < 1e-9

# ======================================================================
# [5] Sélection : WCH (marée bornée) <=> P<=P* ; stable & non nulle <=> P=P* = #5.
# ======================================================================
print("\n" + "-"*74)
print(" VERDICT (a3) :")
print("   [1] le produit P=mλ est CONSERVÉ par la récurrence de l'atlas.")
print("   [2] λ court géométriquement de raison r=P/P*, P*=9k²/4 (ligne de pts fixes en P*).")
print("   [3] le point fixe est NON-HYPERBOLIQUE (vp 1 double, défective) = candidat #5.")
print("   [4] la marée scale P_T ∝ λ : runaway en λ <=> explosion de la marée (Weyl).")
print("   ==> EXIGER une marée gravitationnelle BORNÉE à chaque Big Bang (= WCH / D3)")
print("       EXCLUT la branche P>P* et SÉLECTIONNE P = P* = 9k²/4 = le point fixe #5.")
print("       >>> D3/WCH (★, marée) et candidat #5 (stabilité, fond) COÏNCIDENT.")
print("           La sous-détermination de D1 est levée SOUS WCH : un seul énoncé")
print("           (« faible Weyl = marée bornée = stabilité ») ferme les deux.")
print(" PORTÉE HONNÊTE (pas de surclassement) :")
print("   - SÉLECTION, pas attracteur : P étant conservé, rien ne DRIVE vers P* si on")
print("     démarre ailleurs -> le fine-tuning m̂λ̂=9k²/4 SUBSISTE (mais désormais unifié).")
print("   - question dynamique OUVERTE : la back-réaction (a2), qui renormalise λ (~H⁴~λ²),")
print("     peut-elle DRIVER P vers P* (attracteur dynamique) ? -> nécessite la coupure")
print("     holographique N (LC-E) ; statut : à inventer / hors de portée.")
print("   - FLRW : level-set exacte ; cas inhomogène (Bianchi A) non couvert.")
print("-"*74)
