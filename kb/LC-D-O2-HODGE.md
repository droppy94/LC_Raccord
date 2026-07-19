---
id: LC-D-O2-HODGE
titre: "Pivot O₂, étape (c) — TRANSPORT DE HODGE par la jonction Dirichlet→Neumann : résout le résidu STRUCTUREL de P1 relocalisé par l'audit froid de (b′). Question (c) : la jonction D→N (réciprocité de Penrose Ω·ω=−1) réalise-t-elle la S COMPLÈTE (avec le facteur Hodge porteur du −1), ou seulement le swap SIGN-NEUTRE ? VERDICT = DISCORDANCE (KB-local, structure pincée, fetch NON déclenché). Quatre entrées scellées convergent : (1) MÊME PLAN, OPÉRATIONS DISTINCTES — J=[[0,1],[1,0]] (swap jonction, s=+1, det=−1, ordre 2, vp ±1) et S=[[0,−1],[1,0]] (Hodge, det=+1, ordre 4, vp ±i) agissent sur le même couple (a,b) des modes (f_a,f_b), mais diffèrent par un INVARIANT de classe (det/ordre) ⟹ J≠S même à base près ; J=S ⟺ s=−1, or la jonction nue donne s=+1 (O2-P1) ; (2) GARDE-FOU (cœur scellé CT-DUAL §3) — la transformée de Legendre=jonction D→N donne W̃=−W MAIS ⟨T̃⟩=−2δW̃/δh̃ ⟹ C̃_T=+C_T : la jonction NE FLIPPE PAS le signe physique, signe net = +1 ; (3) SOURCE UNIQUE DU SIGNE — le −1 physique (C_T<0) vient uniquement de la continuation dS i^{d-1}|_{d=3}=−1 réel (CT-REALITE/CT-DUAL-DS), apport structurel INDÉPENDANT, ≠ jonction ; (4) DISJONCTION DE PARITÉ (F6) — E∝g₃ pair (tenseur vrai) / B∝Cotton[g₀] impair (pseudo-tenseur), secteurs DISJOINTS ; le swap g₀↔g₃ reste dans le secteur pair, le −1 du Hodge vit dans la rotation E↔B qui traverse pair↔impair. RÉPONSE : la jonction transporte l'ÉCHANGE (g₀↔g₃ = E↔B) mais NON le −1 du Hodge ; le secteur porteur du signe (dS i^{d-1} + rotation E↔B/Cotton) est INDÉPENDANT de la jonction conforme. (C-O2) en forme FORTE (« réciprocité de Penrose = S complète, facteurs compris ») NON établie par cette voie — la réciprocité ne fournit que le swap sign-neutre ; le −1, donc la sélection du mode propre +i, exige l'apport dS indépendant déjà scellé source unique du signe. Ferme proprement le penchant-discordance laissé ouvert par O2-P1 (b), sans réouverture ni surclassement. NOTE DE RAFFINEMENT (anti-fit) : le critère gelé §3 du cadrage (« réciprocité rotative ⟹ concordance ») devait scinder « rotative=échange » (coïncide) vs « structure porteuse du signe » (indépendante) ; c'est cette dernière qui tranche — signalé puisque le libellé littéral autorisait l'issue agréable, or la dérivation donne l'issue négative (donc PAS un fit). Sceau verif_O2_hodge.py EXIT 0/28, firewall 3 mutations (sha256 421d5f29a9ee). {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; CCC non démontrée."
codename: LC-RACCORD
tags: [module-D, O2, P1, P1-structurel, etape-c, branche-falsifiabilite, jonction, dirichlet-neumann, hodge, dualite-electromagnetique, graviton-dual, de-haro, S-dualite, penrose-reciprocite, legendre, chern-simons, garde-fou-signe, C_T, i-puissance-d-moins-1, ds-continuation, electrique-magnetique, cotton, parite, pseudo-tenseur, F6, residu-bprime, discordance, delimitation, A4, sceau, firewall, §6.4, pivot]
type: "chaînon de front (branche FALSIFIABILITÉ, pivot O₂) — étage (c) : transport de Hodge, SCELLÉ (verif_O2_hodge.py). Résout le résidu structurel de P1 relocalisé par l'audit froid de (b′) (LC-D-O2-BPRIME v0.2 RÉFUTÉ). Subordonné à LC-AUDIT-VERDICT §6.4 et au cadrage gelé LC-WORK-CADRAGE-O2-HODGE v0.1 (sha256 14a7446c3d9a, cibles (c)-G1/G2 gelées avant algèbre/fetch). Verdict NÉGATIF (discordance) : audit froid différable (§5.5 du cadrage)."
statut: "discordance (délimitation) — (c) test du transport de Hodge FAIT (KB-local, fetch non déclenché, sceau réel). VERDICT : J=Swap(s=+1) ≠ S ; la jonction D→N transporte l'échange (g₀↔g₃=E↔B) mais NON le −1 du Hodge. Quatre entrées scellées convergent (J≠S invariant de classe det/ordre ; garde-fou C̃_T=+C_T ; source unique du signe i^{d-1} dS indépendante ; disjonction de parité F6 E pair/B impair). (C-O2) en forme forte NON établie par cette voie ; le −1 (donc la S complète, donc le mode +i) exige l'apport dS indépendant. Ferme le penchant-discordance de O2-P1 (b). Sceau verif_O2_hodge.py EXIT 0/28, firewall 3 mutations (m1 s=−1 ⟹ J=S / m2 réciprocité diagonale ⟹ pas de swap / m3 garde-fou off ⟹ C̃_T=−C_T) ; sha256 421d5f29a9ee. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; N non fixé (≡ Λ) ; CCC non démontrée."
statut_id: "validé après sceau (verif_O2_hodge.py, EXIT 0, 28 asserts, firewall 3 mutations, sha256 421d5f29a9ee) — à enregistrer si validé ; PROPAGER (lot séparé) : LC-AUDIT-VERDICT §8bis, 00_index, 03_glossaire, 04_references, LC-WORK-BRANCHE-FALSIFIABILITE (fiche O₂), LC-D-O2-JONCTION (renvoi : (C-O2) forte délimitée — Legendre ≠ S complète), LC-D-O2-P1 (renvoi : penchant-discordance fermé)."
version: 0.1
langue: fr
date: 2026-06-15
maj: "2026-06-15 — v0.1 : ouverture/scellement de l'étape (c) du pivot O₂ — transport de Hodge par la jonction D→N. Exécute le cadrage gelé LC-WORK-CADRAGE-O2-HODGE v0.1 (S-O2-c-1=KB-local d'abord ; fetch NON déclenché, la structure se pince KB-local ; S-O2-c-2=structure seule ; S-O2-c-3=sceau+firewall). Sceau verif_O2_hodge.py (EXIT 0, 28 asserts, firewall 3 mutations cassantes ; sha256 421d5f29a9ee). Acquis amont NON re-dérivés : (f_a,f_b)=(source g₀, VEV g₃) + swap s=+1 (O2-P1) ; Hodge S²=−𝟙 vp ±i (CT-DUAL §2) ; garde-fou C̃_T=+C_T (CT-DUAL §3) ; source unique du signe i^{d-1} dS (CT-REALITE/CT-DUAL-DS) ; disjonction de parité E pair/B impair (F6). RÉSULTAT : DISCORDANCE — la jonction réalise le swap mais pas le −1 du Hodge (secteur porteur du signe = dS, indépendant). (C-O2) forte non établie par cette voie. Note de raffinement du critère §3 (anti-fit) consignée. SANS SURCLASSEMENT (§6.4) : un test d'algèbre/structure qui délimite la jonction ne construit pas O₂, ne fixe aucun coefficient, ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos."
fichier_compagnon: "verif_O2_hodge.py (SCEAU, EXIT 0, 28 assertions, firewall 3 mutations cassantes — m1 s=−1 ⟹ J=S / m2 réciprocité diagonale ⟹ pas de swap / m3 garde-fou désactivé ⟹ C̃_T=−C_T ; sha256 421d5f29a9ee)"
prerequis_kb: [LC-WORK-CADRAGE-O2-HODGE, LC-D-O2-P1, LC-D-O2-BPRIME, LC-D-O2-JONCTION, LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-HOLOGRAPHIE-G3, LC-D-F6-BMS-MEMOIRE, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_O2_hodge.py, verif_O2_P1.py, verif_D_CT_dual.py]
renvois: [LC-D-O2-P1, LC-D-O2-BPRIME, LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-HODGE, LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-F6-BMS-MEMOIRE, LC-WORK-BRANCHE-FALSIFIABILITE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [discordance, délimitation, établi, formalisable, à inventer, décision ouverte]
---

# LC-D · O₂ — transport de Hodge par la jonction D→N (étape c)

> **Objet de cette étape.** Le cadrage gelé (`LC-WORK-CADRAGE-O2-HODGE` v0.1, sha `14a7446c3d9a`) a
> figé la question **(c)** — *la jonction D→N réalise-t-elle la S COMPLÈTE (avec le Hodge) ou seulement
> le swap sign-neutre ?* — avant toute algèbre. Ce n'est **pas** un calcul de parité (l'artefact réfuté
> de (b′)) mais un **fait structurel**. (c) **tranche** par croisement KB-local de quatre chaînons
> scellés. Résultat : **DISCORDANCE** — la jonction transporte l'**échange** mais **non** le `−1` du
> Hodge. **Rien ici ne construit O₂, ne fixe un coefficient, ni ne réduit A4.** KB-local (fetch non
> déclenché), **scellé** (`verif_O2_hodge.py`, EXIT 0/28, firewall 3).

