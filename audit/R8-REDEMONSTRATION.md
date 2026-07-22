---
id: LC-AUDIT-R8-REDEMONSTRATION
titre: "Redémonstration du lot R-8 (Silo R) — A2★ mésoscopique (Gauss-Kuzmin, non-cascade) + oracle P6. Grade : REPRODUIT-SOUS-RÉSERVE (E-2, plafond annoncé au gel)."
codename: LC-RACCORD
type: "rapport de redémonstration — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-22
lot: R-8
session: S5
gel: "audit/R8-CIBLES-GELEES.md — sha256 6523e4b52ea2ac5fb4fcd8ac022dddb5757c512e64dc249de73e6373288cd249, figé AVANT l'écriture de l'instrument"
instrument: instruments/redemo_R8_A2star.py
resultat: "21/21 PASS discriminants + 10 consignations déclarées — EXIT 0 ; rejeu de sceaux 3/3 rc=0, sha8 concordants"
---

# 1. Ce qui a été redérivé (dérivation aveugle sur les front-matters seuls)

- **Q1 — mesure invariante de Gauss.** Point fixe EXACT de l'opérateur de
  transfert : le terme se réduit à `1/(ln2·(x+k)(x+k+1))`, qui **télescope**,
  et somme à `1/(ln2(1+x))`. Normalisation à 1 vérifiée. La densité uniforme
  n'est pas point fixe (mutation mordante).
- **Q2 — transport en variable d'ère.** `u = 1/x`, jacobien `1/u²` ⟹
  `p(u) = 1/(ln2·u(u+1))`, normalisée sur (1,∞), **queue en `u⁻²`** exacte
  (`u²p(u) → 1/ln2`). Omettre le jacobien casse la normalisation.
- **Q3 — seuil DÉRIVÉ DE LA MESURE.** Exposant de queue de l'intégrande
  `= s − 2` ⟹ convergence ⟺ `s − 2 < −1` ⟺ `s < 1`, soit **s\* = 1 exact**,
  obtenu de la mesure et non ajusté. Divergence en `s = 1` établie par
  **forme fermée** `(ln(B+1) − ln2)/ln2 → ∞` (logarithmique). Marge stricte
  `s_phys = 0 < 1` ⟹ « OC adressé » reproduit.
- **Q4 — exposants de Kasner en paramétrisation d'ère.** `Σp = Σp² = 1`
  identiquement ; bords `u=1 → (−⅓, ⅔, ⅔)` et `u→∞ → (0,0,1)` ;
  **bornitude `|p_i| ≤ 1` ∀u ≥ 1**.
- **Q5 — dichotomie.** Cascade `n_s = n₀(1+ρ)^{N_b}`, taux `= ln(1+ρ)`
  **exact** et strictement monotone (`1/(1+ρ) > 0`) ; `ρ = 0` ⟹ production
  additive `n₀ + cN_b`, **sous-exponentielle** (`n_s e^{−αN} → 0 ∀α > 0`).
  Dichotomie non-cascade ⟺ ρ = 0 reproduite.
- **Q6 (finitude seule).** Charge bornée ⟹ `⟨C_F⟩ ≤ M < ∞` ; **robustesse** :
  même `C_F ~ u^s` avec `0 < s < 1` laisse la moyenne finie.

# 2. Ce qui n'a PAS été atteint — écarts nommés, non résorbés

- **⟨C_F⟩ = 7.18 : NON VISÉE.** Le noyau `C_F(u)` est absent des
  front-matters. La valeur n'a été ni approchée ni ajustée ; seule la
  **finitude** est établie. Toute confrontation ultérieure à 7,18 serait une
  réconciliation §2.0, jamais un PASS (précédent R-2/Q6).
- **Q10 / P6 hors périmètre aveugle.** `κ = 0.8117`, validation à 0,8 %,
  `P(ε_out < κ·ε_in) = 0` : le noyau `ε` est absent des front-matters ⟹ non
  redérivable en aveugle. Couvert par le **rejeu de sceau seul** (§4).
