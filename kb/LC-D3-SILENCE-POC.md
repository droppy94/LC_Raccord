---
id: LC-D3-SILENCE-POC
titre: "Front (a)/GWE — POC « silence asymptotique » EXÉCUTÉ : bilan des trois diagnostics A∧B∧C (tous PASS) et cadrage du verrou résiduel C7-b (rétro-action des spikes). Successeur de résultat de LC-WORK-C7-POC-SILENCE : la note de lancement portait la SPEC du §4 ; celle-ci CONSIGNE l'exécution (3 sceaux en KB) et le verdict consolidé — le silence asymptotique est SOUTENU au niveau POC (signatures nécessaires présentes, aucune réfutation) ⟹ C7 passe de `hors de portée` à `formalisable (borné)`, et se réduit à (oracle homogène pointwise, DÉJÀ scellé) + (spikes, C7-b). La §II cadre la quantification de C7-b (mesure × amplitude, à PROUVER petite). Référence la substance par id ; ne duplique ni l'algèbre du pont/mode exact (LC-D3-WCH-GWE), ni l'oracle (LC-D3-INTERAEON-P6), ni la spec (LC-WORK-C7-POC-SILENCE §4)."
codename: LC-RACCORD
type: note de résultat (chaînon) — consigne l'exécution du POC §4 de LC-WORK-C7-POC-SILENCE et cadre l'étape C7-b. Subordonnée au verdict d'audit (LC-AUDIT-LOG-WCH-GWE v1.0) et à la discipline LC-AUDIT-VERDICT §6.4.
version: 1.1
langue: fr
date: 2026-06-08
maj: "2026-06-08 — v1.1 : VOIE 1 de C7-b EXÉCUTÉE (cf. note dédiée LC-D3-SPIKES-C7B, sceau verif_D3_C7b_spikes.py). Le §II (cadrage) est marqué EXÉCUTÉ : carte de spike=BKL² (raccord à l'oracle), α_s borné (W²_K≤12), statistique spike≡bulk (Th.3.2) ⟹ R_s amplitude/statistique → 0 ; résidu = secteur non-local (gradient des spikes super-horizon) ⟹ voie 2. C7-b : `formalisable`→PASS PARTIEL. Aucune touche au verdict A∧B∧C (§I). | v1.0 : note initiale (POC silence A∧B∧C exécuté, réduction de C7, cadrage C7-b)."
portee: "Consigne UNIQUEMENT le delta de résultat : (I) les trois diagnostics homogènes du POC §4 sont CODÉS, EXÉCUTÉS, et PASS — A (fermeture de l'horizon de particules / velocity-domination), B (sous-dominance de courbure & rebonds isolés), C (découplage causal de points voisins) ; (II) la réduction de C7 qu'ouvre A∧B∧C, et le cadrage exécutable de C7-b (spikes). Ne refait NI la spec (LC-WORK-C7-POC-SILENCE §4), NI l'algèbre du pont/mode exact (LC-D3-WCH-GWE), NI l'oracle de Gauss-Kuzmin (LC-D3-INTERAEON-P6). Discipline §6.4 : un `établi` de sceau = la SIGNATURE NUMÉRIQUE est correcte, jamais « le silence physique est établi ». Le silence reste `formalisable (borné)` ; (A) physique reste conditionnel à C7-b ET C7-a, cadre CCC."
prerequis_kb: [LC-WORK-C7-POC-SILENCE, LC-D3-WCH-GWE, LC-D3-INTERAEON-P6, LC-D3-INTERAEON-CONVERGENCE, LC-A-SURVIE-CONFORME, LC-A-D1-BIANCHI, LC-AUDIT-LOG-WCH-GWE, LC-AUDIT-VERDICT, LC-WORK-BIBLIO-FRONT-A]
fichiers_compagnons_kb: [verif_D3_A_horizon.py, verif_D3_B_curvature.py, verif_D3_C_decoupling.py, verif_D3_interaeon_kappa.py, diag_bounces.py, verif_D3_P6_specB_oracle.py, verif_D3_WCH_GWE.py]
source_externe: ["SILENCE : Uggla-van Elst-Wainwright-Ellis, PRD 68 103502 (2003) — bord silencieux (E_i^a→0). SPIKES (à charger, pas encore en PDF KB) : Lim (thèse + recurring spikes) ; Garfinkle (numérique inhomogène) ; Berger-Moncrief ; Uggla-Wainwright. PDFs déjà en KB : 0901_0806 (Heinzle-Uggla), 0901_0776 (Mixmaster fact vs belief), 0212256 (Damour-Henneaux-Nicolai), 1005_4908 (Reiterer-Trubowitz)."]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# POC « silence asymptotique » exécuté — bilan A∧B∧C, cadrage de C7-b