---

## 0. Rôle et garde-fou `[§6.4 + R-7 + leçon (b′)]`

- **Étage.** (c) est la **résolution du résidu structurel** de P1 relocalisé par l'audit froid de (b′).
  Ce qui y est `établi` est un **fait de structure** (la jonction ne porte pas le `−1`), **jamais** la
  construction d'O₂ ni la réduction d'A4.
- **Pourquoi (c) n'est PAS (b′).** (b′) (`LC-D-O2-BPRIME` v0.2 = RÉFUTÉ) prélevait un signe d'une
  **parité** `(−1)^w` — épissure de deux opérations. (c) ne prélève aucun signe : il demande **quelle
  structure porte le `−1`** et **si la jonction la réalise**. La réponse est lue dans des chaînons
  **déjà scellés**, pas reconstruite.
- **Non-surclassement (§6.4).** **Discordance ≠ réfutation d'O₂ ≠ touche au compte.** Le compte
  **{A4 ; A2★ ; N}** reste **INCHANGÉ** ; A4 non réduit ; D1 non clos ; N ≡ Λ `hors de portée`.
- **Anti-fit + note de raffinement.** Cibles (c)-G1/G2 gelées au cadrage avant l'algèbre. Le verdict
  obtenu est l'issue **négative** (discordance), **non** l'issue agréable (concordance rouvrirait O₂)
  — donc pas un fit. **Raffinement signalé** (§3 ci-dessous) : le libellé gelé « rotative ⟹
  concordance » devait scinder *échange* vs *structure de signe*.
