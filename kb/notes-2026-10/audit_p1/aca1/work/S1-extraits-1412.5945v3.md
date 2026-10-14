# Extraits verbatim de S1 : arXiv:1412.5945v3 (Khavkine, Moretti), lus via alphaXiv answer_pdf_queries le 2026-10-13

Transcription : le texte extrait du PDF est reproduit tel quel ; les symboles mal rendus par l'extraction sont notes entre crochets. Notamment le symbole « k_x ⊳ 0 » (covecteur futur) est rendu « k_x . 0 » et « k_x ⊲ 0 » est rendu « k_x / 0 » par l'extracteur. « M 3 x 7→ » signifie « M ∋ x ↦ ».

## [extrait] Definition 15 (p. 38)

"Definition 15. With M four dimensional, we say that a (not necessarily quasifree) state ω on A(M) and its two point function ω_2 are Hadamard if ω_2 ∈ D'(M × M) and every point of M admits an open normal neighborhood C where
ω_2(x, y) − H_{0+}(x, y) = w(x, y) for some w ∈ C^∞(C × C) . (60)
Here 0+ indicates the standard weak distributional limit as ε → 0+ ("first integrate against test functions and next take the limit")."

Contexte (p. 37) : "In the rest of the chapter we only consider a four dimensional spacetime, essentially following [33]."

## [extrait] Remark 18 (4) (p. 39-40)

"(4) Referring to the literature before the cornerstone results [57, 58] (we consider in Sec. 3.4), Definition 15 properly refers to locally Hadamard states. This is because there also exists a notion of global Hadamard state (Definition 3.4 in [57]), discussed in [45] in a completely rigorous way for the first time. [...] In this regard a technically important result, proved in the appendix B of [45], is that, analogous to Proposition 12 in the case of Minkowski space,
M ∋ x ↦ ω(φ(f)φ(x)) = \overline{ω(φ(x)φ(f))} ∈ C^∞(M) (62)
if f ∈ C^∞_0(M) and ω is a quasifree globally Hadamard state on A(M). We shall prove this fact later using the microlocal approach. This fact has an important consequence we shall prove later using the microlocal approach: if ω and ω' are (locally) Hadamard states, then M × M ∋ (x, y) ↦ ω_2(x, y) − ω'_2(x, y) is smooth. This fact is far from obvious, since Definition 15 guarantees only that the difference is smooth when x and y belong to the same sufficiently small neighborhood.
An important feature of the global Hadamard condition for a quasifree Hadamard state is that it propagates [24, 70]: If it holds in a neighborhood of a Cauchy surface it holds in a neighborhood of any other Cauchy surface. We shall come back later to this property making use of the local notion only. This fact, together with the last comment in (3) proves that quasifree Hadamard states for massive fields (and ξ = 0) exist in globally hyperbolic spacetimes by means of a deformation argument similar to the one exploited in Sect. 2.5.
We shall not insist on the distinction between the global and the local Hadamard property because, in [58], it was established that a local Hadamard state on A(M) is also a global one (the converse is automatic). It was done exploiting the microlocal approach, which we shall discuss shortly."

## [extrait] Theorem 9 (p. 48-49)

"We note that we do not make use of the global Hadamard condition (see (4) in Remark 18). The following theorem collects various results of [57, 58].

Theorem 9 ("Radzikowski theorem"). For a 4-dimensional globally hyperbolic (time oriented) spacetime M and referring to the unital ∗-algebra of Klein-Gordon quantum field A(M) with m^2, ξ ∈ R arbitrarily fixed, let ω be a state on A(M), not necessarily quasifree.
(a) The following statements are equivalent,
(i) ω is Hadamard in the sense of Def. 15,
(ii) the wavefront set of the two-point function ω_2 has the Hadamard form on M or equivalently, it satisfies the microlocal spectrum condition on M:
WF(ω_2) = { (x, y, k_x, −k_y) ∈ T*M^2 \ 0 | (x, k_x) ∼ (y, k_y), k_x ⊳ 0 } =: H. (76)
Here, (x, k_x) ∼ (y, k_y) means that there exists a null geodesic γ connecting x to y such that k_x is coparallel and cotangent to γ at x and k_y is the parallel transport of k_x from x to y along γ, Figure 2. k_x ⊳ 0 means that k_x does not vanish and is future-directed (k_x(v) ≥ 0 for all future-directed v ∈ T_xM), Figure 3.
(b) If ω' is another Hadamard state on A(M), then ω_2 − ω'_2 ∈ C^∞(M × M, C).
Proof. (a) Suppose that ω satisfies (i), then it is globally Hadamard in the sense[11] of [57] due to Theorem 9.2 in [58]. Theorem 5.1 in [57] implies that (ii) holds. Conversely, if (ii) is valid, Theorem 5.1 in [57] entails that ω is globally and thus locally Hadamard so that (i) holds true. (b) immediately arises from Theorem 4.3 in [58]."

