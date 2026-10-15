# RAPPORT FA-1 : dérivation en cécité stricte

Auditeur isolé. Seule source lue : `/home/claude/FW3/auditfw3/PROMPT-AVEUGLE-FA1.md`. Aucune note, aucun script ni sortie du dossier FW3 n'a été consulté. Toutes les relations ci-dessous sont dérivées à partir du cadre fourni (conventions de Friedrich, équations (2.14), (2.15), (3.8), (2.17)) et vérifiées par deux scripts sympy écrits pour l'occasion :

- `/home/claude/FW3/auditfw3/work_fa1/fa1_q3q4.py` (sortie : `fa1_q3q4.out`) : calcul en composantes, sur g = eta de Minkowski, de la courbure de ghat = Omega^-2 eta, du tenseur énergie-impulsion physique du secteur Higgs (avec xi) et Maxwell, du second membre de (2.17), extraction des coefficients de Omega^-2 et Omega^-1 après substitution de (2.14) et (3.8). Vérifie aussi Q1 (courant de Higgs) et l'identité de covariance conforme de Q2.
- `/home/claude/FW3/auditfw3/work_fa1/fa1_q1q5_dirac.py` (sortie : `fa1_q1q5_dirac.out`) : poids de la densité de Yang-Mills, courant de Dirac, connexion de spin de ghat, covariance conforme de l'opérateur de Dirac avec jauge, équation de Dirac rescalée (Yukawa et masse constante), ordre du terme ghat_ab Lag_D, poids du tenseur énergie-impulsion de Dirac.

