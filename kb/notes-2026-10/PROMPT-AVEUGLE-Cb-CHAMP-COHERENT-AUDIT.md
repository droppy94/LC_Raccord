# Mission (audit froid de code et d'un argument)

Tu audites (A) un script sympy, /home/claude/audit_cb/cb_coherent_v3.py (sha256 9c7d5c04bb46cea296a600fdd061f71d7164b3846f6a2b881068eb41f0493e5a : verifie d'abord), et (B) un argument de physique reproduit ci-dessous. Ne lis aucun autre fichier du disque (rien sous /home/claude/n97, /home/claude/n9*, /mnt/user-data). Tu peux executer le script (python3 -I) et ecrire tes controles dans /home/claude/audit_cb/.

## (A) Points a verifier dans le script (verdict OK / DEFAUT pour chacun)
1. Christoffels, derivee covariante, divergence, trace : formules et conventions.
2. Equation du champ de jauge d_mu(I^2 F^{mu nu}) = 0 : correctement posee et satisfaite ?
3. Secteur Maxwell X^M : formule, positions d'indices, signe ; I^2 = e^-2(1 - 2 beta ln s) correspond-il a e^-2(1 + 2 beta ln a) avec a = 1/s ?
4. Trace anomale : la relation sqrt(g) T = dS/dsigma et S_B = -(beta/2e^2) ∫ sigma F.F|eta donnent-elles le signe et la normalisation employes ? Le « controle independant » du script est-il vraiment independant ?
5. Fermeture isotrope, resolution de la conservation, constante d'integration.
6. Calcul de R : definition, antisymetrisation, toutes les composantes non nulles couvertes ? Effet du choix s = -tau (renversement du temps) sur les signes et sur la conclusion.
7. Extraction des termes non lisses et budget anisotrope Pi : correct ? L'ansatz pour Pi est-il assez general (essaie d'autres termes : ln^2, puissances negatives) ?
8. Execute le script : la conclusion imprimee decoule-t-elle du calcul ? Reproduis independamment les termes en ln de R.

## (B) Argument a auditer (texte soumis)
« La dependance anomale se complete covariamment par une fonctionnelle de la metrique seule, Omega[g], qui vaut le facteur de Weyl sur les metriques Weyl-plates (Benevides-Dabholkar-Kobayashi, arXiv:1808.08237, eq. 2.13 : Riegert ou toute autre). L'action anomale covariante est S_B = -(beta/2e^2) ∫ sqrt(g) Omega[g] F_{mu nu}F^{mu nu}. Sa variation metrique a deux parties : (a) a Omega[g] fixe, variation de sqrt(g) F^2 : proportionnelle a Omega[g] fois le tenseur de Maxwell, anisotrope ; (b) variation de Omega[g] : ∫ d^4x F^2(x) delta Omega[g](x)/delta g^{mu nu}(y). Le bitenseur delta Omega[g]/delta g est construit sur le seul fond de Sitter, invariant par rotations spatiales ; la source F^2(x) = 2 B0^2 est un scalaire uniforme. Le resultat en y est donc invariant par rotations : isotrope. Consequence : dans toute completion de cette classe, le secteur non Maxwell est isotrope, et la compensation de l'anisotropie logarithmique du secteur Maxwell est impossible. »
Questions : cet argument est-il correct ? Ses hypotheses implicites (forme de la completion, role de S_flat et de ses termes non locaux en F, homogeneite, conditions aux limites/etat dans la definition d'un operateur non local comme l'inverse de Delta_4 en de Sitter, causalite in-in) sont-elles nommees ? Y a-t-il un contre-exemple ou une faille ?

## Rendu
Rapport : verdict par point (A1 a A8), analyse de (B) avec failles eventuelles, scripts de controle (chemins + sha256), verdict global : conclusion du script (a) confirmee, (b) confirmee avec reserves nommees, (c) infirmee ; argument (B) : valide / valide sous hypotheses nommees / invalide.
