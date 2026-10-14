---
id: NOTE-BORD-EON-90-Q-M3-EXECUTION
numero: 90
serie: I
branche: Q-M3 (chantier D / CCC + M)
reservation: 2026-10-09T16:27 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 90)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-89-ARMEMENT-Q-M3 (sha256 6b8cfacda331cb14a9735c8c4e9c794b1abbdd23c690fcc4148fe9cb2aab5516, 2026-10-09T16:28:34Z)
scripts:
  - qm3_poids.py (v1, sha256 e3ed37da7d7576d645979a39f0ab267d23803005e89ab16e3f17c9085aeff278, pris 16:31:51Z avant execution) : partie B NON INFORMATIVE, conservee
  - qm3_poids_v2.py (sha256 ca999653f3de9bf19f76295f9b8c16a11b02942e64517eaf00d7c781fcce4288, 16:33:12Z) : derniere ligne de E FAUSSE, conservee
  - qm3_poids_v3.py (sha256 8edc1947c9d68702fc3c6565e864c16a849c156e1f69a80e2ecd72e79b9b3db4, 16:33:27Z) : version de reference, EXIT 0
depend: [NOTE-BORD-EON-89-ARMEMENT-Q-M3, S26-02-VERDICT-CHANTIER-D, S27-02-VERDICTS-M-ET-REPLI, REPRISE-AUTOPORTANTE-ROUTE-KAPPA-2026-08-24]
rouvre_si:
  - "modele de champs (inconnues rescalees + equations) pour la source anomale au voisinage de I+"
  - "calcul inhomogene du coefficient du terme en ln Omega dans (2.17)"
  - "objection exterieure sur la lecture de 1311.0700 §2-§3 ci-dessous"
---

# NOTE-90 : execution de Q-M3. Verdict **B-V0 ⊕ A-V3**

