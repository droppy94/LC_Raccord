---
id: NOTE-BORD-EON-135-IR-v-EXECUTION
numero: 135
serie: I
branche: Q-M3 suite (IR-v)
reservation: 2026-10-12T12:43 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 135)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-134-ARMEMENT-IR-v (sha256 4fdd98a3574fbd68dd11c5c870bd6032c72507922cb4c37d89bd155d65e5bea2, sceau 2026-10-12T12:43:56Z)
sources:
  - "R. P. Woodard, arXiv:2501.05077v1 (2025) : extraits src/SOURCE-2501.05077v1-extraits.txt, sha256 2f08e3f1bed7f022498a14b4ff22aba53f9bb353348a11e46ec493445755b01d"
instruments:
  - "irv_conversion.py, sha256 b2cbf6421f7652f100c586761a892638227e59754a93e6b8f8a798fe040516a6, 2026-10-12T12:44:38Z : EXIT 0, sortie irv_conversion_sortie.txt"
depend: [NOTE-BORD-EON-134-ARMEMENT-IR-v, NOTE-BORD-EON-133-IR-u-EXECUTION]
verdict: "V-V1"
prediction_realisee: "partiellement (issue V-V1, prevue comme possible ; la prediction principale etait V-V2)"
rouvre_si:
  - "lecture de Foraci-Woodard arXiv:2501.01972 (source primaire des resommations) contredisant la loi de puissance ou ses conditions"
  - "audit froid de NOTE-133 modifiant la conversion des normalisations ou le signe"
  - "remise en cause de la variante du groupe de renormalisation (logarithmes dominants) par un calcul a deux boucles"
---

# NOTE-135 : IR-v. Woodard resomme le Weyl des ondes gravitationnelles en a^(8bκH²). D'ou W_E ∝ Ω^(−8bκH²). Verdict **V-V1**

## 0. Resume
- **v-1** : oui. La source donne une forme resommee **explicitement pour le Weyl electrique des ondes gravitationnelles**, en presence de matiere conforme (scalaire conforme, fermion de Dirac, photon), et pas seulement pour le potentiel newtonien [extrait].
- **v-2** : c'est une **loi de puissance en a**. Les exposants, convertis par la regle figee au gel, valent exactement 8bκH² pour les trois especes : G/(30π), G/(5π), 2G/(5π) (H = 1) [extrait + calcule].
- **v-3** : conditions enoncees par l'auteur : logarithmes dominants (« at most a single large logarithm at 1-loop order ») ; « variant » de l'equation de Callan-Symanzik ou ln μ est remplace par ln a ; corrections de matiere independantes de jauge [extrait].
- **v-4** : la forme est presentee comme valable « as long as the de Sitter phase persists », donc pour a → ∞ sur de Sitter, la ou se pose la question du raccord [extrait].
- Consequence [derive] : **W_E ∝ Ω^(−8bκH²)** en 𝓘⁺. Le Weyl rescale diverge en loi de puissance, avec un exposant de signe universel.

## 1. Lecture (EX-7, EX-9) [extrait]
Source unique figee au gel, lue apres le sceau (12:43:56Z). Resume, §1, §2.3 (catalogue), §4 (groupe de renormalisation modifie) en entier, §4.4 et debut du §5 (section suivante). Extraits verbatim sauvegardes.

| Element | Contenu de la source |
|---|---|
| Mecanisme (§2.1, §4) | logarithmes issus du desaccord entre divergences primitives et contre-termes ; les contre-termes en C² (c₂) et R² (c₁) sont lus comme renormalisations dependant de la courbure |
| Equation (eq. 143) | « The Weyl tensor for gravitational radiation and the potentials can be viewed as 2-point Green's functions » ; [∂/∂ ln μ + 2γ] G⁽²⁾ = 0, ln μ n'entre que par ln(μa) |
| Scalaire conforme (eq. 147-148) | c₁ = 0 ; C₀ᵢ₀ⱼ → C^tree × a^(κ_W²H²/480π²) |
| Fermion de Dirac (eq. 150-151) | C₀ᵢ₀ⱼ → C^tree × a^(κ_W²H²/80π²) |
| Photon (eq. 153-154) | C₀ᵢ₀ⱼ → C^tree × a^(κ_W²H²/40π²) ; premier ordre (eq. 65) : 1 + κ_W²H²/(40π²) ln a |
| Domaine | « as long as the de Sitter phase persists » (§4.2.1) ; logarithmes dominants seulement (§4.4) |
| Jauge (§5) | corrections de matiere a la gravite « completely gauge independent » |
| Source primaire | les resommations 148, 151, 154 sont attribuees a Foraci et Woodard, arXiv:2501.01972 (cite, non lu) |

## 2. Conversion [calcule, irv_conversion.py]
Regle figee (NOTE-134 §1) : κ_W² = 16πG, κ = 8πG, b = (N_S + 6N_F + 12N_V)/(120(4π)²), Ω ∝ 1/a.

| Champ | Exposant de Woodard (W ∝ a^p) | 8bκH² | Rapport |
|---|---|---|---|
| scalaire conforme | G/(30π) | G/(30π) | 1 |
| fermion de Dirac | G/(5π) | G/(5π) | 1 |
| photon | 2G/(5π) | 2G/(5π) | 1 |

