# Rapport RB-2 : audit adverse de RJ2 (NOTE-216 gel, NOTE-217 execution)

Auditeur isole, consigne PROMPT-AVEUGLE-RB2.md. Date : 2026-10-16.

## 0. Perimetre et methode

**Fichiers lus** : NOTE-BORD-EON-216-ARMEMENT-RJ2.md, NOTE-BORD-EON-217-RJ2-EXECUTION.md (copies de auditrj2/ identiques a celles de RJ2/), NOTE-207-v2-RJ.md, friedrich2016.txt (§3 eq. (3.1) a (3.23), Lemme 4.1, (4.16) a (4.20)), rj2_lemmes.py, rj2_series.py, rj2_ops.py, rj2_ops_check.py, rj2_lin_check.py, rj2_test.py, precheck/eq33_check.py et toutes les sorties (rj2_*_sortie.txt, run_*.txt, eq33_check_sortie.txt). **Aucun autre fichier** de /home/claude n'a ete ouvert (ni le registre, ni les sceaux, ni NOTE-218, ni PROMPT-RB1, ni work_rb1).

**Travail dans work_rb2/** (originaux non modifies) :
- `rb2_quick.py` (sortie `rb2_quick_sortie.txt`) : inverse du co-repere dans `dirac_op` ; structure des secteurs q = +-2k.
- `rb2_cspin.py` (sortie `rb2_cspin_sortie.txt`) : les controles de `dirac_lin` detectent-ils un coefficient de spin faux ?
- `rb2_test.py` : copie de rj2_test.py (lignes 1 a 189, NU et NG parametrables) augmentee de controles positifs (PC1, PC1b, PC1c, PC2) et du calcul de la courbure de la metrique conforme (R, Schouten L, Weyl rescale W = C/Omega) sur la solution d'ordre epsilon^2. Sorties : `rb2_smoke.txt` (NU = 5, NG = 3) et `rb2_full_gen_1310.txt` (NU = 9, NG = 6, mu = 13/10, generique).
- Reexecution des scripts originaux (copies) : `re_lemmes.txt`, `re_ops_check.txt`, `re_lin_check.txt`, `re_eq33.txt`.

**Reproduction** : la partie geometrique de `rb2_full_gen_1310.txt` (lignes 4 a 89) est identique octet pour octet a `run_gen_1310.txt` ; `run_gen_73.txt` ne differe de `run_gen_1310.txt` que par la valeur de mu et les durees. Les reexecutions des lemmes, des controles d'operateurs et du precheck sont commentees en §7.

## 1. Synthese

| # | Classe | Objet | Ou |
|---|---|---|---|
| E1 | erreur | « la geometrie a une limite a scri, oscillations a partir de l'ordre 1 » : faux dans la jauge meme du test ; le Schouten L_00 et le scalaire R de la metrique conforme oscillent a l'ordre 0 | NOTE-217 l.43, l.69, l.75 ; gel l.36 |
| E2 | erreur (sans incidence) | co-repere inverse faux dans `dirac_op` quand h_0i est non nul | rj2_ops.py l.98 |
| E3 | erreur (mineure) | « H_ij TT ordre min 3 (particulier) » : Omega^3 est un exposant homogene, pas une reponse particuliere | NOTE-217 l.57 |
| C1 | correction | verdict global RJ2-V1 surclasse : formel conditionnel a H2 non demontree, clause generique contredite par E1 | NOTE-217 l.71 |
| C2 | correction | H2 presentee comme « le cas formel de la situation de Friedrich » : la jauge de Friedrich est differente et H1/H2 ne fixent pas la jauge conforme | NOTE-217 l.33 |
| C3 | correction | Psi(0) = 0 attribue a (3.3), qui ne contraint que g^{00} | NOTE-217 l.55, l.65 |
| C4 | correction | ecarts au gel : reponse spinorielle epsilon^3 non construite ; equations redondantes non controlees separement | gel l.31 ; NOTE-217 l.46, l.54 |
| C5 | correction | point faible du gel (jauge e_0 // grad Omega vs jauge du test) non discute | gel l.41 ; NOTE-217 l.46 |
| C6 | correction | robustesse surestimee : deux mu equivalents par structure, configuration de k speciale, secteurs +-2k sans oscillation | NOTE-217 l.50, l.70 |
| C7 | correction | « geometrie continue mais pas C^1 » : vrai pour W seulement | NOTE-217 l.43, l.75 |
| C8 | correction | « aucune relation regularisante n'est necessaire » : etabli pour les seconds membres de matiere, pas pour la partie geometrique (incluse dans H2) | NOTE-217 l.30 |
| C9 | correction | texte propose pour la Rem. 2(4) a restreindre | NOTE-217 l.76 |
| R1 a R10 | remarques | controles d'operateurs solides, detecteurs vivants (controles positifs), etapes 1, 2, 4 justes, etc. | §7 |

Verdict de l'auditeur : **le passage a RJ2-V1 global n'est pas justifie tel qu'ecrit.** La partie « classe a un seul exposant preservee, sans pole ni logarithme » tient (formel sous H1 + H2, et test epsilon^3, detecteurs verifies). La clause « classe generique : geometrie avec limite, oscillations a partir de l'ordre 1 » depend de la jauge conforme et est fausse dans la jauge du test pour L et R. Formulation proposee en §6.

## 2. A1 : conformite au gel

**Questions.** RJ2-1 traitee completement. RJ2-2 traitee sous deux hypotheses (H1, H2) que le gel n'avait pas annoncees : le gel demandait (l.30) si K est stable « dans une jauge ou e_0 est parallele a nabla Omega », il ne prevoyait pas une hypothese de resolubilite non demontree. C'est honnetement declare (NOTE-217 l.33, l.77) mais le verdict global (l.71) ne reporte pas la condition (voir C1). RJ2-3 : le gel (l.31) demande la « reponse du spineur d'ordre epsilon^3 » ; seule la source F et le critere de resonance a n = 0 sont calcules (rj2_test.py l.231 a 242), psi_3 n'est pas construit. C'est suffisant pour l'absence de logarithme a cet ordre (la recurrence de Fuchs n'est singuliere qu'a n = 0), mais c'est un ecart de formulation (C4). Le gel demandait aussi les equations redondantes « satisfaites ordre par ordre » : elles sont imposees conjointement (rj2_test.py l.133 a 151), et une incompatibilite serait annoncee « resonance ou violation de contrainte » (l.153) sans distinction (C4). Le gel demandait « deux modes » ; quatre modes (+-k1, +-k2) sont utilises, justifies par la contrainte d'impulsion du secteur q = 0 : acceptable.

**FW-3.** Le critere est applique correctement aux potentiels metriques. Mais il n'est jamais applique aux inconnues de Friedrich (W, L, s, connexion) dans le test, alors que la conclusion (l.43) porte sur « la geometrie ». Applique a L dans la jauge du test, il donne « bornee sans limite » (E1).

**FW-1.** (3.3) recopiee et verifiee (precheck, residu 0, et de Sitter |grad Omega|^2 = -lambda/3) ; j'ai relu (3.3) et (3.8) dans friedrich2016.txt : 6 Omega s - 3 nabla Omega . nabla Omega - lambda = -(1/4) T-hat, T-hat = g-hat^{mu nu} T-hat_{mu nu} : conforme a la note. L'Einstein linearise et l'operateur de Dirac perturbe sont bien derives depuis la metrique (rj2_ops.py). En revanche, H2 invoque « la situation de Friedrich pour la poussiere » sans recopier ni verifier ce qu'est cette situation (jauge comobile e_0 = U, R prescrit, geodesiques conformes, (4.16), seconde regularisation de §5) ; c'est une affirmation sur Friedrich au-dela de (3.3), non controlee, et inexacte (C2).

**FW-2.** Conventions verifiees dans les sorties : Clifford {g^a, g^b} = -2 eta^{ab} ok ; signe du tenseur lu (T_00 = -m avec sgn = +1, d'ou sgn = -1) ; coefficient de spin -1/4 obtenu par nabla gamma = 0 ; SGN et CSPIN recopies a la main dans rj2_ops.py l.57, 58, coherents avec rj2_lemmes_sortie.txt. Constance de mu : par calcul ecrit (etape 1), juste (R8), non scriptee ; le test donne Phi(0) = 0, coherent.

**FW-4, FW-5.** Respectes dans la note (§0, §5 « ce qui n'est pas fait », §7).

## 3. A2 : scripts

**Verifie juste (lecture et calcul) :**
- Serie de Dirac (rj2_test.py l.30 a 38) : de i gamma^a d_a u - (m/Omega) u = 0, Omega = -eta, on obtient du/dOmega = i(beta mu/Omega + alpha.k) u, et la recurrence ((n + i j mu) - i mu beta) u_n = i alpha.k u_{n-1} est exacte ; j = +1 dans beta = +1 (exposant +i mu). Controle l.42 a 46 correct.
- Conversion eta -> Omega : d/deta = -d/dOmega (l.50, l.115, l.220, l.227), coefficients subs(eta, -Om) (l.116) : correct.
- Secteurs de Fourier et conjugaison (l.53 a 66) : sector q = k_m - k_mp, le h.c. du secteur q est le conjugue du secteur -q (conjS change j en -j, Omega reel, mu reel) : correct.
- Tenseur : physique coordonne = Omega^2 T_c (e_a = Omega d_a) ; source `Tc.shift(2)` avec kappa = 1, G + Lambda g = T : correct.
- Operateur de Dirac perturbe (dirac_lin) : delta e_a^mu = -(1/2) h^mu_a, delta omega = d(delta e) + delta Gamma sur fond plat, masse non perturbee car Omega est fixe : correct. Equation epsilon^3 : du/dOmega - i(alpha.k' + beta mu/Omega) u = -i g0 delta D u_1, signe verifie a la main.
- Critere de resonance (l.236 a 239) : a n = 0, l'operateur (i rho - i mu beta) est singulier exactement pour rho = j mu sur le projecteur (1 + j beta)/2 : correct.
- Jauge longitudinale (l.141 a 149) : q.S = 0, H q = 0, tr H = 0 ; secteur q = 0 : Psi_0 = 0 fixe completement le temps (Omega = 1/a), S = 0 force par la contrainte d'impulsion, dont la donnee T_c,0a(q=0) = 0 est verifiee a tous les ordres (sortie « ['0','0','0'] »).
- Troncature : equations retenues pour n <= NG = 6, inconnues jusqu'a 9, lhs valide jusqu'a 7 ; les parametres libres au-dela de NG sont des artefacts, correctement identifies.

**Erreur E2 (rj2_ops.py l.98).** `Ed=sp.eye(4)+eps*(h*eta)/2` avec `Ed[a,mu] = e^a_mu`. Or e^a_mu = delta + (1/2) eta^{a rho} h_{rho mu}, soit `eta*h` et non `h*eta` (transposee). Verification (rb2_quick_sortie.txt) : E*Ed - Id = epsilon x [[0, h01, h02, h03], [-h01, 0, 0, 0], ...], non nul des que h_0i est non nul ; avec `eta*h` l'identite est exacte. **Sans incidence** sur les resultats : `dirac_op` n'est pas utilise par le test, et au premier ordre sur fond plat Ed multiplie la connexion de fond (nulle). Mais aucun controle ne la voit : la covariance conforme (rj2_ops_check.py l.19 ; rj2_lin_check.py) utilise h = 2 phi eta diagonal, la comparaison de degre 1 (rj2_lin_check.py l.76 a 81) est au premier ordre. Le commentaire l.98 (« h_mu^a ») a les indices transposes. A corriger avant tout usage de `dirac_op` au second ordre ou sur fond courbe.

**Controles annonces : testent-ils ce qu'ils pretendent ?**
- Identite de diffeomorphisme pour `dirac_lin` (rj2_lin_check.py (2)) : **plus forte qu'annonce**. Au point, tout 1-jet (h, dh) d'un tenseur symetrique est de jauge pure (dh <-> Gamma lineaire est bijectif, 40 = 40), et delta D ne depend que de (h, dh) : l'identite avec xi et chi generiques determine entierement l'operateur lineaire. Reserve : la loi attendue (signe -1, cK = -1/4, c2 = 0) a ete ajustee sur `dirac_op` (rj2_ops_check.py l.43 a 50), ce qui pouvait etre circulaire. J'ai leve le doute (rb2_cspin_sortie.txt) : avec CSPIN = +1/4, -1/2 ou 0, aucun (signe, cK, c2) ne satisfait l'identite. Le controle n'est pas aveugle a une erreur de connexion de spin.
- Invariance de jauge de l'Einstein linearise : teste l'operateur sur les h de jauge pure seulement ; il ne teste pas la normalisation de la partie physique. Celle-ci est controlee indirectement par la compatibilite des dix equations (conservation de T_c dans chaque secteur), ce qui est un bon controle collectif des bilineaires (R7).
- « Controle RJ reproduit » (l.75, 76) : ne porte que sur la composante 00 du secteur q = 0 ; les autres composantes et les secteurs q non nul ne sont controles que par la compatibilite d'Einstein.
- **Aucun controle positif** dans l'execution : la source F commence a Omega^0 dans les 36 couples, donc le detecteur de resonance n'a jamais ete expose a un terme Omega^{-1}, et aucun systeme n'a ete incompatible. Un detecteur mort aurait donne la meme sortie. J'ai fait les controles positifs (rb2_full_gen_1310.txt l.94 a 105 et fin) :
  - PC1 : Phi(0) = 1/10 injecte dans le secteur q = (2,0,0) -> F commence a Omega^{-1}, resonances (-1, +1) et (-1, -1) detectees pour les 4 modes. **Le detecteur est vivant.**
  - PC1b : H_23(0) = 1 (onde TT a scri) -> F commence a Omega^0, pas de resonance (attendu : seul d_eta porte 1/Omega, et H est spatial).
  - PC1c : S_2(0) = 1 (shift a scri) -> F commence a Omega^{-1} mais projection resonante nulle.
  - PC2 : source TT conservee T_c,23 += Omega^{-1} (Omega^1 dans l'equation, exposant indiciel 3) -> « INCOMPATIBLE » ; T_c,23 += Omega^0 (non resonante) -> compatible. **Le detecteur geometrique distingue bien une resonance.**

**Secteur homogene, secteurs +-2k.** Les secteurs q = +-2k1, +-2k2 ne contiennent structurellement que j = 0 (rb2_quick : identique avec deux jeux de donnees aleatoires) : dans le cas generique, les oscillations ne portent que sur q = +-(k1 - k2), +-(k1 + k2) et q = 0 (C6).

## 4. A3 : le test detecte-t-il vraiment les resonances ?

1. **A l'ordre epsilon^3**, le critere « terme Omega^{-1 + i j mu}, j = +-1, projete sur beta = j » est necessaire et suffisant : la recurrence ((n + i rho) - i mu beta) c_n = i alpha.k' c_{n-1} + F_{n-1} n'est singuliere que pour n = 0 et rho = +-mu. Le terme alpha.k' ne cree pas de resonance (il descend d'un ordre). Les termes j = +-3 sont non resonants. La verification est faite couple par couple (q, mode) et non sur la source totale de chaque k' ; c'est sans consequence ici (somme de termes non resonants), mais a noter si un jour une resonance apparait (des compensations entre couples seraient alors possibles).
2. **Le test est faiblement discriminant tel quel** : F commence a Omega^0 partout, le critere n'est jamais sollicite. La seule voie de resonance est un h d'ordre 0 portant d_eta (Phi(0), et a un degre moindre le shift S(0)), comme le montrent PC1 et PC1c. L'absence de resonance a epsilon^3 se ramene donc a « Phi(0) = 0 et S(0) = 0 » dans la solution d'ordre epsilon^2, ce que la note dit bien (l.65).
3. **Ordres superieurs (epsilon^4 geometrie, epsilon^5 spineur)** : non testes. Canaux possibles : (i) lapse Phi_4(0) non nul : exclu par (3.3) tant que s reste borne (identite valable a tout ordre) ; (ii) shift S_4(0) : PC1c suggere une projection resonante nulle, non demontre en general ; (iii) termes quadratiques en h_2 avec donnees TT libres H(0) non nulles (ondes gravitationnelles a scri) : delta^2 D[H(0), H(0)] ne contient pas de 1/Omega si g^{00}(0) = -1 et S(0) = 0, mais l'equation geometrique d'ordre epsilon^4 contient des sources quadratiques (H(0) x H_3, etc.) qui pourraient frapper les exposants indiciels 0 et 3 : pour la gravitation pure, la regularite de scri (Friedrich, vide) le garantit, pour le couplage croise avec psi_1 psi_3 il faut que T_c,ij n'ait pas de terme j = 0 en Omega^{-1}. Ceci est vrai en composantes covariantes (la partie singuliere est (m/Omega) psibar psi n_mu n_nu/|n|^2, n_mu = d_mu Omega n'a qu'une composante temporelle), mais seulement a l'ordre dominant en h. Conclusion : l'enonce « pas de logarithme » est etabli a epsilon^3 ; au-dela, il repose sur l'argument formel (donc sur H2).
4. **Compatibilite et logarithmes geometriques** : a epsilon^2, les exposants indiciels j = 0 du systeme lineaire (0 et 3 pour TT et cisaillement) sont dans la fenetre n <= 6, et PC2 montre qu'une source resonante produit une incompatibilite. Les systemes compatibles prouvent donc l'absence de logarithme a epsilon^2 jusqu'a l'ordre 6, pour ces donnees. Pour j non nul, aucune resonance n'est possible quel que soit mu reel non nul (parties reelles entieres), ce qui rend le second choix de mu (7/3) sans valeur probante supplementaire (C6).
5. **Mais l'absence de logarithme n'est pas la regularite** : voir E1, la compatibilite ne dit rien de l'ordre auquel les oscillations entrent dans les inconnues de Friedrich.

## 5. A4 : l'argument formel (§2)

**H1** (l.33) : la possibilite d'une jauge (Omega, x), e_0 // grad Omega, est correcte (grad Omega de genre temps pres de scri par (3.3), signe -lambda/3 < 0 en signature (-,+,+,+)). **Mais H1 ne fixe pas la jauge conforme** (le choix de Omega dans sa classe Omega -> theta Omega), alors que Friedrich la fixe (R prescrit, puis facteur conforme le long des geodesiques conformes, d'ou (4.16) ; friedrich2016, p. 10 et §4). Le test, lui, fixe Omega = 1/a(eta) avec eta le temps de la jauge longitudinale : c'est une jauge H1 au premier ordre (coordonnee Omega = -eta, e_0 // grad Omega a O(S) = O(Omega^2) pres) avec un choix conforme particulier.

**H2** (l.33) : « c'est le cas formel de la situation de Friedrich pour la poussiere » est inexact (C2) : Friedrich travaille avec e_0 = U, des coordonnees comobiles et une jauge conforme de type Gauss conforme ; Omega n'y est pas une coordonnee. Il a de plus besoin, en §5, d'une seconde regularisation (zeta_ab) pour obtenir un systeme hyperbolique. H2 est donc une hypothese nouvelle, pas une transposition.

**Etape 1** (l.38) : juste, signes de Friedrich verifies : de (3.3), |grad Omega|^2 = -lambda/3 + 2 Omega s + T-hat/12, et T-hat = g-hat^{mu nu} T-hat_{mu nu} = Omega^3 tr tau (tau dans le repere orthonorme physique) ; donc |n| = nu + O(Omega) des que s est sans puissance negative, ce qui est une hypothese de l'ansatz K (coherence formelle, pas exclusion des poles). En coordonnees (Omega, x), la constance de mu est exactement ce qui interdit le ln Omega issu de d_x Omega^{i mu(x)} : argument correct.

**Etape 2** (l.39) : juste. Les valeurs propres n + i(rho -+ mu) ne s'annulent pas pour n >= 1 ; les corrections portent un facteur Omega pourvu que la connexion soit bornee, ce qui est vrai en H1 (nabla e_0 s'exprime par nabla nabla Omega / |n|, regulier par (3.4)).

**Etape 3** (l.40) : la partie « S/Omega = S(R) bornee » est juste (noyau P1 verifie pour n generique). La partie « G_{n+1} est obtenu en divisant par (n + 1 + 2 i j mu) » suppose que **toutes** les inconnues geometriques obeissent a une equation d'evolution en Omega. C'est faux pour les composantes fixees par la jauge : en H1, L_00 n'a pas d'equation d'evolution par (3.6) ; il est donne par (3.5) (nabla^eta Omega L_{eta mu} = -nabla_mu s + ...), donc par d_Omega s, et perd un ordre. Comme s oscille a l'ordre 1, L_00 oscille a l'ordre 0. **Le calcul le confirme** (E1). Le parenthetique « (W, et les variables qui s'en deduisent par integration) » est juste pour W et la metrique, mais la conclusion (l.43) generalise a « la geometrie ».

**« Pas de relation regularisante necessaire »** (l.30) : etabli pour le terme singulier de matiere (S/Omega, P1 verifie pour n de genre temps quelconque, rj2_lemmes_sortie.txt). La comparaison avec Friedrich (« l'alignement ... doit etre impose par une jauge ») est approximative : chez Friedrich, (4.16) resulte du Lemme 4.1 (dynamique : geodesiques du flot = geodesiques conformes) combine a la jauge conforme ; il ne s'agit pas seulement d'une jauge. Et l'eventuelle necessite d'une regularisation de la partie geometrique en jauge H1 est contenue dans H2 (C8).

**Etape 4** (l.41) : juste (le produit geometrie j = 0 x spineur rho = mu reste en rho = mu ; les bilineaires d'un seul exposant sont en j = 0).

## 6. A5 : verdict et portee

**E1 en detail (rb2_full_gen_1310.txt l.106 a 131).** Pour g_c = eta + h en jauge longitudinale, la linearisation donne (verifie par sympy) :
- R[g_c] = 2 q^2 Phi - 4 q^2 Psi - 6 Psi'' ;
- L_00 = Psi'' - (q^2/3)(Phi + Psi).

Psi contient Omega^{2 +- 2 i mu} (sorties originales, l.55 du tableau : oscillants a partir de l'ordre 2), donc Psi'' contient Omega^{+-2 i mu} a l'ordre 0. Resultat dans les quatre secteurs oscillants : « R[g_c] : osc min 0 ; L00 : osc min 0 » ; L_0i a partir de 1, L_ij a partir de 2 ; W electrique oscillant a partir de 1, magnetique a partir de 2 (ceci confirme la note pour W). Au premier ordre, L(e_0, e_0) = L_00 en coordonnees (le fond conforme est plat), donc l'effet n'est pas un artefact de repere. Dans la jauge du test, qui satisfait H1, une inconnue du systeme de Friedrich (L, liste (3.23)) est donc **bornee sans limite** au sens de FW-3, et la geometrie generique n'a pas de limite a scri. Un autre choix de jauge conforme (theta contenant Omega^{2 +- 2 i mu}, par exemple R prescrit comme chez Friedrich) peut vraisemblablement faire disparaitre l'oscillation d'ordre 0 de L_00, mais ce n'est ni fait ni enonce.

**Consequence pour le verdict.** Le gel distingue V1 (« geometrie avec limite, oscillations d'ordre >= 1 ») et V2 (« geometrie sans limite, oscillation d'ordre 0 ») sans preciser la jauge conforme ni les variables. Avec les donnees de la note elle-meme, la classe generique est V1 pour W et la metrique, V2 pour L et R dans la jauge du test. La contradiction entre RJ2-2 (l.43) et RJ2-3 (calcule ici) n'est pas resolue dans la note ; le gel (l.35) classe ce cas en V0. Je ne propose pas V0 global, car la partie principale tient :

**Formulation proposee** : « RJ2-V1 restreint. (i) La classe a un seul exposant est preservee par le couplage : au sens formel sous H1, H2 et un choix de jauge conforme a expliciter ; dans le test perturbatif de Sitter a l'ordre epsilon^3, sans pole ni logarithme, avec detecteurs controles positivement. (ii) Classe generique : sans pole ni logarithme a l'ordre epsilon^3 ; Weyl rescale continu, pas C^1 ; metrique conforme C^1, pas C^2 ; Schouten et courbure scalaire conformes bornes sans limite dans la jauge du test ; l'existence d'une jauge conforme ou la geometrie entiere a une limite est ouverte. »

**Portee (§5).**
- Classe a un seul exposant (l.74) : acceptable, en ajoutant la condition H2 et la jauge conforme. « sans relation regularisante » a restreindre aux seconds membres de matiere.
- RG-4 (l.75) : le point (1) (spineur sans limite, phase Omega^{+-i mu}) est juste et deja acquis par RJ. Le point (2) « la geometrie est continue mais pas C^1 » doit devenir : W continu non C^1, metrique C^1 non C^2, Schouten sans limite dans la jauge du test. La phrase sur la regle de raccord (« une regle qui n'exige la regularite que de la geometrie admet la classe a un seul exposant ») est juste pour cette classe (aucune oscillation, verifie aussi pour L et R puisque j = 0 seulement), mais pour la classe generique la reponse depend du choix du facteur conforme, ce qui est precisement l'objet d'une regle de raccord en CCC : point a signaler, il touche la regle elle-meme.
- Rem. 2(4) (l.76) : la phrase proposee est acceptable si elle mentionne « on a de Sitter background, four Dirac modes, to third order in the amplitude », et si elle ne dit rien de la regularite de la geometrie generique.
- « Ce qui n'est pas fait » (l.77) : a completer par la jauge conforme et par l'absence de calcul des inconnues de Friedrich dans le test.

## 7. Liste classee des constats

### Erreurs
- **E1.** NOTE-217 l.43 (« la geometrie a une limite a scri, ses termes oscillants commencent a l'ordre 1 »), reprise l.69 et l.75 (2), et clause generique du verdict V1 (gel l.36). Faux dans la jauge du test (jauge H1 au premier ordre) : L_00 = Psi'' - (q^2/3)(Phi + Psi) et R[g_c] = 2q^2 Phi - 4q^2 Psi - 6 Psi'' oscillent a l'ordre 0 dans les secteurs q = +-(2,0,0), +-(0,0,2) (rb2_full_gen_1310.txt l.109, 115, 120, 126). Origine : etape 3 (l.40) suppose une equation d'evolution pour toute inconnue geometrique ; L_00 est fixe par (3.5) via d_Omega s ; H1/H2 ne fixent pas la jauge conforme.
- **E2.** rj2_ops.py l.98 : co-repere inverse `eps*(h*eta)/2` au lieu de `eps*(eta*h)/2` ; E*Ed different de Id des que h_0i est non nul (rb2_quick_sortie.txt). Sans incidence sur les resultats (dirac_op non utilise par le test, effet nul au premier ordre sur fond plat), invisible a tous les controles existants.
- **E3.** NOTE-217 l.57 (« H_ij TT ordre min 3 (particulier) ») : Omega^3 est l'exposant homogene TT (exposants 0 et 3, l.59) ; la source TT Omega^2 T_c,ij commence a Omega^2 (generique) ou Omega^3 (un seul exposant, tau_ab = O(Omega^2)), donc la solution particuliere commence a Omega^4 (resp. Omega^5). Le terme Omega^3 obtenu avec LIBRE = 0 vient du choix des variables libres par linsolve (rj2_test.py l.151 a 155), pas de la source. Meme remarque pour l'Omega^3 de H_ij dans run_un_1310.txt.

### Corrections
- **C1.** NOTE-217 l.71 « Global : RJ2-V1, prediction realisee » : la clause formelle est conditionnelle (H2 non demontree, l.33, l.77) et la clause generique est contredite par E1. Reformuler (§6).
- **C2.** NOTE-217 l.33 « c'est le cas formel de la situation de Friedrich pour la poussiere » : la jauge de Friedrich (e_0 = U, comobile, R prescrit, geodesiques conformes, (4.16), zeta_ab en §5) n'est pas la jauge (Omega, x) ; H2 est une hypothese nouvelle et doit inclure la fixation de la jauge conforme. Affirmation sur Friedrich au-dela de (3.3) non verifiee (FW-1).
- **C3.** NOTE-217 l.55 et l.65 : « Phi(0) = Psi(0) = 0, coherent avec (3.3) » : (3.3) ne contraint que g_c^{00} = -1 + 2 Phi (et le shift au second ordre) ; Psi(0) = 0 vient des contraintes d'Einstein.
- **C4.** Gel l.31 vs NOTE-217 l.46, l.54 : psi_3 non construit (seule la source F et le critere n = 0) ; equations redondantes non controlees separement, message d'incompatibilite ambigu (rj2_test.py l.153). Aucun controle positif dans l'execution (le detecteur n'est jamais sollicite) ; ceux de RB-2 (PC1, PC2) montrent qu'il fonctionne.
- **C5.** Gel l.41 : le point faible annonce (compatibilite de la jauge e_0 // grad Omega avec la forme du test) n'est pas discute dans NOTE-217 ; l'ecart est O(S) = O(Omega^2) pour Dirac, mais c'est le choix conforme du test qui produit E1.
- **C6.** NOTE-217 l.50 et l.70 (« deux valeurs de mu », « 36 couplages ») : la structure de resonance ne depend pas de mu reel non nul (sorties 13/10 et 7/3 identiques hors en-tete) ; k1 orthogonal a k2, normes egales, coplanaires ; les secteurs +-2k1, +-2k2 ne contiennent structurellement que j = 0. La diversite effective est plus faible qu'annoncee ; des k generiques (non orthogonaux, normes differentes, non coplanaires) seraient plus probants.
- **C7.** NOTE-217 l.43 et l.75 (2) : « continue, pas C^1 » vaut pour W ; la metrique est C^1 non C^2 ; L et R n'ont pas de limite dans la jauge du test.
- **C8.** NOTE-217 l.30 : « Aucune relation regularisante n'est necessaire » : a restreindre aux seconds membres de matiere ; et chez Friedrich l'alignement resulte du Lemme 4.1 (dynamique) plus la jauge conforme, pas d'une jauge seule.
- **C9.** NOTE-217 l.76 : texte propose pour la Rem. 2(4) a completer (fond de Sitter, quatre modes, ordre epsilon^3, H2) et sans affirmation sur la geometrie generique.

### Remarques
- **R1.** Reproduction exacte de la geometrie epsilon^2 (rb2_full_gen_1310.txt l.4 a 89 = run_gen_1310.txt). Reexecutions : voir l'addendum en fin de rapport.
- **R2.** Le controle de diffeomorphisme de `dirac_lin` est complet au premier ordre (tout 1-jet de h est de jauge pure) et detecte un coefficient de spin faux (rb2_cspin_sortie.txt : aucun ajustement pour CSPIN = 1/4, -1/2, 0). Point fort du dossier.
- **R3.** Detecteurs vivants : PC1 (Phi(0) injecte -> resonances detectees), PC2 (source TT resonante -> incompatible ; non resonante -> compatible). PC1b et PC1c localisent la seule voie de resonance a epsilon^3 : la valeur a scri du lapse.
- **R4.** Le critere de resonance est verifie couple par couple (rj2_test.py l.198 a 242) et non sur la source totale par k' : sans consequence tant qu'aucun couple n'est resonant.
- **R5.** LIBRE = 1 (l.15, l.155) fixe tous les parametres libres a 1 dans les secteurs q et -q sans imposer h(-q) = conj h(q) : sans effet sur un test lineaire, mais ce n'est pas une metrique reelle.
- **R6.** Les etapes 1, 2 et 4 de l'argument formel sont justes ; l'etape 1 utilise correctement le signe de Friedrich ((3.3), (3.8)) et la trace physique T-hat = Omega^3 tr tau.
- **R7.** La compatibilite des dix equations d'Einstein dans chaque secteur est un controle collectif fort de la conservation de T_c, donc des bilineaires des secteurs q non nul, que le « controle RJ » (q = 0, composante 00) ne couvre pas.
- **R8.** Lemmes (a), (b), (c) et noyau P1 : scripts corrects (relus) ; (b) : K est l'unique solution de i nslash K = m (nslash inversible) ; les valeurs propres de K ne sont calculees que pour n = n0 e^0, mais l'invariance de Lorentz suffit.
- **R9.** A epsilon^4 et epsilon^5, rien n'est teste ; les canaux possibles (lapse, shift, produits de donnees TT libres) sont enumeres en §4.3 ; seul le lapse est protege par une identite exacte ((3.3)).
- **R10.** Le precheck (3.3) ne teste qu'un cas homogene (FLRW) ; il fixe tous les signes de (3.3) (residu nul avec C quelconque), ce qui suffit pour l'etape 1.

## Addendum : reexecutions

Copies des scripts originaux reexecutees dans work_rb2/ (Python 3, SymPy 1.14.0) : rj2_lemmes.py, rj2_ops_check.py, rj2_lin_check.py et precheck/eq33_check.py donnent des sorties **identiques** a rj2_lemmes_sortie.txt, rj2_ops_check_sortie.txt, rj2_lin_check_sortie.txt et eq33_check_sortie.txt. La partie geometrique de rj2_test.py (mu = 13/10, generique) est reproduite a l'identique (rb2_full_gen_1310.txt l.4 a 89). La partie epsilon^3 n'a pas ete relancee telle quelle ; elle est couverte par les controles positifs PC1, PC1b et PC1c, qui reutilisent la meme fonction de source.
