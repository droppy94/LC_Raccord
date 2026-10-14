---
numero: 166
serie: I
branche: CCC-T (raccord par effet tunnel)
reservation: 2026-10-14T14:57 UTC (registre central)
date: 2026-10-14
heure: 17:25 heure de Paris
grade: "[conv], non audite"
nature: EXECUTION de la lecture sous le gel de NOTE-165 (sha256 89be9cb7c961e1c9, scelle 2026-10-14T14:58:48Z, avant toute lecture). Verdicts T-1, T-2, T-3 ; releve T-4 ; comparaison aux predictions ; passe adverse ; taux EX-8.
decision: operateur (Thierry), 2026-10-14 17:00 heure de Paris : « tu as mon accord pour continuer »
pieces_jointes: src\SOURCE-CCC-T-extraits.txt ; cct_coincidence.py ; cct_coincidence_sortie.txt
---

# NOTE-166 : CCC-T, exécution

## 0. Protocole suivi et écarts au gel
1. **Corpus** (gel §6.1) : recherche de « tunnel », « instanton », « sans bord », « no-boundary », « Hartle », « Vilenkin », « Gielen », « Turok » dans `kb/` du dépôt (notes anciennes LC-D-*, glossaire, références) et dans `kb/notes-2026-10/` (notes 89 à 164). Résultat : « Hartle-Hawking » n'apparaît que comme nom du vide euclidien de Bunch-Davies (sélecteur d'état, LC-D-F5, LC-D-O2-P2, LC-D-HOLOGRAPHIE-G3, glossaire) ; « no-boundary » n'apparaît que comme mécanisme-classe de sélection d'état (ligne « NBP ⟹ BD-forcé », LC-D-CRIBLE-EXT-B, bloquée E9) et comme repoussoir de l'univers CPT-symétrique de Boyle-Turok (LC-D-Q8-BORD-LIBRE). **Aucune pièce du corpus ne traite le raccord lui-même comme une amplitude de transition.** CCC-T est donc neuve dans le programme, comme le gel le supposait.
2. **EX-7** : métadonnées vérifiées pour S-T1, S-T2a, S-T2b, S-T4 (références de revue recoupées par les listes de références des articles lus), S-T3 (sommaire APS, texte non lu), S-T5. **Un écart** : le numéro arXiv de S-T5 cité de mémoire au gel (1104.2675) était faux ; le bon (1108.0119) a été retrouvé par titre. Consigné comme défaillance de mémoire EX-7, sans conséquence sur le verdict.
3. **Lecture hors liste, déclarée** : S-T2c, Feldbrugge-Lehners-Turok, « No smooth beginning for spacetime » (1705.00192), lue parce que S-T2a et S-T2b la désignent comme la pièce portant le résultat sur les perturbations, nécessaire à T-2.
4. S-T6 (Penrose 2010) non lu, reste [M]. Lee-Weinberg (S-T3) : métadonnées seulement ; la formule du taux de montée reste [M].
5. Aucun site protégé contourné ; tout lu via alphaXiv et le sommaire public APS.

## 1. T-1 : existence et définition d'un col dS → Big Bang dans le repère conforme

