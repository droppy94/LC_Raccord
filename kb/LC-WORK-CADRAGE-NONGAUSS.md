---
id: LC-WORK-CADRAGE-NONGAUSS
titre: "Note de travail (cadrage paper-first) — OUVRE le front « secteur non-gaussien de D1 : le trois-point ⟨g₃g₃g₃⟩ » (reco §3.1 de LC-WORK-REPRISE-POST-R1-RELECTURE). Trois livrables, AUCUN fetch ici : (1) OBJET dérivé sur papier — la linéarité de la relation d'état BD g₃=-(i/3)k³g₀ propage la gaussianité : ⟨g₃g₃g₃⟩_libre = (i/27)k₁³k₂³k₃³⟨g₀g₀g₀⟩ = 0 EXACTEMENT sur l'état BD libre ⟹ le trois-point se SCINDE en (i) secteur de contact/Ward (fixé par le deux-point scellé via les identités de Ward de difféomorphisme — aucun contenu neuf) et (ii) secteur dynamique (vertex gravitationnel cubique — le SEUL datum non-gaussien authentique), à comparer à la forme générale CFT₃ de ⟨TTT⟩ (2-3 structures tensorielles, comptage à confirmer au fetch). (2) CARTE DE CONVENTIONS FIGÉE avant tout fetch : convention du programme = NUE (γ=1, ψ₂=δ²W, tous les scellés C_T/N=1/(32π²), A_T·N=16, κ₃=1/(32π) sont nus) ; map opérateur trois-point γ₃ ATTENDUE = 2³ = 8 (triple application de T=2δW/δg, Brown-York) — À DÉRIVER ab initio au sceau, PAS à supposer ; seules les DEUX combinaisons cohérentes (tout-nu / tout-canonique) comptent, tout MÉLANGE = artefact pré-enregistré (leçon R1 généralisée d'avance) ; dictionnaire cinématique impulsion↔position du trois-point à dériver À L'AVEUGLE (pattern NACTION-AVEUGLE ; κ=24/π² scellé NE se réutilise PAS numériquement — objet deux-points — seule la MÉTHODE se transpose) ; continuation ℓ_AdS→iℓ_dS en i^p, p = puissance de ℓ du coefficient, dérivée dimensionnellement AVANT fetch (pattern REALITE). (3) CIBLES PRÉ-ENREGISTRÉES P1' (internes, gelées SANS fetch) : P1'-A ancrage Ward — le secteur Ward de ⟨TTT⟩ doit reproduire |C_T|/N=1/(32π²) (nu) EXACT, slack nul ; P1'-B scaling — amplitude connexe ⟨γγγ⟩ ∝ A_T² = 256/N², ZÉRO paramètre libre neuf ; P1'-C zéro libre — ⟨g₃³⟩_libre=0 identiquement (linéarité FG). Comparaison externe (fetch au sceau seulement, aveugle) : structures Osborn-Petkos ⟨TTT⟩ d=3 + ⟨γγγ⟩ Maldacena / Maldacena-Pimentel. Protocole anti-fit P1'-P5' + tri de provenance + firewall + audit à froid (3ᵉ conversation). Subordonnée à LC-AUDIT-VERDICT §6.4 : un trois-point reproduit = établi (algèbre) d'une cohérence de coefficients, JAMAIS « secteur non-gaussien fermé » ni « D1 fermé ». Compte {A4 ; A2★ ; N} INCHANGÉ ; N non fixé ; CCC non démontrée."
codename: LC-RACCORD
type: "note de travail (cadrage paper-first) — ouvre le front non-gaussien de D1 (trois-point). N'EST PAS un chaînon : aucune algèbre scellée, aucun sceau, AUCUN fetch ici. Subordonnée à LC-AUDIT-VERDICT §6.4. Successeur direct de LC-WORK-REPRISE-POST-R1-RELECTURE §3.1/§4.3."
version: 0.1
langue: fr
date: 2026-06-11
maj: "2026-06-11 — v0.1 : cadrage paper-first du trois-point ⟨g₃g₃g₃⟩ (front §3.1 choisi par Thierry). Objet scindé (contact/Ward vs dynamique), carte de conventions figée AVANT fetch (nue par défaut ; γ₃=8 attendu À DÉRIVER ; dictionnaire cinématique trois-point à dériver à l'aveugle ; continuation i^p dimensionnelle), cibles P1' gelées (Ward-ancrage 1/(32π²) exact ; scaling 256/N² ; zéro libre), protocole anti-fit P1'-P5', plan de sceau verif_D_nongauss_TTT.py (6 blocs A-F), tri de provenance, bascule, garde-fous §6.4. AUCUN dépôt, AUCUN fetch, AUCUNE touche KB ici."
statut: "CADRAGE — à valider par Thierry AVANT toute exécution. Aucun fetch tant que la carte §2 n'est pas validée-figée. Périmètre {A4 ; A2★ ; N} inchangé ; D1 non clos ; CCC non démontrée."
prerequis_kb: [LC-D3-SPECTRE-K3, LC-D-CT-GAMMA, LC-D-CT-ATN, LC-D-CT-REALITE, LC-D-HOLOGRAPHIE-G3, LC-WORK-REPRISE-CONSTRUCTIF-R1, LC-AUDIT-LOG-NACTION-AVEUGLE, LC-D-NONLIN-VERROU, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: [verif_D3_spectre_k3.py, verif_naction_gamma_dHSS.py, verif_naction_aveugle.py, verif_D_CT_constructif.py]
tags_epistemiques: [établi (algèbre), formalisable, à inventer, hors de portée, décision ouverte]
---

# Cadrage — le trois-point `⟨g₃g₃g₃⟩` (secteur non-gaussien de D1) ; carte figée AVANT fetch

> **Pour validation AVANT exécution.** Cette note exécute le premier geste du front §3.1 :
> objet dérivé sur papier, carte de conventions **figée**, cibles **pré-enregistrées** P1',
> protocole anti-fit, plan de sceau. **Aucun fetch n'a été fait** pour la produire : tout ce
> qui suit est algèbre interne au programme (chaînons scellés) ou structure générale connue
> sans consultation. Discipline `LC-AUDIT-VERDICT §6.4` portée tout du long.

---

## 0. Rôle, périmètre, et décisions de scoping `[à trancher à la validation]`

**Ce que ce front vise.** Étendre le contrôle du secteur de D1 du deux-point (scellé,
`LC-D3-SPECTRE-K3` : forme `k³` ; `CT-ATN` : amplitude `A_T·N=16` ; `C_T/N=1/(32π²)`) au
**trois-point**, en consommant le dictionnaire opérateur `γ` verrouillé (`LC-D-CT-GAMMA`).
Critère de succès du programme : montrer que le trois-point **n'introduit aucun paramètre
libre neuf** — qu'il est entièrement pendu à `N` (et aux coefficients d'ordre un fixés par la
structure, pas par nous).