> **But.** Consigner que le POC du §4 de `LC-WORK-C7-POC-SILENCE` est **exécuté** (trois
> sceaux en KB) et **PASS**, en tirer la **réduction de C7**, puis **cadrer** le verrou
> résiduel **C7-b** (rétro-action des spikes). Discipline `LC-AUDIT-VERDICT §6.4` : un
> `établi` de sceau = « la signature numérique est correcte », jamais « le silence physique
> est établi ».

---

## 0. État en une ligne `[résumé]`

Les **trois diagnostics homogènes** du POC (A, B, C) sont **codés, exécutés, PASS**. Le
silence asymptotique est **`formalisable` — soutenu au niveau POC** : les signatures
**nécessaires** sont présentes, **aucune réfutation**. ⟹ **C7** (rétro-action inhomogène)
passe de **`hors de portée`** à **`formalisable (borné)`**, et se **réduit** à
**(oracle homogène pointwise, DÉJÀ scellé** `LC-D3-WCH-GWE`/`LC-D3-INTERAEON-P6`**) +
(spikes, C7-b)** — le verrou résiduel, à **prouver** petit, **pas postuler**. L'objectif
explicite de la note de lancement (`faire passer C7 de hors de portée à formalisable borné,
pas à le déclarer établi`) est **atteint**.

---

## 1. Le bilan des trois diagnostics `[établi (sceau) / formalisable]`

Chaque diagnostic intègre le **même noyau homogène** que les scripts sources (Bianchi IX +
radiation + Λ, temps e-fold `N=ln a`, CI de Tod `σ(0)=0`), **vers l'arrière** (`N<0`) —
l'approche de la singularité `a→0` (ρ∝e⁻⁴ᴺ→∞), seule direction où le silence se teste.

### A — fermeture de l'horizon de particules `[sceau verif_D3_A_horizon.py]`
**Question.** L'horizon de particules passé se ferme-t-il (`χ_PH→0`) au bang ?
Équivalent : la singularité est-elle *velocity-dominated* ?
**Résultat PASS.** Le rayon de Hubble comobile `1/(aH)→0` vers le bang ; l'intégrale
`χ_PH(N)=∫dN'/(aH')` **converge** (plateau `≈√(3/ρ0)`, contribution profonde →0 exp.) ⟹
**horizon fini**. Le critère propre `p=−dlnH/dN>1` (si `H~e⁻ᵖᴺ`, alors `a∝(t−t_b)^{1/p}`,
horizon `∫dt/a` convergent ⟺ `p>1`) est tenu : `p∈[2,3]` (radiation `p=2` près de `N=0`,
puis cisaillement-Kasner `p=3` au fond). Budget Ω : approche radiation- puis cisaillement-
dominée (Ω_rad,Ω_σ→1 ; Ω_curv,Ω_Λ→0). **Robuste** en `ε`, `(ρ0,Λ)`.
**Découverte interne** : le contraste hors-Tod (donnée Kasner) fait toucher `p=1`
**exactement** aux **murs de courbure isolés** (`Ω_curv→1`, mesure ~nulle en `N` :
≈98.5 % du temps e-fold a `p>1.05`). Un mur isolé `p=1` est log-marginal, négligeable dans
une intégrale convergente — **c'est la structure de rebonds que B quantifie**.