## 0. Resume
- **(b), le critere : B-V0.** Les deux « criteres » ne sont pas deux seuils sur un meme axe. Le corpus teste l'ordre d'un scalaire evalue sur une solution (trace rescalee Ω⁻⁴T̂ bornee). Friedrich enonce une propriete **structurelle** du systeme conforme ecrit en inconnues rescalees : aucun coefficient Ω⁻ᵏ explicite, seconds membres fonctions lisses des inconnues. Le critere du corpus **n'est pas une condition necessaire** de la regularite de Friedrich : le scalaire regulier de Friedrich a une trace rescalee du corpus en Ω⁻².
- **(a), le canal de jauge sous C-M1 : A-V3, deplace et precise.** Par les canaux ou la trace entre dans le systeme, le canal de jauge a l'ordre Ω⁰ du corpus est regulier. Mais la source anomale n'a pas de description en inconnues rescalees, et la conservation lui impose une partie sans trace en Ω² ln Ω (modele homogene). La question devient une question de **polyhomogeneite de la partie sans trace**, non tranchee.
- Prediction du gel : B-V1 ⊕ A-V3. **B-V1 non realise** (mon constat prealable du §1 de NOTE-89 visait le mauvais objet), **A-V3 realise**. Inclinaison secondaire (« une trace d'ordre Ω⁰ produit des Ω⁻¹ ») **non realisee**.

## 1. Source lue (EX-7)
H. Friedrich, « Smooth non-zero rest-mass evolution across time-like infinity », arXiv:1311.0700v2 [gr-qc], 19 fevrier 2014, article original de recherche, Max-Planck-Institut fur Gravitationsphysik. Texte complet via alphaXiv. Lu au texte : §1 (passage sur les champs a trace nulle), **§2 en entier, §3 en entier (theoreme 3.1 et preuve), §4 en entier** (EX-9 : la section suivant la section citee est lue jusqu'a sa fin), debut du §5.
Convention : chez Friedrich, g = Ω² ĝ avec ĝ physique (§2, l. 1). Le corpus (reprise route κ §2) ecrit g = Ω² g̃ avec g̃ physique : meme structure, chapeau et tilde echanges.

## 2. Ce que dit la source [extrait]
1. **Deux objets notes T\*.** Sous (2.17) : `T*_ρμ = T̂_ρμ − ¼ T̂ ĝ_ρμ`, la partie **sans trace** du tenseur physique. En (3.7) : le scalaire `T* ≡ Ω⁻² T̂`. Homonymie interne a la source, a inscrire au registre d'homonymie (proposition Q-M3-d).
2. La trace physique T̂ entre dans le systeme par (2.13) (`κ/4 T̂`), (2.15) (`κ/(24Ω) ∇̂_μ T̂`) et, via `L̂_μν = κ/2 T*_μν − κ/24 T̂ ĝ_μν + λ/6 ĝ_μν`, par (2.16)-(2.17).
3. (3.15), valable pour toute source (il ne mobilise que les definitions et la transformation conforme) : `∇̂_[ρ L̂_μ]ν = κ/2 { ∇_[ρ T*_μ]ν − 1/12 ∇_[ρ T* g_μ]ν + Ω⁻¹ ( ∇_[ρΩ T*_μ]ν + ∇^πΩ T*_π[ρ g_μ]ν − ⅙ T* ∇_[ρΩ g_μ]ν ) }`, et (2.17) multiplie ce membre par `2Ω⁻¹`. **La trace et la partie sans trace se combinent** dans les termes en Ω⁻¹.
4. Le sens de « regulier » (theoreme 3.1) : « on the right hand sides of the equations no terms of the form Ω⁻ᵏ, k > 0, occur and the right hand sides are in fact smooth function of the unknowns ». C'est une propriete du **systeme d'equations** pour un modele de matiere donne, pas d'une solution.
5. Pour le scalaire : `T̂ = Ω² T*` (3.7), `T* = (λ/3 − 2m²)ψ² + O(Ω)` (3.9), donnee ψ₀ libre sur J (proposition 4.1). Le terme singulier de (3.16) est `(m² − 2λ/3)`, issu de la combinaison du point 3.
6. §4 : « Regularity of T* and the relation T̂ = Ω² T* imply that T̂ = 0, ∇̂_μ T̂ = 0 on J » : c'est le scalaire T* (point 1, second sens) qui doit etre regulier, pas la trace rescalee du corpus.

## 3. Resultats

### 3.1 Les poids [calcule, v3 §A]
Trace rescalee du corpus `Ω⁻⁴ T̂` (reprise route κ §2, indices mixtes) contre scalaire de Friedrich `T* = Ω⁻² T̂` : facteur Ω⁻², **objets differents**. Mon constat prealable (NOTE-89 §1 : homonymie de position d'indice) est **faux sur la cible** : il est exact que le tenseur rescale du corpus, abaisse avec g, porte Ω⁻² (v1 §A), mais S27-02 §A.4(b) visait le **scalaire** T* de (3.7), pas le tenseur `T*_μν`.

### 3.2 Le critere du corpus n'est pas necessaire [calcule, v3 §C ; entrees extraites §2.5]
Scalaire regulier de Friedrich (m² = 2λ/3) : `T*|_J = −λψ₀²`, donc trace rescalee du corpus `Ω⁻⁴T̂ = −λψ₀² Ω⁻²`, **divergente** pour toute donnee ψ₀ ≠ 0, alors que le theoreme 3.1 declare le systeme regulier. Le comptage d'ordres de la trace declarerait obstrue un cas que la source declare regulier.
Suffisance du critere du corpus : **non examinee**.

### 3.3 Canal de jauge sous C-M1, partie trace [derive, ordres verifies v3 §D]
Avec `F̃² = Ω⁴ F²_[g]` ([calcule], verif_S21/S23), la trace anomale donne `T* = Ω⁻² (β/2e) F̂² = Ω² (β/2e) F²_[g]`, fonction lisse des inconnues (Ω, F_[g]) sous H-1. Dans les canaux ou T* entre ((2.13), (2.15), terme `−⅙ Ω⁻¹ T* ∇Ω g` et `∇T* g` de (3.15)), tous les termes tendent vers 0. **Par la trace, le canal de jauge a l'ordre Ω⁰ est regulier.** C'est la moitie juste de la phrase de S27-02 §A.4(b).

### 3.4 Partie sans trace imposee par la conservation [calcule en modele homogene, v3 §E ; portee derive]
Une trace imposee `T̂ = A Ω⁴` et la conservation donnent, en fluide homogene, `ρ = (B − A ln a) a⁻⁴`. La partie sans trace, en composantes g-orthonormees, vaut `Ω²(B + A/4 + A ln Ω)` : continue, **non lisse** des que A ≠ 0 (polyhomogene). Dans (3.15), `Ω⁻¹ ∂(Ω T*_μν) ~ 3Ω ln Ω + Ω`, borne mais non C¹. Avec le Ω⁻¹ supplementaire de (2.17), on obtient `3 ln Ω + 1`, **non borne**, si le coefficient structurel ne s'annule pas. En homogene il s'annule par symetrie (v1, partie B : (2.17) identiquement nul, FLRW conformement plat). **Le cas inhomogene n'est pas evalue.**
Lien possible, non lu dans cette seance (EX-8, ecrit en taux) : la « branche logarithmique » de la reprise route κ §5.2 et le critere de polyhomogeneite ν ∈ ℤ du chantier RG (22 septembre).

## 4. Verdicts
- **(b) : B-V0.** Raison nommee : le corpus et Friedrich ne parlent pas du meme type de critere (ordre d'un scalaire sur une solution contre absence structurelle de coefficients Ω⁻ᵏ pour un modele de champs), et le premier n'est pas une condition necessaire du second (§3.2). Ni B-V2 ni B-V3 : « plus faible / plus fort » suppose un axe commun qui n'existe pas. Restreint au seul canal de trace et a l'ordre Ω⁰, le resultat ressemble a B-V2 (§3.3) ; il ne vaut pas en general.
- **(a) : A-V3.** La source ne fournit pas le critere pour une source anomale sans description de champs. Q-M3(a) est deplacee de la trace (reguliere) vers la partie sans trace imposee par la conservation (polyhomogene en Ω² ln Ω dans le modele homogene, effet sur (2.17) non evalue en inhomogene).
- **Q-M3 reste ouverte.** Aucune incompatibilite de C-M1 n'est etablie (pas de M-V3), aucune compatibilite non plus.

## 5. Portee sur RG-4 (signalement, rien n'est tranche)
Le texte adopte de RG-4 est ecrit dans le critere du corpus : « la contribution de l'electron a la trace rescalee diverge a I+ (ordre Ω⁻¹ non reabsorbable) ». §3.2 montre que ce critere n'est pas le critere de regularite de Friedrich. Le declenchement effectif de RG-4 repose sur S26-02 §2.3, qui n'utilise pas ce comptage : theoreme 3.1 pour le scalaire ([extrait]), phase non convergente `exp(i (m/H) ln Ω)` pour le spineur ([conv]). S26-02 §3 notait deja ne pas avoir etabli la forme « trace rescalee en Ω⁻¹ ».
**Consequence** : le libelle de RG-4 et son fondement effectif ne coincident pas. Le statut de RG-4 (refutation provisoire de la CCC dans sa forme actuelle) n'est **pas** modifie par cette note. Le point doit etre joint au dossier de la lecture exterieure de S26-02 §2.3, et l'operateur peut amender le libelle (Q-M3-c).

## 6. Greffes proposees (non entees)
- **Q-M3-a** : table des ordres (reprise route κ §2 et pieces derivees) : en-tete « comptage d'ordres de la trace rescalee ; ce n'est pas un critere de regularite au sens de Friedrich 1311.0700 ».
- **Q-M3-b** : S27-02 §A.4(b) : remplacer « si le critere de Friedrich est le bon, une trace physique en Ω⁴ est inoffensive et (a) tombe » par « par la trace, oui ; (a) est deplacee vers la partie sans trace imposee par la conservation (NOTE-90 §3.4) ».
- **Q-M3-c** : RG-4 : reecrire le declencheur en termes de regularite du champ rescale (S26-02 §2.3), sans le comptage de trace. Decision operateur.
- **Q-M3-d** : registre d'homonymie : T\* (Friedrich) = `T*_μν` partie sans trace physique (sous 2.17) **et** scalaire `Ω⁻² T̂` (3.7).

## 7. Passe adverse interne (ne vaut pas audit froid)
1. « §3.2 compare des choses heterogenes : le corpus applique son comptage a la trace anomale, pas a la matiere classique. » La table du corpus range aussi la matiere massive (« terme croise, Ω⁻¹, l'electron ») et le scalaire de Friedrich est de la matiere massive ; le comptage s'applique a la trace totale. Tenu.
2. « Le modele homogene de §3.4 est trop particulier. » Exact : il exhibe le Ω² ln Ω impose par la conservation, il ne montre pas qu'il survit en inhomogene ni qu'il rend (2.17) singulier. C'est pourquoi le verdict est A-V3 et non A-V2.
3. « La v1 a ete ecrite pour tester (2.17) et ne teste rien. » Exact ; conservee avec sa sortie, declaree non informative (R-55, pas d'actif fantome).
4. « La v2 imprimait une affirmation fausse. » Exact (ln Ω non borne attribue a (3.15) au lieu de (2.17)) ; corrigee en v3 par calcul de limite, v2 conservee.
5. Non couvert : la suffisance du critere du corpus ; les fermions sans masse comme champs conformes (Friedrich §1 : les champs a trace nulle obeissant a des equations conformement covariantes traversent ; la reference [8] de Friedrich n'est pas lue) ; la partie sans trace non locale de l'anomalie dans un etat realiste.

## 8. Non-surclassement
Ce verdict est [conv], non audite a froid, non scelle. CCC (forme actuelle) : refutee a titre provisoire (RG-4), statut inchange. CCC + M : hypothese ouverte, Q-M3 ouverte et deplacee. Noyau {A4 ; A2★ ; N} inchange, p_Q non fixe, N non chiffre, P2 et P3 non tranchees.