**Décisions de scoping proposées** (flaggées ici, pattern habituel) :

- **(S1) Perturbatif TT seulement.** Niveau arbre, modes TT linéarisés, premier ordre dans
  l'interaction gravitationnelle. La généralisation **non-linéaire** est le front §3.2,
  **séparé** — on ne le mord pas ici (le caveat parent de `WEYL-BUNCHDAVIES §0` reste intact).
- **(S2) Parité paire d'abord.** La structure impaire de `⟨TTT⟩` en `d=3` (type
  Chern-Simons gravitationnel) est **hors périmètre** de ce premier passage
  `[décision ouverte]` — le programme n'a aucun terme impair scellé ; l'introduire serait du
  contenu neuf, pas une réduction.
- **(S3) Cibles de fetch** (au sceau seulement, aveugles) : structures `⟨TTT⟩` CFT₃
  (Osborn–Petkos 1993) côté CFT ; `⟨γγγ⟩` de Bunch–Davies (Maldacena 2003 ;
  Maldacena–Pimentel 2011 pour la lecture dS/CFT) côté dS. Rien d'autre au premier passage.
- **(S4) Nom du sceau** : `verif_D_nongauss_TTT.py`.

---

## 1. L'objet, dérivé sur papier `[algèbre interne — aucun fetch]`

### 1.1 La gaussianité se propage : le trois-point **libre** est exactement nul

La relation d'état BD est **linéaire et déterministe par mode** (scellée,
`verif_D3_bunchdavies.py` bloc [3], re-vérifiée `verif_D3_spectre_k3.py` bloc [1]) :

