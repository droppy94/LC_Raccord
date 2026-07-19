---
id: LC-WORK-AMENDEMENT-R7-G3-IMPORT-BIENPOSE-DS
titre: "AMENDEMENT R-7 DATÉ — conversion de l'import résiduel I-SFG (bien-posé genuine-dS) du verdict LC-D-G3-ADMISSIBILITE v1.4 / chaînon LC-D-G3-ADM-IMPORTS, d'import-en-bloc à contenu vérifié-interne. Exécute l'étape (a) de la séquence a→b (armement de substance β, item de tête V49 §4.1). CI-2 identité DÉJÀ soldée (Phase 1a 2026-07-06 : 2605.03481 v1/non-publié/sans-erratum, grade confirmé). PORTÉE RESSERRÉE PAR R-54 : le contenu de Thm 1.2 (forme FG, deux DDL {g₍₀₎, g₍ₙ₎}, g₍ₙ₎ TT, correspondance 1-1, racines Lemma 3.2 {0,2,3,n,n+1}) est DÉJÀ consommé et interne (LC-D-O2-SCATTERING-FG v0.1, fetch R-7 2026-07-02, R-41 confirmé) — cet amendement NE le re-consomme PAS. L'import résiduel RÉEL à convertir = (i) le bien-posé PDE au sens fort (existence + unicité de la correspondance scattering-data↔solution, lignée Hintz-Vasy 2409.15460, dont SCATTERING-FG n'a lu qu'abstract+méthode) ; (ii) la normalisabilité (énoncé L²) de la branche Δ₊=3, EXPLICITEMENT absente de S1. Cibles BP-1..BP-3, firewall mBP, espace de verdicts figés AVANT tout fetch. R-41 INTÉGRAL source par source. Option opérateur : dépôt PDF + sha256 ⟹ grade sha256-consigné. SANS SURCLASSEMENT (§6.4) : durcir un import ne convertit PAS le T-c-conditionnel en verrou propre (le pas genuine-dS reste testé seulement par le m4-chaînon, étape b) ; {A4 ; A2★ ; N} INCHANGÉ ; β reste T-b ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 (instruction dédiée, paper-first — fige cibles/firewall/verdicts/périmètre AVANT tout fetch). Candidat au gel R-36 : sha + horodatage à consigner HORS-FICHIER au manifeste, au dépôt. NON consommé."
statut: "RÉDIGÉ — candidat au gel R-36. NON consommé. Exécution = Phase 1b (consommation ciblée BP-1..BP-3, identités déjà positionnées) puis Phase 2 (confrontation aux cibles + patch additif du chaînon ADM-IMPORTS). AUCUN sceau attendu (lecture-extraction) ⟹ §0-full NON déclenché. Audit froid NON obligatoire par défaut (pas de verdict NÉGATIF/réfutation en jeu) SAUF si BP-* fait apparaître une DISCORDANCE import↔source (⟹ R-53 + audit froid)."
version: 1.0
langue: fr
date: 2026-07-06
prerequis_kb: [LC-D-G3-ADMISSIBILITE, LC-D-G3-ADM-IMPORTS, LC-D-O2-SCATTERING-FG, LC-D-GAMMA-NSTAR-ADS4, LC-D-G3-TRANSPORT, LC-D-O2-DELTA-C]
renvois: [LC-D-G3-ADM-IMPORTS, LC-D-G3-ADMISSIBILITE, LC-D-O2-SCATTERING-FG]
tags: [amendement, R-7, R-36, R-41, G3-admissibilite, T-c-conditionnel, import-bien-pose, genuine-dS, normalisabilite, L2, Hintz-Vasy, Leimbacher, scattering-data, I-SFG, conversion-import, fetch-gate, §6.4, non-surclassement]
maj: "2026-07-06 — v1.0 : création sur GO Thierry (fork V49 §4.1, séquence a→b, choix (B) « aller au bout de a »). Prérequis de propreté : §0-lite PASS d'ouverture 2026-07-06 (baseline v2.47, PKG-SHA mount 81b316fc reproduit). CI-2 identité soldée en amont (Phase 1a même jour, positionnement multi-miroirs). R-54 appliquée : verdicts de tête G3-TRANSPORT v0.4 / G3-ADMISSIBILITE v1.4 / G3-ADM-IMPORTS + SCATTERING-FG v0.1 lus sur mount AVANT rédaction ⟹ portée resserrée (Thm 1.2 hors-scope car déjà interne)."
---