- **R-7 / additivité.** Aucune touche aux chaînons amont scellés (`O2-P1`, `CT-DUAL`, `CT-REALITE`,
  `F6` byte-identiques) ; `LC-D-O2-BPRIME` v0.2 (réfuté) reste mémoire d'erreur, non ré-ouvert.

---

## 1. Rappel `[hérité — NE PAS refaire]`

Acquis scellés, **non re-dérivés** :
- **(b)** (`O2-P1` §2) : la réciprocité de Penrose **swappe** `g₀↔g₃` sur `(f_a,f_b)` ⟹
  `P=[[0,s],[1,0]]` ; l'involution conforme **nue** ⟹ **`s=+1`** ; `P=S ⟺ s=−1` (non fourni par la
  géométrie nue).
- **Hodge** (`CT-DUAL` §2) : `S=[[0,−1],[1,0]]`, `S²=−𝟙`, vp `±i` (de Haro éq. 43-44-51) ; `S(E)=B`,
  `S(B)=−E`, `E∝g₃∝⟨T⟩`, `B∝Cotton[g₀]`.
- **Factorisation** : `S = Swap ∘ Hodge`. Le swap est réalisé par la jonction (b). **Le `−1` (facteur
  Hodge) est le seul terme dont la réalisation par la jonction restait ouverte.**

**(c)** tranche : la jonction réalise-t-elle ce facteur Hodge ?

---

## 2. Le résultat de la structure `[(c) — sceau verif_O2_hodge.py]`

Quatre entrées scellées convergent.

**[1] Même plan `(a,b)`, opérations DISTINCTES — `J≠S` par invariant de classe.** `J` (jonction,
`s=+1`) et `S` (Hodge) agissent sur le **même** couple `(a,b)` des modes `(f_a,f_b)`, mais :

| | `J=[[0,1],[1,0]]` (swap) | `S=[[0,−1],[1,0]]` (Hodge) |
|---|---|---|
| carré | `J²=+𝟙` | `S²=−𝟙` |
| det | `−1` (réflexion / échange) | `+1` (rotation 90°) |
| ordre | 2 | 4 |
| vp | `±1` | `±i` |

La différence `det J=−1 ≠ +1=det S` est un **invariant** : `J≠S` **même à changement de base près**.
`J=S ⟺ s=−1` (contrôle scellé), or la jonction nue donne `s=+1`. **(c)-G1** : les axes partagent le
plan mais les opérations sont de **classes distinctes**.

