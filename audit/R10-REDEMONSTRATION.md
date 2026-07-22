# R-10 — REDÉMONSTRATION « parité non-linéaire du Weyl rescalé (E pair / B impair, 5+5=10) » — rapport de lot (2026-07-22, session S6)

Protocole §2.0 du lotissement, exécuté dans l'ordre. **Gel figé en S5, NON re-gelé**
(précédent R-6 : gel déposé fin S3, dérivé en S4 sans re-gel).

## 1. Gel de cible (étape 1) — fait en S5, vérifié à l'ouverture

`audit/R10-CIBLES-GELEES.md` — **sha256
8fb1b0bd21c2a6035158ee48743f56c060b246da6f76de2e22e68c732b2a4ca8**,
vérifié conforme à l'ouverture de S6 (attendu de la note de reprise S5).
9 cibles (Q1–Q9) extraites des **front-matters seuls** de `LC-D-NONLIN-VERROU`
et `LC-D-NONLIN-2PT`, corps NON ouverts.

**Plafond annoncé AU GEL : REPRODUIT-SOUS-RÉSERVE (E-2). E-1 exclu d'avance.**
Le gel déclare lui-même que les front-matters portent les valeurs d'arrivée
ET les mécanismes.

## 2. Redérivation indépendante (étape 2)

`instruments/redemo_R10_nonlin.py` — **40/40 PASS discriminants + 14
consignations déclarées, rc 0**, corps des deux têtes restés FERMÉS pendant
toute la dérivation.

Redérivés de bout en bout :

- **Q1** — Cotton de S³, ℝ³, ℍ³ calculé composante par composante (27 chacune) :
  **≡ 0 exactement**, sans argument de représentation ; argument général
  Ric = (R/3)g ⟹ Schouten = (R/12)g, R constant ⟹ ∇S = 0. Cotton linéarisé
  d'une perturbation TT : non nul, symétrique, sans trace, transverse.
- **Q2** — `Π^TT(δ) = Π^TT(P) = Π^TT(n⊗n) = 0` ; SVT complète en d = 3 avec
  rangs **(TT, V, S) = (2, 2, 2)** et somme = identité (6 = 2+2+2) ; hélicités
  **±2** par `R_z(ψ)·e^±·R_z^T = e^{∓2iψ}e^±` ; ⟨g₃⟩ = 0 pour tout tenseur
  symétrique invariant (span{δ, n⊗n}, 8 tirages).
- **Q3** — lois de transformation **recalculées ab initio sur DEUX
  configurations** (polarisation TT générique (a,b), k et H réellement
  transformés par une réflexion det = −1) : Cotton suit `y_R = det(R)(R⊗R)y(Rx)`
  et **échoue** la loi de tenseur vrai ; Ricci l'inverse — les deux contrôles
  négatifs mordent. Espace de Weyl en 4D de **dimension 10** (20 sans la
  condition de trace) ; `E = C_{0i0j}` et `B = ½ε_{ikl}C^{kl}_{j0}` tous deux
  symétriques sans trace (**5 + 5**) ; carte Weyl ⟶ (E,B) de **rang 10 = dim
  source** ⟹ couverture complète, disjointe, sans croisé.
- **Q4** — dimension du secteur **PAIR = 1** (SVD, seuil 1e−10, 5 directions),
  solution ∝ Π^TT ; `k³ = (k²)^{3/2}` non analytique ⟹ coefficient de Fourier
  **12π ≠ 0** ⟹ RADIATIF.
- **Q5** — dimension du secteur **IMPAIR = 1**, solution ∝ D·Π^TT ;
  orthogonalité `Π^TT·(D·Π^TT) = 0` exacte ; type **CONTACT** par le critère
  analytique (n̂ supplémentaire ⟹ puissance nette entière α = 1 ⟹ pôle de
  Γ(−1) ⟹ coefficient de Fourier nul) ⟹ **aucune amplitude radiative neuve** ;
  la scission radiatif/contact suit exactement la frontière de parité.
