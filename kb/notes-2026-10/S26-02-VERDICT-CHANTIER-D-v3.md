---
id: S26-02-VERDICT-CHANTIER-D
version: v3 (greffe G-D1-e, acte NOTE-179, 2026-10-15 ; v2 sha256 d3a1ba28a05714aa et v1 sha256 5a4f81165a80a512 conservees)
seance: S26
date: 2026-09-23
grade: [conv]
gel: S26-01-GEL-CHANTIER-D (sha256 cf1f6e9d0429ab9cc62907596f6895c21955a031ea2d0326e1cc9e4e167e7967, 2026-09-23T14:04:59Z)
script: d_poids_conformes.py (sha256 4935ea40a35ac397157a819a7ec78d7e2d196a92ae987c5a437b0197c583a786, pris avant execution)
---

# S26 : chantier (D), verdict

## VERDICT : D-V2 (+) D-V0 partiel (sur la table des candidats, pas sur la question)
- **D-V2** : le decouplage tient et gouverne pour tout ce qui est effet de boucle (le vide) ; il ne dit rien des electrons presents dans l'etat, et c'est la que se trouve l'obstruction.
- **D-V0 partiel** : la trichotomie (i)/(ii)/(iii) de la reprise du 24 aout est mal posee. Le candidat (iii) est une erreur de poids conforme. Il n'y a qu'une variable de controle, et elle ne depend pas du cadre.

