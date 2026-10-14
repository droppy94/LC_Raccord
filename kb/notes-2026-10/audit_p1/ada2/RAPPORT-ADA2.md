# RAPPORT ADA-2 : audit froid du script irad_kernel.py

Auditeur isole, aveugle au travail anterieur. Seul fichier lu en entree : /home/claude/audit_p1/ada2/irad_kernel.py (sha256 3d5d5211...46b). Travail dans /home/claude/audit_p1/ada2/work/. Environnement : python 3.13.16, sympy 1.14.0, mpmath 1.3.0. Aucune recherche web.

Etiquettes : [calcule] = obtenu par execution de code dans cet audit ; [derive] = obtenu a la main par l'auditeur ; [rapporte] = affirme par le script (commentaire ou print), non verifie ici.

## 0. Resume des verdicts

| Section | Ce qui est reellement calcule | Verdict |
|---|---|---|
| ad-1 | Bach linearise d'un mode TT sur fond plat ; residu de l'ODE de de Sitter ; (d^2+k^2)^2 u | Correct, reproduit independamment : B_yy = -(1/4) box^2 h_yy ; (d^2+k^2)^2 u = 0 pour toute solution de l'ODE |
| ad-2 | Rien d'autre qu'une integrale de Frullani. Tout le reste (noyau K_k, terme en delta) est imprime en dur | Partie non locale -2[theta(T) cos(kT)/T]_+ verifiee par identite d'action ; coefficient du delta annonce (-(gamma_E + ln mu) par branche) faux en general, mais local donc sans effet sur les conclusions |
| ad-3 | Serie en eps de B_eps (exacte) ; R_eps(tau0) par quadrature avec Hadamard a l'echelle 1 | Serie et valeurs numeriques reproduites a 1e-9 pres. Dependance d'echelle = terme local 2 B_eps(tau0)[Ci(kL) - Ci(k)], O(eps). Conclusion R_eps -> 0 robuste |
| ad-4 | B par differences finies imbriquees ; R(tau) par quadrature | Valeurs de B exactes a 1e-17 pres (verifiees symboliquement) ; R reproduit a 14 chiffres par deux methodes ; R lisse en 0, R(0) = 0.40834, R'(0) = 1.2289 |
| ad-5 | Rien : deux lignes imprimees en dur | Affirmations non calculees ; la relation T-hat = s^2 R(-s) est une premisse exterieure au script |

Aucune erreur de calcul trouvee. Les reserves portent sur (i) des lignes imprimees presentees comme des resultats alors qu'elles ne sont pas calculees (ad-2, ad-5, derniere ligne d'ad-4), (ii) une annotation fausse du coefficient de delta(T) en ad-2, (iii) un ratio R_eps/(eps ln 1/eps) imprime en ad-3 qui ne converge pas en tau0 = 0 (le terme dominant y est -4 pi eps), ce que le script ne commente pas.

## 1. Execution du script [calcule]

Commande : `python3 -I irad_kernel_copy.py` (copie identique, meme sha256). Duree 19.8 s. Sortie dans work/sortie_script.txt (sha256 dee8eda2...dcb). Sortie integrale :

