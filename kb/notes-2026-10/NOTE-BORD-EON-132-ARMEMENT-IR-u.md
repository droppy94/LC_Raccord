---
id: NOTE-BORD-EON-132-ARMEMENT-IR-u
numero: 132
serie: I
branche: Q-M3 suite (IR-u)
reservation: 2026-10-12T12:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 132)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, recherche bibliographique, espace des verdicts et prediction figes AVANT tout calcul et toute lecture)
decision: operateur (Thierry), 2026-10-12 14:13 heure de Paris (piste 3)
depend: [NOTE-BORD-EON-125-IR-r-EXECUTION (v2), NOTE-BORD-EON-131-IR-t-EXECUTION]
issue_attendue: "delimitation"
rouvre_si:
  - "modes parasites (ordre superieur) de l'equation completee non elimines par la reduction d'ordre"
  - "litterature donnant un resultat contraire sur l'evolution des modes tensoriels en presence du terme de charge de Weyl"
---

# NOTE-132 : armement de IR-u. Que fait le pole au Weyl rescale ? Dimension anormale

## 0. Origine
NOTE-125 v2 : la source polaire de (2.17) fait diverger W en ln Ω au premier ordre en bκ. La forme resommee W ∝ Ω^γ et le coefficient γ sont conjecturaux. Il faut :
- (i) calculer γ directement, sur l'equation d'Einstein linearisee completee par le tenseur du terme bσC², plutot que par le seul raisonnement sur l'equation de Bianchi ;
- (ii) confronter a la litterature sur les perturbations tensorielles en presence de l'anomalie de trace.

## 1. Cadre (fige)
- ĝ = s⁻²(η + εh), h_yy = −h_zz = u(s) cos kx, Λ = 3 (H = 1). Equation : (G_ab + Λĝ_ab)[ĝ] = κ T̂_ab, a l'ordre ε, avec T̂ = T̂^(C)[h] du terme bσC², σ = −ln s. Convention du gel NOTE-124 : T_ab = (2/√g)δS/δg^{ab}, d'ou T_ab = +8b ∂^c∂^d(σ C_acbd) (NOTE-128). Le resultat pour l'autre convention s'obtient par b → −b.
- Les autres morceaux de l'action anomale n'ajoutent, a l'ordre ε, qu'une constante cosmologique effective 6aĝ (NOTE-131), absorbee dans Λ.
- **Reduction d'ordre** (traitement standard d'une correction d'ordre superieur en derivees) : u = u₀ + bκ u₁, avec u₀ le mode du vide (donnees A, B) et L[u₁] = T̂_yy[u₀]/b, ou L est l'operateur lineaire du membre de gauche. On ecarte les modes parasites de l'equation d'ordre quatre.
- Grandeurs a extraire :
  - u₁ pres de s = 0, en particulier les termes en s^n ln s ;
  - la partie electrique du Weyl rescale W_E = C_sisj[g]/s pour u₀ + bκu₁, sous la forme W_E ≈ W₀(1 + γ bκ ln s + …) ;
  - γ ; sa dependance en k ; la contribution de la donnee A ;
  - controle de coherence entre le coefficient du log de W et le residu du pole de (2.17).
- **Recherche bibliographique** (apres le sceau, EX-7 avant tout verdict) : requete « trace anomaly tensor perturbations de Sitter graviton Weyl-squared coefficient logarithmic », bases alphaXiv et recherche web. Critere de retenue : travaux qui calculent l'evolution des modes tensoriels (ondes gravitationnelles) sur de Sitter ou en inflation avec le terme de charge de Weyl de l'action anomale (ou l'equivalent a une boucle). Candidats connus de memoire, **a verifier** : Hawking, Hertog et Reall, « Trace anomaly driven inflation » (2001) ; travaux de Starobinsky (1981-1983) sur le spectre tensoriel dans le modele a anomalie ; Fabris, Pelinson et Shapiro (vers 2000-2001) sur la stabilite des ondes gravitationnelles avec l'action induite. Lecture minimale : resume et section ou l'equation des modes tensoriels est ecrite (EX-9 : jusqu'a la fin de la section suivante).

## 2. Sous-questions
- **u-1** : u₁ contient-il un terme B s³ ln s ? Quel coefficient ?
- **u-2** : W_E acquiert-il un terme γ bκ W₀ ln s ? Valeur de γ ; independance en k ; role de A.
- **u-3** : coherence avec le residu du pole de (2.17) (|8bκ| W_E/Ω).
- **u-4** : la litterature connait-elle ce comportement (log ou puissance anormale des modes tensoriels, proportionnel au coefficient de charge de Weyl) ? Concordance ou discordance ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **U-V1** | γ ≠ 0 calcule, independant de k ; W_E ≈ W₀(1 + γbκ ln Ω) au premier ordre ; coherent avec le pole ; la litterature retrouve un effet de meme nature (ou ne le contredit pas), qualification nommee. |
| **U-V2** | γ = 0 : la source polaire ne fait pas diverger W une fois l'equation d'Einstein resolue de facon coherente ; G-V3 doit etre requalifie (pole dans R sans perte de regularite de W). |
| **U-V3** | Indecidable : reduction d'ordre ambigue, modes parasites, ou litterature contradictoire sans arbitrage. |
| **U-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**U-V1.**
- u₁ contient un terme proportionnel a B k³ s³ ln s. W_E acquiert γbκ W₀ ln s, avec γ un nombre pur (independant de k), non nul, dont le signe suit la convention de b. La donnee A ne produit pas de log a l'ordre dominant de W_E.
- Le coefficient du log de W est coherent avec le residu du pole, a un facteur de normalisation de l'equation de Bianchi pres.
- La litterature contient un effet de meme nature (modification logarithmique, ou par loi de puissance, des modes tensoriels proportionnelle au coefficient de C² de l'anomalie), sans avoir ete lu sous l'angle de la regularite au raccord.
- Je ne predis pas la valeur numerique de γ.

## 5. Instruments prevus
Script `iru_transport.py` (sympy), empreinte avant execution ; lectures via alphaXiv et recherche web, textes sauvegardes et empreintes.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange.
