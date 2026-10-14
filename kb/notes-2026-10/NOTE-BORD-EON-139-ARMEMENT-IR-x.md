---
id: NOTE-BORD-EON-139-ARMEMENT-IR-x
numero: 139
serie: I
branche: Q-M3 suite (IR-x)
reservation: 2026-10-12T13:16 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 139)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, sous-questions, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-12 15:15 heure de Paris
depend: [NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION]
issue_attendue: "delimitation"
rouvre_si:
  - "audit froid de NOTE-140"
  - "solution homogene de □² non couverte par l'argument de propagation des singularites (donnees non distributionnelles, bord non temporel)"
---

# NOTE-139 : armement de IR-x. Solutions de cone de φ_h : peuvent-elles compenser le pole G-V3 ?

## 0. Origine
NOTE-131 (t-3) : φ = −ln s + φ_h, avec □_η²φ_h = 0 ; un φ_h lisse ne produit aucun pole dans R de (2.17). NOTE-137 (W-c) : □² admet des solutions **singulieres portees par le cone de lumiere**, σ = r² − s² (r² = x² + y² + z²) : ln σ, 1/σ, s/σ, exclues par l'hypothese de regularite mais non instruites. Or la non-compensation du pole repose sur cette hypothese d'etat. Il faut savoir si une solution de ce type, ou une superposition, peut compenser le pole sur 𝓘⁺.

## 1. Cadre (fige)
- Repere plat, s > 0, 𝓘⁺ = {s = 0}. □_η = −∂_s² + Δ. T̂ = s² T, T_ab = −8b ∂^c∂^d(φ_h C_acbd) (convention physique, NOTE-138 ; le signe ne change aucune conclusion de presence ou d'absence de pole). Mode tensoriel de NOTE-131. R de (2.17).
- **Condition de compensation** : annuler le pole (8bκ/Ω)W_E en un point de 𝓘⁺ exige que φ_h se comporte comme +ln s (coefficient 1) pres de ce point, pour que φ = −ln s + φ_h y soit regulier (NOTE-131 t-2 : seul un T̂ d'ordre s¹ a valeur non nulle en s = 0 donne un pole).
- **Admissibilite** : un etat de Hadamard a un tenseur renormalise lisse ; un φ_h dont T̂ est singulier sur une hypersurface du volume (s > 0) correspond a un etat non Hadamard [critere standard, cite de memoire, non relu].

## 2. Sous-questions
- **x-1** : ln σ, 1/σ, s/σ verifient-ils □² = 0 sur s > 0 hors du cone ? Ou est leur support singulier ? (cone passe du point-sommet de 𝓘⁺ : r = s.)
- **x-2** : pour φ_h = ln σ (sommet a l'origine), T̂ et R de (2.17) : en un point fixe de 𝓘⁺ distinct du sommet, y a-t-il un pole en 1/s ? Ou R est-il singulier, et avec quel ordre ?
- **x-3** : une solution homogene de □² (distributionnelle) peut-elle se comporter comme α(x) ln s, α ≠ 0, sur un ouvert de 𝓘⁺ ? Developpement asymptotique en s, et argument de propagation des singularites ({s = 0} est spatiale, non caracteristique pour □²).
- **x-4** : mode de Fourier q = 0 : pour une onde plane de vecteur k, la composante de vecteur k de φ_h C ne recoit, a cet ordre, que la composante q = 0 de φ_h ; celle-ci est-elle necessairement un polynome cubique en s (donc sans ln s) ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **X-V1** | Les solutions de cone sont homogenes sur s > 0, singulieres sur des cones caracteristiques du volume (etat non Hadamard), et ne produisent de comportement en ln s qu'en des points isoles de 𝓘⁺ (sommets) ; aucune solution homogene ne se comporte en α(x) ln s sur un ouvert de 𝓘⁺. Le pole n'est compense par aucun φ_h, singulier ou non, hors d'un ensemble de mesure nulle de 𝓘⁺. L'hypothese d'etat de NOTE-131 n'est plus necessaire pour cette conclusion (elle l'est encore pour Γ[g]). |
| **X-V2** | Comme X-V1, mais une superposition admissible produit une compensation sur un ensemble de 𝓘⁺ non negligeable sous hypothese nommee ; G-V3 qualifie. |
| **X-V3** | Une famille admissible (Hadamard) de φ_h compense le pole sur un ouvert de 𝓘⁺ : G-V3 compromis. |
| **X-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**X-V1.**
- x-1 : □² = 0 verifie hors cone ; support singulier sur r = s (cone passe du sommet), caracteristique.
- x-2 : en un point de 𝓘⁺ distinct du sommet, φ_h est lisse pres de s = 0 : aucun pole ; R singulier sur le cone dans le volume (puissance inverse de σ).
- x-3 : le developpement impose α = 0 (terme −6α/s⁴ non compensable) ; propagation des singularites : un ln s porte par une hypersurface spatiale est exclu.
- x-4 : composante q = 0 cubique en s.
- Consequence : la non-compensation du pole par φ_h tient pour tout φ_h homogene ; seul subsiste un ensemble de mesure nulle (sommets).

## 5. Instruments prevus
Script `irx_cone.py` (sympy), empreinte avant execution. Aucune lecture.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange.
