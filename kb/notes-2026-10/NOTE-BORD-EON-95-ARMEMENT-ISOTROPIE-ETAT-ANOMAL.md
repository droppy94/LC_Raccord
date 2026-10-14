---
id: NOTE-BORD-EON-95-ARMEMENT-ISOTROPIE-ETAT-ANOMAL
numero: 95
serie: I
branche: Q-M3 suite (isotropie de l'etat)
reservation: 2026-10-10T11:47 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 95)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (question, espace des verdicts et prediction figes AVANT toute recherche ou lecture de source)
depend: [NOTE-BORD-EON-94-AUDIT-FROID-Q-M3-CONCORDANCE, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION, REPRISE-AUTOPORTANTE-ROUTE-KAPPA-2026-08-24]
issue_attendue: "delimitation"
rouvre_si:
  - "source non lue dans cette seance traitant explicitement <T_mu nu> de l'anomalie QED dans un champ de fond pres de I+"
  - "objection exterieure sur la lecture des sources de NOTE-96"
---

# NOTE-95 : armement. L'etat anomal QED est-il asymptotiquement isotrope a 𝓘⁺ ?

## 0. Origine
NOTE-92, confirmee par l'audit froid NOTE-94 (AU-V2), etablit dans son cadre (lineaire, fond de Sitter fixe, un mode, secteur scalaire) que, sous C-M1, le second membre de l'equation (2.17) de Friedrich n'est regulier que si la partie logarithmique imposee par la conservation est **isotrope** : `ρ ⊃ A Ω⁴ ln Ω`, `p_i ⊃ (A/3) Ω⁴ ln Ω` (fluide de type rayonnement, de trace nulle). La contrainte anisotrope est une donnee d'etat que le calcul laisse libre. La question devient physique : **un modele de champs de la contribution anomale QED (β/2e)F² a ⟨T_μν⟩ fixe-t-il cette partie, et la rend-il isotrope ?**

## 1. Savoir prealable declare (oriente la prediction, non verifie dans cette seance)
- [calcule, corpus] Reprise route κ du 24 aout, §4 (verif_S21) : « aucun champ de Maxwell classique non nul n'est un fluide de rayonnement isotrope en un point » (argument de rang, `rang(E_iE_j + B_iB_j) ≤ 2 < 3`).
- [souvenir, non lu, EX-8 : ecrit en taux] Il existe une litterature ou l'anomalie de trace de QED brise l'invariance conforme de Maxwell en FLRW conformement plat, par un couplage effectif dependant du facteur d'echelle (mecanisme de type Dolgov pour la generation de champs magnetiques). Dans ce type de modele, la contribution anomale a ⟨T_μν⟩ serait portee par le champ de Maxwell lui-meme.
- [souvenir, non lu] Il existe des actions effectives induites par l'anomalie (forme non locale de Riegert / Fradkin-Tseytlin, forme locale a champs auxiliaires) et des calculs de l'effet Schwinger en de Sitter.

## 2. Sous-questions gelees
- **I-1 (inventaire)** : quels modeles publies donnent la contribution de l'anomalie (β/2e)F² a ⟨T_μν⟩ complet (trace et partie sans trace) dans un fond conformement plat ou de Sitter ?
- **I-2 (determination)** : dans ces modeles, la partie sans trace (contrainte anisotrope) qui accompagne la trace anomale est-elle fixee par la trace seule, par l'etat du champ de Maxwell, ou par l'etat des fermions ?
- **I-3 (isotropie)** : pour les etats que ces sources considerent (vide de Bunch-Davies, champ de fond classique, ensemble statistique), la partie logarithmique a 𝓘⁺ est-elle isotrope ?
- **I-4 (regime)** : ces resultats valent-ils dans le regime de C-M1 (electron sans masse, ω/m → ∞) et au voisinage de 𝓘⁺ ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **ISO-V1** | Un modele publie fixe la partie logarithmique et la rend isotrope pour les etats physiquement naturels : la condition de NOTE-92 est satisfaite, Q-M3(a) levee au niveau lineaire. |
| **ISO-V2** | Un modele publie fixe la partie logarithmique comme un objet generiquement anisotrope (par exemple proportionnel au tenseur de Maxwell d'un champ classique) : condition violee generiquement, candidat M-V3 (a lecture exterieure). |
| **ISO-V3** | Les modeles reportent l'isotropie sur l'etat du champ de Maxwell (ou des fermions) : isotrope pour certains etats (ensembles statistiques isotropes), pas pour d'autres (champ coherent) ; la condition est deplacee, non tranchee. |
| **ISO-V4** | Litterature muette dans ce qui est lu (L-MUET, resultat plein) : aucune source lue ne fixe la partie sans trace dans ce regime. |
| **ISO-V0** | Question mal posee (a nommer ; par exemple si, sous C-M1, la contribution (β/2e)F² n'a pas la forme supposee a 𝓘⁺). |

Composites permis (un verdict principal, une qualification).

## 4. Discipline de lecture (EX-7, EX-8, EX-9, R-41)
- **EX-7** : toute source retenue est declaree dans NOTE-96 (titre, auteurs, date, type) **avant** son verdict de lecture.
- **EX-8** : tout enonce non lu au texte s'ecrit en taux ou en valeur, jamais en qualite.
- **EX-9** : toute section citee est lue jusqu'a la fin de la section suivante ; toute citation elidee joint le texte elide.
- **R-41** : pour chaque source consommee, trois miroirs sont notes (arXiv, une base bibliographique, l'editeur si publie). Une source sans trois miroirs verifies est utilisee en reperage seulement, pas en appui.
- Perimetre : au plus quatre sources lues au texte dans cette seance ; le reste est consigne en reperage.

## 5. Prediction declaree (anti-fit)
**ISO-V3**, inclinaison vers ISO-V2 pour les etats classiques : si la contribution anomale est portee par le champ de Maxwell (couplage effectif dependant de ln a), la partie logarithmique est proportionnelle au tenseur de Maxwell, donc anisotrope pour tout champ classique (§1, argument de rang), et isotrope seulement pour un ensemble statistique isotrope.

## 6. Non-surclassement
Une lecture de sources ne tranche pas CCC + M. RG-4 non concernee. Noyau {A4 ; A2★ ; N} inchange.
