---
id: S27-02-VERDICTS-M-ET-REPLI-v4
seance: S27
date: 2026-09-23 (v1) ; 2026-10-15 (v2, greffe G-M1) ; 2026-10-15 (v3, greffe G-M2) ; 2026-10-16 (v4, greffe G-M3)
grade: [conv]
gel: S27-01-GEL-M-ET-REPLI (sha256 0fa0dc7ce461f25b656a724818383aae7c494d63db6dba626c5de945993fb86c, 2026-09-23T14:27:12Z)
script: m_specification.py (sha256 8170e68a6f6202348507c8236489f738d620ba907f5b4cdcbbc78c5b0085aa88, pris avant execution)
version: "v4 : texte v3 inchange ; §H ajoute par la greffe G-M3 (acte NOTE-200, borne par NOTE-199). v3 (sha256 8e5356e7888f36de), v2 (084a3c0fc2f050fb) et v1 conservees"
---

# S27 : verdicts

## A. Chantier M : **M-V2**, avec une reduction structurale. Prediction REALISEE.

### A.1 Condition C-M1 (masses de Yukawa : leptons charges, quarks) : une seule condition, sur le Higgs
Pres du point symetrique, le Higgs physique se comporte en dS comme h ~ Omega^{3/2 - mu}, mu = sqrt(9/4 - m_h^2/H^2), ou m_h^2 est la courbure du potentiel au point symetrique. Les masses fermioniques valent m_f = y h, donc la masse rescalee vaut m_f^ = m_f/Omega ~ Omega^{1/2 - mu} (script §1).
- m_f^ est bornee si et seulement si m_h^2 >= 2H^2 ;
- tout est lisse (Higgs rescale et masses rescalees) si et seulement si **m_h^2 = 2H^2**, alors h ~ Omega et m_f ~ Omega.
Or 2H^2 = 2 lambda/3 est exactement la condition de Friedrich (theoreme 3.1, S26) pour le Higgs lui-meme. **Une seule condition rend reguliers le Higgs et toutes les masses de Yukawa.** De plus, la condition annexe de Friedrich (pas de terme cubique, mu = 0) est satisfaite d'office par le doublet de Higgs, dont le potentiel ne contient que |H|^2 et |H|^4.
Ce que cela dit de M, et pas plus : pour le secteur de Yukawa, M se ramene a amener le Higgs au point symetrique avec une courbure egale a la masse de couplage conforme.
[v2 : precise et etendu au §F.]

### A.2 Le cout de C-M1 (script §2, ordres de grandeur [M])
Le parametre de masse actuel du Higgs vaut environ -(88 GeV)^2. La cible vaut +2H_inf^2, environ 2,9 x 10^-66 eV^2 : **changement de signe et 87 ordres de grandeur en masse au carre**, avec une valeur d'arrivee exacte. Aucun mecanisme connu ne le fait : un couplage a la courbure xi.R.|H|^2 demanderait xi ~ 5 x 10^86 ; la restauration thermique s'eteint quand T -> 0. D'ou M-V2.

### A.3 Conditions separees
- **C-M2 (baryons)** : la masse du proton et du neutron vient de Lambda_QCD, pas du Higgs. Il faut soit Lambda_QCD -> 0, soit que tous les baryons se desintegrent avant I+ (violation du nombre baryonique, hors Modele standard).
- **C-M4 (matiere noire)** : masse et stabilite inconnues ; condition a part.
- Neutrinos : couverts par C-M1 si leur masse vient d'un operateur de Weinberg (m ~ v^2, donc ~ Omega^2) ; sinon condition a part.