Prediction anti-fit du 24 aout (D-V2, composante D-V3 partielle par C-a) : **D-V2 realise ; composante D-V3 non realisee** (la superselection, C-a, fait partie du residu que D-V2 nomme lui-meme, ce n'est pas un echec du decouplage).
Conviction prealable declaree au gel (D-V2 (+) D-V4) : l'erreur de poids est **confirmee**, mais D-V4 n'est **pas rendu**, parce que D-V4 porte sur l'USAGE que le corpus fait des candidats, et je n'ai pas lu les pieces ou il les utiliserait.

## 1. Source lue (EX-7)
H. Friedrich, « Smooth non-zero rest-mass evolution across time-like infinity », arXiv:1311.0700v2 (19 fevrier 2014), article original. Lu au texte : resume, §1, §3 (theoreme 3.1 et preuve), §4, debut du §5. Hors cran P3s.
**Convention a declarer (FW-6, FW-7)** : chez Friedrich, g = Omega^2 g^ avec g^ PHYSIQUE ; dans le corpus, g^ = Omega^2 g avec g physique. Les chapeaux sont inverses. Tout ce qui suit est ecrit dans la convention du corpus.

## 2. Resultats

### 2.1 Une seule variable de controle (script §1)
Une longueur physique L devient L^ = Omega L ; toute grandeur de dimension inverse-longueur X devient X^ = X/Omega. Donc omega^ = omega/Omega (c'est bien le candidat (i)) et **m^ = m/Omega**, pas Omega*m. Le candidat (iii) de la reprise applique a la masse le poids oppose de celui que le candidat (i) applique a la frequence. Le rapport m/omega est invariant conforme : m^/omega^ = m/omega.
Consequence : quand on approche I+, omega physique tend vers 0 pour le rayonnement qui y arrive, donc m/omega tend vers l'infini **dans les deux cadres**. La masse rescalee ne « s'efface » pas : elle diverge. L'inversion seduisante du §3.2 de la reprise (« la masse est l'alliee du raccord ») tombe avec (iii) ; FW-2 est satisfait.
Controle independant : l'equation (3.5) de Friedrich fait apparaitre le terme de masse sous la forme Omega^-2 m^2 dans l'equation rescalee, c'est-a-dire une masse rescalee m/Omega. Concordant.

### 2.2 Le vide decouple, le canal de jauge tombe (reponse a kappa'''-1)
Dans le regime omega/m -> 0, l'electron sort de la theorie effective. Ce qui en reste dans la trace est (a) l'anomalie (beta/2e)F^2 et (b) le terme (1+gamma_m) m psibar psi ; a basse energie, l'element de matrice de m psibar psi entre etats de photons compense la contribution de l'electron a (a) (theoreme de basse energie de type Shifman-Vainshtein-Voloshin-Zakharov), et il ne reste qu'un operateur de dimension six, supprime en (omega/m)^2.
Ordre dans la trace rescalee (script §4) : la branche Omega^0 de kappa-prime (anomalie non decouplee) est remplacee par **Omega^+2** (residu de dimension six), termes en derivees de Omega non compris.
Grade : le theoreme de basse energie est [M], non lu dans cette seance (EX-8 : ecrit en taux, suppression (omega/m)^2). La reduction de kappa'''-3 a kappa'''-1 (S25-05) est ainsi resolue dans le regime physique : **H-2 est fausse au bord**, beta_eff n'est pas d'ordre Omega^0.

### 2.3 Ce que le decouplage ne touche pas : les electrons de l'etat (FW-8)
Le decouplage porte sur les boucles et les operateurs locaux. Des electrons presents dans l'etat cosmologique (nombre conserve, charge conservee) ne sont pas une boucle.
- **Scalaire (source lue, theoreme 3.1 de Friedrich)** : les equations conformes couplees a un scalaire massif sont regulieres a I+ **si et seulement si m^2 = 2 lambda/3** ; sinon apparaissent des termes (m^2 - 2 lambda/3) Omega^-k, k = 1, 2.
- **Lecture neuve de cette condition (script §2)** : en de Sitter, R^ = 4 lambda, donc 2 lambda/3 = R^/6. La masse de Friedrich est **exactement celle qui rend le scalaire minimalement couple equivalent au scalaire conforme sans masse**. Verification sur le mode homogene : le champ rescale se comporte comme Omega^{1/2 -+ mu}, mu = sqrt(9/4 - m^2/H^2) ; il n'est lisse (exposants 0 et 1) que pour m^2 = 2H^2. Donc 1311.0700 ne montre pas qu'une masse generique traverse I+ : il montre que le seul scalaire massif qui traverse est celui qui, a I+, ne se distingue pas d'un champ conforme. L'effet (1a) de l'addendum P3 (« la forme categorique de l'obstruction tombe ») est **surlu** et doit etre corrige.
- **Spin 1/2 (derive dans cette seance, grade [conv])** : pour un fermion de Dirac, il n'existe aucun terme de courbure qui puisse compenser la masse. Mode homogene : le champ rescale (poids 3/2) vaut psi^ = exp(i (m/H) ln Omega), de module 1 et de phase qui tourne sans fin ; sa derivee par rapport au temps conforme non physique diverge comme 1/tau et psi^ **n'a pas de limite** a I+ (script §3). Seul m = 0 donne un champ regulier. Il n'y a pas d'analogue spinoriel de la condition de Friedrich.
- Consequence : toute population non nulle d'electrons pres de I+ rend le champ rescale non regulier au bord. Avec m_e ~ 5,1 x 10^5 eV et H_inf ~ 1,2 x 10^-33 eV, m_e/H_inf ~ 4 x 10^38 : la phase tourne d'environ 4 x 10^38 radians par facteur e de Omega.

## 3. Portee sur RG-4 (adoptee ce jour) : DECISION D'INTERPRETATION REQUISE
Texte adopte : « La CCC est refutee dans sa forme actuelle si le chantier (D) etablit, dans le regime d'echelle retenu au bord, que la contribution de l'electron a la trace rescalee diverge a I+ (ordre Omega^-1 non reabsorbable) sans mecanisme d'effacement des masses. »
Ce que S26 etablit :
- le regime d'echelle est fixe sans ambiguite : l'electron est infiniment lourd devant tout ce qui se passe au bord ;
- le vide ne produit plus d'obstruction (Omega^+2) ;
- les electrons de l'etat rendent le champ rescale non regulier ; pour le scalaire, la source lue donne des termes en Omega^-1 et Omega^-2 ; pour le spineur, aucune valeur de masse non nulle n'y echappe.

Ce que S26 n'etablit pas : que l'obstruction prenne exactement la forme « trace rescalee en Omega^-1 » pour un gaz d'electrons (c'est le comptage du corpus, que je n'ai pas refait au texte), ni ce qui arrive aux electrons avant I+ (annihilation, capture par des trous noirs qui s'evaporent : l'hypothese de Penrose pour l'essentiel de la matiere, qui laisse en general des electrons isoles).

