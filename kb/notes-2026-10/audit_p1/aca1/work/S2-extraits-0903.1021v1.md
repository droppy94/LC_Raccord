# Extraits verbatim de S2 : arXiv:0903.1021v1 (Ko Sanders, « Equivalence of the (generalised) Hadamard and microlocal spectrum condition for (generalised) free fields in curved spacetime », 3 fevrier 2009), lus via alphaXiv answer_pdf_queries le 2026-10-13

## [extrait] Cadre (p. 3)

"Let M = (M, g) be a spacetime, i.e. M is a smooth, connected manifold of dimension D ≥ 2 with the smooth Lorentzian metric g, where we use the signature convention + − ... −. [...] We assume that M is time-oriented, so we can define the future and past causal cones V^± ⊂ TM and their duals, V^{*±} ⊂ T*M."

"A state on the Borchers-Uhlmann algebra is a normalised continuous positive linear map ω : U_M → C."

## [extrait] Definition 2.7 (p. 5-6)

"Definition 2.7 A state ω on the Borchers-Uhlmann algebra U_M of the spacetime M is called a generalised Hadamard state iff WF(ω_2) ⊂ Γ_2.
Note that a (generalised) Hadamard state need not be quasi-free. We will show in section 3 that the generalised Hadamard condition reduces to the Hadamard condition in the case of free fields."

## [extrait] Definition de ω_{2±} (p. 6)

"ω_{2±}(x_2, x_1) := (1/2)(ω_2(x_2, x_1) ± ω_2(x_1, x_2)). (3)
The idea of the following proof is taken from proposition 6.1 in [21]."

## [extrait] Proposition 2.8 et preuve (p. 6)

"Proposition 2.8 If ω is a generalised Hadamard state, then we have:
• (x_2, k_2; x_1, k_1) ∈ WF(ω_{2±}) iff (x_1, k_1; x_2, k_2) ∈ WF(ω_{2±}) iff (x_2, −k_2; x_1, −k_1) ∈ WF(ω_{2±}),
• WF(ω_{2+}) = WF(ω_{2−}) ⊂ Γ_2 ∪ −Γ_2,
• WF(ω_2) = WF(ω_{2−}) ∩ Γ_2.
Proof. The positivity of ω implies that \overline{ω_2(x_2, x_1)} = ω_2(x_1, x_2) and hence that \overline{ω_{2±}(x_2, x_1)} = ω_{2±}(x_1, x_2) = ±ω_{2±}(x_2, x_1), from which the first property follows. That WF(ω_{2±}) ⊂ Γ_2 ∪ −Γ_2 for a generalised Hadamard state is clear from the definition. Now suppose that (x_2, k_2; x_1, k_1) ∈ WF(ω_{2±}). Then we can distinguish two cases, namely either (x_2, k_2; x_1, k_1) ∉ WF(ω_2) or (x_2, −k_2; x_1, −k_1) ∉ WF(ω_2) by equation (3) and statement 2 of proposition 2.5. Using ω_{2±} = ω_2 − ω_{2∓} and the properties under the first item we find that either (x_2, k_2; x_1, k_1) ∈ WF(ω_{2∓}) or (x_2, −k_2; x_1, −k_1) ∈ WF(ω_{2∓}), as the case may be, and hence that (x_2, k_2; x_1, k_1) ∈ WF(ω_{2∓}). Thus WF(ω_{2+}) ⊂ WF(ω_{2−}) and the opposite inclusion can be proved in the same way. For the last item we use again the definition 2ω_{2−} = ω_2 − ω̃_2, where ω̃_2(x_2, x_1) := ω_2(x_1, x_2). By the assumption on ω_2 we have WF(ω_2) ∩ WF(ω̃_2) = ∅. Hence we deduce: WF(ω_2) ⊂ WF(ω_{2−}), WF(ω̃_2) ⊂ WF(ω_{2−}) and WF(ω_{2−}) ⊂ WF(ω_2) ∪ WF(ω̃_2), from which it follows that WF(ω_{2−}) = WF(ω_2) ∪ WF(ω̃_2). Intersecting with Γ_2 then gives the result."

## [extrait] Lemma 2.9 et preuve (p. 6)

