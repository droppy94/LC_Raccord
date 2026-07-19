---
id: LC-01-CADRE
titre: "Cadre conceptuel — la conjecture et son évaluation"
codename: LC-RACCORD
tags: [cadre-conceptuel, CCC, holographie-celeste, intrication, conforme]
statut: contexte (analyse critique)
version: 1.1
langue: fr
maj: "2026-06-07 — v1.1 : correction du maillon §1 suite au chaînon LC-A-SURVIE-CONFORME. Le caractère spacelike de 𝓘⁺ à Λ>0 n'est PAS une faiblesse mais la condition favorable du raccordement (extension conforme régulière, Friedrich 1986) ; la difficulté réelle est dissociée (matière sans masse / facteur conforme / Weyl). Renvoi LC-A ajouté."
---

# Cadre conceptuel

## 1. Nature de la conjecture

La proposition est une **synthèse** qui raccorde quatre programmes de recherche
réels et largement indépendants :

1. **Cosmologie cyclique conforme (CCC)** de Penrose : le futur lointain d'un
   univers (sans masse, donc « purement conforme ») est identifié au Big Bang de
   l'éon suivant, parce qu'en l'absence de masse seule la structure conforme
   garde un sens opérationnel.
2. **Sphère céleste `S²`** des directions nulles : l'arène de l'*holographie
   céleste*.
3. **Intrication du vide comme « colle » géométrique** : l'idée que la géométrie
   de l'espace-temps émerge des corrélations quantiques (programme « it from
   qubit »).
4. **Holographie** (type AdS/CFT) comme générateur de métrique.

L'intérêt du projet tient à ce regroupement. Sa limite tient à son statut :
c'est une **charpente narrative**, sans action, sans CFT explicite, sans
démonstration qu'un seul des passages fonctionne. Chaque « donc » est une
affirmation, pas une dérivation.

## 2. Ce qui est solide  `[établi]`

- **Identité conforme = champ des cônes nuls.** La structure conforme d'un
  espace-temps lorentzien *est* exactement le champ des cônes de lumière, et
  c'est précisément l'invariant sous `g → Ω²g`. Dire que c'est « le résidu de la
  RG quand l'échelle disparaît » est correct (argument de Penrose).
- **Topologie `S²` des directions nulles.** En un point d'un espace-temps 4D,
  l'espace des directions nulles est topologiquement `S²` (la sphère céleste).
  La définition du fibré `N → M` (texte source §2) est géométriquement saine.

## 3. Ce qui est imprécis ou problématique

Étiquetage par maillon (détails et hypothèses correctives dans
`02_programme-de-recherche.md`).

- **§1 — géométrie vs matière, à dissocier** `[géométrie établi / matière hors de portée]`.
  *Géométrie* : à `Λ > 0`, `𝓘⁺` est de genre **espace** et l'extension conforme y
  est **régulière** (Friedrich 1986) — c'est la **condition favorable** du
  raccordement (raccord spacelike↔spacelike avec un Big Bang), **non** une faiblesse.
  Voir `LC-A-SURVIE-CONFORME` (sceau explicite : `N|_𝓘⁺ = −Λ/3 < 0`, `g̃` non
  dégénérée). *Matière* : la difficulté réelle est ailleurs — (a) rien ne garantit
  que toutes les particules deviennent sans masse (invariance conforme requise au
  crossover) `[hors de portée / spéculatif]` ; (b) unicité du facteur conforme au
  crossover + hypothèse de Weyl `[décision ouverte / à inventer]`. La réintroduction
  d'une échelle par `Λ` (rayon de de Sitter) relève du module `[E]` (retour de
  l'échelle) — et c'est elle qui rend `𝓘⁺` spacelike, donc raccordable.
- **§3 — « cônes incomparables » trop fort** `[à corriger]`. La structure
  conforme conserve une connexion (géométrie de Weyl / Cartan), et les
  géodésiques nulles restent définies comme courbes non paramétrées : la lumière
  se propage encore sans ambiguïté.
- **§4 — « l'intrication ne dépend pas de la métrique » faux tel quel**
  `[à reformuler]`. L'entropie d'intrication suit une loi d'aire
  (`S ~ Aire/ε²`), donc métrique-dépendante et divergente dans l'UV. Pire :
  calculer des aires présuppose la métrique — circularité avec « faire émerger la
  métrique de l'intrication ».
- **§5 — deux erreurs** `[à corriger]`. (i) « La MQ devient une CFT quand la
  masse disparaît » : seules certaines théories sont conformes sans masse
  (Maxwell 4D, scalaire à couplage conforme) ; la QCD sans masse n'est conforme
  qu'au niveau classique (anomalie de trace, `Λ_QCD`). (ii) Comptage de
  dimensions faux : en AdS/CFT une CFT en dimension `d` est duale à une gravité
  en `d+1` ; une CFT sur `S²` (2D) donnerait une gravité 3D, pas 4D.
- **§7 — « unification » = slogan** `[hors de portée]`. Ambiguïté entre
  *conforme-IR* (structure survivante à grande échelle) et *conforme-UV* (point
  fixe régularisant la gravité quantique) ; les pathologies de la gravité
  quantique vivent dans l'UV, pas dans la limite IR décrite. Les approches
  conformes UV (gravité de Weyl) ont leurs propres maux (fantômes / instabilité
  d'Ostrogradski).

## 4. Reformulations clés portées par le projet

Deux déplacements conceptuels orientent tout le programme :

1. **Le résidu géométrique n'est pas la simple classe conforme** mais une
   **géométrie de Cartan conforme** (calcul tracteur), qui rétablit une
   comparaison globale des fibres `S²` — donc « cônes incomparables » est à
   abandonner (module B).
2. **La « colle » quantique n'est pas l'entropie d'intrication** (métrique-
   dépendante) mais la **structure modulaire algébrique du vide**
   (Tomita–Takesaki ; type des algèbres de von Neumann locales), qui est
   intrinsèquement indépendante de la métrique (module C). C'est la reformulation
   la plus originale et la plus fragile du projet.

## 5. Ce que le projet doit fournir pour exister comme proposition

Minimalement : (i) une action / CFT concrète sur `S²` ; (ii) un mécanisme
explicite reliant la structure quantique du vide à la sélection d'une
hypersurface `Σ ≃ S³` ; (iii) un comptage holographique cohérent (trancher
AdS/CFT *vs* holographie céleste) ; (iv) un traitement de `Λ` et de la signature
de `𝓘⁺` ; (v) un argument réel sur la domestication des divergences UV.
