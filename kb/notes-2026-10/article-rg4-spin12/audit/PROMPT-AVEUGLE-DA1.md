# Consigne aveugle DA-1 (derivation en cecite stricte)

Tu es un physicien-mathematicien. Tu ne disposes d'aucun document : tu dois deriver toi-meme. Ecris un rapport en anglais ou en francais, avec les calculs, puis reponds explicitement a chaque question par une affirmation nette (vrai / faux / depend de ...), avec la justification.

## Cadre
Espace-temps de de Sitter, patch en expansion, coordonnees plates : g = -dt^2 + a(t)^2 dx^2, a = e^{Ht}, temps conforme eta = -1/(aH) in (-inf, 0). Metrique non physique g_hat = Omega^2 g avec Omega = 1/a = -H eta ; le bord futur scri+ est eta = 0. Champ de Dirac test psi de masse m (constante, sauf en Q4), equation (i gamma^mu nabla_mu - m) psi = 0 sur g. Champ rescale psi_hat = Omega^{-3/2} psi (poids conforme standard). Signature (-,+,+,+), representation de Dirac standard, beta = gamma^0.

## Questions
Q1. Pour un mode de Fourier psi_hat = e^{i k.x} u(eta), ecris l'equation de u. La norme u^dagger u est-elle conservee ? Pour m != 0, u(eta) a-t-il une limite quand eta -> 0^- ? Traite k = 0 et k != 0 (donne un argument de preuve pour k != 0, pas seulement une heuristique).

Q2. Couple le champ minimalement a un potentiel electromagnetique de jauge pure A = A_eta(eta) d eta (dependant de eta seulement). Une transformation de jauge psi_hat -> e^{-i lambda(eta)} psi_hat change A. (a) Existe-t-il, pour toute solution non nulle, une jauge dans laquelle psi_hat a une limite en scri+ ? (b) Si oui pour certaines solutions seulement, lesquelles, et quel est alors le comportement du potentiel transforme pres de eta = 0 (integrable ou non) ? (c) Ecris cette transformation dans le repere physique (temps t) : est-elle reguliere la ? (d) Existe-t-il une jauge ou psi_hat ET A sont tous deux continus en scri+ ?

Q3. Calcule la densite d'energie rescalee rho_hat = Omega^{-4} T_tt (T tenseur energie-impulsion symetrise du Dirac, sur couche) pour un mode, et donne son comportement quand eta -> 0^-. Est-elle invariante de jauge (couplage minimal) ? A quoi correspond physiquement le terme dominant ?

Q4. Remplace m par une masse dependant du temps m(t) >= 0 continue (scalaire multiplicatif). Donne des conditions necessaires et suffisantes sur m(t) pour que : (a) toute solution u converge en scri+ ; (b) la densite d'energie rescalee d'une solution de type particule (aux temps tardifs) reste bornee ; (c) le coefficient du terme de masse dans l'equation rescalee s'etende de facon lisse a Omega = 0. Ces conditions sont-elles ordonnees (l'une implique-t-elle l'autre) ? Donne un exemple qui separe (a) de (b).

Q5. En theorie quantique, soit omega un etat quasi-libre et omega_f l'etat a une particule obtenu en appliquant un operateur de creation lisse par un mode f. La difference omega_f(T_ab) - omega(T_ab) est-elle independante de la renormalisation ? Que vaut-elle ?

Q6. Sur de Sitter exact, un couplage local du Dirac a la geometrie (construit localement a partir de la metrique, d'ordre au plus un en derivees de psi) peut-il supprimer le comportement de Q1 tout en gardant une masse effective non nulle ? Justifie, et precise la classe de couplages que ton argument couvre.

Rends un rapport autoportant. Ne cherche pas a deviner une reponse attendue : un desaccord argumente est un resultat.
