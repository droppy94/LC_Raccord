---
id: NOTE-BORD-EON-108-IR-g-EXECUTION
numero: 108
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-g)
reservation: 2026-10-11T13:49 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 108)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 925cf1530f32d03c08c208dae43d661cc75d0c23007f573b74fe8eee970dcc77 (conservee)"
greffe: "IR-d''' entee le 2026-10-11 par NOTE-BORD-EON-114 (corrections de l'audit NOTE-113, AU-V3 partiel)"
gel: NOTE-BORD-EON-107-ARMEMENT-IR-g (sha256 7bc4705105dd05a50bbe1e84c79fd0cd5b19ac58107c4b94f03864f642c4ae35, 2026-10-11T13:49:44Z)
instruments:
  - "ir_g.py, sha256 69496f141995e957fceeff25441fd499ce8c008bc224e5d412ea6ea1eb2208c4, 2026-10-11T13:50:56Z : EXIT 0, sortie ir_g_sortie.txt"
depend: [NOTE-BORD-EON-107-ARMEMENT-IR-g, NOTE-BORD-EON-106-AUDIT-OP-IR-CONCORDANCE, NOTE-BORD-EON-102-OP-IR-EXECUTION]
verdict: "G-V0 qualifie G-V3 (G5 seconde moitie suspendue puis corrigee, NOTE-113/114)"
prediction_realisee: "oui"
corrige: "NOTE-106 §0, §4, §5 : le critere est Q_sans_trace, pas ⟨F²⟩"
rouvre_si:
  - "traitement inhomogene de (2.17) pour un champ localise (Q_ij(x) local)"
  - "source persistante jusqu'a scri+ ; champ longitudinal (charges nettes)"
  - "retroaction, ordres superieurs en beta, etat non conforme"
---

# NOTE-108 : IR-g. Ce qui decide du ln Ω n'est pas « magnetique ou E = B ». Verdict **G-V0 qualifie G-V3** (v2 : voir greffe)

> **Greffe IR-d''' (v2, 2026-10-11).** Corrections issues de l'audit froid aveugle NOTE-113 (AU-V3 partiel) :
> 1. **Enonce retire** (§0, §2 schema, §3 qualification, §6) : « Q_tf survit pour tout champ coherent polarise ; il ne s'annule que pour un ensemble isotrope non polarise ». C'est **faux** : onde progressive circulaire, onde stationnaire helicoidale et faisceau non polarise anisotrope donnent Q = 0. **Critere exact** : le ln de (2.17) est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺ (NOTE-113) ; il s'annule pour une onde progressive circulaire, une onde stationnaire helicoidale a Q = 0, un faisceau non polarise, un ensemble isotrope ; il est present pour un reliquat magnetostatique, un dipole rayonne, une onde lineaire ou elliptique.
> 2. **Loi sous forme tensorielle** (§1.B) : R_isj |_{β ln s, s⁰} = (3βκ/e²)(Q_ij − ⅓δ_ij tr Q), composantes hors diagonale comprises ; convention s = −τ (en τ, le signe change) ; retrouvee a l'aveugle par J-a, sans contre-exemple sur 11 configurations (J-b).
> 3. **G1** (§1.A) : « exactement » devient « a l'ordre s² » (β ln s oscillant en X_sx a l'ordre s³, de moyenne nulle).
> 4. **G3** (§1.C) : avec Q moyenne spatiale, les facteurs sont ¼ (non ½) ; ε_Bε_B + ε_Eε_E = δ − k̂k̂ ; le terme en cos(2kD) alimente aussi Q_tf via (⅓𝟙 − k̂k̂) sauf distribution isotrope des k̂ ; decroissance x^−(n+2) pour n pair, x^−(n+1) pour n impair ; le poids spectral est celui de a²k².
> 5. **Script** : reference Q codee en diagonale (covariance non testee par ir_g.py, comblee par l'audit) ; controle de trace tautologique ; code mort ligne 94.
> 6. **Prediction** (§4) : la clause « nulle pour un ensemble isotrope non polarise » (comme seule annulation) etait fausse ; « realisee en tous points » devient « realisee sauf cette clause ».

## 0. Resume
Le calcul montre que la question posee n'etait pas la bonne. Le ln Ω de (2.17) est porte par la **partie sans trace** du tenseur

  Q_ij = ⟨B_iB_j − E_iE_j⟩ sur la tranche 𝓘⁺ (repere conforme),

selon la loi exacte, au premier ordre en β et pour la partie homogene sous C-iso :

  coefficient de ln s dans R_{isi} = (3βκ/e²) × (Q − ⅓ tr Q)_ii.

La trace de Q (c'est-a-dire ⟨F²⟩/2) ne contribue **pas** au ln de (2.17). Elle oscille selon le passage de Hubble a l'extinction de la source et se moyenne vers 0 pour une emission sous-Hubble. [corrige IR-d''' : la v1 disait ici que la partie sans trace survit pour tout champ coherent polarise et ne s'annule que pour un ensemble isotrope non polarise ; c'est faux, voir greffe point 1.] La partie sans trace decide : le ln est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf.

