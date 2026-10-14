---
id: RAPPORT-CSE-CHAMP-COHERENT-AUDIT-AVEUGLE
date: 2026-10-10
objet: rapports des sous-agents C-a et C-b (audit froid aveugle de NOTE-98 / cb_coherent_v3), substance reproduite fidelement
gel: NOTE-BORD-EON-99-ARMEMENT-AUDIT-CHAMP-COHERENT (2026-10-10T12:18:57Z)
---

# Rapport C-a (re-derivation independante, cecite stricte)
Scripts : /home/claude/audit_ca/audit.py (7bd4a4e2…), audit_output.txt (5a01e059…). Aucun fichier existant lu.

1. Equation de jauge : satisfaite (seul F^{xy} constant non nul, I² ne depend que de s, F^{sν} = 0).
2. F̂² = 2B₀²s⁴ ; **X^M = (I²B₀²s²/2) diag(1,1,1,−1) = (B₀²s²/e²)(½ − β ln s) diag(1,1,1,−1)** ; trace 0 ; divergence ∇̂^μX^M_{μs} = βB₀²s³/e², coincide avec −¼(∂_ν I²)F̂².
3. Trace anomale : √|ĝ| ĝ^{μν}T̂_{μν} = δS_B/δσ = −βB₀²/e² ; **ĝ^{μν}T̂_{μν} = −βB₀²s⁴/e²**, negative pour un champ magnetique ; S_flat ne contribue pas.
4. X^R isotrope : r0 = C1 s², r1 = C1 s²/3 − βB₀²s²/(3e²) ; conservation et trace verifiees ; C1 (radiation libre) sans effet sur R.
5. R : composantes non nulles (i,s,i) : R_xsx = R_ysy = κB₀²/e² (½ − β/3 − β ln s), R_zsz = κB₀²/e² (−1 + 2β/3 + 2β ln s). Aucune puissance negative ; **ln Ω present, −βκB₀²/e² (x, y), +2βκB₀²/e² (z)**. Motif purement anisotrope (1,1,−2). Le secteur R seul donne +β/6 isotrope, qui annule la partie isotrope en β du secteur Maxwell. β = 0 : constant, sans log.
6. Π diag(0,1,1,−2) conserve pour tout Π(s) ; R_xsx[Π] = κ(sΠ)'/(2s²). Regularite ⟺ **Π = (2βB₀²/(3e²)) s² ln s + c/s + Σ_{k≥2} p_k s^k** (c/s invisible). Partie anisotrope de X^M : Π_M = (B₀²s²/(3e²))(1 − 2β ln s) : le Π requis compense exactement la partie logarithmique de Π_M.
7. Completion σ → Σ[g] : (a) Σ × Maxwell (anisotrope, porte le ln) ; (b) ∫ J(y) δΣ(y)/δg^{μν}(x) avec J = √g F² = 2B₀² constant : le champ n'entre que par un scalaire invariant par rotation ; noyau covariant sous les isometries ; resultat invariant E(3) : **isotrope**, ne peut produire le Π requis ; (b) coincide avec X^R au terme C1 pres. Hypotheses : Σ fonctionnelle scalaire covariante de la seule metrique ; conditions aux limites / etat de la partie non locale respectant FLRW ; champ entrant par F² seulement ; convergence ou regularisation infrarouge isotrope ; fond fixe ; Σ → Σ + σ sous Weyl. Mise en defaut possible par : facteur de forme agissant sur F (F ln(□) F de Barvinsky-Vilkovisky), couplages F-courbure, conditions aux limites ou regulateur anisotropes, champ non uniforme, retroaction.

# Rapport C-b (audit du code v3 et de l'argument B)
Empreinte verifiee ; EXIT 0. Consultation externe : arXiv:1808.08237 (eq. 2.11 a 2.16, 3.12-3.13).

