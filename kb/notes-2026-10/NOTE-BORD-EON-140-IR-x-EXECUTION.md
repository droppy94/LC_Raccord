---
id: NOTE-BORD-EON-140-IR-x-EXECUTION
numero: 140
serie: I
branche: Q-M3 suite (IR-x)
reservation: 2026-10-12T13:16 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 140)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-139-ARMEMENT-IR-x (sha256 964e05db2efc250121f4974c3d1ee5aa57dd0f7aad3cb7eb600fde6afc8c85ad, sceau 2026-10-12T13:16:31Z)
instruments:
  - "irx_cone.py, sha256 827df834e7ff941c8647edb7fa99e0b8d79fded2a790613739528e81b50ec713, 2026-10-12T13:17:12Z : EXIT 0, sortie irx_cone_sortie.txt"
depend: [NOTE-BORD-EON-139-ARMEMENT-IR-x, NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE]
verdict: "X-V1"
prediction_realisee: "oui"
rouvre_si:
  - "audit froid"
  - "donnees de φ_h sur 𝓘⁺ hors du cadre distributionnel, ou bord non spatial"
---

# NOTE-140 : IR-x. Aucune solution homogene de □², singuliere ou non, ne compense le pole hors de points isoles. Verdict **X-V1**

## 0. Resume
- **x-1** : ln σ, 1/σ et s/σ (σ = r² − s²) verifient □² = 0 hors du cone ; leur singularite est portee par le cone r = s, issu d'un point-sommet de 𝓘⁺, qui est caracteristique [calcule].
- **x-2** : pour φ_h = ln σ, en un point de 𝓘⁺ distinct du sommet, **aucun pole** dans les 24 composantes de R de (2.17) ; en revanche R est singulier en σ⁻³ sur le cone, dans le volume [calcule]. Un tel φ_h correspond a un etat non Hadamard.
- **x-3** : dans l'ansatz general φ = Σ (a_n(x) + c_n(x) ln s) s^n, n = 0 a 7, □²φ = 0 force **c₀ = … = c₇ = 0** : aucune solution homogene ne porte de ln s le long de 𝓘⁺ [calcule].
- **x-4** : la composante q = 0 est un polynome cubique en s [calcule].
- Le comportement en ln s n'apparait qu'au sommet d'un cone, en un point isole de 𝓘⁺. La compensation du pole est donc impossible hors d'un ensemble de mesure nulle, quel que soit l'etat.

