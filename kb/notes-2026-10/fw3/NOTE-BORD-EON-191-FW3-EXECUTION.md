---
id: NOTE-BORD-EON-191-FW3-EXECUTION
numero: 191
serie: I
branche: CCC + M (chantier FW3, extension du theoreme 3.1 de Friedrich au systeme couple)
reservation: 2026-10-15T16:43:52Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 191)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-190-ARMEMENT-FW3.md, sha256 513cbcbfdb538c88, sceau NOTE-190-SCEAU.txt 2026-10-15T16:44:58Z"
source: "H. Friedrich, arXiv:1311.0700v2 (conventions : signature (-,+,+,+), ghat = Omega^-2 g, (2.2)-(2.4), (2.13)-(2.17), (3.2)-(3.8), th. 3.1 ; extrait archive CAL-F/src)"
script: "fw3_check.py et fw3_check_sortie.txt (empreintes au sceau de cloture), sympy, 43 s"
---

# FW3, execution : le systeme couple jauge-Higgs-Dirac-Einstein au sens de Friedrich

## VERDICT : FW3-V1. Prediction (informee) realisee sur tous les points, calibrations comprises.
Le systeme conforme de Friedrich couple a Yang-Mills, a un Higgs complexe (potentiel m_h^2 |H|^2 + lambda_h |H|^4, couplage non minimal xi) et a un Dirac de masse de Yukawa, ecrit en inconnues rescalees (A, H_r = Omega^-1 H, psi_r = Omega^-3/2 psi), est formellement regulier **si et seulement si**

    m_h^2 + 4 lambda xi = 2 lambda/3     (soit M2 = m_h^2/H^2 + 12 xi = 2, lambda = 3H^2).

La meme combinaison gouverne l'equation de Higgs rescalee (coefficient de Omega^-2) et les equations geometriques (coefficient de Omega^-2 et de Omega^-1 dans (2.17), qui s'annulent ensemble a cette valeur). Yang-Mills, Dirac, Yukawa, courants, quartique et derivee covariante de jauge n'apparaissent dans aucun coefficient singulier. La reserve FW-3 de S27-02 v2 §F est levee pour le systeme classique.

## 1. FW3-1 : equations de matiere (script, parties A, B, D)
- **Yang-Mills** : sqrt(-ghat) ghat^{ma} ghat^{nb} = sqrt(-g) g^{ma} g^{nb} (identite en dimension 4) ; l'equation rescalee est nabla_mu F^{mu nu} = j_r^nu avec J^nu = Omega^4 j_r^nu. Courant de Higgs : J_a = i e (H* D_a H - c.c.) est d'ordre Omega^2 et **sans terme en dOmega** (la partie en dOmega de H* D H est reelle) ; courant de Dirac : psibar gammahat_a psi = Omega^2 psibar_r gamma_a psi_r. Regulier pour tout H_r, psi_r.
- **Higgs** : identite verifiee hors couche, avec derivee de jauge : Omega^-3 (boxhat_D - Rhat/6)[Omega H_r] = (box_D - R/6)[H_r]. L'equation rescalee s'ecrit box_D H_r = Omega^-2 (m_h^2 + 4 lambda xi - 2 lambda/3) H_r - (xi - 1/6) kappa T* H_r + 2 lambda_h |H_r|^2 H_r - y psibar_r psi_r (schematique pour le Yukawa), avec T* = Omega^-2 That regulier (partie C) et Rhat = 4 lambda - kappa That (2.2). Reguliere ssi m_h^2 + 4 lambda xi = 2 lambda/3. Quartique et Yukawa de poids 0. La condition mu = 0 du theoreme 3.1 (pas de terme cubique) est automatique par invariance de jauge.
- **Dirac** (jets, signature (+,-,-,-) de ED, connexion de DB-1) : (i gammahat.Dhat - y Omega h_r) psi = Omega^{5/2} (i gamma.D - y h_r) psi_r hors couche, A de poids 0 : coefficient de masse rescale y h_r, regulier ssi h_r l'est. Tenseur cinetique symetrise avec champ de jauge : That = Omega^2 T[psi_r ; eta, A] hors couche (extension de ED-1 a A != 0).

