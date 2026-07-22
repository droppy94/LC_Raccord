---
id: LC-PAQUET-B-OBJET-S2
titre: "Paquet autoportant — Module [B] : l'objet géométrique sur S²"
codename: LC-RACCORD
module: "[B] — objet sur S² (reformulé : géométrie de Cartan conforme)"
statut: "consolidation autoportante — AUCUN sceau, AUCUNE algèbre neuve, AUCUNE réduction. Recopie encadrée de la connaissance KB existante sur [B]."
tags_epistemiques: [établi, décidable-aujourd'hui, à-inventer]
version: "0.1"
langue: fr
sources_kb: [01_cadre-conceptuel, 02_programme, 04_references, GLO, 02_ossature-fibree_section]
maj: "v0.1 — création du paquet autoportant [B]. Consolide sans surclasser."
---

# Paquet autoportant — Module [B] : l'objet géométrique sur S²

> **Garde-fou d'ouverture `[§6.4, non négociable]`.** Ce paquet **consolide** la
> connaissance existante sur `[B]` ; il ne produit **aucun** résultat neuf, aucun
> sceau, aucune algèbre. « Recopier / définir » ≠ « fermer ». Le périmètre
> irréductible **{A4 ; A2★ ; N}** reste **INCHANGÉ** ; D1 non clos ; N non fixé ;
> CCC non démontrée. `[B]` n'a **jamais** eu de fichier `LC-D-*` de chaînon-verdict
> dédié : c'est un module **reformulé**, `décidable aujourd'hui`, dont le calcul
> tracteur explicite **reste à exécuter** (R-55 : rien ici n'est « livré » au-delà
> de la reformulation et de sa littérature).

---

## 0. Ce qu'est ce paquet

Note **autoportante** : elle se lit seule, sans recharger la KB. Elle rassemble,
pour le module `[B]`, sa définition, son statut, sa reformulation, sa fiche-chaînon
standard, l'état de la connaissance dans la base, un glossaire embarqué et les
références. Toutes les affirmations portent leur étiquette de statut.

---

## 1. Définition du module

**Nom (diagramme des six modules)** : `[B]` — *« objet sur S² »*, sous-titre
*reformulé (géométrie de Cartan)*.

**Position dans la chaîne de dépendance** :

```
[A] survie conforme ──► [B] objet sur S² ──► { [C] cohérence quantique ,
                                               [D] holographie / métrique }
                                            ──► [E] retour de l'échelle (Ω)
                                            ──► [F] unification RG–MQ
```

`[B]` présuppose l'aboutissement de `[A]` (existence d'une structure conforme
survivante à la fin d'éon). Il alimente à son tour **et** `[C]` (les fibres où vit
la cohérence quantique) **et** `[D]` (l'arène `S²` de l'holographie). Si l'objet de
`[B]` est trop pauvre pour qu'une théorie de champ y vive, la charge se reporte
entièrement sur `[C]` (voir critère de réfutation, §4).

**Question centrale du module** : *que reste-t-il pour comparer les cônes de
lumière une fois la métrique effacée ?*

---

## 2. Ce qui est solide `[établi]`

Deux acquis géométriques standard, non contestés (`01_cadre-conceptuel §2`) :

- **Identité conforme = champ des cônes nuls.** La structure conforme d'un
  espace-temps lorentzien *est* exactement le champ des cônes de lumière —
  l'invariant sous `g → Ω²g`. La lire comme « le résidu de la RG quand l'échelle
  disparaît » est correct (argument de Penrose).
- **Topologie `S²` des directions nulles.** En un point d'un espace-temps 4D,
  l'espace des directions nulles est topologiquement `S²` (la sphère céleste). La
  définition du fibré `N → M` (fibré des directions nulles, fibre `S²`) est
  géométriquement saine.

---

## 3. La reformulation portée par le projet `[le cœur de [B]]`

Le texte-source de la conjecture affirmait qu'à la fin d'éon « il n'y a plus de
transport parallèle, les cônes deviennent incomparables ». **C'est trop fort et
c'est corrigé** (`01 §3`, `01 §4`) :

> Le résidu géométrique n'est **pas** la simple classe conforme, mais une
> **géométrie de Cartan conforme** (calcul tracteur, Bailey–Eastwood–Gover). Cette
> structure munit la classe conforme d'une **connexion canonique** sur un fibré
> « tracteur », qui **rétablit une comparaison globale** des fibres `S²`.

Conséquence directe : l'énoncé « cônes incomparables » est **abandonné**. La
structure conforme conserve une connexion (géométrie de Weyl / Cartan) ; les
géodésiques nulles restent définies comme **courbes non paramétrées** : la lumière
se propage encore sans ambiguïté. C'est la première des deux reformulations qui
orientent tout le programme (la seconde étant celle de `[C]`).

---

## 4. Fiche-chaînon (gabarit standard du programme) `[texte 02_programme]`

- **Zone ambiguë (§2–§3 du texte-source).** Affirmation « plus de transport
  parallèle, cônes incomparables ».
- **Hypothèse de travail.** Le résidu n'est pas la simple classe conforme mais une
  **géométrie de Cartan conforme** (fibré tracteur), qui fournit une connexion
  canonique et donc une comparaison globale des fibres `S²`.
- **Outils / formalisation.** Calcul tracteur ; reconstruire `N → M` comme fibré
  associé à la connexion de Cartan conforme ; identifier les structures
  effectivement transportables (géodésiques nulles non paramétrées, structure
  projective des rayons).
- **Critère de réfutation.** Si le calcul tracteur montre que la connexion conforme
  ne distingue pas assez d'information pour qu'une théorie de champ y vive (toute la
  dynamique espérée jaugée à zéro), alors la « colle » doit venir **entièrement** de
  `[C]`, et le §3 du texte-source doit être réécrit.
- **Faisabilité.** `[décidable aujourd'hui]` — géométrie conforme établie ; aucun
  formalisme nouveau requis.

---

## 5. État actuel de la connaissance dans la KB `[cartographie honnête]`

- **Aucun chaînon-verdict `LC-D-*` dédié à `[B]`.** Contrairement à `[A]`
  (`LC-A-SURVIE-CONFORME`, cœur géométrique `établi`) ou à `[D]`
  (`LC-D-HOLOGRAPHIE-G3`, dictionnaire Fefferman–Graham), `[B]` **n'a pas** de
  fichier de fermeture propre. Son statut vit dans `01`, `02`, `04`, `GLO`.
- **Ce qui est acquis** : la *reformulation* (Cartan/tracteur) et le rejet de
  « cônes incomparables ». C'est un **redressement conceptuel**, pas une
  démonstration.
- **Ce qui reste à faire** `[décidable aujourd'hui, non exécuté]` : le **calcul
  tracteur explicite** — reconstruire `N → M` comme fibré associé, mesurer
  l'information effectivement transportable, et trancher le critère de réfutation
  (la connexion conforme est-elle assez riche pour qu'une théorie de champ y vive,
  ou toute dynamique est-elle jaugée à zéro ?). Ce calcul est **faisable avec nos
  moyens** mais **n'a pas été mené** dans la KB.
- **Interface avec `[A]`** : les données conformes de Friedrich à `𝓘⁺` (établies en
  `LC-A-SURVIE-CONFORME`, sceau `N|_𝓘⁺ = −Λ/3 < 0`) fournissent la structure
  conforme régulière que `[B]` doit habiller d'une connexion de Cartan.
- **Interface avec l'ossature fibrée** (`02_ossature-fibree_section`, archivée) :
  l'objet de `[B]` est le **contenant géométrique** de `{[C], [D]}` — base `S²`
  portant à la fois les fibres-algèbres (`[C]`) et la métrique émergente (`[D]`).

---

## 6. Glossaire embarqué `[GLO]`

- **Structure conforme.** Classe d'équivalence de métriques sous `g → Ω²g` ;
  équivaut au champ des cônes nuls.
- **Sphère céleste `S²`.** Espace des directions nulles en un point d'un
  espace-temps 4D ; arène de l'holographie céleste.
- **Fibré `N → M`.** Fibré des directions nulles au-dessus de l'espace-temps `M`,
  de fibre `S²`.
- **Géométrie de Weyl.** Géométrie où la métrique n'est définie qu'à un facteur
  conforme près, avec une connexion compatible non métrique.
- **Géométrie de Cartan conforme / calcul tracteur.** Formalisme (Bailey–Eastwood–
  Gover) munissant une structure conforme d'une **connexion canonique** sur un fibré
  « tracteur ». Rétablit une comparaison globale — d'où le rejet de « cônes
  incomparables » (module `[B]`).
- **Géodésiques nulles non paramétrées.** Trajectoires de la lumière définies comme
  courbes (sans paramètre affine privilégié) ; conservées par la structure
  conforme.

---

## 7. Références `[04_references — orientation, non exhaustif]`

- Bailey, Eastwood, Gover — calcul **tracteur** pour structures conformes /
  projectives (« Thomas's structure bundle… »), ~1994.
- Littérature **géométrie de Cartan** et géométries paraboliques (Čap–Slovák).

> `[à vérifier sur arXiv / INSPIRE-HEP avant citation formelle — R-41 : ≥3 miroirs
> indépendants avant toute consommation profonde.]`

---

## 8. Renvois

- `LC-01-CADRE §2, §3, §4` — solide / imprécis / reformulation modulaire de `[B]`.
- `LC-02-PROGRAMME — Module [B]` — fiche-chaînon standard (source du §4).
- `LC-A-SURVIE-CONFORME` — module amont `[A]` : structure conforme survivante que
  `[B]` habille.
- `LC-02-OSSATURE` (archivée) — `[B]` comme contenant géométrique de `{[C], [D]}`.
- `LC-PAQUET-C-COHERENCE-QUANTIQUE` — paquet frère (module `[C]`, reformulation
  modulaire, destinataire de la charge si le critère de réfutation de `[B]` bascule).

> **Garde-fou de portée `[à ne pas sur-lire]`.** `[B]` est `décidable aujourd'hui`
> mais **non tranché** : la reformulation Cartan/tracteur est acquise, le calcul qui
> déciderait de la richesse effective de la connexion **n'est pas fait**. Aucun
> élément de ce paquet ne réduit `{A4 ; A2★ ; N}`.
