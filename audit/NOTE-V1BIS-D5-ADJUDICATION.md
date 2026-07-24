---
id: NOTE-V1BIS-D5-ADJUDICATION
session: S11
date: 2026-07-24
gel: GEL-V1BIS-D5 (sha256 bd0b40c8c7f72bee779296c535c369ce9bfb51431ddb785db0dd6490b2fe5560), byte-intact de bout en bout
amendements: 3 (fichiers séparés datés ; l'amendement 3 rétracte le critère de l'amendement 2)
plafond: CONSTAT SUR PIÈCES LOCALES — annoncé au gel, atteint, non dépassé
verdict: W3
type: "note d'adjudication — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
---

# Volet 1-bis — [D5] : verdict W3

## 1. Verdict

**W3 — PAS DE RÉFÉRENT.** Aucune dispersion d'ordre 500 n'existe dans les trois
pièces au périmètre. Le « σ = O(500) » du correctif R-23 n'a **pas de
correspondant local**. [D5] est tranché **NÉGATIVEMENT, par absence** :
« 900 ± 700 » et « σ = O(500) » ne sont pas la même quantité.

**[D5] est LEVÉ.** Il n'est pas reconduit en consignation.

## 2. Comment le verdict a été atteint — ordre de résolution FIGÉ au gel

L'ordre [D5-c] → [D5-d] → [D5-a] → [D5-b] était figé **avant toute lecture**.
Il a résolu en deux pas et les deux derniers discriminants n'ont pas été
atteints. C'est l'ordre gelé qui opère, non une échappatoire : le réordonner
après mesure aurait été le risque de fit que le gel interdit.

### [D5-c] NORMALISATION — MESURÉ, décisif

Table II **porte une convention d'unité**, et elle n'est ni dans la légende ni
dans les cellules : elle est dans les **EN-TÊTES DE COLONNES**, qui tabulent

    10⁻² f_NL^{ttt,+}   |   10⁻² f_NL^{ttt,−}   |   10⁻² f_NL^{ttt}

Le nombre imprimé dans une cellule est donc 10⁻² f_NL : **f_NL = 100 × valeur
tabulée**. C'est très exactement ce que le prompt S11 donnait pour absent
(« aucune mention d'unité n'y figure ») — la mention existe, à un endroit que
l'extraction en flux ne restitue pas comme un en-tête.

Le comparateur autorisé (Table III de 2409.10595v2, préfixes de ligne en
`(×10⁻²)`) n'a pas eu à être ouvert : la convention est établie sur la pièce
elle-même. Périmètre non consommé.

### [D5-d] EXISTENCE — MESURÉ, NÉGATIF

Panneau inférieur de Table II (Planck 2018, pipeline SEVEM), lu en périmètre :

    T only (Planck 2018)     4 ± 17     90 ± 100     6 ± 16
    E only (Planck 2018)    75 ± 75   −790 ± 830    70 ± 75
    T + E (Planck 2018)     16 ± 14      2 ± 20     13 ± 12

Sous la convention, les dispersions valent 1 200 à 83 000 en f_NL^ttt. En
unités tabulées elles valent 12 à 830.

- Cible ~500 en f_NL : **aucune** (la plus proche est 1 200).
- Cible ~5 en tabulé (ce qui ferait 500 en f_NL) : **aucune** (la plus proche
  est 12).

À **aucune des deux normalisations** le panneau inférieur ne porte une
dispersion d'ordre 500. [D5-d] est NÉGATIF ⟹ **W3**, par la règle figée.

### [D5-a] et [D5-b] — non atteints

L'ordre gelé ne les appelle pas. [D5-a] est par ailleurs déclaré partiellement
non mesurable (amendement 3 §C, clause I-c) : le bloc d'affichage de
l'équation (10) donne une structure d'HÉLICITÉ (trois δ^K fixant λᵢ = +2, trois
tenseurs de polarisation contractés cycliquement), mais sa dépendance en FORME
n'est pas dans la coupe.

## 3. Ce que la convention établit AUSSI — et qui ne rouvre pas V1

Le verdict V1/V6 est clos et déposé ; il n'est pas rouvert et n'est pas amendé.
Mais la convention mesurée ici **le qualifie**, et le taire ferait circuler une
demi-vérité en S12.

V6 déclare F2 inexacte sur la **LOCALISATION** : « 900 ± 700 » n'est pas en
Table II. Cette conclusion portait sur une **CHAÎNE**, et elle reste vraie comme
telle : la chaîne « 900 ± 700 » ne s'imprime pas dans la table.

Or S10 a mesuré et déposé que le ttt équilatéral fiducial y est donné à **± 7**
en unités tabulées. Sous la convention 10⁻² mesurée aujourd'hui, cette
dispersion vaut **± 700 en f_NL^ttt** — soit exactement la seconde moitié de
« 900 ± 700 ».

Autrement dit : **la QUANTITÉ que F2 situe en Table II s'y trouve bien ; c'est
sa CHAÎNE qui ne s'y trouve pas.** V6 a tranché sur la littéralité et l'a fait
correctement ; il ne dit rien de la substance, et il ne doit pas être reporté
comme s'il la réfutait. La valeur centrale (900) n'est pas reconstructible dans
le périmètre : la ligne qui la porterait est hors coupe.

## 4. Ce que ce verdict NE dit PAS

- Il ne statue pas sur le **fond** de R-23. La réserve du §2 du gel est
  inéliminable : le côté R-23 n'a jamais été ouvert, il n'est entré ici que
  tel que le prompt S11 le rapporte. Maintien, amendement ou retrait de R-23
  relèvent d'un **GO séparé** et supposent l'ouverture du corps de F5, voie (i).
- Il ne dit pas d'où vient le « O(500) » de R-23. Une origine par lecture de la
  table **sans** sa convention d'en-tête est concevable, mais la vérifier
  exigerait d'ouvrir R-23 : **non fait, non mesuré, non affirmé**.
- Il ne porte que sur les **trois pièces au périmètre**, pas sur le papier.
  Plafond CONSTAT SUR PIÈCES LOCALES.
- Il ne retire aucune inconnue de `{ A4 ; A2★ ; N }`, ne touche pas au Silo R
  (clos 12/12), ne produit ni instrument ni sceau.

## 5. Écarts de ce volet — quatre, décomposés

1. **§5.5 du gel dégénéré** (borne « marge gauche » = début de l'équation).
   Nommé, amendement 1 §A.
2. **Débordement n° 1** : ligne fiduciaire du panneau supérieur de Table II,
   lue en croyant couper les en-têtes. Consignée, **NON EMPLOYÉE** (amd 1 §C).
   Le verdict n'en dépend pas : la convention vient des en-têtes réels, et
   le ± 700 du §3 vient d'une mesure S10 déjà déposée.
3. **Amendement 2 faux, et aggravant.** Son critère classait comme « affichage »
   la dernière ligne d'un paragraphe. Rétracté par l'amendement 3.
4. **Débordement n° 2** : deux lignes de prose précédant l'équation (10),
   entrées par la coupe élargie de l'amendement 2. Consignées, **NON
   EMPLOYÉES** (amd 3 §B).

Quatre occurrences de la même leçon S10 dans un seul volet, dont une où la
correction a aggravé le défaut. Imputables au pilote.

---

*§6.4 — cadrer, geler, couper, lire, adjuger, amender, rétracter : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
