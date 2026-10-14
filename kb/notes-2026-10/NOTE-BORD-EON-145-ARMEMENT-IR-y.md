---
id: NOTE-BORD-EON-145-ARMEMENT-IR-y
numero: 145
serie: I
branche: Q-M3 suite (IR-y)
reservation: 2026-10-12T15:08 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 145)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, sous-questions, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-12 17:02 heure de Paris (« execute les 3 en sequence », piste 2) ; confirmation 17:04
depend: [NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-140-IR-x-EXECUTION (v2), NOTE-BORD-EON-142-AUDIT-IR-x-CONCORDANCE, NOTE-BORD-EON-144-ACTE-REVISION-LIBELLE-G-V3]
issue_attendue: "delimitation"
rouvre_si:
  - "audit froid de NOTE-146"
  - "etat non quasi-libre dont la fonction a deux points n'est pas Hadamard au sens microlocal"
  - "lecture des sources citees de memoire (§1, EX-8) contredisant un enonce utilise"
---

# NOTE-145 : armement de IR-y. Un etat Hadamard non regulier en 𝓘⁺ peut-il rendre Γ[g] singuliere et compenser le pole G-V3 ?

## 0. Origine
NOTE-131 (t-2) : la partie non locale Γ[g] de l'action effective donne un T̂ = s² × (tenseur lisse du repere plat) **si l'etat est regulier en τ = 0** ; alors pas de pole. NOTE-140 v2 et NOTE-142 ont leve l'hypothese pour le secteur φ_h ; NOTE-144 a porte la classe « WZ integrable + Γ[g] etat regulier » au libelle. La **regularite de l'etat en 𝓘⁺** est la seule hypothese d'etat restante de G-V3. Question : existe-t-il des etats **Hadamard** (admissibles) mais **non reguliers en 𝓘⁺** dont le tenseur T̂_Γ soit d'ordre s¹ avec valeur non nulle en s = 0, et compense donc le pole ?

## 1. Cadre (fige)
- Champ conforme (scalaire conforme comme representant ; la conclusion est attendue identique pour Dirac et Maxwell, qui partagent la structure conforme) sur le fond ĝ = s⁻²(η + εh), repere plat g = η + εh, s = Ω, s > 0, 𝓘⁺ = {s = 0}. Dans le repere plat, 𝓘⁺ est l'hyperplan η = 0 de Minkowski (η = −s), et le demi-espace η < 0 est le domaine de l'eon.
- **Decomposition exacte** (NOTE-131) : W_eff[ĝ] = Γ[g] + WZ[σ ; g]. Les parties a, b, c de WZ sont instruites (125 v2, 131, 118 v2). Ici seule Γ[g] est en jeu, et seulement par sa dependance a l'etat.
- **Comptage** (NOTE-131 t-2) : T̂ ~ s^p Y, Y lisse, donne R ~ s^(p−2) ; pole si et seulement si p = 1 et Y(0) ≠ 0. Avec T̂ = s² T_plat, un pole exige **T_plat ~ 1/s** en s → 0, c'est-a-dire un tenseur du repere plat divergent en η = 0.
- **Etat** : quasi-libre (gaussien) ; fonction a deux points ω₂ = H + w, H parametrix de Hadamard (independante de l'etat), w bisolution lisse sur le domaine. Tenseur renormalise : T_plat = (partie independante de l'etat, locale, deja comptee dans WZ et dans la dependance en μ) + T^w, T^w construit a partir des limites de coincidence de ∂∂w. **Admissibilite** = Hadamard sur tout le domaine η < 0 (s > 0), au sens microlocal : WF(ω₂) ⊂ C⁺ [Radzikowski 1996, cite de memoire, non relu ; EX-8].
- **Regularite en 𝓘⁺** (definition fixee ici) : w se prolonge en fonction lisse a travers η = 0, et donc T^w est lisse en η = 0.
- Enonces exterieurs mobilises, **cites de memoire, non relus** (taux EX-8) : (E1) la condition de Hadamard se propage : un etat Hadamard au voisinage d'une surface de Cauchy l'est sur tout le domaine de dependance [Fulling, Narcowich, Wald 1981] ; (E2) caracterisation microlocale et equivalence avec la forme locale [Radzikowski 1996] ; (E3) pour un champ conforme, la condition de Hadamard est conformement invariante, et le tenseur se transporte par la formule de Brown-Cassidy avec un terme anomal local (le meme que WZ) ; (E4) propagation des singularites pour □ (operateur de type principal reel) [Hormander]. Tout enonce de §4 qui en depend est [derive].
- Premier ordre en ε (onde h = u(s) cos kx, u entier en s), fond de Sitter exact, une boucle.

