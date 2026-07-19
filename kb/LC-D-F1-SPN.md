---
id: LC-D-F1-SPN
titre: "Front F1 (branche FALSIFIABILITÉ) — PONT CONSTRUCTIF Sp(N), verdict (v0.1, SCEAU). Teste le falsifiable POSITIF de LC-E-N-CROSSCHECK (c) en confrontant le coefficient pur du programme à un modèle dS/CFT EXPLICITE (Sp(N)/AHS, déjà en KB). RÉSULTAT À DEUX ÉTAGES : (STRUCTURE) Sp(N) reproduit le signe C_T<0, la proportionnalité ∝N et le mécanisme holographique ⟨J^(s)J^(s)⟩∝ℓ²/G_N (A.10/A.11 AHS), avec identification N(rang)↔ℓ²/G_N dans Vasiliev (C2=1/2N) — CONCORDANT, CONSOLIDATION (renforce LC-D-SPN et le mécanisme (4) de LC-WORK-D-CT-CADRAGE §3). (COEFFICIENT) |C_T^Sp(N)|/N = 3/(32π²) (Osborn-Petkou, N scalaires libres |_{N→−N}) vs cible gelée 3/(4π⁴) ⟹ écart EXACT π²/8 ≠ 1 — NON concordant. Ce facteur EST la signature de l'obstacle O1 (higher-spin/scalaires ≠ Einstein) : le même 8/π² sépare graviton-programme et scalaire libre en impulsion. Issue LC-WORK-D-CT-CADRAGE §6 : (A) à la structure, (B) au coefficient — le désaccord LOCALISE le fossé dS/CFT↔inflation. CONCLUSION : le pont constructif Sp(N) NE BRANCHE PAS le falsifiable positif (le coefficient 1/(32π²) reste spécifique au secteur graviton d'Einstein, non reproductible par le modèle vectoriel higher-spin). Sceau verif_F1_spn.py (EXIT 0, 20 asserts, sha256 19a4931e6f20, firewall 5/5 dont 2 mutations cassantes vérifiées). F1-G1 (A_T·N=16) NON testable (O1, consigné). SANS SURCLASSEMENT (§6.4) : extraction + confrontation `établi (algèbre)` ; compte {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
codename: LC-RACCORD
prerequis_kb: [LC-WORK-CADRAGE-SPN, LC-D-SPN]
tags: [F1, branche-falsifiabilite, Sp(N), AHS, dS-CFT, higher-spin, C_T, A_T·N, falsifiable-positif, O1, fossé-dS-CFT-inflation, §6.4, sceau]
type: "chaînon (verdict — NON scellant pour la CFT de raccordement). Successeur de LC-D-SPN (sous-front (b)). Subordonné à LC-AUDIT-VERDICT §6.4."
statut: "établi (algèbre) — F1 / pont constructif Sp(N). STRUCTURE concordante (signe<0, ∝N, holographique) = CONSOLIDATION ; COEFFICIENT non concordant (écart π²/8) = signature O1 (higher-spin ≠ Einstein), localise le fossé dS/CFT↔inflation. Le falsifiable POSITIF (coefficient testable indépendamment) N'EST PAS branché par Sp(N) — le coefficient reste pendu au secteur graviton d'Einstein. Cibles gelées (cadrage v0.1, AVANT extraction) tenues telles qu'écrites, R-7. Compte {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
version: 0.2
maj: "2026-07-06 — v0.2 : hygiène (§1.4.2 reprise V54) — ajout de l'arête prerequis_kb: [LC-WORK-CADRAGE-SPN, LC-D-SPN] (recollage de l'in-degree structurel : cadrage gelé v0.1 cité en statut/maj + succession déclarée à LC-D-SPN). Additif, 0 ligne de corps perdue, aucun changement de substance ; établi (algèbre) inchangé ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée. | 2026-06-13 — v0.1 : exécution F1 sur GO Thierry (scopings S-F1-1 C_T/N seul, S-F1-2 AHS déjà en KB, S-F1-3 sceau, S-F1-4 audit différé). Gel déposé AVANT extraction (anti-fit). Sceau verif_F1_spn.py (EXIT 0, 20 asserts, sha 19a4931e6f20). Source 1108.5735v1 (AHS) : (A.10) ⟨JJ⟩_EAdS=+(ℓ²/G)f, (A.11) ⟨JJ⟩_dS=−(ℓ²/G)f, (3.7/3.8) C2→−C2≡N→−N, C2=1/(2N), spins pairs. Verdict deux étages (structure CONCORDANTE / coefficient NON, écart π²/8=O1). Falsifiable positif NON branché par Sp(N)."
---

