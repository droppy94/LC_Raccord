# Mission (audit froid de code)

Tu audites un script de calcul symbolique : /home/claude/audit_b/q_m3_log_v5.py (copie fournie, sha256 d240832ca6815f9b7b6295c745a1d971237830049d0c32f092022709d0ce74fa ; verifie l'empreinte d'abord). Ne lis aucun autre fichier du disque que ce script (en particulier rien sous /home/claude/n91w, /home/claude/n91, /mnt/user-data/outputs). Tu peux l'executer (python3 -I, sympy) et ecrire tes propres scripts de controle dans /home/claude/audit_b/.

## Ce que le script pretend faire
Source test lineaire sur de Sitter fixe (hat-g = Omega^{-2} eta, Omega = -tau), un mode e^{ikx}, secteur scalaire, trace physique imposee A Omega^4, conservation exacte ; il evalue R_{rho nu lambda} = 2 Omega^{-1} hat-nabla_{[nu} hat-L_{lambda] rho} (hat-L = kappa/2 (hat-T - hat-T hat-g/3)) et cherche les donnees d'etat polyhomogenes rendant R regulier aux ordres controles.

## Points a verifier, un par un (rends un verdict OK / DEFAUT pour chacun)
1. Christoffels et derivee covariante d'un 2-tenseur covariant : formules et conventions.
2. La solution (a, b, c, d) satisfait-elle vraiment conservation et trace ? Les integrations et la substitution log(tau) -> log(-tau) sont-elles legitimes pour tau < 0 ?
3. L'expression codee de hat-nabla_{[nu} hat-L_{lambda] rho} correspond-elle a la definition (ordre des indices dans DL[(r,m,q)] = hat-nabla_r hat-L_{mq}) ? Le choix des composantes evaluees couvre-t-il toutes les composantes independantes non nulles du secteur scalaire ? Sinon, lesquelles manquent et cela change-t-il le resultat ?
4. Extraction des termes non lisses : la methode (Poly en L, multiplication par tau^10) est-elle correcte, sans perte de termes ?
5. Argument de troncature : la donnee c est tronquee a tau^3 ; le script n'impose les conditions qu'aux ordres tau^m, m <= 1, en affirmant que le coefficient de tau^m dans R depend de c jusqu'a tau^(m+2). Verifie cette affirmation (par exemple en ajoutant des termes d'ordre tau^4, tau^4 ln, tau^4 ln^2 a c et en controlant que les conditions retenues ne changent pas).
6. Completude des inconnues dans linsolve et lecture de la solution.
7. Executes le script ; la conclusion imprimee decoule-t-elle bien du calcul ? Reproduis-la par un controle independant (par exemple en substituant la solution trouvee et en developpant R).

## Rendu
Rapport ecrit : verdict par point, defauts trouves avec leur effet sur la conclusion, scripts de controle (chemins + sha256), et un verdict global : la conclusion du script est-elle (a) confirmee, (b) confirmee avec reserves a nommer, (c) infirmee.
