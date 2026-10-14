---
id: NOTE-BORD-EON-104-IR-a-LECTURE-REF21
numero: 104
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-a)
reservation: 2026-10-10T18:56 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 104)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 95df64c4be1837b024d277e0801bec8ba93d64b65b9ccd4593260d8335eb1ec4 (conservee)"
greffe: "IR-d'' entee le 2026-10-11 par NOTE-BORD-EON-109 (corrections de NOTE-104, NOTE-106 audit AU-V2, NOTE-108)"
gel: NOTE-BORD-EON-103-ARMEMENT-IR-a (sha256 7b8e9ac5ea638fcca2ccb927feafd4d2d2f2e23f3e57adf122427d714ee77fdd, 2026-10-10T18:57:17Z)
depend: [NOTE-BORD-EON-103-ARMEMENT-IR-a, NOTE-BORD-EON-102-OP-IR-EXECUTION]
sources:
  - "S2 = arXiv:1808.08237v2 (Benevides, Dabholkar, Kobayashi), JHEP 11 (2018) 039 : bibliographie, §1, §2 (2.4)-(2.17), §3 (3.1)-(3.17), lus integralement sur ces plages"
  - "[21] de S2 = Bautista, Benevides, Dabholkar, Nonlocal Quantum Effective Actions in Weyl-Flat Spacetimes, arXiv:1711.00135v1 (seule version), DOI 10.1007/JHEP06(2018)055 : LU EN ENTIER (§1 a §3.5 et bibliographie)"
miroirs_R41:
  - "alphaXiv, texte integral v1 (copie locale bbd_1711.00135.txt, sha256 b89ca1f03e41e1d98751fed811e0c19524af825c906172837fcd62f5d9ad71c4)"
  - "arXiv PDF v1 (controle cible de six passages, concordant)"
  - "page arXiv abs (versions, DOI) ; S2 §2, qui resume [21] de facon concordante"
imports_non_lus_EX8: "Donoghue et El-Menoufi arXiv:1507.06321 (forme BV (3.25) de [21]) : non lu, pris tel que [21] le reproduit ; Barvinsky et al. gr-qc/9510037 (decomposition conforme) : non lu"
verdict: "OP-V1 qualifie OP-V3"
prediction_realisee: "oui ; identite de [21] confirmee (hypothese a 0,6 du gel)"
rouvre_si:
  - "calcul de l'action plate S_flat hors du regime de champ rapidement variable (champ quasi constant, type Euler-Heisenberg)"
  - "etat non conforme, fermions massifs, variation metrique hors orbite de Weyl"
---

# NOTE-104 : lecture de la reference [21] de S2. Verdict **OP-V1 qualifie OP-V3** (v2 : voir greffe)

> **Greffe IR-d'' (v2, 2026-10-11).** Corrections entees, issues de NOTE-106 (audit AU-V2) et NOTE-108 :
> 1. **D1 reformule** (§4.1) : « aucune echelle en H » devient « **aucun terme en H² dans l'operateur effectif** ». H n'entre qu'additivement (ln H, absorbable dans λ) et par ks dans l'etat. Hypotheses : metrique exactement Weyl-plate ; champs charges conformement couples ; vide conforme ; prescription causale in-in (le repere conforme ne couvre que η < 0) ; action plate dans son domaine. Contre-exemple hors hypotheses signale par D-b, non lu : QED scalaire minimalement couplee en de Sitter (Prokopec, Törnkvist, Woodard 2002).
> 2. **L3 limite** (§2) : la decomposition conforme n'est etablie qu'a l'ordre R³ et attribuee a [8, 33] ; la forme BV n'est pas invocable en de Sitter (R² ≪ ∇²R viole). L'exactitude de la conclusion repose sur le lemme d'integration (2.44), pas sur (3.25).
> 3. **L1 nuances** : une boucle ; regime R ≪ M₀² (validite de Schwinger-DeWitt) ; anomalie C ignoree ; pas de modes nuls (note 5).
> 4. **L4** : de Sitter est **mentionne** dans [21] comme application possible, sans traitement.
> 5. **L5** : passage ecrit pour le scalaire (§3.3), transpose au cas de jauge ; dans le regime hors horizon (ks ≪ 1) la lecture en impulsion physique ne s'applique pas, seule l'action reste valide.
> 6. **D3 precise** (§4.3a) : ∇² s'entend comme gradient spatial (le d'Alembertien plat est nul sur couche) ; branche electrique : c ≪ k².
> 7. **D4 et §7** : le ln de (2.17) n'est pas fixe par « champ uniforme ou mode » mais par l'etat : (3βκ/e²) × partie sans trace de ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺ (NOTE-108).

