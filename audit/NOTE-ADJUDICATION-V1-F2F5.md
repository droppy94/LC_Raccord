---
id: NOTE-ADJUDICATION-V1-F2F5
titre: "Adjudication documentaire de la tension F2/F5 sur la provenance du chiffre « f_NL^ttt = 900 ± 700 » (consignation (a) de R-11, CONSIGNÉE et NON ARBITRÉE en S9). VERDICT V6 — LES DEUX TÊTES INEXACTES, sur points distincts : LC-D-F2-TTT-PLANCK se trompe sur la LOCALISATION, LC-D-F5-ETAT-RACCORD v0.3 se trompe sur la LITTÉRALITÉ. Le fond du correctif R-23 n'est ni confirmé ni infirmé."
codename: LC-RACCORD
type: "note d'adjudication documentaire — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4). N'est PAS un lot de redémonstration : le Silo R est clos à 12/12 et le reste."
version: 1.0
langue: fr
date: 2026-07-24
session: S10
volet: "1 sur 3 — réouverture ciblée F2/F5"
grade: "CONSTAT SUR PIÈCES LOCALES — plafond annoncé AU GEL, atteint, non dépassé."
cadrage:
  - "GEL-V1-F2F5.md — sha256 201bcfbb1963ea8e83efcacbb1abeaac19d6206872fa7794332024fa4ebd705a"
  - "GEL-V1-F2F5-AMENDEMENT-1.md — sha256 fbfe39bdb87813eb534e924d4feadef7151d14c9b1a390b7d7f2e8d69864cdf2"
  - "GEL-V1-F2F5-AMENDEMENT-2.md — sha256 9629d699fb8e78d2ee17c13fa9b8ad2d5982a4b2f70c9b2954616c66630d9af5"
integrite_cadrage: "les trois pièces re-vérifiées byte-intactes avant l'écriture de la présente note"
---

# Note d'adjudication — VOLET 1 S10, tension F2/F5

## 0. Antériorité et intégrité

Aucune note d'adjudication ne préexistait au relevé. Le gel a été figé **avant
la première ligne d'instrument et avant tout contact avec le contenu des
sources** ; son antériorité est prouvée par l'état du répertoire (`volet1/` vide,
`audit/` sans pièce `f2|f5|adjud|volet` sur 32 entrées, `instruments/` sans
pièce sur 33), et non déclarée. Les deux amendements sont datés, en fichiers
séparés, et le gel est resté byte-intact du début à la fin.

## 1. Question adjudiquée

**Une seule** : lequel, de l'énoncé de F2 ou de celui de F5, dit juste sur la
**PROVENANCE** du chiffre « 900 ± 700 ». Ni sa valeur physique, ni la conclusion
qu'il sert.

- `LC-D-F2-TTT-PLANCK` porte « f^ttt_NL = 900 ± 700 » **comme lecture de
  2312.12498 Table II**.
- `LC-D-F5-ETAT-RACCORD` v0.3 (correctif R-23) déclare ce chiffre **NON LITTÉRAL
  dans la source**, caractérisation approximative d'un σ = O(500) sur le
  template gauge-field/axion FF̃.

R-11 a consigné cette tension sans l'arbitrer, corps fermés.

## 2. Pièces et confrontation

| Pièce | sha256 (16) | octets | confrontation |
|---|---|---|---|
| `sources/2312_12498v2.pdf` | `04d9b4f457ef76c0` | 1 895 152 | **CONCORDANTE** au déclaré de l'AMENDEMENT 1 au prompt |
| `sources/2409_10595v2.pdf` | `27a949802531ea91` | 2 332 898 | **CONCORDANTE** au déclaré de l'AMENDEMENT 2 au prompt |

Re-mesurées immédiatement avant extraction (précédent S8). Extraction
`pdftotext -layout`, rc 0 / rc 0, 20 et 26 pages — comptes recoupés
indépendamment par le nombre d'images des archives du mount.

