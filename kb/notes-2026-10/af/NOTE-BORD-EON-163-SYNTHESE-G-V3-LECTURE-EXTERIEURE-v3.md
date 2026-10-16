---
id: NOTE-BORD-EON-163-SYNTHESE-G-V3-LECTURE-EXTERIEURE
version: v3 (greffe G-AF, acte NOTE-200, 2026-10-16 : pas 2 bis au §3, point de lecture final remplace ; v2 sha256 3755f1a8f864c683 et v1 sha256 8cac0b83311f2369 conservees)
numero: 163
serie: I
branche: Q-M3 suite (synthese G-V3 pour lecture exterieure)
reservation: 2026-10-13T13:20 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 163)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
nature: "PIECE D'APPAREIL : synthese autoportante de la chaine G-V3 (NOTE-124 a 162) destinee a un relecteur humain exterieur. Aucun calcul, aucune lecture nouvelle, aucune gravure. Tout ce qui est affirme ici renvoie a une note numerotee, deposee avec son empreinte."
decision: operateur (Thierry), 2026-10-13 15:16 heure de Paris (« je valide » la suite proposee : synthese lisible, depot, relecteur humain)
depend: [NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION (v4), NOTE-BORD-EON-162-ACTE-GREFFES-ET-REVISION-G-V3-v4, NOTE-BORD-EON-161-AUDIT-IR-ab-ac-aa-ad-CONCORDANCE, NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-128-AUDIT-IR-s-CONCORDANCE]
destinataire: "relecteur humain exterieur (profil : corrections quantiques en de Sitter, ou cosmologie conforme cyclique) ; aucune connaissance prealable du programme supposee"
---

# Synthese de la chaine G-V3 : une obstruction de principe au raccord conforme lisse de la CCC en presence de champs conformes et d'ondes gravitationnelles

## 0. Ce que cette piece est, et ce qu'elle n'est pas

Cette piece resume, pour un lecteur exterieur, un resultat obtenu entre le 11 et le 13 octobre 2026 dans le cadre d'un programme independant de physique theorique (LC-RACCORD) qui teste la cosmologie conforme cyclique (CCC) de Penrose en isolant une a une les hypotheses dont depend le raccord entre deux eons. Le resultat est note **G-V3**. Il est au grade « [conv] » du programme : calcule, audite a l'aveugle en interne, mais **non relu par un tiers humain**. C'est precisement cette relecture que la presente piece sollicite.

Elle ne contient aucun calcul nouveau. Chaque enonce renvoie a une note numerotee (NOTE-BORD-EON-nnn), deposee avec son empreinte sha256, ses scripts et les extraits des sources lues. Les notes d'execution ont chacune un **gel** prealable (cadre, questions, espace des verdicts et prediction, scelles avant tout calcul ou lecture), et un **audit froid aveugle** (re-derivation par des agents isoles qui n'avaient pas acces aux notes). Le §9 dit comment relire.

**Ce que nous demandons au relecteur** : dire si la chaine du §3 tient, et sinon ou elle casse ; dire si les hypotheses du §4 sont celles qu'il aurait posees ; et repondre, s'il le peut, aux objections anticipees du §8, en particulier a la premiere.

---

## 1. L'enonce

### 1.1 Libelle en vigueur (NOTE-138 v4 §1.3, reproduit sans modification)

