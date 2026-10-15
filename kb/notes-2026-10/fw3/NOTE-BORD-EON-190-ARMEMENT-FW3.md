---
id: NOTE-BORD-EON-190-ARMEMENT-FW3
numero: 190
serie: I
branche: CCC + M (extension du theoreme 3.1 de Friedrich au systeme couple jauge-Higgs-Dirac-Einstein ; chantier FW3)
reservation: 2026-10-15T16:43:52Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 190)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant tout calcul : regularite formelle, au sens de Friedrich, du systeme conforme couple Einstein + Yang-Mills + Higgs (doublet, potentiel quartique, couplage non minimal xi) + Dirac (masse de Yukawa)"
decision: "operateur (Thierry), 2026-10-15 18:40 heure de Paris : « ok pour continuer le programme » ; lecture retenue : piste 1 du §11 de la reprise v9.1 (FW-3 elargi), complement de ED (180-184) et HX (185-189)"
amont: "NOTE-181 (ED-V1, audite AU-V2 NOTE-183) ; NOTE-186 (HX-V1, audite AU-V2 NOTE-188) ; S27-02 v2 §F (reserve FW-3) ; NOTE-176/178 (calibration (2.17), combinaison (1/3)(m^2 - 2 lambda/3)) ; Friedrich 1311.0700 th. 3.1 et preuve (src CAL-F)"
---

# Gel FW3 : le systeme couple jauge-Higgs-Dirac-Einstein au sens de Friedrich

## 0. Objet
S27-02 v2 §F etablit que M2 = m_h^2/H^2 + 12 xi = 2 suffit a la regularite formelle du secteur Yukawa et W, Z, **sous la reserve FW-3** : « l'application du theoreme 3.1 (enonce pour un scalaire reel) au systeme couple jauge-Higgs-Dirac (et Einstein) est une extension non verifiee ». ED a traite Einstein-Dirac a masse constante ; HX a traite les poids conformes et les equations de matiere sur solutions homogenes. Reste a verifier que, dans le systeme couple complet ecrit en inconnues rescalees de Friedrich, **les seconds membres de toutes les equations** (matiere : Yang-Mills, Higgs, Dirac ; geometrie : (2.13) a (2.17)) sont formellement reguliers sous la seule condition M2 = 2, sans condition supplementaire venant des couplages de jauge, de Yukawa, ou des termes croises.

## 1. Cadre fixe (ED-0 elargi)
- Metrique physique ghat = Omega^-2 g ; inconnues de Friedrich (e, Gamma, Omega, s, L, W) ; inconnues de matiere rescalees : A_mu (poids 0, inchange), H_r = Omega^-1 H (doublet complexe, 4 composantes reelles), psi_r = Omega^{-3/2} psi, avec leurs derivees premieres (et secondes si un second membre en contient : regle de Friedrich, « unknowns (3.12) and nabla psi »).
- Lagrangien physique (signature de Friedrich) : -(1/4) F^2 + |D H|^2 - V(H) - xi Rhat |H|^2 + psibar (i gamma.D - y H) psi, D = nabla - i g A (abelien suffit pour les poids ; la structure non abelienne, de poids 0, ne change pas le comptage), V = m_h^2 |H|^2 + lambda_h |H|^4. Le parametre m_h^2 est libre de signe (M2 est le parametre) ; **aucun terme cubique** : la condition mu = 0 du theoreme 3.1 est automatique par invariance de jauge.
- Tenseur d'energie-impulsion total : T_YM + T_H (forme (3.2) de Friedrich avec D a la place de nabla, plus le terme d'amelioration xi (Ghat + ghat box_hat - nabla_hat nabla_hat)|H|^2) + T_D (forme cinetique symetrisee, ED) ; variante « cinetique - ghat Lag_D » pour FW3-3.
- Outil : algebre de jets a un point, metrique non physique plate (DB-2 a etendu la covariance de Dirac au cas courbe), signature (+,-,-,-), conventions de ED (connexion de spin fixee par DB-1 : Gamma_mu = (1/4)[gamma_mu, gamma^nu] d_nu sigma, sigma = -ln Omega) ; relations geometriques utilisees a l'ordre dominant : |dOmega|^2 = -lambda/3 + 2 Omega s + O(Omega^2), nabla nabla Omega = s g + O(Omega) ((3.8), (2.14)).

