---
id: NOTE-BORD-EON-183-AUDIT-ED-CONCORDANCE
numero: 183
serie: I
branche: Chantier D (audit ED)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-182-ARMEMENT-AUDIT-ED.md (sceau NOTE-181-182-SCEAU.txt, pose avant lancement)"
rapports: "RAPPORT-DB1.md sha256 39035e3139c643ca ; RAPPORT-DB2.md sha256 07d17965c7d8954d"
---

# Concordance de l'audit ED

## 1. Criteres
| Critere | DB-1 (cecite stricte) | DB-2 (adverse) | Concordance |
|---|---|---|---|
| J-1 covariance hors couche T^ = Omega^2 T[psi_r] | retrouve ; connexion fixee **sans circularite** par covariance de l'operateur de Dirac **et** compatibilite nabla gamma = 0 : Gamma = -(1/4) Omega^-1 [gamma_mu, gamma^nu] d_nu Omega (identique au c = 1/4 de NOTE-181) ; pour un poids w, T^ = Omega^{2w-1} T_r | confirme ; etendu a une metrique non physique **non plate** (tetrades diagonales) et a la signature (-,+,+,+) ; **(A) circulaire et (B) insensible au signe de la connexion** dans ed_check.py (M3) | **oui** ; la limite §5.1 de NOTE-181 est levee (tetrades diagonales) ; le controle de la connexion est fourni par DB-1 |
| J-2 equations geometriques regulieres en forme cinetique | hors couche : tr T^ = Omega^4 tau_r, Omega T* = Omega^3 T*_r, Omega^-1 nabla tr T^ = O(Omega^2), Cotton Omega^0 : **tout regulier pour toute masse** | confirme (calcul avec la vraie structure de Dirac) | **oui** |
| J-3 forme lagrangienne = residu de Dirac | Lag^ = Omega^4 [(i/2)(psibar_r gamma.nabla psi_r - c.c.) - (m/Omega) psibar_r psi_r] ; la forme « cinetique - g Lag » rend visible un terme de trace (m/Omega) psibar psi g et un Cotton en Omega^-1 ; les deux formes coincident sur couche | juste **modulo l'equation de Dirac** seulement, pas comme egalite formelle des seconds membres (M1) ; le lagrangien de (C) n'est pas la forme reelle symetrisee (m1) ; terme (kappa m/2) psibar psi dOmega/Omega explicite | **oui**, formulation corrigee : « meme contenu singulier modulo l'equation de matiere » |
| J-4 contraste scalaire, pas de masse speciale | terme d'ordre Omega^0 du scalaire phi^2(dOmega dOmega - (1/2) g(abs(dOmega)^2 + m^2)) ; coefficient de Omega^-2 dans le Cotton (kappa phi^2/6)(m^2 - 2 lambda/3), **nul a la masse speciale avec le Omega^-1** (calibration positive de Friedrich, independante) ; Dirac : le changement de poids ne produit qu'un terme Clifford-impair (gamma.dOmega), la masse est Clifford-paire ; absorber m exige w = 3/2 -+ i m/H | exposants de Dirac +- i m/H pour tout m != 0 sur dS exact ; scalaire 0 et 1 exactement a m^2 = 2 lambda/3 | **oui** |
| J-5 regulier ssi m = Omega mu | oui ; m = O(Omega^alpha), alpha < 1, ne suffit pas ; **sur couche** : la singularite devient un defaut de lissite (oscillation Omega^{-+ i m/H}, bilineaires Omega^{+-2im/H}), la partie sans trace compensant le Omega^-1 du canal de trace (montre pour la partie dominante) ; exemple : masse de Yukawa m = y Phi^, Phi^ = Omega Phi_r scalaire de poids 1 conformement couple ou de masse m_Phi^2 = 2 lambda/3 | « seulement si » valable **a inconnues fixees** (psi_r = Omega^{-3/2} psi) ; argument des exposants a ajouter (M2) | **oui**, portee precisee |

## 2. Verdict
**AU-V2.** Enonces porteurs J-1 a J-5 confirmes, dont tous a l'aveugle par DB-1 ; aucune erreur grave. Corrections : M1 (modulo l'equation de Dirac), M2 (inconnues fixees ; exposants +- i m/H), M3 (controle circulaire de la connexion dans ed_check.py, remplace par la determination de DB-1), m1 (lagrangien reel symetrise), m2 a m6 (ordres, terme lambda/6 g^, signature, sortie concatenee, limite §5.1 trop prudente). **Prediction AU-V2 realisee.**
Apports nouveaux des auditeurs, retenus : extension a metrique non physique courbe (DB-2) ; calibration positive inhomogene du scalaire de Friedrich (DB-1) ; lecture sur couche (defaut de lissite, pas de puissance negative) ; exemple de Yukawa realisant m = Omega mu, qui recoupe S27 (C-M1, m_h^2 = 2H^2 = 2 lambda/3).

## 3. Consequences (gel NOTE-182, acte NOTE-184)
- Article v2.3 : la Remarque « Formal regularity in Friedrich's sense » integre ED-V1 avec les reserves M1, M2 et la lecture sur couche ; mention de l'exemple de Yukawa comme lien avec la condition de Higgs.
- S26-02 v4 : §9, la reserve « systeme couple non traite » est levee dans les limites ci-dessus.
- ed_check.py n'est pas reecrit (piece scellee) ; la faiblesse M3 est consignee ici et la determination de la connexion par DB-1 (RAPPORT-DB1) fait foi.

## 4. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. RG-4 refutee a titre provisoire ; p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
