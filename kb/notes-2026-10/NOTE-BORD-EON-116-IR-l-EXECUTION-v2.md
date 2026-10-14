---
id: NOTE-BORD-EON-116-IR-l-EXECUTION
numero: 116
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-l)
reservation: 2026-10-11T15:54 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 116)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 8436e99a79bc0b3caee11813185acdf968808624a5995822aa198f8555688d85 (conservee)"
greffe: "IR-m-b entee le 2026-10-11 par NOTE-BORD-EON-121 (corrections de l'audit froid aveugle NOTE-120, AU-V2)"
audit: "NOTE-BORD-EON-119 (gel) / NOTE-BORD-EON-120 (concordance) : AU-V2 ; formule de Q_k, composante E l=2 et codimension 5 retrouvees en cecite stricte par M-a2"
gel: NOTE-BORD-EON-115-ARMEMENT-IR-l (sha256 7ed4cd22f2b9db9947891b3d0857609b7c326714680e0ef2951eba69ead66710, 2026-10-11T15:54:54Z)
instruments:
  - "ir_l.py (v1), sha256 2c6234d20252fc3de3c8636f24afe7e45fb2b101a27e1de1ba4520e9c44f110e, 2026-10-11T15:56:32Z : INTERROMPUE (integration angulaire symbolique trop lente), sortie partielle conservee ir_l_v1_sortie_INTERROMPUE.txt (parties A et B, concordantes avec la v2)"
  - "ir_l_v2.py, sha256 bc17eb35414874c0bddd2cb956258f1464848e533d7d791edef91ebb74a2c38c, 2026-10-11T16:06:48Z : EXIT 0, sortie ir_l_v2_sortie.txt (moyennes angulaires par moments isotropes exacts)"
depend: [NOTE-BORD-EON-115-ARMEMENT-IR-l, NOTE-BORD-EON-114-ACTE-GREFFE-IR-d3, NOTE-BORD-EON-113-AUDIT-IR-g-CONCORDANCE]
verdict: "L-V1"
prediction_realisee: "oui"
rouvre_si:
  - "source persistante jusqu'a scri+ ; charges nettes"
  - "fermeture non Maxwell (H-loc) pour un champ localise ; ordres superieurs"
---

# NOTE-116 : IR-l. Q_tf = 0 est exceptionnel pour une source causale. Verdict **L-V1** (v2 : voir greffe)

> **Greffe IR-m-b (v2, 2026-10-11).** Corrections issues de l'audit froid aveugle NOTE-120 (AU-V2). Les resultats porteurs sont inchanges : la formule exacte de Q_k, la polarisation lineaire seule, la composante E ℓ = 2 seule et la codimension 5 ont ete retrouvees en cecite stricte par M-a2 et reproduites par M-b.
> 1. **Enonce reformule** (§0, schema du §3, §3 L-3, §4, §6). L'enumeration « seules y echappent une source a helicite pure, un motif sans composante E ℓ = 2, ou un ensemble isotrope » etait **tautologique** : la deuxieme classe est la condition elle-meme. Elle laissait aussi croire que l'helicite est le mecanisme d'echappement. Enonce correct : **Q_tf = 0 si et seulement si la composante E ℓ = 2 du motif de polarisation lineaire, ponderee en k, s'annule (5 conditions reelles).** L'helicite pure dans toutes les directions et l'ensemble isotrope en sont deux cas. D'autres cas physiques existent :
>    - p ∥ m de meme amplitude **en phase**, d'helicite nulle (motif B pur, alors que L ≠ 0 localement) ;
>    - p = x̂ + iŷ avec m = x̂ − iŷ.
>
>    Pour une source dipolaire, la condition s'ecrit STF Re(pp†) = STF Re(mm†) (termes croises E1 × M1 nuls par parite). **L'helicite n'est ni necessaire, ni suffisante lorsqu'elle est partielle.**
> 2. **Interference** (§2D, §3 L-2) : la moyenne vers 0 est **asymptotique** (|t₀| grand devant la duree de la source ; pour une enveloppe gaussienne de largeur σ, le rapport interference sur diagonale vaut environ e^{−2t₀²/σ²}, soit 0,13 pour σ = 10, t₀ = −10) et **globale** (moyenne spatiale). Avec une bande a bords francs, la decroissance n'est qu'en O(1/(|t₀|Δk)). Pour un aimant eteint (cas de NOTE-111), le rapport tombe a 4·10⁻⁵ des |t₀| = 2.

## 0. Resume
Pour une source causale eteinte avant 𝓘⁺, Q a une expression exacte en fonction des composantes du courant sur couche de masse, J₊ = Ĵ(+k) et J₋ = Ĵ(−k) :

  Q_k = −½ L(J₊J₊† + J₋J₋†) − ½ Re(J₊·J₋*) (δ − k̂k̂),