> **G-V3, obstruction de principe** : en presence, a 𝓘⁺, de champs quantiques conformes (b > 0) et d'ondes gravitationnelles a donnee electrique non nulle, le Weyl rescale n'a pas de limite finie en 𝓘⁺ : W ≈ W₀ (1 + 8bκ ln a) au premier ordre (γ = 8, calcule et retrouve a l'aveugle ; coefficient identique a Foraci-Litos-Woodard 2026 pour trois especes) ; sous la prescription de resommation de Woodard 2025 (logarithmes dominants), W ∝ Ω^(−ε), ε = 8bκH² > 0, de signe universel. Incompatible avec un raccord lisse au sens de la limite, et plus generalement avec tout raccord exigeant W fini en 𝓘⁺. **Portee physique** : ε ~ 10⁻¹²² × N_eff pour H actuel ; l'effet ne devient d'ordre un qu'apres ~1/ε e-folds, echelle de meme dependance parametrique que le temps de rupture quantique de de Sitter (Dvali-Gomez-Zell), ou la description semi-classique dont G-V3 est issu cesse d'etre fiable. Candidat, non grave ; classe « WZ integrable + Γ[g] dans un etat Hadamard » : sans condition sur φ_h et sans hypothese d'etat au-dela de Hadamard (pour un champ conforme, tout etat Hadamard sur l'eon se prolonge avec w C^∞ jointe a travers 𝓘⁺, par la propagation de la forme microlocale de Hadamard et l'equivalence local/global ; le seul comportement compensateur, en 1/η, est non Hadamard, singulier sur le cone reflechi, y compris pour les etats homogenes anisotropes) ; fond de Sitter exact, premier ordre en ε et en bκ, mode tensoriel, action effective a une boucle, forme ln(−□/μ²) du facteur de forme sur le Weyl, onde solution de l'equation de de Sitter linearisee au voisinage de 𝓘⁺ a source B[h] integrable dans le passe, reduction d'ordre. **Clause resommee** : la puissance Ω^(−ε) est obtenue par un procede de groupe de renormalisation (Callan-Symanzik, γ issu de la renormalisation de champ du graviton par le seul contre-terme de Weyl, β_G = 0 a l'ordre calcule, substitution ln μ → ln a ; Foraci-Woodard 2501.01972 ; Woodard 2501.05077 ; origine Miao-Tsamis-Woodard 2110.08715), fonde sur l'appariement ln μ / ln a de la regularisation dimensionnelle et sur l'absence de queue des champs conformes, que la source introduit par « suggests », sans verification a l'ordre superieur, sous deux hypotheses declarees par ses auteurs (absence de course de G ; attribution du contre-terme a la renormalisation de champ) et sans discussion de l'independance de jauge gravitationnelle, et declare valable « tant que la phase de Sitter persiste » ; son usage dans la limite Ω → 0 est une extrapolation du programme, non un enonce de la source.

### 1.2 En une page

La CCC identifie l'infini futur 𝓘⁺ d'un eon (de genre espace, Λ > 0) au Big Bang de l'eon suivant par un rescaling conforme ĝ = Ω⁻²g, Ω → 0 sur 𝓘⁺, et **suppose** ce raccord lisse (Tod 1309.7248 : « assumed to be smooth » ; Meissner-Penrose 2503.24263 : « an assumption of CCC »). L'objet transmis d'un eon au suivant est le tenseur de Weyl rescale W = C/Ω, qui doit avoir une limite finie en 𝓘⁺.

Le programme pose la question : que fait, a ce raccord, l'**anomalie de trace** des champs quantiques conformes (photon, fermions sans masse, scalaires conformes), c'est-a-dire les champs memes dont la CCC a besoin au bord ? L'action effective a une boucle de ces champs se decompose exactement en W_eff[ĝ] = Γ[g] + WZ[σ ; g], ou g = η + εh est la metrique conforme de reference (Minkowski portant une onde gravitationnelle h, repere « plat »), σ = −ln Ω, et WZ l'action de Wess-Zumino locale de l'anomalie. Le terme local **b σ C²** de WZ produit, dans l'equation (2.17) de Friedrich (celle qui gouverne la regularite du systeme conforme a 𝓘⁺), un **pole** (8bκ/Ω) W_E, ou W_E est la partie electrique du Weyl rescale. Ce pole est retrouve a l'aveugle, robuste (polarisations, incidence, jauge, facteur conforme), et n'est compense par aucune autre contribution : ni la partie d'Euler de WZ, ni la partie non locale Γ[g] (pour tout etat Hadamard, et quelle que soit l'histoire de l'onde), ni les modes homogenes du champ auxiliaire σ.

Transporte dans l'equation du Weyl rescale, le pole donne une **dimension anormale** : W_E ≈ W₀(1 + 8bκ ln a). Le coefficient 8bκ est identique, pour trois especes (scalaire conforme, Dirac, photon), a celui que Foraci, Litos et Woodard (2026) et Foraci et Woodard (2024-2025) obtiennent par un calcul direct en de Sitter pour le Weyl electrique des ondes gravitationnelles. Ces auteurs resomment le logarithme par une variante du groupe de renormalisation : W ∝ a^(8bκH²). Lu a 𝓘⁺ (a → ∞, Ω → 0) : W ∝ Ω^(−ε), ε = 8bκH² > 0 : **le Weyl rescale n'a pas de limite finie**.

L'exposant est minuscule (ε ~ 10⁻¹²² pour H actuel) ; l'effet ne devient d'ordre un qu'apres ~1/ε e-folds, soit l'echelle du temps de rupture quantique de de Sitter. C'est pourquoi le programme parle d'**obstruction de principe** : elle atteint la CCC telle qu'elle est formulee (un enonce de limite), elle ne peut etre ni levee ni confirmee physiquement dans le cadre semi-classique qui la produit.

```
   scri+ (Omega -> 0)
   -----------------------------------------------------------------------------------
   champs conformes (b > 0)  +  onde gravitationnelle (W_E != 0)
         |
         v   action anomale locale  b sigma C^2,  sigma = -ln Omega
   T-hat ~ s^1  ==>  (2.17) de Friedrich : R ~ (8 b kappa / Omega) W_E      [pole]
         |
         v   transport du Weyl rescale (equation d'Einstein linearisee + T^(C), reduction d'ordre)
   W_E ~ W_0 (1 + 8 b kappa ln a)                                         [gamma = 8]
         |
         v   resommation (Callan-Symanzik, ln mu -> ln a ; procede, non theoreme)
   W_E ~ Omega^(-8 b kappa H^2)                                           [pas de limite finie]
```

---

## 2. Cadre et conventions

| Objet | Choix du programme | Note |
|---|---|---|
| Critere de regularite | Equation (2.17) de Friedrich : R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), L̂ = (κ/2)(T̂ − ⅓ĝ tr T̂), T̂ = Ω² T ; regularite = absence de termes en Ω^(−k) et de logarithmes dans le systeme conforme en inconnues rescalees | NOTE-90, 123 v2 |
| Convention de regularite | Lisse (C^∞) **au sens de la limite** Ω → 0, qui est le sens de Tod et de Meissner-Penrose ; decision de l'operateur, apres examen des options C³ et C² (qui ne changeraient rien a G-V3 : W n'est pas borne) | NOTE-126, 138 |
| Fond | de Sitter exact, H = 1 sauf mention ; coordonnees conformes, s = Ω = −η > 0 sur l'eon, 𝓘⁺ = {s = 0} ; ĝ = s⁻²(η + εh) | NOTE-124, 125 v2 |
| Onde | mode tensoriel h_yy = −h_zz = u(s) cos kx, u₀ = A(cos ks + ks sin ks) + B(sin ks − ks cos ks) ; W_E,yy|𝓘⁺ = −Bk³ cos kx / 2 (B = donnee electrique, A = magnetique) | NOTE-125 v2 |
| Action anomale locale | W ⊃ ∫√g { b σC² + a[σ(E − ⅔□R) + 2σΔ₄σ] }, forme de Wess-Zumino integrable ; ⟨T^a_a⟩ = bC² + … | NOTE-131, 137 |
| Signe physique | Carroll-Wald : ⟨T_ab⟩ = −(2/√−g) δW/δg^{ab}, signature (−,+,+,+), W ⊃ +b∫σC², T_ab = −8b ∂^c∂^d(σC_acbd) ; b > 0 ⟹ Weyl rescale **croissant** (le c₀ = +8 du gel initial est garde pour la tracabilite, passage b → −b) | NOTE-138 |
| Normalisations | κ = 8πG ; b = (N_S + 6N_F + 12N_V)/(120(4π)²) ; 8bκ = G/(30π) par scalaire conforme, G/(5π) par Dirac, 2G/(5π) par photon ; chez Woodard κ_W² = 16πG | NOTE-133, 137, 148 v2, 153 |
| Etat quantique | quasi-libre (gaussien), Hadamard sur l'eon ; fonction a deux points ω₂ = H + w, w bisolution lisse | NOTE-145, 146 v3 |
| Comptage | T̂ ~ s^p Y, Y lisse ⟹ R = s^(p−2) A_p[Y(0)] + O(s^(p−1)) en composantes de coordonnees : **borne superieure seulement** ; le coefficient A_p peut s'annuler (sources homogenes isotropes conservees : contribution nulle) et des poles apparaissent hors de p = 1 (scalaire inhomogene). **Le pole de G-V3 n'est pas tire de cette regle** : il est calcule par derivee covariante explicite (irr_c.py) et re-derive a l'aveugle (NOTE-128) | NOTE-131 ; greffe G-CAL-a (NOTE-179) |

