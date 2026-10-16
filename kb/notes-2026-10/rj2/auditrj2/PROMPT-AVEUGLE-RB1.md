# Consigne RB-1 (derivation independante, cecite stricte)

Tu es un auditeur isole. Tu ne lis AUCUN fichier de /home/claude sauf : cette consigne et /home/claude/RJ2/auditrj2/friedrich2016.txt (texte de arXiv:1601.04506, Friedrich, « Sharp asymptotics for Einstein-lambda-dust flows » ; tu peux en lire les §§ 1 a 4). Tu travailles dans /home/claude/RJ2/auditrj2/work_rb1/ avec tes propres scripts (Python, SymPy, NumPy disponibles). Rapport en francais, sans tiret long, dans /home/claude/RJ2/auditrj2/RAPPORT-RB1.md.

## Cadre
Espace de de Sitter, carte plate, H = 1 : g = a^2(-d eta^2 + dx^2), a = -1/eta, facteur conforme Omega = -eta, constante cosmologique lambda = 3. Champ de Dirac de masse m (on note mu = m/H). Spineur conforme psi_c = Omega^{-3/2} psi, metrique conforme g_c = Omega^2 g. Poids « poussiere » de Friedrich : tau_jk = Omega^{-3} T(e_j, e_k), e repere orthonorme physique, T tenseur d'energie-impulsion du champ de Dirac. Conventions imposees : signature (-,+,+,+), {gamma^a, gamma^b} = -2 eta^{ab} ; n_a = nabla_a Omega (indice bas).

## Questions
Q1. Montre (ou refute) : tau = Omega T_c, ou T_c est le tenseur cinetique du spineur conforme dans la metrique conforme, pour un facteur conforme Omega(x) quelconque.
Q2. Sur une solution qui se comporte pres de Omega = 0 comme Omega^K P(x, Omega), P regulier, avec nabla_b psi = (n_b/Omega) K psi + (regulier) : determine K, ses valeurs propres, et la partie de T_c d'ordre 1/Omega, pour n de genre temps quelconque et un repere orthonorme quelconque. Est-elle proportionnelle a n_a n_b ? Avec quel coefficient ?
Q3. Les termes croises entre les deux sous-espaces propres de K s'annulent-ils dans psibar psi a l'ordre dominant ?
Q4. Avec l'equation (3.3) de Friedrich (a lire et a verifier toi-meme), que vaut nabla Omega . nabla Omega sur scri en presence de matiere de Dirac dans ce poids ? L'exposant de Fuchs du spineur est-il constant le long de scri ?
Q5. Systeme couple Einstein-lambda-Dirac, perturbatif autour de de Sitter : prends un champ de Dirac d'ordre epsilon forme d'au moins deux modes de vecteurs d'onde non colineaires, avec les deux exposants de Fuchs presents. Calcule independamment la reponse metrique d'ordre epsilon^2 dans au moins un secteur de Fourier non nul et le secteur homogene, dans une jauge de ton choix que tu fixes et justifies, sous forme de developpements en puissances Omega^{n + i j mu} (j entier) jusqu'a un ordre >= 5. Questions : y a-t-il des poles, des logarithmes (resonances) ? A quel ordre minimal apparaissent les termes oscillants (j non nul) ? Le lapse est-il nul a scri ? Puis la source d'ordre epsilon^3 de l'equation du spineur : contient-elle un terme Omega^{-1 + i j mu}, j = +-1, dont la projection sur le sous-espace propre correspondant est non nulle (resonance, donc ln Omega dans le spineur) ?
Q6. Meme question pour la classe « a un seul exposant » (a la limite, seulement Omega^{+i mu}) : la geometrie est-elle en series entieres et la classe stable a l'ordre epsilon^3 ?
Q7. Argument a tous les ordres : sous quelles hypotheses peut-on conclure qu'aucun logarithme n'apparait a aucun ordre, et que la classe a un seul exposant est stable ? Sois explicite sur ce qui est prouve et ce qui est suppose.

Classe tes conclusions : etabli (par calcul), plausible, refute. Indique pour chaque signe la sortie de script qui le fixe.