## 2. Sous-questions
- **y-1 (classe homogene explicite)** : pour un etat gaussien homogene de Bogoliubov (coefficients α_k, β_k), calculer la partie dependante de l'etat de w(x, x) et de T^w sur le repere plat, et leur comportement en η → 0⁻ selon la decroissance de α_k β_k* : (a) decroissance plus rapide que toute puissance (Schwartz) ; (b) decroissance en loi de puissance k^(−N). Pour quel N obtient-on T_plat ~ 1/η (donc T̂ ~ s¹, pole) ?
- **y-2 (admissibilite dans la classe homogene)** : les etats du cas (b) sont-ils Hadamard sur η < 0 ? Calculer le support singulier du terme α β* de w(x, x′) ; prediction : singularite sur le « cone reflechi » (η + η′)² = |x − x′|², qui rencontre le domaine η, η′ < 0, donc etat **non** Hadamard pour toute decroissance polynomiale ; Hadamard si et seulement si α β* est a decroissance rapide, auquel cas w est lisse a travers η = 0.
- **y-3 (classe generale)** : argument de prolongement : un etat Hadamard sur η < 0 l'est au voisinage de la surface de Cauchy η = −ε de Minkowski ; par (E1) son prolongement (resolution du probleme de Cauchy pour la bisolution) est Hadamard sur tout Minkowski, donc w est lisse a travers η = 0 ; alternativement, par (E4), une singularite de w portee par η = 0 se propagerait le long de bicaracteristiques nulles dans η < 0, contredisant la lissite sur le domaine. Conclusion attendue : **Hadamard ⟹ regulier en 𝓘⁺** pour les champs conformes dans le repere plat.
- **y-4 (reponse d'ordre ε)** : le tenseur d'ordre ε de Γ[g] dans un etat Hadamard general = noyau retarde de Minkowski (lisse hors coincidence, singularite [θ(T)/T]₊ integrable) applique a h entier en s, plus termes en w lisses : lisse en η = 0 ; T̂ ~ s² ; pas de pole. Verifier le comptage sur le cas homogene de y-1 (b) : quel N donne un pole, et ce N est-il non Hadamard d'apres y-2 ?
- **y-5 (parallele avec IR-x)** : l'etat qui compenserait le pole (y-1 (b), N critique) est-il, comme les solutions de cone de NOTE-140, singulier sur une hypersurface nulle du volume ? Lire le resultat comme : la compensation exige la meme pathologie dans le secteur Γ[g] que dans le secteur φ_h.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **Y-V1** | Pour un champ conforme, tout etat Hadamard sur l'eon est regulier en 𝓘⁺ dans le repere plat (w lisse a travers η = 0) ; T̂_Γ ~ s² × lisse ; aucun etat admissible ne compense le pole. Les seuls etats qui le compenseraient (T_plat ~ 1/η) sont non Hadamard, singuliers sur une hypersurface nulle du volume. **L'hypothese d'etat de NOTE-131 est levee** : la classe de G-V3 devient « WZ integrable + Γ[g] dans un etat Hadamard ». |
| **Y-V2** | Comme Y-V1 dans la classe homogene, mais l'argument general (y-3) repose sur un enonce exterieur non verifie ; hypothese d'etat levee **sous reserve de lecture** des sources (E1)-(E4). |
| **Y-V3** | Il existe des etats Hadamard non reguliers en 𝓘⁺ (w non lisse en η = 0) mais aucun ne produit T_plat ~ 1/η ; pas de pole, hypothese levee par un autre chemin. |
| **Y-V4** | Une famille Hadamard compense le pole sur un ouvert de 𝓘⁺ : G-V3 compromis. |
| **Y-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**Y-V1 qualifie Y-V2.**
- y-1 : partie d'etat de w(x, x) ∝ ∫ dk k Re(α β* e^(−2ikη)) + const ; T^w ∝ ∫ dk k³ Re(α β* e^(−2ikη)) ; cas (a) : entier en η, lisse a travers 0 ; cas (b) : comportement |η|^(N−4) (log si N = 4) ; **N = 3** donne T_plat ~ 1/η, donc T̂ ~ s¹ : c'est le seul exposant qui compenserait le pole.
- y-2 : le terme α β* de w(x, x′) est la fonction a deux points de Minkowski entre x et le point reflechi (−η′, x′), convoluee par la transformee de α β* ; support singulier sur (η + η′)² = |x − x′|², qui rencontre η, η′ < 0 ; non Hadamard pour toute decroissance polynomiale ; Hadamard ssi decroissance rapide, et alors w est entiere en η.
- y-3 : Hadamard ⟹ regulier en 𝓘⁺, **[derive]** via (E1) ou (E4), cites de memoire ; d'ou la qualification Y-V2.
- y-4 : T̂_Γ ~ s² dans tout etat Hadamard ; N = 3 est non Hadamard.
- y-5 : oui, meme pathologie (singularite sur une hypersurface nulle du volume), parallele exact avec NOTE-140.
- Consequence : classe de G-V3 « WZ integrable + Γ[g] dans un etat Hadamard » ; les hypotheses restantes ne sont plus des hypotheses d'etat mais de cadre (une boucle, premier ordre, resommation).

## 5. Instruments prevus
Script `iry_state.py` (sympy et mpmath), empreinte avant execution : y-1 (integrales de Fourier avec decroissance gaussienne et en loi de puissance, exposant critique), y-2 (forme fermee du terme α β* pour α β* = 1 et pour k^(−N), support singulier), y-4 (comptage T̂ = s² T_plat, pole ssi N = 3). Aucune lecture de source.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v2) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Les enonces (E1)-(E4) sont cites de memoire : tout resultat qui en depend reste [derive] et conditionne la qualification Y-V2.
