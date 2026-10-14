---
id: NOTE-BORD-EON-133-IR-u-EXECUTION
numero: 133
serie: I
branche: Q-M3 suite (IR-u)
reservation: 2026-10-12T12:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 133)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-132-ARMEMENT-IR-u (sha256 ecb66e5bb65da353ac585c7e999693c7b139caf67ac60f41917f4efae2f5fdf2, sceau 2026-10-12T12:22:28Z)
instruments:
  - "iru_transport.py, sha256 5e1112b73e07fcb8cec256cc1f21bfa3195ab20286f41d9ec6ea86907437e305, 2026-10-12T12:23:10Z : EXIT 0, sortie iru_transport_sortie.txt"
  - "iru_coherence.py, sha256 dff42507624a3911e6a66f0f44a3aa1500541a738c0570bd51bf84e08a749063, 2026-10-12T12:24:40Z : EXIT 0, sortie iru_coherence_sortie.txt (controle u-3 prevu au gel §1)"
  - "iru_litt_check.py, sha256 53dd3b9276fce9194804ce911caea986528dfa7892421129f32442eef64a127b : EXIT 0, sortie iru_litt_check_sortie.txt (comparaison numerique u-4, ajoutee apres lecture, non prevue au gel)"
sources:
  - "Foraci, Litos, Woodard, arXiv:2606.17963v1 (2026) : extraits src/SOURCE-2606.17963v1-extraits.txt, sha256 0de0294f1f3a563200663feb826d04f89cf9d0f915b4cb203f9f06c96ed892f7"
  - "Froeb, Roura, Verdaguer, arXiv:1205.3097v2 (2012) : extraits src/SOURCE-1205.3097v2-extraits.txt, sha256 55b714cd678b11a5325da57952282feffdfcf55f772577d7348280ff211faa28"
  - "Hawking, Hertog, Reall, arXiv:hep-th/0010232v4 (2001) : extraits src/SOURCE-hep-th0010232v4-extraits.txt, sha256 0250e02417f1d04a995e05da4834f633a21a8383ad8915134df9a017a981a38c"
depend: [NOTE-BORD-EON-132-ARMEMENT-IR-u, NOTE-BORD-EON-125-IR-r-EXECUTION (v2), NOTE-BORD-EON-131-IR-t-EXECUTION]
verdict: "U-V1"
prediction_realisee: "oui (depassee sur u-4 : accord quantitatif, non seulement qualitatif)"
rouvre_si:
  - "modes parasites de l'equation d'ordre quatre pris au serieux (hors reduction d'ordre)"
  - "convention de normalisation de b ou de kappa differente de celle supposee au §2.4"
  - "resommation (groupe de renormalisation) contredisant la forme W ∝ Ω^γ"
  - "audit froid"
---

# NOTE-133 : IR-u. γ = 8 au premier ordre, et la litterature donne exactement le meme coefficient. Verdict **U-V1**

## 0. Resume
- **u-1** : u₁ contient (8/3) B k³ s³ ln s, soit exactement 8 ln s fois le terme B k³s³/3 du mode du vide [calcule].
- **u-2** : W_E ≈ W₀ (1 + 8 bκ ln s) avec W₀ = −Bk³ cos kx / 2. **γ = 8**, independant de k ; la donnee A ne produit pas de log a l'ordre s⁰ [calcule].
- **u-3** : residu du pole de (2.17) = −8bκ W₀ (composante R_ysy) ; s ∂_s du terme log de W_E = +8bκ W₀. Meme module, signe oppose : c'est l'orientation (s croit vers le passe, η^ss = −1 dans la contraction de Bianchi) [calcule pour les deux nombres, derive pour le signe].
- **u-4** : Foraci, Litos et Woodard (2026) donnent pour le Weyl electrique des ondes gravitationnelles en presence de matiere conforme un facteur 1 + (3κ_W²H²/π²) C_q ln a, d'origine renormalisation. Converti dans nos conventions, leur coefficient egale **exactement** 8bκ (en ln a), pour le scalaire conforme, le fermion de Dirac et le photon [extrait + calcule].

