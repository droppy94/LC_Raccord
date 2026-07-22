# R-7 — REDÉMONSTRATION « A4 / cible Q-W : verdict W2 (résidu-cassant) » — rapport de lot (2026-07-22, session S7)

Protocole §2.0 du lotissement, exécuté dans l'ordre.

## 1. Gel de cible (étape 1)

`audit/R7-CIBLES-GELEES.md` — **sha256
ef6e9f5e74483271637eb45d57d2604ed5adaac73ca5bed74eeaf28edc986b47**,
6184 octets — 12 cibles (Q1–Q12) extraites du **SEUL front-matter** de
`kb/LC-D-A4-QW.md` v0.4 (159 lignes ; front-matter clos ligne 15).
**Corps lignes 16–159 JAMAIS OUVERT.** Les six prérequis KB déclarés
(`LC-WORK-CADRAGE-A4-QW`, `LC-WORK-AMENDEMENT-R7-A4-QW-PHASE0`,
`LC-D-IRREDUCTIBILITE-MOYENS`, `LC-D3-WEYL-BUNCHDAVIES`,
`LC-D-CB-WEYL-MAGNETIQUE`, `LC-D-G3-ADM-IMPORTS`) et l'amendement
`…-TYPEI-CORR` sont restés **fermés** (note S6 §5.2 : « depuis
`LC-D-A4-QW` SEULE »).

**Plafond E-2 ANNONCÉ AU GEL**, avant la première ligne d'instrument,
sur quatre motifs : M1 le front-matter porte le MÉCANISME · M2 il porte
des VALEURS (`Σq²=2/3`, `g₃=−4q_i`, `𝓔=−6q_i`, `3/2H`, `1/H`) · M3 le
no-hair de Wald est un THÉORÈME IMPORTÉ · M4 Q9/Q10/Q12 sont des
énoncés de STATUT, hors décompte PASS par construction.

