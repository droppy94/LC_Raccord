# RAPPORT XA-2 : audit de irx_cone.py et recherche de contre-exemples

Auditeur aveugle. Fichiers lus : /home/claude/irq/PROMPT-AVEUGLE-XA2-SCRIPT.md (consigne), /home/claude/audit_xa2/irx_cone.py, /home/claude/audit_xa2/irx_cone_sortie.txt. Rien d'autre. Calculs : sympy 1.14.0 (python3), dans /home/claude/audit_xa2/work/.
Etiquettes : [calcule] = sorti d'un script de ce dossier ; [derive] = raisonnement analytique de l'auditeur.

## 0. Empreintes

| Fichier | SHA-256 |
|---|---|
| irx_cone.py (attendu 827df834...0ec713) | 827df834e7ff941c8647edb7fa99e0b8d79fded2a790613739528e81b50ec713 : **CONFORME** |
| irx_cone_sortie.txt | eee35b275a10073ba5f92837a1315fb4757a1584c815642f6e279f1f5b814294 |
| work/rerun_irx_cone.txt (reexecution, 64 s) | eee35b275a10073ba5f92837a1315fb4757a1584c815642f6e279f1f5b814294 (identique octet pour octet a la sortie fournie) |
| work/xa2_A_x1_x3_x4.py | bd36000fa5ee41e2885e15a706401e51d5cef32ee4459bf81743be811dec554f |
| work/xa2_A_sortie.txt | 5b3d2fb387ddd3683ecec9990545fd5dff4d32c13c8d416be4fd3514f1b38d63 |
| work/xa2_B_x2.py | f1268ad54a115371a93abcde5d80de9f9240c9fe91b02a30d6f572105537ef90 |
| work/xa2_B_sortie.txt | a13e1079f1ef4eef3d36c8fb7bb03772de700754eecbfcfd1cefe11dfe1591e1 |
| work/xa2_C_weyl_scri.py | 14a0345843c25177ad301aa9d99d68c00ef3edcc760f8b60b9ea38afeb6fd192 |
| work/xa2_C_sortie.txt | 9ee25c4f3f24fc16e6d7592a7a513516baa5aa8ecfda37f87326bcf3bf8c01b3 |
| work/xa2_D_suite.py | ada4bfd8d0fc2390e5b1350e0d01aff42b6c9c394160bd7fa601c7993e302613 |
| work/xa2_D_sortie.txt | 5e94babc6f95acf2b6ae105989d5f4c2d11648b11cd956ca8e15dc6629c1f6d6 |
| work/xa2_E_superpositions.py | 4f5a6abac05c8bea23c4c6a89b7138e7cc856e527d9dbff70843ecab4deb2f03 |
| work/xa2_E_sortie.txt | e6f80803246fb3fb5b20bbea7638483cd05f73eba7cc21a0907edf117b9d26c3 |

Note : xa2_D et xa2_E reutilisent par `exec` l'en-tete de xa2_B_x2.py (Weyl, Christoffels, fonctions R_of_T, T_of_phi) ; les trois empreintes vont ensemble.

## 1. Audit du script, point par point

### x-1 (□² = 0 hors cone)
- Operateur `box = -∂_s² + Δ` : correct pour η = diag(-1,1,1,1). **OK**
- Resultats confirmes et expliques [calcule, xa2_A] : □σ^p = 4p(p+1) σ^(p-1) ; □ ln σ = 4/σ, □(1/σ) = 0, □(s/σ) = -4s/σ², puis □² = 0 pour les trois. Le controle □² ln s = -6/s⁴ est juste. **OK**

