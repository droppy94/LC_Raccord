---
id: NOTE-BORD-EON-199-AUDIT-AF-CONCORDANCE
numero: 199
serie: I
branche: G-V3 / Q-M3 (audit AF)
reservation: 2026-10-16T14:09:58Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 199)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-198-ARMEMENT-AUDIT-AF.md sha256 7475004fa15d519e (sceau NOTE-197-198-SCEAU.txt, 2026-10-16T14:10:12Z, pose avant lancement)"
rapports: "RAPPORT-AA1.md sha256 1df40044e8c12422 ; RAPPORT-AA2.md sha256 890e9874f8b73e4c ; scripts et sorties work_aa1/, work_aa2/ (empreintes au sceau NOTE-199-200-SCEAU.txt)"
---

# Concordance de l'audit AF

## 0. Deroulement
Deux auditeurs isoles (Opus 5.5), sans interruption. AA-1 : cecite stricte, scripts propres (720 equations de contrainte, 210 jets elimines). AA-2 : adverse ; reproduction octet pour octet de la sortie de reference ; 12 variantes, dont une verification independante de toute la chaine par un Omega explicite quadratique (s = 1/5 non nul) et des champs polynomiaux (12/12 egalites exactes).

## 1. Criteres
| Critere | AA-1 (cecite stricte) | AA-2 (adverse) | Concordance |
|---|---|---|---|
| K-1 partie ln de T = sigma x Lin(D, dD) ; Omega^1 de That = -c0 b E^n | etabli : T = c0 b [-E^n/Omega - (n^d D_bda + n^c D_acb) + sigma (n^d D_bda + n^c D_acb + Omega d^c D_acb)] | etabli ; parametrisation generique (10 composantes) ; forme fermee conforme | **oui** |
| K-2 pole -kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho)/Omega, sans jets | etabli ; sans derivees de W, sans lambda ni s | etabli sur 24 composantes ; dans le repere de n, R(i,0,j) = -b c0 kappa E_ij/Omega seules | **oui** |
| K-3 logs nuls si D = dD = ddD = 0 | etabli ; les trois niveaux sont necessaires (D = dD = 0 laisse Omega^2 ln Omega) | etabli ; necessaire et suffisant ; **reserve** : div W = R = O(kappa b), la reinjection donne des termes kappa^2 b^2 lineaires en W, du type Omega^-1 ln Omega par comptage (non calcules) | **oui**, a l'ordre b sur div W = 0 |
| K-4 Maxwell, (2.17), annulation | **signe** : d^a F_ab = **-**4 e^2 beta_* n^a F_ab / Omega ; coefficient (6, 2) exact ; annulation ssi (EE + BB)_tf = 0 et E x B = 0 ; reels : E = B = 0 (la partie sans trace suffit) | meme correction de signe (v_E5_signe_maxwell) ; robustesse a une completion isotrope ou construite sur (eta, n) : (EE + BB)_tf = 0 reste impose (v_E5) ; argument de rang juste | **oui**, avec correction de signe |
| K-5 controles | (a) 8 b kappa e / Omega ; (b) coefficients de NOTE-98, **a condition de lire n_a = (1,0,0,0)** (indice bas) ; avec n^a tous les signes s'inversent | conformes ; calibration NOTE-125 = controle arithmetique d'entrees importees (e, cible), non derivation independante | **oui**, convention a preciser |
| K-6 sensibilite | (non demande) | sigma -> Omega, 1, Omega^2 : ni pole ni log ; b C^2 local seul : regulier ; beta_* = 0 ou sigma -> Omega : rien ; identite du ln en defaut seulement par trace (via s) ou symetrie de paires | **oui** |

