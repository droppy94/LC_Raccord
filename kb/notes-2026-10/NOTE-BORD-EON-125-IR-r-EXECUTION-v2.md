---
id: NOTE-BORD-EON-125-IR-r-EXECUTION
numero: 125
serie: I
branche: Q-M3 suite (retroaction IR-r)
reservation: 2026-10-11T17:51 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 125)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 6150cb19aae7bc55fd7caadbe836cfedb9d79905d94df9a1b8d3f128c1c72c69 (conservee)"
greffe: "IR-s-b entee le 2026-10-12 par NOTE-BORD-EON-129 (corrections de l'audit froid aveugle NOTE-128, AU-V2)"
audit: "NOTE-BORD-EON-127 (gel) / NOTE-BORD-EON-128 (concordance) : AU-V2 ; pole retrouve en cecite stricte par S-a1 (valeur absolue 8b kappa, signe selon la convention de T) ; robustesse et partie a (S-b)"
gel: NOTE-BORD-EON-124-ARMEMENT-IR-r (sha256 a736ef17a1ad3326dcc18a5dc24ded22f2ab3cf4b8179d88d0a51ee9f6896871, sceau 2026-10-11T18:00:44Z)
instruments:
  - "irr_c.py, sha256 ef0c3f4fac14d233652deafaf931348b47736596f9ff33aa3fc678de7019cde9, 2026-10-11T18:01:35Z : EXIT 0, sortie irr_c_sortie.txt"
  - "irr_c_ctrl.py, sha256 8035a342d686d4f2a760f5469d960812e8a03f659ba9c439c40c77303bb548ed : EXIT 0, sortie irr_c_ctrl_sortie.txt (controle ajoute apres execution, non prevu au gel : identification de B avec le Weyl electrique rescale)"
depend: [NOTE-BORD-EON-124-ARMEMENT-IR-r, NOTE-BORD-EON-120-AUDIT-IR-m-CONCORDANCE, NOTE-BORD-EON-123-IR-q-EXECUTION]
verdict: "R-V1 qualifie R-V3"
prediction_realisee: "oui"
rouvre_si:
  - "partie a (Euler) de l'action anomale au premier ordre en h"
  - "partie invariante de Weyl non locale de l'action effective gravitationnelle (facteur de forme) pres de scri+"
  - "choix de la solution phi de l'equation auxiliaire (modes homogenes de Delta_4) ; etat non conforme"
  - "audit froid"
---

# NOTE-125 : IR-r. Sur un fond portant des ondes gravitationnelles, le terme φC² met un pole Ω⁻¹ dans (2.17). Verdict **R-V1 qualifie R-V3** (v2 : voir greffe)