### 1.1 Ce que les sources établissent
- **Gielen-Turok 2016** : pour de la matière conforme (rayonnement parfait, scalaires conformément couplés), l'intégrale de chemin de minisuperespace se calcule exactement ; le propagateur de Feynman est régulier à a = 0 ; les solutions réelles régulières n'existent génériquement pas avec anisotropies, mais **des solutions complexes régulières existent** et sont revendiquées comme cols légitimes ; les modes de fréquence positive se prolongent sans mélange (« without even a phase shift ») ; la continuation « respects all the symmetries of general relativity and yields an unambiguous result ». Hypothèse clé déclarée par les auteurs : « no singularities obstructing such a continuation ». Limite déclarée : rupture de la théorie des perturbations à grand |η| (chocs du fluide).
- **Mais** : le rebond de Gielen-Turok traverse **a = 0** (η = 0) d'un univers plat dominé par le rayonnement, **sans constante cosmologique**. Aucune mention de a → ∞, de 𝓘⁺, ni de la CCC. Dans le repère conforme ĝ = η⁻²... non : chez eux ĝ est la métrique plate et a(η) ∝ η passe par zéro ; le point régulier traversé est a = 0, pas a = ∞. Pour le transposer au raccord de Penrose il faudrait un modèle où ĝ est régulière au point a_1 → ∞ ∧ a_2 → 0, c'est-à-dire un facteur conforme Ω qui change de signe (Ω → −Ω) ou s'inverse (Ω → −1/Ω) : exactement la route Ω déjà instruite (NOTE-42/43), **que FW-T6 interdit de rouvrir ici**. Le résultat de Gielen-Turok est donc un **analogue** (FW-T4), pas une réponse à T-1.
- **Feldbrugge-Lehners-Turok 2017 (S-T2a)** : la méthode de Picard-Lefschetz sur l'intégrale lorentzienne fixe « completely » quels cols contribuent et avec quel poids ; pour le sans-bord, le col pertinent donne exp(−12π²/ħΛ), inverse de Hartle-Hawking, en accord avec Vilenkin. **Mais Diaz Dorronsoro et al. (S-T2b)** obtiennent le résultat de Hartle-Hawking exp(+12π²/ħΛ) avec la même méthode et un **autre contour** (toute la droite réelle du lapse, passant sous N = 0), et montrent que le contour demi-infini de FLT donne une fonction de Green et non une solution de Wheeler-DeWitt ; ils citent Teitelboim : le choix du signe du lapse « is a choice, not a necessity ». FLT répliquent (S-T2c) qu'aucun contour n'évite les perturbations non supprimées. **L'ambiguïté de contour n'est donc pas levée dans la littérature lue** : deux groupes, même outil, deux amplitudes de signe exponentiel opposé, et un désaccord déclaré sur le principe qui fixe le contour.
- **Transition depuis un état dS existant** (ce que CCC-T demande, et non une création « from nothing ») : Brown-Dahlen établissent que sur fond dS fixe « all transitions are possible » (volume fini à transférer, un horizon), avec un taux de Boltzmann Γ ∼ exp(−ΔU/T_dS), non nul, et que **depuis Minkowski (ou AdS) la montée est impossible** (horizon infini). Hartle-Hawking-Hertog mentionnent la possibilité de « quantum mechanical transitions rather than classical ones across cosmological singularities that connect two classical regimes » en renvoyant à Turok-Craps-Hertog (non lu). Aucune des sources lues ne construit un col reliant un **𝓘⁺ asymptotiquement dS** à un Big Bang : les transitions dS → dS de Brown-Dahlen changent le vide à l'intérieur d'un horizon, elles ne traversent pas 𝓘⁺.

