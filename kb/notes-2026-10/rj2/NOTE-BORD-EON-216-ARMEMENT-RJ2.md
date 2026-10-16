---
id: NOTE-BORD-EON-216-ARMEMENT-RJ2
numero: 216
serie: I
branche: Chantier D (chantier RJ, second etage)
reservation: 2026-10-16T16:37:05Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 216)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant tout calcul du second etage"
decision: "operateur (Thierry), 2026-10-16 18:29 Paris : « passe a l'execution de la question PSE et ensuite le second etage RJ »"
amont: "NOTE-207 v2 §5 et §7 (question ouverte : le couplage complet preserve-t-il la classe a un seul exposant ?) ; NOTE-210 §3 ; article v2.5 Rem. 2(4) (« the coupling could reintroduce poles ») ; NOTE-215"
precheck: "precheck/eq33_check.py et sortie (equation (3.3) de Friedrich 2016 recopiee et verifiee sur FLRW Lambda + poussiere, precedent xiv)"
---

# Gel RJ2 : le couplage Einstein-Dirac complet preserve-t-il la classe a un seul exposant ?

## 0. Etat de connaissance declare avant le gel
- **Acquis RJ (premier etage, ente NOTE-210)** : champ de Dirac test sur de Sitter, poids poussiere tau = Omega^{-3} T(e,e) (repere physique orthonorme) ; tau_00 = m B + Omega k.J, tau_0a et tau_ab d'ordre Omega pour toute solution ; identite P0 et noyau P1 (S = 0 si et seulement si tau est proportionnel a n n) ; forme de Fuchs du/dOmega = ((i m/H) beta / Omega + (i/H) alpha.k) u, exposants +- i m/H ; classe a un seul exposant : sources series entieres ; generique : bornees sans limite.
- **Friedrich 1601.04506** lu [§§ 2, 3, 4, 5 debut, 7 debut]. Equation (3.3) recopiee et verifiee (precheck) : 6 Omega s - 3 nabla Omega . nabla Omega - lambda = -(1/4) T-hat, d'ou nabla Omega . nabla Omega = -lambda/3 + O(Omega) a scri des que la trace de tau est bornee.
- **Analyse preliminaire faite de tete avant le gel (a verifier, rien n'est acquis)** :
  (a) dans le poids poussiere, tau = Omega T_c[psi_c ; g_c] (T_c tenseur cinetique du spineur conforme dans le repere conforme) : les seconds membres geometriques sont formellement reguliers, le seul coefficient singulier du systeme couple est le terme de masse de l'equation de Dirac ;
  (b) sur une solution de type Fuchs, la partie singuliere de T_c serait exactement (m/Omega)(psi-bar psi) nu nu, nu = n/\|n\|, dans un repere orthonorme quelconque ; elle est donc dans le noyau P1 ;
  (c) les termes croises entre sous-espaces propres de n-slash s'annuleraient dans psi-bar psi au premier ordre (orthogonalite pour l'adjoint de Dirac) ;
  (d) l'exposant mu = m/nu, nu = sqrt(lambda/3), serait constant sur scri par (3.3) ; une perturbation du lapse non nulle a scri changerait l'exposant et produirait des logarithmes seculaires en perturbation ; (3.3) l'interdit.
  Ces points sont des conjectures de travail ; FW-2 impose leur verification.