---

## 3. La chaine en dix pas

Chaque pas : ce qui est etabli, par quelle note, avec quel verdict, et par quel audit. Les verdicts sont ceux de l'espace fige au gel de chaque chantier ; « qualifie » signifie que le verdict principal est assorti d'une reserve nommee.

| Pas | Enonce | Note (verdict) | Audit | Etiquette |
|---|---|---|---|---|
| **1** | La CCC suppose un raccord lisse ; (2.17) est le bon critere ; un ln Ω dans (2.17) rend la metrique-pont C³ non C⁴ et W continue non C¹ | 123 v2 (Q-V3 qualifie Q-V1), lecture de Tod, Friedrich, Meissner-Penrose | 128 (AU-V2) | [extrait], [calcule] |
| **2** | Sur de Sitter portant une onde, le terme bσC² donne un T̂ sans trace, conserve, sans log (Bach nul sur couche) et un **pole** R_isj = (8bκ/Ω) W_E,ij dans (2.17) ; independant du mecanisme M, present pour tout champ conforme | 125 v2 (R-V1 qualifie R-V3) | 128 : pole retrouve en cecite stricte, robuste (polarisations, k oblique, superposition, jauge, facteur conforme) | [calcule] |
| **2 bis** | **Forme formelle du pole** : au premier ordre autour de la metrique conforme plate, avec C = ΩW et les inconnues de Friedrich en jets, le second membre de (2.17) contient −κc₀b(n_ν Eⁿ_λρ − n_λ Eⁿ_νρ)/Ω, Eⁿ_ab = n^c n^d W_acbd, sans aucune derivee de W ; regulier ssi b = 0 ; logs nuls a l'ordre b sur div W = 0 ; integre sur un mode homogene : E ∝ Ω^{−8bκ}, l'exposant de la clause resommee | 197 v2 (AF-V1) | 199 (AA-1 cecite stricte, AA-2 adverse avec verification independante de la chaine : AU-V2) | [calcule] |
| **3** | La partie a (Euler, WZ integrable) vaut exactement 6aĝ a l'ordre ε : aucun effet sur R | 131 (T-V1 qualifie T-V3) | 137 (W-c) ; 128 (S-b, independant) | [calcule] |
| **4** | Le log de σ est force (□²(ln s) = −6/s⁴) ; aucun mode homogene lisse de σ ne produit de pole ; les solutions de cone (ln σ, 1/σ, s/σ) ne compensent rien hors d'un ensemble de mesure nulle, vide au sens des distributions ; argument general : Cauchy hyperbolique (Garding) + unicite de Holmgren, sans hypothese de croissance | 131 ; 140 v2 (X-V1) | 137 (W-c) ; 142 (XA-V2) : c_n = 0 pour tout n, argument reformule | [calcule], [derive] |
| **5** | Pour un champ conforme, **tout etat Hadamard** sur l'eon se prolonge avec w C^∞ jointe a travers 𝓘⁺ (probleme de Cauchy des bisolutions ; propagation de la forme microlocale de Hadamard, Prop. 16 (b) de Khavkine-Moretti, sans positivite ; equivalence local/global, Th. 9, pour des etats) ; T̂_Γ ~ s² × lisse : rien. Le seul comportement compensateur (T_plat ~ 1/η) est non Hadamard, singulier sur le **cone reflechi** (η + η′)² = |x − x′|² ; dans la classe homogene de Bogoliubov, Hadamard ⟺ αβ* a decroissance rapide ; pour un etat homogene **anisotrope**, le terme αβ* du tenseur conforme est purement sans trace, entier en η si Hadamard | 146 v3 (Y-V1) ; 155 v2 (AC-V2 ⊕ AC-V4) ; 157 v2 (AA-V1 ⊕ AA-V2) | 150 (YA-1 cecite stricte : prolongement joint retrouve et renforce, positivite necessaire ; YA-2 : correction d'objet) ; 161 (ACA-1, AAA-1, AAA-2) | [calcule] (classe homogene), [extrait, secondaire] (theoremes), [derive] |
| **6** | Le noyau retarde de Γ[g] (ln(−□/μ²) sur le Weyl) agit sur le **Bach linearise** B = −¼□²h, qui est **identiquement nul** sur l'onde de de Sitter exacte ; en limite adiabatique la reponse non locale est nulle (R_ε(0) = −4πk³ε + O(ε² ln ε) → 0) ; pour une emission a temps fini elle est lisse en 𝓘⁺ ; T̂_Γ ~ s² : jamais de s¹. L'hypothese « passe adiabatique » devient une condition explicite sur l'onde | 159 v2 (AD-V1 qualifie AD-V2) ; appui exterieur : Foraci-Woodard 2412.11022 eq. 49-50 (« the nonlocal contribution vanishes ») | 161 (ADA-1 cecite stricte : forme fermee ; ADA-2 : robustesse de la regularisation) | [calcule] |
| **7** | **Transport** : equation d'Einstein linearisee completee par T^(C), reduction d'ordre : u₁ ⊃ (8/3)Bk³s³ ln s ; **W_E ≈ W₀(1 + 8bκ ln s)**, γ = 8, independant de k ; la donnee magnetique A ne produit pas de log ; module egal au residu du pole | 133 (U-V1) | 137 (W-a : recalcul de bout en bout depuis la seule trace anomale, Γ = 64πGb = 8bκ, Weyl rescale croissant ; log par resonance) | [calcule] |
| **8** | **Litterature** : Foraci-Litos-Woodard 2606.17963 (Weyl electrique des ondes gravitationnelles, trois especes), Foraci-Woodard 2501.01972 (Dirac, eq. 35, 42, 46), Foraci-Woodard 2412.11022 (photon, eq. 53, 60), Miao-Tsamis-Woodard 2405.01024 (δZ, eq. 91) : coefficient du logarithme **egal a 8bκ** pour scalaire conforme, Dirac, photon (table §6) ; raison structurelle : pour un champ conforme c₁ = 0 et l'exposant est fixe par le seul contre-terme de Weyl, dont ∂c₂/∂ln μ = b | 133, 148 v2, 153 (AB-V1 qualifie AB-V4) | 137 (W-b lecture aveugle : n = 8) ; 150 (ZA-1) ; 161 (ABA-1) | [extrait], [calcule] (conversions) |
| **9** | **Resommation** : Callan-Symanzik avec γ de la renormalisation de champ du graviton, β_G = 0 a l'ordre calcule, ln μ → ln a (appariement de la regularisation dimensionnelle, [8] eq. 5 ; champs conformes sans queue) : C₀ᵢ₀ⱼ → C^tree a^(8bκH²) ; d'ou W_E ∝ Ω^(−8bκH²). Statut selon les sources : « suggests », « can be resummed », « if we ignore possible running of Newton's constant » ; aucune verification a deux boucles | 135 (V-V1), 148 v2 (Z-V1 qualifie Z-V2), 153 | 137, 150, 161 | [extrait] ; **procede, non theoreme** |
| **10** | **Lecture a 𝓘⁺** : W ∝ Ω^(−ε) n'est pas borne ; aucune convention exigeant W fini ne survit ; l'exposant ne se deplace pas dans le facteur conforme (Ω′ = Ω^(1−ε) degenererait la metrique compactifiee) ; ε·S_dS = 1/30 par scalaire ; 1/ε e-folds ~ temps de rupture quantique de de Sitter (Dvali-Gomez-Zell, meme dependance M_P²/(N H²)) | 138 (acte, option A) | reexamen argumente, non audite | [derive], [calcule] (ordre de grandeur) |

