# RAPPORT YA-2 : audit du script iry_state_v2.py et reproduction independante

Auditeur froid, aveugle au travail anterieur. Perimetre lu : /home/claude/audit_ya2/ uniquement. Date : 2026-10-12.
Etiquettes : [calcule] = obtenu par execution (sympy / mpmath) ; [derive] = obtenu par raisonnement analytique.

## 0. Empreintes sha256

| Fichier | sha256 |
|---|---|
| iry_state_v2.py (script audite) | b72b70f006d24678eb4fb3bf79df22700060eb50cd7bc8bd759a61112647e2e0 |
| work/iry_state_v2_sortie.txt (sortie du script, identique a stdout) | 39621a8963eeb36e5dab4f744d7378e1616c154e05304adeb6749cf4cf985eec |
| work/repro_ya2.py (code de l'auditeur) | b436e6d9387e324e03116ff84d0198a3cc7ca1143ef6f22f20907872424ce716 |
| work/repro_ya2_sortie.txt (sortie du code de l'auditeur) | c8c805e58e42c5f6856339a0ea4cdb512b35e26d695b8a58f5492b16a3138194 |

Le script s'execute sans erreur en 8,8 s (sympy, mpmath) et ecrit iry_state_v2_sortie.txt dans le repertoire courant.

## 1. Ce que le script fait reellement (tache 1)

Le script ne demontre presque rien par le calcul : l'essentiel des « resultats » est imprime en dur (chaines P(...)). Les seuls calculs effectifs sont :

1. deux integrales gaussiennes sympy (m = 1, 3, partie cos) ;
2. une table de coefficients Gamma(a) cos(pi a/2) pour a = m - N + 1, sans integrale ;
3. un controle mpmath de eta x int sin(2 k eta) e^{-k/1000} dk ;
4. une integrale 1D sympy int sin(kr) cos(kT) e^{-ak} dk, a -> 0.

Tout le reste (forme fermee de y-2, « convolution par |.|^(N-4) », comptage y-4, y-5) est de l'affirmation imprimee, etiquetee [calcule] a tort.

Comparaison sortie / pretentions, point par point :

| Ligne de sortie | Verifie ? | Commentaire |
|---|---|---|
| I_1, I_3 gaussiennes entieres | oui [calcule] | retrouve, voir section 2.1 |
| table Gamma(a) cos(pi a/2) | formule juste, annotations fausses | voir 2.2 et 3 |
| « m=3, N=3 : coefficient nul : puissance entiere paire » | annotation fausse | a = 1 est impair ; le coefficient cos s'annule pour a impair |
| controle numerique : valeurs 0.49999, 0.49995, 0.49969, « attendu -> -1/2 » | la valeur numerique est juste, l'annotation est fausse | la limite exacte est +1/2 (section 2.2) |
| « sin-partie ~ -1/(2 eta) » | signe faux | int dk sin(2k eta) = +1/(2 eta) [calcule] |
| y-2 forme fermee 1/(4 pi^2)/(r^2 - (eta+eta')^2) | juste [calcule par l'auditeur], mais non calculee par le script | voir 2.3 |
| « transformee de k^(-N), qui est |.|^(N-4) » | faux / incoherent | le commentaire du code dit r^{N-3} ; l'ordre pertinent est (r-|T|)^{N-1} |
| « (sympy, N=1, mesure k dk) » | mal etiquete | l'integrale calculee est le cas alpha beta* = 1 (N = 0), pas N = 1 |
| y-4 « T-hat ~ s^(N-2) ; pole ssi N = 3 » | non etaye, et faux pour le scalaire conforme | section 2.5 |
| « terme |beta|^2 : bisolution lisse partout » (commentaire) | faux en general | lisse seulement si |beta|^2 est a decroissance rapide |

## 2. Reproduction independante (tache 2)

### 2.1 f gaussienne, f = exp(-k^2/L^2), m = 1 et 3 [calcule]

Parties cos et sin de int_0^inf dk k^m f(k) e^{-2 i k eta} :

- m = 1 : cos = L^2/2 - (sqrt(pi)/2) L^3 eta e^{-L^2 eta^2} erfi(L eta) ; sin = (sqrt(pi)/2) L^3 eta e^{-L^2 eta^2}.
- m = 3 : cos = (L^4/4) e^{-L^2 eta^2} [ (2 L^2 eta^2 - 3)(sqrt(pi) L eta erfi(L eta) - e^{L^2 eta^2}) - e^{L^2 eta^2} ] ; sin = (sqrt(pi)/4) L^5 eta (3 - 2 L^2 eta^2) e^{-L^2 eta^2}.

Series en eta = 0 : series entieres (m=3, cos : L^4/2 - 2 L^6 eta^2 + 2 L^8 eta^4 ... ; sin : (3 sqrt(pi)/4) L^5 eta - ...). Controle numerique mpmath a 12 chiffres : accord. Conclusion : fonctions entieres de eta, le script a raison (il n'avait traite que la partie cos ; la partie sin est aussi entiere).

### 2.2 f = k^{-N}, m = 1 et 3 : regularisation [calcule + derive]

Regularisation justifiee : facteur d'Abel e^{-ak}, a -> 0+. Pour s = m - N + 1 > 0 :

int_0^inf dk k^{s-1} e^{-ak} e^{2 i k eta} = Gamma(s)/(a - 2 i eta)^s  ->  Gamma(s) e^{i pi s/2}/(2|eta|)^s   (eta < 0).

D'ou, avec phase alpha beta* = k^{-N} e^{i phi}, Re(alpha beta* e^{-2 i k eta}) = k^{-N} cos(2 k eta - phi) :

I_m^{phi}(eta) = Gamma(s) cos(pi s/2 + phi) / (2|eta|)^s,   eta < 0.

Verification sympy des limites : s = 1 : i/(2 eta) (Re = 0, Im = 1/(2 eta)) ; s = 2 : -1/(4 eta^2) ; s = 3 : -i/(4 eta^3).

Consequences :
- m = 3, N = 3 (s = 1) : partie cos = 0, partie sin = +1/(2 eta) = -1/(2|eta|). Le controle numerique du script (eta x integrale -> +0.5) est coherent avec +1/(2 eta) ; l'annotation « attendu -1/2 » et « ~ -1/(2 eta) » est fausse. La conclusion « T^w ~ 1/eta » survit au signe, mais ELLE EXIGE sin(phi) differente de 0.
- Le coefficient cos s'annule pour s impair (pas pair) : s = 1 (N = 3) et s = 3 (N = 1) a m = 3.
- Pour s <= 0 (m = 3, N >= 4 ; m = 1, N >= 2) l'integrale DIVERGE en k -> 0 : la « valeur regularisee » du script n'a pas de sens sans coupure IR k0. Avec coupure, int_{k0}^inf = [continuation analytique] - int_0^{k0} (serie de Taylor en eta) ; les poles de Gamma(s) sont compenses ou non par cos(pi s/2 + phi) :
  - s = 0 (N = 4) : phi = 0 -> ln|eta| ; phi = pi/2 -> borne, pas de log.
  - s = -1 (N = 5) : phi = 0 -> |eta| (C^0) ; phi = pi/2 -> eta ln|eta| (C^0).
  - s = -2 (N = 6) : phi = 0 -> eta^2 ln|eta| (C^1) ; phi = pi/2 -> eta|eta| (C^1).
  Le script ecrit « |eta|^(-a) + regulier » pour N = 6 : la forme exacte est eta^2 ln|eta| ; la classe C^1 est bonne.
- N non entier : la formule vaut telle quelle, coefficient generiquement non nul : |eta|^{N-4} pour tout N reel < 4 ; 1/eta exactement ssi N = 3.

### 2.3 Forme fermee de int d^3k/(2k(2 pi)^3) e^{-ik(eta+eta')} e^{ik.(x-x')} [calcule]

Integration angulaire : W_r(T, r) = (1/(4 pi^2 r)) int_0^inf dk sin(kr) e^{-ikT}, T = eta + eta' (mesure dk, et non k dk). Sympy avec e^{-ak} : r/(r^2 + (a + iT)^2) ; limite a -> 0 : Re = r/(r^2 - T^2) hors cone, Im = -(pi/2)[delta(r - T) - delta(r + T)]. Donc

W_r = 1/(4 pi^2) x 1/( |x-x'|^2 - (eta + eta' - i0)^2 ),

singulier sur le cone reflechi |x - x'| = |eta + eta'|, qui coupe le domaine eta, eta' < 0 (eta = eta' = -1, r = 2). Pretention y-2 retrouvee. Le script n'a calcule que la partie reelle (N = 0, alpha beta* = 1), etiquetee a tort « N = 1 ».

Ordre de la singularite pour alpha beta* = k^{-N} : w_N = (1/(4 pi^2 r)) 2 Re[e^{i phi} int dk k^{-N} sin(kr) e^{-ikT}] et int dk k^{-N} e^{ikb} ~ Gamma(1-N)(-ib)^{N-1}, b = r - |T| : singularite transverse en sgn(b)|b|^{N-1} (alpha beta* reel) ou b^{N-1} ln|b| (avec phase), classe exactement C^{N-2}, jamais C^inf. Controle numerique : N = 2, F_2'(2 + d) croit comme ln(1/d) (0.94, 2.09, 3.26, 4.64 pour d = 10^{-1..-4}) ; N = 3, F_3'' tend vers deux limites distinctes (-0.68 / +0.87) de part et d'autre du cone. Le « |.|^(N-4) » imprime par le script (et le « r^{N-3} » du commentaire) sont a remplacer par N - 1 transversalement au cone.

### 2.4 Comportement de T^w(alpha beta*) pour N = 2 a 6, coupure IR k0 = 1 [calcule]

Formes fermees exactes (Abel) pour N <= 3 et controle mpmath pour N >= 4 (J_N(eta) = int_{k0}^inf dk k^{3-N} cos(2 k eta - phi)) :

| N | phi = 0 | phi = pi/2 |
|---|---|---|
| 2 | -cos(2 k0 eta)/(4 eta^2) - k0 sin(2 k0 eta)/(2 eta) ~ -1/(4 eta^2) | (2 k0 eta cos - sin)/(4 eta^2) ~ -2 k0^3 eta/3 : REGULIER |
| 3 | -sin(2 k0 eta)/(2 eta) -> -k0 : REGULIER, pas de 1/eta | cos(2 k0 eta)/(2 eta) ~ 1/(2 eta) |
| 4 | ~ -ln|eta| (ecarts de ln 2 entre eta et eta/2) | borne, J' -> -2 : eta ln|eta| en sous-dominant, C^0 |
| 5 | J' -> +pi en 0- : terme |eta|, C^0 | J'' ~ -2/eta : eta ln|eta|, C^0 |
| 6 | J'' ~ 2c ln|eta| : eta^2 ln|eta|, C^1 | J'' -> const avec saut : eta|eta|, C^1 |

Bilan y-1 corrige : T^w(alpha beta*) ~ Gamma(4-N) cos(pi(4-N)/2 + phi) (2|eta|)^{N-4} + regulier. Le 1/eta exige N = 3 ET sin(phi) non nul. Pour N = 3 et alpha beta* reel positif, il n'y a AUCUNE singularite en eta = 0 (le script a vu le zero du coefficient mais ecrit « remplacer par le terme suivant / log » : il n'y a pas de terme suivant, la fonction est reguliere).

### 2.5 Le tenseur energie-impulsion du scalaire CONFORME ne contient pas de terme alpha beta* [calcule]

Point decisif, absent du script. Calcul complet par mode de T_{mu nu} = d_mu phi d_nu phi - (1/2) g_{mu nu}(d phi)^2 + xi (g_{mu nu} Box - d_mu d_nu) phi^2 avec v_k = alpha u_k + beta u_k*, etat homogene et isotrope, apres moyenne angulaire k_i k_j -> k^2 delta_ij/3 (sympy) :

- terme croise alpha beta* de <T_00> : 0, pour tout xi (les contributions phi'^2 et (grad phi)^2 se compensent exactement, le terme en xi est nul par homogeneite) ;
- terme croise de <T_ij>/delta_ij : (k/3)(6 xi - 1) [alpha beta* e^{-2 i k eta} + c.c.] ;
- terme croise de <phi^2> : (1/(2k)) [alpha beta* e^{-2 i k eta} + c.c.] (non nul : c'est lui que le script derive).

Pour xi = 1/6 (champ conforme, objet declare du script), le terme alpha beta* de <T_{mu nu}> est identiquement nul. Le tenseur d'etat se reduit a rho = int d^3k/(2 pi)^3 k |beta_k|^2, p = rho/3, independant de eta. C'est le resultat classique : pour un champ sans masse a couplage conforme, les termes d'interference de Bogoliubov ne contribuent pas a <T_{mu nu}> ; ils contribuent a <phi^2> et, pour xi different de 1/6, a la pression avec le facteur (xi - 1/6). Seule la partie sans trace d'un etat ANISOTROPE survivrait a xi = 1/6.

Le passage « T^w ~ d d w » du script est donc une erreur d'objet : il calcule d^2/d eta^2 de la limite de coincidence du terme alpha beta* de w (c'est-a-dire de <phi^2>), pas T^w. Toute la chaine y-1 -> y-4 (comportement |eta|^{N-4} de T^w, pole ssi N = 3) ne s'applique au tenseur que pour xi different de 1/6, et seulement a la pression.

## 3. Erreurs relevees (tache 3)

1. Erreur d'objet (majeure) : pour le scalaire conforme, le terme alpha beta* de T^w est nul (2.5). La pretention y-1 porte en realite sur <phi^2> ou sur T_ij a xi non conforme.
2. Signe : « attendu -1/2 » et « sin-partie ~ -1/(2 eta) » ; la valeur est +1/2 et +1/(2 eta) (le controle numerique du script lui-meme donne +0.4999, en contradiction avec son annotation).
3. Annotation « puissance entiere paire » pour a = 1, 3 : ce sont les a impairs qui annulent cos(pi a/2).
4. Regularisation non justifiee : pour m - N + 1 <= 0 les integrales divergent en k -> 0 ; la « valeur regularisee » n'est definie qu'avec coupure IR, qui ajoute une serie de Taylor (en particulier un terme lineaire en eta si sin(phi) non nul) ; pour les cas a = -2n les poles de Gamma donnent des logs (eta^2 ln|eta| pour N = 6) que le script ne mentionne pas.
5. « coupure UV implicite non necessaire pour m - N < -1 » : c'est la coupure IR qui est necessaire dans ce cas, et la coupure UV (Abel) qui est necessaire pour m - N >= -1 ; le commentaire inverse les roles.
6. Conclusion non etayee : « N = 3 donne 1/eta » n'est vrai que si sin(phi) non nul ; pour phi = 0 la fonction est reguliere (2.4). Le script le signale a moitie (« avec phase generique ») mais la table et la conclusion generale l'oublient.
7. y-2 : la forme fermee n'est pas calculee par le script (contrairement a l'en-tete « forme fermee calculee a la main par sympy ») ; l'integrale sympy effectuee est le cas alpha beta* = 1, mal etiquete « N = 1 » ; l'exposant « |.|^(N-4) » est faux (commentaire : r^{N-3} ; correct : singularite transverse d'ordre N - 1, classe C^{N-2}).
8. Terme |beta|^2 : qualifie de « lisse partout ». Il est invariant par translation en eta (donc sans effet en eta -> 0, ce qui est le point utile), mais il est singulier sur le cone de lumiere ordinaire (eta - eta')^2 = r^2 des que |beta|^2 decroit en puissance ; avec |alpha beta*|^2 = |beta|^2 (1 + |beta|^2), une queue alpha beta* ~ k^{-N} impose |beta|^2 ~ k^{-2N}, singularite de classe C^{2N-2} sur le cone ordinaire. L'etat est non Hadamard par les deux termes.
9. Cas limites oublies : N non entier (la formule vaut, exposant N - 4 generique, 2.2) ; phase phi (determine lequel des deux coefficients s'annule) ; phase dependante de k (deplace la singularite, section 4) ; |beta|^2 non negligeable (pas d'effet sur eta -> 0 mais sur le caractere Hadamard) ; etats anisotropes (partie sans trace survit a xi = 1/6).
10. Etiquetage : des lignes purement imprimees portent [calcule] (y-2 forme fermee, y-4).

## 4. Contre-exemples (tache 4) [calcule + derive]

Question : famille alpha beta* avec T^w ~ 1/eta en eta -> 0- et w sans singularite dans le domaine eta, eta' < 0 ? Reponse : non.

- (i) Phase lineaire alpha beta* = k^{-3} e^{2 i k eta_0} (etat translate en temps) : int dk e^{2ik(eta_0 - eta)} = -i/(2(eta - eta_0)) : pole en eta_0, pas en 0. Si eta_0 < 0 la singularite de T^w est dans le domaine ; si eta_0 > 0, T^w est lisse en 0- mais w est singulier sur le cone r = |eta + eta' - 2 eta_0| qui coupe le domaine. Pas de contre-exemple.
- (ii) Oscillant alpha beta* = k^{-3} cos(k l) : int dk cos(k l) e^{-2 i k eta} = 2 i eta/(l^2 - 4 eta^2) : poles en eta = +-l/2, rien en 0 ; w singulier sur les cones r = |T +- l|. Pas de 1/eta.
- (iii) Support compact alpha beta* = k^{-3} 1_{k < K} : int_0^K dk e^{-2 i k eta} = (1 - e^{-2 i K eta})/(2 i eta), fonction entiere ; w entiere en (T, x). Ni 1/eta ni cone.
- (iv) Argument general : w_ab(T, x) = int d^3k/(2k(2 pi)^3) 2 Re(alpha beta* e^{-ikT}) e^{ik.x} est une solution distributionnelle de l'equation des ondes en (T, x) sur tout R^4. Si T^w ~ 1/eta, w_ab n'est pas lisse au point (T, x) = (0, 0). Par propagation des singularites (le front d'onde d'une solution de Box u = 0 est invariant par le flot bicaracteristique nul), cette singularite se propage le long des rayons nuls T = -|x| vers T < 0, c'est-a-dire aux points eta + eta' = T < 0, |x - x'| = |T|, par exemple eta = eta' = T/2 < 0. Donc toute famille (temperee, homogene) donnant T^w ~ 1/eta rend w singulier dans le domaine. Les familles oscillantes deplacent la singularite, les supports compacts la suppriment avec le 1/eta.
- Pour le scalaire conforme la question est vide : T^w n'a pas de terme alpha beta* (2.5).

## 5. Verdicts (tache 5)

- y-1 (T^w ~ |eta|^{N-4}, 1/eta pour N = 3 seulement, entiere pour gaussienne) : INFIRMEE pour le champ scalaire conforme tel que declare : le terme alpha beta* du tenseur est identiquement nul en etat homogene isotrope, T^w est independant de eta (terme |beta|^2 seul). RETROUVEE AVEC CORRECTIONS en tant qu'enonce sur la limite de coincidence de <phi^2> (ou sur la pression a xi different de 1/6) : exposant N - 4 avec coefficient Gamma(4-N) cos(pi(4-N)/2 + phi), 1/eta ssi N = 3 et sin(phi) non nul (regulier pour alpha beta* reel), logs aux N pairs (N = 4 : ln ; N = 6 : eta^2 ln), coupure IR obligatoire pour N >= 4, signe du 1/eta inverse dans le script, parite inversee dans l'annotation. Partie gaussienne : retrouvee.
- y-2 (singularite du terme alpha beta* sur le cone reflechi, dans le domaine) : RETROUVEE. Forme fermee 1/(4 pi^2 (r^2 - (T - i0)^2)) verifiee ; cone atteint dans le domaine ; pour k^{-N}, classe exactement C^{N-2} (le script donne un exposant faux et un etiquetage N = 1 errone, mais la conclusion « ordre fini, jamais C^inf » tient). Complement : le terme |beta|^2 est lui aussi singulier (cone ordinaire) pour une decroissance en puissance.
- y-4 (T-hat = s^2 T_plat ; terme s^1 ssi N = 3) : INFIRMEE pour le scalaire conforme : T_plat^w = constante, T-hat ~ s^2 exactement, aucun terme s^1 quel que soit N. RETROUVEE AVEC CORRECTION pour un scalaire a xi different de 1/6 (pression seulement) : T-hat ~ s^{N-2}, terme s^1 ssi N = 3 et sin(phi) non nul ; pour N < 3 le terme est plus singulier que s^1, pour 3 < N < 4 moins singulier mais non lisse ; la coupure IR n'ajoute qu'un terme s^3 (jamais s^1).

Fichiers : /home/claude/audit_ya2/work/repro_ya2.py, /home/claude/audit_ya2/work/repro_ya2_sortie.txt, /home/claude/audit_ya2/work/iry_state_v2_sortie.txt.
