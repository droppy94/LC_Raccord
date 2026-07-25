---
id: LC-BETA-04-P0-RENDU-SEPT-SOURCES
titre: "P-0 (R-41) RENDU sur les SEPT sources du périmètre gelé — identités, grades, miroirs, sha256 des octets consommés. Porte l'ARBITRAGE nº3 de l'opérateur (2026-07-25) et la RÉSERVE ÉCRITE qui l'accompagne sur S9 et S10."
codename: LC-RACCORD
type: "registre d'identification R-41. Il n'est PAS un classement. Aucune ligne n'y est portée en C-i/C-ii/C-iii/C-iv."
version: 1.0
langue: fr
date: 2026-07-25
session: S16
portee: "Rend la précondition dure « PAS D'IDENTITÉ, PAS DE POSITIONNEMENT ». Il ne déclenche RIEN : S-B1 exige un GO séparé."
---

# P-0 (R-41) — rendu sur les sept sources

## 0. Ce que cette pièce n'est pas

Elle **n'ouvre aucune gate**, **ne classe aucune ligne**, **ne touche aucun verdict**.
Un sha256 atteste des **octets**, jamais un titre, des auteurs, un DOI ni un grade.
`{ A4 ; A2★ ; N }` INCHANGÉ · β `T-b` NON RÉSOLU · CCC ni démontrée ni réfutée.

## 1. Ordre d'exécution — opposable

Les identités ont été lues **dans les octets d'abord**, la recherche **ensuite**.
À aucun moment une identité n'a été obtenue par recherche puis soumise à confirmation
de l'opérateur : cela aurait constitué **un seul témoignage corrélé** (R-54).

## 2. Octets consommés (§1.5)

| réf | fichier | octets | sha256 | p. |
|---|---|---|---|---|
| `B1` | `2503.09372v2.pdf` | 979 890 | `6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62` | 38 |
| `B2` | `1909.11703v2.pdf` | 386 010 | `e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7` | 14 |
| `B3` | `2402.04308v2.pdf` | 4 629 572 | `1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2` | 78 |
| `B4` | `2312.17316v2.pdf` | 1 223 061 | `7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541` | 88 |
| `S8` | `9511019v1.pdf` | 673 944 | `f63ff614514117b9be2bdde735c793aae45c3e44b8efa945e594ba9850423b00` | 51 |
| `S9` | `2602.15275v2.pdf` | 422 924 | `a98eefabf1660c6a6710adbd27ac827f8ae8dc35a529d6edda294543cb5ec131` | 25 |
| `S10` | `2605.11821v2.pdf` | 479 610 | `225b33ef0bbea5524e55957fec37f20f9722388b45f2debf01b15664ccf588b5` | 13 |

`%PDF` en tête, `%%EOF` en queue, sur les sept.
**B1–B4 : 4/4 CONCORDANTS au registre `NOTE-REPRISE-GIT-S15` §3.1**, hachés **en flux, avant
extraction**. **S8/S9/S10 : PREMIÈRES MESURES**, aucun registre ne les précédait — elles font
référence à compter de cette pièce (précédent S10 nº9).

## 3. Identités, grades (§1.3) et miroirs (§1.2)

| réf | auteurs / titre lus dans les octets | grade éditorial ÉCRIT | miroirs à éditeurs distincts | §1.2 |
|---|---|---|---|---|
| `B1` | Parvizi, Sheikh-Jabbari, Taghiloo — *Freelance Holography, Part II: Moving Boundary in Gauge/Gravity Correspondence* | **SciPost Phys. Core 8, 075 (2025)**, DOI `10.21468/SciPostPhysCore.8.4.075`, publié 31/10/2025 | arXiv · SciPost Foundation · INSPIRE-HEP · ADS | ✓ |
| `B2` | Horowitz, Wang — *Gravitational Corner Conditions in Holography* | **JHEP 01 (2020) 155**, DOI `10.1007/JHEP01(2020)155`, SISSA/Springer | arXiv · Springer · INSPIRE-HEP · Deutsche Nationalbibliothek | ✓ |
| `B3` | Liu, Santos, Wiseman — *New Well-Posed Boundary Conditions for Semi-Classical Euclidean Gravity* | **JHEP 06 (2024) 044**, DOI `10.1007/JHEP06(2024)044` | arXiv · Springer · INSPIRE-HEP | ✓ |
| `B4` | Bzowski, McFadden, Skenderis — *Renormalisation of IR divergences and holography in de Sitter* | **JHEP 05 (2024) 053**, DOI `10.1007/JHEP05(2024)053` | arXiv · Springer · ADS · DOAJ · dépôt institutionnel Southampton | ✓ |
| `S8` | Bros, Moschella — *Two-point Functions and Quantum Fields in de Sitter Universe* | **Rev. Math. Phys. 8 (1996) 327–392**, DOI `10.1142/S0129055X96000123`, World Scientific | arXiv · World Scientific · multiples | ✓ |
| `S9` | Nakayama — *To boost or not to boost, that's the question*, YITP-26-13 | **PRÉPRINT arXiv NON ARBITRÉ** (v1 17/02/2026, v2 18/02/2026) | **arXiv SEUL** | ✗ |
| `S10` | Ghaffari, Luciano, Mantica — *Thermodynamic formulation of Cotton gravity in the Codazzi parametrization* | **PRÉPRINT arXiv NON ARBITRÉ** (v1 12/05/2026 ; octets consommés = v2, daté 09/07/2026) | **arXiv SEUL** | ✗ |

