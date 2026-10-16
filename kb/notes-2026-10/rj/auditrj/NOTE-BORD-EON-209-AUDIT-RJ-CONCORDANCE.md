---
id: NOTE-BORD-EON-209-AUDIT-RJ-CONCORDANCE
numero: 209
serie: I
branche: Chantier D (audit RJ)
reservation: 2026-10-16T15:28:30Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 209)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-208-ARMEMENT-AUDIT-RJ.md sha256 1619fc386f4598ee (sceau NOTE-207-208-SCEAU.txt, 2026-10-16T15:29:12Z, pose avant lancement)"
rapports: "RAPPORT-RA1.md, RAPPORT-RA2.md, work_ra1/, work_ra2/ (empreintes au sceau NOTE-209-SCEAU.txt)"
---

# Concordance de l'audit RJ

## 0. Deroulement
Deux auditeurs isoles (Opus), sans interruption. RA-1 : cecite stricte, derivation complete par ses propres scripts (identite, noyau, tenseur de Dirac derive de l'action avec connexion de spin, numerique a m/H = 1.3). RA-2 : adverse ; reproduction octet pour octet de la sortie ; identite retestee pour Omega et T-hat arbitraires et une metrique conforme courbe ; conservation complete sur une superposition ; paquets ; sensibilite (m/H de 0.05 a 5, \|k\| de 0.1 a 10).

## 1. Criteres
| Critere | RA-1 | RA-2 | Concordance |
|---|---|---|---|
| K-1 identite et noyau | retrouvee independamment (meme A, ecrite avec tau au lieu de tau') ; noyau rho nu nu, rang 9 | exacte en toute generalite (fonctions arbitraires, g courbe) ; **S(rho U U, n) = rho Z de Friedrich exactement** pour U et n quelconques | **oui** ; lacune du §2 comblee |
| K-2 tenseur de Dirac | tau_00 = m B + Omega k.J, tau_0a = **-** Omega k_a N, tau_ab = (Omega/2)(k_a J_b + k_b J_a) ; spin-connexion nulle dans la partie symetrique | memes formules ; **signe de tau_0a inverse dans le script** ; le test de conservation du script (composante 0, mode unique) etait aveugle a ce signe ; test complet sur superposition : 1e-10 avec le signe physique | **oui**, correction de signe (D1) |
| K-3 limites de S/Omega | generique : borne, sans limite, c = 2m/H mesure ; **particule pure : serie entiere (Frobenius, phases compensees)** ; k = 0 : nul ; m = 0 : regulier | idem : **particule pure : tau analytique en Omega a tout ordre** ; la note confond le comportement de l'inconnue chi (phase a l'ordre Omega) et celui des bilineaires | **oui : resultat de la note sur la classe pure infirme** (D2) |
| K-4 equation pour chi, transformations | coefficient borne sans limite ; aucune V reguliere (monodromie, exposants +- i m/H) ; aucune V independante de k ; une V dependant de k et non reguliere (propagateur) annule le coefficient sans rien changer aux bilineaires | memes conclusions, memes clauses ; structure de Fuchs : exposants +- i m/H, difference non entiere | **oui**, enonce a restreindre (D3) |
| K-5 verdict et portee | aucun pole dans la source de (3.7) ; obstruction = interference des deux exposants de Fuchs ; classe reguliere : un seul secteur, k = 0, m = 0 | RJ-V2 confirme et renforce (la classe exceptionnelle exigee au gel existe) ; « plus aucun pole » a restreindre aux seconds membres Einstein (3.3) a (3.7) ; l'equation de matiere garde un pole de Fuchs (en u) ou une phase (en chi) | **oui** |
| K-6 sensibilite, completude | (non demande) | conclusions inchangees ; terme derivee de (3.7) borne, oscillant generiquement, regulier pour la classe pure ; (3.3) a (3.6) sans puissance negative de Omega ; courant de Dirac non au repos generiquement ; densite limite sans signe fixe ; §5 incomplet (FLRW, flot non geodesique, signe) ; FW-1 partiel, FW-4 au premier etage seulement | **retenu** (D4 a D7) |

## 2. Corrections
- **D1** : tau_0a = - Omega k_a N (convention e^{+ik.x}) ; sans effet sur S/Omega en module ni sur aucune conclusion. Script v2 (rj_check_v2.py) ; conservation complete : renvoi au test de RA-2 (superposition, 4 composantes, 1e-10).
- **D2 (erreur, classe pure)** : pour une solution a un seul exposant de Fuchs (particule pure ou antiparticule pure a la limite, paquets de meme type compris), **tous les bilineaires sont des series entieres en Omega** (u = Omega^{+- i m/H} fois une serie entiere) : tau_ab = O(Omega^2), tau_00 = m + O(Omega^2) (P4 de la v2 ; RA-2 C2). La phase n'est portee que par l'inconnue chi. La ligne « C^0, pas C^1 » de la note est fausse.
- **D3** : « aucun choix d'inconnue spinorielle ne la retire » vaut pour toute V reguliere ou toute V independante de k ; l'enonce invariant est : l'interference entre les deux exposants de Fuchs +- i m/H (phase relative de la Prop. 2(b)) est presente si et seulement si les deux composantes limites sont non nulles.
- **D4** : « plus aucun pole » vaut pour les seconds membres du secteur Einstein ((3.3) a (3.7), terme derivee compris) ; l'equation de Dirac reste singuliere pour toute inconnue reguliere (point singulier regulier de Fuchs en u ; phase en chi), y compris pour la classe pure. Le pole ou la phase est un choix d'inconnue ; l'invariant est la paire d'exposants.
- **D5** : l'absence de pole ne vient pas de la jauge U (S ne depend que de tau et de n = d Omega) mais de la domination de la masse (tau_0a, tau_ab = O(Omega) pour toute solution, le terme de masse s'eliminant ponctuellement dans psi-dagger {alpha_i, beta} psi = 0). Le courant de Dirac n'est pas asymptotiquement au repos pour une solution generique (vitesse J/N d'ordre 1, oscillante) : l'option « flot = courant de Dirac » du gel echoue generiquement ; la note a pris la normale de Hubble sans le dire.
- **D6** : la limite m(\|chi0+\|^2 - \|chi0-\|^2) n'a pas de signe fixe et peut s'annuler, alors que Friedrich utilise rho-hat >= 0 et rho > 0 sur scri ; l'analogie « poussiere + inclinaison reguliere » cesse quand elle s'annule.
- **D7** : verdict a etiqueter « premier etage (champ test, FW-4) » ; FW-1 en conformite partielle (§5 et §7 de Friedrich lus en debut seulement) ; §5 a completer : FLRW tendant vers de Sitter, flot de Dirac non geodesique, signe de la densite, couplage formel.

## 3. Verdict
**AU-V3 partiel**, au sens strict du gel : le critere K-3 est infirme sur la ligne « particule pure » et confirme par les deux auditeurs independamment (D2). L'erreur ne renverse pas le verdict du chantier ; elle le **renforce** : RJ-V2 tel que defini au gel (regularisation pour une classe exceptionnelle explicite) est etabli, la classe etant celle des solutions a un seul exposant de Fuchs, et k = 0. **Prediction AU-V2 non realisee.** Entee de NOTE-207 v1 suspendue ; NOTE-207 v2 integre D1 a D7.

## 4. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. RG-4 refutee a titre provisoire, raison reformulee (NOTE-207 v2 §7) ; noyau {A4 ; A2★ ; N} inchange.
