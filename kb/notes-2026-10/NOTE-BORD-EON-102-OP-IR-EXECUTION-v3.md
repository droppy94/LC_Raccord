---
id: NOTE-BORD-EON-102-OP-IR-EXECUTION
numero: 102
serie: I
branche: Q-M3 suite (OP-IR)
reservation: 2026-10-10T16:05 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 102)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
version: 3
remplace: "v1, sha256 ea774ca54e2e5c032bb97cc931a8bb8265f75b743d1ac0d1ddd1d2caa75dda3c (conservee)"
greffe: "IR-d''' entee le 2026-10-11 par NOTE-BORD-EON-114 (audit NOTE-113) ; v2 sha256 4bc0b72978987e468847c12a03bcc061c7d3614491982579cc2db49f08c2fae3 conservee ; anterieurement IR-d'' entee le 2026-10-11 par NOTE-BORD-EON-109 (corrections de NOTE-104, NOTE-106 audit AU-V2, NOTE-108)"
gel: NOTE-BORD-EON-101-ARMEMENT-OP-IR (sha256 e4c36854d2d29bb49837ff9baa18684356b02c52bce47481856c9f7f06c578b5, 2026-10-10T16:06:37Z)
depend: [NOTE-BORD-EON-101-ARMEMENT-OP-IR, NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
sources: ["arXiv:1808.08237v2 (S2), eq. (2.12), (3.9)-(3.16), lues en NOTE-96"]
instruments:
  - "op_ir.py v1, sha256 824357b3afacb0f41a755e7ab1692d0fe778e04c21ff58e36d1d1eef2ad70448, 2026-10-10T16:07:59Z : ECHEC (IndexError, partie A), conserve (R-55), sortie op_ir_v1_sortie.txt"
  - "op_ir_v2.py, sha256 77620a4161cedaab8a0e3172d4f5eee5ab5bb98df8ac421f2c81ab3c34396fb5, 2026-10-10T16:09:53Z : EXIT 0, sortie op_ir_v2_sortie.txt"
  - "op_ir_v2_ctrl.py, sha256 1b24fd9de15a29467a14acc1155bedf66ff48f3732918cb1d334dd1e485c4fbe, 2026-10-10T16:11:26Z : EXIT 0, sortie op_ir_v2_ctrl_sortie.txt"
verdict: "IR-V1 qualifie IR-V3 (v1) ; v2 : IR-V1, qualification reduite au domaine de validite de l'action plate, critere d'etat Q_tf ≠ 0"
prediction_realisee: "oui, avec deux precisions (§5)"
rouvre_si:
  - "lecture de la reference [21] de S2 (derivation de l'action exacte Weyl-plate)"
  - "regularisation explicite du log plat sur couche de masse (terme residuel de S2 hors approximation 3.10)"
  - "ordres superieurs en beta-tilde ou retroaction ; fermions massifs ; etat non conforme"
---

# NOTE-102 : OP-IR par un mode a k fini hors horizon. Verdict **IR-V1 qualifie IR-V3** (v2 : voir greffe)

> **Greffe IR-d'' (v2, 2026-10-11).** Corrections entees, issues de NOTE-104 (lecture de [21]), NOTE-106 (audit AU-V2) et NOTE-108 (IR-g) :
> 1. **Residu de S2** (§3.2) : il agit sur {u'' + k²u}, d'ordre β ; il n'entre qu'a l'ordre β² (β² ln² s au plus pour la branche electrique). Les resultats au premier ordre n'en dependent pas.
> 2. **Choix de l'operateur** (§3.3) : [21] fixe l'operateur plat du repere conforme ; aucun terme en H² dans l'operateur effectif (sous hypotheses : Weyl-plat exact, champs charges conformes, vide conforme, in-in). La qualification IR-V3 se reduit au domaine de validite de l'action plate (u₀ ≪ k, c ≪ k²).
> 3. **Dependance a l'etat** (IR-1, §4) : le ln de (2.17) vaut (3βκ/e²) × partie sans trace de Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺ (NOTE-108). [corrige IR-d''' : la v2 disait « present pour tout champ coherent polarise, nul pour un ensemble isotrope non polarise », faux, NOTE-113.] Il est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺ (NOTE-113) ; il s'annule pour une onde progressive circulaire, une onde stationnaire helicoidale a Q = 0, un faisceau non polarise, un ensemble isotrope ; il est present pour un reliquat magnetostatique, un dipole rayonne, une onde lineaire ou elliptique.
> 4. **Sorties du script** (D1, D3) : « residu = 0 a k⁰ = 0 » est log 1, tautologique ; « R = 12 » et la ligne D3 sont codes en dur ; le controle (i) de op_ir_v2_ctrl.py (mode libre sur couche) est tautologique. Ce sont des rappels, pas des calculs.
> 5. **Terme β s² ln s de R_ysy** : reel (confirme par D-a : (5/2)βκk⁴u₀²/e² s² ln s), mais la ligne est incomplete, les termes s² sans log ayant ete tronques (troncature mixte, section C du script).
> 6. **Robustesse** : seuls les coefficients de ln s sont robustes (ils ne viennent que de I_B, exact). Les constantes (−β/6, termes en λ, b₁ = 142/105 de la branche electrique) dependent de choix (fermeture C-iso, solution homogene) et du tenseur hors orbite de Weyl, inaccessible.
> 7. **Branche electrique** : X^M ∝ 1/I² exactement ; le rapport +2 n'en est que le premier ordre, et seulement a l'ordre dominant en s.
> 8. **Coincidence avec le champ uniforme** : exacte algebriquement a l'ordre s⁰, formelle physiquement (k = 0 hors du domaine de l'action plate).