---

## 4. Les hypotheses, et leur statut

Toutes les hypotheses restantes sont **de cadre** : elles delimitent le calcul, aucune ne porte sur l'etat quantique au-dela de la condition de Hadamard.

| Hypothese | Statut | Ou elle est instruite |
|---|---|---|
| Fond exactement de Sitter | cadre ; la CCC suppose Λ > 0 et 𝓘⁺ de genre espace (branche PREMISSE du programme, P1/P2, hors de cette chaine) | 124 |
| Premier ordre en ε (onde) et en bκ | cadre ; retroaction d'ordre κ²b negligeable | 125 v2 |
| Mode tensoriel, onde plane | cadre ; robustesse aux polarisations, a l'incidence oblique, a la superposition verifiee a l'audit | 128 |
| Action effective a une boucle comme source semi-classique | cadre, commune a tout le canal | 131 |
| Forme ln(−□/μ²) du facteur de forme sur le Weyl (Barvinsky-Vilkovisky) ; termes d'Euler non locaux et ordre superieur en courbure hors cadre | cadre ; **point ouvert** | 158, 159 v2 |
| Onde solution de l'equation de de Sitter linearisee pres de 𝓘⁺, source B[h] integrable dans le passe | **instruite** (remplace « passe adiabatique ») | 159 v2 |
| Etat Hadamard (quasi-libre) | **instruite** : aucune hypothese au-dela ; anisotropie comprise ; theoremes confirmes sur source secondaire de revue (primaires de 1996 non lues, acces refuse) | 146 v3, 155 v2, 157 v2 |
| Modes homogenes de σ | **instruite** : aucune condition | 140 v2, 142 |
| Reduction d'ordre (modes parasites de l'equation d'ordre quatre ecartes) | cadre | 133 |
| Procede de resommation | **extrait et qualifie** : procede de groupe de renormalisation, non verifie a l'ordre superieur, sous deux hypotheses declarees par ses auteurs ; independance de jauge gravitationnelle non discutee | 148 v2, 153 |
| Limite Ω → 0 | **extrapolation du programme** : les sources parlent d'« endless phase of de Sitter expansion », pas de 𝓘⁺ | 138, 148 v2, 153 |
| Convention lisse au sens de la limite ; (2.17) comme critere | decisions de l'operateur, argumentees | 126, 138 |

