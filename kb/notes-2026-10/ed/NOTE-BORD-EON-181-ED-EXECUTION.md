---
id: NOTE-BORD-EON-181-ED-EXECUTION
numero: 181
serie: I
branche: Chantier D (systeme Einstein-Dirac couple, chantier ED)
reservation: 2026-10-15T15:28:07Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 181)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-180-ARMEMENT-ED.md, sha256 2735ea0207665b3e, sceau NOTE-180-SCEAU.txt 2026-10-15T15:28:07Z"
source: "H. Friedrich, arXiv:1311.0700v2, equations (2.13)-(2.17), (3.2), (3.11), theoreme 3.1 (extrait archive CAL-F/src)"
script: "ed_check.py et ed_check_sortie.txt (empreintes au sceau de cloture)"
---

# ED, execution : le systeme Einstein-Dirac couple au sens de Friedrich

## VERDICT : ED-V1. Prediction (informee) realisee.
La singularite du systeme conforme couple Einstein-Dirac massif est **confinee au secteur de matiere** : l'equation de Dirac rescalee porte le coefficient m/Omega (et les equations qu'on en derive pour les derivees de psi_hat portent m/Omega et ses derivees). Les seconds membres des equations geometriques (2.13) a (2.17) sont **formellement reguliers** pour toute masse lorsque le tenseur d'energie-impulsion est ecrit sous forme cinetique. Il n'existe ni masse speciale ni couplage de la classe du Lemme 2 de l'article qui retire la singularite a masse effective non nulle.

## 1. ED-1 : covariance conforme du tenseur cinetique (script, partie B)
Conventions verifiees d'abord (FW-2) : signature (+,-,-,-), metrique non physique plate, metrique physique g_hat = Omega^-2 eta, tetrade e_hat^a_mu = Omega^-1 delta, connexion de spin Gamma_mu = (1/4)[gamma_mu, gamma^nu] d_nu sigma, sigma = -ln Omega ; avec ce coefficient, i gamma_hat^mu nabla_hat_mu (Omega^{3/2} psi_hat) = Omega^{5/2} i gamma^mu d_mu psi_hat hors couche (partie A).
**Identite (hors couche, algebrique en psi_hat et ses derivees premieres)** : T_hat_{mu nu}[psi ; g_hat] = Omega^2 T_{mu nu}[psi_hat ; eta], ou T est le tenseur cinetique symetrise (i/4)(psibar gamma_(mu nabla_nu) psi - nabla_(nu psibar gamma_mu) psi), reel. Le tenseur ne contient pas m.