### 1.2 Verdict T-1 : **T1-V2 ⊕ T1-V3 (composite)**
- V2 : des cols complexes réguliers existent dans des modèles voisins (rebond conforme à a = 0 ; sans-bord dS), et leur amplitude souffre d'une **ambiguïté de contour non levée** (S-T2a contre S-T2b, S-T2c), portant sur le signe même de l'exposant semi-classique.
- V3 (partiel) : **aucun col connu** dans la littérature lue ne relie un état asymptotiquement de Sitter à 𝓘⁺ à un Big Bang dans le repère conforme ; le candidat le plus proche (Gielen-Turok) traverse a = 0 sans Λ, et sa transposition à a = ∞ exige précisément la route Ω interdite ici.
**Prédiction T1-V2 : réalisée pour la moitié « ambiguïté », dépassée pour la moitié « existence »** (le gel supposait implicitement que le col existait ; il n'existe que pour un problème voisin).

## 2. T-2 : ce que le col sélectionne (Weyl → 0 ?)

### 2.1 Ce que les sources établissent
- Contour de Hartle-Hawking (S-T2b, S-T4) : fluctuations **gaussiennes supprimées**, exp(−π² l(l+1)(l+2) φ²/ħH²) ; les histoires classiques prédites sont inflationnaires, lisses ; « fluctuations away from homogeneity and isotropy will be at a minimum at the bounce » (S-T4). Favorise Weyl → 0.
- Contour de Picard-Lefschetz lorentzien (S-T2c) : **gaussienne inverse**, exp(+l(l+1)(l+2) φ²/2ħH²) ; « large perturbations are favored and the theory is out of control » ; théorème général : « the problem of unbounded perturbations, at small wavelengths, is unavoidable ». Défavorise Weyl → 0, jusqu'à la perte de contrôle.
- Gielen-Turok : pas de création de perturbations à travers le rebond pour la matière conforme ; **les anisotropies entrantes ressortent** (modes prolongés sans mélange). Indifférent : le rebond transmet le Weyl, il ne le sélectionne pas.

### 2.2 Verdict T-2 : **T2-V2** (résultat dépendant du contour : V1 sous Hartle-Hawking, V3 sous Picard-Lefschetz lorentzien ; indifférent chez Gielen-Turok). **Prédiction réalisée.**
Conséquence pour A2★ : CCC-T ne fournit pas l'hypothèse de courbure de Weyl ; selon le contour elle la donne gratuitement ou la détruit. A2★ reste à établir par la voie actuelle (généricité, OA-2).

## 3. T-3 : ce que l'amplitude porte

### 3.1 Ce que les sources établissent
- Brown-Dahlen : la raison d'être des transitions dS → dS est précisément d'**effacer la mémoire** (« erase the memory of the starting point. The landscape would have no hair ») ; un taux non nul suffit.
- Hartle-Hawking-Hertog : de part et d'autre d'un rebond sans bord, la flèche thermodynamique pointe vers l'extérieur ; « events on one side are therefore unlikely to have a causal impact on the other and have much explanatory value ». Diaz Dorronsoro et al. : « the physical arrows of time would reverse around the bounce », en contraste explicite avec l'ekpyrotique.
- Gielen-Turok : **exception** : pour la matière conforme, les modes de fréquence positive passent sans mélange ni déphasage, donc une structure (les perturbations entrantes) est portée déterministement à travers a = 0, « for conformal matter » seulement ; « for theories with nontrivial running and/or soft breaking terms, one would find finite particle production ».

### 3.2 Verdict T-3 : **T3-V1 ⊕ T3-V3 conditionnel**
- V1 : dans les cadres de transition dS (Brown-Dahlen) et sans bord (HHH, DDHHJ), rien n'est porté ; les flèches du temps divergent du point de raccord.
- V3 conditionnel : dans le seul cadre à matière **exactement conforme** (Gielen-Turok), une structure conforme passe. Or le programme a déjà établi que la matière du Modèle standard **n'est pas conforme au bord** (RG-4 : masse de l'électron ; S27 : coût de C-M1) et que même les champs conformes engendrent un terme anomal (G-V3). La condition d'exception de Gielen-Turok est donc exactement celle que RG-4 et G-V3 refusent. **La seule version de CCC-T qui porterait un signal est celle que le reste du programme a déjà écartée.**
**Prédiction T3-V1 : réalisée dans le cas générique ; l'exception conforme est nommée, non prédite.**

## 4. T-4 : relevé numérique (sans verdict, FW-T5)
Script `cct_coincidence.py`, sortie archivée. Avec κ = 8πG, b = n/(120(4π)²), n = N_S + 6N_F + 12N_V :
8bκH² = n·GH²/(30π) ; 1/S_dS = GH²/π [M : S_dS = π/(GH²)].

| Espèce | n | ε = 8bκH² | ε · S_dS |
|---|---|---|---|
| scalaire | 1 | GH²/(30π) | 1/30 |
| Dirac | 6 | GH²/(5π) | 1/5 |
| photon | 12 | 2GH²/(5π) | 2/5 |

Les deux nombres sont le même GH²/π à un rationnel près (n/30). Recoupement avec les sources lues : l'exposant 12π²/Λ de FLT et DDHHJ (8πG = 1) vaut exactement S_dS/2 (vérifié numériquement : 0,5). Ordre de grandeur : GH₀² ≈ 1,5 × 10⁻¹²² ; 1/S_dS ≈ 4,8 × 10⁻¹²³ ; ε_photon ≈ 1,9 × 10⁻¹²³. **Relevé, pas d'argument** : les deux grandeurs comptent la même combinaison GH², l'une par une boucle de matière conforme sur fond dS, l'autre par l'aire de l'horizon ; aucune explication n'est proposée.

## 5. Comparaison aux prédictions et conséquence fixée d'avance

