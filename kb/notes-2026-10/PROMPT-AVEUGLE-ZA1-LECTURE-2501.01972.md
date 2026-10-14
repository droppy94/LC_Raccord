# Prompt ZA-1 : lecture aveugle d'une source et conversion (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_za1/ (rien sous /mnt/user-data/, /home/claude/iry/, /home/claude/irz/, /home/claude/auditY/, ni dans d'autres dossiers audit_*). Lis la source via les outils alphaXiv (get_paper_content avec fullText, answer_pdf_queries). Reponds en francais, sans tirets longs. Etiquettes : [extrait] (citation verbatim avec numero d'equation ou de page), [calcule], [derive].

## Source
S : arXiv:2501.01972 (Foraci, Woodard, decembre 2024).

## Taches
1. Releve titre, auteurs, date, type (prepublication ou publie), et le resume.
2. Releve, avec numero d'equation, la correction a une boucle du Weyl electrique C_0i0j des ondes gravitationnelles sur de Sitter pour (a) le fermion de Dirac sans masse, (b) le scalaire conformement couple, et ce que la source dit du photon. Releve la convention de κ de la source.
3. Releve la forme resommee (puissance de a) et la methode : quelle equation, quelle fonction γ ou β, quelle substitution, quelle justification ; cite verbatim les phrases qui introduisent et concluent la resommation. La source demontre-t-elle la forme resommee, la verifie-t-elle a un ordre superieur, ou la presente-t-elle comme un procede ? Avec quels mots ?
4. Releve les conditions de validite declarees (duree de la phase de Sitter, logarithmes dominants, etat, prescription in-in, jauge). Dis explicitement ce que la source NE discute PAS parmi : independance de jauge, limite a → ∞, nombre maximal d'e-folds, echelle de rupture.
5. Conversion : en posant κ_P² = 8πG (κ_P = racine de 8πG) et b = (N_S + 6N_F + 12N_V)/(120(4π)²) (coefficient du carre de Weyl dans la trace anomale pour N_S scalaires, N_F Dirac, N_V vecteurs), exprime le coefficient du ln a de la source pour chaque espece sous la forme n × b κ_P² H², et donne n. Les n sont-ils egaux ? Fais ce calcul en sympy dans /home/claude/audit_za1/work/.
6. Releve la correction a une boucle du potentiel newtonien et sa forme resommee ; a-t-elle le meme exposant que le Weyl electrique ?

Rends un rapport structure dans /home/claude/audit_za1/RAPPORT-ZA1.md ; sauvegarde les extraits verbatim dans /home/claude/audit_za1/work/ avec leurs empreintes sha256.
