---
id: NOTE-BORD-EON-94-AUDIT-FROID-Q-M3-CONCORDANCE
numero: 94
serie: I
branche: Q-M3 suite (audit)
reservation: 2026-10-09T17:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 94)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-93-ARMEMENT-AUDIT-FROID-Q-M3 (sha256 b2673a078f203d874b8d6a7ce0d5c0641b1ce3cff4ef565acbfd947513002dea, 2026-10-09T17:23:33Z)
rapport: RAPPORT-CSE-Q-M3-AUDIT-AVEUGLE.md
depend: [NOTE-BORD-EON-93-ARMEMENT-AUDIT-FROID-Q-M3, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION]
rouvre_si:
  - "preuve ou contre-exemple a tous les ordres de la queue logarithmique"
  - "traitement de k = 0 ou des secteurs vectoriel et tensoriel"
---

# NOTE-94 : audit froid aveugle de NOTE-92. Verdict **AU-V2**

## 0. Resume
Les deux sous-agents (S-a re-derivation en cecite stricte, S-b audit du code v5) concordent avec NOTE-92 sur tous les resultats porteurs. Aucune discordance. Quatre corrections ou precisions mineures, dont une elargit la famille reguliere sans toucher a la conclusion. Prediction du gel (AU-V2) **realisee**.

## 1. Table de concordance

| Resultat porteur (NOTE-93 §1) | S-a | S-b | Etat |
|---|---|---|---|
| P-1 equations, exposant 2, resonance | memes equations (parametrisations h et f) | OK | **concordant** |
| P-2 c₀ = c₁ = 0, e₂ = A/3, autres ln nuls | retrouve (Yxx sans τ⁰, τ¹, avec (A/3)τ² ln) ; famille plus large (voir §2.1) | confirme, reproduit | **concordant, precise** |
| P-3 ln force dans la source, structure isotrope | retrouve : partie en ln de trace nulle, type rayonnement, `ρ ⊃ AΩ⁴ ln Ω`, `p_i ⊃ (A/3)Ω⁴ ln Ω` | confirme | **concordant** |
| P-4 κA/2 · ln Ω ; c₀ = −A/k² donne un pole Ω⁻² | retrouve, plus les poles Ω⁻¹ (`iAκ/(2k)`, `−iAκ/(4k)`) | confirme | **concordant, complete** |
| P-5 troncature | ordres m ≤ 2 controles (parametrisation h) | vrai pour la pire composante, conservateur ; solution reguliere prolongee jusqu'a N = 7 | **concordant, renforce** |

## 2. Corrections et precisions (mineures)
1. **Famille reguliere plus large.** L'ansatz de NOTE-92 commencait `c` a τ⁰. S-a autorise des puissances negatives et trouve des etats reguliers avec `Yxx ⊃ −2a₁/(k²τ)` (et `Y00 = a₁τ + …`). Seuls τ⁻², τ⁰, τ¹ sont exclus de Yxx. P-2 reste exact dans son ansatz ; P-3 n'est pas touche (le ln reste force).
2. **Ansatz incomplet sans effet** (S-b) : pas de termes ln² en τ⁰, τ¹ (f₀, f₁) ni ln³ ; ajoutes par les auditeurs, ils sont forces a zero.
3. **Dependance en k de la queue** (S-b) : la condition dominante e₂ = A/3 est independante de k, mais la queue ne l'est pas (`C4₁ = −k²A/10`, `C6₁ = k⁴A/168`). NOTE-92 §2.2 (« condition independante de k ») vaut pour l'ordre dominant seulement.
4. **Cosmetique** (S-b) : composantes (0,2,2), (1,2,2) identiquement nulles ; equation « 0 » parasite filtree. Les composantes evaluees couvrent les deux composantes independantes non nulles.

Precision physique apportee par S-a, a verser : la resonance est seculaire. La trace imposee decroit en a⁻⁴, au rythme exact de la radiation conforme, et l'equation de continuite `ρ' + 4Hρ = −H·trace` force `ρ ∝ Ω⁴(c + A ln Ω)`. L'etat regulier est celui dont la partie logarithmique est un fluide de radiation isotrope.

## 3. Verdict
**AU-V2** : concordance sur les resultats porteurs (P-2, P-3), corrections mineures nommees au §2. NOTE-92 est maintenue (L-V4 qualifie L-V3), avec les precisions §2.1 et §2.3.

## 4. Reserves communes des auditeurs
- Pas de preuve a tous les ordres (verifie jusqu'a N = 7) : condition de `rouvre_si`.
- La conclusion suppose l'admission de donnees d'etat polyhomogenes (gel NOTE-91 §1 l'autorise).
- Lineaire, fond fixe, un mode, k > 0 ; k = 0 et secteurs vectoriel/tensoriel non traites.

## 5. Greffe proposee (non entee)
- **Q-M3-e** : NOTE-92 §2.1, ajouter « famille plus large si `c` admet des puissances negatives (Yxx ∝ τ⁻¹ permis) » ; §2.2, remplacer « independante de k » par « independante de k a l'ordre dominant ; la queue depend de k ».

## 6. Non-surclassement
Audit concordant : NOTE-92 reste [conv] dans son cadre. RG-4 inchangee. CCC + M : hypothese ouverte, condition d'isotropie asymptotique de l'etat ajoutee, non tranchee. Noyau {A4 ; A2★ ; N} inchange.