**Important** : le premier ordre (γ = 8, le logarithme) ne depend pas du procede de resommation. Si le relecteur rejette la clause resommee, il reste : W_E ≈ W₀(1 + 8bκ ln a), c'est-a-dire une divergence logarithmique du Weyl rescale en 𝓘⁺, deja incompatible avec un raccord lisse (W continue non C¹ au mieux, NOTE-123 v2).

---

## 5. Qu'est-ce qui compense le pole ? (table des contributions a R de (2.17), ordre ε)

| Contribution | Effet sur R | Note |
|---|---|---|
| WZ partie c : b σ C² | **pole (8bκ/Ω) W_E** | 125 v2, 128 |
| WZ partie a : Euler, integrable | 6aĝ : rien | 131, 137 |
| Γ[g] non locale, tout etat Hadamard (ordre ε) | w C^∞ jointe a travers 𝓘⁺ : s² × lisse, rien | 146 v3, 150, 155 v2, 161 |
| Γ[g], noyau retarde sur l'histoire de l'onde | B[h] ≡ 0 sur l'onde exacte ; reponse lisse pour toute emission a temps fini : rien | 159 v2, 161 |
| Etat homogene anisotrope (ordre ε⁰) | Hadamard : rien ; non Hadamard N = 3 : pole propre, independant de l'onde, non compensateur | 157 v2, 161 |
| σ_h homogene, lisse ou singulier | rien hors d'un ensemble de mesure nulle (vide dans D′) | 140 v2, 142 |
| Etats non Hadamard (cone reflechi ; cones de σ_h) | seuls compensateurs possibles ; exclus par admissibilite | 140 v2, 146 v3, 157 v2 |
| Retroaction d'ordre κ²b | negligeable | 125 v2 |
| **Total** | **pole non compense dans la classe Hadamard** | |

