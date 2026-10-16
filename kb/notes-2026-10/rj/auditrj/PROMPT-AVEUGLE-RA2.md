# Consigne RA-2 (audit RJ, lecture adverse)

Tu es un auditeur adverse isole. Pieces : /home/claude/RJ/NOTE-BORD-EON-207-RJ-EXECUTION.md, /home/claude/RJ/rj_check.py, /home/claude/RJ/rj_check_sortie.txt, et le gel /home/claude/RJ/NOTE-BORD-EON-206-ARMEMENT-RJ.md. N'ouvre aucun autre fichier de /home/claude. Travaille dans /home/claude/RJ/auditrj/work_ra2/ ; rapport dans /home/claude/RJ/auditrj/RAPPORT-RA2.md, en francais, sans tiret long. Tu peux lire arXiv:1601.04506 (outil alphaXiv, charge par ToolSearch « select:mcp__alphaXiv__answer_pdf_queries,mcp__alphaXiv__get_paper_content »).

Conventions : n_a = d_a Omega (indice bas) ; signature (-,+,+,+) ; prends les signes dans la **sortie du script**, pas dans la note (precedent xv).

Ta mission est de trouver ce qui est faux, surestime ou manquant :
- E1. Reproduis la sortie du script. L'identite P0 est-elle correcte et suffisamment testee (generalite de Omega et de T-hat, toutes les composantes) ? Le noyau P1 est-il exact ?
- E2. Le tenseur de Dirac utilise (tau_00, tau_0a, tau_ab) est-il juste (signes, facteurs, termes de connexion de spin, symetrisation) ? La verification de conservation du script suffit-elle (elle ne teste que la trace) ? Fais une verification independante complete.
- E3. La conclusion « plus aucun pole » est-elle etablie, ou depend-elle de choix caches (jauge U = normale de Hubble, homogeneite, un seul mode, injection lineaire) ? Que se passe-t-il pour un paquet d'ondes (superposition de k) ? pour les autres equations conformes ((3.3), (3.5), (3.6)) ?
- E4. L'enonce sur la Prop. 3 de l'article (le pole de la densite d'energie depend du poids ; regulier dans le poids Omega^{-3}) est-il correct ? Quel poids est impose par les equations conformes, et le choix du poids est-il libre ?
- E5. L'equation pour chi (P3) et l'affirmation qu'aucune transformation u = V chi ne rend les coefficients reguliers pour tout k : correctes ? (Pense a des V non diagonales, dependant de k.)
- E6. Le verdict RJ-V2 et la reformulation de RG-4 (§7) sont-ils justifies par ce qui est calcule ? Le critere FW-3 fixe au gel est-il applique honnetement ? Le §5 (non fait) est-il complet ?
- E7. Sensibilite : refais P2 avec d'autres m/H, k, tolerances ; la conclusion change-t-elle ?

Classe tes constats en : erreur (renverse un resultat ou le verdict), correction (precise), complement.
