---
id: NOTE-BORD-EON-91-ARMEMENT-Q-M3-LOG
numero: 91
serie: I
branche: Q-M3 suite (chantier D / CCC + M)
reservation: 2026-10-09T17:04 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 91)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (espace des verdicts fige AVANT tout calcul)
depend: [NOTE-BORD-EON-90-Q-M3-EXECUTION, NOTE-BORD-EON-89-ARMEMENT-Q-M3, S27-02-VERDICTS-M-ET-REPLI]
issue_attendue: "delimitation"
rouvre_si:
  - "modele de champs pour l'etat anomal au voisinage de I+ (fixe la contrainte anisotrope)"
  - "traitement non lineaire (retroaction de la source sur la geometrie)"
---

# NOTE-91 : armement de la suite de Q-M3 (le terme en ln Ω de (2.17), cas inhomogene)

## 0. Origine
NOTE-90 §3.4 laisse ouvert un point precis. Une trace physique imposee `T̂ = A Ω⁴` (canal de jauge sous C-M1) force, par la conservation et en modele homogene, une partie sans trace en `Ω² ln Ω`. Celle-ci donnerait un `ln Ω` non borne dans le second membre de l'equation (2.17) de Friedrich (arXiv:1311.0700v2), **si le coefficient structurel ne s'annule pas**. En homogene il s'annule par symetrie (FLRW conformement plat). Le cas inhomogene n'a pas ete evalue.

## 1. Cadre du calcul (fige)
- Fond fixe : de Sitter exact, `ĝ = Ω⁻² η`, `Ω = −Hτ` (temps conforme τ → 0⁻ a 𝓘⁺), `H = 1`. Source **test**, au premier ordre en κ, sans retroaction.
- Inconnues : composantes covariantes `X_μν = T̂_μν` en coordonnees plates (ce sont les composantes g-orthonormees de Friedrich). Le scalaire de Friedrich est alors `T* = η^μν X_μν = Ω⁻² T̂`.
- Un seul mode de Fourier spatial `e^{ikx}`, secteur scalaire (`X_00, X_0x, X_xx, X_yy = X_zz`). k = 0 redonne le modele homogene de NOTE-90 (controle).
- Trace imposee : `T* = A τ² e^{ikx}` (soit `T̂ = A Ω⁴`, ordre Ω⁰ dans la trace rescalee du corpus).
- Conservation `∇̂^μ T̂_μν = 0` imposee exactement. Ansatz polyhomogene pres de τ = 0 : puissances de τ et de ln(−τ).
- Second membre evalue : `R_ρνλ = 2 Ω⁻¹ ∇̂_[ν L̂_λ]ρ` avec `L̂ = κ/2 (T̂ − ⅓ T̂ ĝ)` (partie source).
- Un degre de liberte reste libre apres trace et conservation (une contrainte anisotrope, donnee d'etat). Il est traite comme parametre, pas fixe par moi.

## 2. Sous-questions
- **L-1** : pour k ≠ 0, toute completion conservee de cette trace porte-t-elle un terme en ln Ω, ou existe-t-il des completions lisses ?
- **L-2** : quand un terme en ln Ω est present dans la source, son coefficient dans `R_ρνλ` est-il non nul pour k ≠ 0 ?
- **L-3** : la reponse depend-elle de la donnee d'etat libre, et de facon uniforme en k (limite k → 0) ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **L-V1** | Pour k ≠ 0 generique, il existe des completions lisses (sans ln) avec `R` lisse ; et le ln, quand il est present, ne mord pas sur `R`. Le canal de jauge n'est pas une obstruction au niveau lineaire. |
| **L-V2** | Toute completion conservee porte un ln qui entre dans `R` avec un coefficient non nul : singularite logarithmique generique de (2.17). Candidat d'incompatibilite de C-M1 (M-V3 candidat, a lecture exterieure). |
| **L-V3** | Le ln est force dans la source, mais son coefficient dans `R` s'annule identiquement (comme en homogene) : `R` regulier, source seulement polyhomogene. |
| **L-V4** | Dependance a l'etat : le ln dans `R` s'annule pour un choix particulier de la contrainte anisotrope et pas en general ; la regularite est une condition sur l'etat, non une propriete du canal. |
| **L-V0** | Question mal posee dans ce cadre (a nommer). |

Composites permis (un verdict principal, une qualification).

## 4. EX-7, EX-8
- Objet externe vise : aucun nouveau. Seule la forme de (2.17) et (3.15) de Friedrich 1311.0700v2 (deja lue au texte en NOTE-90 §1).
- Imports non lus, en taux : l'etat effectif de l'anomalie QED dans un champ de fond (qui fixerait la contrainte anisotrope) ; non utilise.

## 5. Prediction declaree (anti-fit)
**L-V4**, avec cette inclinaison : pour k ≠ 0 la liberte anisotrope permet d'eviter le ln, mais au prix d'un terme en 1/k² qui ne se raccorde pas a la limite homogene ; quand le ln est present, il entre dans R avec un coefficient non nul proportionnel a k.

## 6. Instruments prevus
Script `q_m3_log.py` (sympy), empreinte prise avant execution : resolution exacte de la conservation par serie polyhomogene, calcul de `R_ρνλ`, extraction des coefficients de ln(−τ).

## 7. Non-surclassement
Calcul lineaire sur fond fixe, mode unique, secteur scalaire : il ne peut rien etablir au-dela de ce cadre. RG-4 non concernee. Noyau {A4 ; A2★ ; N} inchange.
