# RAPPORT AA-2 : audit adverse de NOTE-BORD-EON-197-AF-EXECUTION et de af_check.py (v2)

Auditeur isole, adverse. Pieces lues : la note 197, af_check.py (v2), af_check_sortie.txt, af_check_v1_defectueux.py et sa sortie, les consignes AA-2 et AA-1. Rien d'autre n'a ete ouvert.
Dossier de travail : /home/claude/AF/auditaf/work_aa2/ (toutes les variantes et leurs sorties y sont).

## 0. Reproduction

- af_check.py copie en work_aa2/af_check_copie.py (sha256 identique : 9c184b32...e4c). Execution : 1 min 44 s, sortie work_aa2/sortie_copie.txt **identique octet pour octet** a af_check_sortie.txt.
- diff v1 / v2 relu ligne a ligne : (i) signe de la partie spatiale W_ijkl (v1 : -, v2 : +) ; (ii) jetify etendu aux fonctions F ; (iii) comparaisons au pole et a Omega^1 faites apres reduction de n.n sur l'expression entiere ; (iv) jets d'ordre 3 ajoutes ; (v) symboles de calibration declares reels. La sortie v1 montre bien trace non nulle, ajustement du pole vide, logs non annules, calibration en echec et plantage en AF-2 : la v1 est correctement qualifiee de defectueuse et les cinq defauts annonces dans l'en-tete de la note sont exactement ceux du diff.

## E1. Parametrisation du Weyl et forme fermee de T

**Genericite.** Variante work_aa2/v_E1_weyl.py (sortie v_E1_weyl_sortie.txt) : resolution lineaire de toutes les symetries de Weyl sur les 256 composantes (antisymetries, symetrie de paires, identite cyclique, trace) : dimension **10** ; rang de l'application (E_ij, B_ij) -> W du script : **10**. La parametrisation est donc un isomorphisme sur l'espace des tenseurs de Weyl : generique. Le choix de l'axe x0 n'entraine aucune perte, n restant un covecteur symbolique quelconque soumis a (3.8).

