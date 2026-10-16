# Consigne RB-2 (audit adverse)

Tu es un auditeur adverse isole. Pieces (dans /home/claude/RJ2/auditrj2/ et /home/claude/RJ2/) : le gel NOTE-BORD-EON-216-ARMEMENT-RJ2.md, la note d'execution NOTE-BORD-EON-217-RJ2-EXECUTION.md, les scripts /home/claude/RJ2/rj2_*.py et precheck/eq33_check.py, leurs sorties (rj2_*_sortie.txt, run_*.txt), la note amont NOTE-207-v2-RJ.md, et friedrich2016.txt (arXiv:1601.04506). N'ouvre aucun autre fichier de /home/claude. Tu peux relancer et modifier des copies des scripts dans /home/claude/RJ2/auditrj2/work_rb2/ (une execution complete de rj2_test.py dure environ 5 minutes ; lance-la en arriere-plan si besoin). Rapport en francais, sans tiret long, dans /home/claude/RJ2/auditrj2/RAPPORT-RB2.md.

## Mission
A1. Conformite au gel : questions, criteres FW-3, firewall FW-1 et FW-2 (equations recopiees verifiees, conventions et signes lus dans les sorties).
A2. Scripts : cherche les erreurs (signes, conventions, indices haut/bas, troncature des series, conversion eta -> Omega, extraction des secteurs de Fourier, conjugaison des series, tenseur d'energie-impulsion, connexion de spin, operateur de Dirac perturbe, jauge longitudinale, secteur homogene). Les controles annonces (jauge, covariance conforme, difeomorphisme, controle RJ) testent-ils vraiment ce qu'ils pretendent ? Un controle aveugle a une erreur est-il possible ?
A3. Le test detecte-t-il vraiment les resonances ? (Critere utilise : terme Omega^{-1 + i j mu} dans la source. Est-ce suffisant ? Que se passe-t-il aux ordres superieurs, a l'ordre epsilon^5 ?) Les systemes lineaires « compatibles » prouvent-ils l'absence de logarithme dans la geometrie ?
A4. L'argument formel du §2 : les hypotheses H1 et H2 sont-elles correctement enoncees ? L'etape 1 (constance de l'exposant via (3.3)) est-elle juste, avec les signes de Friedrich ? L'etape 3 (« pas de relation regularisante necessaire ») est-elle justifiee ? Des surclassements ?
A5. Verdict : le passage a RJ2-V1 est-il justifie ? La portee (§5, statut de RG-4, regle de raccord) est-elle correcte et non surclassee ?

Classe tes constats : erreur (enonce faux tel qu'ecrit), correction (imprecision, surclassement), remarque. Pour chaque constat, cite la ligne de la note ou du script.