## 2. Apports des auditeurs, retenus
- **Poids anomal (AA-2, E4)** : avec C = Omega^p W_p, le pole electrique vaut -E (3 x p^2 - x - 2p + 2)/2, x = b c0 kappa, et un pole magnetique (p - 1) B apparait. Aucun p constant ne retire le pole pour W generique. Pour B = 0, p = 1 + b c0 kappa + O(b^2) retire le pole electrique et le transfere au canal magnetique. Une redefinition W' = W + ln Omega X l'echange contre un log. Le « seulement si » vaut **pour le choix d'inconnues de Friedrich** (W de poids 1).
- **Exposant (AA-2, E6.6)** : sur un mode homogene purement electrique, (2.17) se reduit a -d_0 E_ij = -b c0 kappa E_ij / Omega + O(Omega^0), d'ou E = E0 Omega^{b c0 kappa}. Avec c0 = -8 (convention de Carroll-Wald, NOTE-128), on obtient **E proportionnel a Omega^{-8 b kappa}**, exposant et signe de G-V3 (W proportionnel a Omega^{-epsilon}, epsilon = 8 b kappa H^2, NOTE-138 v4, a H = 1 ; « Weyl rescale croissant »). Le poids anomal formel p - 1 = b c0 kappa = -8 b kappa est la dimension anormale gamma = 8 de NOTE-133. **Recoupement independant** : le coefficient du pole formel redonne, par simple integration, la dimension anormale calculee par transport (NOTE-133) et l'exposant de la litterature (NOTE-135, 148, 153). C'est une exponentiation de l'ordre b, pas une preuve de la resommation.
- **Partie principale (AA-2, E2)** : le second membre contient des derivees de W (452 termes en jets d'ordre 1 a Omega^0 apres reduction), par exemple -(b c0 kappa/2) d_0 E11 dans R(1,0,1). La partie principale est donc modifiee a l'ordre kappa b (facteur regulier 1 - kappa b c0/2, non degenere). Le systeme n'est pas litteralement du type du theoreme 3.1 (second membre sans derivees) ; le pole, lui, ne contient aucun jet.
- **Distinction formel / sur solution (AA-2, E6.8)** : les alternatives « ou E^n = 0 au bord », « ou F = 0 au bord » sont des enonces sur solution, a retirer des enonces formels.

## 3. Corrections (aucune ne renverse le resultat)
- D1 : equation de Maxwell rescalee : d^a F_ab = -4 e^2 beta_* n^a F_ab / Omega (+4 e^2 beta_* n^a F_ba / Omega). Le script etait juste ; la note et l'enonce K-4 de la consigne AA-1 portaient la coquille.
- D2 : logs de G-V3 : « nuls a l'ordre b sur la couche div W = 0 ». La reinjection de div W = R donne des termes d'ordre kappa^2 b^2, lineaires en W, du type Omega^-1 ln Omega par comptage ; ils ne sont pas calcules.
- D3 : partie principale modifiee a l'ordre kappa b ; « du type du theoreme 3.1 » a nuancer.
- D4 : « seulement si » pour les inconnues de Friedrich ; poids anomal et transfert electrique vers magnetique.
- D5 : retirer « ou E^n = 0 / F = 0 au bord » des enonces formels ; « aucun champ electromagnetique non nul a scri » est une consequence sur solution.
- D6 : requalifier comme importes ou non calcules : concordance avec NOTE-128 (That, S-b), calibration NOTE-125 (controle arithmetique), lien a NOTE-133 (vrai au premier ordre en b, loi de puissance par exponentiation, cf. §2), mecanisme de compensation de NOTE-113, cadre C-M1.
- D7 : convention : n_a = (1,0,0,0) (indice bas) dans les controles ; ligne d'impression « (and its first derivatives) » a lire « jusqu'aux derivees secondes » ; real_sols non imprime (l'argument de rang fait foi, verifie par AA-1 et AA-2).

## 4. Verdict
**AU-V2.** Concordance sur K-1 a K-6 ; le resultat central est retrouve en cecite stricte et resiste a l'audit adverse (y compris une verification independante de toute la chaine) ; une coquille de signe (D1), une convention a preciser, des corrections de portee D2 a D6. **Prediction AU-V2 realisee.**
Precedent (xv) : une consigne d'audit doit donner la position des indices des vecteurs (n_a ou n^a) et reprendre les signes **de la sortie du script**, pas de la note.

## 5. Consequences (acte NOTE-200)
NOTE-197 v2 (corrections D1 a D7) ; NOTE-163 v3 (point de lecture G-CAL-a remplace par l'enonce formel, pas 2 bis, recoupement de l'exposant) ; NOTE-138 v5 (phrase formelle dans le libelle de G-V3) ; S27-02 v4 §H (M-V3 au sens formel, sous C-M1).

## 6. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. G-V3 candidat ; M-V3 candidat conditionnel ; RG-4 refutee a titre provisoire ; CCC + M ouverte ; noyau {A4 ; A2★ ; N} inchange.
