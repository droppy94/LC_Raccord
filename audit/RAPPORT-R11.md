---
id: RAPPORT-R11
titre: "Lot R-11 (Silo R, DERNIER lot) — redémonstration de la branche FALSIFIABILITÉ F1–F6 « épuisée » + mémoire BMS (BORD-EON V-A) + W2/WCH-GWE. Grade REPRODUIT-SOUS-RÉSERVE (E-2), plafond annoncé au gel atteint non dépassé. 36/36 PASS discriminants + 19 consignations, rc 0 — au SECOND passage : correction d'instrument exécutée après dénonciation de QUATRE faux PASS par l'audit de vacuité du harnais. Harnais 7/7 mutations mordantes. Cinq sceaux ARCHIVE rejoués rc=0, sha8 relevés, 4/4 comptes confrontables concordants. Trois écarts NOMMÉS, tous imputables au pilote, aucun au dépôt : défaut d'énoncé du gel (F4-1), quatre asserts structurellement vacants, une cible reclassée par la clause I-c. Silo R clos à 12/12. §6.4 : rien scellé — clore le Silo R ne retire AUCUNE inconnue. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "rapport de lot de redémonstration — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount reste autoritaire (R-54)."
version: 1.0
langue: fr
date: 2026-07-24
session: S9
gel: "GEL-R11.md — sha256 298e2094ffdffc853118564d328b4faead57dcb5eefbf554c5f63e9b3cccd21d"
amendement: "GEL-R11-AMENDEMENT-1.md — sha256 9d30fce67f2e67ef…"
grade: "REPRODUIT-SOUS-RÉSERVE (E-2) — plafond annoncé AU GEL, atteint, NON dépassé"
---

# Rapport du lot R-11

## 1. Cadre et antériorité

Lot ouvert sur GO opérateur après §0-lite S9 conforme (235/235 PASS,
82 consignations, 11/11 rc=0, HEAD `c683691`, comptes 31/76/29/215/4,
inventaire 6/76/1, `verif_paquet_propre` sha8=051e2833).

