---
id: NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE
numero: 100
serie: I
branche: Q-M3 suite (audit)
reservation: 2026-10-10T12:17 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 100)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-99-ARMEMENT-AUDIT-CHAMP-COHERENT (sha256 58b35dce573141e49261aeb5c8e9fcb803b1ec8e3e838f1753034c006b2cb627, 2026-10-10T12:18:57Z)
rapport: RAPPORT-CSE-CHAMP-COHERENT-AUDIT-AVEUGLE.md
depend: [NOTE-BORD-EON-99-ARMEMENT-AUDIT-CHAMP-COHERENT, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
rouvre_si:
  - "determination de l'echelle infrarouge du terme non local de S_flat pour un champ coherent a 𝓘⁺ (point ouvert OP-IR)"
  - "calcul a k fini (mode hors horizon) avec la prescription a⋆ = k/M de S2"
---

# NOTE-100 : audit froid aveugle de NOTE-98. Verdict **AU-V2**

## 0. Resume
Les deux auditeurs concordent **entierement sur le calcul** (Q-1 a Q-4) : le second membre de (2.17) porte, sous C-iso, un ln Ω de coefficient κβ̃B₀²/e², et le budget anisotrope requis est exactement l'oppose de la partie logarithmique du secteur Maxwell. L'**argument de symetrie** (Q-5) est juge **valide sous hypotheses nommees** ; C-b en ajoute une, decisive, que NOTE-98 n'avait pas nommee comme telle (H5 : echelle infrarouge du terme non local de S_flat). Prediction du gel (AU-V2, reserve sur S_flat et l'etat de l'operateur non local) **realisee**.

## 1. Concordance

| Resultat porteur | C-a | C-b | Etat |
|---|---|---|---|
| Q-1 secteur Maxwell, trace nulle, divergence | identique | OK | **concordant** |
| Q-2 trace anomale | identique | OK ; controle de NOTE-98 **tautologique**, remplace par une vraie variation metrique (ctrl1), concordante | **concordant, corrige** |
| Q-3 ln Ω dans (2.17), coefficients | identique | reproduit | **concordant** |
| Q-4 budget = −Π_M | identique, famille complete (+ c/s sans effet) | confirme, ansatz elargi | **concordant, renforce** |
| Q-5 argument de symetrie | valide sous 6 hypotheses | lemme valide sous H1-H4 ; conclusion exige **H5** ; lemme faux hors H1 (Euler-Heisenberg) mais terme en ln inchange | **valide sous hypotheses, precise** |

## 2. Corrections et precisions a porter sur NOTE-98
1. **Controle de trace** : le « controle independant » du script v3 est tautologique (meme formule). Le vrai controle est ctrl1 de C-b (variation metrique explicite), concordant.
2. **C-iso n'est pas un choix** : c'est le cas isotrope general (toute partie isotrope homogene conservee de trace fixee a cette forme) (C-b A5).
3. **Lemme d'isotropie restreint a H1** : hors de la classe « Ω[g] fonctionnelle de la seule metrique », la completion d'Euler-Heisenberg (Ω_F = −¼ ln(F·F/M⁴)) rend le secteur non Maxwell anisotrope (Π constant, −βB₀²s²/(6e²)), **sans changer le terme en ln de (2.17)**. Le resultat porteur survit ; l'enonce intermediaire « secteur non Maxwell isotrope » doit etre restreint.
4. **H2** : la definition de Ω[g] par Δ₄⁻¹ en de Sitter doit exclure les modes nuls anisotropes de Δ₄ (x² − z², s·x, …) en imposant Ω = −ln s exactement.
5. **H3** : causalite in-in ; noyau retarde ; tranche initiale homogene requise ; isotropie preservee.
6. **H5, point ouvert OP-IR** : pour un champ strictement uniforme (k = 0), le terme non local −β̃ F log(−∂²/M²) F de S_flat est mal defini. Avec une echelle infrarouge comobile (a⋆ constant, choix du script), le ln a persiste et la conclusion tient. Avec une echelle physique (par ex. H), un ln a anisotrope oppose apparait et **annule exactement** celui du secteur Maxwell : il n'y a plus rien a compenser. NOTE-98 §6 point 3 (« ne change pas la dependance en ln a ») est **trop fort** : il ne vaut qu'avec une echelle comobile.
7. Budget restreint au cas diagonal homogene axisymetrique ; T_{0z} exclu par parite (a dire).

## 3. Contre-point consigne (non tranche) [derive]
La formule exacte de S2 pour les metriques Weyl-plates, eq. (2.12), s'ecrit `1 − β̃ log(−∂² /(M² e^{2Ω(x)}))` : le couplage court avec l'impulsion **physique** k/a, sans coupure en H, ce qui est attendu pour des fermions sans masse conformement couples (ils ne voient du fond que le facteur conforme). Pour un mode a k fini, la prescription comobile de S2 (a⋆ = k/M) s'applique et le ln a persiste ; le cas k = 0 est une limite singuliere ou la prescription infrarouge n'est pas fixee par S2. Ce contre-point n'est pas audite ; il oriente la suite (OP-IR) sans la trancher.

## 4. Verdict
**AU-V2** : concordance totale sur les resultats calcules (Q-1 a Q-4) ; Q-5 valide sous hypotheses H1 a H5 nommees ; corrections §2. NOTE-98 est maintenue (CB-V2 qualifie CB-V3) avec cette lecture : **le ln Ω dans (2.17) est etabli dans le modele de S2 avec une echelle infrarouge comobile ; sa survie pour un champ coherent reel depend de OP-IR**.

## 5. Portee sur Q-M3 et CCC + M
Le candidat M-V3 de NOTE-98 reste **conditionnel**, et ses conditions sont maintenant completes : modele de S2, echelle infrarouge comobile du terme non local (ou mode a k fini selon la prescription de S2), completion covariante dans la classe H1-H4 ou de type Euler-Heisenberg, lineaire, fond fixe. Rien n'est grave. RG-4 inchangee.

## 6. Greffes proposees (non entees)
- **CB-a** : NOTE-98 §3, restreindre « secteur non Maxwell isotrope » a la classe H1 ; ajouter H2 a H5 ; §6 point 3 : « ne change pas la dependance en ln a avec une echelle infrarouge comobile ; question ouverte OP-IR sinon ».
- **CB-b** : chantier suivant possible : refaire NOTE-98 pour un mode a k fini hors horizon avec la prescription a⋆ = k/M de S2, ce qui evite la singularite k = 0 et teste directement OP-IR.

## 7. Non-surclassement
[conv], audite a froid (AU-V2), non scelle comme resultat. Aucune incompatibilite gravee. Noyau {A4 ; A2★ ; N} inchange.
