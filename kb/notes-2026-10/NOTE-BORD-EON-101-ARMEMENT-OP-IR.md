---
id: NOTE-BORD-EON-101-ARMEMENT-OP-IR
numero: 101
serie: I
branche: Q-M3 suite (OP-IR)
reservation: 2026-10-10T16:05 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 101)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION, NOTE-BORD-EON-96-ISOTROPIE-ETAT-ANOMAL-EXECUTION]
sources: ["arXiv:1808.08237v2 (S2, appui R-41 etabli en NOTE-96)"]
issue_attendue: "delimitation"
rouvre_si:
  - "lecture de la reference [21] de S2 (derivation de l'action exacte Weyl-plate), non lue"
  - "calcul de l'action effective a une boucle hors approximation (3.10) de S2 (terme residuel sur couche de masse)"
  - "fermions massifs ou etat non conforme"
---

# NOTE-101 : armement. Trancher OP-IR par un mode a k fini hors horizon

## 0. Origine
NOTE-100 (audit AU-V2) laisse un point ouvert, **OP-IR** : pour un champ strictement uniforme (k = 0), le terme non local −β̃ F log(−∂²/M²) F de S_flat est mal defini. Selon que son echelle infrarouge est comobile (le couplage court avec l'impulsion physique k/a) ou physique (par exemple H), le ln a du secteur Maxwell persiste ou s'annule exactement. Un mode a k fini evite la singularite k = 0 et permet d'appliquer la prescription de S2 (a⋆ = k/M, eq. 3.15).

## 1. Ce que dit deja la source (rappel, [extrait], NOTE-96 §2)
- S2 (2.12) : pour une metrique Weyl-plate, `S = −1/(4e²) ∫∫ F(x) ⟨x| 1 − β̃ log(−∂²_η /(M² e^{2Ω_S(x)})) |y⟩ F(y)` ; S2 §2 la presente comme exacte a une boucle sur les metriques Weyl-plates, resommant le developpement de Barvinsky-Vilkovisky (derivation dans leur reference [21], **non lue**, EX-8).
- S2 (3.9)-(3.16) : separation `I² = e⁻²[1 + 2β̃ ln(a/a⋆)]` plus un terme residuel `−β̃ log(k_νk^ν/(M²a⋆²))` ; approximation (3.10) du residu ; choix a⋆ = k/M ; condition de validite (3.16) `1 + 2β̃ ln(aM/k) ≫ β̃`.

## 2. Cadre du calcul (fige)
- Fond de Sitter fixe, coordonnee s = −τ = Ω > 0, `ĝ = Ω⁻² η`. H = 1.
- Mode reel : `A_y = u(s) cos(kx)`, k > 0 fini, jauge de Coulomb, autres composantes nulles. Champs : `F_xy = −k u sin(kx)` (magnetique selon z), `F_sy = u_s cos(kx)` (electrique).
- Equation de mode de S2 (3.14), en s : `(I² u_s)_s + k² I² u = 0`, `I² = e⁻²[1 + 2β̃(λ − ln s)]`, `λ = ln(M/k)` (a⋆ = k/M).
- Regime : hors horizon, k s → 0. Developpement polyhomogene en s, **au premier ordre en β̃** (ordre de toute l'analyse anomale).
- Branche consideree : branche « magnetique gelee » (u → u₀ ≠ 0) ; la branche electrique (I² u_s → C) est traitee separement.
- Secteur Maxwell : `X^M = I² (F F ĝ⁻¹ − ¼ ĝ F·F)`, moyenne spatiale (partie homogene) et partie en e^{2ikx}.
- Second membre de (2.17) pour la **partie homogene** avec la fermeture C-iso (comme NOTE-98) : comparaison terme a terme avec NOTE-98 (B₀² → ⟨B²⟩).
- Confrontation des facteurs de forme sur ce mode : (i) forme exacte de S2, operateur `−∂²_η e^{−2Ω}` ; (ii) forme covariante `−□` (laplacien covariant de de Sitter agissant sur la 2-forme F) ; extraction de « l'echelle infrarouge effective » de chacune pour la partie statique du champ.

## 3. Sous-questions
- **IR-1** : au premier ordre en β̃, le secteur Maxwell du mode a k fini porte-t-il, pres de 𝓘⁺, un terme Ω² ln Ω anisotrope ? Avec quel coefficient (comparer a 2β̃) ?
- **IR-2** : le terme residuel de S2, evalue sur la partie statique (k⁰ = 0) du mode, s'annule-t-il ? Sa taille relative tend-elle vers 0 vers 𝓘⁺ (condition 3.16) ?
- **IR-3** : la forme covariante −□ donne-t-elle, sur ce mode hors horizon, une echelle effective k_phys² + c H² (donc « physique ») ? Les deux formes different-elles, et laquelle S2 retient-il comme exacte ?
- **IR-4** : la partie homogene reproduit-elle le ln Ω de NOTE-98 dans (2.17) ?

## 4. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **IR-V1** | Avec la prescription de S2 a k fini, le ln a persiste dans le secteur Maxwell (coefficient 2β̃ au premier ordre), le residu ne le compense pas, et la partie homogene reproduit NOTE-98 : OP-IR tranche en faveur de l'echelle comobile **dans le cadre de S2**. |
| **IR-V2** | Le residu ou la dynamique du mode compense le ln a (echelle effective physique) : OP-IR tranche en faveur de l'echelle physique ; l'obstruction de NOTE-98 est levee. |
| **IR-V3** | Non tranchable dans le cadre lu : les deux formes du facteur de forme different sur ce mode et S2 ne fournit pas de quoi les departager au-dela de sa revendication d'exactitude (reference [21] non lue) ou de l'approximation (3.10). Delimitation. |
| **IR-V0** | Question mal posee (a nommer). |

Composites permis (un verdict principal, une qualification).

## 5. Prediction declaree (anti-fit)
**IR-V1 qualifie IR-V3** : ln a persistant avec coefficient 2β̃ et residu nul sur la partie statique ; mais la forme covariante −□ donnera une echelle en H differente de la forme exacte de S2, de sorte que la conclusion repose sur la revendication d'exactitude Weyl-plate de S2 (reference [21] non lue).

## 6. Instruments prevus
Script `op_ir.py` (sympy), empreinte prise avant execution. Audit froid propose ensuite (non engage par ce gel).

## 7. Non-surclassement
Premier ordre en β̃, fond fixe, un mode, cadre S2. RG-4 non concernee. Noyau {A4 ; A2★ ; N} inchange.
