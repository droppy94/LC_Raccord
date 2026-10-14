---
id: NOTE-BORD-EON-130-ARMEMENT-IR-t
numero: 130
serie: I
branche: Q-M3 suite (IR-t)
reservation: 2026-10-12T12:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 130)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-12 14:13 heure de Paris (piste 2)
depend: [NOTE-BORD-EON-125-IR-r-EXECUTION (v2), NOTE-BORD-EON-128-AUDIT-IR-s-CONCORDANCE, NOTE-BORD-EON-129-ACTE-GREFFE-IR-s]
sources: ["aucune nouvelle ; decomposition W_eff[ĝ] = Γ[g] + WZ[σ ; g] (action de Wess-Zumino de l'anomalie de trace, forme integrable donnee par l'audit S-b) ; formules standard controlees par le calcul"]
issue_attendue: "delimitation"
rouvre_si:
  - "etat quantique du repere plat non regulier en τ = 0, ou noyau retarde non convergent (passe non adiabatique)"
  - "ordres superieurs en ε et en bκ ; validite de l'action effective a une boucle comme source semi-classique"
---

# NOTE-130 : armement de IR-t. Le pole G-V3 est-il compense ?

## 0. Origine
Le pole |8bκ| W_E/Ω de G-V3 (NOTE-125 v2, audite par NOTE-128) vient du terme bσC² de l'action de Wess-Zumino, avec σ = −ln s.
- L'audit S-b a montre, hors verdict, que la partie a (Euler) ne contribue pas a R a l'ordre ε. Ce resultat est a **acter** par une execution independante.
- Deux sources possibles de compensation restent ouvertes :
  - la partie non locale Γ[g] de l'action effective, evaluee sur la reference g = η + εh dans l'etat correspondant ;
  - les modes homogenes de l'equation auxiliaire pour φ.

## 1. Cadre (fige)
- ĝ = s⁻²(η + εh), mode tensoriel de de Sitter h_yy = −h_zz = u(s) cos kx (NOTE-124 §1). Premier ordre en ε.
- Decomposition exacte de l'action effective a une boucle des champs conformes : W_eff[ĝ] = Γ[g] + WZ[σ ; g], σ = −ln s, avec WZ = ∫√g { bσC² + a[σ(E − ⅔□R) + 2σΔ₄σ] } (forme integrable). Tenseur physique T̂ = s² T[g] pour chaque morceau.
- Equation testee : second membre de (2.17), comme en NOTE-124.
- **t-1, partie a** : variation brute de ∫√g [σ(E − ⅔□R) + 2σΔ₄σ] sur la famille g = diag(−1, 1, 1 + εP, 1 + εQ)(s, x), puis evaluation sur P = −Q = u cos kx. Par la symetrie d'helicite autour de k, seule T̂_yy − T̂_zz (et T̂_yz) peut etre non nulle et non proportionnelle a ĝ a l'ordre ε. Test : δT̂_yy = 6a δĝ_yy ? Controle du fond : T̂ = 6a ĝ (trace 24a).
- **t-2, partie non locale** : Γ[g] est une fonctionnelle des seules quantites du repere plat (aucun σ). Dans l'etat conforme (vide de Minkowski du repere plat, prepare adiabatiquement dans le passe), son tenseur T_Γ est un noyau retarde invariant par translation applique a une histoire lisse sur ]−∞, τ] ; τ = 0 n'y est pas un point distingue. Test calcule : pour T̂ = s² Y(s, x) avec Y lisse (developpement en serie generique, de la forme du mode tensoriel), R n'a pas de pole. Argument [derive] sur la regularite de T_Γ en τ = 0.
- **t-3, modes homogenes de φ** : toute solution de l'equation auxiliaire s'ecrit −ln s + φ_h, avec √g Δ₄ φ_h = 0, soit □_η² φ_h = 0 dans le repere plat. Tests calcules : □_η²(ln s) ≠ 0, de sorte que le log n'est pas un mode homogene ; pour φ_h lisse, le terme b∂∂(φ_h C) donne T̂ = s² × lisse, sans pole.

## 2. Sous-questions
- **t-1** : la partie a d'ordre ε est-elle proportionnelle a ĝ (donc sans effet sur R) ?
- **t-2** : la partie non locale peut-elle produire un T̂ en Ω¹ (ordre necessaire pour un pole) ?
- **t-3** : un mode homogene peut-il annuler la singularite logarithmique de φ, ou produire un pole compensateur ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **T-V1** | Aucune des trois contributions ne compense le pole : G-V3 est robuste dans la classe « WZ integrable + Γ[g] dans un etat conforme regulier + φ_h lisse ». |
| **T-V2** | Une contribution compense le pole (a nommer) : G-V3 tombe ou change de forme. |
| **T-V3** | Indecidable dans le cadre : la conclusion depend de l'etat, de la prescription (in-in, adiabaticite) ou de termes non controles. |
| **T-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**T-V1 qualifie T-V3.**
- t-1 : la partie a se reduit a 6a ĝ a l'ordre ε, comme S-b l'a trouve.
- t-2 : T̂_Γ est en s² × (tenseur lisse) ; R est regulier, sans pole.
- t-3 : le log de φ est force par la source F₄ ; un φ_h lisse ne donne pas de pole.
- Qualification : la regularite de l'etat du repere plat en τ = 0 et la convergence du noyau retarde (passe adiabatique) sont des **hypotheses**, non des resultats ; l'usage de l'action effective a une boucle comme source semi-classique dans (2.17) est une hypothese de tout le canal.

## 5. Instruments prevus
Scripts `irt_a.py` (t-1), `irt_gamma_phi.py` (t-2, t-3), sympy, empreintes avant execution.

## 6. Non-surclassement
[conv]. T-V1 consoliderait G-V3 comme candidat, sans le graver (audit et lecture exterieure requis). RG-4 inchangee ; noyau {A4 ; A2★ ; N} inchange.
