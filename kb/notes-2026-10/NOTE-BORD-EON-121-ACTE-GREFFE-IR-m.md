---
id: NOTE-BORD-EON-121-ACTE-GREFFE-IR-m
numero: 121
serie: I
branche: Q-M3 suite (greffe IR-m)
reservation: 2026-10-11T17:46 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 121)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
nature: "acte d'entee de greffes (aucun calcul, aucune lecture nouvelle, pas de gel requis)"
decision: operateur (Thierry), 2026-10-11 19:46 heure de Paris : « Enter les trois greffes (IR-m-a, b, c) en versions v2 de 111, 116 et 118, avec un acte de greffe sous le numero 121 »
depend: [NOTE-BORD-EON-120-AUDIT-IR-m-CONCORDANCE, NOTE-BORD-EON-114-ACTE-GREFFE-IR-d3]
---

# NOTE-121 : acte d'entee des greffes IR-m-a, IR-m-b, IR-m-c (corrections de l'audit NOTE-120)

## 1. Regle suivie
Meme regle que NOTE-109 et NOTE-114 :
- les versions anterieures sont conservees intactes ;
- chaque note corrigee recoit une nouvelle version avec en-tete (`version`, `remplace`, `greffe`, `audit`) ;
- un encadre de greffe est place en tete de la nouvelle version ;
- chaque passage touche porte une marque `[corrige IR-m]` ou `[ajout IR-m]`.

Aucun resultat porteur n'est modifie ; aucun verdict ne change.

## 2. Table des greffes

| Greffe | Note | Version source (sha256) | Nouvelle version (sha256) | Corrections (NOTE-120 §2) |
|---|---|---|---|---|
| IR-m-a | NOTE-111 | v1 7f8597f1edf6be3b… | **v2** 5c252635af896f60… | 1 coefficients libres hors des logs a s⁰ seulement, fondement structurel (X^R sans log sous H-loc) ; 2 bornes D ∓ 6w ; 3 prediction de la coquille 21,4466 (et non 21,36), ecart −1,8·10⁻⁵, explication par le melange retiree ; 4 structures de meme signe, total egal a la prediction rayonnee ; 7 defauts du script ir_i.py |
| IR-m-b | NOTE-116 | v1 8436e99a79bc0b3c… | **v2** 88766f74e2010036… | 4 enonce « Q_tf = 0 si et seulement si la composante E ℓ = 2 ponderee s'annule » ; helicite ni necessaire ni suffisante si partielle ; deux sources a Q_tf = 0 ajoutees au tableau (p ∥ m en phase ; p = x̂ + iŷ, m = x̂ − iŷ) ; condition dipolaire STF Re(pp†) = STF Re(mm†) ; 5 moyenne de l'interference asymptotique et globale |
| IR-m-c | NOTE-118 | v1 17d0fd95a495d414… | **v2** 5248e3d3dd1c6ef3… | 6 qualifications de K-V3 remplacees par K-D1 (lissite de W), K-D2 (fond fixe, terme φC²), K-D3 (regularite de W sur les modes a impulsion nulle) ; « famille diagonale » et « ψ causal et lisse » retirees ; « W hors orbite » reformule ; 8 T_2 = T_3 n'est pas un controle (forme covariante) ; pistes IR-n (levee pour T^(b)), IR-o (reformulee), IR-r (ajoutee) |

## 3. Etat consolide de la chaine du canal anomal (versions en vigueur)
- **Audites** :
  - NOTE-92 (par NOTE-94) ;
  - NOTE-98 (par NOTE-100) ;
  - NOTE-102 v3 et NOTE-104 v2 (par NOTE-106 v3) ;
  - NOTE-108 v2 (par NOTE-113) ;
  - **NOTE-111 v2, NOTE-116 v2 et NOTE-118 v2 (par NOTE-120)**.
- **Non audites** : NOTE-90 (critere de regularite) et NOTE-96 (lecture de S2).
- Critere consolide : dans le cadre S2 + [21], premier ordre en β, fond fixe, R_isj |_{β ln s, s⁰} = (3βκ/e²)(Q_ij − ⅓δ_ij tr Q)(x), point par point. Le ln Ω de (2.17) est present si et seulement si la partie sans trace de B_iB_j − E_iE_j a 𝓘⁺ est non nulle. Pour une source causale, cela revient a une composante E ℓ = 2 ponderee non nulle (5 conditions), cas generique.

## 4. Effet sur M-V3 et sur les pistes
- M-V3 reste un **candidat renforce, non grave**. Conditions en vigueur :
  - cadre S2 + [21] ;
  - premier ordre en β ;
  - fond fixe sans retroaction (K-D2) ;
  - lissite et regularite de W (K-D1, K-D3) ;
  - source causale generique ;
  - (2.17) comme critere pertinent (IR-q).
- Pistes :
  - IR-n levee pour T^(b) ;
  - IR-o reformulee (regularite de W) ;
  - IR-r ouverte (retroaction metrique) ;
  - IR-e, IR-h, IR-p, IR-q inchangees.
- Greffe anterieure toujours **non entee** : « Correction NOTE-111 » de la reprise du 2026-10-11 (§6.3), qui lie NOTE-111 §0 et §3 I-4 a NOTE-118 (H-loc levee pour le coefficient du log). Elle n'entre pas dans le perimetre de cet acte. NOTE-111 v2 garde donc le texte de la v1 sur ce point, et c'est NOTE-118 v2 §4 qui fait foi.

## 5. Non-surclassement
Acte editorial, [conv]. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.
