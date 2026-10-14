---
id: NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION
numero: 92
serie: I
branche: Q-M3 suite (chantier D / CCC + M)
reservation: 2026-10-09T17:04 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 92)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
calibration: "[calcule] dans le cadre fige (script v5, EXIT 0) ; lecture physique [derive]"
gel: NOTE-BORD-EON-91-ARMEMENT-Q-M3-LOG (sha256 9bdb1d59c6bf3e09bc7496b20d81d85736a24798a3b8361b8d8d9b3d31f9d4c8, 2026-10-09T17:05:08Z)
scripts:
  - q_m3_log.py (v1, 815d3a7c..., 17:06:08Z) : ECHEC, sympy integre 1/tau en log(tau) avec tau < 0
  - q_m3_log_v2.py (2016b267..., 17:06:32Z) : donnee d'etat supposee LISSE, plus etroite que le gel ; resultat partiel
  - q_m3_log_v3.py (74a95854..., 17:07:00Z) : conditions imposees a tous les ordres, au-dela de la troncature ; incompatibilite FAUSSE
  - q_m3_log_v4.py (c38225f6..., 17:07:26Z) : inconnues incompletes, linsolve vide, ligne CONCLUSION imprimee SANS FONDEMENT
  - q_m3_log_v5.py (d240832c..., 17:07:45Z) : version de reference, EXIT 0
depend: [NOTE-BORD-EON-91-ARMEMENT-Q-M3-LOG, NOTE-BORD-EON-90-Q-M3-EXECUTION]
rouvre_si:
  - "modele de champs de l'etat anomal (fixe la contrainte anisotrope et tranche l'isotropie asymptotique)"
  - "secteurs vectoriel et tensoriel, ou traitement non lineaire"
  - "ordres superieurs a tau^1 (au-dela de la troncature)"
---

# NOTE-92 : le terme en ln Ω de (2.17), cas inhomogene. Verdict **L-V4**, qualifie par L-V3

