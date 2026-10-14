---
id: NOTE-BORD-EON-161-AUDIT-IR-ab-ac-aa-ad-CONCORDANCE
numero: 161
serie: I
branche: Q-M3 suite (audit IR-ab, IR-ac, IR-aa, IR-ad)
reservation: 2026-10-13T11:30 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 161)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-160-ARMEMENT-AUDIT-IR-ab-ac-aa-ad (sha256 9ab4bf9a9ef2a7d45cd2e8a125d1e9593cc68c776281a11bf8cd42c132646d36, sceau 2026-10-13T11:26:53Z)
rapports:
  - "audit_p1/aba1/RAPPORT-ABA1.md, sha256 954839625dec36fba75452858265af63ee773a644a8154848d554943d666bf3e (lecture aveugle de [8] et [27], conversion sympy)"
  - "audit_p1/aca1/RAPPORT-ACA1.md, sha256 92640de841c280e7b582d59b0134039f98b8c796a2625aa985f48080674f3b14 (lecture aveugle de Khavkine-Moretti et Sanders, application au demi-espace)"
  - "audit_p1/aaa1/RAPPORT-AAA1.md, sha256 7069f03811020d3a0619e54f7a7bed5705ed2ef6eba8b0face289e7f5ab0f97e (derivation en cecite stricte du tenseur anisotrope)"
  - "audit_p1/aaa2/RAPPORT-AAA2.md, sha256 048ea8da9ebe22ccaee4a4d60ba6866cf806c75fa01f5f4d4615d0b594940487 (audit de iraa_aniso_v2.py, reproduction independante)"
  - "audit_p1/ada1/RAPPORT-ADA1.md, sha256 6b4a7edb60af60ba0b8eadb64445542813aae54d8b479171a53fa31a89bbc2ea (derivation en cecite stricte : Bach, noyau, limite adiabatique, emission finie)"
  - "audit_p1/ada2/RAPPORT-ADA2.md, sha256 9e43745d1745ae0c262b035586608f8bd6f07a6cb166899de730034bd4543faf (audit de irad_kernel.py, robustesse des regularisations)"
objet: [NOTE-BORD-EON-153-IR-ab-LECTURE-2412.11022-2405.01024, NOTE-BORD-EON-155-IR-ac-LECTURE-FNW-RADZIKOWSKI, NOTE-BORD-EON-157-IR-aa-EXECUTION, NOTE-BORD-EON-159-IR-ad-PASSE-ADIABATIQUE-EXECUTION]
verdict: "AU-V1 pour 153 ; AU-V2 pour 155 ; AU-V2 pour 157 ; AU-V2 pour 159"
prediction_realisee: "oui (les quatre verdicts predits) ; contenus des precisions en partie differents de ceux predits"
rouvre_si:
  - "lecture primaire de Radzikowski 1996 / Radzikowski-Verch 1996 contredisant un enonce de S1 utilise"
  - "termes d'Euler non locaux ou ordre superieur en courbure (hors cadre de 159)"
---

# NOTE-161 : concordance de l'audit froid aveugle conjoint de NOTE-153, 155, 157 et 159. Tous les resultats porteurs sont retrouves ; precisions de detail pour 155, 157, 159 ; aucune correction de verdict. Verdicts **AU-V1 (153)**, **AU-V2 (155)**, **AU-V2 (157)**, **AU-V2 (159)**