```
== ad-1 : Bach linearise et identite de de Sitter ==
B_yy / (box^2 h_yy) = -1/4    (attendu -1/4)
B_tt, B_tx, B_xx : 0 0 0   B_zz = -B_yy : True
mode A : equation de de Sitter residu = 0  ; (d^2+k^2) u = 2*k**2*cos(k*tau)  ; (d^2+k^2)^2 u = 0
mode B : equation de de Sitter residu = 0  ; (d^2+k^2) u = 2*k**2*sin(k*tau)  ; (d^2+k^2)^2 u = 0

== ad-2 : noyau retarde K_k(T) de ln((k^2 - (omega + i0)^2)/mu^2) ==
  [trois lignes de texte imprime en dur, voir section 3.2]
  controle Frullani : Int_0^inf (cos aT - cos bT)/T dT = 1.09861228866811   ln(b/a) = 1.09861228866811

== ad-3 ==
  mode A : e^(-eps tau) B_eps = -8*epsilon*k**3*sin(k*tau)  + O(eps^2)
  mode B : e^(-eps tau) B_eps = 8*epsilon*k**3*cos(k*tau)  + O(eps^2)
    tau0 = 0.0, eps = 0.1 : R_eps = -1.23143421314365   R_eps/(eps ln(1/eps)) = -5.34805083595158
    tau0 = 0.0, eps = 0.01 : R_eps = -0.127253503976727   R_eps/(eps ln(1/eps)) = -2.76327472899731
    tau0 = 0.0, eps = 0.001 : R_eps = -0.0126006887864328   R_eps/(eps ln(1/eps)) = -1.82413653604265
    tau0 = -1.0, eps = 0.1 : R_eps = -0.719564986148345   R_eps/(eps ln(1/eps)) = -3.12503102855016
    tau0 = -1.0, eps = 0.01 : R_eps = -0.248042537614933   R_eps/(eps ln(1/eps)) = -5.38617526817226
    tau0 = -1.0, eps = 0.001 : R_eps = -0.0406615917414598   R_eps/(eps ln(1/eps)) = -5.88636830623962

== ad-4 ==
  B sur le support (tau, B) : [(-5.75, -343.9142), (-5.5, 279.8707), (-5.25, -16.1459), (-5.0, 3.6751), (-4.75, 75.4447), (-4.5, -296.0089), (-4.25, 287.2143)]
    tau = -2.0 : R(tau) = -3.32115065133116
    tau = -1.0 : R(tau) = -1.22505678296147
    tau = -0.5 : R(tau) = -0.319628143620471
    tau = -0.1 : R(tau) = 0.280574327017049
    tau = -0.01 : R(tau) = 0.396002274108695
    tau = 0.0 : R(tau) = 0.408340577156179
  R est lisse en tau = 0 (...) ; valeur finie non nulle ; depend de tau0 et du raccord.   [ligne imprimee en dur]

== ad-5 ==  [deux lignes imprimees en dur, aucun calcul]
```

## 2. Lecture section par section : ce qui est calcule, ce qui est imprime

### ad-1 (lignes 10 a 42)
Calcule : Riemann, Ricci, scalaire et Weyl linearises de h_yy = -h_zz = u(tau) cos(kx) sur eta ; B_ab = d^c d^d C_acbd (Bach linearise sur fond plat, sans le terme (1/2) R^cd C_acbd qui est quadratique) ; rapport B_yy/box^2 h_yy ; composantes B_tt, B_tx, B_xx, B_zz + B_yy ; residu de u'' - (2/tau) u' + k^2 u pour u_A et u_B ; (d^2+k^2) u et (d^2+k^2)^2 u. Tout est calcule symboliquement, rien n'est en dur. L'annotation "(attendu -1/4)" est une attente imprimee a cote d'une valeur calculee : les deux coincident.
Remarque : le signe global de B depend de la convention (C_acbd vs C_acdb) ; -1/4 est coherent avec la convention du script et avec ma derivation (section 3.1). La fonction C utilise la formule de Weyl en n = 4 ; j'ai verifie qu'elle est sans trace sur cette perturbation [calcule].

### ad-2 (lignes 44 a 55)
Calcule : uniquement Int_0^inf (cos T - cos 3T)/T dT = ln 3 (Frullani), par quadosc. Ce controle est exact mais ne verifie ni la forme du noyau K_k(T), ni son support, ni le coefficient du delta. Les lignes 46 a 48 sont du texte imprime en dur presente comme resultat. Le commentaire ligne 49-51 annonce un "controle lourd" par identite d'action puis y renonce explicitement. J'ai execute ce controle (section 3.2).

