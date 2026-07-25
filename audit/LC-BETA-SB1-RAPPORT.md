---
id: LC-BETA-SB1-RAPPORT
titre: "S-B1 RENDU — positionnement STÉRILE des sept lignes du périmètre sous la grille gelée de LC-BETA-03 §2. Répartition C-i 0 · C-ii 0 · C-iii 7 · C-iv 0. S-B2 NON ARMÉ. Chantier refermé sur une DÉLIMITATION À CONTENU NOMMÉ."
codename: LC-RACCORD
type: "rapport de positionnement. CE N'EST PAS UN VERDICT. Aucune gate ouverte, aucune cible confrontée, aucune conclusion de physique."
version: 1.0
langue: fr
date: 2026-07-25
session: S17
cadre_gele: "LC-BETA-03-CADRAGE §2 (espace C-i..C-iv) et §4 (pare-feu FB-1..FB-6). Espace NON MODIFIÉ, aucune classe ajoutée après mesure."
precondition: "P-0 (R-41) rendu à 11e924e sur les sept lignes — cinq pleinement, deux sous la réserve écrite du §7 de LC-BETA-04-P0-RENDU-SEPT-SOURCES."
arbitrage_canal: "Opérateur, 2026-07-25, lecture (i) : le canal raster/OCR est ADMISSIBLE comme base de classement, avec MENTION DU CANAL PORTÉE SUR CHAQUE LIGNE."
---

# S-B1 — rendu

## 0. Régime, et ce qui le protège

`S-B1` **classe**. Il ne confronte aucune cible, ne teste rien, ne scelle rien. Sa protection
n'est pas le gel : c'est sa **stérilité** (`LC-BETA-03` §2). **S'il conclut sur la physique, il
a violé son régime.** Il ne conclut pas.

L'espace `C-i`/`C-ii`/`C-iii`/`C-iv` était **gelé et déposé avant toute lecture**. Aucune classe
n'a été ajoutée, retirée ni redéfinie après mesure.

## 1. CANAL, porté par ligne — arbitrage opérateur (i)

| lignes | canal | contrôle du canal |
|---|---|---|
| `B1` `B2` `B3` `B4` | mount `/mnt/project`, **raster + OCR intégral**, 38 / 14 / 78 / 88 p. lues localement | pagination **4/4 concordante** au registre ; canal contrôlé **3/3** contre de vrais PDF du dépôt (`sources/`, pagination 20/20, 26/26, 22/22, texte de page 1 concordant) |
| `S8` `S9` `S10` | **P-0 §4** — signatures d'objet mesurées DANS LES OCTETS en S16 — complété par résumés récupérés au canal web en S17 | identité, pagination, journal-ref et historique de versions concordants |

**AUCUNE ligne n'est classée sur des octets confrontables.** Les deux ensembles sont **lus**,
aucun n'est **haché**. Cette phrase se recopie avec le rapport.

### 1.1 Nature réelle du mount — MESURÉE, et elle n'est pas celle qui était consignée

Les sept `.pdf` de `/mnt/project` portent `50 4b 03 04` en tête et `PK\x05\x06` en queue :
**archives ZIP**, aucun `%PDF`, aucun `%%EOF`. Quatrième occurrence de la classe consignée à
`3419d49`, `af97865`, `NOTE-REPRISE-GIT-S15` §3.2 et `LC-BETA-04-P0-RENDU` §9 — **élargie de
quatre fichiers à sept**.

**FAIT NEUF** : les archives n'avaient jamais été **ouvertes**. Chacune contient **une image de
page ET un texte OCR par page**, plus un `manifest.json`. Les manifestes ne portent **aucun sha
de source** : la confrontation d'octets par cette voie est **impossible, définitivement**.

**Qualification à substituer à la précédente** : le mount est un **canal de LECTURE fidèle** et
un **canal de HACHAGE nul**. Trois sessions ont lu « ne sert rien » dans « ne sert pas les
octets ». Ce sont deux propositions distinctes, et seule la seconde était mesurée.

## 2. ANTÉRIORITÉ — mesurée sur les sept, pas sur une

| | `B1` | `B2` | `B3` | `B4` | `S8` | `S9` | `S10` |
|---|---|---|---|---|---|---|---|
| fichiers `kb/` citant la ligne | **15** | **10** | **11** | **21** | **0** | **0** | **0** |

`PROMPT-OUVERTURE-S17.md` §6 ITEM 1 n'adjuge d'antériorité qu'à `B4`. **Les quatre lignes de
l'ensemble B en ont une.** `B3` est inscrite **consommée** à `kb/LC-D-O2-COIN-TRANSMISSION.md`
sous le sigle `LSW 2402.04308`, et elle y fournit la **famille `p`** sur laquelle le dossier
appuie son coin de transmission — face `D` (éon `n`, GHY/Dirichlet, `g₀` fixé) contre face `N`
(éon `n+1`, Neumann/conforme, `g₃ = 0`).

