# RAPPORT AA-1 (dérivation en cécité stricte)

Auditeur isolé. Seul document lu : `PROMPT-AVEUGLE-AA1.md`. Tous les calculs sont refaits par des scripts sympy écrits pour cet audit, dans `/home/claude/AF/auditaf/work_aa1/` :

- `common.py` : base de Weyl en 4D (signature (-,+,+,+)), jets de Taylor génériques, Omega au premier ordre, calcul de R à partir de T par la définition (2.17) (Christoffel de ghat = Omega^-2 eta, Lhat complet avec trace et terme lambda).
- `q123.py` (sortie `q123.out`) : Q1, Q2, Q3.
- `q45.py` (sortie `q45.out`) : Q4, Q5.

Méthode commune. Au premier ordre, Omega(x) = Omega + n_a x^a + (s/2) eta_ab x^a x^b exactement (car d_a d_b Omega = s eta_ab et d s = 0). Le tenseur W(x) est écrit W_abcd(x) = Sum_k w_k(x) B^k_abcd, où les B^k forment une base (calculée, rang 10) de l'espace des tenseurs de Weyl, et w_k(x) est un polynôme de Taylor générique d'ordre 3 dont les 35 coefficients par k sont des inconnues indépendantes (les jets d^alpha W(0)). Tout est évalué au point x = 0, puis ln Omega est remplacé par un symbole `ell` pour séparer les puissances et les logarithmes. R est calculé depuis la définition, sans utiliser de formule intermédiaire dérivée à la main ; les formules à la main ci dessous sont ensuite comparées terme à terme au résultat machine.

Convention d'indices : n_a = d_a Omega (indice bas), n^a = eta^ab n_b, D_abc = d^d W_abcd, E^n_ab = n^c n^d W_acbd.

## Q1 (partie c de l'anomalie)

Dérivation. sigma C = -ln(Omega) Omega W. Avec d_c Omega = n_c, d_c n_d = s eta_cd et la trace nulle de W :

d^d(sigma C_acbd) = -(ln Omega + 1) n^d W_acbd - Omega ln Omega d^d W_acbd,

d^c d^d(sigma C_acbd) = -(1/Omega) n^c n^d W_acbd - (ln Omega + 1)(n^d d^c W_acbd + n^c d^d W_acbd) - Omega ln Omega d^c d^d W_acbd

(le terme s eta^cd W_acbd est nul par trace). Par les symétries de Weyl, n^d d^c W_acbd = n^d D_bda et n^c d^d W_acbd = n^c D_acb, d'où

**T_ab = c0 b [ -(1/Omega) E^n_ab - (n^d D_bda + n^c D_acb) + sigma (n^d D_bda + n^c D_acb + Omega d^c D_acb) ]**

| terme | coefficient dans T_ab / (c0 b) |
|---|---|
| Omega^-1 | -E^n_ab |
| Omega^0 | -(n^d D_bda + n^c D_acb) |
| ln Omega (et Omega ln Omega) | -(n^d D_bda + n^c D_acb) - Omega d^c D_acb, soit sigma x [n^d D_bda + n^c D_acb + Omega d^c D_acb] |

La partie en ln Omega est donc sigma fois une combinaison linéaire de D et de dD (coefficients n et Omega) : il n'y entre aucune composante de W qui ne soit pas une divergence. T est symétrique et sans trace (vérifié).

That_ab = Omega^2 T_ab : **coefficient de Omega^1 (sans logarithme) = -c0 b E^n_ab**.

Vérification machine (`q123.py`, sortie `q123.out`) :
```
rang base de Weyl : 10 | symetries/trace verifiees : True
T symetrique : True
trace eta^{ab} T_ab = 0 : True
puissances presentes dans T : seulement Om^-1, Om^0, ln Om, Om ln Om : True
T = c0 b [ -E^n/Om - (lnOm+1)(n^d D_bda + n^c D_acb) - Om lnOm d^c D_acb ] : True
coef de Om^1 (sans log) dans That = -c0 b E^n : True
```
K-1 : établi.

## Q2 (plus basse puissance de R)

Dérivation. Comme That est sans trace et que nablahat ghat = 0, R_rho nu lambda = (kappa/2) Omega^-1 (nablahat_nu That_lambda rho - nablahat_lambda That_nu rho). Avec Gammahat^a_bc = -Omega^-1 (delta^a_b n_c + delta^a_c n_b - eta_bc n^a) et That = Omega^2 T, on obtient

