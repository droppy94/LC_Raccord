# RAPPORT ADA-1 : noyau retarde non local et onde de de Sitter (derivation aveugle)

Auditeur froid, isole. Aucun fichier lu hors de /home/claude/audit_p1/ada1/. Aucune recherche bibliographique. Calculs sympy 1.14.0 et mpmath 1.3.0, scripts et sorties dans /home/claude/audit_p1/ada1/work/. Date : 2026-10-13.

Etiquettes : [calcule] = resultat verifie par script ; [derive] = derivation analytique a la main, verifiee numeriquement lorsque c'est indique.

## 0. Conventions adoptees

- eta = diag(-1, 1, 1, 1), coordonnees (tau, x, y, z), box = -d_tau^2 + d_x^2 + d_y^2 + d_z^2.
- Riemann linearise : R_abcd = (1/2)(d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac) ; Ricci R_bd = eta^{ac} R_abcd.
- Weyl (n = 4) : C_abcd = R_abcd - (1/2)(g_ac R_bd - g_ad R_bc - g_bc R_ad + g_bd R_ac) + (R/6)(g_ac g_bd - g_ad g_bc).
- Bach linearise sur fond plat : B_ab = d^c d^d C_acbd (le terme (1/2) R^cd C_acbd est d'ordre eps^2 et disparait).
- Transformee de Fourier temporelle : f(T) = Int dw/(2 pi) e^{-i w T} f~(w), donc f~(w) = Int dT e^{i w T} f(T). Avec cette convention, « retarde » = analytique dans le demi-plan Im w > 0 = support en T > 0.

Un changement de signe global de la convention de Riemann ou de Bach change le signe du coefficient de la question 1 ; le point structurel (proportionnalite a box^2 h et annulation sur u_A, u_B) n'en depend pas.

## 1. Tenseur de Bach sur une perturbation TT ; solutions u_A, u_B [calcule]

Script : work/q1_bach_sympy.py, sortie work/q1_bach_sympy.out.

### 1.1 Proportionnalite a box^2 h_ab

Derivation (a la main, puis verifiee) : pour h transverse (d^a h_ab = 0) et sans trace, R_ab^(1) = -(1/2) box h_ab, R^(1) = 0. Alors

- d^c d^d R_acbd = -(1/2) box^2 h_ab (les trois autres termes contiennent une divergence ou la trace) ;
- la partie Ricci du Weyl donne -(1/2) box R_ab = +(1/4) box^2 h_ab (les termes d^c R_cb et d^c d^d R_cd sont nuls).

Resultat :

    B_ab[h] = -(1/4) box^2 h_ab        (h transverse, sans trace, conventions ci-dessus).

Verification sympy a deux niveaux :
1. sur la perturbation de l'enonce h_yy = -h_zz = u(tau) cos(kx) : divergence [0,0,0,0], trace 0, R_ab + (1/2) box h_ab = 0, R = 0, et la matrice B_ab + (1/4) box^2 h_ab est identiquement nulle. Explicitement B_yy = -(1/4)(u'''' + 2 k^2 u'' + k^4 u) cos(kx) = -(1/4) (d_tau^2 + k^2)^2 u cos(kx).
2. sur une onde plane TT generique h_ab = e_ab exp(i(-w tau + p.x)), e_ab symetrique quelconque (10 composantes), avec les 5 contraintes p^a e_ab = 0 et eta^{ab} e_ab = 0 resolues par sympy : B_ab + (1/4) box^2 h_ab = 0 identiquement, box^2 h_ab = (p^2)^2 h_ab, p^2 = -w^2 + |p|^2.

### 1.2 Solutions de u'' - (2/tau) u' + k^2 u = 0

sympy.dsolve donne u = tau^{3/2}(C1 J_{3/2}(k tau) + C2 Y_{3/2}(k tau)), soit sous forme elementaire :

    u_A(tau) = cos(k tau) + k tau sin(k tau),
    u_B(tau) = sin(k tau) - k tau cos(k tau),

residu de l'EDO nul pour les deux, Wronskien W = k^3 tau^2 (non nul pour tau != 0). Forme complexe : (1 - i k tau) e^{i k tau} = u_A + i u_B. Au voisinage du point singulier tau = 0 les deux solutions sont regulieres : u_A = 1 + k^2 tau^2/2 + O(tau^4), u_B = k^3 tau^3/3 + O(tau^5).

### 1.3 Action de (d_tau^2 + k^2)^2

    (d^2 + k^2) u_A = 2 k^2 cos(k tau),     (d^2 + k^2)^2 u_A = 0,
    (d^2 + k^2) u_B = 2 k^2 sin(k tau),     (d^2 + k^2)^2 u_B = 0.

Consequence : box^2 h_ab = (d_tau^2 + k^2)^2 u cos(kx) = 0 pour toute combinaison lineaire u = a u_A + b u_B, donc

    B_ab[h] = 0 identiquement sur les solutions exactes,

et par suite T_ab[h] = ln(-box/mu^2) B_ab[h] = 0 trivialement, quelle que soit la prescription (retardee, avancee, Feynman) et quelle que soit l'echelle mu. Remarque : h n'est pas solution de l'equation d'onde plate (box h != 0 puisque (d^2+k^2) u_A = 2 k^2 cos != 0), mais elle est dans le noyau de box^2, c'est-a-dire Bach-plate au premier ordre. Tout T non nul ne peut donc provenir que d'un ecart de u aux solutions exactes (branchement, facteur adiabatique, etc.), et sa valeur depend alors de cet ecart, c'est-a-dire de l'histoire.

## 2. Noyau temporel retarde K_k(T) [derive, verifie numeriquement]

Script : work/q2_q3_noyau_adiabatique.py (section Q2), sortie work/q2_q3_noyau_adiabatique.out.

### 2.1 Derivation

Soit L(w) = ln((k^2 - (w + i0)^2)/mu^2) = ln(k - w - i0) + ln(k + w + i0) - 2 ln mu. Sa derivee est une somme de deux poles retardes :

    dL/dw = 1/(w - k + i0) + 1/(w + k + i0).

Or Int dw/(2 pi) e^{-i w T} /(w - a + i0) = -i theta(T) e^{-i a T} (fermeture dans le demi-plan inferieur pour T > 0). Donc la transformee inverse de dL/dw est -2 i theta(T) cos(kT). Comme la transformee inverse de dL/dw vaut i T K(T) (integration par parties), on obtient l'equation distributionnelle

    T K(T) = -2 theta(T) cos(kT),

dont la solution generale est K(T) = -2 Pf[theta(T) cos(kT)/T] + C delta(T). Le coefficient C se fixe par une valeur de L : en w = i a (a > 0), L(ia) = ln((k^2 + a^2)/mu^2) = Int_0^inf e^{-aT} K(T) dT. Avec la partie finie de Hadamard a l'echelle T0,

    Pf_{T0} Int_0^inf F(T)/T dT := Int_0^{T0} (F(T) - F(0))/T dT + Int_{T0}^inf F(T)/T dT,

et les integrales de Frullani Int_0^inf (e^{-aT} cos kT - e^{-bT})/T dT = ln b - (1/2) ln(a^2 + k^2) et Int_0^inf (e^{-bT} - theta(T0 - T))/T dT = -gamma - ln(b T0), on trouve C = -2 ln(mu T0 e^gamma). Resultat :

    K_k(T) = -2 Pf_{T0}[ theta(T) cos(kT)/T ] - 2 ln(mu T0 e^gamma) delta(T).

### 2.2 Proprietes demandees

- Support : T >= 0 (noyau strictement retarde ; K = 0 pour T < 0). Verification de signe : pour w reel > k, Im L(w + i0) = -pi, reproduit numeriquement (voir 2.3).
- Singularite en T = 0 : non integrable, de type 1/T (partie finie de Hadamard obligatoire). La partie finie depend de l'echelle T0 choisie, mais la combinaison totale (Pf + terme delta) n'en depend pas : changer T0 deplace une constante entre la partie non locale et la partie locale.
- Comportement T -> infini : K ~ -2 cos(kT)/T, decroissance lente (en 1/T) et oscillante a la frequence k. Le noyau n'est pas absolument integrable : la convergence de la convolution est conditionnelle et repose sur les oscillations.
- Partie locale : -2 ln(mu T0 e^gamma) delta(T). Toute la dependance en mu est locale (elle provient du -2 ln mu de L). Le choix T0 = 1/(mu e^gamma) annule le terme delta et met toute l'information dans la partie finie ; le choix T0 = 1/k donne K = -2 Pf_{1/k}[...] - 2 ln(mu e^gamma / k) delta(T).
- Realite : K est reel (L(-w) = conj L(w)).

### 2.3 Verification numerique [calcule]

Pour k = mu = 1, T0 = 1 (C = -1.15443...), Int_0^inf e^{i w T} K(T) dT recalcule par mpmath coincide avec ln((k^2 - w^2)/mu^2) pour w = i, 0.5 i, 0.5 + 0.3 i, 2 + 0.3 i, 3 + 0.1 i, -3 + 0.1 i, 0.3 + 0.05 i, avec des ecarts de 1e-28 a 1e-30 (precision 30 chiffres). Le resultat est inchange pour T0 = 0.5, 2, 5. Pour w = 3 + 0.02 i, Im L = -3.1266 -> -pi (signe retarde correct, continuite dans le demi-plan superieur).

## 3. Histoire adiabatique u_eps = e^{eps tau} u_A [calcule]

Script : work/q2_q3_noyau_adiabatique.py (section Q3), meme sortie.

### 3.1 B_eps a l'ordre eps

Identite exacte : (D^2 + k^2)^2 (e^{eps tau} u_A) = e^{eps tau} ((D + eps)^2 + k^2)^2 u_A. sympy donne

    B_eps(tau) = e^{eps tau} [ -8 eps k^3 sin(k tau)
                              + eps^2 (8 k^2 cos(k tau) - 4 k^3 tau sin(k tau))
                              + 4 eps^3 k^2 tau cos(k tau)
                              + eps^4 (cos(k tau) + k tau sin(k tau)) ].

A l'ordre eps : B_eps = -8 eps k^3 e^{eps tau} sin(k tau) + O(eps^2). Il n'y a pas de croissance seculaire a cet ordre ; les termes en tau apparaissent a partir de eps^2 (et sont attenues par e^{eps tau} pour tau -> -inf). B_eps(0) = 8 eps^2 k^2 + eps^4 (ordre eps^2 : la partie locale delta ne contribue qu'a l'ordre eps^2).

### 3.2 Regularisation declaree

R_eps(0) = Int_0^inf K(T) B_eps(-T) dT avec K de la section 2 : partie finie de Hadamard a l'echelle T0 pour la singularite 1/T en T = 0, plus le terme local -2 ln(mu T0 e^gamma) B_eps(0). k = mu = 1. Calcul numerique avec T0 = 1 et, en controle, T0 = 3 (le resultat doit etre identique) ; queue oscillante decoupee en periodes jusqu'a T = 60/eps ; precision 30 chiffres.

### 3.3 Forme fermee

Toutes les integrales sont elementaires (Int e^{-eps T} sin(2kT)/T = arctan(2k/eps), Frullani pour les termes en cos^2(kT)/T) ; les dependances en T0 et en gamma se compensent exactement entre la partie finie et le terme delta, comme il se doit :

    R_eps(0) = -8 eps k^3 arctan(2k/eps) + 8 eps^2 k^4/(eps^2 + 4k^2) + 4 eps^2 k^2 + 2 eps^4 k^2/(eps^2 + 4k^2)
               + (8 eps^2 k^2 + eps^4) ln( eps sqrt(eps^2 + 4k^2) / mu^2 ).

### 3.4 Resultats numeriques (k = mu = 1)

| eps   | R_eps(0) numerique (T0 = 1) | numerique (T0 = 3)  | forme fermee        | -4 pi eps     | R_eps(0)/eps |
|-------|-----------------------------|---------------------|---------------------|---------------|--------------|
| 0.1   | -1.2854863215924            | -1.2854863215924    | -1.2854863215924    | -1.2566370614 | -12.8549     |
| 0.01  | -0.12779335700145           | -0.12779335700145   | -0.12779335700145   | -0.1256637061 | -12.7793     |
| 0.001 | -0.012606087484694          | -0.012606087484694  | -0.012606087484694  | -0.0125663706 | -12.6061     |

Accord numerique / forme fermee a 14 chiffres, independance en T0 verifiee.

### 3.5 Limite et borne

Developpement (sympy) : R_eps(0) = -4 pi k^3 eps + eps^2 (8 k^2 ln(eps/mu) + 8 k^2 ln(2k/mu) + 10 k^2) + O(eps^4 ln eps) (ecrit ici pour k = mu = 1 dans le script : -4 pi eps + eps^2 (8 ln eps + 8 ln 2 + 10) + ...).

- Limite eps -> 0 : R_eps(0) -> 0, lineairement en eps. La reponse non locale retardee s'eteint avec le branchement adiabatique ; le terme dominant -4 pi k^3 eps est purement non local (il vient de arctan(2k/eps) -> pi/2, donc de toute la queue en 1/T du noyau), independant de mu ; la dependance en mu (partie locale) n'apparait qu'a l'ordre eps^2 ln eps.
- Borne analytique : puisque |arctan| < pi/2 et que les autres termes sont O(eps^2 |ln eps|), on a pour 0 < eps <= 1/2 et k = mu = 1
    |R_eps(0)| <= 4 pi eps + 7.4 eps^2 |ln eps| <= 13 eps,
  et plus precisement |R_eps(0) + 4 pi k^3 eps| <= C eps^2 |ln eps|. Verification numerique sur une grille 1e-10 <= eps <= 0.56 : sup |R_eps(0)|/eps = 12.99, sup |R_eps(0) + 4 pi eps|/(eps^2 |ln eps|) = 7.32 (eps < 0.5).

Remarque importante : la limite eps -> 0 de R_eps n'est pas uniforme vis-a-vis de l'ordre des limites ; a eps fixe, B_eps est non nul sur tout l'axe et la reponse integre une memoire de longueur 1/eps. La valeur limite 0 est coherente avec B[h] = 0 sur u_A.

## 4. Histoire a emission finie u = S(tau) u_A [calcule]

Script : work/q4_q5_emission_finie.py, sortie work/q4_q5_emission_finie.out. k = 1, tau0 = -6, delta = 2, S(tau) = f((tau - tau0)/delta) avec f(xi) = g(xi)/(g(xi) + g(1 - xi)), g(x) = e^{-1/x} (transition C^infini standard, S(-5) = 1/2).

### 4.1 Support de B[h]

B = (D^2 + k^2)^2 (S u_A) cos(kx) est nul pour tau < tau0 (S = 0) et pour tau > tau0 + delta (S = 1 et (D^2 + k^2)^2 u_A = 0). B[h] est donc a support compact dans la fenetre de branchement [-6, -4], ou il prend des valeurs de l'ordre de 10^2 (B(-5.5) = 279.9, B(-4.5) = -296.0 ; les derivees quatriemes de la transition sont grandes). Controles : Int cos(k tau') B = 0 et Int tau' cos(k tau') B = 0 a 1e-19 pres ; Int sin(k tau') B = -2 k^3 exactement, egal au concomitant bilineaire J[sin, u_A] (terme de bord en tau0 + delta, ou S u_A = u_A ne s'annule pas), verifie par sympy.

### 4.2 R(tau) pour tau > tau0 + delta

Pour tau > -4, tau - tau' > 0 sur tout le support de B : la singularite en T = 0 et le terme delta ne sont jamais atteints, et

    R(tau) = -2 Int_{-6}^{-4} cos(k(tau - tau'))/(tau - tau') B(tau') dtau'.

Quadrature de Gauss-Legendre composite (16 puis 32 sous-intervalles, resultat identique a 15 chiffres).

| tau  | R(tau)              |
|------|---------------------|
| -2   | -3.32115065133116   |
| -1   | -1.22505678296147   |
| -0.5 | -0.319628143620471  |
| -0.1 |  0.280574327017049  |
|  0   |  0.408340577156179  |

### 4.3 Reponses aux questions

- R est-elle lisse en tau = 0 ? Oui. L'integrande est analytique en tau pour tau > -4 (le noyau derive sous l'integrale) ; derivees en 0 : R(0) = 0.408341, R'(0) = 1.228887, R''(0) = -0.989980, R'''(0) = -0.418808, R''''(0) = 0.631408 ; le polynome de Taylor d'ordre 4 reproduit R(-0.1) = 0.280574 (ecart 4e-8, d'ordre s^5). R est en fait analytique sur ]-4, +inf[ ; tau = 0 n'y joue aucun role particulier (le point singulier de l'EDO en tau = 0 n'est pas vu par R, qui ne depend de u_A qu'a travers B).
- Sa valeur en 0 est-elle nulle ? Non : R(0) = 2 Int cos(k tau') B(tau')/tau' dtau' = 0.408340577 (k = 1, tau0 = -6, delta = 2). Il n'existe pas de raison structurelle d'annulation : cos(k tau')/tau' n'est pas dans le noyau de (D^2 + k^2)^2, contrairement a cos et sin (dont les moments de B s'annulent ou se reduisent a un terme de bord).
- Depend-elle de tau0 ? Oui, fortement et de maniere oscillante :

| tau0 | R(0)          | tau0 R(0) |
|------|---------------|-----------|
| -5   | 0.700271      | -3.501    |
| -6   | 0.408341      | -2.450    |
| -8   | 0.181816      | -1.455    |
| -12  | 0.093296      | -1.120    |
| -20  | 0.014087      | -0.282    |
| -40  | 0.007141      | -0.286    |
| -80  | 0.000984      | -0.079    |

R(0) decroit grossierement comme 1/|tau0| (queue du noyau) avec des oscillations en cos(k tau0) ; elle depend aussi de delta (0.205, 0.408, 0.577 pour delta = 1, 2, 3) et de la forme de S. Autrement dit, la reponse en tau = 0 est entierement une fonction de l'histoire du branchement, pas de l'etat local de la perturbation.

## 5. Condition de convergence et de lissite ; developpement de T-hat = s^2 R(-s) [derive]

### 5.1 Condition

R(tau) = Int_{-inf}^{tau} K(tau - tau') B(tau') dtau' avec K ~ -2 cos(kT)/T a grand T et une singularite Pf en T = 0. Deux conditions :

(i) Convergence en tau' -> -inf. Condition suffisante absolue : Int_{-inf}^0 |B(tau')| /(1 + |tau'|) dtau' < inf (par exemple B a support compact, ou B = O(|tau'|^{-a}) avec a > 0, ou B exponentiellement amortie comme dans l'histoire adiabatique). Si B ne decroit pas, la convergence n'est que conditionnelle et il y a un piege de resonance : une composante de B en cos(k tau') de meme frequence que le noyau donne un integrande en cos^2(kT)/T ~ 1/(2T), divergence logarithmique infrarouge ; une composante en sin(k tau') donne sin(2kT)/(2T), convergente. C'est exactement ce qui se produit dans l'histoire adiabatique : le terme d'ordre eps de B_eps est en sin(k tau) (convergent et fini quand eps -> 0), tandis que les termes en cos(k tau) sont d'ordre eps^2 et produisent les ln eps.

(ii) Lissite au voisinage de tau = 0. Il faut et il suffit que B soit C^infini au voisinage de 0 (alors R, convolution de la distribution K a support dans T >= 0 avec une fonction lisse, est lisse). Le cas le plus simple et le plus net est B identiquement nul sur un voisinage ]-a, 0] : la partie finie et le terme local delta ne sont plus sollicites, R est analytique au voisinage de 0 et independante de mu. En termes de u : u doit etre, au voisinage de 0, une combinaison exacte a u_A + b u_B (a, b constantes) ; tout ecart lisse a la solution exacte dans ce voisinage donne une contribution locale en -2 ln(mu T0 e^gamma) B(tau) et une contribution Pf, toutes deux lisses mais dependantes de mu.

Dans le cadre de l'enonce (u = solution exacte de l'EDO de de Sitter, branchee a une date finie ou adiabatiquement), B[h] est nul pres de 0 (respectivement O(eps)), et R est lisse en 0 ; sa valeur R(0) est en general non nulle et fixee par l'histoire du branchement (section 4) ; elle tend vers 0 lorsque le branchement est repousse a l'infini (en 1/|tau0|, section 4.3) ou rendu adiabatique (en eps, section 3.5).

### 5.2 Premier ordre en s de T-hat = s^2 R(-s)

Si R est lisse en 0 : R(-s) = R(0) - s R'(0) + s^2 R''(0)/2 + ..., donc

    T-hat(s) = R(0) s^2 - R'(0) s^3 + O(s^4).

- Le premier ordre non nul est s^2 (coefficient R(0), non nul en general ; pour tau0 = -6, delta = 2 : 0.408341 s^2 - 1.228887 s^3 + ...). Si de plus R(0) = 0 (histoire particuliere), il est en s^3. Si B[h] = 0 identiquement (solution exacte sur tout l'axe), T-hat = 0.
- Il ne peut pas y avoir de terme lineaire en s, ni de terme constant : un terme c s dans T-hat exigerait R(-s) ~ c/s, un pole en tau = 0, ce qui est exclu par la lissite (condition (ii)). Numeriquement T-hat/s = 0.0280, 0.00396, 0.000407 pour s = 0.1, 0.01, 0.001 : tend vers 0 lineairement, et T-hat/s^2 -> R(0) = 0.40834.

| s     | R(-s)           | T-hat(s)         | T-hat/s         |
|-------|-----------------|------------------|-----------------|
| 1     | -1.22505678     | -1.22505678      | -1.22505678     |
| 0.3   | -0.00278765     | -2.50888e-4      | -8.36294e-4     |
| 0.1   |  0.28057433     |  2.80574e-3      |  2.80574e-2     |
| 0.03  |  0.37103037     |  3.33927e-4      |  1.11309e-2     |
| 0.01  |  0.39600227     |  3.96002e-5      |  3.96002e-3     |
| 0.001 |  0.40711119     |  4.07111e-7      |  4.07111e-4     |

## 6. Synthese des conclusions

1. Pour h TT, B_ab = -(1/4) box^2 h_ab (conventions de la section 0). Les solutions u_A = cos + k tau sin, u_B = sin - k tau cos de l'EDO de de Sitter verifient (d^2 + k^2)^2 u = 0 : B[h] = 0 et T[h] = 0 identiquement sur les solutions exactes, pour toute prescription et toute echelle mu.
2. Le noyau retarde est K_k(T) = -2 Pf[theta(T) cos(kT)/T] - 2 ln(mu T0 e^gamma) delta(T) : support T >= 0, singularite 1/T en 0 (partie finie obligatoire), queue oscillante en -2 cos(kT)/T non absolument integrable, partie locale portant toute la dependance en mu. Verifie numeriquement a 1e-28.
3. Branchement adiabatique : B_eps = -8 eps k^3 e^{eps tau} sin(k tau) + O(eps^2) ; R_eps(0) = -4 pi k^3 eps + O(eps^2 ln eps) (forme fermee et numerique en accord a 14 chiffres : -1.28549, -0.127793, -0.0126061 pour eps = 0.1, 0.01, 0.001 avec k = mu = 1) ; limite 0, borne |R_eps(0)| <= 13 eps pour eps <= 1/2.
4. Branchement a date finie : B a support dans [tau0, tau0 + delta] ; R est analytique pour tau > tau0 + delta, en particulier lisse en 0 ; R(0) = 0.408341 n'est pas nulle et depend de tau0, delta et de la forme de S (decroissance oscillante ~ 1/|tau0|).
5. Condition : B integrable contre 1/(1 + |tau'|) a l'infini (gare a la resonance cos(k tau')) et nul, ou au moins C^infini, pres de 0. Alors T-hat = s^2 R(-s) = R(0) s^2 - R'(0) s^3 + ... : premier ordre s^2, jamais de terme lineaire en s (il exigerait un pole de R en 0).

Point d'attention pour le programme (hors de ma connaissance du travail anterieur) : toute valeur attribuee a T[h] ou a T-hat en tau = 0 sur la base de ce calcul est une fonctionnelle de l'histoire de branchement de la perturbation, pas une propriete de la solution de de Sitter elle-meme, qui est Bach-plate et donne T = 0.

## 7. Empreintes sha256

Scripts :

    7174432cbc03495aa2a1b89eb8afbce4b94350210cc209b526cf03a8504e5f96  work/q1_bach_sympy.py
    1275768fe5caf2b90a1c3b48f2ab5d445c7c74f0be10ba87c87f10c6ba2d0359  work/q2_q3_noyau_adiabatique.py
    5a2a424aa624b2a7cbca7e2db8d0d7a53e06a1bad2e8aab5daf3653385f167d6  work/q4_q5_emission_finie.py

Sorties :

    8fd32871c2030348dfe1a8d2d6a8a587a03b86a86903cc205d71654272a6f0a5  work/q1_bach_sympy.out
    08584833922dac55c226fff4eef65fd94b2ef645ab1ec6c102ab8258fb6fe230  work/q2_q3_noyau_adiabatique.out
    c1dec7210991cc7a74a63905285992b9af6cadfd311e95eff4fdecde55d8a05f  work/q4_q5_emission_finie.out

Temps de calcul : q1 38 s, q2_q3 8 min 20 s (precision 30 chiffres, queues jusqu'a T = 60/eps), q4_q5 2 min. Versions : python3, sympy 1.14.0, mpmath 1.3.0.
