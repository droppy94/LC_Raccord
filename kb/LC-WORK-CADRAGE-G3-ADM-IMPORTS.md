---
id: LC-WORK-CADRAGE-G3-ADM-IMPORTS
codename: LC-RACCORD
titre: "Cadrage gelé R-36 — CONSOLIDATION des imports contingents {I1, I5, I3, I4} du verdict LC-D-G3-ADMISSIBILITE v1.4 (T-c-conditionnel). Fige AVANT toute algèbre/fetch : CI-1 = dérivation INTERNE des racines indicielles {0,3} de l'opérateur d'Einstein FG-jaugé spin-2 TT en d=3 (durcit I1 Δ₋=0 + I5 Δ₊=3 ; sceau verif_G3_adm_imports.py ARMÉ conditionnel) ; CI-2 = positionnement de grade de la source 2605.03481 (v2/publication, R-41) ; CI-3/CI-4 = audits de concordance import↔source KB-only (I3 transmission⟹mono-bord ; I4 DELTA-C T2b). PORTÉE HONNÊTE PRÉ-DÉCLARÉE : l'algèbre indicielle est sign(Λ)-symétrique ⟹ NE teste PAS le pas genuine-dS (m4 du chaînon RESTE vacant) ; le bien-posé genuine-dS (lissité 𝓘⁺, g₍₃₎ libre) RESTE un import (Leimbacher). Une consolidation DURCIT le T-c-conditionnel SANS le convertir en verrou propre. Espace de verdicts FIGÉ : CONSOLIDÉ-partiel / NÉGATIF (⟹ R-53 réouverture du chaînon + audit froid OBLIGATOIRE) / INDÉTERMINÉ. SANS SURCLASSEMENT (§6.4) : consolider des imports ne réduit RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
type: "cadrage gelé R-36 (work-active) — arme la consolidation (D) du fork V42 §4. NE scelle rien, NE vote pas. Gel sha256 consigné HORS-FICHIER au manifeste au dépôt."
statut: "work-active — GELÉ au dépôt (R-36), NON consommé. Sceau CI-1 conditionnel : son dépôt incrémente .py 75→76 ⟹ §0-full au lot de dépôt."
version: 1.0
langue: fr
date: 2026-07-04
maj: "2026-07-04 — v1.0 : création sur GO Thierry (fork V42 §4 voie (D)). Rédigé APRÈS §0-lite PASS (PKG-SHA v2.34 8692c344 reproduit byte-exact) et APRÈS veilles (C) négatives du 2026-07-04 (non gravées, fenêtre sub-journalière). AUCUNE algèbre exécutée, AUCUN fetch engagé avant ce gel."
prerequis_kb: [LC-D-G3-ADMISSIBILITE, LC-D-O2-SCATTERING-FG, LC-D-O2-DELTA-C, LC-D-G3-TRANSPORT, LC-D-GAMMA-NSTAR-ADS4]
tags: [cadrage, gel-R36, anti-fit, R-7, consolidation-imports, I1, I5, I3, I4, G3-admissibilite, T-c-conditionnel, racines-indicielles, FG, spin-2-TT, Delta-0-3, SFG-1, DELTA-C-T2b, transmission-mono-bord, Leimbacher, sceau-conditionnel, R-53, §6.4]
---

# Cadrage gelé — consolidation des imports `{I1, I5, I3, I4}` de `G3-ADMISSIBILITE`