**Lecture des miroirs, déclarée et non tue** : l'éditeur de publication (SciPost, SISSA/Springer,
World Scientific) est un miroir indépendant sans ambiguïté. INSPIRE-HEP et ADS tiennent des
fiches curées mais **ingèrent la métadonnée arXiv** — comptés, dépendance déclarée. Un article
qui **cite** un préprint n'est **pas** compté (règle R-41 §1.2).

**Recoupements de pagination non corrélés aux octets** : `B1` 38 p. (INSPIRE) · `B2` 14 p.
(arXiv) · `B4` 88 p. (ADS). Trois sur sept.

## 4. Objet vérifié, pas le titre (§1.4)

Recensement d'occurrences dans les octets consommés, par extraction texte :

| réf | signature d'objet mesurée |
|---|---|
| `B1` | 147 « boundary condition », 77 Dirichlet, 28 Neumann, 37 cutoff, 5 « two boundar », 67 AdS |
| `B2` | conditions de coin, 21 AdS, 5 « boundary condition », 14 p. |
| `B3` | 168 « boundary condition », 65 Dirichlet, 13 « conformal boundary » |
| `B4` | 129 « de Sitter », 151 « renormalis », 95 « shadow », **4 « graviton » sur 88 p.** |
| `S8` | 125 « de Sitter », 16 « perikernel », **0 graviton, 0 AdS** |
| `S9` | 63 « aether », 18 « de Sitter », 0 « boundary condition » |
| `S10` | 86 « Codazzi », 39 « Cotton », **0 AdS, 0 graviton, 0 « boundary condition »** |

Chaque objet **concorde avec son titre**. **Aucune de ces mesures ne classe quoi que ce soit** :
la grille `C-i`/`C-ii`/`C-iii`/`C-iv` n'est pas ouverte ici.

**ANTÉRIORITÉ `B4`** : le dossier a DÉJÀ adjugé Skenderis comme scalaire **MONO-bord**, muet sur
le graviton deux-bords. Le recensement ci-dessus **ne confirme ni n'infirme** cette adjudication :
il la précède dans l'ordre imposé (« classer sous la grille PUIS confronter »). Il est
**interdit de l'importer comme acquis** (`FB-2`/`FB-3` non franchis) et **interdit de reclasser
en ignorant le dossier**.

## 5. ISSUE FANTÔME — écartée par mesure

**0 fantôme sur 7.** Les sept identités sont attestées hors de la mémoire du pilote et hors du
seul témoignage de l'opérateur. `R-41` avait déjà intercepté un article fantôme ; ici il n'en
intercepte aucun. **C'est un résultat, pas une formalité** — et il est daté : un préprint peut
être retiré ou remplacé après cette mesure.

## 6. ARBITRAGE nº3 (opérateur, 2026-07-25)

**Question posée** : `S9` et `S10` ne sont **ni fantômes ni sans octets** — identité attestée,
objet vérifié, octets mesurés — mais **sans grade arbitré** et **avec un seul éditeur**. Le
statut `SUSPENDU POUR NON-IDENTIFICATION` (arbitrage nº1 §2) **ne les couvre pas** : il vise
l'absence d'identité, pas l'absence de grade. Le cas n'était pas prévu.

**Deux lectures ont été présentées, non tranchées par le pilote.**
**Lecture retenue par l'opérateur : (ii).**

> « préprint arXiv non arbitré » est un grade **ÉCRIT**, et le seuil de trois miroirs **vise le
> fantôme**, désormais écarté ⟹ **`S9` et `S10` sont CLASSABLES, SOUS RÉSERVE ÉCRITE.**

**Portée** : cet arbitrage porte sur `S9` et `S10` **et sur rien d'autre**. Il ne modifie ni
`R-41` §1.2 dans sa lettre, ni l'arbitrage nº1, ni le statut de quelque autre ligne.

## 7. LA RÉSERVE ÉCRITE — à contenu nommé

Elle est **opposable** et **se recopie avec la ligne**. Une ligne `S9`/`S10` qui apparaîtrait
sans elle est une ligne **incomplète**.

