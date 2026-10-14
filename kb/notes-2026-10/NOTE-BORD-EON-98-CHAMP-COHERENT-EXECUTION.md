---
id: NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION
numero: 98
serie: I
branche: Q-M3 suite (champ coherent)
reservation: 2026-10-10T12:12 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 98)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
calibration: "[calcule] (script v3, EXIT 0, forme close) pour CB-1 a CB-4 ; [derive] pour l'argument de symetrie du §3"
gel: NOTE-BORD-EON-97-ARMEMENT-CHAMP-COHERENT (sha256 510f9c6fabadf3112b8e1095ac016e70417141519e95aa1d1db300720fc8aa61, 2026-10-10T12:14:27Z)
scripts:
  - cb_coherent.py (v1, 8fb36218..., 12:15:26Z) : ECHEC, log(-1/tau) non reduit ; sortie partielle deja porteuse
  - cb_coherent_v2.py (7f9dfded..., 12:15:43Z) : ECHEC, simplify reecrit log(-tau) en log(tau) + i pi pour tau < 0
  - cb_coherent_v3.py (9c7d5c04..., 12:15:59Z) : reference, coordonnee s = -tau = Omega > 0, EXIT 0
incident: "la sortie originale de v2 a ete ecrasee par celle de v1 lors d'une copie (erreur de manipulation) ; v2 (script intact, deterministe) a ete relancee, sortie conservee sous cb_coherent_v2_sortie_REGENEREE.txt, meme echec"
sources: ["arXiv:1808.08237v2 (S2)"]
depend: [NOTE-BORD-EON-97-ARMEMENT-CHAMP-COHERENT, NOTE-BORD-EON-96-ISOTROPIE-ETAT-ANOMAL-EXECUTION, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION]
rouvre_si:
  - "audit froid discordant"
  - "completion covariante de l'anomalie qui ne soit pas de la forme ∫ Ω[g] F² (termes non locaux en F, ou contribution covariante de S_flat dependant de l'anisotropie)"
  - "champ coherent inhomogene ou a k fini (le champ uniforme est la limite hors horizon)"
---

# NOTE-98 : champ magnetique coherent a 𝓘⁺. Verdict **CB-V2**, qualifie par CB-V3

## 0. Resume
Pour un champ magnetique uniforme dans le modele de S2 (couplage de Maxwell courant en ln a), avec la fermeture C-iso du secteur non Maxwell :
- le second membre de l'equation (2.17) de Friedrich porte un **terme en ln Ω non borne, de coefficient κβ̃B₀²/e²** (CB-V2) ;
- la regularite exigerait que le secteur non Maxwell porte une contrainte anisotrope **exactement opposee** a la partie logarithmique anisotrope du secteur Maxwell (CB-V3) ;
- argument [derive] : pour toute completion covariante de la forme `∫ Ω[g] F²` (S2, eq. 2.13 : Riegert ou toute fonctionnelle de la metrique seule), la partie non Maxwell est **necessairement isotrope** pour un champ uniforme ; la compensation est impossible et C-iso est impose, pas choisi. Le terme en ln Ω survit dans toute cette classe.

## 1. Resultats [calcule, v3]

| Etape | Resultat |
|---|---|
| Maxwell `∂_μ(I² F^μν) = 0` | satisfait exactement par `F_xy = B₀` |
| Secteur Maxwell | `X^M = (B₀²/e²) Ω² (½ − β̃ ln Ω) · diag(1, 1, 1, −1)`, trace nulle |
| Non-conservation du secteur Maxwell | `∇̂^μ X^M_μ0 = β̃B₀² Ω³/e²` (echange avec le secteur anomal) |
| Trace anomale (variation de Weyl de S_B) | `T̂ = −(β̃B₀²/e²) Ω⁴`, soit `A = −β̃B₀²/e²` ; controle independant concordant |
| Fermeture C-iso | `X^R = diag(r₀, r₁, r₁, r₁)`, `r₀ = C Ω²`, `r₁ = (C − β̃B₀²/e²) Ω²/3` ; conservation totale exacte |
| (2.17), composantes non nulles | (1,0,1), (2,0,2) : `κB₀²/e² (½ − β̃/3 − β̃ ln Ω)` ; (3,0,3) : `−2 ×` le meme |
| Termes non lisses | **ln Ω**, coefficients `−κβ̃B₀²/e²`, `−κβ̃B₀²/e²`, `+2κβ̃B₀²/e²` |
| Controle β̃ = 0 | constantes, regulier |
| Budget anisotrope `Π diag(0,1,1,−2)` (conserve automatiquement) | regularite ⟺ `Π = (2β̃B₀²/3e²) Ω² ln Ω + p₂Ω² + …` (p₀ = p₁ = q₃ = 0) |
| Partie anisotrope logarithmique du secteur Maxwell | `Π_M = −(2β̃B₀²/3e²) Ω² ln Ω` : **Π requis = −Π_M** |