$$g_{(3)}(k) = -\tfrac{i}{3}\,k^3\,g_{(0)}(k)\qquad(\text{par polarisation}).$$

Sur l'état BD **libre**, `g₀` est gaussien ⟹ tout corrélateur impair s'annule. En
particulier, par triple substitution :

$$\langle g_{(3)}g_{(3)}g_{(3)}\rangle_{\rm libre}
= \Big(-\tfrac{i}{3}\Big)^{\!3} k_1^3k_2^3k_3^3\,\langle g_{(0)}g_{(0)}g_{(0)}\rangle_{\rm libre}
= \tfrac{i}{27}\,k_1^3k_2^3k_3^3\cdot 0 = 0\quad\text{identiquement}.$$

**Lecture.** Le trois-point n'est pas un « résidu » du deux-point : c'est un objet de
**première classe nouvelle**, qui vit au **premier ordre dans l'interaction**. La chaîne
linéaire `g₃=-(i/3)k³g₀` ne le produit pas — elle ne fait que **transporter** la
non-gaussianité de `g₀` (engendrée par le vertex cubique) vers la donnée radiative.
`[établi (algèbre) dès que scellé — cible P1'-C, §3]`

### 1.2 La scission contact/Ward vs dynamique

Le trois-point se scinde en deux secteurs de statuts épistémiques **distincts** :

1. **Secteur de contact / Ward** : les identités de Ward de difféomorphisme relient les
   termes de contact de `⟨TTT⟩` au deux-point `⟨TT⟩`. Ce secteur est **entièrement fixé par
   le deux-point scellé** — il ne porte **aucun contenu neuf** ; sa reproduction est un test
   de **cohérence** (l'ancrage P1'-A, §3), pas une découverte.
2. **Secteur dynamique** : la partie de la forme générale CFT₃ de `⟨TTT⟩` **non fixée** par
   Ward — c'est le **seul datum non-gaussien authentique**. Côté dS, il correspond au
   `⟨γγγ⟩` du vertex gravitationnel cubique sur BD. La question du programme : ce secteur
   est-il, pour le raccord CCC, **pendu à `N` sans liberté neuve** (coefficients d'ordre un
   fixés par la structure Einstein-duale), ou introduit-il un paramètre ?

**Comptage des structures** : la forme générale conservée-sans-trace de `⟨TTT⟩` en `d=3`
est paramétrée par **2-3 structures tensorielles** (paires ; la dégénérescence exacte en
`d=3` est **à confirmer au fetch** — on ne fige ici que le **pattern** : `n_structures −
n_Ward = n_libre ≥ 1`). Le comptage précis appartient au bloc [D] du sceau, pas au cadrage.
`[décision ouverte jusqu'au fetch]`

### 1.3 Côté holographique : ce que le dictionnaire doit dire

Le dictionnaire un-point est scellé : `⟨T⟩=(d/16πG)g₃` (`LC-D-HOLOGRAPHIE-G3`). Le
trois-point holographique se lit sur `ψ₃ ≡ δ³W/δh³` (coefficient **nu** de fonction d'onde,
le prolongement direct de `ψ₂=δ²W` que lit le programme) versus `⟨TTT⟩`canon (triple
Brown–York). La map entre les deux est l'objet `γ₃` — voir §2, C2.

---

## 2. CARTE DE CONVENTIONS `[FIGÉE ICI — AVANT TOUT FETCH ; NE PAS REPARAMÉTRER]`

