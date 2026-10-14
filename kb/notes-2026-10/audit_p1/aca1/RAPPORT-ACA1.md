# RAPPORT ACA-1 : lecture aveugle d'enonces de TQC en espace courbe (etats Hadamard, propagation, positivite)

Auditeur froid, isole. Date : 2026-10-13. Perimetre de lecture : /home/claude/audit_p1/aca1/ uniquement. Sources lues via alphaXiv (answer_pdf_queries) : S1 = arXiv:1412.5945v3 (Khavkine, Moretti), S2 = arXiv:0903.1021v1 (Sanders). Metadonnees : WebFetch sur link.springer.com (une page lue, deux refusees par limitation de debit), ScienceDirect et Project Euclid refuses ; aucun contournement tente.

Etiquettes : [extrait] = citation verbatim avec numero d'enonce ou de page ; [derive] = raisonnement de l'auditeur a partir des seuls extraits. Les extraits complets sont dans work/ (voir empreintes en section 8). Convention de transcription : le symbole « k ⊳ 0 » (covecteur futur non nul) est rendu « k . 0 » par l'extracteur PDF ; je le retablis en ⊳.

---

## 1. S1 : definitions et theoremes releves (tache 1)

### 1.1 Definition de l'etat Hadamard

[extrait] S1, Definition 15, p. 38 :
« With M four dimensional, we say that a (not necessarily quasifree) state ω on A(M) and its two point function ω_2 are Hadamard if ω_2 ∈ D'(M × M) and every point of M admits an open normal neighborhood C where ω_2(x, y) − H_{0+}(x, y) = w(x, y) for some w ∈ C^∞(C × C). (60) »

[extrait] Contexte, p. 37 : « In the rest of the chapter we only consider a four dimensional spacetime ». H_{0+} est la parametrix de Hadamard (58) construite dans un voisinage convexe, qui « distributionally satisfies KG equation in both arguments up to jointly smooth functions of x and y » (p. 38, eq. (59)).

[derive] Points saillants des hypotheses : (i) dimension 4 ; (ii) l'objet est un ETAT ω sur A(M) (donc positif) ET sa fonction a deux points ω_2 ; la definition est locale (voisinages normaux) ; (iii) « not necessarily quasifree ». S1 precise en Remark 18 (4) que cette definition est la notion LOCALE ; la notion globale (Definition 3.4 de [57], Kay-Wald [45]) n'est pas utilisee par S1 : « We note that we do not make use of the global Hadamard condition » (p. 48).

### 1.2 Theoreme d'equivalence (Theorem 9)

[extrait] S1, Theorem 9 (« Radzikowski theorem »), p. 48-49 :
« For a 4-dimensional globally hyperbolic (time oriented) spacetime M and referring to the unital ∗-algebra of Klein-Gordon quantum field A(M) with m^2, ξ ∈ R arbitrarily fixed, let ω be a state on A(M), not necessarily quasifree.
(a) The following statements are equivalent,
(i) ω is Hadamard in the sense of Def. 15,
(ii) the wavefront set of the two-point function ω_2 has the Hadamard form on M or equivalently, it satisfies the microlocal spectrum condition on M: WF(ω_2) = { (x, y, k_x, −k_y) ∈ T*M^2 \ 0 | (x, k_x) ∼ (y, k_y), k_x ⊳ 0 } =: H. (76)
[...]
(b) If ω' is another Hadamard state on A(M), then ω_2 − ω'_2 ∈ C^∞(M × M, C).
Proof. (a) Suppose that ω satisfies (i), then it is globally Hadamard in the sense of [57] due to Theorem 9.2 in [58]. Theorem 5.1 in [57] implies that (ii) holds. Conversely, if (ii) is valid, Theorem 5.1 in [57] entails that ω is globally and thus locally Hadamard so that (i) holds true. (b) immediately arises from Theorem 4.3 in [58]. »

[extrait] Note 11, p. 49 : « Results in [57, 58] are stated for ξ = 0 in KG operator, however they are generally valid for m^2 replaced by a given smooth function, as specified at the beginning of p. 533 in [57]. »

[derive] Hypotheses exactes : dimension 4 ; espace-temps globalement hyperbolique oriente en temps ; l'objet est un ETAT sur A(M) (positivite incluse par definition d'un etat), pas une simple bidistribution ; quasi-libre NON requis ; m^2, ξ reels arbitraires. La partie (b) suppose que ω et ω' sont tous deux des etats Hadamard sur A(M) (sur tout M), et conclut a la lissite globale de la difference sur M × M. La preuve de (b) renvoie integralement a Radzikowski-Verch [58], Theorem 4.3 ; S1 ne la redemontre pas.

Tableau de synthese des hypotheses :

