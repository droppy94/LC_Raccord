---
id: LC-WORK-CADRAGE-NONLIN-2PT
titre: "Note de travail (cadrage paper-first) — OUVRE le front « généralisation NON-LINÉAIRE du DEUX-POINT de A3 » (reco §3.1 de LC-WORK-REPRISE-POST-PROPAGATION-NONGAUSS, tranchée par Thierry le 2026-06-12). Analogue RANG 2 du triptyque LC-D-NONLIN-VERROU : remplacer la relation d'état BD (perturbative, mode par mode) par un argument d'INVARIANCE (représentation, non-perturbatif) pour le deux-point du secteur de Weyl rescalé COMPLET (E⊕B, DEUX parités). Question : sous A3 + Ward exactes (d=3 impair, pas d'anomalie), la forme k³·Π^TT du deux-point est-elle FORCÉE, avec pour unique liberté résiduelle UNE amplitude (celle déjà pendue à N via C_T) ? Quatre décisions de scoping TRANCHÉES (2026-06-12) : (i) périmètre deux-point seulement, quatre-point/boucles HORS périmètre ; (ii) secteur impair ⟨EB⟩ INCLUS ; (iii) sceau UNIQUE à blocs, phase 1 interne EXIT 0 AVANT tout fetch (modèle NONGAUSS) ; (iv) comparanda KB d'abord (OP 9307010, de Haro 0808.2054), fetch web SEULEMENT si l'impair-contact l'exige, flagué. CIBLES GELÉES ICI (R-7 active dès ce gel : toute décision de scoping réductrice postérieure exige un amendement formel daté du présent libellé) : C1 dim(structures paires invariantes)=1, forme k³Π^TT forcée ; C2 dim(impair)=1 ET contact/local — sinon ÉCHEC ; C3 refermeture BD : ⟨EE⟩,⟨BB⟩,⟨EB⟩ ∝k³, ratios fixés sans paramètre neuf, recoupement carte S (S²=−1) ; C4 catalogue {2,4,8} actif. Firewall : Δ≠3, d pair, admixture trace/hélicité-0, n≠2 doivent CASSER. Garde-fou : issue maximale = « forme verrouillée, liberté résiduelle = 1 amplitude pendue à N » — JAMAIS « A3 dérivé », JAMAIS « deux-point dérivé ». Subordonnée à LC-AUDIT-VERDICT §6.4. Compte {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
codename: LC-RACCORD
type: "note de travail (cadrage paper-first) — ouvre le front non-linéaire du deux-point (rang 2). N'EST PAS un chaînon : aucune algèbre scellée, aucun sceau, AUCUN fetch ici. Subordonnée à LC-AUDIT-VERDICT §6.4. Successeur direct de LC-WORK-REPRISE-POST-PROPAGATION-NONGAUSS §3.1/§4."
version: 0.1
langue: fr
date: 2026-06-12
maj: "2026-06-12 — v0.1 : cadrage paper-first du front §3.1 (généralisation non-linéaire du deux-point de A3). Quatre décisions de scoping tranchées par Thierry (périmètre confirmé ; impair ⟨EB⟩ inclus ; sceau unique à blocs avec phase 1 interne EXIT 0 avant fetch ; comparanda KB d'abord). Objet dérivé sur papier (trois sub-questions sub-R1/R2/R3, miroir du triptyque rang 1), carte de conventions figée (réutilisation des maps SCELLÉES γ=4/κ=24/π²/i^p — aucune map neuve attendue), cibles C1-C4 GELÉES avec firewall, R-7 portée dès le gel, plan de sceau verif_nonlin_deuxpoint.py (6 blocs A-F, deux phases), critère d'échec recevable. AUCUN dépôt, AUCUN fetch, AUCUNE touche KB ici."
statut: "CADRAGE — à valider par Thierry AVANT toute exécution. R-7 ACTIVE dès la validation (gel des cibles §3). Aucun fetch (y compris lecture des PDF KB OP/de Haro) tant que la phase 1 du sceau n'est pas écrite et EXIT 0. Périmètre {A4 ; A2★ ; N} inchangé ; D1 non clos ; CCC non démontrée."
prerequis_kb: [LC-D-NONLIN-VERROU, LC-D3-SPECTRE-K3, LC-D-CT-DUAL, LC-D-CT-ATN, LC-D-CT-GAMMA, LC-D-HOLOGRAPHIE-G3, LC-D3-WEYL-BUNCHDAVIES, LC-WORK-D1-E-AMPLITUDE, LC-D-NONGAUSS-TTT, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: [verif_nonlin_repr.py, verif_nonlin_cotton.py, verif_nonlin_parity.py, verif_D3_spectre_k3.py, verif_D_CT_dual.py, verif_naction_gamma_dHSS.py]
tags_epistemiques: [établi (algèbre), formalisable, à inventer, hors de portée, décision ouverte]
---

# Cadrage — verrou NON-LINÉAIRE du DEUX-POINT (rang 2) ; cibles gelées, R-7 active

> **Pour validation AVANT exécution.** Cette note exécute le premier geste du front §3.1 :
> objet dérivé sur papier, conventions figées (toutes **déjà scellées** — aucune map neuve),
> cibles **gelées** C1-C4, protocole anti-fit, plan de sceau. **Aucun fetch n'a été fait**
> pour la produire — y compris : les PDF en KB (OP, de Haro) n'ont **pas** été rouverts ;
> tout ce qui suit est algèbre interne au programme (chaînons scellés) ou structure générale
> connue sans consultation. Discipline `LC-AUDIT-VERDICT §6.4` portée tout du long.
> **R-7** (règle de méthode permanente, `VERDICT v1.29 §8bis`) : dès la validation de cette
> note, toute décision de scoping **réductrice** postérieure au gel §3 exige un **amendement
> formel, daté et tracé**, du libellé gelé, **au moment de la décision**.

---

## 0. Rôle, périmètre, décisions de scoping `[TRANCHÉES — Thierry, 2026-06-12]`

**Ce que ce front vise.** Le triptyque `LC-D-NONLIN-VERROU` a porté le **un-point** du Weyl
rescalé complet (`E⊕B`, deux parités) de `établi perturbatif` à `établi` non-perturbatif,
par représentation (Ward exactes ⟹ pur spin-2 ⟹ `spin-2 ∩ invariants = {0}`). Le
**deux-point** `⟨g₃g₃⟩∝k³` n'est, lui, établi qu'au niveau **perturbatif TT**
(`LC-D3-SPECTRE-K3`, via la relation d'état BD `g₃=-(i/3)k³g₀`, déterministe par mode).
Ce front est l'**analogue rang 2** : remplacer la relation d'état (perturbative) par un
argument d'**invariance** (non-perturbatif) — montrer que sous A3 + Ward exactes, la
**forme** `k³·Π^TT` du deux-point complet est **forcée**, l'unique liberté résiduelle étant
**une amplitude** (celle déjà pendue à `N` : `C_T∝N`, `A_T·N=16`).

**Décisions de scoping — TRANCHÉES (2026-06-12), consignées :**

- **(S1) Périmètre : deux-point seulement.** Quatre-point, boucles, secteur non-gaussien
  au-delà du passage léger : **HORS périmètre** (héritage S1 de NONGAUSS, inchangé). Le
  passage lourd du trois-point reste le front §3.2, séparé.
- **(S2) Secteur impair `⟨EB⟩` : INCLUS.** C'est la condition du « complet » — le rang 1
  couvrait les deux parités ; le rang 2 doit faire de même. Pré-attendu (gelé en C2) :
  l'impair est de type **contact/local** en `d=3`, cohérent avec « forme impaire hors
  bispectre » du rang 3 (`NONGAUSS [D]`). Si l'impair s'avère **radiatif** (non-contact),
  c'est un ÉCHEC du verrou, consigné tel quel.
- **(S3) Format : sceau UNIQUE à blocs**, `verif_nonlin_deuxpoint.py`, avec **phase 1
  interne écrite et EXIT 0 AVANT tout fetch** (modèle NONGAUSS — la frontière de phase est
  matérialisée dans le script). Les trois sub-questions partagent la machinerie SVT du
  triptyque rang 1.
- **(S4) Comparanda : KB d'abord.** Au fetch (phase 2 seulement) : Osborn–Petkou
  hep-th/9307010 (structures conformes du deux-point, `d=3` — PDF en KB) ; de Haro
  0808.2054 (dualité E/B au deux-point — PDF en KB). **Fetch web autorisé UNIQUEMENT si le
  secteur impair-contact l'exige** (référence absente de la KB), **flagué au moment venu**
  — et, R-7 oblige, sans extension du périmètre.

---

## 1. L'objet, dérivé sur papier `[algèbre interne — aucun fetch]`

### 1.1 Ce que le rang 1 donne — et ce qu'il ne donne pas

Le rang 1 verrouille : `g₃` est **pur spin-2 tous ordres** (Ward exactes : sans trace +
conservé, `d=3` impair, pas d'anomalie — `verif_nonlin_repr.py`) ; `B∝Cotton[g₀]`
(pseudo-tenseur, impair) ; `(E,B)=(5,5)=10` épuise le Weyl, disjointement. Au un-point,
`spin-2 ∩ invariants = {0}` suffit : `⟨E⟩=⟨B⟩=0`.

Au **deux-point**, l'intersection n'est plus vide : il **existe** des structures invariantes
à deux indices de paires — c'est précisément `Π^TT` et ses parentes. La question rang 2
n'est donc pas « zéro » mais « **combien** » : quelle est la **dimension** de l'espace des
deux-points invariants compatibles avec les contraintes exactes (spin-2, conservation, sans
trace, `Δ=d=3`) ? Si elle vaut 1 par parité (et que l'impair est contact), la forme est
forcée et toute la liberté tient en **une** amplitude.

### 1.2 Les trois sub-questions `[miroir du triptyque rang 1]`

- **sub-R1 — électrique, paire : la dimension.** Pour un opérateur symétrique, transverse,
  sans trace, de dimension `Δ=3` en `d=3`, l'invariance (rotations + échelle à `𝓘⁺`)
  contraint `⟨EE⟩(k)` à une combinaison de structures tensorielles construites sur
  `{δ_ij, k̂_i}` portées par une puissance globale `k^{2Δ-d}=k³`. La contrainte TT projette
  sur les structures transverses-sans-trace. **Pré-attendu (gelé, C1)** : il en reste
  exactement **une** — `Π^TT(k̂)·k³` — donc une seule amplitude. La dérivation (catalogue
  exhaustif des structures, projection, comptage) appartient au bloc [A] du sceau ; le
  cadrage ne fige que la **cible**.
- **sub-R2 — impaire : `⟨EB⟩` (et la part impaire éventuelle de chaque secteur).** Toute
  structure impaire porte un `ε_{ijk}` (B pseudo-tenseur, sub-Q3 rang 1). En `d=3`, sur un
  deux-point TT, le catalogue des structures `ε`-portées compatibles est à dériver au bloc
  [B]. **Pré-attendu (gelé, C2)** : dimension **1**, et la structure est **analytique en
  `k`** (polynomiale ⟹ contact/local — aucune donnée radiative neuve). Échec recevable :
  une structure impaire **non-analytique** (radiative) existerait ⟹ le « complet » du
  verrou tombe.
- **sub-R3 — refermeture.** Le résultat perturbatif DOIT se retrouver comme **cas
  particulier** : sous la relation d'état BD, `E∝g₃` et `B∝Cotton[g₀]∝k³g₀` (dérivée
  tierce) donnent `⟨EE⟩`, `⟨BB⟩`, `⟨EB⟩` tous `∝k³`, avec des **ratios fixés** par les
  seules définitions (`E_ij=(d/2H)g₃` scellée ; normalisation Cotton dérivée au sceau,
  jamais supposée). Recoupement : la carte `S` de la dualité (`S²=−𝟙`, `CT-DUAL`) échange
  les secteurs — la cohérence des ratios avec `S` est un contrôle interne gratuit.

### 1.3 Ce que « non-linéaire » veut dire ici `[même sens qu'au rang 1]`

Comme au rang 1 : **pas** un calcul de boucles. « Non-linéaire » = l'argument ne repose
**que** sur des identités **exactes, tous ordres** (Ward de `d` impair, théorie des
représentations, parité), jamais sur la linéarisation TT ni sur la relation d'état BD —
celle-ci n'intervient qu'en **refermeture** (sub-R3), comme cas particulier de contrôle.

---

## 2. CARTE DE CONVENTIONS `[FIGÉE — tout est DÉJÀ scellé ; AUCUNE map neuve]`

Particularité de ce front : **aucune map de conventions nouvelle n'est attendue** — le
deux-point est l'objet pour lequel toutes les maps existent déjà, scellées :

- **C2pt-1 — Convention nue par défaut** (programme) : `ψ₂=δ²W`, scellés nus
  `C_T/N=1/(32π²)`, `A_T·N=16`. Map canonique `γ=4` **scellée** (`LC-D-CT-GAMMA`,
  `verif_naction_gamma_dHSS.py`) — se **réutilise**, ne se re-dérive pas.
- **C2pt-2 — Dictionnaire cinématique** : `κ=24/π²` **scellé** (`NACTION-AVEUGLE`) est un
  objet **deux-points** — réutilisable ici si une conversion impulsion↔position s'avérait
  nécessaire. **Pré-déclaration : la phase 1 n'en a PAS besoin** (cibles structurelles, en
  impulsion) ; tout recours ultérieur sera flagué.
- **C2pt-3 — Continuation `ℓ_AdS→iℓ_dS`** : règle `i^p` scellée (`REALITE`) ; pour `C_T~ℓ²`,
  `p=2` — inchangé. Signes portés par la continuation ; **dimensions/structures** = objets
  du test.
- **C2pt-4 — Identifications** : `N=πℓ_dS²/G` ; `d=3` ; `M_Pl²=1/(8πG)` ;
  `E_ij=(d/2H)g₃` (scellée, `verif_D3_bunchdavies.py`) ; `B∝Cotton[g]` (normalisation
  exacte **dérivée au sceau** depuis la définition du Weyl rescalé — c'est la seule
  constante non encore explicite en KB, et elle est **déductive**, pas ajustable).
- **Catalogue {2,4,8}** (NONGAUSS [B]) : actif — tout facteur résiduel pur en puissance
  de 2 dans une comparaison = candidat **mélange de conventions**, à vérifier contre `γ`
  scellé **avant** tout NO-GO.

---

## 3. CIBLES GELÉES `[C1-C4 — R-7 ACTIVE dès la validation de cette note]`

- **C1 (dimension paire — exact, symbolique).** L'espace des structures **paires**
  invariantes du deux-point d'un opérateur TT spin-2, `Δ=d=3`, en `d=3`, est de
  **dimension 1** ; la forme `k³·Π^TT` est **forcée** ; l'unique liberté est l'amplitude
  (déjà cataloguée : `C_T∝N`). Falsification : le catalogue exhaustif en exhibe ≥2.
- **C2 (secteur impair — exact, symbolique).** Dimension **1**, structure `ε`-portée, et
  **contact/local** (analytique en `k`) ⟹ aucune amplitude **radiative** neuve.
  Falsification : structure impaire non-analytique (radiative) ⟹ **ÉCHEC du verrou**,
  consigné sans retrofit.
- **C3 (refermeture BD — exact, slack nul).** Sous la relation d'état BD : `⟨EE⟩`, `⟨BB⟩`,
  `⟨EB⟩` tous `∝k³` ; ratios **fixés par les définitions** (aucun paramètre neuf) ;
  cohérence avec la carte `S` (`S²=−𝟙`). Tout écart pur ∈ {2,4,8} = candidat mélange (C4)
  **avant** verdict ; tout écart résiduel après alignement = NO-GO informatif.
- **C4 (anti-numérologie).** Entrées libres du test strictement moindres que sorties
  appariées ; le catalogue {2,4,8} s'applique à toute comparaison numérique.

**Firewall (gelé).** Les injections suivantes doivent **CASSER** : `Δ≠3` (la puissance
quitte `k³`) ; `d` pair (anomalie de trace ⟹ Ward non exactes ⟹ l'argument spin-2 pur
tombe) ; admixture de trace / hélicité 0 (doit être exclue par `Π^TT`) ; `n≠2` dans
`T=nδW/δg` (⟹ `γ=n²≠4`).

**Ce que les cibles ne sont pas.** C1-C3 sont les **prédictions du programme**, gelées
sans consultation. Le comptage exact des structures conformes du deux-point chez OP, et la
normalisation E/B chez de Haro, sont les **comparanda** de phase 2 — inconnus à ce stade
au sens du protocole (PDF non rouverts pour ce cadrage). Connaître C1-C4 n'autorise
**aucun** ajustement des dérivations de phase 1.

---

## 4. Protocole anti-fit `[transposé NONGAUSS, rodé ; R-7 intégrée]`

- **P1''** : cibles §3 gelées ici, sans fetch (fait).
- **P2''** : dérivations de phase 1 (catalogue pair, catalogue impair, normalisation
  Cotton, refermeture BD) **déductives**, dans des blocs dédiés, **avant** toute lecture
  des comparanda ; chaque dérivation auditable hors contexte.
- **P3''** : identifications C2pt-1→4 **inchangées** (aucune liberté d'identification au
  sceau ; les maps scellées se réutilisent, ne se re-dérivent ni ne s'ajustent).
- **P4''** : fetch (lecture OP/de Haro en KB) en **phase 2 seulement**, après phase 1
  EXIT 0 ; critère gelé, pas de reparamétrage. Fetch web : uniquement selon S4, flagué.
- **P5''** : firewall §3 implémenté et **prouvé discriminant** (les injections cassent).
- **R-7** : toute décision de scoping réductrice post-gel ⟹ amendement formel daté du
  libellé gelé, **au moment de la décision** — pas de régularisation rétroactive.
- **Audit à froid** : si le sceau aboutit, audit en conversation incognito séparée
  (pattern §4.1/AF — l'instance qui scelle ne s'auto-audite pas), sur décision de Thierry.

---

## 5. Plan du sceau `verif_nonlin_deuxpoint.py` `[à écrire APRÈS validation ; DEUX phases]`

**PHASE 1 — interne, écrite et EXIT 0 AVANT tout fetch** (frontière matérialisée dans le
script, pattern NONGAUSS) :

- `[A]` **Catalogue pair + dimension (C1)** : construction exhaustive des structures
  symétriques invariantes sur `{δ, k̂}`, projection TT (machinerie `verif_nonlin_repr.py` :
  `Π^TT(δ)=Π^TT(P)=0`, hélicités ±2), puissance `k^{2Δ-d}` ; comptage ⟹ dim. Symbolique
  (n=ẑ) + numérique multi-directions.
- `[B]` **Catalogue impair (C2)** : structures `ε`-portées sur un deux-point TT en `d=3` ;
  test d'analyticité (contact vs radiatif) ; cohérence de parité (pattern
  `verif_nonlin_parity.py`, réflexion `det R=−1`).
- `[C]` **Refermeture BD interne (C3, partie KB-only)** : `E=(d/2H)g₃`, normalisation
  Cotton dérivée ab initio, relation BD ⟹ `⟨EE⟩`, `⟨BB⟩`, `⟨EB⟩` explicites ; ratios ;
  recoupement `S²=−𝟙` (`verif_D_CT_dual.py` [A]).

--- frontière de phase : EXIT 0 requis ici, AVANT toute lecture de comparandum ---

**PHASE 2 — comparanda (KB d'abord, S4) :**

- `[D]` **Fetch KB** : comptage des structures conformes du deux-point chez OP `d=3` ;
  décomposition E/B et normalisations chez de Haro 0808.2054 ; mise en convention unique
  (nue) via `γ=4` scellé.
- `[E]` **Tests centraux** : C1 (dim=1 confirmée/infirmée contre OP) ; C2 (impair contact)
  ; C3 (ratios, slack nul) ; C4 (anti-numérologie) ; identification explicite de la liberté
  résiduelle (= l'amplitude, pendue à `N`) et de son statut.
- `[F]` **Firewall global + bilan §6.4** (sans surclassement, compte inchangé).

---

## 6. Garde-fous `[discipline §6.4 — portés tout du long]`

- **Issue maximale** : « la **forme** du deux-point complet est verrouillée par
  l'invariance ; la liberté résiduelle de D1 au niveau gaussien = **une** amplitude, pendue
  à `N` » — soit le passage de ce constat (déjà en KB au niveau perturbatif,
  `D1-E-AMPLITUDE`) au **non-perturbatif**. JAMAIS « A3 dérivé », JAMAIS « le deux-point
  est dérivé » : `k³` **reste la donnée de Cauchy irréductible** tant qu'elle n'est pendue
  qu'à `N`.
- **Consolidation ≠ réduction.** Si la dérivation s'avère une réécriture du catalogue
  existant (structures OP), le verdict chute en **consolidation**, consigné tel quel.
- **NO-GO informatif.** Un écart non résorbable par les maps scellées est un **résultat**.
- **Compte inchangé.** `{A4 ; A2★ ; N}` ni réduit ni augmenté par ce front (attendu) ;
  `N` non fixé (circularité `LC-E` intacte) ; D1 non clos ; **CCC non démontrée**.

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. `N≡Λ`).
