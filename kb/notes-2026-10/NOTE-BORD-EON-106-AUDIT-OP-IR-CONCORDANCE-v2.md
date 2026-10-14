---
id: NOTE-BORD-EON-106-AUDIT-OP-IR-CONCORDANCE
numero: 106
serie: I
branche: Q-M3 suite (audit OP-IR)
reservation: 2026-10-10T19:19 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 106)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 d89e75b2dd670f69b0192c080cc1d8594994bd9b921ae320d77b0362c72ce465 (conservee)"
greffe: "IR-d'' entee le 2026-10-11 par NOTE-BORD-EON-109 (corrections de NOTE-104, NOTE-106 audit AU-V2, NOTE-108)"
gel: NOTE-BORD-EON-105-ARMEMENT-AUDIT-OP-IR (sha256 3b4b2fcdfae713e548fce716175cd0401db4ad6ba76e8cb19efb5fd95a11afc8, 2026-10-10T19:20:21Z)
rapport: RAPPORT-OP-IR-AUDIT-AVEUGLE-Da-Db.md
controle_post_audit: "ctrl_etat.py, sha256 780298d6013b1d64d18b451d8c6ca674e4dc2d62a0003c8a17c519f59cc83404, 2026-10-10T19:30:20Z, EXIT 0 (verification independante de la reserve d'etat de D-b)"
depend: [NOTE-BORD-EON-105-ARMEMENT-AUDIT-OP-IR, NOTE-BORD-EON-102-OP-IR-EXECUTION, NOTE-BORD-EON-104-IR-a-LECTURE-REF21]
verdict: "AU-V2"
prediction_realisee: "oui"
rouvre_si:
  - "etat du champ a 𝓘⁺ autre qu'une configuration a dominante magnetique (⟨F²⟩ → 0)"
  - "champs charges non conformes (contre-exemple de type Prokopec-Törnkvist-Woodard)"
  - "action plate en regime de champ quasi constant"
---

# NOTE-106 : audit froid aveugle conjoint de NOTE-102 et NOTE-104. Verdict **AU-V2** (v2 : voir greffe)

> **Greffe IR-d'' (v2, 2026-10-11).** Correction entee, issue de NOTE-108 (IR-g, ir_g.py) :
> 1. **Critere du ln de (2.17)** (§0, §4, §5) : la v1 disait « present si ⟨F²⟩ ne s'annule pas a 𝓘⁺ ». C'est **inexact**. ⟨F²⟩ (trace de Q) commande la partie isotrope de X^M et la trace anomale T̂, que la fermeture C-iso absorbe sans log. Le ln de (2.17) vaut exactement (3βκ/e²) × **partie sans trace** de Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺.
> 2. **Lecture du §2** : la « partie anisotrope liee a la direction de k » est precisement ce qui nourrit le ln de (2.17). Elle disparait pour un ensemble isotrope non polarise, mais survit pour tout champ coherent polarise (dipole : (4/5)(mm − ⅓m²)), meme a poids E et B egaux.
> 3. **Conditions de M-V3** (§5) : « champ coherent a ⟨F²⟩ ≠ 0 » devient « **Q_tf ≠ 0 a 𝓘⁺** ».
> 4. **Greffes** (§6) : IR-g est instruite (NOTE-108) ; IR-d' est remplacee par IR-d'' (la presente).

## 0. Resume
Les deux auditeurs concordent sur tout le calcul (C1 a C4) et D-b confirme la lecture de [21] (L1 a L5), avec des nuances. Les conclusions D1 a D3 tiennent sous hypotheses nommees. D-b apporte une correction de fond a D4, que j'ai verifiee independamment : **le ln a du secteur Maxwell isotrope est proportionnel a ⟨F²⟩ = 2(⟨B²⟩ − ⟨E²⟩) a 𝓘⁺** [precise IR-d'' : le ln de (2.17), lui, est porte par la partie sans trace de ⟨B_iB_j − E_iE_j⟩, greffe point 1]. Il est present pour un champ coherent a dominante magnetique (le cas de NOTE-98), absent dans son secteur isotrope pour une configuration a poids E et B egaux (rayonnement, Bunch-Davies hors horizon). Prediction du gel (AU-V2 avec reserves sur D1 et D2, precision sur D3) **realisee**.

## 1. Concordance

| Resultat | D-a | D-b | Etat |
|---|---|---|---|
| C1 mode | identique (u₁ magnetique sans log, electrique 2c s ln s) | OK (Green) ; b1 arbitraire | **concordant** |
| C2 ⟨X^M⟩, rapports −2 / +2 | identique | OK ; rapport exact a l'ordre dominant seulement | **concordant** |
| C3 R (2.17), coincidence avec l'uniforme | coincidence exacte a s⁰, y compris −⅔β ; ecart a s² | reproduit a l'identique | **concordant** |
| C4 plat 0, Hodge 0, Bochner −4 | identique, Weitzenböck p(n−p)H² | OK, controle par etoile de Hodge | **concordant** |
| C5 residu statique, (3.16) | (non pose) | calcul exact, **portee surinterpretee**, sortie tautologique | **corrige** |
| L1-L5 lecture de [21] | (non lu, cecite) | exacts ; L3 limite a l'ordre R³ et attribue | **confirme, nuance** |
| D1 echelle H | Q7 : non, l'action plate ne voit ni a ni H | valide sous hypotheses ; reformuler | **concordant, precise** |
| D2 residu O(β²) | O(β²) ; electrique β² ln² s | valide au premier ordre fixe | **concordant** |
| D3 u₀ ≪ k | idem ; c ≪ k² electrique ; ∇² spatial | valide | **concordant, precise** |
| D4 verdict | coincidence avec l'uniforme formelle (hors validite) | **dependance a l'etat** | **corrige** |

