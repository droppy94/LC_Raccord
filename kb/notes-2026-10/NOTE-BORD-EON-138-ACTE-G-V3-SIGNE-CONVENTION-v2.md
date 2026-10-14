---
id: NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION
numero: 138
serie: I
branche: Q-M3 suite (decision)
reservation: 2026-10-12T13:12 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 138)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 5a778f86aec326e7 (16 premiers ; conservee)"
greffe: "revision du libelle de G-V3 entee le 2026-10-12 par NOTE-BORD-EON-144 (suite de NOTE-140 v2 et de l'audit NOTE-142, XA-V2)"
nature: "acte de decision operateur (reexamen argumente, une lecture declaree hors gel, aucun calcul nouveau au-dela d'un ordre de grandeur)"
decision: "operateur (Thierry), 2026-10-12 15:10 heure de Paris (acte demande), puis option « A : lisse maintenue » retenue en reponse au reexamen (15:13 environ)"
depend: [NOTE-BORD-EON-126-ACTE-DECISION-CONVENTION-LISSE, NOTE-BORD-EON-133-IR-u-EXECUTION, NOTE-BORD-EON-135-IR-v-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-140-IR-x-EXECUTION, NOTE-BORD-EON-142-AUDIT-IR-x-CONCORDANCE, NOTE-BORD-EON-144-ACTE-REVISION-LIBELLE-G-V3]
sources:
  - "Dvali, Gomez, Zell, arXiv:1701.08776v2 : extraits src/SOURCE-1701.08776v2-extraits.txt, sha256 a285ac7e798aa0daaf73e0ead1b6da19efd65a1b7d56dd6988f9a017e8ba1d85 (lecture hors gel, declaree : elle sert le reexamen, pas un verdict)"
---

# NOTE-138 : acte. Libelle de G-V3, convention de signe physique, reexamen de la convention lisse (v2 : voir greffe)

> **Revision du libelle (v2, 2026-10-12).** Entee par NOTE-144 a la suite de NOTE-140 v2 (X-V1) et de l'audit NOTE-142 (XA-V2). Un seul changement, annonce par NOTE-140 §5 et NOTE-142 §6 : la classe d'hypotheses du libelle de G-V3 (§1.3) passe de « WZ integrable + Γ[g] etat regulier + φ_h lisse » a **« WZ integrable + Γ[g] etat regulier »**, sans condition sur φ_h, et la mention « premier ordre en ε » est completee par la liste des hypotheses de NOTE-131 et 140 v2. Les decisions 1, 2 et 4, le reexamen (§2) et les options consignees sont inchanges. Les points ouverts du §3 sont mis a jour. Passages marques `[corrige rev-138]`.