> **Règle générale (leçon R1, généralisée d'avance).** Seules **deux combinaisons
> cohérentes** existent : **tout-nu** (convention du programme) et **tout-canonique**. Tout
> **mélange** produit des facteurs purs (`γ`, `γ₃`, leurs rapports : 2, 4, 8…) qui sont des
> **artefacts pré-enregistrés**, à identifier contre les maps dérivées **avant** de déclarer
> un NO-GO. Aucun rattrapage de convention *a posteriori* : les maps sont dérivées en blocs
> aveugles, puis appliquées une fois.

- **C1 — Convention par défaut = NUE.** Le programme lit `ψ₂=δ²W` (c'est l'objet de
  `|Im F|`) : **tous** les scellés sont nus — `C_T/N=1/(32π²)`, `A_T·N=16`, `κ₃=1/(32π)`,
  `N_action=1/4` (étiquette tranchée, `LC-D-CT-GAMMA [C]`). Le trois-point du programme se
  lit donc sur `ψ₃=δ³W` (nu). Équivalent canonique disponible à tout moment via C2.
- **C2 — Map opérateur trois-point `γ₃`.** Par la même logique Brown–York que
  `LC-D-CT-GAMMA [B]` (chaque insertion de `T` = une application de `T=2δW/δg`), la map
  attendue est `γ₃ ≡ ⟨TTT⟩`canon`/ψ₃ = 2³ = 8`. **Statut : ATTENDU, à DÉRIVER ab initio au
  sceau** (bloc [B], variation troisième + firewall `T=nδW/δg ⟹ γ₃=n³`), **jamais supposé**.
  Si la dérivation donne autre chose (combinatoire de la variation troisième), c'est la
  dérivation qui fait foi — la valeur 8 est une **pré-déclaration falsifiable**, pas une cible
  de succès.
- **C3 — Dictionnaire cinématique impulsion↔position (trois-point).** Le `κ=24/π²` scellé
  (`NACTION-AVEUGLE`) est un objet **deux-points** : il ne se réutilise **pas** numériquement.
  Seule la **méthode** se transpose : dériver le dictionnaire cinématique du trois-point **à
  l'aveugle** (depuis les seules définitions, étalonné sur un cas libre connu, **sans** la
  cible), dans un bloc dédié, **avant** d'insérer toute valeur fetchée.
- **C4 — Continuation `ℓ_AdS→iℓ_dS`.** Facteur `i^p`, `p` = puissance de `ℓ` du coefficient
  considéré, dérivée **dimensionnellement avant fetch** (pattern `REALITE` : pour `C_T~ℓ²`,
  `p=2`, `i²=−1`, réel négatif). Pour les coefficients de `⟨TTT⟩`, `p` se lit sur `ℓ^p/G` par
  analyse dimensionnelle au moment où la structure est posée — la **règle** est figée ici, la
  valeur de `p` sera mécanique. Signes portés par la continuation ; **magnitudes** = objets
  du test.
- **C5 — Identifications.** `N = Aire/4G = πℓ_dS²/G` (P3 de R1, inchangée) ; `d=3` ;
  `M_Pl²=1/(8πG)` ; `𝒫=2H²/(M_Pl²k³)` (spectre vérifié, porteur de `β=M_Pl²/4`, **aveugle à
  `γ`** — la séparation β/γ de `GAMMA [D]` vaut aussi au trois-point : aucune information de
  map ne peut être extraite du spectre).

---

## 3. CIBLES PRÉ-ENREGISTRÉES `[P1' — GELÉES ICI, SANS FETCH]`

- **P1'-A (ancrage Ward — exact, slack nul).** Le secteur Ward de `⟨TTT⟩`, une fois les maps
  C2-C4 appliquées (combinaison cohérente unique), doit reproduire **exactement** le
  deux-point scellé : `|C_T|/N = 1/(32π²)` en nu (équivalent canonique `1/(8π²)`). Tout écart
  pur en puissance de 2 = candidat artefact de mélange (vérifier contre `γ`, `γ₃` dérivés)
  **avant** verdict ; tout écart résiduel après alignement = **NO-GO informatif**.
- **P1'-B (scaling en `N` — exact, zéro liberté).** L'amplitude **connexe** du trois-point
  est d'ordre `A_T² = (16/N)² = 256/N²` (non-gaussianité relative
  `⟨γ³⟩/⟨γ²⟩^{3/2} ~ A_T^{1/2} = 4/√N`). **Aucun paramètre libre neuf** : entrées libres du
  test strictement moindres que sorties appariées (critère anti-numérologie). Si la
  comparaison exige d'introduire un coefficient ajusté → **échec du critère de réduction**,
  consigné comme tel.
- **P1'-C (zéro du secteur libre — exact, symbolique).** `⟨g₃g₃g₃⟩_libre = 0` identiquement
  par linéarité de la relation FG (§1.1) — scellable en sympy sans aucune entrée externe.