## 0. Resume
Avec la prescription de S2 (a⋆ = k/M), un mode a k fini hors horizon porte dans son secteur Maxwell le meme ln a que le champ uniforme de NOTE-98, au coefficient 2β̃. Sa partie homogene reproduit NOTE-98 terme a terme dans (2.17) avec B₀² → ⟨B²⟩ = k²u₀²/2. Le ln a est la course du couplage avec l'impulsion **physique** k/a : il n'y a pas de coupure en H dans le cadre de S2. OP-IR est donc tranche **dans le cadre de S2**. Reste une reserve : sur le mode libre, l'operateur plat de S2 est nul (log 0), et c'est la prescription a⋆ = k/M avec l'approximation (3.10), non une derivation, qui fixe l'echelle infrarouge. La forme covariante de Bochner donnerait a la place une echelle en H, celle de Hodge redonne 0 comme S2.

## 1. Incident d'instrument (R-55)
op_ir.py v1 imposait l'equation de mode jusqu'aux ordres ou la source etait tronquee : systeme incompatible, `IndexError` en partie A. La v2 resout par recurrence (branche magnetique) et n'impose l'equation qu'aux ordres controles s^p, p ≤ N−1 (branche electrique). Les parties B a D sont identiques a la v1.

## 2. Resultats [calcule] (op_ir_v2_sortie.txt)

### A. Le mode (premier ordre en β̃, s = Ω → 0)
| Branche | u(s) | Remarque |
|---|---|---|
| magnetique gelee | u₀cos(ks) + β̃(−u₀k²s² + u₀k⁴s⁴/9 + …) | aucun log dans u : le mode reste analytique |
| electrique | (c/k)sin(ks) + β̃(2c s ln s + … ) | I²u_s → c(1+2β̃λ) constant, comme attendu |
Residu de (3.14) a l'ordre β̃ : nul jusqu'a l'ordre tronque, dans les deux branches.

### B. Secteur Maxwell moyenne ⟨X^M⟩ (diagonale s, x, y, z)
| Branche | Ordre 0 | Coefficient de β̃ ln s | Rapport |
|---|---|---|---|
| magnetique | (k²u₀²s²/4e²) diag(1,1,1,−1) | −2 × ordre 0 | **−2** sur les 4 composantes |
| electrique | (c²s²/4e²) diag(1,1,−1,1) | +2 × ordre 0 | **+2** sur les 4 composantes |

Branche magnetique : X^M ∝ I² ⟨B²⟩ avec I² = e⁻²[1 + 2β̃ ln(aM/k)], ln a de coefficient **2β̃** (IR-1 : oui). Branche electrique : X^M ∝ (I²u_s)²/I² ∝ 1/I², meme log de signe oppose. Dans les deux cas l'argument du log est **aM/k = M/k_phys**.

### C. (2.17), partie homogene, fermeture C-iso, branche magnetique
Conservation totale verifiee (ordre tronque). Composantes non nulles de R, premier ordre en β̃, s → 0 (κ, e, u₀, k explicites) :

| Composante | Constante | Terme en ln s |
|---|---|---|
| R_xsx | κk²u₀²/(4e²) − β̃κk²u₀²/(6e²) + β̃κk²u₀²λ/(2e²) | −β̃κk²u₀²/(2e²) |
| R_ysy | idem (plus β̃ s² ln s, sous-dominant) | −β̃κk²u₀²/(2e²) |
| R_zsz | −2 × la ligne x | **+β̃κk²u₀²/e²** |

Avec B₀² → k²u₀²/2, c'est exactement NOTE-98 : R_xsx = κB₀²/e² (½ − β̃/3 − β̃ ln s), motif (1,1,−2). Le seul ajout est la constante β̃λ, qui vient de a⋆ = k/M et ne cree aucun terme non lisse (IR-4 : oui). Le terme β̃ s² ln s de R_ysy reflete l'anisotropie x/y propre au mode ; il est sous-dominant.

### D. Facteurs de forme sur le mode
| Operateur, sur le mode libre (β̃ = 0) | Valeur propre | Echelle infrarouge implicite |
|---|---|---|
| S2 exact, −∂²_η e^{−2Ω} (ctrl i) | **0** (couche de masse) | aucune : log 0, regule par a⋆ = k/M |
| S2, partie statique k⁰ = 0 | k² s² = k_phys² | impulsion physique, pas de H |
| Hodge Δ = dδ + δd (ctrl ii) | **0** (δF = 0, dF = 0) | aucune, comme S2 |
| Bochner −□ (champ uniforme et mode) | **−4** (H = 1) | **H²**, independant de a |