# Amendement R-7 — conversion de l'import résiduel `I-SFG` (bien-posé genuine-dS)

> **Paper-first.** Cibles, firewall, espace de verdicts et périmètre de sources FIGÉS ici,
> AVANT tout fetch et toute algèbre. **R-36** : gel horodaté consigné hors-fichier au
> manifeste, au dépôt. **R-7** : toute extension de portée post-gel = nouvel amendement
> daté. **§6.4** : rien ici ne réduit quoi que ce soit — durcir un import ≠ convertir le
> conditionnel en verrou (cela reste réservé au m4-chaînon, étape b).

## 0. Provenance et objet

Le verdict `LC-D-G3-ADMISSIBILITE` v1.4 (DÉLIMITATION RENFORCÉE / `T-c`-conditionnel) est
contingent aux imports `{I1, I5, I3, I4}`. Le chaînon `LC-D-G3-ADM-IMPORTS` (CONSOLIDÉ-PARTIEL)
a durci `I1`/`I5` (racines `{0,3}` dérivées ab initio, sceau `a0b962c8`) en réduisant ce qui
reste importé à un **import résiduel unique** : le **bien-posé genuine-dS lorentzien**
(existence, unicité, correspondance de scattering au `𝓘⁺`), grade `I-SFG`, adossé à
Leimbacher `2605.03481` (`I1`/`I5`) et à la lignée Hintz-Vasy.

**Constat R-54 (SCATTERING-FG v0.1, mount) — resserre la portée.** Le contenu de
`2605.03481` Thm 1.2 est **déjà consommé et interne** (fetch R-7 daté 2026-07-02, texte HTML
intégral, R-41 confirmé) : forme bloc-diagonale près `𝓘⁺`, deux DDL fonctionnels
`{g₍₀₎, g₍ₙ₎}`, `g₍ₙ₎` TT, **correspondance 1-1** solution↔scattering data, racines Lemma 3.2
`{0,2,3,n,n+1}`. Cet amendement **ne re-consomme pas** Thm 1.2. Mais SCATTERING-FG a
lui-même **posé deux barrières explicites** (« ce que la source n'établit PAS ») :

1. **Le bien-posé au sens PDE fort.** La correspondance lue est *donnée↔solution*
   (cinématique). L'**existence + unicité** de la solution pour toute donnée de scattering
   prescrite (le théorème PDE lui-même, lignée Hintz-Vasy `2409.15460`) n'a été consommée
   qu'au grade « abstract + méthode via le porteur primaire » — **pas le théorème d'existence/
   unicité proprement dit**.
2. **La normalisabilité.** « S1 ne dit rien de la **normalisabilité** (aucun énoncé L² sur la
   branche `r^{Δ₊}`) » — précisément l'énoncé qui, dans `G3-ADMISSIBILITE`, sous-tend
   l'implication charnière « `Δ₋=0 ⟹` mode lent non-normalisable FG-symplectique sans cutoff ».

**Objet.** Convertir `I-SFG` d'**import-en-bloc** à **contenu vérifié-interne** sur ces DEUX
volets résiduels — et EUX SEULS.

**Question figée (Q-BP).** Le bien-posé genuine-dS (existence/unicité de la correspondance
scattering-data↔solution, lignée Hintz-Vasy) et la normalisabilité de la branche `Δ₊=3`
sont-ils **établis par les sources telles qu'imprimées** (⟹ import converti en interne,
grade « source-établi vérifié »), **partiellement établis** (⟹ import réduit + résidu nommé),
ou **absents/discordants** avec l'usage qu'en fait `G3-ADMISSIBILITE` (⟹ R-53 + audit froid) ?

## 1. Cibles figées (avant toute consommation)