## 2. FW3-2 : equations geometriques (script, partie C)
Procedure formelle de Friedrich : jets a un point, g = eta ; les derivees secondes et troisiemes de Omega sont remplacees par (2.14) et sa derivee avec (2.15), |dOmega|^2 par (3.8) (reduction polynomiale en n_0) ; T* et sa trace y sont des symboles generiques reguliers (S_ab, Str) ; les derivees de H_r jusqu'a l'ordre 3 et de A jusqu'a l'ordre 2 sont des inconnues independantes.
- **Calibration 1** (scalaire reel, xi = 0, A = 0 : theoreme 3.1) : That_ab et Omega^-2 That reguliers ; la source de (2.17) a pour plus basse puissance Omega^-2 avec coefficient **exactement** (kappa/3)(m^2 - 2 lambda/3) p^2 n_[nu eta_lambda]rho (p = psi de Friedrich) ; coefficient de Omega^-1 non nul en general (exemple : (kappa/18)(3 m^2 - 2 lambda) p d_1 p), **nul a m^2 = 2 lambda/3** ; aucun Omega^-3. Le theoreme 3.1 est reproduit (sens « si » et « seulement si »), et la combinaison (1/3)(m^2 - 2 lambda/3) de NOTE-176/178 est retrouvee.
- **Calibration 2** (xi = 1/6, m = 0) : tous les coefficients singuliers s'annulent (scalaire conformement couple).
- **Systeme complet** (Higgs complexe avec D_a = d_a - i e A_a, Yang-Mills, xi) : That_ab (indices bas) et Omega^-2 That reguliers, y compris les termes d'amelioration xi (Ghat, boxhat, nablahat nablahat de |H|^2 exprimes par (2.3), (2.4), (2.14)) ; source de (2.17) : plus basse puissance Omega^-2, coefficient **exactement** (kappa/3)(m_h^2 + 4 lambda xi - 2 lambda/3) (phi_1^2 + phi_2^2) n_[nu eta_lambda]rho (H_r = (phi_1 + i phi_2)/sqrt 2) ; a m_h^2 + 4 lambda xi = 2 lambda/3, les coefficients de Omega^-2 **et** de Omega^-1 s'annulent identiquement ; aucun Omega^-3. Les coefficients singuliers ne contiennent ni A, ni dA, ni lambda_h : les symboles presents sont (p, q, dp, dq, n, kappa, lambda, m, xi) seulement.
- Doublet : T_H est additif sur les composantes (le quartique, d'ordre Omega^2 dans That, ne compte pas) ; une composante complexe suffit, le coefficient se lit sur Sum_i phi_i^2 = 2 |H_r|^2.
- Dirac cinetique : That_D = Omega^2 Theta (partie D), donc Lhat_D = Omega^2 x regulier et (2.17) regulier (comptage ED partie D, puissance 2 donne plus basse puissance 0) ; Yang-Mills inclus explicitement dans la partie C.
- Les autres equations : (2.13) regulier car That = Omega^2 Str ; (2.14), (2.15) reguliers car T*_ab (indices bas) regulier ; (2.16) implique par (2.17).

## 3. FW3-3 : representation du tenseur de Dirac
Lag_D[psi ; ghat, A, yH] = Omega^4 psibar_r (i gamma.D - y h_r) psi_r hors couche ; donc ghat Lag_D = Omega^2 (...) eta est d'ordre Omega^2 dans Lhat et (2.17) reste regulier dans la forme « cinetique - ghat Lag ». Avec la masse de Yukawa, **la dependance a la representation de ED-3 disparait** (a masse constante, le terme de masse de ghat Lag est d'ordre Omega^1, controle reproduit). La reserve M1 de NOTE-183 (« modulo l'equation de matiere ») n'est plus necessaire pour le systeme a masse de Yukawa.

## 4. FW3-4 : bilan
- **Une seule condition**, M2 = 2, pour tout le systeme classique couple : elle apparait au meme endroit que chez Friedrich (equation de Higgs et equations (2.16)-(2.17)), avec la meme structure (la masse de jauge et de Yukawa sont de poids 0 ; seul le terme de masse du Higgs est de poids -2, compense par R/6 a M2 = 2). Le sens « seulement si » tient au sens formel : le coefficient de Omega^-2 de (2.17) est une fonction non nulle des inconnues des que M2 != 2.
- Inconnues supplementaires du systeme etendu : avec xi != 0, That contient nablahat nablahat |H|^2, donc les derivees secondes de H_r entrent dans T* et les derivees troisiemes dans nablahat Lhat ; a xi = 0, derivees secondes seulement (comme chez Friedrich). Les derivees de A jusqu'a l'ordre 2 (Yang-Mills). Les derivees de psi_r jusqu'a l'ordre 2 (ED).
- Hors du resultat (FW-7) : Majorana nue (poids -1, coefficient M/Omega, singulier comme ED) ; operateur de Weinberg (suffisance seulement : H_r lisse donne un coefficient Omega H_r^2 lisse) ; Lambda_QCD, courses, anomalies ; existence et hyperbolicite ; cout du reglage.
- Lien avec le corpus : HX avait obtenu M2 = 2 par le theoreme 3.1 applique au Higgs seul et par les poids ; le present chantier verifie que le systeme couple complet n'ajoute aucune condition et que le secteur geometrique porte la meme combinaison en xi. ED reste valable a masse constante (singularite confinee a l'equation de matiere) ; a masse de Yukawa, la singularite migre entierement dans le secteur Higgs (equation de Higgs et (2.17)) et disparait a M2 = 2.

