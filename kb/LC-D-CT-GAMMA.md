---
id: LC-D-CT-GAMMA
titre: "Module D / dS-CFT — MAP OPÉRATEUR « ab initio » `⟨TT⟩ = γ·ψ₂` DÉRIVÉE de l'action holographique renormalisée de de Haro (arXiv:0808.2054, JHEP 01 (2009) 042 ; éq. 61/63/90) + variation seconde. Exécute la tranche R-2 « dérivation ab initio de la map opérateur » posée par LC-WORK-REPRISE-POST-AUDIT-FROID et tranche le statut de `N_action=1/4`. Ce chaînon SCELLE (verif_naction_gamma_dHSS.py, EXIT 0, 18 asserts, 5 blocs A–E) : [A] DICTIONNAIRE de de Haro — `c_W=ℓ²/(8κ²)` (éq.61) ; coefficient NU de fonction d'onde `ψ₂ ≡ δ²W/δh² = 2c_W` (ce que le programme lit comme `C_T^prog`) ; tenseur de stress par la définition UNIVERSELLE `T=2δW/δg` (éq.63) appliquée deux fois ⟹ `⟨T⟩=4c_W h`, `⟨TT⟩_canon = 8c_W = ℓ²/κ²` (= éq.90 reproduite). [B] MAP FORCÉE — `γ ≡ ⟨TT⟩_canon/ψ₂ = 8c_W/2c_W = 4` ; les deux facteurs 2 sont les DEUX applications de la définition de T (Brown-York), PAS un choix (le 2 de la dérivée seconde est COMMUN aux deux côtés et n'entre pas dans γ). [C] `N_action=γ/4` — canonique γ=4 ⟹ `N_action=1`, `C_T^prog=C_T^dH` (MÊME objet, f_W=1) ; nu γ=1 (O=T/2) ⟹ `N_action=1/4`, `C_T^prog=¼ C_T^dH` ; recoupement `(1/8π²)/(1/32π²)=4` (=f_W à γ=1, recoupe CT-ATN/DUAL). [D] SÉPARATION β/γ — le spectre `𝒫=1/(2|Im F|)=2H²/(M_Pl²k³)` FORCE `β=M_Pl²/4` UNIQUEMENT et NE contient PAS γ ⟹ magnitude et map DISJOINTES (le spectre est aveugle à la normalisation opérateur). [E] FIREWALL — `T=n δW/δg` : SEUL `n=2` (Brown-York) reproduit l'éq.90 ⟹ `γ=n²=4` SENSIBLE ; `n=1` (sans le 2) donne `⟨TT⟩=2c_W=¼ ℓ²/κ²` = lecture nue γ=1 (casse l'éq.90). VERDICT : `γ=1` n'est PAS forcé — c'est la normalisation NU (opérateur `O=T/2`), un CHOIX ; le canonique forcé est `γ=4` (⟹ `C_T^prog=C_T^dH`, aligné Osborn-Petkos) ; `N_action=1/4` = ÉTIQUETTE de la convention « opérateur nu ». SANS SURCLASSEMENT (§6.4) : « γ=4 canonique / γ=1 convention nue » est de la NORMALISATION au niveau ALGÈBRE, ≠ « D1 fermé / N fixé / CCC démontrée » ; aucune contradiction, PAS de NO-GO ; compte {A4 ; A2★ ; N} INCHANGÉ ; D1 NON clos ; N non fixé."
codename: LC-RACCORD
tags: [module-D, ds-cft, map-operateur, gamma, N_action, de-haro, brown-york, tenseur-de-stress, variation-seconde, action-renormalisee, C_T, convention, canonique, nue, separation-beta-gamma, spectre-aveugle, firewall, eq-90, eq-63, eq-61, sceau, R-2]
type: "chaînon (résultat — scelle la map opérateur ab initio de la tranche R-2 : dictionnaire ⟨TT⟩=γ·ψ₂, γ_canon=4 FORCÉ, séparation β/γ, firewall n=2 ; SCEAU FAIT verif_naction_gamma_dHSS.py ; tranche le statut de N_action=1/4 = convention nue)"
statut: "établi (algèbre), SCEAU FAIT — map opérateur dérivée ab initio. [A] dictionnaire de Haro reproduit : ψ₂=2c_W (coeff. nu), ⟨TT⟩_canon=8c_W=ℓ²/κ²=éq.90 (chaîne 2×2 sur éq.63). [B] γ=⟨TT⟩_canon/ψ₂=4 FORCÉ (deux 2 = définition de T, Brown-York ; pas un choix). [C] N_action=γ/4 ; canonique γ=4⟹N_action=1, C_T^prog=C_T^dH ; nu γ=1⟹N_action=1/4 ; recoupement ratio 4. [D] séparation β/γ : 𝒫 force β=M_Pl²/4, aveugle à γ ⟹ DISJOINTS. [E] firewall : n=2 UNIQUE reproduit éq.90 ⟹ γ=4 SENSIBLE ; n=1 = lecture nue. VERDICT : γ=1 = CONVENTION (O=T/2), canonique forcé = γ=4 ; N_action=1/4 = étiquette de convention nue. SANS SURCLASSEMENT (§6.4) : normalisation au niveau algèbre, JAMAIS « D1 fermé / N fixé / CCC démontrée ». Compte {A4 ; A2★ ; N} inchangé ; D1 non clos ; N non fixé."
statut_id: "validé après sceau (verif_naction_gamma_dHSS.py déposé en KB, EXIT 0, 18 asserts) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §8, lot additif SÉPARÉ, NON exécutée ici) : LC-AUDIT-LOG-NACTION-ALPHA §AF (clôture du verrou : tranché en CONVENTION, pas en M_Pl²/4 posé), LC-AUDIT-VERDICT §8bis, 00_index (+ absorber la dette twin « facteur-2 » du changelog v1.36 → annotation de corps « facteur-2 d'AMPLITUDE ; map γ tranchée »), 03_glossaire (entrées N_action / f_W / Map ⟨TT⟩∝F ; AJOUTER entrée γ), LC-WORK-REPRISE-POST-NACTION §3 R-2 (R-2 tranché = convention), LC-D-CT-DUAL §4 (renvoi : le PRODUIT=4 = γ canonique). NB : la re-lecture interne de R1 (verif_D_CT_constructif) est un pas DISTINCT (cf. §8 (ii)) — PAS une réfutation de R1."
version: 0.1
langue: fr
date: 2026-06-11
maj: "2026-06-11 — v0.1 : scelle la tranche R-2 « map opérateur ab initio » (γ via dHSS), posée par LC-WORK-REPRISE-POST-AUDIT-FROID et LC-WORK-REPRISE-POST-GAMMA-DHSS. verif_naction_gamma_dHSS.py (EXIT 0, 18 asserts, 5 blocs A–E, stack 3.12/sympy 1.14) : [A] ψ₂=δ²W/δh²=2c_W ; ⟨T⟩=2δW/δh=4c_W h ; ⟨TT⟩_canon=2δ⟨T⟩/δh=8c_W=ℓ²/κ² (éq.90) ; [B] γ=⟨TT⟩_canon/ψ₂=4 FORCÉ (deux 2 de éq.63 = définition de T) ; [C] N_action=γ/4 ; γ=4→1 (C_T^prog=C_T^dH), γ=1→1/4 (C_T^prog=¼C_T^dH) ; recoupement (1/8π²)/(1/32π²)=4 ; [D] 𝒫=1/(2|Im F|)=2H²/(M_Pl²k³)⟹β=M_Pl²/4 UNIQUE, γ∉𝒫 (séparation) ; [E] T=n δW/δg : n=2 UNIQUE (éq.90)⟹γ=n²=4 sensible, n=1=lecture nue. VERDICT : γ=1 CONVENTIONNEL (O=T/2), canonique forcé γ=4, N_action=1/4 = étiquette de convention nue. SANS SURCLASSEMENT (§6.4) : « γ=4 / γ=1 » = normalisation algèbre ≠ « D1 fermé / N fixé / CCC démontrée » ; PAS de NO-GO. Aucune touche aux chaînons existants (algèbre ATN/REALITE/DUAL/NONLIN-VERROU intacte ; verif_naction_alpha reste flaggé ERRATUM v1.1, inchangé). Propagation §8 NON exécutée (proposée, lot séparé). Compte {A4 ; A2★ ; N} inchangé ; D1 non clos."
fichier_compagnon: verif_naction_gamma_dHSS.py
prerequis_kb: [LC-AUDIT-LOG-NACTION-ALPHA, LC-WORK-CADRAGE-NACTION-ALPHA, LC-D-CT-DUAL, LC-D-CT-ATN, LC-D-CT-REALITE, LC-WORK-REPRISE-CONSTRUCTIF-R1, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE]
fichiers_compagnons_kb: [verif_naction_alpha.py, verif_naction_aveugle.py, verif_naction_firewall.py, verif_D_CT_ATN.py, verif_D_CT_dual.py, verif_D_CT_constructif.py]
renvois: [LC-AUDIT-LOG-NACTION-ALPHA, LC-WORK-CADRAGE-NACTION-ALPHA, LC-D-CT-DUAL, LC-D-CT-ATN, LC-D-CT-REALITE, LC-WORK-REPRISE-CONSTRUCTIF-R1, LC-D-HOLOGRAPHIE-G3, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] holographie / dS-CFT — fixe le DICTIONNAIRE OPÉRATEUR ⟨TT⟩=γ·ψ₂ entre le coefficient nu de fonction d'onde (ψ₂=δ²W, ce que le programme lit) et le deux-point canonique du tenseur de stress (Brown-York, de Haro éq.63) ; ferme la tranche R-2 de la route α en tranchant que N_action=1/4 est une CONVENTION (opérateur nu), pas une grandeur dérivée. Ne tranche aucune physique."
  - "[D] / route α∪R-2 (audit à froid) — successeur direct de LC-AUDIT-LOG-NACTION-ALPHA §AF : l'audit avait RÉTRACTÉ le surclassement et laissé N_action=1/4 en décision ouverte (pivot f_W≡1/b_prog) ; ce chaînon la tranche au niveau ALGÈBRE comme étiquette de convention nue, le canonique forcé étant γ=4 (C_T^prog=C_T^dH)."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·C_T·γ — Map opérateur `⟨TT⟩=γ·ψ₂` dérivée ab initio (de Haro) ; `γ`canonique`=4` forcé / `γ=1` convention nue (algèbre)

