# Extraits verbatim de S27 : arXiv:2405.01024v2 [gr-qc], 7 Oct 2024, CCTP-2024-7, UFIFT-QG-24-04
# "Summing Gravitational Effects from Loops of Inflationary Scalars", S. P. Miao, N. C. Tsamis, R. P. Woodard
# Source : texte integral obtenu via mcp__alphaXiv__get_paper_content (fullText = true), 2026-10-13.
# Reference de revue (non presente dans le texte de S27 lui-meme, mais donnee par S8, ref. [14]) :
# Class. Quant. Grav. 41, no.21, 215007 (2024), doi:10.1088/1361-6382/ad7dc8.

## Section 1 : les deux mecanismes de logarithmes

[extrait, sec. 1] "The large logarithms of scalar potential models derive from what DeWitt and Brehme termed the "tail" part [23] of the MMC scalar propagator,"

[extrait, eq. (5)] D = 4 => i Delta(x;x') = (1/(4 pi^2)) 1/(a a' (x-x')^2) - (H^2/(8 pi^2)) ln[ (1/4) H^2 (x-x')^2 ]

[extrait, sec. 1] "The situation when derivative interactions are present is more complicated because renormalization provides a new mechanism for generating large logarithms. When using dimensional regularization it turns out that D-dependent factors of a(t) do not occur in divergent primitive contributions, which are incompletely canceled by counterterms,"

[extrait, eq. (6)] ( Primitive : (2H)^{D-4}/(D-4) ) - ( Counterterm : (mu a)^{D-4}/(D-4) ) = - ln( mu a/(2H) ) + O(D-4)

[extrait, sec. 1] "These sorts of large logarithms are correctly described by a variant of the renormalization group [27]."

## Section 2 : modeles sigma non lineaires, Table 1, validation

[extrait, sec. 2] "Non-linear sigma models have the same h partial h partial h derivative interactions as gravity, and induce the same factors of ln[a(t)] on de Sitter background, but without the complex index structure or the gauge issue."

[extrait, eq. (17)] beta = partial delta lambda / partial ln(mu) = 0 lambda^3 + O(lambda^5)

[extrait, sec. 2] "All the coefficients in (12-15) are determined so that they absorb the primitive divergences of the perturbative diagrams. The leading logarithm renormalized results are most conveniently presented in the form of Table 1 [27, 39]:"

[extrait, legende Table 1] "Table 1: Leading logarithm renormalized perturbative results for the AB model to leading logarithm. Red denotes leading logarithms explained by the stochastic formalism while green denotes those explained by the renormalization group."

[extrait, Table 1, lignes] u_A(eta,k) : { 1 - (lambda^2 H^2)/(32 pi^2) ln(a) + O(lambda^4) } x H/sqrt(2k^3) ; u_B : { 1 + 0 + O(lambda^4) } ; P_A(eta,r) : { 1 - (lambda^2 H^2)/(32 pi^2) ln(a) + (lambda^2 H^2)/(32 pi^2) ln(Hr) + O(lambda^4) } x (KH/(4 pi)) ln(Hr) ; P_B : { 1 - (lambda^2 H^2)/(32 pi^2) ln(Hr) + O(lambda^4) } ; <A> : { 1 + (lambda^2 H^2)/(64 pi^2) ln(a) } x (lambda H^2/(16 pi^2)) ln(a) ; <A^2>_ren : { 1 - (lambda^2 H^2)/(64 pi^2) ln(a) } x (H^2/(4 pi^2)) ln(a) ; <B> = 0 ; <B^2>_ren : { 1 + (3 lambda^2 H^2)/(32 pi^2) ln(a) } x (H^2/(4 pi^2)) ln(a).

[extrait, sec. 2, RG] "For the leading logarithms coming from the ultraviolet sector, the standard QFT re-summation methodology of the renormalization group needs, as well, an extension due to the presence of a curved spacetime: counterterms can be regarded as curvature-dependent renormalizations of the bare parameters present in the original theory."

[extrait, eq. (28)] G_N(x_1,...,x_N; lambda; mu) = G_N(x_1,...,x_N; lambda; mu_0) x [ mu_0/mu ]^{N gamma(lambda)}

[extrait, sec. 2] "* Agreement: Stochastic Analysis. To substantiate that the above re-summations do indeed produce the leading logarithms, we must compare their predictions against the perturbative results of Table 1."

[extrait, sec. 2] "Comparing (29) and (30) with their perturbative counterparts <Omega|A(x)|Omega> and <Omega|A^2(x)|Omega> in Table 1 shows perfect agreement, a highly non-trivial achievement indeed."