### x-2 (pas de 1/s hors sommet ; e⁻³ pres du cone)
- Formules [calcule, xa2_B, implementation differente : Riemann complet de η + εh puis d/dε, Christoffels de ĝ recalcules directement] : Riemann lineaire, Weyl (trace nulle verifiee), T_ab = -8b ∂^c∂^d(φ C_acbd), T̂ = s²T, trace (nulle car C sans trace), Γ̂ de ĝ = s⁻²η, ∇̂, R_ρνλ = s⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ). Tout concorde avec le script. **OK**
- Point (3/2, 1/2, 0) : σ = 5/2 − s² > 0 pour s < √(5/2) ≈ 1,58, donc hors cone pour tout s petit et ln σ bien defini. **OK**
- Detection du pole : `series(vp*s, s, 0, 2)` puis `subs(s, 0)`. Un pole d'ordre ≥ 2 ou un ln s donnerait zoo/oo, donc != 0 et serait signale. Detection fiable. **OK**
- **DEFAUT (portee, pas calcul)** : le test ne peut pas echouer. Lemme [calcule, xa2_B] : pour un T_ab lisse ARBITRAIRE (fonctions generiques de s,x,y,z), (s·R)|_{s=0} = 0 pour les 24 composantes. Raison [derive] : Γ̂ ~ 1/s agit sur L̂ ~ s²T, donc ∇̂L̂ = O(s) et Ω⁻¹∇̂L̂ = O(1). L'absence de 1/s en un point ou φ est lisse est donc structurelle, independante de ln σ et de la forme de h. Le test au point (3/2,1/2,0) ne dit rien de plus que "ln σ est lisse en ce point". Il ne sonde ni le sommet (r = 0, ou ln σ = ln(−s²)), ni l'endroit ou le cone touche le bord.
- Ordre de R hors cone [calcule, xa2_D] : au point (1, 1/2, 2/3), ordres dominants s⁰ ou s¹ selon les composantes : R est fini et generiquement non nul en s = 0.
- Pres du cone : la droite y = z = 0 est speciale (4 composantes non nulles seulement, par symetrie) et les parametres sont specialises (k = 1, A = 0, B = 1 : la branche A est eteinte). Le calcul d'ordre (`series(ve, e, 0, 0)` puis decalage e⁶) suppose un ordre ≥ −6 : satisfait. **OK avec reserve** (non generique).
- Libelle : "pole en un point de scri+ distinct du sommet : False" generalise a partir d'un seul point. **DEFAUT mineur de formulation**, rendu sans objet par le lemme (le resultat est vrai partout ou φ est lisse).

### x-3 (ansatz log, c_n forces a 0)
- Extraction : `eq = expand(□²φ · s⁴)` ; les puissances de □²φ vont de s⁻⁴ a s^(N+3), donc s⁴ suffit. `coeff(s, p)` puis `coeff(Ls, 1)` ou `subs(Ls, 0)`.
  - Point technique [calcule] : `(3 + 5 ln s + 7s).coeff(s, 0) = 3`, c'est-a-dire que coeff(s, 0) ELIMINE les termes en s⁰ ln s. Pour p = 0 (ordre s⁻⁴ de □²φ) cela serait un defaut s'il y avait un terme s⁻⁴ ln s ; il n'y en a pas (coefficient P(0)c₀ = 0, voir ci-dessous). **Inoffensif ici, fragile en general.**
  - Pour p ≥ 1 les termes s^p ln s sont bien captes (verifie par une extraction independante via Poly(s, L) apres remplacement ln s → L). **OK**
- Troncature n ≤ 7 [derive + calcule] : l'equation a l'ordre s^(m−4) ne fait intervenir que c_m, c_(m−2), c_(m−4) (et des a_n seulement pour m ≥ 4, sans ln s). Les ordres p = 0..7 sont donc complets ; les ordres p = 8..11 (qui feraient intervenir c₈..c₁₁ absents) ne sont pas testes, ce qui est correct. Pas d'ordre mal resolu. **OK**
- Ordre de resolution [derive + calcule] : recurrence exacte, valable pour tout n :
  - ordre s^(m−4) ln s : P(m)c_m − 2(m−2)(m−3)Δc_(m−2) + Δ²c_(m−4) = 0, avec P(m) = m(m−1)(m−2)(m−3) ;
  - ordre s^(m−4) (m ≤ 3) : P'(m)c_m + (termes en c_(m−2)) = 0, avec P'(0..3) = −6, 2, −2, 6 ≠ 0.
  Chaque equation est lineaire en c_m avec coefficient non nul, et les a_n ne produisent jamais de ln s. Aucune solution c_n ≠ 0 ne peut etre masquee. Reproduction jusqu'a N = 12 : c₀..c₁₁ = 0 (coefficients −6, 2, −2, 6, 24, 120, 360, 840, 1680, 3024, 5040, 7920) [calcule, xa2_A].