- **BP-1 (PORTANTE) — bien-posé PDE : existence + unicité genuine-dS.** Localiser dans le
  périmètre armé l'énoncé EXACT du théorème de bien-posé (Cauchy asymptotique / scattering au
  `𝓘⁺` spacelike, Λ>0 genuine, `n=3`) : existence ET unicité de la solution Einstein-vide pour
  donnée `{g₍₀₎, g₍₃₎}` prescrite au bord conforme. Confronter à l'usage `G3-ADMISSIBILITE` :
  la réduction de la question de normalisabilité deux-faces à une analyse mono-bord à `𝓘⁺`
  présuppose-t-elle plus que ce que le théorème livre ? **Test figé** : l'import consommé
  est-il ⊆ l'énoncé source (ni extrapolation dimensionnelle silencieuse, ni transfert
  AdS→dS non déclaré) ?

- **BP-2 — normalisabilité de la branche `Δ₊=3` (énoncé L²).** Exhiber (ou constater absent)
  un énoncé de (non-)normalisabilité L² de la branche `r^{Δ₊=3}` du mode spin-2 TT en dS
  genuine sans cutoff. **Deux issues figées** : (i) un tel énoncé EXISTE dans le périmètre
  ⟹ l'implication charnière de `G3-ADMISSIBILITE` (`Δ₋=0 ⟹` mode lent non-normalisable)
  acquiert un support source direct (import converti) ; (ii) AUCUN énoncé L² dans le périmètre
  ⟹ la normalisabilité **RESTE un import** honnêtement nommé (le durcissement est PARTIEL),
  et ce résidu est routé vers l'étape b (m4-chaînon), qui devra le tester ou l'importer
  explicitement. NE PAS blanchir une absence en présence.

- **BP-3 — cohérence de la parité dimensionnelle.** Thm 1.2 distingue `n` impair (lisse
  jusqu'à `𝓘⁺`) de `n` pair (tenseur d'obstruction). Vérifier que l'usage `n=3` (impair, cas
  du programme, sans obstruction) est le régime effectivement couvert par les énoncés BP-1/BP-2,
  et que rien du raisonnement `G3-ADMISSIBILITE` ne s'appuie tacitement sur le cas pair ou sur
  une continuation. **Test** : le maillon consommé vit-il entièrement dans `n=3` impair ?

## 2. Firewall mBP (figé)

- **mA — anti-doublon SCATTERING-FG.** Rien de ce qui est DÉJÀ interne (Thm 1.2 forme FG,
  deux DDL, `g₍ₙ₎` TT, correspondance 1-1, racines `{0,2,3,n,n+1}`) n'est re-crédité comme
  neuf ici. Seuls BP-1 (existence/unicité PDE) et BP-2 (L²) sont matière à conversion.
- **mB — anti-import HKB source-par-source (R-41 intégral).** Aucune bibliographie consommée
  en bloc. Chaque source (Hintz-Vasy `2409.15460` ; toute source additionnelle) : identité
  vérifiée multi-miroirs AVANT consommation de contenu. Identité `2605.03481` DÉJÀ soldée
  (Phase 1a) — sa RE-lecture éventuelle pour un énoncé L² spécifique reste sous R-41.
- **mC — anti-circularité `A4`.** Aucune invocation du postulat de Weyl ni d'aucun élément de
  `{A4 ; A2★ ; N}` dans la lecture des énoncés de bien-posé/normalisabilité.
- **mD — non-conversion du conditionnel.** Le chaînon de sortie DOIT porter en clair que
  durcir `I-SFG` **NE convertit PAS** `T-c`-conditionnel en verrou propre : le pas genuine-dS
  (sign(Λ)-asymétrie testée) reste l'objet du **m4-chaînon (étape b)**, non touché ici. Toute
  formulation suggérant un verrou = violation de cadrage.