## 1. Resultats [calcule] (ir_g_sortie.txt)

### A. Quel morceau de X^M porte le log (mode mixte u₀ magnetique, c electrique)
Le coefficient de β ln s dans X^M, composante par composante et **sans moyenne spatiale**, est, a l'ordre s² [precise IR-d'''], **−2 (T_B − T_E)**, ou T_B et T_E sont les tenseurs de Maxwell construits avec la seule partie magnetique ou la seule partie electrique. Le terme croise de Poynting (s, x) n'a **pas** de log. Raison : le secteur magnetique est gele (X ∝ I²), le secteur electrique a I²u_s conserve (X ∝ 1/I²), et le produit croise ne porte que I² × I⁻² = 1.

### B. Traduction dans (2.17), partie homogene, C-iso
Avec ⟨B²⟩ = k²u₀²/2 (B selon z) et ⟨E²⟩ = c²/2 (E selon y), Q = diag(0, −⟨E²⟩, ⟨B²⟩) sur (x, y, z).

| Composante | Coefficient de ln s [calcule] | (3βκ/e²) Q_sans trace | Ecart |
|---|---|---|---|
| R_xsx | −κ(k²u₀² − c²)/(2e²) | idem | 0 |
| R_ysy | −κ(k²u₀² + 2c²)/(2e²) | idem | 0 |
| R_zsz | +κ(2k²u₀² + c²)/(2e²) | idem | 0 |
| partie isotrope (somme) | **0** | 0 | |

(Coefficients indiques au facteur β pres.) Cas E = B en module (c = ku₀) : R_xsx sans log, mais R_ysy = −3κk²u₀²/(2e²), R_zsz = +3κk²u₀²/(2e²). Le log survit.

### C. Source causale eteinte a η_off = −D (configuration magnetostatique)
A 𝓘⁺ : amplitude de B = ak cos(kD), amplitude de E = ak sin(kD). Par mode,

  Q = ½a²k² (ε_Bε_B − ε_Eε_E) + ½a²k² cos(2kD) (ε_Bε_B + ε_Eε_E),   [IR-d''' : ¼ au lieu de ½ si Q est la moyenne spatiale]

ou ε_B et ε_E sont les directions unitaires orthogonales de B et E.
- Premier terme : poids ½a²k², **independant de D**, deja sans trace.
- Second terme : poids cos(2kD). Il porte toute la trace (⟨F²⟩) et une partie sans trace.

Moyenne spectrale de cos(2kD) avec P(k) ∝ kⁿ e^{−k/k⋆}, x = 2k⋆D :

| n | ⟨cos 2kD⟩ | Decroissance pour x ≫ 1 |
|---|---|---|
| 2 | (1 − 3x²)/(1 + x²)³ | −3/x⁴ |
| 4 | (5x⁴ − 10x² + 1)/(1 + x²)⁵ | 5/x⁶ |
| 5 | (1 − 15x² + 15x⁴ − x⁶)/(1 + x²)⁶ | −1/x⁶ |

Emission super-Hubble (x ≪ 1) : ⟨cos 2kD⟩ → 1, champ a dominante magnetique. Emission sous-Hubble (x ≫ 1) : la trace et la partie en cos(2kD) s'eteignent en loi de puissance (au moins x^{−(n+1)}) ; il ne reste que le premier terme.

### D. Source coherente unique : dipole magnetique m
Moyenne sur les directions de k : ⟨ε_Bε_B − ε_Eε_E⟩ = **(4/5)(m m − ⅓ m² 𝟙)** (verifie exactement). Non nul, sans trace, aligne sur le dipole.
Ensemble isotrope d'orientations de m : moyenne **nulle**.

## 2. Lecture [derive]

```
                         tranche 𝓘⁺ (repere conforme)
  source eteinte a -D ──► B = ak cos kD,  E = ak sin kD   (par mode)
                                │
         ┌──────────────────────┴───────────────────────┐
   trace de Q  (= ⟨F²⟩/2)                        partie sans trace de Q
   poids cos(2kD)                               poids ½a²k² (fixe) + cos(2kD)·(...)
   → 0 si emission sous-Hubble                   survit si ⟨BB⟩_tf ≠ ⟨EE⟩_tf [corrige IR-d''']
   ne nourrit PAS le ln de (2.17)                nourrit le ln de (2.17) : 3βκ/e² × Q_tf
                                                 → 0 aussi pour onde circulaire,
                                                   helicoidale, faisceau non polarise