| Enonce | Dimension | Objet | Quasi-libre ? | Positivite ? | Conclusion |
|---|---|---|---|---|---|
| Def. 15 | 4 | etat ω et ω_2 | non requis | oui (etat) | notion locale |
| Thm 9 (a) | 4 | etat sur A(M) | non requis | oui (etat) | Def. 15 ⇔ WF(ω_2) = H |
| Thm 9 (b) | 4 | deux etats Hadamard sur A(M) | non requis | oui (etats) | ω_2 − ω'_2 ∈ C^∞(M × M) |
| Prop. 16 (b) | n ≥ 2 | etat ω avec ω_2 ∈ D'(M × M) | non requis | oui (etat), mais voir Rem. 23 | WF Hadamard sur O ⇒ sur M |
| Rem. 23 | n ≥ 2 | ω_2 ∈ D'(M × M) bisolution a lisse pres | sans objet | NON | idem Prop. 16 (b) |

### 1.3 Propagation de la forme microlocale de Hadamard (Proposition 16 (b))

[extrait] S1, Proposition 16, p. 50 :
« Consider a state ω on A(M), with ω_2 ∈ D'(M × M), where M is a (time oriented) globally hyperbolic spacetime with dimension n ≥ 2. The following facts hold.
(a) If WF(ω_2) has the Hadamard form, then M ∋ x ↦ ω_2(x, f) is smooth for every f ∈ C^∞_0(M).
(b) If WF(ω_2|_{O×O}) has the Hadamard form on O, where O is an open neighborhood of a smooth spacelike Cauchy surface Σ of M, then WF(ω_2) has the Hadamard form on M. »

[extrait] Debut de la preuve de (b), p. 50 : « The 2-point function ω_2(x, y) is a bisolution of the Klein-Gordon operator P = □_M + m^2 + ξR, as in (8). So the value of ω_2(f, g), for f, g ∈ C^∞_0(M), depends on the arguments only up to the addition of any term from P[C^∞_0(M)]. [...] we can define an S ∈ D'(O × M) such that the corresponding operator maps S : C^∞_0(M) → C^∞_0(O) and we have the identity ω_2 = S^t ∘ ω_2 ∘ S. Then, using the result of Theorem 8 on the composition of kernels and the fact that ω_2 has the Hadamard form on O, we can show that ω_2 has the Hadamard form on all of M. »

[extrait] Noyau de S, eq. (78), p. 51 : « S(x, y) = δ(x, y) − P_x[χ_+(x)E^−(x, y) + χ_−(x)E^+(x, y)] », avec χ_± partition de l'unite adaptee a Σ (supports dans J^+(Σ_−) et J^−(Σ_+)).

[extrait] Fin de la preuve, p. 51 : « By the Hadamard condition on O, we have k_x ⊳ 0 and k_y ⊳ 0. On the other hand, the condition of being a point in F_± induces the condition that either both k_y ⊳ 0 and k_z ⊳ 0 or both k_y ⊲ 0 and k_z ⊲ 0. Combining the two conditions we find that k_z ⊳ 0, and hence that (x, z, k_x, k_z) ∈ H'_M. This concludes the proof. »

[derive] Hypotheses exactes de Prop. 16 (b) telles qu'enoncees : dimension n ≥ 2 (pas seulement 4) ; M globalement hyperbolique oriente en temps ; ω est un etat sur A(M) (donc positif, et ω_2 est une bisolution de KG par la relation (8) de l'algebre) ; Σ surface de Cauchy spatiale lisse de M ; O voisinage ouvert de Σ ; hypothese microlocale sur O × O seulement. Observation importante : la preuve etablit en fait l'INCLUSION WF(ω_2) ⊂ H (« WF(ω_2) = WF(S^t ∘ ω_2 ∘ S) ⊂ H »), l'egalite n'est pas demontree dans ce passage. Les seuls ingredients utilises sont : (1) ω_2 bisolution (pour ω_2 = S^t ∘ ω_2 ∘ S), (2) les fronts d'onde de δ, E^± (Prop. 15) et le theoreme de composition des noyaux (Theorem 8), (3) l'orientation des covecteurs sur O. La positivite n'intervient nulle part dans la preuve ecrite.

### 1.4 Affaiblissement (Remark 23) : positivite ou simple bisolution ?

[extrait] S1, Remark 23, p. 51 :
« With an elementary re-adaptation, statement (b) holds true weakening the hypotheses, only requiring that ω_2 ∈ D'(M × M) and that it satisfies KG equation in both arguments up to smooth functions r, l ∈ C^∞(M × M, C), i.e. P_x ω_2(x, y) = l(x, y), P_y ω_2(x, y) = r(x, y). »