**L'ambiguite de RG-4, a trancher par l'operateur** : « sans mecanisme d'effacement des masses » peut se lire de deux facons.
- Lecture stricte : il faut un MECANISME connu. Il n'en existe pas (Friedrich, §1 : « At present no process is known which would allow one to justify it »). RG-4 tire : la CCC dans sa forme actuelle est refutee au sens ou elle exige une physique nouvelle (effacement des masses) absente du Modele standard.
- Lecture souple : un POSTULAT d'effacement suffit (c'est la forme actuelle chez Penrose). RG-4 ne tire pas ; l'obstruction est confirmee et precisee, et toute la viabilite du cote I+ repose sur ce postulat.
Je ne tranche pas : la regle a ete adoptee aujourd'hui, et son ambiguite est un resultat de cette seance.

## 4. Passe adverse interne (ne vaut pas audit froid)
1. « Les modes homogenes ne sont pas le cas general. » Exact ; ils suffisent a exhiber l'obstruction (un contre-exemple suffit pour la non-regularite) et concordent avec le theoreme general de Friedrich pour le scalaire.
2. « Le poids 3/2 du Dirac est une convention. » C'est le poids qui rend l'operateur de Dirac sans masse covariant conforme ; avec un autre poids, le terme de masse reste en m/Omega. Tenu.
3. « Le theoreme de basse energie n'est pas lu. » Exact, [M] ; 2.2 est conditionnel a sa lecture.
4. « D-V0 partiel est-il un verdict gele ? » D-V0 est gele ; je l'applique a la table §3.1, pas a la question. Composite nomme au moment du verdict, ce que la reprise autorise.

## 5. Corrections et greffes proposees (non entees)
- S26-a : retirer le candidat (iii) de la table §3.1 de la reprise du 24 aout, ou le reecrire m^ = m/Omega.
- S26-b : corriger l'effet (1a) de l'ADDENDUM-REPRISE-P3 : la condition de Friedrich est la masse de couplage conforme ; elle ne fait pas tomber l'obstruction pour des masses generiques ni pour les spineurs.
- S26-c : table des ordres : ligne de jauge = Omega^+2 (residu de dimension six) dans le regime physique ; branche Omega^0 retiree.
- S26-d : (T) peut maintenant etre instruit : le secteur conforme au bord est Maxwell libre (plus les gravitons), ce qui donne son objet a l'anomalie c.W^2 - a.E4.

## 6. Non-surclassement
La CCC n'est ni demontree ni refutee par cette seance : la refutation depend de la lecture de RG-4, reservee a l'operateur. p_Q non fixe, N non chiffre, P2 non tranchee, noyau {A4 ; A2* ; N} inchange. Aucun numero NOTE consomme.

---

## 7. Greffe G-D1 (2026-10-14, acte NOTE-174 ; enonces audites NOTE-172/173)
Le corps ci-dessus (§0 a §6) est la v1, inchange. La presente section precise le §2.3 et complete le §2.4. Source : article NOTE-171 v2.1 (`dirac-mass-scri-v2.1.tex`), Prop. 1 a 4 et Lemme 2 restreint, confirmes par l'audit froid aveugle NOTE-173 (DA-1 en cecite stricte, DA-2 adverse). Grade [conv].

**G-D1-a (§2.3, precision de jauge).** La phrase « psi^ n'a pas de limite a I+ » est exacte pour le champ libre et pour toute jauge a potentiel integrable jusqu'a I+. Pour une solution qui est, aux temps tardifs, purement particule (ou purement antiparticule), l'enroulement est une phase commune que la transformation de jauge U(1) lambda = (m/H) ln Omega = -mt retire ; elle est reguliere dans le repere physique (psi -> e^{imt} psi, A_t -> A_t + m/e) mais donne au potentiel, dans le repere conforme, un pole non integrable (A_eta = a A_t). Enonce invariant : **il n'existe aucune jauge ou le champ rescale et le potentiel s'etendent tous deux continument a I+** ; pour une solution generique (composantes particule et antiparticule non nulles), aucune jauge ne donne de limite. La phrase « toute population non nulle d'electrons pres de I+ rend le champ rescale non regulier » doit se lire au sens de cet enonce invariant, ou au sens de G-D1-b.

