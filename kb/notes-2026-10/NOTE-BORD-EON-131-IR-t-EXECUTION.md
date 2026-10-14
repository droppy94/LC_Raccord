---
id: NOTE-BORD-EON-131-IR-t-EXECUTION
numero: 131
serie: I
branche: Q-M3 suite (IR-t)
reservation: 2026-10-12T12:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 131)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-130-ARMEMENT-IR-t (sha256 eef62b048845b0c53cc538cef04f4ef4cbe39b71776da82710eeac264814e815, sceau 2026-10-12T12:18:35Z)
instruments:
  - "irt_a.py, sha256 97ca373277844327960a23bcbd43b06035752a018c911afb772036e32993d95b, 2026-10-12T12:19:19Z : EXIT 0, sortie irt_a_sortie.txt"
  - "irt_a_ctrl.py, sha256 62b96e1cc4df53223d85e52bae766e33430e16c2dbd2302bb35380f82ffdae37 : EXIT 0 (controle de non-trivialite : coefficient non integrable −1/2 ; ajoute apres irt_a, non prevu au gel)"
  - "irt_gamma_phi.py, sha256 0d3f44cdde18ca5b5b17a8e7342e1c38ca27142fbf7aa4a29c917fe4f8b1e064 : EXIT 0, sortie irt_gamma_phi_sortie.txt"
depend: [NOTE-BORD-EON-130-ARMEMENT-IR-t, NOTE-BORD-EON-125-IR-r-EXECUTION (v2), NOTE-BORD-EON-128-AUDIT-IR-s-CONCORDANCE]
verdict: "T-V1 qualifie T-V3"
prediction_realisee: "oui"
rouvre_si:
  - "etat du repere plat non regulier en τ = 0 ; noyau retarde de Γ non convergent (passe non adiabatique)"
  - "action effective a une boucle inadequate comme source semi-classique ; ordres superieurs"
  - "audit froid"
---

# NOTE-131 : IR-t. Ni la partie a, ni la partie non locale, ni les modes homogenes de φ ne compensent le pole. Verdict **T-V1 qualifie T-V3**

## 0. Resume
- **t-1 (partie a)** : calcul independant de celui de l'audit S-b. Sous la forme de Wess-Zumino integrable, la partie a d'ordre ε se reduit **exactement** a 6a ĝ_ab, avec un fond T̂ = 6a ĝ retrouve sans l'imposer. Elle n'a aucun effet sur R. Le controle a coefficient non integrable (−½) donne un fond et une perturbation differents : le test discrimine.
- **t-2 (partie non locale Γ[g])** : un pole dans R exige un T̂ d'ordre Ω¹. Toute contribution de la forme s² × (tenseur lisse du repere plat) donne un R d'ordre au moins s⁰ [calcule]. Or Γ[g] ne depend que de quantites du repere plat, ou τ = 0 n'est pas un point distingue ; dans un etat regulier, son tenseur est lisse en τ = 0 [derive, sous hypothese d'etat].
- **t-3 (modes homogenes de φ)** : □_η²(ln s) = −6/s⁴ ≠ 0. Le log de φ n'est donc pas un mode homogene : il est force par la source de l'equation auxiliaire. Un mode homogene lisse ne produit aucun pole [calcule].
- **G-V3 est robuste** dans la classe « WZ integrable + Γ[g] dans un etat conforme regulier + φ_h lisse ». Les hypotheses restantes portent sur l'etat et sur la validite du traitement semi-classique.

## 1. Resultats [calcule]
### t-1 (irt_a.py, irt_a_ctrl.py)
Famille g = diag(−1, 1, 1 + eP, 1 + eQ)(s, x), densite √g[σ(E − ⅔□R) + 2σΔ₄σ], σ = −ln s, variation d'Euler-Lagrange par rapport a P, puis P = −Q = u cos kx (mode tensoriel).

| Grandeur | Coefficient 2 (integrable) | Coefficient −½ (controle) |
|---|---|---|
| T̂_yy, fond | **6/s² = 6 ĝ_yy** | 17/(2s²) ≠ 6ĝ_yy |
| T̂_yy, ordre ε − 6 δĝ_yy | **0** | non nul |

Le signe de normalisation est fixe par le fond (sgn = +1). Par symetrie d'helicite autour de k, les autres composantes d'ordre ε non proportionnelles a ĝ sont nulles. La partie a d'ordre ε vaut donc 6a ĝ_ab, covariantement constant : contribution nulle a R.

### t-2 (irt_gamma_phi.py)
T̂ = s^p Y, avec Y_yy = −Y_zz = y(s) cos kx, y = y₀ + y₁s + y₂s² + y₃s³ (sans trace, conserve).