```
  secteur Maxwell (S2)            secteur anomal hors orbite de Weyl         (2.17)
  -------------------------       ----------------------------------       ---------------
  ln Omega anisotrope         +   isotrope (C-iso, ou impose §3)       ->  ln Omega non borne
  ln Omega anisotrope         +   anisotropie exactement opposee       ->  regulier
```

## 2. Lecture
- Le resultat prolonge NOTE-92 au secteur homogene anisotrope : la regularite de (2.17) exige que la partie logarithmique totale soit isotrope. Le champ coherent y apporte une partie logarithmique anisotrope, portee par son tenseur de Maxwell (CB-1), qui n'est compensee que si le secteur anomal non Maxwell porte l'anisotropie opposee.
- La limite β̃ → 0 est reguliere : l'obstruction est entierement due a l'anomalie, avec le coefficient β̃B₀².

## 3. Portee de la fermeture : argument de symetrie [derive, a auditer]
S2 (2.13) [extrait] : la dependance anomale en Ω se complete covariamment par une fonctionnelle de la metrique seule, `Ω[g]`, qui vaut le facteur de Weyl sur les metriques Weyl-plates (« One example is the Riegert functional » ; d'autres existent, refs [22-24] de S2). L'action anomale covariante est alors `S_B = −(β̃/2e²) ∫ √g Ω[g] F_μν F^μν`. Sa variation metrique a deux parties :
- (a) a Ω[g] fixe, variation de `√g F²` : `∝ Ω[g] × T^Max_μν`. C'est la partie logarithmique du secteur Maxwell (CB-1), anisotrope.
- (b) variation de Ω[g] : `∫ d⁴x F²(x) δΩ[g](x)/δg^μν(y)`. Le bitenseur `δΩ[g]/δg` est construit sur le seul fond de Sitter, invariant par rotations spatiales ; la source `F²(x) = 2B₀²` est un **scalaire uniforme**. Le resultat en y est donc invariant par rotations : **isotrope**.
Consequence : dans toute completion de cette classe, le secteur non Maxwell est isotrope ; la conservation et la trace le fixent alors (a la constante de rayonnement C pres). C'est C-iso. La compensation requise au §1 est impossible, et le terme en ln Ω de (2.17) survit.
Hors de cette classe (non couvert) : contributions covariantes de S_flat (terme non local `F log(−□) F`), termes non locaux en F au-dela de l'action simplifiee, ou completion qui ne soit pas de la forme `Ω[g] F²`.

## 4. Verdict
- **CB-V2 realise** : sous C-iso, (2.17) porte un ln Ω de coefficient proportionnel a β̃B₀² ≠ 0.
- **Qualification CB-V3** : la regularite exigerait un budget anisotrope exactement oppose a celui du secteur Maxwell. Par l'argument du §3 [derive], ce budget est nul dans toute completion de la forme ∫ Ω[g] F² : la qualification CB-V3 y est vide et CB-V2 y vaut sans condition de fermeture.
- Prediction du gel (CB-V2 qualifie CB-V3, budget exactement oppose) : **realisee**, y compris l'egalite exacte du budget.

## 5. Portee sur Q-M3 et CCC + M
- Candidat **M-V3 conditionnel** (a lecture exterieure, non grave) : sous C-M1, un champ magnetique classique coherent present a 𝓘⁺ rend le second membre de (2.17) logarithmiquement singulier, au niveau lineaire, dans le modele de S2 et pour toute completion covariante de la forme ∫ Ω[g] F². Conditions : modele de S2 (action simplifiee), champ uniforme (limite hors horizon), lineaire, fond fixe, argument de symetrie [derive].
- La condition d'etat de CCC + M (NOTE-92, NOTE-96) se precise : **aucun champ electromagnetique classique coherent ne doit atteindre 𝓘⁺**, sous peine de singularite logarithmique, dans le cadre ci-dessus. Les champs magnetiques coherents ne se diluent pas dans le cadre conforme (B₀ constant).
- RG-4 (CCC, forme actuelle) inchangee ; ce resultat porte sur CCC + M.

## 6. Passe adverse interne (ne vaut pas audit froid)
1. « Deux echecs techniques (v1, v2). » Exact, conserves ; la v1 contenait deja le resultat porteur, la v3 le confirme en forme close.
2. « L'argument du §3 est [derive]. » Exact : il est le point le plus fort et le plus fragile ; il est soumis en priorite a l'audit froid.
3. « Le champ uniforme est une idealisation. » C'est la limite hors horizon (k ≪ aH), vers laquelle tend tout mode coherent a 𝓘⁺ ; le terme log(k²) de S2 diverge alors mais ne change pas la dependance en ln a (S2, choix a⋆ = k/M).
4. « Le second membre constant a β̃ = 0 est-il regulier ? » Oui : fonction lisse (constante) ; Maxwell est conforme.
5. « La constante C du fluide isotrope peut-elle aider ? » Non : elle n'entre pas dans les termes non lisses (verifie, R ne depend pas de C).

## 7. Non-surclassement
[conv], non audite a froid, non scelle. Aucune incompatibilite n'est gravee : M-V3 reste un candidat conditionnel. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.
