# Consigne RB-3 (re-audit court et adverse de NOTE-217 v2)

Tu es un auditeur adverse isole. Pieces autorisees : /home/claude/RJ2/auditrj2/NOTE-BORD-EON-217-RJ2-EXECUTION.md (v1), /home/claude/RJ2/auditrj2/NOTE-BORD-EON-217-RJ2-EXECUTION-v2.md (v2), RAPPORT-RB1.md, RAPPORT-RB2.md, NOTE-BORD-EON-219-AUDIT-RJ2-CONCORDANCE.md (meme dossier), les scripts /home/claude/RJ2/rj2_ops.py, /home/claude/RJ2/rj2_test_v2.py, /home/claude/RJ2/rj2_series.py et les sorties /home/claude/RJ2/v2runs/*.txt. N'ouvre aucun autre fichier de /home/claude. Travaille dans /home/claude/RJ2/auditrj2/work_rb3/ (copies si tu modifies ou relances ; une execution de rj2_test_v2.py dure environ 5 a 10 minutes, a lancer en arriere-plan). Rapport en francais, sans tiret long, dans /home/claude/RJ2/auditrj2/RAPPORT-RB3.md.

Mission, limitee aux corrections :
- R1. Chaque constat de NOTE-219 (E1 a E3, C1 a C9, points RB-1 retenus) est-il traite dans la v2, et correctement ?
- R2. Le nouveau script (courbure de g_c : R, Schouten L, Weyl W = C/Omega ; jauge B ; jeu de vecteurs « gen » ; controle positif ; source totale par vecteur cible) est-il correct ? Verifie en particulier la formule de Riemann linearise, la contraction de Ricci, le Schouten et le Weyl en dimension 4, la jauge B, et que les sorties disent ce que la v2 en tire.
- R3. La v2 introduit-elle une erreur, un surclassement ou une contradiction ? L'enonce « il existe, a l'ordre epsilon^2, un facteur conforme ou toute la geometrie a une limite » et la lecture « changement de facteur conforme theta = 1 + O(Omega^{2 +- 2 i mu}) » sont-ils justes ?
- R4. Verdict : la v2 peut-elle etre entee (aucune erreur restante parmi les points audites) ?

Classe tes constats : erreur, correction, remarque.
