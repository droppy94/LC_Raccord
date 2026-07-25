---
id: LC-WORK-REGISTRE-CORPUS
titre: "Registre des corpus consommés — identifiant canonique, version, sha256 des octets consommés, assaut d'origine, procédure de récupération. LES OCTETS NE SONT PAS DÉPOSÉS, et c'est délibéré."
codename: LC-RACCORD
type: "registre. Il n'atteste ni un titre, ni des auteurs, ni un DOI, ni un grade — seulement des octets qui ont été mesurés, et l'aveu de ceux qui ne l'ont pas été."
version: 1.0
langue: fr
date: 2026-07-25
session: S16
---

# Registre de corpus

## 0. Pourquoi PAS les octets

Trois motifs, tous antérieurs à cette pièce et aucun inventé pour l'occasion :
**le dépôt est PUBLIC** · **les licences arXiv sont hétérogènes** · **git conserve
tout blob binaire pour toujours** — une erreur de dépôt d'octets ne se retire pas,
elle se réécrit. (`NOTE-REPRISE-GIT-S15` §6.4.)

Ce que ce registre remplace, c'est la **refourniture**. Les quatre corps `B` ont dû
être refournis **DEUX fois** faute de registre, et **une troisième en S16**. À
compter d'ici, une session neuve **récupère et confronte** ; elle ne réclame plus.

## 1. Ce qu'un sha256 de ce registre atteste — et ce qu'il n'atteste pas

**Il atteste : les octets qui ont été effectivement consommés par LC-RACCORD.**

**Il n'atteste PAS que ces octets sont ceux qu'arXiv sert aujourd'hui.** Aucune
confrontation externe n'a pu être faite : l'allowlist `bash` **ne couvre pas
arxiv.org**, et le canal web rend du **texte**, non des octets hachables. De plus
arXiv **régénère** ses PDF depuis la source : un sha qui diffère à la récupération
est un **événement de surface à NOMMER**, pas nécessairement une divergence de
substance. Dans ce cas : ne rien conclure, consigner, et confronter le **contenu**
(pagination, titre, résumé, sections) avant tout usage.

## 2. Périmètre `S-B1` — les sept sources, P-0 rendu à `11e924e`

Détail complet des grades et miroirs : `audit/LC-BETA-04-P0-RENDU-SEPT-SOURCES.md`.

| réf | identifiant canonique | version consommée | octets | sha256 | assaut d'origine |
|---|---|---|---|---|---|
| `B1` | `arXiv:2503.09372` | v2 | 979 890 | `6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62` | intrant β, ensemble B |
| `B2` | `arXiv:1909.11703` | v2 | 386 010 | `e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7` | intrant β, ensemble B |
| `B3` | `arXiv:2402.04308` | v2 | 4 629 572 | `1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2` | intrant β, ensemble B |
| `B4` | `arXiv:2312.17316` | v2 | 1 223 061 | `7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541` | intrant β, ensemble B ; ANTÉRIORITÉ adjugée |
| `S8` | `arXiv:gr-qc/9511019` | v1 | 673 944 | `f63ff614514117b9be2bdde735c793aae45c3e44b8efa945e594ba9850423b00` | ensemble A |
| `S9` | `arXiv:2602.15275` | v2 | 422 924 | `a98eefabf1660c6a6710adbd27ac827f8ae8dc35a529d6edda294543cb5ec131` | ensemble A |
| `S10` | `arXiv:2605.11821` | v2 | 479 610 | `225b33ef0bbea5524e55957fec37f20f9722388b45f2debf01b15664ccf588b5` | ensemble A |

**RAPPEL DE LA LIMITE §8 du rendu P-0** : ces sha portent sur les **PRÉPRINTS**.
Cinq de ces sept lignes ont un grade éditorial qui porte, lui, sur la **version
publiée**, **jamais confrontée à ces octets**.

## 3. Corps consommés par les assauts β — sha NON MESURÉS

Ces corps ont été **lus** au cours des assauts de transport, avant l'existence de
tout registre. **Leurs octets n'ont jamais été hachés.** Ce registre les inscrit
pour ce qu'ils sont : des **identifiants sans empreinte**.

| identifiant | assaut d'origine | sha256 |
|---|---|---|
| `arXiv:2007.06800` | `S-G3T-2` (wedge, AdS/BCFT) | **NON MESURÉ** |
| `arXiv:2606.09170` | `S-G3T-3b` | **NON MESURÉ** |
| `arXiv:2412.00183` | `S-G3T-3b` | **NON MESURÉ** |
| `arXiv:2409.08709` | `S-G3T-4b` (ST) | **NON MESURÉ** |
| `arXiv:0808.2054` | `S-G3T-4b` (de Haro) | **NON MESURÉ** |

**Conséquence à porter, non à dissimuler** : les verdicts de transport
`S-G3T-*` reposent sur des lectures dont **aucun octet n'est traçable**. Ce n'est
pas une faute rétroactive sous G-4 prospectif ; c'est un **écart qui se paiera à la
première bascule de branche**. Une re-mesure ultérieure produira des sha de
**première mesure**, pas des confrontations.

## 4. Corps déjà AU DÉPÔT — `sources/`

Rattachés à `R-11`/`R-23`. Octets présents en arbre, donc rien à récupérer.

| fichier | octets | sha256 (8) |
|---|---|---|
| `sources/2312_12498v2.pdf` | 1 895 152 | `04d9b4f4` |
| `sources/2409_10595v2.pdf` | 2 332 898 | `27a94980` |
| `sources/2503_19957v1.pdf` | 910 410 | `113ab4a2` |

**`sources/` est HORS COMPTE au §0-lite** : un répertoire non compté est un
répertoire dont **on ne détecte pas la dérive**. Reste à faire entrer dans le
compte, ou à assumer. **NON ARBITRÉ.**

## 5. Procédure de récupération

1. Récupérer `https://arxiv.org/abs/<identifiant>` puis le PDF de la **version
   exacte** de la colonne « version consommée ». **Une version non spécifiée n'est
   pas une récupération.**
2. **Le canal `bash` ne joint pas arxiv.org.** Passer par le canal web, ou par
   l'opérateur. C'est une contrainte d'environnement, pas une règle.
3. Hacher les octets récupérés et **CONFRONTER** à la colonne sha256.
   **Enregistrer n'est pas confronter** (précédent S10 nº9).
4. Concordance ⟹ les octets sont ceux de LC-RACCORD, utilisables.
   Discordance ⟹ **NE RIEN CONCLURE**. Consigner, vérifier `%PDF`/`%%EOF`, la
   pagination et le résumé, et **nommer l'écart** avant tout usage. Une régénération
   arXiv et une substitution ont la même signature au niveau du sha.
5. Ligne « NON MESURÉ » ⟹ la récupération produit une **première mesure**, qui
   **fait référence à compter de là** et ne confronte rien.
6. **Travailler en atelier séparé** : hors dépôt, hors mount, hors répertoire de
   paquet gelé (précédent S15 nº2 et nº3).

## 6. Ce que ce registre ne fait pas

Il ne classe aucune source, n'ouvre aucune gate, ne touche aucun verdict,
n'atteste aucun grade éditorial et ne rend aucune physique reproductible. La partie
**CALCULÉE** du dossier est reproductible depuis le seul dépôt ; la partie **LUE**
ne l'est pas, et ce registre **la rend récupérable sans la rendre reproductible**.

---

*§6.4 — inscrire un identifiant, écrire un sha, décrire une procédure : aucun de
ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit. β `T-b`,
non résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