**Désambiguïsation consignée** : les fichiers
`LC-WORK-AMENDEMENT-R7-A4-QW-*` relèvent de la **règle de discipline
R-7** (« cibles tenues telles qu'écrites, zéro amendement, zéro fetch »),
non du **lot R-7**. Homonymie de numérotation, pas une fuite
d'aveuglement.

## 2. Redérivation (étape 2)

`instruments/redemo_R7_A4QW.py` — sympy 1.14.0 — **45/45 PASS
discriminants + 10 consignations déclarées, EXIT 0**, durée ≈ 4 min.

Jambes redérivées de bout en bout, depuis les seules prémisses nommées :

- **Moteur.** Contrainte hamiltonienne `Σ_{i<j}H_iH_j = Λ` et équation
  spatiale dérivées du tenseur d'Einstein du Bianchi I diagonal.
  Identité `Ḣ_i + H_iθ − Λ = ½(Ec + E_i − E_j − E_k)` obtenue par
  **coefficients indéterminés RÉSOLUS** (½, ½, −½, −½) ⟹ `(V·σ_i)' = 0`,
  donc `σ_i = c_i/V`.
- **Q2 — taux 3, RÉSOLU.** `ω = √(3Λ) = 3H` et `A² = Σc²/(2Λ)` résolus
  par annulation des coefficients de `sinh²` et du terme constant dans
  `V'² = 3ΛV² + (3/2)Σc²` ⟹ `V ∝ sinh(3Ht) ~ e^{3Ht}` ⟹ `σ ~ e^{−3Ht}`.
  Le taux **sort de √(3Λ)/H**, il n'est jamais affecté.
- **Q5 — `Σq=0` et `Σq²=2/3`, RÉSOLUS.** Injection de la famille
  `a_i = sinh^{1/3}(3Ht)·tanh^{q_i}(3Ht/2)` dans la contrainte :
  le coefficient de `cosh(3Ht)` **résout** `Σq_i = 0` ; le terme constant
  **s'ajuste** en `9·e₂ + 3` (solve sur `μ, ν`) ⟹ `e₂ = −1/3` ⟹
  `Σq² = 0 − 2(−1/3) = 2/3`. L'évolution ne contraint que `Σq=0` : la
  valeur `2/3` est portée par la **contrainte hamiltonienne seule**.
  FIREWALL : le système `{Σq=0 ; Σq²=2/3 ; q₁=q₂=q₃}` est **sans
  solution** ⟹ le type I VIDE ne contient **aucun** point isotrope.
- **Q3 — la coïncidence est STRUCTURELLE.** Racines indicielles de
  `h'' − ((d−1)/η)h' + k²h = 0` **résolues par Frobenius** : `{0, d}`.
  En dimension `d`, la contrainte isotrope **résout**
  `H = √(2Λ/d(d−1))`, donc `θ = dH`, donc taux de cisaillement `= d`.
  Taux et `Δ₊` sont **la même expression en d** — 3 et 3 à `d=3`, 4 et 4
  à `d=4`. Ce n'est pas un accident de `d = 3`.
- **Q5/Q9 — FG.** Série en `η` de `g_ii(η)` : **aucun terme η¹**,
  **`g₂ = 0`** (aucun terme `η²` : `g₀` conformément plat, Schouten nul),
  et coefficient **RÉSOLU par solve** : `g₃ = −4·q·g₀`. `g₃` sans trace.
- **Q2/Q4 — Weyl.** Tenseur de Weyl 4D calculé à partir de la métrique,
  `E_î = C_{0i0i}/a_i²` évalué sur la solution exacte :
  `lim e^{3Ht}·E_i = 6H²q_i` (coefficient **résolu**). Firewalls de taux :
  `e^{2Ht}E_i → 0` et `e^{4Ht}|E_i| → ∞` — les deux mordent, le taux 3
  est unique. Résidu rescalé `𝓔_i = Ω⁻³E_i = 6q_i/H`, fini et non nul,
  sans trace. Rapport `𝓔/g₃` **résolu** : facteur **3/2 reproduit
  exactement**.
- **Q3/Q8 — TRANSCRIPTION.** Le coefficient du mode décroissant du Weyl
  nu est **proportionnel à `g₃`, avec le même rapport sur les trois
  axes** : ce qui décroît dans le bulk EST ce qui survit au bord. Weyl
  nu → 0 (taux 3) ET résidu rescalé ≠ 0 **simultanément** ⟹ le chaînon
  « no-hair ⟹ Weyl-rescalé-propre » CASSE.
- **Q7 — exception isotrope.** Le point `q_i=0` (`a_i = sinh^{1/3}`) est
  isotrope mais **NON VIDE** : Friedmann **résout** `ρ = 3H²/sinh²(3Ht)`,
  et `ρ·a⁶` est constant ⟹ **fluide raide**. De Sitter `a_i = e^{Ht}` est,
  lui, le membre isotrope **VIDE** (`ρ = 0`) avec `g_ii(η) = H²`
  constant ⟹ **`g₃ = 0`**. Deux points isotropes **distincts** ⟹
  l'universalité de `g₃=−4q_i` est **FAUSSE** au membre isotrope vide :
  universalité **RETIRÉE**, W2 **générique** intact. Concordant avec le
  successeur `[05']`.
- **Q6 — magnétique.** `Cotton[Nil]` calculé composante par composante :
  **8 composantes non nulles**, dont `C_{xyz} = −1/2`, avec `R = −1/2`
  **CONSTANT**. FIREWALL de contrôle : `Cotton[δ₃ plat] = 0`
  identiquement — la machinerie **discrimine**. Le verrou magnétique
  tient à la **non-platitude conforme**, PAS à la constance de `R`
  (recoupe R-10/Q1). Aucun `q_i`, aucun `g₃` n'entre dans `Cotton[Nil]`
  ⟹ **𝓑 indépendant des données**.
- **Q8 — verdict.** Secteur `𝓔` générique non nul au type I vide +
  secteur `𝓑` identiquement non nul au type II ⟹ la limite du Weyl
  RESCALÉ à ℐ⁺ est un **RÉSIDU FINI GÉNÉRIQUE**, pas un nettoyage ⟹ **W2**
  dans l'espace pré-gelé `{W1 / W2 / W3}`.

## 3. Auto-audit anti-tautologie — AVANT le grade (précédent S6 §3)

- **Balayage statique** : 46 blocs `check` analysés. **Aucun assert ne
  porte un `True` littéral** ; aucun assert ne compare une valeur posée à
  elle-même. Tout coefficient cible sort d'un `solve`, d'une `series`,
  d'une `limit` ou d'un calcul tensoriel.
- **Harnais de mutation, 6/6 MORDANTES** :
  `M1` Λ=3H²→2H² · `M2` exposant sinh 1/3→1/2 · `M3` argument sinh
  3Ht→2Ht (les trois détruisent `Σq²=2/3`) · `M4` puissance tanh 2q→q
  (`g₃/q` : −4 → −2) · `M5` racine indicielle d=3→4 (3 → 4) ·
  `M6` Cotton Nil→δ₃ (8 → 0 composantes).
- **UNE MUTATION VACANTE DÉTECTÉE ET REMPLACÉE** : muter l'exposant `2/3`
  du facteur `((1−η⁶)/2)` **ne change pas** `g₃/q = −4`. Motif structurel :
  ce facteur ne contribue qu'à l'ordre `η⁶`, jamais à `η³` — **`g₃` est
  porté par le seul facteur anisotrope `tanh^{2q_i}`**. Mutation mal
  ciblée, **vacante**, remplacée par `M4` qui mord. Précédent S5 :
  « mutation invariante = VACANTE », elle se remplace, elle ne se compte
  pas.

## 4. Sceaux (étape 3) — rejoués aux comptes EXACTS de Q11

| sceau | zone | sha8 | attendu Q11 | issue |
|---|---|---|---|---|
| `verif_A4_QW.py` | LIVE | `a4637a2c` | 14/14, EXIT 0 | **14/14, rc 0** (3,9 s) |
| `verif_A4_QW_typeI_succ.py` | LIVE | `79f09a8c` | 8/8, EXIT 0 | **8/8, rc 0** (2,5 s) |

sha8 **concordants** avec le gel. Le sceau successeur rejoue ses deux
firewalls de sur-grade (« 𝓔≠0 à de Sitter » ⟹ FAUX ; « q=0 est vide »
⟹ FAUX), concordants avec la redérivation de Q7.

## 5. Réconciliation — un écart nommé

**ÉCART DE SIGNE (Q4), NOMMÉ ET NON CORRIGÉ.** Sous les conventions
déclarées en tête d'instrument (Riemann
`R^a_{bcd} = ∂_cΓ^a_{bd} − ∂_dΓ^a_{bc} + ΓΓ − ΓΓ` ;
`E_ab = C_{acbd}u^cu^d`, `u = ∂_t` ; `Ω = Hη`), le `solve` rend
**`𝓔 = −(3/2H)·g₃`** ; la cible écrit `𝓔 = +(3/2H)·g₃`.

