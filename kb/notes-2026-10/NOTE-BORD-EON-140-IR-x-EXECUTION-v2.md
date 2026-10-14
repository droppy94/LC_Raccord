---
id: NOTE-BORD-EON-140-IR-x-EXECUTION
numero: 140
serie: I
branche: Q-M3 suite (IR-x)
reservation: 2026-10-12T13:16 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 140)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 d1ddf4b4fd2cf3a6ab3432809e3bf9371db4972e062ace215028646df71734fc (conservee)"
greffe: "IR-x entee le 2026-10-12 par NOTE-BORD-EON-143 (corrections de l'audit froid aveugle NOTE-142, XA-V2)"
audit: "NOTE-BORD-EON-141 (gel) / NOTE-BORD-EON-142 (concordance) : XA-V2 ; x-3 retrouve a l'aveugle (XA-1 jusqu'a n = 8, XA-2 jusqu'a n = 11 et recurrence exacte) ; x-2 retrouve (XA-2) ; argument general reformule (XA-1)"
gel: NOTE-BORD-EON-139-ARMEMENT-IR-x (sha256 964e05db2efc250121f4974c3d1ee5aa57dd0f7aad3cb7eb600fde6afc8c85ad, sceau 2026-10-12T13:16:31Z)
instruments:
  - "irx_cone.py, sha256 827df834e7ff941c8647edb7fa99e0b8d79fded2a790613739528e81b50ec713, 2026-10-12T13:17:12Z : EXIT 0, sortie irx_cone_sortie.txt"
depend: [NOTE-BORD-EON-139-ARMEMENT-IR-x, NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-142-AUDIT-IR-x-CONCORDANCE, NOTE-BORD-EON-143-ACTE-GREFFE-IR-x]
verdict: "X-V1"
prediction_realisee: "oui"
rouvre_si:
  - "version purement ponctuelle sans domination locale (non tranchee par XA-1, pathologique, aucun exemple connu)"
  - "donnees de φ_h sur 𝓘⁺ hors du cadre distributionnel, ou bord non spatial"
---

# NOTE-140 : IR-x. Aucune solution homogene de □², singuliere ou non, ne compense le pole hors d'un ensemble de mesure nulle. Verdict **X-V1** (v2 : voir greffe)

> **Greffe IR-x (v2, 2026-10-12).** Corrections issues de l'audit froid aveugle NOTE-142 (XA-V2 ; rapports XA-1 482220e3f4500b7a…, XA-2 e8647942b05a0ebd…). Les resultats porteurs sont inchanges et renforces : x-3 retrouve deux fois (c_n = 0 pour tout n, y compris s^μ et ln² s), x-2 retrouve (24 composantes, e⁻³ sur le cone), verdict X-V1 inchange.
> 1. **(i) Argument general** [corrige IR-x] : l'enonce « propagation des singularites » (§2.1 v1) est remplace par le **probleme de Cauchy hyperbolique** (Garding) joint a l'**unicite de Holmgren** : toute solution distributionnelle de □²φ = 0 sur une tranche (0, ε) × Ω se prolonge en fonction C^∞ de s a travers s = 0, a valeurs distributions, **sans hypothese de croissance temperee** ; les hyperfonctions n'echappent pas non plus. La propagation du front d'onde est un enonce interieur ; le resultat pertinent est le prolongement a travers une hypersurface non caracteristique d'un operateur hyperbolique.
> 2. **(ii) Ensembles exceptionnels** [corrige IR-x] : la phrase « ln s qu'aux sommets, points isoles » est trop etroite. Un comportement en ln s (et un R en s⁻¹) est possible ponctuellement sur des **points** (sommets sur le bord), des **2-spheres** (cone de sommet au-dela du bord, front nul traversant s = 0), des **2-plans** (superposition plane de sommets, φ = −π ln |z² − s²|) et des **unions denombrables** (eventuellement denses) ; toujours d'interieur vide, de mesure nulle, et **nuls au sens des distributions**. Avec un poids ajuste, une superposition plane pourrait compenser le pole sur ce plan ; jamais sur un ouvert.
> 3. **(iii) x-2 structurel** [ajout IR-x] : l'absence de pole hors du sommet est vraie pour tout T lisse au point choisi ; le test x-2 ne sonde donc que la regularite de φ en ce point, et n'est pas discriminant par construction.
> 4. **Defauts mineurs du script** [ajout IR-x, XA-2] : droite symetrique et A = 0 pour l'ordre au cone ; conclusion automatique de x-3 limitee a c₀..c₄ (le resultat imprime est juste) ; `coeff(s, 0)` ignore les termes s⁰ ln s (inoffensif ici). Reexecution identique octet pour octet.
> 5. **Point reste ouvert** [ajout IR-x] : la version purement ponctuelle sans domination locale, non tranchee par XA-1 (pathologique, aucun exemple connu) ; portee en `rouvre_si`.