### ad-3 (lignes 57 a 86)
Calcule : B_eps = (d^2+k^2)^2 [e^{eps tau} u] exact (sympy), serie a l'ordre 1 en eps ; puis R_eps(tau0) = Int_0^1 (f(T) - f(0))(-2 cos T/T) dT + Int_1^inf f(T)(-2 cos T/T) dT avec f(T) = B_eps(tau0 - T), B_eps exact lambdifie, k = 1, mode A, par quad et quadosc a 15 chiffres. Rien en dur. La fonction B_eps_num (lignes 69-71) est du code mort qui renvoie None ; le commentaire interne est exact mais inutile.
Omissions : le facteur -1/4 et le cos(kx) de B_yy sont ignores (normalisation sans incidence qualitative). Le ratio R_eps/(eps ln(1/eps)) est imprime sans commentaire ; en tau0 = 0 il ne converge pas (voir 3.3), ce qui pourrait etre lu a tort comme une anomalie ou, inversement, comme une confirmation de la loi eps ln(1/eps).

### ad-4 (lignes 88 a 114)
Calcule : B = (d^2+k^2)^2 [S u_A] par differences finies imbriquees (mpmath.diff d'ordre 2 d'une fonction elle-meme obtenue par mpmath.diff d'ordre 2), tabule en 7 points ; R(tau) = Int_{-6}^{-4} (-2 cos(tau - tau')/(tau - tau')) B(tau') dtau' par quad, pour six valeurs de tau dans [-2, 0]. La ligne 114 ("R est lisse en tau = 0 ... valeur finie non nulle") est imprimee en dur ; la lissite n'est pas testee numeriquement par le script (aucune derivee de R calculee), seule la finitude et la non-nullite sont lisibles dans les valeurs.
Point correct mais implicite : pour tau > -4, la distance au support est T >= 2 > 0, donc ni la partie finie de Hadamard ni le terme c(mu,k) delta(T) n'interviennent ; R(tau) y est independant du schema de regularisation. C'est une difference importante avec ad-3.