> **Objet.** Le verdict `LC-D-G3-ADMISSIBILITE` v1.4 (DÉLIMITATION RENFORCÉE / `T-c`-conditionnel) est
> **contingent** aux quatre imports `{I1, I5, I3, I4}` (chaînon §4). Ce cadrage fige les cibles de
> consolidation **AVANT** toute algèbre et tout fetch. Faible enjeu de réduction ; l'enjeu est de
> **durcir** le conditionnel (réduire la surface d'import) et de **tester la concordance** des imports
> avec ce que leurs chaînons sources établissent réellement.

## 0. État des imports au gel `[constat, non adjugé]`

- **`I1`** (`Δ₋=0`, **charnière**) : SFG-1 ← Leimbacher `2605.03481` Thm 1.2, racines indicielles
  `{0,2,3,n,n+1}`, extrêmes `{0,3}` pour `n=3`. Grade : **identité-vérifiée**, préprint v1 non publié.
  Corroboré « en direction » par Phase 1 (`74be5932` : théorème dS-genuine dédié ABSENT des lignées AdS).
- **`I5`** (`Δ₊=3`) : même provenance + étalon AdS₄ `NA-1` (`LC-D-GAMMA-NSTAR-ADS4`). Déclaré à l'audit
  mandataire, **omis du sceau** `010a0562`.
- **`I3`** (transmission ⟹ mono-bord) : structurel KB (jonction D↔N, `COIN-TRANSMISSION`/`JONCTION` ;
  cellule `R1″` de `G3-TRANSPORT` v0.4). **Jamais isolé comme énoncé propre.**
- **`I4`** (`DELTA-C` T2b) : rupture de la carte shadow `Δ↔d−Δ` au pas marginal quand la renormalisation
  est requise. Établi comme **lecture-extraction**, périmètre **scalaire/mono-bord** (Skenderis), sans sceau.

## 1. Cibles figées `[AVANT algèbre/fetch]`

### `CI-1` — dérivation interne des racines indicielles (durcit `I1` + `I5`) `[PORTANTE]`

Dériver en SymPy exact, depuis l'équation du mode spin-2 TT de l'opérateur d'Einstein linéarisé en jauge
FG (métrique `ds² = ℓ²/z² (dz² + g_ij(z,x) dx^i dx^j)`, `g_ij = g₍₀₎ + z g₍₁₎ + …`), **l'équation
indicielle** du comportement de bord `h ~ z^Δ` et ses racines pour `d=3` (dimension de bord).

- **Attendu figé** : racines `{Δ₋, Δ₊} = {0, d} = {0, 3}` pour le secteur métrique TT.
- **Sceau conditionnel** `verif_G3_adm_imports.py` : ARMÉ si et seulement si la dérivation aboutit
  (asserts = équation indicielle dérivée de la métrique, racines exactes, témoins m1/m2 ci-dessous).
- **Portée honnête PRÉ-DÉCLARÉE** : l'équation indicielle est **sign(Λ)-symétrique** (elle ne dépend que
  de la structure FG locale, pas du signe de la courbure) ⟹ cette cible **NE teste PAS** le pas
  genuine-dS. Le `m4` du chaînon **RESTE vacant**. Le bien-posé genuine-dS lorentzien (lissité de `s²g` à
  `𝓘⁺`, `g₍₃₎` TT libre, correspondance de scattering) **RESTE un import** porté par Leimbacher.
- **Effet si positif** : `I1`/`I5` passent d'« import en bloc » à « **algèbre interne** (racines) +
  **import résiduel réduit** (bien-posé genuine-dS) ». Le sceau `010a0562` reste inchangé ; la déclaration
  `I5` omise-du-sceau est **acquittée** par le sceau neuf.

### `CI-2` — positionnement de grade de la source (volet `I1`/`I5`, léger)

Vérifier (R-41, multi-miroirs) si `2605.03481` a : (i) une **v2+** ; (ii) une **publication** en revue ;
(iii) des erratums touchant Thm 1.2. **Positionnement d'identité seul** — toute consommation de contenu
NEUF (delta v1→v2 substantiel) = **amendement R-7 daté** préalable. Option (décision opérateur) : dépôt
PDF + sha256 ⟹ montée au grade **sha256-consigné**.

### `CI-3` — concordance `I3` (transmission ⟹ mono-bord) `[KB-only]`

Localiser l'énoncé source **exact** dans les chaînons (`JONCTION` Legendre D↔N ; `COIN-TRANSMISSION` ;
`G3-TRANSPORT` `R1″`) et confronter à l'usage fait par `G3-ADMISSIBILITE` (réduction de la question de
normalisabilité deux-faces à une analyse mono-bord à `𝓘⁺`). Question figée : **l'import consommé
est-il ⊆ ce que la source établit ?** (ni plus, ni extrapolation silencieuse).