1. **AUCUN COMITÉ DE LECTURE NE S'EST PRONONCÉ.** Le grade de `S9` et `S10` est
   *préprint arXiv non arbitré*. Aucune conclusion tirée de ces deux lignes ne peut
   s'adosser à un grade éditorial : **il n'y en a pas**.
2. **§1.2 N'EST PAS SATISFAIT À LA LETTRE.** Ces lignes sont classables **par arbitrage
   d'opérateur**, non par satisfaction du critère. La distinction ne s'efface pas avec le temps.
3. **UN SEUL ÉDITEUR ATTESTE.** arXiv. Si arXiv se trompe, se fait tromper, ou retire la pièce,
   **rien ne le rattrape** : il n'existe aucune contrepartie indépendante.
4. **LA RÉSERVE EST RÉVERSIBLE PAR L'ÉVÉNEMENT, DANS LES DEUX SENS.** Publication ultérieure ⟹
   le grade change et la ligne **SE RE-CONFRONTE**, elle ne s'hérite pas. Retrait ou remplacement
   ⟹ la ligne retombe sous `SUSPENDU`. **La mesure vieillit ; sa date la borne.**
5. **CETTE RÉSERVE N'EST PAS UN DÉFAUT DE RECHERCHE.** `S9` et `S10` sont des préprints de
   février et mai 2026. **Aucune quantité de recherche ne leur fabriquera un second éditeur.**
   L'écart est une propriété des objets, pas de l'instrument.

## 8. LIMITE OUVERTE SUR LES SEPT — NON couverte par l'arbitrage nº3

**LE GRADE PORTE SUR L'ARTICLE PUBLIÉ ; LES OCTETS CONSOMMÉS SONT LE PRÉPRINT.**
Pour `B1`, `B2`, `B3`, `B4` et `S8`, le sha256 du §2 atteste une version arXiv `vN`, **pas** la
version d'éditeur qui porte le grade du §3. Les octets publiés **n'ont pas été fournis** et les
deux versions **n'ont pas été confrontées**. §1.3 est satisfait **pour l'article**, et **n'est
pas transféré aux octets**.

Cette limite vaut sur **CINQ lignes sur sept** et **l'arbitrage nº3 ne la touche pas** : il
portait sur l'absence de grade, non sur le décalage version-consommée / version-gradée.
**Elle reste OUVERTE et NON ARBITRÉE.**

Corollaire mesuré : **aucun sha256 externe n'atteste ces octets.** L'allowlist `bash` ne couvre
pas arxiv.org ; le canal web rend du **texte**, non des octets hachables. Pour `S9`, le texte
servi par arXiv concorde avec les octets locaux — concordance de **contenu**, **même éditeur**,
pas d'octets. Pour `B1`–`B4`, la concordance 4/4 est une **re-confrontation au registre LC**,
lui-même issu d'une mesure antérieure d'octets fournis par l'opérateur : **ce n'est pas une
attestation indépendante.**

## 9. Surfaces — mesuré en S16

Le mount `/mnt/project` a servi `2503_09372v2.pdf`, `1909_11703v2.pdf`, `2402_04308v2.pdf`,
`2312_17316v2.pdf` : **quatre archives ZIP nommées `.pdf`** (`PK\x03\x04`), tailles et sha256
sans rapport avec le registre. **Ce n'est PAS une divergence du registre, c'est une surface qui
ne sert pas les octets** — classe déjà consignée à `3419d49` (S10), `af97865` (S11) et
`NOTE-REPRISE-GIT-S15` §3.2, **reproduite à l'identique une troisième fois**.

Conséquence : **le canal 2 ne corrobore rien.** La concordance des quatre corps `B` repose sur
**un seul canal** en S16.

Pare-feu β sur sa surface réelle (`LC-BETA-05` §1) : **0 fuite, 0 intrus** sur `/mnt/project`.
Travail conduit en **atelier séparé**, hors dépôt, hors mount, hors répertoire du paquet gelé.

## 10. Ce que P-0 rend, et ce qu'il ne rend pas

**REND** : la précondition dure « PAS D'IDENTITÉ, PAS DE POSITIONNEMENT » est **satisfaite sur
les sept lignes** — cinq pleinement, deux sous la réserve du §7.

**NE REND PAS** : aucun classement, aucune gate, aucun verdict, aucune conclusion de physique.
`S-B1` exige un **GO séparé** et reste **STÉRILE** par régime : s'il conclut sur la physique, il
a violé son régime.

---

*§6.4 — sentinelle terminale. Identifier, hacher, dater, réserver, arbitrer : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit. Rendre P-0 n'ouvre aucune
gate et ne classe aucune ligne. β `T-b`, non résolu, SEUL facteur d'O₂ ouvert.
**CCC n'est ni démontrée ni réfutée.***
