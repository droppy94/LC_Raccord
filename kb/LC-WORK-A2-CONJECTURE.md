---
id: LC-WORK-A2-CONJECTURE
titre: "Front (a)/GWE — C7-b, facteur A2 : CADRAGE PAPIER (Option 1, paper-first, AUCUN code). Réduit le résidu A2 (mesure/production de spikes générique n_s^gen, `à inventer`/`hors de portée` après LC-D3-C7B-VERDICT-A2) à UNE SEULE conjecture nommée et falsifiable — la conjecture A2★ (non-cascade / charge de gradient agrégée des spikes sous-exponentielle en τ) — adossée à du matériel DÉJÀ SCELLÉ : la factorisation et le scaling 1/ℓ→e^{−|w|τ} de A1 (LC-D3-A1-SUPERHORIZON), et l'oracle de Gauss-Kuzmin du deep-bang (marche aléatoire O(1) par bounce, PAS d'emballement ; LC-D3-INTERAEON-P6). DÉDUCTION : A2★ + (N_bounce(τ) sous-exp., BKL standard, cohérent avec l'oracle scellé) + (I_spike^gen~e^{−|w|τ}, A1) ⟹ R_grad,gen→0 ⟹ C7-b complet en générique. CE QUE CE CADRAGE FAIT : transforme A2 d'un trou non structuré en UN postulat unique, explicite, réfutable, physiquement motivé — une RÉDUCTION D'HYPOTHÈSE (critère central du programme). CE QU'IL NE FAIT PAS : il ne PROUVE pas A2★ (donc ne lève PAS C7) ; l'attente physique reste non scellée (§6.4). Propose (non exécuté) un sceau futur verif_D3_C7b_A2_reduction.py."
codename: LC-RACCORD
type: note de cadrage analytique (paper-first) — PAS un chaînon (aucun sceau). Exécute l'Option 1 du pivot post-LC-D3-C7B-VERDICT-A2. Subordonnée à LC-AUDIT-VERDICT §6.4.
version: 0.3
langue: fr
date: 2026-06-08
portee: "Consigne (I) la factorisation exacte du résidu générique héritée de A1 ; (II) la réduction à UNE grandeur agrégée (la charge de gradient des spikes par horizon) et UNE condition (sous-exponentialité en τ) ; (III) l'énoncé précis de la conjecture A2★ et le pont vers la statistique de bounces scellée (Garfinkle + Gauss-Kuzmin) ; (IV) la DÉDUCTION A2★ ⟹ C7-b complet ; (V) le critère de réfutation pré-enregistré ; (VI) le statut épistémique (réduction, pas surclassement) ; (VII) le sceau futur proposé (non exécuté ; paper-first). Ne refait NI A1 (LC-D3-A1-SUPERHORIZON) NI l'oracle (LC-D3-INTERAEON-P6) NI le verdict A2 (LC-D3-C7B-VERDICT-A2). Discipline §6.4 : A2★ n'est PAS scellée ; C7 levée seulement sous preuve."
prerequis_kb: [LC-D3-C7B-VERDICT-A2, LC-D3-A1-SUPERHORIZON, LC-D3-GRADIENT-C7B, LC-D3-SPIKES-C7B, LC-D3-INTERAEON-P6, LC-D3-SILENCE-POC, LC-D3-WCH-GWE, LC-AUDIT-VERDICT]
source_externe: ["Garfinkle gr-qc/0312117 (mécanisme de spike : un Nᵢ s'annulant sur une surface S ⟹ bounces de part et d'autre ⟹ naissance d'une structure de spike ; les spikes sont PRODUITS aux bounces). Andersson-van Elst-Lim-Uggla gr-qc/0402051 (silence générique : ℓ(τ)→∞). Lim 0710.0628 (profil exact, C_F^Lim=2π·A²). Lifshitz-Khalatnikov / BKL ; Khalatnikov-Lifshitz-Sinai-Khanin-Shchur (statistique d'ères, mesure de Gauss-Kuzmin, taux de bounces O(1) par unité de τ). Tous en KB sauf le dernier (statistique d'ères) — à ajouter à 04_references si A2★ est sealée."]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# C7-b, facteur A2 — cadrage papier : réduction à la conjecture A2★

