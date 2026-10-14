# Prompt AAA-2 : audit d'un script (aveugle au travail anterieur)

Tu es un auditeur froid. Ne lis aucun fichier du disque en dehors de /home/claude/audit_p1/aaa2/ (rien sous /mnt/user-data/, /home/claude/work/, ni dans d'autres dossiers audit_*). Le seul fichier fourni est /home/claude/audit_p1/aaa2/iraa_aniso_v2.py. Travaille dans /home/claude/audit_p1/aaa2/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive], [rapporte].

## Taches
1. Lis le script, execute-le (python3, sympy et mpmath installes), sauvegarde sa sortie et son empreinte sha256.
2. Dis ce que le script calcule reellement (quel tenseur, quel etat, quelle convention de signature, quelle structure de phase) et si les commentaires et les messages imprimes correspondent a ce qui est calcule. Releve toute ligne imprimee « en dur » (non calculee) presentee comme un resultat, et toute annotation fausse (signe, parite, valeur attendue).
3. Reproduis independamment, par ton propre code (sans copier le sien), le resultat central : la contribution du terme alpha beta* (phase e^{-ik(eta+eta')}) au tenseur ameliore du scalaire conforme (xi = 1/6) a la coincidence, composantes T_00, T_0i, T_ij, et sa decomposition en trace / partie sans trace. Concorde-t-elle avec le script ?
4. Verifie le controle numerique du cas N = 3 (integrale Int_0^inf dk sin(2 k eta) e^{-a k}) par une forme fermee et dis si la valeur attendue annoncee dans le script est juste ou fausse (signe).
5. Cherche des contre-exemples : existe-t-il une dependance angulaire de alpha beta* ou une loi de decroissance telle que la partie sans trace de T_ij se comporte en 1/eta quand eta -> 0 tout en provenant d'un alpha beta* a decroissance rapide en |k| ? Justifie.

Rends un rapport structure dans /home/claude/audit_p1/aaa2/RAPPORT-AAA2.md, avec les empreintes sha256 de tes scripts et sorties.
