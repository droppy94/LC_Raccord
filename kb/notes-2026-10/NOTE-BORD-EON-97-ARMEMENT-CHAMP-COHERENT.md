---
id: NOTE-BORD-EON-97-ARMEMENT-CHAMP-COHERENT
numero: 97
serie: I
branche: Q-M3 suite (champ coherent)
reservation: 2026-10-10T12:12 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 97)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (modele, fermeture, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-96-ISOTROPIE-ETAT-ANOMAL-EXECUTION, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION, NOTE-BORD-EON-90-Q-M3-EXECUTION]
sources: ["arXiv:1808.08237v2 (S2, appui R-41 deja etabli en NOTE-96)"]
issue_attendue: "delimitation"
rouvre_si:
  - "source ou derivation donnant la partie sans trace du secteur non Maxwell (variation metrique hors orbites de Weyl)"
  - "fermeture alternative physiquement motivee (champ auxiliaire de type Riegert, dilaton dynamique)"
  - "configurations inhomogenes ou champ electrique"
---

# NOTE-97 : armement. Champ magnetique coherent a 𝓘⁺ avec le couplage anomal de S2

## 0. Origine
NOTE-96 laisse ouvert le cas d'un champ electromagnetique **classique coherent** porte jusqu'a 𝓘⁺. Aucune source lue ne donne la partie sans trace de ⟨T_μν⟩ du secteur anomal F² ; S2 (note 4) l'exclut de sa methode. Ce chantier construit le calcul nous-memes, avec une fermeture **declaree** du secteur manquant.

## 1. Modele (fige)
- Fond : de Sitter fixe, `ĝ = Ω⁻² η`, `Ω = −τ` (H = 1), τ → 0⁻ a 𝓘⁺. Source test, premier ordre, sans retroaction sur la geometrie.
- Secteur de jauge : action simplifiee de S2 (3.12)-(3.13), `S = −¼ ∫ d⁴x I(τ)² F_μν F^μν` (indices plats), `I² = e⁻² [1 + 2β̃ ln(a/a⋆)]`, avec `a = 1/Ω` (attention : chez S2, Ω designe ln a ; ici Ω est le facteur conforme du corpus).
- Configuration : **champ magnetique uniforme** dans le cadre conforme, `F_xy = B₀` constant, pas de champ electrique. C'est une solution exacte de `∂_μ(I² F^μν) = 0` (a verifier dans le script).
- Secteur Maxwell du tenseur physique : `X^M_μν = I² (F_μα F_νβ ĝ^αβ − ¼ ĝ_μν F_αβ F^αβ|ĝ)`, composantes covariantes en coordonnees plates (= composantes g-orthonormees de Friedrich, comme en NOTE-90 a 92).
- Trace anomale : obtenue par variation de Weyl de (2.11) de S2, `√ĝ T̂ = δS_B/δΩ_S`, soit `T̂ = −(β̃/e²) Ω⁴ F²|η / 2` pour `F²|η = 2B₀²` (signe et normalisation a verifier dans le script ; ce passage est [derive] de S2, non lu tel quel).
- **Fermeture C-iso du secteur non Maxwell** (hypothese, pas un resultat) : le reste `X^R` est un fluide **homogene et isotrope** (`X^R_00 = r₀(τ)`, `X^R_ii = r₁(τ)` identiques), qui porte toute la trace anomale (le secteur Maxwell est sans trace) et retablit la conservation totale `∇̂^μ (X^M + X^R)_μν = 0`. Une constante d'integration libre (rayonnement isotrope arbitraire).
- Objet evalue : second membre de l'equation (2.17) de Friedrich, `R_ρνλ = 2Ω⁻¹ ∇̂_[ν L̂_λ]ρ`, `L̂ = κ/2 (T̂ − ⅓ T̂ ĝ)` (partie source), sur toutes les composantes (24, ρ quelconque, ν < λ).
- **Budget anisotrope** : en plus, chercher la contrainte anisotrope homogene minimale `Π(τ) diag(0, 1, 1, −2)` (forme tensorielle compatible avec la symetrie axiale du champ) qu'il faudrait ajouter au secteur non Maxwell (avec conservation) pour rendre R regulier, et la comparer a la partie logarithmique du secteur Maxwell.

## 2. Sous-questions
- **CB-1** : la partie logarithmique du secteur Maxwell est-elle presente et anisotrope (structure `diag(1,1,1,−1)` attendue pour B selon z) ?
- **CB-2** : sous C-iso, le second membre de (2.17) est-il regulier (ni puissance negative de Ω, ni ln Ω) ?
- **CB-3** : quel budget anisotrope Π le secteur inconnu devrait-il porter pour la regularite ? Est-il exactement l'oppose de la partie logarithmique anisotrope du secteur Maxwell ?
- **CB-4** : limite β̃ → 0 (Maxwell conforme pur) : R doit etre regulier (controle).

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **CB-V1** | Sous C-iso, R est regulier : un champ magnetique coherent est compatible avec la regularite de (2.17) dans ce modele. |
| **CB-V2** | Sous C-iso, R porte un terme non lisse (ln Ω ou pole) de coefficient proportionnel a β̃B₀² ≠ 0 : incompatibilite dans ce modele et cette fermeture (candidat M-V3 conditionnel a la fermeture, a lecture exterieure). |
| **CB-V3** | La regularite depend de la fermeture : singulier sous C-iso, mais un budget anisotrope fini et nomme du secteur inconnu (CB-3) la retablit ; la question est reportee sur la partie sans trace hors orbite de Weyl. |
| **CB-V0** | Question mal posee dans ce cadre (a nommer). |

Composites permis (un verdict principal, une qualification).

## 4. EX-7, EX-8
- Objet externe : S2 seulement (deja declare et appuye en NOTE-96). Aucune nouvelle lecture.
- Non lu, ecrit en taux : la forme covariante de l'action anomale avec le terme F² (Riegert, champs auxiliaires) qui fixerait la partie sans trace.

## 5. Prediction declaree (anti-fit)
**CB-V2 qualifie CB-V3** : sous C-iso, un terme en ln Ω non nul, proportionnel a β̃B₀², apparait dans R ; le budget requis est exactement l'oppose de la partie logarithmique anisotrope du secteur Maxwell (le secteur inconnu devrait l'annuler).

## 6. Instruments prevus
Script `cb_coherent.py` (sympy), empreinte prise avant execution ; puis audit froid aveugle (deux sous-agents) sous gel separe.

## 7. Non-surclassement
Modele + fermeture choisie : le resultat ne vaut que sous C-iso et pour un champ uniforme, lineaire, fond fixe. RG-4 non concernee. Noyau {A4 ; A2★ ; N} inchange.