[derive] Reponse a la question posee : d'apres Remark 23, la propagation de la forme microlocale de Hadamard (Prop. 16 (b)) N'EXIGE PAS la positivite de l'etat. Elle exige seulement que ω_2 soit une distribution sur M × M qui est bisolution de KG a fonctions lisses pres. Le mot « state » dans l'enonce de Prop. 16 est donc une commodite de presentation et non une hypothese utilisee. Ce que la Remark 23 ne dit pas et qu'il faut noter : (i) elle conclut a « statement (b) », donc formellement a « WF(ω_2) has the Hadamard form on M », mais la preuve ne fournit que l'inclusion WF(ω_2) ⊂ H ; (ii) rien n'est dit sur le passage de l'inclusion microlocale a la Definition 15 geometrique pour une bidistribution non positive, le Theorem 9 n'etant enonce que pour des etats.

---

## 2. S1 : la lacune de Radzikowski 1996 et l'attribution de la propagation (tache 2)

### 2.1 La lacune

[extrait] S1, Remark 23, p. 51 : « In this form, it closes a gap[12] present in the proof of the main result of [57], Theorem 5.1 (the fact that 1 implies 3), and proves the statement on p. 548 of [57] immediately after the proof of the mentioned theorem. It should be mentioned that the same gap had been previously explicitly identified and filled in the work of Sahlmann and Verch [61]. These authors merged the partial proof of Radzikowski with the more restrictive result on the 'propagation of Hadamard form' obtained previously in the works [24, 26, 45] without the methods of microlocal analysis. Somewhat later, the same gap was also filled in the thesis of Sanders [62], who relied on purely microlocal but somewhat sophisticated methods developed earlier in [68]. On the other hand, our method, though sharing some similarity in spirit with the ideas in [24, 26, 45], is both purely microlocal and rather elementary. »

[extrait] Note 12, p. 51 : « The gap is the content of the three lines immediately before th proof (ii) 3 ⇒ 2 on p. 547 of [57]: The reasoning presented there cannot exclude elements of the form either (x_1, x_2, 0, p_2) or (x_1, x_2, p_1, 0) from WF(ω_2) outside N. The idea of our proof was suggested by N. Pinamonti to the authors. »

[derive] Synthese : la lacune se situe dans la preuve du Theorem 5.1 de Radzikowski [57], implication « 1 ⇒ 3 », aux trois lignes precedant la preuve de « 3 ⇒ 2 », p. 547 ; elle concerne l'impossibilite d'exclure des points du front d'onde avec un covecteur nul dans l'un des deux facteurs, en dehors du voisinage N de la surface de Cauchy. Elle a ete comblee, selon S1, successivement par : (1) Sahlmann et Verch, Rev. Math. Phys. 13, 1203-1246 (2001), DOI 10.1142/s0129055x01001010 [61] ; (2) la these de Sanders, University of York (2008), arXiv:0809.4828 [62], par des methodes de Strohmaier-Verch-Wollenberg [68] ; (3) S1 lui-meme (Prop. 16 (b) + Remark 23), sur une idee de N. Pinamonti.

Nuance sur Theorem 9 : [derive] le Theorem 9 (a) de S1 cite « Theorem 5.1 in [57] » dans les deux sens, sans mentionner la lacune a cet endroit ; la lacune n'est signalee qu'en Remark 23, deux pages plus loin. Un lecteur qui ne lirait que Theorem 9 ignorerait que l'implication « geometrique ⇒ microlocal sur tout M » repose, dans [57], sur un passage incomplet.

### 2.2 Attribution du theoreme de propagation de la condition de Hadamard globale

[extrait] S1, Remark 18 (4), p. 39 : « An important feature of the global Hadamard condition for a quasifree Hadamard state is that it propagates [24, 70]: If it holds in a neighborhood of a Cauchy surface it holds in a neighborhood of any other Cauchy surface. We shall come back later to this property making use of the local notion only. »

[extrait] Bibliographie S1 : « 24. Fulling, S., Sweeny, M., Wald, R.: Singularity structure of the two-point function in quantum field theory in curved spacetime. Communications in Mathematical Physics 63, 257–264 (1978). » ; « 70. Wald, R.M.: Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics. Chicago Lectures in Physics. University Of Chicago Press (1994) ».

[derive] Reponse : S1 attribue le theoreme de propagation « it propagates [24, 70] » a Fulling-Sweeny-Wald 1978 (CMP 63) et au livre de Wald 1994. Fulling-Narcowich-Wald 1981 [26] n'est PAS cite a cet endroit ; [26] est cite (p. 39) pour le caractere Hadamard des etats invariants sous un Killing temporel dans les espaces-temps statiques (« are Hadamard [26, 70] »), et en Remark 23 dans la liste « [24, 26, 45] » des travaux anterieurs non microlocaux sur la « propagation of Hadamard form » que Sahlmann-Verch ont fusionnes avec la preuve de Radzikowski. Kay-Wald [45] est cite pour la premiere formulation rigoureuse de la condition globale et pour (62).

