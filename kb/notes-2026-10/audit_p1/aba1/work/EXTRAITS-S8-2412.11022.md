# Extraits verbatim de S8 : arXiv:2412.11022v1 [gr-qc], 15 Dec 2024, UFIFT-QG-24-08
# "Resumming Photon Loops for Inflationary Gravity", A. J. Foraci et R. P. Woodard
# Source : texte integral obtenu via mcp__alphaXiv__get_paper_content (fullText = true), 2026-10-13.
# Les equations sont retranscrites en notation lineaire depuis le texte extrait du PDF.

## Section 1 : les deux sources de logarithmes seculaires

[extrait, sec. 1] "The struggle to develop such a technique has been long and confusing because secular corrections have two distinct sources, each requiring its own resummation technique. The first source is from what DeWitt and Brehme termed the "tail" part of the graviton propagator [6]. Because the mode functions of dynamical gravitons agree with those of the massless, minimally coupled scalar [7] their propagators agree as well. The tail is the logarithm term of this propagator on D = 4 dimensional de Sitter background,"

[extrait, eq. (4)] i Delta(x;x') = (1/(4 pi^2)) [ 1/(a a' Delta x^2) ] - (H^2/(8 pi^2)) ln[ (1/4) H^2 Delta x^2 ]

[extrait, sec. 1] "Secular corrections from this source can be resummed using a variant of Starobinsky's stochastic formalism [8-11]."

[extrait, sec. 1] "The other source of secular logarithms comes from renormalization. To make the discussion concrete, suppose we employ dimensional regularization in conformal coordinates, in which case interaction vertices inherit a factor of a^D from the measure sqrt(-g). It turns out that the propagator from x^mu to x'^mu goes like 1/(aa')^{D/2-1}, times integer powers of aa', so that D-dependent scale factors cancel from 1-loop diagrams, in both the ultraviolet divergent and finite parts. On the other hand, counterterms inherit D-dependent powers of a from the measure factor, so there is an incomplete cancellation between primitive divergences and counterterms [11],"

[extrait, eq. (5)] (2H)^{D-4}/(D-4) - (a mu)^{D-4}/(D-4) = - ln( mu a / (2H) ) + O(D-4)

[extrait, sec. 1] "Here mu is the usual mass scale of dimensional regularization. The close relation between mu and a(t) in relation (5) suggests that this second source of secular logarithms can be resummed by a variant of the renormalization group [11]."

[extrait, sec. 1, resultats scalaires rappeles, eqs. (7)-(10)]
C_{0i0j}(t,x) = C^{tree}_{0i0j}(t,x) { 1 - (3 hbar G H^2)/(10 pi c^5) ln[a(t)] + ... }   (7)
Psi(t,r) = GM/(a(t) r) { 1 + hbar G/(20 pi c^3 a^2(t) r^2) - (3 hbar G H^2)/(10 pi c^5) ln[a(t)Hr/c] + ... }   (8)
C_{0i0j}(t,x) -> C^{tree}_{0i0j}(t,x) x [a(t)]^{-(3 hbar G H^2)/(10 pi c^5)}   (9)
"These logarithms also derive from the second source (5) and can be resummed using a variant of the renormalization group to give [14],"

## Section 2 : convention de kappa

[extrait, eq. (12)] g_{mu nu}(x) = a^2 [ eta_{mu nu} + kappa h_{mu nu} ] ,  kappa^2 = 16 pi G

## Section 4 : self-energy de Schwinger-Keldysh et sort de la partie non locale

