# RAPPORT ZA-1 : lecture aveugle de arXiv:2501.01972

Auditeur froid, sans connaissance du travail anterieur. Source lue via alphaXiv (get_paper_content fullText, puis answer_pdf_queries ; les deux retours sont identiques). Date de lecture : 2026-10-12.

Etiquettes : [extrait] citation verbatim (numero d'equation ou page PDF alphaXiv, page 1 = titre) ; [calcule] resultat sympy ; [derive] deduction de l'auditeur a partir du texte, non ecrite telle quelle dans la source.

Pieces : `work/extraits_verbatim_2501.01972.txt` (extraits E01 a E14), `work/conversion_za1.py`, `work/conversion_za1.out`, `work/SHA256SUMS.txt`.

| Fichier | sha256 |
|---|---|
| extraits_verbatim_2501.01972.txt | c852eee2d08b601581b0e9cd8072dafa5409a77e4730cd00c1e9337ca7707906 |
| conversion_za1.py | 09107dc29527a4974f0276e36c6cd8c2e3543a5d6d5db169a8630a02f5c601d6 |
| conversion_za1.out | 278c38cdd2ddbec5d6c014b60147e1d2ffc4ddae8a75f01a3b5892f6c59ec463 |

---

## 1. Identification

- Titre [extrait, p.1] : « Resumming Fermion Loops for Inflationary Gravity »
- Auteurs [extrait, p.1] : A. J. Foraci et R. P. Woodard, Department of Physics, University of Florida, Gainesville.
- Date [extrait, p.1] : « arXiv:2501.01972v1 [gr-qc] 27 Dec 2024 », rapport interne UFIFT-QG-24-09.
- Type : prepublication (v1 arXiv). Le texte recupere ne porte aucune mention de journal, de DOI ni d'acceptation. Je n'ai pas d'information independante sur une publication ulterieure.
- Resume [extrait E01, p.1] : « We compute the 1-loop contribution to the graviton self-energy from a loop of massless fermions on a general cosmological background. The result is used to quantum-correct the linearized Einstein equation on de Sitter background and work out 1-loop corrections to gravitational radiation and to the response to a point mass. The renormalization group is employed to sum these to all orders for as long as the de Sitter phase persists. »
- Longueur : 10 pages PDF, 47 equations, 30 references.

## 2. Correction a une boucle du Weyl electrique C_0i0j

Convention de κ [extrait E02, eq. (2)] : « g_{μν}(x) ≡ a² g̃_{μν} ≡ a² [η_{μν} + κ h_{μν}(x)] , κ² ≡ 16πG ». Donc κ² = 16πG, soit κ² = 2 κ_P² avec κ_P² = 8πG.

(a) Fermion de Dirac sans masse [extrait E07, eq. (35)] :

    C_{0i0j}(x) → C^tree_{0i0j}(x) { 1 + κ²H²/(80π²) ln(a) + ... }   (35)

La source ne resout pas l'equation (28) pour Dirac de maniere independante ; elle transfere le resultat de Maxwell [extrait E07, p.7] : « Because the massless Dirac contribution (32) is 1/2 times the contribution from electromagnetism [6], we can read off the 1-loop solutions for Dirac from those for Maxwell. Hence the 1-loop correction to the electric components of the Weyl tensor for plane wave gravitational radiation is [8], ». La self-energie Schwinger-Keldysh de Dirac est l'eq. (32), prefacteur −κ²/(2⁹·5·π³).

(b) Scalaire conformement couple (MCC) [extrait E13, eq. (46)] :

    C_{0i0j} = C^tree_{0i0j} { 1 + κ²H²/(480π²) ln(a) + ... }   (46)

obtenu par le rapport [extrait E13, p.9] : « The Schwinger-Keldysh result is 1/12 times that of electromagnetism [30] », self-energie eq. (45), prefacteur −κ²/(2¹⁰·3·5·π³). Le rapport Dirac/MCC des prefacteurs (32)/(45) vaut 6 [calcule], coherent avec 80 × 6 = 480.

(c) Photon : la source ne donne PAS d'equation explicite pour le photon ; elle renvoie a [6] et [8] (Wang-Woodard 2015, Foraci-Woodard arXiv:2412.11022). Elle en dit deux choses :
- [extrait E07] la contribution Dirac est « 1/2 times the contribution from electromagnetism », et [extrait E13] la contribution MCC est « 1/12 times that of electromagnetism » ;
- [extrait E12, p.8] : « We could not assume that the primitive contribution from photons would be the same as in flat space because electromagnetism is only conformally invariant for D = 4 dimensions. This shows up in the photon propagator on de Sitter background depending on the scale factor and the Hubble constant for general D [28]. »

[derive] Par le rapport 1/2, le coefficient photon implicite est κ²H²/(40π²) ln(a) ; il n'est pas ecrit dans la source.

## 3. Forme resommee et methode

Forme resommee [extrait E10, eq. (42)] : C_{0i0j}(x) → C^tree_{0i0j}(x) × [a(t)]^{κ²H²/(80π²)} ; pour MCC [extrait E13, eq. (46)] : × [a(t)]^{κ²H²/(480π²)}. C'est une puissance du facteur d'echelle, l'exposant etant exactement le coefficient du ln a a une boucle (exponentiation du logarithme).

Methode, pas a pas (toutes les pieces aux extraits E09 et E10, p.7 et p.8) :

1. Lien μ ↔ a : eq. (38), identite de reecriture de la self-energie renormalisee (27) : « 4π² ln(aa') iδ⁴(x−x') + ∂²[ln(μ²Δx²)/Δx²] = 4π² ln(μ²aa') iδ⁴(x−x') + ∂²[ln(Δx²)/Δx²] ». Le ln(aa') et le ln(μ²) sont rassembles en ln(μ²aa') devant le terme local.
2. Renormalisation de champ du graviton : eq. (39), « δZ = D[2(D−1)c₁ − c₂] κ²H² », combinaison importee de [27] (scalaire minimalement couple) et de [8] (electromagnetisme).
3. Fonction γ : eq. (40), « γ ≡ ∂ln(1+δZ)/∂ln(μ²) = −κ²H²/(160π²) », avec c₁ = 0 et c₂ de l'eq. (26). Pas de fonction β : « The beta function vanishes to the order we are working ».
4. Equation de Callan-Symanzik : eq. (41), « [∂/∂ln(μ) + β_G ∂/∂G + 2γ] G⁽²⁾ = 0 », en traitant C_{0i0j} et Ψ comme des fonctions de Green a 2 points.
5. Substitution : « we can replace the derivative with respect to ln(μ) in equation (41) by a derivative with respect to ln(a) ». [derive] Avec β_G = 0, l'equation devient ∂G/∂ln a = −2γ G, de solution G ∝ a^{−2γ} = a^{κ²H²/(80π²)}, ce qui reproduit (42).

Phrase d'introduction [extrait E09, p.7] : « During a prolonged period of de Sitter inflation, the secular 1-loop corrections in (35) and (36) must eventually overwhelm the tree order result. At this point perturbation theory breaks down and one must invoke a nonperturbative resummation scheme to work out what happens. » puis : « This suggests that the secular logarithms can be resummed using a variant of the renormalization group. »

Phrase de conclusion [extrait E10, p.8] : « At this point one sees that the renormalization group explains the secular factors in expressions (35) and (36) and even permits their resummation, » suivie de (42)-(43). Dans les conclusions [extrait E11, p.8] : « And we were able to resum the results using a variant of the renormalization group (42-43). » Pour MCC [extrait E13] : « In the same way we can solve the linearized Einstein equation (28) and resum the results using the renormalization group, ».

Statut de la resommation : la source ne la DEMONTRE pas et ne la VERIFIE pas a un ordre superieur (aucun calcul a deux boucles, aucun terme en ln²a n'est produit ni compare). Elle la PRESENTE comme un procede, avec un vocabulaire d'hypothese et d'analogie : « suggests », « a variant of the renormalization group », « one can consider ... to be 2-point Green's functions », « explains ... and even permits ». La justification avancee est double : (i) l'identite (38) qui lie μ et a dans le terme local ; (ii) la coincidence entre le coefficient a une boucle et −2γ (« the renormalization group explains the secular factors »). Le mot « variant » est utilise trois fois (p.2, p.7, p.8) ; le terme « conjecture » ou « proof » n'apparait pas.

## 4. Conditions de validite declarees

Ce que la source DIT :
- Duree de la phase de Sitter : « for as long as the de Sitter phase persists » (resume) ; « During a prolonged period of de Sitter inflation » (p.7). Fond de Sitter exact : a = e^{Ht} = −(Hη)^{−1}, H constant [extrait E06, eq. apres (33)]. La self-energie (32)/(45) est valable pour tout a(t) ; la resolution et la resommation sont specifiques a de Sitter.
- Logarithmes dominants : la source parle de « secular logarithms » et de « secular 1-loop corrections » ; elle n'emploie pas l'expression « leading logarithm » et ne distingue pas ln a dominant / sous-dominant. [derive] La resommation RG ne retient par construction que la tour ln^n a ; la source ne le dit pas.
- Etat : vide |Ω₀⟩ du propagateur fermionique plat (eq. (8)) ; aucune mention explicite de Bunch-Davies. Le mode fonction d'arbre (30) est le mode de Bunch-Davies standard [derive].
- Prescription in-in : explicitement Schwinger-Keldysh [extrait E05, p.6] : « Employing the in-out self-energy (27) in this equation would be inappropriate because it is neither real nor causal. ... employing the in-in, or Schwinger-Keldysh, formalism [22–24]. » Resultat eq. (32)-(33), avec fonction causale f_B a support θ(Δη−Δr).
- Jauge : jauge de Lorentz locale fixee par vierbein symetrique [extrait E14, p.3] ; pour le graviton, h_{μν} defini par rescaling conforme (eq. (2)), ondes planes transverses sans trace purement spatiales (eq. (29)), potentiels Ψ, Φ dans la metrique perturbee (31). Aucune fixation de jauge gravitationnelle n'est discutee (le self-energie fermionique a une boucle n'en requiert pas ; l'operateur de Lichnerowicz (34) est utilise sans terme de jauge).
- Regularisation / renormalisation : dimensionnelle + BPHZ, contre-termes R² et C² (eq. (7)), c₁ = 0, c₂ eq. (26) ; echelle μ.
- Ordre de validite de β : « vanishes to the order we are working ».

Ce que la source NE discute PAS :
- Independance de jauge : non discutee. Aucune phrase sur la dependance de jauge de (35)-(37) ni des exposants (42)-(43).
- Limite a → ∞ : non discutee. La forme a^{κ²H²/80π²} est ecrite sans commentaire sur son comportement asymptotique ni sur sa compatibilite avec la fin de la phase de Sitter.
- Nombre maximal d'e-folds : non discute. Aucune valeur numerique d'e-folds, aucun N_max, aucune estimation de 80π²/(κ²H²).
- Echelle de rupture : seulement qualitative : « must eventually overwhelm the tree order result. At this point perturbation theory breaks down ». Aucune echelle, aucun critere quantitatif.
- Egalement absents : incertitude sur l'etat initial, dependance a l'echelle μ apres resommation, terme constant −κ²H²/(80π²) du slip (37) laisse hors resommation, effets de masse.

## 5. Conversion en unites b κ_P² H²

Definitions imposees par le prompt : κ_P² = 8πG ; b = (N_S + 6N_F + 12N_V)/(120(4π)²).

[calcule] κ² (source) / κ_P² = 2. Donc coef_source × κ²H² = 2 coef_source × κ_P²H².

| Espece | coefficient du ln a (source) | en κ_P²H² | b (une espece) | n |
|---|---|---|---|---|
| Dirac (N_F = 1) | κ²H²/(80π²) [eq. 35] | κ_P²H²/(40π²) | 1/(320π²) | **8** |
| Scalaire conf. (N_S = 1) | κ²H²/(480π²) [eq. 46] | κ_P²H²/(240π²) | 1/(1920π²) | **8** |
| Photon (N_V = 1) | κ²H²/(40π²) [derive du rapport 1/2, E07] | κ_P²H²/(20π²) | 1/(160π²) | **8** |

Resultat : n = 8 pour les trois especes, les n sont egaux. Le coefficient du ln a de la source s'ecrit uniformement 8 b κ_P² H², soit, pour N_S scalaires, N_F Dirac, N_V vecteurs, coefficient = (N_S + 6N_F + 12N_V) κ_P² H²/(240π²).

Controle de coherence interne [calcule] : 12 × (coefficient MCC) = 2 × (coefficient Dirac) = coefficient photon, conforme aux deux rapports « 1/2 » et « 1/12 » enonces par la source. Le n du photon repose sur ces rapports, pas sur une equation de la source.

Script : `work/conversion_za1.py` (sympy, execute avec python3 -I), sortie `work/conversion_za1.out`.

## 6. Potentiel newtonien

Une boucle, Dirac [extrait E08, eq. (36)] :

    Ψ(t,r) = GM/(ar) { 1 + κ²/(120π² a² r²) + κ²H²/(80π²) ln(aHr) + ... }   (36)

Slip [eq. (37)] : Ψ + Φ = GM/(ar) { 0 + κ²/(240π² a² r²) − κ²H²/(80π²) + ... } ; le terme en κ²H² du slip est une constante, pas un logarithme.

Forme resommee [extrait E10, eq. (43)] : Ψ(t,r) → GM/(a(t) r) × [a(t)Hr]^{κ²H²/(80π²)}.

Scalaire MCC [eq. (47)] : Ψ = GM/(ar){1 + κ²/(720π² a²r²) + κ²H²/(480π²) ln(aHr) + ...} → GM/(ar) × [a(t)Hr]^{κ²H²/(480π²)}.

Meme exposant que le Weyl electrique ? OUI, pour chaque espece : 80π² pour Dirac (eq. 42 vs 43), 480π² pour MCC (eq. 46 vs 47). La difference est l'argument : a(t) pour C_{0i0j}, a(t)Hr pour Ψ (la correction d'arbre κ²/(a²r²) n'est pas resommee et disparait de la forme (43)). [derive] L'egalite des exposants decoule de la methode elle-meme : les deux quantites sont traitees comme des fonctions de Green a 2 points soumises a la meme γ ; la source le dit en ces termes (« One can consider both the Weyl tensor (35) and the Newtonian potential (36) to be 2-point Green's functions »).

## 7. Observations de l'auditeur

- La source est courte et explicite sur le fait que les resultats de Sitter (35)-(37) sont lus a partir des references [6] et [8] par un facteur de proportionnalite (1/2), et non recalcules.
- L'exposant resomme est exactement le coefficient a une boucle ; aucune verification independante a deux boucles n'est offerte, aucune estimation de domaine de validite n'est fournie.
- La conversion montre une structure universelle n = 8 avec le coefficient de Weyl de l'anomalie de trace, ce qui est coherent avec le fait que seul le contre-terme C² intervient (c₁ = 0) pour les trois champs conformes.