## 1. Resultats [calcule]
### u-1, u-2 (iru_transport.py)
| Grandeur | Resultat |
|---|---|
| Operateur L[u] = (G + 3ĝ)_yy, ordre ε | (k²s u + s u'' − 2u') cos kx / (2s) ; fond nul ; L[u₀] = 0 |
| T̂_yy[u₀] / b (c₀ = +8) | 4k³ s (−A sin ks + B cos ks) cos kx |
| Partie log de u₁ | (8Bk³s³/3 − 4Bk⁵s⁵/15) ln s (+ modes homogenes libres) |
| W_E,yy (b = 0) en s = 0 | −Bk³/2 |
| Coefficient de ln s dans W_E,yy a s⁰ | −4Bbk³κ |
| **γ** | **8** |

La donnee A n'entre dans W_E qu'aux ordres s¹ et au-dela. Les modes homogenes (a₅, a₆) ne renormalisent que W₀ (terme 15a₅bκ/k²), sans log.

### u-3 (iru_coherence.py)
| Grandeur | En unites de bκW₀ |
|---|---|
| Residu de 1/s dans R_ysy (2.17), T̂[u₀] | −8 |
| Residu de 1/s dans R_zsz | +8 (polarisation opposee) |
| s ∂_s (8bκW₀ ln s) | +8 |
| Trace de T̂ | 0 |

## 2. Litterature (EX-7, EX-8, EX-9)
### 2.1 Declaration EX-7
Recherche apres le sceau (12:22:28Z) : alphaXiv (discover_papers, puis lecture ciblee). Le gel listait trois candidats de memoire. **Lu** : Hawking-Hertog-Reall 2001 (candidat du gel). **Non lus** : Starobinsky 1981-83 et Fabris-Pelinson-Shapiro (pas de version arXiv lisible trouvee par l'outil dans cette session ; remplaces par deux travaux qui satisfont mieux le critere de retenue). **Ajoutes** : Froeb-Roura-Verdaguer 2012 (perturbations tensorielles sur de Sitter, matiere conforme, action anomale avec ln a) et Foraci-Litos-Woodard 2026 (fonctions de mode des ondes gravitationnelles, Weyl electrique). Lecture : resume et sections ou l'equation des modes et le Weyl sont ecrits, jusqu'a la fin de la section suivante (EX-9). La reference [12] de Foraci et al. (Woodard 2025, resommation par groupe de renormalisation) est **citee, non lue**.

### 2.2 Ce que disent les sources [extrait]
1. **Foraci, Litos, Woodard (arXiv:2606.17963), eq. 26-27, 31** : pour la matiere conforme, u₁ ∝ A + B(k/aH)² + iC ln(a)(k/aH)³ ; le Weyl electrique vaut C^tree × {1 + 3κ_W²H² C ln(a)/π² + …}, avec C_q = 32/(3q), q = 2¹⁰·3·5 (scalaire), 2⁹·5 (fermion), 2⁸·5 (photon), κ_W² = 16πG. « The correction proportional to C arises from renormalization. » Elle provient du terme 8π ln(aa′) δ⁴ de l'auto-energie (eq. 11), qui est la trace du terme local en ln a × C², c'est-a-dire notre bσC².
2. **Froeb, Roura, Verdaguer (arXiv:1205.3097), eq. 3.19, 4.38** : l'action quadratique des modes tensoriels contient 3ακ² ∫ (□h)(□h) ln a, et le spectre super-horizon (amplitude de la metrique) ne recoit qu'un decalage constant.
3. **Hawking, Hertog, Reall (hep-th/0010232)** : calcul euclidien sur S⁴, propagateur tensoriel en (p⁴ log p)⁻¹ aux grands p ; normalisation c = (N_S + 6N_F + 12N_V)/(120(4π)²) du coefficient de C² dans la trace (eq. 2.7). Ils n'etudient pas la croissance tardive du Weyl electrique : ni concordance ni contradiction sur ce point.

### 2.3 Concordance qualitative [derive]
- La structure de Foraci et al. (log a l'ordre (k/aH)³ du mode, d'ou un log a l'ordre dominant du Weyl electrique, coefficient independant de k) est **celle de u-1 et u-2** : notre (8/3)Bk³s³ ln s est leur iC ln(a)(k/aH)³.
- Froeb et al. : la metrique (spectre) n'est decalee que d'une constante ; chez nous aussi, le log de u₁ n'apparait qu'a l'ordre s³, ce qui laisse la valeur figee de h inchangee. Le log porte sur le Weyl, pas sur la metrique.

### 2.4 Concordance quantitative [calcule, iru_litt_check.py]
Hypotheses de conversion : κ = 8πG (Friedrich, L̂ = (κ/2)(T̂ − ⅓ĝ tr T̂)) ; b = coefficient de C² dans ⟨T^a_a⟩ (normalisation HHR eq. 2.7) ; ln s = −ln a ; H = 1.

| Champ | Foraci et al., coefficient de ln a | IR-u, c₀ = −8 (Carroll-Wald) | IR-u, c₀ = +8 (gel) |
|---|---|---|---|
| scalaire conforme | G/(30π) | G/(30π) | −G/(30π) |
| fermion de Dirac | G/(5π) | G/(5π) | −G/(5π) |
| photon | 2G/(5π) | 2G/(5π) | −2G/(5π) |

Rapport egal a 1 pour les trois champs. Le module de γ est donc confirme par un calcul independant (auto-energie a une boucle, regularisation dimensionnelle, conditions de Bunch-Davies) ; le **signe physique** est celui de la convention Carroll-Wald : W_E ≈ W₀(1 + 8bκ ln a), croissance pour b > 0.

## 3. Lecture [derive]
1. Le pole G-V3 de (2.17) est la transcription, dans les equations conformes de Friedrich, d'un **effet connu et calcule** de la litterature : la croissance seculaire logarithmique du Weyl electrique des ondes gravitationnelles en presence de matiere conforme, d'origine renormalisation. G-V3 n'est donc pas un artefact du formalisme conforme.
2. Ce qui est nouveau ici est la **lecture** : sous l'angle du raccord, cette croissance signifie que le Weyl rescale n'a pas de limite finie en Ω → 0 au premier ordre (divergence en ln Ω). La litterature ne pose pas cette question (prediction §4 du gel : « sans avoir ete lu sous l'angle de la regularite au raccord »).
3. **Forme resommee** (conditionnelle, non verifiee ici) : si la resommation par groupe de renormalisation citee par Foraci et al. donne une loi de puissance, alors W_E ∝ a^{8bκH²} = Ω^{−8bκH²} (convention physique). Le Weyl rescale diverge en 𝓘⁺ comme une puissance tres petite de Ω⁻¹. C'est incompatible avec la condition de Penrose W|𝓘⁺ fini et non nul, quelle que soit la petitesse de bκH².
4. Le resultat est independant de k : il concerne toute onde gravitationnelle a 𝓘⁺ avec donnee electrique B ≠ 0 (donc w ≠ 0 de NOTE-125).

```
   W_E / W0  pres de scri+  (premier ordre, convention physique, b > 0)

   1 + 8 b kappa ln a      ln a -> +inf quand Omega -> 0
                           (Foraci-Litos-Woodard : meme coefficient, 3 champs)
   resomme (conditionnel) : Omega^(-8 b kappa H^2)  -> diverge lentement
```

## 4. Verdict
**U-V1.** γ = 8 calcule, non nul, independant de k ; W_E ≈ W₀(1 + γbκ ln Ω) au premier ordre (signe selon la convention de T) ; coherent en module avec le residu du pole de (2.17) ; la litterature retrouve le meme effet avec le **meme coefficient** pour trois especes de champs conformes. Qualifications nommees : (i) premier ordre en bκ, reduction d'ordre ; (ii) normalisations de b et κ supposees (§2.4) ; (iii) forme resommee non etablie ici (reference citee non lue).

## 5. Confrontation a la prediction
Prediction (NOTE-132 §4) : terme B k³ s³ ln s dans u₁ [**realise**] ; γ nombre pur non nul, independant de k, signe suivant la convention [**realise**, γ = 8] ; A sans log a l'ordre dominant [**realise**] ; coherence avec le pole a un facteur de normalisation pres [**realise**, facteur −1 d'orientation] ; litterature : effet de meme nature, non lu sous l'angle du raccord [**realise et depasse** : accord numerique exact]. La valeur de γ n'etait pas predite.

## 6. Consequences (rien n'est grave)
- **G-V3 consolide une troisieme fois** : retrouve a l'aveugle (NOTE-128), non compense (NOTE-131), et maintenant **ancre dans un resultat publie independant**. Libelle propose pour NOTE-126 (a acter par l'operateur) : « le Weyl rescale des ondes gravitationnelles diverge logarithmiquement en 𝓘⁺ au premier ordre, avec le coefficient 8bκ ; effet connu (croissance seculaire du Weyl par la matiere conforme), lu ici comme obstruction au raccord lisse ».
- La convention de signe c₀ doit etre unifiee sur Carroll-Wald (c₀ = −8) dans les libelles physiques ; le gel de NOTE-124 reste valide comme convention de calcul.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 restent des candidats non graves.

## 7. Pistes
- **Lecture de Woodard 2025 (arXiv:2501.05077)** : la resommation donne-t-elle W ∝ Ω^{−8bκ} ? (EX-7, gel prealable).
- **Audit froid** de NOTE-131 et NOTE-133 (en particulier la conversion §2.4 et le signe).
- **Acte** de requalification de G-V3 (libelle §6), sur decision de l'operateur.

## 8. Non-surclassement
[conv], non audite. Premier ordre en ε et en bκ, fond de Sitter, mode tensoriel, reduction d'ordre. La concordance avec la litterature porte sur le coefficient du log, pas sur la question du raccord, qui reste une lecture propre au programme.