L'ensemble A est à **0/3**. **La partition A/B n'est pas administrative : elle sépare le
déjà-consommé du neuf.**

**Ordre tenu sur les quatre lignes de B, pas seulement sur `B4`** : classement sous la grille
**d'abord**, confrontation au dossier **ensuite**. Rien n'a été importé comme acquis ; rien n'a
été reclassé en ignorant le dossier.

## 3. LA GRILLE — sept lignes, par source, indépendamment

### `B1` — Parvizi, Sheikh-Jabbari, Taghiloo, `arXiv:2503.09372v2` → **`C-iii`** · canal OCR

Arène **AdS** (64 occurrences contre 3 « de Sitter »), surface de **cutoff** (37). Les trois
occurrences de « two boundaries » sont, au §5 de la source, l'**interpolation entre deux rayons
d'une même surface** — un déplacement radial, pas une jonction à deux faces. « mixed boundary » :
**bibliographie seulement**.

`FB-2` **mord** (mono-bord ≠ deux-faces) · `FB-4` **mord** (cutoff ≠ genuine).
Touche β par les conditions de bord arbitraires au-delà de Dirichlet en CPSF — **contexte, pas
comblement**.

### `B2` — Horowitz, Wang, `arXiv:1909.11703v2` → **`C-iii`** · canal OCR

Conditions de coin à l'intersection de la surface de données initiales et du bord timelike à
l'infini, asymptotiquement AdS. 0 Dirichlet, 0 Neumann, 0 « shadow », 0 « graviton ».
Bord unique ⟹ `FB-2` **mord**.
Touche β par la **bonne-position** du problème aux limites — **contexte**.

### `B3` — Liu, Santos, Wiseman, `arXiv:2402.04308v2` → **`C-iii`** · canal OCR
### C'est l'approche la plus serrée de tout le périmètre, et elle échoue par quatre qualificatifs

Mesuré dans son propre texte : gravité euclidienne 4D **en cavité finie** (127 « cavity »,
149 « Euclidean »), `γ^p K = fixed`, **`p → 0` = Anderson, `p → ∞` = Dirichlet**, spectre de
Lichnerowicz stable pour `p > 1/6`, et une **pléthore de modes dynamiquement instables hors
symétrie sphérique**. « mixed boundary » : **bibliographie seulement** (Odak–Speziale).

C'est la **question** du levier — admissibilité et stabilité de modes sous une famille de
conditions de bord gravitationnelles. **Ce n'est pas le levier** :

- `FB-2` mord **à la lettre du pare-feu**, qui écrit « deux **points fixes** D et N : ce n'est
  pas une jonction de transmission ». La source livre **exactement** ces deux points fixes.
- `FB-4` mord : cavité finie = **timelike-bounded**, ce n'est pas le `𝓘⁺` genuine sans cutoff.
- `FB-1` en vigilance : une cavité euclidienne est une **régularisation**, pas une renormalisation.

**Confrontation au dossier, APRÈS classement** : concordante. Le dossier consomme `B3` comme
**appui** de la famille `p`, jamais comme comblement de la cellule.

### `B4` — Bzowski, McFadden, Skenderis, `arXiv:2312.17316v2` → **`C-iii`** · canal OCR

95 « shadow », 133 « de Sitter », 372 « AdS ». **Les 4 occurrences de « graviton » sont TOUTES
en bibliographie — ZÉRO dans le corps, sur 88 pages.** Contre-termes locaux au bord futur de dS
pour des **champs scalaires de volume** en Schwinger-Keldysh. Les 3 occurrences de
« renormalisab » portent sur la **renormalisabilité des amplitudes**, jamais sur la
**normalisabilité d'un mode**.