## 2. ED-2 : les equations geometriques (forme cinetique)
Avec T_hat = Omega^2 Theta, Theta fonction reguliere de (psi_hat, d psi_hat) :
- trace : T_hat = g_hat^{ab} T_hat_ab = Omega^4 Theta_tr ; (2.13) regulier ; terme de (2.15) - (kappa/24) Omega^-1 nabla T_hat = - (kappa/24) Omega^-1 d(Omega^4 Theta_tr) : regulier ;
- partie sans trace T*_mu nu = T_hat - (1/4) T_hat g_hat = Omega^2 (Theta - (1/4) Theta_tr eta) : (2.14) Omega T* et (2.15) nabla Omega . T* reguliers ;
- (2.16)-(2.17) : L_hat = (kappa/2) Omega^2 (Theta - (1/3) Theta_tr eta) + (lambda/6) g_hat ; le terme en lambda est annule par nabla_hat ; pour L_hat = Omega^2 Y, Y lisse generique, la plus basse puissance de Omega dans 2 Omega^-1 nabla_hat_[nu L_hat_lambda] rho est **0** (script, partie D, Omega(x) et Y(x) generiques) : **formellement regulier**.
Les seconds membres contiennent des derivees secondes de psi_hat (comme chez Friedrich pour le scalaire, qui l'indique explicitement) ; ce sont des inconnues du systeme etendu, et c'est par leur equation d'evolution, derivee de l'equation de Dirac, que m/Omega rentre.

## 3. ED-3 : dependance a la representation
Hors couche, le lagrangien vaut **Lag[psi ; g_hat] = Omega^4 psibar_hat (i gamma.d - m/Omega) psi_hat** (script, partie C) : c'est Omega^4 fois le residu de l'equation de Dirac rescalee. Si l'on ecrit T sous la forme « cinetique - g_hat Lag », le terme g_hat Lag = Omega^2 eta (psibar_hat i gamma.d psi_hat) - m Omega psibar_hat psi_hat eta donne a L_hat une composante d'ordre Omega^1 proportionnelle a m ; pour L_hat = Omega Y, la plus basse puissance dans (2.17) est **-1** (script, variante). Ces termes sont des multiples du residu de l'equation de Dirac : nuls sur couche, ils ne sont que la singularite de l'equation de matiere reportee dans les equations geometriques. Le contenu singulier du systeme est donc le meme dans les deux representations : **m/Omega**.

## 4. ED-4 : bilan et contraste avec le scalaire
- **Scalaire** (Friedrich) : T_hat contient m^2 phi^2 g_hat = m^2 psi^2 eta et d phi d phi = psi^2 dOmega dOmega + ..., tous deux d'ordre Omega^0 (script, partie E pour le premier) ; L_hat a une composante d'ordre 1, d'ou des termes en Omega^-1, Omega^-2 dans (2.16)-(2.17) et dans (3.11), qui se combinent en multiples de (m^2 - 2 lambda/3) (theoreme 3.1 ; non reproduit ici). La masse speciale vient de cette compensation entre m^2 et la courbure (lambda, via dOmega dOmega = lambda/3 + ...).
- **Dirac** : aucune composante d'ordre Omega^0 ou Omega^1 dans L_hat sous forme cinetique ; la masse n'entre que par l'equation de matiere, lineairement (m/Omega) ; rien ne peut la compenser (pas de terme de courbure d'ordre Omega^-1 dans l'equation de Dirac rescalee, l'operateur sans masse etant conformement covariant sans terme de courbure) ; Lemme 2 pour les couplages locaux.
- **Consequence** : au sens formel de Friedrich, le systeme couple Einstein-Dirac est regulier si et seulement si le coefficient m/Omega l'est, c'est-a-dire si m = Omega mu avec mu lisse (Prop. 4(c) de l'article) ; aucune masse constante non nulle ne convient. C'est l'analogue, pour le systeme couple, du theoreme 3.1, avec une difference de structure : pas de masse speciale pour le spin 1/2.

## 5. Limites
- Calcul formel en jets sur fond conformement plat (metrique non physique plate) : l'identite B est algebrique et ne depend pas de la courbure de la metrique non physique dans la forme ou elle est ecrite ici ; son extension a une metrique non physique generale passe par la covariance conforme generale de l'operateur de Dirac et de son tenseur cinetique (standard), non verifiee symboliquement ici.
- Le comptage D est fait pour Y generique ; il ne dit rien des structures particulieres (il est une borne, conformement au precedent xii, mais ici la borne est 0, ce qui suffit pour la regularite).
- La question de l'existence de solutions (evolution hyperbolique) n'est pas traitee, ni la retroaction a l'ordre non lineaire au-dela de la structure formelle.

## 6. Propositions (non entees ; audit FW-4 d'abord)
- **Article v2.3** : remplacer, dans la Remarque « Formal regularity in Friedrich's sense », la phrase « The geometric equations of the coupled Einstein–Dirac system are not treated here » par l'enonce de §4 (geometrie formellement reguliere en forme cinetique ; singularite confinee a l'equation de matiere ; regulier ssi m = Omega mu), avec l'identite de covariance et la remarque de representation.
- **S26-02 v4 (§8, lecture (ii))** : retirer « Les equations geometriques du systeme couple Einstein-Dirac ne sont pas traitees » et inscrire le resultat ED-V1.

## 7. Non-surclassement
Rien de grave. RG-4 refutee a titre provisoire ; G-V3 inchange ; p_Q non fixe ; N non chiffre ; noyau {A4 ; A2* ; N} inchange.