> **But.** `LC-WORK-REPRISE-POST-AUDIT-FROID` recommande de **dériver la map opérateur**
> `⟨TT⟩ = γ·ψ₂` *ab initio* — depuis l'action holographique renormalisée de de Haro
> (arXiv:0808.2054 ; éq. 61/63/90) plus une **variation seconde** — afin de **trancher** si
> `γ=1` (posé par le programme, ⟹ `N_action=1/4`) est **forcé** ou **conventionnel**. C'est la
> dernière tranche ouverte de la route `α∪R-2` après que l'`AUDIT À FROID`
> (`LC-AUDIT-LOG-NACTION-ALPHA §AF`) eut **rétracté** le surclassement et laissé `N_action`
> en **décision ouverte**. **Ce chaînon scelle la dérivation** (`verif_naction_gamma_dHSS.py`,
> EXIT 0, 18 asserts, 5 blocs).
>
> **Verdict (calculé, `verif_naction_gamma_dHSS.py`, EXIT 0 ; 5 blocs A–E).**
> **[A] Dictionnaire de de Haro** `[établi — algèbre]`. `c_W=ℓ²/(8κ²)` (éq. 61) ; le coefficient
> **nu** de fonction d'onde `ψ₂ ≡ δ²W/δh² = 2c_W` (= ce que le programme lit comme `C_T^prog`) ;
> par la définition **universelle** `T=2δW/δg` (éq. 63) appliquée **deux fois** :
> `⟨T⟩=2δW/δh=4c_W h`, `⟨TT⟩`canon`=2δ⟨T⟩/δh=8c_W=ℓ²/κ²` (= **éq. 90** reproduite).
> **[B] Map forcée** `[établi — algèbre ; le cœur]`. `γ ≡ ⟨TT⟩`canon`/ψ₂ = 8c_W/2c_W = 4`. Les
> **deux** facteurs `2` sont les **deux applications de la définition de `T`** (Brown-York), **pas**
> un choix ; le `2` de la dérivée **seconde** est **commun aux deux côtés** et n'entre **pas** dans
> `γ`. **[C] `N_action=γ/4`.** Canonique `γ=4` ⟹ `N_action=1`, `C_T^prog=C_T^dH` (**même** objet,
> `f_W=1`) ; nu `γ=1` (`O=T/2`) ⟹ `N_action=1/4`, `C_T^prog=¼ C_T^dH` ; recoupement
> `(1/8π²)/(1/32π²)=4` (= `f_W` à `γ=1`, recoupe `CT-ATN`/`DUAL`). **[D] Séparation `β/γ`**
> `[établi — algèbre]`. Le spectre `𝒫=1/(2|Im F|)=2H²/(M_Pl²k³)` **force** `β=M_Pl²/4`
> **uniquement** et **ne contient pas** `γ` ⟹ magnitude et map **disjointes** (le spectre est
> **aveugle** à la normalisation opérateur). **[E] Firewall** `[établi — algèbre]`. `T=n δW/δg` :
> **seul** `n=2` reproduit l'éq. 90 ⟹ `γ=n²=4` **sensible** ; `n=1` donne `⟨TT⟩=2c_W=¼ ℓ²/κ²` =
> lecture nue `γ=1` (casse l'éq. 90).
>
> **`γ=1` n'est PAS forcé : il est CONVENTIONNEL** (normalisation de l'opérateur **nu** `O=T/2`).
> Le canonique **forcé** est `γ=4` (⟹ `C_T^prog=C_T^dH`, aligné Osborn-Petkos). **`N_action=1/4`
> est l'étiquette de la convention « opérateur nu »**, à libeller comme telle (branche 2 du `§AF`).
> Discipline `§6.4` : tout cela est de la **normalisation au niveau algèbre**, **jamais**
> « D1 fermé / `N` fixé / CCC démontrée ».

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce chaînon **enregistre un résultat scellé** : la map opérateur entre le coefficient **nu** de
fonction d'onde (`ψ₂=δ²W`, l'objet que le programme manipule depuis `LC-D-HOLOGRAPHIE-G3`) et le
deux-point **canonique** du tenseur de stress (Brown-York, de Haro). Il **tranche** une **décision
de convention** laissée ouverte par l'audit à froid, **au niveau algèbre uniquement**.