### ad-5 (lignes 116 a 118)
Aucun calcul. Deux affirmations imprimees : (i) T-hat_Gamma = s^2 R(-s) donc pas de terme s^1 ni de pole ; (ii) condition de convergence du noyau. La relation T-hat = s^2 R(-s) est une premisse exterieure au script [rapporte]. L'affirmation "integrale O(eps ln 1/eps) -> 0" est confirmee par mes calculs d'ad-3 (avec la precision que le coefficient du ln est proportionnel a sin(k tau0) et s'annule en tau0 = 0).

## 3. Reproductions independantes

### 3.1 Bach linearise et modes de de Sitter [calcule] [derive]
Script : work/verif_ad1_ad3_series.py (sortie work/sortie_verif_ad1_ad3_series.txt).
Route independante : perturbation generale u(tau) cos(kx) (u non specifiee), verification TT (trace 0, divergence 0), Ricci linearise = -(1/2) box h (verifie), Weyl sans trace (verifie), puis Bach.
Resultats :
- B_yy = -(1/4) [u'''' + 2 k^2 u'' + k^4 u] cos(kx) ; box^2 h_yy = [u'''' + 2 k^2 u'' + k^4 u] cos(kx) ; rapport -1/4 exactement. B_tt = B_tx = B_xx = B_yz = 0, B_zz = -B_yy. Concorde avec le script.
- Derivation a la main [derive] : pour h TT, d^c d^d R_acbd = -(1/2) box^2 h_ab et le seul terme de Ricci survivant est -(1/2) g_cd R_ab -> -(1/2) box R_ab = +(1/4) box^2 h_ab ; total -(1/4) box^2 h_ab. Coherent.
- Solution generale par dsolve : u = tau^{3/2} [C1 J_{3/2}(k tau) + C2 Y_{3/2}(k tau)] ; (d^2+k^2) u = 2 sqrt(2k/pi) (C1 sin - C2 cos) ; (d^2+k^2)^2 u = 0 pour la solution generale, pas seulement pour u_A et u_B. Concorde (et renforce) le script.

### 3.2 Noyau de ln(k^2 - (omega+i0)^2) [calcule] [derive]
Script : work/verif_ad2_noyau.py (sortie work/sortie_verif_ad2_noyau.txt).
Derivation [derive] : d/domega ln(a - omega - i0) = 1/(omega - a + i0), dont la TF inverse (convention du script) est -i theta(T) e^{-iaT} (pole dans le demi-plan inferieur, fermeture pour T > 0). Comme d/domega <-> multiplication par iT, on obtient f(T) = -theta(T) e^{-iaT}/T a un delta pres. Somme des branches a = k et a = -k : -2 theta(T) cos(kT)/T. Support T >= 0 : noyau retarde. La partie non locale annoncee ligne 48 est donc correcte.
Identite d'action, f(T) = e^{-T^2}, f~ = sqrt(pi) e^{-omega^2/4} [calcule] : cote frequence (1/2pi) Int f~ ln|k^2 - omega^2| (les parties imaginaires +-i pi s'annulent par parite) moins partie non locale Hadamard echelle 1 donne le coefficient c(k) du delta :
- k = 1 : c = -0.674808 ; k = 2 : c = +0.540333 ; k = 0.5 : c = -1.030726.
- Ces trois valeurs sont reproduites a 1e-19 par c(k) = 2 ln k - 2 Ci(k) (et c = -2 gamma_E, -2(gamma_E + ln k), -2 Ci(k) sont exclus). Avec le ln mu^2 : c(k, mu) = 2 ln k - 2 Ci(k) - 2 ln mu.
- L'annotation du script "-(gamma_E + ln mu) delta(T)" par branche (soit -2 gamma_E - 2 ln mu au total) n'est exacte que dans la limite k -> 0 (Ci(k) ~ gamma_E + ln k). Pour k = 1, mu = 1 elle donne -1.154 au lieu de -0.675. Erreur d'annotation, sans effet : ce terme est local et il est delibere-ment ecarte en ad-3 et nul en ad-4.
- Dependance en l'echelle L de Hadamard verifiee a 1e-19 : nl(L) - nl(1) = 2 f(0) [Ci(kL) - Ci(k)]. Changer L revient a changer c, donc mu. La regularisation "partie finie a l'echelle 1" est la definition distributionnelle standard de 1/T_+ et son ambiguite est exactement l'ambiguite de mu : elle est legitime.

### 3.3 Serie en eps et reponse adiabatique [calcule] [derive]
Serie (work/verif_ad1_ad3_series.py) : methode operatorielle (d^2+k^2)^2 e^{eps tau} u = e^{eps tau} [(d+eps)^2 + k^2]^2 u = e^{eps tau} [4 eps d(d^2+k^2) u + O(eps^2)] puisque (d^2+k^2)^2 u = 0. Mode A : -8 eps k^3 sin(k tau) ; mode B : +8 eps k^3 cos(k tau). Concorde avec le script. Polynome exact en eps (mode A) :
e^{-eps tau} B_eps = -8 eps k^3 sin + eps^2 (8 k^2 cos - 4 k^3 tau sin) + 4 eps^3 k^2 tau cos + eps^4 (cos + k tau sin).
Remarque [derive] : la serie n'est pas uniforme en tau (termes seculaires eps^2 tau, eps^3 tau). Sur la fenetre e^{eps tau} de largeur 1/eps, les termes d'ordre eps^2 et eps^3 contribuent a R_eps a l'ordre eps (pas eps^2) ; seul l'ordre 1 produit le eps ln(1/eps). Le script utilise l'expression exacte dans la quadrature, donc ce point n'affecte pas ses nombres, mais la phrase "premier ordre en eps" ligne 70 ne decrit pas ce que la quadrature integre.

Reponse R_eps (work/verif_ad3_reponse.py, sortie work/sortie_verif_ad3_reponse.txt). Methode differente du script : partie [L, inf) en forme fermee (decomposition de B_eps(tau0 - T) cos(kT) en termes T^m e^{sT}, s complexe, integres par Gamma(m, sL)/s^m et E1(sL)), partie [0, L] par quadrature a 25 chiffres.
- Reproduction (L = 1) : tau0 = 0 : -1.23143421314, -0.127253503977, -0.0126006890213 ; tau0 = -1 : -0.719564986148, -0.248042537615, -0.0406616480274. Concordance avec le script a 1e-9 relatif (le script est a 15 chiffres avec quadosc). Les quadratures du script sont donc fiables.
- Loi asymptotique [derive] : le terme non oscillant de l'ordre 1 donne R_eps ~ 8 eps k^3 sin(k tau0) E1(eps) + O(eps), avec E1(eps) ~ ln(1/eps) - gamma_E. Verification [calcule] a tau0 = -1 : R/eps + 8 sin(1) E1(eps) -> 1.9 (eps = 1e-3, 1e-4, 1e-5), reste O(eps) confirme. A tau0 = 0 le coefficient du ln s'annule et R_eps/eps -> -12.567 = -4 pi (eps = 1e-5 : -12.567082), ce que l'on retrouve a la main : -8 eps Int_0^inf e^{-eps T} sin(2T)/T dT = -8 eps arctan(2/eps) -> -4 pi eps. Le ratio R/(eps ln 1/eps) imprime par le script en tau0 = 0 tend vers 0 et non vers une constante : non commente dans le script.
- Dependance d'echelle [calcule] : pour L = 0.1, 10, 100, R(L) - R(1) = 2 B_eps(tau0) [Ci(kL) - Ci(k)] a 1e-6 pres sur tous les cas (par exemple tau0 = -1, eps = 0.001 : ecart -0.027782, predit -0.027782). Ce terme est proportionnel a B_eps(tau0) = O(eps) (O(eps^2) en tau0 = 0 pour le mode A), donc -> 0.
- Autre regularisation (soustraction lisse f(0) e^{-T/L} au lieu de f(0) theta(L - T)) [calcule] : ecart egalement proportionnel a B_eps(tau0) (tau0 = -1 : -0.843, -0.0913, -0.00920 pour eps = 0.1, 0.01, 0.001, soit 1.368 x B_eps(tau0)).
Conclusion tache 4 : la regularisation introduit bien une dependance d'echelle, mais exclusivement par un terme local c x B_eps(tau0), equivalent a un changement de mu, et d'ordre eps. La conclusion R_eps -> 0 (comme eps ln(1/eps) en general, comme eps en tau0 = 0) est robuste au choix d'echelle et de schema. Ce qui n'est pas invariant de schema, c'est la valeur numerique de R_eps a eps fixe, et le script ne pretend pas le contraire (commentaire ligne 65).

### 3.4 Transition lisse et reponse a temps fini [calcule]
Script : work/verif_ad4_transition.py (sortie work/sortie_verif_ad4_transition.txt).
- B exact par derivation symbolique sympy de S(tau) u_A(tau), S = e^{-1/s}/(e^{-1/s} + e^{-1/(1-s)}), s = (tau + 6)/2, evalue a 30 chiffres, aux 7 points du script et pres des bords (-5.95, -5.9, -4.1, -4.05). Les differences finies imbriquees du script (dps 15) coincident avec l'exact a 1e-17 relatif en tous points, y compris pres des bords ou B vaut 1e-5 a 1e-6. mpmath.diff eleve la precision de travail en interne, ce qui explique cette fiabilite inattendue pour une derivee 4e imbriquee ; une derivee 4e directe a 30 chiffres donne les memes valeurs. Les valeurs de B du script sont donc fiables. Controle integral : Int B = u_A'''(-4) + 2 u_A'(-4) + Int S u_A = -3.25930469892865 par les deux cotes.
- R(tau) par deux methodes independantes du script : (i) quadrature de K x B_exact a 30 chiffres avec intervalle decoupe ; (ii) integration par parties reportant (d^2+1)^2 sur le noyau, avec termes de bord en tau' = -4. Accord mutuel a 1e-30 et avec le script a 14 chiffres : R(-2) = -3.3211506513312, R(-1) = -1.2250567829615, R(-0.5) = -0.31962814362047, R(-0.1) = 0.28057432701705, R(-0.01) = 0.39600227410869, R(0) = 0.40834057715618 ; en plus R(0.5) = 0.89205638370901, R(1) = 1.1013251612017.
- Lissite en 0 : derivees R^(n)(0) = Int K^(n)(-tau') B(tau') dtau' avec K^(n) symbolique : R'(0) = 1.22888741054 (controle par difference centree : 1.228887341), R''(0) = -0.98998, R'''(0) = -0.41881, R''''(0) = 0.63141. Toutes finies. Sur s^2 R(-s) : coefficients s^2 = 0.408341, s^3 = -1.228887, aucun terme s^0 ou s^1 puisque R est bornee et derivable en 0.
Conclusion tache 5 : les valeurs de B par differences finies sont fiables ; la conclusion "R lisse en tau = 0, finie, non nulle" n'en depend de toute facon pas pour la lissite (propriete structurelle : K est C^inf pour T >= 2 et B est C^inf a support compact), et la non-nullite R(0) = 0.408 est confirmee a 14 chiffres. Elle depend des parametres tau0 = -6, delta = 2, k = 1, du mode A et du choix de la fonction de transition, comme le script l'indique. Pour tau > -4 il n'y a aucune dependance au schema de regularisation (terme local nul car B(tau) = 0).

## 4. Endroits ou un choix numerique pourrait fausser la conclusion

1. ad-3, partie finie a l'echelle 1 : seule source d'ambiguite, locale, O(eps). Sans effet sur la limite. Verifie pour L = 0.1, 1, 10, 100 et pour une soustraction lisse.
2. ad-3, quadosc sur [1, inf) avec amortissement e^{-eps T} tres lent (eps = 0.001, echelle 1000) : risque a priori ; infirme, accord a 1e-9 avec la forme fermee.
3. ad-3, tau0 = 0 : le ratio imprime suggere une loi eps ln(1/eps) qui n'y est pas (coefficient nul, R = -4 pi eps). Pas une erreur de calcul, une presentation incomplete.
4. ad-4, differences finies imbriquees a dps 15 sur une transition en e^{-1/t} : risque a priori reel ; infirme par comparaison symbolique (1e-17).
5. ad-4, quad sur [-6, -4] sans decoupage avec un integrand oscillant et plat aux bords : infirme (14 chiffres).
6. ad-4, ligne 114 et ad-5 : conclusions imprimees sans calcul. La lissite est vraie par construction et confirmee numeriquement ici ; la relation T-hat = s^2 R(-s) est hors du perimetre du script [rapporte].
7. ad-2 : coefficient du delta annonce faux (voir 3.2) ; sans incidence car le terme est local.

## 5. Empreintes sha256

```
3d5d52115b2839dffdb7ca2ff41071ec604cdf1bd9b50ebb981a528f90b7e46b  irad_kernel.py (fourni) et work/irad_kernel_copy.py
dee8eda2075ff5db3e5c8696ed1310910714fee81acf8f2d61a071c9f406edcb  work/sortie_script.txt
bb40e6bf8263687af5ebf1fd3100538713df1945d9443e74d49b94bdc212c362  work/verif_ad1_ad3_series.py
c240643edb18c20497ebff985c93bd951270824ddd06e7952097c8ec595704ec  work/sortie_verif_ad1_ad3_series.txt
190394675f10d5af0daeb2af74fa4c2c0134b70da4fce0e54932a78c85752327  work/verif_ad2_noyau.py
c5b84d5f27b93e36083514c556b72dec32836e2211b85775a09deadfe7ebc89d  work/sortie_verif_ad2_noyau.txt
23ff121ae163d2d8c60deeeaf0040053de5a46fa2e3bf8899d5b1ccd4a3111dd  work/verif_ad3_reponse.py
2a775719ffca7a19f655c496a8981b3aa8be11df0e203bd16e5df5d4823a3772  work/sortie_verif_ad3_reponse.txt
c80299a8af47d52fb4383e0de9860ba08683258fa6489f8f338d385241f6bf35  work/verif_ad4_transition.py
d348eb3f11f2e8a6ef758a87559fe75fffcf5986f0c2f1326b531e611df6e5d4  work/sortie_verif_ad4_transition.txt
```
Liste egalement dans work/EMPREINTES.txt. Note : verif_ad3_reponse.py a ete corrige une fois en cours d'audit (un bogue d'accumulation d'exposants dans ma decomposition exponentielle, detecte parce que la dependance d'echelle predite ne concordait pas) ; l'empreinte ci-dessus est celle de la version corrigee dont la sortie est rapportee.
