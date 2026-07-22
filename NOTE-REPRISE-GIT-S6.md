---
id: NOTE-REPRISE-GIT-S6
titre: "Note de reprise autoportante — fin de session S6 (2026-07-22) : lot R-10 dérivé, clos et déposé (REPRODUIT-SOUS-RÉSERVE E-2) après une panne d'exécuteur survenue entre le GO et le push. Prochain geste : R-7, reprise de ZÉRO depuis LC-D-A4-QW seule."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-22
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S6 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S6 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -8   # attendu : HEAD = « Reprise S6 … », puis f415070 (R-10),
                           #   db10757 (Reprise S5), c0ea2ba (R-8), 7c9fb0b (Reprise S4),
                           #   a931a4c (R-1), 9568756 (R-12), 782b600 (R-2)
    ls instruments/*.py | wc -l                    # attendu : 28
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 25
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py          # attendu : 35/35 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R5_reductions_b.py  # attendu : 17/17 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R3_spectre.py       # attendu : 16/16 PASS + 6 consignations, EXIT 0
    python3 instruments/redemo_R6_nongauss.py      # attendu : 16/16 PASS + 6 consignations, EXIT 0
    python3 instruments/redemo_R2_D1.py            # attendu : 12/12 PASS + 8 consignations, EXIT 0
    python3 instruments/redemo_R12_O2.py           # attendu : 11/11 PASS + 7 consignations, EXIT 0
    python3 instruments/redemo_R1_moduleA.py       # attendu : 6/6 PASS + 3 consignations, EXIT 0
    python3 instruments/redemo_R8_A2star.py        # attendu : 21/21 PASS + 10 consignations, EXIT 0
    python3 instruments/redemo_R10_nonlin.py       # attendu : 40/40 PASS + 14 consignations, EXIT 0
                                                   #   (NOUVEAU S6 ; ~30 s, sympy + numpy)

**Total attendu : 174/174 PASS + 64 consignations, 9/9 rc = 0.**
Tout écart est à décomposer AVANT de poursuivre (leçon V62).

Leçons d'environnement opposables, toutes MAINTENUES : rejeu long =
`setsid nohup … &` puis poll (S2) ; créer un répertoire de logs dans un appel
SÉPARÉ du lancement (S4) ; vérification de push = repli `origin/main` (S4) ;
compter `ls audit/` et non `ls audit/*.md` — `rejeu_sceaux_resultats.json` en
fait partie (S5). `verif_D3_P6_specB_oracle.py` est LENT (~130 s).
**Nouveau S6** : `verif_nonlin_cotton` ≈ 139 s, `verif_nonlin_parity` ≈ 308 s
(canari) ; ne PAS lancer deux sceaux en concurrence dans le même arbre.
Branche distante `origin/front-pq` : RÉSIDUELLE, contenue dans main — bénigne,
ne pas toucher.

**Écart d'arbre bénin, récurrent et attendu** : `inventaire_sceaux.py` réécrit
sa propre ligne de date à chaque exécution (bilan identique). Restaurer par
`git checkout -- audit/INVENTAIRE-SCEAUX.md` ; ce n'est pas une modification
de substance.

## 1. Ce qui a été fait en S6 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S5 rejoué CONFORME** sur toute la ligne : 134/134 PASS,
   50 consignations, 8/8 rc = 0, HEAD et comptes exacts, gel R-10 vérifié
   `8fb1b0bd…4ca8`.
2. **LOT R-10 DÉRIVÉ ET CLOS** (commit `f415070`) sur le gel **déjà figé en S5,
   NON re-gelé** (précédent R-6 respecté). **Corps de `LC-D-NONLIN-VERROU` et
   `LC-D-NONLIN-2PT` JAMAIS OUVERTS** — l'aveuglement est intact et le reste,
   disponible pour toute contestation ultérieure. 40/40 PASS discriminants +
   14 consignations, rc 0, **aucune mutation vacante**. Rejeu 4/4 rc 0 aux
   comptes EXACTS de Q9 : `verif_nonlin_cotton` ARCHIVE `b218f974` 12/12 ·
   `verif_nonlin_repr` ARCHIVE `98f34c75` 14/14 · `verif_nonlin_parity` LIVE
   `9df8e53e` 5/5 · `verif_nonlin_deuxpoint` ARCHIVE `1e40f5e8` 41 asserts
   (27 phase 1 + 14 phase 2). Grade **E-2**, plafond du gel atteint non
   dépassé ; aucun audit froid déclenché (issue conforme, §2.0-5).
3. **AUTO-AUDIT CONTRE LE PILOTE, avant tout grade.** La première version de
   l'instrument portait **trois asserts tautologiques** — le ½ du Ricci
   linéarisé **posé** puis comparé à lui-même ; le préfacteur Cotton adossé à
   ce ½ posé ; la loi de tenseur vrai testée sous forme `x − x = 0`. C'est
   exactement le défaut E-3 du CSE. Les trois ont été remplacés par une
   dérivation **ab initio** (Christoffel → Ricci → Schouten → Cotton au premier
   ordre en ε) à coefficients **RÉSOLUS** par `solve` ; `c_E` est extrait du
   développement du mode BD et `c_B` du préfacteur Cotton résolu. Le 40/40 est
   celui de la version corrigée ; la version tautologique n'a jamais servi de
   base à un grade.
4. **INCIDENT D'EXÉCUTEUR, décomposé puis clos.** L'exécuteur Anthropic est
   tombé **immédiatement après le GO opérateur, avant même le `git add`**
   (incident de service confirmé : status.claude.com, 2026-07-22 17:27 UTC).
   Deux commandes de dépôt en échec, puis deux tests minimaux (`echo ok`)
   également en échec ⟹ panne d'outil, pas d'erreur de commande. **Arrêt
   délibéré sans reboucler** (précédent S5). Les deux pièces ont été restituées
   **en texte** à l'opérateur, explicitement qualifiées de RECONSTRUCTION non
   attestée. Au retour de l'exécuteur, **le conteneur avait survécu** : les
   sha256 recalculés sont **identiques** à ceux annoncés avant la panne
   (`e7c569bc…6da9` et `1a34cdcf…472f`) ⟹ les pièces déposées sont les pièces
   **attestées**, la reconstruction n'a pas servi. Aucune corruption, HEAD
   intact tout du long.
5. Le commit qui dépose la présente note (swap −S5 +S6 ; S1–S5 restent dans
   l'historique git).

**Bilan Silo R : 9/12 lots clos — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓ R-6 ✓ R-8 ✓
R-10 ✓ R-12 ✓, TOUS au grade REPRODUIT-SOUS-RÉSERVE (E-2). Restent : R-7 (à
reprendre de ZÉRO depuis `LC-D-A4-QW` seule, aveuglement intact) ; R-11
(gabarit lourd) ; R-9 (têtes [B] à localiser au git — possiblement ABSENTES
⟹ écart à consigner le cas échéant).**

## 2. Contenu de substance de R-10 — pour mémoire

- **Q1** Cotton de S³/ℝ³/ℍ³ ≡ 0 composante par composante ; argument général
  Ric = (R/3)g ⟹ Schouten = (R/12)g, R constant ⟹ ∇S = 0, **sans argument de
  représentation**. **Témoin mordant** : `diag(1, e^{2x}, e^{4x})`, homogène,
  R = −14 **CONSTANT**, mais Cotton **NON NUL** ⟹ le verrou magnétique tient à
  la **platitude conforme (donc A3)**, pas à la constance de R.
- **Q2** `Π^TT(δ) = Π^TT(P) = Π^TT(n⊗n) = 0` ; SVT (2,2,2) de somme =
  identité ; hélicités ±2 par `R_z(ψ)e^±R_z^T = e^{∓2iψ}e^±`.
- **Q3** parité testée en **recalculant deux configurations séparées**
  (polarisation TT générique (a,b), k et H transformés par une réflexion
  det = −1) : Cotton suit la loi pseudo et **échoue** la loi vraie ; Ricci
  l'inverse. Weyl 4D de dimension **10** (20 sans la condition de trace) ;
  E et B symétriques sans trace ; carte Weyl ⟶ (E,B) de **rang 10** ⟹ (5,5)
  complète, disjointe, sans croisé.
- **Q4/Q5** dim(pair) = dim(impair) = 1 ; radiativité par le coefficient de
  Fourier ∝ Γ((d+2α)/2)/Γ(−α) : α = 3/2, d = 3 ⟹ **12π ≠ 0** (radiatif) ;
  α entier ⟹ pôle de Γ(−α) ⟹ **0** (contact). Le secteur impair porte un n̂
  de plus ⟹ α net = 1 ⟹ contact. **La scission radiatif/contact coïncide
  exactement avec la frontière de parité.**
- **Q6** coefficient du Ricci **résolu** à −½, préfacteur du Cotton **résolu**
  à ½, `C^lin = (i/2)k³(Dh)` sur les 9 composantes. `D² = −𝟙` et **D
  antisymétrique ⟹ D^T D = 𝟙** : c'est l'**isométrie** qui fait
  l'équipartition. BD : ⟨EE⟩ = (2H²/9M_Pl²)k³ — **recoupe exactement
  R-5/P4** — ⟨BB⟩ = (H²/2M_Pl²)k³, ⟨EB⟩ radiatif nul.
- **Q7** imports (Osborn–Petkou, de Haro) consignés, non comptés comme
  redérivation. **Q8** firewall 5/5 mordants.

**Trois consignations de fond, à ne pas perdre :**

- **(a)** Ratio **nu** `⟨BB⟩/⟨EE⟩ = (1/2)²/(1/3)² = 9/4` avec les préfacteurs
  du programme. L'équipartition **= 1 est un énoncé en unités de dualité**
  (𝓑 = D𝓔, D isométrique). Écart de convention **NOMMÉ, non corrigé**, aucune
  tolérance desserrée (précédent R-2/Q6).
- **(b)** Le critère d'analyticité **seul** ne sépare pas Δ = 2 (α = 1/2,
  demi-entier, donc radiatif lui aussi : coefficient −π ≠ 0). Ce qui
  singularise Δ = 3 à d = 3 n'est **pas** la radiativité mais la
  **marginalité Δ = d**. Limite nommée, non contournée.
- **(c)** Le gel annonce `cotton`/`repr`/`parity` comme LIVE ; l'inventaire
  place cotton et repr en **ARCHIVE** (seul parity est LIVE). sha8 concordants
  ⟹ écart de **libellé**, pas de substance (précédent S4).

## 3. Discipline en vigueur (inchangée + précédents S6)

Discipline amendée post-CSE (note S3 §2), précédents S4 et précédents S5
(arbre partagé ⟹ attestabilité nulle ; orphelins d'une session interrompue ne
se lisent ni ne se déposent ; le critère du gel jamais remplacé par un
desserrage de tolérance ; mutation invariante = VACANTE ; reboucler n'est pas
§2.0) : **tous maintenus**. Précédents S6 opposables :

- **Un redemo qui POSE son coefficient puis le compare à lui-même n'est pas un
  PASS, c'est un défaut E-3.** Tout coefficient cible doit sortir d'un `solve`,
  d'une série ou d'un calcul tensoriel — **jamais d'une affectation
  littérale**. Corollaire : une loi de transformation se teste en
  **recalculant les deux configurations**, jamais en transportant la première
  à la main. **L'auto-audit de l'instrument précède le grade, il ne le suit
  pas.**
- **Ne jamais affirmer à l'opérateur ce qu'il « a déjà »** : les contenus
  produits dans un appel d'outil lui sont INVISIBLES. En S6 le pilote a
  affirmé qu'un rapport était « dans le message précédent » alors qu'il ne
  vivait que dans un `create_file`. Vérifier le canal, pas sa propre mémoire.
- **Une panne d'exécuteur se constate en deux tests et s'annonce ; elle ne se
  reboucle pas.** Et l'état réel se dit sans adoucissement : « rien n'est
  déposé, HEAD est inchangé ».
- **Le token est le DERNIER intrant, jamais le premier.** En S6, deux tokens
  ont été exposés en conversation avant que l'exécuteur soit confirmé vivant ;
  le premier n'a jamais servi. Ordre correct : tester l'exécuteur → vérifier
  la survie du conteneur → annoncer les sha → demander le token → pousser.
- **Un sha annoncé avant une interruption se RE-CONFRONTE au retour**, jamais
  ne se réaffirme de mémoire. En S6 la confrontation a été concluante ; si
  elle ne l'avait pas été, la pièce aurait été requalifiée en reconstruction
  et ré-exécutée avant dépôt.
- **La durée d'exécution n'est pas une clé de sceau** (les durées consignées
  attestent UNE exécution sur CE clone à CETTE date).

## 4. Décisions opérateur EN ATTENTE

- **G-4** : autorité mount vs git (hypothèse reconduite : mount autoritaire
  R-54, git miroir vérifiable).
- **Priorisation de substance** : β / P-1 (cartographie v1.2 : β#1 maintenu)
  vs report modulaire d = 3 / P-3 (recommandation #1 des decks).
- **PDF du mount** (5014 Ko) : confrontation à `sources/2503_19957v1.pdf`.
- **G-5b/c** : index `LC-00-INDEX`, arborescence des silos — cadrages non
  exécutés.
- **Ordre du Silo R après R-7** : R-11 (gabarit lourd) ou R-9 (localisation
  des têtes [B] d'abord).

## 5. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus, 9 redemo).
2. **R-7 — reprise de ZÉRO** depuis la tête `LC-D-A4-QW` **seule** : gel de
   cible AVANT la première ligne d'instrument, corps NON ouvert, plafond de
   grade à annoncer au gel. Cible stipulée : W2 « résidu-cassant » (le no-hair
   ne nettoie pas le Weyl rescalé) — 14/14 + successeur type-I 8/8. Sceaux :
   `verif_A4_QW` (LIVE, sha8 `a4637a2c`), `verif_A4_QW_typeI_succ` (LIVE,
   sha8 `79f09a8c`). Les artefacts de l'instance interrompue de S5 ont été
   purgés et S6 n'y a pas touché : **l'aveuglement est intact**.
3. **R-11** (gabarit lourd) ou **R-9** (localiser les têtes [B] au git AVANT
   d'ouvrir le lot ; si absentes, consigner l'écart et demander l'intrant
   opérateur — têtes au mount).
4. Silos P/V/X : inchangés (P-3 report d = 3 recommandé #1 des decks ;
   tracker R-53 : 0/4).

## 6. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, dépôt `LC_Raccord` seul, Contents R/W,
  courte durée) — **à fournir seulement une fois l'exécuteur confirmé vivant
  et les sha annoncés**, pas au premier message. Les **deux** tokens de S6
  sont **à RÉVOQUER** : le premier n'a jamais servi (panne), le second a servi
  au push de cette session ; tous deux restent lisibles en conversation. De
  même pour ceux de S3, S4 et S5 s'ils ne l'ont pas encore été.
- **Une seule instance à la fois** sur le dépôt.
- Aucun autre intrant requis pour R-7 (tête et sceaux au dépôt) ; R-9
  pourrait requérir les têtes [B] du mount.

## 7. Périmètre — INCHANGÉ

`{ A4 ; A2★ ; N }` INCHANGÉ · verrou un-point de R-10 **conditionnel à A3** et
**spécifique à d = 3** ; le « tous ordres » du secteur électrique porté par les
**identités de Ward exactes**, qui sont un IMPORT ; `⟨g₃g₃⟩ ∝ k³` reste la
donnée de Cauchy irréductible, pendue à la seule amplitude `A_T ~ 1/N` ·
A3/A4 NON fusionnés · A4 route par-ℐ⁺ délimitée (W2), postulat renforcé, non
réfuté · A2★ décision ouverte, mieux située ; C7 non levée · D1 non clos ·
N non fixé (≡Λ, R-53 : 0/4) · O₂ non construit (β ≡ G3 seul facteur ouvert) ·
nœud (i) INDÉTERMINÉ (pas A) · **CCC non démontrée NI réfutée**.

*§6.4 — sentinelle terminale. Dériver, rejouer, consigner, perdre son
exécuteur puis le retrouver : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit.*