Ce qu'il **n'est pas** : il ne ferme **pas** `D1`, ne **fixe pas** `N`, ne **démontre pas** CCC, et
ne **réduit pas** le compte `{A4 ; A2★ ; N}`. Le `γ` est une **normalisation d'opérateur**, pas une
hypothèse physique. Aucune **contradiction** n'est levée ni introduite : il n'y a **pas de NO-GO**.
Le sceau précédent `verif_naction_alpha.py` (route α) reste **flaggé `⚠️ ERRATUM v1.1`** et **n'est
pas modifié** par ce chaînon.

---

## 1. Le résultat, en une ligne `[ce que le sceau confirme]`

`⟨TT⟩`canon` = 4·ψ₂` (forcé par la double application de `T=2δW/δg`) ⟹ `N_action = γ/4` ⟹
**canonique `γ=4` ⟹ `N_action=1` et `C_T^prog=C_T^dH`** ; la valeur `N_action=1/4` du programme est
**l'étiquette d'un choix d'opérateur nu** `O=T/2` (`γ=1`), pas une grandeur dérivée. Le spectre
**force** séparément `β=M_Pl²/4` **sans voir** `γ`.

---

## 2. Le dictionnaire de de Haro : `ψ₂`, `⟨T⟩`, `⟨TT⟩` et l'éq. 90 `[établi — algèbre]`