| p | Plus basse puissance de s dans R | Terme en 1/s |
|---|---|---|
| 1 | −1 | κ y₀ cos kx (pole) |
| 2 | 0 | 0 (pas de pole) |

### t-3 (irt_gamma_phi.py)
- □_η²(ln s) = −6/s⁴ ≠ 0.
- φ_h = c₁s + c₂s² + c₃s³ + c₄(x² + s²) verifie □_η²φ_h = 0 et est lisse en s = 0. Le tenseur 8b ∂^c∂^d(φ_h C_acbd), avec T̂ = s² T, est sans trace et **ne donne aucun pole** dans R.

## 2. Lecture [derive]
1. **t-1** : la partie a ne depend de σ que par ses derivees, et sa forme integrable est fixee par la condition de Wess-Zumino. Elle se comporte a l'ordre ε comme une constante cosmologique effective (6a ĝ). Le resultat de S-b est **acte**, retrouve par une chaine independante.
2. **t-2** : la decomposition W_eff[ĝ] = Γ[g] + WZ[σ ; g] est exacte. Γ[g] est l'action effective sur la metrique de reference g = η + εh, dans l'etat transporte, qui est le vide conforme (Minkowski) du repere plat. Son tenseur a l'ordre ε est un noyau **retarde** invariant par translation, du type ∂∂ ln(−□/μ²) C[h], applique a une histoire lisse sur ]−∞, τ].
   - La singularite du noyau en coincidence est celle de [θ(T)/T]₊, qui envoie les fonctions lisses sur des fonctions lisses ; la partie dependant de k est lisse.
   - Le point τ = 0 (𝓘⁺) n'est pas distingue dans le repere plat. T_Γ y est donc lisse, et T̂_Γ = s² T_Γ ne peut pas produire de pole (t-2 calcule).
   - La dependance en μ est locale (∝ ∫C², donc ∝ Bach, nul sur couche).
   - **Hypotheses** : etat regulier du repere plat en τ = 0, et convergence du noyau retarde, qui exige une preparation adiabatique dans le passe lointain, ou les modes du repere plat croissent comme s.
3. **t-3** : φ = −ln s + φ_h. Le terme singulier est impose par la source F₄/4 ≠ 0 de l'equation auxiliaire sur de Sitter et ne peut etre annule par un mode homogene. Un mode homogene non lisse en τ = 0 supposerait un etat singulier sur 𝓘⁺ dans le repere plat, ce qui sort de l'hypothese d'etat de t-2.

```
   contributions a R de (2.17), ordre epsilon, onde w != 0 a scri+
   ───────────────────────────────────────────────────────────────
   WZ, partie c : b sigma C^2      ->  pole (8 b kappa / Omega) w   (NOTE-125 v2)
   WZ, partie a : Euler            ->  6a ghat : rien                (t-1)
   Gamma[g] non locale             ->  s^2 x lisse : rien            (t-2, etat regulier)
   phi_h homogene lisse            ->  rien                          (t-3)
   ───────────────────────────────────────────────────────────────
   total : pole non compense
```

## 3. Verdict
**T-V1 qualifie T-V3.**
- **T-V1** : aucune des trois contributions ne compense le pole. G-V3 est robuste dans la classe « WZ integrable + Γ[g] dans un etat conforme regulier + φ_h lisse ».
- **T-V3** : la regularite de Γ repose sur des hypotheses d'etat (regularite en τ = 0, passe adiabatique), qui ne sont pas des resultats. L'usage de l'action effective a une boucle comme source semi-classique dans (2.17) est une hypothese de tout le canal (M-V3 compris).

## 4. Confrontation a la prediction
Prediction (NOTE-130 §4) : « T-V1 qualifie T-V3 ; partie a = 6a ĝ ; T̂_Γ en s² × lisse, pas de pole ; log force par F₄, φ_h lisse sans pole ; qualifications : etat, adiabaticite, une boucle ». **Realisee** en tous points.

## 5. Consequences (rien n'est grave)
- **G-V3 consolide** : pole retrouve a l'aveugle (NOTE-128), robuste (polarisations, jauge, facteur conforme) et non compense par les autres parties de l'action anomale dans la classe consideree. Son libelle (NOTE-126) peut preciser : « dans la classe des actions effectives a une boucle des champs conformes, etat conforme regulier, convention lisse ».
- Les hypotheses restantes sont **communes a M-V3 et G-V3** : traitement semi-classique a une boucle, etat conforme, premier ordre. Elles ne distinguent pas les deux canaux.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 6. Pistes
- **IR-u** (NOTE-132/133) : transport de W avec la source polaire, et coefficient de la dimension anormale.
- Audit froid de NOTE-131 (propose, non engage).

## 7. Non-surclassement
[conv], non audite. Premier ordre en ε, fond de Sitter, mode tensoriel, etat conforme regulier suppose. G-V3 reste un candidat non grave.