> **Greffe IR-s-b (v2, 2026-10-12).** Corrections issues de l'audit froid aveugle NOTE-128 (AU-V2). Le resultat porteur est confirme : S-a1, en cecite stricte, retrouve le pole avec la meme valeur absolue 8bκ. S-b le reproduit et montre qu'il resiste a la polarisation croix, a un k oblique, a une superposition de modes, aux diffeomorphismes lineaires et au changement de facteur conforme.
> 1. **Convention de signe.**
>    - Avec T_ab = (2/√g)δS/δg^{ab}, convention ecrite au gel NOTE-124 §1, la forme fermee est T_ab = **+8b** ∂^c∂^d(φC_acbd) et le pole vaut **R_isj|pole = −(8bκ/Ω) w_ij** (S-a1, S-b).
>    - Avec T^{ab} = (2/√−g)δS/δg_ab (Carroll, Wald), coherente avec ⟨T^a_a⟩ = bC² + … pour l'action +b∫σC², c0 = −8 et le pole vaut +(8bκ/Ω) w_ij (valeurs de la v1).
>    - La valeur absolue et l'existence ne dependent pas de la convention. Le commentaire de la ligne 59 de irr_c.py est errone sur ce point (script conserve, R-55).
> 2. **Generalite** : R_isj|pole = −c0 bκ W_E,ij/Ω des que Bach[g] = 0, pour toute polarisation, toute direction de k et toute superposition (S-b) ; R_ijk et R_sij n'ont pas de pole. Forme exacte : T̂_ij = ∓8b Ω W_sisj. La donnee B porte la partie electrique W_E ; la donnee A porte la partie magnetique (W_syxy → ½Ak³ sin kx), qui ne produit pas de pole.
> 3. **Origine du pole** (S-a1) : L̂_ij ∝ s W_ij ; ∇̂_s L̂ contribue −12, ∇̂_j L̂_si contribue +4 (par les Christoffel du fond), d'ou −8.
> 4. **Absence de log : sur couche seulement.** Le coefficient de ln s dans T̂ est ∝ s² Bach[g]. Pour un h source par une matiere (exemple de S-b : u = mode B + γs⁴), T̂ contient s² ln s et R un ln s, sans changer le pole. Cela concorde avec l'ordre κ²b du cas (ii).
> 5. **Consequence sur W (§2.5-2.6) corrigee.** Au premier ordre en bκ, W diverge logarithmiquement a 𝓘⁺ (W ≈ W₀(1 + c bκ ln Ω)), et la metrique-pont n'est que **C²** (modele f ~ τ³ ln τ, S-b). La forme resommee W ∝ Ω^γ et la classe C^{2,γ} de la v1 sont **conjecturales**. La regularite de W exige W_E|𝓘⁺ = 0 (S-a1).
> 6. **Partie a (Euler)**, calculee par S-b hors verdict : sous la forme de Wess-Zumino integrable ∫√g{bσC² + a[σ(E − ⅔□R) + 2σΔ₄σ]}, la partie a d'ordre ε se reduit a 6a ĝ, sans contribution a R. Les contre-termes locaux ∫R² et ∫C² ne contribuent pas non plus. La qualification R-V3 se reduit a la partie non locale Γ[g] et aux modes homogenes de φ (piste IR-t).

## 0. Resume
Au premier ordre en une onde gravitationnelle de de Sitter :
- Le terme de charge de Weyl de l'action anomale, b∫√g φ C² avec φ = −ln s, donne un tenseur physique T̂ **sans trace, conserve, sans aucun log**. Le ln s × ∂⁴h releve par l'audit M-b a pour coefficient le tenseur de Bach de la metrique conforme, nul pour une onde solution du vide.
- En revanche, les termes en derivees de φ donnent T̂ ~ s · w, ou w est la partie electrique du Weyl rescale a 𝓘⁺ (donnee libre de rayonnement gravitationnel). Le second membre de (2.17) porte alors un **pole** :

  **R_isj ⊃ (8bκ/Ω) w_ij**   (normalisation de irr_c.py ; le signe suit la convention de b) [corrige IR-s : avec la convention T_ab = (2/√g)δS/δg^{ab} du gel, −(8bκ/Ω) w_ij ; la valeur absolue est retrouvee a l'aveugle].

Ce terme est plus singulier que le log de M-V3, qui est d'ordre Ω⁰ ln Ω. Il ne depend pas du champ electromagnetique, et il existe pour tout champ quantique conforme a b ≠ 0, photon compris : il est donc **independant de C-M1**. La version retroaction (h d'ordre κ, source par la contrainte de Maxwell) est d'ordre κ²b et negligeable devant M-V3. Il s'agit d'un **candidat d'obstruction gravitationnelle**, non grave, a auditer et a completer (partie a, partie non locale).

## 1. Resultats [calcule]
### A. Controle de la forme fermee (irr_c.py, partie 0)
T_ab = c0 ∂^c∂^d(φ C_acbd[h]) coincide avec la variation brute d'Euler-Lagrange de φC² sur la famille diagonale de M-b, a un facteur pres : λ = −1/4, verifie identiquement sur les trois composantes. Normalisation retenue : c0 = −8, multipliee par b [corrige IR-s : c0 = −8 vaut pour T^{ab} = (2/√−g)δS/δg_ab ; c0 = +8 pour T_ab = (2/√g)δS/δg^{ab}, convention ecrite au gel].

