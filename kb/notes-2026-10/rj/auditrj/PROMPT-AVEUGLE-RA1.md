# Consigne RA-1 (audit RJ, cecite stricte)

Tu es un auditeur isole. Tu n'as que cette consigne. N'ouvre aucun fichier de /home/claude hors de /home/claude/RJ/auditrj/work_ra1/ (ton dossier de travail). Ecris ton rapport dans /home/claude/RJ/auditrj/RAPPORT-RA1.md, en francais, sans tiret long. Fais tes calculs par scripts (Python, sympy, numpy, scipy) et conserve-les dans ton dossier.

## Cadre
Equations conformes de Friedrich (arXiv:1601.04506, eq. (3.7) ; arXiv:1311.0700) : g = Omega^2 g-hat, g-hat metrique physique, g metrique conforme. L'equation du Weyl rescale W = Omega^{-1} C[g] s'ecrit
  nabla_i W^i_{jkl} = 2 Omega^{-1} nabla-hat_{[k} L-hat_{l]j},
avec L-hat le tenseur de Schouten physique. Avec les equations d'Einstein (kappa = 1, constante cosmologique lambda), L-hat_ab = (1/2)(T-hat_ab - (1/3) T-hat g-hat_ab) + (lambda/6) g-hat_ab, T-hat = g-hat^{ab} T-hat_ab. Convention de signature (-,+,+,+). On note n_a = d_a Omega (indice **bas**), et n^a = g^{ab} n_b.
On rescale la matiere avec le poids « poussiere » de Friedrich : dans un repere g-orthonormal e_j et le repere g-hat-orthonormal e-hat_j = Omega e_j, tau_jk = Omega^{-3} T-hat(e-hat_j, e-hat_k). (Pour une poussiere T-hat = rho-hat U-hat U-hat, cela donne tau = rho U U avec rho = Omega^{-3} rho-hat.)

## Questions
- Q1. Calculer, pour un T-hat symetrique **quelconque**, la partie de 2 Omega^{-1} nabla-hat_{[k} L-hat_{l]j} proportionnelle a Omega^{-1} (sans derivee de tau) en fonction de tau et n, et la partie restante. Verifier ton resultat par un calcul exact independant (par exemple g = Minkowski, Omega et T-hat explicites).
- Q2. Pour n de genre temps, quel est l'ensemble des tau qui annulent cette partie singuliere ? Interpreter.
- Q3. Champ de Dirac test sur de Sitter (carte plate) : metrique physique a^2(-d eta^2 + dx^2), a = -1/(H eta), Omega = 1/a ; pour un mode de Fourier psi = a^{-3/2} u(eta) e^{i k.x}, i u' = (alpha.k + beta m a) u (representation de Dirac, beta = diag(1,1,-1,-1)). Calculer tau_00, tau_0a, tau_ab de ce mode (derive le tenseur d'energie-impulsion de Dirac toi-meme, verifie sa conservation), leur ordre en Omega quand Omega -> 0, et les composantes qui oscillent en exp(i c ln Omega) ; preciser c.
- Q4. Avec n = d Omega pour ce de Sitter, la partie singuliere de Q1 divisee par Omega a-t-elle une limite quand Omega -> 0 : (a) pour une solution generique, (b) pour une solution dont la limite chi0 (definie par u = exp(i beta (m/H) ln Omega) chi, chi -> chi0) n'a de composante que dans l'espace propre beta = +1, (c) pour k = 0 ? Donner les ordres (analytique), puis verifier numeriquement.
- Q5. Avec chi defini en Q4, ecrire l'equation verifiee par chi. Ses coefficients ont-ils une limite en Omega -> 0 ? Un autre choix de transformation unitaire dependant du temps, u = V(eta) chi, peut-il rendre les coefficients reguliers (serie entiere en Omega) pour tout k ? Argumenter.
- Q6. Conclusion : dans ce poids et cette jauge, reste-t-il des poles en 1/Omega dans l'equation du Weyl rescale pour le champ de Dirac test ? Quelle est l'obstruction residuelle a la regularite formelle (critere : seconds membres series entieres en Omega, sans ln Omega ni phase exp(i c ln Omega)) ?