## 1. Resultats [calcule]
| Sous-question | Resultat |
|---|---|
| x-1 : □²(ln σ), □²(1/σ), □²(s/σ) | 0, 0, 0 (hors cone) ; controle □²(ln s) = −6/s⁴ |
| x-2 : trace de T̂ (φ_h = ln σ) | 0 |
| x-2 : coefficient de 1/s dans R, point (3/2, 1/2, 0) de 𝓘⁺ | 0 pour les 24 composantes |
| x-2 : R pres du cone (x = s + e, s = ½, e → 0⁺) | R_ysy, R_yxy, R_zsz, R_zxz ~ e⁻³ |
| x-3 : coefficients c_n du ln s | c₀ a c₇ forces a 0, ordre par ordre (s⁻⁴, s⁻³, s⁻², s⁻¹, puis s⁰ ln s a s³ ln s) |
| x-4 : □² f(s) = f'''' | f = C₁ + C₂s + C₃s² + C₄s³ |

## 2. Lecture [derive]
1. **Pourquoi aucun ln s le long de 𝓘⁺.** {s = 0} est une hypersurface spatiale, non caracteristique pour □² ; s = 0 n'est pas un point singulier de cet operateur a coefficients constants (racines indicielles 0, 1, 2, 3, sans log). x-3 le montre directement : le terme −6c₀/s⁴ ne peut etre compense par aucun autre, puis la recurrence annule tous les c_n. Par propagation des singularites (resultat standard pour les operateurs hyperboliques, cite de memoire), le support singulier d'une solution homogene est forme de surfaces caracteristiques ; un ln s porte par toute une hypersurface spatiale est exclu.
2. **Ce que font les solutions de cone.** Elles portent leur singularite sur le cone passe d'un point-sommet de 𝓘⁺. En un point de 𝓘⁺ hors du sommet, elles sont analytiques en s pres de 0 (σ → r² > 0) : T̂ = s² × (lisse), donc pas de pole (NOTE-131 t-2, confirme par W-c). Sur l'axe r = 0, ln |σ| = 2 ln s : le comportement logarithmique n'existe qu'au sommet, point isole. (Avec ½ ln |σ|, le coefficient serait exactement celui qui compense, mais seulement sur cet axe.)
3. **Superpositions.** Une superposition de solutions de cone a sommets repartis sur 𝓘⁺, avec un poids lisse, est une solution a donnees lisses, donc lisse en s pres de 0 (x-3 s'applique) ; avec un poids distributionnel, les singularites restent portees par des cones et des sommets. Aucune ne produit un ln s sur un ouvert de 𝓘⁺.
4. **Admissibilite.** Une solution de cone donne un R (et un T̂) singulier sur une hypersurface nulle du volume. Elle correspond a un etat dont le tenseur renormalise n'est pas lisse, donc non Hadamard.
5. **Mode q = 0.** Pour une onde plane de vecteur k, la composante de vecteur k du terme φ_h C ne recoit, a l'ordre lineaire, que la composante q = 0 de φ_h, cubique en s : jamais de ln s.

```
   compensation du pole G-V3 par phi_h homogene

   phi_h lisse (etat regulier)        -> pas de pole            (NOTE-131, W-c)
   phi_h de cone, hors sommet          -> pas de pole            (x-2, calcule)
   phi_h de cone, au sommet            -> ln s ponctuel          (point isole de scri+)
   phi_h ~ alpha(x) ln s sur un ouvert -> impossible : c_n = 0   (x-3, calcule)
   cout des solutions de cone          -> R ~ sigma^-3 sur un cone du volume : non Hadamard
```

## 3. Verdict
**X-V1.** Les solutions de cone sont homogenes sur s > 0, singulieres sur des cones caracteristiques du volume (etat non Hadamard), et ne produisent de comportement en ln s qu'aux sommets, points isoles de 𝓘⁺. Aucune solution homogene de □² ne se comporte en α(x) ln s sur un ouvert de 𝓘⁺. Le pole n'est compense par aucun φ_h, singulier ou non, hors d'un ensemble de mesure nulle. **L'hypothese d'etat de NOTE-131 n'est plus necessaire pour le secteur φ_h** ; elle le reste pour la partie non locale Γ[g].

## 4. Confrontation a la prediction
Prediction (NOTE-139 §4) : □² = 0 hors cone, support singulier caracteristique [**realise**] ; pas de pole hors du sommet, R singulier sur le cone [**realise**, ordre σ⁻³] ; α = 0 force [**realise**, et tous les c_n jusqu'a n = 7] ; q = 0 cubique [**realise**] ; mesure nulle [**realise**]. **Prediction realisee.**

## 5. Consequences (rien n'est grave)
- La classe de NOTE-131 se reduit : « WZ integrable + Γ[g] etat regulier + **φ_h homogene quelconque** ». L'hypothese de regularite de φ_h tombe ; seule demeure celle de l'etat pour Γ[g].
- Le point ouvert releve par W-c (NOTE-137) est clos.
- Libelle de G-V3 (NOTE-138) inchange, a une precision pres, a porter lors d'une revision : la classe d'hypotheses devient « WZ integrable + Γ[g] etat regulier », sans condition sur φ_h.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- **Audit froid** de NOTE-140 (court : x-3 et l'argument de propagation).
- Seule hypothese d'etat restante : regularite de Γ[g] en 𝓘⁺ (noyau retarde, passe adiabatique). Une instruction directe (IR-y) porterait sur le tenseur de Γ[g] pour un etat non regulier mais Hadamard.
- Lecture de Foraci-Woodard 2501.01972, sous gel.

## 7. Non-surclassement
[conv], non audite. Premier ordre en ε, fond de Sitter, mode tensoriel pour x-2. L'argument de propagation des singularites est cite de memoire ; x-3 en donne une verification formelle independante.
