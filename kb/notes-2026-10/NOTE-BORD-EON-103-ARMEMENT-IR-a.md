---
id: NOTE-BORD-EON-103-ARMEMENT-IR-a
numero: 103
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-a)
reservation: 2026-10-10T18:56 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 103)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (questions, sources declarees, espace des verdicts et prediction figes AVANT toute recherche ou lecture)
depend: [NOTE-BORD-EON-102-OP-IR-EXECUTION, NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE]
issue_attendue: "delimitation"
rouvre_si:
  - "reference [21] de S2 inaccessible ou differente de ce que la bibliographie de S2 indique"
  - "derivation exacte de [21] contredite par une source posterieure lue"
---

# NOTE-103 : armement de la greffe IR-a. Quel operateur S2 utilise-t-il vraiment ?

## 0. Origine
NOTE-102 rend **IR-V1 qualifie IR-V3** : avec la prescription a⋆ = k/M, le ln a persiste, mais l'echelle infrarouge repose sur l'exactitude revendiquee de la forme Weyl-plate (2.12) de S2 et sur l'approximation (3.10). Sur le mode libre, trois operateurs candidats different : S2 exact (plat dans le repere conforme, 0 sur couche de masse), Hodge (0), Bochner (−4H²). La derivation de (2.12) est renvoyee par S2 a sa reference [21], non lue (EX-8).

## 1. Sources declarees (EX-7)
- **S2** : arXiv:1808.08237v2 (Benevides, Dabholkar, Kobayashi), bibliographie, pour identifier [21] ; §2 autour de (2.11)-(2.12).
- **[21]** : identite a etablir dans la bibliographie de S2. Hypothese a priori, **non lue**, taux de confiance ≈ 0,6 : Bautista, Benevides, Dabholkar, « Nonlocal quantum effective actions in Weyl-flat spacetimes » (arXiv:1711.00135). Si [21] est autre, le gel s'applique a la reference effective.
- Lecture : sections portant la derivation de l'action effective Weyl-plate pour le secteur de jauge, **jusqu'a la fin de la section suivante** (EX-9).
- Miroirs (R-41, au moins 3) : page arXiv abs, texte arXiv (HTML ou PDF), alphaXiv ; INSPIRE ou l'editeur pour la reference publiee.
- Aucune autre source ne sera importee sans etre declaree dans NOTE-104 comme ajout posterieur au gel.

## 2. Sous-questions
- **A-1** : [21] derive-t-il (2.12) de facon **exacte** pour toute metrique Weyl-plate, et sous quelles hypotheses (champs sans masse conformement couples, une boucle, schema, etat) ?
- **A-2** : quel est l'operateur dans le log : d'Alembertien **plat** du repere conforme (avec le facteur e^{2Ω} sorti par l'anomalie), un operateur covariant (lequel : scalaire, Hodge, Bochner, Lichnerowicz), ou une forme dont l'identification reste ambigue ?
- **A-3** : [21] dit-il quelque chose de l'echelle infrarouge ou du comportement sur couche de masse (log 0) du terme non local, pour des champs ou des modes sans masse ?
- **A-4** : [21] traite-t-il de Sitter et les termes de courbure de type H² (ou les modes hors horizon) explicitement ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **OP-V1** | [21] etablit (2.12) comme exacte sur les metriques Weyl-plates avec l'operateur plat du repere conforme (dependance en Ω entierement fixee par l'anomalie) ; un terme en H² de type Bochner est exclu dans ce cadre. La qualification IR-V3 de NOTE-102 est levee **en ce qui concerne le choix de l'operateur**. |
| **OP-V2** | [21] donne une forme covariante dont l'evaluation en de Sitter produit une echelle en H (ou S2 (2.12) n'est qu'une approximation) : NOTE-102 passe a IR-V2 ou IR-V3 principal. |
| **OP-V3** | [21] ne tranche pas : derivation non exacte, operateur ambigu, ou exactitude etablie sans rien dire de l'echelle infrarouge sur couche de masse ; IR-V3 maintenu, precise. |
| **OP-V0** | [21] inaccessible ou hors sujet. |

Composites permis (un verdict principal, une qualification).

## 4. Prediction declaree (anti-fit)
**OP-V1 qualifie OP-V3** : [21] obtient l'action exacte en integrant l'anomalie de Weyl depuis le repere plat, si bien que l'operateur est le d'Alembertien plat et qu'aucun terme en H² n'apparait ; mais la derivation laisse ouvert le comportement sur couche de masse (log 0) et l'echelle infrarouge, qui relevent de l'action plate elle-meme. La qualification IR-V3 se reduit donc a ce seul point.

## 5. Non-surclassement
Lecture de source, [conv]. Ne change ni RG-4 ni le noyau {A4 ; A2★ ; N}.
