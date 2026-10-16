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
scripts: "rj2_lemmes.py, rj2_series.py, rj2_ops.py, rj2_ops_check.py, rj2_lin_check.py, rj2_test.py ; sorties rj2_lemmes_sortie.txt, rj2_ops_check_sortie.txt, rj2_lin_check_sortie.txt, run_*.txt (empreintes au sceau NOTE-217-SCEAU.txt)"
environnement: "Python 3.13.16, SymPy 1.14.0"
---

# Execution RJ2 : le couplage Einstein-Dirac complet et la classe a un seul exposant

## 0. Portee
Systeme couple Einstein-lambda-Dirac, poids poussiere de Friedrich. Deux niveaux, conformement a FW-4 : (i) un argument formel a tous les ordres (series dans la classe K), sous deux hypotheses explicites (§2) ; (ii) un test perturbatif explicite autour de de Sitter jusqu'a l'ordre epsilon^3 (§3). Aucun enonce de convergence, d'existence ou de stabilite.

Conventions (FW-2), lues dans les sorties : signature (-,+,+,+) ; {gamma^a, gamma^b} = -2 eta^{ab} ; representation de Dirac ; T_ab = -(i/4)[psibar gamma_a nabla_b psi + (a<->b) - h.c.] (le signe -1 est celui qui donne T_00 = +m psi^dag psi pour une particule au repos) ; nabla_mu psi = d_mu psi - (1/4) omega_{mu ab} gamma^a gamma^b psi (coefficient -1/4 impose par nabla gamma = 0) ; Omega = -H eta, H = 1, lambda = 3, kappa = 1 ; mu = m/H ; n_a = nabla_a Omega.

## 1. RJ2-1 : lemmes algebriques (rj2_lemmes.py, tous verifies exactement)
- **(a) Poids.** Pour un facteur conforme Omega(x) **quelconque** (quatre variables), g = Omega^{-2} eta, psi = Omega^{3/2} psi_c, connexion de spin calculee depuis le vierbein : Omega^{-3} T_phys(e,e) = Omega T_c(e_c,e_c), 10 composantes. Le tenseur cinetique ne contient pas la masse ; dans le poids poussiere, les sources geometriques sont donc **Omega fois** un bilineaire cinetique du spineur conforme, formellement regulieres comme fonctions des jets.
- **(b) Partie singuliere.** Si, sur une solution de type Fuchs, nabla_b psi = (n_b/Omega) K psi + (regulier), l'equation impose K = -i m nslash/\|n\|^2 (verifie : i nslash K = m), et la partie singuliere du tenseur est exactement
  T_sing,ab = (m/Omega) (psibar psi) n_a n_b / \|n\|^2,
  pour n de genre temps **quelconque** et un repere orthonorme quelconque (10 composantes, spineur generique). Valeurs propres de K : +- i m/\|n\|, d'ou les exposants +- i mu avec mu = m/\|n\|.
- **(c) Termes croises.** Les projecteurs P+- = (1 +- nslash/\|n\|)/2 verifient P+ P- = 0 et sont auto-adjoints pour l'adjoint de Dirac ; donc (P+ psi)bar (P- phi) = 0 : psibar psi n'a pas de terme croise entre les deux exposants a l'ordre dominant.
- **Noyau P1, n generique.** S(rho nu nu, n) = 0 pour tout n de genre temps (et non seulement dans le repere de n).
- **Consequence.** Sur une solution de type Fuchs, tau = m (psibar psi) nu nu + Omega R, avec R borne : la partie d'ordre 0 de tau est dans le noyau de S, quel que soit le repere ; S(tau)/Omega = S(R) est borne. **Aucune relation regularisante n'est necessaire** : contrairement a la poussiere de Friedrich, ou l'alignement du flot U sur nabla Omega doit etre impose par une jauge, ici l'equation de Dirac aligne d'elle-meme la partie singuliere sur n.

## 2. RJ2-2 : cloture fuchsienne a tous les ordres (argument formel)
**Hypotheses.** (H1) Jauge : coordonnees (Omega, x^alpha) au voisinage de scri, e_0 parallele a nabla Omega (possible car nabla Omega est de genre temps pres de scri, par (3.3)). (H2) Dans cette jauge, la partie geometrique des equations conformes de Friedrich, ecrite dans le poids poussiere, se resout ordre par ordre en Omega a partir de donnees sur scri (scri non caracteristique ; contraintes propagees), avec des coefficients reguliers : c'est le cas formel de la situation de Friedrich pour la poussiere ; (H2) n'est **pas** demontree ici.

**Classe K.** Spineur : sommes de Omega^{n + i rho} psi_{n,rho}(x), n >= 0, rho dans mu(2Z+1) ; geometrie : Omega^{n + 2 i j mu} G_{n,j}(x), j entier.

