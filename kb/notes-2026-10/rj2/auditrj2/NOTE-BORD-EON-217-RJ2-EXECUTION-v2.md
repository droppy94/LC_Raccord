---
id: NOTE-BORD-EON-217-RJ2-EXECUTION
numero: 217
serie: I
branche: Chantier D (chantier RJ, second etage)
reservation: 2026-10-16T16:37:05Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 217)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-216-ARMEMENT-RJ2.md sha256 4127534b32e0ae79 (sceau NOTE-216-SCEAU.txt, 2026-10-16T16:37:58Z)"
decision: "operateur (Thierry), 2026-10-16 18:29 Paris"
version: "v2 apres audit (NOTE-219, AU-V3 : erreur E1 sur la geometrie generique ; corrections E2, E3, C1 a C9). v1 conservee (sha256 9fdf5d619104418d), non entee."
scripts: "v1 : rj2_lemmes.py, rj2_series.py, rj2_ops.py, rj2_ops_check.py, rj2_lin_check.py, rj2_test.py (sorties run_*.txt) ; v2 : rj2_ops.py corrige (E2), rj2_test_v2.py (sorties v2runs/run_*.txt). Empreintes aux sceaux NOTE-217-SCEAU.txt et NOTE-217-v2-SCEAU.txt"
environnement: "Python 3.13.16, SymPy 1.14.0"
---

# Execution RJ2 (v2) : le couplage Einstein-Dirac complet et la classe a un seul exposant

## 0. Portee
Systeme couple Einstein-lambda-Dirac, poids poussiere de Friedrich. Deux niveaux (FW-4) : (i) un argument formel a tous les ordres, conditionnel (§2) ; (ii) un test perturbatif explicite autour de de Sitter jusqu'a l'ordre epsilon^3, dans deux jauges et pour deux jeux de vecteurs d'onde (§3), confirme independamment par l'auditeur RB-1 dans ses propres jauges (NOTE-219). Aucun enonce de convergence, d'existence ou de stabilite.

Conventions (FW-2), lues dans les sorties : signature (-,+,+,+) ; {gamma^a, gamma^b} = -2 eta^{ab} ; representation de Dirac ; T_ab = -(i/4)[psibar gamma_a nabla_b psi + (a<->b) - h.c.] (signe fixe par T_00 = +m psi^dag psi au repos) ; nabla_mu psi = d_mu psi - (1/4) omega_{mu ab} gamma^a gamma^b psi (coefficient fixe par nabla gamma = 0) ; Omega = -H eta, H = 1, lambda = 3, kappa = 1 ; mu = m/H ; n_a = nabla_a Omega.

## 1. RJ2-1 : lemmes algebriques (rj2_lemmes.py ; confirmes independamment par RB-1)
- **(a) Poids.** Pour un facteur conforme Omega(x) quelconque : Omega^{-3} T_phys(e,e) = Omega T_c(e_c,e_c), 10 composantes (tenseur pris sur couche, donc cinetique, sans terme de masse explicite).
- **(b) Partie singuliere.** Sur une solution de type Fuchs (nabla_b psi = (n_b/Omega) K psi + regulier), K = -i m nslash/\|n\|^2 = i m nslash/(n.n), valeurs propres +- i m/\|n\| ; la partie d'ordre 1/Omega du tenseur vaut exactement (m/Omega)(psibar psi) n_a n_b/\|n\|^2, pour n de genre temps et un repere orthonorme quelconques.
- **(c) Termes croises.** P+ P- = 0, P+- auto-adjoints pour l'adjoint de Dirac : psibar psi n'a pas de terme croise entre les deux exposants a l'ordre dominant (psibar gamma psi en a : T_c oscille des l'ordre Omega^0, tau des l'ordre Omega^1).
- **Noyau P1, n generique.** S(rho nu nu, n) = 0 pour tout n de genre temps.
- **Consequence.** tau = m (psibar psi) nu nu + Omega R, R borne ; S(tau)/Omega = S(R) borne. **Pour les seconds membres de matiere**, aucune relation regularisante n'est necessaire : l'equation de Dirac aligne d'elle-meme la partie singuliere sur n (chez Friedrich, l'alignement du flot de poussiere sur nabla Omega resulte du Lemme 4.1 et de la jauge conforme). Ce point ne dit rien de la partie geometrique du systeme, couverte par l'hypothese H2 ci-dessous.
- **Signe.** rho = m psibar psi n'a pas de signe fixe en general (psibar psi = \|P+ psi\|^2 - \|P- psi\|^2) ; il est positif dans la classe a un seul exposant +i mu, seule classe ou l'hypothese rho-hat >= 0 de Friedrich est automatique (RB-1).