**Completude des verifications.** Le script ne teste que la trace (1,3) et l'identite cyclique a premier indice fixe. C'est suffisant en principe (antisymetries et symetrie de paires sont imposees par construction dans setW ; l'identite cyclique a premier indice fixe, avec ces symetries, equivaut a la cyclicite complete ; la trace (1,3) avec les symetries donne toutes les traces). La variante verifie quand meme explicitement antisymetrie, symetrie de paires et trace (1,4) : True. Remarque : le controle « traceless » de la v1 avait bien detecte l'erreur de signe, ce qui confirme que le test est discriminant.

**Forme fermee.** Variante v_E1_variation.py : au premier ordre, C^abcd R_abcd[h] = -2 C^abcd d_a d_c h_bd (verifie symboliquement pour C de Weyl generique et h quelconque). D'ou delta(b Int sigma C^2) = -4 b Int d_a d_c(sigma C^abcd) h_bd et, avec T_ab = -2/sqrt(g) dS/dg^ab = +2 dS/dg_ab,

  T_ab = -8 b d^c d^d (sigma C_acbd)   (renommage C_cadb = C_acbd).

Donc c0 = -8 dans la convention T = -2/sqrt(g) dS/dg^ab, ce qui est la valeur utilisee en calibration ; |c0| = 8 est confirme. Les termes R^cd sigma C_acbd et ceux venant de delta sqrt(g), delta g^.. sont d'ordre 2 : correctement ecartes. La relation That_ab = Omega^2 T_ab (indices bas, ghat = Omega^-2 g) est correcte.

**Implementation.** Ligne 103 : up(c) up(d) d_c d_d (f C[(a, c, bb, d)]) : indices et contraction avec eta (diagonale) corrects. Variante : T est symetrique et eta-sans-trace hors couche (True), conformement aux symetries de Weyl.

**Conclusion E1 : conforme.** Aucune erreur trouvee.

## E2. Procedure formelle

**Substitutions.** subs_omega remplace d Omega par n, d d Omega par s eta, les derivees d'ordre >= 3 par 0, puis ln Omega par LOG ; reduce_nn elimine n0^2 par (3.8) a l'ordre zero. Test independant, variante v_E2_explicite.py (sortie v_E2_explicite_sortie.txt) : Omega **explicite** quadratique, Omega = 2 + k.x + (s/2) eta(x,x) avec s = 1/5 non nul (pour lequel d d Omega = s eta, d s = 0 et n.n = -lambda/3 + 2 Omega s sont exacts), champs E, B polynomiaux arbitraires de degre 3 (non a divergence nulle), (2.17) recalcule directement par une implementation propre (vrai logarithme, Christoffel de Omega^-2 eta recrit a la main). Comparaison exacte avec le second membre formel src du script en 2 points x 6 composantes : **12/12 egalites exactes**. La chaine subs_omega / jetify / reduce_nn / laurent_log est donc correcte, y compris les termes en s.

**Ordre retenu.** Les termes -Omega L_ab + (kappa/2) Omega T*_ab de (2.14), le terme (kappa/12) That de (3.8) et le terme en nablahat That de (2.15) ne sont ecartes que la ou ils multiplient W (ou F^2) : partout dans le calcul d d Omega et les derivees d'ordre superieur n'apparaissent qu'en facteur de W, et la trace de That est nulle a cet ordre (verifie). Ecart legitime au premier ordre en W. La substitution C = Omega W est bien celle de Friedrich (W = Omega^-1 C, Weyl de g, indices abaisses par g). Christoffel de ghat = Omega^-2 g : Gamma^a_bc = -(delta^a_b n_c + delta^a_c n_b - eta_bc n^a)/Omega, correct ; cov et R217 implementent bien Omega^-1 (nablahat_nu Lhat_lambda rho - nablahat_lambda Lhat_nu rho) ; la partie (lambda/6) ghat de Lhat est omise a juste titre (nablahat ghat = 0).

**Comparaisons au bon ordre.** v1 comparait le coefficient de Omega^-1 (deja extrait) a un candidat contenant n0^2 puis reduisait : la reduction n0^2 -> ... - 2 Omega s injectait des termes d'ordre Omega^0 dans une comparaison d'ordre Omega^-1, d'ou un ajustement vide. v2 forme src - cand/Omega (et That + c0 b Omega E^n), reduit l'expression entiere, puis extrait l'ordre : correct. En AF-2, le candidat est lineaire en n (pas de n0^2) : pas de melange possible.

**Reduction d'ordre.** Jets de W : 40, 100, 200 variables aux ordres 1, 2, 3 ; contraintes resolues 16, 58, 136 (systemes lineaires compatibles, solution retournee). Variante v_E2_analyse.py : les coefficients en ln Omega contiennent des jets jusqu'a l'ordre 3 (Omega^2 ln Omega) ; la resolution jusqu'a l'ordre 3 est donc **necessaire et suffisante** ; les 72 coefficients log non nuls hors couche s'annulent tous sur couche (re-verifie).

**Deux reserves de fond (hypotheses cachees).**
1. *La couche « div W = 0 » n'est pas l'equation (2.17).* Avec l'anomalie, (2.17) dit div W = R = O(kappa b), et R contient le pole. Les logs sont kappa b x Lin(D, dD, ddD) ; en reinjectant D = R ils deviennent d'ordre kappa^2 b^2, toujours **lineaires en W** (la troncature au premier ordre en W ne les elimine pas), et, par simple comptage de puissances (D ~ Omega^-1, Omega dD ~ Omega^-1), du type Omega^-1 ln Omega. Non calcule ici. L'enonce « tous les termes en ln Omega s'annulent quand div W = 0 » est exact comme identite, mais au sens de la definition meme de la note (jets traites comme inconnues independantes) le second membre **contient** 72 termes en ln Omega ; leur disparition est une propriete « a l'ordre b, modulo l'equation du vide », a dire comme telle.
2. *Le second membre contient des derivees de l'inconnue W.* Variante v_E2_derivees.py : apres reduction d'ordre complete, il reste 452 termes en jets d'ordre 1 a Omega^0 et 30 a Omega^1 ; par exemple, dans le repere n = (1,0,0,0), R(1,0,1) contient -(b c0 kappa / 2) d_0 E11 a Omega^0, alors que le membre de gauche est -d_0 E11 + d_3 B12 - d_2 B13. Le systeme couple n'est donc pas, litteralement, du type du theoreme 3.1 de Friedrich (second membre fonction des inconnues, sans derivees) : la partie principale est modifiee a l'ordre kappa b (facteur regulier 1 - kappa b c0/2 sur d_0 E, non degenere). Cela ne touche pas le pole (qui ne contient aucun jet, cf. E4), mais la phrase « enonces formels du type du theoreme 3.1 » (§3) suppose tacitement que ces termes derives sont absorbes dans la partie principale.

**Conclusion E2 : procedure correcte et validee independamment ; deux precisions de formulation requises (logs : « a l'ordre b, modulo div W = 0 » ; partie principale modifiee a l'ordre kappa b).**

## E3. Controles de sensibilite

**(a) sigma remplace par une fonction lisse.** Variante v_E3a.py (le script de reference, seule la ligne sigma = -ln Omega du bloc AF-1 remplacee ; sorties v_E3a_{omega,un,omega2}_sortie.txt) :

| f a la place de sigma | puissances (p, log) dans That | puissances (p, log) dans le second membre de (2.17) | pole | log |
|---|---|---|---|---|
| sigma = -ln Omega (reference) | (1,0) ... et logs | (-1,0), (0,1), (1,1), (2,1), ... | oui | oui (72) |
| Omega | (2,0), (3,0) | (0,0) ... (3,0) | non | non |
| 1 (terme de Bach local b C^2) | (2,0), (3,0) | (0,0), (1,0), (2,0) | non | non |
| Omega^2 | (3,0) | (1,0), (2,0), (3,0) | non | non |

Le pole et les logs viennent exclusivement du facteur sigma : la plus basse puissance de That passe de Omega^1 a Omega^2, ce qui decale R de Omega^-1 a Omega^0. Le controle (f = 1) est instructif : le terme local b C^2 seul (sans sigma) est formellement regulier, l'irregularite est donc bien propre a la partie de Wess-Zumino.

**(b) W sans symetries de Weyl.** Variante v_E3b.py, au niveau de la partie ln Omega de T (dont derive celle de (2.17)), apres resolution de D = 0 et dD = 0 (D_abc = d^d W_abcd) :
- mode « trace » (W + produit de Kulkarni-Nomizu eta o S, S symetrique ; symetries de Riemann conservees, trace non nulle) : 16/16 composantes du log non nulles sur couche ; residu exactement -LOG c0 b s eta^cd W_acbd (par exemple (0,0) : -b c0 s (3 S00 - S11 - S22 - S33)) ; **avec s = 0, le residu disparait**.
- mode « nopair » (36 fonctions, seulement antisymetrique en (ab) et (cd)) : 16/16 composantes non nulles ; residu exactement -LOG c0 b [s eta^cd W_acbd + n^d (d^c W_acbd - D_bda)], le second terme etant la divergence sur le 2e indice, qui ne se ramene a D que par symetrie de paires.

L'identite du ln est donc en defaut **seulement** par la trace (via s, i.e. d d Omega = s eta) ou par la symetrie de paires, conformement a l'identite hors couche du script. La cyclicite n'intervient pas dans l'identite (elle intervient seulement dans la parametrisation).

**(c) AF-2 sans sigma.** Variante v_E3c.py (bloc AF-2 du script, seule la ligne coup modifiee ; sorties v_E3c_{ref,beta0,omega}_sortie.txt) :
- ref (1/e2 - 4 beta_* sigma) : pole dans Maxwell, logs (0,1), (1,1) dans (2.17) (reproduit la reference) ;
- beta_* = 0 : second membre de Maxwell nul ; (2.17) : (0,0), (1,0) seulement ; ni pole ni log ;
- sigma -> Omega (1/e2 - 4 beta_* Omega) : Maxwell recoit -4 beta_* e2 (...) **sans** 1/Omega ; (2.17) : (0,0), (1,0), (2,0) ; ni pole ni log.

**Conclusion E3 : K-6 satisfait** ((a) et (c) sans pole ni log ; (b) defaut uniquement par trace ou symetrie de paires). Les controles montrent que le script n'est pas « aveugle » : il produit des poles et logs seulement en presence de sigma.

## E4. Le « seulement si »

**Non-nullite generique.** Variante v_E2_analyse.py : dans le repere n = (1,0,0,0) (lambda = 3, s = 0), les seules composantes non nulles du pole sont R(i,0,j) = -b c0 kappa E_ij / Omega (et R(3,0,3) = +b c0 kappa (E11 + E22)/Omega = -b c0 kappa E33/Omega). Le pole est donc non nul des que b c0 kappa != 0 et E^n != 0, et il ne contient aucun jet de W (ensemble des symboles : n, E, B, lambda, b, c0, kappa ; B disparait apres reduction dans le repere, et lambda n'entre que par la reduction de n.n). Pour des inconnues generiques, le coefficient est non nul : la direction « seulement si » est etablie **dans le choix d'inconnues de Friedrich** (W de poids 1).

**Changement de poids, C = Omega^p W_p.** Variante v_E4.py (sortie v_E4_sortie.txt) : l'equation pour W_p s'ecrit d.W_p = Omega^{1-p} R - (p-1) Omega^-1 n.W_p ; en recalculant R avec C = Omega^p W_p (les termes en derivees de W produisent aussi des contributions au pole quand p != 1), le coefficient total de Omega^-1 vaut, dans le repere de n :

  R(i,0,j) : -E_ij (3 b c0 kappa p^2 - b c0 kappa - 2 p + 2)/2 ;   R(k,i,j) spatiaux : (p - 1) x B (par exemple B11 (p - 1)).

- b = 0 : seul p = 1 est regulier (controle : c'est la raison du poids de Friedrich).
- b != 0, E et B generiques : **aucun p** n'annule le pole (sympy : []).
- b != 0, W purement electrique relativement a n (B = 0) : p = [1 +- sqrt(1 - 6x + 3x^2)]/(3x), x = b c0 kappa, dont la racine p = 1 + b c0 kappa + O(b^2) retire le pole electrique. Mais avec ce p, le canal magnetique recoit le pole (p - 1) B = b c0 kappa B/Omega. Interpretation (non au-dela du calcul) : la partie electrique porte une dimension anomale Omega^{b c0 kappa}, que l'on peut absorber dans le poids, mais pas uniformement avec la partie magnetique ; le pole est deplace, pas supprime.

**Redefinition W' = W + f(Omega) X.** Pour f lisse, d.(f X) = f' n.X + f d.X ne contient pas de Omega^-1 : le pole est inchange (si f(0) != 0 et X = W, il est seulement renormalise). Pour annuler le pole, il faut f singulier : v_E4.py trouve qu'avec f = ln Omega, le choix X = -b c0 kappa x (partie electrique de W relative a n, B_X = 0) annule exactement le pole (solution unique), mais introduit ln Omega d.X_el, non nul sur div W = 0 (18 composantes sur 24, par exemple -d_0 E11). On echange alors le pole contre un log, et W' = W + ln Omega X n'est plus lisse quand W l'est : le contenu (la classe de regularite des inconnues) change.

**Conclusion E4.** Le « seulement si » est etabli pour le choix d'inconnues de Friedrich et resiste, dans ce qui a ete calcule, aux changements de poids constants et aux redefinitions lisses. Il n'est pas etabli pour des changements d'inconnues dependant de b (poids anomal) au-dela de ce calcul : la note devrait preciser « pour le choix d'inconnues de Friedrich (W de poids 1) » ; l'existence d'un poids anomal pour la partie electrique est un fait nouveau a signaler, compatible avec E6 (comportement en puissance sur solution).

## E5. AF-2 (sigma F^2)

**Variation a sigma fixe.** S = -(1/(4 e^2)) Int sqrt(g) F^2 + beta_* Int sqrt(g) sigma F^2 = -(1/4) Int sqrt(g) (1/e^2 - 4 beta_* sigma) F^2. Avec T_ab = -2/sqrt(g) dS/dg^ab et d(sqrt(g) F^2)/dg^ab = sqrt(g)(2 F_ac F_b^c - (1/2) g_ab F^2), on obtient T_ab = (1/e^2 - 4 beta_* sigma) M_ab, M_ab = F_ac F_b^c - (1/4) g_ab F^2, puis That_ab = (1/e^2 + 4 beta_* ln Omega) Omega^2 M_ab[F ; eta] (F de poids 0, ghat^cd = Omega^2 eta^cd). C'est bien ce que code le script (lignes 237 a 251). La forme de Wess-Zumino a sigma fixe est la forme locale standard ; elle donne un T sans trace, la trace anomale beta_* F^2 n'apparaissant que par la dependance de sigma en la metrique.

**Equation de Maxwell : erreur de signe dans la note.** d^a[(1/e^2 + 4 beta_* ln Omega) F_ab] = 0 donne d^a F_ab = **-** 4 e^2 beta_* n^a F_ab / Omega + O(beta_*^2). Variante v_E5_signe_maxwell.py : le second membre imprime par le script est egal a -4 e2 beta_* n^a F_ab/Omega (True) et non a +4 e2 beta_* n^a F_ab/Omega (False). La sortie du script est juste ; la transcription de la note (§VERDICT, §2, tableau §3) a le mauvais signe (ou il faut ecrire n^a F_ba). Le critere K-4 de la consigne AA-1 porte la meme coquille. Sans effet sur l'existence du pole.

**Completion de S2 (Omega[g] fonctionnelle de la metrique).** Si sigma depend de la metrique, il s'ajoute a T un terme beta_* F^2 dsigma/dg^ab : le facteur dsigma/dg est geometrique (independant de F) et ne porte pas de ln Omega ; au premier ordre il ne peut se construire que sur eta, n (le Weyl donnerait un produit d'ordre 2). Variante v_E5.py : ajout a That de Omega^2 [a1 eta + a2 n n] beta_* F^2 (sans log), et meme, par exces de prudence, de Omega^2 ln Omega [(a3 eta + a4 n n) F^2 + a5 eta F.Ftilde], avec Lhat = (kappa/2)(That - (1/3) ghat tr That) :
- les composantes hors diagonale (i,0,j), i != j, restent -6 kappa beta_* (E_iE_j + B_iB_j), **independantes de a1 ... a5** ;
- les differences diagonales R(1,0,1) - R(2,0,2) = -6 kappa beta_* (Bx^2 - By^2 + Ex^2 - Ey^2), etc., sont independantes de a1 ... a5 ;
- seules les traces et des parties du type (E^2, B^2, E.B) sont deplacees.
Donc (E_iE_j + B_iB_j)_tf = 0 reste impose : une partie isotrope (ou construite sur n) ne peut pas modifier la conclusion formelle. Reserve : un dsigma/dg non local dependant de F n'est pas couvert (il n'existe pas dans le cadre ou sigma est geometrique).

**Argument de rang.** S = EE^T + BB^T est semi-defini positif de rang <= 2. S_tf = 0 donne S = (tr S / 3) I ; si tr S = |E|^2 + |B|^2 > 0, S serait de rang 3 : contradiction. Donc tr S = 0, E = B = 0. L'argument est juste et n'utilise meme pas la condition de Poynting. Remarque d'execution : dans le script il est imprime comme texte (ligne 304) et la variable real_sols (ligne 302) est calculee mais jamais imprimee ; la conclusion « champs reels => E = B = 0 » repose donc sur l'argument, non sur une sortie. Les solutions complexes listees (B = +- i E, composante par composante) sont coherentes avec la condition (EE + BB)_tf = 0 et E x B = 0.

**Calibration AF-3 (ii)** : -kappa beta~ B0^2/e^2, idem, +2 kappa beta~ B0^2/e^2 reproduits (sortie_copie.txt) : conforme a K-5 (b).

**Conclusion E5 : conforme, une correction de signe (equation de Maxwell) ; conclusion formelle robuste a une completion isotrope ou construite sur (eta, n).**

## E6. Surdits

Phrases de la note non soutenues (ou soutenues seulement en partie) par la sortie du script ou un calcul :

1. **« d^a F_ab = 4 e^2 beta_* n^a F_ab / Omega »** (VERDICT, §2, tableau) : signe faux, cf. E5. A corriger en -4 e^2 beta_* n^a F_ab / Omega.
2. **« concorde avec That_ij = -+ 8 b Omega W_sisj, NOTE-128 »** : aucune comparaison dans le script ; le signe « -+ » n'est pas fixe. Accord de forme seulement (coefficient 8 = |c0|, verifie en E1).
3. **Calibration NOTE-125 (« valeur exacte de NOTE-125 »)** : le script code en dur e = -B k^3 cos kx / 2 et la cible -4 b kappa B k^3 cos kx, et verifie 8 x (-1/2) = -4 avec c0 = -8. C'est un controle de coherence arithmetique entre une valeur formelle et deux nombres importes, non une derivation independante ; il suppose en outre que le repere de NOTE-125 a n = (1,0,0,0), lambda = 3, s = 0. Le resultat formel 8 b kappa e / Omega (K-5 a) est, lui, bien produit.
4. **« Dans le vide, apres reduction d'ordre (NOTE-133), il n'y a pas de log a l'ordre b »** : vrai a l'ordre b sur la couche div W = 0 (verifie) ; mais l'equation est div W = R, et l'iteration donne des logs d'ordre kappa^2 b^2 lineaires en W, du type Omega^-1 ln Omega par comptage (non calcule), cf. E2.
5. **« il reste ln Omega x Lin(J), d'ordre kappa^2 b (concorde avec S-b, NOTE-128) »** : la structure Lin(J) suit de l'identite hors couche (verifiee) ; l'ordre kappa^2 b et la concordance avec NOTE-128 ne sont pas calcules (la sortie imprime seulement qu'un coefficient log est non nul hors couche).
6. **« Sur solution, le pole formel produit la divergence en ln de W (NOTE-133) »** : non calcule dans le script. Calcul AA-2 (composantes du pole et membre de gauche, v_E2_analyse_sortie.txt) : pour un mode homogene purement electrique dans le repere n = (1,0,0,0), (2.17) se reduit a -d_0 E_ij = -b c0 kappa E_ij / Omega + O(Omega^0), d'ou E_ij = E0_ij Omega^{b c0 kappa} = E0_ij (1 + b c0 kappa ln Omega + O(b^2)) ; les composantes de contrainte et l'equation de B sont compatibles (pole nul, B constant). La phrase est donc **juste au premier ordre en b**, mais la resommation donne une loi de puissance (exposant -8 b kappa pour c0 = -8, divergente si b kappa > 0), coherente avec le poids anomal trouve en E4 (p = 1 + b c0 kappa). La note doit dire « au premier ordre en b ».
7. **« La reserve G-CAL-a est levee »** : levee au sens « le pole est un terme du second membre comme fonction des inconnues », oui. Mais (i) le second membre contient des derivees de W (E2, reserve 2), ce qui sort litteralement du cadre du theoreme 3.1 ; (ii) le « seulement si » vaut pour le choix d'inconnues de Friedrich (E4). A formuler avec ces deux bornes.
8. **« regulier ssi ... (ou E^n = 0 au bord) », « (ou F = 0 au bord) »** (VERDICT, tableau, §3) : ces alternatives sont des enonces **sur solution** (valeur des inconnues a scri), pas des enonces formels ; au sens de la definition de la note, le second membre comme fonction des inconnues contient le pole des que b != 0 (resp. beta_* != 0). Melange formel / sur solution, precisement la distinction que la note revendique. Meme reserve pour « aucun champ electromagnetique non nul a scri » (§3), qui est une consequence sur solution, a dire comme telle.
9. **Comparaison NOTE-113/114** : « la condition formelle est plus forte » est exact pour des champs reels (E = B = 0 implique (BB - EE)_tf = 0). L'explication (« F recoit, par le pole de Maxwell, des corrections en ln qui peuvent compenser ») n'est pas calculee.
10. **« dans CCC + M a M2 = 2, la masse physique y Omega H_r tend vers 0 ... cadre C-M1 »** : importe, non calcule.
11. Details d'execution du script (sans effet sur les resultats) : ligne 116 imprime l'enonce « the ln Omega part of T is sigma x Lin(D, dD) » sans test (il est soutenu par l'identite testee ligne 113 et par la trace nulle (0)) ; ligne 205 annonce « div W = 0 (and its first derivatives) » alors que les derivees secondes sont aussi utilisees ; real_sols non imprime (E5).

Points de la note **soutenus** par la sortie (reproduite a l'identique) et par les variantes : genericite du Weyl, identite hors couche, trace nulle de That, That = -c0 b Omega E^n + O(Omega^2), plus basse puissance Omega^-1 sans Omega^-2, coefficient du pole exact sur 24 composantes et sans jets, 72 logs aux ordres (0,1), (1,1), (2,1) nuls sur couche (jets 1 a 3 : 16, 58, 136), K-5 (a) et (b), coefficients gam = 6, gam2 = 2, conditions (EE + BB)_tf et Poynting.

## Verdict

**CONFIRME AVEC CORRECTIONS.**

Criteres : K-1 satisfait (E1, E3 b) ; K-2 satisfait (pole -kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho), sans jets) ; K-3 satisfait (logs nuls sur D = dD = ddD = 0) ; K-4 satisfait au signe pres de l'equation de Maxwell (d^a F_ab = -4 e^2 beta_* n^a F_ab / Omega ; la coquille est aussi dans l'enonce de K-4) et pour la partie (2.17) (6, 2 ; E = B = 0 pour des champs reels) ; K-5 (a) et (b) satisfaits ; K-6 satisfait (E3).