**Etapes.**
1. Par (3.3), nabla Omega . nabla Omega = -lambda/3 + O(Omega) des que s et tau sont bornes (le second membre de (3.3) est T-hat = Omega^3 tr tau) ; donc \|n\| = nu + O(Omega), nu = sqrt(lambda/3), dans **toute** la classe K. L'exposant mu = m/nu est **constant sur scri** : pas de ln Omega par derivation spatiale de Omega^{i mu}.
2. L'equation de Dirac prend la forme de Fuchs Omega d_Omega psi = A_0 psi + Omega B[psi, d_x psi ; G], avec A_0 constant de valeurs propres +- i mu, et A - A_0 = O(Omega) (etape 1). Recurrence : (n + i rho - A_0) psi_{n,rho} = (termes d'ordre < n). Pour n >= 1 l'operateur est inversible (valeurs propres n + i(rho -+ mu), jamais nulles). Pour n = 0, aucun terme force (toutes les corrections portent un facteur Omega) : seuls rho = +- mu sont presents, dans les sous-espaces propres de A_0. **Aucun logarithme dans le spineur, a aucun ordre.**
3. Sources geometriques sur la serie : par §1, tau = m (psibar psi) nu nu + Omega R. Par (c), les termes oscillants (j non nul) de psibar psi commencent a l'ordre 1 ; ceux de Omega R aussi. Donc tau = (j = 0, ordre 0) + (oscillant, ordre >= 1) ; S/Omega = S(R) et nabla tau' sont bornes (ordre >= 0, oscillants a l'ordre 0 au plus). Sous (H2), le systeme geometrique est regulier : G_{n+1} est obtenu en divisant par (n + 1 + 2 i j mu), jamais nul. **Pas de logarithme, pas de pole ; termes oscillants de la geometrie a l'ordre n >= 1** (W, et les variables qui s'en deduisent par integration).
4. Classe a un seul exposant (rho = mu seulement) : bilineaires en j = 0 seulement ; geometrie en series entieres ; produits geometrie x spineur restent en rho = mu. **La classe est stable.**

**Conclusion formelle (sous H1, H2).** La classe a un seul exposant est preservee par le couplage ; la classe generique reste dans K, sans pole ni logarithme ; la geometrie a une limite a scri, ses termes oscillants commencent a l'ordre 1 (le Weyl rescale est continu, de derivee bornee sans limite : pas C^1 en Omega). Le spineur lui-meme garde le point singulier regulier : pas de limite (phase Omega^{+- i mu}).

## 3. RJ2-3 : test perturbatif explicite (rj2_test.py)
**Montage.** De Sitter (H = 1). Ordre epsilon : quatre modes de Dirac de vecteurs d'onde +-k1, +-k2, k1 = (1,0,1), k2 = (1,0,-1) (non colineaires), coefficients c+- donnes, normes egales pour k et -k (impulsion totale nulle, exigee par la contrainte d'impulsion du secteur homogene ; verifiee : T_c,0a(q=0) = 0). Ordre epsilon^2 : metrique physique a^2[eta + h], h en jauge longitudinale (Phi, Psi, S_i transverse, H_ij transverse sans trace) dans chacun des neuf secteurs de Fourier q = k - k' ; secteur q = 0 avec Psi_0 = 0 (Omega = 1/a exactement), S = 0, Phi_0 et cisaillement H_ij sans trace. Les dix equations d'Einstein linearisees, **derivees symboliquement** de la metrique (rj2_ops.py), sont imposees ensemble avec les conditions de jauge ; leur compatibilite contient les equations redondantes (conservation). Ordre epsilon^3 : source F de l'equation du spineur dans la metrique perturbee (operateur de Dirac perturbe derive symboliquement), pour les 36 couples (secteur, mode) ; une resonance serait un terme Omega^{-1 + i j mu}, j = +-1, de projection non nulle sur le sous-espace propre beta = j.

**Controles des operateurs** (rj2_ops_check.py, rj2_lin_check.py) : fond de Sitter exact ; invariance de jauge de l'Einstein linearise (perturbation L_xi g_b, xi generique, 10 composantes nulles) ; covariance conforme de l'operateur de Dirac perturbe ; identite exacte de diffeomorphisme delta D chi = L_xi(D_0 chi) - D_0(L_xi chi) avec la derivee de Kosmann (coefficient -1/4, pas de terme en div xi) ; forme lineaire directe (celle qu'utilise le test) controlee par les deux identites precedentes avec fonctions generiques, et egale a la derivee de la forme complete sur un h de degre 1 (rj2_lin_check_sortie.txt). Controle RJ reproduit : tau_00(q=0) = mu B + Omega k.J.

**Resultats** (cinq executions : mu = 13/10 et 7/3, cas generique ; mu = 13/10, un seul exposant ; donnees homogenes nulles ou egales a 1) :

| Quantite | Generique | Un seul exposant |
|---|---|---|
| Systemes lineaires (9 secteurs x classes j) | tous compatibles : **aucune resonance** | idem |
| Phi, Psi (secteurs q non nul) | ordre min 1 (Phi(0) = Psi(0) = 0, coherent avec (3.3)) ; oscillants a partir de l'ordre **2** | ordre min 1 ; **aucun terme oscillant** |
| S_i | ordre min 2 ; oscillants a partir de 3 | ordre min 2 ; aucun |
| H_ij TT | ordre min 3 (particulier) ; oscillants a partir de 4 | aucun oscillant |
| Secteur homogene | Phi_0 a partir de Omega^3 (Friedmann), cisaillement oscillant a partir de 4 | Phi_0 en Omega^3, Omega^5 ; aucun oscillant |
| Solutions homogenes (j = 0) | 4 par secteur q non nul (2 polarisations x exposants 0 et 3), 10 dans le secteur homogene (5 composantes de cisaillement x exposants 0 et 3) : compte physique exact | idem |
| Parametres libres des classes j non nul | n'atteignent **aucun** coefficient d'ordre <= 6 (artefacts de troncature) | sans objet |
| Source F du spineur (36 couples) | commence a Omega^0 au plus bas ; **0 resonance**, aucune puissance < -1 | idem |

Avec des donnees homogenes non nulles (ondes gravitationnelles libres et cisaillement d'amplitude 1 a l'ordre epsilon^2), le bilan est inchange.

**Lecture.** Le terme le plus dangereux est le lapse Phi devant le terme de masse : une valeur Phi(0) non nulle changerait l'exposant et creerait des logarithmes seculaires. Le test donne Phi(0) = 0 dans tous les secteurs, comme l'impose (3.3). Les termes oscillants n'entrent dans la source du spineur qu'a l'ordre >= 1 : la recurrence de Fuchs ne rencontre jamais d'exposant propre.

## 4. Verdicts
- **RJ2-1** : (a), (b), (c) et le noyau, verifies ; la partie singuliere du tenseur de Dirac est exactement de type poussiere alignee sur n, dans tout repere.
- **RJ2-2** : sous (H1) et (H2), cloture formelle a tous les ordres, sans logarithme ; classe a un seul exposant stable ; geometrie generique continue, oscillante a partir de l'ordre 1.
- **RJ2-3** : confirme jusqu'a l'ordre 6 (geometrie) et 5 (source du spineur), sur 36 couplages, deux valeurs de mu, donnees homogenes nulles ou non.
- **Global : RJ2-V1, prediction realisee.**

## 5. Portee (RJ2-4)
- **Classe a un seul exposant** : ce n'est plus seulement une propriete d'un champ test. Au sens formel, et dans le test perturbatif, le couplage complet la preserve : la geometrie y est en series entieres a scri, comme pour la poussiere de Friedrich, et sans relation regularisante.
- **RG-4** : la refutation provisoire porte desormais sur deux points seulement. (1) Le spineur n'a pas de limite a scri (point singulier regulier, phase Omega^{+- i mu}) pour toute masse constante non nulle, quelle que soit la classe. (2) Pour une matiere generique (les deux exposants, k non nul), la geometrie est continue mais pas C^1 en Omega. Une regle de raccord qui n'exige la regularite que de la geometrie admet la classe a un seul exposant ; une regle qui exige un prolongement du spineur n'en admet aucune.
- **Article v2.5, Rem. 2(4)** : la phrase « the coupling could reintroduce poles » peut devenir, apres audit, « at the formal level (under stated gauge and solvability assumptions) and in a perturbative test to third order, the coupling does not reintroduce poles or logarithms; the single-exponent class is preserved ». A traiter dans une v2.6, pas avant l'acte.
- **Ce qui n'est pas fait** : (H2) non demontree (resolubilite formelle des equations conformes dans la jauge (Omega, x)) ; aucune convergence ; test limite a de Sitter, a l'ordre epsilon^3, a quatre modes ; FLRW non de Sitter couvert seulement par l'argument formel (etape 1 utilise lambda > 0).

## 6. Erreurs de travail consignees (precedent ix, transparence)
- Premier jet du lemme (a) avec une connexion de spin ecrite de tete : ecart ; remplacee par la connexion calculee depuis le vierbein, coefficient fixe par nabla gamma = 0.
- Rapport des parametres libres du premier passage trompeur (les variables libres choisies par le solveur etaient d'ordre eleve) : remplace par le decompte des parametres atteignant les ordres <= 6.
- Controle de diffeomorphisme d'abord ecrit avec une derivee de Lie spinorielle incomplete (partie symetrique de d xi incluse) : aucune solution ; correct avec la partie antisymetrique seule.
- Derivation symbolique generale de l'operateur de Dirac perturbe trop lente (fonctions generiques simplifiees) : remplacee par la forme lineaire directe, controlee contre la forme complete.

## 7. Non-surclassement
Calcul par IA, non relu par un humain, non audite a ce stade (FW-5). Formel et perturbatif. RG-4 refutee a titre provisoire, raison resserree (§5) ; noyau {A4 ; A2★ ; N} inchange.
