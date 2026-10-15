---
id: NOTE-BORD-EON-193-AUDIT-FW3-CONCORDANCE
numero: 193
serie: I
branche: CCC + M (audit FW3)
reservation: 2026-10-15T16:54:14Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 193)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-192-ARMEMENT-AUDIT-FW3.md sha256 7a403b7a0073a3a9 (sceau NOTE-191-192-SCEAU.txt, 2026-10-15T16:54:32Z, pose avant lancement)"
rapports: "RAPPORT-FA1.md sha256 0ac10cf6c3eb2992 ; RAPPORT-FA2.md sha256 22a1ce0acada7905 ; scripts et sorties work_fa1/, work_fa2/ (empreintes au sceau NOTE-193-194-SCEAU.txt)"
controle: "ctrl193/fw3_check_215corrige.py (577bee4c0391f363) et sortie (f2bc7166a850ce9f, identique octet pour octet a fw3_check_sortie.txt)"
---

# Concordance de l'audit FW3

## 0. Incident de procedure (consigne)
Les deux auditeurs ont ete lances sur le modele Fable 5.1. Une limite de quota de ce modele a interrompu les deux agents vers 17:10 UTC. **FA-1** avait deja ecrit son rapport complet (verdict compris) ; seule sa reponse finale manque. **FA-2** avait execute ses variantes E2 a E5 sans rediger de rapport. Une seconde instance FA-2 (meme role, meme consigne, meme perimetre de lecture, modele Opus 5.5) a repris le dossier `work_fa2/` : elle a relu le code de maniere critique, re-execute les variantes (sorties `work_fa2/rerun/`, identiques), ajoute trois variantes (E1, E2b, E4b) et redige le rapport. L'isolement est preserve : aucune des deux instances n'a lu FA-1, ni les notes 190 et 192. Consigne : la reprise d'un auditeur interrompu par son propre dossier de travail est admise, a condition de la declarer en tete du rapport (fait).

## 1. Criteres
| Critere | FA-1 (cecite stricte) | FA-2 (adverse) | Concordance |
|---|---|---|---|
| K-1 courants Omega^4 ; courant de Higgs sans dOmega | derive et verifie (scripts propres) | Higgs : verifie (calcul reel) ; Dirac et YM : la partie (A) du script est un **comptage de poids code a la main**, pas une verification (E6-4) | **oui** ; requalification de la partie (A) |
| K-2 coefficient Omega^-2 de Higgs = m^2 + 4 lambda xi - 2 lambda/3 | retrouve | retrouve ; formule fermee pour un poids w quelconque : coefficient m^2 + 4 lambda xi - (lambda/3) w(3 - w), terme Omega^-1 = 2(w - 1)(n.D h + w s h) | **oui** |
| K-3 (2.17) : plus basse puissance Omega^-2, coefficient (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) Sum phi_i^2 n_[nu eta_lambda]rho, sans A, F, lambda_h, y | retrouve a l'aveugle (main + sympy) | retrouve par calcul a la main independant (2 beta + alpha n.n) et par `var_E5` (Ghat via (2.3), sans le code de la note) ; la part xi vient de Ghat f (-2/3) et de l'amelioration (+2), total 4/3 | **oui** |
| K-4 Omega^-1 nul a la condition, tout xi | retrouve : coefficient (kappa/6)(m^2 + 4 lambda xi - 2 lambda/3) nabla_[nu(Sum phi_i^2) g_lambda]rho | verifie (C2, E2, choix de variable eliminee indifferent) ; exemple (kappa/18)(12 lambda xi - 2 lambda + 3 m^2)(Sum phi dphi_1) | **oui**, et forme explicite du coefficient Omega^-1 obtenue a l'aveugle |
| K-5 Dirac : y H_r ; ghat Lag_D d'ordre Omega^2 contre Omega^1 | retrouve, connexion de spin recalculee a partir de Gammahat, tenseur cinetique avec jauge = Omega^2 T_r | identites hors couche verifiees ; le « controle a masse constante » de la partie (D) est une arithmetique ad hoc (resultat exact) | **oui** ; requalification du controle |
| K-6 variante Omega^2 Y_ab + deux composantes | (non demande) | **verifie** (`var_E3` (b)) : meme coefficient avec Sum sur les quatre composantes reelles, Omega^-1 nul, ni Y ni A ni lambda_h dans les coefficients singuliers | **oui** |