ou L est le tenseur de **polarisation lineaire** (partie symetrique sans trace dans le plan transverse). L'intensite et la polarisation circulaire ne contribuent pas. Le second terme est une interference qui oscille en cos(2k t₀) avec l'instant d'emission ; il se moyenne vers 0 pour une emission sous-Hubble. Il reste alors Q_tf = −½ Σ_k L_k. Apres integration sur les directions, seule la composante **quadrupolaire de type E** (ℓ = 2) du motif de polarisation survit. Annuler Q_tf impose donc **5 conditions reelles** : une source generique ne les satisfait pas. [corrige IR-m] Q_tf = 0 si et seulement si la composante E ℓ = 2 ponderee s'annule ; l'helicite pure (dipole chiral) et l'ensemble isotrope en sont deux cas, a cote d'autres (p ∥ m en phase, d'helicite nulle ; p = x̂ + iŷ, m = x̂ − iŷ). Le ln Ω existe donc pour une source causale generique.

## 1. Incident d'instrument (R-55)
La v1 (integration angulaire symbolique) a depasse le temps d'execution ; ses parties A et B, ecrites avant l'interruption, sont conservees et concordent avec la v2. La v2 remplace l'integration par les moments isotropes exacts des monomes de n (meme calcul, methode exacte et rapide).

## 2. Resultats [calcule] (ir_l_v2_sortie.txt)

### A. Champ a 𝓘⁺ d'une source eteinte (fonction de Green retardee)
a = A_k(0) = i(J₊ − J₋)/(2k), b = E_k(0) = −(J₊ + J₋)/2. Controle numerique sur une impulsion : a = −0,376427910603 et b = 0,800359009706, identiques par la fonction de Green et par la formule (12 chiffres).

### B. Decomposition exacte de Q_k
- Identite Re(R M Rᵀ − M) = −2 L(M) pour M hermitienne 2×2 (R rotation de 90° dans le plan transverse) : verifiee.
- Re(R C Rᵀ + C) = tr(C) 𝟙 : verifiee.
- Q_k calcule directement sur des J₊, J₋ complexes quelconques moins la formule ci-dessus : **0**.

Lecture : le terme magnetique k²(k̂ × a)(k̂ × a)† est le terme electrique tourne de 90°. Or une rotation de 90° change le signe de la polarisation lineaire et laisse intactes l'intensite et la polarisation circulaire. D'ou : seule la polarisation lineaire survit dans B B† − E E†.

### C. Moyennes angulaires de L (moments exacts)

| Source | ⟨L⟩ | Q_tf rayonne |
|---|---|---|
| dipole magnetique lineaire m | −(2/5)(mm − ⅓m²) | ≠ 0 (retrouve NOTE-108 D1 a la normalisation pres) |
| dipole electrique lineaire p | +(2/5)(pp − ⅓p²) | ≠ 0, signe oppose (dualite E ↔ B) |
| dipole magnetique **tournant** (x − iy) | diag(−2/15, −2/15, 4/15) | **≠ 0** |
| dipole **chiral** (p et m colineaires en quadrature, m = −ip) | L = 0 **dans chaque direction** | **0** |
| p ∥ m de meme amplitude **en phase** (helicite nulle) [ajout IR-m, M-a2, M-b] | L ≠ 0 localement, ⟨L⟩ = 0 (motif B pur) | **0** |
| p = x̂ + iŷ, m = x̂ − iŷ [ajout IR-m, M-b] | L ≠ 0 localement, ⟨L⟩ = 0 | **0** |
| ensemble isotrope d'orientations | 0 | 0 |
| motif E pur ℓ = 2 (tenseur A) | (2/5)A | ≠ 0 |
| motif B pur ℓ = 2 | 0 | 0 |
| combinaison generique (p, m, quadrupole electrique) | matrice pleine non nulle | ≠ 0 |

### D. Terme d'interference
Pour une impulsion en t₀ : J₊·J₋* ∝ e^{2ik t₀}. Moyenne sur une bande [k₁, k₁ + Δk] : [sin(2t₀(k₁ + Δk)) − sin(2k₁t₀)]/(2Δk t₀), qui tend vers 0 des que Δk·t₀ ≫ 1 (emission sous-Hubble au sens de la bande). [corrige IR-m] Cette decroissance n'est qu'en O(1/(|t₀|Δk)) pour une bande a bords francs ; pour un spectre lisse, elle est rapide mais exige |t₀| grand devant la duree de la source (enveloppe gaussienne : e^{−2t₀²/σ²}). La moyenne est asymptotique et globale.

