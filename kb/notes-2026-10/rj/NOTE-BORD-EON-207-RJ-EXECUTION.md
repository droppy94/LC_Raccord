---
id: NOTE-BORD-EON-207-RJ-EXECUTION
numero: 207
serie: I
branche: Chantier D (chantier RJ : regularisation par jauge)
reservation: 2026-10-16T15:17:31Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 207)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-206-ARMEMENT-RJ.md sha256 44f184af4568e3ed (sceau NOTE-206-SCEAU.txt, 2026-10-16T15:18:01Z)"
decision: "operateur (Thierry), 2026-10-16 17:22 Paris : « ok, go pour executer la suite »"
script: "rj_check.py (sha256 6f2aae275fb256b6), sortie rj_check_sortie.txt (sha256 e0e0589b81772307)"
---

# Execution RJ

## 0. Portee
Champ de Dirac **test** sur de Sitter exact (carte plate, Omega = -H eta), tenseur injecte lineairement dans l'equation du Weyl rescale des equations conformes (FW-4, premier etage). Le couplage formel complet n'est pas calcule (§5).

## 1. RJ-1 : le mecanisme de Friedrich (arXiv:1601.04506, lu [§§ 2, 3, 4, 5 debut, 7 debut])
- Inconnues de matiere : U = Omega U-hat, rho = Omega^{-3} rho-hat (« poids poussiere »). Seuls deux seconds membres sont singuliers : l'equation du flot (3.21) et celle du Weyl rescale (3.20), ou le terme singulier est rho Z_jkl / Omega avec Z_jkl = d_[k Omega g_l]j + 2 d_[k Omega U_l] U_j + U_[k g_l]j U^q d_q Omega. Les deux n'ont de limite que si le gradient de Omega devient parallele a U a scri.
- Mecanisme (Lemme 4.1) : pour la poussiere, les geodesiques du flot sont, a reparametrage pres, des geodesiques conformes ; celles-ci sont des invariants conformes et traversent scri. D'ou la **relation regularisante** (4.16) : d Omega = -(d_U Omega + Omega <U,f>) U - Omega f, avec f regulier. En la reportant dans Z, (3.20) et (3.21) deviennent regulieres (4.17), (4.18). Hypotheses utilisees : T-hat = rho-hat U-hat U-hat, flot geodesique. En §5, une seconde regularisation (zeta_ab = (chi_ab - g_ab chi/3)/Omega, xi) donne un systeme symetrique hyperbolique valable des deux cotes de scri.

## 2. Identite generale (P0, exacte)
Pour un tenseur d'energie-impulsion **quelconque**, avec tau_jk = Omega^{-3} T-hat(e-hat_j, e-hat_k) (le poids poussiere de Friedrich), tau' = tau - (1/3) tr(tau) g, n = d Omega, kappa = 1 :

2 Omega^{-1} nabla-hat_[k L-hat_l]j = (1/2)(nabla_k tau'_lj - nabla_l tau'_kj) + Omega^{-1} S_jkl,
S_jkl = (1/2)[ 2(n_k tau'_lj - n_l tau'_kj) - g_kj n^m tau'_lm + g_lj n^m tau'_km ].

Verifiee par sympy, exactement, sur les 24 composantes (Omega et T-hat polynomiaux generiques, g de Minkowski) : 0 residu. Pour la poussiere alignee (tau = rho U U, U parallele a n), S = 0 (cas particulier de P1). La proportionnalite exacte entre S et le Z de Friedrich hors alignement n'est pas verifiee.

## 3. Noyau (P1)
Pour n de genre temps (n = -nu e0), S = 0 **si et seulement si** tau = tau_00 e0 e0 (rang 9 sur 10, noyau de dimension 1). Le terme singulier ne disparait donc que pour une matiere qui, a scri, se reduit a une densite au repos dans le repere de n : poussiere alignee. Toute composante tau_0a ou tau_ab d'ordre 1 laisse un pole ; d'ordre Omega, elle laisse un terme borne.

## 4. Champ de Dirac (P2, P3)
Tenseur de Dirac dans le poids poussiere (modes de Fourier, u spineur conforme, B = u-dagger beta u, N = u-dagger u, J_i = u-dagger alpha_i u ; conservation verifiee numeriquement, residu relatif 7e-9) :
- tau_00 = m B + Omega k.J ; **le terme de masse est sans 1/Omega** : dans le poids poussiere, la densite d'energie de Dirac est reguliere, de limite m(\|chi0+\|^2 - \|chi0-\|^2). Le « pole m/Omega » de la Prop. 3 de l'article est celui du poids radiatif Omega^{-4} ; il disparait dans le poids Omega^{-3} de Friedrich, comme pour la poussiere.
- tau_0a = Omega k_a N : d'ordre Omega, non oscillant ; S/Omega en recoit une contribution **reguliere** (constante k N), l'analogue de l'inclinaison reguliere f de Friedrich.
- tau_ab = (Omega/2)(k_a J_b + k_b J_a) ; J contient les interferences particule-antiparticule, J = 2 Re(e^{2i theta} chi-dagger_- sigma chi_+), theta = (m/H) ln Omega.