## 2. RJ2-2 : argument formel a tous les ordres (conditionnel)
**Hypotheses.**
- (H1) Coordonnees (Omega, x^alpha) pres de scri, e_0 parallele a nabla Omega (possible : nabla Omega est de genre temps pres de scri par (3.3)).
- (H2) **Hypothese nouvelle, non demontree, distincte de la situation de Friedrich** (qui utilise une jauge comobile e_0 = U, R prescrit, des geodesiques conformes, la relation (4.16) et une seconde regularisation) : dans la jauge (H1) completee par un choix de jauge conforme, la partie geometrique des equations conformes dans le poids poussiere se resout ordre par ordre en Omega a partir de donnees sur scri, sans obstruction logarithmique dans le vide (cf. RB-1, S1) ; aucune convergence (S2).

**Etapes.**
1. Par (3.3) (trace physique T-hat = Omega^3 tr tau), nabla Omega . nabla Omega = -lambda/3 + O(Omega) sur scri des que Omega s -> 0 ; l'exposant mu = m/nu, nu = sqrt(lambda/3), est **constant sur scri**. (3.3) ne fixe que la composante g_c^{00} : elle protege le **lapse** (Phi(0) = 0), seul canal de resonance a l'ordre epsilon^3 (§3) ; Psi(0) = 0 vient des contraintes d'Einstein, pas de (3.3).
2. Equation de Dirac de Fuchs : (n + i rho - A_0) psi_{n,rho} = (termes d'ordre < n), inversible pour n >= 1 ; pour n = 0, aucun terme force si le lapse et le decalage prennent leur valeur de de Sitter sur scri (etape 1 pour le lapse ; choix de coordonnees H1, x^alpha transportes le long de nabla Omega, pour le decalage ; un decalage d'ordre 0 ne resonne d'ailleurs pas a epsilon^3, RB-1 et RB-2). **Pas de logarithme dans le spineur.**
3. Sources geometriques : tau = (j = 0, ordre 0) + (oscillant, ordre >= 1) ; S/Omega et nabla tau' bornes. Sous (H2), pas de logarithme ni de pole d'origine materielle. **L'ordre auquel les oscillations entrent dans les inconnues geometriques depend du facteur conforme** : une inconnue fixee par une contrainte plutot que par une evolution (L_00, donne par (3.5) via d_Omega s) peut perdre un ordre. (La v1 affirmait a tort que toutes les inconnues s'obtiennent par integration ; erreur E1, NOTE-219.)
4. Classe a un seul exposant : bilineaires en j = 0 seulement ; aucune oscillation nulle part ; produits geometrie x spineur restent en rho = mu. **Stable**, quelle que soit la jauge conforme.

**Conclusion formelle (sous H1, H2).** Classe a un seul exposant preservee, sans logarithme. Classe generique : sans pole ni logarithme d'origine materielle ; la regularite des inconnues geometriques (limite ou non a scri) depend du choix du facteur conforme.