### B — sous-dominance de courbure & rebonds isolés `[sceau verif_D3_B_curvature.py]`
**Question.** La courbure spatiale Hubble-normalisée est-elle sous-dominante (Kasner) **entre**
des rebonds **isolés** ?
**Correctif technique** : `diag_bounces` détecte les pics sur `|³S|` **brut** (valable vers
l'avant, `³S→0`) ; vers le bang `³S~a⁻²→∞` croît monotone ⟹ on détecte sur la courbure
**normalisée** `Ω_curv=−³R/(6H²)` (spike à O(1) aux murs, →0 entre).
**Résultat PASS.** Bang **physique de Tod** (WCH) : `f_act=0`, **0 rebond** — approche
**quiescente** (silence non-oscillatoire, la forme la plus forte). Bang **générique** (Kasner) :
billard de Mixmaster, `f_act≈0.22` (**Kasner sur ~78 %** de `N`), rebonds de largeur ~1.1
**≪** espacement ~4.8 (**isolés**), `|Ω_curv|→0` entre eux ; `f_deep≈0.08` (courbure **non
persistante**).
**Réserve consignée** : l'intégration directe **halte la cascade** (nombre **fini** de
rebonds, le système se fige sur un Kasner — c'est « le germe halte la cascade » de
`diag_bounces`). B confirme donc la **structure** (Kasner + murs isolés, non persistance) ;
l'isolement de la **cascade infinie** **défère à l'oracle Gauss-Kuzmin**
(`verif_D3_P6_specB_oracle.py`, déjà en KB), à appliquer pointwise sous silence.

### C — découplage causal de points voisins `[sceau verif_D3_C_decoupling.py]`
**Question.** Deux points voisins `{ε, ε+δ}` (séparés d'une échelle comobile `L`) se
découplent-ils quand `χ_PH` (de A) tombe sous `L` ?
**Résultat PASS.** Pour **tout** `L>0`, `χ_PH(N)` passe sous `L` à profondeur finie `N_dec(L)`,
puis `χ_PH/L→0` ⟹ **déconnexion causale générique** (deux points comobiles quelconques
perdent le contact). Le découplage est **lisse** dans le régime capturé (gain `Δ_Σ/δ=O(1)`).
**Constat honnête (≠ attendu)** : le proxy **n'amplifie pas** la séparation — car la cascade
halte (B), le chaos de Mixmaster n'a pas le temps de raidir les gradients. ⟹ Le proxy
homogène **ne peut NI exhiber NI exclure les spikes** (C7-b), qui sont une propriété de la
cascade **infinie** (oracle) ou proprement **inhomogène**. *Borne nette sur ce que l'outil
homogène livre.*

---

## 2. La réduction de C7 qu'ouvre A∧B∧C `[formalisable (borné)]`

A∧B∧C tous PASS ⟹ par le **§5 de `LC-WORK-C7-POC-SILENCE`**, le silence asymptotique est
**soutenu** (niveau POC) et **C7 se réduit** à deux pièces, l'une déjà close :

- **C7-a — sélection WCH pointwise.** Sous silence (E_i^a→0, signature A+C), la sélection du
  mode régulier `j₀` (vs `y₀`/mécanisme `Y`, exclu par Friedrich) est une **condition
  locale**. La **dichotomie homogène** `j₀`/`y₀` est **déjà scellée** (`LC-D3-WCH-GWE`
  `[1]`+`[2-4]`) ; C7-a = « cette dichotomie scellée, appliquée **point par point** ». Sous le
  découplage de A/C, **C7-a se réduit au déjà-scellé** appliqué pointwise. → `formalisable`,
  largement instruit.
- **C7-b — rétro-action des spikes.** Le **verrou résiduel** : les spikes (exceptions
  inhomogènes de **mesure ~nulle en localisation**, mais **dynamiquement réelles**)
  modifient-ils `⟨Ω_σ⟩` ? Le non-sequitur « mesure nulle ⟹ négligeable » est **corrigé en
  KB** ; il faut **quantifier** (mesure × amplitude), pas postuler. → **objet de la §II
  ci-dessous.**

> **Statut de C7** : `hors de portée` → **`formalisable (borné)`**. (A) physique reste
> `formalisable`, conditionnel à **C7-b** (et C7-a pointwise), cadre CCC.

---

## 3. Discipline et registre froid `[méta — §6.4]`

Conformément à `LC-AUDIT-VERDICT §6.4`, **sans surclassement ni rétrogradation** :
- Les trois scripts sont `établi (sceau)` = **la signature numérique est correcte** (horizon
  fini ; courbure sous-dominante + rebonds isolés ; déconnexion causale + découplage lisse
  capturé). Re-exécutables, sans réseau, contrainte hamiltonienne relative ~1e-12.
- Le **silence physique** reste `formalisable` (soutenu au POC) — **pas** `établi`. Les trois
  outils sont **homogènes** : ils n'ont pas de `E_i^a` spatial, donc ne **prouvent pas** le
  silence inhomogène ; ils en attestent les **signatures nécessaires**.
- « Le bang gagne » (P6 (B), `LC-D3-INTERAEON-P6`) **intact** : le POC ne réintroduit aucun
  mécanisme de contraction libre ; il borne le contenu de la WCH au crossover, pas l'issue
  inter-éon.

---

# II. Cadrage de la quantification des spikes — C7-b `[formalisable → le chantier]`

> **⟹ VOIE 1 EXÉCUTÉE (v1.1).** Le cadrage ci-dessous a été exécuté : voir la note de
> résultat dédiée **`LC-D3-SPIKES-C7B`** (sceau `verif_D3_C7b_spikes.py`). Résultat :
> carte de spike = BKL² (raccord à l'oracle confirmé) ; **α_s borné** (`W²_K≤12`,
> compacité) ; **statistique spike ≡ bulk** (Théorème 3.2) ⟹ `α_s(moyenné)→1` ⟹
> **`R_s = μ_s(α_s−1) → 0`** indépendamment de μ_s. **C7-b : `formalisable` → PASS
> PARTIEL** ; reste le seul **secteur non-local** (gradient des spikes super-horizon),
> objet de la **voie 2**. Le §II ci-dessous est conservé tel quel comme cadrage d'origine.

## 4. Ce que C établit comme point de départ `[établi (sceau)]`

C a montré que le **proxy homogène est aveugle aux spikes** : la cascade halte, la séparation
de points voisins ne s'amplifie pas. Donc C7-b **ne peut pas** être tranché par l'intégration
directe homogène. Deux voies seulement, par ordre de coût croissant :

1. **Statistique de spikes via l'oracle (semi-analytique).** Les spikes naissent de la
   sensibilité de la **carte de Gauss** `u↦1/(u−1)` (rebonds BKL) là où des points voisins
   franchissent un mur **différemment** — structures récurrentes de Lim. L'**oracle de
   Gauss-Kuzmin déjà en KB** (`verif_D3_P6_specB_oracle.py`, `LC-D3-INTERAEON-P6`) fournit la
   **statistique des rebonds** ; on peut en dériver la **mesure** (fraction de l'espace
   spatial portant un spike à une époque donnée) et l'**amplitude** (l'excès de `Ω_σ` sur un
   spike). C'est la première brique, **dans le prolongement direct de l'outillage P6**.
