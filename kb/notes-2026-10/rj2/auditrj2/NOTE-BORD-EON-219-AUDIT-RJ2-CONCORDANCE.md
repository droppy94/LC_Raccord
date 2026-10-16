---
id: NOTE-BORD-EON-219-AUDIT-RJ2-CONCORDANCE
numero: 219
serie: I
branche: Chantier D (audit RJ2)
reservation: 2026-10-16T16:37:05Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 219)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-218-ARMEMENT-AUDIT-RJ2.md (sceau NOTE-218-SCEAU.txt, 2026-10-16T19:47:41Z, pose avant lancement)"
rapports: "RAPPORT-RB1.md, RAPPORT-RB2.md, work_rb1/, work_rb2/ (empreintes au sceau NOTE-219-SCEAU.txt)"
---

# Concordance de l'audit RJ2

## 0. Deroulement
RB-1 : derivation independante en cecite stricte (seul Friedrich 2016 accessible), scripts propres, deux jauges (decalage nul et trace spatiale nulle ; synchrone conforme). RB-2 : audit adverse, reexecution des scripts (sorties reproduites a l'identique), controles positifs ajoutes, calcul de la courbure de la metrique conforme sur la solution d'ordre epsilon^2.

## 1. Constats concordants (etablis independamment par les deux)
| Point | RB-1 | RB-2 | Statut |
|---|---|---|---|
| tau = Omega T_c pour Omega quelconque | Q1 etabli (g_c plate et non plate) | relu, reexecute | confirme |
| Partie singuliere m (psibar psi) n n / \|n\|^2, tout repere ; K = i m nslash/(n.n) (meme matrice) | Q2 etabli | R8 | confirme |
| Termes croises nuls dans psibar psi (pas dans psibar gamma psi) | Q3 etabli | relu | confirme |
| nabla Omega . nabla Omega = -lambda/3 sur scri, exposant constant | Q4 etabli (sous Omega s -> 0, verifie a epsilon^2) | R6 | confirme |
| Lapse nul sur scri | Q5 etabli | C3 (Phi(0) seulement par (3.3)) | confirme |
| Aucun logarithme ni pole a epsilon^2 | Q5 (jusqu'a Omega^7 symbolique, Omega^9 numerique, deux jauges) | reproduction | confirme |
| Aucune resonance du spineur a epsilon^3 ; seul canal possible : lapse moyen sur scri | Q5, q5_canaux (h generique) | PC1, PC1b, PC1c (detecteurs vivants) | confirme |
| Classe a un seul exposant : geometrie en series entieres, stable a epsilon^3 | Q6 etabli | « tient » | confirme |
| Argument a tous les ordres : formel, conditionnel | Q7 plausible (S1 vide non lineaire, S2 convergence, S3 existence ouverte) | C1, C2 (H2 hypothese nouvelle) | confirme comme conditionnel |

## 2. Erreur et divergence
- **E1 (RB-2, erreur sur un resultat ecrit).** NOTE-217 affirme que, dans la classe generique, « la geometrie a une limite a scri, oscillations a partir de l'ordre 1 ». Dans la jauge du test (longitudinale, Omega = -eta), le Schouten conforme L_00 = Psi'' - (q^2/3)(Phi + Psi) et R[g_c] oscillent a l'ordre 0 : bornes sans limite. L'etape 3 de l'argument formel supposait une equation d'evolution pour toute inconnue ; L_00 est fixe par (3.5) via d_Omega s et perd un ordre.
- **Divergence apparente avec RB-1.** RB-1 trouve, dans sa jauge (decalage nul, trace spatiale nulle, Omega fixe), une metrique conforme oscillante seulement a partir de Omega^{4 +- 2 i mu}, donc L et R a partir de Omega^2, W a partir de Omega^1 : toute la geometrie a une limite.
- **Resolution (verifiee par calcul ecrit, a confirmer par script en v2).** A Omega fixe comme fonction de coordonnee, une transformation de jauge de composante xi^eta non nulle change le facteur conforme : h -> h + L_xi eta + 2(xi^eta/Omega) eta (signe corrige apres RB-3, M1 ; sans incidence sur les ordres). Passer de la jauge longitudinale a celle de RB-1 demande xi^eta d'ordre Omega^{3 +- 2 i mu}, soit un changement de facteur conforme theta = 1 + O(Omega^{2 +- 2 i mu}), dont le hessien retire exactement l'oscillation d'ordre 0 de L. Les deux resultats sont justes ; ils portent sur deux facteurs conformes differents. **La regularite de la geometrie generique depend du choix du facteur conforme**, c'est-a-dire de la regle de raccord elle-meme (RB-2, portee).

## 3. Autres constats retenus
- E2 (rj2_ops.py, co-repere inverse dans dirac_op) : erreur sans incidence (premier ordre sur fond plat ; dirac_op non utilise par le test) ; a corriger.
- E3 : « H_ij TT ordre min 3 (particulier) » faux : Omega^3 est l'exposant homogene ; la reponse particuliere commence a Omega^4 (generique) ou Omega^5 (un seul exposant).
- C2 et C8 : H2 n'est pas « le cas formel de Friedrich » (jauge comobile, R prescrit, geodesiques conformes, seconde regularisation) ; « aucune relation regularisante » vaut pour les seconds membres de matiere seulement.
- C3 : Psi(0) = 0 vient des contraintes d'Einstein, pas de (3.3).
- C4 : psi_3 non construit ; le critere a n = 0 suffit pour l'absence de logarithme a epsilon^3 (RB-1 et RB-2) ; controles positifs a integrer.
- C6 : diversite des tests surestimee (deux mu equivalents par structure ; k1 orthogonal a k2, normes egales, coplanaires ; secteurs +-2k sans oscillation).
- C7 : « continue, pas C^1 » vaut pour W ; metrique C^1 non C^2 ; L et R selon le facteur conforme.
- C9 : texte propose pour la Rem. 2(4) a restreindre.
- RB-1 : rho = m psibar psi sans signe fixe en general ; positif dans la classe a un seul exposant (seule classe ou l'hypothese rho-hat >= 0 de Friedrich est automatique).
- RB-1 S3 : dans la classe a deux exposants, tau est continu non C^1 a scri ; le theoreme lisse de Friedrich ne s'applique pas tel quel.

## 4. Verdict
**AU-V3** au sens du gel (§2) : une erreur sur un resultat ecrit (E1), confirmee par calcul. Elle **ne renverse pas** le resultat principal (classe a un seul exposant preservee, absence de logarithme et de resonance a epsilon^3, lapse nul sur scri), etabli independamment par les deux auditeurs ; elle **remplace** la clause generique par un enonce dependant du facteur conforme. **Prediction AU-V2 non realisee.**

Verdict scientifique propose pour NOTE-217 v2 : **RJ2-V1 restreint.** (i) Classe a un seul exposant preservee par le couplage : formel sous H1, H2 (reformulee, jauge conforme incluse) ; perturbatif a epsilon^3 sur de Sitter, etabli par deux calculs independants. (ii) Classe generique : sans pole ni logarithme a epsilon^3 ; W continu non C^1 ; la limite du Schouten et de R depend du facteur conforme (aucune dans la jauge longitudinale ; limite dans la jauge de RB-1 a epsilon^2).

## 5. Suite
NOTE-217 v2 avec corrections E1 a E3, C1 a C9 et un script v2 (courbure de g_c dans les deux jauges, controles positifs, vecteurs d'onde generiques) ; re-audit court par un agent isole ; puis decision de l'operateur sur l'entee (acte NOTE-220).

## 6. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. Noyau {A4 ; A2★ ; N} inchange.

## 7. Re-audit court RB-3 (ajout du 2026-10-16)
Consigne PROMPT-REAUDIT-RB3.md scellee avant lancement (REAUDIT-RB3-SCEAU.txt, 2026-10-16T20:46:04Z). Verdict : **la v2 peut etre entee** ; aucune erreur restante parmi les points audites ; script v2 verifie contre une derivation independante (Riemann, Ricci, Schouten, Weyl 4D, jauge B, controle positif, source totale) ; changement de facteur conforme theta = 1 + O(Omega^{2 +- 2 i mu}) verifie par calcul (xi^eta d'ordre Omega^3 ; ecart de Schouten = moins le hessien de xi^eta/Omega ; Weyl inchange). Corrections appliquees en v2 avant sceau final : K1 (phrase proposee pour la Rem. 2(4)), K2 (renvoi de l'etape 2), M1 (signe au §2 ci-dessus), remarques C5, secteurs +-2k, liberte residuelle de la jauge B. Remarques non appliquees : PC2 (controle positif geometrique de RB-2) non integre au script ; courbure calculee avec donnees libres nulles et une seule valeur de mu.
