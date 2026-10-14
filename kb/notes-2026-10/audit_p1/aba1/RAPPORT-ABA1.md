# RAPPORT ABA-1 : lecture aveugle de S8 et S27, et conversion

Auditeur froid, isole. Date : 2026-10-13. Perimetre : uniquement /home/claude/audit_p1/aba1/ et les textes integraux des deux sources obtenus via alphaXiv (get_paper_content, fullText = true). Aucun autre fichier ni contexte consulte.

Etiquettes : [extrait] citation verbatim avec numero d'equation ou de section ; [calcule] resultat sympy ; [derive] deduction de l'auditeur a partir des extraits.

Fichiers de travail (empreintes sha256 en section 7) : work/EXTRAITS-S8-2412.11022.md, work/EXTRAITS-S27-2405.01024.md, work/conversion_aba1.py, work/conversion_aba1.out, work/SHA256SUMS.txt.

Avertissement de transcription : les equations ci-dessous sont retranscrites en notation lineaire a partir du texte extrait du PDF ; les numeros d'equation sont ceux des sources.

---

## 1. Identification des sources

### S8
- Titre : "Resumming Photon Loops for Inflationary Gravity".
- Auteurs : A. J. Foraci, R. P. Woodard (University of Florida).
- Date : arXiv:2412.11022v1 [gr-qc], 15 decembre 2024 ; numero interne UFIFT-QG-24-08.
- Type : prepublication (v1). Aucune reference de revue ne figure dans le texte lu. [derive] Le statut de publication eventuelle posterieure n'est pas verifiable a partir du texte seul.
- Resume [derive du resume et des conclusions] : reexamen de la contribution a une boucle du photon au self-energy du graviton sur de Sitter (resultat anterieur de Wang et Woodard, ref. [16] de S8). (i) Demonstration qu'il n'existe pas d'obstacle local a la conservation (eq. 30, proportionnelle a D-4), contrairement au cas du scalaire MMC ; correlation avec l'absence de contre-terme R^2 (c_1 = 0) et avec l'annulation du tenseur energie-impulsion induit par le photon dans un champ graviton constant (eq. 34). (ii) Calcul de la correction seculaire a une boucle aux composantes electriques du tenseur de Weyl d'une onde gravitationnelle plane (eq. 53), de meme coefficient que la correction au potentiel newtonien (eq. 54), de signe positif (oppose au cas scalaire). (iii) Resommation des deux par une variante du groupe de renormalisation (sec. 5, eqs. 60-61).

