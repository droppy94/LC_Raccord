# Rapport RB-3 : re-audit court et adverse de NOTE-217 v2

Auditeur isolé, consigne PROMPT-REAUDIT-RB3.md. Date : 2026-10-16.

## 0. Périmètre et méthode

**Pièces lues (et elles seules)** : NOTE-BORD-EON-217-RJ2-EXECUTION.md (v1), NOTE-BORD-EON-217-RJ2-EXECUTION-v2.md (v2), RAPPORT-RB1.md, RAPPORT-RB2.md, NOTE-BORD-EON-219-AUDIT-RJ2-CONCORDANCE.md, /home/claude/RJ2/rj2_ops.py, rj2_test_v2.py, rj2_series.py, et les six sorties /home/claude/RJ2/v2runs/*.txt. Aucun autre fichier de /home/claude n'a été ouvert (ni rj2_test.py v1, ni rj2_ops_check.py, ni les sceaux, ni work_rb1/, ni work_rb2/).

**Empreintes vérifiées** : la v1 a bien le sha256 9fdf5d619104418d... annoncé dans l'en-tête de la v2.

**Travail dans work_rb3/** (copies ; aucun original modifié) :

| Script | Objet | Sortie |
|---|---|---|
| `rb3_courbure_check.py` | formules de courbure linéaire du script v2 contre une dérivation indépendante ; tests Schouten et Weyl | `rb3_courbure_check_sortie.txt` |
| `rb3_signe_jauge.py` | loi de transformation de h sous un difféomorphisme, Omega = -eta fixe | `rb3_signe_jauge_sortie.txt` |
| `rb3_e2_check.py` | co-repère inverse corrigé (E2) | `rb3_e2_check_sortie.txt` |
| `rb3_geo.py` | copie exacte des lignes 1 à 187 de rj2_test_v2.py, plus sauvegarde de la géométrie | `rb3_geo_long_gen.txt`, `rb3_geo_B_gen.txt`, `*.pkl` |
| `rb3_equiv.py` | les solutions j = ±2 des deux jauges sont-elles reliées par un xi, et lequel ? | `rb3_equiv_sortie.txt` |

**Reproduction** : relancée (mu = 13/10, générique, vecteurs « gen »), la partie géométrique est identique ligne à ligne à `run_generique_long_gen.txt` et à `run_generique_B_gen.txt` (bloc « secteur ... » jusqu'à « geometrie : fin », durées exclues).

## 1. Synthèse

| # | Classe | Objet |
|---|---|---|
| (néant) | erreur | **aucune** dans la v2 sur les points audités |
| K1 | correction | texte proposé pour la Rem. 2(4) : « conformal curvature » désigne usuellement le Weyl, dont la limite ne dépend pas du facteur conforme ; « test-field background » est inexact ; il manque « four Dirac modes » |
| K2 | correction (mineure) | étape 2 : la condition sur le décalage à scri renvoie à l'étape 1, qui ne protège que le lapse |
| M1 à M9 | remarques | voir §5 (dont une erreur de signe dans NOTE-219, sans incidence sur la v2) |

**Verdict R4** : la v2 **peut être entée**. Aucune erreur ne subsiste parmi les points audités. La phrase destinée à l'article (K1) doit être reformulée avant toute v2.6. La retouche de l'étape 2 (K2) est souhaitable mais ne modifie aucun résultat.

## 2. R1 : traitement des constats de NOTE-219

| Constat | Traitement dans la v2 | Jugement |
|---|---|---|
| E1 (limite de la géométrie générique) | §2 étape 3 réécrite (une inconnue fixée par contrainte, L_00 via (3.5), perd un ordre) ; tableau §3 par jauge ; verdict §4 restreint ; §6 consigne l'erreur | **correct** ; sorties concordantes (§3 ci-dessous) |
| E2 (co-repère inverse) | rj2_ops.py l.53 : `eta*h` | **correct** : E·Ed = Id + O(eps²), Ed·E idem, Ed^T eta Ed = eta + eps h (`rb3_e2_check_sortie.txt`) ; la v1 donnait bien le défaut [[0,h01,h02,h03],[-h01,0,0,0],...] |
| E3 (Omega³ de H_ij) | §3 : exposant homogène TT ; réponse forcée à partir de Omega⁴ (générique) ou Omega⁵ (un seul exposant) | **correct** ; `run_unexposant_long_gen.txt` : H en Omega³, Omega⁵ |
| C1 (verdict surclassé) | « RJ2-V1 restreint », conditions H1, H2 reportées dans le verdict | **correct** |
| C2 (H2 n'est pas le cas de Friedrich) | H2 « hypothèse nouvelle, non démontrée, distincte » avec la liste des différences | **correct** |
| C3 (Psi(0) = 0) | attribué aux contraintes d'Einstein | **correct** |
| C4 (psi_3, contrôles positifs) | psi_3 déclaré non construit ; contrôle positif du lapse intégré au script et exécuté six fois | **correct**, partiel : le contrôle positif géométrique de RB-2 (PC2) n'est pas repris (M3) |
| C5 (jauge e_0 // grad Omega et jauge du test) | pas nommé ; la jauge B (décalage nul) et la discussion du facteur conforme y répondent en partie | **suffisant** (M4) |
| C6 (diversité) | jeu « gen » (k1.k2 = 2, normes 5 et 10) ; mu déclaré sans effet structurel | **correct** ; les secteurs ±2k restent sans oscillation dans « gen » aussi (non dit, M5) |
| C7 (continuité) | W continu non C¹ ; métrique C¹ non C² en jauge longitudinale | **correct** |
| C8 (relation régularisante) | restreinte aux seconds membres de matière ; Lemme 4.1 + jauge conforme chez Friedrich | **correct** |
| C9 (Rem. 2(4)) | texte restreint | **incomplet et partiellement fautif** : K1 |
| RB-1, signe de rho | §1 « Signe » | **correct** |
| RB-1, S3 | §5 « tau n'est pas C¹ à scri » | **correct** |

## 3. R2 : le script v2

### 3.1 Courbure de g_c (rj2_test_v2.py l.261 à 293)

Schéma vérifié symboliquement contre une dérivation indépendante, pour h générique (dix fonctions de quatre variables) :

| Élément | Vérification | Résultat |
|---|---|---|
| Riemann linéarisé, `Riem(a,b,c,d)` = ½(∂_b∂_c h_ad + ∂_a∂_d h_bc − ∂_a∂_c h_bd − ∂_b∂_d h_ac) | égal à η_ae(∂_c Γ^e_bd − ∂_d Γ^e_bc), 256 composantes | exact |
| Ricci R_bd = η^{ac} R_abcd (1re et 3e) | convention R^a_bad | correcte |
| Schouten 4D, L = ½(Ric − R g/6) | h = 2σ η donne L_ab = −∂_a∂_b σ, R = −6 □σ | exact |
| Weyl, C = Riem − (g∧L) | h = 2σ η donne C = 0 ; C sans trace, symétries et Bianchi cyclique pour h générique | exact |
| W = C/Omega | `shift(-1)` | correct |
| Dérivées | ∂_eta = −∂_Omega, ∂_i = i q_i | correctes |
| Formules de RB-2, jauge longitudinale | R = 2q²Φ − 4q²Ψ − 6Ψ'' ; L_00 = Ψ'' − (q²/3)(Φ + Ψ) | retrouvées exactement |

En plus : L_11 = q²(Φ − 2Ψ)/3 et L_22 = −q²(Φ + Ψ)/6 (q selon x), sans Ψ''. Seul L_00 porte l'oscillation d'ordre 0. L'attribution « (L_00) » de la v2 est donc juste. Le script v2 ne l'imprime pas lui-même (il agrège les composantes de L), mais `rb3_equiv_sortie.txt` le confirme par composante : L_00 oscille à l'ordre 0, L_0i à l'ordre 1, L_ij à l'ordre 2.

### 3.2 Jauge B

`names = Phi, H11..H33`, Psi = S = 0, trace de H nulle : h_00 = −2Φ, h_0i = 0, h_ij sans trace. C'est bien la jauge de RB-1 (décalage nul, trace spatiale nulle, lapse libre). Quatre conditions pour quatre degrés de jauge. Le secteur q = 0 est identique dans les deux jauges, comme attendu.

### 3.3 Jeu « gen », contrôle positif, source totale

- « gen » : k1 = (1,2,0), k2 = (0,1,3), non orthogonaux, de normes différentes. La condition N(k) = N(−k) est vérifiée par l'assertion l.46. Les secteurs ±(k1 − k2) et ±(k1 + k2) oscillent ; les secteurs ±2k ne contiennent que j = 0.
- Contrôle positif : `h_00 += −2` à l'ordre 0, soit Φ(0) = 1, injecté dans le premier secteur. Il est détecté dans les six exécutions : (−1, ±1) en générique, (−1, +1) seulement en un seul exposant. C'est cohérent avec RB-1 (P±S = −(μ/2)H_00 P±C).
- Source totale par cible : la somme sur les couples (q, m) avec k' = k_m + q est correcte, et la cible est évaluée même pour un couple de source vide. Les 16 cibles donnent 0 résonance. En jauge B, il y a 32 couples non vides au lieu de 36 : dans chaque secteur ±2k1, un mode a une source identiquement nulle. Ce n'est pas un défaut.

### 3.4 Les sorties disent-elles ce que la v2 en tire ?

| Énoncé de la v2 (tableau §3) | Sorties | Concordance |
|---|---|---|
| Aucune résonance (systèmes ε² compatibles) | « ok » partout, six exécutions | oui |
| Φ(0) = 0 ; jauge B : Φ en Omega³ | long : Φ nmin 1 ; B : Φ nmin 3 | oui |
| Potentiels, long : Φ, Ψ en Omega^{2±2iμ}, S en Omega³, H en Omega⁴ ; B : tout en Omega^{4±2iμ} | `ordre minimal des termes oscillants` | oui |
| R[g_c] : long, oscillation à l'ordre 0 ; B, à partir de 4 | BILAN : R 0 / R 4 | oui |
| L : long, ordre 0 ; B, à partir de 2 | L 0 / L 2 | oui |
| W : limite, oscillation à partir de 1, dans les deux jauges | W 1, ordre min de W 0 dans les deux | oui |
| Un seul exposant : aucun terme oscillant | « aucune » pour R, L, W et la métrique | oui |
| Source ε³ : 0 résonance, aucune puissance < −1 | BILAN par couple et par cible | oui |
| Contrôle positif vivant dans les six exécutions | oui | oui |

## 4. R3 : erreurs, surclassements ou contradictions introduits

### 4.1 « theta = 1 + O(Omega^{2±2iμ}) » : juste, et vérifié par calcul

À Omega = −eta fixé comme fonction de coordonnée, j'ai établi la loi de transformation par calcul (`rb3_signe_jauge_sortie.txt`) :

h → h + L_xi eta + 2 (xi^eta/Omega) eta

La partie difféomorphisme L_xi eta ne change aucune courbure linéaire sur fond plat. Seule la partie conforme σ = xi^eta/Omega agit, avec ΔL = −∂∂σ, ΔR = −6□σ et ΔC = 0.

Pour chaque secteur oscillant et pour j = ±2, j'ai résolu h^B − h^L = L_xi eta + 2σ eta (`rb3_equiv_sortie.txt`) :

```
secteur          xi existe ?   xi^eta commence a   sigma commence a   Delta L = -dd sigma
(-1,-3,-3) j=±2      oui          Omega^3              Omega^2              vrai
(-1,-1, 3) j=±2      oui          Omega^3              Omega^2              vrai
( 1, 1,-3) j=±2      oui          Omega^3              Omega^2              vrai
( 1, 3, 3) j=±2      oui          Omega^3              Omega^2              vrai
```

Les seuls paramètres libres de xi sont aux ordres 7 et 8 (artefacts de troncature) : xi est unique aux ordres utiles. Le facteur conforme change donc par θ = 1 + σ, avec σ = O(Omega^{2±2iμ}). Son hessien est d'ordre Omega^{0±2iμ} et retire exactement l'oscillation d'ordre 0 de L_00 (et de R). C'est la lecture (2) de la v2, désormais confirmée par script, ce que NOTE-219 §2 demandait.

```
jauge longitudinale --(xi^eta ~ Omega^{3+-2i mu} ; theta - 1 ~ Omega^{2+-2i mu})--> jauge B
   L_00 : Omega^{0+-2i mu}        -  dd theta  ~ Omega^{0+-2i mu}         L_00 : Omega^{4+-2i mu}
   W    : inchange (invariance conforme a l'ordre lineaire)
```

### 4.2 « Il existe, à l'ordre ε², un facteur conforme où toute la géométrie a une limite » : juste, à préciser

Dans la jauge B, les oscillations commencent à l'ordre 4 pour la métrique, 2 pour L, 4 pour R et 1 pour W. W n'a pas de pôle : C = O(Omega). Les autres inconnues de Friedrich s'en déduisent. Exemple : en jauge B, □Omega = −Φ' au premier ordre, donc s oscille au plus tôt à l'ordre 3. La connexion est en ∂h, donc d'ordre Omega³. L'énoncé est donc vrai pour les configurations calculées. RB-1 l'établit aussi indépendamment, dans un autre secteur et avec d'autres k, et son argument algébrique (racines indicielles 0 et 3, source physique oscillante en Omega^{2±2iμ}, donc h en Omega^{4±2iμ}) le rend général à l'ordre ε² linéaire. Pas de surclassement, sous réserve de M6 et M7.

### 4.3 Autres points

- **K1 (correction), Rem. 2(4)** : « for generic solutions the limit of the conformal curvature at scri depends on the choice of conformal factor ». En usage courant, « conformal curvature (tensor) » signifie tenseur de Weyl. Or la limite du Weyl rescalé W ne dépend pas du facteur conforme : elle est identique dans les deux jauges, et l'invariance est exacte à l'ordre linéaire. Lue ainsi, la phrase contredit le résultat. Il faut écrire « the limits of the Schouten tensor and of the scalar curvature of the conformal metric ». Par ailleurs, « for a test-field background perturbed to third order » est inexact : le calcul porte sur le système couplé, développé en ε jusqu'à l'ordre 3, autour de de Sitter, et non sur un fond de champ test. Enfin, « four Dirac modes » manque, alors que C9 le demandait via RB-2. Proposition : « In a perturbative expansion of the coupled system about de Sitter space, to third order in the amplitude and for four Dirac modes, the coupling does not reintroduce poles or logarithms; the single-exponent class is preserved, with power-series geometry; for generic solutions the rescaled Weyl tensor has a limit at scri, while the limits of the Schouten tensor and scalar curvature of the conformal metric depend on the choice of conformal factor. A formal all-order version rests on an unproven solvability assumption. »
- **K2 (correction mineure), §2 étape 2** : « aucun terme forcé si le lapse et le décalage prennent leur valeur de de Sitter sur scri (étape 1) ». L'étape 1 ne protège que le lapse ; (3.3) ne fixe que g_c^{00}. La nullité du décalage sur scri relève du choix de coordonnées (complément de H1 : x^α transportés le long de ∇Omega). En outre, à l'ordre ε³, un décalage d'ordre 0 ne résonne pas (RB-1, tableau des canaux ; PC1c de RB-2). Il suffit de remplacer le renvoi par « (étape 1 pour le lapse ; choix de coordonnées H1 pour le décalage) ». La v1 ne posait pas la condition sous cette forme : la phrase est nouvelle en v2.
- Aucune contradiction interne relevée entre §2, §3, §4 et §5. La clause RG-4 (« géométrie continue à dérivées bornées » avec un facteur conforme adapté) est conforme aux sorties de la jauge B. Elle est même prudente : en jauge B, la métrique est C³ et L est C¹.

## 5. Remarques

- **M1. NOTE-219, signe.** NOTE-219 §2 écrit « h → h + L_xi eta − 2(xi^eta/Omega) eta ». Le calcul donne + 2(xi^eta/Omega) eta (`rb3_signe_jauge_sortie.txt`). C'est sans incidence sur les ordres, et la v2 ne reprend pas la formule. À corriger dans NOTE-219 ou dans l'acte, ou à préciser si xi^Omega = −xi^eta était visé.
- **M2.** L'équivalence de jauge (§4.1) ne vaut que pour les parties j = ±2, qui sont la réponse forcée et unique. Les parties j = 0 des deux exécutions diffèrent aussi par les données homogènes : les variables libres choisies par linsolve sont mises à 0 dans les deux cas, mais ce ne sont pas les mêmes données physiques. C'est sans effet sur les conclusions, qui portent sur les oscillations.
- **M3.** Le contrôle positif intégré porte sur le canal spinoriel (lapse). Aucun contrôle positif du calcul de courbure ni du détecteur géométrique (PC2 de RB-2) n'est intégré. Mon contrôle §3.1 couvre la courbure ; PC2 reste dans work_rb2 seulement.
- **M4.** C5 n'est pas nommé dans la v2. La jauge B (décalage nul, donc ∂_eta // ∇Omega) et la discussion sur le facteur conforme en traitent le fond.
- **M5.** Dans « gen » comme dans « orth », les secteurs ±2k ne portent que j = 0. Les oscillations ne passent que par ±(k1 ± k2) et q = 0. Il vaut la peine de le dire au §3 (3).
- **M6.** Toute la courbure v2 est calculée avec les paramètres libres nuls (les six exécutions en « zero »). Le bilan avec données libres non nulles (« v1, bilan inchangé ») ne couvre que les potentiels et la source ε³, pas R, L et W.
- **M7.** Les énoncés du tableau v2 reposent sur une seule valeur, mu = 13/10. L'équivalence 13/10 et 7/3 vient de la v1. C'est sans conséquence (RB-2 §4.4), mais à préciser.
- **M8.** « 4 solutions homogènes par secteur q non nul » vaut pour la jauge longitudinale. En jauge B, 7 paramètres atteignent les ordres ≤ 6 : 4 physiques et 3 de jauge résiduelle, ce qui est cohérent avec RB-1.
- **M9.** La correction E2 ne change pas dirac_op au premier ordre sur fond plat : Ed multiplie une connexion de fond nulle. Je n'ai pas eu accès à rj2_ops_check.py pour en vérifier la réexécution, qui n'est d'ailleurs pas requise.

## 6. Verdict (R4)

**La v2 peut être entée.** Les constats E1 à E3, C1 à C9 et les points RB-1 retenus sont traités, et traités correctement, à l'exception de C9 qui l'est incomplètement (K1). Le script v2 est correct : courbure linéaire, Schouten et Weyl 4D, jauge B, jeu « gen », contrôle positif, source totale. Ses sorties disent ce que la v2 en tire. Les deux énoncés nouveaux visés par R3 sont justes. Le changement de facteur conforme θ = 1 + O(Omega^{2±2iμ}), xi^eta = O(Omega^{3±2iμ}), est vérifié ici par calcul explicite. L'existence d'un facteur conforme où toute la géométrie a une limite à l'ordre ε² est établie pour les configurations calculées et générale à cet ordre par l'argument de RB-1.

Réserves avant l'acte : reformuler la phrase proposée pour la Rem. 2(4) (K1), corriger le renvoi de l'étape 2 (K2) et le signe de NOTE-219 (M1).

Non-surclassement : audit par IA, ne vaut pas lecture humaine.