# F1 — pont constructif Sp(N) : verdict

> **§6.4.** `établi (algèbre)` = l'extraction AHS et les confrontations sont correctes. Ce chaînon
> **ne** permet **pas** de dire « CFT de raccordement identifiée / falsifiable positif tranché /
> D1 clos / `N` fixé / CCC démontrée ». Le gel des cibles (cadrage F1 v0.1) précède l'extraction
> (anti-fit) ; **R-7** : zéro amendement.

---

## 1. Question et dispositif `[falsifiable positif, LC-E-N-CROSSCHECK (c)]`

Le falsifiable **positif** du programme est le **coefficient pur** `C_T/N` (et `A_T·N`), testable
**seulement** là où `C_T`/`A_T` **et** `N` sont accessibles **indépendamment** du scellement
holographique interne (où tout est `f(N)`, cf. `LC-E-N-CROSSCHECK` (a)). F1 cherche cet accès dans
un **modèle dS/CFT explicite** : **Sp(N)/AHS** (`N` = rang, paramètre indépendant). C'est le *test
de cohérence positif* appelé par `LC-WORK-D-CT-CADRAGE §6`.

---

## 2. Extraction AHS `[établi — telle qu'imprimée, 1108.5735v1]`

| Réf. AHS | Contenu extrait |
|---|---|
| (A.10)/(A.11) | `⟨J^(s)J^(s)⟩_EAdS = +(ℓ²_AdS/G_N)f` ; `⟨J^(s)J^(s)⟩_dS = −(ℓ²_dS/G_N)f` — **signe −**, ∀ spin pair (dont **s=2** = tenseur de stress) |
| (3.7)/(3.8) | `C2 → −C2 ≡ N → −N` (`O(−N)=Sp(N)`) |
| p.8 / p.10 | `C2 ∼ −G_NΛ ∼ 1/N` et `C2 = 1/(2N)` ⟹ `ℓ²/G_N ∼ N` (**rang**) **dans Vasiliev** |
| p.4 | courants singlets conservés de spins **pairs** ; modèle = **scalaires** (vecteur) |

⟹ pour le tenseur de stress : `C_T^Sp(N) ∝ −ℓ²/G_N ∼ −N`, **signe négatif**.

---

## 3. Confrontation aux cibles gelées `[établi — sceau verif_F1_spn.py]`

| Cible gelée | Sp(N) (extrait) | Verdict |
|---|---|---|
| **F1-G3** `sign(C_T) < 0` | `< 0` (A.11, Fermi) | **CONCORDANT** (déjà acquis LC-D-SPN, reconfirmé) |
| `C_T ∝ N` | `∝ −N` (linéaire) | **CONCORDANT** |
| mécanisme holographique `⟨JJ⟩∝ℓ²/G_N` | (A.10/A.11) | **CONCORDANT** (≡ mécanisme (4) cadrage C_T §3) |
| **F1-G2′** `\|C_T\|/N = 3/(4π⁴)` (OP) | `3/(32π²)` (OP, `N` scalaires `\|_{N→−N}`, étalon F1-G4) | **NON concordant — écart `π²/8`** |
| **F1-G1** `A_T·N = 16` | — | **NON testable** (O1, consigné) |