## 5. Limites
- Calcul formel en jets sur metrique non physique plate (DB-2 a etendu la covariance de Dirac au cas courbe ; pour le Higgs et YM les transformations (2.3), (2.4) et l'identite (3.4) sont generales).
- La partie C n'inclut pas le tenseur cinetique de Dirac explicitement (son ordre Omega^2 est etabli en partie D et le comptage de ED partie D s'applique) ; un audit adverse pourra l'inclure.
- Groupe de jauge abelien dans le script ; la structure non abelienne (commutateurs de poids 0, courant de jauge de poids 0) ne change pas le comptage, non verifiee symboliquement.
- Le signe de m_h^2 est libre : la condition M2 = 2 exige m_h^2 + 12 xi H^2 = 2H^2 > 0 ; le potentiel du Modele standard au point symetrique (m_h^2 < 0) impose xi > 1/6 (cout, hors chantier).
- Rien sur les solutions : « regulier » = seconds membres fonctions lisses des inconnues.

## 6. Propositions (non entees ; audit FW-4 d'abord)
- **S27-02 v3, greffe G-M2 sur §F** : remplacer la reserve FW-3 par : « verifie (NOTE-191, audite) pour le systeme classique couple YM-Higgs-Dirac-Einstein : regularite formelle ssi M2 = 2, meme combinaison en xi dans l'equation de Higgs et dans (2.16)-(2.17) ; restent hors champ : Majorana nue, Weinberg (suffisance seule), effets quantiques, existence ». Ligne CCC + M de la reprise : « condition unique sur le Higgs, etablie pour le systeme couple classique ».
- **Article (v2.4, Remarque « Formal regularity ») ** : une phrase : avec une masse de Yukawa m = y Omega H_r, la singularite de l'equation de Dirac disparait et se reporte sur le secteur Higgs, ou la condition de Friedrich m_h^2 + 4 lambda xi = 2 lambda/3 est celle du systeme couple complet ; la forme lagrangienne du tenseur de Dirac est alors reguliere.

## 7. Non-surclassement
Rien de grave. CCC + M hypothese ouverte (condition unique sur le Higgs, desormais etablie pour le systeme couple classique, sous audit). RG-4 refutee a titre provisoire ; G-V3 candidat ; p_Q non fixe, N non chiffre, noyau {A4 ; A2★ ; N} inchange.
