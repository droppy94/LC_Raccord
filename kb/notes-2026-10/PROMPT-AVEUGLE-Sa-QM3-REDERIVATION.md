# Mission (audit froid, re-derivation independante)

Tu es un physicien mathematicien. Resous le probleme ci-dessous de facon independante, avec ton propre code (sympy conseille, dans un dossier neuf que tu crees, par exemple /home/claude/audit_a/). Ne lis AUCUN fichier existant ailleurs sur le disque (en particulier rien sous /home/claude/n91w, /home/claude/n91, /home/claude/qm3, /mnt/user-data/outputs). Travaille uniquement a partir de cet enonce.

## Cadre
- Metrique conforme plate g = eta = diag(-1,1,1,1) en coordonnees (tau, x, y, z). Metrique physique de Sitter : hat-g = Omega^{-2} eta, avec Omega = -tau (H = 1), et tau -> 0^- correspond a l'infini futur conforme.
- Tenseur energie-impulsion physique test hat-T_{mu nu} (premier ordre, fond fixe, pas de retroaction). On note X_{mu nu} ses composantes covariantes dans les coordonnees (tau,x,y,z).
- Un seul mode de Fourier spatial : X_{mu nu}(tau, x) = Y_{mu nu}(tau) e^{i k x}, k > 0, restreint au secteur scalaire : Y_00, Y_0x, Y_xx, Y_yy = Y_zz, toutes les autres composantes nulles.
- Contraintes : (i) conservation exacte hat-nabla^mu hat-T_{mu nu} = 0 (connexion de Levi-Civita de hat-g) ; (ii) trace physique imposee hat-g^{mu nu} hat-T_{mu nu} = A Omega^4 e^{ikx}, A constante.
- Objet a etudier : R_{rho nu lambda} = 2 Omega^{-1} hat-nabla_{[nu} hat-L_{lambda] rho}, avec hat-L_{mu nu} = (kappa/2) (hat-T_{mu nu} - (1/3) hat-T hat-g_{mu nu}), antisymetrisation [nu lambda] avec facteur 1/2. (C'est le second membre de l'equation (2.17) de H. Friedrich, arXiv:1311.0700v2, partie source.)

## Questions
1. Ecris les equations de conservation et de trace pour les Y. Identifie les donnees libres (fonctions ou constantes) qui restent apres ces contraintes.
2. Resous au voisinage de tau = 0 en autorisant des developpements polyhomogenes (puissances de tau et de ln(-tau)), y compris pour les donnees libres.
3. Determine l'ensemble des choix de donnees libres pour lesquels toutes les composantes de R sont exemptes de puissances negatives de Omega et de facteurs ln Omega, aux ordres Omega^m avec m <= 1 (precise et justifie quels ordres ton developpement controle vraiment).
4. Cet ensemble est-il vide pour A different de 0 ? S'il ne l'est pas, caracterise-le physiquement (que doit satisfaire l'etat ?). Les termes en ln(Omega) sont-ils presents dans hat-T pour ces choix ?
5. Pour un etat sans aucun ln dans les donnees libres, donne le coefficient du terme ln Omega dominant dans R (composante de ton choix, a preciser) et dis si un choix des donnees peut le supprimer, et a quel prix.

## Rendu
Un rapport ecrit (texte), avec : equations obtenues, solution, conditions trouvees, reponses aux questions 1 a 5, controles effectues (au minimum : verification que ta solution satisfait exactement conservation et trace ; cas A = 0), et toute ambiguite de l'enonce que tu as du trancher. Joins le chemin de ton script et son empreinte sha256. Ne cherche pas a deviner un resultat attendu : il n'y en a pas de communique.