**Homonymes du mount** : `/mnt/project/2312_12498v2.pdf` et `2409_10595v2.pdf`
ne sont pas des PDF mais des **archives ZIP** de rendu page à page (20 et 26
JPEG, autant de `.txt` d'extraction, un `manifest.json`, aucune entrée `.pdf`).
Verdict de confrontation **C-3 — ARCHIVE HÉTÉROGÈNE**, déclarée **NON
CONCLUANTE** par la clause I-c. La confrontation octet mount↔git est
**impossible en principe sur cette surface** pour ce type de fichier. Aucune
archive n'a été extraite, aucun `.txt` interne ouvert.

## 3. Mesures — décomposées

**[D1] — occurrences, mesuré AVANT toute consultation de table.**
Deux occurrences isolées de `900`, deux de `700`, toutes appariées, p. 1 et p. 2.
Phrases porteuses, extraites phrase à phrase :

> p. 1 — « We report no detection of non-Gaussianity (of either parity), with
> the template amplitude constrained to f_NL^ttt = 900 ± 700 (stable with
> respect to a number of analysis variations), compared to 1300 ± 1200 in
> Planck 2018. »

> p. 2 — « The most stringent value is obtained from the full T, E and B
> dataset, with f_NL^ttt = 900 ± 700, which represents an improvement over
> previous constraints (f_NL^ttt = 1300 ± 1200) by a factor greater than two,
> mostly owing to the inclusion of B-modes. »

**Statut : L-STRICT SATISFAIT** au sens du §4 du gel — couple (valeur centrale,
incertitude) rendu exactement par les chaînes `900` et `700`, pour le mode ttt,
dans un même énoncé.

**[D2] — Table II de 2312.12498v2 et sa légende.**
Table des contraintes Planck PR4 sur le paramètre **équilatéral** de
non-gaussianité tensorielle f_NL^ttt ; colonnes parité paire / parité impaire /
combinée. Onze lignes d'analyse :

    Fiducial (T+E+B)   0 ± 8    −0 ± 14    0 ± 7
    T only             1 ± 20   −1 ± 135   1 ± 20
    E only             0 ± 30   −20 ± 436  0 ± 30
    B only            −0 ± 68   −6 ± 60   −3 ± 44
    T+E               −0 ± 11   −2 ± 32   −0 ± 10
    T+B                0 ± 14   −0 ± 18    0 ± 11
    E+B               −0 ± 17   −2 ± 40   −1 ± 16
    ℓmin = 4           0 ± 9    −0 ± 15    0 ± 8
    ℓmax = 375         0 ± 8    −0 ± 14    0 ± 7
    No linear term    −1 ± 8    −0 ± 14    0 ± 7

**Aucune occurrence de `900` ni de `700`.** σ observées de 7 à 436. Aucune
convention d'unité n'est mentionnée dans la table ni dans sa légende. La légende
annonce un **panneau inférieur** portant les résultats Planck 2018 ; ce panneau
est **absent de l'extraction**.

**[D3] — template.** Table II est celle du template **équilatéral**. **Aucune
ligne gauge-field/axion n'y figure.** Table I de 2312.12498v2, lue au titre de
l'extension, est une table de significations de détection en σ gaussiens
équivalents (test de rang χ² contre 500 simulations FFP10) : elle ne porte aucun
f_NL.

**[D4] — Table III de 2409.10595v2 et sa légende.** Onze templates. Ligne `FeF`,
section Tensor-Tensor-Tensor, préfixe `(×10⁻²)` : −16 ± 27 (T), −10 ± 10 (T+E),
**3 ± 6** (T+E+B).

**[D5] — NON MESURABLE dans le périmètre gelé.**
**CONSIGNATION par la clause I-c ([C5] du gel), pré-déclarée au gel et non
décidée après coup.** Établir « MÊME QUANTITÉ » au sens du §4 — même template,
même statistique, même normalisation — exigerait trois pièces hors périmètre :
l'équation (10) de 2312.12498v2, le panneau inférieur manquant de Table II, et
la convention d'unité de Table II.

## 4. Verdict — **V6**

Ordre de résolution du §5 du gel appliqué **sans réordonnancement**.

- **V1 exclu par MESURE.** V1 exigeait D1 = L-STRICT **et** localisation en
  Table II **et** concordance de template. La première condition est remplie ;
  **[D2] fait échouer la seconde**. Aucun amendement n'a desserré cette
  condition — elle est tombée sur une mesure.
- **V2 exclu** : le chiffre est littéral, [D1].
- **V6, évalué avant V3 (AMENDEMENT 2), RETENU** : l'énoncé de F2 et celui de
  F5 sont **chacun** contredits par au moins une mesure discriminante.
- V3, V4, V5 : non atteints.

## 5. Désignation — ce qui est inexact, tête par tête

**AVERTISSEMENT OPPOSABLE** : les corps de F2 et F5 n'ont **jamais** été ouverts,
et **leurs front-matters non plus**. Les énoncés adjudiqués sont ceux rapportés
par le prompt S10 (`de9ce9da…`, §5 volet 1). La présente note **désigne une
assertion**, elle ne cite aucune chaîne de caractères des têtes. Toute correction
suppose d'ouvrir la tête concernée — geste hors du présent volet.

**`LC-D-F2-TTT-PLANCK` — inexacte sur la LOCALISATION.**
L'assertion « 900 ± 700 est une lecture de 2312.12498 **Table II** » est
contredite par [D2] : Table II ne porte pas ce couple. Ce qui est juste, et que
la tête pourrait dire : le chiffre est une lecture littérale de 2312.12498v2,
sise en **abstract (p. 1) et en introduction (p. 2)**, où il est donné comme
l'amplitude de template contrainte, à comparer aux 1300 ± 1200 de Planck 2018.

**`LC-D-F5-ETAT-RACCORD` v0.3 — inexacte sur la LITTÉRALITÉ.**
L'assertion « ce chiffre est NON LITTÉRAL dans la source » est contredite par
[D1] : il y est imprimé deux fois, verbatim, avec son exposant ttt. Ce qui reste
possiblement juste, et que la présente note ne tranche pas : la portée du
correctif R-23, à savoir que le chiffre ne se rapporterait pas au template
visé par F5 — c'est [D5], consigné non mesurable.

**Conséquence pour R-23** : le correctif repose sur une prémisse fausse
(non-littéralité). **Son fond n'est pour autant ni confirmé ni infirmé.** Il ne
peut être ni maintenu tel quel ni retiré sur la foi de la présente note.

## 6. Consignations

Pré-déclarées au gel : **[C1]** corps des têtes fermés, aucune affirmation sur
l'intention du rédacteur · **[C2]** statut des archives du mount NON TRANCHÉ,
G-4 · **[C3]** le correctif R-23 n'est pas réaudité, seule sa lecture de la
source est confrontée · **[C4]** aucune conclusion physique tirée ni révisée ·
**[C5]** clause I-c appliquée à [D5].

Survenues en cours d'exécution, consignées au titre du §7.6 :

1. **Débordement lors de [D4]** : bornage par numéros de ligne, sans vérifier la
   fin de légende. Ont été lus en sus une note de bas de page sur les
   contributions ISW-lensing et les premiers paragraphes de la section V de
   2409.10595v2. Non employés.
2. **Débordement lors de la lecture de Table I** : l'AMENDEMENT 2 §3 prescrivait
   de borner par **détection de fin de légende** ; l'implémentation a détecté la
   fin de **page**. Environ dix-sept lignes de prose lues au-delà de la légende.
   **La correction de protocole n'a pas été appliquée par son propre auteur** —
   échec d'exécution, imputable au pilote, non défaut d'énoncé.
3. **Information hors périmètre, déclarée et NON EMPLOYÉE** : une de ces lignes
   annonce une analyse model-specific « for the template given in (10) ». Cela
   orienterait [D5] vers un template distinct de l'équilatéral de Table II.
   **[D5] reste consigné non mesurable** et le verdict V6 tient sur [D1] et [D2]
   seuls, tous deux dans le périmètre. Cette information est nommée ici pour
   qu'elle ne circule pas en contrebande dans une session ultérieure.

## 7. Portée — ce que ce verdict n'est PAS

Plafond **CONSTAT SUR PIÈCES LOCALES** annoncé au gel, atteint, non dépassé.
Aucun sceau. Aucune entrée au compte. Aucun retrait d'inconnue.

`{ A4 ; A2★ ; N }` **INCHANGÉ** · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
réfuté · A2★ décision ouverte, C7 non levée · **D1 non clos**, conclusion **D1c
intacte** — les deux lectures pointaient déjà la même conclusion et la présente
note n'y touche pas · N non fixé (≡Λ, R-53 : 0/4) · O₂ non construit · nœud (i)
INDÉTERMINÉ · **CCC non démontrée NI réfutée**.

Silo R : **clos à 12/12**, inchangé. La présente note n'est pas un lot.

## 8. Ce qui reste ouvert

- **[D5]** — même-quantité, non mesurable dans ce périmètre. Trois pièces
  nommées au §3 le lèveraient.
- **Sort de R-23** — sa prémisse est fausse, son fond indécis. Décision
  opérateur.
- **Correction des deux têtes** — suppose l'ouverture des corps, voie (i), sur
  GO distinct.
- **G-4** — gagne un fait mesuré (la surface `/mnt/project` ne transporte pas
  d'octets originaux pour les PDF, alors qu'elle transporte byte-intactes 10 des
  12 pièces texte du §0-lite). Reste **NON TRANCHÉE**. Relève du volet 3.
- **Écart de prompt** relevé au §0-lite (deux textes concurrents, celui du mount
  antérieur de 23 lignes) — sans conclusion, même question d'autorité.

---

*§6.4 — geler, confronter, extraire, mesurer, trancher une provenance, nommer
ses propres débordements : aucun de ces gestes ne scelle, ne réduit, ne compte,
ne démontre quoi que ce soit.*
