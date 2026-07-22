---
id: LC-AUDIT-R10-CIBLES-GELEES
titre: "Gel de cibles — lot R-10 (Silo R) : parité non-linéaire du Weyl rescalé (E pair / B impair, 5+5=10), verrou un-point (triptyque) et verrou deux-point (rang 2). Cibles figées depuis les FRONT-MATTERS SEULS, AVANT toute redérivation."
codename: LC-RACCORD
type: "document de gel — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-22
lot: R-10
session_de_gel: S5
session_de_derivation: "session NEUVE — ce gel NE SERA PAS re-gelé (précédent R-6 : gel déposé fin S3, dérivé en S4 sans re-gel)"
sources_du_gel: [kb/LC-D-NONLIN-VERROU.md (front-matter), kb/LC-D-NONLIN-2PT.md (front-matter)]
corps_non_lus: "Les corps des deux têtes n'ont PAS été ouverts. Seuls les blocs YAML l'ont été. L'aveuglement sur les corps doit être TENU jusqu'à la fin de la dérivation."
---

# 0. Déclaration de révélation

Les front-matters de R-10 sont du **gabarit LOURD**, au moins autant que ceux
de R-8. Ils portent, corps fermés :

- les **valeurs d'arrivée** : `(E,B) = (5,5) = 10` · dimension `1` des deux
  secteurs invariants · coefficient Cotton `½` · `C^lin = (i/2)k³·(Dh)` ·
  `D² = −𝟙` · équipartition `⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 1` exacte · `Γ(−3/2)` finie ·
  `c_FT = π²/12` · cas catalogue `{2,4,8}` de produit net `1` · comptes de
  sceaux `12/12`, `14/14`, `5/5`, `41` asserts, firewall `5/5` ;
- les **mécanismes** : platitude conforme du fond maximalement symétrique en
  d=3, Ward exactes en d impair, décomposition SVT, `Π^TT(δ) = Π^TT(P) = 0`,
  hélicités ±2, Cotton pseudo-tenseur vs Ricci tenseur vrai, non-analyticité
  de `k³ = (k²)^{3/2}` comme critère de radiativité.

**PLAFOND DE GRADE ANNONCÉ AU GEL : REPRODUIT-SOUS-RÉSERVE (E-2).**
E-1 est **exclu d'avance**. Aucune lecture ultérieure ne relèvera ce plafond.

# 1. Cibles gelées — rang 1 (un-point, triptyque `LC-D-NONLIN-VERROU`)

| # | Cible | Attendu |
|---|---|---|
| **Q1** | Secteur MAGNÉTIQUE, parité IMPAIRE : `B ∝ Cotton[g₀]` ; sous A3 le fond est maximalement symétrique ⟹ **conformément plat en d=3** ⟹ `Cotton(S³) = Cotton(ℝ³) = Cotton(ℍ³) = 0` exactement ⟹ `⟨B⟩ = 0` IDENTIQUEMENT, **sans** argument de représentation. Cotton linéarisé d'une perturbation TT : non nul, symétrique, sans trace, transverse (objet TT, pas de fuite de singlet) | DÉRIVABLE |
| **Q2** | Secteur ÉLECTRIQUE, parité PAIRE : `E ∝ g₃ ∝ ⟨T⟩` ; décomposition SVT complète en d=3 ; `Π^TT(δ) = Π^TT(P) = 0` (spin-2 ∩ invariants = {0}) ; hélicités ±2 via `R_z(ψ)·e^±·R_zᵀ = e^{∓2iψ}e^±`, **pas d'hélicité 0** ; `g₃` transverse et sans trace par les **Ward EXACTES** (d=3 impair, pas d'anomalie) ⟹ pur spin-2 tous ordres ⟹ `⟨E⟩ = ⟨g₃⟩ = 0` exactement | DÉRIVABLE (Ward = import) |
| **Q3** | Cohérence de PARITÉ : Cotton = **pseudo-tenseur** (`y_R = det(R)·(R⊗R)·y(Rx)`, contrôle négatif inclus) ⟹ B impair ; Ricci/Schouten/stress = tenseur **vrai** (sans `det`, contrôle négatif inclus) ⟹ E pair ; couverture `(E,B) = (5,5) = 10` **complète, disjointe, sans croisé** ; chaque secteur annulé par SON argument respectant SA parité | DÉRIVABLE |

# 2. Cibles gelées — rang 2 (deux-point, `LC-D-NONLIN-2PT`)