2. **Probe inhomogène minimal (numérique, Garfinkle-style).** Un solveur **proprement
   inhomogène** (1D, `E_i^a` spatial explicite) sur une tranche near-bang. C'est la seule
   façon de **voir** un spike se former. **Coût élevé**, `à inventer / partiellement hors de
   portée` avec l'outillage actuel (homogène).

## 5. L'observable de décision `[formalisable]`

Le contenu dynamique de la WCH au crossover (`LC-D3-WCH-GWE`) est porté par `⟨Ω_σ⟩`. On le
décompose en **bulk** (le mode régulier sélectionné, déjà scellé) + **spikes** :
```
⟨Ω_σ⟩_total  =  ⟨Ω_σ⟩_bulk            +  ⟨Ω_σ⟩_spikes
              (mode régulier j₀,          (mesure_spikes ×
               LC-D3-WCH-GWE, scellé)      amplitude_spikes)
```
- **Mesure des spikes** `μ_s` : fraction (volume comobile) portant un spike actif à l'époque
  considérée — à estimer via la statistique de l'oracle (voie 1) ou la probe inhomogène
  (voie 2). *Mesure ~nulle ne signifie pas amplitude bornée : les deux facteurs comptent.*
- **Amplitude** `α_s` : l'excès `Ω_σ^{spike}/Ω_σ^{bulk}` sur un spike (les spikes sont des
  pics localisés de cisaillement/courbure).
- **Critère.** Contribution relative `R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk`.