"The following result on the comparison of two generalised Hadamard states is well known and lies at the basis of the renormalisation of the stress-energy-momentum tensor in the free field case:
Lemma 2.9 For two generalised Hadamard states ω, ω' we have that ω_2 − ω'_2 is smooth iff ω_{2−} − ω'_{2−} is smooth.
Proof. We define w(x_2, x_1) := (ω_2 − ω'_2)(x_2, x_1), w̃(x_2, x_1) := w(x_1, x_2) and w_{2−} := (1/2)(w − w̃) and argue as in the proof of proposition 2.8: WF(w) ⊂ Γ_2, WF(w̃) ⊂ −Γ_2 and hence WF(w) ∩ WF(w̃) = ∅. It then follows from w − w̃ = 2w_{2−} that WF(w_{2−}) = WF(w) ∪ WF(w̃). Now WF(w_{2−}) = ∅ if and only if WF(w) = ∅, which proves the statement."

## [extrait] Proposition 3.2, Corollary 3.3 et commentaire (p. 7-8)

"Proposition 3.2 If ω is a generalised Hadamard state and a generalised free field state with commutator E, then E = −2iω_{2−}, WF(E) ⊂ Γ_2 ∪ −Γ_2 and WF(ω_2) = WF(E) ∩ Γ_2.
Proof. The first equality follows by applying ω to the commutation relations (6). The others follow from the last two items of proposition 2.8."

"Corollary 3.3 If a state ω satisfies the Klein-Gordon equation with parameters m, ξ on a globally hyperbolic spacetime M and the commutation relations with commutator E_{m,ξ}, then it is a generalised Hadamard state if and only if it is a Hadamard state.
Proof. The result of Radzikowski implies that a free field state on a globally hyperbolic spacetime which satisfies the commutation relations with commutator E_{m,ξ} is a Hadamard state if and only if WF(ω_2) = WF(E_{m,ξ}) ∩ Γ_2. The result therefore follows from proposition 3.2."

"We see from proposition 3.2 and lemma 2.9 that for two generalised free field states ω and ω' with commutator functions E and E' respectively, ω_2 − ω'_2 is smooth iff E − E' is smooth."

## [extrait] Proposition 4.1 et preuve (p. 9-10)

"We now start our analysis of the singularities of higher n-point distributions of a generalised free field state with a result that exploits the positivity of the state.
Proposition 4.1 Let ω be a generalised Hadamard state and assume that for n ≥ 1 we have (x_n, k_n; ...; x_1, k_1) ∈ WF(ω_n). Then (x_1, k_1) ∈ V^{*+} ∪ Z and (x_n, k_n) ∈ V^{*−} ∪ Z. In particular, WF(ω_1) = ∅.
Proof. The positivity of ω implies \overline{ω_n(f_n, ..., f_1)} = ω_n(\bar f_1, ..., \bar f_n), and hence the second statement follows from the first. In fact, the positivity allows us to perform the GNS-construction, which yields a representation π_ω of U_M on a Hilbert space H_ω by closable operators and a vector Ω_ω ∈ H_ω such that ω(A) = ⟨Ω_ω, π_ω(A)Ω_ω⟩ for all A ∈ U_M. We can then define the H_ω-valued distributions φ_m(f_m, ..., f_1) := π_ω(f_m ⊗ ... ⊗ f_1)Ω_ω for all m ∈ N. Using the inner product of H_ω we can write:
ω_n(f_n, ..., f_1) = ⟨φ_{n−1}(\bar f_2, ..., \bar f_n), φ_1(f_1)⟩, ω_2(f_2, f_1) = ⟨φ_1(\bar f_2), φ_1(f_1)⟩.
The calculus of Hilbert space-valued distributions (see e.g. [21] proposition 2.2 or [18] theorem A.1.6) now means that (x_n, k_n; ...; x_1, k_1) ∈ WF(ω_n) implies (x_1, k_1) ∈ WF(φ_1) ∪ Z and if k_1 ≠ 0 then (x_1, −k_1; x_1, k_1) ∈ WF(ω_2). The conclusion follows from the assumption that WF(ω_2) ⊂ Γ_2."

## [extrait] Lemma 4.6 et preuve (p. 11-12)

"Lemma 4.6 Consider two generalised Hadamard states ω, ω', which both satisfy commutation relations with the same commutator E such that WF(E) ≠ ∅. For any n ≥ 0 we have that ω_{n+2} − ω'_{n+2} is smooth if and only if ω_n ≡ ω'_n.
Proof. The case n = 0 follows from lemma 2.9. For n ≥ 1 we first suppose that ω_n ≡ ω'_n. For any index 1 ≤ i < n we then have (ω_{n+2} − ω'_{n+2})(x_{n+2}, ..., x_1) = (ω_{n+2} − ω'_{n+2})(x_{n+2}, ..., x_i, x_{i+1}, ..., x_1), where we swapped the indices i and i + 1 and the commutator terms vanish by the assumption. We can therefore permute indices ad lib. and in this way we derive (ω_{n+2} − ω'_{n+2})(x_{n+2}, ..., x_1) = (ω_{n+2} − ω'_{n+2})(x_1, ..., x_{n+2}). Using the assumption that both states are generalised Hadamard states and items two and four of proposition 2.5 we find that WF(ω_{n+2} − ω'_{n+2}) ⊂ Γ_{n+2} ∩ −Γ_{n+2} = ∅. This proves that ω_{n+2} − ω'_{n+2} is smooth.
For the opposite direction we assume that ω_{n+2} − ω'_{n+2} is smooth [...] This contradicts the assumption on E, so we must have w_n ≡ 0.
The same statement still holds when the commutators E and E' of the two states differ by a smooth function."

## Recherche negative : invariance conforme

La requete « conformal invariance of Hadamard condition, conformal coupling » n'a renvoye aucune page de S2 traitant du sujet. ξ n'apparait dans S2 que comme parametre generique du KG (Definition 3.1, Corollary 3.3, Proposition 5.5) et dans le commentaire p. 8 montrant que E_{m,ξ} − E_{m',ξ'} n'est en general pas lisse.