[extrait, sec. 2] "* Agreement: Renormalization Group. A similar non-trivial agreement is maintained when we consider the renormalization group analysis and its re-summation of the leading logarithms. For instance, the Callan-Symanzik equation for the composite operator A^2(x) has the form [27],"

[extrait, eq. (31)] [ a partial/partial a + beta partial/partial lambda + gamma_{A^2} ] <Omega|A^2(x)|Omega>_ren = 0

[extrait, eq. (32)] beta = partial delta lambda/partial ln(mu) = 0 + O(lambda^5) ,  gamma_{A^2} = partial ln(Z_{A^2})/partial ln(mu^2) = 0 + O(lambda^4)

[extrait, sec. 2] "Therefore, there should no leading logarithms coming from this analysis to this order (2-loop) and indeed the corresponding perturbative result seen in Table 1 for <Omega|A^2(x)|Omega>_ren confirm this; both leading logarithms are stochastic effects as described above."

[extrait, eq. (33)] Z_{B^2} = 1 - 2 K_{B2} x R + O(lambda^4) => gamma_{B^2} = - (3 lambda^2 H^2)/(16 pi^2) + O(lambda^4 H^4)

[extrait, sec. 2] "so that its associated Callan-Symanzik equation predicts the leading logarithm contribution to this order to be + (3 lambda^2 H^2)/(16 pi^2) which is identical to what is seen in Table 1 for <Omega|B^2(x)|Omega>_ren."

[extrait, sec. 2, Comments] "It turns out that all entries in Table 1 are reproduced by one or the other of the re-summation techniques. Yet another example, is the lambda^0 order term (H^2/(4 pi^2)) ln(a) that appears in the VEV's of Table 1: it comes from the coincidence limit of the scalar propagator and is a stochastic effect; it could not be explained by the renormalization group since it does not obey the Callan-Symanzik equation."

## Section 5 : analyse par le groupe de renormalisation

[extrait, eq. (80)] C_{0i0j}(t,x) = C^{(0)}_{0i0j}(t,x) { 1 - (3 G H^2)/(10 pi) x ln(a) + O(G^2) }

[extrait, eq. (82)] Psi(t,r) = GM/(a r) { 1 + G/(20 pi a^2 r^2) - (3 G H^2)/(10 pi) x ln(aHr) + O(G^2) }

[extrait, eq. (83)] Phi(t,r) = - GM/(a r) { 1 - G/(60 pi a^2 r^2) - (3 G H^2)/(10 pi) x [ln(aHr) + 1] + O(G^2) }

[extrait, sec. 5] "The three leading logarithm corrections (80) and (82-83) are not explained by the induced stress tensor we considered in the previous section. They closely resemble the logarithmic corrections previously found to the electric components of the field strength tensor for plane wave electromagnetic radiation [13], and to the Coulomb potential for a static point charge [12]. Those two results can be explained by a variant of the renormalization group [53], and it turns out that a similar explanation works for the gravitational logarithms (80) and (82-83)."

[extrait, eq. (84)] Delta L = c_1 R^2 sqrt(-g) + c_2 C^{alpha beta gamma delta} C_{alpha beta gamma delta} sqrt(-g)

[extrait, eq. (85)] c_1 = mu^{D-4} ( Gamma(D/2) / (2^8 pi^{D/2}) ) x ( (D-2) / ((D-1)^2 (D-3)(D-4)) )

[extrait, eq. (86)] c_2 = mu^{D-4} ( Gamma(D/2) / (2^8 pi^{D/2}) ) x ( 2 / ((D+1)(D-1)(D-3)^2 (D-4)) )

[extrait, sec. 5] "where mu is the scale of dimensional regularization."

### (a) Dissection des contre-termes, attribution a une renormalisation de champ plutot que de G