> **But (Option 1).** Le verdict `LC-D3-C7B-VERDICT-A2` a laissé A2 (mesure de spikes générique
> `n_s^gen`) comme `à inventer` / `hors de portée`, avec une **attente physique** (croissance
> polynomiale, bounces BKL ~ linéaires) **explicitement non scellée**. Ce cadrage **structure**
> cette attente : il montre que A2 se réduit à **une seule** conjecture nommée et **falsifiable**,
> adossée à du matériel **déjà scellé**. C'est une **réduction d'hypothèse**, pas une preuve.
> Discipline `§6.4` : A2★ reste `décision ouverte` ; C7 n'est pas levée. **Paper-first : aucun
> code ici.**

---

## 0. Résultat du cadrage en une ligne `[réduction]`

Le résidu générique de C7-b se met sous la forme `R_grad,gen(τ) = Q(τ)·e^{−|w|τ}/⟨Ω_σ⟩_bulk`, où
`Q(τ)=Σ_spikes C_F` est la **charge de gradient agrégée des spikes par volume d'horizon**. Comme
`⟨Ω_σ⟩_bulk=O(1)` au deep-bang (`LC-D3-INTERAEON-P6`, (B) : `Ω_σ→1`), **`R_grad,gen→0` ⟺ `Q(τ)`
croît plus lentement que `e^{|w|τ}`** (sous-exponentiel). Toute la question A2 tient désormais
dans **une grandeur scalaire** `Q(τ)` et **une condition** — c'est l'énoncé de la **conjecture
A2★** (§4).

---

## 1. La factorisation exacte héritée de A1 `[établi (sceaux) — point de départ]`

De `LC-D3-A1-SUPERHORIZON` (sceau `verif_D3_C7b_A1_superhorizon.py`, 10/10) et de
`LC-D3-GRADIENT-C7B` (voie 1.5, profil exact), l'énergie de gradient Hubble-normalisée **par
spike** vaut, pour un spike de largeur `ℓ` en unités d'horizon et de profil `F` :
```
I_spike^gen(τ) = C_F / ℓ(τ) ,   C_F = ∫ (dF/du)² du   (charge O(1), dépend du profil),
```
et le silence asymptotique (`E_i^a→0`, `gr-qc/0402051` : horizons → 0) impose `ℓ(τ)→+∞`. Sur le
profil exact de Lim, `ℓ(τ)=cosh(wτ)/w` (éq.43, `0710.0628`), donc
```
I_spike^gen(τ) = C_F · w/cosh(wτ) ≈ C_F · 2w · e^{−|w|τ}   (τ→∞).
```
**Le facteur par spike décroît exponentiellement.** A1 a établi que le **scaling `1/ℓ` est
universel** (indépendant du profil ; pente log-log `−1` à `1e-6`, 6 profils), le profil n'entrant
que par `C_F`.

> **La brèche que A1 a explicitement nommée.** A1 réserve un et un seul mécanisme pouvant casser
> `I→0` : une **cascade** — régénération **sous-horizon** de structure faisant **diverger `C_F`**
> (ou, de façon équivalente, multipliant le nombre de spikes). C'est **exactement** le facteur A2.
> Il n'y a pas d'autre voie : hors cascade, `I_spike^gen→0` pour tout profil à `C_F` bornée.

---

## 2. Réduction à une grandeur agrégée `[algèbre élémentaire]`

Le résidu générique de C7-b (`LC-WORK-REPRISE-C7B-GENERIQUE §2 N2`) se factorise
```
R_grad,gen(τ) = [ Σ_{spikes actifs} C_F ] · (1/ℓ(τ)) / ⟨Ω_σ⟩_bulk(τ).
```
Les deux faces de A2 (la **mesure** `n_s^gen` et la **charge par spike** `C_F`, susceptible de
diverger par cascade) se **confondent** dans une **seule** grandeur :
```
Q(τ) := Σ_{spikes actifs par horizon} C_F(spike, τ)   =   « charge de gradient agrégée par horizon ».
```
Avec `1/ℓ ≈ 2w·e^{−|w|τ}` (§1) et `⟨Ω_σ⟩_bulk=O(1)` (deep-bang) :
```
R_grad,gen(τ) ≈ 2w · Q(τ) · e^{−|w|τ}     ⟹     R_grad,gen → 0  ⟺  Q(τ) = o(e^{|w|τ}).
```
**On a remplacé « la mesure de spikes générique » (objet mal défini) par une grandeur scalaire
`Q(τ)` et une condition de sous-exponentialité.** Aucune hypothèse cachée : c'est de l'algèbre sur
la factorisation A1.

---

## 3. Le pont vers la statistique de bounces `[ce qui est scellé / standard / résiduel]`

Pourquoi attendre `Q(τ)` sous-exponentielle ? Parce que les spikes sont **produits aux bounces** :

