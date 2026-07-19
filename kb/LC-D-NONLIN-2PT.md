---
id: LC-D-NONLIN-2PT
titre: "Module A↔D — VERROU NON-LINÉAIRE DU DEUX-POINT (rang 2), SCELLÉ : sous A3 + Ward exactes (d=3 impair, pas d'anomalie), la FORME du deux-point du secteur de Weyl rescalé COMPLET (E⊕B, DEUX parités) est FORCÉE par la seule théorie des représentations — k³·Π^TT, liberté résiduelle = UNE amplitude (celle déjà pendue à N via C_T). Analogue RANG 2 du triptyque LC-D-NONLIN-VERROU : la relation d'état BD (perturbative, mode par mode, LC-D3-SPECTRE-K3) est REMPLACÉE par un argument d'INVARIANCE (non-perturbatif) ; elle n'intervient plus qu'en REFERMETURE (cas particulier de contrôle). Sceau UNIQUE à blocs verif_nonlin_deuxpoint.py (EXIT 0, 41 asserts, deux phases — phase 1 interne EXIT 0 AVANT tout fetch, sha256 ad13634…74ff déposé, asserts 1-27 byte-identiques dans la version finale). RÉSULTATS : [A] C1 — l'espace des structures PAIRES invariantes du deux-point TT spin-2, Δ=d=3, est de DIMENSION 1 (symbolique ẑ + 50 directions SVD) ; solution ∝ Π^TT ; complétude hélicités ±2 ; k³=(k²)^{3/2} NON-analytique ⟹ RADIATIF. [B] C2 — secteur IMPAIR de dimension 1 ET de type CONTACT (k³·S^odd POLYNOMIAL ⟹ local) ; pseudo-tenseur ; orthogonal au pair ⟹ AUCUNE amplitude radiative neuve ; la scission radiatif/contact suit EXACTEMENT la frontière de parité ; cohérent « impaire hors bispectre » (NONGAUSS [D]). [C] C3 — Cotton linéarisé DÉRIVÉ AB INITIO : C^lin=(i/2)k³·(Dh) (coefficient ½ sorti du Ricci linéarisé) ; D²=−𝟙 sur TT recoupe S²=−𝟙 (CT-DUAL) INDÉPENDAMMENT ; refermeture BD : ⟨EE⟩,⟨BB⟩ ∝ k³ ; ⟨EB⟩ radiatif NUL sur BD (double fermeture du canal impair : représentation ET état). [D/E] comparanda KB fetchés APRÈS phase 1 : OP (2.23)-(2.24) = 1 structure / 1 constante ⟹ C1 CONFIRMÉE ; de Haro (47) coefficient Cotton ½ ⟹ convergence slack nul ; de Haro (49)/(50) ⟹ ÉQUIPARTITION ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩=1 EXACTE en unités de dualité — cas catalogue {2,4,8} (2 des préfacteurs vs ½ du Cotton) identifié et RÉSOLU, produit net 1 ; map prog↔dH=κ²/(Hℓ²) facteur fixe pur ; dictionnaire FT : Γ(−3/2) FINIE (d=3 pole-free), c_FT=π²/12. [F] firewall 5/5 (Δ≠3 ; d=4 ⟹ pôle Γ(−2) — spécificité d=3 STRUCTURELLE ; Cotton ×2 ⟹ ratio 4≠1 ; trace annihilée par Π^TT ; n≠2). R-7 : cibles gelées au cadrage TENUES TELLES QU'ÉCRITES, ZÉRO amendement. EFFET : « liberté résiduelle de D1 au niveau gaussien = UNE amplitude A_T~1/N » passe de `établi perturbatif TT` à `établi` PAR INVARIANCE (secteur complet, deux parités). SANS SURCLASSEMENT (§6.4) : forme verrouillée = comptage de représentation — JAMAIS « A3 dérivé / deux-point dérivé / D1 clos / N fixé / CCC démontrée » ; le k³ RESTE la donnée de Cauchy irréductible, pendue à N seul ; conditionnel à A3 ; spécifique d=3. Compte {A4 ; A2★ ; N} INCHANGÉ."
codename: LC-RACCORD
tags: [module-A, module-D, front-a, A3, A4, weyl-rescale, electrique-magnetique, cotton-york, deux-points, spectre, k3, representation, spin-2, helicite, parite, pseudo-tenseur, contact, radiatif, equipartition, dualite, S-dualite, ds-cft, non-lineaire, osborn-petkou, de-haro, sceau, D1, R-7]
type: "chaînon (résultat — scelle le verrou NON-LINÉAIRE du deux-point sur le secteur de Weyl complet ; analogue rang 2 de LC-D-NONLIN-VERROU ; cadrage LC-WORK-CADRAGE-NONLIN-2PT v0.1 ; SCEAU FAIT verif_nonlin_deuxpoint.py, deux phases, 41 asserts)"
statut: "établi (algèbre), SCEAU FAIT — C1 : dimension paire = 1, forme k³·Π^TT forcée (interne + OP 2.23) ; C2 : impair dimension 1 ET contact (interne + cohérence OP points séparés) — aucune amplitude radiative neuve ; C3 : Cotton (i/2)k³ ab initio ≡ dH (47), équipartition ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ exacte (dH 49/50), D²=−𝟙 recoupe S²=−𝟙, ⟨EB⟩ radiatif nul sur BD ; C4 : 0 entrée libre < 3 sorties appariées, cas {2,4,8} résolu. R-7 : zéro amendement des cibles gelées. EFFET : résidu gaussien de D1 = UNE amplitude — relevé de `établi perturbatif TT` à `établi` par invariance. NON SCELLÉ / inchangé : l'amplitude elle-même (A_T~1/N, décision ouverte) ; A3 non dérivé ; D1 non clos ; compte {A4 ; A2★ ; N} inchangé."
version: 0.1
langue: fr
date: 2026-06-12
maj: "2026-06-12 — v0.1 : scelle le verrou non-linéaire du deux-point (rang 2), exécution du front §3.1 (cadrage LC-WORK-CADRAGE-NONLIN-2PT v0.1, quatre décisions de scoping tranchées, cibles C1-C4 gelées, R-7 active). Sceau unique à blocs verif_nonlin_deuxpoint.py : phase 1 interne (blocs [A][B][C], 27 asserts) écrite et EXIT 0 AVANT tout fetch (version déposée, sha256 ad13634…74ff), puis phase 2 (blocs [D][E][F], 14 asserts) après lecture des comparanda KB (OP 9307010 p.7-8 ; de Haro 0808.2054 p.13-14 — archives ZIP/JPEG, OCR embarqué). Asserts 1-27 byte-identiques entre les deux versions. Mutations pilotes : Cotton ×2 ⟹ assert 22 CASSE ; préfacteur E ×2 ⟹ nombre pur porté bouge (×4), formes k insensibles — comportement attendu, discriminé en phase 2 (équipartition). Notes d'honnêteté §5. Propagation §6 NON exécutée (proposée, lot séparé)."
statut_id: "validé après sceau (verif_nonlin_deuxpoint.py déposé en KB, EXIT 0, 41 asserts) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §6, lot séparé) : LC-D-NONLIN-VERROU §4 (le résidu deux-point passe de « décision ouverte » à « forme verrouillée, amplitude seule libre »), LC-D3-SPECTRE-K3 §renvoi, LC-WORK-D1-E-AMPLITUDE §renvoi (relevé non-perturbatif), LC-D-CT-DUAL §renvoi (D²=−𝟙 recoupé), LC-AUDIT-VERDICT §8bis, LC-00-INDEX, 03_glossaire, 02_programme, 04_references (OP et de Haro DÉJÀ en KB)."
fichier_compagnon: verif_nonlin_deuxpoint.py
prerequis_kb: [LC-WORK-CADRAGE-NONLIN-2PT, LC-D-NONLIN-VERROU, LC-D3-SPECTRE-K3, LC-D-CT-DUAL, LC-D-CT-ATN, LC-D-CT-GAMMA, LC-D-HOLOGRAPHIE-G3, LC-D3-WEYL-BUNCHDAVIES, LC-WORK-D1-E-AMPLITUDE, LC-D-NONGAUSS-TTT, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: [verif_nonlin_repr.py, verif_nonlin_cotton.py, verif_nonlin_parity.py, verif_D3_spectre_k3.py, verif_D_CT_dual.py, verif_D3_bunchdavies.py]
renvois: [LC-WORK-CADRAGE-NONLIN-2PT, LC-D-NONLIN-VERROU, LC-D3-SPECTRE-K3, LC-D-CT-DUAL, LC-D-CT-ATN, LC-WORK-D1-E-AMPLITUDE, LC-D-NONGAUSS-TTT, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[A] / front (a) — verrouille la FORME du deux-point du Weyl complet (E⊕B) par invariance, non-perturbativement ; l'écart A3/A4, qui vit au deux-point (NONLIN-VERROU §0), se réduit à UNE amplitude. Ne dérive ni A3 ni A4 ; D1 non clos."
  - "[D] holographie / dS-CFT — repose sur les Ward EXACTES de d impair (g₃ pur spin-2 tous ordres) + comptage des structures invariantes ; confirmé par OP (2.23) et de Haro (47),(49)-(51) ; équipartition ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ exacte ; D²=−𝟙 recoupe la carte S."
tags_epistemiques: [établi (algèbre), formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·NONLIN·2PT — Verrou NON-LINÉAIRE du DEUX-POINT (rang 2), scellé

> **But.** `LC-D-NONLIN-VERROU` a porté le **un-point** du Weyl rescalé complet à `établi`
> non-perturbatif, en laissant le **deux-point** `⟨g₃g₃⟩∝k³` au niveau **perturbatif TT**
> (`LC-D3-SPECTRE-K3`, via la relation d'état BD) et en notant que l'écart A3/A4 « vit
> entièrement au deux-point ». Ce chaînon exécute le front §3.1 (cadrage
> `LC-WORK-CADRAGE-NONLIN-2PT`, cibles gelées, R-7 active) : il **remplace** la relation
> d'état (perturbative) par un argument d'**invariance** (non-perturbatif).
>
> **Thèse.** Sous **A3** + Ward exactes (`d=3` impair, pas d'anomalie ⟹ `g₃` pur spin-2
> tous ordres), la **forme** du deux-point du secteur de Weyl complet — `E⊕B`, deux
> parités — est **forcée** : `k³·Π^TT` dans le pair, contact pur dans l'impair. **Toute**
> la liberté résiduelle tient en **une amplitude** : celle déjà pendue à `N` (`C_T∝N`).
>
> **Verdict (calculé, `verif_nonlin_deuxpoint.py`, EXIT 0, 41 asserts, 2 phases).**
> **(C1)** L'espace des structures **paires** invariantes du deux-point d'un opérateur TT
> spin-2, `Δ=d=3`, est de **dimension 1** (symbolique `ẑ` + 50 directions SVD) ; solution
> `∝Π^TT` ; `k³=(k²)^{3/2}` **non-analytique** ⟹ radiatif. **Confirmé** : OP (2.23)-(2.24)
> — une structure, une constante. `[établi — algèbre]`
> **(C2)** Le secteur **impair** est de dimension 1 **et de type contact** (`k³·S^odd`
> polynomial ⟹ local) ⟹ **aucune amplitude radiative neuve** ; la scission
> radiatif/contact suit **exactement** la frontière de parité. Cohérent OP (points
> séparés) et « impaire hors bispectre » (rang 3). `[établi — algèbre]`
> **(C3)** Cotton linéarisé **dérivé ab initio** : `C^lin=(i/2)k³·(Dh)` — coefficient `½`
> identique à de Haro (47), **slack nul** ; `D²=−𝟙` sur TT **recoupe `S²=−𝟙`**
> (CT-DUAL) indépendamment ; refermeture BD : `⟨EE⟩,⟨BB⟩∝k³` ; **équipartition
> `⟨𝓑𝓑⟩/⟨𝓔𝓔⟩=1` exacte** en unités de dualité (dH 49/50) ; `⟨EB⟩` radiatif **nul** sur
> BD. `[établi — algèbre]`
> **(C4)** 0 entrée libre < 3 sorties appariées ; le cas `{2,4,8}` (le `2` des
> préfacteurs vs le `½` du Cotton) **identifié et résolu**, produit net 1. `[tenue]`
>
> ⟹ **Le résidu gaussien de D1 — « une amplitude `A_T~1/N` » — passe de
> `établi perturbatif TT` à `établi` PAR INVARIANCE** (secteur complet, deux parités).

---

## 0. Rôle et garde-fou

Ce chaînon est un **résultat de comptage** (théorie des représentations), pas une
démonstration physique. Discipline `LC-AUDIT-VERDICT §6.4` :

- **La forme est verrouillée, pas la donnée.** Le `k³` reste la **donnée de Cauchy
  radiative irréductible** de `[D]` ; ce qui est gagné est que **rien d'autre** que son
  amplitude n'est libre. **A3 et A4 ne fusionnent toujours pas** — leur écart, qui vivait
  « au deux-point », se concentre maintenant en **un seul nombre** (pendu à `N`).
- **Conditionnel à A3** (état dS-invariant) : on ne dérive pas A3. **Spécifique `d=3`**
  (Ward exactes en `d` impair ; `Γ(−3/2)` finie — firewall F-2 : en `d=4` le pôle
  `Γ(−2)` signale l'anomalie, la spécificité est **structurelle**).
- **`A_T` elle-même** reste `décision ouverte` (`LC-WORK-D1-E-AMPLITUDE`) ; **D1 non
  clos** ; **`N` non fixé** (circularité `LC-E` intacte) ; **pas la CCC**.

---

## 1. La thèse, en une ligne `[ce que le sceau scelle]`

$$\langle (E\oplus B)\,(E\oplus B)\rangle\;=\;\underbrace{A\cdot k^{3}\,\Pi^{TT}}_{\text{pair — RADIATIF, dim 1}}\;\oplus\;\underbrace{(\text{contact local})}_{\text{impair — dim 1, polynomial}},\qquad A\ \text{unique}\ (\,C_T\propto N\,).$$

Le rang 1 (`NONLIN-VERROU`) tenait du fait que `spin-2 ∩ invariants = {0}` au un-point.
Au deux-point l'intersection n'est **plus vide** — la question devient une question de
**dimension**, et la réponse est **1 par parité**, l'impair étant de surcroît **contact**.

---

## 2. Le sceau — deux phases, six blocs `[établi — algèbre]`

### Phase 1 — interne, écrite et EXIT 0 AVANT tout fetch (asserts 1-27)

- **[A] Catalogue pair (C1).** Les 5 monômes `{δ,k̂}` symétrisés ; contraintes TT (trace +
  transversalité, deux paires) ⟹ espace de solutions de **dimension 1**, solution
  `∝Π^TT` (facteur ½ explicite) ; idempotence, complétude hélicités `±2`
  (`Π^TT=e⁺⊗e⁺*+e⁻⊗e⁻*`), pas d'hélicité 0 ; puissance `k^{2Δ-d}=k³` ;
  `k³=(k²)^{3/2}` **non-analytique** ⟹ radiatif ; confirmation **numérique** sur 50
  directions aléatoires (SVD).
- **[B] Catalogue impair (C2).** Monômes `ε_{abm}k̂_m×{δ,k̂k̂}` ; TT ⟹ **dimension 1** ;
  symétrie d'échange `X_{kl,ij}(−k̂)=X_{ij,kl}(k̂)` vérifiée ; `k³·S^odd` **polynomial**
  en `(k_x,k_y,k_z)` ⟹ **contact/local** ; pseudo-tenseur sous réflexion (vs `Π^TT`
  tenseur vrai) ; orthogonal au pair — **aucun mélange**.
- **[C] Refermeture BD (C3, partie interne).** Opérateur de courbure `D` : diagonal sur
  les hélicités (`λ_±` purs `±i`), **`D²=−𝟙`** sur TT — **recoupement structurel,
  indépendant, de `S²=−𝟙`** (CT-DUAL [A]). Cotton linéarisé **ab initio** depuis le
  Ricci linéarisé d'une perturbation TT : `C^lin=(i/2)k³·(Dh)`, coefficient **dérivé**.
  Chaîne BD ⟹ `⟨EE⟩,⟨BB⟩∝k³` (pentes log = 3) ; ratio k-indépendant ; `⟨EB⟩` radiatif
  `∝λ̄₊(P₊−P₋)` ⟹ **nul** sur BD parité-symétrique — **double fermeture** du canal
  impair (représentation [B] **et** état [C]).

### Phase 2 — comparanda KB (asserts 28-41), APRÈS l'EXIT 0 de phase 1

- **[D] Épinglage fetché.** Dictionnaire FT : `(x²)^{−3}→(π²/12)k³` en `d=3`,
  `Γ(−3/2)` **finie** (pas de log). **OP (2.23)-(2.24)** : `⟨TT⟩=C_T 𝓘/x^{2d}` —
  **une** structure, **une** constante, paire, points séparés. **de Haro (47)** :
  `2C=−|p|³P` ⟹ `|coeff|=½` ≡ ab initio, slack nul. **de Haro (49)/(50)** :
  `𝓔=−(ℓ²/2κ²)P`, `𝓑=(ℓ²/κ²)C[h₀]` ⟹ **équipartition `⟨𝓑𝓑⟩/⟨𝓔𝓔⟩=1` EXACTE** ;
  le cas `{2,4,8}` (préfacteur `2` vs Cotton `½`) **résolu**, produit net 1.
- **[E] Tests centraux.** C1 confirmée (interne ≡ OP) ; C2 confirmée (contact interne ≡
  invisibilité à points séparés) ; C3 confirmée et épinglée (ratio 1 ; map prog↔dH
  `=κ²/(Hℓ²)`, facteur fixe pur) ; C4 tenue.
- **[F] Firewall (5/5, tout CASSE).** `Δ=2⟹k¹≠k³` ; `d=4⟹Γ(−2)` pôle ; Cotton
  `×2⟹ratio 4≠1` ; trace/hélicité-0 annihilée par `Π^TT` ; `n≠2⟹γ=n²≠4`.

---

## 3. Synthèse `[le tableau ; portée §6.4]`

| secteur | parité | dimension | nature | comparandum | verdict |
|---|---|---|---|---|---|
| pair | paire | **1** (`∝Π^TT·k³`) | **radiatif** (`(k²)^{3/2}`) | OP (2.23) : 1 structure | C1 **confirmée** |
| impair | impaire | **1** | **contact** (polynomial) | absent à points séparés (OP) | C2 **confirmée** |
| refermeture BD | — | ratios fixés | `⟨𝓑𝓑⟩=⟨𝓔𝓔⟩` exact ; `⟨EB⟩`=0 | dH (47),(49)-(51) | C3 **confirmée** |

**Effet (réduction interne).** Le constat « liberté résiduelle de D1 au niveau gaussien =
**une** amplitude `A_T~1/N` » (`LC-WORK-D1-E-AMPLITUDE`, alors adossé au perturbatif TT)
est **relevé** : il tient désormais **par invariance**, sur le secteur de Weyl **complet**,
**deux parités**, sans recours à la relation d'état BD (réservée à la refermeture).

**Portée (anti-surclassement, §6.4) :** forme verrouillée ≠ donnée dérivée — le `k³`
**reste** la donnée de Cauchy irréductible, pendue à `N` seul ; conditionnel à A3 ;
spécifique `d=3` ; `A_T` ouverte ; **D1 non clos** ; compte `{A4 ; A2★ ; N}` **inchangé**.

---

## 4. R-7 — bilan d'application `[zéro amendement]`

Les cibles C1-C4 ont été **gelées au cadrage** (`LC-WORK-CADRAGE-NONLIN-2PT §3`,
validé avant exécution) et **tenues telles qu'écrites**. **Aucune décision de scoping
réductrice** n'est intervenue après le gel ⟹ **aucun amendement** n'était requis.
La frontière de phase a été respectée : phase 1 écrite, EXIT 0 et **déposée**
(sha256 `ad13634…74ff`) **avant** l'ouverture des comparanda ; les asserts 1-27 sont
**byte-identiques** entre la version phase-1 et la version finale (vérifié au diff).

---

## 5. Notes d'honnêteté `[consignées, pattern R-1]`

- **Quatre corrections en développement de phase 1**, toutes de plomberie de test,
  aucune orientée vers les cibles : (i) assert 03 — comparaison à proportionnalité près
  (normalisation explicite λ=½) au lieu d'égalité brute ; (ii) assert 06 — réécriture
  trig↔exp pour la simplification ; (iii) assert 09 — passage du multi-directions en
  numérique (SVD) pour le coût ; (iv) assert 25 — le signe `λ̄₊` était **codé en dur du
  mauvais côté** ; corrigé en le **dérivant** (préfacteur exprimé par `λ̄₊` calculé),
  jamais en l'ajustant à la cible.
- **Mutations pilotes** (pouvoir discriminant prouvé avant livraison) : Cotton `i/2→i`
  ⟹ assert 22 **CASSE** ✓ ; préfacteur `E` `×2` ⟹ les formes en `k` (asserts 23-24)
  tiennent mais le **nombre pur porté bouge** (`×4`) — comportement attendu en phase 1
  (le nombre y est *porté*, pas testé) ; c'est l'équipartition de phase 2 (assert 39 :
  `×2 ⟹ ratio 4≠1` CASSE) qui le discrimine.
- **Accès comparanda** : OP 9307010 et de Haro 0808.2054 sont des archives ZIP de pages
  JPEG avec OCR embarqué (`.txt`) ; pages lues : OP p.7-8 (éq. 2.22-2.27) ; dH p.13-14
  (éq. 43-53). Aucune autre page consultée.

---

## 6. Propagation / housekeeping `[à appliquer — lot séparé, sur validation]`

Propagation **additive** proposée (NON exécutée ici) :
- **`LC-D-NONLIN-VERROU §4`** : le premier point ouvert (« Le deux-point ») est précisé —
  la **forme** est désormais verrouillée par invariance (ce chaînon) ; reste l'amplitude.
- **`LC-D3-SPECTRE-K3 §renvoi`** : la chaîne `k³` perturbative est refermée comme cas
  particulier du verrou de forme.
- **`LC-WORK-D1-E-AMPLITUDE §renvoi`** : le « résidu = une amplitude » relevé en
  non-perturbatif.
- **`LC-D-CT-DUAL §renvoi`** : `D²=−𝟙` dérivé indépendamment au niveau Cotton
  linéarisé — recoupement de `S²=−𝟙` ; équipartition exacte en unités (49)/(50).
- **`LC-AUDIT-VERDICT §8bis`** : bullet daté (verdict au sens strict §6.4 ; R-7
  appliquée, zéro amendement).
- **`LC-00-INDEX`** (ligne carte + changelog), **`02-PROGRAMME`**, **`03-GLOSSAIRE`**
  (entrées : *verrou de forme du deux-point* ; *scission radiatif/contact par parité* ;
  *équipartition `⟨𝓑𝓑⟩=⟨𝓔𝓔⟩`* ; *opérateur `D`, `D²=−𝟙`*).
- **`04-REFERENCES`** : OP 9307010 et de Haro 0808.2054 **déjà en KB** (web-vérifiées
  aux lots antérieurs) — renvois d'équations seulement ((2.23)-(2.24) ; (43)-(53)).

---

## 7. Renvois, glossaire, références

- **Cadrage** : `LC-WORK-CADRAGE-NONLIN-2PT` (cibles gelées, décisions de scoping).
- **Parent rang 1** : `LC-D-NONLIN-VERROU` (un-point, triptyque).
- **Parent perturbatif** : `LC-D3-SPECTRE-K3` (chaîne `k³` TT, relation d'état BD).
- **Dualité au deux-point** : `LC-D-CT-DUAL` (carte `S`, `S²=−𝟙`, éq. 43-51, 61-63, 90).
- **Amplitude** : `LC-WORK-D1-E-AMPLITUDE` (`A_T~1/C_T~1/N`) ; `LC-D-CT-ATN` (`C_T∝N`
  géométrique).
- **Rang 3** : `LC-D-NONGAUSS-TTT` (impaire hors bispectre — cohérence trans-rang).
- **Références (`LC-04`, en KB)** : Osborn–Petkou, Ann. Phys. **231**, 311 (1994),
  hep-th/9307010, éq. (2.23)-(2.24) ; de Haro, JHEP **01** (2009) 042, arXiv:0808.2054,
  éq. (43)-(53).

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. `N≡Λ`).
