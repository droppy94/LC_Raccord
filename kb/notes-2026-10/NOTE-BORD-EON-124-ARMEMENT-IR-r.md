---
id: NOTE-BORD-EON-124-ARMEMENT-IR-r
numero: 124
serie: I
branche: Q-M3 suite (retroaction IR-r)
reservation: 2026-10-11T17:51 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 124)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-11 19:50 heure de Paris
depend: [NOTE-BORD-EON-120-AUDIT-IR-m-CONCORDANCE, NOTE-BORD-EON-118-IR-k-EXECUTION (v2), NOTE-BORD-EON-123-IR-q-EXECUTION]
sources: ["aucune nouvelle ; action anomale de Riegert (partie c, terme φC²) telle qu'utilisee par l'audit M-b (NOTE-120, indep_K_weyl.py) ; mode tensoriel de de Sitter : formule standard, controlee par le calcul"]
issue_attendue: "delimitation"
rouvre_si:
  - "partie a (Euler) de l'action anomale au premier ordre en h, non calculee ici"
  - "partie invariante de Weyl non locale (facteur de forme C ln(box) C) singuliere pres de scri+"
  - "ordres superieurs en h, en kappa, en beta"
---

# NOTE-124 : armement de IR-r. Le fond fixe masque-t-il un canal gravitationnel dans (2.17) ?

## 0. Origine et reformulation
- NOTE-120 et NOTE-118 v2 (K-D2) : toute la chaine 89 a 121 est calculee sur un fond **exactement de Sitter, Weyl-plat**. Le terme de l'action anomale en charge de Weyl, b∫√g φ C², est nul sur ce fond. A l'ordre lineaire en une perturbation h, il donne ln s × ∂⁴h (calcul M-b).
- L'audit presentait ce point comme une retroaction (h d'ordre κ). Il faut distinguer deux origines de h :
  - **(i)** une donnee d'ondes gravitationnelles **libre** a 𝓘⁺, d'ordre 1 : partie electrique w_ab du Weyl rescale, metrique de bord a_ij. Cette donnee est generique ; selon Meissner et Penrose (NOTE-123, MP5), elle domine meme l'approche du raccord.
  - **(ii)** la reponse metrique a la contrainte de Maxwell, d'ordre κ.
- Le cas (i) n'est pas une retroaction : c'est un canal gravitationnel present des que le fond porte de la courbure de Weyl.
- **Constat prealable d'ordre, fait avant ce gel, non calcule (transparence)** : avec φ = −ln s, les termes (∂∂φ)C et (∂φ)(∂C) du tenseur de φC² pourraient produire, dans le repere non physique, des termes en W/s. Ce serait **plus fort** qu'un log.

## 1. Cadre (fige)
- Metrique physique ĝ = s⁻²(η + ε h), s = −τ = Ω, H = 1, premier ordre en ε.
- h : mode tensoriel de de Sitter, k selon x, polarisation « plus » dans le plan (y, z) : h_yy = −h_zz = u(s) cos kx, avec u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks). Ce mode est solution du vide linearise avec Λ. Pres de 𝓘⁺ : u = A(1 + k²s²/2 + …) + B(k³s³/3 + …). A est la perturbation de la metrique de bord ; B la donnee libre de rayonnement (terme c_ij de Starobinsky, partie electrique du Weyl rescale).
- Action : S_C = b ∫ √ĝ φ Ĉ², avec φ = Ω[ĝ] = −ln s a l'ordre zero. Par invariance de Weyl, S_C = b ∫ √g φ C²[g], g = η + εh.
- Tenseur : T_μν[g] = (2/√g) δS_C/δg^{μν}, au premier ordre en ε (forme fermee −4b ∂^ρ∂^σ(φ C_μρνσ) a normalisation pres, **controlee** contre une variation brute d'Euler-Lagrange sur la famille diagonale de M-b) ; tenseur physique T̂_μν = s² T_μν[g].
- Equation testee : L̂ = (κ/2)(T̂ − ⅓ĝ tr T̂) ; R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), Christoffel de ĝ de fond.
- Controles : conservation ∇̂^μ T̂_μν = 0 au premier ordre ; trace.
- (ii) : ordre de grandeur de la meme contribution quand h est la reponse a la contrainte de Maxwell (h d'ordre κ F²), compare au log de M-V3, (3βκ/e²)Q_tf.

## 2. Sous-questions
- **r-1** : pour la donnee (A, B), quelle est la plus basse puissance de s dans T̂^(C) et dans R ? Y a-t-il un pole en Ω⁻¹, un ln Ω, ou rien de singulier ? Quel coefficient, quelle donnee le porte (A, B) ?
- **r-2** : structure tensorielle du terme singulier (electrique, magnetique, partie sans trace). Peut-il compenser le log de M-V3, dont la structure est Q_tf ?
- **r-3** : pour h d'origine (ii), quel est l'ordre en κ et en b relativement au log de M-V3 ?
- **r-4** : portee. Le coefficient b de charge de Weyl est non nul pour tout champ quantique conforme (photon, fermion sans masse). Le canal concerne-t-il la CCC sous sa forme actuelle (photons presents a 𝓘⁺), independamment de C-M1 ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **R-V1** | Pour une donnee gravitationnelle generique a 𝓘⁺, le terme φC² produit dans (2.17) un terme singulier (pole Ω⁻¹ ou ln Ω) au meme ordre que M-V3 ou plus fort : canal gravitationnel, structure et coefficient nommes. |
| **R-V2** | Aucun terme singulier : les contributions se compensent ou restent lisses. Le fond fixe n'etait pas une restriction pour la regularite de (2.17). |
| **R-V3** | Indecidable dans la classe : le resultat depend de la partie invariante de Weyl non locale, de la partie a, ou de l'etat. |
| **R-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**R-V1 qualifie R-V3.**
- Avec B ≠ 0 (rayonnement libre a 𝓘⁺), le terme φC² donne un second membre de (2.17) singulier. Son ordre dominant serait un **pole en Ω⁻¹** (pas seulement un ln Ω), proportionnel a la partie electrique du Weyl rescale a 𝓘⁺. Il serait porte par les termes (∂∂φ)C + 2(∂φ)(∂C), dont les coefficients ne se compensent pas.
- Le canal existerait pour tout champ conforme a b ≠ 0 (photon compris), donc **independamment de C-M1**.
- Le cas (ii) serait d'ordre κb, supplementaire et negligeable devant M-V3.
- Qualifications : partie a (Euler) non calculee ; partie invariante de Weyl non locale (facteur de forme) susceptible de modifier le resultat ; ordre zero de l'etat.

## 5. Instruments prevus
Script `irr_c.py` (sympy), empreinte avant execution.

## 6. Non-surclassement
[conv]. Un resultat R-V1 ne serait pas une refutation : il nommerait un canal a auditer, a confronter a la partie a et a la partie non locale, et a lire a l'aune de la convention de regularite de NOTE-123. RG-4 inchangee ; M-V3 candidat non grave ; noyau {A4 ; A2★ ; N} inchange.
