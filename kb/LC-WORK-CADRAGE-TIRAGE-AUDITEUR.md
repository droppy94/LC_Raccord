---
id: LC-WORK-CADRAGE-TIRAGE-AUDITEUR
titre: "Cadrage-instrument — DROIT DE TIRAGE DE L'AUDITEUR (item ② du mandat Tier 1, amendement LC-WORK-AMENDEMENT-R7-CONVERSION-R56-M1, gel 2d82fc1e). Toute section RETIRÉE d'une pièce jointe à un paquet incognito reste TIRABLE À LA DEMANDE de l'auditeur : livraison sha-attestée, hors paquet initial, sur le canal multi-tours. Le sha de chaque segment retiré est PRÉ-ENGAGÉ dans le harnais AVANT expédition — l'opérateur ne peut pas substituer le texte après coup. La conséquence d'un tirage sur l'aveuglement est un fait que le SOUVERAIN ASSUME : elle n'est JAMAIS un motif de refus du pilote ni de l'opérateur. Éteint le défaut #13 (contournement par robustesse faute de matériau — précédent J4/V91) et la moitié de M-3.d pour toute gate armée sous ce régime. PROSPECTIF, MONOTONE-SÛR : ajoute un droit à l'auditeur, n'en retire aucun ; ne rejuge AUCUNE gate passée. Première instanciation prévue : harnais CSE-KPS. SANS SURCLASSEMENT (§6.4) : instrumenter un droit de tirage ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "cadrage-instrument (protocole de gate — exécute le mandat ② de 2d82fc1e ; ne re-gèle AUCUNE cible, n'adjuge rien, ne consomme rien, ne touche aucune pièce d'une gate rendue)"
statut: "work-active — INSTRUMENT FIGÉ AU DÉPÔT, gel R-36 hors-fichier. Obligatoire à TOUT harnais futur (② DOIT être dans le prochain harnais, quel qu'il soit — journal V92 §5). Ne répare rétroactivement AUCUNE gate passée : #13 est éteint POUR LES GATES FUTURES à compter de la première instanciation. Compatible ⑨ (tout retrait R56-1 passe par D, texte verbatim à l'appui, AVANT retrait) et ⑩ (le registre des retraits est une déclaration de faiblesse d'INSTRUMENT : exigée, jamais tue). {A4 ; A2★ ; N} INCHANGÉ ; β T-b, seul facteur d'O₂ ouvert ; R-53 0/4 ; CCC non démontrée NI réfutée."
statut_id: provisoire — à enregistrer si validé
version: "0.1"
langue: fr
date: "2026-07-17"
gel_R36: "cet instrument N'EMBARQUE PAS son propre sha256 (anti-auto-référence). Le gel R-36 est horodaté HORS-FICHIER au dépôt, byte-exact livrable==mount."
prerequis_kb: [LC-WORK-AMENDEMENT-R7-CONVERSION-R56-M1, LC-WORK-AMENDEMENT-R7-KPS-CSE-EXPOSITION, LC-WORK-AMENDEMENT-R7-NOTE07-CSE-REDACTION, LC-WORK-AMENDEMENT-R7-SHA-GATE-FORMAT-NOM, LC-AUDIT-VERDICT]
renvois: [LC-WORK-AMENDEMENT-R7-CONVERSION-R56-M1, LC-WORK-AMENDEMENT-R7-KPS-CSE-EXPOSITION, LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION, LC-WORK-R41-KPS-MIROIRS]
tags: [cadrage, instrument, droit-de-tirage, item-2, mandat-2d82fc1e, defaut-13, M-3d, exposition, redaction, sha-atteste, pre-engagement, multi-tours, souverain, aveuglement, prospectif, monotone-sur, KPS, §6.4]
---

# Instrument — droit de tirage de l'auditeur (②)

## §0 — Nature et origine

**Mandat source, verbatim (`2d82fc1e` §2-②)** : toute section retirée d'une pièce jointe reste
tirable à la demande de l'auditeur (livraison sha-attestée, hors paquet initial). Éteint #13 et
la moitié de `M-3.d`.

**Défaut d'origine (#13, consigné V91, KB `1f1270fc` §10bis.6)** : le retrait d'une section (J4 §2)
a emporté le matériau R-41 fondant l'axe I-A de l'auditeur ; celui-ci a contourné par
**robustesse**, pas par **vérification**. Un retrait d'exposition ne doit jamais réduire la
capacité de vérification du souverain : ce qu'on lui cache pour l'aveugler doit lui rester
**accessible s'il en décide**.

Cet instrument **ne rejuge rien** : les gates passées restent telles que rendues.

## §1 — Le registre des retraits `[obligatoire à tout harnais]`

Pour toute pièce d'un paquet incognito ayant subi une rédaction d'exposition (classe
`588d09f5` / `99bf591c`), le harnais porte un **REGISTRE DES RETRAITS** :