| # | Cible | Attendu |
|---|---|---|
| **Q4** | C1 — l'espace des structures **PAIRES** invariantes du deux-point TT spin-2 à `Δ = d = 3` est de **DIMENSION 1** ; solution `∝ Π^TT` ; complétude des hélicités ±2 ; `k³ = (k²)^{3/2}` **non analytique** ⟹ RADIATIF | DÉRIVABLE |
| **Q5** | C2 — le secteur **IMPAIR** est de dimension 1 **ET** de type **CONTACT** (`k³·S^odd` polynomial ⟹ local) ; pseudo-tenseur ; orthogonal au pair ⟹ **aucune amplitude radiative neuve** ; la scission radiatif/contact suit EXACTEMENT la frontière de parité | DÉRIVABLE |
| **Q6** | C3 — Cotton linéarisé **ab initio** : `C^lin = (i/2)·k³·(Dh)`, le **½** sortant du Ricci linéarisé ; `D² = −𝟙` sur TT, recoupant `S² = −𝟙` (CT-DUAL) **indépendamment** ; refermeture BD : `⟨EE⟩, ⟨BB⟩ ∝ k³` ; `⟨EB⟩` radiatif **NUL** sur BD | DÉRIVABLE (BD = import) |
| **Q7** | C4 — comparanda : OP (2.23)-(2.24) = 1 structure / 1 constante ; de Haro (47) coefficient Cotton `½` ; de Haro (49)/(50) ⟹ **équipartition `⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 1` EXACTE** en unités de dualité ; cas catalogue `{2,4,8}` (2 des préfacteurs vs ½ du Cotton) de produit net `1` ; map `prog↔dH = κ²/(Hℓ²)` facteur fixe pur ; `Γ(−3/2)` FINIE (d=3 pole-free), `c_FT = π²/12` ; 0 entrée libre < 3 sorties appariées | **IMPORTS externes** (Osborn–Petkou, de Haro) : consignation, sauf le comptage interne qui est dérivable |
| **Q8** | Firewall 5/5 : `Δ ≠ 3` casse ; `d = 4 ⟹` pôle `Γ(−2)` (spécificité d=3 **structurelle**) ; `Cotton ×2 ⟹` ratio 4 ≠ 1 ; trace annihilée par `Π^TT` ; `n ≠ 2` | DÉRIVABLE (mutations mordantes) |
| **Q9** | Sceaux du lot : `verif_nonlin_cotton.py` 12/12 · `verif_nonlin_repr.py` 14/14 · `verif_nonlin_parity.py` 5/5 · `verif_nonlin_deuxpoint.py` EXIT 0 / **41 asserts** (phase 1 interne = 27 asserts écrits AVANT tout fetch, sha256 `ad13634…74ff`, asserts 1–27 byte-identiques dans la version finale) | REJEU + confrontation à l'inventaire |

# 3. Tolérances déclarées AVANT comparaison

- Identités algébriques et de parité (Q1, Q3, Q6) : **exactitude symbolique**, tolérance nulle.
- Comptages de dimension par SVD / échantillonnage de directions (Q2, Q4, Q5) : seuil de rang `1e-10` sur les valeurs singulières ; le **comptage** est l'observable, jamais une valeur numérique isolée.
- Équipartition (Q7) : ratio **exactement 1**, aucune tolérance — un écart quelconque est un écart, pas un arrondi.
- Non-analyticité / caractère contact (Q4, Q5) : établis par **critère analytique** (parité de la puissance, polynomialité), jamais par un ajustement numérique. *(Précédent R-8/C9 : un test numérique qui contredit le critère déclaré se remplace par le critère, jamais par un desserrage de tolérance.)*

# 4. Anti-fit et conduite de la dérivation

- Aucun coefficient, aucune convention, aucune tolérance ne sera modifié après lecture d'un écart. Un jeu de conventions manqué se consigne TEL QUEL (précédent R-2/Q6).
- Les **corps** des deux têtes restent fermés jusqu'à la fin de la dérivation. Toute lecture d'un corps est une réconciliation §2.0 post-dérivation, à déclarer.
- Toute mutation laissant la cible invariante est **vacante** et doit être remplacée (précédent R-8/C10) ; convention unique : l'argument `mutation` est la **claim MUTÉE**, qui doit être FAUSSE.
- `Q7` est majoritairement de l'import externe : ne pas le compter comme redérivation.

*§6.4 — ce gel n'établit rien. Le verrou un-point reste conditionnel à A3 et spécifique à d=3 ; le deux-point `⟨g₃g₃⟩ ∝ k³` reste la donnée de Cauchy irréductible, pendue à la seule amplitude `A_T ~ 1/N` ; A3/A4 NON fusionnés ; D1 NON clos ; N non fixé. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.*