---

## 6. Concordance avec la litterature

| Espece | 8bκ (programme) | Source exterieure, converti (κ_W² = 16πG) | Equation | Egal |
|---|---|---|---|---|
| Scalaire conforme | G/(30π) | 2501.01972 eq. 46 ; 2606.17963 | κ_W²H²/(480π²) | oui |
| Fermion de Dirac | G/(5π) | 2501.01972 eq. 35, 42 ; 2606.17963 | κ_W²H²/(80π²) | oui |
| Photon | 2G/(5π) | 2412.11022 eq. 53, 60 ; 2606.17963 | κ_W²H²/(40π²) | oui |
| Exposant resomme | −2γ = coefficient du log | 2412.11022 eq. 58 ; 2405.01024 eq. 91 | γ = −κ_W²H²/(80π²) (photon) | oui |

Scripts de conversion : iru_litt_check.py (133), irv_conversion.py (135), irz_conv.py (148), irab_conv.py (153) ; lectures aveugles W-b (137), ZA-1 (150), ABA-1 (161).

Le programme ne revendique pas le coefficient : il est dans la litterature depuis 2024-2026. Ce qu'il apporte : (i) une derivation independante par l'action anomale dans le repere conforme, qui le relie a l'anomalie de trace (b) et au contre-terme de Weyl ; (ii) sa lecture a 𝓘⁺ comme obstruction au raccord de la CCC, que ces auteurs ne considerent pas.

---

## 7. Calibration des enonces