**Action de bord renormalisée (éq. 61).** `W = c_W ∫ h □^{3/2} h`, avec `c_W = ℓ²/(8κ²)`. En
impulsion, `□^{3/2} → k³` ; on suit le **coefficient** de la forme quadratique.

**Coefficient nu de fonction d'onde.** La variation seconde **nue** de la forme quadratique est
`ψ₂ ≡ δ²W/δh² = 2c_W`. C'est **exactement** ce que le programme lit comme `C_T^prog` (cf.
`LC-D-CT-DUAL §4` : `C_T^prog=2c_W`) — le seul `2` est celui de la dérivée seconde de `h²`.

**Tenseur de stress par sa définition universelle (éq. 63).** `T = 2δW/δg`, appliquée **deux** fois :

```
  ⟨T⟩  = 2 δW/δh        = 4 c_W h
  ⟨TT⟩ = 2 δ⟨T⟩/δh      = 8 c_W      = ℓ²/κ²      (= éq. 90 de de Haro)
```

La valeur `⟨TT⟩`canon`=8c_W=ℓ²/κ²` **reproduit l'éq. 90** : la chaîne `2×2` (deux applications de
la définition de `T`) appliquée à `ψ₂=2c_W` donne le deux-point canonique. (Le sceau vérifie
`⟨TT⟩`canon`−8c_W=0` et `⟨TT⟩`canon`−ℓ²/κ²=0`.)