## 0. Resume
La reference [21] de S2 est bien Bautista, Benevides, Dabholkar (arXiv:1711.00135). La lecture complete etablit trois points :
- la partie anomale de l'action est **exacte** sur toute metrique Weyl-plate, quelle que soit l'amplitude des courbures ;
- la partie non locale restante est **l'action plate du repere conforme**, sans aucune dependance en Ω ;
- une covariantisation de type « log du d'Alembertien covariant » seul est explicitement ecartee : les termes de courbure se combinent en un morceau invariant de Weyl, qui se reduit a l'action plate.

Une echelle en H de type Bochner est donc exclue dans ce cadre. Le ln a de NOTE-98 et NOTE-102 ne peut pas etre compense par l'action plate. La qualification restante (OP-V3) porte sur le **domaine de validite de l'action plate**, que [21] restreint aux champs rapidement variables, et sur le silence de [21] concernant de Sitter et l'infrarouge.

## 1. Identification de [21] [extrait]
Bibliographie de S2, entree [21] : « T. Bautista, A. Benevides, and A. Dabholkar, Nonlocal Quantum Effective Actions in Weyl-Flat Spacetimes, arXiv:1711.00135 ». Une seule version (v1, 31 octobre 2017), publiee sous le DOI 10.1007/JHEP06(2018)055. L'hypothese du gel est confirmee.

## 2. Ce que dit [21] [extrait, avec equations de [21]]

| Point | Contenu | Lieu |
|---|---|---|
| Methode | identite de groupe (lemme d'integration) : S[g] = S[ḡ] + S_A[ḡ, Ω], valable « a tout ordre si l'anomalie est connue a cet ordre » | (2.39)-(2.46) |
| Exactitude de la partie anomale | I_B = −(b/4)∫ η η F Ω F ; « ne requiert aucune approximation de champ faible » ; elle decoule du developpement local de Schwinger-DeWitt | (3.8), §3.2 |
| Action plate | « −∂² est le d'Alembertien de l'espace plat » ; log defini par representation spectrale ou par Fourier, log(p²/M²) | (3.9)-(3.11) |
| Limite de validite | « In (3.9) we have used the weak gauge field approximation F⁴ ≪ ∇⁴F² » ; « we still need to assume F² ≪ ∇²F » ; le regime de champ constant est cite comme extension possible, **non faite** | §1, §3.2 |
| Lecture en impulsion physique | si le facteur d'echelle varie lentement devant le champ : k²/M²(x) = p²(x)/M², p² = e^{−2Ω}k² ; couplage courant avec l'impulsion physique | §3.3, (3.21) |
| Facteur d'echelle rapide | « one cannot use the momentum basis as above but equation (3.20) is still valid » | §3.3 |
| Covariantisation | « One might be tempted to interpret the full answer in terms of log(−∇²/M²) » ; elle exige de nombreux termes non locaux supplementaires qui se combinent en un morceau invariant de Weyl | §3.3, §3.5 |
| Decomposition conforme | dans la forme BV (3.25), tous les termes sauf F(−⅙ ∇⁻²R)F sont invariants de Weyl ; sur une metrique Weyl-plate ils se reduisent a l'action plate (3.28) | (3.25)-(3.30) |
| Riegert | Ω[g] = ¼∫G₄F₄ ; son developpement redonne le terme BV, a O(R⁴) pres | (3.31)-(3.38) |
| de Sitter, H, infrarouge, couche de masse | **absents** : de Sitter cite comme application possible, H seulement dans l'introduction, aucun traitement infrarouge, rien sur log(p²) a p² = 0 | (controle PDF) |

## 3. Reponses aux sous-questions

| Question | Reponse | Etiquette |
|---|---|---|
| **A-1** exactitude | Oui pour la partie anomale, a une boucle, sur toute metrique Weyl-plate, sans approximation de courbure. Hypotheses : champs sans masse conformement couples, regulateur de temps propre covariant, operateurs sans modes nuls (note 5), anomalie C gravitationnelle ignoree. L'action plate, elle, n'est connue que dans le regime F² ≪ ∇²F. | [extrait] |
| **A-2** operateur | **D'Alembertien plat du repere conforme**, toute la dependance en Ω etant portee par S_B. Pas de log du d'Alembertien covariant seul : sa covariantisation passe par des termes de courbure qui, combines, forment un morceau invariant de Weyl reduit a l'action plate. | [extrait] |
| **A-3** infrarouge et couche de masse | Rien dans [21]. | [extrait] |
| **A-4** de Sitter, hors horizon | Rien d'explicite. Le regime hors horizon (k/a < H) est celui que [21] appelle « facteur d'echelle rapidement variable » : la forme (3.12) reste valide, mais la lecture en impulsion physique, sur laquelle repose la separation (3.10) de S2, ne l'est plus. | [extrait] + [derive] |

## 4. Consequences pour OP-IR [derive]

1. **L'echelle H est exclue dans le cadre de [21].** [reformule IR-d'' : aucun terme en H² dans l'operateur effectif, sous hypotheses, greffe point 1] Le lemme d'integration est une identite : toute la dependance en Ω est dans S_B, exacte. S_flat est une fonctionnelle du seul champ du repere plat et ne contient pas H. Le scenario d'annulation de C-b (log(−∂²e^{−2Ω}/M²) → log(H²/M²)) exigerait une dependance en Ω dans S_flat ; la structure de [21] l'interdit. La valeur −4H² de Bochner (NOTE-102, D2) vient d'une covariantisation tronquee : elle est compensee par les autres termes de courbure du morceau invariant de Weyl. L'accord de Hodge avec S2 (0 sur couche de masse) n'est pas un hasard.

