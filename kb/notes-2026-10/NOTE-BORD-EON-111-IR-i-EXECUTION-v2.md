---
id: NOTE-BORD-EON-111-IR-i-EXECUTION
numero: 111
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-i)
reservation: 2026-10-11T15:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 111)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 7f8597f1edf6be3b17195d262cfc57327790d7e11bef19e96bf97f394a17b543 (conservee)"
greffe: "IR-m-a entee le 2026-10-11 par NOTE-BORD-EON-121 (corrections de l'audit froid aveugle NOTE-120, AU-V2)"
audit: "NOTE-BORD-EON-119 (gel) / NOTE-BORD-EON-120 (concordance) : AU-V2, resultats porteurs confirmes (I-A retrouvee en cecite stricte par M-a1)"
gel: NOTE-BORD-EON-110-ARMEMENT-IR-i (sha256 e44b4f05a5a374baa330d5c74ad1853c819574cd4b32657847df06c624eeab00, 2026-10-11T15:14:15Z)
instruments:
  - "ir_i.py, sha256 060efdf85b2213f64cb3e485ee325bcad618d34291c543b7770cf44d7b4e4972, 2026-10-11T15:16:00Z : EXIT 0, sortie ir_i_sortie.txt ; DEFAUT D'ETIQUETTE (voir §1)"
