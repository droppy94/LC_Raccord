---
id: LC-D-O2-P1B-SOPERATION
titre: "Gate P1, route b′ ré-armée via la S-opération SL(2,Z) (Witten S1 / Leigh-Petkou S2) — verdict global : PARTIEL-délimitation. La structure S est confirmée pour le doublet spin-2 (C_T, W_T) AU NIVEAU DEUX-POINTS/LINÉARISÉ (AdS-side), mais le −𝟙 central de SL(2,Z) est porté par la couche de QUANTIFICATION (BF, symplectique) chez Witten pour U(1) SEUL et n'est imprimé nulle part pour le graviton ; il est de surcroît STRUCTURELLEMENT invisible au niveau deux-points (action effective = PSL(2,Z), sceau V1/V3). SP-3 (parité de w) non fixée. P1 reste non franchie ; discordance s=+1 de O2-P1 non levée."
codename: LC-RACCORD
tags: [D, O2, P1, route-b-prime, S-operation, SL2Z, Witten, Leigh-Petkou, moins-un, quantification, PSL, doublet-de-bord, delimitation, AdS-side]
statut: "établi (algèbre) pour V1-V3 (sceau verif_O2_P1b_soperation.py, 3/3 PASS) ; consignations de lecture R-7 datées 2026-07-03 pour S1/S2 ; verdict global PARTIEL-délimitation dans l'espace FIGÉ du gel 52b84cfd. AUCUNE conclusion physique ; aucun surclassement."
type: "chaînon de verdict (Phase 2 du cadrage LC-WORK-CADRAGE-O2-P1B-SOPERATION, gel 52b84cfd — CONSOMMÉ par le présent chaînon)"
version: 1.0
langue: fr
date: 2026-07-03
prerequis_kb: [LC-WORK-CADRAGE-O2-P1B-SOPERATION, LC-D-O2-P1, LC-D-O2-HODGE, LC-D-CT-DUAL, LC-D-CT-DUAL-DS, LC-D-CT-REALITE, LC-D-O2-JONCTION, LC-D-O2-SCATTERING-FG]
scripts: [verif_O2_P1b_soperation.py]
maj: "2026-07-03 — v1.0 : verdicts SP-1..SP-3 sur pièces S1 (checkpoint mi-fetch, fetch daté 2026-07-03) et S2 (dépôt opérateur, texte intégral consommé 2026-07-03)."
---

# P1-b′ — la S-opération fournit-elle le −𝟙 ? Verdict `[PARTIEL-délimitation]`

## 0. Pièces et grades `[R-41 / R-7]`

- **S1** Witten, `hep-th/0307041` v3 : identité-vérifiée multi-miroirs
  (précédent PRISMA/SCATTERING-FG), texte intégral consommé, extraction
  consignée au checkpoint `LC-WORK-CHECKPOINT-P1B-PHASE1-MIFETCH` §2
  (fetch daté 2026-07-03) — fait foi, non re-consommé.
- **S2** Leigh & Petkou, « SL(2,Z) Action on Three-Dimensional CFTs and
  Holography », `hep-th/0309177` v2 (20 Nov 2003), JHEP 0312:020,
  CERN-TH/2003-215. **Dépôt opérateur** : sha256 PDF =
  `21c645eb40a73924d6e3b1ee2ff4782b1aef603b1eb5d476588f32264a810a04`
  (19 pages, couche texte native) — grade **sha256-consigné**, supérieur
  au grade identité-vérifiée. Incident R-41 consigné : un premier dépôt
  était `hep-ph/0309177` (Munier-Peschanski, QCD) — même numéro, mauvaise
  archive ; REJETÉ au crible d'identité AVANT toute lecture de fond,
  zéro contamination.
- **Nuance R-41 (héritée du checkpoint)** : le descripteur du cadrage
  disait « dualité gravitationnelle AdS₄/CFT₃ » ; titre réel =
  SL(2,Z)/holographie. Paraphrase, pas mauvaise identité : l'abstract et
  le §2.2 couvrent bien le tenseur T.
- **S3** de Haro 0808.2054 : substance déjà portée par les 4 chaînons
  scellés (Phase 0 PASS au checkpoint) ; non re-mobilisée au-delà.
- **S4** Penrose (réciprocité conforme) : non mobilisée ici — SP-3 reste
  ouverte, voir §3.

## 1. SP-1 — Existence et périmètre du S²=−𝟙 `[verdict : hérité-U(1)-seul]`