### S27
- Titre : "Summing Gravitational Effects from Loops of Inflationary Scalars".
- Auteurs : S. P. Miao (NCKU Tainan), N. C. Tsamis (Crete), R. P. Woodard (Florida, auteur correspondant).
- Date : arXiv:2405.01024v2 [gr-qc], 7 octobre 2024 (v2) ; numeros internes CCTP-2024-7, UFIFT-QG-24-04.
- Type : publie. Le texte de S27 lui-meme ne porte pas de reference de revue, mais S8 le cite (ref. [14]) comme : Class. Quant. Grav. 41, no. 21, 215007 (2024), doi:10.1088/1361-6382/ad7dc8. [derive] La version v2 du 7 octobre 2024 est compatible avec une version acceptee.
- Resume [derive du resume et de l'epilogue] : procedure de resommation des grands logarithmes induits dans la gravite par une boucle de scalaire MMC. Sec. 2 : rappel des modeles sigma non lineaires (modele AB), Table 1 des logarithmes dominants et de leur explication (stochastique ou RG). Sec. 3 : integration du scalaire dans l'equation d'Einstein pour un champ graviton constant, equivalente au remplacement H^2 -> -g~_00 H^2 (eq. 42), donnant un tenseur induit (eq. 48) qui explique la renormalisation finie de la constante cosmologique necessaire a la conservation. Sec. 4 : extension conservee de ce tenseur par un lagrangien f(R) (eqs. 57-69), non unique. Sec. 5 : explication par une variante du groupe de renormalisation des logarithmes de C_0i0j (eq. 80) et des potentiels Psi, Phi (eqs. 82-83), avec resommation en puissance (eqs. 93-95) sous reserve de la course de G. Sec. 6 : perspectives pour les boucles de gravitons.

---

## 2. S8 : releve detaille

### 2.1 Convention de kappa
[extrait, eq. (12)] g_{mu nu}(x) = a^2 [ eta_{mu nu} + kappa h_{mu nu} ], kappa^2 = 16 pi G.

### 2.2 Correction a une boucle du Weyl electrique (photon)
[extrait, eq. (53)] C_{0i0j}(x) -> C^{tree}_{0i0j}(x) { 1 + (kappa^2 H^2)/(40 pi^2) ln(a) + ... }

Correction au potentiel newtonien, rappelee de la ref. [16] de S8 :
[extrait, eq. (54)] Psi(t,r) = GM/(a r) { 1 + kappa^2/(60 pi^2 a^2 r^2) + (kappa^2 H^2)/(40 pi^2) ln(aHr) + ... }

[extrait, sec. 4] "Interestingly, the fractional corrections proportional to kappa^2 H^2 are the same in expressions (53) and (54). The positive sign is opposite to the analogous effects (7-8) engendered by a loop of massless, minimally coupled scalars [13]."

Etapes intermediaires (sec. 4) : mode fonction a l'ordre zero [extrait, eq. (46)] u_0 = (H/sqrt(2k^3)) [1 + ik eta] e^{-ik eta} ; correction tardive [extrait, eq. (52)] u_1(eta,k) -> (H/sqrt(2k^3)) x (i H^2 ln(a))/(120 pi^2) (k/(aH))^3.

### 2.3 Forme resommee finale (section 6, hbar et c restaures)
[extrait, eq. (60)] C_{0i0j} = C^{tree}_{0i0j} { 1 + (2 hbar G H^2)/(5 pi c^5) ln[a] + ... } -> C^{tree}_{0i0j} x [a(t)]^{(2 hbar G H^2)/(5 pi c^5)}

[extrait, eq. (61)] Psi = GM/(a r) { 1 + (4 hbar G)/(15 pi c^3 a^2 r^2) + (2 hbar G H^2)/(5 pi c^5) ln[aHr/c] + ... } -> GM/(a r) x [a(t)Hr/c]^{(2 hbar G H^2)/(5 pi c^5)}

[calcule] Coherence interne : kappa^2 H^2/(40 pi^2) avec kappa^2 = 16 pi G vaut 2 G H^2/(5 pi), identique au coefficient de (60). Verifie par sympy (section 6 ci-dessous).

### 2.4 Contre-termes, delta Z, gamma, Callan-Symanzik (section 5)
[extrait, eq. (55)] Delta L = c_1 R^2 sqrt(-g) + c_2 C^{alpha beta gamma delta} C_{alpha beta gamma delta} sqrt(-g)

[extrait, eq. (56)] c_1 = 0, c_2 = (mu^{D-4}/(D-4)) x (Gamma(D/2)/(2^8 pi^{D/2})) x ((D-2) D/((D+1)(D-3)^2))

[extrait, eq. (57)] delta Z = D [ 2(D-1) c_1 - c_2 ] kappa^2 H^2

[extrait, eq. (58)] gamma = partial ln(1 + delta Z)/partial ln(mu^2) = - (kappa^2 H^2)/(80 pi^2)

[extrait, eq. (59)] [ partial/partial ln(mu) + beta_G partial/partial G + 2 gamma ] G^{(2)} = 0

[extrait, sec. 5] "Because the photon propagator has no tail term, the only secular logarithms from photon loops derive from renormalization (5). This means that factors of ln(mu) are always come in the form ln(mu a), so we can replace the derivative with respect to ln(mu) by a derivative with respect to ln(a) in equation (59). Taking account of the fact that the beta function vanishes at 1-loop gives a simple RG explanation for the laboriously derived results (53-54)."

[derive] S8 ne derive pas lui-meme la formule (57) : il l'importe de S27 (ref. [14]) en invoquant l'identite de forme des contre-termes ("Because the counterterms have the same form (55) as for Maxwell plus Einstein, the analysis is identical").

### 2.5 Contribution non locale du self-energy au mode graviton (section 4)
Le self-energy de Schwinger-Keldysh est decompose en une partie locale et une partie non locale :
[extrait, eq. (37)] [^{mu nu} Sigma^{rho sigma}](x;x') = -(kappa^2)/(2^8 . 5 . pi^3) C^{alpha beta gamma delta mu nu} x C'^{rho sigma}_{alpha beta gamma delta} [ 8 pi ln(a a') delta^4(x-x') + f_B(x-x') ]

[extrait, eq. (39)] f_B(x-x') = partial^4 { theta(Delta eta - Delta r) ( ln[mu^2(Delta eta^2 - Delta r^2)] - 1 ) }

[extrait, sec. 4] "Note that the Schwinger-Keldysh graviton self-energy is both real and causal, albeit nonlocal."

Sort de la partie non locale sur le mode de de Sitter u_0 :
[extrait, eq. (49)] (partial_0 + ik) partial_0 u_0(eta,k) = (H/sqrt(2k^3)) k^2 e^{-ik eta}, (partial_0 + ik)^2 partial_0 u_0(eta,k) = 0

[extrait, sec. 4] "Of course we can perform the delta function integral in (48), and the nonlocal contribution vanishes when we reflect the derivatives onto partial'_0 u_0(eta',k) and invoke the second identity of (49),"

[extrait, eq. (50)] a^2 [partial_0^2 + 2aH partial_0 + k^2] u_1(eta,k) = -(ik (partial_0 + ik)^2)/(2^4 . 5 . pi^2) [ 2 ln(a) partial_0 u_0(eta,k) ]

[derive] Autrement dit : sur le mode de de Sitter u_0, la partie non locale f_B du self-energy ne contribue PAS a l'ordre kappa^2 ; elle s'annule par l'identite (partial_0 + ik)^2 partial_0 u_0 = 0 (seconde identite de (49)), apres reflexion des derivees. Seul le terme local 8 pi ln(aa') delta^4 survit et engendre le ln(a) de (53). Le logarithme seculaire du Weyl est donc entierement d'origine "renormalisation" (terme local en ln(aa')), et non d'origine "queue" ni d'origine non locale.

### 2.6 Les deux sources de logarithmes seculaires (section 1)
Premiere source :
[extrait, sec. 1] "The first source is from what DeWitt and Brehme termed the "tail" part of the graviton propagator [6]. [...] The tail is the logarithm term of this propagator on D = 4 dimensional de Sitter background,"
[extrait, eq. (4)] i Delta(x;x') = (1/(4 pi^2)) [1/(a a' Delta x^2)] - (H^2/(8 pi^2)) ln[(1/4) H^2 Delta x^2]
[extrait, sec. 1] "Secular corrections from this source can be resummed using a variant of Starobinsky's stochastic formalism [8-11]."

Seconde source :
[extrait, sec. 1] "The other source of secular logarithms comes from renormalization. [...] counterterms inherit D-dependent powers of a from the measure factor, so there is an incomplete cancellation between primitive divergences and counterterms [11],"
[extrait, eq. (5)] (2H)^{D-4}/(D-4) - (a mu)^{D-4}/(D-4) = - ln(mu a/(2H)) + O(D-4)
[extrait, sec. 1] "Here mu is the usual mass scale of dimensional regularization. The close relation between mu and a(t) in relation (5) suggests that this second source of secular logarithms can be resummed by a variant of the renormalization group [11]."

Laquelle s'applique au photon : la seconde (renormalisation), explicitement.
[extrait, sec. 5] "Because the photon propagator has no tail term, the only secular logarithms from photon loops derive from renormalization (5)."
[extrait, sec. 6] "With the possible exception of pure gravity, it seems as if all large loop corrections involving gravity plus matter arise from renormalization (5), with no contribution from the tail part of the propagator (4)."

Relation entre mu et a qui motive le procede : eq. (5), la combinaison ln(mu a/(2H)). [derive] C'est cette apparition systematique de mu sous la forme mu a qui justifie, en sec. 5, de remplacer partial/partial ln(mu) par partial/partial ln(a) dans (59).

---

## 3. S27 : releve detaille

### 3.1 Formule de delta Z et valeur de gamma
[extrait, eq. (85)] c_1 = mu^{D-4} (Gamma(D/2)/(2^8 pi^{D/2})) x ((D-2)/((D-1)^2 (D-3)(D-4)))
[extrait, eq. (86)] c_2 = mu^{D-4} (Gamma(D/2)/(2^8 pi^{D/2})) x (2/((D+1)(D-1)(D-3)^2 (D-4)))
[extrait, eq. (91)] delta Z = D [ 2(D-1) c_1 - c_2 ] kappa^2 H^2  =>  gamma = partial ln(1 + delta Z)/partial ln(mu^2) = (3 G H^2)/(20 pi)
Convention : [extrait, sec. 3] "Here and henceforth kappa^2 = 16 pi G is the loop-counting parameter of quantum gravity."

Valeur de gamma pour le scalaire MMC : gamma = 3 G H^2/(20 pi) (eq. 91), soit [calcule] 3 kappa^2 H^2/(320 pi^2).

### 3.2 Equation de Callan-Symanzik
[extrait, eq. (92)] [ partial/partial ln(mu) + beta_G partial/partial G + 2 gamma ] G^{(2)} = 0

### 3.3 Justification du remplacement d/d ln mu -> d/d ln a
[extrait, sec. 5] "The beta-function for G vanishes at the order we are working. From expression (6) we see that factors of the renormalization scale mu come in the form ln(mu a), so that we can replace the derivative with respect to ln(mu) by a derivative with respect to ln(a). The Weyl tensor (80) can be considered as the 2-point correlator between the operator C_{0i0j} and the single particle creation operator; similarly, the potentials (82-83) can be considered as 2-point correlators. It follows that the three large logarithms in (80) and (82-83) can all be explained using the renormalization group."
avec [extrait, eq. (6)] (Primitive : (2H)^{D-4}/(D-4)) - (Counterterm : (mu a)^{D-4}/(D-4)) = - ln(mu a/(2H)) + O(D-4).

[derive] La justification est de meme nature que dans S8 : un argument de forme (mu apparait toujours dans ln(mu a)), et non une demonstration generale. Elle est posee pour l'ordre une boucle, avec beta_G = 0 a cet ordre.

### 3.4 (a) Dissection des contre-termes, attribution a une renormalisation de champ plutot que de G
[extrait, sec. 5] "Like the non-linear sigma models considered in Section 3, our model (7) is nonrenormalizable. Recall from Section 3 that it was necessary to sort the resulting BPHZ (Bogoliubov, Parasiuk [55], Hepp [56] and Zimmermann [57,58] counterterms into those which can be viewed as renormalizing parameters of the bare theory and those that provide irrelevant higher derivative contributions which do not induce large logarithms. Experience with the large electromagnetic logarithms induced by graviton loops [53] shows that this sometimes requires dissecting the original counterterms."
(Note d'auditeur : les modeles sigma sont en fait traites en Section 2 de S27 ; le renvoi "Section 3" est une incoherence interne de numerotation.)

[extrait, sec. 5] "The analogous decomposition of the gravitational counterterms (84) begins by writing the Eddington (R^2) counterterm as the sum of three terms,"
[extrait, eq. (89)] R^2 = (R - D Lambda)^2 + 2 D Lambda [R - (D-2) Lambda] + D(D-4) Lambda^2

[extrait, sec. 5] "(i) The first term in (89) involves products of second derivatives of the graviton field, and explicit computation shows that it engenders no large logarithms [35].
(ii) However, the second term can be viewed either as a renormalization of Newton's constant in the original model (7), or else as a renormalization of the graviton field strength. Because we have no information about higher order couplings it is convenient to adopt the latter interpretation.
(iii) The third term is finite."

[extrait, sec. 5] "The interpretation adopted for the second term in (89) applies as well to the special term arising, at quadratic order, from the term proportional to partial_0^2 h_{nu sigma} in the Weyl counterterm of (84),"
[extrait, eq. (90)] C^{mu nu rho sigma} C_{mu nu rho sigma} = -(2 kappa/a^4) partial_mu partial_rho h_{nu sigma} tilde C^{mu nu rho sigma} + O(kappa^3 h^3) -> -(2 kappa/a^4) partial_0^2 h_{ij} tilde C^{0i0j}
[extrait, sec. 5] "Direct calculation [35] shows that the two time derivatives can act on scale factors to eventually contribute to the large logarithms (80) and (82-83)."
[extrait, sec. 5] "Hence the total field strength renormalization is," (suivi de l'eq. 91).

[derive] Points saillants : le choix "renormalisation de champ" plutot que "renormalisation de G" est presente comme une commodite ("it is convenient to adopt the latter interpretation"), motivee par l'absence d'information sur les couplages d'ordre superieur. La contribution du terme de Weyl repose sur un "calcul direct" de la ref. [35] (arXiv:2405.00116), non reproduit dans S27.

### 3.5 (b) Sommation en puissance et reserve sur la course de G
[extrait, sec. 5] "If we ignore possible running of Newton's constant it is even possible to sum up the effects to conclude,"
[extrait, eq. (93)] C_{0i0j}(t,x) -> C^{(0)}_{0i0j}(t,x) x [a(t)]^{-(3 G H^2)/(10 pi)}
[extrait, eq. (94)] Psi(t,r) -> GM/(a(t) r) x [a(t) H r]^{-(3 G H^2)/(10 pi)}
[extrait, eq. (95)] Phi(t,r) -> -GM/(a(t) r) x [a(t) H r]^{-(3 G H^2)/(10 pi)}

Reserve reiteree en epilogue :
[extrait, sec. 6] "If we ignore possible running of Newton's constant, it is even possible to give fully resummed results (93-95). We remark that it should be possible to determine any running of G by computing the 1PI 3-point function, the same as has recently been done for non-linear sigma models [39]."

Autre reserve (contre-termes supplementaires attendus pour les boucles de gravitons) :
[extrait, sec. 6] "Finally, we expect the need for more counterterms than just the two covariant possibilities (84), owing to the same de Sitter breaking which produced the noncovariant Delta C counterterm (87) for electromagnetism."

### 3.6 (c) Statut de validation de la variante RG (section 2, modeles sigma, Table 1)
Ce que dit S27 :
[extrait, sec. 2] "To substantiate that the above re-summations do indeed produce the leading logarithms, we must compare their predictions against the perturbative results of Table 1."
[extrait, sec. 2] "A similar non-trivial agreement is maintained when we consider the renormalization group analysis and its re-summation of the leading logarithms."
[extrait, eq. (33)] Z_{B^2} = 1 - 2 K_{B2} x R + O(lambda^4) => gamma_{B^2} = -(3 lambda^2 H^2)/(16 pi^2) + O(lambda^4 H^4)
[extrait, sec. 2] "so that its associated Callan-Symanzik equation predicts the leading logarithm contribution to this order to be + (3 lambda^2 H^2)/(16 pi^2) which is identical to what is seen in Table 1 for <Omega|B^2(x)|Omega>_ren."
[extrait, sec. 2] "It turns out that all entries in Table 1 are reproduced by one or the other of the re-summation techniques."
[extrait, sec. 2] "Therefore, there should no leading logarithms coming from this analysis to this order (2-loop) and indeed the corresponding perturbative result seen in Table 1 for <Omega|A^2(x)|Omega>_ren confirm this; both leading logarithms are stochastic effects as described above."
[extrait, legende Table 1] "Red denotes leading logarithms explained by the stochastic formalism while green denotes those explained by the renormalization group."

Lecture de l'auditeur [derive] :
- La validite de la variante RG n'est PAS prouvee dans S27 : aucun theoreme, aucune demonstration generale. Pour le formalisme stochastique, S27 renvoie a une preuve externe ("Starobinsky's technique can be proven to reproduce each order's leading logarithms [19]"), mais aucune affirmation analogue n'est faite pour la variante RG.
- La validation consiste en une COMPARAISON avec des resultats perturbatifs (Table 1 du modele AB, a l'ordre lambda^2, soit une boucle pour les quantites concernees ; "this order (2-loop)" pour <A^2>, ou la conclusion est l'absence de logarithme RG). Les coefficients verifies (gamma_{B^2}, u_A, P_A, P_B) sont au premier ordre non trivial.
- Aucune verification de la resommation en puissance (eq. 28 ou eqs. 93-95) a un ordre superieur (ordre lambda^4 ou G^2) n'est presentee ; les entrees de la Table 1 sont toutes a O(lambda^4) pres.
- Pour le modele gravitationnel (sec. 5), la validation est la reproduction des trois coefficients a une boucle (80), (82), (83) par un seul gamma ; c'est une coherence a une boucle, pas un test de la resommation.

---

## 4. Independance de jauge, limite a -> infini, e-folds, deux boucles, "late time"

### 4.1 Independance de jauge gravitationnelle des logarithmes induits par la matiere
- S8 : NON discutee. La seule mention de jauge concerne la jauge electromagnetique U(1) : [extrait, sec. 2] "Because the field strength is U(1) gauge invariant, there is no dependence on the electromagnetic gauge fixing." Rien sur la jauge gravitationnelle (le graviton est externe/classique dans l'equation effective linearisee (35), et le calcul a une boucle de matiere ne fixe pas de jauge gravitationnelle quantique). [derive] S8 ne pose ni ne traite la question de l'invariance de jauge gravitationnelle des coefficients de ln(a).
- S27 : NON discutee de facon directe. Mentions indirectes seulement : [extrait, sec. 2] les modeles sigma reproduisent les logarithmes "without the complex index structure or the gauge issue" ; [extrait, sec. 5, note 10] "The non-covariant Delta C counterterm arises from the unavoidable breaking of de Sitter invariance in the graviton propagator." (ceci concerne les boucles de gravitons, pas les boucles de matiere) ; [extrait, sec. 6] attente de contre-termes non covariants supplementaires pour les boucles de gravitons. [derive] Aucune des deux sources n'affirme ni ne demontre l'independance de jauge gravitationnelle des logarithmes induits par la matiere.

### 4.2 Ce qui n'est PAS discute (les deux sources)
- Jauge gravitationnelle : non discutee (voir 4.1).
- Limite a -> infini : non discutee en tant que telle. Les formes resommees (S8 eqs. 60-61 ; S27 eqs. 93-95) sont ecrites comme des lois de puissance de a(t) sans examen de leur domaine de validite, de leur convergence, ni de la limite formelle. [derive] La fleche "->" est une sommation formelle de la serie geometrique des logarithmes dominants, pas une analyse asymptotique.
- Nombre maximal d'e-folds : non discute. Aucune borne sur ln(a), aucune estimation du nombre d'e-folds a partir duquel kappa^2 H^2 ln(a) ~ 1, dans aucune des deux sources. [derive] Seule une affirmation qualitative figure en S8 sec. 1 ("During a prolonged period of inflation these secular corrections can become large enough that perturbation theory breaks down") et en S27 sec. 1 et 6 ("Over a prolonged period of inflation these factors must overwhelm even the smallest coupling constant").
- Verification a deux boucles : non effectuee. Ni S8 ni S27 ne presentent de calcul a deux boucles (ordre kappa^4 ou G^2) pour la gravite + matiere qui testerait le terme ln^2(a) predit par la resommation. S8 le dit implicitement : [extrait, sec. 4] "Because we only know the graviton self-energy at 1-loop order the only way to solve equation (44) is perturbatively". S27 ne cite la mention "2-loop" que pour <A^2> dans le modele AB (sec. 2), ou la conclusion est l'absence de logarithme RG.

### 4.3 Ce que S8 dit de "late time"
[extrait, sec. 6] "Note from the fractional power of r in the Newtonian potential that the resulting late time effective field theory cannot be local. Note also that "late time" here means during an endless phase of de Sitter expansion. More work needs to be done to infer what would happen in the current universe after a long phase of primordial expansion, although a very good approximate solution has been obtained for nonlinear sigma models [33] which proves that significant late time effects can persist [34]."

[derive] S8 restreint donc explicitement la portee de ses resultats resommes a une phase de de Sitter sans fin ; la transposition a l'univers actuel apres l'inflation est declaree ouverte. L'usage de "late time" en sec. 4 (eqs. 52-53, "late time solution", "late time limiting form") designe simplement la limite k/(aH) -> 0 (mode super-horizon) dans ce meme cadre de Sitter.

---

## 5. Conversion [calcule] (sympy 1.14, script work/conversion_aba1.py, sortie work/conversion_aba1.out)

Conventions posees : kappa^2 = 16 pi G (S8 et S27) ; kappa_P^2 = 8 pi G, donc kappa^2 = 2 kappa_P^2 ; b = (N_S + 6 N_F + 12 N_V)/(120 (4 pi)^2).

### 5.1 Coefficient du ln a de S8 (photon) sous la forme n b kappa_P^2 H^2
- Coefficient de S8, eq. (53) : kappa^2 H^2/(40 pi^2) = 2 G H^2/(5 pi) = kappa_P^2 H^2/(20 pi^2). Egalite avec l'eq. (60) verifiee.
- b(photon) = b(N_S = 0, N_F = 0, N_V = 1) = 12/(120 x 16 pi^2) = 1/(160 pi^2).
- n = [kappa_P^2 H^2/(20 pi^2)] / [kappa_P^2 H^2/(160 pi^2)] = 8.

Resultat : coefficient du ln a de S8 pour le photon = + 8 b kappa_P^2 H^2, avec n = 8 (signe positif).

Complement (non demande mais utile pour la comparaison) : pour le scalaire MMC de S27, eq. (80), le coefficient est - 3 G H^2/(10 pi) ; avec b(N_S = 1) = 1/(1920 pi^2), on obtient |coefficient| = 72 b kappa_P^2 H^2, soit n = -72 avec le signe de (80). [derive] Le rapport des coefficients photon/scalaire vaut donc (8 x 12)/(72 x 1) = 4/3 en valeur absolue, c'est-a-dire que les coefficients NE sont PAS dans le rapport des poids 12 : 1 de b ; la normalisation par b ne rend donc pas les deux resultats "universels" avec un meme n.

### 5.2 gamma de S8 a partir de c_2 (eq. 56) et exposant -2 gamma
- Avec c_1 = 0, delta Z (eq. 57) = -D c_2 kappa^2 H^2.
- gamma = partial ln(1+delta Z)/partial ln(mu^2) = (1/2) partial delta Z/partial ln mu + O(kappa^4) ; partial mu^{D-4}/partial ln mu = (D-4) mu^{D-4} annule le pole 1/(D-4).
- Limite D -> 4 : gamma = -(1/2) x 4 x (1/(256 pi^2)) x (2 x 4/(5 x 1)) kappa^2 H^2 = -kappa^2 H^2/(80 pi^2) = -G H^2/(5 pi).
- Accord avec l'eq. (58) : OUI.
- -2 gamma = kappa^2 H^2/(40 pi^2) = 2 G H^2/(5 pi) : egal au coefficient du ln a de (53) et a l'exposant de (60). Verifie : OUI.

### 5.3 gamma de S27 a partir de c_1, c_2 (eqs. 85-86) et comparaison a la valeur affichee
- delta Z (eq. 91) = D [2(D-1) c_1 - c_2] kappa^2 H^2.
- Limite D -> 4 de (1/2) partial delta Z/partial ln mu : (kappa^2 H^2/(128 pi^2)) x [4/3 - 2/15] = (kappa^2 H^2/(128 pi^2)) x 6/5 = 3 kappa^2 H^2/(320 pi^2) = 3 G H^2/(20 pi).
- Contributions separees : part de c_1 = + G H^2/(6 pi) ; part de c_2 = - G H^2/(60 pi) ; somme = 3 G H^2/(20 pi).
- Accord avec la valeur affichee en (91), gamma = 3 G H^2/(20 pi) : OUI.
- -2 gamma = -3 G H^2/(10 pi) : egal a l'exposant de (93)-(95) et au coefficient de (80), (82), (83). Verifie : OUI.

### 5.4 Bilan de la conversion
| Quantite | Valeur source | Recalcul sympy | Accord |
|---|---|---|---|
| S8 coef ln a (eq. 53) | kappa^2 H^2/(40 pi^2) | 2 G H^2/(5 pi) = 8 b kappa_P^2 H^2 (n = 8) | oui |
| S8 gamma (eq. 58) | -kappa^2 H^2/(80 pi^2) | -G H^2/(5 pi) | oui |
| S8 exposant (eq. 60) | +2 G H^2/(5 pi) | -2 gamma | oui |
| S27 gamma (eq. 91) | 3 G H^2/(20 pi) | 3 G H^2/(20 pi) | oui |
| S27 exposant (eq. 93) | -3 G H^2/(10 pi) | -2 gamma | oui |

---

## 6. Observations de l'auditeur [derive]

1. Les deux sources sont du meme groupe (Woodard et collaborateurs) ; S8 importe de S27 la formule de delta Z (eq. 57 = eq. 91) sans la rederiver, sur la base de l'identite de forme des contre-termes. L'argument de "dissection" des contre-termes (S27 sec. 5, points (i)-(iii)) est donc le seul fondement de la formule utilisee dans les deux articles, et il contient un choix declare de commodite (interpretation "field strength" plutot que "renormalisation de G").
2. Le remplacement partial/partial ln mu -> partial/partial ln a repose, dans les deux sources, sur l'observation que mu n'apparait que dans ln(mu a) (eq. 5 de S8, eq. 6 de S27), a une boucle. Aucune des deux ne presente de preuve que cette structure persiste aux ordres superieurs.
3. La resommation en loi de puissance est explicitement conditionnelle dans S27 ("If we ignore possible running of Newton's constant") ; S8 la presente sans cette reserve explicite en sec. 6, mais en sec. 5 note que "the beta function vanishes at 1-loop", ce qui revient a la meme hypothese.
4. Le statut epistemique de la variante RG dans S27 est : coherence verifiee avec des resultats perturbatifs au premier ordre non trivial (Table 1 pour le modele AB ; eqs. 80, 82, 83 pour la gravite), sans preuve generale ni test a l'ordre suivant.
5. S8 limite explicitement "late time" a une phase de de Sitter eternelle et declare ouverte la question de l'univers actuel.
6. Incoherence mineure dans S27 : renvoi a "Section 3" pour les modeles sigma, traites en Section 2.
7. Normalisation par b : le coefficient photon correspond a n = 8 ; le coefficient scalaire MMC de S27 correspondrait a n = -72. Les deux ne partagent donc pas un facteur universel commun apres division par b, ce qui est coherent avec le fait que ni S8 ni S27 n'invoquent le coefficient d'anomalie conforme (N_S + 6 N_F + 12 N_V) comme origine de leurs logarithmes.

---

## 7. Empreintes sha256 des fichiers de travail

```
03cc2dfe75acb894c906ffd3eed2654084e189bf76e1ed49105dc3aea0ed7efb  work/EXTRAITS-S8-2412.11022.md
217169762a4a6f9c4431822342a6db5b78430556a20cfaa01331b9bb983b8778  work/EXTRAITS-S27-2405.01024.md
f4df5449216408488066e19235ca2fefe063c23e85c23b70d1000c9eacb421b6  work/conversion_aba1.py
62a124731f6cadd1696f63d04009c8a16ad06ac3d934cab16b45016adb51af29  work/conversion_aba1.out
```
(Liste egalement dans work/SHA256SUMS.txt.)

Fin du rapport ABA-1.