## 1. Questions figees
- **RJ2-1 (lemmes algebriques).** Verifier (a), (b), (c) symboliquement, repere et n quelconques (n de genre temps), S(tau) pour tau = (m psi-bar psi) nu nu.
- **RJ2-2 (cloture fuchsienne, tous ordres, au sens formel).** Pour le systeme couple Einstein-lambda-Dirac ecrit avec les inconnues conformes de Friedrich et le spineur conforme, dans une jauge ou e_0 est parallele a nabla Omega : la classe K = { sommes de Omega^{n + i j mu} c_{n,j}(x), n entier >= 0, j entier } est-elle stable (j pair pour la geometrie, j impair pour le spineur) ? Ou apparaissent les resonances (termes en ln Omega) ? La sous-classe a un seul exposant (spineur Omega^{i mu} fois serie entiere, geometrie serie entiere) est-elle stable ? A quel ordre minimal n apparaissent les termes oscillants (j non nul) de la geometrie ?
- **RJ2-3 (test explicite, perturbatif).** De Sitter + champ de Dirac d'ordre epsilon (deux modes de vecteurs d'onde non colineaires, coefficients c+- generiques, puis un seul exposant) ; reponse metrique d'ordre epsilon^2 dans les secteurs de Fourier q = k1 - k2 (scalaire en jauge longitudinale, vectoriel, tensoriel) et q = 0 (Friedmann) ; reponse du spineur d'ordre epsilon^3. Developpements formels dans la classe K jusqu'a un ordre fixe N >= 6, coefficients exacts (mu et k symboliques ou rationnels). Controles : equations d'Einstein redondantes (contrainte d'impulsion, trace spatiale) satisfaites ordre par ordre ; Phi et Psi nuls a scri (coherence avec (3.3)) ; absence ou presence de ln Omega et de puissances negatives ; ordre minimal des termes oscillants.
- **RJ2-4 (portee).** Consequence pour RG-4, pour la Rem. 2(4) de l'article v2.5 et pour le statut de la classe a un seul exposant.

## 2. Espace de verdicts
- **RJ2-V0** : non concluant (calcul inacheve, ou contradiction entre RJ2-2 et RJ2-3 non resolue).
- **RJ2-V1** : la classe a un seul exposant est preservee par le couplage (au sens formel et dans le test explicite) ; la classe generique reste sans pole ni logarithme, la geometrie y a une limite a scri avec des termes oscillants d'ordre n >= 1 (continue, pas C^1 en Omega).
- **RJ2-V2** : la classe a un seul exposant est preservee, mais la classe generique acquiert des logarithmes ou une geometrie sans limite (oscillation d'ordre 0).
- **RJ2-V3** : le couplage reintroduit des poles ou des logarithmes meme pour la classe a un seul exposant ; la classe exceptionnelle de RJ ne survit pas au couplage.

## 3. Prediction (informee, precedent ix)
**RJ2-V1.** Raisons : points (a) a (d) du §0. Point faible : la jauge (e_0 parallele a nabla Omega) peut ne pas etre compatible avec la forme d'evolution choisie dans le test explicite ; les resonances dependent de l'ordre auquel les termes oscillants entrent dans le coefficient du terme de masse (lapse) ; une erreur sur (d) donnerait RJ2-V2 ou RJ2-V3.

## 4. Firewall
- FW-1 : aucune lecture nouvelle de Friedrich au-dela du niveau declare ; si une equation de 1601.04506 autre que (3.3) est utilisee, elle est recopiee et verifiee par script avant usage (precedent xiv). La perturbation lineaire de la gravitation (jauge longitudinale, secteurs scalaire, vectoriel, tensoriel) et l'operateur de Dirac perturbe sont **derives symboliquement** depuis la metrique dans le script, non recopies.
- FW-2 : les lemmes (a) a (c) et la constance de mu sont prouves par script ou par calcul ecrit verifie, pas affirmes ; conventions fixees par ecrit avant calcul : signature (-,+,+,+), {gamma^a, gamma^b} = -2 eta^{ab}, beta = gamma^0, alpha_i = gamma^0 gamma^i, Omega = -H eta (H = 1 dans les scripts sauf mention), mu = m/H, n_a = nabla_a Omega (indice bas), nu = n/\|n\| ; les signes sont lus dans la sortie des scripts (precedent xv).
- FW-3 : critere : une quantite est reguliere si elle est serie entiere en Omega ; « bornee sans limite » si son developpement contient Omega^{i j mu}, j non nul, a l'ordre 0 ; « continue, pas C^1 » si les termes oscillants commencent a l'ordre 1 ; un ln Omega ou une puissance negative est une irregularite.
- FW-4 : RJ2-2 est un enonce formel (series), sans convergence, existence ni hyperbolicite ; RJ2-3 est perturbatif (ordre epsilon^3) sur de Sitter ; aucun enonce non lineaire global n'en est tire.
- FW-5 : execution scellee avec ses scripts et sorties ; audit froid par deux agents isoles (une derivation aveugle, une adverse) avant toute entee ; l'article v2.5 n'est pas modifie par ce chantier avant l'acte.

## 5. Non-surclassement
Rien de grave. RG-4 refutee a titre provisoire (raison reformulee par RJ) ; noyau {A4 ; A2★ ; N} inchange.