**[2] Garde-fou de signe (cœur scellé `CT-DUAL` §3) — la jonction ne flippe pas le signe physique.**
La transformée de Legendre = jonction D→N donne `W̃=−W` (`−` relatif réel, via Chern-Simons) **mais**
`⟨T̃⟩=−2δW̃/δh̃` (le `−2` explicite, éq. 63) vs `⟨T⟩=+2δW/δh` ⟹ **`C̃_T=+C_T`**. Signe **net** de la
jonction sur `C_T` = **`+1`**. Le `−` de Legendre est **compensé** ; aucun `−1` physique transporté.

**[3] Source UNIQUE du signe — continuation dS `i^{d-1}`, INDÉPENDANTE.** Le `−1` physique (`C_T<0`
requis par la CCC) vient **uniquement** de la continuation dS `ℓ²→−ℓ²` ⟹ `i^{d-1}|_{d=3}=i²=−1`
(réel, `CT-REALITE`/`CT-DUAL-DS`, **source unique du signe**). C'est l'opération `ℓ²→−ℓ²`, **≠** la
Legendre/swap : `−1` (dS) `≠` `+1` (signe net jonction) ⟹ **apport structurel indépendant**.

**[4] Disjonction de parité (`F6`).** `E∝g₃` est **pair** (tenseur vrai, même secteur que `g₃`) ;
`B∝Cotton[g₀]` est **impair** (pseudo-tenseur) — secteurs **DISJOINTS**. Le swap `g₀↔g₃` relie deux
data de **même** parité (pair) ⟹ reste dans le secteur pair. Le `−1` du Hodge vit dans `S(B)=−E`, la
rotation `E↔B` qui **traverse** pair↔impair (médiée par le Cotton). **(c)-G2** : la jonction est
rotative au sens *échange*, mais la structure porteuse du signe (`i^{d-1}` dS + traversée de parité)
est **hors** de son secteur.

> **Sceau.** `verif_O2_hodge.py` (EXIT 0, **28 assertions**) avec **firewall 3 mutations cassantes** :
> **(m1)** jonction forcée `s=−1` ⟹ `J=S` (casse la discordance) ; **(m2)** réciprocité forcée
> **diagonale** (det `+1`) ⟹ pas d'échange (casse « la jonction réalise le swap ») ; **(m3)** garde-fou
> désactivé (`⟨T̃⟩=+2δW̃`) ⟹ `C̃_T=−C_T` (casse « pas de flip »). sha256 `421d5f29a9ee`.

---

## 3. Verdict `[(c)]`

`discordance` (`délimitation`). **La jonction D→N transporte l'ÉCHANGE (`g₀↔g₃ = E↔B`) mais NON le
`−1` du Hodge.** `J = Swap(s=+1) ≠ S`. Le secteur porteur du signe — continuation dS `i^{d-1}` (source
unique) + rotation `E↔B` traversant la parité (Cotton) — est **INDÉPENDANT** de la jonction conforme.

**(C-O2) en forme FORTE** (« réciprocité de Penrose `=` S complète, **facteurs compris** ») **NON
établie par cette voie.** La réciprocité fournit le **swap** ; le `−1`, donc la **S complète**, donc la
**sélection du mode propre `+i`**, exige l'apport dS **indépendant**, déjà scellé source unique du
signe. Le chemin « jonction `=` S pleine ⟹ état `=+i` ⟹ WCH ⟹ A4 » de `O2-JONCTION §5` **n'est pas
auto-suffisant** : la jonction ne sélectionne pas seule le mode propre.

**Conséquence pour O2-P1 (b).** Le **penchant-discordance** laissé ouvert par (b) est **fermé** —
non par un calcul de parité (réfuté), mais par la structure : le `−1` n'est pas dans la jonction. O₂
reste `à inventer` par cette voie.