## 6. Critères pass/fail de C7-b `[décision ouverte]`

- **PASS (C7 levée)** : `R_s ≪ 1` (spikes **prouvés** négligeables en moyenne) **ET** C7-a
  (sélection WCH pointwise) tient ⟹ **C7 levée** ⟹ **(A) passe de `formalisable` à
  `établi (sous WCH/A3-A4, cadre CCC)`** ⟹ **front (a) clos par la physique.**
- **PASS partiel** : silence soutenu (déjà acquis) mais `R_s` non encore quantifié ⟹ C7
  reste à C7-b, verrou résiduel **borné** (l'état présent de cette note).
- **FAIL** : `R_s = O(1)` ou davantage (les spikes dominent `⟨Ω_σ⟩` en moyenne) ⟹ couplage
  inhomogène irréductible ⟹ **C7 reste ouvert**, (A) demeure `formalisable` conditionnel.
  **Résultat honnête à consigner**, pas un échec : il borne précisément ce que la WCH délivre.

## 7. Premier pas pour la conversation neuve C7-b `[pratique]`

> Recharger `prerequis_kb` (en particulier `LC-D3-INTERAEON-P6` pour l'oracle, `LC-D3-WCH-GWE`
> pour `⟨Ω_σ⟩_bulk` scellé) → **charger la littérature spikes** (Lim, Garfinkle,
> Berger-Moncrief, Uggla-Wainwright ; **pas encore en PDF KB**, cf. `LC-WORK-BIBLIO-FRONT-A`)
> → **voie 1** : dériver `μ_s` et `α_s` de la statistique de l'oracle Gauss-Kuzmin déjà en
> main, calculer `R_s`. Si `R_s≪1` robuste ⟹ C7-b prouvé petit ; sinon → décider si la
> **voie 2** (probe inhomogène 1D) est dans nos moyens ou se consigne `hors de portée`. Tenir
> §6.4 : tout `établi` reste « signature » ; C7 levé seulement sous **preuve** de `R_s≪1`.

---

## 8. Propagation suggérée `[à faire — housekeeping, hors de cette note]`

À consigner lors du prochain housekeeping (non fait ici, comme la discipline le veut) :
`00-INDEX` (ajout de `LC-D3-SILENCE-POC` à la carte ; bump version) ; `LC-D3-WCH-GWE` §6
(C7 : `hors de portée`→`formalisable (borné)`, réduit à oracle pointwise + C7-b) ;
`LC-AUDIT-VERDICT` §8bis (enregistrer A∧B∧C PASS, sans surclassement) ; `LC-02`, `LC-03-
GLOSSAIRE` (entrées silence asymptotique / spikes / C7-a / C7-b) ; `LC-WORK-C7-POC-SILENCE`
(marquer §4 EXÉCUTÉ, renvoyer ici pour le verdict).

---

## Appendice — chiffres de lancement (scellés, à ne pas re-prouver)

- **A** : `χ_PH(0)≈√(3/ρ0)` (0.173 à ρ0=100), `1/(aH)→0`, `p∈[2,3]>1` ; murs isolés `p=1`
  ⟺ `Ω_curv→1` (≈98.5 % du temps `p>1.05`).
- **B** : Tod `f_act=0` (quiescent) ; Kasner `f_act≈0.22` (Kasner 78 %), largeur~1.1 ≪
  espac.~4.8, `f_deep≈0.08` ; cascade haltée ⟹ cascade infinie → oracle.
- **C** : `χ_PH/L→0` ∀ `L>0` (déconnexion causale) ; gain `Δ_Σ/δ=O(1)` (Tod 6.4, Kasner 1.0,
  régime capturé) ; spikes hors de portée du proxy.

**Tags épistémiques.** `établi (sceau)` = les trois signatures numériques. **Silence
asymptotique** : `formalisable` (soutenu au POC). **C7** : `formalisable (borné)`, réduit à
**C7-a** (`formalisable`, = dichotomie scellée pointwise) **+ C7-b** (`décision ouverte` :
`R_s≪1` à **prouver**). **(A) physique** : `formalisable`, conditionnel à C7-b ∧ C7-a, cadre
CCC. *Discipline §6.4 maintenue de bout en bout.*
