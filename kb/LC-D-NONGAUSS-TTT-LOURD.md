---
id: LC-D-NONGAUSS-TTT-LOURD
titre: "Module D / front non-gaussien de D1 — PASSAGE LOURD du trois-point ⟨g₃g₃g₃⟩ (front §3.2, décision (a) de Thierry 2026-06-12). Successeur de LC-D-NONGAUSS-TTT v0.1 (qui RESTE gelé, baseline d'audit) ; honore les QUATRE exigences contractuelles de LC-AUDIT-LOG-NONGAUSS §5. Ce chaînon SCELLE (verif_D_nongauss_TTT_lourd.py, EXIT 0, 34 asserts = 15 phase 1 + 19 phase 2, sha256 2cb9343235d34d060ffcff144f34738d9ad361a87a8f2436c58bc81722946923 ; bi-phase R-10, dépôt de phase 1 sha e494c8c6…c294b en KB AVANT fetch, asserts 01-15 BYTE-IDENTIQUES) : [C/PL-A TELLE QU'ÉCRITE] l'identité de Ward d'OP éq. (6.42) telle qu'imprimée — 4S_d[(d−2)(d+3)a − 2b − (d+1)c]/[d(d+2)] = C_T, coefficients d=3 : (6, 2, 4, 15), consignation [E4] VÉRIFIÉE À LA SOURCE — REFERME EXACTEMENT, en d GÉNÉRAL, sur DEUX étalons libres imprimés : scalaire (5.12)→(5.5) et fermion (5.13)→(5.6), slack nul ; C_T^sc(d=3)=3/(32π²) (l'étalon de calibration de κ) RETROUVÉ À LA SOURCE (S₃=4π) ; refermeture programme κ·[1/(32π²)]=3/(4π⁴) aller-retour exact ⟹ |C_T|/N=1/(32π²) (nu) slack NUL — l'étalon Ward OP NUMÉRIQUE est opérationnel telle-qu'écrite (exigence P1'-A du léger SOLDÉE). [D/PL-B TRANCHÉE] énoncé EXPLICITE exhibé verbatim (MP p.6) : ε^A_ij ε^{*B}_ij = 4δ^{AB} ⟹ ε·ε* = 4 (pas 2) ; 4=2² absorbé par le catalogue {2,4,8} ; éq. (2.6) avec le 4 explicite RE-REFERME le spectre scellé 𝒫=2H²/(M_Pl²k³) slack nul ; insensibilité des ratios scellés re-dérivée (rescaling de base compensé) ; mode BD imprimé = mode des scellés ; R-4 du léger SOLDÉE PAR EXHIBITION. [B'/PL-D] invariance rang 3 par représentation, SANS consommer MP/OP : 8 configs d'hélicité (±2)³, orbites sous S₃×P = 2 classes EXACTEMENT ; cinématique trois-points sans masse exacte (branche holomorphe, conservation symbolique) ; UNICITÉ par classe (système de petit groupe det=−2≠0) : (−−+)⟹⟨12⟩⁶/(⟨13⟩²⟨23⟩²) [dim 2 = EINSTEIN] et (+++)⟹([12][13][23])² [dim 6 = W³] — la graduation en dérivées RECOUPE la scission Einstein/W³ du léger PAR UNE ROUTE INTERNE ⟹ dimension PAIRE = 2 = comptage 2+1 scellé ; l'impaire « hors bispectre » = scellé du léger RECOUPÉ, pas re-dérivé. [A/PL-C] non-régressions exactes (γ₃=8 ; π⁴/4 slack nul ; ⟨g₃³⟩_libre=0). [E] 0 entrée libre neuve < 5 sorties appariées. [F] firewall 6/6 + mutations pilotes M1-M4 hors sceau. R-7 : ZÉRO AMENDEMENT, quatre cibles tenues TELLES QU'ÉCRITES (troisième front entièrement sous la règle). PÉRIMÈTRE CONSIGNÉ : les (a,b,c) PROPRES du programme ne sont PAS dérivés — la CFT de raccordement reste [décision ouverte] ; liberté W³~(LH)⁴ [décision ouverte] ; quatre-point/boucles/non-perturbatif HORS périmètre (S1). SANS SURCLASSEMENT (§6.4) : « ancrage Ward numérique reproduit + forensique tranchée » = cohérence de coefficients, JAMAIS « secteur non-gaussien fermé / D1 fermé / N fixé / CCC démontrée ». Compte {A4 ; A2★ ; N} INCHANGÉ."
codename: LC-RACCORD
type: "chaînon (résultat scellé) — passage lourd du trois-point. Subordonné à LC-AUDIT-VERDICT §6.4. Successeur de LC-D-NONGAUSS-TTT (qui reste v0.1, baseline gelée) ; consomme LC-WORK-CADRAGE-NONGAUSS-LOURD v0.1 (cibles gelées, R-7)."
version: 0.2
langue: fr
date: 2026-06-12
maj: "2026-06-12 — v0.2 : patch STATUT-ONLY (option (b1) du menu de LC-WORK-REPRISE-POST-SYNTHESE-2 §3, tranchée par Thierry 2026-06-12 en régime de veille (a)) : « AUDIT À FROID PENDANT (S-L4) » → « AUDIT À FROID CLOS, verdict ACQUIS » conformément au statut faisant foi de LC-AUDIT-LOG-NONGAUSS-LOURD v0.1 (4/4 CONFIRMATION). AUCUNE autre modification — corps, sceaux et algèbre intouchés (le sceau verif_D_nongauss_TTT_lourd.py reste byte-identique, sha 2cb934…6923). | 2026-06-12 — v0.1 : création au scellement du passage lourd (cycle complet en une conversation : cadrage validé → phase 1 EXIT 0/15 déposée AVANT fetch → fetch tracé → sceau final EXIT 0/34 byte-identique sur la phase 1 → extraits+manifeste). R-7 tenue, zéro amendement. Audit à froid COMMANDÉ (S-L4), instruction à produire."
statut: "établi (algèbre), SCEAU FAIT — PL-A tenue TELLE QU'ÉCRITE (étalon Ward OP numérique : (6.42) imprimée refermée sur deux étalons libres en d général, slack nul ; refermeture |C_T|/N=1/(32π²) via κ scellé) ; PL-B TRANCHÉE (ε·ε*=4, énoncé explicite p.6 verbatim ; spectre scellé re-refermé ; R-4 soldée) ; PL-C tenue (non-régressions) ; PL-D tenue (dimension paire = 2 par représentation, graduation 2/6 ≡ Einstein/W³). Conditionnel aux scellés amont (A_T·N=16, n=2, relation BD, convention nue, κ=24/π²) et à la gravité d'Einstein. NON SCELLÉ / inchangé : (a,b,c) propres du programme (CFT de raccordement, décision ouverte) ; coefficient W³ (décision ouverte) ; quatre-point (S1). AUDIT À FROID CLOS (S-L4 soldée) — verdict ACQUIS, 4/4 CONFIRMATION, zéro rétro-ajustement (LC-AUDIT-LOG-NONGAUSS-LOURD v0.1) ; lot de propagation exécuté. Compte {A4 ; A2★ ; N} inchangé ; D1 non clos ; N non fixé ; CCC non démontrée."
prerequis_kb: [LC-WORK-CADRAGE-NONGAUSS-LOURD, LC-D-NONGAUSS-TTT, LC-AUDIT-LOG-NONGAUSS, LC-D-NONLIN-2PT, LC-D-CT-GAMMA, LC-D-CT-ATN, LC-AUDIT-LOG-NACTION-AVEUGLE, LC-D3-SPECTRE-K3, LC-AUDIT-VERDICT, LC-04-REFERENCES]
fichiers_compagnons_kb: [verif_D_nongauss_TTT_lourd.py, verif_D_nongauss_TTT_lourd_phase1.py, LC-WORK-AUDIT-EXTRAITS-MANIFESTE-LOURD.md, EXTRAIT_hepth9307010v2_WARD.pdf, EXTRAIT_1104_2846v2_P6.pdf]
tags_epistemiques: [établi (algèbre), formalisable, décision ouverte, hors de portée]
---