## 2. Constats propres a chaque auditeur, retenus
- **E1-a (FA-2), erreur reelle, sans incidence.** Dans (2.15), le facteur devant nablahat That est Omega^-1, non Omega. FA-2 l'etablit par identite (derivation de (3.8) et (2.14)). La lecture du corpus (NOTE-181 §2 : « - (kappa/24) Omega^-1 nabla T_hat ») etait correcte ; l'erreur est entree dans `fw3_check.py` et dans la consigne PROMPT-AVEUGLE-FA1, ou j'ai mal transcrit l'extrait de Friedrich (« κ/24Ω » lu comme (κ/24)Ω). **Controle independant (ctrl193)** : la correction du facteur dans une copie du script donne une sortie identique octet pour octet. FA-2 (E2 (ii)) le confirme dans sa bibliotheque. Le terme est d'ordre Omega^0 (forme juste) et n'entre dans la source qu'a travers des facteurs O(Omega^2).
- **E3c (FA-2), sensibilite.** La procedure detecte une singularite Omega^-1 residuelle a la condition pour mu phi^3, mu |H|^3 et un terme de type Majorana (modele M Omega eta B) : elle n'est pas aveugle.
- **E4 (FA-2), « seulement si ».** Aucun poids conforme ne retire tous les termes singuliers hors condition (seul w = 1 annule Omega^-1, et il impose la condition ; les exposants de dS Delta(3 - Delta) = M2 sont retrouves) ; le coefficient ne depend que de |H_r|^2, donc aucune jauge, meme singuliere, ne le retire ; a kappa = 0, la condition reste necessaire par l'equation de Higgs.
- **E2b (FA-2), non-circularite.** Avec xi != 0, les termes en dd Omega s'annulent exactement dans le tenseur d'amelioration ; s n'entre dans That qu'a l'ordre Omega, Str a l'ordre Omega^2 ; le point fixe Str = (A + Omega s B)/(1 - Omega^2 C) est regulier.
- **Reserve de convention (FA-1).** Si l'on elimine H^dagger boxhat_D H par l'equation de Higgs, le coefficient de K-3 est multiplie par (1 - 4 xi) ; la condition d'annulation est inchangee (a xi = 1/4, l'equation de Higgs reste singuliere). Le resultat formel de NOTE-191 est en jets, sans usage de l'equation de matiere, comme chez Friedrich.

## 3. Corrections a porter (forme, aucune sur le resultat)
- C1 : (2.15) avec facteur Omega^-1 ; signaler que la correction ne change aucun coefficient (ctrl193, E2).
- C2 : « mu = 0 automatique par invariance de jauge » remplace par « par invariance de jauge et polynomialite du potentiel (un terme |H|^3 produirait une singularite Omega^-1, E3c) ».
- C3 : dans l'equation de Higgs, « T* = Omega^-2 That » designe la trace (Str), non T*_ab.
- C4 : partie (A) (poids YM, courant de Dirac) et « controle a masse constante » requalifies en comptages de poids, non en verifications symboliques.
- C5 : doublet et tenseur cinetique de Dirac dans la partie C : etablis par l'audit (K-6), non par le script.
- C6 : limites maintenues : groupe non abelien (argument, non verifie), Weinberg (suffisance, non calcule), (2.16) et (2.13)-(2.15) argumentes non calcules, Yukawa ecrit avec h_r reel (structure chirale y H psibar P_R psi + h.c. de memes poids), theoreme 3.1 reproduit pour V = m^2 phi^2/2 + lambda_h phi^4.
- C7 : coefficient explicite de Omega^-1 (FA-1) a inscrire.
- Mineure : duree d'execution 43 s ici, 54 s chez FA-2.

## 4. Verdict
**AU-V2.** Concordance sur K-1 a K-6 ; le resultat central est retrouve en cecite stricte (FA-1) et resiste a l'audit adverse (FA-2, dont un calcul a la main independant) ; une erreur reelle de transcription (C1), sans incidence et controlee ; corrections de forme C2 a C7. **Prediction AU-V2 realisee.**
Precedent consigne : la consigne d'audit reprend les formules du gel ; une erreur de transcription de la source s'y propage. Desormais, recopier les equations de la source dans la consigne a partir de l'extrait archive et en verifier la coherence mutuelle par un script avant le gel (FA-2 E1 en donne le modele).

## 5. Consequences (acte NOTE-194)
NOTE-191 v2 (corrections C1 a C7, v1 conservee) ; greffe G-M2 sur S27-02 (v3) : reserve FW-3 levee pour le systeme couple classique. Article : proposition v2.4 maintenue, non entee dans cet acte.

## 6. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. CCC + M ouverte ; p_Q non fixe, N non chiffre, noyau {A4 ; A2★ ; N} inchange.
