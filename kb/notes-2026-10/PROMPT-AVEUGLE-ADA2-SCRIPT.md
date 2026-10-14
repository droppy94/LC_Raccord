# Prompt ADA-2 : audit d'un script (aveugle au travail anterieur)

Tu es un auditeur froid. Ne lis aucun fichier du disque en dehors de /home/claude/audit_p1/ada2/ (rien sous /mnt/user-data/, /home/claude/work/, ni dans d'autres dossiers audit_*). Le seul fichier fourni est /home/claude/audit_p1/ada2/irad_kernel.py. Travaille dans /home/claude/audit_p1/ada2/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive], [rapporte].

## Taches
1. Lis le script, execute-le (python3, sympy et mpmath installes ; l'execution peut prendre plusieurs minutes), sauvegarde sa sortie et son empreinte sha256.
2. Dis ce que chaque section calcule reellement et si les commentaires et messages imprimes correspondent au calcul. Releve toute ligne imprimee en dur presentee comme un resultat, toute annotation ou valeur attendue fausse, et tout endroit ou une regularisation ou un choix numerique (partie finie du noyau, quadrature, differences finies) peut fausser la conclusion.
3. Reproduis independamment, par ton propre code : (a) le coefficient reliant le Bach linearise de h_yy = -h_zz = u cos(kx) a box^2 h ; (b) l'identite (d^2 + k^2)^2 u = 0 pour les solutions de u'' - (2/tau) u' + k^2 u = 0 ; (c) le developpement au premier ordre en eps de (d^2 + k^2)^2 [e^{eps tau} u]. Concordent-ils avec le script ?
4. Examine la section ad-3 (reponse retardee en limite adiabatique) : la regularisation « partie finie a l'echelle 1 » est-elle legitime, introduit-elle une dependance d'echelle, et la conclusion R_eps -> 0 quand eps -> 0 est-elle robuste a ce choix ? Verifie numeriquement avec une autre echelle ou une autre regularisation.
5. Examine la section ad-4 : les valeurs de B calculees par differences finies sur une transition en e^{-1/t} sont-elles fiables (compare avec un calcul symbolique ou une autre methode) ? La conclusion « R lisse en tau = 0, finie, non nulle » en depend-elle ?

Rends un rapport structure dans /home/claude/audit_p1/ada2/RAPPORT-ADA2.md, avec les empreintes sha256 de tes scripts et sorties.