## 3. RJ2-3 : test perturbatif explicite (rj2_test.py v1, rj2_test_v2.py)
**Montage.** De Sitter (H = 1). Ordre epsilon : quatre modes +-k1, +-k2, coefficients c+- donnes, normes egales pour k et -k (impulsion totale nulle, exigee par la contrainte d'impulsion du secteur homogene ; verifiee). Deux jeux : « orth » k1 = (1,0,1), k2 = (1,0,-1) (v1 : orthogonaux, normes egales, coplanaires) ; « gen » k1 = (1,2,0), k2 = (0,1,3) (non orthogonaux, normes differentes). Ordre epsilon^2 : metrique physique a^2[eta + h], dix equations d'Einstein linearisees derivees de la metrique, imposees ensemble avec les conditions de jauge (leur compatibilite contient les equations redondantes). Deux jauges, Omega = -eta fixe dans les deux : **longitudinale** (Phi, Psi, S_i transverse, H_ij TT) et **B** (decalage nul, trace spatiale nulle, lapse libre ; celle de RB-1). Secteur homogene : Psi_0 = 0, S = 0. Ordre epsilon^3 : source F de l'equation du spineur (operateur de Dirac perturbe derive de la metrique), par couple (secteur, mode) et totale par vecteur d'onde cible. v2 : courbure de la metrique conforme (R, Schouten L, Weyl rescale W = C/Omega) par secteur ; controle positif.

**Controles des operateurs.** Fond de Sitter exact ; invariance de jauge de l'Einstein linearise ; covariance conforme et identite de diffeomorphisme (derivee de Kosmann, coefficient -1/4) de l'operateur de Dirac perturbe, fonctions generiques (ce controle determine entierement l'operateur au premier ordre et rejette un coefficient de spin faux, RB-2) ; controle RJ tau_00(q=0) = mu B + Omega k.J. Le co-repere inverse de la fonction complete dirac_op est corrige (E2, sans incidence : effet nul au premier ordre sur fond plat, et fonction non utilisee par le test).

**Controle positif (v2).** Un lapse Phi(0) = 1 injecte a scri est detecte comme resonance (j = +-1 en generique, j = +1 en un seul exposant) dans les six executions : le detecteur fonctionne.

**Resultats.**

| Quantite | Jauge longitudinale | Jauge B |
|---|---|---|
| Resonances (systemes epsilon^2 incompatibles) | aucune | aucune |
| Lapse a scri | Phi(0) = 0 | Phi(0) = 0 (Phi en Omega^3) |
| Potentiels metriques, generique : premiers termes oscillants | Phi, Psi : Omega^{2 +- 2 i mu} ; S : Omega^3 ; H : Omega^4 | toutes composantes : Omega^{4 +- 2 i mu} |
| R[g_c], generique | **oscille a l'ordre 0 : pas de limite** | oscille a partir de l'ordre 4 |
| Schouten L, generique | **oscille a l'ordre 0 (L_00) : pas de limite** | oscille a partir de l'ordre 2 |
| Weyl rescale W, generique | limite ; oscille a partir de l'ordre 1 | idem |
| Un seul exposant | aucun terme oscillant (metrique, R, L, W) | idem |
| Source du spineur epsilon^3 (par couple et totale par cible) | 0 resonance, aucune puissance < -1 | idem |

Solutions homogenes de la classe j = 0 : 4 par secteur q non nul (2 polarisations x exposants 0 et 3) et 10 dans le secteur homogene (5 composantes de cisaillement x exposants 0 et 3) ; les parametres libres des classes j non nul n'atteignent aucun coefficient d'ordre <= 6 (artefacts de troncature). Avec ces donnees libres mises a 1 (v1), bilan inchange. **Correction E3** : le terme Omega^3 de H_ij est l'exposant homogene TT, pas une reponse particuliere ; la reponse forcee commence a Omega^4 (generique) ou Omega^5 (un seul exposant).

**Lecture.** (1) Le seul canal de resonance a epsilon^3 est le lapse sur scri ; il est nul. (2) L'ecart entre les deux jauges est un changement de facteur conforme : a Omega fixe comme fonction de coordonnee, une transformation de composante xi^eta d'ordre Omega^{3 +- 2 i mu} change le facteur conforme par theta = 1 + O(Omega^{2 +- 2 i mu}), dont le hessien deplace l'oscillation d'ordre 0 de L. W, conformement invariant a theta pres, oscille a partir de l'ordre 1 dans les deux. (3) Le point faible annonce au gel (compatibilite de la jauge H1 avec la forme du test, C5) se resout ainsi : pour l'equation de Dirac, l'ecart a H1 est d'ordre O(S) = O(Omega^2) ; pour la geometrie, c'est le choix du facteur conforme qui compte (point 2). (4) Diversite reelle des tests (C6) : la structure de resonance ne depend pas de mu reel non nul (13/10 et 7/3 donnent la meme structure) ; le jeu « gen » leve la specialite du jeu « orth » ; les secteurs +-2k ne portent structurellement que j = 0 (aucune oscillation) ; les calculs de courbure sont faits avec des donnees libres nulles et une seule valeur de mu. En jauge B, sept parametres libres (au lieu de quatre) atteignent les ordres <= 6 dans les secteurs q non nuls : la jauge B garde une liberte residuelle reguliere (RB-1).

## 4. Verdicts (v2)
- **RJ2-1** : confirme (deux derivations independantes).
- **RJ2-2** : conditionnel (H1, H2) ; classe a un seul exposant stable ; classe generique sans pole ni logarithme d'origine materielle, regularite geometrique dependant du facteur conforme.
- **RJ2-3** : a epsilon^3 sur de Sitter, deux jauges, deux jeux de vecteurs d'onde, confirme par RB-1 dans ses jauges.
- **Global : RJ2-V1 restreint.** (i) La classe a un seul exposant est preservee par le couplage : formellement sous H1 et H2, et perturbativement a epsilon^3 (etabli par deux calculs independants). (ii) Classe generique : sans pole ni logarithme a epsilon^3 ; W continu, pas C^1 ; la metrique conforme oscille a partir de Omega^2 (jauge longitudinale : C^1, pas C^2) ou de Omega^4 (jauge B) ; le Schouten et la courbure scalaire conformes n'ont pas de limite dans la jauge longitudinale et en ont une dans la jauge B : **il existe, a l'ordre epsilon^2, un facteur conforme ou toute la geometrie a une limite**, mais la regularite depend de ce choix. La prediction RJ2-V1 n'est donc realisee que sous cette forme restreinte.

## 5. Portee (RJ2-4)
- **Classe a un seul exposant** : au sens formel et dans le test, le couplage la preserve ; la geometrie y est en series entieres, comme pour la poussiere de Friedrich, sans relation regularisante pour les seconds membres de matiere. Le spineur garde le facteur Omega^{i mu} : l'equation de matiere reste fuchsienne, donc le systeme n'est pas regulier au sens strict de Friedrich (RB-1, S3).
- **RG-4** : la refutation provisoire porte sur : (1) le spineur sans limite a scri pour toute masse constante non nulle, dans toute classe ; (2) pour une matiere generique, une geometrie dont la regularite a scri depend du facteur conforme : W continu non C^1, metrique conforme et Schouten plus ou moins reguliers selon le facteur conforme (Schouten sans limite en jauge longitudinale, avec limite en jauge B). Or le choix du facteur conforme a scri est precisement ce que fixe une regle de raccord en CCC : la question de la classe generique devient une question sur la regle elle-meme. Une regle qui n'exige la regularite que de la geometrie, avec un facteur conforme adapte, admet la classe a un seul exposant sans restriction et, a l'ordre calcule, la classe generique avec une geometrie continue a derivees bornees ; une regle qui exige un prolongement du spineur n'en admet aucune.
- **Article v2.5, Rem. 2(4)** : texte propose pour une v2.6, apres acte (reformule selon RB-3, K1) : « In a perturbative expansion of the coupled system about de Sitter space, to third order in the amplitude and for four Dirac modes, the coupling does not reintroduce poles or logarithms; the single-exponent class is preserved, with power-series geometry; for generic solutions the rescaled Weyl tensor has a limit at scri, while the limits of the Schouten tensor and scalar curvature of the conformal metric depend on the choice of conformal factor. A formal all-order version rests on an unproven solvability assumption. »
- **Ce qui n'est pas fait** : (H2) ; convergence ; existence non lineaire (dans la classe generique, tau n'est pas C^1 a scri, et le theoreme lisse de Friedrich ne s'applique pas tel quel) ; ordres epsilon^4 et au-dela (seul le lapse y est protege par une identite exacte, (3.3)) ; reponse psi_3 non construite (le critere a n = 0 suffit pour l'absence de logarithme a cet ordre) ; FLRW non de Sitter ; jauge conforme de Friedrich (R prescrit) non testee.

## 6. Erreurs consignees (precedent ix)
- v1, E1 : affirmation fausse sur la limite de la geometrie generique (etape 3 supposait une equation d'evolution pour toute inconnue).
- v1, E2 : co-repere inverse de dirac_op (sans incidence).
- v1, E3 : exposant homogene TT pris pour une reponse particuliere.
- v1 : H2 presentee a tort comme le cas formel de Friedrich ; Psi(0) = 0 attribue a tort a (3.3) ; diversite des tests surestimee.
- Travail : connexion de spin ecrite de tete au premier jet du lemme (a) ; rapport trompeur des parametres libres ; derivee de Lie spinorielle incomplete au premier controle de diffeomorphisme ; derivation symbolique generale trop lente remplacee par la forme lineaire directe.

## 7. Non-surclassement
Calcul et audit par IA, non relus par un humain. Formel (conditionnel) et perturbatif (epsilon^3, de Sitter). RG-4 refutee a titre provisoire, raison resserree (§5) ; noyau {A4 ; A2★ ; N} inchange.