### A.4 Tension nommee, non tranchee (Q-M3)
C-M1 rend l'electron sans masse. Un electron sans masse ne decouple plus, et l'anomalie (beta/2e)F^2 revient (inversion du §3.2 de la reprise du 24 aout, que S26 avait ecartee pour un electron massif). Deux questions en decoulent, ouvertes :
- (a) sous H-1, le canal de jauge revient a l'ordre Omega^0 dans la trace rescalee du corpus ;
- (b) **le critere de regularite lui-meme est a verifier** : le corpus juge la trace par Omega^-4.T (physique), alors que Friedrich travaille avec T* = Omega^-2.T et localise les singularites ailleurs (dans l'equation de Cotton, terme (m^2 - 2 lambda/3) Omega^-1). Si le critere de Friedrich est le bon, une trace physique en Omega^4 est inoffensive et (a) tombe. Point a instruire avant toute conclusion sur Q-M3.
Pas de M-V3 : aucune incompatibilite n'est etablie.

## B. Chantier REPLI : **RL-V2**. Prediction (informee) REALISEE.

### B.1 Le resultat qui manquait a la serie R : le meme Omega joue des roles opposes aux deux bords (script §4)
- Au Big Bang, la metrique physique s'ecrit g = Omega^2 g~ avec Omega -> 0 : la masse en unites regulieres vaut m~ = Omega.m -> 0. **La masse devient negligeable**, comme l'energie des particules diverge devant elle.
- A I+ (convention du corpus), m^ = m/Omega -> infini. **La masse domine.**
Sous repli, le seul bord est le Big Bang : **la masse de l'electron n'y est pas une obstruction**, sans aucun mecanisme M.

### B.2 Le prix, deja nomme par la serie R (lu au texte : reprise POST-R10, R-04, R-10)
Le repli fait de la singularite isotrope (WCH) toute son hypothese. La serie R l'a instruit : R2 = RW3 (indecidable ; la singularite generique est BKL-oscillatoire, Weyl non borne ; ancrage 3D generique ouvert, meme verrou OA-1/OA-2 que A2*) ; R5 = R5-0 (+) R5-b (probleme de Cauchy conforme vers le passe bien pose seulement sous contrainte isotrope, non generique). Le repli echange donc l'obstruction de l'electron contre la question de genericite A2*, deja au programme. D'ou RL-V2.

### B.3 Origine probable de l'erreur du candidat (iii)
La reprise du 24 aout ecrivait, a I+, « m^ = Omega.m -> 0 ». C'est exactement le poids correct AU BIG BANG (B.1). Origine probable : un poids valable au bord passe transplante au bord futur. Enonce d'hypothese sur l'origine, non verifie dans les pieces.

## C. Consequences
- La CCC conditionnelle « CCC + M » est maintenant SPECIFIEE : M doit (i) amener le Higgs au point symetrique avec m_h^2 = 2H_inf^2 exactement ; (ii) eliminer les baryons ou annuler Lambda_QCD ; (iii) traiter la matiere noire ; (iv) survivre a Q-M3. Aucune extension connue ne fait (i).
- Le repli acyclique reste la seule forme ou la condition de bord conforme survit sans M, et son sort est suspendu a A2* (donc a OA-2, RG-1).
- **Consequence d'organisation** : RG-1 (simulation OA-2) devient le test porteur de la seule forme survivante du programme de bord conforme sans physique nouvelle.

## D. Passe adverse interne
1. « Le Higgs n'est pas un champ libre ; le quartique et les couplages de jauge changent l'analyse. » Pres du point symetrique, h ~ Omega, le quartique est sous-dominant ; les couplages de jauge sont conformes en 4D. Tenu au premier ordre, non demontre en general.
2. « Condition bornee (m_h^2 >= 2H^2) contre condition lisse (= 2H^2) : laquelle compte ? » S26 et Friedrich retiennent la regularite lisse ; j'ai donne les deux.
3. « B.1 est trivial. » Il est simple ; il n'etait ecrit nulle part dans la serie R, et il explique l'erreur de la table du 24 aout.
4. Non couvert : le Higgs comme doublet complexe (quatre composantes) et la jauge ; le comptage de trace de Q-M3.

## E. Non-surclassement
Aucune extension n'est proposee ni adoptee. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange. Statut de la CCC : celui de l'acte RG-4.

## F. Greffe G-M1 (2026-10-15 ; chantier HX, NOTE-185/186 ; audit 187/188, AU-V2 ; acte 189)

### F.1 Trois niveaux de C-M1
Notations : H constante de Hubble asymptotique, Lambda = 3H^2 (cosmologique), lambda_h quartique du Higgs, M2 = m_h^2/H^2 + 12 xi (sans dimension ; xi couplage a la courbure, R = 12H^2 sur dS). Higgs homogene pres du point symetrique : h = c1 Omega^{3/2 - mu} + c2 Omega^{3/2 + mu}, mu = sqrt(9/4 - M2) (a mu = 0 : Omega^{3/2}(c1 + c2 ln Omega)). Masse fermionique m_f = y h ; trois conditions de l'article (Prop. 4) : (a) champ de Dirac rescale continu ssi int m_f dt fini ; (b) densite d'energie rescalee bornee ssi m_f a = m_f/Omega borne ; (c) coefficient m_f/Omega lisse.

| M2 | (a) | (b) | (c) |
|---|---|---|---|
| <= 0 | non | non | non |
| ]0, 2[ | oui | non | non |
| 2 | oui | oui | oui |
| ]2, 9/4[ | oui | oui | non (exposants non entiers) |
| 9/4 | oui | oui | non (log) |
| > 9/4 | oui | oui | non (oscillation) |

Donnees generiques (c1 != 0). Ensemble exceptionnel c1 = 0 : (c) aussi pour M2 = -(n+1)(n-2) (2, 0, -4, -10, ...), mais l'equation rescalee du Higgs, h~'' + (M2 - 2) h~/Omega^2 = 0, reste singuliere hors M2 = 2 : solution lisse n'est pas equation lisse (precedent xii). La ligne M2 <= 0 pour le Higgs actuel sort du domaine lineaire ; le « non » y tient par la masse constante y v.
Nouveau par rapport a A.1 : la zone 0 < M2 < 2, ou le champ de Dirac rescale converge alors que sa densite d'energie rescalee diverge (confirmee numeriquement par l'audit).