---

## 3. S2 : ou intervient la positivite ; lissite des differences (tache 3)

Cadre de S2 : [extrait] p. 3 « M is a smooth, connected manifold of dimension D ≥ 2 », oriente en temps ; « A state on the Borchers-Uhlmann algebra is a normalised continuous positive linear map ω : U_M → C ». [extrait] Definition 2.7, p. 5 : « A state ω on the Borchers-Uhlmann algebra U_M of the spacetime M is called a generalised Hadamard state iff WF(ω_2) ⊂ Γ_2. » Note : la condition est une INCLUSION, pas une egalite ; aucune equation du mouvement n'est supposee ; « a (generalised) Hadamard state need not be quasi-free ».

### 3.1 Proposition 2.8 : positivite utilisee pour la symetrie du front d'onde

[extrait] S2, Proposition 2.8, p. 6 : « If ω is a generalised Hadamard state, then we have: • (x_2, k_2; x_1, k_1) ∈ WF(ω_{2±}) iff (x_1, k_1; x_2, k_2) ∈ WF(ω_{2±}) iff (x_2, −k_2; x_1, −k_1) ∈ WF(ω_{2±}), • WF(ω_{2+}) = WF(ω_{2−}) ⊂ Γ_2 ∪ −Γ_2, • WF(ω_2) = WF(ω_{2−}) ∩ Γ_2. »

[extrait] Preuve, p. 6 : « The positivity of ω implies that \overline{ω_2(x_2, x_1)} = ω_2(x_1, x_2) and hence that \overline{ω_{2±}(x_2, x_1)} = ω_{2±}(x_1, x_2) = ±ω_{2±}(x_2, x_1), from which the first property follows. »

[derive] La positivite n'intervient dans Prop. 2.8 que pour obtenir l'hermiticite ω_2(x_2, x_1)^* = ω_2(x_1, x_2), d'ou les symetries du premier point, puis l'egalite WF(ω_{2+}) = WF(ω_{2−}) et l'identite WF(ω_2) = WF(ω_{2−}) ∩ Γ_2. C'est cette derniere identite, via Prop. 3.2 (WF(ω_2) = WF(E) ∩ Γ_2), qui permet de passer de l'inclusion WF(ω_2) ⊂ Γ_2 a l'EGALITE du front d'onde (forme de Hadamard au sens fort du Theorem 9 de S1) pour un champ libre (Corollary 3.3).

### 3.2 Proposition 4.1 : positivite utilisee via la construction GNS

[extrait] S2, p. 9 : « We now start our analysis of the singularities of higher n-point distributions of a generalised free field state with a result that exploits the positivity of the state.
Proposition 4.1 Let ω be a generalised Hadamard state and assume that for n ≥ 1 we have (x_n, k_n; ...; x_1, k_1) ∈ WF(ω_n). Then (x_1, k_1) ∈ V^{*+} ∪ Z and (x_n, k_n) ∈ V^{*−} ∪ Z. In particular, WF(ω_1) = ∅. »

[extrait] Preuve, p. 9-10 : « The positivity of ω implies \overline{ω_n(f_n, ..., f_1)} = ω_n(\bar f_1, ..., \bar f_n), and hence the second statement follows from the first. In fact, the positivity allows us to perform the GNS-construction [...] (x_n, k_n; ...; x_1, k_1) ∈ WF(ω_n) implies (x_1, k_1) ∈ WF(φ_1) ∪ Z and if k_1 ≠ 0 then (x_1, −k_1; x_1, k_1) ∈ WF(ω_2). The conclusion follows from the assumption that WF(ω_2) ⊂ Γ_2. »

[derive] Ici la positivite est essentielle : elle fournit l'espace de Hilbert GNS et l'ecriture ω_n = ⟨φ_{n−1}, φ_1⟩, puis le calcul des distributions a valeurs vectorielles ramene l'orientation du covecteur extremal au front d'onde de ω_2 sur la diagonale. Sans positivite, aucune contrainte d'orientation sur les fonctions a n points.

### 3.3 Lemma 2.9 : difference de deux etats Hadamard generalises