| Question | Prédit | Obtenu | Statut |
|---|---|---|---|
| T-1 | V2 | V2 ⊕ V3 | réalisée et dépassée (pas de col pour le problème posé) |
| T-2 | V2 | V2 | réalisée |
| T-3 | V1 | V1 ⊕ V3 conditionnel (matière exactement conforme) | réalisée dans le cas générique |

La conséquence écrite au gel s'applique, renforcée : **CCC-T ne sauve même pas le raccord tel que posé** (aucun col 𝓘⁺ → Big Bang dans le repère conforme n'est connu ; le plus proche exige la route Ω) ; là où un col voisin existe, son amplitude est ambiguë jusqu'au signe de l'exposant, elle ne fixe pas la courbure de Weyl, et elle n'emporte un signal que pour une matière exactement conforme, hypothèse déjà refusée par RG-4 et G-V3. **CCC-T reste une hypothèse nommée, non un candidat au noyau.** Le désirable (V1 ⊕ V1 ⊕ V3) ne s'est pas produit.

## 6. Passe adverse interne
1. « Le gel a mal posé T-1 : un raccord 𝓘⁺ → Big Bang dans le repère conforme est, par construction, un rebond à travers un point régulier de ĝ ; Gielen-Turok y répond donc directement. » Non : chez Gielen-Turok le point régulier de ĝ est a = 0 du **même** univers, avec a changeant de signe (a < 0 → a > 0) ; identifier a → ∞ du premier éon à a → 0 du second est une opération supplémentaire (Ω → −1/Ω) qui n'est pas dans la source et que le gel interdit d'instruire ici. Tenu.
2. « L'ambiguïté de contour est un débat de 2017 ; elle a pu être tranchée depuis. » Possible ; seules les pièces listées au gel ont été lues (plus S-T2c). Un verdict T1-V1 reste possible sur lecture ultérieure ; il faudrait un nouveau gel. Déclaré comme limite.
3. « Brown-Dahlen traitent des transitions à l'intérieur d'un horizon, pas d'un raccord cosmologique ; les invoquer pour T-3 est hors sujet. » Partiellement : ils servent pour la non-nullité du taux et l'effacement de mémoire, qui sont des propriétés de toute transition quantique de ce type ; ils ne servent pas pour l'existence du col (§1). Tenu avec cette restriction.
4. « T-4 est une tautologie : tout ce qui est construit avec G et H sur dS donne GH². » C'est pourquoi T-4 n'a pas de verdict. La valeur du relevé est le rationnel n/30, pas la puissance de GH².
5. Non couvert : les cosmologies à rebond non conforme (LQC, ekpyrotique) ; Turok-Craps-Hertog (Crunch → Bang par AdS/CFT, cité par S-T4) ; la littérature postérieure à 2017 sur le contour.

## 7. Taux EX-8 et pièces
- Citations de mémoire au verdict : 4 sur 17 énoncés de source (formule de Lee-Weinberg ; S_dS = π/GH² ; position de Penrose ; H₀ et M_P numériques). Détail en fin de `src\SOURCE-CCC-T-extraits.txt`.
- Extraits verbatim : `src\SOURCE-CCC-T-extraits.txt`. Script et sortie : `cct_coincidence.py`, `cct_coincidence_sortie.txt`.

## 8. Greffes proposées (non entées, pour acte)
- G-T1 : ajouter au tableau des statuts de la prochaine reprise la ligne « **CCC-T** (raccord par amplitude de transition) : hypothèse nommée (NOTE-165), instruite (NOTE-166) : aucun col connu pour le problème posé ; ambiguïté de contour ; Weyl non sélectionné ; rien de porté sauf matière exactement conforme. Non candidate. Rouvre_si : un col 𝓘⁺ → Big Bang est construit dans le repère conforme sans route Ω, ou l'ambiguïté de contour est levée. »
- G-T2 : noter au registre des précédents qu'un numéro arXiv cité de mémoire doit être vérifié par titre avant d'être écrit dans un gel (défaillance S-T5).

## 9. Non-surclassement
Rien de sélectionné, p_Q non fixé, N non chiffré, noyau {A4 ; A2★ ; N} inchangé. CCC (forme actuelle) : réfutée à titre provisoire ; CCC + M : hypothèse ouverte ; G-V3 : candidat non gravé ; **CCC-T : hypothèse nommée, instruite, non candidate**. La route Ω (NOTE-42/43) n'a pas été rouverte.