[extrait, sec. 5] "Like the non-linear sigma models considered in Section 3, our model (7) is nonrenormalizable. Recall from Section 3 that it was necessary to sort the resulting BPHZ (Bogoliubov, Parasiuk [55], Hepp [56] and Zimmermann [57,58] counterterms into those which can be viewed as renormalizing parameters of the bare theory and those that provide irrelevant higher derivative contributions which do not induce large logarithms. Experience with the large electromagnetic logarithms induced by graviton loops [53] shows that this sometimes requires dissecting the original counterterms."
(Remarque de l'auditeur : le texte renvoie a la "Section 3" pour les modeles sigma, alors que ceux-ci sont traites en Section 2 ; il s'agit d'une incoherence interne de numerotation dans S27.)

[extrait, eq. (87)] Delta L = Delta C H^2 F_{ij} F_{kl} g^{ik} g^{jl} sqrt(-g) + C H^2 F_{mu nu} F_{rho sigma} g^{mu rho} g^{nu sigma} sqrt(-g) + C_4 D^alpha F_{mu nu} D^beta F_{rho sigma} g_{alpha beta} g^{mu rho} g^{nu sigma} sqrt(-g)

[extrait, eq. (88)] delta Z = -4 [ C - (3D-8) C_4 ] H^2

[extrait, sec. 5] "The analogous decomposition of the gravitational counterterms (84) begins by writing the Eddington (R^2) counterterm as the sum of three terms,"

[extrait, eq. (89)] R^2 = ( R - D Lambda )^2 + 2 D Lambda [ R - (D-2) Lambda ] + D(D-4) Lambda^2

[extrait, sec. 5] "(i) The first term in (89) involves products of second derivatives of the graviton field, and explicit computation shows that it engenders no large logarithms [35].
(ii) However, the second term can be viewed either as a renormalization of Newton's constant in the original model (7), or else as a renormalization of the graviton field strength. Because we have no information about higher order couplings it is convenient to adopt the latter interpretation.
(iii) The third term is finite."

[extrait, sec. 5] "The interpretation adopted for the second term in (89) applies as well to the special term arising, at quadratic order, from the term proportional to partial_0^2 h_{nu sigma} in the Weyl counterterm of (84),"

[extrait, eq. (90)] C^{mu nu rho sigma} C_{mu nu rho sigma} = - (2 kappa/a^4) partial_mu partial_rho h_{nu sigma} tilde C^{mu nu rho sigma} + O(kappa^3 h^3) -> - (2 kappa/a^4) partial_0^2 h_{ij} tilde C^{0i0j}

[extrait, sec. 5] "where tilde C^{mu nu rho sigma} is the conformally rescaled Weyl tensor. Direct calculation [35] shows that the two time derivatives can act on scale factors to eventually contribute to the large logarithms (80) and (82-83)."

### Formule de delta Z et gamma

[extrait, sec. 5] "Hence the total field strength renormalization is,"

[extrait, eq. (91)] delta Z = D [ 2(D-1) c_1 - c_2 ] kappa^2 H^2  =>  gamma = partial ln(1 + delta Z) / partial ln(mu^2) = (3 G H^2)/(20 pi)

### Equation de Callan-Symanzik et remplacement de d/d ln mu par d/d ln a

[extrait, sec. 5] "The Callan-Symanzik equation for a 2-point Green's function reads,"

[extrait, eq. (92)] [ partial/partial ln(mu) + beta_G partial/partial G + 2 gamma ] G^{(2)} = 0

[extrait, sec. 5] "The beta-function for G vanishes at the order we are working. From expression (6) we see that factors of the renormalization scale mu come in the form ln(mu a), so that we can replace the derivative with respect to ln(mu) by a derivative with respect to ln(a). The Weyl tensor (80) can be considered as the 2-point correlator between the operator C_{0i0j} and the single particle creation operator; similarly, the potentials (82-83) can be considered as 2-point correlators. It follows that the three large logarithms in (80) and (82-83) can all be explained using the renormalization group."

### (b) Sommation en puissance et reserve sur la course de G

[extrait, sec. 5] "If we ignore possible running of Newton's constant it is even possible to sum up the effects to conclude,"

[extrait, eq. (93)] C_{0i0j}(t,x) -> C^{(0)}_{0i0j}(t,x) x [a(t)]^{-(3 G H^2)/(10 pi)}

[extrait, eq. (94)] Psi(t,r) -> GM/(a(t) r) x [a(t) H r]^{-(3 G H^2)/(10 pi)}

[extrait, eq. (95)] Phi(t,r) -> - GM/(a(t) r) x [a(t) H r]^{-(3 G H^2)/(10 pi)}

## Section 6 : epilogue, reserves

[extrait, sec. 6] "These logarithms are described by a variant of the renormalization group in which some portion of the BPHZ counterterms can be regarded as renormalizing couplings or field strengths of the original theory. That procedure was described in Section 2 for non-linear sigma models, and we applied it in Section 5 to the large logarithms (80) and (82-83) which occur in our model (7). The two BPHZ counterterms (84) can be regarded as giving rise to a graviton field strength renormalization (91) which explains all three of the large logarithms. If we ignore possible running of Newton's constant, it is even possible to give fully resummed results (93-95). We remark that it should be possible to determine any running of G by computing the 1PI 3-point function, the same as has recently been done for non-linear sigma models [39]."

[extrait, sec. 6] "Finally, we expect the need for more counterterms than just the two covariant possibilities (84), owing to the same de Sitter breaking which produced the noncovariant Delta C counterterm (87) for electromagnetism."

[extrait, sec. 3, convention de kappa] "Here and henceforth kappa^2 = 16 pi G is the loop-counting parameter of quantum gravity."
