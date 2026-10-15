# Consigne aveugle DA-2 (audit adverse du manuscrit et du script)

Tu es relecteur adverse d'un manuscrit de physique mathematique. Ta tache est de le REFUTER si possible : chercher des erreurs de calcul, de signe, de logique, des hypotheses cachees, des contre-exemples, des affirmations plus fortes que ce qui est demontre. Tu ne sais rien du programme de recherche qui l'a produit, et tu ne dois pas en tenir compte.

## Pieces (chemins locaux)
- Manuscrit : /home/claude/article-rg4/audit/dirac-mass-scri-v2.tex (lis le source LaTeX en entier).
- Script : /home/claude/article-rg4/audit/dirac_scri_check_v2.py ; tu peux l'executer (python3, scipy installe) et le modifier dans une copie pour tester d'autres cas.

## Ce qui est demande
Pour chacun des enonces suivants, rends un verdict (correct / correct avec correction mineure / faux / non demontre) avec justification, et propose la correction s'il y a lieu :
E1. Lemme 1 et Proposition 1 (norme constante ; structure u = exp(i beta (m/H) ln Omega) chi avec chi -> chi_0, borne ||chi - chi_0|| <= k|eta| ||chi_0|| ; absence de limite). Verifie en particulier la borne et l'argument de convergence de chi.
E2. Proposition 2 (jauge) : points (a), (b), (c), et la phrase finale « no gauge in which both psi_hat and A extend continuously ». Verifie la lecture physique lambda = -mt, A_eta = a A_t.
E3. Proposition 3 et formule (6) de la densite d'energie rescalee ; verifie le calcul, l'invariance de jauge et l'affirmation sur l'etat a une particule (difference de valeurs moyennes sans ambiguite de renormalisation).
E4. Lemme 2 (couplages locaux sur de Sitter exact) : la classe est-elle bien definie, la preuve couvre-t-elle toute la classe, y a-t-il un contre-exemple dans la classe ?
E5. Proposition 4 (masse variable) : conditions (a), (b), (c), leur ordre strict, l'exemple m ~ Omega^{1/2}.
E6. Proposition 5 et section 5 : la conclusion est-elle bien conditionnelle et proportionnee aux enonces demontres ?
E7. Script : fait-il ce que la section « Verification » affirme ? Y a-t-il un defaut d'implementation ou de conventions (signes, normalisation de rho_hat) ?

Termine par une liste des erreurs trouvees classees par gravite (bloquante / a corriger / cosmetique) et un verdict global. Un rapport qui ne trouve rien doit dire ce qu'il a effectivement verifie.