- **DEFAUT mineur** : la ligne de conclusion du script teste seulement c₀..c₄ (`range(5)`) alors que l'affirmation porte sur c₀..c₇ ; la sortie imprime bien les huit valeurs nulles, donc le resultat est juste mais la verification automatique est incomplete.

### x-4
- □f(s) = −f'', □²f = f'''' ; solution C₁ + C₂s + C₃s² + C₄s³. Trivial. **OK** [calcule]

## 2. Reproductions independantes

| Test | Resultat |
|---|---|
| x-2, point (1, 1/2, 2/3) (z ≠ 0), k, A, B, κ, b symboliques | aucune puissance negative ni ln s [calcule, xa2_B] |
| x-2, point du script (3/2, 1/2, 0) | idem [calcule, xa2_B] |
| x-2, cone, direction generique x = (s+e)(2,1,2)/3, s = 1/2, k = 1, A = 1/3, B = 1/2 | les 24 composantes non nulles, toutes en e⁻³ [calcule, xa2_B] |
| x-2, droite du script y = z = 0 | 4 composantes (ysy, yxy, zsz, zxz) en e⁻³, retrouve [calcule, xa2_B] |
| x-3, implementation par Poly(s, ln s) et recurrence symbolique en n | c₀..c₁₁ = 0 [calcule, xa2_A] |

La composante la plus singuliere pres du cone : aucune n'est plus singuliere que e⁻³ ; en direction generique toutes atteignent e⁻³. Comptage [derive] : ∂²ln σ ~ σ⁻², T ~ σ⁻², ∇̂L̂ ~ σ⁻³.

Fait annexe utile [calcule, xa2_C] : le Weyl lineaire du mode s'annule au bord, C = O(s) (par ex. C_sysy ≈ k³s(Aks − B)cos kx / 2). C'est l'annulation attendue du Weyl conforme a 𝓘⁺ ; elle gouverne les ordres trouves au paragraphe 3(a).

## 3. Contre-exemples

### (a) Sommet hors du bord : σ' = r² − (s + s₀)², s₀ = 1

```
 s (vers le passe)
 ^
 |   \          /         cone de sommet (s = -s0, r = 0)
 |    \        /
 |     \      /
 |------X----X---------  s = 0 (bord futur), coupe le cone sur la sphere r = s0
 |   r=s0    r=s0
```

| Zone | Comportement de R quand s → 0 |
|---|---|
| r < s₀ (dans le cone, ln(−σ')), r > s₀ (hors cone) | fini, aucun 1/s ni ln s [calcule, xa2_B, xa2_D] |
| Sur la sphere r = s₀ (σ' = −2s s₀ − s² < 0) | **s⁻¹ dans les 24 composantes** [calcule, xa2_B] |
| Chemins r = s₀ + λs, λ = 3, 1/2, 0 | s⁻¹ pour tout λ : singularite homogene de degre −1 en la distance au "coin" (s = 0, r = s₀) [calcule, xa2_D] |
| A s = 1/4 fixe, r = s₀ + s + e | e⁻³, comme x-2 [calcule, xa2_D] |

Interpretation [derive] : il y a bien un comportement en 1/s sur la sphere, mais ce n'est pas un pole propre du bord : c'est la trace de la singularite de cone σ'⁻³, attenuee au coin par deux gains d'un ordre chacun : C = O(s) (+1), et T̂ = s²T divise par Ω = s (+1 net). Degre total −3 + 1 + 1 = −1. Hors de la sphere, R est regulier (lemme du §1).

### (b) φ = α(x) ln s + correcteurs

- Analyse d'indice [derive + calcule, xa2_A] : ∂_s⁴(s^μ ln^j s) = s^(μ−4)[P(μ) ln^j s + jP'(μ) ln^(j−1) s + ...]. Les termes −2Δ∂_s² et Δ² decalent l'exposant de +2 et +4 et ne peuvent pas compenser l'ordre dominant. L'exposant minimal doit verifier P(μ) = 0, donc μ ∈ {0,1,2,3} (entiers : pas de s^μ non entier) ; les racines etant simples, jP'(μ) ≠ 0 impose j = 0. Par recurrence sur les reseaux μ₀ + 2ℕ, aucun ln s n'apparait jamais (pas de resonance : aux ordres μ = 2, 3 le terme induit par l'ordre μ − 2 a un coefficient (μ−2)(μ−3) = 0).
- Test explicite : α ln s + β ln² s + γ s² ln² s donne a l'ordre s⁻⁴ : ln s → −12β, ln⁰ → −2(3α − 11β), donc β = 0 puis α = 0 [calcule].
- Conclusion : **impossible avec α lisse** (developpement formel uniforme en x), y compris avec s^μ et ln² s. C'est l'expression du fait que s = 0 est non caracteristique pour l'operateur a coefficients constants □².

### (c) Superpositions de sommets dans s = 0

| Source | φ (poids constant) | Pres de s = 0 |
|---|---|---|
| Ligne de ln σ | 2π√(ρ⊥² − s²) + cste, □² = 0 [calcule] | analytique en s² pour ρ⊥ > 0 ; R fini (ordres s⁰, s¹) [calcule, xa2_E] |
| Ligne de 1/σ | π/√(ρ⊥² − s²), □ = 0 [calcule] | sur l'axe (ρ⊥ = 0) : partie Im = −π/s, partie Re (valeur principale) finie = −2√π pour le poids e^(−ξ²) [calcule] ; R de la partie 1/s : s⁻² [calcule, xa2_E] |
| Plan de 1/σ (valeur principale) | −π ln\|z² − s²\| + cste, □ = 0 [calcule] ; poids gaussien : πe^q E₁(q) ≈ −π ln q − πγ [calcule] | **sur le plan z = 0 : φ = −2π ln s exactement**, avec R ~ s⁻¹ [calcule, xa2_E] ; hors plan (z = 1/2) : regulier |

Point important [derive] : ln\|z² − s²\| = ln\|z − s\| + ln\|z + s\| est une solution distributionnelle authentique de □φ = 0 (donc □²φ = 0) sur s > 0, et elle vaut 2 ln s sur le plan z = 0. C'est un "α ln s" porte par un ensemble de mesure nulle (le support des sommets) : a z ≠ 0 fixe, φ est analytique en s², et le ln s n'apparait que sur le plan, donc aucun developpement a coefficients lisses en (x,y,z) ne le represente. Cela ne contredit pas x-3, dont l'ansatz suppose des c_n lisses, mais montre que la conclusion "pas de ln s au bord" ne vaut que hors du support des sommets et pour des poids/coefficients reguliers. Avec un poids lisse, les corrections sont analytiques en q = z² − s² (ou ρ⊥² − s²) et ne changent pas le terme dominant [derive, controle numerique a q = 7/10 : 1,78998129596744 dans les deux calculs].

## 4. Verdicts

| Affirmation | Verdict |
|---|---|
| **x-1** | **VALIDE** (hors cone, σ ≠ 0). |
| **x-2** | **VALIDE SOUS HYPOTHESES** : (H1) point du bord ou φ est lisse (hors sommet, hors intersection cone/bord) ; dans ce cas l'absence de 1/s est un fait structurel vrai pour tout T lisse (lemme), donc le test n'apporte pas d'information specifique sur ln σ. (H2) pour "e⁻³" : approche du cone a s > 0 fixe ; verifie en direction generique (24 composantes) et sur la droite du script. Au coin ou un cone rencontre s = 0 (cas (a)), l'ordre devient s⁻¹ (homogene de degre −1), pas e⁻³. |
| **x-3** | **VALIDE SOUS HYPOTHESES** : (H3) coefficients a_n, c_n lisses en (x,y,z), developpement formel uniforme ; resultat vrai pour tout n (recurrence), pas seulement n ≤ 7, et robuste a l'ajout de s^μ et ln^j s. (H4) hors du support des sommets : une superposition plane de cones donne une vraie solution egale a 2 ln s sur ce plan (§3c). Defaut mineur du script : la conclusion automatique ne teste que c₀..c₄. |
| **x-4** | **VALIDE** (trivial). |

Defauts du script recapitules : (i) test x-2 non discriminant (structurellement toujours negatif hors singularite de φ) ; (ii) test de cone sur une droite symetrique avec A = 0 ; (iii) conclusion x-3 limitee a c₀..c₄ ; (iv) `coeff(s, 0)` qui ignore s⁰ ln s (inoffensif ici). Aucun defaut ne change les resultats imprimes.