```

1. **G-1** : le log de X^M est −2(T_B − T_E) ; celui de (2.17) est la seule partie sans trace de Q. La trace (⟨F²⟩) alimente la partie isotrope de X^M et la trace anomale T̂, que la fermeture C-iso absorbe sans log.
2. **G-2** : la dependance en kD ne touche que la trace et un morceau de la partie sans trace. Le passage de Hubble decide si le champ est « magnetique » ou « E = B en moyenne », mais pas si le ln existe.
3. **G-3** : un dipole coherent unique laisse (4/5)(mm − ⅓m²) ; seul un ensemble isotrope d'orientations l'annule.
4. **G-4** : non, la dichotomie n'est pas le bon critere. Q_tf = 0 exige B_iB_j − E_iE_j ∝ δ_ij ; un tenseur de rang au plus 2 ne pouvant etre proportionnel a δ_ij sans etre nul, la condition revient a B_iB_j = E_iE_j, soit E = ±B **paralleles**. Un champ de rayonnement (E ⊥ B) ne la satisfait jamais localement. Seules les moyennes d'ensemble (polarisations et orientations isotropes) l'annulent.

## 3. Verdict
**G-V0 qualifie G-V3.**
- G-V0 : la question « dominante magnetique ou E = B » est mal posee pour l'existence du ln Ω. L'objet decisif est Q_tf = partie sans trace de ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺.
- Qualification G-V3 : le passage de Hubble a l'extinction (kD) fixe la trace (⟨F²⟩, loi de puissance en k⋆D) et une partie de Q_tf ; la structure de polarisation fixe le reste. [corrige IR-d''' :] Q_tf ≠ 0 si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf ; nul pour une onde circulaire, helicoidale, un faisceau non polarise ou un ensemble isotrope.

## 4. Confrontation a la prediction
Prediction (NOTE-107 §4) : « G-V0 qualifie G-V3 ; log porte par Q_ij, Poynting sans log ; ln de (2.17) par la partie sans trace ; trace en cos(2kD) se moyennant en loi de puissance pour une emission sous-Hubble ; partie sans trace survivant pour un champ polarise, non nulle pour un dipole, nulle pour un ensemble isotrope non polarise ». **Realisee sauf une clause** [corrige IR-d''' : la clause « nulle seulement pour un ensemble isotrope non polarise » est fausse, NOTE-113]. Precision : la decroissance spectrale est x^{−(n+1)} ou plus rapide selon la parite de n.

## 5. Correction de NOTE-106
NOTE-106 §0, §4 et §5 disent que le ln Ω de (2.17) existe « pour un champ coherent dont ⟨F²⟩ ne s'annule pas a 𝓘⁺ ». C'est **inexact** : ⟨F²⟩ commande la partie isotrope de X^M et T̂, pas le ln de (2.17). Le bon enonce : le ln Ω de (2.17) existe des que **Q_tf ≠ 0** a 𝓘⁺. L'observation de D-b (poids egaux : plus de log apres isotropisation, ±3/2 anisotropes pour une direction fixee) est confirmee et s'explique ainsi.

## 6. Portee sur Q-M3 et CCC + M
- Le ln Ω de (2.17) n'est pas reserve aux champs magnetiques gelés : [corrige IR-d''' :] il est present des que ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf, y compris pour un rayonnement emis sous-Hubble a polarisation lineaire ou pour un dipole ; il n'est pas generique pour tout champ coherent polarise (onde circulaire : absent).
- Il disparait pour un etat statistiquement isotrope et non polarise, ce qui est le cas du vide (coherent avec ISO-V3 de NOTE-96).
- M-V3 reste conditionnel. Conditions mises a jour : champs charges conformes, vide conforme, prescription in-in, **Q_tf ≠ 0 a 𝓘⁺**, u₀ ≪ k, premier ordre en β, fond fixe, partie homogene (C-iso). Rien n'est grave. RG-4 inchangee.

## 7. Limites
- Partie homogene seulement : pour un champ localise, le passage de Q_ij(x) a R local demande le traitement inhomogene (cf. NOTE-92). L'enonce local du §2.4 est [derive], pas calcule.
- Modele de source : extinction franche depuis une configuration magnetostatique ; une source plus generale change les poids, pas la structure (premier terme independant de D).
- Champ longitudinal (charges nettes persistantes) non traite.

## 8. Greffes proposees (non entees)
- **IR-i** : version inhomogene : Q_ij(x) local dans (2.17) pour un dipole (prolonge NOTE-92).
- **IR-j** : audit froid aveugle de NOTE-108 (notamment la loi R_ln = 3βκ/e² Q_tf).
- **IR-d''** : porter les corrections sur NOTE-102, NOTE-104 et NOTE-106 (remplace IR-d').

## 9. Non-surclassement
[conv], non audite. Premier ordre en β, fond fixe, cadre S2 + [21]. Noyau {A4 ; A2★ ; N} inchange.