## 0. Resume
- **x-1** : ln σ, 1/σ et s/σ (σ = r² − s²) verifient □² = 0 hors du cone ; leur singularite est portee par le cone r = s, issu d'un point-sommet de 𝓘⁺, qui est caracteristique [calcule].
- **x-2** : pour φ_h = ln σ, en un point de 𝓘⁺ distinct du sommet, **aucun pole** dans les 24 composantes de R de (2.17) ; en revanche R est singulier en σ⁻³ sur le cone, dans le volume [calcule]. Un tel φ_h correspond a un etat non Hadamard.
- **x-3** : dans l'ansatz general φ = Σ (a_n(x) + c_n(x) ln s) s^n, n = 0 a 7, □²φ = 0 force **c₀ = … = c₇ = 0** : aucune solution homogene ne porte de ln s le long de 𝓘⁺ [calcule].
- **x-4** : la composante q = 0 est un polynome cubique en s [calcule].
- Le comportement en ln s n'apparait que sur des ensembles exceptionnels de 𝓘⁺ (points, 2-spheres, 2-plans, unions denombrables), de mesure nulle et nuls au sens des distributions [corrige IR-x]. La compensation du pole est donc impossible hors d'un ensemble de mesure nulle, quel que soit l'etat, et pour toute solution distributionnelle, sans hypothese de croissance [corrige IR-x].

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
1. **Pourquoi aucun ln s le long de 𝓘⁺.** {s = 0} est une hypersurface spatiale, non caracteristique pour □² ; s = 0 n'est pas un point singulier de cet operateur a coefficients constants (racines indicielles 0, 1, 2, 3, sans log). x-3 le montre directement : le terme −6c₀/s⁴ ne peut etre compense par aucun autre, puis la recurrence annule tous les c_n. [corrige IR-x] Le resultat general est le probleme de Cauchy hyperbolique (Garding) joint a l'unicite de Holmgren : toute solution distributionnelle sur une tranche (0, ε) × Ω se prolonge en fonction C^∞ de s a travers s = 0, a valeurs distributions, sans hypothese de croissance ; un ln s porte par un ouvert de l'hypersurface spatiale {s = 0} est exclu. (La v1 invoquait la propagation des singularites, enonce interieur, imprecis ici.) Contraste : un ln s generique exigerait un operateur fuchsien en s = 0 ou un bord caracteristique, ni l'un ni l'autre ici. Propagateur de □² : K̂(s, k) = (sin ks − ks cos ks)/(2k³), entier en s.
2. **Ce que font les solutions de cone.** Elles portent leur singularite sur le cone passe d'un point-sommet de 𝓘⁺. En un point de 𝓘⁺ hors du sommet, elles sont analytiques en s pres de 0 (σ → r² > 0) : T̂ = s² × (lisse), donc pas de pole (NOTE-131 t-2, confirme par W-c). Sur l'axe r = 0, ln |σ| = 2 ln s : pour un sommet sur le bord, le comportement logarithmique n'existe qu'au sommet, point isole. [corrige IR-x] Pour un sommet decale en s = −s₀, le cone traverse s = 0 sur la sphere r = s₀, ou ln |σ′| = ln s + ln(s + 2s₀) : un ln s des deux cotes, trace d'un front nul qui traverse le bord, non un phenomene de bord ; R y est en s⁻¹, homogene de degre −1 en la distance au coin. (Avec ½ ln |σ|, le coefficient serait exactement celui qui compense, mais seulement sur cet axe.)
3. **Superpositions.** Une superposition de solutions de cone a sommets repartis sur 𝓘⁺, avec un poids lisse, est une solution a donnees lisses, donc lisse en s pres de 0 (x-3 s'applique) ; avec un poids distributionnel, les singularites restent portees par des cones, des spheres de traversee et des sommets. [corrige IR-x] Une superposition plane de 1/σ (valeur principale) donne φ = −π ln |z² − s²|, soit φ = −2π ln s exactement sur le plan z = 0 et R ~ s⁻¹ sur ce plan, regulier hors du plan ; une superposition denombrable dense Σ 2^{−j} ln |σ_j| donne un ln s ponctuel sur un ensemble dense, de coefficient distributionnel nul. Aucune ne produit un ln s sur un ouvert de 𝓘⁺.
4. **Admissibilite.** Une solution de cone donne un R (et un T̂) singulier sur une hypersurface nulle du volume. Elle correspond a un etat dont le tenseur renormalise n'est pas lisse, donc non Hadamard.
5. **Mode q = 0.** Pour une onde plane de vecteur k, la composante de vecteur k du terme φ_h C ne recoit, a l'ordre lineaire, que la composante q = 0 de φ_h, cubique en s : jamais de ln s.

```
   compensation du pole G-V3 par phi_h homogene

   phi_h lisse (etat regulier)        -> pas de pole            (NOTE-131, W-c)
   phi_h de cone, hors sommet          -> pas de pole            (x-2, calcule)
   phi_h de cone, au sommet            -> ln s ponctuel          (point isole de scri+)
   phi_h de cone, sommet au-dela       -> ln s sur une 2-sphere   (front nul transverse, XA-1/XA-2)
   superposition plane                 -> ln s sur un 2-plan      (XA-2)
   superposition denombrable           -> ensemble dense, interieur vide, nul au sens de D'
   phi_h ~ alpha(x) ln s sur un ouvert -> impossible : c_n = 0   (x-3, calcule)
   cout des solutions de cone          -> R ~ sigma^-3 sur un cone du volume : non Hadamard
```

## 3. Verdict
**X-V1.** Les solutions de cone sont homogenes sur s > 0, singulieres sur des cones caracteristiques du volume (etat non Hadamard), et ne produisent de comportement en ln s que sur des ensembles exceptionnels de 𝓘⁺ (points, 2-spheres, 2-plans, unions denombrables), de mesure nulle et nuls au sens des distributions [corrige IR-x]. Aucune solution homogene de □², distributionnelle ou non, sans hypothese de croissance, ne se comporte en α(x) ln s sur un ouvert de 𝓘⁺ [corrige IR-x]. Le pole n'est compense par aucun φ_h, singulier ou non, hors d'un ensemble de mesure nulle. **L'hypothese d'etat de NOTE-131 n'est plus necessaire pour le secteur φ_h** ; elle le reste pour la partie non locale Γ[g].

## 4. Confrontation a la prediction
Prediction (NOTE-139 §4) : □² = 0 hors cone, support singulier caracteristique [**realise**] ; pas de pole hors du sommet, R singulier sur le cone [**realise**, ordre σ⁻³] ; α = 0 force [**realise**, et tous les c_n jusqu'a n = 7] ; q = 0 cubique [**realise**] ; mesure nulle [**realise**]. **Prediction realisee.**

## 5. Consequences (rien n'est grave)
- La classe de NOTE-131 se reduit : « WZ integrable + Γ[g] etat regulier + **φ_h homogene quelconque** ». L'hypothese de regularite de φ_h tombe ; seule demeure celle de l'etat pour Γ[g].
- Le point ouvert releve par W-c (NOTE-137) est clos. [ajout IR-x] Audite : NOTE-142, XA-V2 ; greffe entee par NOTE-143.
- Libelle de G-V3 (NOTE-138) inchange, a une precision pres, a porter lors d'une revision : la classe d'hypotheses devient « WZ integrable + Γ[g] etat regulier », sans condition sur φ_h.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- [corrige IR-x] Audit froid realise (NOTE-141/142, XA-V2) ; greffe entee (NOTE-143).
- Seule hypothese d'etat restante : regularite de Γ[g] en 𝓘⁺ (noyau retarde, passe adiabatique). Une instruction directe (IR-y) porterait sur le tenseur de Γ[g] pour un etat non regulier mais Hadamard.
- Lecture de Foraci-Woodard 2501.01972, sous gel.

## 7. Non-surclassement
[conv], audite (NOTE-142, XA-V2). Premier ordre en ε, fond de Sitter, mode tensoriel pour x-2. Les theoremes de Garding et de Holmgren sont cites de memoire par l'auditeur XA-1, numeros non certifies ; x-3 en donne une verification formelle independante (recurrence exacte P(m)c_m − 2(m−2)(m−3)Δc_{m−2} + Δ²c_{m−4} = 0, P(m) ≠ 0).