**Ce que les cibles ne sont pas.** P1'-A/B/C sont les **prédictions du programme** ; les
valeurs littérature (coefficients de Maldacena, structures OP) sont **inconnues à ce stade**
(non fetchées). Le sceau les récupère et compare. Connaître P1' n'autorise **aucun**
ajustement des maps C2-C4 — c'est l'objet de l'audit à froid (§6).

---

## 4. Protocole anti-fit `[P1'-P5' — transposé de R1, rodé]`

- **P1'** : cibles §3 gelées ici, sans fetch (fait).
- **P2'** : maps de conventions (C2 `γ₃` ; C3 cinématique ; C4 continuation) **dérivées à
  l'aveugle** dans des blocs dédiés du sceau, **avant** insertion de toute valeur fetchée ;
  chaque map auditable hors contexte (déductive, étalon libre, jamais la cible).
- **P3'** : identifications C5 inchangées (aucune liberté d'identification au sceau).
- **P4'** : fetch **aveugle** au moment du sceau seulement (S3 : OP 1993 ;
  Maldacena 2003 ; Maldacena–Pimentel 2011) ; critère gelé, pas de reparamétrage.
- **P5'** : **firewall** — injecter coefficients faux (×2, mauvaise puissance de `ℓ`,
  `n≠2` dans `T=nδW/δg` ⟹ `γ₃=n³`) : le test doit **casser** (pouvoir discriminant prouvé).
- **Audit à froid** : 3ᵉ conversation, instance sans contexte — re-dérive les maps,
  re-fetch, re-exécute, vérifie le firewall (pattern §AF, identique à R1).

---

## 5. Plan du sceau `verif_D_nongauss_TTT.py` `[à écrire APRÈS validation ; deux temps]`

**Temps 1 — Tri de provenance (paper, AVANT sceau ; pattern R1 Temps 1).** Tracer si la
chaîne dS-native du programme (BD + vertex cubique) est **indépendante** des valeurs
`⟨TTT⟩`/`⟨γγγ⟩` de la littérature, ou en serait une réécriture. Indépendante ⟹ verdict
visé = **convergence** (GO). Réécriture ⟹ chute en **consolidation**, consignée comme telle
(toujours utile : elle rattacherait le trois-point au catalogue existant — pattern C_T-réalité).

**Temps 2 — Sceau, 6 blocs :**
- `[A]` **Zéro libre** : `⟨g₃³⟩_libre=0` symbolique (P1'-C) + scission contact/dynamique posée.
- `[B]` **Map `γ₃` ab initio** : variation troisième de `W`, triple Brown–York ;
  pré-déclaration `γ₃=8` confrontée à la dérivation ; firewall `n³`.
- `[C]` **Dictionnaire cinématique trois-point à l'aveugle** : dérivé des définitions,
  étalon libre, sans cible (pattern NACTION-AVEUGLE).
- `[D]` **Fetch aveugle + structures** : `⟨TTT⟩` OP `d=3` (comptage des structures confirmé
  ici), `⟨γγγ⟩` BD ; mise en convention unique (tout-nu) via [B]+[C]+C4.
- `[E]` **Tests centraux** : P1'-A (ancrage Ward, slack nul) ; P1'-B (scaling `256/N²`,
  zéro paramètre ajusté) ; identification du secteur dynamique (le datum non-gaussien) et de
  son statut (pendu à `N` / liberté résiduelle, consignée).
- `[F]` **Firewall global + bilan §6.4** (sans surclassement, compte inchangé).

---

## 6. Garde-fous `[discipline §6.4 — portés tout du long]`

- **Trois-point reproduit = `établi (algèbre)` d'une cohérence de coefficients.** JAMAIS
  « secteur non-gaussien fermé », JAMAIS « D1 fermé » (le non-gaussien complet excède le
  trois-point : quatre-point, boucles, non-perturbatif — hors périmètre S1).
- **NO-GO informatif.** Un écart non résorbable par les maps figées est un **résultat**.
- **Bascule consignée.** Convergence → consolidation si le tri de provenance l'exige ;
  positif fort **réservé** (seulement si un ancrage donnée-CFT-vérifiée est scellé).
- **Compte inchangé.** `{A4 ; A2★ ; N}` ni réduit ni augmenté par ce front ; `N` non fixé
  (circularité `LC-E` intacte) ; pont φ↔CCC aspirationnel ; **CCC non démontrée**.

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. `N≡Λ`).
