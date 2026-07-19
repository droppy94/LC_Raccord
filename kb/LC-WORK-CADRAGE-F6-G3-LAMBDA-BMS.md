---
id: LC-WORK-CADRAGE-F6-G3-LAMBDA-BMS
titre: "Cadrage d'EXÉCUTION du volet F6-G3 (branche FALSIFIABILITÉ rang 6 — obstruction Λ>0 / flux-balance Λ-BMS à scri spacelike). NE RE-GÈLE PAS les cibles : celles-ci sont déjà figées par LC-WORK-CADRAGE-F6-BMS-MEMOIRE v0.1, daté 2026-06-15 AVANT toute source (anti-fit acquis). Ce fichier fige la GRILLE D'EXÉCUTION de G3 : la question opérationnelle, la grille tripartite G3-a/b/c, les K-checks internes, les forks S-G3-1..4, la décision de fetch (HOLD primaire), le livrable (chaînon de délimitation + sceau structurel optionnel). Acquis amont NON rejugé : G1 (Δσ_ij = Hessien électrique pair, secteur g₃) + G2 (Q[f] linéaire en g₃ = secteur C_T), niveau représentation+dictionnaire, INDÉPENDANT du flux-balance détaillé (LC-D-F6-BMS-MEMOIRE v0.1, scellé). Issue honnête attendue = DÉLIMITATION (gap nommé), pré-déclarée au cadrage F6 §2 ; ZÉRO réduction du compte. Lead racine commune : la fermeture du secteur C_T est suspendue à O₂ (4 obstructions F5). SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé (≡ Λ, hors de portée) ; CCC non démontrée. ACTIVE."
codename: LC-RACCORD
tags: [cadrage, execution, paper-first, falsifiabilite, F6, G3, BMS, Lambda-BMS, flux-balance, scri-spacelike, dS, memoire-gravitationnelle, triangle-IR, supertranslation, saut-entre-vides, temps-retarde, news, garde-fou-CT, O2, racine-commune, delimitation, fetch-hold, anti-fit, gel, §6.4, A2star, N, ACTIVE]
type: "cadrage d'exécution — fige la grille G3 (question, grille tripartite, K-checks, forks, fetch, livrable) AVANT toute algèbre et tout fetch G3. Aucun résultat, aucune dérivation à ce stade."
statut: work-active
version: 0.1
langue: fr
maj: "2026-06-16 — v0.1 : création du cadrage d'EXÉCUTION de F6-G3 (Λ-BMS / flux-balance dS). NE re-gèle PAS les cibles (déjà figées par LC-WORK-CADRAGE-F6-BMS-MEMOIRE v0.1, anti-fit acquis, source non consommée). Fige la grille tripartite G3-a (bonne-définition du saut entre vides à scri spacelike) / G3-b (transport de la loi de flux-balance, lead O₂) / G3-c (imprint CCC vs mémoire GR standard), les K-checks internes (K-a parité E/B + Hessien G1 ; K-b garde-fou C̃_T=+C_T + 4 obstructions F5→O₂ ; K-c BD dS +i + ⟨g₃g₃⟩∝k³), les forks S-G3-1 (KB-local, fetch HOLD — PRIMAIRE) / S-G3-2 (fetch conditionnel pré-autorisé, repli, tracé gel→fetch, R-7) / S-G3-3 (sceau structurel optionnel, réversible) / S-G3-4 (audit froid différé). Ordre anti-fit : ce fichier daté 2026-06-16 PRÉCÈDE toute consommation de source G3 ; fetch HOLD primaire préserve l'ordre trivialement. Aucune algèbre, aucun fetch, aucun sceau à ce stade. SANS SURCLASSEMENT (§6.4) : issue attendue = délimitation ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
---

# Cadrage d'exécution F6-G3 — obstruction Λ>0 / flux-balance Λ-BMS (paper-first)