Le premier ordre de ces formes resommees redonne exactement les logarithmes de NOTE-133 : la chaine est coherente du premier ordre (calcul propre, γ = 8) a la resommation (source).

## 3. Lecture [derive]
1. **Forme resommee** : W_E(Ω) ≈ W₀ (Ω/Ω₀)^(−8bκH²), avec 8bκH² = 8κH² Σ b_i pour un contenu de champs conformes {i}.
2. **Signe universel** : le coefficient b (c dans la trace) est strictement positif pour tout champ conforme unitaire. Les contributions s'ajoutent toutes avec le meme signe ; aucun contenu de champs ne peut les compenser. Le Weyl rescale **diverge** en 𝓘⁺ (il ne s'annule pas), quel que soit le secteur conforme.
3. **Ordre de grandeur** : pour H ~ H_Λ actuel, GH² ~ 10⁻¹²² en unites de Planck. La divergence est donc formelle et d'une lenteur extreme. Elle n'en est pas moins une divergence : W n'a pas de limite finie en Ω → 0, ce qui est la propriete que mesure la convention lisse (NOTE-126).
4. **Statut du « variant »** : l'equation de Callan-Symanzik avec ln μ → ln a est une prescription de resommation des logarithmes dominants, justifiee par l'auteur par l'accord avec les calculs exacts a une boucle (et a deux boucles dans d'autres modeles). Ce n'est pas un theoreme. La forme Ω^(−8bκH²) a ce statut.
5. **Coefficient de normalisation de l'arbre** : la resommation multiplie C^tree, quelle que soit la puissance de a portee par l'arbre dans les conventions de l'auteur. Le facteur correctif est donc transposable a W_E, dont l'arbre tend vers W₀ fini en 𝓘⁺ (NOTE-133).

```
   W_E / W0 en fonction de Omega -> 0  (de Sitter, matiere conforme, b > 0)

   premier ordre :   1 - 8 b kappa H^2 ln Omega          (NOTE-133, calcule)
   resomme       :   Omega^(-8 b kappa H^2)              (Woodard eq. 148/151/154, converti)

   exposant > 0 pour tout champ conforme unitaire  ->  divergence, pas d'annulation
   exposant ~ 1e-122 x N pour H actuel             ->  divergence formelle, extremement lente
```

## 4. Verdict
**V-V1.** La source resomme les logarithmes en une loi de puissance en a pour le Weyl electrique des ondes gravitationnelles, avec un exposant egal, apres conversion, a 8bκH², pour trois especes de champs conformes, et la presente comme valable tant que dure la phase de Sitter. D'ou W_E ∝ Ω^(−8bκH²). Qualifications nommees : (i) logarithmes dominants, prescription de resommation non demontree ; (ii) source primaire (Foraci-Woodard 2501.01972) non lue ; (iii) normalisations de b et κ et signe sous reserve de l'audit de NOTE-133 ; (iv) fond exactement de Sitter.

## 5. Confrontation a la prediction
Prediction (NOTE-134 §4) : « V-V2, avec possibilite V-V1 » ; mecanisme par contre-termes en C² et R² avec ln μ → ln a [**realise**] ; exposant egal au coefficient du premier ordre [**realise**] ; application explicite d'abord au potentiel newtonien, ondes gravitationnelles incertaines [**non realise** : le Weyl des ondes gravitationnelles est traite explicitement, a egalite avec le potentiel] ; conditions logarithmes dominants [**realise**]. Prediction **partiellement realisee** : l'issue est celle declaree comme possible, non la principale.

## 6. Consequences (rien n'est grave)
- **G-V3 au-dela du premier ordre** : sous la prescription de resommation de Woodard, le pole de (2.17) se resomme en une divergence en loi de puissance du Weyl rescale en 𝓘⁺, W ∝ Ω^(−8bκH²), de signe universel. Le libelle propose en NOTE-133 §6 peut etre complete : « … ; resomme (logarithmes dominants, Woodard 2025) : W ∝ Ω^(−8bκH²), exposant positif pour tout contenu conforme unitaire ».
- **Point a peser par l'operateur** : l'exposant est ~10⁻¹²² × N pour H actuel. Sous la convention lisse (NOTE-126), une divergence aussi lente reste une incompatibilite. Sous une convention plus faible (W borne a un facteur Ω^(−ε) pres, ε arbitrairement petit), elle ne le serait pas. Le choix de convention, deja tranche en NOTE-126, prend ici tout son poids.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 restent des candidats non graves.

## 7. Pistes
- **Audit froid** de NOTE-131, 133 et 135 (conversion des normalisations, signe, lecture des sources).
- **Lecture de Foraci-Woodard 2501.01972** (source primaire des resommations), sous gel.
- **Acte** : libelle de G-V3 (NOTE-133 §6 complete par §6 ci-dessus), et reexamen explicite de la convention lisse face a un exposant de l'ordre de 10⁻¹²², sur decision de l'operateur.

## 8. Non-surclassement
[conv], non audite. Lecture d'une revue (non de la source primaire), logarithmes dominants, fond de Sitter. La concordance porte sur l'exposant ; l'interpretation en termes de raccord reste propre au programme.