---

## 3. La map opérateur `γ = ⟨TT⟩`canon`/ψ₂ = 4`, FORCÉE `[établi — algèbre ; le cœur]`

```
         ⟨TT⟩canon      8 c_W
   γ  =  ──────────  =  ──────  =  4
            ψ₂          2 c_W
```

Les **deux** facteurs `2` qui composent `γ=4` sont les **deux applications de la définition de `T`**
(Brown-York `T=2δW/δg`), **pas** un choix de normalisation. Le `2` de la dérivée **seconde** (qui
fait `ψ₂=2c_W`) est **commun aux deux côtés** du quotient et **n'entre donc pas** dans `γ`. Ce sont
exactement les « préfacteurs `W↔⟨TT⟩` » isolés par `LC-D-CT-DUAL §4 v0.4` (part « normalisation du
projecteur `Π` » `=1`, tout le `4` dans les préfacteurs ; PRODUIT `=4` inchangé).

---

## 4. `N_action = γ/4` : lecture canonique vs lecture nue `[établi — algèbre]`

De la sonde (`LC-WORK-REPRISE-POST-AUDIT-FROID §3`) : `⟨TT⟩=γ·ψ₂`, `C_T^prog=γ·(ψ₂/N)`,
`f_W=C_T^dH/C_T^prog=4/γ`, donc `N_action=1/f_W=γ/4`. Le sceau re-vérifie `f_W−4/γ=0` et
`N_action−γ/4=0` symboliquement, puis les deux substitutions :

| normalisation opérateur | `γ` | `C_T^prog/N` | `f_W` | `N_action` | lecture |
|---|---|---|---|---|---|
| **canonique** (`T=2δW/δg`, de Haro / Osborn-Petkos) | **4** | `1/(8π²)` | **1** | **1** | `C_T^prog = C_T^dH` (**même** objet) |
| nue (programme, opérateur `O=T/2`) | 1 | `1/(32π²)` | 4 | 1/4 | `C_T^prog = ¼ C_T^dH` |

**Recoupement des valeurs scellées `/N`.** `(1/8π²)/(1/32π²)=4` : le rapport de la valeur
**canonique** (de Haro, `LC-D-CT-DUAL`) à la valeur **nue** (programme, `LC-D-CT-ATN`) est
exactement `f_W` à `γ=1`. Les deux valeurs déjà scellées sont donc **cohérentes** — elles décrivent
le **même** objet dans **deux conventions d'opérateur**, reliées par le facteur fixe `4`.

