# Consigne FA-1 (derivation en cecite stricte)

Vous ne recevez que cette consigne. Ne cherchez aucun contexte exterieur. Repondez en francais, sans tirets longs, avec des formules explicites, en un rapport structure Q1 a Q5 puis une section « Verdict » (choisir : CONFIRME / CONFIRME AVEC CORRECTIONS / INFIRME, avec motifs). Chaque affirmation doit etre derivee, pas affirmee ; indiquez ce que vous n'avez pas pu verifier.

## Cadre
Conventions de H. Friedrich (arXiv:1311.0700) : signature (-,+,+,+) ; metrique physique ghat = Omega^-2 g ; Einstein : Rhat_ab - (1/2) Rhat ghat_ab + lambda ghat_ab = kappa That_ab, d'ou -Rhat + 4 lambda = kappa That. Relations conformes (g flat pour le calcul) : Rhat_ab = 2 Omega^-1 nabla_a nabla_b Omega + (Omega^-1 box Omega - 3 Omega^-2 |dOmega|^2) g_ab ; Rhat = Omega^2 (6 Omega^-1 box Omega - 12 Omega^-2 |dOmega|^2). Equations conformes : (2.14) nabla_a nabla_b Omega = s g_ab - Omega L_ab + (kappa/2) Omega T*_ab avec T*_ab = That_ab - (1/4) That ghat_ab ; (2.15) nabla_a s = -nabla^b Omega L_ba + (kappa/2) nabla^b Omega T*_ba - (kappa/24) Omega nablahat_a That ; (3.8) |dOmega|^2 = -lambda/3 + 2 Omega s + (kappa/12) Omega^2 (Omega^-2 That) ; (2.17) nabla_mu W^mu_rho nu lambda = 2 Omega^-1 nablahat_[nu Lhat_lambda]rho avec Lhat_ab = (kappa/2)(That_ab - (1/3) That ghat_ab) + (lambda/6) ghat_ab. « Formellement regulier » (Friedrich, th. 3.1) : les seconds membres, exprimes en fonction des inconnues rescalees (Omega, dOmega, s, L, W, champs rescales et leurs derivees), ne contiennent aucun terme Omega^-k, k > 0.

Matiere physique : L = -(1/4) F^2 - ghat^{ab} (D_a H)^dagger D_b H - m^2 |H|^2 - lambda_h |H|^4 - xi Rhat |H|^2 + psibar (i gamma.D - y H) psi, D = nabla - i e A, H complexe (une composante suffit ; le doublet est une somme), A de poids conforme 0. Inconnues rescalees : A_a (inchange), H_r = Omega^-1 H, psi_r = Omega^-3/2 psi.

## Questions
- Q1. Montrer que l'equation de Yang-Mills rescalee est reguliere : poids de sqrt(-ghat) ghat^{ma} ghat^{nb}, et poids des courants de Higgs et de Dirac (ecrire J^nu = Omega^k j_r^nu avec k explicite). Le courant de Higgs contient-il un terme en dOmega ?
- Q2. Ecrire l'equation de Higgs rescalee pour H_r (utiliser la covariance conforme de box - R/6 en dimension 4 et -Rhat + 4 lambda = kappa That). Donner le coefficient exact du terme en Omega^-2 et la condition pour qu'il s'annule, sous la forme d'une egalite explicite en m^2, lambda, xi. Les termes de Yukawa et quartique sont-ils reguliers ?
- Q3. Pour le systeme couple, calculer la plus basse puissance de Omega dans le second membre de (2.17) et son coefficient a l'ordre dominant, en fonction des inconnues, apres substitution de (2.14) et (3.8) ; donner le resultat sous la forme c (m^2, lambda, xi) x |H_r|^2 x (structure tensorielle), c explicite. Verifier que le cas xi = 0, H reel, redonne le theoreme 3.1 de Friedrich (condition m^2 = 2 lambda/3). Le champ de jauge (A, F), le quartique lambda_h et le Yukawa contribuent-ils a un coefficient singulier ?
- Q4. Le terme d'ordre Omega^-1 de (2.17) s'annule-t-il aussi lorsque la condition de Q3 est satisfaite (avec xi quelconque) ? Si vous ne pouvez pas conclure, dites-le.
- Q5. Dirac : avec la masse de Yukawa, le coefficient de masse de l'equation de Dirac rescalee est-il regulier ? Le terme ghat Lag_D (Lag_D = psibar (i gamma.D - yH) psi) est-il regulier une fois rescale, et quel ordre en Omega a-t-il ? Comparer au cas d'une masse constante m.

## Criteres (egalites explicites)
- K-1 : J^nu = Omega^4 j_r^nu pour les deux courants ; courant de Higgs sans terme en dOmega.
- K-2 : coefficient de Omega^-2 dans l'equation de Higgs rescalee = m^2 + 4 lambda xi - 2 lambda/3.
- K-3 : plus basse puissance de (2.17) = Omega^-2 ; coefficient = (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) (phi_1^2 + phi_2^2) nabla_[nu Omega g_lambda]rho avec H_r = (phi_1 + i phi_2)/sqrt 2 ; aucun A, F, lambda_h, y dans les coefficients singuliers.
- K-4 : le coefficient de Omega^-1 de (2.17) s'annule identiquement a m^2 + 4 lambda xi = 2 lambda/3.
- K-5 : coefficient de Dirac rescale = y H_r ; ghat Lag_D rescale d'ordre Omega^2 (regulier) contre Omega^1 pour le terme de masse constante.