Note 11 (p. 49) : "Results in [57, 58] are stated for ξ = 0 in KG operator, however they are generally valid for m^2 replaced by a given smooth function, as specified at the beginning of p. 533 in [57]."

## [extrait] Phrase introduisant la Proposition 16 (p. 49)

"With this result and the microlocal technology previously introduced we can prove some remarkable properties of Hadamard states, especially in relation with what was already discussed in (4) in Remark 18. The second statement, for n = 4, implies that the singularity structure of Hadamard states propagates through the spacetime."

## [extrait] Proposition 16 et preuve (p. 50-51)

"Proposition 16. Consider a state ω on A(M), with ω_2 ∈ D'(M × M), where M is a (time oriented) globally hyperbolic spacetime with dimension n ≥ 2. The following facts hold.
(a) If WF(ω_2) has the Hadamard form, then M ∋ x ↦ ω_2(x, f) is smooth for every f ∈ C^∞_0(M).
(b) If WF(ω_2|_{O×O}) has the Hadamard form on O, where O is an open neighborhood of a smooth spacelike Cauchy surface Σ of M, then WF(ω_2) has the Hadamard form on M.
Proof. (a) From (e) in Theorem 5 and the Hadamard form of WF(ω_2) we conclude that WF(ω_2(·, f)) = ∅. Next, (a) in Theorem 5 implies the thesis.
(b) The 2-point function ω_2(x, y) is a bisolution of the Klein-Gordon operator P = □_M + m^2 + ξR, as in (8). So the value of ω_2(f, g), for f, g ∈ C^∞_0(M), depends on the arguments only up to the addition of any term from P[C^∞_0(M)]. In fact, we can choose h, k ∈ C^∞ such that supp(f + P[h]) and supp(g + P[k]) are both contained in O. More precisely, we can define an S ∈ D'(O × M) such that the corresponding operator maps S : C^∞_0(M) → C^∞_0(O) and we have the identity ω_2 = S^t ∘ ω_2 ∘ S. Then, using the result of Theorem 8 on the composition of kernels and the fact that ω_2 has the Hadamard form on O, we can show that ω_2 has the Hadamard form on all of M.
Consider a smooth partition of unity χ_+ + χ_− = 1 adapted to the Cauchy surface Σ. That is, there exist two other Cauchy surfaces, Σ_+ in the future of Σ and Σ_− in the past of Σ, such that supp χ_+ ⊂ J^+(Σ_−) and supp χ_− ⊂ J^−(Σ_+). Such an adapted partition of unity always exists if O is globally hyperbolic in its own right and, if not, since M is globally hyperbolic, any open neighborhood of Σ will contain a possibly smaller neighborhood of Σ that is also globally hyperbolic [7, 6].
Let S f = f − P[χ_+ E^− f + χ_− E^+ f], with the corresponding integral kernel
S(x, y) = δ(x, y) − P_x[χ_+(x)E^−(x, y) + χ_−(x)E^+(x, y)], (78)
where the subscript on P_x means that it is acting only on the x variable. A straight forward calculation shows that S has the desired properties. Multiplication by a smooth function and the application of a differential operator does not increase the wavefront set, hence
WF(S) ⊂ WF(δ) ∪ WF(E^−) ∪ WF(E^+) (79)
as a subset of T*(O × M). [...] We can now appeal to Theorem 8 on the wavefront set of the composition of kernels to how that WF(ω_2) = WF(S^t ∘ ω_2 ∘ S) ⊂ H. The first thing to check is that WF(S)_{M_i}, WF(ω_2)_{M_i}, i = 1, 2 denoting respectively the first and the second factor in M × M, are all empty, because they contain no element of the form (x, y, k_x, 0) or (x, y, 0, k_y). Second, due to the hypothesis WF'(ω_2)|_O ⊂ H'_O, the symmetry of the composition and the fact that composition with δ(x, y) leaves any wavefront set invariant, it is sufficient to check that the compositions of wavefront sets as relations satisfy H'_O ∘ F'_± ⊂ H'_M.
Consider any (x, y, k_x, k_y) ∈ H'_O and (y, z, k_y, k_z) ∈ F'_±, so that (x, z, k_x, k_z) ∈ H'_O ∘ F'_±. Then (x, k_x) ∼ (y, k_y) and (y, k_y) ∼ (z, k_z) in M according to the relation ∼ defined in Theorem 9, so that (x, k_x) ∼ (z, k_z) by transitivity of that relation in M. The only question is about the allowed orientations of k_x and k_y. By the Hadamard condition on O, we have k_x ⊳ 0 and k_y ⊳ 0. On the other hand, the condition of being a point in F_± induces the condition that either both k_y ⊳ 0 and k_z ⊳ 0 or both k_y ⊲ 0 and k_z ⊲ 0. Combining the two conditions we find that k_z ⊳ 0, and hence that (x, z, k_x, k_z) ∈ H'_M. This concludes the proof."