**Verdict de convention.** `γ=1` (l'opérateur **nu** `ψ₂`, `O=T/2`) **n'est pas le tenseur de stress
canonique** ; il **n'est donc pas forcé**. Le canonique **forcé** est `γ=4`, qui rend
`C_T^prog=C_T^dH` (cohérence : **même** objet physique) et s'aligne sur Osborn-Petkos. **`N_action=1/4`
est l'étiquette de la convention « opérateur nu »** (branche 2 de la dichotomie `§AF` : « si la
définition de `𝒫` tolère le facteur 2 ⟹ choix de convention »).

---

## 5. Séparation `β/γ` : le spectre force `β`, aveugle à `γ` `[établi — algèbre]`

La partie finie de `F` s'écrit `|Im F|/k³ = β/H²` (avec `β` la **magnitude**, libre). La prescription
dS/CFT du programme donne le spectre `𝒫 = 1/(2|Im F|) = H²/(2β k³)`. Exiger le spectre tensoriel
standard `𝒫 = 2H²/(M_Pl²k³)` impose

```
   β = M_Pl²/4     (UNIQUE solution ; magnitude FORCÉE)
```

et le spectre **ne contient pas** `γ` (`γ ∉ 𝒫.free_symbols`). **Magnitude (`β`) et map (`γ`) sont
donc des objets disjoints** : le spectre fixe `β` **sans rien dire** de la normalisation opérateur.
Ceci confirme l'acquis de l'`AUDIT À FROID` (la magnitude `M_Pl²/4` est l'**unique** porteur du
spectre, posée) et l'**isole** proprement de la question — distincte — de la map.

---

## 6. Firewall : `n=2` est l'unique définition reproduisant l'éq. 90 `[établi — algèbre]`

On injecte des définitions **fausses** de `T` : `T = n δW/δg` avec `n` facteurs au lieu de `2`. Alors
`⟨TT⟩ = n² ψ₂`. Résoudre `n² ψ₂ = ℓ²/κ²` donne `n=2` comme **unique** racine positive
(Brown-York) ⟹ `γ=n²=4` est **sensible** (non tautologique). Contrôles :

- `n=1` (sans le `2`) ⟹ `⟨TT⟩=2c_W ≠ ℓ²/κ²` : **casse** l'éq. 90 ;
- et `n=1` reproduit **exactement** `2c_W = ¼·ℓ²/κ²` = la **lecture nue** `γ=1`.

Le résultat dépend donc de la **vraie** définition du tenseur de stress, pas d'un ajustement.

---

## 7. Format de chaînon

- **Type.** Résultat scellé autonome (`verif_naction_gamma_dHSS.py`, EXIT 0, 18 asserts, 5 blocs
  A–E ; stack Python 3.12 / sympy 1.14). Successeur de `LC-AUDIT-LOG-NACTION-ALPHA §AF`.
- **Statut épistémique.** `établi (algèbre)` : algèbre correcte + cibles reproduites (éq. 90,
  spectre `2H²/(M_Pl²k³)`, recoupement des valeurs scellées). Le **verdict de convention** (`γ=4`
  canonique / `γ=1` nue) est `établi (algèbre)` ; rien d'autre n'est affirmé.
- **Conditionnalités.** Conditionnel aux **prescriptions exhibées** : définition de `T` (éq. 63),
  ancrage de `|Im F|` sur le spectre vérifié, lecture `ψ₂=δ²W`. `d=3`.
- **Ce qui reste hors de ce chaînon.** La **re-lecture interne de `verif_D_CT_constructif` (R1)**
  est un pas **distinct** (cf. §8 (ii)) — **non** une réfutation de R1 ; et la fixation de `N` (≡Λ)
  reste `hors de portée`.

---