Resultats numeriques (m/H = 0.7, \|k\| = 1, integration DOP853 jusqu'a Omega = 1e-8) :

| Solution | S/Omega (max) | tau_ab/Omega | Comportement a scri |
|---|---|---|---|
| generique (chi0- non nul) | 0.40 + oscillation | 0.34 a 0.73, sans limite | **borne, sans limite** (amplitude d'oscillation 0.76 sur la derniere decade) |
| particule pure a la limite | 0.40 | decroit comme Omega (0.099 a Omega = 0.1, 1e-6 a 1e-8) | continu ; oscillation d'amplitude O(Omega) : C^0, pas C^1 |
| k = 0 (homogene) | 0 | 0 | **regulier** |

Aucun pole dans aucun cas : les poles en 1/Omega du chantier ED, dans ce terme, sont absorbes par le poids poussiere et le choix U = normale de Hubble.

Equation de matiere (P3) : avec chi = U0-dagger u, U0 = exp(i beta theta), le coefficient m/Omega disparait et devient alpha.k exp(2 i beta theta) (identite verifiee) : coefficient **borne, de module 1, sans limite** (phase lente en ln Omega). C'est le meme echange : un pole contre une phase log-periodique. Il porte sur le coefficient de l'equation, donc sur **toute** solution avec k non nul, quelle que soit sa limite.

## 5. Ce qui n'est pas fait
- Couplage formel complet Einstein-Dirac (jets, comme FW3) dans les inconnues chi et la jauge de Friedrich : non calcule. Il ne peut pas donner RJ-V1, puisque l'equation de matiere a deja des coefficients sans limite (P3) ; il dirait seulement si le couplage non lineaire reintroduit des poles.
- Espaces non homogenes (d_a Omega non nul) : la relation regularisante devrait controler d_a Omega / Omega comme chez Friedrich ; non verifie.
- Equations (3.3), (3.5) (trace) : terme Omega^{-1} nabla-hat T-hat avec T-hat = -m Omega^3 B (poids poussiere) : regulier a l'ordre dominant par comptage, non calcule.

## 6. Verdicts
- **RJ-1** : mecanisme identifie (relation regularisante, geodesiques conformes du flot), hypotheses : poussiere et flot geodesique.
- **RJ-2** : tenseur de Dirac = poussiere (tau_00 regulier) + inclinaison reguliere (tau_0a) + contraintes d'ordre Omega portant les interferences (tau_ab).
- **RJ-3** : dans le poids poussiere et la jauge de Hubble, **plus aucun pole** ; il reste une oscillation **bornee** en exp(2i(m/H) ln Omega), d'amplitude proportionnelle a \|chi0+\| \|chi0-\| (generique) ou d'ordre Omega (particule pure), nulle pour k = 0 ; l'equation de Dirac garde un coefficient sans limite pour tout k non nul.
- **Global : RJ-V2**, prediction realisee, avec une precision que la prediction n'avait pas : la regularisation retire **tous les poles** ; l'obstruction residuelle n'est pas un pole mais une oscillation log-periodique bornee, c'est-a-dire exactement le contenu invariant de jauge des Prop. 1 et 2(b). Selon le critere FW-3 fixe au gel (phase en ln Omega = irregularite), le systeme reste formellement irregulier.

## 7. Portee (RJ-4)
- **RG-4** : la refutation provisoire tient, mais sa raison change. Ce n'est plus « un pole en m/Omega dans les equations de Friedrich » (artefact du poids 3/2 reel et du poids radiatif du tenseur), c'est « une phase en (m/H) ln Omega sans limite, bornee, invariante de jauge, dans les equations comme dans les solutions ». L'obstruction est plus faible qu'un pole (elle n'empeche ni la bornitude ni la continuite pour une particule pure) et plus robuste (aucun choix d'inconnue spinorielle ne la retire, Prop. 2(b)).
- **Article v2.5** :
  - Prop. 3 : preciser que le pole de la densite d'energie rescalee depend du poids ; dans le poids Omega^{-3} (Friedrich, poussiere) la densite est reguliere, de limite m(\|chi0+\|^2 - \|chi0-\|^2). Le fait invariant est la limite de m fois la difference de normes, pas le pole.
  - Prop. 5(b) : la bornitude du tenseur rescale n'est pas une exigence intrinseque (S19, et ce chantier) ; a reformuler comme regle de raccord choisie, ou a retirer.
  - Remarque Friedrich : ajouter que le pole formel d'ED et FW3 est retire par le poids poussiere et la jauge de Hubble, et que l'obstruction qui reste est la phase log-periodique (Prop. 1, 2(b)).
- Lien avec AF (poids anomal) : le meme schema (un poids reel donne un pole ; un poids complexe 3/2 + i m/H le transforme en phase) que le poids anomal p = 1 + b c0 kappa de NOTE-199 ; ici le poids qui retire le pole est complexe, donc non admissible comme regularisation.

## 8. Non-surclassement
Champ test, un seul etage (FW-4) ; calcul par IA, non relu par un humain ; audit froid requis (FW-5). RG-4 refutee a titre provisoire, raison reformulee (§7) ; noyau {A4 ; A2★ ; N} inchange.