| Point | Verdict |
|---|---|
| A1 Christoffels, ∇, div, trace | OK |
| A2 equation de jauge | OK |
| A3 secteur Maxwell, I² = 1 + 2β ln a | OK |
| A4 trace anomale | OK sur le fond ; **DEFAUT : le « controle independant » est tautologique** (meme formule reecrite) ; remplace par ctrl1, variation metrique explicite d'une completion locale, concordant pour tout facteur conforme FLRW |
| A5 fermeture isotrope | OK ; C-iso est le cas isotrope **general** (toute partie isotrope homogene conservee de trace fixee a cette forme) |
| A6 R | OK ; balayage complet, seules (i,0,i) non nulles ; s = −τ change les signes des composantes a un indice 0 (confirme en τ), sans effet |
| A7 termes non lisses, Π | OK sur le fond ; ansatz incomplet (c/s, ln², …) ; ctrl2 (s^k L^j, k = −3..4, j = 0..3, solution generale) : le terme s²L de Π vaut necessairement 2B₀²β/(3e²) = −Π_M ; code mort l. 143-150 |
| A8 execution | OK ; termes en ln reproduits independamment ; β = 0 lisse |

Reserves : (1) champ strictement uniforme et a⋆ = 1 : BDK choisissent a⋆ = k/M par mode ; a k = 0 le terme log(−∂²) de S_flat diverge dans l'infrarouge ; si l'echelle infrarouge est comobile, le coefficient de ln a ne change pas ; **si elle est physique (par ex. H), log(−∂² e^{−2Ω}/M²) → log(H²/M²) et le ln a total s'annule exactement**. (2) Budget restreint au cas diagonal homogene axisymetrique (T_{0z} exclu par parite, a dire).

Argument (B) : **valide sous hypotheses nommees**. Correct : Ω[g] covariant, fond et definition E(3)-invariants ⟹ partie (b) isotrope. Hypotheses : H1 Ω ne depend que de la metrique (contre-exemple au lemme : completion d'Euler-Heisenberg Ω_F = −¼ ln(F·F/M⁴), qui se decale de +σ sous Weyl et vaut ln a + cte sur le fond ; avec elle, trace et conservation exactes, secteur non Maxwell −(β/2e²)F_{μα}F_ν^α **anisotrope** a coefficient constant, Π = −βB₀²s²/(6e²) ; « secteur non Maxwell isotrope » faux hors H1, mais **le terme logarithmique de R reste identique**) ; H2 etat/conditions aux limites E(3)-invariants pour G₄ = Δ₄⁻¹ (ctrl3 : Δ₄(−ln s) = F₄/4 en dS, √g Δ₄ = □_η² ; modes nuls anisotropes x² − z², s·x… a exclure en imposant Ω = −ln s exactement ; modes homogenes 1, s, s², s³ inoffensifs) ; H3 causalite in-in (noyau retarde ; integrale sur le cone passe divergente dans l'infrarouge, tranche initiale s0 requise ; isotropie preservee) ; H4 homogeneite (√g F² constant, pas F²) ; **H5 role de S_flat, decisive et non nommee** : toute completion = S_B[Ω_metrique] + W (W Weyl-invariant) ; evalue dans un repere conforme stationnaire (vide conforme, champs sans masse, F uniforme, a⋆ constant), W n'apporte aucun log et la compensation est impossible ; faille reelle : le terme −β̃ F log(−∂²/M²) F de S_flat, mal defini a k = 0, qui regularise par une echelle physique produit un ln a anisotrope oppose annulant celui du secteur Maxwell ; masse des fermions et etat non conforme sont d'autres breches.

Conclusion C-b : le coefficient de ln a est robuste dans la classe « a⋆ constant » ; point ouvert : l'echelle infrarouge de S_flat pour un champ uniforme (comobile ou physique).

Scripts : ctrl1_independant.py (33f10ebe…), ctrl2_ansatz_Pi.py (494503c0…), ctrl3_riegert_dS.py (5cd20c99…).