## [extrait] Remark 23 et note 12 (p. 51-52)

"Remark 23. With an elementary re-adaptation, statement (b) holds true weakening the hypotheses, only requiring that ω_2 ∈ D'(M × M) and that it satisfies KG equation in both arguments up to smooth functions r, l ∈ C^∞(M × M, C), i.e. P_x ω_2(x, y) = l(x, y), P_y ω_2(x, y) = r(x, y). In this form, it closes a gap[12] present in the proof of the main result of [57], Theorem 5.1 (the fact that 1 implies 3), and proves the statement on p. 548 of [57] immediately after the proof of the mentioned theorem. It should be mentioned that the same gap had been previously explicitly identified and filled in the work of Sahlmann and Verch [61]. These authors merged the partial proof of Radzikowski with the more restrictive result on the 'propagation of Hadamard form' obtained previously in the works [24, 26, 45] without the methods of microlocal analysis. Somewhat later, the same gap was also filled in the thesis of Sanders [62], who relied on purely microlocal but somewhat sophisticated methods developed earlier in [68]. On the other hand, our method, though sharing some similarity in spirit with the ideas in [24, 26, 45], is both purely microlocal and rather elementary. In fact, it only takes advantage of the microlocal analysis in the guise of the theorem on the composition of wavefront sets."

Note 12 : "The gap is the content of the three lines immediately before th proof (ii) 3 ⇒ 2 on p. 547 of [57]: The reasoning presented there cannot exclude elements of the form either (x_1, x_2, 0, p_2) or (x_1, x_2, p_1, 0) from WF(ω_2) outside N. The idea of our proof was suggested by N. Pinamonti to the authors."

## [extrait] Theorem 8 (Composition of kernels) (p. 47)

"Theorem 8 (Composition of kernels). Consider three smooth manifolds X, Y, Z and K_1 ∈ D'(X × Y), K_2 ∈ D'(Y × Z). If WF'(K_1)_Y ∩ WF(K_2)_Y = ∅ and the projection supp K_2 ∋ (y, z) ↦ z ∈ Z is proper (that is, the inverse of a compact set is compact), then the composition K_1 ∘ K_2 is well defined, giving rise to K ∈ D'(X, Z), and reduces to the standard one when the kernel are smooth. It finally holds (the symbol ∘ denoting the composition of relations)
WF'(K) ⊂ WF'(K_1) ∘ WF'(K_2) ∪ (WF(K_1)_X × Z × {0}) ∪ (X × {0} × WF'(K_2)_Z). (73)"

## [extrait] Proposition 15 (p. 49)

