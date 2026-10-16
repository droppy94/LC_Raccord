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
script: "rj_check.py (sha256 6f2aae275fb256b6), sortie e0e0589b81772307 ; v2 apres audit : rj_check_v2.py (sha256 bda4f1c2ba1533fc), sortie 2699e91908172f5d"
version: "v2 (corrections D1 a D7 de NOTE-209, audit AU-V3 partiel ; v1 conservee, sha256 91b938e4dc6e5db2)"
---

# Execution RJ

## 0. Portee
Champ de Dirac **test** sur de Sitter exact (carte plate, Omega = -H eta), tenseur injecte lineairement dans l'equation du Weyl rescale des equations conformes (FW-4, premier etage). Le couplage formel complet n'est pas calcule (§5).

## 1. RJ-1 : le mecanisme de Friedrich (arXiv:1601.04506, lu [§§ 2, 3, 4, 5 debut, 7 debut] ; FW-1 en conformite partielle, NOTE-209 D7)
- Inconnues de matiere : U = Omega U-hat, rho = Omega^{-3} rho-hat (« poids poussiere »). Seuls deux seconds membres sont singuliers : l'equation du flot (3.21) et celle du Weyl rescale (3.20), ou le terme singulier est rho Z_jkl / Omega avec Z_jkl = d_[k Omega g_l]j + 2 d_[k Omega U_l] U_j + U_[k g_l]j U^q d_q Omega. Les deux n'ont de limite que si le gradient de Omega devient parallele a U a scri.
- Mecanisme (Lemme 4.1) : pour la poussiere, les geodesiques du flot sont, a reparametrage pres, des geodesiques conformes ; celles-ci sont des invariants conformes et traversent scri. D'ou la **relation regularisante** (4.16) : d Omega = -(d_U Omega + Omega <U,f>) U - Omega f, avec f regulier. En la reportant dans Z, (3.20) et (3.21) deviennent regulieres (4.17), (4.18). Hypotheses utilisees : T-hat = rho-hat U-hat U-hat, flot geodesique, rho-hat >= 0 (et rho > 0 sur scri pour la simplification des contraintes). En §5, une seconde regularisation (zeta_ab = (chi_ab - g_ab chi/3)/Omega, xi) donne un systeme symetrique hyperbolique valable des deux cotes de scri.

## 2. Identite generale (P0, exacte)
Pour un tenseur d'energie-impulsion **quelconque**, avec tau_jk = Omega^{-3} T-hat(e-hat_j, e-hat_k) (le poids poussiere de Friedrich), tau' = tau - (1/3) tr(tau) g, n = d Omega, kappa = 1 :

2 Omega^{-1} nabla-hat_[k L-hat_l]j = (1/2)(nabla_k tau'_lj - nabla_l tau'_kj) + Omega^{-1} S_jkl,
S_jkl = (1/2)[ 2(n_k tau'_lj - n_l tau'_kj) - g_kj n^m tau'_lm + g_lj n^m tau'_km ].

Verifiee par sympy, exactement, sur les 24 composantes (Omega et T-hat polynomiaux generiques, g de Minkowski) : 0 residu. Pour la poussiere, S(rho U U, n) = rho Z_jkl de Friedrich **exactement**, pour U et n quelconques (verifie par RA-2) : P0 est la generalisation exacte de (3.20) de Friedrich a un tenseur quelconque. L'identite tient aussi pour une metrique conforme courbe et des fonctions arbitraires (RA-2).

## 3. Noyau (P1)
Pour n de genre temps (n = -nu e0), S = 0 **si et seulement si** tau = tau_00 e0 e0 (rang 9 sur 10, noyau de dimension 1). Le terme singulier ne disparait donc que pour une matiere qui, a scri, se reduit a une densite au repos dans le repere de n : poussiere alignee. Toute composante tau_0a ou tau_ab d'ordre 1 laisse un pole ; d'ordre Omega, elle laisse un terme borne.