### `CI-4` — concordance `I4` (`DELTA-C` T2b) `[KB-only]`

Même question figée pour T2b : l'usage par `G3-ADMISSIBILITE` respecte-t-il le périmètre déclaré
**scalaire/mono-bord** de l'extraction (T2c : deux-bords/graviton « non traités, extrapolation
structurelle ») ? Consigner explicitement toute marche d'extrapolation restante comme **partie de
l'import**, pas comme acquis.

## 2. Firewall `CI-R` `[mutations figées]`

- **`m1` — témoin scalaire.** La même dérivation appliquée au scalaire massif doit redonner la relation
  standard `Δ(Δ−d) = m²ℓ²` (racines `{0,d}` au cas sans masse). Échec ⟹ dérivation cassée.
- **`m2` — dimension générique.** En `d` symbolique, le secteur TT doit donner `{0,d}` ; la
  spécialisation `d=3` doit être la SEULE étape qui produit `{0,3}`. Échec ⟹ fit caché sur `d=3`.
- **`m3` — anti-circularité `A4`.** Aucune invocation du postulat de Weyl ni d'aucun élément de `{A4 ;
  A2★ ; N}` dans la dérivation ni dans les audits de concordance.
- **`m4` — déclaration de non-portée.** Le chaînon de sortie DOIT porter en clair que l'algèbre
  indicielle est sign-symétrique et que genuine-dS reste import. Toute formulation laissant entendre que
  `m4`-chaînon est comblé = violation de cadrage.

## 3. Espace de verdicts `[FIGÉ]`

- **CONSOLIDÉ-partiel** : `CI-1` racines `{0,3}` dérivées + sceau EXIT 0 + `m1`/`m2` mordent, ET
  `CI-3`/`CI-4` concordants ⟹ `I1`/`I5` réduits à l'import résiduel bien-posé ; `I3`/`I4` documentés
  concordants. Le `T-c`-conditionnel est **durci**, PAS converti (ni verrou propre, ni `T-a`).
- **NÉGATIF** (l'un des cas) : racines ≠ `{0,3}` ; OU discordance `CI-3`/`CI-4` (l'import consommé
  excède la source) ⟹ **déclencheur R-53** : révision de `LC-D-G3-ADMISSIBILITE` + **audit froid
  OBLIGATOIRE** avant toute propagation.
- **INDÉTERMINÉ** : dérivation non aboutie ou concordance non décidable KB-only ⟹ consigner, aucun
  statut ne bouge.

## 4. Phases `[ordre figé]`

- **Phase 0 — KB-only** : `CI-3` + `CI-4` (lecture de concordance, aucun fetch), puis `CI-1` (algèbre +
  sceau). Aucun amendement R-7 requis.
- **Phase 1 — positionnement `CI-2`** : fetch d'identité R-41 seul (v2/publication). Consommation de
  contenu neuf = amendement R-7 daté préalable. HOLD par défaut au-delà de l'identité.

## 5. Relation `R-53` & effets

- Ce cadrage **teste** les imports du verdict v1.4 ; il ne le rouvre pas par décret. Verdict
  CONSOLIDÉ-partiel ⟹ couche additive sur le chaînon (déclaration d'imports durcis), `G3-TRANSPORT`
  **RESTE `T-b`** (aucun verrou propre ne peut naître ici — la cible ne touche ni `R1″` ni `R2″` ni
  `R4″`).
- Dépôt du sceau `CI-1` ⟹ `.py` 75→76 ⟹ **§0-full** au lot de dépôt (cadence §9bis).

## 6. Non-surclassement `(§6.4)` `[terminal]`

Consolider des imports / auditer une concordance / positionner un grade de source = **aucune réduction**.
`{A4 ; A2★ ; N}` INCHANGÉ ; `D1` non clos ; `N` non fixé (≡Λ) ; `A4` non réduit ; `A2★` non tranché ;
`O₂` non construit ; `β` reste `T-b` ; CCC **non démontrée NI réfutée**.