**Note de raffinement du critère gelé `[anti-fit, datée 2026-06-15]`.** Le critère §3 du cadrage
disait « réciprocité rotative ⟹ concordance ». La dérivation montre que **« rotative » devait être
scindé** : *échange* (`E↔B`, qui **coïncide** avec le swap) vs *structure porteuse du signe* (`i^{d-1}`
dS + traversée de parité, **indépendante**). C'est cette dernière qui tranche (c). Le libellé littéral
aurait autorisé l'issue **agréable** (concordance) ; la dérivation donne l'issue **négative** — d'où
le signalement (ce n'est **pas** un fit). Aucune cible déplacée ; raffinement consigné, non
rétro-ajusté.

---

## 4. Format de chaînon

- **Hypothèse.** La jonction D→N (réciprocité de Penrose) réalise la S complète (facteur Hodge `−1`
  compris).
- **Outil.** Croisement KB-local de quatre chaînons scellés (`O2-P1`, `CT-DUAL` §2-§3, `CT-REALITE`,
  `F6`) ; sceau symbolique encodant les matrices, le garde-fou, le facteur dS et la parité.
- **Critère de réfutation (du chaînon lui-même).** (i) si `det J = det S`, l'argument d'invariant de
  classe tomberait (firewall m1) ; (ii) si la jonction n'échangeait pas (`det J=+1`), le swap serait
  faux (firewall m2) ; (iii) si le garde-fou flippait (`C̃_T=−C_T`), le `−1` serait porté par la
  jonction (firewall m3). Aucune ne survit.
- **Verdict.** (c) **`discordance`** : la jonction réalise le swap mais **pas** le `−1` du Hodge ;
  (C-O2) forte non établie par cette voie. **Ne construit pas O₂ ; ne fixe aucun coefficient ; ne
  réduit pas A4 ; {A4 ; A2★ ; N} inchangé.**

---

## 5. Prochain pas `[handoff — sur GO]`

- **P2** (`O2-JONCTION §5`) — la seconde gate (cohérence de jonction ⟹ état `=` eigenmode), `à
  inventer`. **Mais (c) en a changé la portée** : la sélection du mode propre `+i` ne peut **pas**
  s'appuyer sur « jonction `=` S complète » (réfuté ici) ; elle devrait s'appuyer sur l'apport dS
  **indépendant** (`i^{d-1}`, source unique). Toute reprise de P2 doit intégrer cette dépendance — `à
  inventer`, cadrage gelé dédié.
- **F4** (A4 principiel) — réserve de fond.
- **Audit froid (c)** : **différable** (verdict négatif/délimitation, §5.5 du cadrage ; sceau réel,
  firewall en place).
- **N ≡ Λ** — `hors de portée`.

---

## 6. Renvois, glossaire, références

**Renvois.** `LC-D-O2-P1 §2-§3` (swap `s=+1`, `P=S⟺s=−1`, penchant-discordance — **fermé ici**) ;
`LC-D-O2-BPRIME §R-7` (parité réfutée — mémoire d'erreur) ; `LC-D-O2-JONCTION §3,§5` ((C-O2) forte
**délimitée** : Legendre `≠` S complète ; gate P2 reportée) ; `LC-D-CT-DUAL §2-§3` (`S²=−𝟙` ;
garde-fou `C̃_T=+C_T`) ; `LC-D-CT-REALITE` (`i^{d-1}` dS, source unique du signe) ;
`LC-D-F6-BMS-MEMOIRE` (E pair / B impair, secteurs disjoints) ; `LC-AUDIT-VERDICT §6.4`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Transport de Hodge (O₂-c)* : la jonction D→N transporte l'échange `g₀↔g₃=E↔B` (swap, `s=+1`,
  involution det `−1`) mais **non** le `−1` du Hodge (`S`, rotation 90° det `+1`, vp `±i`) ; le signe
  physique vient de la continuation dS `i^{d-1}` (source unique), indépendante de la jonction.
  Verdict : **discordance** ; (C-O2) forte non établie par cette voie.

**Références (`LC-04`).** S-O2-c-1 = **KB-local** (de Haro `0808.2054` ; `CT-DUAL`, `CT-REALITE`, `F6`,
`O2-P1` — tous en KB). **Fetch post-gel NON déclenché** : la structure s'est pincée KB-local ; la
ligne `[ANTI-FETCH — c]` du cadrage reste **non consommée** (à marquer `non consommé — pincé
KB-local`).

---

## Appendice — Légende des tags épistémiques
`discordance` : (c) — la jonction ne réalise pas la S complète ; (C-O2) forte non établie par cette voie.
`délimitation` : la jonction est circonscrite au swap sign-neutre ; le `−1` est hors de son secteur.
`établi` : les **faits de structure** (J≠S par invariant ; garde-fou `C̃_T=+C_T` ; `i^{d-1}` indépendant ;
parité disjointe) — algèbre correcte, adossée aux sceaux amont.
`à inventer` : O₂ (construction) ; coefficient O(1) (différé) ; P2 (à re-cadrer).
`décision ouverte` : la reprise de P2 sous la dépendance dS révélée par (c).
**A4 non réduit ; D1 non clos ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé ; CCC non démontrée.**