### F.2 Invariance conforme et reduction
Poids (H 1, psi 3/2, A 0) : Yukawa 0 (doublet complet, h.c. compris), masse de jauge 0, F^2 0, lambda_h abs(H)^4 0 ; m_h^2 abs(H)^2 -2 (terme de Friedrich, compense par le R/6 de la metrique physique, 2H^2, a M2 = 2) ; terme cubique -1 (absent du doublet). Le coefficient de masse de l'equation de Dirac rescalee est y H_r = m_f/Omega, sans hypothese d'homogeneite.
- **Suffisance** : M2 = 2 rend lisse le Higgs rescale (theoreme 3.1 de Friedrich, etendu au systeme couple par §G), donc tout le secteur Yukawa et W, Z (coefficient de Proca rescale g^2 abs(H_r)^2, analyse sur le doublet complet avec Goldstones, la jauge unitaire etant singuliere au point symetrique).
- **Necessite** : pour les fermions charges, donnees generiques, (c) impose M2 = 2. Pour les W, Z, aucun seuil (a)/(b) n'est etabli. Neutrinos de Weinberg (poids +1, m_nu/Omega ~ Omega H_r^2/M) : seuils propres (b) M2 >= 5/4, (c) M2 in {5/4, 2} ; en conjonction avec les fermions charges, la condition du secteur redevient M2 = 2.
- Conclusion : **pour le secteur dont la masse vient du Higgs, la condition de bord est une condition unique sur le Higgs**, M2 = 2 = 2 Lambda/(3H^2) (regularite formelle), M2 >= 2 (energie bornee), M2 > 0 (champ continu).

### F.3 Hypotheses et limites
- Le Higgs doit tendre vers le point symetrique ; dans le vide brise (h -> v), m_f/Omega diverge et la reduction ne vaut pas.
- FW-3 : **levee pour le systeme classique** (v3, §G). Restent : groupe non abelien (argument), Weinberg (suffisance), existence et hyperbolicite.
- Hors reduction : Lambda_QCD (C-M2), masse de Majorana nue (poids -1, coefficient M/Omega singulier), matiere noire (C-M4), courses des couplages y, g, lambda_h et anomalies de trace (Q-M3 pour QED). Argument classique.
- Aucun mecanisme qui amenerait M2 a 2 ; le cout A.2 n'est pas rouvert.
- D.4 « non couvert : doublet et jauge » : leve pour les poids et la suffisance ; FW-3 leve par §G pour le systeme classique.

### F.4 Non-surclassement
CCC + M reste une hypothese ouverte ; C-M1 precisee, non resolue. [conv], audit par IA, non relu par un humain.

## G. Greffe G-M2 (2026-10-15, acte NOTE-194, borne par NOTE-193, AU-V2) : le systeme couple au sens de Friedrich

### G.1 Enonce
Le systeme conforme de Friedrich couple a Yang-Mills, a un Higgs (doublet, potentiel polynomial m_h^2 |H|^2 + lambda_h |H|^4, couplage non minimal xi) et a des fermions de masse de Yukawa, en inconnues rescalees (A, H_r = Omega^-1 H, psi_r = Omega^-3/2 psi), est **formellement regulier si et seulement si m_h^2 + 4 lambda xi = 2 lambda/3**, soit M2 = 2 (lambda = 3H^2). Sources : NOTE-191 v2 (script fw3_check.py), retrouve en cecite stricte (FA-1) et sous audit adverse (FA-2).