**Présence re-mesurée sur le clone, jamais reportée** (le lotissement v0.1
porte encore « ✗ » en colonne « présent au git » pour R-11 ; le relevé S7
disait le contraire ; c'est la mesure de S9 qui fait foi ici) :

- 20 têtes F1–F6/WCH présentes en `kb/` (1 branche + 11 chaînons D +
  7 cadrages + 1 amendement) ;
- 5 sceaux cités présents en `instruments/archives-scelees/` :
  `verif_F1_spn.py`, `verif_F4_principiel.py`, `verif_F5_scaling.py`,
  `verif_F6_memoire_cisaillement.py`, `verif_D3_WCH_GWE.py`.

**Aucun intrant.** Lot intégralement autoportant depuis le git, comme annoncé.

**Gel figé AVANT la première ligne d'instrument** : `GEL-R11.md`,
sha8 `298e2094`, 164 lignes / 9062 octets, horodaté 2026-07-24T12:52:15Z.
L'antériorité est auditable et non pas déclarée : au moment du relevé du sha,
le répertoire de travail ne contenait QUE le gel — listing à l'appui.
Le gel a été re-vérifié byte-intact à `298e2094` APRÈS dérivation.

**Corps des 20 têtes JAMAIS ouverts** : seuls les blocs YAML de front-matter
ont été lus, par extraction mécanique (`awk` entre les deux `---`).
**Code des 5 sceaux JAMAIS lu** : rejeu par exécution seule.

## 2. Plafond de grade, annoncé au gel

**E-2 — REPRODUIT-SOUS-RÉSERVE.** Plafond, non objectif. Motifs énoncés au
gel et non après coup : corps fermés ; sceaux non lus ; une part
substantielle du lot est de nature DÉLIMITATION / CARTOGRAPHIE (F2, F3,
F5(a), F6-G3, BORD-EON) donc non algébrisable ; imports non redérivés
(dictionnaire holographique ⟨T⟩=(d/16πG)g₃, Ω^𝒯=Weyl⊕Cotton (BEG),
littérature AHS / Osborn–Petkou / Philcox–Shiraishi / Heinzle–Uggla /
Garfinkle / Meissner–Penrose, W2 hérité de R-7).

Le gel a en outre pré-trié chaque cible en **[D] discriminante** (comptée en
PASS) ou **[C] consignation** (lue, non redémontrable), AVANT de savoir
laquelle passerait — ce qui interdit de reclasser après coup un échec en
consignation.

## 3. Résultats

| Instrument | Résultat |
|---|---|
| `redemo_R11_falsifiabilite.py` | **36/36 PASS + 19 consignations, rc = 0** |
| `harnais_R11.py` | **7/7 mordantes**, 0 vacante, rc = 0 |
| 5 sceaux ARCHIVE | **5/5 rc = 0** |

Recompte indépendant des logs au motif tolérant `^\s*\[?PASS\]?` et son
pendant CONSIGNATION : PASS=36, CONS=19, FAIL=0 — concordant avec le bilan
auto-déclaré par l'instrument.

### Sceaux rejoués — sha8 RELEVÉS, non prédits

| Sceau | sha8 | assertions | confrontation |
|---|---|---|---|
| `verif_F1_spn` | `19a4931e` | 20 | concorde (sha ET compte déclarés au front-matter) |
| `verif_F4_principiel` | `9947b8ed` | 25 | concorde avec la version DURCIE (§7) ; le `0e8ecf85`/26 du titre est le record historique v0.1, explicitement additif-only |
| `verif_F5_scaling` | `a959f137` | 19 | concorde avec le durcissement R-28 (19), non avec les 14 de la v0.2 |
| `verif_F6_memoire_cisaillement` | `23a7d264` | 18 | concorde |
| `verif_D3_WCH_GWE` | `664660ee` | — | rc=0 ; aucun compte déclaré à confronter |

4/4 comptes confrontables concordants. Un seul sceau à la fois dans l'arbre.

## 4. ÉCARTS — trois, tous imputables au PILOTE, aucun au dépôt

### 4.1 Défaut d'énoncé du gel (F4-1)

Le gel `298e2094` écrivait « f strictement monotone **décroissante** ».
L'énoncé est FAUX : l'argmin d'une f décroissante sur [0,∞) part à l'infini,
jamais en w=0. Le sens contraint par l'argument est l'inverse (l'entropie
gravitationnelle croît avec l'invariant de Weyl, sens de Penrose).

Traitement : **AMENDEMENT-1** (`9d30fce6`), fichier SÉPARÉ, daté AVANT la
première ligne d'instrument, gel laissé BYTE-INTACT. Aucune tolérance
desserrée, aucun seuil touché, nombre de cibles inchangé (3 [D], 1 [C]).

**Un gel qui contient une erreur d'énoncé est un gel défectueux, même
rattrapé à temps.** L'écart est porté ici et non dilué.

### 4.2 Quatre faux PASS au premier passage

La v1 de l'instrument sortait **38/38 PASS**. Le harnais, par son **audit de
vacuité structurelle**, a dénoncé quatre asserts qu'aucun porteur mutable ne
traverse — donc incapables d'échouer :

- **F4-2** comparait littéralement deux ensembles codés en dur (`{0}=={0}`) ;
- **F6-2d** vérifiait `det(−I₃) = −1`, fait trivial déconnecté de tout porteur ;
- **F6-5a / F6-5b** testaient la linéarité d'une expression écrite linéaire :
  tautologie.

Traitement : **correction d'instrument exécutée**. F4-2 et F6-5 retirés du
compte et consignés avec motif ; F6-2d **remplacé** par une construction
effective de l'objet à un epsilon `Y_ij = ε_i^kl Cotton_klj` sur fond Nil,
doté d'un porteur `P_F6_PSEUDO` — la mutation m7 le mord désormais.

Conséquence à ne pas maquiller : **ce lot n'est PAS « premier passage sans
correction »**, contrairement à R-9. Le compte final 36/36 est celui du
SECOND passage.

### 4.3 Cible F3-1 reclassée (clause I-c pré-déclarée)

La cible gelée demandait de retrouver que « transitoire » est CONDITIONNEL à
|w|>1 (permanent pour 0<|w|<1 — Lim §5.1, correctif R-20). Ce fait vit au
corps des sources : tout assert écrit ici aurait été une recopie du
front-matter, donc vacant. **Retirée du compte PASS, motif nommé**, via la
clause I-c que le gel avait prévue précisément pour ce cas.

## 5. Substance retrouvée

### 5.1 Axe WCH-GWE — le cœur mordant

Le mode exact `Ω_σ/ε² = (x cos x − sin x)²/(3x²)`, x = kη, redérivé ab initio :

- terme dominant du développement = **exactement x⁴/27** ⟹ la forme scellée
  `Ω_σ = (kη)⁴ε²/27` est RETROUVÉE, pas recopiée ;
- terme suivant = **−1/135**, non nul et négatif ⟹ **le tronqué surestime** ;
- **sup = 0,376730 atteint en x = 2,7437**, donc ≤ 0,377 et < 0,5 ;
  confirmation asymptotique `Ω_σ/ε² → cos²x/3 ≤ 1/3` ⟹ la borne n'est pas un
  artefact de la fenêtre de balayage ⟹ **régime (A) pour tout kη** ;
- le tronqué `x⁴/27` atteint 0,5 en `x = 13,5^(1/4) = 1,9168` ⟹ le
  « basculement (A)/(B) à kη ≈ 1,9 » est l'**artefact EXACT de la troncature**,
  non un fait du mode exact ;
- au pic CGB (x = 2·10⁻⁷) : `5,956·10⁻²⁹`, ordre 6·10⁻²⁹ retrouvé.

### 5.2 Autres axes

- **F1** : rapport Sp(N)/programme = **π²/8 = 1,2337** exact, ≠ 1 et > 1 —
  excès, non déficit ⟹ le coefficient ne branche pas le falsifiable positif.
- **F2** : exposant du plancher Einstein = **−2** exact sous A_T ∝ N⁻¹.
- **F3** : témoin métrique séparant la famille G₂ adaptée du générique, avec
  contrôle de non-vacuité (une métrique G₂ authentique passe).
- **F4** : argmin en w=0 pour six functionals croissants distincts, **et
  cassure sur `(w−1)²`** ⟹ la circularité de la voie entropie-de-Weyl est
  établie ET sa contingence à la monotonie est exhibée.
- **F5** : `A_T·N` indépendant de ℓ **et de d** (d symbolique) ⟹ identité
  ∀ d ; garde-fou anti-surclassement vérifié : le coefficient O(1) reste un
  symbole LIBRE et n'est pas résolu.
- **F6** : Hessien covariant symétrique et sans trace sur fond **Nil** (non
  plat, Christoffels réels), avec `R[Nil] = −1/2` constant et
  `Cotton[Nil] ≠ 0` redérivés — recoupe R-7/Q6 et R-9/A5-A6. Parité paire de
  Δσ vs parité impaire de l'objet à un epsilon ⟹ secteurs disjoints.
- **Transverse** : aucun des six fronts n'est de niveau « réduction » ⟹
  union des inconnues retirées VIDE ⟹ **{A4 ; A2★ ; N} INCHANGÉ**.

## 6. Consignations de fond — à ne pas perdre

1. **Tension interne entre deux têtes du dépôt**, pré-déclarée au gel puis
   CONFIRMÉE : la tête F2 porte `f^ttt_NL = 900 ± 700` comme lecture de
   2312.12498 Table II ; la tête F5 v0.3 (correctif R-23) déclare ce chiffre
   **NON LITTÉRAL dans la source**, caractérisation approximative d'un
   σ = O(500). Les deux énoncés coexistent au dépôt. **Consignée, NON
   ARBITRÉE** : les corps sont fermés, rien au front-matter ne permet de
   trancher. C'est un point de reprise réel pour qui rouvrira F2 ou F5.
2. **F3-2 est borné** : le témoin établit la non-appartenance à la famille G₂
   ADAPTÉE au couple (∂_y, ∂_z). Il n'exclut PAS l'existence d'un autre
   couple de Killing commutants. Suffisant pour « un soutien en G₂ ne borne
   pas le générique », insuffisant comme théorème de classification.
3. **T-2 invérifiable par construction** : « branche entièrement épuisée » est
   un constat de NON-EXISTENCE d'un front borné et sceau-able restant. On ne
   prouve pas une absence par sympy. Déclaré tel AU GEL, jamais compté.
4. **F6-5 / G2** : la substance n'est pas la linéarité de Q[f] mais le
   DICTIONNAIRE `⟨T⟩ = (d/16πG) g₃` — import holographique, non redérivable
   ici.
5. **W2 « résidu-cassant »** : import de R-7, recoupement seul, non redérivé.
6. **W1 (LC-D3-WCH-CANCELLATION)** : axe INTÉGRALEMENT consigné, **zéro PASS
   revendiqué** — le contenu discriminant vit au corps, fermé.
7. **Piège de sonde, variante neuve** : `ps -eo pid,etime,cmd | grep "[p]ython3"`
   a AUTO-MATCHÉ, non par le grep, mais parce que la ligne de commande du
   shell parent contenait elle-même la chaîne. Le motif `[p]` protège du
   self-match de grep, pas de celui du shell englobant. Re-sondé à froid :
   aucun processus vivant. À reporter comme leçon d'environnement.

## 7. État de sortie

`git status` propre avant et après, HEAD inchangé `c683691`, aucun processus
résiduel, aucun sceau en concurrence. **Rien déposé.**

Comptes post-dépôt **MESURÉS sur arbre modifié localement** (copie des pièces,
mesure, restauration intégrale — sans commit ni push), conformément au
précédent S8 : `instruments/*.py` = 33, `archives-scelees` = 76, `audit/` = 32,
`kb/*.md` = 215, `hors-KB/B/` = 4, inventaire **6/76/1 INCHANGÉ** (ni les
redemo ni hors-KB ne sont balayés), `verif_paquet_propre` sha8 = 051e2833
inchangé.

## 8. Bilan de silo

**Silo R : 12/12 lots clos** — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓ R-6 ✓ R-7 ✓
R-8 ✓ R-9 ✓ R-10 ✓ R-11 ✓ R-12 ✓, TOUS au grade REPRODUIT-SOUS-RÉSERVE (E-2).

*§6.4 — sentinelle terminale. Dériver, muter, rejouer, corriger un instrument
et consigner des réserves : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. **Clore le Silo R ne retire AUCUNE
inconnue** — c'est exactement ce que la cible transverse T-1 a vérifié.*

`{ A4 ; A2★ ; N }` INCHANGÉ · D1 non clos · N non fixé (≡Λ) · O₂ non
construit · A2★ décision ouverte, C7 non levée · nœud (i) INDÉTERMINÉ ·
**CCC non démontrée NI réfutée**.
