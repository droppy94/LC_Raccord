# Rapport W-b : lecture aveugle de S1, S2, S3 et conversion en Γ = n b κ

Auditeur froid, sans accès au travail antérieur. Sources lues uniquement via alphaXiv (get_paper_content fullText, answer_pdf_queries) le 2026-10-12. Seul fichier hors de /home/claude/audit_wb/ ouvert : le prompt de consigne.

Étiquettes : **[extrait]** citation verbatim (transcription linéarisée de l'extraction texte du PDF, équation et page imprimée) ; **[calculé]** arithmétique vérifiée (Python, fractions exactes) ; **[dérivé]** raisonnement de l'auditeur.

Pièces : `work/EXTRAITS-S1.txt`, `work/EXTRAITS-S2.txt`, `work/EXTRAITS-S3.txt`, `work/S2-fulltext-alphaxiv.txt` (texte brut S2), empreintes dans `work/SHA256SUMS.txt` :

| fichier | sha256 |
|---|---|
| EXTRAITS-S1.txt | 04687f9bce54a2b3557ec4320b5ab56dc79df8dfc29487c44022e0b485f8b574 |
| EXTRAITS-S2.txt | 3fa3fbc77365281e3ab73d20f887f38c6c698664a93ebb138cc7ea51ff9d31cd |
| EXTRAITS-S3.txt | 61af1d2c49dbc18b2e8275d64f434ad23f5b027afd4793753a3137ffb12b5319 |
| S2-fulltext-alphaxiv.txt | e86b2e3dc2dfed55fdfc75f90a47b38b474158f6af49ca6fe1035a23cf10d5ca |

---

## 1. Coefficients du terme en ln a (partie électrique du Weyl) et exposants résommés

### 1.1 Conventions (S1 et S2 identiques)

- **κ** : [extrait] S1 éq. (5), p.2 : « g_{μν}(x) ≡ a²[η_{μν} + κh_{μν}(x)] ≡ a² g̃_{μν}(x) , κ² ≡ 16πG ». Même chose S2 éq. (11), p.3, et S2 p.2 : « κ² ≡ 16πG is used in place of Newton's constant ». Donc **κ_Woodard² = 16πG** (et non κ = 8πG).
- **h** : perturbation de la métrique **rescalée** g̃ = a⁻² g = η + κh (S1 (5) : « subtracting away the background from the conformally rescaled metric tensor »). h n'est pas la perturbation de la métrique physique g mais de g̃.
- **Quel Weyl** : [extrait] S1 éq. (14), p.3 : « the linearized, conformally rescaled Weyl tensor, C̃_{αβγδ} = C_{αβγδ}^{μν} × κh_{μν} + O(h²) ». La quantité C_{0i0j} de S1 (27) est calculée directement à partir de κh, donc c'est le Weyl de g̃, indices bas, en coordonnées conformes (η, x).
- **C^tree** : [extrait] S1 éq. (27), p.5 : « C_{0i0j} = ε_{ij} e^{ik·x} × −¼(∂₀² − k²)u(t,k) = −i√(2k³)/(4a) ε_{ij} e^{ik·x} × {1 − iκ²H²/π² (B − A/2)(aH/k) + 3κ²H²/π² C ln(a) + …} ≡ C^tree_{0i0j} × {…} ».
  - [dérivé, vérifié à la main] Avec u^tree = H/√(2k³)(1 + ikη)e^{−ikη} (η = −1/(aH)), on obtient (∂_η² − k²)u^tree = i√(2k³)/a · e^{ik/(aH)}, d'où exactement C^tree_{0i0j} = −i√(2k³)/(4a) ε_{ij} e^{ik·x} e^{ik/(aH)}. **C^tree porte a⁻¹** (composantes de C̃ en coordonnées conformes), et tend vers −i√(2k³)/(4a) ε_{ij}e^{ik·x} à temps tardif.
  - [dérivé] Pour la métrique physique : C_{abcd}[g] = a² C̃_{abcd} ∝ a ; composantes en repère orthonormé de g : a⁻⁴ · a² C̃ ∝ a⁻³ ; tenseur mixte C^a_{bcd} (invariant conforme) ∝ a⁻¹. Le crochet multiplicatif est le même dans tous les cas (voir §5).

### 1.2 Tableau des coefficients (H restauré, κ² = 16πG)

S1 donne la forme générale : [extrait] S1 (31), p.6 : « B_q = A_q/2 , C_q = 32/(3q) », avec S1 (12), p.3 : « q = 2¹⁰·3·5 , MCC scalars ; 2⁹·5 , fermions ; 2⁸·5 , photons ». Coefficient du ln a dans le Weyl = 3κ²H²C/π² = 32κ²H²/(qπ²).

| champ | q (S1 (12)) | coef. ln a, S1 via (27)+(31) [calculé] | coef. ln a, S2 [extrait] | exposant résommé, S2 [extrait] | γ (S2) [extrait] |
|---|---|---|---|---|---|
| scalaire MCC | 15360 | κ²H²/(480π²) | (44) p.9 : « 1 + κ²H²/(480π²) ln(a) » | (148) p.26 : « [a(t)]^{κ²H²/(480π²)} » | (147) : −κ²H²/(960π²) |
| Dirac | 2560 | κ²H²/(80π²) | (56) p.11 : « 1 + κ²H²/(80π²) ln[a] » | (151) p.27 : « [a(t)]^{κ²H²/(80π²)} » | (150) : −κ²H²/(160π²) |
| photon | 1280 | κ²H²/(40π²) | (65) p.12 : « 1 + κ²H²/(40π²) ln[a] » | (154) p.27 : « [a(t)]^{κ²H²/(40π²)} » | (153) : −κ²H²/(80π²) |
| (MMC, hors consigne, pour contraste) | « −2¹⁰·5/3 » (S1 p.6) | S1 (37) : −3κ²H²/(160π²) | (32) p.7 : −3κ²H²/(160π²) | (145) p.26 : « [a(t)]^{−3κ²H²/(160π²)} » | (144) : 3κ²H²/(320π²) |

- [calculé] S1 et S2 concordent exactement pour les trois champs conformes. Rapports MCC : Dirac : photon = 1 : 6 : 12.
- [calculé] Dans tous les cas, exposant = coefficient du ln a = −2γ, conformément à S2 (143) : « [∂/∂ln(μ) + 2γ] G⁽²⁾ = 0 » avec ln μ → ln a.
- S1 ne donne pas lui-même la forme résommée pour le Weyl des champs conformes ; il renvoie à [12] = S2 (« can be summed up using a variant of the renormalization group [12, 15] », S1 p.6). Les exposants proviennent de S2.
- [extrait] S1 (27) : pour les champs conformes, le terme en (aH/k) s'annule (« The relation between A_q and B_q demonstrates that the correction in Eq. (27) vanishes »). Pour MMC, il ne s'annule pas : S1 (37) « 1 + iκ²H²/(96π²) aH/k − 3κ²H²/(160π²) ln(a) ».

---

## 2. Conditions de validité énoncées

| condition | énoncé dans les sources |
|---|---|
| Logarithmes dominants | S1 p.7 [extrait] : « Recent work suggests that the leading logarithm corrections can be captured by a combining a variant of Starobinsky's stochastic formalism with a variant of the renormalization group ». S2 (146) suivi de : « The renormalization group does not explain the 1-loop results (35) for the gravitational slip because they are not leading logarithm. » La résommation RG ne vaut qu'au niveau leading log, et la substitution ln μ → ln a est une « variant », justifiée par S2 (9) et le texte qui suit (143), pas démontrée comme théorème. |
| Durée de la phase de Sitter | S2 p.26 [extrait] : « These results can even be resumed as long as the de Sitter phase persists ». S2 p.1 : la croissance de ln a « must eventually make these contributions of order one … it does mean that perturbation theory has broken down ». |
| Dépendance de jauge | S2 §5, p.32 [extrait] : les corrections de boucle de matière « (32-35), (44-46), (56-58) and (65-67) involve no graviton propagators and are completely gauge independent ». S1 p.7 : « Matter loop corrections provide an especially simple venue because they are gauge independent. » |
| État initial | S1 résumé : « subject to the usual ambiguity in the initial state ». S1 (19) : « for Bunch-Davies initial conditions ». S1 (25) : intégrales de t' = 0 à t (instant initial où a = 1). S1 Épilogue : savoir si δZ « can be absorbed into perturbative corrections to the initial state » reste ouvert. |
| Fond | S1 p.3 : (11) « valid on any cosmological background » pour MCC et fermions ; le photon n'est conformément invariant qu'en D = 4. Mais les modes et la résommation de S1/S2 sont calculés sur de Sitter exact (ε = 0). |
| Régime temporel | S1 (26) : forme « late time », développement en puissances de k/(aH), donc valable pour aH ≫ k (mode hors horizon). |

---

## 3. S3 : normalisation de la trace anomale et signe de ⟨T_ij⟩

- [extrait] S3 éq. (2.3)-(2.8), p.7 : « g^{ij}⟨T_{ij}⟩ = cF − aG + d∇²R », « F = C_{ijkl}C^{ijkl} », « c = 1/(120(4π)²) (N_S + 6N_F + 12N_V) », « a = 1/(360(4π)²)(N_S + 11N_F + 62N_V) », « d = 1/(180(4π)²)(N_S + 6N_F − 18N_V) », « N_S is the number of real scalar fields, N_F the number of Dirac fermions and N_V the number of vector fields ».
- **Remarque de nommage** : S3 appelle **c** le coefficient du carré de Weyl (la consigne le nomme b). Ci-dessous b ≡ c_{S3}.
  - scalaire réel conforme : b_S = 1/(120(4π)²) = 1/(1920π²) [calculé]
  - fermion de Dirac : b_F = 6/(1920π²) = 1/(320π²)
  - vecteur : b_V = 12/(1920π²) = 1/(160π²)
- Fermions : S3 compte des **Dirac** (p.7 : « 4N² Majorana fermions, which is equivalent to 2N² Dirac fermions »).
- Signe de ⟨T_ij⟩ : [extrait] S3 (1.1)-(1.3), p.3 : « exp(−W[g]) = ∫d[φ] exp(−S[φ;g]) », « R_ij − ½Rg_ij = 8πG⟨T_ij⟩ », « ⟨T_ij⟩ = −2/√−g δW/δg^{ij} ». Les calculs sont en signature **euclidienne** (p.5 ; (2.12) : « ⟨T_σσ⟩ = −ρ … The minus sign … arises because we are considering Euclidean signature »). Convention de positivité : « a positive trace anomaly permits a de Sitter solution » (p.4). S3 utilise G avec 8πG dans (1.2), ce qui fixe naturellement κ = 8πG.

---

## 4. Conversion

### 4.1 En unités de G (H = 1) [calculé]

κ² = 16πG ⇒ κ²/(Nπ²) = 16G/(Nπ).

| champ | Γ (coef. de ln a, = exposant résommé) |
|---|---|
| scalaire MCC | κ²/(480π²) = **G/(30π)** |
| Dirac | κ²/(80π²) = **G/(5π)** |
| photon | κ²/(40π²) = **2G/(5π)** |
| (MMC) | −3κ²/(160π²) = −3G/(10π) |

### 4.2 Sous la forme Γ = n b κ, κ = 8πG, b normalisé S3 [calculé]

| champ | b (S3) | bκ | Γ | **n** |
|---|---|---|---|---|
| MCC | 1/(1920π²) | G/(240π) | G/(30π) | **8** |
| Dirac | 1/(320π²) | G/(40π) | G/(5π) | **8** |
| photon | 1/(160π²) | G/(20π) | 2G/(5π) | **8** |
| (MMC, non conforme) | 1/(1920π²) (si l'on prend le seul terme C²) | G/(240π) | −3G/(10π) | −72 |

**Les trois n sont égaux : n = 8** (avec H restauré : Γ = 8 b κ H² = 4 b κ_W² H²).

### 4.3 Pourquoi l'égalité n'est pas une coïncidence [dérivé]

- [calculé] Les coefficients de contre-terme de Weyl de S2 coïncident avec le b de S3 : c₂^{MCC} = 1/(2⁷·3·5·π²) = 1/(1920π²) = b_S ; c₂^{Dirac} = 1/(2⁶·5·π²) = 1/(320π²) = b_F ; donc c₂ = b · μ^{D−4}/(D−4) pour les champs conformes (c₁ = 0).
- Avec S2 (142) en D = 4 et c₁ = 0 : δZ = −4c₂κ_W²H², d'où γ = ∂ln(1+δZ)/∂ln μ² = −2bκ_W²H², puis Γ = −2γ = 4bκ_W²H² = 8bκH². La formule (142) est validée indépendamment par S2 (181) pour les gravitons (23/160 retrouvé [calculé]).
- Donc n = 8 est universel pour tout champ conforme : l'exposant est fixé par le seul coefficient du pôle de Weyl, qui est aussi le coefficient b de la trace anomale. Les rapports 1 : 6 : 12 de S1 (q) et de S3 (c) sont les mêmes.
- Le MMC (n = −72) sort de ce schéma : son exposant est dominé par c₁ (contre-terme R²), absent pour les champs conformes.

---

## 5. Le facteur s'applique-t-il au Weyl rescalé W = C/Ω (Ω ∝ 1/a) ?

**Réponse : oui pour le facteur relatif, mais pas pour le comportement absolu, qu'il faut recalculer à partir de C^tree ∝ a⁻¹.** [dérivé]

1. **Identification géométrique.** S1/S2 définissent g = a² g̃, c'est-à-dire g̃ = Ω² g avec Ω = 1/a exactement (H = 1, a = −1/η). g̃ = η + κh est donc précisément la métrique conformément compactifiée de la carte de de Sitter (Minkowski plus perturbation), et 𝓘⁺ est en η → 0⁻, soit a → ∞.
2. **Le facteur est une fonction scalaire du fond.** Passer de C̃_{0i0j} au Weyl physique, au tenseur mixte ou au Weyl rescalé revient à multiplier par une puissance de a (fond seul, la perturbation κh n'est pas touchée). Le crochet {1 + Γ ln a + …}, ou a^Γ, est un **rapport** C/C^tree. Il est donc inchangé : W = W^tree × {1 + Γ ln a + …}.
3. **Ce qui change, c'est W^tree.** Avec la convention de Penrose/Friedrich W^a_{bcd} = Ω⁻¹C^a_{bcd} et C^a_{bcd}[g] = C̃^a_{bcd}[g̃] (invariance conforme du tenseur mixte) : W = a · C̃^a_{bcd}. Comme C^tree_{0i0j} ∝ a⁻¹ (§1.1), **W^tree → constante finie non nulle** à 𝓘⁺ (≈ ∓i√(2k³)/4 ε_ij e^{ik·x}). C'est cohérent avec la régularité du Weyl rescalé à 𝓘⁺ au niveau des arbres.
4. **Conséquence à une boucle.** W = W^tree(1 + Γ ln a) avec ln a = −ln(−Hη) → ∞ : divergence **logarithmique** de W à 𝓘⁺ pour tout Γ ≠ 0. Version résommée : W ∝ a^Γ = (−Hη)^{−Γ}, ce qui diverge à 𝓘⁺ pour Γ > 0 (les trois champs conformes) et s'annule pour Γ < 0 (MMC). Si l'on se trompait sur C^tree (par exemple en prenant la composante orthonormée physique ∝ a⁻³), on conclurait à tort W ∝ a⁻² → 0 : la puissance portée par C^tree décide de tout.
5. **Réserves** :
   - Le placement des indices dans la définition de W change la puissance absolue (Ω⁻¹C_{abcd}[g] ∝ a³ C̃ ∝ a² au niveau des arbres), mais pas le rapport. Il faut fixer la convention W^a_{bcd} = Ω⁻¹C^a_{bcd} (ou de manière équivalente avec indices abaissés par g̃).
   - Le « + … » de S1 (27) contient des termes non spécifiés. Pour MMC, le terme ∝ aH/k (S1 (37)) domine ln a et ferait croître W comme a. S1 (39)-(41) l'interprètent comme un décalage δH, pas comme une croissance physique.
   - La limite a → ∞ exige une phase de Sitter de durée infinie, ce qui sort du « as long as the de Sitter phase persists » (S2) et du régime leading log. Le résultat à 𝓘⁺ est une **extrapolation** de la résommation RG, pas un énoncé des sources.
   - La correction porte sur C, pas sur h : selon S1 (26), κ²u₁ reste borné et le ln a apparaît dans un terme ∝ (k/aH)³ de u, qui devient dominant après l'action de (∂₀² − k²).
   - [dérivé] À l'ordre linéaire, le Weyl de la perturbation sur un fond conformément plat est invariant de jauge (le Weyl du fond est nul), ce qui va dans le même sens que l'indépendance de jauge énoncée par S2 §5.

---

## 6. Ambiguïtés de convention susceptibles de changer n ou son signe

| # | ambiguïté | effet |
|---|---|---|
| 1 | κ : Woodard κ² = 16πG ; consigne κ = 8πG | Si l'on écrivait Γ = n' b κ_W² : n' = 4. Si l'on confondait κ_W² avec 8πG : n = 16. Le facteur 2 est la principale source d'erreur. |
| 2 | Comptage des fermions (Dirac ou Weyl/Majorana) | S1, S2 et S3 utilisent tous des Dirac : n = 8. Si b était normalisé par fermion de Weyl ou de Majorana (3 au lieu de 6) avec Γ de Dirac, n_F = 16 et l'égalité des trois n serait brisée. |
| 3 | Signe de l'anomalie | S3 : euclidien, ⟨T_ij⟩ = −2/√g δW/δg^{ij}, trace = +cF − aG + d∇²R avec c > 0. D'autres conventions (par exemple signature (+,−,−,−), autre signe de T_ab, écriture « −(1/2880π²)[…] ») inversent le signe affiché de b. n changerait alors de signe sans changement physique. Il faut fixer b > 0 pour le terme C² au sens de S3. |
| 4 | Signe du ln dans la relation RG | S2 (9) : contre-terme ∝ −ln(μa/2H). Le signe de Γ dépend de la chaîne c₂ = +b μ^{D−4}/(D−4) → γ = −2bκ_W²H² → Γ = −2γ. Inverser la convention de (143) inverserait n. |
| 5 | Origine de ln a et choix de μ | ln(μa/2H) : changer μ ou l'instant initial (a = 1 à t = 0 dans S1 (25)) décale ln a d'une constante. La normalisation de C^tree change, mais pas Γ ni n. |
| 6 | Unités | Γ est sans dimension seulement avec H : Γ = n b κ H². Avec H = 1 implicite, une confusion avec H = H₀ ou H_inf change la valeur numérique de Γ, pas n. |
| 7 | Normalisation de C_{0i0j} (facteur ¼ dans S1 (27)) | Sans effet sur le rapport, donc sans effet sur n. |
| 8 | Coquilles internes à S2 (relevées, sans effet sur n pour les trois champs) | (a) S2 (153) imprime c₂^{photon} = 1/(2²·5·π²) = 1/(20π²), incompatible avec « 12 times » et avec γ = −κ²H²/(80π²). La valeur cohérente est 1/(2⁵·5·π²) = 1/(160π²) = b_V [calculé : 1/20 donnerait γ = −1/10]. (b) S2 (57) affiche « − κ²H²/(80π²) ln[aHr] » pour le potentiel du Dirac, alors que (152) donne un exposant positif et que le texte dit que les fermions « strengthen gravity ». Le signe de (57) est vraisemblablement une coquille. (c) S2 §4.2.2 intitulé MCC mais écrit « massless, minimally coupled scalar ». (d) MMC : avec le c₁ = 1/(2⁷·3·π²) imprimé en (144), la formule (142) donne γ = 29κ²H²/(960π²), et non 3κ²H²/(320π²). Il faudrait c₁ = 1/(2⁷·3²·π²). Le Weyl MMC (−3/160) est toutefois confirmé indépendamment par S1 (36)-(37). |
| 9 | Champ MMC | Non conforme, il n'entre pas dans la forme Γ = n b κ (n = −72 n'a pas de sens universel, la contribution c₁ ∝ R² domine). |

---

## Conclusion

- Coefficients du ln a dans C_{0i0j} (κ² = 16πG) : MCC κ²H²/(480π²), Dirac κ²H²/(80π²), photon κ²H²/(40π²). S1 (via C_q = 32/(3q)) et S2 concordent. Les exposants résommés (S2 (148), (151), (154)) sont égaux à ces coefficients.
- En unités de G (H = 1) : G/(30π), G/(5π), 2G/(5π).
- Avec b = coefficient C² de S3 (c dans S3, fermions de Dirac) et κ = 8πG : **n = 8 pour les trois champs**, ce qui s'explique structurellement par c₂^{Woodard} = b et Γ = −2γ = 8bκH².
- h est la perturbation de la métrique rescalée et C^tree (composantes de C̃) porte a⁻¹. Le facteur multiplicatif passe tel quel au Weyl rescalé W = Ω⁻¹C^a_{bcd}, mais comme W^tree → constante, W diverge alors logarithmiquement (puis en a^Γ) à 𝓘⁺. Cette conclusion est une extrapolation hors du domaine énoncé (phase de Sitter finie, leading log, perturbatif).