- **Mécanisme (Garfinkle `gr-qc/0312117`, déjà lu).** À chaque bounce un `Nᵢ` croît
  exponentiellement ; s'il **s'annule sur une surface** `S`, on a des bounces de part et d'autre
  mais pas sur `S` ⟹ **naissance d'une structure de spike** sur `S`. Les spikes ne surgissent pas
  spontanément : ils sont **engendrés par l'oscillation BKL**. ⟹ `Q(τ)` est **alimentée par les
  bounces**.
- **Statistique des bounces (scellée, `LC-D3-INTERAEON-P6`).** L'oracle de Gauss-Kuzmin scelle que
  le deep-bang est, **par bounce**, une **marche aléatoire `O(1)`** (`|b_n|~O(1)`, direction
  Gauss-Kuzmin) — **pas** un emballement exponentiel de l'anisotropie. « Le bang gagne », mais
  **borné par bounce**. ⟹ chaque bounce injecte une charge de spike `O(1)`, pas exponentielle.
- **Taux de bounces (BKL standard, à invoquer).** Dans le temps Hubble-normalisé `τ` (vers le
  bang), le nombre de bounces `N_b(τ)` croît **sous-exponentiellement** : structure d'ères
  (épochs `u→u−1`) entrecoupées de transitions (`u→{1/u}`), taux moyen `O(1)` par unité de `τ`
  sous la mesure de Gauss-Kuzmin ⟹ `N_b(τ)` essentiellement **linéaire** (avec fluctuations à
  queue lourde des ères longues, mais une ère longue **coûte** d'autant en `τ`). *C'est un résultat
  BKL classique, cohérent avec l'oracle scellé ; il n'est pas séparément scellé dans la KB —
  candidat au sceau futur §7.*

**Bilan du pont.** Si chaque bounce engendre une charge de spike `O(1)` par horizon (pas de
cascade) **et** `N_b(τ)` est sous-exponentiel, alors `Q(τ) ≲ ⟨charge/bounce⟩ · N_b(τ)` est
sous-exponentielle. La **seule** maille non acquise est « **pas de cascade** » : c'est A2★.

---

## 4. La conjecture A2★ et la déduction `[énoncé précis + conséquence]`

> **Conjecture A2★ (non-cascade).** Dans le deep-bang générique sous silence asymptotique, la
> charge de gradient agrégée des spikes par volume d'horizon, `Q(τ)=Σ_{spikes} C_F`, croît
> **sous-exponentiellement** en `τ` :
> ```
> Q(τ) = o(e^{|w|τ})   (équivalent : aucune cascade de régénération sous-horizon ne
>                        multiplie Q plus vite que e^{|w|τ}).
> ```
> Forme **suffisante et physiquement attendue** : `Q(τ) ≤ A·N_b(τ)^p` (polynomial), avec
> `N_b(τ)` le nombre de bounces et `A,p` des constantes `O(1)` — la **charge par bounce est
> bornée**.

**Déduction (algèbre, conditionnelle à A2★).**
```
A2★  (Q = o(e^{|w|τ}))                          [conjecture, §4]
  +  I_spike^gen = C_F/ℓ ≈ 2w·e^{−|w|τ}         [A1, scellé]
  +  ⟨Ω_σ⟩_bulk = O(1) au deep-bang             [P6, scellé]
  ⟹  R_grad,gen(τ) ≈ 2w·Q(τ)·e^{−|w|τ} → 0      [§2]
  ⟹  le facteur de gradient générique est borné → C7-b COMPLET en générique
  ⟹  (avec C7-a pointwise + silence)  C7 LEVÉE  ⟹  (A) `établi (sous WCH/A3-A4, CCC)`.
```
Autrement dit : **toute la levée de C7 repose désormais sur la seule conjecture A2★** (modulo le
fait BKL-standard `N_b` sous-exp., non contentieux). C'est la **réduction** visée.

---

## 5. Critère de réfutation `[pré-enregistré — CONSORT, AVANT tout calcul]`

A2★ est **falsifiable**. Serait **réfutée** (et C7-b rouvert) par l'un des constats suivants, issu
d'une simulation générique 3D sans symétrie (le « work in progress » de Garfinkle) ou d'un
argument analytique :
- **(R1) Prolifération exponentielle de spikes** : `n_s^gen(τ) ~ e^{cτ}` avec `c>0` (nombre de
  surfaces de spike actives croissant exponentiellement avec la profondeur).
- **(R2) Cascade de charge** : `C_F` par spike divergeant par régénération sous-horizon de sorte
  que `Σ C_F` croisse `~ e^{|w|τ}` ou plus vite (la brèche nommée par A1).
- **(R3) Yield par bounce non borné** : la charge de spike engendrée **par bounce** croissant avec
  la profondeur (contredisant la marche aléatoire `O(1)` par bounce de l'oracle de Gauss-Kuzmin).

**Soutien (non preuve).** Le mécanisme de Garfinkle (spikes nés aux bounces) + l'oracle scellé
(marche `O(1)` par bounce, pas d'emballement) + `N_b` sous-exp. **rendent A2★ physiquement
attendue**. Mais aucune de ces pièces ne **prouve** l'absence de cascade en générique — c'est
précisément le « work in progress » que la littérature ne ferme pas (`gr-qc/0312117`).

---

## 6. Statut épistémique `[discipline §6.4 — sans surclassement]`

- **Ce que ce cadrage A FAIT.** Il **réduit le nombre d'hypothèses indépendantes** : A2 passe de
  « mesure de spikes générique, objet non structuré, `à inventer` » à **une conjecture scalaire
  unique A2★**, explicite, falsifiable (§5), et **physiquement motivée** par du matériel scellé
  (A1, oracle P6). C'est le **critère central du programme**.
- **Ce qu'il NE FAIT PAS.** Il ne **prouve pas** A2★. C7 **n'est pas levée**. (A) physique reste
  `formalisable`, conditionnel — maintenant au **seul A2★** (au lieu d'« A2 non structuré »).
  L'attente physique (`Q` polynomial) **n'est pas scellée**.
- **Tag de A2 après ce cadrage.** `décision ouverte`, mais **structurée** : = conjecture A2★ +
  fait BKL-standard (`N_b` sous-exp.). La conjecture A2★ elle-même : `à inventer` (preuve) /
  réfutable par simulation générique (`hors de portée` réaliste du projet). C7-b : **PASS
  substantiel** (inchangé). « Le bang gagne » (P6 B) intact.

---

## 7. Sceau de réduction — FAIT `[exécuté 2026-06-08]`

> **MàJ — sceau exécuté (`verif_D3_C7b_A2_reduction.py`, EXIT 0, 16/16 ASSERTS).** La réduction
> est scellée dans ses **deux maillons NON-A2★** : **(A)** la déduction §4 (symbolique) — `Q`
> sous-exponentielle ⟹ `R_grad,gen→0`, raccord exact à A1 (`lim I_spike/(2·C_F·w·e^{−wt})=1`),
> avec **contrôle de seuil** `Q=e^{wt} ⟹ R↛0` (réfutation R2) ; **(B)** `N_b(τ)`
> **sous-exponentiel** le long de l'oracle de Gauss-Kuzmin (`N_b(n)≈1,60·n·ln n`, `R²=0,9998`,
> exposant log-log `1,11`, `ln(N_b)/n=0,003` ⟹ non-exponentiel ; queue lourde des ères longues
> **bornée**, coût `τ` proportionnel). **Le sceau NE scelle PAS A2★** (la non-cascade) : c'est le
> **seul** maillon qui reste, isolé. ⟹ toute la chaîne de C7-b est `formalisable` **sauf** la
> conjecture A2★. C7 **non levée**. Discipline §6.4 : signature numérique, pas thèse physique.

*Énoncé initial du sceau proposé (conservé, historique) :*

Si tu valides la réduction, un sceau **léger** `verif_D3_C7b_A2_reduction.py` pourrait :
1. **Vérifier la déduction §4 symboliquement** (sympy) : `Q(τ)·e^{−|w|τ}→0` pour toute `Q`
   sous-exponentielle ; et le raccord `2w·Q·e^{−|w|τ}` à la factorisation A1 (cohérence avec
   `LC-D3-GRADIENT-C7B`).
2. **Sceller `N_b(τ)` sous-exponentiel numériquement** depuis l'oracle de Gauss-Kuzmin **déjà
   codé** (`verif_D3_P6_specB_oracle.py` / `diag_bounces.py`) : compter les bounces vs `τ` sur de
   longues trajectoires, vérifier pente linéaire (et borner la contribution des ères longues à
   queue lourde). *Ceci scellerait le maillon BKL-standard du §3, retirant la dernière pièce
   non-A2★ de la chaîne.*
3. **NE PAS** prétendre sceller A2★ (la non-cascade en générique) — qui resterait `à inventer`.

Effet attendu d'un tel sceau : faire passer le statut de « réduction » à « réduction **scellée**
(modulo A2★) » — soit `formalisable` pour toute la chaîne **sauf** la conjecture A2★ isolée. Ce
serait l'aboutissement honnête de C7 : un verrou **réduit à un unique postulat nommé**.

> **[MàJ — 2026-06-13 ; substantiation F3 : `LC-D-F3-A2STAR` v0.1 + audit froid `LC-AUDIT-LOG-F3` v0.3 CLOS 3/3].** Le front F3 a **confronté** A2★ (sa maille C, la non-cascade) à la statistique rigoureuse des singularités génériques (cibles gelées AVANT lecture, anti-fit). **A2★ reste `décision ouverte`, mais est désormais MIEUX SITUÉE et faiblement soutenue, en réduction G₂** : le cadre BKL modifié (Heinzle-Uggla-Lim, *Spike Oscillations* 1206.0932), la statistique de spikes (Heinzle-Uggla, GRG 45 (2013)) et le caractère **transitoire** des spikes (Lim 0710.0628) **concordent** avec la non-cascade ; **aucune réfutation** (R1/R2/R3 non observés). **Gap nommé** (ce qui sépare encore A2★ de `établi sous principes`) : **(i)** extension de la statistique de spikes **G₂ → générique 3D** (le billard ultralocal **exclut les spikes par construction** — OB ; Garfinkle gr-qc/0312117 « work in progress », hors régime convergent — OA) ; **(ii)** **pont `u_ère → C_F`** non fait (OC). **R-19 (précision load-bearing).** La qualification « **G₂-réduite** » porte sur la **base physique** — le **mécanisme de spike récurrent** n'est statistiqué rigoureusement qu'en symétrie G₂ — et **NON** sur l'**arithmétique** de la *spike map* : celle-ci (carte BKL² / fractions continues / mesure de Gauss-Kuzmin) est **map-générique** (théorie des nombres), valable indépendamment de la symétrie. ⟹ le maillon **(B) déjà scellé** (`N_b(τ)` sous-exp. via l'oracle, §7) n'est **pas** affaibli par la réduction G₂ ; le **seul** résidu reste **A2★ (non-cascade physique en générique 3D)**. **Sans surclassement** (§6.4) : A2★ ni prouvée ni réfutée ; « soutenu en G₂ » ≠ « soutenu en générique » ; C7 non levée ; `{A4 ; A2★ ; N}` inchangé ; CCC non démontrée. (cf. `LC-D-F3-A2STAR` ; `LC-AUDIT-LOG-F3 §3` R-19.)

---

## Appendice — chaîne logique (d'un coup d'œil)

| Maillon | Statut | Source |
|---|---|---|
| `I_spike^gen = C_F/ℓ`, scaling `1/ℓ` universel | `établi (sceau)` | `LC-D3-A1-SUPERHORIZON` |
| `1/ℓ(τ) ≈ 2w·e^{−|w|τ}` (silence) | `établi (sceau)` | `LC-D3-GRADIENT-C7B`, `gr-qc/0402051` |
| `⟨Ω_σ⟩_bulk = O(1)` au deep-bang | `établi (ordre dom.)` | `LC-D3-INTERAEON-P6` (B) |
| spikes **produits aux bounces** | `établi` (mécanisme) | Garfinkle `gr-qc/0312117` |
| marche `O(1)` **par bounce** (pas d'emballement) | `établi (sceau)` | `LC-D3-INTERAEON-P6`, oracle GK |
| `N_b(τ)` sous-exponentiel (linéaire) | BKL standard ; **sceau §7 proposé** | littérature / oracle GK |
| **A2★ : `Q(τ)` sous-exponentielle (non-cascade)** | **`décision ouverte` / `à inventer`** | **conjecture, ce cadrage** |
| `R_grad,gen → 0` ⟹ C7-b complet ⟹ C7 levée | **conditionnel à A2★** | déduction §4 |

**Tags.** Factorisation, scaling, raccord A1, `⟨Ω_σ⟩_bulk=O(1)`, marche O(1)/bounce :
`établi (sceau / ordre dominant)`. `N_b` sous-exp. : `formalisable` (sceau §7 proposé). **A2★
(non-cascade) : `décision ouverte` / `à inventer`** ; falsifiable (§5) ; preuve générique
probablement `hors de portée`. C7-b : **PASS substantiel**. (A) physique : `formalisable`,
conditionnel au **seul A2★**. *Réduction d'hypothèse, PAS surclassement (§6.4) ; A2★ non scellée ;
« le bang gagne » intact.*
