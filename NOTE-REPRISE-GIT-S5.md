---
id: NOTE-REPRISE-GIT-S5
titre: "Note de reprise autoportante — fin de session S5 (2026-07-22) : lot R-8 clos et déposé (REPRODUIT-SOUS-RÉSERVE E-2), orphelins d'une instance interrompue détectés puis PURGÉS sur instruction opérateur, gel R-10 déposé pour dérivation en session neuve. Prochain geste : DÉRIVATION de R-10 sur le gel déjà figé (PAS de re-gel)."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-22
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S5 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S5 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -8   # attendu : HEAD = « Reprise S5 … », puis c0ea2ba (R-8),
                           #   7c9fb0b (Reprise S4), a931a4c (R-1), 9568756 (R-12),
                           #   782b600 (R-2), c99a523 (R-6), 8824501 (Reprise S3)
    ls instruments/*.py | wc -l                    # attendu : 27
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l      # attendu : 24 (les 21 de S4 + R8-CIBLES-GELEES,
                           #   R8-REDEMONSTRATION, R10-CIBLES-GELEES)
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

Tout écart est à décomposer AVANT de poursuivre (leçon V62).
Leçons d'environnement opposables : rejeu long = `setsid nohup … &` puis poll
(S2) ; créer un répertoire de logs dans un appel SÉPARÉ du lancement (S4) ;
vérification de push = repli `origin/main` (S4) ; **compter `ls audit/` et non
`ls audit/*.md` — la 24ᵉ entrée est `rejeu_sceaux_resultats.json` (S5)**.
Branche distante `origin/front-pq` : RÉSIDUELLE, contenue dans main — bénigne,
ne pas toucher. `verif_D3_P6_specB_oracle.py` est LENT (~130 s) : le prévoir.

## 1. Ce qui a été fait en S5 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S4 rejoué CONFORME** sur toute la ligne : 113/113 PASS,
   40 consignations, 9/9 rc=0, HEAD et comptes exacts.
2. **INCIDENT D'ISOLATION, décomposé puis clos.** Deux fichiers non suivis
   (`audit/R7-CIBLES-GELEES.md`, `instruments/redemo_R7_A4_QW.py`) et deux
   logs (`R7.log`, `R7DONE`) sont apparus dans l'arbre de travail APRÈS le
   clone, entre deux appels d'outil. Provenance nommée par l'opérateur :
   artefacts d'une instance S5 antérieure, **interrompue deux fois** parce
   qu'elle rebouclait sur le même rejeu R-7 en signalant une erreur sans la
   régler. **Aucune corruption du dépôt** : HEAD était intact, rien n'avait
   été poussé. Conduite tenue : les fichiers n'ont **JAMAIS été lus**
   (métadonnées seules), mis en quarantaine hors arbre, puis **PURGÉS sur
   instruction opérateur**. Conséquence : **R-10 et R-7 restent
   intégralement dérivables en aveugle.**
3. **LOT R-8 CLOS** (commit `c0ea2ba`) : gel S5 `6523e4b5`, figé avant la
   première ligne d'instrument. Point fixe EXACT de l'opérateur de transfert
   de Gauss par télescopage ⟹ `p(x)=1/(ln2(1+x))` ; transport d'ère
   `p(u)=1/(ln2·u(u+1))`, queue `u⁻²` exacte ; **seuil `s*=1` DÉRIVÉ DE LA
   MESURE** (convergence ⟺ `s−2 < −1`), divergence en `s=1` par forme fermée
   `(ln(B+1)−ln2)/ln2` ; marge stricte `s_phys = 0 < s*` (OC adressé) ;
   Kasner `Σp = Σp² = 1` identiquement, `|p_i| ≤ 1 ∀u ≥ 1` ; dichotomie
   non-cascade ⟺ `ρ = 0`, taux `ln(1+ρ)` exact et strictement monotone ;
   finitude de `⟨C_F⟩` robuste jusqu'à `s < 1`. **Deux cibles NON ATTEINTES,
   nommées** : `⟨C_F⟩ = 7.18` (noyau `C_F(u)` absent des front-matters,
   jamais visée ni approchée) et le noyau `ε` de P6 (`κ = 0.8117`, 0,8 %) —
   couvertes par rejeu seul. 21/21 PASS + 10 consignations, rc0 ; rejeu 3/3
   rc0 sha8 concordants (`76e9257c` LIVE 22 asserts firewall m1/m2/m3+c1/c2 ;
   `162696c1` LIVE ; `ee03c385` ARCHIVE). Grade **E-2**.
4. **GEL R-10 DÉPOSÉ, non dérivé** : `audit/R10-CIBLES-GELEES.md`,
   sha256 `8fb1b0bd21c2a6035158ee48743f56c060b246da6f76de2e22e68c732b2a4ca8`,
   figé le 2026-07-22 à 16:34:02 UTC depuis les **front-matters seuls** de
   `LC-D-NONLIN-VERROU` et `LC-D-NONLIN-2PT`, corps NON ouverts. Motif du
   report : R-10 est du gabarit lourd (triptyque + sceau à 41 asserts, quatre
   sous-lots) et l'entamer en fin de contexte dégraderait la dérivation —
   c'est exactement le mécanisme qui a produit la boucle du point 2.
5. Le commit qui dépose la présente note (swap −S4 +S5 ; S1–S4 restent dans
   l'historique git).

**Bilan Silo R : 8/12 lots clos — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓ R-6 ✓
R-8 ✓ R-12 ✓, TOUS au grade REPRODUIT-SOUS-RÉSERVE (E-2). Restent :
R-10 (GEL DÉJÀ FIGÉ, à dériver) ; R-7 (à reprendre de zéro depuis
`LC-D-A4-QW` seule) ; R-11 (gabarit lourd) ; R-9 (têtes [B] à localiser au
git — possiblement ABSENTES ⟹ écart à consigner le cas échéant).**

## 2. Discipline en vigueur (inchangée + précédents S5)

Discipline amendée post-CSE (note S3 §2) et précédents S4 (échec consigné tel
quel puis réconciliation §2.0 par instrument indépendant ; écart de libellé à
sha concordant ; corrections d'instrument consignées nominalement) :
**tous maintenus**. Précédents S5 opposables :

- **Un arbre de travail partagé par deux instances invalide l'attestabilité**
  (un sha ne certifie plus l'objet dérivé). Conduite : re-cloner sous chemin
  UNIQUE, poser un canari, vérifier `git status` avant tout gel.
- **Des orphelins d'une session interrompue ne se déposent pas et ne se
  lisent pas** : leur lecture consommerait l'aveuglement sur leur lot. Soit
  purge sur instruction, soit dépôt sous provenance consignée.
- **Un test numérique qui contredit le critère déclaré au gel se remplace par
  le critère du gel, JAMAIS par un desserrage de tolérance** (R-8/C9 :
  ratio 1,000145 au lieu de 1, pur effet de taille finie, consigné et borné
  en `1/ln B` ; tolérance 1e−9 non touchée).
- **Une mutation qui laisse la cible invariante est VACANTE** (R-8/C10 :
  `p1²` invariant sous `p1 → −p1`). Convention unique : l'argument `mutation`
  est la **claim MUTÉE**, qui doit être FAUSSE. Le harnais doit détecter les
  vacances — en S5 il en a détecté 19 sur 21 sans produire un seul faux PASS.
- **Reboucler sur un rejeu en signalant une erreur sans la régler n'est pas
  §2.0.** Une dérivation qui ne reproduit pas se CONSIGNE (§2.1-4) et sort en
  E-2 ou NON-REPRODUIT — c'est un résultat. Forcer le PASS est du fit.

## 3. Décisions opérateur EN ATTENTE

- **G-4** : autorité mount vs git (hypothèse reconduite : mount autoritaire
  R-54, git miroir).
- **Priorisation de substance** : β/P-1 vs report modulaire d=3/P-3.
- **PDF du mount** (5014 Ko) : confrontation à `sources/2503_19957v1.pdf`.
- **G-5b/c** (index `LC-00-INDEX`, arborescence des silos) : cadrages non exécutés.
- **Ordre du Silo R après R-10** : R-7 (reprise à zéro) ou R-11 (gabarit
  lourd) ou R-9 (localisation des têtes [B] d'abord).

## 4. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus).
2. **DÉRIVATION de R-10 sur le gel `8fb1b0bd…4ca8` DÉJÀ FIGÉ.**
   **NE PAS RE-GELER** (précédent R-6 : gel déposé fin S3, dérivé en S4 sans
   re-gel). Ouvrir la session sur contexte plein : le lot est du gabarit
   lourd. Les **corps** de `LC-D-NONLIN-VERROU` et `LC-D-NONLIN-2PT` doivent
   rester FERMÉS jusqu'à la fin de la dérivation ; toute lecture de corps est
   une réconciliation §2.0 à déclarer. Plafond E-2 déjà annoncé au gel.
   Sceaux à rejouer : `verif_nonlin_cotton`, `verif_nonlin_repr`,
   `verif_nonlin_parity` (LIVE), `verif_nonlin_deuxpoint` (ARCHIVE).
3. **R-7** : reprise de ZÉRO depuis la tête `LC-D-A4-QW` seule. Les artefacts
   de l'instance interrompue ont été purgés ; l'aveuglement est intact.
4. **R-9** : localiser les têtes [B] au git AVANT d'ouvrir le lot ; si
   absentes, consigner l'écart et demander l'intrant opérateur (têtes au mount).
5. Silos P/V/X : inchangés (P-3 report d=3 recommandé #1 des decks ;
   tracker R-53 : 0/4).

## 5. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, dépôt LC_Raccord seul, Contents R/W,
  courte durée) au premier message. Le token de S5 a servi au push de cette
  session et **reste lisible dans DEUX conversations** (l'instance
  interrompue et celle-ci) ⟹ **À RÉVOQUER IMMÉDIATEMENT**, de même que ceux
  de S3 et S4 s'ils ne l'ont pas encore été. Sans token : tout reste faisable
  en local, seuls les pushes attendent.
- **Une seule instance à la fois** sur le dépôt : la campagne S5 a montré que
  deux sessions concurrentes écrivent dans le même arbre.
- Aucun autre intrant requis pour R-10 ou R-7 (têtes et sceaux au dépôt) ;
  R-9 pourrait requérir les têtes [B] du mount.

## 6. Périmètre — inchangé

`{ A4 ; A2★ ; N }` INCHANGÉ · A2★ décision ouverte, mieux située (délimitation
à lean positif ; `ρ = 0` input motivé non dérivé du générique 3D ; gap OA hors
de portée) · C7 non levée · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) ·
**CCC non démontrée NI réfutée**.

*§6.4 — sentinelle terminale. Cette note organise ; elle ne scelle, ne réduit,
ne compte, ne démontre rien.*