[extrait, eq. (37)] [^{mu nu} Sigma^{rho sigma}](x;x') = - (kappa^2)/(2^8 . 5 . pi^3) C^{alpha beta gamma delta mu nu} x C'^{rho sigma}_{alpha beta gamma delta} [ 8 pi ln(a a') delta^4(x-x') + f_B(x-x') ]

[extrait, eq. (39)] f_B(x-x') = partial^4 { theta(Delta eta - Delta r) ( ln[ mu^2 (Delta eta^2 - Delta r^2) ] - 1 ) }

[extrait, sec. 4] "Note that the Schwinger-Keldysh graviton self-energy is both real and causal, albeit nonlocal."

[extrait, eq. (45)] u(eta,k) = u_0(eta,k) + kappa^2 u_1(eta,k) + kappa^4 u_2(eta,k) + ...

[extrait, eq. (46)] u_0(eta,k) = (H/sqrt(2k^3)) [1 - ik/(aH)] exp[ik/(aH)] = (H/sqrt(2k^3)) [1 + ik eta] e^{-ik eta}

[extrait, eq. (47)] partial_0 u_0 = (H/sqrt(2k^3)) k^2 eta e^{-ik eta} = (i/(2k)) (partial_0^2 - k^2) u_0

[extrait, eq. (49)] (partial_0 + ik) partial_0 u_0(eta,k) = (H/sqrt(2k^3)) k^2 e^{-ik eta} ,  (partial_0 + ik)^2 partial_0 u_0(eta,k) = 0

[extrait, sec. 4] "Of course we can perform the delta function integral in (48), and the nonlocal contribution vanishes when we reflect the derivatives onto partial'_0 u_0(eta',k) and invoke the second identity of (49),"

[extrait, eq. (50)] a^2 [partial_0^2 + 2aH partial_0 + k^2] u_1(eta,k) = - ( ik (partial_0 + ik)^2 )/(2^4 . 5 . pi^2) [ 2 ln(a) partial_0 u_0(eta,k) ]

[extrait, eq. (52)] u_1(eta,k) -> (H/sqrt(2k^3)) x ( i H^2 ln(a) )/(120 pi^2) ( k/(aH) )^3

[extrait, eq. (53)] C_{0i0j}(x) -> C^{tree}_{0i0j}(x) { 1 + (kappa^2 H^2)/(40 pi^2) ln(a) + ... }

[extrait, eq. (54)] Psi(t,r) = GM/(a r) { 1 + kappa^2/(60 pi^2 a^2 r^2) + (kappa^2 H^2)/(40 pi^2) ln(aHr) + ... }

[extrait, sec. 4] "Interestingly, the fractional corrections proportional to kappa^2 H^2 are the same in expressions (53) and (54). The positive sign is opposite to the analogous effects (7-8) engendered by a loop of massless, minimally coupled scalars [13]."

## Section 5 : groupe de renormalisation

[extrait, eq. (55)] Delta L = c_1 R^2 sqrt(-g) + c_2 C^{alpha beta gamma delta} C_{alpha beta gamma delta} sqrt(-g)

[extrait, eq. (56)] c_1 = 0 ,  c_2 = ( mu^{D-4}/(D-4) ) x ( Gamma(D/2) / (2^8 pi^{D/2}) ) x ( (D-2) D / ((D+1)(D-3)^2) )

[extrait, sec. 5] "Because the counterterms have the same form (55) as for Maxwell plus Einstein, the analysis is identical. For general coefficients c_1 and c_2 one finds that a certain combination can be viewed as a field strength renormalization [14],"

[extrait, eq. (57)] delta Z = D [ 2(D-1) c_1 - c_2 ] kappa^2 H^2

[extrait, eq. (58)] gamma = partial ln(1 + delta Z) / partial ln(mu^2) = - (kappa^2 H^2)/(80 pi^2)

[extrait, eq. (59)] [ partial/partial ln(mu) + beta_G partial/partial G + 2 gamma ] G^{(2)} = 0

[extrait, sec. 5] "Because the photon propagator has no tail term, the only secular logarithms from photon loops derive from renormalization (5). This means that factors of ln(mu) are always come in the form ln(mu a), so we can replace the derivative with respect to ln(mu) by a derivative with respect to ln(a) in equation (59). Taking account of the fact that the beta function vanishes at 1-loop gives a simple RG explanation for the laboriously derived results (53-54)."

## Section 6 : forme resommee finale et "late time"

[extrait, sec. 6] "The same analysis can be used to resum these large logarithms to all orders, which we present here with the factors of hbar and c restored,"

[extrait, eq. (60)] C_{0i0j} = C^{tree}_{0i0j} { 1 + (2 hbar G H^2)/(5 pi c^5) ln[a] + ... } -> C^{tree}_{0i0j} x [a(t)]^{(2 hbar G H^2)/(5 pi c^5)}

[extrait, eq. (61)] Psi = GM/(a r) { 1 + (4 hbar G)/(15 pi c^3 a^2 r^2) + (2 hbar G H^2)/(5 pi c^5) ln[aHr/c] + ... } -> GM/(a r) x [a(t)Hr/c]^{(2 hbar G H^2)/(5 pi c^5)}

[extrait, sec. 6] "Note from the fractional power of r in the Newtonian potential that the resulting late time effective field theory cannot be local. Note also that "late time" here means during an endless phase of de Sitter expansion. More work needs to be done to infer what would happen in the current universe after a long phase of primordial expansion, although a very good approximate solution has been obtained for nonlinear sigma models [33] which proves that significant late time effects can persist [34]."

[extrait, sec. 6] "With the possible exception of pure gravity, it seems as if all large loop corrections involving gravity plus matter arise from renormalization (5), with no contribution from the tail part of the propagator (4)."

[extrait, sec. 6] "Because all large loop corrections in gravity plus matter seem to derive from renormalization (5), it would be interesting to see if they persist for the contributions from massive particles. Of course renormalization will certainly induce such logarithms, but it is not yet clear whether or not they will be suppressed by inverse powers of the scale factor."

## Section 2 (jauge) : seule mention de la jauge dans S8

[extrait, sec. 2] "Because the field strength is U(1) gauge invariant, there is no dependence on the electromagnetic gauge fixing."