[extrait] S2, Lemma 2.9, p. 6 : « For two generalised Hadamard states ω, ω' we have that ω_2 − ω'_2 is smooth iff ω_{2−} − ω'_{2−} is smooth.
Proof. We define w(x_2, x_1) := (ω_2 − ω'_2)(x_2, x_1), w̃(x_2, x_1) := w(x_1, x_2) and w_{2−} := (1/2)(w − w̃) and argue as in the proof of proposition 2.8: WF(w) ⊂ Γ_2, WF(w̃) ⊂ −Γ_2 and hence WF(w) ∩ WF(w̃) = ∅. It then follows from w − w̃ = 2w_{2−} that WF(w_{2−}) = WF(w) ∪ WF(w̃). Now WF(w_{2−}) = ∅ if and only if WF(w) = ∅, which proves the statement. »

[derive] Lecture attentive de la preuve : les seuls ingredients sont (a) WF(ω_2), WF(ω'_2) ⊂ Γ_2 (hypothese Hadamard generalisee, donc WF(w) ⊂ Γ_2), (b) WF(w̃) ⊂ −Γ_2 par transposition des arguments (propriete 4 de Prop. 2.5, purement geometrique), (c) Γ_2 ∩ −Γ_2 = ∅ (propriete 2 de Prop. 2.5). La positivite n'est PAS utilisee dans la preuve du Lemma 2.9, bien que l'enonce parle d'« etats ». La phrase « argue as in the proof of proposition 2.8 » renvoie a la methode (decomposition w, w̃), pas a l'hermiticite. Consequence : le Lemma 2.9 vaut, tel que prouve, pour deux bidistributions quelconques dont les fronts d'onde sont inclus dans Γ_2.

[extrait] S2, p. 8, commentaire apres Corollary 3.3 : « We see from proposition 3.2 and lemma 2.9 that for two generalised free field states ω and ω' with commutator functions E and E' respectively, ω_2 − ω'_2 is smooth iff E − E' is smooth. »

### 3.4 Lemma 4.6 : generalisation aux fonctions a n points

[extrait] S2, Lemma 4.6, p. 11 : « Consider two generalised Hadamard states ω, ω', which both satisfy commutation relations with the same commutator E such that WF(E) ≠ ∅. For any n ≥ 0 we have that ω_{n+2} − ω'_{n+2} is smooth if and only if ω_n ≡ ω'_n. Proof. The case n = 0 follows from lemma 2.9. [...] » et p. 12 : « The same statement still holds when the commutators E and E' of the two states differ by a smooth function. »

[derive] Pour n = 0, Lemma 4.6 n'est que Lemma 2.9 joint a l'identite E = −2iω_{2−} (Prop. 3.2) : deux etats Hadamard generalises de meme commutateur ont des fonctions a deux points qui different d'une fonction lisse. Le sens direct (n ≥ 1) utilise les relations de commutation et les proprietes 2 et 4 de Prop. 2.5 ; le sens reciproque utilise Prop. 3.2 et donc la positivite (via Prop. 2.8).

---

## 4. Application [derive] : prolongement d'un etat Hadamard du demi-espace {η < 0} a tout Minkowski R^4 (tache 4)

Donnees : M = R^4 de Minkowski, champ scalaire sans masse (m = 0 ; ξ sans effet car R = 0). M_− := {η < 0} est un ouvert causalement convexe, globalement hyperbolique en lui-meme, de surface de Cauchy Σ := {η = −ε}, ε > 0, qui est aussi une surface de Cauchy de M. ω est un etat quasi-libre sur A(M_−), Hadamard au sens de la Definition 15 sur M_−. On prolonge ω_2 a M × M par le probleme de Cauchy des bisolutions depuis Σ.

Schema des etapes et de l'enonce qui porte chacune :

```
 [E0] ω etat Hadamard (Def. 15) sur A(M_-), dim 4        <- donnee ; POSITIVITE utilisee ici
      |
      v  Theorem 9 (a), sens (i) => (ii), applique sur M_-
 [E1] WF(ω_2|_{M_-×M_-}) = H_{M_-} ; en particulier forme de Hadamard sur O ⊂ M_-, O ∋ Σ
      |
      v  prolongement de Cauchy des bisolutions (construction, hors S1/S2)
 [E2] ω_2 ∈ D'(M×M), P_x ω_2 = 0 = P_y ω_2 sur M×M, ω_2 = S^t ∘ ω_2 ∘ S
      |
      v  Prop. 16 (b) sous la forme de Remark 23 (aucune positivite requise)
 [E3] WF(ω_2) ⊂ H_M sur tout M×M, y compris a travers {η = 0}
      |
      v  Remark 18 (3), m = 0 : vide de Minkowski Hadamard ; (75) : WF(ω^M_2) = H_M
 [E4] w := ω_2 − ω^M_2 verifie WF(w) ⊂ H_M
      |
      v  S2 Lemma 2.9 (preuve purement microlocale) + controle de la partie antisymetrique
 [E5] w ∈ C^∞(M×M)  <=>  ω_{2−} − ω^M_{2−} lisse ; or les deux valent (i/2)E sur M×M  =>  w lisse
```

Detail de chaque etape.

[E0] → [E1]. Theorem 9 (a) exige : dimension 4 (ok), espace-temps globalement hyperbolique (M_− l'est), un ETAT sur A(M_−) (ok : ω est donne comme etat ; c'est ici que la positivite est consommee, car Def. 15 et Theorem 9 ne sont enonces que pour des etats), quasi-libre non requis. Conclusion : WF(ω_2) = H_{M_−} sur M_− × M_−. Identification necessaire [derive] : la relation ∼ de Theorem 9 sur M_− est la restriction de celle de M (les geodesiques nulles de M_− sont les segments de celles de M), donc H_{M_−} = H_M ∩ T*(M_− × M_−). Ainsi WF(ω_2|_{O×O}) a la forme de Hadamard « sur O » au sens requis par Prop. 16 (b) sur M.

[E1] → [E2]. Le prolongement n'est pas un enonce de S1 ni de S2 ; c'est une construction. Ce qu'il faut en retenir pour la suite : la bidistribution prolongee, notee encore ω_2, est dans D'(M × M), est bisolution de P = □ sur M × M, et coincide avec l'originale sur M_− × M_− (unicite du probleme de Cauchy des bisolutions, ω_2 originale etant deja bisolution sur M_−). La preuve de Prop. 16 (b) fournit l'expression explicite ω_2 = S^t ∘ ω_2 ∘ S avec S de noyau (78) : c'est precisement la formule qui definit le prolongement a partir des valeurs sur O × O.

[E2] → [E3]. Prop. 16 (b) telle qu'affaiblie par Remark 23 : hypotheses = M globalement hyperbolique (R^4), dimension n ≥ 2, Σ = {η = −ε} surface de Cauchy spatiale lisse de M, O voisinage ouvert de Σ (on prend O ⊂ M_−), ω_2 ∈ D'(M × M) bisolution (a lisse pres). AUCUNE positivite, aucune propriete d'etat. Conclusion : WF(ω_2) ⊂ H_M sur tout M × M. L'inclusion vaut en particulier pour les points (x, y) avec η(x) < 0 < η(y), ou avec x ou y sur {η = 0} : le passage a travers {η = 0} est exactement ce que Prop. 16 (b) controle, puisque O est un voisinage d'une seule surface de Cauchy et la conclusion porte sur M entier. Reserve : la preuve ne donne que l'inclusion ⊂ H, et c'est tout ce dont la suite a besoin.

[E3] → [E4]. Remark 18 (3) : le vide de Minkowski est Hadamard, « The result holds also for m = 0 » ; et (75), p. 48 : WF(ω^M_2) = H_M, « correct and holds true also for m = 0 ». Donc WF(w) ⊂ WF(ω_2) ∪ WF(ω^M_2) ⊂ H_M (Remark 20, sous-additivite).

[E4] → [E5]. Deux routes possibles.
Route A (S1, Theorem 9 (b)) : il faudrait que ω_2 prolongee soit la fonction a deux points d'un ETAT Hadamard sur A(M) (Def. 15 sur tout M). Cela exige (a) la positivite sur M, (b) l'egalite WF(ω_2) = H_M (pas seulement ⊂) pour remonter de (ii) a (i) par Theorem 9 (a). Aucun des deux n'est fourni par Remark 23. La route A consomme donc la positivite une seconde fois, sur M entier.
Route B (S2, Lemma 2.9) : la preuve du Lemma 2.9 n'utilise que WF(ω_2) ⊂ Γ_2, WF(ω^M_2) ⊂ Γ_2 et Γ_2 ∩ −Γ_2 = ∅ (section 3.3 ci-dessus). Sur Minkowski, H_M ⊂ Γ_2 (Γ_2 de S2 contient les points relies par une geodesique nulle avec covecteur causal futur ; H_M en est le sous-ensemble a covecteurs nuls). Donc w lisse ⇔ ω_{2−} − ω^M_{2−} lisse. Or ω_{2−} = (i/2)E sur M_− × M_− (relations de commutation de A(M_−) ; E_{M_−} = E|_{M_−×M_−} par convexite causale) et, ω_{2−} prolongee et (i/2)E etant deux bisolutions sur M × M de memes valeurs sur O × O, elles coincident sur M × M (meme formule S^t ∘ · ∘ S). De meme ω^M_{2−} = (i/2)E. Donc ω_{2−} − ω^M_{2−} = 0 et w ∈ C^∞(M × M). La route B ne consomme PAS la positivite de ω_2 prolongee sur M.

Ou la positivite est necessaire : uniquement a l'etape [E0] → [E1], pour appliquer Theorem 9 (a) (sens geometrique ⇒ microlocal) sur M_−, parce que S1 n'enonce ce theoreme que pour des etats. Ni la propagation (Remark 23), ni la lissite de la difference (Lemma 2.9 tel que prouve) n'en ont besoin. Si l'on suit la Route A, la positivite est aussi requise sur M entier au travers de l'hypothese « Hadamard state on A(M) » de Theorem 9 (b). Remarque complementaire [derive] : la positivite sur M decoule en fait de celle sur M_−, car pour f ∈ C^∞_0(M) on a ω_2(\bar f, f) = ω_2(\overline{Sf}, Sf) ≥ 0 avec Sf ∈ C^∞_0(O) (S est un operateur reel) ; mais cette deduction n'est pas dans S1 ni S2 et doit etre explicitee si l'on veut la Route A.

Hypotheses supplementaires a expliciter (non fournies par les enonces releves) :
1. Que le prolongement de Cauchy des bisolutions produit bien une distribution sur M × M (et non seulement sur un ouvert), bisolution exacte, coincidant avec ω_2 sur M_− × M_− ; et unicite de ce prolongement (sinon « ω_2 prolongee » n'est pas definie). La formule ω_2 = S^t ∘ ω_2 ∘ S de la preuve de Prop. 16 (b) le fournit, mais S1 l'ecrit pour un etat sur A(M) deja donne, pas comme construction d'un prolongement.
2. Que ω_{2−} prolongee vaut (i/2)E sur M × M (controle de la partie antisymetrique) : necessaire pour la Route B, et pour que ω_2 prolongee soit la fonction a deux points d'un etat (CCR) dans la Route A.
3. L'identification H_{M_−} = H_M ∩ T*(M_−^2) et l'inclusion H_M ⊂ Γ_2 (passage entre les conventions de S1 et S2 ; S2 eq. (2), p. 4, pour Γ_2 ; S1 (76) pour H). Les conventions de signe de Fourier concordent (S1 note 10 : « agrees with those of [32, 57, 58] »).
4. Que la Def. 15 de S1 soit appliquee sur l'espace-temps M_− (4D, globalement hyperbolique) et non sur M : la donnee « Hadamard sur le seul demi-espace » doit etre lue ainsi.
5. Pour conclure a « Hadamard au sens de Def. 15 sur M » (et non seulement a « w lisse »), il faut de plus l'egalite WF(ω_2) = H_M ; elle resulte de WF(w) = ∅ et WF(ω^M_2) = H_M, mais ce n'est qu'une consequence du resultat, pas une etape intermediaire. Noter que « w lisse sur M × M » est strictement plus fort que « Hadamard sur M » au sens local de Def. 15 (Remark 18 (4) : « Definition 15 guarantees only that the difference is smooth when x and y belong to the same sufficiently small neighborhood »).

---

## 5. Invariance conforme de la condition de Hadamard pour ξ = 1/6 (tache 5)

Les sources lues ne disent RIEN de l'invariance conforme de la condition de Hadamard, ni du couplage conforme ξ = 1/6. Requetes explicites lancees sur S1 et S2 (« conformal invariance of Hadamard condition conformal coupling xi=1/6 ») : aucune page pertinente renvoyee. Occurrences de ξ dans S1 : parametre arbitraire du KG (Theorem 9, Prop. 15, Prop. 16), note 11 (ξ = 0 dans [57, 58]), restrictions « ξ = 0 » des resultats d'existence et d'equivalence unitaire (Remark 18 (4), (5), Sect. 2.5), Remark 2 (4) (ξ fonction lisse admise). Occurrences dans S2 : parametre generique (Definition 3.1, Corollary 3.3, Prop. 5.5) et le commentaire p. 8 montrant que E_{m,ξ} − E_{m',ξ'} n'est en general pas lisse. Aucun enonce sur une transformation conforme de la metrique.

---

## 6. Metadonnees des quatre articles de revue (tache 6)

Acces : une seule page editeur a pu etre lue (Fulling-Sweeny-Wald sur link.springer.com). Les pages Springer de Radzikowski 1996 et Radzikowski-Verch 1996 ont ete refusees par le proxy (HTTP 429, limitation de debit, avec consigne de ne pas reessayer) ; ScienceDirect (Fulling-Narcowich-Wald) refuse par robots.txt ; Project Euclid refuse par une protection anti-robot. Aucun contournement tente. Pour les trois articles non lus a la source, les metadonnees proviennent de la bibliographie de S1 (refs [57], [58], [26]) ; le statut de libre acces n'a pas pu etre verifie.

| Article | Titre | Auteurs | Revue | Vol. | Pages | Annee | DOI | Libre acces ? | Source |
|---|---|---|---|---|---|---|---|---|---|
| Radzikowski 1996 | Micro-local approach to the Hadamard condition in quantum field theory on curved space-time | M. J. Radzikowski | Commun. Math. Phys. | 179 | 529-553 | 1996 | 10.1007/BF02100096 | non verifie | S1 [57] |
| Radzikowski, Verch 1996 | A local-to-global singularity theorem for quantum field theory on curved space-time | M. J. Radzikowski, R. Verch | Commun. Math. Phys. | 180 | 1-22 | 1996 | 10.1007/BF02101180 | non verifie | S1 [58] |
| Fulling, Sweeny, Wald 1978 | Singularity structure of the two-point function in quantum field theory in curved spacetime | S. A. Fulling, M. Sweeny, R. M. Wald | Commun. Math. Phys. | 63 (no 3) | 257-264 | 1978 (octobre) | 10.1007/BF01196934 | NON : « Access this article », « Buy article PDF USD 39.95 », pas de badge Open Access | page Springer lue ; concorde avec S1 [24] |
| Fulling, Narcowich, Wald 1981 | Singularity structure of the two-point function in quantum field theory in curved spacetime, II | S. A. Fulling, F. J. Narcowich, R. M. Wald | Annals of Physics | 136 | 243-272 | 1981 | 10.1016/0003-4916(81)90098-1 | non verifie | S1 [26] |

---

## 7. Synthese des conclusions

1. Def. 15 (S1) : notion LOCALE, dimension 4, enoncee pour un etat (positif), quasi-libre non requis.
2. Theorem 9 (S1) : dimension 4, etat sur A(M) non necessairement quasi-libre ; (a) equivalence Def. 15 ⇔ WF(ω_2) = H ; (b) difference de deux etats Hadamard lisse sur M × M, preuve deleguee a Radzikowski-Verch Thm 4.3.
3. Prop. 16 (b) (S1) : propagation microlocale depuis un voisinage d'une surface de Cauchy, dimension n ≥ 2 ; la preuve n'utilise que le caractere bisolution, les fronts d'onde de E^± et le theoreme de composition ; elle etablit l'inclusion WF ⊂ H.
4. Remark 23 (S1) : la propagation n'exige PAS la positivite, seulement ω_2 ∈ D'(M × M) bisolution a lisse pres.
5. Lacune de Radzikowski Thm 5.1 (1 ⇒ 3, p. 547, covecteurs nuls dans un facteur hors de N) : comblee par Sahlmann-Verch 2001 [61], puis Sanders 2008 [62], puis S1 (idee de Pinamonti).
6. Propagation de la condition globale attribuee par S1 a Fulling-Sweeny-Wald 1978 [24] et Wald 1994 [70] ; Fulling-Narcowich-Wald 1981 [26] cite ailleurs (etats statiques ; liste [24, 26, 45] en Remark 23).
7. S2 : la positivite sert en Prop. 2.8 (hermiticite de ω_2, d'ou egalite des fronts d'onde des parties symetrique et antisymetrique) et en Prop. 4.1 (construction GNS) ; Lemma 2.9 est enonce pour des etats mais sa preuve n'utilise que les inclusions de fronts d'onde ; Lemma 4.6 (n = 0) = Lemma 2.9 + commutateur commun.
8. Application : w lisse sur R^4 × R^4, y compris a travers {η = 0}, par la chaine Thm 9 (a) sur M_− → Remark 23 sur M → Lemma 2.9 + partie antisymetrique = (i/2)E. La positivite n'est necessaire qu'au depart (Thm 9 (a) sur M_−) ; elle serait requise sur tout M si l'on passait par Thm 9 (b). Hypotheses a expliciter : existence et unicite du prolongement bisolution, controle de la partie antisymetrique, identification des cones H et Γ_2 entre S1 et S2.
9. Rien dans S1 ni S2 sur l'invariance conforme de la condition de Hadamard a ξ = 1/6.
10. Metadonnees : une seule page editeur verifiee (FSW 1978, payant) ; les trois autres non verifiables a la source, metadonnees prises dans la bibliographie de S1.

---

## 8. Fichiers de travail et empreintes sha256

Repertoire : /home/claude/audit_p1/aca1/work/

```
727d3428ed629940f43eac7a3bbdf47c35bb7408543d93ee89a7ff32f7489464  S1-extraits-1412.5945v3.md
b1404a949b9fd182861451dfaa20e645dd9cb5270c6cf42713b9578eba0dd6e3  S2-extraits-0903.1021v1.md
7ea599e24da7be7c04695989ab59fab564e98bf0a75958bb8b3f0f9b5be55b1a  METADONNEES-revues.md
```

Fichier recapitulatif : /home/claude/audit_p1/aca1/work/SHA256SUMS.txt (empreinte calculee et consignee a la fin de ce rapport, voir SHA256SUMS-final.txt).