- **Q6** — Cotton linéarisé **ab initio**, préfacteurs **RÉSOLUS et non posés** :
  le coefficient du Ricci linéarisé sort à **−½** (avec R^(1) = 0), celui du
  Cotton à **½**, et l'égalité tensorielle `C^lin − (i/2)k³(Dh) = 0` tient sur
  les 9 composantes. `D² = −𝟙` sur TT (5 tirages) ; **D antisymétrique ⟹
  D^T D = 𝟙 : D est une ISOMÉTRIE** du secteur TT — c'est le mécanisme exact
  de l'équipartition. Refermeture BD : `⟨EE⟩ = (2H²/9M_Pl²)k³` — **recoupe
  exactement R-5/P4** — et `⟨BB⟩ = (H²/2M_Pl²)k³`, tous deux ∝ k³ ; `⟨EB⟩`
  radiatif nul.
- **Q8** — firewall **5/5** mordants : η² déterminé vs η³ libre (Δ = d = 3) ;
  d = 4 ⟹ pôle Γ(−2) ⟹ contact ; Cotton ×2 ⟹ ratio 4 ≠ 1 ; trace annihilée
  par Π^TT ; n ≠ 2.

**Q7** est majoritairement de l'import externe (Osborn–Petkou, de Haro) :
consigné, non compté comme redérivation. Seul le comptage interne est dérivé
(catalogue {2,4,8} apparié à (½)^p ⟹ produit net 1 ; Γ(−3/2) finie vs Γ(−2)
pôle).

**Aucune mutation vacante** : le harnais n'en a signalé aucune sur 40.

## 3. Auto-audit d'instrument — trois asserts tautologiques CORRIGÉS

Consigné **contre le pilote**, en application du verdict CSE E-3 (S3) :
la **première version** de l'instrument contenait trois asserts qui
**paraphrasaient leur cible au lieu de la calculer** —

1. le ½ du Ricci linéarisé était **posé** (`coef_ric = 1/2`) puis comparé à
   lui-même ;
2. le préfacteur `(i/2)k³` du Cotton reposait sur ce même ½ posé ;
3. la loi de tenseur vrai du Ricci était testée sous la forme `x − x = 0`.

Les trois ont été **remplacés par une dérivation ab initio** (moteur de
linéarisation : Christoffel → Ricci → Schouten → Cotton au premier ordre en ε
pour g = δ + εh) où les coefficients sont **résolus** par `solve`, et où les
deux configurations de la loi de parité sont **recalculées séparément**.
De même, `c_E = −i/3` n'est plus écrit à la main mais **extrait** du
développement du mode BD, et `c_B` du préfacteur Cotton résolu.
Le compte 40/40 est celui de la version corrigée ; la version tautologique
n'a jamais servi de base à un grade.

## 4. Réconciliation — trois points consignés, aucun écart de cible

- **(a) Écart de convention NOMMÉ, non corrigé (anti-fit).** Avec les
  préfacteurs **nus** du programme (c_E = −i/3 de la relation d'état BD ;
  c_B = i/2 du Cotton), le ratio nu `⟨BB⟩/⟨EE⟩` vaut **(1/2)²/(1/3)² = 9/4**,
  pas 1. L'équipartition **= 1 est un énoncé en unités de dualité**
  (𝓑 = D𝓔, D isométrique) — ce que le gel dit d'ailleurs explicitement.
  Aucune tolérance desserrée, aucun coefficient modifié (précédent R-2/Q6).
- **(b) Limite du firewall 1 NOMMÉE.** Le critère d'analyticité **seul** ne
  sépare pas Δ = 2 (α = 1/2, demi-entier, donc radiatif lui aussi :
  coefficient −π ≠ 0). Ce qui singularise Δ = 3 à d = 3 n'est pas la
  radiativité mais la **marginalité Δ = d**. Limite consignée, non contournée.