## 8. Propagation / housekeeping `[à appliquer — note de reprise séparée ; NON exécutée]`

Lot **additif** (ancres `count==1`, contrôles de delta de lignes ; suppressions ⊆ `{version, maj}`),
à conduire **après dépôt** de ce chaînon :

1. **`LC-AUDIT-LOG-NACTION-ALPHA §AF`** — clôture du verrou : `N_action=1/4` **tranché en
   CONVENTION** (opérateur nu `O=T/2`), **pas** en « `M_Pl²/4` posé » ; canonique forcé `γ=4`.
2. **`LC-AUDIT-VERDICT §8bis`** — enregistrement du chaînon `LC-D-CT-GAMMA` (établi-algèbre,
   convention tranchée, sans surclassement).
3. **`00_index`** — ligne carte `LC-D-CT-GAMMA` ; **absorber la dette twin « facteur-2 »** (le
   libellé ancien ne subsiste qu'en entrée de changelog `maj:` v1.36) en annotation de corps :
   « facteur-2 d'**AMPLITUDE** levé ; **map `γ` tranchée** (convention nue / canonique `γ=4`) ».
4. **`03_glossaire`** — entrées `N_action`, `f_W`, `Map ⟨TT⟩∝F` alignées ; **ajouter** l'entrée `γ`
   (map opérateur ; `γ=4` canonique forcé / `γ=1` convention nue ; `N_action=γ/4`).
5. **`LC-WORK-REPRISE-POST-NACTION §3 R-2`** — R-2 **tranché = convention** (renvoi).
6. **`LC-D-CT-DUAL §4`** — renvoi : le PRODUIT `=4` du facteur de convention **est** `γ` canonique.

**(ii) Pas DISTINCT — re-lecture interne de `verif_D_CT_constructif` (R1).** `[C]` de R1 passe à
`N_action=1/4` car sa **cible** est la valeur **nue** `1/(32π²)`. Deux lectures cohérentes restent
ouvertes (corriger cible **et** valeur vers le canonique `1/(8π²)`, `N_action=1` ⟹ `[C]` re-passe ;
**ou** garder R1 en convention nue et l'**annoter**). **Ce n'est PAS une réfutation de R1** — une
dépendance de convention à expliciter. Trancher exige de relire la structure interne du sceau (carte
`N_FT=π²/24=1/κ`, branche P2.7 position/OP, test `N_cin·κ₃=?1/(32π)`). **Non fait ici.**

---

## 9. Renvois, glossaire, références

- **Amont.** `LC-AUDIT-LOG-NACTION-ALPHA §AF` (audit à froid : surclassement rétracté, pivot
  `f_W≡1/b_prog`) ; `LC-WORK-CADRAGE-NACTION-ALPHA` ; `LC-D-CT-DUAL §4` (facteur de convention `=4`,
  préfacteurs `W↔⟨TT⟩`) ; `LC-D-CT-ATN` (`C_T^prog/N=1/(32π²)`, candidat-égalité `A_T·N=16`) ;
  `LC-D-CT-REALITE` (observable `𝒫` robuste) ; `LC-D-HOLOGRAPHIE-G3` (lecture `ψ₂`).
- **Aval.** `LC-WORK-REPRISE-CONSTRUCTIF-R1` (re-lecture de R1, §8 (ii)) ; `LC-AUDIT-VERDICT §8bis` ;
  `00_index` ; `03_glossaire` ; `04_references`.
- **Référence.** de Haro, *Dual gravitons in AdS₄/CFT₃ and the holographic Cotton tensor*,
  arXiv:0808.2054 (JHEP 01 (2009) 042), éq. 61 / 63 / 90 — **déjà en KB** (`04_references`).
- **Glossaire (à compléter, §8.4).** `γ` (map opérateur) ; `ψ₂` (coeff. nu de fonction d'onde
  `=δ²W=2c_W`) ; `N_action` (`=γ/4`) ; `f_W` (`=4/γ`) ; `c_W` (`=ℓ²/(8κ²)`).

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. `N≡Λ`).