## 3. Lecture [derive]
1. **L-1** : Q_tf ne voit que la polarisation **lineaire** du rayonnement, plus un terme d'interference proportionnel a (⅓𝟙 − k̂k̂). L'intensite et la polarisation circulaire s'eliminent exactement.
2. **L-2** : apres moyenne du terme d'interference, Q_tf = −½ ∫ L(k̂) sur les directions (et les modules). Une integrale de tenseur de spin 2 sur la sphere ne garde que sa composante ℓ = 2 de type E : la composante B est un pseudo-tenseur et donne 0, ce que confirme le calcul.
3. **L-3** : l'helicite **partielle** ne suffit pas (le dipole tournant, circulaire sur l'axe mais lineaire a l'equateur, donne Q_tf ≠ 0). Une helicite **pure** dans toutes les directions suffit, ce que realise le dipole chiral (p et m colineaires en quadrature, de meme amplitude). [corrige IR-m] Elle n'est pas necessaire : p et m colineaires de meme amplitude **en phase** (helicite nulle) donnent aussi Q_tf = 0, par un motif B pur. Pour des dipoles, la condition exacte est STF Re(pp†) = STF Re(mm†).
4. **L-4** : la composante E ℓ = 2 est un tenseur symetrique sans trace, soit 5 nombres reels. Q_tf = 0 impose ces 5 conditions ; une source generique (la combinaison testee) ne les remplit pas. La classe Q_tf = 0 est de codimension 5.

```
   source causale eteinte
          │
   J₊ = Ĵ(+k), J₋ = Ĵ(−k)  (courant sur couche)
          │
   ┌──────┴───────────────────────────┐
   terme diagonal                     terme d'interference
   −½ L(J₊J₊† + J₋J₋†)                −½ Re(J₊·J₋*) (δ − k̂k̂)
   (polarisation lineaire seule)      ∝ cos(2k t₀) → 0 si sous-Hubble
          │
   ∫ directions → composante E, ℓ = 2 (5 nombres)
          │
   = 0 si et seulement si cette composante E ℓ = 2 s'annule (5 conditions)
   cas : helicite pure, ensemble isotrope, motif B pur (p ∥ m en phase), ...   [corrige IR-m]
```

## 4. Verdict
**L-V1.** Q_tf = 0 est exceptionnel (codimension 5) pour une source causale ; une source generique, y compris un dipole tournant, donne Q_tf ≠ 0. [corrige IR-m] Q_tf s'annule si et seulement si la composante E quadrupolaire ponderee s'annule ; l'helicite pure et l'ensemble isotrope en sont deux cas parmi d'autres (motif B pur d'helicite nulle).

## 5. Confrontation a la prediction
Prediction (NOTE-115 §4) : « L-V1 ; polarisation lineaire seule ; composante E ℓ = 2 seule ; 5 conditions ; dipole chiral 0 ; dipole tournant ≠ 0 ; dipole lineaire (4/5)(mm − ⅓m²) a la normalisation pres ; ensemble isotrope 0 ; generique ≠ 0 ; interference se moyennant vers 0 ». **Realisee.** Coherence avec NOTE-108 D1 : ⟨ε_Bε_B − ε_Eε_E⟩ = Re(R M Rᵀ − M) = −2⟨L⟩ = −2·(−(2/5))(mm − ⅓m²) = (4/5)(mm − ⅓m²), exactement la valeur de NOTE-108.

## 6. Portee
- Le ln Ω de (2.17) existe pour un champ coherent issu d'une source causale **generique**. [corrige IR-m] Il n'en est exempt que si la composante E quadrupolaire ponderee du motif de polarisation lineaire s'annule : c'est le cas d'une helicite pure, d'un motif B pur (meme d'helicite nulle) ou d'un ensemble isotrope, entre autres.
- Pour CCC + M, la condition de regularite de (2.17) dans ce canal devient une condition de **fin reglage** de la polarisation des sources a 𝓘⁺ (5 conditions), sauf ensemble isotrope. M-V3 reste un candidat conditionnel (H-loc pour un champ localise, NOTE-111). Rien n'est grave. RG-4 inchangee.

## 7. Greffes proposees (non entees)
- **IR-k** (en cours, troisieme greffe demandee) : tester H-loc par la completion de Riegert pour une source localisee.
- **IR-m** : audit froid aveugle de NOTE-111 et NOTE-116.

## 8. Non-surclassement
[conv], audite par NOTE-120 (AU-V2) [corrige IR-m]. Etat a l'ordre zero, source compacte eteinte, cadre S2 + [21] pour la loi. Noyau {A4 ; A2★ ; N} inchange.