R_rho nu lambda = (kappa/2) [ 3 (n_nu T_lambda rho - n_lambda T_nu rho) + eta_lambda rho n^a T_a nu - eta_nu rho n^a T_a lambda + Omega (d_nu T_lambda rho - d_lambda T_nu rho) ].

Seul le terme -c0 b E^n/Omega de T produit du Omega^-1 : directement (facteur 3) et via Omega d_nu(Omega^-1) = -n_nu/Omega (facteur -1). Les termes n^a E^n_a nu sont nuls (n^a n^c n^d W_acnu d = 0 par antisymétrie). D'où

**plus basse puissance : Omega^-1, coefficient -kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho).**

Il ne dépend que de n et de W au point (via E^n), ni des dérivées de W, ni de lambda, ni de s. Il n'y a ni terme Omega^-1 ln Omega, ni puissance plus négative.

Vérification machine (R calculé depuis la définition (2.17), Lhat complet, Christoffel de ghat) :
```
plus basse puissance de Om dans R : -1
coef Om^-1 de R = -kappa c0 b (n_nu E_lam rho - n_lam E_nu rho) : True
le coefficient depend de derivees de W : False
le coefficient depend de lambda ou s : False
```
K-2 : établi.

## Q3 (annulation des ln Omega pour W à divergence nulle)

Dérivation. D'après Q1, T = -c0 b ln(Omega) Y_ab + (termes sans log), avec Y_ab = n^d D_bda + n^c D_acb + Omega d^c D_acb. Dans R, la dérivée de ln Omega ne produit que des termes sans log, donc

R^(ln)_rho nu lambda = -(kappa c0 b / 2) ln Omega [ 3 (n_nu Y_lambda rho - n_lambda Y_nu rho) + eta_lambda rho n^a Y_a nu - eta_nu rho n^a Y_a lambda + Omega (d_nu Y_lambda rho - d_lambda Y_nu rho) ],

où d_e Y fait intervenir D, dD et Omega ddD. Aucun terme en (ln Omega)^2.

Résolution explicite sur les jets (machine). Les contraintes D(0) = 0, dD(0) = 0, ddD(0) = 0 sont écrites comme équations linéaires sur les jets de W, résolues par `sp.solve`, puis substituées dans le coefficient de `ell` de chacune des 64 composantes de R :
```
R contient ln^2 : False
contraintes d^k D = 0 pour k in [0] : 48 equations, 16 jets elimines ; composantes de R avec ln Om restant : 48
contraintes d^k D = 0 pour k in [0, 1] : 240 equations, 74 jets elimines ; composantes de R avec ln Om restant : 48
contraintes d^k D = 0 pour k in [0, 1, 2] : 720 equations, 210 jets elimines ; composantes de R avec ln Om restant : 0
forme fermee de la partie ln Om de R en fonction de D=J (Y_ab = n^d J_bda + n^c J_acb + Om d^c J_acb) : True
```
Conclusion : **tous les ln Omega de R s'annulent quand D = dD = ddD = 0 au point** (K-3 établi). Précision utile : les trois niveaux sont nécessaires en un point isolé. Avec D = dD = 0 seulement, il reste des termes Omega^2 ln Omega proportionnels à ddD ; avec D = 0 seulement, il reste des termes Omega ln Omega en dD. Le niveau dominant Omega^0 ln Omega ne demande que D = 0. Si W est à divergence nulle comme champ (D = 0 sur un ouvert), les trois conditions sont automatiques.

Si D = J != 0 (matière classique) : il reste exactement la forme fermée ci dessus avec D remplacé par J (vérifiée identiquement par la machine). Hiérarchie :
- Omega^0 ln Omega : -(kappa c0 b/2)[3(n_nu Y0_lambda rho - n_lambda Y0_nu rho) + eta_lambda rho n^a Y0_a nu - eta_nu rho n^a Y0_a lambda], Y0_ab = n^d J_bda + n^c J_acb ;
- Omega^1 ln Omega : termes en n d J, s J et n^a d^c J ;
- Omega^2 ln Omega : termes en dd J.

Le second membre est alors formellement singulier au sens de la consigne (présence de ln Omega), au niveau dominant Omega^0 ln Omega, et avec un coefficient linéaire en la source J (donc proportionnel à kappa c0 b J). Non établi ici : la relation entre J et un tenseur énergie impulsion de matière précis (la consigne ne la fixe pas) et l'éventuelle annulation de Y0 pour une classe particulière de matière.

## Q4 (sigma F^2)