- une ligne par segment retiré : **étiquette opaque** (p.ex. `X-1`, `X-2`, …) + **octets du
  segment retiré** + **sha256 du segment retiré, texte verbatim** ;
- l'étiquette ne décrit **pas** le contenu (une description serait la fuite qu'on ferme) ;
- le registre déclare le **compte total** des segments retirés — rien ne peut être retiré
  hors registre ;
- format `bd495c65` : **un champ par ligne, jamais un tableau à pipes**.

**Pré-engagement.** Les sha du registre sont écrits dans le harnais **AVANT expédition**, par
le script générateur de paquet (①), **jamais à la main**. L'opérateur conserve **hors-KB** le
texte verbatim de chaque segment. **Le sha lie : aucune substitution post-hoc n'est possible.**

**⑩ opposable.** Le registre est une **déclaration de faiblesse d'instrument** (des pièces sont
incomplètes) : elle est **exigée**, jamais tue. Le silence ne prime jamais sur une faiblesse
d'instrument.

## §2 — La procédure de tirage

1. **Demande.** L'auditeur nomme la ou les étiquettes qu'il veut tirer. Canal **multi-tours**
   (régime constitution en vigueur). Il n'a **aucune justification à fournir**.
2. **Livraison.** L'opérateur livre le texte **verbatim** du segment, **hors paquet initial**,
   dans le tour suivant. Le pilote **ne filtre pas, ne résume pas, ne commente pas** le segment
   livré.
3. **Vérification.** L'auditeur **recompute** le sha256 du segment reçu et le confronte au
   registre. **Écart = segment réputé NON LIVRÉ**, défaut à consigner, et le tirage reste dû.
4. **Consignation.** Chaque tirage (étiquette, tour, sha confronté, verdict de conformité) est
   consigné **au manifeste** (R56-3 : au manifeste, jamais au paquet), **après** l'issue de la
   gate — jamais pendant, pour ne pas dater les curiosités du souverain dans un document que le
   pilote relit.

## §3 — La clause d'aveuglement `[le cœur de l'instrument]`

Un tirage **peut** révéler à l'auditeur ce que l'exposition lui cachait — y compris l'issue
d'une adjudication voisine ou l'origine d'une piste. **Cette conséquence est un fait que le
souverain assume en tirant.**

- Elle n'est **JAMAIS** un motif de refus, de délai ou de mise en garde ciblée du pilote ou de
  l'opérateur. La seule mise en garde admise est **générique**, écrite au harnais, identique
  pour toutes les étiquettes : *tirer un segment peut affecter l'aveuglement que l'exposition
  institue ; l'arbitrage de ce coût t'appartient*.
- Une mise en garde **différenciée par étiquette** (p.ex. plus insistante sur l'une) serait un
  **signal de contenu** — c'est-à-dire la fuite ; elle est **interdite**.
- L'auditeur qui a tiré **adjuge quand même**, et **déclare** dans son rendu ce qu'il a tiré et
  ce que cela a changé à son propre aveuglement. Cette déclaration est un **fait du rapport**,
  pas un motif d'invalidation automatique : la validité de l'arbitrage post-tirage relève du
  souverain lui-même et, en dernier ressort, de D.

## §4 — Bornes

- **b1.** Prospectif : s'applique à toute gate **armée après ce dépôt**. Aucun usage rétroactif ;
  #13 n'est pas réécrit pour les gates passées.
- **b2.** Monotone-sûr : ajoute un droit à l'auditeur, n'en retire aucun ; ne peut pas changer
  un verdict — seulement empêcher qu'un verdict futur soit rendu **faute de matériau**.
- **b3.** Compatible ⑨ : un retrait de classe `R56-1` passe par D, texte verbatim à l'appui,
  **avant** retrait ; le présent instrument règle la **restituabilité** du retrait, pas sa
  **licéité**, qui reste chez D.
- **b4.** Le registre n'élargit pas le paquet : les segments retirés restent **hors paquet
  initial** ; seuls leurs sha y figurent.
- **b5.** Aucune issue d'aucune gate ne dépend de cet instrument : il n'oriente rien, ne
  provisionne rien, ne favorise aucune issue.

---
> **SANS SURCLASSEMENT (§6.4).** Instrumenter un droit de tirage ne scelle / ne réduit / ne
> compte / ne démontre **RIEN**. `{A4 ; A2★ ; N}` **INCHANGÉ** ; `D1` non clos ; `N` non fixé
> (≡ Λ, voie A close, `R-53` **0/4 INCHANGÉ**) ; `O₂` **non construit** ; `β` **T-b**, seul
> facteur d'`O₂` ouvert ; `A4` route par-`𝓘⁺` délimitée (W2), non réfuté ; `A2★` parqué pending
> OA ; têtes scellées = **autorité, intactes** ; **CCC non démontrée NI réfutée.**