> **Statut : GEL ANTI-FIT (grille d'exécution).** Ce fichier fige la **grille** de G3 **avant**
> toute algèbre et tout fetch G3. Il **ne re-gèle pas** les cibles : F6-G1..G4 sont déjà figées par
> `LC-WORK-CADRAGE-F6-BMS-MEMOIRE` v0.1 (anti-fit acquis, source non consommée). Toute réduction
> *postérieure* de la grille exige un **amendement R-7 daté**, jamais une réinterprétation silencieuse.

## 0. Contexte et ancrage

Volet **G3** du front **F6** (branche FALSIFIABILITÉ rang 6). Les sous-objectifs **G1/G2 sont
SCELLÉS** (`LC-D-F6-BMS-MEMOIRE` v0.1 ; `verif_F6_memoire_cisaillement.py` EXIT 0/18, firewall 3) au
**niveau représentation + dictionnaire**, explicitement **indépendant du flux-balance détaillé**.
**G3 est resté `décision ouverte`, différé / fetch-conditionnel.** Ce cadrage l'arme.

**Acquis amont — NON rejugé ici :**
- **G1** : `Δσ_ij = -2(D_iD_j - (1/d) g₀_ij D²) C` = **Hessien** (symétrique, sans trace, **parité
  paire**), secteur électrique de `g₃` ; disjoint du magnétique `B = Cotton[g₀]` (pseudo-tenseur,
  impair). La mémoire **n'ajoute aucun datum libre** au-delà de `{cisaillement / g₀ / g₃}`.
- **G2** : `Q[f]` = fonctionnelle **linéaire** de `g₃` = secteur `C_T` (`⟨T⟩=(d/16πG)g₃`, `d=3`).
  **Consolidation**, pas de route neuve.
- **Socle dS interne** : garde-fou `C̃_T = +C_T` (`LC-D-CT-DUAL-DS`) ; prescription BD dS `+i`
  (`i^{d-1}` source du signe, S2) ; carte `S²=−𝟙` ; arbre des **4 obstructions F5 ⟹ racine `O₂`**
  (`LC-D-F5-ETAT-RACCORD`) ; `⟨g₃g₃⟩ ∝ k³ ≠ 0` (`Δ=3`, irréductible).

**Le point dur (rappel F6).** Le triangle IR canonique (Strominger : théorèmes mous ⟺ symétrie
asymptotique ⟺ mémoire) est bâti à `𝓘` **nul, Λ=0**. Le `𝓘⁺` du programme (≡ crossover `𝒞`) est
**dS / spacelike (Λ>0)** : le groupe et la mémoire pertinents sont la version **Λ-BMS** (non
standard, débattue). C'est là que vit le « volet à bâtir » de la fiche F6.

## 1. Question opérationnelle G3 (la cible est figée ; ceci est sa mise en œuvre)

À `𝓘⁺` **dS / spacelike**, la **loi de flux-balance** Λ=0 — qui donne au « saut net entre vides »
`Δσ` son sens **dynamique** (variation nette à travers une histoire radiative) — :

- **(réduction)** transporte-t-elle proprement, refermant `Δσ ↔ aspect de masse / flux` **sans
  paramètre neuf** ? — ou
- **(délimitation)** bute-t-elle sur un **gap structurel nommable** (absence de feuilletage en temps
  retardé ⟹ pas de coupe vide-passé/vide-futur ; Λ-BMS non standard ; fermeture `C_T` suspendue à
  `O₂`) ? — ou
- **(positif, anti-fit-protégé)** laisse-t-elle un **imprint CCC-spécifique** dérivable à l'ordre
  perturbatif ?

## 2. Grille tripartite gelée — G3-a / G3-b / G3-c

> La grille encode l'**attente honnête** (délimitation). Chaque branche déclare le **critère de
> bascule** réduction ↔ délimitation ↔ positif, et l'**attendu pré-déclaré**.

- **G3-a — bonne-définition du « saut entre vides » à scri spacelike.**
  *Critère :* existe-t-il un analogue Λ>0 du feuilletage en **temps retardé `u`** (avec coupes
  `u→±∞`) entre lesquelles `Δσ` est une variation **dynamique nette** — ou `Δσ` reste-t-il une
  identité **cinématique / de représentation** (Goldstone Hessien de G1) sans contenu de flux ?
  *Attendu :* **pas d'analogue propre** en dS spacelike ⟹ `Δσ` bien défini comme **objet de
  représentation** (G1, intact) mais **pas** comme saut dynamique ⟹ **gap**.

- **G3-b — transport de la loi de flux-balance (Λ-BMS).**
  *Critère :* la loi Λ=0 `ΔQ[f] = flux mou + flux dur` se referme-t-elle **en interne** en dS — ou
  sa fermeture **coïncide-t-elle avec / pointe-t-elle vers `O₂`** (secteur `C_T` non refermé, 4
  obstructions F5) ?
  *Attendu :* **fermeture suspendue à `O₂`** ⟹ le gap G3-b **est** le nœud `O₂` déjà identifié ⟹
  **pas de route neuve, pas de réduction** (le compte ne bouge pas ; `O₂` déjà au périmètre).

- **G3-c — imprint CCC-spécifique vs mémoire GR standard.**
  *Critère :* une déviation CCC est-elle **dérivable à l'ordre Einstein/perturbatif** — ou le
  programme prédit-il la **mémoire GR standard** (la seule « signature » concevable étant l'écart
  `Λ>0` / l'imprint de crossover, **non** une prédiction nette perturbative) ?
  *Attendu :* **mémoire GR standard** ⟹ **cohérence** (style F2 / D1c, « non exclu »), **pas** un
  positif (recouvre G4). `inconfrontable` tant qu'aucune signature CCC propre n'est dérivée.

## 3. K-checks internes (ce qui pince chaque branche, KB-local)

- **K-a (pince G3-a)** : disjonction de parité `E`/`B` + caractère **Hessien** de `Δσ` (G1, scellé)
  ⟹ le saut est **purement électrique / Goldstone** = un fait de **représentation**, **niveau-
  indépendant du flux-balance** (déjà acté §5 de `LC-D-F6-BMS-MEMOIRE`).
- **K-b (pince G3-b)** : garde-fou `C̃_T=+C_T` (`LC-D-CT-DUAL-DS`) + **4 obstructions F5 → `O₂`**
  (`LC-D-F5-ETAT-RACCORD`) ⟹ la fermeture **dynamique** du secteur de charge molle (`C_T`) est le
  **nœud `O₂`**, déjà au périmètre `à inventer`.
- **K-c (pince G3-c)** : prescription BD dS `+i` (`i^{d-1}`) + `⟨g₃g₃⟩ ∝ k³ ≠ 0` (`Δ=3`) ⟹ à
  l'ordre perturbatif, **mémoire GR standard** (aucune déviation CCC dérivable proprement).

## 4. Forks / scopings — S-G3-1..4

- **S-G3-1 — KB-local, fetch HOLD (PRIMAIRE).** Nommer le gap depuis la **machinerie dS interne**
  (K-a/K-b/K-c). Posture F4 : la circularité/obstruction est **pinçable en interne** ; un functional
  réglant la fermeture dynamique en dS spacelike est inaccessible sans `O₂`.
- **S-G3-2 — fetch conditionnel pré-autorisé (REPLI).** **Seulement si** la nomination KB-local
  n'atteint pas une délimitation honnête : Strominger `1703.05448` (triangle IR) ; **Λ-BMS** Compère
  et al. ; mémoire Christodoulou / Thorne. Tracé **gel→fetch** (ce fichier daté **avant** toute
  source) ; cibles **non amendées** sauf **R-7**. *Note : ces réfs ne sont pas en KB ⟹ le fetch
  **corrobore** la littérature « Λ-BMS débattue » mais le **verdict délimitation est robuste sans**.*
- **S-G3-3 — sceau structurel OPTIONNEL.** Style F4 : firewall **réel** sur (i) la disjonction de
  parité `Δσ` électrique vs magnétique, (ii) la **dégénérescence** du saut dynamique quand le
  feuilletage retardé est retiré (scri spacelike). **Réversible**, **sans cible numérique externe**.
  Décision d'armement au moment du livrable.
- **S-G3-4 — audit froid différé / réversible** (cohérent F6 S-F6-4). Sans coût sur le présent volet.

## 5. Plan d'exécution (un fichier à la fois, GO explicites)

1. **(ce fichier)** gel de la grille G3 — *en validation.*
2. **Nomination KB-local (S-G3-1).** Dérouler K-a/K-b/K-c ; **nommer** le gap (G3-a non-défini
   dynamiquement ; G3-b = nœud `O₂` ; G3-c = mémoire GR standard). **Chaînon-verdict de
   délimitation** `LC-D-F6-G3-LAMBDA-BMS`. Sceau structurel **optionnel** (S-G3-3).
3. **Repli S-G3-2 uniquement si nécessaire** (GO séparé, tracé gel→fetch).
4. **Bilan F6 (G1/G2 scellé + G3 délimité)** + propagation (lot additif transverse) sur GO séparé.

À chaque étape : `count==1` avant tout `str_replace`, YAML revalidé (frontmatter `yaml.safe_load`),
deltas additifs contrôlés (suppr. ⊆ `{version, maj, statut}`), sceaux EXIT 0 (contenu vérifié)
avant dépôt ; bâtir sur les versions déposées.

## 6. Garde-fous / sans surclassement (§6.4)

- G3 est **exploratoire** : issue honnête attendue = **délimitation** (gap nommé). **Aucune** issue
  ne réduit le compte `{A4 ; A2★ ; N}`. « gap nommé / pointé vers `O₂` » ≠ « `O₂` construit / `C_T`
  refermé / signature CCC établie / CCC démontrée ».
- `N ≡ Λ` reste **explicitement hors de portée** (rappel fiche F6) : aucun effort n'y sera dépensé ;
  G3 **n'attaque pas** `N`, il **délimite** la mémoire/flux-balance en dS.
- **Anti-fit** : la grille (§2) encode l'attente **pré-déclarée** au cadrage F6 §2 (« GAP NOMMÉ ») ;
  ce fichier **précède** toute source G3 ; fetch HOLD primaire rend l'ordre trivial. Un imprint CCC
  surgissant **malgré** ce gel serait un positif réellement protégé — non attendu.