**G-D1-b (§2.4, comble pour la densite d'energie).** L'obstruction invariante de jauge est portee par la densite d'energie rescalee : rho^ = Omega^{-4} T_tt = u^dag (alpha.k) u + (m/Omega) u^dag beta u, d'ou un **pole simple m/Omega** fois la densite de particules tardive (lecture physique : poussiere, rho ~ m a^{-3}, Omega^{-4} rho ~ m/Omega). Pour un etat a une particule au-dessus d'un etat quasi-libre, la difference des valeurs moyennes est independante de la renormalisation ; pour Bunch-Davies, Omega (omega_f - omega)(rho^) -> m tanh(pi m/H) norme(f)^2 > 0. Le §2.4 disait que la forme « trace rescalee en Omega^-1 » n'etait pas refaite au texte : elle l'est desormais pour la composante d'energie (pole d'ordre Omega^-1), pas pour la trace complete d'un gaz.

**G-D1-c (§2.3, couplages).** Sur dS exact, tout couplage local a la geometrie derivant d'une action reelle, U(1)-invariante, d'ordre au plus un en derivees de psi, avec Z1^2 > Z2^2, se reduit a une masse effective constante (eventuellement chirale) ; il ne leve l'obstruction que si m_eff = 0, c'est-a-dire par ajustement fin d'une echelle nouvelle contre H_inf (ex. l = m/(12 H^2) dans (m - l R) psi_bar psi). « Il n'existe pas d'analogue spinoriel de la condition de Friedrich » se lit : aucun analogue a masse effective non nulle.

**G-D1-d (masse variable).** Si la masse depend du temps : continuite du champ ssi int^inf m dt < inf ; densite d'energie rescalee bornee ssi m a borne (masse physique decroissant au moins comme 1/a) ; coefficient lisse ssi m = Omega mu, mu lisse. Ordre strict (exemples m ~ Omega^{1/2}, m ~ Omega (1 + Omega^{1/2})). La phrase de la v1 de l'article « la masse devrait etre inferieure a H_inf sur tout l'intervalle » est fausse et retiree ; elle ne figurait pas dans S26-02.

**Portee sur RG-4.** Le declenchement de RG-4 (lecture stricte) est **inchange** et mieux fonde : RG-4 porte sur la divergence de la trace rescalee a l'ordre Omega^-1, et le pole G-D1-b en est la composante d'energie, invariante de jauge ; la convention lisse (NOTE-126) est violee dans toute jauge (G-D1-a). Le grade reste « refutee a titre provisoire » : un audit IA ne vaut pas lecture humaine exterieure.

---

## 8. Greffe G-D1-e (2026-10-15, acte NOTE-179 ; calibration CAL-F, NOTE-175 a 178)
La phrase de G-D1 (§7, « Portee sur RG-4 ») selon laquelle le declenchement serait « mieux fonde » par le pole de la densite d'energie est precisee ainsi. RG-4 a deux lectures du critere, et l'electron l'obstrue sous les deux :
- **(i) Critere du corpus** (texte litteral de RG-4 : trace rescalee, Omega^-4 T) : pole simple m/Omega de la densite d'energie rescalee (G-D1-b), invariant de jauge.
- **(ii) Critere de Friedrich transpose a l'equation de matiere** (regularite formelle des seconds membres en fonction des inconnues rescalees, sens du theoreme 3.1 de 1311.0700) : l'equation de Dirac rescalee porte le coefficient m/Omega, singulier pour **toute** masse constante non nulle ; la ou le scalaire a une masse speciale (terme Omega^-2 (m^2 - 2 lambda/3), nul a m^2 = 2 lambda/3), le spineur n'en a aucune. Les solutions homogenes Omega^{+-im/H} ne sont pas lisses : aucune redefinition lisse des inconnues ne retire ce coefficient ; une phase U(1) produit un terme en gamma^mu, pas un terme de masse (audit CA-2). Les equations geometriques du systeme couple Einstein-Dirac ne sont pas traitees.
- **Retire** (ne figurait que dans la proposition de NOTE-176) : toute affirmation tiree de la valeur de (2.17) sur une poussiere homogene ; une valeur nulle sur couche ne dit rien de la regularite formelle.
RG-4 reste declenchee a titre provisoire.