La **magnitude** et le **facteur 3/2** sont reproduits **exactement**.
L'écart est **borné à un signe global commun aux trois composantes** et
tient à une convention non fixée par le front-matter (orientation de la
normale à ℐ⁺ — de genre **espace** en dS, ce qui échange les rôles
électrique/magnétique par rapport au cas lorentzien — et signe de la
définition de `𝓔`). **Aucune tolérance desserrée, aucune cible amendée**
(précédents R-2/Q6 et R-10/(a)).

Aucun autre écart. Aucune cible non atteinte.

## 6. Corrections d'instrument (consignées, même cycle, avant tout grade)

1. **v1 retirée** : elle portait un assert d'évolution **mal construit et
   quasi-vacant** (comparaison d'une expression à elle-même). Détecté par
   auto-audit, retiré, remplacé par l'identité à coefficients
   indéterminés **résolus**. **La v1 n'a jamais servi de base à un
   grade.**
2. `sp.solve` sur `Max(0,d) = d` — `NotImplementedError`. Reformulé sans
   `Max`, par sélection de la racine non nulle.
3. Sélection de branche : `solve` rendait les deux racines `±` ; filtrage
   explicite de la branche positive, test par résidu et non par `Eq`.
4. Bloc Weyl initialement évalué sur la famille à `q₃` **libre**, alors
   que les équations d'Einstein imposent `Σq=0` : basculé sur la famille
   contrainte.
5. `simplify` non borné (14 min sur un seul assert) : la substitution
   `Σq=0` **avant** dérivation réduit `V` à `sinh(3Ht)` et ramène le même
   test à **1,6 s**.

**Aucune cible, aucune tolérance, aucun coefficient n'a été modifié.**

## 7. Grade (étape 4)

**REPRODUIT-SOUS-RÉSERVE (E-2)** — plafond annoncé au gel **atteint, non
dépassé**.

12/12 cibles traitées : Q1–Q8 et Q11 **reproduites** par redérivation
(45 asserts discriminants, 6/6 mutations mordantes) ; Q9, Q10, Q12
**consignées** comme énoncés de statut, conformément au motif M4 déclaré
au gel. Un écart de signe nommé et borné (§5). Sceaux d'origine rejoués
verts aux comptes et sha8 exacts.

Issue **conforme** à la tête scellée ⟹ **aucun audit froid déclenché**
(§2.0-5 : obligatoire seulement si l'issue diffère).

## 8. §6.4 — sans surclassement

« REPRODUIT-SOUS-RÉSERVE » = **algèbre correcte + cibles reproduites,
sous hypothèses explicites** — jamais davantage. En particulier :

- W2 est une **DÉLIMITATION** de la route A4-par-ℐ⁺, pas une réfutation
  de A4. Le statut de **postulat** de A4 en sort **RENFORCÉ**.
- Le no-hair de Wald reste un **import** ; le lot ne le redémontre pas.
- Le périmètre couvert est **type I (électrique) + type II/Nil
  (magnétique)** — les deux jambes déclarées porteuses. Le type V n'est
  pas traité ; VI/VII/VIII restent **non exécutés**.
- La réserve `[10]` semi-vacante et les asserts `[06]/[07]` non
  reproduits par l'auditeur d'origine ne sont **ni levés ni reproduits**.

`{ A4 ; A2★ ; N }` **INCHANGÉ** · A4 **non réfuté** · A2★ décision
ouverte · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) · O₂ non construit
(β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) ·
**CCC non démontrée NI réfutée**.

---

*§6.4 — sentinelle terminale. Redériver, muter, rejouer et consigner :
aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que
ce soit.*