**Chez Witten (S1), telle qu'imprimée** : S²=−𝟙 est DÉMONTRÉ pour les CFT₃
à courant U(1), au niveau de la THÉORIE (retour à la théorie initiale avec
`J→−J`), par la QUANTIFICATION de la théorie BF intermédiaire (fonction
delta, structure symplectique, un seul état). Périmètre STRICTEMENT
abélien ; graviton absent du papier (checkpoint §2, S1).

**Chez Leigh-Petkou (S2), telle qu'imprimée** : la S-opération est
explicitement CONSTRUITE pour le doublet spin-2. Deux-points général
(éq. 2.10) : `⟨T_{µν}T_{λρ}⟩ = C_T·Π⁽²⁾/p + W_T·Π^{(1.5)}` — exactement
le dictionnaire `{g₀, g₃}` ↔ (partie propagante, terme de contact
conforme) attendu côté bord. Construction §2.2 : couplage à `h_{µν}`
externe, gauge-fixing (ξ₁, ξ₂), inversion, courant dual
`T̂ = Π^{(1.5)}h` (éq. 2.17) ; résultat gauge-indépendant (éq. 2.18) :

    S : (C_T, W_T) ↦ ( C_T, −W_T ) / (C_T² + W_T²)

même carte que le cas U(1) (éq. 2.4). MAIS :

1. **Aucune occurrence de S²=−𝟙 dans S2** ; le renvoi au groupe modulaire
   cite Witten [13] pour U(1) uniquement.
2. **Obstruction structurelle (sceau V1/V3)** : au niveau deux-points, la
   carte S est une INVOLUTION EXACTE — `S∘S = Id` sur (C_T, W_T)
   (V1, algèbre exacte). Sur `τ = W_T + iC_T`, S agit comme `τ ↦ −1/τ`
   (V3) ; la matrice S de SL(2,Z) satisfait bien `S² = −Id`, mais son
   action de Möbius est l'identité : **le −𝟙 central vit dans
   `ker(SL(2,Z) → PSL(2,Z))` et est INDÉTECTABLE au niveau deux-points.**
   L'extension de S2 vivant entièrement à ce niveau (« linearized
   level », abstract, §4, §5), elle ne peut NI exhiber NI exclure un
   S²=−𝟙 gravitonique : le niveau où le −𝟙 se voit (théorie/courant,
   `J→−J`) n'est atteint que par la quantification BF de Witten, U(1).
3. La couche de quantification (delta BF, appariement symplectique,
   niveau entier) **n'a aucun analogue gravitonique dans S2**.

**Verdict SP-1 (espace figé)** : `{hérité-U(1)-seul}`. Le −𝟙 est démontré
par quantification pour U(1) (S1) ; pour le doublet graviton, il n'est ni
démontré ni hérité formellement — la seule extension imprimée (S2) vit à
un niveau où il est invisible par construction. Firewall m2 appliqué :
aucune identification silencieuse U(1)→graviton.

## 2. SP-2 — Générateur et niveau `[verdict : quantification U(1) ; graviton non porté]`

- **Générateur du −𝟙 (S1, U(1))** : la QUANTIFICATION (BF, symplectique),
  PAS la géométrie conforme — confirmé telle qu'imprimée (checkpoint §2).
- **Générateur de la S-opération chez S2** : déformation double-trace
  `−(g/2)∫T_{µν}T^{µν}` **IRRELEVANTE** (éq. 3.23, §3.3 ; couplage de
  dimension de masse négative, point fixe UV non trivial SUPPOSÉ).
  **Friction m3 consignée et tranchée sur pièces** : l'affirmation du
  document externe de criblage (« générateur CS marginal ») est
  CONTREDITE telle qu'imprimée — l'abstract dit irrelevante, le corps le
  confirme. Rapport à `Δ_𝒞 = d` marginal de DELTA-C : la déformation
  `T²` a dimension 2(d)=6 > 3 en d=3 ; l'objet marginal de DELTA-C et le
  générateur de S2 ne sont PAS le même objet — à ne pas fusionner.
- **CS gravitationnel de bord** : il apparaît bien chez S2 (éq. 4.7,
  bord du Pontryagin ajouté à MacDowell-Mansouri, éq. 4.1/4.6) mais comme
  générateur de **T** (shift `θ_N → θ_N + 2π` ⟹ shift de W_T,
  éq. 4.10-4.11) — pas de S. Pour S côté bulk : « one expects » une
  généralisation de la dualité électrique-magnétique, au linéarisé
  seulement (éq. 4.13-4.15, τ± = 4π/g_N² ± iθ_N/2π) ; au-delà du
  linéarisé explicitement relégué en spéculation (§5). Aucun niveau k
  entier, aucune structure symplectique gravitonique imprimés.