Residu de S2 sur la partie statique : −β̃ log((k²−k⁰²)/k²) = 0 a k⁰ = 0. Condition (3.16) : β̃/(1 + 2β̃ ln(aM/k)) → 0 vers 𝓘⁺ (IR-2 : oui sur la partie statique).

## 3. Lecture [derive]
1. **Ce que le mode a k fini apporte.** La singularite k = 0 disparait : l'echelle a⋆ = k/M est finie, le log s'ecrit ln(M/k_phys) et croit comme ln a. C'est la reponse de S2 a OP-IR : pour des fermions sans masse conformement couples, le couplage court avec l'impulsion physique du mode, sans plancher en H. L'argument de NOTE-100 §3 se trouve confirme par un calcul.
2. **Ce qu'il n'apporte pas.** [corrige IR-d'' : point surestime, le residu est d'ordre β², greffe point 1] Sur le mode libre, le d'Alembertien plat est nul : l'argument du log exact de S2 est sur couche de masse, la ou le log d'une boucle sans masse est singulier. S2 separe ce log en ln(a/a⋆) plus un residu, puis neglige le residu par (3.10). Ce residu n'est nul que sur la composante statique. Le calcul ne fixe donc pas l'echelle, il applique celle de S2.
3. **Les deux formes covariantes ne disent pas la meme chose.** Bochner donne −4H², donc log(H²/M²) constant : plus de course en ln a, c'est le scenario d'annulation releve par C-b (IR-V2). Hodge donne 0, comme S2, et c'est l'operateur naturel pour une 2-forme de Maxwell en dimension 4 (il ne voit pas la courbure sur couche de masse). Les deux different par le terme de Weitzenböck. Le choix « −□ » du gel etait ambigu, et l'ambiguite est exactement la question OP-IR. [Tranche par [21], greffe point 2 : −4H² est le terme de Weitzenböck d'une covariantisation tronquee.]
4. **Hors premier ordre.** 2β̃(λ − ln s) → ∞ vers 𝓘⁺ (ctrl iii) : le premier ordre en β̃ n'est pas uniforme. Dans l'action simplifiee de S2, I² est cependant exactement lineaire en ln s et la branche magnetique reste gelee, de sorte que X^M ∝ I²⟨B²⟩ garde son ln a sans troncature. Ce point est [derive], il n'est pas calcule au-dela du premier ordre ici.

## 4. Verdict
**IR-V1 qualifie IR-V3.**
- IR-V1 : avec la prescription de S2 a k fini, le ln a persiste (coefficient 2β̃) [pour la branche magnetique pure ; en general (3βκ/e²) Q_tf dans (2.17), greffe point 3], le residu statique est nul, la partie homogene reproduit NOTE-98. Dans le cadre de S2, l'echelle infrarouge est l'impulsion physique du mode (a⋆ comobile) : la lecture de NOTE-98 tient.
- Qualification IR-V3 : cette conclusion repose sur la revendication d'exactitude Weyl-plate de S2 (2.12) (reference [21] non lue, EX-8) et sur l'approximation (3.10), car l'operateur est nul sur couche de masse. Une forme covariante de type Bochner donnerait une echelle H et lèverait l'obstruction. Hodge s'accorde avec S2.

## 5. Confrontation a la prediction
Prediction (NOTE-101 §5) : « IR-V1 qualifie IR-V3 ; ln a persistant avec coefficient 2β̃, residu nul sur la partie statique ; la forme covariante −□ donnera une echelle en H ». **Realisee**, avec deux precisions :
- (a) le residu n'est nul que sur la partie statique ; sur le mode complet, l'operateur est nul et le log singulier ;
- (b) seule la forme de Bochner donne H ; celle de Hodge s'accorde avec S2. Cela affaiblit la qualification IR-V3 sans la lever.

## 6. Portee
- NOTE-100 / CB-a : la lecture « ln Ω dans (2.17) avec echelle infrarouge comobile » est maintenant soutenue par un calcul a k fini dans le cadre de S2. OP-IR passe de **ouvert** a **tranche dans S2, conditionnel hors S2** (reference [21], residu sur couche de masse).
- M-V3 (NOTE-98) reste un candidat conditionnel. Ses conditions se resserrent : la condition « echelle comobile » est remplacee par « exactitude Weyl-plate de S2 avec (3.10) ». Rien n'est grave. RG-4 inchangee.

## 7. Greffes proposees (non entees)
- **IR-a** : lire la reference [21] de S2 (derivation de la forme exacte Weyl-plate) pour savoir si l'operateur est Hodge ou autre, ce qui leverait la qualification IR-V3.
- **IR-b** : regulariser le log sur couche de masse par la petite deviation β̃ du mode (le mode corrige n'est plus exactement sur couche) et voir si l'echelle qui sort est k_phys ou H.
- **IR-c** : audit froid aveugle de NOTE-102 (non engage par le gel).

## 8. Non-surclassement
[conv], premier ordre en β̃, fond de Sitter fixe, un mode, cadre S2. Non audite. Noyau {A4 ; A2★ ; N} inchange.