## 1. Decisions
1. **Convention de signe physique (Carroll-Wald).** Pour tout libelle et toute lecture physique : ⟨T_ab⟩ = −(2/√−g) δW/δg^{ab}, signature (−,+,+,+) ; terme local de l'action anomale W ⊃ +b ∫√−g σ C², σ = −ln Ω ; d'ou T_ab = −8b ∂^c∂^d(σ C_acbd) (c₀ = −8). La convention de calcul c₀ = +8 du gel de NOTE-124 reste valide pour la tracabilite de NOTE-125 a 133 ; le passage de l'une a l'autre se fait par b → −b. Base : NOTE-133 §2.4, NOTE-137 (W-a, derivation aveugle de bout en bout).
2. **Convention de regularite : lisse maintenue (option A).** La convention de NOTE-126 est confirmee apres reexamen (§2), au sens de la **limite** Ω → 0, qui est celui sous lequel la CCC est formulee (Tod 1309.7248 ; Meissner-Penrose 2503.24263).
3. **Libelle de G-V3** (remplace celui de NOTE-126 §3) :
   > **G-V3, obstruction de principe** : en presence, a 𝓘⁺, de champs quantiques conformes (b > 0) et d'ondes gravitationnelles a donnee electrique non nulle, le Weyl rescale n'a pas de limite finie en 𝓘⁺ : W ≈ W₀ (1 + 8bκ ln a) au premier ordre (γ = 8, calcule et retrouve a l'aveugle ; coefficient identique a Foraci-Litos-Woodard 2026 pour trois especes) ; sous la prescription de resommation de Woodard 2025 (logarithmes dominants), W ∝ Ω^(−ε), ε = 8bκH² > 0, de signe universel. Incompatible avec un raccord lisse au sens de la limite, et plus generalement avec tout raccord exigeant W fini en 𝓘⁺. **Portee physique** : ε ~ 10⁻¹²² × N_eff pour H actuel ; l'effet ne devient d'ordre un qu'apres ~1/ε e-folds, echelle de meme dependance parametrique que le temps de rupture quantique de de Sitter (Dvali-Gomez-Zell), ou la description semi-classique dont G-V3 est issu cesse d'etre fiable. Candidat, non grave ; classe « WZ integrable + Γ[g] etat regulier », sans condition sur φ_h (toute solution homogene de □², singuliere ou non, ne compense le pole que sur un ensemble de mesure nulle, nul au sens des distributions : NOTE-140 v2, audit NOTE-142) [corrige rev-138] ; fond de Sitter exact, premier ordre en ε et en bκ, mode tensoriel, action effective a une boucle, passe adiabatique, reduction d'ordre, resommation par logarithmes dominants non demontree [corrige rev-138].
4. **M-V3** : libelle de NOTE-126 §3 inchange.

## 2. Reexamen de la convention lisse [derive, sauf mention]
### 2.1 La divergence ne discrimine pas entre degres de regularite
W ∝ Ω^(−ε) n'est pas borne en 𝓘⁺. Les conventions (b) C³ et (c) C², ecartees en NOTE-126, ne sauveraient pas le raccord : toute convention qui exige un W fini est violee. Le choix entre « lisse » et « C^k » n'est donc plus le point decisif pour G-V3 ; seule une convention tolerant une divergence (borne a Ω^(−ε) pres) l'evite.

### 2.2 L'exposant ne se deplace pas dans le facteur conforme
Choisir Ω′ = Ω^(1−ε) rend W′ = C/Ω′ fini, mais la metrique compactifiee g′ = Ω′² ĝ = Ω^(−2ε) g degenere en 𝓘⁺. La singularite est deplacee, non supprimee.

### 2.3 Ordre de grandeur et seuil
- ε par scalaire conforme : GH²/(30π). Avec S_dS = π/(GH²) : ε·S_dS = 1/30 (1/5 par fermion de Dirac, 2/5 par photon) [calcule].
- H actuel (2,2 × 10⁻¹⁸ s⁻¹) : GH² ≈ 1,4 × 10⁻¹²², 1/ε ≈ 6,7 × 10¹²³ e-folds par scalaire, divise par le poids effectif du contenu de champs [calcule, ordre de grandeur].
- Dvali-Gomez-Zell (arXiv:1701.08776, eq. 90 et p. 47) : la description classique de de Sitter n'est fiable que sur au plus M_P²/(N_sp H²) e-folds [extrait]. Meme dependance parametrique (M_P²/H², inverse du nombre d'especes) que 1/ε [derive ; l'accord porte sur la dependance, pas sur les facteurs numeriques].

### 2.4 Lecture
Dans le domaine ou il est derive, G-V3 est un facteur 1 + O(10⁻¹²²) : formel. Il ne devient d'ordre un qu'a la frontiere ou la description semi-classique tombe pour une raison independante. Mais la CCC elle-meme prolonge la geometrie conforme classique jusqu'a Ω → 0, donc au-dela de cette frontiere. G-V3 atteint la CCC **telle qu'elle est formulee** (enonce de limite) ; il ne peut etre ni leve ni confirme physiquement dans le cadre qui le produit. D'ou le terme « obstruction de principe ».

### 2.5 Options examinees
| Option | Convention | Statut de G-V3 | Retenue |
|---|---|---|---|
| A | lisse, au sens de la limite | candidat d'incompatibilite, obstruction de principe, portee physique inscrite au libelle | **oui** |
| B | regularite exigee dans le seul domaine semi-classique (tolerance Ω^(−ε)) | declasse : effet formel hors domaine | non |
| C | lisse, question declaree hors cadre | indecidable dans le cadre semi-classique | non |

Les options B et C restent consignees pour toute revision. B serait a reconsiderer si le programme adoptait une formulation de la CCC a temps conforme fini ; C, si un cadre au-dela du temps de rupture montrait que la limite Ω → 0 n'a pas de sens physique.

```
   statut de G-V3 en fonction de la convention

   exige W fini en scri+ (lisse, C^k, k >= 0)  ->  W ~ Omega^(-eps) : INCOMPATIBLE   <- retenu (A)
   tolere W ~ Omega^(-eps)                    ->  compatible, effet formel       (B, non retenu)

   portee : eps ~ 1e-122 x N_eff ; O(1) apres ~1/eps e-folds ~ temps de rupture quantique de dS
```

## 3. Effets
- G-V3 : libelle §1.3 en vigueur ; toute citation doit reprendre la mention de portee physique.
- La reserve de NOTE-126 (« le choix est une convention, pas un resultat ») est maintenue et precisee : pour G-V3, la convention en jeu n'est plus le degre de lissite mais l'exigence d'un W fini.
- Points ouverts [corrige rev-138] : solutions de cone de φ_h **clos** (NOTE-140 v2, audit NOTE-142) ; seule hypothese d'etat restante, regularite de Γ[g] en 𝓘⁺ (piste IR-y) ; secteurs hors classe ; source primaire des resommations (2501.01972), lecture sous gel a venir.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 restent des candidats non graves : aucun acte de gravure n'est pris ici.

## 4. Non-surclassement
Acte [conv] ; v2 editoriale, un seul passage de fond modifie (la classe du libelle), sans calcul ni lecture nouvelle. Le reexamen est un argument, non un resultat audite ; le rapprochement avec le temps de rupture est parametrique. La lecture de Dvali-Gomez-Zell est hors gel et declaree comme telle.