Équation de Maxwell. Action -(1/4) Int sqrt(g) f F_ab F^ab avec f = 1/e^2 - 4 beta_* sigma = 1/e^2 + 4 beta_* ln Omega. F étant de poids conforme 0 et sqrt(g) g^ac g^bd invariant en dimension 4, l'équation est la même pour g, ghat ou eta : d^a (f F_ab) = 0. Comme d^a f = -4 beta_* d^a sigma = +4 beta_* n^a / Omega :

**d^a F_ab = -(d^a f / f) F_ab = -4 e^2 beta_* n^a F_ab / Omega + O(beta_*^2)**  (de façon équivalente : +4 e^2 beta_* n^a F_ba / Omega).

Le second membre est formellement singulier (pôle Omega^-1), de coefficient de module 4 e^2 beta_*. Vérification machine par les équations d'Euler Lagrange de sympy (`q45.py`) :
```
EL[1] / d^a(f F_a1) = 1
  d^a F_a1 - (-4 e^2 beta n^a F_a1/Omega) = O(beta^2) : True | avec signe + (K-4) : False
```
(identique pour les quatre composantes). **Écart avec K-4 : le signe.** Avec l'écriture littérale « d^a F_ab = 4 e^2 beta_* n^a F_ab / Omega », le signe est faux ; il devient juste si l'on écrit n^a F_ba, ou d^a F_ba. La conclusion qualitative (singularité Omega^-1 d'ordre beta_*) n'est pas affectée.

Termes en ln Omega de R. Avec That = f Omega^2 M (M sans trace, donc That sans trace), la formule de Q2 donne, avec T = That/Omega^2 = f M :

R = (kappa/2) f [3(n_nu M_lambda rho - n_lambda M_nu rho) + eta_lambda rho n^c M_c nu - eta_nu rho n^c M_c lambda + Omega(d_nu M_lambda rho - d_lambda M_nu rho)] + 2 kappa beta_* (n_nu M_lambda rho - n_lambda M_nu rho),

le dernier terme venant de Omega d_nu(4 beta_* ln Omega) = 4 beta_* n_nu (sans log). D'où

**coefficient de Omega^0 ln Omega = kappa beta_* [6 (n_nu M_lambda rho - n_lambda M_nu rho) + 2 (eta_lambda rho n^c M_c nu - eta_nu rho n^c M_c lambda)]**,

plus un terme Omega ln Omega en dM. Pas de pôle Omega^-1 dans R à cet ordre. Machine (R depuis la définition) :
```
(degre en ln Omega, puissance de Omega) presents dans R : [(0, 0), (0, 1), (1, 0), (1, 1)]
coef Omega^0 ln Omega = kappa beta [6(...) + 2(...)] : True
```
Condition d'annulation, n_a = (1,0,0,0), E_i = F_0i, B_i = (1/2) eps_ijk F_jk, M_ab = F_ac F_b^c - (1/4) eta_ab F^2. À la main : la composante (rho, nu, lambda) = (j, 0, i) donne 6 M_ij - 2 delta_ij M_00 = 0, soit (M_ij)_tf = 0 ; la composante (0, 0, i) donne 4 M_0i = 0. Or M_0i = (E x B)_i et (M_ij)_tf = -(E_i E_j + B_i B_j)_tf. Machine : l'espace linéaire engendré par les 64 équations coïncide avec celui engendré par {(E_iE_j + B_iB_j)_tf, (E x B)_i} (rangs 8, 8, 8 pour les deux familles et leur union) :

**annulation ssi (E_i E_j + B_i B_j)_tf = 0 et E x B = 0.**

Champs réels : la matrice E E^T + B B^T est de rang au plus 2 (det = 0, vérifié), alors que (.)_tf = 0 impose E E^T + B B^T = mu I. Donc mu^3 = 0, mu = 0, et sa trace |E|^2 + |B|^2 = 0 : **E = B = 0**. (La condition E x B = 0 n'est même pas nécessaire pour cette conclusion.) Pour des champs complexes, la condition admet des solutions non nulles, par exemple E = (1, i, 0), B = i E : alors E E^T + B B^T = E E^T - E E^T = 0 et E x B = i E x E = 0 (vérification à la main ; la sortie machine montre seulement que E = (1, i, 0), B = 0 ne suffit pas). Conclusion pour des champs réels : il ne reste aucun champ de Maxwell non nul qui annule la partie ln Omega ; le seul cas régulier est F = 0. K-4 : établi pour R et pour la condition, avec correction de signe pour l'équation de Maxwell.

## Q5 (contrôles)

Convention : « n = (1,0,0,0) » est lu comme n_a = d_a Omega = (1,0,0,0) (indice bas). Le cas n^a = (1,0,0,0) (donc n_0 = -1) est aussi calculé, car il change tous les signes. Les deux vérifient |dOmega|^2 = -1 = -lambda/3 + 2 Omega s pour lambda = 3, s = 0.

(a) W(0) purement électrique, E_yy = -E_zz = e (W_0i0j = E_ij, W_0ijk = 0 ; solution unique pour les 10 composantes, vérifiée). À la main par K-2 : R_y0y pôle = -kappa c0 b (n_0 E_yy - n_y E_0y)/Omega = -kappa c0 b n_0 e / Omega. Machine (sur le R complet de Q2) :
```
n_a = (1,0,0,0) : residu du pole de R_y0y (coef de 1/Omega) = 8*b*e*kappa
n^a = (1,0,0,0) : residu du pole de R_y0y (coef de 1/Omega) = -8*b*e*kappa
```
**Pôle 8 b kappa e / Omega** (pour n_a = (1,0,0,0)), conforme à K-5(a).

(b) F_12 = B0 : M = diag(B0^2/2, B0^2/2, B0^2/2, -B0^2/2), dM = 0. À la main : R_i0i(ln) = kappa beta_* (6 M_ii - 2 M_00), soit 2 kappa beta_* B0^2, 2 kappa beta_* B0^2, -4 kappa beta_* B0^2, puis beta_* = -beta~/(2 e^2). Machine :
```
n_a = (1,0,0,0) (indice bas) : coef ln Omega de R_101, R_202, R_303 = [-B0**2*betatilde*kappa/e2, -B0**2*betatilde*kappa/e2, 2*B0**2*betatilde*kappa/e2]
n^a = (1,0,0,0) (indice haut, donc n_0 = -1) : [+..., +..., -2 ...]
```
**Coefficients -kappa beta~ B0^2/e^2, -kappa beta~ B0^2/e^2, +2 kappa beta~ B0^2/e^2**, conformes à K-5(b) pour n_a = (1,0,0,0).

## Verdict

**CONFIRME AVEC CORRECTIONS.**

| critère | statut | commentaire |
|---|---|---|
| K-1 | établi | T = c0 b[-E^n/Omega - (n^d D_bda + n^c D_acb) + sigma(n^d D_bda + n^c D_acb + Omega d^c D_acb)] ; coef Omega^1 de That = -c0 b E^n |
| K-2 | établi | plus basse puissance Omega^-1, coefficient -kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho), sans dérivées de W, sans lambda ni s |
| K-3 | établi | par résolution explicite (720 équations, 210 jets éliminés, 0 composante résiduelle). Précision : en un point, les trois niveaux D, dD, ddD sont tous nécessaires (D = dD = 0 laisse des Omega^2 ln Omega) |
| K-4 | établi avec correction | **signe** de l'équation de Maxwell : d^a F_ab = -4 e^2 beta_* n^a F_ab / Omega (ou +4 e^2 beta_* n^a F_ba / Omega). Coefficient Omega^0 ln Omega de R et condition d'annulation exacts ; E = B = 0 pour des champs réels (la condition sur la partie sans trace suffit à elle seule) |
| K-5 | établi sous convention | (a) 8 b kappa e / Omega, (b) -kappa beta~ B0^2/e^2, -kappa beta~ B0^2/e^2, +2 kappa beta~ B0^2/e^2, **à condition de lire n = (1,0,0,0) comme n_a (indice bas)** ; avec n^a = (1,0,0,0) tous les signes s'inversent. La convention doit être précisée |

Ce qui n'a pas été établi ou reste hors champ :
- Tout est au premier ordre autour de eta (produits de deux quantités du premier ordre négligés, en particulier g = eta dans les Christoffel et la non linéarité de M en F est traitée comme une source donnée). Aucun contrôle des ordres supérieurs.
- La normalisation |c0| = 8 et son signe n'ont pas été dérivés (gardés symboliques ; seul c0 = -8 est utilisé en Q5(a), comme demandé). La forme T_ab = c0 b d^c d^d(sigma C_acbd) est prise de la consigne, non rederivée de l'action de Wess Zumino.
- La cohérence de That avec les équations (2.14), (2.15), (3.8) (conservation, contraintes) n'a pas été examinée ; seul le second membre de (2.17) est calculé.
- Le lien entre J = d^d W_abcd et une matière classique précise, et l'éventuelle annulation du résidu Omega^0 ln Omega pour une classe de matière, ne sont pas établis.