Méthode des scripts : « variables de jet ». Omega, ses dérivées jusqu'à l'ordre 3, phi_1, phi_2 et leurs dérivées jusqu'à l'ordre 3, A_a et ses dérivées jusqu'à l'ordre 2 sont des symboles indépendants ; un opérateur D(expr, c) applique la règle de la chaîne. Toute expression devient un polynôme de Laurent en Omega dont on lit les coefficients. Les symboles de Christoffel, le tenseur de Ricci et le scalaire de ghat sont recalculés directement à partir de ghat = Omega^-2 eta (et non pris des formules de l'énoncé) ; le script confirme ensuite que les formules de l'énoncé pour Rhat_ab et Rhat sont exactes.

Notations : signature (-,+,+,+) ; ghat_ab = Omega^-2 g_ab, ghat^{ab} = Omega^2 g^{ab}, sqrt(-ghat) = Omega^-4 sqrt(-g) ; H = Omega H_r, psi = Omega^{3/2} psi_r, A_a inchangé ; H_r = (phi_1 + i phi_2)/sqrt 2, donc |H_r|^2 = (phi_1^2 + phi_2^2)/2 ; Omega_a = nabla_a Omega ; |dOmega|^2 = g^{ab} Omega_a Omega_b ; C := m^2 + 4 lambda xi - 2 lambda/3.

Relation structurelle utilisée partout : pour ghat = Omega^-2 g avec g plat,

    Gammahat^c_ab = -Omega^-1 (delta^c_a Omega_b + delta^c_b Omega_a - g_ab Omega^c).

(Dérivée directement de Gammahat^c_ab = (1/2) ghat^{cd}(d_a ghat_db + d_b ghat_da - d_d ghat_ab) ; vérifiée par le script.)

---

## Q1. Équation de Yang-Mills rescalée

**Poids de la densité.** sqrt(-ghat) ghat^{ma} ghat^{nb} = Omega^-4 . Omega^2 . Omega^2 . sqrt(-g) g^{ma} g^{nb} = sqrt(-g) g^{ma} g^{nb}. Poids Omega^0 (invariance conforme de Maxwell en dimension 4). Comme A_a est de poids 0, F_ab = d_a A_b - d_b A_a est inchangé. L'équation physique

    d_m ( sqrt(-ghat) ghat^{ma} ghat^{nb} F_ab ) = sqrt(-ghat) Jhat^n

devient donc

    d_m ( sqrt(-g) F^{mn} ) = Omega^-4 sqrt(-g) Jhat^n .

Elle est régulière si et seulement si Jhat^n = Omega^4 j_r^n avec j_r^n régulier.

**Courant de Higgs.** Jhat^n = i e ghat^{nb} ( H^dagger D_b H - (D_b H)^dagger H ). Avec H = Omega H_r :

    D_b H = Omega D_b H_r + Omega_b H_r ,

    H^dagger D_b H - (D_b H)^dagger H
      = Omega^2 ( H_r^dagger D_b H_r - (D_b H_r)^dagger H_r ) + Omega Omega_b ( |H_r|^2 - |H_r|^2 )
      = Omega^2 ( H_r^dagger D_b H_r - (D_b H_r)^dagger H_r ) .

Le terme en dOmega disparaît parce que |H_r|^2 est réel (la combinaison est antihermitienne). Avec ghat^{nb} = Omega^2 g^{nb} :

    Jhat^n_Higgs = Omega^4 . i e g^{nb} ( H_r^dagger D_b H_r - (D_b H_r)^dagger H_r ) = Omega^4 j_r^n , k = 4 .

Vérifié symboliquement (script 1, ligne « Q1 : J^n_Higgs = Om^4 j_r^n, sans terme en dOm : verifie »).

**Courant de Dirac.** Jhat^n = e psibar gammahat^n psi, gammahat^n = ehat_A^n gamma^A avec ehat_A^n = Omega delta_A^n (de sorte que ghat^{mn} = Omega^2 eta^{mn}), donc gammahat^n = Omega gamma^n. psibar = Omega^{3/2} psibar_r. D'où

    Jhat^n_Dirac = Omega^{3/2} . Omega . Omega^{3/2} e psibar_r gamma^n psi_r = Omega^4 j_r^n , k = 4 .

Vérifié (script 2, « Q1 : J^n_Dirac = Om^4 j_r^n : verifie »).

**Conclusion Q1.** Équation de Yang-Mills rescalée : nabla_m F^{mn} = j_r^n[H_r, A] + j_r^n[psi_r], régulière. K-1 confirmé : les deux courants sont de poids Omega^4 et le courant de Higgs ne contient aucun terme en dOmega.

---

## Q2. Équation de Higgs rescalée

**Équation physique.** De L = -ghat^{ab}(D_a H)^dagger D_b H - m^2|H|^2 - lambda_h|H|^4 - xi Rhat |H|^2 - y psibar H psi (une composante), la variation en H^dagger donne

    boxhat_D H = ( m^2 + xi Rhat + 2 lambda_h |H|^2 ) H + y S ,

où boxhat_D = ghat^{ab} D_a D_b (covariant de Levi-Civita et de jauge) et S est la source de Yukawa, un bilinéaire psibar Gamma psi (Gamma = 1 ou projecteur chiral selon la structure du doublet ; cela n'affecte pas le poids).

**Covariance conforme de box - R/6.** Pour ghat = Omega^-2 g en dimension 4 :

    ( boxhat_D - Rhat/6 ) ( Omega H_r ) = Omega^3 ( box_D - R/6 ) H_r = Omega^3 box_D H_r   (g plat).

Dérivation directe (g plat) : boxhat_D H = Omega^4 D_a( Omega^-2 g^{ab} D_b H ), et avec D_b H = Omega D_b H_r + Omega_b H_r on obtient

    boxhat_D H = Omega^3 box_D H_r + Omega^2 (box Omega) H_r - 2 Omega |dOmega|^2 H_r ,

tandis que (Rhat/6) H = (Omega^2/6)(6 Omega^-1 box Omega - 12 Omega^-2 |dOmega|^2) Omega H_r = Omega^2 (box Omega) H_r - 2 Omega |dOmega|^2 H_r. La différence est bien Omega^3 box_D H_r (les termes croisés Omega^a D_a H_r se compensent). Le script 1 vérifie cette identité avec le champ de jauge inclus (« Q2 : ... verifie »).

**Équation rescalée.** On écrit boxhat_D H - (Rhat/6) H = ( m^2 + (xi - 1/6) Rhat + 2 lambda_h |H|^2 ) H + y S, on divise par Omega^3 et on utilise |H|^2 = Omega^2 |H_r|^2, S = Omega^3 S_r (psibar psi = Omega^3 psibar_r psi_r) :

    box_D H_r = Omega^-2 ( m^2 + (xi - 1/6) Rhat ) H_r + 2 lambda_h |H_r|^2 H_r + y S_r .

Puis Rhat = 4 lambda - kappa That (trace d'Einstein) :

    box_D H_r = Omega^-2 ( m^2 + 4 lambda xi - 2 lambda/3 ) H_r
                - (xi - 1/6) kappa ( Omega^-2 That ) H_r
                + 2 lambda_h |H_r|^2 H_r + y S_r .

Le script 1 établit que That, exprimé en variables rescalées, a pour plus basse puissance Omega^2 (« Trace That : plus basse puissance de Om = 2 »), ce qui est aussi évident à la main : That = ghat^{ab} That_ab = Omega^2 g^{ab} That_ab et That_ab est polynomial en Omega (vérifié). Donc Omega^-2 That est régulier (c'est d'ailleurs la quantité qui figure dans (3.8)).

**Coefficient exact de Omega^-2** : m^2 + 4 lambda xi - 2 lambda/3. **Condition d'annulation** :

    m^2 + 4 lambda xi = 2 lambda/3 .

Cas particuliers : xi = 0 donne m^2 = 2 lambda/3 (Friedrich) ; xi = 1/6 (couplage conforme) donne m^2 = 0, comme il se doit.

**Yukawa et quartique** : 2 lambda_h |H_r|^2 H_r est d'ordre Omega^0 ; la source de Yukawa y S_r = y Omega^-3 (psibar Gamma psi) = y psibar_r Gamma psi_r est d'ordre Omega^0. Les deux sont réguliers.

**Conclusion Q2.** K-2 confirmé.

---

## Q3. Plus basse puissance de Omega dans (2.17) et coefficient dominant

### Mise en forme du second membre

Avec Lhat_ab = (kappa/2)(That_ab - That ghat_ab/3) + (lambda/6) ghat_ab et nablahat ghat = 0, le terme en lambda disparaît sous nablahat et

    2 Omega^-1 nablahat_[nu Lhat_lambda]rho = kappa Omega^-1 nablahat_[nu ( That_lambda]rho - (1/3) That ghat_lambda]rho ) .

Expression de nablahat par nabla (g plat) : nablahat_nu That_lambda rho = nabla_nu That_lambda rho - Gammahat^c_nu lambda That_c rho - Gammahat^c_nu rho That_lambda c. Le premier terme de Christoffel est symétrique en (nu, lambda) et disparaît par antisymétrisation ; le second donne, That étant symétrique,

    - Gammahat^c_[nu|rho That_|lambda]c = Omega^-1 ( Omega_[nu That_lambda]rho - g_rho[nu That_lambda]c Omega^c ) .

Pour la trace, nablahat_[nu (That ghat_lambda]rho) = ghat_rho[lambda nabla_nu] That = Omega^-2 g_rho[lambda nabla_nu] That. Donc, exactement,

    RHS_rho nu lambda = kappa [ Omega^-1 nabla_[nu That_lambda]rho
                              + Omega^-2 ( Omega_[nu That_lambda]rho - g_rho[nu That_lambda]c Omega^c )
                              - (1/3) Omega^-2 g_rho[lambda nabla_nu] That ] .          (*)

### Puissances de Omega dans That_ab

Tenseur énergie-impulsion du Higgs (signature -+++, Einstein Ghat + lambda ghat = kappa That) :

    That_ab = 2 D_(a H^dagger D_b) H + ghat_ab L_0 + 2 xi ( Ghat_ab + ghat_ab boxhat - nablahat_a nablahat_b ) |H|^2 ,
    L_0 = -ghat^{cd}(D_c H)^dagger D_d H - m^2 |H|^2 - lambda_h |H|^4 .

Maxwell : That^F_ab = F_ac F_b^c (ghat) - (1/4) ghat_ab F^2 = Omega^2 ( F_ac F_b^c (g) - (1/4) g_ab F^2(g) ). Dirac + Yukawa : l'action est invariante de Weyl avec les poids donnés (vérifié au Q5 : Lag_D = Omega^4 Lag_D^r), donc That^{D+Y}_ab = Omega^2 T^{D+Y}_ab[psi_r, H_r, A] exactement ; le script 2 le vérifie explicitement pour la partie cinétique symétrisée (y compris la connexion de spin, où les termes en dOmega se compensent), et le terme de Yukawa dans ghat_ab Lag_D est d'ordre Omega^2.

Exprimé en variables rescalées, That_ab (Higgs) est un polynôme en Omega (aucune puissance négative ; vérifié par le script), et sa partie d'ordre Omega^0 est, à la main :

- 2 D_(a H^dagger D_b) H : ordre 0 = 2 Omega_a Omega_b |H_r|^2 ;
- ghat_ab L_0 : ordre 0 = - g_ab ( |dOmega|^2 + m^2 ) |H_r|^2 ;
- 2 xi Ghat_ab |H|^2 avec Ghat_ab = 2 Omega^-1 Omega_ab - 2 Omega^-1 (box Omega) g_ab + 3 Omega^-2 |dOmega|^2 g_ab : ordre 0 = 6 xi |dOmega|^2 |H_r|^2 g_ab ;
- 2 xi ghat_ab boxhat |H|^2 : ordre 0 = 2 xi g_ab g^{cd} (6 Omega_c Omega_d - 2 g_cd |dOmega|^2)|H_r|^2 = -4 xi |dOmega|^2 |H_r|^2 g_ab ;
- -2 xi nablahat_a nablahat_b |H|^2 : ordre 0 = -2 xi ( 6 Omega_a Omega_b - 2 g_ab |dOmega|^2 ) |H_r|^2.

Somme :

    That^(0)_ab = |H_r|^2 [ (2 - 12 xi) Omega_a Omega_b + ( (6 xi - 1)|dOmega|^2 - m^2 ) g_ab ] .

Les ordres Omega^1 et supérieurs de That_ab, ainsi que That^F et That^{D+Y} (ordre Omega^2), ne peuvent contribuer dans (*) qu'à partir de Omega^-1 (pour l'ordre Omega^1 de That) ou Omega^0 (pour l'ordre Omega^2), puisque Omega^-1 nabla(Omega^2 Q) = 2 Omega_nu Q + O(Omega). La plus basse puissance possible est donc Omega^-2 et elle ne reçoit que That^(0).

### Substitution de (3.8) et (2.14)

(3.8) : |dOmega|^2 = -lambda/3 + 2 Omega s + (kappa/12) Omega^2 (Omega^-2 That). (2.14) : Omega_ab = s g_ab - Omega L_ab + (kappa/2) Omega T*_ab, avec L_ab = 0 pour g plat (cohérence vérifiée à la main : (2.14) et (3.8) avec L = 0, insérées dans la formule de Rhat_ab, redonnent exactement Rhat_ab = kappa(That_ab - That ghat_ab/2) + lambda ghat_ab). Pour les coefficients de Omega^-2 et Omega^-1 il suffit de |dOmega|^2 -> -lambda/3 + 2 Omega s et Omega_ab -> s g_ab, les corrections (kappa/12) Omega^2 That et (kappa/2) Omega T*_ab ne touchant que l'ordre Omega^0 ; le script le confirme en refaisant le calcul avec ces corrections incluses (section « Robustesse » : coefficients Omega^-2 et Omega^-1 inchangés).

À l'ordre dominant, That^(0)_ab = alpha Omega_a Omega_b + beta g_ab avec alpha = (2 - 12 xi)|H_r|^2, beta = -(m^2 + 2 lambda xi - lambda/3)|H_r|^2, et tau^(0) = g^{ab} That^(0)_ab = -alpha lambda/3 + 4 beta.

### Coefficient de Omega^-2 (à la main)

Dans (*), le terme Omega^-2 reçoit : Omega_[nu That_lambda]rho = beta Omega_[nu g_lambda]rho (le terme alpha s'annule par antisymétrie) ; -g_rho[nu That_lambda]c Omega^c = -(-alpha lambda/3 + beta) g_rho[nu Omega_lambda] ; et le terme de trace, That = Omega^2 tau, nabla_nu That = 2 Omega Omega_nu tau + O(Omega^2), donc -(1/3) Omega^-2 g_rho[lambda nabla_nu] That -> -(2/3) Omega^-1 g_rho[lambda Omega_nu] tau^(0) = +(2/3) Omega^-1 g_rho[nu Omega_lambda] tau^(0), c'est-à-dire une contribution Omega^-2 après le facteur kappa Omega^-1... (en regroupant correctement les puissances : ce terme est d'ordre Omega^-2 dans RHS). Avec Omega_[nu g_lambda]rho = - g_rho[nu Omega_lambda] :

    C_-2 / kappa = g_rho[nu Omega_lambda] [ -beta + alpha lambda/3 - beta + (2/3)(-alpha lambda/3 + 4 beta) ]
                 = g_rho[nu Omega_lambda] [ (2/3) beta + alpha lambda/9 ]
                 = g_rho[nu Omega_lambda] |H_r|^2 [ -(2/3) m^2 - (8/3) lambda xi + (4/9) lambda ]
                 = -(2/3) ( m^2 + 4 lambda xi - 2 lambda/3 ) |H_r|^2 g_rho[nu Omega_lambda] .

Donc

    C_-2 = (2 kappa/3) ( m^2 + 4 lambda xi - 2 lambda/3 ) |H_r|^2 nabla_[nu Omega g_lambda]rho
         = (kappa/3) ( m^2 + 4 lambda xi - 2 lambda/3 ) ( phi_1^2 + phi_2^2 ) nabla_[nu Omega g_lambda]rho .

### Vérification sympy

Le script 1 calcule les 24 composantes indépendantes de RHS_rho nu lambda (nu < lambda) à partir de (*) sous la forme brute 2 Omega^-1 nablahat_[nu Lhat_lambda]rho, avec That = Higgs(xi) + Maxwell, substitue (2.14) et (3.8), et compare le coefficient de Omega^-2 à K-3 :

- plus basse puissance : Omega^-2 pour toutes les composantes où g_lambda rho ou g_nu rho est non nul, Omega^0 pour les autres (où K-3 vaut aussi zéro) ; aucune puissance inférieure à -2 (assertion) ;
- « coeff Om^-2 - K3 = 0 » pour les 24 composantes ;
- exemple : coeff Om^-2 (rho=0, nu=0, lambda=1) = Omega_1 kappa (phi_1^2 + phi_2^2)(12 lambda xi - 2 lambda + 3 m^2)/18, soit (kappa/3) C (phi_1^2 + phi_2^2) Omega_1 / 2, conforme à K-3.

**Cas xi = 0, H réel (phi_2 = 0)** : C_-2 = (kappa/3)(m^2 - 2 lambda/3) phi_1^2 nabla_[nu Omega g_lambda]rho, nul si et seulement si m^2 = 2 lambda/3 : c'est la condition du théorème 3.1 de Friedrich. (Je n'ai pas eu accès au texte de l'article ; je ne peux affirmer que la concordance de la condition m^2 = 2 lambda/3 telle que rappelée dans la consigne.)

**Jauge, quartique, Yukawa** : That^F_ab = Omega^2 (...) et That^{D+Y}_ab = Omega^2 (...) contribuent à (*) à l'ordre Omega^0 seulement. lambda_h n'apparaît dans That_ab que par -lambda_h |H|^4 ghat_ab = -lambda_h Omega^2 |H_r|^4 g_ab, ordre Omega^2. Le champ A n'apparaît dans That (Higgs) qu'à travers D_a H_r, c'est-à-dire aux ordres Omega^1 et plus ; à l'ordre Omega^1 il entre par Omega Omega_(a ( H_r^dagger D_b) H_r + c.c. ) = Omega Omega_(a d_b) |H_r|^2 où A se compense. Le script confirme : aucun des coefficients de Omega^-2 ni de Omega^-1 ne contient A, F, lambda_h (le Yukawa y n'est pas dans le calcul en composantes mais son poids Omega^2 dans That est établi au Q5). Le coefficient y n'entre pas non plus par l'équation de Higgs puisque celle-ci n'est pas utilisée ici.

**Conclusion Q3.** K-3 confirmé intégralement : plus basse puissance Omega^-2, coefficient (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3)(phi_1^2 + phi_2^2) nabla_[nu Omega g_lambda]rho, aucun A, F, lambda_h, y dans les coefficients singuliers.

**Remarque (hors critères, mais importante pour xi différent de 0).** Le résultat ci-dessus est obtenu « en jets », sans utiliser l'équation de Higgs. Le terme 2 xi ghat_ab boxhat |H|^2 contient H^dagger boxhat_D H + c.c., que l'on peut aussi remplacer par l'équation de Higgs ; cette substitution modifie That_ab à l'ordre Omega^0 (car boxhat_D H = Omega^-2 (...) Omega^3 ...) : la variante « sur couche » du script donne un coefficient de Omega^-2 égal à (1 - 4 xi) fois K-3. La condition d'annulation est la même pour xi différent de 1/4, et pour xi = 1/4 l'équation de Higgs elle-même (Q2) reste singulière si C n'est pas nul, de sorte que la condition globale de régularité du système reste m^2 + 4 lambda xi = 2 lambda/3. Mais le coefficient numérique de K-3 n'est pas intrinsèque pour xi différent de 0 : il dépend de la convention « jets seuls » adoptée par la consigne (« après substitution de (2.14) et (3.8) » uniquement). Sous cette convention, K-3 est exact.

---

## Q4. Terme d'ordre Omega^-1 de (2.17)

Le script extrait le coefficient de Omega^-1 des 24 composantes (après substitution (2.14), (3.8) à l'ordre nécessaire, robustesse vérifiée). Résultat, lisible sur les composantes imprimées :

    C_-1 = (kappa/3) ( m^2 + 4 lambda xi - 2 lambda/3 ) nabla_[nu |H_r|^2 g_lambda]rho
         = (kappa/6) ( m^2 + 4 lambda xi - 2 lambda/3 ) nabla_[nu (phi_1^2 + phi_2^2) g_lambda]rho .

(Exemple : coeff Om^-1 (rho=0, nu=0, lambda=1) = kappa (phi_1 d_1 phi_1 + phi_2 d_1 phi_2)(12 lambda xi - 2 lambda + 3 m^2)/18.) Il ne contient ni s, ni les dérivées secondes de Omega, ni A, F, lambda_h : tout ce qui vient de 2 Omega s dans (3.8), de s g_ab dans (2.14) et des termes Omega Omega_(a d_b)|H_r|^2 de That se compense exactement. Le coefficient de Omega^-1 est donc proportionnel à la même combinaison C et s'annule identiquement lorsque m^2 + 4 lambda xi = 2 lambda/3, pour xi quelconque : le script le confirme composante par composante (« Le coefficient de Om^-1 s annule identiquement sous la condition : True »), et aussi dans la variante « sur couche » du Q3.

Forme compacte de la partie singulière totale, qui résume Q3 et Q4 :

    RHS_rho nu lambda = (kappa/3) ( m^2 + 4 lambda xi - 2 lambda/3 ) Omega^-3 nabla_[nu |H|^2 g_lambda]rho + O(Omega^0) ,

avec |H|^2 = Omega^2 |H_r|^2 (le développement de Omega^-3 nabla(Omega^2 |H_r|^2) redonne exactement C_-2 Omega^-2 + C_-1 Omega^-1).

**Conclusion Q4.** K-4 confirmé. Ce que je n'ai pas établi : la régularité de l'ordre Omega^0 est acquise par définition, mais je n'ai pas vérifié la régularité complète de (2.15) ni des autres équations du système conforme ; pour (2.15) le seul terme matière supplémentaire, -(kappa/24) Omega nablahat_a That = -(kappa/24) Omega d_a (Omega^2 tau), est manifestement régulier.

---

## Q5. Secteur de Dirac

Tétrade ehat^A_mu = Omega^-1 delta^A_mu, connexion de spin omega_mu AB calculée directement à partir de Gammahat (script 2), signe de Sigma_mu = (1/4) omega_mu AB gamma^A gamma^B fixé par le postulat de la tétrade nablahat_mu gammahat^nu = 0 (un seul signe convient ; le script le détermine).

**Covariance conforme** (vérifiée avec le champ de jauge inclus) :

    gammahat^mu Dhat_mu ( Omega^{3/2} psi_r ) = Omega^{5/2} gamma^mu D_mu psi_r .

**Équation de Dirac avec masse de Yukawa** : ( i gammahat^mu Dhat_mu - y H ) psi = 0 avec H = Omega H_r, psi = Omega^{3/2} psi_r :

    Omega^{5/2} [ ( i gamma^mu D_mu - y H_r ) psi_r ] = 0 .

Le coefficient de masse rescalé est y H_r : régulier (ordre Omega^0). Comparaison avec une masse constante m : ( i gammahat.Dhat - m ) psi = Omega^{5/2} [ ( i gamma.D - m Omega^-1 ) psi_r ], coefficient m/Omega singulier. Les deux identités sont vérifiées par le script.

**Terme ghat_ab Lag_D.** Lag_D = psibar ( i gammahat.Dhat - y H ) psi = Omega^{3/2} . Omega^{5/2} psibar_r ( i gamma.D - y H_r ) psi_r = Omega^4 Lag_D^r (vérifié). Donc

    ghat_ab Lag_D = Omega^2 g_ab Lag_D^r : ordre Omega^2, régulier.

Avec masse constante : ghat_ab ( -m psibar psi ) = -m Omega^-2 Omega^3 g_ab psibar_r psi_r = -m Omega g_ab psibar_r psi_r : ordre Omega^1 (vérifié). Le terme de masse constante reste formellement régulier dans ghat_ab Lag_D (puissance positive), mais c'est bien l'ordre Omega^1 contre Omega^2 pour le Yukawa ; la singularité de la masse constante se manifeste dans l'équation de Dirac elle-même (coefficient m/Omega), pas dans ghat_ab Lag_D. (Sur couche, Lag_D est nul dans les deux cas ; les ordres ci-dessus sont ceux des expressions formelles, comme demandé.)

**Tenseur énergie-impulsion de Dirac.** Partie cinétique symétrisée (i/4)[psibar gammahat_(a Dhat_b) psi - (Dhat_(b psibar) gammahat_a) psi] : le script établit That^D_ab = Omega^2 T^D_ab[psi_r, A] exactement, les termes en dOmega de la connexion de spin et du poids 3/2 se compensant. Joint à l'ordre Omega^2 du terme ghat_ab Lag_D, cela justifie l'affirmation du Q3 que le secteur Dirac + Yukawa ne contribue à (2.17) qu'à l'ordre Omega^0.

**Conclusion Q5.** K-5 confirmé.

---

## Ce que je n'ai pas pu établir

1. Je n'ai pas vérifié la forme de (2.17) elle-même (normalisation 2 Omega^-1, placement des indices) ni celle de (2.14), (2.15), (3.8) contre l'article de Friedrich ; elles sont prises comme données. J'ai seulement vérifié leur cohérence mutuelle avec les équations d'Einstein pour g plat, et l'exactitude des formules de Rhat_ab et Rhat fournies.
2. Le calcul en composantes de (2.17) inclut Higgs (avec xi) et Maxwell, mais pas le spineur ; le secteur Dirac + Yukawa est traité par son poids exact Omega^2 dans That_ab (démontré par l'invariance de Weyl de l'action et vérifié symboliquement pour la partie cinétique symétrisée). Je n'ai pas inclus explicitement le terme ghat_ab Lag_D dans le tenseur, mais son ordre Omega^2 est vérifié.
3. Le coefficient de K-3 est exact dans la convention « jets » (sans utilisation de l'équation de Higgs). Avec élimination de H^dagger boxhat_D H par l'équation de Higgs, il est multiplié par (1 - 4 xi) ; la condition d'annulation est inchangée (sauf xi = 1/4, où l'équation de Higgs reste singulière). Je signale cette dépendance de convention sans la compter comme erreur.
4. Je n'ai pas examiné les ordres supérieurs (Omega^0) ni la régularité de l'ensemble du système (en particulier le traitement de Omega^-2 That comme inconnue régulière dans (3.8) et dans l'équation de Higgs, qui suppose que That_ab reste un polynôme en Omega quand on substitue toutes les équations ; c'est vrai en jets, vérifié).
5. Le texte du théorème 3.1 de Friedrich n'a pas été consulté ; la concordance se limite à la condition m^2 = 2 lambda/3 rappelée par la consigne.

---

## Verdict

**CONFIRME.**

Motifs : K-1 (poids Omega^4 des deux courants, courant de Higgs sans dOmega), K-2 (coefficient Omega^-2 de l'équation de Higgs rescalée égal à m^2 + 4 lambda xi - 2 lambda/3), K-3 (plus basse puissance Omega^-2 de (2.17), coefficient (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3)(phi_1^2 + phi_2^2) nabla_[nu Omega g_lambda]rho, absence de A, F, lambda_h, y), K-4 (coefficient de Omega^-1 égal à (kappa/6)(m^2 + 4 lambda xi - 2 lambda/3) nabla_[nu (phi_1^2 + phi_2^2) g_lambda]rho, identiquement nul sous la condition, pour tout xi) et K-5 (coefficient de masse y H_r, ghat_ab Lag_D d'ordre Omega^2 contre Omega^1 pour une masse constante) sont tous dérivés indépendamment et confirmés par les scripts sympy. Réserve de convention (point 3 ci-dessus) : la valeur numérique du coefficient de K-3 pour xi différent de 0 dépend de l'absence d'utilisation de l'équation de Higgs, conformément à l'énoncé ; cela n'affecte ni la plus basse puissance ni la condition de régularité.