## 0. Resume
Dans le cadre fige (source test lineaire sur de Sitter, un mode e^{ikx}, secteur scalaire, trace imposee `T̂ = A Ω⁴`, conservation exacte, donnee d'etat polyhomogene), aux ordres controles :
- **le ln Ω est toujours present dans la source** des que A ≠ 0 (aucune completion reguliere n'en est exempte) ;
- **le second membre de (2.17) n'est regulier que pour un etat precis** : pas de contrainte anisotrope aux ordres Ω⁰ et Ω¹, et une structure logarithmique dominante **isotrope** (`X_00 = A τ² ln Ω`, `X_ii = (A/3) τ² ln Ω`) ;
- **tout autre etat rend (2.17) singulier**, en ln Ω ou par des poles Ω⁻¹, Ω⁻².

La regularite du canal de jauge sous C-M1 devient une **condition sur l'etat** : isotropie asymptotique a 𝓘⁺. Ce n'est ni une obstruction du canal en soi, ni une regularite automatique.

## 1. Les equations [calcule, v5]
Avec `a = X_00`, `b = −i X_0x`, `c = X_xx`, `d = X_yy = X_zz` (composantes g-orthonormees de Friedrich) et `T* = A τ²` :

```
trace          : −a + c + 2d = A τ²
conservation 0 : τ a' − 2a = A τ² − k τ b
conservation x : τ b' − 2b = k τ c
```
Exposant indiciel 2 pour a et b. La source A τ² est resonante : c'est l'origine du ln. La donnee d'etat libre est `c` (contrainte anisotrope).

## 2. Resultats

### 2.1 Conditions de regularite aux ordres controles [calcule, v5]
`c = c₀ + c₁τ + c₂τ² + c₃τ³ + (e₀ + e₁τ + e₂τ² + e₃τ³) ln Ω + (f₂τ² + f₃τ³) ln² Ω`. La regularite du second membre de (2.17) aux ordres τ^m, m ≤ 1 (seuls controles par la troncature), a pour solution generale :

| Coefficient | Valeur imposee | Sens |
|---|---|---|
| c₀, c₁ | 0 | pas de contrainte anisotrope aux ordres Ω⁰, Ω¹ (sinon poles Ω⁻², Ω⁻¹) |
| e₀, e₁, e₃, f₂, f₃ | 0 | pas d'autre structure logarithmique |
| **e₂** | **A/3** | ln Ω isotrope a l'ordre Ω² |
| c₂, c₃, α, β | libres | donnees non contraintes a ces ordres |

### 2.2 Ce que cela veut dire
- Le cas homogene isotrope de NOTE-90 (`c = d`) satisfait exactement ces conditions : c'est pourquoi (2.17) y etait nul.
- **Exemple de singularite** (v2) : etat sans ln dans c (e₂ = 0) : composante (1,0,1) du second membre egale a `κ(A + c₀k²)/2 · ln Ω`. Choisir `c₀ = −A/k²` tue le ln mais cree un pole `−c₀κ/2 · Ω⁻²`. Il n'existe aucune issue avec un etat lisse.
- La condition reguliere est **independante de k** et se raccorde a la limite homogene.

```
              etat de la source a I+                     second membre de (2.17)
  ------------------------------------------------   ------------------------------
  anisotropie O(Omega^0) ou O(Omega^1)             -> poles Omega^-2, Omega^-1
  pas de ln dans c (etat "lisse")                  -> ln Omega, coefficient kappa*A/2
  ln isotrope a l'ordre Omega^2 (e2 = A/3)         -> regulier (ordres controles)
```

## 3. Verdict
- **L-V4 realise** : la regularite est une condition sur l'etat (isotropie asymptotique), pas une propriete du canal.
- **Qualification L-V3** : le ln est force dans la source dans toute completion reguliere ; il ne mord pas sur (2.17) seulement pour l'etat isotrope.
- Prediction du gel : L-V4. **Realisee.** Inclinaison declaree **non realisee** : le ln n'est pas evitable au prix d'un terme en 1/k² (ce choix cree un pole), et le coefficient du ln dans (2.17) n'est pas proportionnel a k (il vaut κ(A − 3e₂)/2 pour la composante (1,0,1)).

## 4. Portee sur Q-M3 et CCC + M
Q-M3(a), deplacee par NOTE-90 vers la partie sans trace, est maintenant **precisee** : sous C-M1, le canal de jauge est compatible avec la regularite de (2.17) au niveau lineaire **si et seulement si** l'etat est asymptotiquement isotrope a 𝓘⁺, aux deux premiers ordres de la contrainte anisotrope. CCC + M recoit donc une condition supplementaire, de type « pas de cheveux » pour l'etat de matiere, qui s'ajoute a C-M1, C-M2, C-M4. Aucune incompatibilite n'est etablie (pas de M-V3). Q-M3 reste ouverte : la question devient de savoir si l'etat anomal reel satisfait l'isotropie asymptotique.

## 5. Passe adverse interne (ne vaut pas audit froid)
1. « Quatre versions defectueuses avant la bonne. » Exact, toutes conservees avec leur sortie et leur defaut nomme (frontmatter). La v4 a imprime une conclusion sans fondement : c'est le defaut le plus grave, intercepte par la v5 qui garde l'ensemble vide.
2. « La troncature a τ³ et les conditions limitees aux ordres m ≤ 1 laissent ouverts les ordres superieurs. » Exact ; c'est une condition de `rouvre_si`.
3. « Un seul mode, secteur scalaire, lineaire, fond fixe. » Exact ; le resultat ne vaut que dans ce cadre (gel §7).
4. « La contrainte anisotrope est traitee comme libre alors que l'etat physique la fixe. » C'est precisement ce que le verdict isole : la question physique restante.
5. « Le critere de regularite est le second membre de (2.17) seul. » Exact ; (2.13)-(2.16) ont ete examines pour la trace en NOTE-90 §3.3, pas pour cette partie sans trace.

## 6. Non-surclassement
[conv], non audite a froid, non scelle. RG-4 (CCC, forme actuelle) inchangee. CCC + M : hypothese ouverte, une condition d'etat ajoutee, non tranchee. Noyau {A4 ; A2★ ; N} inchange, p_Q non fixe, N non chiffre.