`FB-3` **mord** (scalaire ≠ graviton d'Einstein propageant) · bord futur unique ⟹ `FB-2`.

**Confrontation à l'antériorité adjugée, APRÈS classement** : le dossier tient Skenderis pour
**scalaire mono-bord, muet sur le graviton deux-bords**. Le classement l'a **atteint
indépendamment** et **concorde**. L'adjudication n'a pas servi de prémisse.

### `S8` — Bros, Moschella, `arXiv:gr-qc/9511019` → **`C-iii`** · canal P-0/octets + web

Fonctions à deux points et champs libres généralisés en dS d-dimensionnel ; perikernels ;
condition spectrale géodésique ; caractérisation thermique des états de vide ; géométrie de
l'espace-temps de de Sitter complexifié. Mesuré dans les octets : 125 « de Sitter »,
16 « perikernel », **0 graviton, 0 AdS**.

C'est **littéralement l'exemple écrit dans la grille gelée** — « dS-QFT, structure analytique ».
Contexte de la plus haute qualité, **et contexte**.

### `S9` — Nakayama, `arXiv:2602.15275v2` → **`C-iii`, SOUS RÉSERVE ÉCRITE** · canal P-0/octets + web

Einstein-Aether ; dS/CFT contre dS/SFT pour les corrélateurs cosmologiques ; invariance d'échelle
sans invariance conforme dans des théories duales non unitaires ; **absence de symétrie de boost
de volume**. Mesuré dans les octets : 63 « aether », 18 « de Sitter »,
**0 « boundary condition »**.

`FB-3` en vigilance : Einstein-Aether est une gravité modifiée, pas le graviton d'Einstein.
Touche β par l'holographie dS — **contexte**.

### `S10` — Ghaffari, Luciano, Mantica, `arXiv:2605.11821v2` → **`C-iii`, SOUS RÉSERVE ÉCRITE** · canal P-0/octets + web

Gravité de Cotton en paramétrisation de Codazzi ; thermodynamique d'horizon ; FRW et statique à
symétrie sphérique ; entropie holographique modifiée = Bekenstein-Hawking + correction induite
par le tenseur de Codazzi. Mesuré dans les octets : 86 « Codazzi », 39 « Cotton »,
**0 AdS, 0 graviton, 0 « boundary condition »**.

Classée `C-iii` **par la lettre de la grille gelée**, qui nomme « thermodynamique » parmi ses
exemples. **Voir l'écart nº2 du §7 : cette classification est celle que la grille impose, et la
grille est peut-être trop large.**

## 4. RÉSERVE ÉCRITE — se recopie avec `S9` et `S10`, jamais séparée

Une ligne `S9`/`S10` qui apparaîtrait sans elle est une ligne **incomplète**.

1. **Aucun comité de lecture ne s'est prononcé.** Grade : *préprint arXiv non arbitré*. Aucune
   conclusion tirée de ces deux lignes ne peut s'adosser à un grade éditorial : il n'y en a pas.
2. **§1.2 n'est pas satisfait à la lettre.** Ces lignes sont classables **par arbitrage
   d'opérateur**, non par satisfaction du critère. La distinction ne s'efface pas avec le temps.
3. **Un seul éditeur atteste.** arXiv. Aucune contrepartie indépendante n'existe.
4. **Réversible par l'événement, dans les deux sens.** Publication ⟹ la ligne SE RE-CONFRONTE,
   elle ne s'hérite pas. Retrait ou remplacement ⟹ retour sous `SUSPENDU`.
5. **Ce n'est pas un défaut de recherche.** Aucune quantité de recherche ne fabriquera un second
   éditeur à des préprints de février et mai 2026. L'écart est une propriété des objets.

**État au 2026-07-25** : ni retrait ni remplacement constaté sur `S9` ni sur `S10`. Les deux
lignes **ne retombent pas** sous `SUSPENDU`.

## 5. CLÔTURE — délimitation à contenu nommé

**`C-i` 0 · `C-ii` 0 · `C-iii` 7 · `C-iv` 0.**

Condition 3 de `LC-BETA-03` §3 — *au moins une source en `C-i` ou `C-ii`* — **FAUSSE**.
**`S-B2` N'EST PAS ARMÉ.** Le cadrage l'écrit d'avance : c'est **une issue complète, pas un
échec**. Aucun amendement R-7 n'est écrit, aucun scoping n'est gelé — les écrire obligerait à
nommer une classe non établie, **c'est-à-dire le fit**.

**CE QUI EST DÉLIMITÉ, NOMMÉ.** Les sept sources du périmètre ne comblent pas la cellule
résiduelle `R1″ ∧ R2″ ∧ R4″` et n'attaquent pas le levier d'admissibilité. L'approche la plus
serrée est `B3`, qui livre une famille de conditions de bord gravitationnelles **bien posée**
assortie d'un **critère de stabilité de modes** — donc la **forme** du levier — mais en cavité
euclidienne finie, entre deux points fixes `D` et `N`.

**CE QU'IL FAUDRAIT POUR ATTEINDRE `C-ii`, ET QUI N'EST DANS AUCUNE DES SEPT** : la même analyse
d'admissibilité, mais **lorentzienne**, au **`𝓘⁺` genuine sans cutoff**, sur une **jonction à
deux faces**, pour un **graviton d'Einstein propageant**. Ces quatre qualificatifs manquent à
`B3`, et ils lui manquent **séparément**.

**LEVIER FALSIFIABLE** (clause de dissolution, note §6.2) : une source portant **les quatre**
basculerait le classement. C'est une cible nommée, pas une espérance.

**Aucune source n'est écartée pour non-fourniture d'octets.** La clause `SUSPENDU` ne s'applique
à personne. Écarter une ligne ici aurait été présenter un fait administratif comme un résultat.

## 6. Confrontation à l'ISSUE ANTICIPÉE — datée d'avant, NON RETOUCHÉE

| point anticipé | mesuré | |
|---|---|---|
| A en `C-iii`/`C-iv` pour les trois | `C-iii` ×3 | dans l'anticipation |
| B sans aucune ligne en `C-i`, au plus une en `C-ii` | **0** et **0** | dans l'anticipation, strictement plus serré |
| `S-B2` non armé | non armé | confirmé |
| chantier refermé sur une délimitation | délimitation | confirmé |

**4/4.** Et son prix reste **sa date, pas son exactitude**. Une anticipation confirmée ne lève
aucune incertitude sur la physique : elle mesure la calibration de celui qui l'a écrite, et rien
d'autre. **Elle n'est pas retouchée, ni après S15, ni après S16, ni ici.**

## 7. ÉCARTS CONSIGNÉS

**nº1 — défaut de portée du prompt, imputable à la pièce.** Le §6 ITEM 1 n'adjuge d'antériorité
qu'à `B4`. Trois autres lignes en ont une, dont `B3` à 11 fichiers `kb/`. Le risque créé est
exactement celui que le prompt nomme pour `B4` — **importer comme acquis** — et il n'était
couvert que sur une ligne sur quatre. **Sans effet ici** : l'ordre classer-puis-confronter a été
tenu sur les quatre.

**nº2 — propriété de l'espace gelé, imputable à personne, LOURDE.** `C-iv` n'a mordu **sur
aucune ligne**. Avec « dS-QFT, structure analytique, thermodynamique » pour exemples de `C-iii`,
`C-iv` est en pratique **inatteignable**, et tout le pouvoir discriminant de la grille repose sur
`C-i`/`C-ii`. **Ce n'est pas un résultat sur les sources : c'est une propriété de l'espace.**
À arbitrer si le chantier rouvre — `C-iv` est-il une classe, ou est-il vide par construction ?
**Cet écart est nommé ICI et non corrigé** : modifier la grille après mesure serait exactement
ce que son gel interdit.

**nº3 — tampon de version de `S10`.** Le registre et P-0 §3 déclarent les octets consommés en
**v2 daté 09/07/2026**. Le tampon récupéré au canal web porte **`08 Jul 2026`**. Un jour d'écart.
Une réconciliation plausible existe — soumission contre annonce — **et elle n'est pas retenue** :
le registre §5.4 impose de ne rien conclure et de nommer. **Nommé, non résolu.** Ce qui est
établi : **v2 existe.**

**nº4 — l'ensemble A n'est plus re-confrontable.** Les octets de `S8`, `S9`, `S10` ont été
mesurés en **premières mesures** en S16, dans un atelier qui n'existe plus. **Aucune surface ne
les porte aujourd'hui** — 0 fichier sur cinq motifs cherchés, dépôt et mount. Les trois sha du
registre pour A sont donc des empreintes **sans contrepartie mesurable**. Ce qui a été confronté
ici est le **contenu**, jamais l'empreinte.

## 8. Ce que `S-B1` ne rend pas

Aucune gate ouverte. Aucun verdict touché. Aucune ligne consommée en substance. Aucune cible
confrontée. Aucune physique.

`{ A4 ; A2★ ; N }` **INCHANGÉ** · `[B]` = B-PAUVRE · W2 = DÉLIMITATION, A4 non réfuté ·
A2★ décision ouverte, C7 non levée · D1 non clos, conclusion D1c **INTACTE** · N non fixé
(≡ Λ, R-53 : 0/4) · O₂ non construit · β **`T-b`, NON RÉSOLU, SEUL facteur d'O₂ ouvert** ·
G3-a non levé · nœud (i) indéterminé · Silo R clos à 12/12.

---

*§6.4 — sentinelle terminale. Classer, positionner, délimiter, nommer un levier : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit. Un classement `C-iii` n'est
pas un jugement sur la valeur d'une source — c'est un constat de position par rapport à une
cellule résiduelle, et rien d'autre. `S-B2` non armé n'est pas un échec, et une anticipation
confirmée n'est pas une réussite. β `T-b`, non résolu, SEUL facteur d'O₂ ouvert.
**CCC n'est ni démontrée ni réfutée.***