## 0. Resume
- **153 (IR-ab) confirmee sans correction** (ABA-1) : n = 8 pour le photon, γ depuis c₂, exposant −2γ, γ_MMC, δZ ; appariement ln μ / ln a (eq. 5/6), deux sources de logarithmes, photon sans queue ; « nonlocal contribution vanishes » par (∂₀ + ik)²∂₀u₀ = 0 ; attribution « convenient to adopt the latter interpretation » ; sommation « If we ignore possible running of Newton's constant » ; validite comparee a des resultats perturbatifs au premier ordre non trivial, jamais a l'ordre superieur ; jauge, a → ∞, e-folds, deux boucles non discutes ; « endless phase of de Sitter expansion ». Deux remarques hors criteres, sans greffe : (i) [27] renvoie a « Section 3 » pour les modeles sigma traites en section 2 (incoherence interne de la source) ; (ii) le scalaire MMC de [27] correspond a n = −72 (pas de facteur universel en b hors champs conformes, ce qui est attendu : seuls les champs conformes relevent de G-V3).
- **155 (IR-ac) confirmee avec precisions** (ACA-1) : Def. 15, Th. 9, Prop. 16 (b), Rem. 23 releves verbatim ; **propagation sans positivite** confirmee (la preuve n'utilise que la bisolution, les fronts d'onde de E± et la composition des noyaux) ; lacune de Radzikowski Th. 5.1 (p. 547) comblee par Sahlmann-Verch 2001, these de Sanders 2008, S1 (idee de Pinamonti) ; attribution de la propagation a **Fulling-Sweeny-Wald 1978 [24] et Wald 1994 [70]** ; FNW 1981 cite pour les etats statiques et dans la liste [24, 26, 45]. Precisions a porter en v2 : (a) la preuve de Prop. 16 (b) n'etablit que l'**inclusion** WF(ω₂) ⊂ H, l'egalite vient de l'hermiticite (positivite) via Sanders Prop. 2.8 / 3.2 pour un champ libre ; (b) **chemin alternatif** pour y-3 : Th. 9 (a) sur le demi-espace → Rem. 23 sur R⁴ → Sanders Lemma 2.9 (dont la preuve n'utilise pas la positivite) avec partie antisymetrique iE/2 : la positivite n'est consommee qu'au depart ; le chemin de NOTE-155 (par Th. 9 (b)) la consomme a l'arrivee ; les deux sont valides ; (c) hypotheses a expliciter : existence et unicite du prolongement bisolution (formule S^t∘ω₂∘S), controle de la partie antisymetrique, identification des cones H (S1) et Γ₂ (S2) et de la relation ∼ sur le demi-espace comme restriction de celle de R⁴ ; (d) metadonnees : Springer a refuse (HTTP 429) les pages de Radzikowski 1996 et Radzikowski-Verch 1996 a l'auditeur ; NOTE-155 les avait obtenues : sans contradiction, statut inchange (non libres). (e) invariance conforme : rien dans S1 ni S2, conforme.
- **157 (IR-aa) confirmee avec precisions** (AAA-1 en cecite stricte, AAA-2) : terme αβ* : **T₀₀ = T₀ᵢ = 0, T_ij = A(k_i k_j − ⅓k²δ_ij)**, retrouve deux fois (AAA-1 par forme bilineaire sur les modes, AAA-2 par sympy et differences finies a 2,6 × 10⁻¹²) ; isotrope : disparait ; anisotrope : seul le moment ℓ = 2 survit ; I_N = Γ(4−N)(−2is)^(N−4), N = 3 → 1/s (coefficient ∝ sin φ, nul pour αβ* reel), N = 4 → ln (coupure IR), gaussien entier ; cone reflechi, singularite conormale d'ordre fini, non Hadamard pour tout N, anisotropie sans effet sur le critere ; s²T ~ s^(N−2), terme lineaire ssi N = 3, non Hadamard ; **aucun contre-exemple** (borne uniforme |T^tf| ≤ (2/3)(2π)⁻³∫d³k k|αβ*| : decroissance rapide ⟹ C^∞). Precisions a porter en v2 : (a) l'annotation « attendu −1/2 » est fausse de signe (η·I → +1/2) ; (b) le commentaire « P1 (vide, soustrait) » est trompeur : P1 porte |β|² apres soustraction et contribue au secteur |β|² autant que P2 (le script n'en calcule que la moitie ; sans effet sur le terme αβ*) ; (c) les sections aa-3 et aa-4 du script sont imprimees en dur ([rapporte], non [calcule]) ; (d) coefficient du 1/η en sin φ (deja en NOTE-146 v2) ; (e) la somme P1 + P2 du secteur |β|² est un gaz de quanta nuls (T₀ᵢ = 0 apres somme).
- **159 (IR-ad) confirmee avec precisions** (ADA-1 en cecite stricte, ADA-2) : B = −¼□²h retrouve (ADA-1 aussi sur onde plane TT generique ; ADA-2 : (∂² + k²)²u = 0 pour la **solution generale** de l'ODE, par dsolve) ; noyau derive par ADA-1 avec sa partie locale, verifie a 10⁻²⁸ ; B_ε = −8εk³e^(ετ)sin kτ ; **R_ε(0) = −4πk³ε + O(ε² ln ε)** en forme fermee (ADA-1), valeurs numeriques concordantes a 14 chiffres (ADA-1) et 10⁻⁹ (ADA-2) ; emission finie : R analytique pour τ > −4, R(0) = 0,408341, R′(0) = 1,228887, dependance en τ₀ (0,70 ; 0,41 ; 0,18 ; 0,093 ; 0,014 pour τ₀ = −5, −6, −8, −12, −20), lissite structurelle ; **regularisation de la partie finie legitime** : changer l'echelle L ajoute 2B_ε(τ₀)[Ci(kL) − Ci(k)], terme local O(ε) equivalent a un changement de μ, nul pour τ > −4 en emission finie ; differences finies concordantes a 10⁻¹⁷ avec la derivation symbolique. Precisions a porter en v2 : (a) l'annotation du coefficient de δ(T) est fausse : c(k, μ) = 2 ln k − 2Ci(k) − 2 ln μ (non −2(γ_E + ln μ), limite k → 0 seulement) ; sans effet (terme local, ∝ B) ; (b) le noyau d'ad-2 et les sections ad-5 et la derniere ligne d'ad-4 sont imprimes en dur ; (c) en τ₀ = 0 le terme dominant est −4πk³ε (le coefficient du ln s'annule), le rapport R_ε/(ε ln(1/ε)) imprime tend vers 0 ; en τ₀ ≠ 0 la loi est 8εk³ sin(kτ₀)E₁(ε) + O(ε) ; (d) la serie en ε n'est pas uniforme en τ (termes ε²τ), sans effet car l'expression exacte est integree ; (e) code mort (B_eps_num) ; (f) resonance logarithmique possible si B contient une composante cos kτ′ non amortie (condition de convergence a formuler ainsi).

## 1. Confrontation aux criteres (figes, NOTE-160 §2)
| Critere | Resultat | Statut |
|---|---|---|
| **C-1 (153)** | ABA-1 : n = 8 ; γ_S8 = −GH²/(5π) depuis c₂ ; −2γ = exposant de (60) ; γ_S27 = 3GH²/(20π) (parts c₁ : +GH²/(6π), c₂ : −GH²/(60π)) ; δZ = D[2(D−1)c₁ − c₂]κ²H² (eq. 91 / 57) | **satisfait** |
| **C-2 (153)** | ABA-1 : eq. 5 et 6 relevees ; deux sources ; « no tail term » ; aucune verification d'ordre superieur ; « convenient » ; « If we ignore possible running of Newton's constant » ; « nonlocal contribution vanishes » par (49) ; « endless phase » | **satisfait** |
| **C-3 (155)** | ACA-1 : Prop. 16 (b) + Rem. 23 sans positivite ; Th. 9 pour des etats ; lacune p. 547 comblee par Sahlmann-Verch 2001 (et Sanders 2008, S1) ; propagation attribuee a [24] FSW 1978 et [70] Wald 1994 | **satisfait**, precision ([70] identifie) |
| **C-4 (155)** | ACA-1 : chaine reconstruite ; positivite au depart (Th. 9 (a)) par le chemin Lemma 2.9, a l'arrivee par Th. 9 (b) ; hypotheses a expliciter (prolongement, partie antisymetrique, identification des cones) | **satisfait avec precisions** |
| **C-5 (157)** | AAA-1, AAA-2 : T₀₀ = T₀ᵢ = 0, T_ij ∝ e^(−2ikη)(k_i k_j − ⅓k²δ_ij) ; |β|² independant de η ; exposant N − 4, 1/η pour N = 3, entiere pour gaussienne ; annotation « −1/2 » fausse relevee | **satisfait** |
| **C-6 (157)** | AAA-1 : anisotropie sans effet sur le cone reflechi ; AAA-2 : aucun contre-exemple, borne uniforme | **satisfait** |
| **C-7 (159)** | ADA-1, ADA-2 : B = −¼□²h ; (∂² + k²)²u = 0 (solution generale) ; B_ε ; noyau −2 Pf[θ cos/T] + local | **satisfait** |
| **C-8 (159)** | ADA-1 : R_ε(0) = −4πk³ε → 0 ; ADA-2 : robuste a l'echelle (terme local O(ε)) ; R lisse en 0, finie, non nulle, dependante de τ₀ | **satisfait** |

## 2. Points de detail [rapporte]
### 2.1 ABA-1
- [8] : eq. 12 (κ² = 16πG), 53, 60 ; sections 1 et 4 ; « late time » = « endless phase » ; theorie effective non locale (puissance fractionnaire de r).
- [27] : eq. 6, 89, 91, 92, 93-95 ; reserves verbatim ; comparaison Table 1 (modele AB) au premier ordre non trivial seulement.
- Hors criteres : « Section 3 » pour section 2 ; MMC n = −72.

### 2.2 ACA-1
- Def. 15 : locale, dimension 4, enoncee pour un etat, quasi-libre non requis. Th. 9 (b) : preuve deleguee a Radzikowski-Verch Th. 4.3.
- Prop. 16 (b) : hypothese microlocale sur O × O ; preuve : ω₂ = S^t∘ω₂∘S ; inclusion WF ⊂ H seulement.
- S2 : positivite en Prop. 2.8 (hermiticite ⟹ egalite WF(ω₂) = WF(ω₂₋) ∩ Γ₂) et Prop. 4.1 (GNS) ; Lemma 2.9 prouve sans positivite ; Lemma 4.6 (n = 0) = Lemma 2.9 + commutateur commun.
- Metadonnees : seule la page de FSW 1978 lue (CMP 63, 257-264, non libre) ; Springer 429 pour les deux Radzikowski ; Euclid et ScienceDirect bloques ; aucun contournement.

### 2.3 AAA-1 et AAA-2
- AAA-1 : sans amelioration (ξ = 0) une pression isotrope oscillante subsiste ; l'amelioration la retire. N = 5 : 1/μ + s ln s + cs. Reserves : Q4 sur cas calcules (f = 1, P₂), non preuve generale ; coupure IR pour N ≥ 4.
- AAA-2 : reproduction a 2,6 × 10⁻¹² ; lignes en dur 72 (formule Γ, juste au sens d'Abel), 81 (annotation fausse), 85, aa-3, aa-4 ; cas limite (gaussien direction par direction, constant sur un axe) donne un k⁻³ effectif et un 1/η mais n'est ni Schwartz ni Hadamard ; une quadrature de son premier script etait tronquee, remplacee.

### 2.4 ADA-1 et ADA-2
- ADA-1 : K_k(T) = −2Pf[θ(T)cos(kT)/T] − 2 ln(μT₀e^γ)δ(T), independance en T₀ verifiee ; R_ε(0) forme fermee avec developpement −4πk³ε + ε²(8k² ln(ε/μ) + 8k² ln(2k/μ) + 10k²) + … ; borne |R_ε(0)| ≤ 13ε ; point d'attention : toute valeur en τ = 0 est une fonctionnelle de l'histoire de branchement, non une propriete de l'onde de de Sitter, Bach-plate.
- ADA-2 : c(k) = 2 ln k − 2Ci(k) verifie a 10⁻¹⁹ ; dependance d'echelle 2B_ε(τ₀)[Ci(kL) − Ci(k)] a 10⁻⁶ ; R(τ) a 14 chiffres par deux methodes ; derivees 2 a 4 finies ; bogue de son propre script corrige en cours d'audit.

```
   audit conjoint du 13 octobre : ce qui est retrouve a l'aveugle
   -------------------------------------------------------------------------------------------
   153  n = 8 (photon), gamma depuis c_2, exposant -2 gamma, reserves L1 L2, "vanishes"   ABA-1
   155  propagation sans positivite, equivalence pour etats, lacune / Sahlmann-Verch,    ACA-1
        FSW 1978 + Wald 1994 ; chemin alternatif Lemma 2.9 ; inclusion vs egalite
   157  T_00 = T_0i = 0, T_ij sans trace, N = 3 seul, cone reflechi, pas de contre-ex.   AAA-1, AAA-2
   159  B = -1/4 box^2 h, Bach nul, R_eps(0) = -4 pi k^3 eps -> 0, R lisse en 0,         ADA-1, ADA-2
        regularisation = ambiguite de mu
   -------------------------------------------------------------------------------------------
   aucun verdict modifie ; greffes v2 de 155, 157, 159 (precisions) ; 153 inchangee
```

## 3. Verdicts
- **NOTE-153 : AU-V1.** Criteres C-1, C-2 satisfaits sans correction. Deux remarques consignees ici, sans greffe.
- **NOTE-155 : AU-V2.** C-3, C-4 satisfaits ; greffe v2 proposee : chemin alternatif (Lemma 2.9), inclusion vs egalite, [70] = Wald 1994, FNW 1981 cite pour les etats statiques, hypotheses a expliciter (prolongement bisolution, partie antisymetrique, identification des cones).
- **NOTE-157 : AU-V2.** C-5, C-6 satisfaits ; greffe v2 proposee : annotation de signe, commentaire P1, sections en dur requalifiees [rapporte], gaz de quanta nuls, coefficient sin φ.
- **NOTE-159 : AU-V2.** C-7, C-8 satisfaits ; greffe v2 proposee : coefficient de δ(T), noyau et ad-5 requalifies [rapporte], loi exacte R_ε(0) = −4πk³ε, dependance d'echelle = ambiguite de μ, resonance logarithmique dans la condition de convergence, code mort.

## 4. Confrontation a la prediction
Prediction (NOTE-160 §4 : AU-V1, AU-V2, AU-V2, AU-V2) : **realisee** pour les quatre verdicts. Contenus : 153 remarques non predites (section, n = −72) ; 155 : la precision predite ([70] ; demi-espace globalement hyperbolique) est retrouvee, et deux non predites (inclusion vs egalite ; chemin par Lemma 2.9 deplacant la positivite au depart) ; 157 : annotation predite, et P1 / sections en dur non predites ; 159 : dependance d'echelle predite (terme local O(ε)), et la forme fermee −4πk³ε, le coefficient de δ(T) et les differences finies **fiables** (contrairement a la prediction « bruitees ») non predits.

## 5. Consequences (rien n'est grave)
- Greffes v2 de 155, 157, 159 a enter par NOTE-162 avec 146 v3 et 138 v4 ; 153 inchangee.
- Libelle de G-V3 : les precisions ne touchent ni la classe ni les clauses ; la revision v4 (NOTE-162) integre 153, 155, 157, 159 telles qu'auditees.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Non-surclassement
[conv]. Audit par sous-agents isoles sous consignes scellees ; les auditeurs de lecture n'ont pas eu acces aux sources primaires de revue (memes blocages que NOTE-155) ; la cecite est stricte pour AAA-1 et ADA-1 (aucun contexte de G-V3 ni de (2.17)).