"Proposition 15. The retarded and advanced fundamental solutions of the Klein-Gordon operator P = □_M + m^2 + ξR on M, E^+, E^− ∈ D'(M × M) respectively, have the following wavefront sets (Figure 4):
WF(E^±) = WF(δ) ∪ { (x, y, k_x, −k_y) ∈ T*M^2 \ 0 | (x, k_x) ∼ (y, k_y), x ∈ J^±(y) } =: F_±, (77)
where ∼ denotes the same relation as in Theorem 9."

## [extrait] Remark 18 (3) (p. 39) : vide de Minkowski, cas m = 0

"(3) Minkowski vacuum ω_M defined by the two point function (37) is Hadamard. In particular, for m > 0, it holds ω_{M2}(x, y) = (1/4π^2) 1/σ_{0+}(x, y) + (m^2/2(2π)^2) [I_1(m√σ)/(m√σ)] ln(m^2 σ_{0+}(x, y)) + w(x, y) where w is smooth. The result holds also for m = 0 and in that case, only the first term in the right-hand side does not vanish in the expansion above."

## [extrait] Remark 2 (4) (p. 14) : fonctions lisses m^2, ξ

"(4) Everything we will say holds equally for m^2 and ξ replaced by corresponding smooth real functions, also in the case where m^2 attains negative values."

## [extrait] Bibliographie (p. 58-60)

"24. Fulling, S., Sweeny, M., Wald, R.: Singularity structure of the two-point function in quantum field theory in curved spacetime. Communications in Mathematical Physics 63, 257–264 (1978). DOI 10.1007/bf01196934"
"26. Fulling, S.A., Narcowich, F.J., Wald, R.M.: Singularity structure of the two-point function in quantum field theory in curved spacetime, II. Annals of Physics 136, 243–272 (1981). DOI 10.1016/0003-4916(81)90098-1"
"45. Kay, B.S., Wald, R.M.: Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate killing horizon. Physics Reports 207, 49–136 (1991). DOI 10.1016/0370-1573(91)90015-e"
"57. Radzikowski, M.J.: Micro-local approach to the Hadamard condition in quantum field theory on curved space-time. Communications in Mathematical Physics 179, 529–553 (1996). DOI 10.1007/bf02100096"
"58. Radzikowski, M.J., Verch, R.: A local-to-global singularity theorem for quantum field theory on curved space-time. Communications in Mathematical Physics 180, 1–22 (1996). DOI 10.1007/bf02101180"
"61. Sahlmann, H., Verch, R.: Microlocal spectrum condition and Hadamard form for vector-valued quantum fields in curved spacetime. Reviews in Mathematical Physics 13, 1203–1246 (2001). DOI 10.1142/s0129055x01001010"
"62. Sanders, K.: Aspects of locally covariant quantum field theory. Ph.D. thesis, University of York (2008). URL http://arxiv.org/abs/0809.4828"
"68. Strohmaier, A., Verch, R., Wollenberg, M.: Microlocal analysis of quantum fields on curved space-times: Analytic wave front sets and reeh-schlieder theorems. Journal of Mathematical Physics 43, 5514–5530 (2002). DOI 10.1063/1.1506381"
"70. Wald, R.M.: Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics. Chicago Lectures in Physics. University Of Chicago Press (1994)"
"49. Khavkine, I., Moretti, V.: Algebraic QFT in curved spacetime and quasifree Hadamard states: An introduction. In: R. Brunetti, C. Dappiaggi, K. Fredenhagen, J. Yngvason (eds.) Advances in Algebraic Quantum Field Theory, Mathematical Physics Studies, pp. 191–251. Springer, Berlin (2015). DOI 10.1007/978-3-319-21353-8_5"

## Recherche negative : invariance conforme

Les requetes « conformal invariance of Hadamard condition conformal coupling xi=1/6 » n'ont renvoye aucune page de S1 traitant de l'invariance conforme. Les seules occurrences de ξ dans les pages lues sont : ξ parametre arbitraire du KG (Thm 9, Prop 15, Prop 16), note 11 (ξ = 0 dans [57,58]), et les restrictions « ξ = 0 » pour les resultats d'existence/unitarite (Remark 18 (4), (5), Sect. 2.5).