- **Articulation aux −𝟙 existants (consignée SANS adjuger, gel §1
  SP-2)** : trois objets distincts sur pièces — (i) le −𝟙 de Witten
  (quantification BF, AdS-side, U(1), niveau théorie) ; (ii) le −1
  structural de Hodge (`O2-HODGE` : ne transite pas par la jonction) ;
  (iii) le −1 physique `i^{d-1}` dS (`CT-REALITE`/`CT-DUAL-DS`, source
  unique côté dS). Aucun des trois n'est porté au doublet graviton par
  la couche SL(2,Z) telle qu'imprimée. L'hypothèse « même objet sous
  continuation » reste NON testée (hors scope, m1).
- **m4** : la carte S préserve le signe de C_T (V2 : `C_T>0 ⟹ S(C_T)>0`)
  — cohérence avec le garde-fou scellé `C̃_T = +C_T`, zéro friction.

## 3. SP-3 — Le signe s=(−1)^w `[verdict : non fixé ; bifurcation close côté S1/S2]`

S2 ne touche ni la parité du poids conforme w du mode TT sous `Ω↦−1/Ω`,
ni la réciprocité tensorielle de Penrose. La bifurcation gelée (« le −𝟙
par quantification dispense-t-il de w impair ? ») est TRANCHÉE
négativement sur le périmètre disponible : la route quantificationnelle
du −𝟙 n'existe que pour U(1) (SP-1) ⟹ **aucune dispense pour le doublet
graviton**. La trichotomie de `O2-P1` (w impair / w pair / indécidable)
reste ENTIÈRE, fetch-gated côté S4 + lois FG. La discordance s=+1 de
`O2-P1` n'est PAS levée.

## 4. Verdict global `[espace FIGÉ du gel 52b84cfd]`

**PARTIEL-délimitation** : structure S confirmée pour le spin-2 au niveau
deux-points/linéarisé, AdS-side (acquis de délimitation : le dictionnaire
(C_T, W_T) de S2 coïncide formellement avec `{g₀, g₃}` de SCATTERING-FG,
consolidation de cohérence, pas de réduction) ; le −𝟙 n'est PAS porté au
graviton ; w non fixé. NI POSITIF-AdS (pas d'audit froid obligatoire
déclenché), NI NÉGATIF (la discordance n'est pas non plus aggravée : le
niveau deux-points ne peut pas voir le −𝟙, donc son absence à ce niveau
ne réfute rien), NI INDÉTERMINÉ (les pièces suffisent pour trancher
SP-1/SP-2 dans l'espace figé).

**Sceau** : `verif_O2_P1b_soperation.py` — V1 (S∘S=Id sur (C,W)),
V2 (signe de C_T préservé), V3 (équivalence τ↦−1/τ ; Möbius(−Id)=Id) ;
3/3 PASS, SymPy exact. Le sceau atteste l'ALGÈBRE seule.

**Firewall SP-R** : m1 respecté (tout énoncé AdS-side ; transport β hors
scope) ; m2 appliqué (SP-1) ; m3 appliqué et documenté (SP-2, friction
CS-marginal tranchée contre le crible) ; m4 vérifié (V2).

## 5. Conséquences pour la gate P1 `[sans surclassement]`

P1 reste NON franchie. Route b′ : l'espoir d'un −𝟙 fourni par la couche
SL(2,Z) indépendamment de w est ÉTEINT sur le périmètre S1/S2 (U(1)
seul) ; la route se re-réduit à sa cible historique s=(−1)^w (S4 + lois
FG), inchangée. C-O2 reste étayée non prouvée ; P2 (+i) et β (transport)
entiers.

## 6.4. Non-surclassement `[terminal]`

Ce chaînon délimite ; il ne réduit rien. O₂ non construit ; D1 non clos.
`{A4 ; A2★ ; N}` INCHANGÉ ; N non fixé (≡Λ) ; A4 non réduit ; A2★ non
tranché ; CCC non démontrée NI réfutée.

## 7. Renvois

Gel `52b84cfd` (cadrage, CONSOMMÉ) ; checkpoint mi-fetch (S1) ;
`LC-D-O2-P1` (s=+1, trichotomie w) ; `LC-D-O2-HODGE` ; `LC-D-CT-DUAL` /
`CT-DUAL-DS` / `CT-REALITE` ; `LC-D-O2-JONCTION` (C-O2) ;
`LC-D-O2-SCATTERING-FG` ({g₀,g₃}) ; hep-th/0307041 ; hep-th/0309177
(sha256 `21c645eb…`).