depend: [NOTE-BORD-EON-110-ARMEMENT-IR-i, NOTE-BORD-EON-108-IR-g-EXECUTION, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
verdict: "I-V1 qualifie I-V3"
prediction_realisee: "oui"
rouvre_si:
  - "fermeture non Maxwell anisotrope fixee par un modele (partie (b) de NOTE-98 pour une source inhomogene)"
  - "ordres superieurs en s, retroaction, ordres superieurs en beta"
---

# NOTE-111 : IR-i, version inhomogene. Verdict **I-V1 qualifie I-V3** (v2 : voir greffe)

> **Greffe IR-m-a (v2, 2026-10-11).** Corrections issues de l'audit froid aveugle NOTE-120 (AU-V2). Les resultats porteurs sont inchanges : la loi locale a l'ordre s⁰ et les gradients en s ln s ont ete retrouves en cecite stricte par M-a1, et etendus hors diagonale par M-b.
> 1. **Coefficients libres** (§2A) : « aucun dans un coefficient de log » vaut **a l'ordre s⁰**. Le test de ir_i.py ne le prouvait pas : il derive en β avant de chercher les symboles libres, alors que ceux-ci sont independants de β. Fondement correct, par M-b [derive, controle] : div X^M|₀ + T̂/s = 0, de sorte que X^R obeit a un systeme hyperbolique a coefficients constants et a source lisse ; sous H-loc, **X^R ne contient donc aucun log, a tous les ordres**. Sur les 60 coefficients libres, 6 sont des donnees de Cauchy et 54 (ordres j ≥ 3) des artefacts de la troncature de la conservation.
> 2. **Bornes des regions** (§2B) : les integrales portent sur r < D − 6w, abs(r − D) < 6w et r > D + 6w, et non 3w comme etiquete.
> 3. **Prediction de la coquille** (§2B, §5) : la valeur 21,36 etait un artefact de quadrature (∫m̈² evalue a 2,1243 au lieu de 32/15). La prediction exacte est (4/5)·4π·4/(15w³) = **21,4466**. L'ecart reel avec l'integrale calculee (21,4462) est de −1,8·10⁻⁵, et non de 0,4 %. **L'explication par un « melange statique-rayonne » est retiree.**
> 4. **Ajout** (§3) : les structures statique (1/5) et rayonnee (4/5) sont de **meme signe**. L'integrale sur toutes les regions egale la prediction rayonnee a 10⁻⁹ pres : le reliquat statique positif est compense par les termes croises d'induction dans la coquille (M-b). M-a1 retrouve la coquille exactement : J = 16/(75w³) a 2·10⁻⁶ pres.
> 5. **Script** (§1) : drapeau final a lire True (confirme par M-b) ; variable « termes negatifs en s » a lire « termes en s ln s » ; le test diagonal accepte ±ref (signe non impose) ; test des libres aveugle (point 1) ; etiquettes des bornes (point 2). Script conserve tel quel (R-55).

## 0. Resume
Sous une fermeture locale isotrope du secteur non Maxwell (H-loc), la loi de NOTE-108 vaut **point par point** : a l'ordre s⁰, le coefficient de ln s dans R_{isi}(x) est (3βκ/e²) × partie sans trace de Q(x) = B_iB_j − E_iE_j, sans aucune moyenne. Les gradients n'entrent qu'a l'ordre s ln s, et les 60 coefficients libres de la fermeture ne touchent aucun log. Pour un dipole magnetique eteint a η = −D, la carte de 𝓘⁺ a trois regions :
- une boule r < D vide de champ, donc sans log ;
- une coquille rayonnee r ≈ D, ou le log est anisotrope ;
- un reliquat magnetostatique r > D, ou le log est porte par le champ magnetique.

La reserve est la meme qu'en NOTE-98 et NOTE-92 : une contrainte anisotrope non Maxwell d'ordre s² ln s pourrait compenser le log, et le cadre ne la fixe pas.

## 1. Incident d'instrument (R-55)
La ligne « loi locale verifiee … : False » de la sortie est un **defaut d'etiquette** : la variable nommee « termes negatifs en s » contient en realite les termes **positifs** en s (ordre s ln s). Les trois composantes signalees (0,0,1), (2,1,2), (3,1,3) ont un coefficient de ln s **nul a l'ordre s⁰** ; leurs termes sont des corrections de gradient d'ordre s ln s. Le drapeau aurait du etre vrai. Le script est conserve tel quel ; la lecture correcte est donnee ici. [ajout IR-m] Lecture confirmee par l'audit M-b (drapeau corrige : True). Autres defauts releves par l'audit : test diagonal sans signe impose ; test des coefficients libres aveugle ; bornes des regions mal etiquetees (greffe points 1, 2, 5).

## 2. Resultats [calcule] (ir_i_sortie.txt)

### A. Loi locale (mode mixte non moyenne, fermeture H-loc)
52 equations de conservation aux ordres controles, 108 inconnues, solution trouvee, 60 coefficients libres.

| Composante | Coefficient de ln s a s⁰ | Ecart a (3βκ/e²) Q_tf(x) |
|---|---|---|
| R_xsx | −κ(k²u₀² sin²kx − c² cos²kx)/e² | 0 |
| R_ysy | −κ(k²u₀² sin²kx + 2c² cos²kx)/e² | 0 |
| R_zsz | +κ(2k²u₀² sin²kx + c² cos²kx)/e² | 0 |
| autres composantes | 0 | sans objet |

(Facteur β omis, comme dans la sortie.) Ici B(x)² = k²u₀² sin²kx et E(x)² = c² cos²kx : la loi vaut avec les valeurs **locales**.
- Gradients : premiers termes en s ln s, proportionnels a ∂_x(B²) et ∂_x(E²) (par exemple, coefficient de ln s dans R_(0,0,1) : exactement −(κ s/e²) ∂_x(B² − E²)).
- Termes suivants dans R_xsx : ordre s² ln s.
- Coefficients libres de la fermeture : **aucun** dans un coefficient de log **a l'ordre s⁰** [corrige IR-m : le test du script etait aveugle ; fondement structurel, X^R sans log a tous les ordres sous H-loc, voir greffe point 1].

### B. Dipole magnetique eteint (D = 10, w = 1/2, m₀ = 1)
Les equations de Maxwell sont verifiees exactement en un point generique (div B, Faraday, Ampere : 0).

| Region a 𝓘⁺ | abs B | abs E | B·E | norme de Q_tf | ln dans (2.17) |
|---|---|---|---|---|---|
| r = 3 (boule deja traversee) | 2·10⁻¹² | 2·10⁻¹² | 0 | 8·10⁻²⁴ | non |
| r = 10, 45° (coquille) | 0,015 | 0,0071 | 0 | 2,1·10⁻⁴ | oui |
| r = 10, equateur | 0,0095 | 0,0100 | 0 | 1,3·10⁻⁴ | oui |
| r = 20 (reliquat) | 2,0·10⁻⁴ | 2·10⁻¹⁸ | 0 | 3,2·10⁻⁸ | oui |

Forme radiale : B = α(r)(3n n_z − ẑ) + γ(r)(n n_z − ẑ), E = ε(r) n × ẑ, controlee en un point generique (ecart ~10⁻⁷⁶). Moyennes angulaires des parties sans trace (unite diag(−⅓, −⅓, ⅔)) :

| Structure | Moyenne |
|---|---|
| statique (3n n_z − ẑ)² | **1/5** |
| rayonnee (n n_z − ẑ)² − (n × ẑ)² | 7/15 + 1/3 = **4/5** (retrouve NOTE-108 D1) |

Integrales radiales de Q_tf (composante zz) :

| Region | Integrale | Prediction |
|---|---|---|
| boule r < D − 6w [corrige IR-m] | 1,2·10⁻⁸ | 0 |
| coquille abs(r − D) < 6w [corrige IR-m] | 21,4462 | **21,4466** (rayonnement pur, (4/5)·4π·4/(15w³)) ; ecart −1,8·10⁻⁵ [corrige IR-m : la valeur 21,36 et l'ecart de 0,4 % venaient d'une erreur de quadrature ; explication par le melange retiree] |
| reliquat r > D + 6w [corrige IR-m] | 3,8108·10⁻⁴ | 3,8132·10⁻⁴ (statique pur, (1/5)·4π/(3 r³_min), r_min = D + 6w) |
| toutes regions [ajout IR-m] | 21,4466058 | 21,4466058 (prediction rayonnee, a 10⁻⁹) |

Domaine de l'action plate : abs(B)·r² = m₀/r = 0,08 a r = 20 ; condition r ≫ m₀.

## 3. Lecture [derive]

```
            𝓘⁺ (repere conforme), dipole eteint a eta = -D
   ┌──────────────────────────────────────────────────────────┐
   │   reliquat r > D : B statique, E = 0   -> ln, structure 1/5 │
   │      ┌──────────────────────────────────────┐            │
   │      │ coquille r ≈ D : E ⊥ B rayonne       │ -> ln, 4/5  │
   │      │      ┌──────────────────────┐        │            │
   │      │      │ boule r < D : vide   │ -> pas de ln         │
   │      │      └──────────────────────┘        │            │
   │      └──────────────────────────────────────┘            │
   └──────────────────────────────────────────────────────────┘
   D = rayon de Hubble comobile au moment de l'extinction
```

1. **I-1** : oui. Pres de 𝓘⁺, les derivees en s dominent les gradients d'un facteur 1/(ks) ; chaque point evolue comme un univers homogene a l'ordre dominant. La loi homogene se transporte donc localement, a la fermeture pres.
2. **I-2** : la boule r < D (le rayon de Hubble comobile a l'extinction) est videe par l'onde d'extinction. Il n'y a pas de log a l'interieur ; il y en a partout ailleurs ou le champ subsiste.
3. **I-3** : la coquille redonne (4/5)(mm − ⅓m²)·∫m̈² ; le reliquat donne (1/5)(mm − ⅓m²)·4π/(3r³). Les deux structures sont de meme signe ; sur l'ensemble des regions, le reliquat est compense par les termes croises d'induction de la coquille, et le total egale la prediction rayonnee [ajout IR-m].
4. **I-4** : **non teste**. NOTE-98 (Q-4, audite AU-V2) montre qu'un budget anisotrope Π d'ordre s² ln s, exactement oppose a la partie logarithmique du secteur Maxwell, annulerait le log. L'argument de symetrie qui l'excluait (NOTE-98 §3) repose sur l'homogeneite (H4), violee ici. Pour une source inhomogene, la partie (b) de la completion ∫Ω[g]F² peut etre anisotrope. H-loc reste donc une hypothese.

## 4. Verdict
**I-V1 qualifie I-V3.**
- I-V1 : sous H-loc, la loi R_ln(x) = (3βκ/e²) Q_tf(x) tient point par point a l'ordre s⁰ ; les gradients sont en s ln s et la fermeture libre ne touche pas le log. Pour le dipole, le log existe partout ou le champ est non nul a 𝓘⁺ et s'annule dans la boule deja traversee par l'onde d'extinction.
- Qualification I-V3 : la fermeture du secteur non Maxwell n'est pas fixee pour une source inhomogene ; une contrainte anisotrope peut compenser le log.

## 5. Confrontation a la prediction
Prediction (NOTE-110 §4) : « I-V1 qualifie I-V3 ; loi locale a s⁰, gradients en s ln s ou plus haut ; boule vide, coquille 4/5, reliquat 1/5 ; compensation possible sans H-loc ». **Realisee.** [corrige IR-m] L'integrale de la coquille concorde avec la prediction de rayonnement pur a 1,8·10⁻⁵ pres ; l'ecart de 0,4 % annonce en v1 venait d'une erreur de quadrature de la prediction, et l'explication par le melange statique-rayonne est retiree.

## 6. Portee
- Pour un champ coherent reel (localise), la question de la regularite de (2.17) devient : **la fermeture du secteur non Maxwell est-elle localement isotrope ?** C'est la meme question qu'en NOTE-92 (contrainte anisotrope libre), maintenant posee pour un champ localise.
- M-V3 reste conditionnel ; une condition est ajoutee : H-loc. Rien n'est grave. RG-4 inchangee.

## 7. Greffes proposees (non entees)
- **IR-k** : calculer la partie (b) de la completion de Riegert ∫J δΩ[g]/δg pour une source J = √g F² statique dans le repere conforme et localisee, pour voir si elle fournit la contrainte anisotrope compensatrice (teste H-loc).
- **IR-j** : audit froid aveugle de NOTE-108 (demande, en cours) ; l'etendre a NOTE-111 si utile.

## 8. Non-surclassement
[conv], audite par NOTE-120 (AU-V2) [corrige IR-m]. Premier ordre en β, fond fixe, cadre S2 + [21], fermeture H-loc. Noyau {A4 ; A2★ ; N} inchange.