## 4. Champ de Dirac (P2 a P4)
Tenseur de Dirac dans le poids poussiere (u spineur conforme, B = u-dagger beta u, N = u-dagger u, J_i = u-dagger alpha_i u ; derive independamment par RA-1 depuis l'action avec connexion de spin ; conservation complete sur une superposition verifiee par RA-2) :
- tau_00 = m B + Omega k.J ; **le terme de masse est sans 1/Omega** : densite reguliere, de limite m(\|chi0+\|^2 - \|chi0-\|^2), **sans signe fixe** (peut etre negative ou nulle).
- tau_0a = **-** Omega k_a N (signe corrige, D1) : d'ordre Omega, non oscillant.
- tau_ab = (Omega/2)(k_a J_b + k_b J_a).
Le terme de masse s'elimine ponctuellement de tau_0a et tau_ab (psi-dagger {alpha_i, beta} psi = 0) : tau_0a, tau_ab = O(Omega) **pour toute solution**, paquets compris. C'est cette domination de la masse, et non le choix d'un repere U, qui supprime le pole (S ne depend que de tau et de n).

Structure de Fuchs : en variable Omega, du/dOmega = ((i m/H) beta / Omega + (i/H) alpha.k) u, point singulier regulier d'exposants +- i m/H (difference non entiere, pas de logarithme). Toute solution s'ecrit u = c+ Omega^{i m/H} P+(Omega) + c- Omega^{-i m/H} P-(Omega), P+- series entieres. Les bilineaires sont
\|c+\|^2 (serie) + \|c-\|^2 (serie) + c+* c- Omega^{-2i m/H} (serie) + c.c.

| Solution | Bilineaires (tau) | S/Omega et terme derivee de (3.7) |
|---|---|---|
| generique (c+ et c- non nuls) | bornes ; phase exp(+-2i(m/H) ln Omega) des l'ordre dominant dans tau_ab/Omega, a l'ordre Omega dans tau_00 | **bornes, sans limite** (amplitude proportionnelle a k et a \|c+\| \|c-\|) |
| un seul exposant (particule pure ou antiparticule pure a la limite, paquets de meme type) | **series entieres en Omega** : tau_ab = O(Omega^2), tau_00 = m + O(Omega^2) (P4, v2) | **reguliers (series entieres)** |
| k = 0 | tau = m B e0 e0, constant | nuls |
| m = 0 | reguliers (cas conforme, RA-1) | reguliers |

La ligne « particule pure : C^0, pas C^1 » de la v1 etait fausse (NOTE-209 D2) : elle decrivait l'inconnue chi, pas les bilineaires.

Equation de matiere (P3) : avec chi = U0-dagger u, U0 = exp(i beta theta), le coefficient m/Omega devient alpha.k exp(2 i beta theta) : borne, sans limite. Aucune transformation u = V chi **reguliere**, ni aucune V **independante de k**, ne rend les coefficients reguliers (exposants +- i m/H non entiers, invariants modulo Z ; RA-1, RA-2). Une V dependant de k et non reguliere (le propagateur) annule le coefficient mais ne change pas les bilineaires. L'equation de Dirac reste donc singuliere pour toute inconnue reguliere (pole de Fuchs en u, phase en chi), **y compris pour la classe a un seul exposant** : la regularite de cette classe est celle des sources, pas celle de l'equation.

## 5. Ce qui n'est pas fait (complete apres audit)
- Couplage formel complet Einstein-Dirac (jets, comme FW3) avec Omega dynamique et la relation regularisante de Friedrich : non calcule. Il ne peut pas donner RJ-V1 (l'equation de matiere reste singuliere) mais pourrait reintroduire des poles et toucher la classe a un seul exposant.
- FLRW tendant vers de Sitter (demande par RJ-2 au gel) : non fait.
- Espaces non homogenes et inconnue Omega : d_a Omega non nul, transposition de la jauge par geodesiques conformes a un flot de Dirac qui n'est pas geodesique et, generiquement, pas au repos (vitesse J/N d'ordre 1, oscillante ; RA-2) : non fait.
- Signe de la densite limite (D6) : peut s'annuler ; l'analogie poussiere cesse alors.
- Fermes par l'audit : (3.3) a (3.6) sans puissance negative de Omega dans le poids poussiere ; terme derivee de (3.7) borne, oscillant generiquement, regulier pour la classe a un seul exposant (RA-2).

## 6. Verdicts (premier etage, champ test, FW-4)
- **RJ-1** : mecanisme identifie (relation regularisante, geodesiques conformes du flot), hypotheses : poussiere, flot geodesique, rho-hat >= 0.
- **RJ-2** : tenseur de Dirac = densite au repos reguliere (tau_00, sans signe fixe) + inclinaison O(Omega) (tau_0a) + contraintes O(Omega) portant les interferences (tau_ab).
- **RJ-3** : dans le poids poussiere, **aucun pole** dans les seconds membres du secteur Einstein ((3.3) a (3.7)) pour toute solution ; seconds membres **series entieres** pour la classe a un seul exposant de Fuchs (particule pure, antiparticule pure, paquets de meme type) et pour k = 0 ; **bornes sans limite** (phase exp(+-2i(m/H) ln Omega)) pour une solution generique. L'equation de Dirac reste singuliere (Fuchs) pour toute inconnue reguliere.
- **Global : RJ-V2**, prediction realisee, avec la classe exceptionnelle explicite exigee par le gel. Au critere FW-3, la classe generique est formellement irreguliere (sources) ; la classe a un seul exposant est reguliere au niveau des sources ; aucune n'est reguliere au niveau de l'equation de matiere.

## 7. Portee (RJ-4)
- **RG-4** : la refutation provisoire tient au premier etage, mais sa raison change. Ce n'est plus « un pole en m/Omega dans les equations de Friedrich » (artefact du poids 3/2 reel du spineur et du poids radiatif du tenseur) ; c'est l'**interference entre les deux exposants de Fuchs +- i m/H** (phase relative de la Prop. 2(b)), presente si et seulement si les deux composantes limites sont non nulles, plus le caractere singulier (Fuchs) de l'equation de Dirac a scri. Pour une matiere de Dirac a un seul exposant (que des particules, ou que des antiparticules, a la limite), les sources de la geometrie sont analytiques : c'est l'analogue spinoriel de la poussiere de Friedrich. Question ouverte au second etage : le couplage complet preserve-t-il cette classe ?
- **Article v2.5** :
  - Prop. 3 : le pole m/Omega est celui de la variable radiative (poids Omega^{-4}, celui que donne naturellement le spineur de poids 3/2) ; les seconds membres des equations conformes, qui ne dependent pas de ce choix, n'en ont pas ; dans le poids Omega^{-3} la densite est reguliere, de limite m(\|chi0+\|^2 - \|chi0-\|^2), sans signe fixe. Corriger « signe fixe » en « fixe pour une solution donnee, non positif en general ».
  - Prop. 5(b) : la bornitude du tenseur rescale n'est pas une exigence intrinseque (S19 et ce chantier) ; a reformuler comme regle de raccord choisie, ou a retirer.
  - Remarque Friedrich : le pole formel d'ED et FW3 est retire, pour les sources geometriques, par le poids poussiere ; ce qui reste est la singularite de Fuchs de l'equation de Dirac et, pour une solution generique, la phase d'interference ; la classe a un seul exposant donne des sources analytiques (premier etage).
- Lien avec AF (poids anomal) : meme schema qu'en NOTE-199 (un poids reel donne un pole, un poids complexe le transforme en phase) ; ici le poids qui retire le pole de l'inconnue spinorielle est complexe (3/2 +- i m/H), donc non admissible comme inconnue reguliere, mais les bilineaires a un seul exposant n'en ont pas besoin.

## 8. Non-surclassement
Champ test, premier etage (FW-4) ; calcul et audit par IA, non relus par un humain. RG-4 refutee a titre provisoire, raison reformulee et classe exceptionnelle identifiee (§7) ; noyau {A4 ; A2★ ; N} inchange.