- **mE — routage honnête des résidus.** Si BP-2 issue (ii) (pas d'énoncé L² dans le périmètre) :
  la normalisabilité reste import, nommée, routée vers b. Pas de fermeture par défaut.

## 3. Périmètre de sources ARMÉ (figé)

- **S1 — Leimbacher `2605.03481`** (identité soldée Phase 1a) : RE-lecture ciblée AUTORISÉE
  pour un éventuel énoncé de normalisabilité / bien-posé au-delà de Thm 1.2 déjà interne
  (§ existence-unicité, remarques L² si présentes). Grade identité-vérifié.
- **S2 — Hintz-Vasy `2409.15460`** (« approche similaire à », porteur du bien-posé) : identité
  R-41 à CONFIRMER multi-miroirs AVANT consommation ; consommation ciblée du théorème
  d'existence/unicité (BP-1). SCATTERING-FG n'en a lu qu'abstract+méthode.
- **Sources additionnelles** (p.ex. Hintz `Asymptotically de Sitter metrics from scattering
  data`, Vasy `2010`, Ringström) : identité R-41 datée AVANT toute consommation ; toute source
  hors de cette liste = **extension datée** (nouvel amendement).

## 4. Espace de verdicts `[FIGÉ]`

- **CONVERTI** : BP-1 (existence/unicité) ET BP-2 (énoncé L²) établis par les sources telles
  qu'imprimées, ⊆ usage `G3-ADMISSIBILITE`, `n=3` impair (BP-3 ✓) ⟹ `I-SFG` passe d'import
  à **contenu vérifié-interne** ; `T-c`-conditionnel **durci** (surface d'import réduite à
  ~zéro), NON converti en verrou.
- **CONVERTI-PARTIEL** : BP-1 établi mais BP-2 issue (ii) (pas d'énoncé L² dans le périmètre)
  ⟹ existence/unicité internalisée, normalisabilité **reste import nommé**, routé vers b.
  `T-c`-conditionnel durci partiellement.
- **DISCORDANT** (⟹ R-53) : l'usage `G3-ADMISSIBILITE` **excède** ce que les sources
  établissent (extrapolation silencieuse, transfert AdS→dS non déclaré, cas pair invoqué)
  ⟹ **déclencheur R-53** : révision de `LC-D-G3-ADMISSIBILITE` + **audit froid OBLIGATOIRE**
  avant toute propagation.
- **INDÉTERMINÉ** : énoncés non localisables / non décidables dans le périmètre KB+sources
  armées ⟹ consigner, aucun statut ne bouge, résidu routé vers b.

## 5. Phases `[ordre figé]`

- **Phase 1b — consommation ciblée** : (a) confirmer identité R-41 de S2 (Hintz-Vasy) et de
  toute source additionnelle ; (b) consommer les énoncés BP-1 (existence/unicité) et chercher
  BP-2 (L²) ; (c) BP-3 (parité `n`). AUCUNE algèbre neuve (lecture-extraction). 0 sceau.
- **Phase 2 — confrontation + patch** : confronter aux cibles, statuer dans l'espace figé,
  **patch additif** du chaînon `LC-D-G3-ADM-IMPORTS` (§4 CI-2 soldée + nouveau §7 conversion
  `I-SFG`) ; le cas échéant patch additif consignation sur `G3-ADMISSIBILITE` (import durci,
  SANS réouverture si non-DISCORDANT).

## 6. Relation `R-53` & effets `[figés]`

- Cet amendement **teste/durcit** un import du verdict v1.4 ; il ne le rouvre pas par décret.
  Issue CONVERTI ou CONVERTI-PARTIEL ⟹ couche additive, `G3-TRANSPORT` **RESTE `T-b`** (aucun
  verrou propre ne peut naître ici — la cible ne touche ni `R1″` ni `R2″` ni `R4″`, seulement
  la surface d'import du conditionnel).
- Issue DISCORDANT ⟹ R-53 pleine (révision + audit froid).
- Dans TOUS les cas : le pas genuine-dS reste testé seulement par l'étape b (m4-chaînon).

## 7. Non-surclassement `[§6.4, terminal]`

Convertir un import d'« en-bloc » à « vérifié-interne » réduit la SURFACE D'IMPORT d'un verdict
conditionnel ; cela **ne construit ni ne réduit** aucun des invariants du programme. `T-c`
reste **conditionnel** (non un verrou propre) tant que le m4-chaînon (étape b) n'a pas testé le
pas genuine-dS ; `G3-TRANSPORT` reste **T-b** ; `{A4 ; A2★ ; N}` INCHANGÉ ; D1 non clos ; N non
fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ; O₂ non construit ; CCC non démontrée NI réfutée.
(cf. `LC-D-G3-ADM-IMPORTS`, `LC-D-G3-ADMISSIBILITE` v1.4, `LC-D-O2-SCATTERING-FG` v0.1,
`LC-D-G3-TRANSPORT` v0.4)