- **[calcule]** (sortie de script empreintee, reproduite a l'audit) : le pole et son coefficient (125 v2, 128) ; 6aĝ (131, 137) ; c_n = 0 (140 v2, 142) ; la classe homogene de Bogoliubov et le cone reflechi (146 v3, 150) ; le tenseur anisotrope (157 v2, 161) ; le Bach nul, la reponse adiabatique et l'emission finie (159 v2, 161) ; γ = 8 (133, 137) ; les conversions (133, 135, 148 v2, 153).
- **[extrait]** (lu a la source, verbatim) : les enonces de Tod, Friedrich, Meissner-Penrose sur la lissite supposee (123 v2) ; les coefficients et le procede de resommation (135, 148 v2, 153) ; les theoremes de propagation et d'equivalence, lus dans Khavkine-Moretti 1412.5945 et Sanders 0903.1021 (155 v2 ; **sources primaires de Radzikowski 1996 et Fulling-Sweeny-Wald 1978 non lues**, acces refuse).
- **[derive]** (raisonnement du programme) : l'argument general Hadamard ⟹ w lisse jointe (146 v3, reconstruit a l'audit 150 et 161 sur les enonces lus) ; la transposition a Dirac et Maxwell du resultat anisotrope (157 v2) ; la condition de convergence (159 v2) ; le reexamen de la convention et le rapprochement avec le temps de rupture (138).
- **Cite de memoire** (EX-8) : l'invariance conforme de la condition de Hadamard pour le scalaire a ξ = 1/6 ; Miao-Tsamis-Woodard 2110.08715 et Glavan et al. 2307.09386 (origine du procede) ; Sahlmann-Verch 2001.

---

## 8. Objections anticipees, et ce que le programme repond aujourd'hui

1. **« Le logarithme seculaire des corrections quantiques en de Sitter est un artefact de jauge ou de choix d'observable. »** C'est l'objection la plus serieuse et le programme ne la tranche pas : les sources lues ne discutent pas l'independance de jauge gravitationnelle des logarithmes induits par les boucles de matiere (153). Elements en faveur de la robustesse : le pole est retrouve dans une famille de jauges et de facteurs conformes (128) ; le Weyl est un invariant de jauge lineaire ; le coefficient coincide entre deux methodes tres differentes (action anomale dans le repere conforme ; calcul direct en de Sitter). Le relecteur est invite a dire si une transformation de jauge peut absorber un ln a du Weyl electrique.
2. **« La resommation en puissance n'est pas demontree. »** Exact, et dit tel quel dans le libelle (clause resommee). Mais le premier ordre suffit a l'obstruction (§4, remarque finale).
3. **« L'effet est de 10⁻¹²² : il n'a aucun sens physique. »** Le programme en convient et l'ecrit (portee physique). L'obstruction est « de principe » : elle atteint la CCC comme enonce de limite Ω → 0. Une CCC reformulee a temps conforme fini (option B de NOTE-138) ne serait pas touchee ; elle n'est pas la CCC de Penrose.
4. **« L'action effective a une boucle n'est pas une source semi-classique legitime pres de 𝓘⁺. »** Hypothese de cadre, commune a tout traitement semi-classique du raccord ; le programme n'a pas d'argument au-dela.
5. **« Vous avez suppose l'etat Hadamard ; la CCC pourrait exiger un autre etat au bord. »** Tout etat non Hadamard ne compense le pole qu'au prix d'une singularite sur une hypersurface nulle du volume (cone reflechi) ou d'un pole propre d'ordre zero (157 v2). Le programme considere qu'un tel etat n'est pas un etat physique ; le relecteur peut en juger autrement.
6. **« Friedrich (2.17) n'est pas le bon critere. »** Instruit en 123 v2 : c'est le critere de regularite du systeme conforme ; la CCC exige au moins la finitude de W, qui est violee independamment du critere.
7. **« Le mode tensoriel sur de Sitter exact est trop particulier. »** Robustesse verifiee (128) ; un fond asymptotiquement de Sitter (P2 de la branche PREMISSE) n'est pas traite ; le programme ne pretend pas au-dela du cadre.
8. **« Les theoremes de propagation de Hadamard ont ete lus dans une introduction, pas a la source. »** Exact, declare (155 v2) ; les hypotheses exactes sont citees avec numeros de theoremes ; l'acces aux CMP de 1996 a ete refuse par les editeurs aux outils du programme.

---

## 9. Comment relire