### B. Mode tensoriel de de Sitter (partie 1)
h_yy = −h_zz = u(s) cos kx, u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks). Equation de mode verifiee (residu 0).
- Trace ĝ^{ab}T̂_ab = 0. Divergence ∇̂^a T̂_ab = 0 pour u quelconque.
- T̂_yy = −T̂_zz = b(−4Bk³ s + 4Ak⁴ s²) cos kx + O(s³) ; toutes les autres composantes sont nulles a cet ordre. **Aucun ln s.**
- Second membre de (2.17) :

| Composante | Developpement |
|---|---|
| R_ysy = −R_zsz | −4bκBk³ cos kx / s + 6bκAk⁴ cos kx + 4bκBk⁵ s cos kx |
| R_yxy = −R_zxz | 2bκBk⁴ sin kx − 2bκAk⁵ s sin kx |

### C. Identification (irr_c_ctrl.py)
Partie electrique du Weyl rescale de g = η + h : W_E,yy = −W_E,zz = −Bk³ cos kx/2 + O(s), W_E,xx = 0. Donc **R_isj|_pole = (8bκ/Ω) w_ij** avec w = W_E a 𝓘⁺, en la normalisation ci-dessus.

## 2. Lecture [derive]
1. **r-1** : le terme singulier est un **pole Ω⁻¹**, porte par la donnee de rayonnement B (ou w). La donnee de bord A ne donne que des termes reguliers. Origine : dans ∂∂(φC), (∂∂φ)C = C/s² et 2(∂φ)(∂C) donnent des termes en W/s qui ne se compensent pas. Le terme φ∂∂C, en ln s, est proportionnel au tenseur de Bach, nul sur couche [corrige IR-s : hors couche, pour un h source par une matiere, ce log est present (S-b) ; le pole n'en est pas change].
2. **r-2** : la structure tensorielle est celle de w (TT, electrique), a l'ordre Ω⁻¹. Le log de M-V3 est d'ordre Ω⁰ ln Ω et porte par Q_tf (polarisation electromagnetique). Ordres et structures different : **pas de compensation possible**, et le pole domine pres de 𝓘⁺ des que bw ≠ 0.
3. **r-3** : si h est la reponse metrique a la contrainte de Maxwell, w et le Bach sont d'ordre κ. La contribution a R est d'ordre κ²b (pole et log), negligeable devant M-V3 (ordre κβ).
4. **r-4** : b > 0 pour tout champ conforme physique (scalaires conformes, fermions sans masse, photons). Le canal existe donc pour la CCC **sous sa forme actuelle** (photons a 𝓘⁺, ondes gravitationnelles), sans C-M1. Il s'ajoute a CCC + M sous C-M1 (fermions devenus sans masse). Il ne concerne pas le repli acyclique, qui n'a pas de raccord a 𝓘⁺.
5. **Consequence sur W** : une source en Ω⁻¹ dans l'equation de Bianchi rescalee donne, au premier ordre en bκ, un terme en bκ w ln Ω dans W. Resomme, cela donnerait W ~ w Ω^γ avec γ = O(bκ) : une **dimension anormale du Weyl rescale** a 𝓘⁺. Le coefficient exact de γ demande l'equation de transport complete et n'est pas fixe ici. [corrige IR-s] Au premier ordre, W **diverge** logarithmiquement a 𝓘⁺. La forme resommee est conjecturale (piste IR-u).
6. **Regularite (convention de NOTE-123)** : avec W ~ Ω^γ, C[g] ~ Ω^{1+γ} et la metrique-pont est de classe C^{2,γ}. Le canal viole la lissite **et** une convention C³. Il est compatible avec une convention C², pas au-dela. [corrige IR-s] Au premier ordre en bκ, la metrique-pont n'est que C² (f ~ τ³ ln τ, S-b) ; la classe C^{2,γ} suppose la resommation. La convention retenue (NOTE-126) est la lissite.
7. **Ordre de grandeur** : γ ∝ bκH², ou κH² ~ (ℓ_P H)² ~ 10⁻¹²¹ et b ~ 10⁻³ par champ. L'effet est structurellement decisif pour la lissite et numeriquement minuscule. C'est la meme situation que M-V3, dont le coefficient porte aussi κ. Le critere du programme est structurel.

```
   ordre en Omega dans R de (2.17), pres de scri+
   Omega^-1 ───────────────── Omega^0 ln Omega ────────────── Omega^0 (regulier)
      │                              │
   canal gravitationnel           canal anomal de jauge (M-V3)
   b phi C^2, onde w != 0         beta F^2, Q_tf != 0, sous C-M1
   tout champ conforme (photon)   fermions devenus sans masse
   NOTE-125                       NOTES 91-121
```

## 3. Verdict
**R-V1 qualifie R-V3.**
- **R-V1** : pour une donnee gravitationnelle generique a 𝓘⁺ (w ≠ 0), le terme φC² de l'action anomale produit dans (2.17) un pole (8bκ/Ω) w_ij, plus fort que le log de M-V3, independant de C-M1.
- **R-V3** [corrige IR-s : la partie a a ete calculee par S-b et ne contribue pas ; restent la partie non locale et les modes homogenes de φ] : non calcules en v1 :
  - la partie a (Euler) de l'action anomale au premier ordre en h, qui ne contient φ que derive mais peut contribuer aux memes ordres ;
  - la partie invariante de Weyl non locale de l'action effective gravitationnelle ;
  - le choix de la solution φ de l'equation auxiliaire (modes homogenes de Δ₄).
  Chacun peut modifier le coefficient, voire compenser le pole.

## 4. Confrontation a la prediction
Prediction (NOTE-124 §4) : « R-V1 qualifie R-V3 ; pole Ω⁻¹ proportionnel a la partie electrique du Weyl rescale, porte par (∂∂φ)C + 2(∂φ)(∂C) ; tout champ conforme a b ≠ 0, independant de C-M1 ; cas (ii) d'ordre κb negligeable ; qualifications partie a, partie non locale, etat ». **Realisee.**
Deux precisions :
- l'ordre du cas (ii) est κ²b dans R (κb dans T̂) ;
- aucun ln s n'apparait sur couche, ce que la prediction ne disait pas.

## 5. Consequences (rien n'est grave)
- **Hypothese « fond fixe » (K-D2)** : elle masquait un canal **plus fort** que M-V3. Sous la convention « raccord lisse », ce canal suffirait a lui seul a violer la regularite de (2.17) des qu'il y a du rayonnement gravitationnel a 𝓘⁺, avec ou sans C-M1. M-V3 n'est plus le candidat le plus fort.
- **Nouveau candidat (nom propose : G-V3, « canal gravitationnel de l'anomalie »)** : incompatibilite d'un raccord lisse (ou C³) avec la presence simultanee, a 𝓘⁺, de champs quantiques conformes et d'ondes gravitationnelles. Il touche la CCC sous sa forme actuelle independamment de RG-4 (sous convention lisse) et CCC + M.
- **Tension avec Meissner et Penrose (NOTE-123, MP4, MP5)** : leur raccord est domine par une epoque d'ondes gravitationnelles et leur loi de conservation suppose W fini et transporte a travers X. Ce canal donne a W une dimension anormale d'ordre bκ : a signaler, sans conclure.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 6. Pistes proposees (non engagees)
- **IR-s** : audit froid aveugle de NOTE-123 et NOTE-125. [corrige IR-s] Conduit : NOTE-127/128, AU-V2.
- **IR-t** : partie a (Euler) de l'action anomale au premier ordre en h sur de Sitter ; compense-t-elle le pole ? [corrige IR-s] Partie a sans contribution (S-b, a acter) ; IR-t est reformulee : partie non locale Γ[g] et modes homogenes de φ.
- **IR-u** : transport de W avec la source (8bκ/Ω) w : coefficient exact de la dimension anormale γ ; lien avec la litterature des perturbations tensorielles en presence de l'anomalie de trace (a lire, EX-7 et EX-8).
- **IR-q-d** (greffe) : decision de convention de regularite (NOTE-123 §5), desormais a prendre avec ce canal en vue.

## 7. Non-surclassement
[conv], audite par NOTE-128 (AU-V2) [corrige IR-s]. Premier ordre en h et en bκ, fond de Sitter, partie c seule de l'action anomale, φ = −ln s. Aucune incompatibilite gravee. M-V3 et G-V3 sont des candidats.
