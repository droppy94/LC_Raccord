# R-3 — CIBLES GELÉES (protocole §2.0 amendé post-CSE) — 2026-07-21

Source : front-matter SEUL de LC-D3-SPECTRE-K3 v0.3 (corps NON lu), lu
depuis le dépôt git (R-54 tenu : le mount reste autoritaire, le git est
miroir — décision opérateur de session). Figé AVANT toute redérivation ;
sha256 consigné au rapport de lot.

## DÉCLARATION DE RÉVÉLATION DU MÉCANISME (règle post-CSE, opposable)

Le front-matter révèle : la CHAÎNE ENTIÈRE du spectre (𝒫_h=const ⟺
P_{g₀}∝k⁻³ ⟺ P_{g₃}=⅑k⁶P_{g₀}∝k³ ⟺ ⟨TT⟩∝k^{2Δ−d}), la relation d'état
g₃=−(i/3)k³g₀ (déjà R-5 P1), l'ENVELOPPE du noyau de variance (cos²x/3),
sa moyenne (1/6), les constantes d'arrivée (β∞=0,04503 ; C≈23,46) et le
cutoff (√(N/π)=ℓ_dS/ℓ_P≈1,02·10⁶¹).

⟹ PLAFOND DE GRADE ANNONCÉ AU GEL : au mieux REPRODUIT-SOUS-RÉSERVE au
sens E-2 (reproduction guidée). JAMAIS E-1.

SEULE PIÈCE NON RÉVÉLÉE : la FORME EXACTE du noyau de variance (le
front-matter n'en donne que l'enveloppe et la moyenne). La reconstruction
aveugle du noyau exact — adjugée par la constante gelée β∞=0,04503, qui
discrimine les candidats — est le seul contenu quasi-indépendant du lot.
Le nombre de candidats essayés sera consigné (anti-fit).

## Cibles

| # | cible | valeur revendiquée |
|---|---|---|
| K1 | spectre du mode | 𝒫_h=2H²/(M_Pl²k³) ; k³𝒫_h=const (invariance) — PRÉ-COUVERT R-4 T1, à consigner sans double compte |
| K2 | chaîne g₃ | P_{g₃}=(1/9)k⁶P_{g₀} ∝ k³ — PRÉ-COUVERT R-5 P1/P4 ; la COMPOSITION de chaîne est à re-calculer ici |
| K3 | lecture holographique | ⟨TT⟩ ∝ k^{2Δ−d}=k³ avec Δ=d=3 ; carte ⟨TT⟩=(d/16πG)²·P_{g₃} (coefficient importé) |
| K4 | FINDING variance | PAS de divergence quartique (k_UVη_*)⁴ (artefact du leading) ; croissance LOG : noyau exact d'enveloppe cos²x/3, moyenne 1/6 ⟹ Ω_σ^tot/A_T=(1/6)ln(k_UVη_*)+β∞, β∞=0,04503 |
| K5 | cutoff holographique | k_UVη_*=√(N/π)=ℓ_dS/ℓ_P≈1,02·10⁶¹ ⟹ Ω_σ^tot/A_T≈23,46, FINI, ≪0,5 dès A_T≪1 (H sous-Planckien) |
| K6 | rôles de N | cutoff log-doux ET normalisation A_T~(H/M_P)² ; les deux reportés sur la circularité LC-E (N=S_dS présuppose ℓ_P) — DÉCLARATIF, consignation |

Sceaux du lot (ARCHIVE, RC0 au harnais G-3) : verif_D3_spectre_k3.py,
verif_D3_bunchdavies.py — rejeu de confirmation inclus au lot (GO
opérateur). Leur CODE n'est pas lu avant la redérivation (il porte la
dérivation d'origine) ; ils sont exécutés, pas consultés.

Grades possibles : REPRODUIT-SOUS-RÉSERVE (E-2) ·
REPRODUIT-SOUS-RÉSERVE (écart nommé borné) · NON-REPRODUIT.

§6.4 : figer des cibles ne scelle, ne réduit, ne compte, ne démontre rien.