2. **Correction a NOTE-102 §3 point 2.** Le terme residuel de S2 (seconde ligne de (3.9) de S2) agit sur {u'' + k²u}, qui est d'ordre β̃ pour le mode corrige. Le residu est donc d'ordre β̃² dans l'equation de mode, quelle que soit sa valeur singuliere sur le mode libre. Les resultats de NOTE-102 au premier ordre n'en dependent pas. L'inquietude « log 0 sur couche de masse » de NOTE-102 etait surestimee pour le premier ordre.

3. **Ce qui reste (OP-V3).**
   - (a) **Domaine de validite de S_flat.** [21] exige F² ≪ ∇²F (dans la normalisation de S2, ou e est absorbe dans A). Pour le mode de NOTE-102, F ~ k u₀ et ∇ ~ k : la condition s'ecrit **u₀ ≪ k**. Elle est **independante du temps**, car le rapport B_phys/k_phys² = F/k² est invariant sous le facteur conforme. Pour le champ strictement uniforme de NOTE-98 (k = 0), elle est violee : c'est le regime « champ constant » que [21] laisse ouvert. Ce cas releve d'une action plate de type Euler-Heisenberg, deja identifiee par C-b (H1). Par le point 1, cette action resterait sans Ω et ne compenserait pas le ln a, mais elle n'est pas calculee.
   - (b) **Etat.** L'action plate suppose le vide de Minkowski du repere conforme, c'est-a-dire le vide conforme (Bunch-Davies pour des fermions sans masse). C'est deja l'hypothese H3 de NOTE-100.
   - (c) **Variation metrique hors des orbites de Weyl** : toujours inaccessible (S2 note 4). Elle concerne le tenseur energie-impulsion complet, pas l'equation de mode.

## 5. Verdict
**OP-V1 qualifie OP-V3.**
- OP-V1 : [21] etablit l'action Weyl-plate comme exacte dans sa partie anomale, avec l'operateur plat du repere conforme ; un terme en H² de type Bochner est exclu. La qualification IR-V3 de NOTE-102 est **levee quant au choix de l'operateur**.
- Qualification OP-V3 : [21] ne dit rien de l'infrarouge ni de de Sitter, et ne couvre l'action plate que pour des champs rapidement variables (u₀ ≪ k pour le mode). Le cas uniforme de NOTE-98 est hors de ce domaine.

## 6. Confrontation a la prediction
Prediction (NOTE-103 §4) : « OP-V1 qualifie OP-V3 : operateur plat, pas de terme en H² ; comportement sur couche de masse et echelle infrarouge laisses ouverts ». **Realisee**, avec deux ecarts :
- (i) la question de la couche de masse perd son poids au premier ordre (point 4.2) ;
- (ii) la reserve qui subsiste vraiment est le domaine de validite de S_flat, que la prediction n'avait pas nomme.

## 7. Bilan sur OP-IR et NOTE-102
| Element | Avant (NOTE-102) | Apres (NOTE-104) |
|---|---|---|
| Choix de l'operateur | ambigu (S2, Hodge, Bochner) | **plat du repere conforme** ([21]) |
| Echelle H | possible (Bochner) | **exclue** dans le cadre [21] (terme en H², sous hypotheses) |
| Residu sur couche de masse | reserve | **sans effet au premier ordre** |
| Verdict NOTE-102 | IR-V1 qualifie IR-V3 | **IR-V1**, qualification reduite au domaine de validite de S_flat ; critere d'etat Q_tf ≠ 0 (NOTE-108) |
| Champ uniforme (NOTE-98) | ln a si echelle comobile | ln a porte par S_B exact ; S_flat de champ constant non calcule |

## 8. Greffes proposees (non entees)
- **IR-d** : porter sur NOTE-102 la correction du §4.2 (residu d'ordre β̃²) et la reduction de la qualification IR-V3.
- **IR-e** : instruire le regime de champ constant (action plate de type Euler-Heisenberg pour des fermions sans masse) et verifier qu'elle n'introduit aucun ln a ; c'est la seule voie qui reste pour le champ uniforme de NOTE-98.
- **IR-f** : audit froid aveugle de NOTE-102 et NOTE-104 ensemble.

## 9. Non-surclassement
Lecture de source, [conv]. M-V3 reste un candidat conditionnel ; ses conditions se resserrent sans qu'il soit grave. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.