- **(c) Écart de LIBELLÉ de zone, sha concordant.** Le gel annonce
  `verif_nonlin_cotton`, `verif_nonlin_repr` et `verif_nonlin_parity` comme
  LIVE ; l'inventaire du dépôt place les deux premiers en **ARCHIVE** (seul
  `parity` est LIVE, conforme aux 6 LIVE du §0-lite). sha8 concordants dans
  les deux cas ⟹ écart de libellé, pas de substance (précédent S4).

Incidents d'instrument bénins, consignés : (i) `simplify` seul insuffisant sur
les identités trigonométriques du Cotton de S³ (composante résiduelle
`sin2r·tan r + cos2r − 1`), `expand_trig` requis — instrument, pas algèbre
(précédent R-4) ; (ii) un rejeu lancé dans un appel composé a perdu son
répertoire courant (rc 2, « can't open `//instruments/run_sceau.py` ») ;
relancé sériellement, rc 0 — **aucun sceau n'a été exécuté en concurrence
d'un autre pour son résultat retenu**.

## 5. Sceaux (étape 3) — rejeu du lot, 4/4 rc 0

| sceau | zone (inventaire) | sha8 | asserts | rc | durée |
|---|---|---|---|---|---|
| `verif_nonlin_cotton.py` | ARCHIVE | `b218f974` | **12/12** | 0 | 139 s |
| `verif_nonlin_repr.py` | ARCHIVE | `98f34c75` | **14/14** | 0 | 1,9 s |
| `verif_nonlin_parity.py` | LIVE | `9df8e53e` | **5/5** | 0 | 308 s |
| `verif_nonlin_deuxpoint.py` | ARCHIVE | `1e40f5e8` | **41** (27 phase 1 + 14 phase 2) | 0 | 16 s |

Les quatre comptes sont **exactement** ceux annoncés en Q9. sha8 concordants
avec le tableau du rapport R-5 (`b218f974` / `98f34c75` / `1e40f5e8`) et avec
la liste des canaris de la note S5 (`9df8e53e`).

## 6. Grade (étape 4)

**REPRODUIT-SOUS-RÉSERVE (E-2)** — plafond annoncé au gel, atteint et non
dépassé. 8 cibles dérivables sur 9 reproduites par redérivation (Q1–Q6, Q8),
Q7 consigné comme import, Q9 rejoué 4/4 rc 0 aux comptes exacts.
La réserve porte, comme au gel, sur le fait que les front-matters révélaient
les mécanismes autant que les valeurs : la dérivation est **guidée**, sa force
probante est celle d'une corroboration, pas d'une découverte indépendante.

L'issue étant conforme au plafond déclaré au gel, **aucun audit froid n'est
déclenché** (§2.0-5 : obligatoire seulement si l'issue diffère).

**Corps des deux têtes : jamais ouverts.** Aucun écart contre le gel n'exigeait
de réconciliation par lecture de corps ; l'aveuglement est donc conservé
intact et reste disponible pour toute contestation ultérieure.

## 7. §6.4 — sans surclassement

« REPRODUIT-SOUS-RÉSERVE » = algèbre correcte + cibles reproduites, sous
hypothèses explicites — JAMAIS « le verrou est démontré ». Le verrou un-point
reste **conditionnel à A3** (sans A3, le témoin homogène diag(1, e^{2x}, e^{4x}),
à R constant, a un Cotton NON NUL) et **spécifique à d = 3** (à d = 4 le pôle
Γ(−2) rend la structure de contact). Le « tous ordres » du secteur électrique
est porté par les **identités de Ward exactes**, qui sont un IMPORT.
`⟨g₃g₃⟩ ∝ k³` reste la donnée de Cauchy irréductible, pendue à la seule
amplitude `A_T ~ 1/N`. A3/A4 NON fusionnés · D1 NON clos · N non fixé
(≡Λ, R-53 : 0/4) · nœud (i) INDÉTERMINÉ (pas A) ·
{ A4 ; A2★ ; N } INCHANGÉ · **CCC non démontrée NI réfutée.**