### G.2 Contenu
- Equation de Higgs rescalee : coefficient de Omega^-2 egal a m_h^2 + 4 lambda xi - 2 lambda/3 ; quartique et Yukawa de poids 0.
- Equations geometriques : plus basse puissance de (2.17) Omega^-2, coefficient (kappa/3)(m_h^2 + 4 lambda xi - 2 lambda/3) Sum phi_i^2 n_[nu eta_lambda]rho ; coefficient de Omega^-1 (kappa/6)(m_h^2 + 4 lambda xi - 2 lambda/3) nabla_[nu(Sum phi_i^2) g_lambda]rho ; les deux s'annulent a la meme condition, pour tout xi. Meme combinaison 4 lambda xi dans les deux secteurs.
- Ni le champ de jauge, ni le quartique, ni le Yukawa, ni le tenseur de Dirac n'entrent dans un coefficient singulier ; Yang-Mills conformement invariant ; courants d'ordre Omega^4.
- Avec masse de Yukawa, la forme lagrangienne du tenseur de Dirac est reguliere (ordre Omega^2) : la reserve de representation de ED (M1, NOTE-183) ne s'applique pas au secteur fermionique du Modele standard ; la singularite de masse migre entierement dans le secteur Higgs et disparait a M2 = 2.
- Calibrations : theoreme 3.1 reproduit (xi = 0, scalaire reel, V = m^2 phi^2/2 + lambda_h phi^4) ; xi = 1/6, m = 0 donne 0 ; sensibilite : un terme |H|^3 ou de type Majorana laisse un Omega^-1.
- « Seulement si » au sens formel : coefficient non nul hors condition, fonction de |H_r|^2 seul (aucune jauge ne le retire), aucun poids conforme ne retire tous les termes singuliers.

### G.3 Limites
Regularite formelle (seconds membres), pas existence ni hyperbolicite ; groupe non abelien par argument ; Weinberg en suffisance ; (2.13)-(2.16) argumentes ; hors champ : Majorana nue, Lambda_QCD, courses et anomalies (Q-M3), matiere noire ; Higgs tendant vers le point symetrique (F.3) ; m_h^2 > 0 ou xi > 1/6 requis par M2 = 2 (cout A.2 non rouvert).

### G.4 Ligne de statut
CCC + M : hypothese ouverte ; **condition unique sur le Higgs, M2 = 2, etablie pour le systeme couple classique YM-Higgs-Dirac-Einstein** (audit IA, non relu par un humain).

## H. Greffe G-M3 (2026-10-16, acte NOTE-200, borne par NOTE-199, AU-V2) : M-V3 au sens formel

### H.1 Enonce
Sous C-M1 (fermions charges sans masse a scri ; a M2 = 2, la masse physique y Omega H_r tend vers 0 : rapprochement importe), le terme local de Wess-Zumino de l'anomalie QED, beta_* Int sqrt(g) sigma F^2 (couplage effectif 1/e^2 - 4 beta_* sigma, sigma = -ln Omega ; forme de S2 : beta_* = -beta~/(2 e^2)), rend le systeme conforme **formellement irregulier si et seulement si beta_* != 0** (au premier ordre, inconnues de Friedrich ; NOTE-197 v2) :
- l'equation de Maxwell rescalee recoit un **pole** : d^a F_ab = -4 e^2 beta_* n^a F_ab / Omega + O(beta_*^2) ;
- le second membre de (2.17) recoit des termes en ln Omega, de coefficient (Omega^0 ln Omega) kappa beta_* [6 (n_nu M_lambda rho - n_lambda M_nu rho) + 2 (eta_lambda rho n^c M_c nu - eta_nu rho n^c M_c lambda)], M tenseur de Maxwell ;
- calibration : les coefficients de NOTE-98 (champ uniforme) sont retrouves exactement.

### H.2 Consequence sur solution (a ne pas confondre avec l'enonce formel)
Les coefficients en ln Omega ne s'annulent, pour des champs reels, que si F = 0 au point (argument de rang : (E_iE_j + B_iB_j)_tf = 0 force E = B = 0). La condition est plus forte que celles de NOTE-98 (champ coherent) et de NOTE-113/114 (<B_iB_j>_tf = <E_iE_j>_tf sur solution, verifiee par l'helicite pure) ; l'ecart tient a la distinction formel / sur solution (precedent xii) ; le mecanisme de compensation sur solution n'est pas calcule.

### H.3 Limites
Premier ordre ; champ F classique (ou valeur moyenne) ; completion de S2 de la forme Omega[g] F^2 : une partie isotrope ou construite sur (eta, n) ne change pas la conclusion (AA-2) ; termes non locaux (S_flat) hors champ ; C-M1 est une hypothese de CCC + M.

### H.4 Ligne de statut
CCC + M : hypothese ouverte ; condition unique sur le Higgs (M2 = 2) pour le systeme couple classique (§G) ; **au niveau quantique (anomalie de trace), M-V3 est formel sous C-M1** : la presence de charges sans masse a scri rend le systeme formellement irregulier ; G-V3 (formel, b > 0) s'applique a CCC + M comme a la CCC.