Corrections demandees avant entee :
1. Signe de l'equation de Maxwell rescalee (VERDICT, §2, tableau §3).
2. Logs de G-V3 : « nuls a l'ordre b sur la couche div W = 0 » ; signaler que la reinjection de div W = R donne des termes d'ordre kappa^2 b^2 lineaires en W (non calcules).
3. Mentionner que le second membre contient des derivees de W (partie principale modifiee a l'ordre kappa b) : « du type du theoreme 3.1 » a nuancer.
4. « Seulement si » : preciser « pour le choix d'inconnues de Friedrich (W de poids 1) » ; signaler qu'un poids anomal p = 1 + b c0 kappa retire le pole electrique mais le transfere au canal magnetique (aucun poids ne le retire pour W generique), et qu'une redefinition en ln Omega l'echange contre un log.
5. Retirer des enonces formels les alternatives « ou E^n = 0 / F = 0 au bord » (ce sont des enonces sur solution).
6. Requalifier comme non calcules ou importes les rapprochements NOTE-128 (That et S-b), NOTE-125 (calibration = controle arithmetique d'entrees importees), NOTE-133 (vrai au premier ordre en b, loi de puissance a la resommation), NOTE-113 (mecanisme de compensation) et C-M1.

Aucune de ces corrections ne renverse le resultat central : au premier ordre autour de eta, avec les inconnues de Friedrich, la partie c de Wess-Zumino met dans (2.17) un pole Omega^-1 de coefficient -kappa c0 b n_[nu E^n_lambda]rho (x2), absent pour b = 0 ; sigma F^2 met un pole dans l'equation de Maxwell et du ln Omega dans (2.17), dont l'annulation impose E = B = 0 pour des champs reels.

Fichiers joints (work_aa2) : af_check_copie.py, sortie_copie.txt, temps_copie.txt ; v_E1_weyl.py, v_E1_variation.py ; v_E2_explicite.py, v_E2_analyse.py, v_E2_derivees.py ; v_E3a.py (modes omega, un, omega2), v_E3b.py (modes trace, nopair), v_E3c.py (modes ref, beta0, omega) ; v_E4.py ; v_E5.py, v_E5_signe_maxwell.py ; chacun avec son fichier *_sortie.txt.
