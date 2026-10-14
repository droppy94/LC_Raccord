# RAPPORT AAA-1 : tenseur d'un etat homogene anisotrope du scalaire conforme (derivation aveugle)

Auditeur froid, isole. Aucune lecture hors de `/home/claude/audit_p1/aaa1/`, aucune recherche bibliographique. Outils : python3, sympy 1.14.0, mpmath 1.3.0. Scripts et sorties dans `/home/claude/audit_p1/aaa1/work/`.

Conventions : signature (-,+,+,+), coordonnees (eta, x), s = -eta > 0 sur le demi-espace eta < 0, k = |k-vec|, k^ = k-vec/k. Le terme d'amelioration est pris avec xi = 1/6 comme dans l'enonce. Etiquettes : [calcule] = obtenu par le calcul symbolique ou numerique des scripts ; [derive] = raisonnement a partir de ces resultats.

## 0. Resume des conclusions

| Question | Conclusion |
|---|---|
| Q1 (P2) | T_00 = |beta|^2 k/(16 pi^3), T_0i = |beta|^2 k_i/(16 pi^3), T_ij = |beta|^2 k_i k_j/(16 pi^3 k) ; trace nulle. La somme des deux phases |beta|^2 donne un gaz de quanta sans masse : T_00 = |beta|^2 k/(2 pi)^3, T_0i = 0, T_ij = |beta|^2 k_i k_j/((2 pi)^3 k). |
| Q1 (P3) | T_00 = 0, T_0i = 0, T_ij = A k_i k_j + B delta_ij avec A = alpha beta* e^{-2 i k eta}/(16 pi^3 k), B = -A k^2/3. Partie isotrope nulle, T_ij est deja purement sans trace : T_ij = A (k_i k_j - k^2 delta_ij/3). Trace nulle. |
| Q2 | Etat isotrope : le terme alpha beta* disparait entierement de <T_mu nu> (moyenne angulaire de k_i k_j - k^2 delta_ij/3 nulle). Etat anisotrope : il ne survit que dans la partie spatiale sans trace et ne depend que du moment quadrupolaire (l = 2) de alpha beta*(k, k^) sur la sphere, a k fixe. |
| Q3 | I_N(eta) = (2 i eta)^{N-4} Gamma(4-N) (continuation d'Abel). N = 3 : I_3 = i/(2 s), en s^{-1}, verifie numeriquement par quadosc (s Im I_3 = 0.5 a 30 chiffres). N = 4 : -ln s + cte (coupure IR necessaire). N = 5 : 1/mu + s ln s + c s (coupure IR, aucun terme singulier). Gaussien : fonction entiere de s, I_G = Lambda^4/2 + (3 i sqrt(pi)/4) Lambda^5 s + O(s^2). |
| Q4 | Pour alpha beta* = f(k^), le terme est singulier sur le cone reflechi (eta + eta')^2 = |x - x'|^2 (cone de lumiere du point image (-eta', x')), distinct du cone de lumiere entre x et x' des que eta eta' differe de 0. Une decroissance en loi de puissance k^{-N} (dans une direction ou toutes) laisse une singularite conormale d'ordre fini sur ce cone : l'etat n'est pas Hadamard sur eta < 0, pour tout N fini. L'anisotropie ne change pas la reponse, elle ne fait que restreindre les directions spatiales du cone reflechi ou la singularite est portee. |
| Q5 | s^2 <T_ij> possede un terme lineaire en s a coefficient non nul en s = 0 pour N = 3 exactement (coefficient proportionnel a sin(phi) Y_2, nul si alpha beta* est reel). Cet etat n'est pas Hadamard (singularite sur le cone reflechi, et densite de particules IR divergente). |

## 1. Q1 [calcule] : separation de points, structures P2 et P3

### 1.1 Methode

Pour w(x, x') bilineaire, on applique
- d_mu phi d_nu phi -> (1/2)(d_mu d'_nu + d_nu d'_mu) w,
- (d phi)^2 -> g^{ab} d_a d'_b w,
- phi^2 -> w, et d_mu d_nu phi^2 -> (d_mu + d'_mu)(d_nu + d'_nu) w, box phi^2 -> g^{ab}(d_a + d'_a)(d_b + d'_b) w,

puis la coincidence x' -> x (script `q1_tenseur.py`). Controle independant (script `q1_controle_modes.py`) : forme bilineaire symetrisee T_mu nu(phi_k, phi_k-bar) sur le mode de Bogoliubov, soustraction du vide (alpha = 1, beta = 0) avec |alpha|^2 = 1 + |beta|^2. Les deux methodes coincident composante par composante.

### 1.2 Structure P2 : |beta|^2 e^{+ik(eta - eta')} e^{ik.(x-x')}/(2k(2pi)^3)

- T_00 = |beta|^2 k/(16 pi^3)
- T_0i = |beta|^2 k_i/(16 pi^3)
- T_ij = |beta|^2 k_i k_j/(16 pi^3 k)
- trace g^{mu nu} T_mu nu = -T_00 + T_ii = -k/16 + k/16 = 0 (en unites |beta|^2/pi^3).

La phase conjuguee e^{-ik(eta - eta')} donne les memes T_00 et T_ij et T_0i de signe oppose. La somme (terme |beta|^2 complet de l'enonce) est :

T_00 = |beta|^2 k/(2 pi)^3, T_0i = 0, T_ij = |beta|^2 k_i k_j/((2 pi)^3 k).

Lecture : gaz de quanta sans masse de densite d^3k |beta|^2/(2 pi)^3, d'energie k et d'impulsion k_i chacun ; tenseur d'un fluide nul par mode (T_mu nu proportionnel a k_mu k_nu avec k_0 = k), sans trace, independant de eta. Aucune dependance temporelle, aucun terme d'amelioration ne survit (box de w et d_mu d_nu de w a la coincidence sont nuls pour cette phase puisque w depend de x - x' seul et k^2 - k_i k_i = 0).

### 1.3 Structure P3 : alpha beta* e^{-ik(eta + eta')} e^{ik.(x-x')}/(2k(2pi)^3)

- T_00 = 0
- T_0i = 0
- T_ij = A k_i k_j + B delta_ij avec

  A = alpha beta* e^{-2 i k eta}/(16 pi^3 k), B = -alpha beta* k e^{-2 i k eta}/(48 pi^3) = -A k^2/3.

- Partie isotrope (moyenne angulaire, <k_i k_j> = k^2 delta_ij/3) : coefficient A k^2/3 + B = 0.
- Partie sans trace : T_ij = A (k_i k_j - k^2 delta_ij/3), tout le tenseur.
- Trace : -T_00 + T_ii = 0 + (A k^2 + 3B) = 0.

Le terme alpha* beta e^{+2 i k eta} est le conjugue ; le total physique est 2 Re[A (k_i k_j - k^2 delta_ij/3)].

Remarque de controle (script `q1_controle_modes.py`, xi = 0) : sans le terme d'amelioration, P3 donne T_00 = 0 egalement (massless : les termes cinetiques phi-point^2 et (grad phi)^2 se compensent exactement dans le terme croise) mais T_ij = [k_i k_j - k^2 delta_ij] e^{-2 i k eta}/(16 pi^3 k), de trace -k e^{-2 i k eta}/(8 pi^3). Le terme d'amelioration (xi = 1/6) retire exactement la pression isotrope oscillante : c'est lui qui rend P3 purement sans trace. Ce point est le pivot de Q2.

## 2. Q2 [derive] : etat isotrope et anisotrope

<T_ij>^{(alpha beta*)} = Int d^3k alpha beta*(k-vec) e^{-2 i k eta}/(16 pi^3 k) (k_i k_j - k^2 delta_ij/3) + c.c., et <T_00> = <T_0i> = 0 pour cette structure.

- Etat isotrope (alpha, beta fonctions de k seules) : a k fixe, Int dOmega (k^_i k^_j - delta_ij/3) = 0. Il ne reste RIEN du terme alpha beta* dans <T_mu nu>. Toute la valeur moyenne est donnee par le terme |beta|^2 (gaz de quanta, section 1.2). Il n'y a en particulier aucune oscillation en e^{-2ik eta} dans <T_00> ni dans la pression isotrope, a la difference du cas xi = 0.

- Etat anisotrope : il reste uniquement une contrainte spatiale sans trace. Comme k^_i k^_j - delta_ij/3 est la combinaison standard des cinq harmoniques Y_2m(k^), le theoreme de projection donne

  <T_ij>^{(alpha beta*)} = Int_0^inf dk k^3 e^{-2 i k eta}/(16 pi^3) Int dOmega [alpha beta*]_{l=2}(k, k^) (k^_i k^_j - delta_ij/3) + c.c.,

  ou [alpha beta*]_{l=2} est la projection de alpha beta*(k, .) sur l = 2 a k fixe. Seul le moment QUADRUPOLAIRE (l = 2) de alpha beta* contribue ; les moments l = 0 (isotrope), l = 1 (dipole), l >= 3 sont annules par l'integrale angulaire. Le terme |beta|^2, lui, contribue a <T_00> par son monopole et a <T_ij> par ses moments l = 0 et l = 2 (<T_0i> par son moment l = 1).

## 3. Q3 [calcule] : comportement de I(eta) = Int_0^inf dk k^{3-N} e^{-2 i k eta}, eta -> 0^-

Avec a = 2 i eta = -2 i s (convergence UV par la prescription d'Abel a -> a + epsilon), et une coupure IR mu lorsque necessaire : I_N = a^{N-4} Gamma(4 - N, a mu). Pour mu -> 0 et N < 4 : I_N = Gamma(4 - N) (-2 i s)^{N-4}, soit |I_N| proportionnel a s^{N-4}.

| N | forme fermee | comportement s -> 0^+ |
|---|---|---|
| 3 | I_3 = 1/a = i/(2 s) (mu = 0 ; avec coupure : e^{-a mu}/a = i/(2s) - mu + O(s)) | s^{-1}, coefficient i/2 |
| 4 | I_4 = E_1(a mu) = -ln(2 s mu) - gamma_E + i pi/2 - 2 i mu s + O(s^2) | -ln s (IR divergente sans coupure) |
| 5 | I_5 = a Gamma(-1, a mu) = 1/mu + a [ln(a mu) + gamma_E - 1] + O(s^2) | constante IR 1/mu, puis terme en s ln s et terme lineaire en s ; aucun terme singulier |
| gaussien, alpha beta* = Y e^{-k^2/Lambda^2} | I_G = Int k^3 e^{-k^2/Lambda^2} e^{2iks} dk, forme fermee en erfc(i Lambda s) (voir `q3_sortie.txt`) | fonction entiere : Lambda^4/2 + (3 i sqrt(pi)/4) Lambda^5 s - 2 Lambda^6 s^2 + O(s^3) |

Controle numerique N = 3 (mpmath, 30 chiffres, `quadosc` avec omega = 2s) pour s = 0.1, 0.01, 0.001 : Re I_3 = 0 a 10^{-35} pres, Im I_3 = 5, 50, 500 ; s Im I_3 = 0.5 exactement. La regularisation d'Abel e^{-epsilon k} avec epsilon = 10^{-4} s donne i/(2s) a 10^{-8} relatif pres. Les formes fermees N = 4, 5 (mu = 1) coincident avec la quadrature oscillante a 10 chiffres ; le gaussien (Lambda = 1) a 12 chiffres.

Consequences pour la partie sans trace de <T_ij> (facteur Int dOmega Y_2 (k^_i k^_j - delta_ij/3) e^{i phi}/(16 pi^3) et son conjugue) : divergence en 1/s pour N = 3, logarithmique pour N = 4, finie pour N = 5 (mais dominee par la constante IR 1/mu, signe d'un etat IR mal defini), finie et reguliere pour le gaussien.

Remarque sur la coherence de l'enonce : pour N >= 2 la densite de quanta Int d^3k |beta|^2 avec |beta|^2 ~ k^{-N}|Y| (pour k -> 0) et la fonction a deux points elle-meme (Int d^3k/k times k^{-N}) divergent dans l'IR. Les cas N = 3, 4, 5 supposent donc implicitement une coupure IR ; elle n'affecte pas le terme dominant en s^{-1} de N = 3.

## 4. Q4 [derive] : support singulier du terme alpha beta* et caractere Hadamard

Posons tau = eta + eta', Dx = x - x', r = |Dx|, u = k^.Dx - tau. Pour alpha beta* = f(k^) :

w_3(x, x') = Int dOmega f(k^) Int_0^inf k dk e^{i k u}/(2 (2 pi)^3) = -(1/(2(2 pi)^3)) Int dOmega f(k^)/(u + i0)^2.

- Isotrope (f = 1) [calcule] : Int dOmega/(r c - tau)^2 = 4 pi/(tau^2 - r^2). Le terme est donc la fonction de Wightman du vide evaluee entre x et le point IMAGE x~' = (-eta', x') : singulier exactement sur le cone reflechi tau^2 = r^2, c'est-a-dire (eta + eta')^2 = |x - x'|^2.
- Anisotrope (f = P_2(k^.n), n = Dx/r) [calcule] : l'integrale angulaire donne des poles 1/(tau^2 - r^2) et des logarithmes ln((tau - r)/(tau + r)) ; pres de tau = r + d : 2 pi/(d r) + (6 pi/r^2) ln d + ... Le support singulier est encore {tau^2 = r^2}. A l'interieur du cone (|tau| < r) le pole traverse l'interieur du domaine d'integration mais, f etant lisse, la prescription i0 fournit une fonction lisse de tau : seules les extremites c = +-1 (k^ parallele a +-Dx) produisent une singularite. Pour f lisse a support dans un cone de directions, la singularite est portee par la portion du cone reflechi dont la direction spatiale +-Dx/r appartient au support de f.

Reponse a la premiere question : oui, le terme alpha beta* est singulier ailleurs que sur le cone de lumiere entre x et x' : sur le cone de lumiere du point image (-eta', x'), (eta + eta')^2 = |x - x'|^2. Les deux cones coincident si et seulement si eta eta' = 0. Pour eta, eta' < 0, le cone reflechi est a |tau| = |eta| + |eta'| >= |eta - eta'| : il est strictement a l'exterieur du cone de lumiere et traverse tout le demi-espace eta < 0 (exemple : eta = eta' = -1, |x - x'| = 2).

Decroissance en loi de puissance k^{-N} [calcule puis derive] : l'integrale radiale devient Int k^{1-N} e^{iku} dk = (-iu)^{N-2} Gamma(2 - N, -i u mu), dont la partie non analytique est u^{N-2} ln|u| (N entier). L'integration angulaire pres des extremites eleve l'ordre d'une unite, de sorte qu'en un point generique du cone reflechi w_3 se comporte comme (tau -+ r)^{N-1} ln|tau -+ r| (verifie pour f = 1, N = 3 : termes (tau -+ r)^2 ln|tau -+ r|, C^1 non C^2). Au sommet du cone (Dx = 0, tau = 2 eta -> 0) il n'y a pas de lissage angulaire et T ~ tau^{N-4}, ce qui redonne les comportements de Q3.

Caractere Hadamard : la partie du vide etant soustraite, l'etat est Hadamard si et seulement si la partie dependante de l'etat de la fonction a deux points est C^infini. Or pour tout N fini, w_3 possede sur le cone reflechi une singularite conormale d'ordre fini (non C^infini), et ce cone rencontre le demi-espace eta < 0. Conclusion : un etat dont alpha beta* decroit en loi de puissance dans une seule direction n'est PAS Hadamard sur eta < 0. Le terme |beta|^2 (avec |beta|^2 ~ k^{-2N} dans l'UV) est, lui, de type Fourier d'une fonction a decroissance polynomiale : il est C^m avec m fini mais n'est pas C^infini non plus ; il porte sa singularite d'ordre fini sur le cone de lumiere ordinaire. Les deux termes excluent le caractere Hadamard strict, mais le terme alpha beta* est le seul a produire une singularite hors du cone de lumiere.

L'anisotropie change-t-elle la reponse ? Non. Le cas isotrope (f = 1, ou k^{-N} isotrope) est deja singulier sur le cone reflechi complet, et non Hadamard. L'anisotropie ne modifie que (i) l'ensemble des directions spatiales de Dx ou la singularite reflechie est portee, et (ii) le fait que la singularite survive dans <T_mu nu> a la coincidence via le moment l = 2 (Q2) : en isotrope la singularite du cone reflechi est presente dans w mais invisible dans <T_mu nu> a cause de la projection angulaire ; en anisotrope elle devient visible dans la partie sans trace de <T_ij>. Le caractere non Hadamard, lui, est une propriete de w et ne depend pas de l'anisotropie. Seule une decroissance plus rapide que toute puissance (gaussienne par exemple) donne un w_3 lisse et donc un etat Hadamard, isotrope ou non.

## 5. Q5 [derive] : terme lineaire en s dans s^2 <T_mu nu>

Avec s = -eta, la partie sans trace de <T_ij> se comporte comme I_N ~ Gamma(4 - N)(-2 i s)^{N-4} (section 3), donc s^2 <T_ij> ~ s^{N-2}. Un terme lineaire en s a coefficient non nul en s = 0 apparait pour N - 2 = 1, soit N = 3, et pour lui seul :

s^2 <T_ij>^{(alpha beta*)} = s^2 times 2 Re[e^{i phi} (i/(2s))] times C_ij + O(s^2) = -sin(phi) s C_ij + O(s^2),

avec C_ij = (1/(16 pi^3)) Int dOmega Y_2(k^)(k^_i k^_j - delta_ij/3), non nul pour Y de moment l = 2. Le coefficient est non nul si et seulement si sin(phi) differe de 0, c'est-a-dire si alpha beta* a une partie imaginaire : pour alpha beta* reel (phi = 0 mod pi) le terme en 1/s de I_3 est imaginaire pur et disparait de la valeur moyenne reelle ; le reste (-mu + O(s) avec coupure) donne alors s^2 times cte, sans terme lineaire. Pour N = 2 on obtient une constante, pour N = 4 un terme s^2 ln s, pour N = 5 un terme s^2/mu + s^3 ln s ; aucun n'est lineaire. Pour un N non entier, s^{N-2} n'est lineaire que si N = 3.

Cet etat (N = 3) est-il Hadamard ? Non, par la section 4 : alpha beta* = k^{-3} Y e^{i phi} donne une singularite conormale (tau -+ r)^2 ln|tau -+ r| sur le cone reflechi, hors du cone de lumiere, a l'interieur du demi-espace eta < 0. De plus |beta|^2 ~ k^{-3}|Y| pour k -> 0 rend la densite de quanta Int d^3k |beta|^2 logarithmiquement divergente dans l'IR, et le terme |beta|^2 de <T_00>, Int d^3k k |beta|^2, converge mais la fonction a deux points elle-meme (Int d^3k/k times k^{-3}) diverge : il faut une coupure IR, qui ne supprime pas le terme lineaire. Le terme lineaire en s dans s^2 <T_mu nu> est donc precisement la signature d'un etat non Hadamard, portee par le sommet du cone reflechi atteint en s = 0 ; il ne peut etre produit par aucun etat Hadamard (alpha beta* a decroissance rapide), pour lequel s^2 <T_ij> = s^2 (c_0 + c_1 s + ...) commence au second ordre.

## 6. Empreintes sha256 des scripts et sorties

```
11feb23a0b2ab3f7d97ba8a09b6e09c2a5379a758594d50038e4a72d3090c051  q1_tenseur.py
6335f8c690f9d81e3124e72307b39b7fa1bd3dbcabc31461f395049b6dc79f0c  q1_sortie.txt
6ebf950886fff6bc7c01f9d9a4c1e1a01769ccd48f2743228f71cb99040f2c7a  q1_controle_modes.py
c2bc5dbba10df1b538988c0837e18dd3f310be24650d16f62c8cde60889cf131  q1_controle_sortie.txt
cbb0a648e12d7f2bd5166118036639e63578f891cd83d18a516903503d18c85a  q3_integrale.py
2e5e40e1fae126ea377671e17d209637667077bc6a0cfcda32ea1ded8cc1762a  q3_sortie.txt
3bbff945e8c0c79d77f3f34aa27a3c1af52c66b06933d96cd1f672cf560c3b58  q4_singularites.py
535284f7ffe4fd6b2b05b2b378c1325b93f9164106c30896ace64954c3a9e6cd  q4_sortie.txt
```

Fichiers dans `/home/claude/audit_p1/aaa1/work/` (liste reproduite dans `SHA256SUMS.txt`).

## 7. Limites de l'audit

- Le calcul Q1 est exact (symbolique) ; les affirmations Q2, Q4, Q5 sont des derivations appuyees sur les integrales angulaires et radiales calculees en sympy (f = 1, f = P_2 ; N = 3, 4, 5), non sur une preuve generale de theorie des distributions pour f arbitraire. L'argument de lissage interieur (prescription i0 avec f lisse) et l'argument « Hadamard ssi partie d'etat C^infini » sont pris comme acquis standard.
- Les cas N >= 4 exigent une coupure IR que l'enonce ne fixe pas ; les comportements donnes sont ceux de la partie dependante de s, la constante IR etant signalee.