# Passage lourd du trois-point `⟨g₃g₃g₃⟩` — le contrat honoré telle-qu'écrite

> Subordonné à `LC-AUDIT-VERDICT §6.4`. Le passage léger (`LC-D-NONGAUSS-TTT` v0.1)
> **reste gelé** : ce chaînon est son successeur, pas son amendement. Sceau
> `verif_D_nongauss_TTT_lourd.py` (EXIT 0, **34 asserts**, bi-phase R-10).

---

## 0. Mandat et architecture `[fait]`

Exécution du front §3.2 sous les **quatre exigences contractuelles** héritées de
l'audit du léger (`LC-AUDIT-LOG-NONGAUSS §5`) : **(E-L1)** étalon Ward OP numérique
— P1'-A **telle qu'écrite** ; **(E-L2)** forensique `ε·ε*` avec extrait p.6 de MP
étendu à ce moment-là seulement ; **(E-L3)** R-7 armée dès le gel ; **(E-L4)**
périmètre S1. Cadrage paper-first `LC-WORK-CADRAGE-NONGAUSS-LOURD` v0.1 validé
**avant** tout calcul ; scopings S-L1..S-L6 tranchés « tout recommandé » ; cibles
PL-A..PL-D gelées **sans fetch**.

**Bi-phase stricte (S-L6, R-10).** Phase 1 interne (blocs [A], [B], [B']) écrite,
EXIT 0/15, **déposée en KB et validée AVANT le premier fetch**
(`verif_D_nongauss_TTT_lourd_phase1.py`, sha `e494c8c6…c294b`) ; mutations pilotes
M1-M4 vérifiées cassantes hors sceau. Le sceau final embarque le segment de phase 1
**byte-identique** (extraction mécanique, vérifiée). Phase 2 = fetch tracé
(OP p.19/20/27/28 ; MP p.6/7 — manifeste + extraits, sha complets).

---

## 1. PL-A telle qu'écrite — l'étalon Ward OP **numérique** `[établi — algèbre ; bloc C]`

L'éq. **(6.42)** d'OP, telle qu'imprimée (p.27) :

$$4S_d\,\frac{(d-2)(d+3)\,a \;-\; 2\,b \;-\; (d+1)\,c}{d(d+2)} \;=\; C_T,$$

coefficients en `d=3` : **(6, 2, 4, 15)** — la consignation **[E4]** de
`04_references` est **vérifiée à la source**.

**Validation numérique sur DEUX étalons libres imprimés, en `d` général :**
- **scalaire** : `(a,b,c)` de (5.12) insérés dans (6.42) ⟹ `C_T = nφ·d/((d−1)S_d²)`
  = (5.5) **exactement** (le polynôme interne se factorise :
  `2d²(d−1)²(d+2)`, slack nul) ; en `d=3`, `S₃=4π` ⟹ `C_T^sc = 3/(32π²)` —
  **l'étalon de calibration de `κ` (NACTION-AVEUGLE) retrouvé à la source** ;
- **fermion** : (5.13) ⟹ (5.6) **exactement** (`−(d+2)c` se simplifie), deuxième
  étalon indépendant, slack nul.

**Refermeture programme.** Le dictionnaire scellé `κ = 24/π²` ferme l'aller-retour
exactement : `κ·[1/(32π²)] = 3/(4π⁴)` (la valeur OP scellée) et inversement ⟹
**`|C_T|/N = 1/(32π²)` (nu), slack nul**, porté par l'appareil d'OP avec ses
valeurs imprimées. Les coefficients de Ward sont des **rationnels purs** : le
verrou dimensionnel de phase 1 ([B-3], `Δ=d ⟹` coefficient sans dimension) est
**saturé** — aucun paramètre dimensionnel neuf ne peut entrer au secteur Ward.

**Périmètre, sans surclassement.** Les `(a,b,c)` **propres** du programme ne sont
pas dérivés : il n'existe pas de CFT de raccordement exhibée dont on lirait ces
coefficients — c'est l'item `décision ouverte` hérité, **inchangé**. Ce que PL-A
établit telle qu'écrite : le secteur Ward de `⟨TTT⟩`, dans l'appareil numérique
d'OP validé sur deux étalons imprimés, **porte** `C_T` en nombres purs et referme
sur `1/(32π²)` nu via le dictionnaire scellé. **L'exigence §5 de l'audit du léger
est SOLDÉE** (P1'-A testée telle qu'écrite, plus « dS-native seulement »).

## 2. PL-B tranchée — forensique `ε·ε*` `[établi — algèbre ; bloc D]`

Énoncé **explicite** exhibé verbatim (MP **p.6**, extrait au manifeste) :
« *The helicities can be normalized by* `ǫ^A_ij ǫ^{*B}_ij = 4δ^{AB}` » ⟹
**`ε·ε* = 4`**, pas 2 — **R-4 du léger soldée par exhibition** (la page attendue
était la bonne). Conséquences scellées :
- `4 = 2²` ∈ catalogue `{2,4,8}` : artefact de normalisation de base, **absorbé**,
  aucun nombre neuf ;
- l'éq. **(2.6)** (p.7) avec le 4 explicite **re-referme le spectre scellé** :
  `(1/2k³)(H/M_Pl)²·4 = 2H²/(M_Pl²k³) = 𝒫` — le 4 imprimé **est** la convention
  sous laquelle les scellés du programme sont vrais, slack nul ;
- **insensibilité re-dérivée** : `ε→λε ⊗ γ_cl→γ_cl/λ` laisse le champ physique
  invariant ⟹ les ratios scellés du léger (`π⁴/4`, `64π⁴/N²`, `O(1)`) sont
  `ε`-indépendants — le second volet de PL-B est tenu, aucun impact à consigner ;
- non-régression de source : le mode BD imprimé p.6, `(1−ikη)e^{ikη}`, est le
  mode des scellés (`CT-DUAL-DS`).

## 3. PL-D — invariance rang 3 `[établi — algèbre, niveau arbre ; bloc B', phase 1]`

Dérivé **sans consommer MP/OP** (phase 1, avant fetch) : (i) 8 configurations
d'hélicité `(±2)³`, orbites sous `S₃×P` = **2 classes exactement**
({tout-même} ⊔ {un-différent}) ; (ii) cinématique trois-points sans masse exacte
(branche holomorphe, conservation `Σλλ̃=0` symbolique, `[ij]≡0`, `⟨ij⟩≠0`) ;
(iii) **unicité par classe** : la covariance de petit groupe est un système
linéaire 3×3 de déterminant `−2 ≠ 0` ⟹ `(−−+) ⟹ ⟨12⟩⁶/(⟨13⟩²⟨23⟩²)` et
`(+++) ⟹ ([12][13][23])²` ; (iv) graduation en dérivées **2** et **6** ⟹ la
scission **Einstein / W³** du léger est recoupée **par une route interne**,
indépendante du fetch MP∩OP ⟹ **dimension paire = 2** = comptage `2+1` scellé.
L'impaire « hors bispectre » est le scellé du léger, **recoupé** (cohérence
trans-rang), pas re-dérivé. Conditionnalités : niveau arbre (S1) ; squelette de
petit groupe sur cinématique plate complexifiée ; la complétion dS de chaque
structure est **exhibée** (actions Einstein et `W³` sur dS), non re-classifiée.
Corroboration **excédentaire** (postérieure au gel de phase 1, ne l'a pas
informée) : MP p.7 §2.2 emploie eux-mêmes le squelette plat trois-points.

**Effet de comptage interne :** le front « rang-3 par invariance » rendu
formulable par `LC-D-NONLIN-2PT` est **absorbé ici** (S-L1a) — il cesse d'être
une décision ouverte séparée du menu.

## 4. PL-C, anti-numérologie, firewall `[établi — algèbre ; blocs A, E, F]`

Non-régressions **exactes** : `γ₃ = n³`, `n=2 ⟹ 8` ; `(H/M_Pl)⁴/A_T² = π⁴/4`
slack nul ; `(−i/3)³ = i/27` et moment impair gaussien nul ⟹ `⟨g₃³⟩_libre = 0`.
**DoF** : 0 entrée libre neuve < 5 sorties appariées neuves (étalon scalaire `d`
général ; étalon fermion `d` général ; aller-retour `κ` ; spectre re-refermé avec
le 4 explicite ; [E4] vérifié à la source). **Firewall 6/6** : coefficient Ward
`+1` ; `b↔c` ; `ε·ε*=2 ⟹` spectre faux ; `κ` faussé ; `d=4 ⟹ (14,24)` ;
`C_T×2`. Mutations pilotes M1-M4 vérifiées cassantes **hors sceau** avant dépôt.

## 5. Format de chaînon

- **Hypothèse testée.** « L'ancrage CFT-Ward de P1'-A tient-il **telle qu'écrite**
  (étalon OP numérique), et l'énoncé `ε·ε*` est-il explicite et absorbé ? » —
  Réponse scellée : **oui aux deux**, slack nul, zéro amendement.
- **Outil.** OP (6.42)+(5.5)/(5.6)/(5.12)/(5.13) telle qu'imprimées ; MP p.6/p.7 ;
  dictionnaire `κ` scellé ; spineurs-hélicité symboliques (B') ; bi-phase R-10 ;
  sceau sympy 34 asserts.
- **Critère de réfutation.** *PL-A* : refermeture exigeant un nombre hors
  `{N, imprimés OP, {2,4,8}}` ⟹ échec consigné — **non observé** (les deux étalons
  referment en `d` général). *PL-B* : énoncé explicite absent ⟹ R-4 restait
  « cohérent » — **non observé** (énoncé exhibé p.6). *PL-D* : dimension interne
  ≠ comptage fetché ⟹ conflit consigné — **non observé** (2 = 2, graduation 2/6
  alignée).
- **Verdict.** **Convergence** (PL-A, PL-B, PL-D : routes/sources indépendantes
  refermant sur des scellés) **+ consolidation** (PL-C), `[établi — algèbre]`,
  conditionnel aux scellés amont (`A_T·N=16`, `n=2`, relation BD, convention nue,
  `κ=24/π²`) et à la gravité d'Einstein. Résidus délimités : `(a,b,c)` propres /
  CFT de raccordement `[décision ouverte]` ; coefficient `W³` `[décision ouverte]` ;
  quatre-point/boucles/non-perturbatif **hors périmètre** (S1).

## 6. Ce que cela change — et ne change pas — pour le programme

**Change.** (1) La **dernière réserve de l'audit du léger est soldée** : P1'-A
testée telle qu'écrite — le bilan R-8 (« dS-native seulement ») est levé. (2) R-4
soldée par exhibition. (3) Le comptage `2+1` du bispectre tient désormais par
**deux routes** (fetch MP∩OP au léger ; représentation interne ici). (4) Le front
« rang-3 par invariance » est absorbé (plus d'item séparé au menu). (5) Le `4` de
MP est identifié **à la source** comme la convention des scellés du programme.

**Ne change pas.** Aucune réduction du compte : **{A4 ; A2★ ; N} inchangé**.
D1 non clos (l'amplitude `A_T~1/N` reste LA décision ouverte du secteur) ; `N`
non fixé ; la circularité LC-E intacte ; la CFT de raccordement et le coefficient
`W³` restent ouverts ; CCC non démontrée. Ce chaînon est une **cohérence de
coefficients** sous contrat, pas une fermeture.

## 7. Propagation prévue `[lot post-audit]`

1. `00_index` — ligne carte + changelog ; 2. `03_glossaire` — entrées (étalon Ward
numérique ; forensique `ε·ε*` soldée ; invariance rang 3) ; 3. `LC-AUDIT-VERDICT`
§8bis — bullet (bilan R-7 troisième front) ; 4. `04_references` — renvois
d'équations OP (5.5)/(5.6)/(5.12)/(5.13)/(6.42) et MP p.6/(2.6) (R-4 soldée) ;
5. `02_programme` — renvoi Module [D]. Le lot est **suspendu au verdict de
l'audit à froid** (S-L4, commandé), pattern habituel.
