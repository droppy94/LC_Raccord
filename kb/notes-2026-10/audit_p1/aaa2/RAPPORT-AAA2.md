# RAPPORT AAA-2 : audit froid du script iraa_aniso_v2.py

Date : 2026-10-13. Auditeur isole, aveugle au travail anterieur. Seul fichier lu : /home/claude/audit_p1/aaa2/iraa_aniso_v2.py (sha256 c3a30a362ea2d7f2b1bee80ae292b5507123e2471892a287e1de8c3811fc32a1). Aucune recherche web. Etiquettes : [calcule] (obtenu par mon code), [derive] (obtenu a la main et verifie), [rapporte] (affirme par le script, non verifiable ici).

## 0. Resume des conclusions

1. Le resultat central (terme alpha beta*, phase e^{-ik(eta+eta')}, tenseur ameliore xi = 1/6, coincidence) est juste et reproduit independamment : T_00 = 0, T_0i = 0, T_ij = (k_i k_j - k^2 delta_ij/3) e^{-2 i k eta}, trace 4D nulle, partie isotrope nulle, tout le terme est dans la partie sans trace spatiale. [calcule]
2. Le controle numerique N = 3 est correct dans ses chiffres (quadosc et forme fermee concordent) mais son annotation « (attendu -1/2) » est fausse : la quantite imprimee, eta * Int_0^inf dk sin(2 k eta) e^{-ak}, tend vers +1/2 (pour eta < 0 comme pour eta > 0). Erreur de signe dans le texte en dur, pas dans le calcul. [calcule]
3. Plusieurs lignes « resultats » de la section aa-2, et la totalite des sections aa-3 et aa-4, sont du texte imprime en dur, non calcule par le script. La formule Gamma(4-N)(2 i eta)^{N-4} (N < 4, regularisation d'Abel) est juste ; les affirmations aa-3/aa-4 sont [rapporte].
4. Contre-exemples : aucun. Si alpha beta* est a decroissance rapide en |k| uniformement en direction (sens Schwartz sur R^3, c'est le sens du critere Hadamard), la partie sans trace de T_ij est bornee uniformement en eta par (2/3)(2pi)^{-3} Int d^3k k |alpha beta*| et continue ; un comportement en 1/eta est impossible quelle que soit la dependance angulaire. Le 1/eta du cas k^{-3} vient de la queue ultraviolette (k ~ 1/|eta|), pas de l'infrarouge. Un cas limite construit (decroissance gaussienne direction par direction mais nulle sur un axe) reproduit un 1/eta, mais il n'est pas a decroissance rapide sur R^3 et n'est pas Hadamard : ce n'est pas un contre-exemple au sens de la question. [derive, calcule]

## 1. Execution du script (tache 1)

Commande : python3 -I iraa_aniso_v2.py, duree 3,6 s, code de retour 0. Sortie sauvegardee dans work/sortie_script.txt (sha256 8afe1323b87207816e49ab874747a2ac96d334d7870a653c5da597b2d7e1d420).

Resultats calcules par le script (extraits) :

- terme |beta|^2 : T_00 = k^2, T_0i = k k_i, T_ij = k_i k_j, trace 4D = 0 ;
- terme alpha beta* : T_00 = 0, T_0i = 0, T_ij = A k_i k_j + B delta_ij avec A = e^{-2 i eta k}, B = -(k^2/3) e^{-2 i eta k}, trace 4D = 0, trace spatiale = 0, partie isotrope = 0 ;
- controle N = 3 : eta * I = 0,49999 ; 0,49995 ; 0,49969 (eta = -0,1 ; -0,05 ; -0,02), annote « (attendu -1/2) » ;
- gaussienne : expression sympy en erfc et exp.

## 2. Ce que le script calcule reellement (tache 2)

### 2.1 Objet calcule

- Tenseur : le tenseur energie-impulsion ameliore classique du scalaire sans masse, T_mn = d_m phi d_n phi - (1/2) g_mn (d phi)^2 - xi (d_m d_n - g_mn box) phi^2, xi = 1/6, en espace de Minkowski plat (pas de terme en courbure, « ordre zero en eps » selon l'en-tete). Il est applique comme operateur bilineaire par point-splitting a une fonction de deux points w(x,x'), puis evalue a la coincidence x' = x. Le produit d_m phi d_n phi est symetrise en (1/2)(d^x_m d^x'_n + d^x_n d^x'_m) w, ce qui est le bon choix pour la partie symetrique (la partie antisymetrique de la fonction de deux points est independante de l'etat et disparait dans w = omega_2 - H).
- Signature : g = diag(-1,+1,+1,+1), utilisee a la fois comme g_mn et g^mn (legitime, g^{-1} = g). Le d'Alembertien est box = -d_eta^2 + Laplacien. La trace nulle obtenue pour les deux structures de phase confirme la coherence interne du signe du terme d'amelioration : avec le signe oppose, la trace vaudrait -2(d phi)^2 - phi box phi et ne s'annulerait pas sur un mode sur couche. [derive]
- Etat : etat de Bogoliubov homogene (transformation alpha_k, beta_k diagonale en k), dont la fonction de deux points par mode a quatre structures de phase. Le script ne calcule que deux d'entre elles, par mode, en omettant le facteur 1/(2k(2pi)^3) :
  - P2 = e^{ik(eta-eta')} e^{ik.(x-x')} (coefficient |beta|^2) ;
  - P3 = e^{-ik(eta+eta')} e^{ik.(x-x')} (coefficient alpha beta*).
  Le facteur phi^2 du terme d'amelioration est pris egal a w a la coincidence (w0 = e^{-2ik eta} pour P3, w0 = 1 pour P2), ce qui est correct.
- Structure de phase : j'ai verifie [derive] que, pour phi = somme_k (a_k u_k + a_k^+ u_k*) avec u_k = e^{-ik eta + ik.x}/sqrt(2k(2pi)^3) et a_k = alpha_k b_k + beta_k* b_{-k}^+, la fonction de deux points dans le vide des b contient bien |alpha|^2 e^{-ik(eta-eta')}, |beta|^2 e^{+ik(eta-eta')}, alpha_k beta_{-k}* e^{-ik(eta+eta')} et son conjugue, toutes multipliees par e^{ik.(x-x')}/(2k(2pi)^3). Les structures P2 et P3 du script sont donc les bonnes. Pour un etat anisotrope le coefficient de P3 est alpha_k beta_{-k}*, pas alpha_k beta_k* ; le script n'en dit rien (sans consequence pour la structure tensorielle par mode).

### 2.2 Concordance commentaires / calcul

- Le commentaire de la ligne 19 dit « P1 = e^{-ik(eta-eta')} (vide, soustrait) ». C'est inexact : apres soustraction du vide, la structure P1 garde le coefficient |alpha|^2 - 1 = |beta|^2 (comme la ligne 18 le dit elle-meme). La structure P1 apporte au terme |beta|^2 la meme contribution que P2 (T_00 = k^2, T_0i = -k k_i au signe pres de k, T_ij = k_i k_j, verifie [calcule] dans work/repro_T3.py). Le script ne calcule donc que la moitie du secteur |beta|^2 ; la densite d'energie complete est Int d^3k/(2pi)^3 k |beta_k|^2 et non la moitie. Ceci n'affecte pas le terme alpha beta*, objet de la note, mais le commentaire est trompeur.
- La structure conjuguee P4 = e^{+ik(eta+eta')} (alpha* beta) n'est pas calculee ; la section aa-2 la prend en compte implicitement par « 2 Re[...] ». Acceptable.
- Ligne 61 : « moyenne angulaire isotrope => 0 (YA-2 retrouve) » : la moyenne angulaire de (n_i n_j - delta_ij/3) est bien nulle [derive]. La reference « YA-2 » est [rapporte].
- Ligne 64 : « T_00 = k^2 (independant de eta) » : exact pour P2.

### 2.3 Lignes imprimees en dur, presentees comme resultats

| Ligne | Texte imprime | Statut |
|---|---|---|
| 72 | I(eta) = Gamma(4-N)(2 i eta)^{N-4} pour N<4 ; N=3 : 1/(2 i eta) ; N=4 : log ; N>=5 : coupure IR | En dur. Formule juste au sens de la regularisation d'Abel (verifiee, section 4). « N>=5 : coupure IR » est juste mais incomplet : l'integrale est alors divergente en k -> 0 pour tout eta, il n'y a plus de loi en eta sans coupure. |
| 81 | « (attendu -1/2) » | En dur et FAUX (signe). La bonne valeur attendue est +1/2. |
| 85 | « -> entiere en eta (erf, exp) » | En dur ; l'affirmation est juste (expression du script verifiee numeriquement, section 4). |
| 88 a 91 | toute la section aa-3 | En dur, aucun calcul. Enonces plausibles mais [rapporte] ; voir remarque 2.4. |
| 94 a 95 | toute la section aa-4 | En dur, aucun calcul ; depend d'une equation « (2.17) » et d'un facteur s externes au fichier. [rapporte] |

Le premier commentaire du fichier signale que la v1 avait un « controle numerique aa-2 defectueux, quad non oscillante ». La v2 utilise quadosc et imprime en plus la forme fermee ; les deux concordent a 10^-16 pres. Le defaut residuel est l'annotation de signe.

### 2.4 Annotations fausses ou fragiles

1. Signe « attendu -1/2 » (ligne 81) : faux, voir section 4.
2. Ligne 90 : « un multiplicateur de Fourier homogene de degre 0 [...] preserve le front d'onde ». Un operateur pseudo-differentiel d'ordre 0 verifie WF(Pu) inclus dans WF(u), avec egalite seulement la ou le symbole est elliptique (f(k^) non nul). « Preserve » est trop fort si f s'annule dans certaines directions ; l'enonce reste vrai pour la conclusion visee (la singularite du cone reflechi subsiste dans toute direction ou f ne s'annule pas). Nuance, pas erreur.
3. Section aa-2, cas N = 3 : pour alpha beta* reel, Re[1/(2 i eta)] = 0 ; le terme dominant en 1/eta n'existe que par la phase e^{i phi} (partie imaginaire de alpha beta*). Le script inclut cette phase dans la definition « k^{-N} Y_2(k^) e^{i phi} » et son controle numerique porte sur la partie en sinus, donc il est coherent, mais la phrase « N=3 : 1/(2 i eta) -> 1/eta » devrait preciser que le coefficient est sin(phi)/(2 eta). Pour phi = 0 le terme regularise est a/(a^2+4 eta^2), c'est-a-dire une distribution concentree sur eta = 0, pas une loi en 1/eta. [derive, calcule]
4. Ligne 72 pour N < 3 : l'integrale diverge a l'ultraviolet (pas seulement conditionnellement) ; la formule Gamma ne vaut qu'au sens de la regularisation d'Abel (facteur e^{-ak}, a -> 0+) ou de la distribution. Le texte dit « analytique » sans le preciser.

## 3. Reproduction independante du resultat central (tache 3)

Script : work/repro_T3.py (sha256 303deee7903cb3a7442e36ba4cbd54548fa1c428f886cd908be98ae8cab7ca9f), sortie work/sortie_repro_T3.txt (sha256 cb87d5675abd0a4c00038b017d3b9e0b003f6250a55e2af8af0f3d802a6c9c75). Formulation differente de celle du script : la fonction de deux points est ecrite comme produit f(x) h(x') de deux fonctions d'un point, les composantes k1, k2, k3 sont cartesiennes avec k = sqrt(k1^2+k2^2+k3^2) (pas d'angles), et l'operateur bilineaire est code a part. Un second controle, purement numerique, remplace la differentiation symbolique par des differences finies centrees (mpmath, 30 decimales, h = 10^-6) sur trois vecteurs k et trois points tires au hasard.

Resultats [calcule] :

- T_00 = 0 ; T_0i = 0 ;
- T_ij - (k_i k_j - k^2 delta_ij/3) e^{-2 i k eta} = 0 (matrice nulle) ;
- trace 4D g^{mn} T_mn = 0 ; trace spatiale T_ii = 0 ; partie isotrope T_ii/3 = 0 ;
- differences finies : ecart maximal |T_num - T_theorique| = 2,6 x 10^-12 (coherent avec h^2).

Derivation a la main [derive], pour controle : avec w = e^{-ik(eta+eta')} e^{ik.(x-x')}, d^x_0 d^x'_0 w = -k^2 w, d^x_i d^x'_j w = k_i k_j w, le terme croise temps-espace est antisymetrique sous l'echange (x,x') et disparait par symetrisation ; (d phi)^2 = g^{ab} d_a d'_b w = (k^2 + k^2) w = 2 k^2 w ; donc la partie canonique donne T_00 = -k^2 + k^2 = 0 et T_ij = (k_i k_j - k^2 delta_ij) w. L'amelioration avec w0 = e^{-2ik eta} : d_0 d_0 w0 = -4k^2 w0, box w0 = +4k^2 w0, d'ou une contribution nulle a T_00 et +(2/3) k^2 delta_ij w0 a T_ij. Total T_ij = (k_i k_j - k^2 delta_ij/3) e^{-2ik eta}.

Decomposition : trace 4D nulle (et trace spatiale nulle, puisque T_00 = 0) ; partie sans trace = tout le tenseur, A = e^{-2ik eta} fois (k_i k_j - k^2 delta_ij/3), partie isotrope nulle. Concordance complete avec le script (A = exp(-2 I eta k), B = -k^2 exp(-2 I eta k)/3). La signification physique : dans cette convention, le terme d'interference alpha beta* ne contribue ni a la densite d'energie ni au flux ni a la pression isotrope, seulement a une contrainte anisotrope oscillante en e^{-2ik eta}, qui s'annule apres moyenne angulaire pour un etat isotrope.

Le terme |beta|^2 (structure P2) est aussi reproduit : T_00 = k^2, T_0i = k k_i, T_ij = k_i k_j, trace nulle.

## 4. Controle numerique du cas N = 3 (tache 4)

Scripts : work/controle_N3_et_contreexemples.py (sha256 18fb1050171e8460667bf1970bd41c92c6446b4e52e0eb4d1941a7ab7dae32c2, sortie work/sortie_controle.txt, sha256 2a258b202085da089df1564babd7c47cd4b38270443dc30ddb359a2ecfd60490) et work/controle_gamma.py (sha256 7b349d367bce0b4a6bedabb0ea31c9946bfd93f9a10f239e479a2111dbeddc3d, sortie work/sortie_gamma.txt, sha256 33a2990a62c6333f7dc542d3bf8af7a89605a8312111bfaed44dda3c39e83b21).

Forme fermee [calcule, sympy] : Int_0^inf dk sin(2 k eta) e^{-ak} = 2 eta/(a^2 + 4 eta^2) ; Int_0^inf dk cos(2 k eta) e^{-ak} = a/(a^2 + 4 eta^2) ; donc Int_0^inf dk e^{-2ik eta} e^{-ak} = 1/(a + 2 i eta).

Limite a -> 0+ (eta non nul) : eta * Int sin = 2 eta^2/(a^2 + 4 eta^2) -> +1/2, independamment du signe de eta. Quadrature amortie par morceaux (independante de quadosc) : 0,499988 (eta = -0,1), 0,499950 (eta = -0,05), 0,499688 (eta = -0,02), 0,499950 (eta = +0,05), en accord avec la forme fermee et avec les chiffres imprimes par le script.

Verdict : les valeurs numeriques du script sont justes ; l'annotation « (attendu -1/2) » est fausse par le signe. L'origine probable de l'erreur : Int_0^inf dk e^{-2ik eta} = 1/(2 i eta) = -i/(2 eta), dont la partie imaginaire eta * Im = -1/2 correspond a -Int sin ; le script integre +sin et conserve l'attendu de -Im. Pour que l'annotation soit juste il faudrait integrer -sin(2 k eta) (ou annoncer +1/2).

Formule generale (ligne 72) [calcule, controle_gamma.py] : pour a > 0 fixe, Int_0^inf k^{3-N} e^{-(a+2i eta)k} dk = Gamma(4-N)(a + 2 i eta)^{N-4} verifiee a 10^-12 pres pour N = 2,5 ; 3 ; 3,5 et a = 0,2 ; 0,05. La limite a -> 0+ donne Gamma(4-N)(2 i eta)^{N-4} en branche principale (arg(2 i eta) = -pi/2 pour eta < 0), module Gamma(4-N)(2|eta|)^{N-4}. L'enonce du script est donc juste pour N < 4 au sens de la regularisation d'Abel.

Gaussienne (ligne 84-85) : l'expression sympy du script pour Int_0^inf k^3 e^{-k^2/L^2} e^{-2ik eta} dk concorde avec une quadrature directe a 10^-12 pres en eta = -0,7 ; -0,05 ; 0 (L = 1,3). Elle est entiere en eta et bornee par L^4/2 sur l'axe reel. [calcule, derive]

## 5. Recherche de contre-exemples (tache 5)

Question : existe-t-il une dependance angulaire de alpha beta* ou une loi de decroissance telle que la partie sans trace de T_ij se comporte en 1/eta quand eta -> 0 tout en provenant d'un alpha beta* a decroissance rapide en |k| ?

Reponse : non, et c'est demontrable par une borne uniforme. [derive]

Ecrivons F(k) = alpha_k beta_{-k}* et n = k/|k|. Avec le resultat de la section 3 (et son conjugue pour alpha* beta) :

T^tf_ij(eta) = (2 pi)^{-3} Int_0^inf dk k^3 Re[ e^{-2ik eta} M_ij(k) ],   M_ij(k) = Int dOmega F(k, n) (n_i n_j - delta_ij/3).

Le facteur angulaire est borne : |n_i n_j - delta_ij/3| <= 2/3. Donc, pour tout eta reel,

|T^tf_ij(eta)| <= (2/3)(2 pi)^{-3} Int d^3k |k| |F(k)|.

Si F est a decroissance rapide en |k| (uniformement en direction, c'est-a-dire |F(k)| <= C_M (1+|k|)^{-M} pour tout M, le sens usuel de « rapidement decroissant » sur R^3 et le sens du critere Hadamard rappele par le script lui-meme a la ligne 91), le membre de droite est fini. T^tf est alors borne uniformement en eta, continu (lemme de Riemann-Lebesgue : c'est une transformee de Fourier en eta d'une fonction integrable de k), et meme C^infini puisque tous les moments Int dk k^{3+m} |M_ij(k)| existent. Un comportement en 1/eta, ou toute divergence quand eta -> 0, est impossible. La dependance angulaire de F n'intervient que par M_ij(k), qui est bornee par (2/3) Int dOmega |F| : elle fixe le tenseur Q_ij, pas la loi en eta. Il suffit meme que Int d^3k |k| |F| soit fini (decroissance en k^{-N} avec N > 4) pour conclure a la bornitude.

Origine du 1/eta du cas N = 3 : c'est un effet ultraviolet. Dans Int_0^inf dk e^{-2ik eta}, la contribution dominante vient de k ~ 1/|eta| -> infini. Avec une coupure ultraviolette K, Int_0^K dk e^{-2ik eta} = (1 - e^{-2iK eta})/(2 i eta) tend vers K quand eta -> 0 : fini. L'infrarouge ne peut pas produire un 1/eta non plus : pres de k = 0 le facteur e^{-2ik eta} est regulier en eta ; une decroissance en k^{-N} avec N >= 4 a l'infrarouge rend T infini pour tout eta (coupure necessaire), ce qui n'est pas une loi en eta.

Cas limite examine [calcule] : F(k, theta) = i exp(-k^2 theta^{4/3}), theta angle polaire. Pour chaque direction theta > 0, F est gaussienne en k ; mais sur l'axe theta = 0, F = i pour tout k. Le moment angulaire M_zz(k) se comporte en c k^{-3} (verifie : k^3 M_zz = 2,7021 ; 2,7829 ; 2,7841 ; 2,7842 pour k = 5 ; 20 ; 80 ; 320, limite theorique c = 2 pi (2/3) Int_0^inf u e^{-u^{4/3}} du = 2,7842), d'ou un N = 3 effectif et eta * Int dk k^3 M_zz sin(2 k eta) -> c/2 = 1,392 (valeurs 0,925 ; 1,249 ; 1,352 pour eta = -0,2 ; -0,1 ; -0,05, convergence lente attendue en O(eta)). Ce cas donne bien un 1/eta a partir d'une F « rapidement decroissante direction par direction », mais il ne repond pas a la question posee : F n'est pas a decroissance rapide sur R^3 (aucune decroissance sur l'axe), l'etat n'est pas Hadamard (le cone reflechi reste singulier dans la direction de l'axe), et l'hypothese du critere de la ligne 91 est violee. Il montre seulement que l'hypothese « decroissance rapide dans TOUTES les directions » doit etre comprise avec uniformite en direction, ce qui est le cas de la formulation Schwartz standard.

Conclusion de la tache 5 : pas de contre-exemple. La proposition « alpha beta* a decroissance rapide (au sens Schwartz) implique T^tf plat borne et regulier en eta, donc aucun pole en 1/eta » est etablie par la borne ci-dessus, independamment de la structure angulaire.

## 6. Points a corriger dans le script

1. Ligne 81 : remplacer « (attendu -1/2) » par « (attendu +1/2) », ou integrer -sin(2 k eta).
2. Ligne 19 : « P1 (vide, soustrait) » est trompeur ; P1 porte |beta|^2 apres soustraction et contribue au secteur |beta|^2 autant que P2.
3. Ligne 72 : preciser « au sens de la regularisation d'Abel / distribution » pour N <= 3, et que pour N = 3 le coefficient du 1/eta est sin(phi)/(2 eta) (nul pour alpha beta* reel).
4. Sections aa-3 et aa-4 : ce sont des enonces imprimes, non des calculs ; a etiqueter comme tels dans la sortie.

## 7. Empreintes sha256

| Fichier | sha256 |
|---|---|
| iraa_aniso_v2.py (script audite) | c3a30a362ea2d7f2b1bee80ae292b5507123e2471892a287e1de8c3811fc32a1 |
| work/sortie_script.txt (sortie du script audite) | 8afe1323b87207816e49ab874747a2ac96d334d7870a653c5da597b2d7e1d420 |
| work/repro_T3.py | 303deee7903cb3a7442e36ba4cbd54548fa1c428f886cd908be98ae8cab7ca9f |
| work/sortie_repro_T3.txt | cb87d5675abd0a4c00038b017d3b9e0b003f6250a55e2af8af0f3d802a6c9c75 |
| work/controle_N3_et_contreexemples.py | 18fb1050171e8460667bf1970bd41c92c6446b4e52e0eb4d1941a7ab7dae32c2 |
| work/sortie_controle.txt | 2a258b202085da089df1564babd7c47cd4b38270443dc30ddb359a2ecfd60490 |
| work/controle_gamma.py | 7b349d367bce0b4a6bedabb0ea31c9946bfd93f9a10f239e479a2111dbeddc3d |
| work/sortie_gamma.txt | 33a2990a62c6333f7dc542d3bf8af7a89605a8312111bfaed44dda3c39e83b21 |
| work/sha_script.txt | 51fb4a75e08185abdc53ee06093fe6fc353c96329adae3aa5d3f28b110c48422 |

Note sur la sortie de controle_N3_et_contreexemples.txt : le bloc « Formule Gamma » de ce script utilise une quadrature tronquee a k = 4000 avec a = 10^-4, insuffisante pour N = 2,5 et N = 3 (ecarts visibles dans la sortie). Ce bloc est remplace par controle_gamma.py (a = 0,2 et 0,05, intervalle adapte), dont les resultats font foi. Les autres blocs de controle_N3_et_contreexemples.py (tache 4, gaussienne, cas limite) ne sont pas affectes.
