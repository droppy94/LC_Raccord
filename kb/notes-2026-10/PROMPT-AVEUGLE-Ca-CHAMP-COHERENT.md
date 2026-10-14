# Mission (audit froid, re-derivation independante)

Tu es un physicien mathematicien. Resous le probleme ci-dessous de facon independante, avec ton propre code (sympy conseille), dans un dossier neuf que tu crees : /home/claude/audit_ca/. Ne lis AUCUN fichier existant ailleurs sur le disque (en particulier rien sous /home/claude/n97, /home/claude/audit_cb, /home/claude/n9*, /mnt/user-data). Travaille uniquement a partir de cet enonce. Il n'y a pas de resultat attendu communique.

## Cadre
- Coordonnees (s, x, y, z), metrique conforme plate eta = diag(-1,1,1,1). Metrique physique de Sitter : hat-g = Omega^{-2} eta avec Omega = s > 0 (s = -tau, temps conforme renverse ; s -> 0+ est l'infini futur conforme). Facteur d'echelle a = 1/Omega.
- Electrodynamique avec anomalie de Weyl (Benevides, Dabholkar, Kobayashi, arXiv:1808.08237, eq. 2.11 et 3.12-3.13) : action effective du champ de jauge en metrique Weyl-plate g = e^{2 sigma} eta :
  S = S_flat + S_B,  S_B = -(beta/(2 e^2)) ∫ d^4x sigma(x) F_{mu nu} F^{mu nu}  (indices leves par eta),
  ce qui donne en FLRW l'action simplifiee S = -1/4 ∫ d^4x I^2 F_{mu nu}F^{mu nu} (indices eta), I^2 = e^{-2}[1 + 2 beta ln a]. Ici sigma = ln a. beta > 0 petit, e > 0.
- Configuration : champ magnetique uniforme dans le cadre conforme, F_xy = -F_yx = B0 constant, toutes les autres composantes nulles.
- Conventions : signature (-+++), T_{mu nu} = -(2/sqrt|g|) delta S / delta g^{mu nu} ; sous g -> e^{2 sigma} g on a sqrt|g| g^{mu nu} T_{mu nu} = delta S/delta sigma.
- Tenseur physique hat-T : on note X_{mu nu} ses composantes covariantes dans les coordonnees (s,x,y,z). Il se decompose en (i) un secteur Maxwell X^M = I^2 (F_{mu a} F_{nu b} hat-g^{ab} - 1/4 hat-g_{mu nu} F_{ab}F_{cd} hat-g^{ac} hat-g^{bd}) et (ii) un secteur R qui porte toute la trace anomale (deduite de S_B) et retablit la conservation totale hat-nabla^mu (X^M + X^R)_{mu nu} = 0.
- Fermeture imposee pour le secteur R : homogene et isotrope, X^R = diag(r0(s), r1(s), r1(s), r1(s)).
- Objet : R_{rho nu lambda} = 2 Omega^{-1} hat-nabla_{[nu} hat-L_{lambda] rho}, hat-L_{mu nu} = (kappa/2)(hat-T_{mu nu} - (1/3) hat-T hat-g_{mu nu}), antisymetrisation avec facteur 1/2 (second membre de l'equation (2.17) de H. Friedrich, arXiv:1311.0700v2, partie source).

## Questions
1. Verifie que la configuration resout l'equation du champ de jauge issue de l'action simplifiee.
2. Calcule X^M, sa trace, sa divergence hat-nabla^mu X^M_{mu nu}.
3. Calcule la trace anomale hat-g^{mu nu} hat-T_{mu nu} a partir de S_B (precise signe et normalisation).
4. Determine X^R (fermeture isotrope) a partir de la trace et de la conservation.
5. Calcule toutes les composantes non nulles de R pour le total. Contient-il des puissances negatives de Omega ou des facteurs ln Omega ? Donne les coefficients. Controle beta = 0.
6. On ajoute au secteur R une contrainte anisotrope homogene Pi(s) diag(0,1,1,-2). Est-elle conservee ? Quelles fonctions Pi rendent R exempt de ln Omega et de puissances negatives ? Compare a la structure du secteur Maxwell.
7. Question de structure (raisonnement, sans calcul lourd) : si la dependance en sigma de S_B est completee covariamment en remplacant sigma par une fonctionnelle Sigma[g] de la seule metrique (egale a ln a sur FLRW conformement plat), que peut-on dire, pour CE champ uniforme sur CE fond, de la structure tensorielle (isotrope ou non) de la contribution a T_{mu nu} provenant de la variation de Sigma[g] ? Justifie, et dis quelles hypotheses ton argument utilise et ce qui pourrait le mettre en defaut.

## Rendu
Rapport ecrit : resultats de 1 a 7, controles, ambiguites tranchees, chemin et sha256 de tes scripts.
