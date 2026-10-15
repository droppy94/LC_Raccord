---
id: NOTE-BORD-EON-175-ARMEMENT-CAL-F
numero: 175
serie: I
branche: Chantier D / critere (2.17) (calibration CAL-F)
reservation: 2026-10-15T14:40 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 175)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant toute lecture : calibration de l'emploi de l'equation (2.17) de Friedrich dans le corpus sur le cas connu (scalaire massif, theoreme 3.1 de 1311.0700), puis application a un gaz de Dirac massif"
decision: "operateur (Thierry), 2026-10-15 16:26 heure de Paris : « merci de continuer le programme en attendant » (accord general de poursuite ; chantier choisi par l'assistant, motif §0)"
---

# Gel CAL-F : le critere (2.17) tel qu'employe par le corpus reproduit-il le theoreme 3.1 de Friedrich ?

## 0. Motif (declare, informe)
Le corpus juge la regularite au raccord par l'equation (2.17) de Friedrich (arXiv:1311.0700v2), R_rho nu lambda = Omega^-1 (nabla_nu L_lambda rho - nabla_lambda L_nu rho), L = (kappa/2)(T - (1/3) g trT), avec la regle de comptage de NOTE-131 (auditee NOTE-137) : T ~ s^p Y, Y lisse ⟹ R ~ s^(p-2) ; pole ssi p = 1 et Y(0) != 0. Cette regle porte G-V3 (pole (8 b kappa/Omega) W_E) et, depuis la greffe G-D1 (NOTE-174), l'obstruction invariante de l'electron.
En preparant un croisement avec S27 (le 15 octobre, avant ce gel), l'assistant a applique de tete cette regle au **scalaire minimalement couple homogene a la masse de Friedrich m^2 = 2H^2** : h = phi0 s + phi1 s^2, a^2 rho = (3/2)H^2 phi0^2 + 4H^2 phi0 phi1 s + ..., d'ou un terme R ~ s^-1 non nul si phi0 phi1 != 0. Le theoreme 3.1 dit au contraire que le systeme couple est regulier exactement a cette masse. **Ou bien le calcul de tete est faux, ou bien la regle de comptage n'est pas le critere de Friedrich complet (termes de matiere supplementaires, convention de T, role des equations couplees).** Le cas du scalaire est le seul ou la reponse est connue : il sert de calibration.

## 1. Questions figees
- **F-0 (source).** Lire 1311.0700v2 au texte : forme exacte de (2.17) et des equations conformes avec matiere (quels termes de matiere, quel T : T* = Omega^-2 T ou autre ; homonymie signalee NOTE-90) ; comment Friedrich obtient les termes (m^2 - 2 lambda/3) Omega^-k pour le scalaire (theoreme 3.1 et sa preuve).
- **F-1 (calibration).** Le scalaire homogene minimalement couple, traite avec (2.17) tel que le corpus l'emploie, donne-t-il un terme singulier pour m^2 = 2H^2 ? Si oui, quel terme ou quelle convention manque pour retrouver le theoreme 3.1 ? Si non, ou est l'erreur du calcul de tete ?
- **F-2 (Dirac).** Avec le critere calibre, un gaz homogene de particules de Dirac massives au repos a temps tardif (poussiere, rho ~ m n0 a^-3) donne-t-il un terme singulier dans le systeme de Friedrich ? Ordre en Omega, residu.
- **F-3 (consequences).** Effet sur (i) la regle de NOTE-131 et donc G-V3 ; (ii) G-D1-b et le fondement de RG-4 ; (iii) la Prop. 4(b) de l'article v2.1 (condition m a bornee) traduite dans le critere calibre.

## 2. Espace de verdicts
- **CAL-V0** : source inaccessible ou illisible sur le point (F-0 non tranche) ; pause.
- **CAL-V1** : calibration reussie sans amendement (calcul de tete faux) ; la regle de NOTE-131 reproduit le theoreme 3.1 ; F-2 traite avec elle.
- **CAL-V2** : la regle de NOTE-131 est incomplete pour une matiere massive (terme ou convention manquant), mais l'amendement ne change pas G-V3 (source conforme, sans masse) ; F-2 traite avec le critere amende.
- **CAL-V3** : l'amendement change aussi le traitement de G-V3 ; alerte : la chaine G-V3 (NOTE-125 a 162) est a reexaminer sur ce point, et la synthese NOTE-163 ne peut pas etre remise en l'etat.
- Composite nomme au verdict si necessaire.

## 3. Prediction (informee, precedent ix ; ne vaut pas pari a l'aveugle)
**CAL-V2** : Friedrich traite le scalaire avec ses equations couplees completes (le scalaire entre aussi ailleurs que par L), et les termes (m^2 - 2 lambda/3) Omega^-k s'y annulent ; la regle de NOTE-131, etablie pour des sources conformes (sans trace, ou de trace imposee), reste valide pour elles. Pour la poussiere de Dirac (F-2), prediction : terme singulier a residu proportionnel a m n0, d'ordre au moins Omega^-1. Incertitude declaree elevee sur la separation CAL-V2 / CAL-V3.

## 4. Firewall
- FW-1 : ne pas « corriger » la regle de NOTE-131 sans source lue ; toute citation de 1311.0700 est verbatim (extraits archives).
- FW-2 : ne rien changer a G-V3, a NOTE-163 ni a G-D1 dans ce chantier ; les consequences sont proposees en greffes, entees par acte distinct.
- FW-3 : un calcul symbolique de controle est obligatoire pour F-1 et F-2 (script scelle avec la sortie).
- FW-4 : si F-0 montre que l'assistant a mal compris les conventions du corpus (hats, poids de T), le dire et refaire F-1 avec les conventions exactes avant tout verdict.
- FW-5 : audit froid aveugle avant entee de toute greffe (precedent x).

## 5. Sources
S-F1 : H. Friedrich, « Smooth non-zero rest-mass evolution across time-like infinity », arXiv:1311.0700v2 (deja lue au corpus, S26-02, NOTE-90, NOTE-123) ; relecture ciblee §2 et §3. Corpus : NOTE-90, NOTE-131, NOTE-137, NOTE-163.

## 6. Non-surclassement
Rien de grave. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