- **Depot** : toutes les pieces sont dans `D:\temporaire` (copie locale de l'operateur) et seront deposees sur Zenodo (v2) et sur `github.com/droppy94/LC_Raccord`. Chaque note a un sceau `NOTE-nnn-SCEAU.txt` (horodatage UTC, empreintes sha256 de la note, des scripts, des sorties et des extraits de sources). Le registre central (`REGISTRE-CENTRAL-NUMEROS-NOTES.md`) donne, pour chaque numero, le fichier, l'empreinte et le statut.
- **Ordre de lecture conseille** (une demi-journee) : 138 v4 (le libelle et le reexamen) ; 125 v2 (le pole) et 128 (son audit) ; 131 et 133 (compensation, transport) et 137 (audit) ; 146 v3 (etat Hadamard) et 150 ; 148 v2 et 153 (sources de la resommation) ; 159 v2 (noyau retarde) ; 161 (dernier audit). Les gels (124, 130, 132, 134, 145, 147, 152, 154, 156, 158, 160) montrent ce qui etait predit avant chaque calcul.
- **Scripts** (python3, sympy, mpmath) : irr_c.py (125), irt_a.py, irt_gamma_phi.py (131), iru_transport.py (133), irv_conversion.py (135), irx_cone.py (140), iry_state_v2.py (146), irz_conv.py (148), irab_conv.py (153), iraa_aniso_v2.py (157), irad_kernel.py (159). Les rapports des auditeurs, avec leurs propres scripts, sont dans les dossiers `audit_*`.
- **Sources lues**, extraits empreintes dans `src\` : Tod 1309.7248 ; Friedrich 1311.0700 ; Meissner-Penrose 2503.24263 ; Foraci-Litos-Woodard 2606.17963 ; Woodard 2501.05077 ; Foraci-Woodard 2501.01972 et 2412.11022 ; Miao-Tsamis-Woodard 2405.01024 ; Froeb-Roura-Verdaguer 1205.3097 ; Hawking-Hertog-Reall hep-th/0010232 ; Dvali-Gomez-Zell 1701.08776 ; Khavkine-Moretti 1412.5945 ; Sanders 0903.1021.

---

## 10. Non-surclassement

Cette piece compile ; elle ne grave rien. G-V3 est un **candidat** d'incompatibilite, au grade [conv], audite en interne, non relu par un tiers. La CCC dans sa forme actuelle est par ailleurs refutee a titre provisoire par une autre voie (RG-4, l'electron massif : synthese NOTE-164) ; CCC + M (mecanisme d'effacement des masses) reste une hypothese ouverte, et G-V3 l'atteint aussi puisqu'il ne depend pas de M. Le noyau irreductible du programme {A4 ; A2★ ; N} est inchange. Aucune promotion de G-V3 n'aura lieu sans acte de l'operateur fonde sur une lecture exterieure.


---

## Greffe G-CAL-a (2026-10-15, acte NOTE-179)
La ligne « Comptage » de la table des conventions est remplacee (v1 : « pole si et seulement si p = 1 et Y(0) ≠ 0 »). Motif : calibration CAL-F (NOTE-175 a 178), confirmee par deux auditeurs isoles. Contre-exemples : poussiere homogene (p = 1, contribution nulle) ; scalaire sans masse inhomogene phi = x (p = 0, pole double −κ/(3s²)) ; phi = x s^Δ (pole d'exposant non entier pour 0 < m² < 2, absent a m² = 2, point de Friedrich). **Aucun resultat de G-V3 ne change** : la chaine repose sur des calculs covariants explicites. Point de lecture ajoute pour le relecteur (v2) : un pole du second membre de (2.17) evalue sur une solution prouve l'irregularite au sens de Friedrich si les autres inconnues sont lisses sur cette solution ; la reciproque est fausse (le critere de Friedrich est la regularite formelle des seconds membres en fonction des inconnues).

## Greffe G-AF (v3, 2026-10-16, acte NOTE-200)
Le point de lecture ci-dessus est **leve** : le pole est etabli comme terme **formel** du second membre de (2.17) (pas 2 bis, NOTE-197 v2, audit NOTE-199), independamment de la lissite des autres inconnues sur une solution. Bornes a connaitre pour la relecture : premier ordre autour de la metrique conforme plate ; choix d'inconnues de Friedrich (un poids anomal p = 1 + bc₀κ retire le pole electrique en le transferant au canal magnetique, aucun poids constant ne le retire pour W generique) ; la partie principale est modifiee a l'ordre κb (derivees de W au second membre). Recoupement : l'integration du pole formel sur un mode homogene redonne la dimension anormale γ = 8 (pas 7) et l'exposant resomme (pas 9) par exponentiation de l'ordre b. Question supplementaire au relecteur : la forme formelle du pole vous parait-elle la bonne maniere de poser l'obstruction au sens de Friedrich, compte tenu de la modification de la partie principale ?