## 2. Questions figees
- **FW3-1 (equations de matiere).** Les equations rescalees de Yang-Mills (D_mu F^{mu nu} = J^nu, courants de Higgs et de Dirac), de Higgs ((box - R/6) H_r = ...) et de Dirac ((i gamma.D - y H_r) psi_r = 0) sont-elles formellement regulieres, et sous quelle condition ? Les termes de Yukawa, quartique et de jauge produisent-ils des Omega^-k ?
- **FW3-2 (equations geometriques, coefficient singulier).** Avec T total, quel est le coefficient du terme d'ordre Omega^-1 dans 2 Omega^-1 nablahat_[nu Lhat_lambda] rho (2.17) (et dans (2.16)) a l'ordre dominant en Omega, comme fonction des inconnues ? Contributions separees : YM, Higgs (xi = 0), terme xi, Dirac cinetique, termes croises (derivee covariante de jauge dans T_H, courants). Calibration obligatoire : a xi = 0, A = 0, psi = 0, retrouver (kappa/2)(1/3)(m_h^2 - 2 lambda/3) |H_r|^2 nabla_[rho Omega g_mu]nu (NOTE-176 §F-0, confirme CA-1/CA-2) ; a xi = 1/6, m_h = 0, retrouver 0.
- **FW3-3 (representation).** Avec la masse de Yukawa, la forme « cinetique - ghat Lag_D » du tenseur de Dirac est-elle encore singuliere (comme a masse constante, ED-3 : terme d'ordre Omega^1 dans Lhat) ou reguliere ?
- **FW3-4 (bilan).** Le systeme couple complet est-il formellement regulier si et seulement si une seule condition est satisfaite, et laquelle ? Quelles inconnues supplementaires le systeme etendu exige-t-il (derivees secondes de H_r si xi != 0) ? Que reste-t-il hors du resultat (Majorana nue, Weinberg, Lambda_QCD, anomalies) ?

## 3. Espace de verdicts
- **FW3-V0** : non concluant (identites non verifiees symboliquement, ou coefficient de (2.17) non isole).
- **FW3-V1** : le systeme couple complet est formellement regulier **si et seulement si** m_h^2 + 4 lambda xi = 2 lambda/3 (soit M2 = 2 avec lambda = 3H^2), la meme combinaison apparaissant dans l'equation de Higgs et dans les equations geometriques ; Yang-Mills, Dirac, Yukawa, courants et termes croises n'ajoutent aucune condition. La reserve FW-3 de S27-02 v2 est levee pour le systeme classique.
- **FW3-V2** : les equations geometriques imposent une condition **distincte** de celle de l'equation de Higgs (par exemple une dependance en xi differente) ; les deux ne sont compatibles qu'a m_h = 0 ou jamais : CCC + M se referme (ou se reduit a un Higgs sans masse).
- **FW3-V3** : les termes croises (jauge, Yukawa) produisent des Omega^-k qu'aucune valeur de M2 ne retire : obstruction plus forte que HX, CCC + M fermee dans cette classe.
- **FW3-V4** : une structure du systeme couple retire la condition (regulier sur un ouvert de valeurs de M2) : contredit HX, revision obligatoire.

## 4. Prediction (informee, precedent ix)
**FW3-V1.** Motifs ecrits avant tout calcul : (i) YM est conformement invariant en dimension 4 (sqrt(-ghat) ghat^{ma} ghat^{nb} = sqrt(-g) g^{ma} g^{nb}), T_YM = Omega^2 T[A ; g] sans trace : rien dans (2.17) a l'ordre Omega^-1 ; (ii) les courants rescalent en Omega^4 (Dirac : gammahat^mu = Omega gamma^mu et psi = Omega^{3/2} psi_r ; Higgs : la partie en dOmega de H* D H est reelle et s'elimine dans i(H* DH - c.c.)), donc l'equation de YM rescalee est reguliere ; (iii) pour le Higgs, (3.4) donne (box - R/6) H_r = Omega^-2 (m_h^2 + (xi - 1/6)(4 lambda - kappa That)) H_r + 2 lambda_h |H_r|^2 H_r + y psibar_r psi_r + ..., ou Omega^-2 That = T* est regulier (3.7) : regulier ssi m_h^2 + 4 lambda xi = 2 lambda/3, Yukawa et quartique de poids 0 (HX, poids verifies par HA-2) ; (iv) dans (2.17), la partie d'ordre Omega^0 de T*_mn du Higgs est |H_r|^2 (dOmega dOmega - (1/4)|dOmega|^2 g) comme pour le scalaire de Friedrich, la derivee de jauge n'ajoutant que des termes d'ordre superieur ; d'ou la combinaison (1/3)(m_h^2 - 2 lambda/3)|H_r|^2 a xi = 0 ; le terme xi est lineaire en xi et doit s'annuler avec le reste a (xi, m_h) = (1/6, 0) (scalaire conformement couple sans masse : T sans trace, That = Omega^2 T) ; par linearite, le coefficient est (1/3)(m_h^2 + 4 lambda xi - 2 lambda/3)|H_r|^2 ; (v) FW3-3 : Lag_D = Omega^4 psibar_r (i gamma.D - y H_r) psi_r est d'ordre Omega^4, donc ghat Lag_D = Omega^2 (...) g est d'ordre Omega^2 et ne produit plus le terme d'ordre Omega^1 de ED-3 : la dependance a la representation disparait avec la masse de Yukawa. Incertitudes declarees : le terme xi dans les equations geometriques (calcul neuf, le motif de linearite n'est qu'un argument) ; les termes croises de T_H a l'ordre Omega^0 et Omega^1 (D H = Omega D H_r + H_r dOmega : le terme en A |H_r|^2 dOmega est d'ordre Omega^1 et pourrait laisser un Omega^0 apres division).

## 5. Firewall
- FW-1 : regularite **formelle** (seconds membres comme fonctions des inconnues rescalees, en jets), jamais une valeur sur une solution (precedent xii).
- FW-2 : toute identite est verifiee symboliquement (script scelle avec sa sortie) ; les relations geometriques (3.8), (2.14) ne sont utilisees que pour les ordres dominants explicitement ecrits au §1.
- FW-3 : calibration a reponse connue (precedent xii) : xi = 0 scalaire seul reproduit (1/3)(m^2 - 2 lambda/3) ; (xi, m) = (1/6, 0) donne 0 ; Dirac a masse constante reproduit ED-3 (ordre Omega^1 dans la forme lagrangienne).
- FW-4 : audit froid aveugle (cecite stricte + adverse) avant toute greffe (precedent x).
- FW-5 : aucune modification de S27-02 v2 ni de l'article dans ce chantier ; propositions seulement.
- FW-6 : les criteres transmis aux auditeurs sont ecrits sous forme d'egalites explicites (lecon HA-1, NOTE-188).
- FW-7 : hors champ declare : existence et hyperbolicite (evolution), effets quantiques (courses, anomalies, Lambda_QCD), Majorana nue (poids -1, reste singulier), operateur de Weinberg (traite seulement en suffisance : H_r lisse implique Omega H_r^2 lisse), cout du reglage M2 = 2 (S27 A.2). Le verdict porte sur le systeme classique.

## 6. Non-surclassement
Rien de grave. CCC + M hypothese ouverte ; RG-4 refutee a titre provisoire ; G-V3 candidat ; p_Q non fixe, N non chiffre, noyau {A4 ; A2★ ; N} inchange.