**Lecture de l'écart `π²/8` `[établi — c'est O1]`.** Le **même** facteur `8/π²` sépare le
`C_T/N` graviton du programme et le scalaire libre **en convention impulsion**
(`(1/(32π²)) / (1/256) = 8/π²`). L'écart de coefficient n'est donc **pas** un artefact de
convention résiduel : il **est** l'obstacle **O1** — le `C_T` de Sp(N) est celui du tenseur de
stress **composite des scalaires** (Vasiliev), **pas** du **graviton d'Einstein** du programme.

---

## 4. Verdict `[deux étages — issue §6 du cadrage C_T]`

- **STRUCTURE → CONSOLIDATION (issue A).** Signe `< 0` (cohérent firewall `i^{d−1}`),
  proportionnalité `∝N`, mécanisme holographique `⟨JJ⟩∝ℓ²/G_N`, identification `N(rang)↔ℓ²/G_N`
  dans Vasiliev. Renforce `LC-D-SPN` et le mécanisme (4) de `LC-WORK-D-CT-CADRAGE §3`.
- **COEFFICIENT → DÉSACCORD (issue B), LOCALISANT le fossé.** `|C_T^Sp(N)|/N = 3/(32π²)` (OP) vs
  cible `3/(4π⁴)`, écart **`π²/8`**. Le désaccord **expose précisément le fossé
  dS/CFT↔inflation** : un modèle dS/CFT explicite **du type vectoriel/higher-spin** ne reproduit
  **pas** le coefficient du secteur **graviton d'Einstein** du programme.
- **CONCLUSION.** Le **pont constructif Sp(N) NE BRANCHE PAS le falsifiable positif**. Le
  coefficient `1/(32π²)` **reste spécifique au secteur graviton d'Einstein**, non reproductible par
  Sp(N). Cohérent avec `LC-E-N-CROSSCHECK` (a) : aucun cross-check indépendant validant le
  coefficient n'émerge. F1-G1 (`A_T·N=16`) reste hors d'atteinte ici (O1).

---

## 5. Sans surclassement `[§6.4]`

- F1 **cartographie** ce qu'un modèle dS/CFT explicite peut (structure) et ne peut pas (coefficient
  graviton) faire. Ce **n'est pas** une réduction de `{A4 ; A2★ ; N}` (INCHANGÉ).
- **Ne ferme pas** D1 ; n'**identifie pas** la CFT de raccordement (au contraire : confirme que
  ce **n'est pas** Sp(N), via le coefficient) ; ne **fixe pas** `N` ; ne **démontre pas** CCC.
- Conditionnel : étalon scalaire libre OP (F1-G4) ; dictionnaire `κ=24/π²` (`LC-NACTION-AVEUGLE`) ;
  identité des deux `N` valable **dans Vasiliev** seulement (O4 résiduel : Vasiliev ≠ Einstein).

---

## 6. Renvois

`LC-WORK-CADRAGE-F1-SPN` v0.1 (gel, plan, critère §6) ; `LC-E-N-CROSSCHECK` (c) (falsifiable
positif) ; `LC-WORK-D-CT-CADRAGE §3,§6` (mécanisme holographique, critère de réfutation) ;
`LC-D-SPN` (sous-front (b), signe/∝N) ; `LC-D-CT-ATN` (A_T·N=16, C_T/N=1/(32π²)) ;
`LC-AUDIT-LOG-NACTION-AVEUGLE` (κ=24/π², OP 3/(4π⁴), étalon scalaire 3/(32π²)) ;
`LC-WORK-BRANCHE-FALSIFIABILITE` (F1 rang 1). Source : `1108.5735v1` (AHS). Sceau :
`verif_F1_spn.py` (EXIT 0, 20 asserts, sha256 `19a4931e6f20`).