- **Écart numérique C9.** Un test de ratio entre décades donnait 1,000145 au
  lieu de 1 — effet de taille finie de `ln(B+1)` à `B = 10³`, sans rapport
  avec la divergence. **La tolérance du gel (1e−9) n'a PAS été desserrée** :
  le test a été remplacé par le critère **analytique** que le gel §2
  prescrivait dès l'origine. L'écart est consigné tel quel et borné (décroît
  comme `1/ln B`).

# 3. Corrections d'instrument (consignées nominalement, précédent S4)

- **C8 — convention de mutation.** La v1 mélangeait deux conventions :
  **19 mutations sur 21 déclarées VACANTES par le harnais lui-même**. Aucune
  n'a produit de faux PASS — le harnais a fonctionné comme prévu. v2 unifie
  la convention (l'argument est la claim MUTÉE, qui doit être FAUSSE).
  Second défaut : sympy refuse `limit(exp((ln2−α)N))` avec α symbolique
  (signe indécidable) ; α concrétisé à `1/2 < ln2`.
- **C10 — mutation vacante réelle.** « `p1` pris positif » ne peut pas casser
  une somme de **carrés** (`p1²` invariant sous `p1 → −p1`). Vacance
  authentique, détectée par le harnais ; remplacée par `p1 → −2u/den`, qui
  mord. **Cible Q4 inchangée.**

Aucune cible, aucune tolérance, aucun coefficient n'a été modifié à aucun
moment.

# 4. Rejeu des sceaux du lot (Q9)

| Sceau | Étagère | sha8 rejoué | Inventaire | rc | Attendu du gel |
|---|---|---|---|---|---|
| `verif_A2_numerique.py` | LIVE | `76e9257c` | `76e9257cfdd337b6` | 0 | ✓ sha ET « 22 assertions, firewall m1/m2/m3 + c1/c2 » reproduits littéralement |
| `verif_D3_P6_specB_oracle.py` | LIVE | `162696c1` | `162696c131f55ea2` | 0 | ✓ (128,3 s ; 2 assertions oracle + bang_wins) |
| `verif_D3_C7b_A2_reduction.py` | ARCHIVE | `ee03c385` | `ee03c385d750bb0f` | 0 | ✓ |

**3/3 rc = 0, sha8 concordants.** Aucun écart de libellé d'étagère.

# 5. Grade

**REPRODUIT-SOUS-RÉSERVE (E-2)** — plafond annoncé au gel, jamais E-1 :
front-matters de gabarit lourd portant à la fois les valeurs d'arrivée et le
mécanisme. Réserve additionnelle propre au lot : deux cibles (⟨C_F⟩ = 7.18 ;
noyau ε de P6) n'étaient pas atteignables en aveugle et sont couvertes par
rejeu, non par redérivation.

Issue conforme à la tête : aucun audit froid mandaté (§2.0-5).

# 6. Ce que le lot n'établit pas (§6.4)

« Reproduit » vaut ici : **mesure de Gauss-Kuzmin redérivée, seuil s\* = 1
dérivé de la mesure, bornitude de Kasner établie, dichotomie ρ formalisée,
sceaux rejoués verts**. Cela ne vaut **jamais** « A2★ est démontrée ».
Le verdict de la tête tient inchangé : **délimitation à lean positif**.
`ρ = 0` reste un **input physique motivé** (Garfinkle), non dérivé d'un
théorème générique 3D ; le gap `OA` persiste `hors de portée` ; A2 n'est pas
formalisable comme théorème depuis la source (`work in progress`, résolution
hors régime convergent).

**A2★ reste DÉCISION OUVERTE. C7 non levée. { A4 ; A2★ ; N } INCHANGÉ.
D1 non clos · N non fixé · O₂ non construit · nœud (i) INDÉTERMINÉ ·
CCC non démontrée NI réfutée.**
