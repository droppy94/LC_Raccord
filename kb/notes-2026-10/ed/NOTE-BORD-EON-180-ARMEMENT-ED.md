---
id: NOTE-BORD-EON-180-ARMEMENT-ED
numero: 180
serie: I
branche: Chantier D (systeme Einstein-Dirac couple, sens de Friedrich ; chantier ED)
reservation: 2026-10-15 (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 180)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant tout calcul : regularite formelle du systeme conforme de Friedrich couple a un champ de Dirac massif"
decision: "operateur (Thierry), 2026-10-15 17:26 heure de Paris : « ok pour executer "Traiter le systeme Einstein-Dirac couple au sens de Friedrich." »"
---

# Gel ED : le systeme Einstein-Dirac couple au sens de Friedrich

## 0. Objet
Le theoreme 3.1 de Friedrich (1311.0700) etablit, pour le systeme couple Einstein-scalaire massif ecrit en inconnues rescalees, que les seconds membres sont formellement reguliers (pas de Omega^-k, fonctions lisses des inconnues) si et seulement si m^2 = 2 lambda/3. Le corpus a etabli (S26-02 v3 §8, article v2.2 Remarque) que l'equation de Dirac rescalee porte le coefficient m/Omega pour toute masse constante non nulle ; les equations geometriques (2.13)-(2.17) avec source de Dirac n'ont pas ete traitees (NOTE-179 §3).

## 1. Questions figees
- **ED-0 (conventions).** Inconnues : celles de Friedrich (e, Gamma, Omega, s, L, W) et psi_hat = Omega^{-3/2} psi (poids conforme standard), avec ses derivees. Forme du tenseur d'energie-impulsion de Dirac : forme cinetique symetrisee (sans terme lagrangien) et forme avec le terme - g L ; les deux coincident sur couche.
- **ED-1 (covariance).** Le tenseur cinetique symetrise de Dirac satisfait-il, comme identite algebrique hors couche en (psi_hat, derivees premieres), T_ab[psi ; g_hat] = Omega^2 T_ab[psi_hat ; g] (indices bas) ? Verification symbolique obligatoire.
- **ED-2 (equations geometriques).** Avec T sous forme cinetique, les seconds membres de (2.13), (2.14), (2.15), (2.16), (2.17) sont-ils formellement reguliers en fonction des inconnues (psi_hat et ses derivees comprises), pour toute masse ? Ou apparaissent-ils des termes Omega^-k (comme le terme m^2 phi^2 g_hat le fait pour le scalaire) ?
- **ED-3 (dependance a la representation).** Avec T sous forme « cinetique - g L », quels termes singuliers apparaissent, et sont-ils des multiples de l'equation de Dirac (donc la meme singularite que celle de l'equation de matiere) ?
- **ED-4 (bilan).** Ou se trouve la singularite du systeme couple, et existe-t-il une masse speciale ou un couplage (classe du Lemme 2 de l'article) qui la retire sans annuler la masse effective ?

## 2. Espace de verdicts
- **ED-V0** : non concluant (identite ED-1 non verifiee, ou dependance a la representation non resolue).
- **ED-V1** : la singularite du systeme couple est confinee a l'equation de matiere (coefficient m/Omega et ses derivees) ; les equations geometriques sont formellement regulieres en representation cinetique ; pas de masse speciale.
- **ED-V2** : les equations geometriques portent en plus des termes singuliers proportionnels a m, non reductibles a l'equation de matiere (obstruction plus forte).
- **ED-V3** : une masse speciale ou un couplage de la classe rend le systeme couple formellement regulier a masse effective non nulle (contredirait l'article v2.2 ; revision obligatoire).

## 3. Prediction (informee, precedent ix)
**ED-V1.** Motif, ecrit avant tout calcul : le tenseur cinetique ne contient pas m explicitement et devrait etre conformement covariant (poids Omega^2) ; L_hat serait alors Omega^2 fois une fonction reguliere, et 2 Omega^-1 nabla_hat_[nu L_hat_lambda] rho serait regulier. La masse n'entrerait que par l'equation de matiere. A l'inverse du scalaire, dont T contient m^2 phi^2 g_hat = m^2 psi^2 g (ordre 1), ce qui produit les termes (m^2 - 2 lambda/3) Omega^-1. Pour ED-3 : termes en m Omega^-1 qui sont des multiples de l'equation de Dirac. Incertitude : la covariance hors couche (ED-1) peut echouer a cause de la connexion de spin ; c'est le point a verifier.

## 4. Firewall
- FW-1 : regularite **formelle** (seconds membres comme fonctions des inconnues), jamais une valeur sur une solution (precedent xii).
- FW-2 : toute identite utilisee est verifiee symboliquement (script scelle avec sa sortie) ; la convention de connexion de spin est fixee en verifiant d'abord la covariance conforme de l'operateur de Dirac sans masse.
- FW-3 : calibration : le meme calcul applique au scalaire massif doit faire apparaitre le terme en m^2 phi^2 g_hat responsable des termes de Friedrich (controle de coherence, pas une reproduction complete du theoreme 3.1).
- FW-4 : audit froid aveugle avant toute greffe (precedent x).
- FW-5 : pas de modification de l'article ni de S26-02 dans ce chantier ; propositions seulement.

## 5. Non-surclassement
Rien de grave. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
