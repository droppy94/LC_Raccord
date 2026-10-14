---
id: NOTE-BORD-EON-122-ARMEMENT-IR-q
numero: 122
serie: I
branche: Q-M3 suite (critere IR-q)
reservation: 2026-10-11T17:51 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 122)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (question, sources, espace des verdicts et prediction figes AVANT toute lecture et tout calcul)
decision: operateur (Thierry), 2026-10-11 19:50 heure de Paris : « reprendre les pistes. IR-q [...] reste la plus structurante. IR-r [...] touche la condition fond fixe »
depend: [NOTE-BORD-EON-90-Q-M3-EXECUTION, NOTE-BORD-EON-121-ACTE-GREFFE-IR-m, S26-02-VERDICT-CHANTIER-D, S27-02-VERDICTS-M-ET-REPLI]
issue_attendue: "delimitation"
rouvre_si:
  - "source de la CCC fixant explicitement une classe de regularite du raccord (C^k, polyhomogene) non lue ici"
  - "objection exterieure sur la lecture des sources ci-dessous"
---

# NOTE-122 : armement de IR-q. La regularite de (2.17) est-elle le bon critere pour CCC + M ?

## 0. Origine
- NOTE-90 a etabli que le critere de regularite de Friedrich (1311.0700, theoreme 3.1) est **structurel** : aucun terme en Ω⁻ᵏ dans le second membre du systeme conforme ecrit en inconnues rescalees, seconds membres fonctions lisses des inconnues.
- Toute la chaine 91 a 121 mesure la presence d'un ln Ω non borne dans le second membre R de l'equation (2.17). C'est ce terme qui fonde le candidat M-V3.
- Personne n'a encore verifie que la **CCC elle-meme**, telle que formulee par ses auteurs, exige cette regularite plutot qu'une regularite plus faible (differentiabilite finie, structure conforme continue, developpement polyhomogene admis). Si la CCC tolere un ln Ω dans (2.17), M-V3 perd son fondement.

## 1. Sources declarees avant lecture (EX-7)
| Id | Titre | Auteurs | Date | Type | Acces |
|---|---|---|---|---|---|
| T | The equations of Conformal Cyclic Cosmology | K. P. Tod | arXiv:1309.7248 (v2) ; Gen. Rel. Grav. 47 (2015) 17 | article de recherche | PDF local `D:\temporaire\1309.7248v2.pdf` |
| F | Smooth non-zero rest-mass evolution across time-like infinity | H. Friedrich | arXiv:1311.0700v2 (2014) ; Ann. Henri Poincare 16 (2015) 2215 | article de recherche | deja lu en NOTE-90 (§1-§4) ; relecture ciblee via alphaXiv (§1, §5 et discussion) |
| MP | The Physics of Conformal Cyclic Cosmology | K. A. Meissner, R. Penrose | arXiv:2503.24263v1 (2025) | prepublication | PDF local `D:\temporaire\PACKAGE-LC-RACCORD\40-refs-pdf\2503.24263v1.pdf` |

Regle de lecture (EX-9) : chaque passage retenu est lu jusqu'a la fin de la section qui suit ; le texte elide est joint en annexe de NOTE-123. Imports non lus ecrits en taux (EX-8). R-41 (trois miroirs) : non realisable pour les PDF locaux ; leur identite est controlee par empreinte et par la page de titre, et l'ecart est declare.

## 2. Sous-questions
- **q-1 (T)** : quelle regularite Tod exige-t-il au raccord ? Classe de differentiabilite de la metrique rescalee et du facteur conforme a travers 𝓘⁺, hypothese reciproque Ω → −1/Ω, conditions sur la matiere au raccord, role des equations de champ conformes. Les termes polyhomogenes (Ωᵏ ln Ω) sont-ils envisages ? Une regularite finie (C^k) est-elle jugee suffisante ?
- **q-2 (F)** : que dit Friedrich de la regularite « lisse » contre une regularite finie, et des consequences, sur la solution, d'un second membre non regulier ?
- **q-3 (MP)** : quelle regularite du raccord les auteurs supposent-ils ou annoncent-ils ? Que disent-ils des masses au raccord ?
- **q-4 (calcul)** : si le second membre R_νλρ de (2.17) contient A ln Ω (A ≠ 0), quelle est la regularite, a travers 𝓘⁺, de la courbure de Weyl rescalee W (equation de Bianchi rescalee ∇^μ W_μνλρ = R_νλρ), du tenseur de Weyl de la metrique non physique g, de g elle-meme, et de la courbure de Weyl de l'eon suivant (sous la regle de raccord de T si elle est explicite) ? Modele : mode spatialement homogene ou a k fini, ordre dominant.
- **q-5 (synthese)** : le critere (2.17) est-il necessaire, suffisant, ou conventionnel pour le raccord de CCC + M ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **Q-V1** | Necessaire : les formulations lues exigent une extension conforme lisse, ou une regularite que le ln Ω viole, et (2.17) est le canal par lequel elle se perd. Le critere de M-V3 est fonde sur les sources. |
| **Q-V2** | Non necessaire : les formulations lues n'exigent qu'une regularite finie compatible avec un ln Ω dans (2.17). Le log ne fait pas obstacle au raccord ; M-V3 perd son fondement en l'etat. |
| **Q-V3** | Delimitation : les sources ne fixent pas de classe de regularite precise, ou se contredisent. Le choix du critere est une convention a arbitrer par l'operateur. M-V3 devient conditionnel a une convention nommee, avec la classe exacte que le log autorise (q-4). |
| **Q-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**Q-V3, inclinant vers Q-V1.** Je m'attends a ce que T et MP supposent une extension conforme **lisse** (C^∞ ou analytique) comme hypothese de travail, sans discuter une regularite finie ni les termes polyhomogenes, et a ce que F ne traite que le cas lisse. La regularite de (2.17) serait alors la traduction fidele de l'exigence de la CCC telle qu'enoncee, mais aucune source ne montrerait qu'elle est **physiquement necessaire** : une version de la CCC a differentiabilite finie ne serait pas exclue par les textes.

Calcul q-4, prediction : un ln Ω dans R donne une W continue mais non C¹ a 𝓘⁺ (W ~ W₀ + Ω ln Ω), un tenseur de Weyl de g en Ω² ln Ω, et une metrique g de classe finie (C³ au mieux, non C⁴), polyhomogene. La courbure de Weyl de l'eon suivant resterait finie a l'ordre dominant : le raccord ne « casse » pas, il **perd de la regularite**.

## 5. Instruments prevus
Lecture : PDF locaux (pdftotext, rendu image si les formules l'exigent), alphaXiv pour F. Calcul : script `irq_diff.py` (sympy), empreinte avant execution.

## 6. Non-surclassement
[conv]. Aucune lecture ni aucun calcul avant le sceau de ce gel. RG-4 inchangee ; M-V3 candidat non grave ; noyau {A4 ; A2★ ; N} inchange.