## 2. Controle independant de la reserve d'etat [calcule]
Mode mixte u = u₀cos(ks) + (c/k)sin(ks) + β U₁, U₁ par fonction de Green (ctrl_etat.py) :
- coefficient de β ln s dans ⟨X^M⟩_ss et ⟨X^M⟩_xx, rapporte a s² : −(k²u₀² − c²)/(2e²) ;
- dans ⟨X^M⟩_yy et ⟨X^M⟩_zz : ∓(k²u₀² + c²)/(2e²) (partie anisotrope, propre a la direction de k) ;
- ⟨F²⟩_η a l'ordre 0, s → 0 : k²u₀² − c².

Pour c = ku₀ (poids egaux) le log s'annule dans la partie isotrope et dans la trace anomale. Il ne reste qu'une partie anisotrope liee a la direction de k, qui disparait apres moyenne sur les directions. La reserve de D-b est **confirmee**.

## 3. Corrections a porter
1. **NOTE-102 C5 / D1-D3 du script** : la sortie « residu = 0 a k₀ = 0 » est tautologique (log 1) ; « R = 12 » et la ligne D3 sont codees en dur, non calculees. A etiqueter. Troncature mixte s² ln s en section C : cosmetique.
2. **NOTE-104 D1** : remplacer « aucune echelle en H » par « **aucun terme en H² dans l'operateur effectif** ». H n'entre qu'additivement (ln H, absorbable dans λ) et par k s dans l'etat. Hypotheses : metrique exactement Weyl-plate ; champs charges conformement couples ; vide conforme ; prescription causale in-in ; action plate dans son domaine. La forme BV n'est pas invocable en de Sitter (R² ≪ ∇²R viole) ; L3 ne vaut qu'a l'ordre R³.
3. **NOTE-104 D4 et NOTE-102 IR-1** : « le ln a persiste » devient « **le ln a du secteur isotrope est proportionnel a ⟨F²⟩ a 𝓘⁺** : present pour une configuration coherente a dominante magnetique, absent pour des poids E et B egaux ». L'etat du champ devient une hypothese explicite du verdict.
4. **Robustesse** : seuls les coefficients de ln s sont robustes (ils ne viennent que de I_B, exact). Les constantes (−⅔β, termes en λ) dependent de la fermeture C-iso et du tenseur hors orbite de Weyl, inaccessible (S2 note 4).
5. **Non-uniformite** : tout est a premier ordre fixe et cesse d'etre fiable pour β|ln s| ~ 1, sauf la branche magnetique ou le log est exact dans l'action simplifiee.
6. **Domaine** : la coincidence avec le champ uniforme (C3) est exacte algebriquement mais formelle physiquement, le cas k = 0 etant hors du domaine de l'action plate.

## 4. Verdict
**AU-V2** : concordance sur C2, C3 et L1-L3 ; D1 a D3 valides sous hypotheses nommees ; corrections ci-dessus, dont une de fond sur D4 (dependance a l'etat). NOTE-102 (IR-V1) et NOTE-104 (OP-V1 qualifie OP-V3) sont **maintenues avec cette lecture** : dans le cadre de S2 et de [21], pour des champs charges conformes dans le vide conforme, le ln Ω de (2.17) existe pour un champ coherent dont ⟨F²⟩ ne s'annule pas a 𝓘⁺ [corrige IR-d'' : dont la partie sans trace de Q ne s'annule pas], et son echelle infrarouge ne peut pas etre deplacee vers H par l'action plate.

## 5. Portee sur Q-M3 et CCC + M
OP-IR est **tranche dans le cadre S2 + [21]**, sous les hypotheses du §3. Le candidat M-V3 de NOTE-98 reste conditionnel ; sa liste de conditions s'ecrit desormais : champs charges conformes, vide conforme, prescription in-in, champ coherent a ⟨F²⟩ ≠ 0 [corrige IR-d'' : Q_tf ≠ 0] a 𝓘⁺ dans le domaine de l'action plate (u₀ ≪ k), premier ordre en β (ou branche magnetique exacte), fond fixe. Rien n'est grave. RG-4 inchangee.

## 6. Greffes proposees (non entees)
- **IR-d'** : porter sur NOTE-102 et NOTE-104 les corrections du §3 (remplace IR-d).
- **IR-e** : action plate en regime de champ quasi constant (seule voie pour k → 0).
- **IR-g** : etat physique du champ a 𝓘⁺ : un champ coherent issu d'une source causale reste-t-il a dominante magnetique (⟨F²⟩ ≠ 0), ou tend-il vers E = B ? C'est desormais la question qui decide de l'existence du ln Ω.
- **IR-h** : verifier la piste Prokopec-Törnkvist-Woodard (citee de memoire par D-b, non lue) pour delimiter l'hypothese « champs charges conformes ».

## 7. Non-surclassement
[conv], audite a froid (AU-V2), non scelle comme resultat. Aucune incompatibilite gravee. Noyau {A4 ; A2★ ; N} inchange.
