---
id: R23-AU-FOND-VERDICT-AMENDEMENT-1
titre: "Amendement 1 au verdict R-23 AU FOND — confrontation de 13 pièces d'archive opérateur, HORS DÉPÔT. Le verdict n'est PAS retourné : C-1/C-2/C-3 tiennent et sont CONFIRMÉS PAR UNE SURFACE INDÉPENDANTE. Une sous-affirmation du §2 est CORRIGÉE. Généalogie complète du mot `soldée` établie par comptage."
codename: LC-RACCORD
type: "amendement daté à un verdict rendu. Le verdict reste BYTE-INTACT. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
verdict_amende: "audit/R23-AU-FOND-VERDICT.md — sha256 07225d4d4bd059f9742a53d767eaba4ec0aa33b99c62ee4581bb95fb7e735c59 — NON MODIFIÉ."
---

# Amendement 1 — ce que l'archive opérateur fait au verdict

## §0. Régime, et pourquoi le verdict n'est pas réécrit

Le verdict a été **rendu sur le dépôt seul**, avant que ces pièces n'existent dans le contexte du
pilote. Le réécrire en place effacerait le fait le plus utile de la séance : **le dépôt était
suffisant.** Le verdict reste donc **byte-intact** et cet amendement porte ce que l'archive ajoute,
retire ou corrige. Les treize pièces proviennent de `/mnt/user-data/uploads`, **surface sans version,
sans sha et sans historique** — elles ne font pas foi contre le git (`R-54` est borné aux INTRANTS,
et ce ne sont pas des intrants).

## §1. TROIS PIÈCES CONFRONTÉES AU BIT — et c'est une première

| pièce | archive opérateur | dépôt | verdict |
|---|---|---|---|
| `LC-D-F5-ETAT-RACCORD` | 30 423 o · `9b3d23a6` | `kb/` idem | **IDENTIQUE AU BIT** |
| `LC-WORK-CADRAGE-F5-ETAT-RACCORD` | 18 631 o · `930691d7` | `kb/` idem | **IDENTIQUE AU BIT** |
| `verif_F5_scaling.py` | 6 954 o · `a959f137` | `instruments/archives-scelees/` idem | **IDENTIQUE AU BIT** |

**3/3.** C'est la **première confrontation d'octets de pièces `kb/` contre une surface indépendante
du dépôt**. Le corps sur lequel le verdict a été rendu est **le bon corps**. Le sceau déposé est le
**durci `d` symbolique**, rejoué ici : **rc = 0, 19 assertions**, coefficient O(1) effectivement
libre.

**ÉCART PILOTE S20 nº4** : le verdict et l'annonce précédente ont cherché `verif_F5_scaling.py` dans
`instruments/` et l'ont déclaré absent. Il est dans `instruments/archives-scelees/`. **Correspondance
fausse du pilote, pas une absence du dépôt.**

## §2. GÉNÉALOGIE DU MOT `soldée` — comptée, et elle tranche

Occurrences de `sold*` dans l'échafaudage F5 complet :

| pièce | occurrences |
|---|---|
| `LC-D-F5-ETAT-RACCORD` (le chaînon) | **0** |
| `LC-WORK-CADRAGE-F5-ETAT-RACCORD` | **0** |
| `LC-WORK-AUDIT-FROID-F5` (instruction d'audit) | **0** |
| `LC-WORK-AUDIT-FROID-F5-PASSE4-ROUTES` | **0** |
| `LC-AUDIT-LOG-F5` (le verdict d'audit froid) | **1** |
| `LC-WORK-PROPAGATION-LOG-F5` | **24** |

**L'unique occurrence du log d'audit n'est pas dans son verdict : elle est dans sa consigne de
propagation.** Et les deux paragraphes se suivent, à trois lignes d'intervalle, dans le même §4 :

> *« **Intrants amont hors périmètre** pris comme acquis (**non re-jugés**) : … **héritage R-23
> (AUDIT-LOG-F2)**. »*
>
> *« **Suite : propagation F5 sur GO.** Lot additif transverse (… branche FALSIFIABILITÉ
> [F5 TRAITÉ + **dette R-23 soldée**], …) »*

**Le même document déclare, en deux paragraphes consécutifs, que `R-23` n'a PAS été re-jugée et
qu'il faut propager « dette R-23 soldée ».** C'est l'instant exact où un héritage non re-jugé devient
une dette soldée — **par consigne de propagation, jamais par verdict.** Puis 24 occurrences dans le
log de propagation, puis les cinq registres.

**Précédent proposé** : *un mot qui n'apparaît dans aucune pièce de science et dans toutes les pièces
de propagation n'est pas un résultat — c'est un effet de transport.*

## §3. `C-1`, `C-2`, `C-3` — aucune n'est retournée

- **`C-1` = (a) CONTINGENTE : CONFIRMÉE, et par un canal neuf.** Le log d'audit écrit que la
  classification `L1 inconfrontable` est *« justifiée ni "trop prudent" ni L3 »*. **`L3` non
  déclenché est précisément l'exclusion du cas structurel** : l'audit froid a explicitement séparé
  L1 (pas de valeur programme) de L3 (contradiction de forme). L'issue (b) est écartée **une seconde
  fois, par une pièce indépendante du corps**.
- **`C-2` = (b) ENREGISTRÉ : CONFIRMÉE PAR F5 LUI-MÊME.** L'audit froid de F5 range `héritage R-23
  (AUDIT-LOG-F2)` parmi les **intrants pris comme acquis, NON RE-JUGÉS**. Ce n'est plus une
  inférence du pilote : **c'est écrit par l'instance qui a audité F5.** Reste une CONFIRMATION
  D'ANTICIPATION — l'enveloppe l'avait pré-emptée, et le prix reste sa date.
- **`C-3` = (a) LEVIER ÉCRIT : inchangée.** Rien dans l'archive ne modifie le levier nommé.

## §4. CORRECTION D'UNE SOUS-AFFIRMATION DU VERDICT §2

Le verdict écrit que F5 **dérive l'extraction**, en citant *« le coefficient `0,5291` de la note 6 »*
parmi les gestes propres de F5. **C'est faux pour ce coefficient.** Le registre `R-27` du log
d'audit établit que « 0,53 » est une **valeur héritée de F2/R-23, présente en KB AVANT F5, non
re-fetchée pour F5**.

**Énoncé corrigé** : F5 dérive l'extraction **de la Table III** (les trois lignes `n_NL`, la note
d'honnêteté sur `O(500)` contre « 900 ± 700 ») ; **le coefficient `0,5291` est hérité de F2**, comme
la classification. La part propre de F5 est donc **plus étroite** que le verdict ne l'écrit — ce qui
**renforce** `C-2` sans en changer l'issue.

## §5. DEUX RÉSERVES NEUVES, écrites par l'audit de F5 et absentes du dépôt

1. **Anti-fit de F5 : non certifiable, et son propre audit le dit.** *« Chronologie réelle d'écriture
   non vérifiable (cadrage + 3 versions datés du même jour) ; la présence de "0,53" dans le cadrage
   "pré-fetch" est expliquée (F2-héritée) mais non certifiable ⟹ R-27. »* Seule l'indépendance
   **logique** forme ⊥ lecture est attestée.
2. **`R-7` vérifiée par le journal `maj`, PAS par diff** — les versions v0.1/v0.2 étaient absentes du
   paquet d'audit.

**Ces deux réserves ne sont dans AUCUNE pièce déposée.** Elles s'ajoutent aux réserves qui se
recopient : **une ligne F5 citée sans elles est incomplète.**

## §6. SIX PIÈCES ABSENTES DU DÉPÔT — dette de fourniture, PAS un défaut de R-23

Absentes du git, présentes chez l'opérateur : `LC-AUDIT-LOG-F5` · `LC-WORK-AUDIT-FROID-F5` ·
`LC-WORK-AUDIT-FROID-F5-PASSE4-ROUTES` · `LC-WORK-PROPAGATION-LOG-F5` ·
`LC-WORK-REPRISE-POST-PROPAGATION-F5` · `LC-WORK-REPRISE-POST-PROPAGATION-F5-APPLIQUEE`.

Le verdict §2 écrivait *« 0 pièce `LC-AUDIT-LOG-*` dans `kb/` »* : **cet énoncé reste vrai du
dépôt**, et se précise — la classe **existe**, elle n'est **pas déposée**. C'est une **dette de
fourniture**, de la même famille que `G-1` (`hors-KB/A/`), **et non un défaut propre à `R-23`.**

**AUCUNE de ces six pièces n'est déposée par le présent amendement.** Les déposer déplacerait le
compte des 215 scellés et le manifeste `v2.124` : **arbitrage opérateur requis, non pris ici.**

## §7. QUATRE PIÈCES SUR TREIZE N'ONT AUCUN RAPPORT — collision de nomenclature, troisième du genre

`ANNEXE_F_fiches_F01-F50_v1.md` · `KNOWLEDGE_BASE_INDEX_QCCC_v32_POST_F5.md` ·
`PATCH_F5_KB_INDEX_QCCC_v31_VERS_v32_v1.md` · `PATCH_ANNEXE_F_F51EW_C2beta_v1.md`.

**Mesuré : `LC-RACCORD` = 0 occurrence dans les quatre ; `QCCC` = 1, 51, 34, 1.** Corpus **QCCC**
(arithmétique des constantes du Modèle Standard, PSLQ, Annexe F, fiches `F.51`, phase R-III, avril
2026) — **projet distinct**, sans intersection de contenu avec le front F5 de LC-RACCORD.

**DEUX `F5` :** le front `F5` de LC-RACCORD (sélection d'état / CFT de raccordement, juin 2026) et
la série `F.51` / l'index `POST_F5` de QCCC. **Troisième collision de nomenclature de ce dossier**
après `DEUX D5` et `TROIS W3`. Le lot a été constitué **par chaîne de caractères dans les noms de
fichiers**, et la chaîne `F5` est ambiguë entre deux corpus.

**Précédent proposé** : *un lot rassemblé par sous-chaîne de nom de fichier n'est pas un lot
thématique ; le tri se fait par `codename`, jamais par le nom.* `codename:` est justement le champ
qui distingue les deux corpus, et il est présent dans les pièces LC-RACCORD, absent des quatre autres.

## §8. Ce que cet amendement ne fait pas

Il ne dépose aucune pièce absente, ne modifie aucun octet de `kb/`, ne retourne aucune cible, n'arme
aucun sceau, ne convertit aucune borne, ne construit pas `O₂`, ne fixe pas `N`. **Une confirmation
par surface indépendante n'est pas une démonstration ;** elle atteste que le dépôt et l'archive
disent la même chose, jamais que ce qu'ils disent est vrai de la physique.

`{ A4 ; A2★ ; N }` INCHANGÉ · `D1` non clos, `D1c` intacte · Silo R clos à 12/12 · β `T-b`, NON
RÉSOLU, seul facteur d'`O₂` ouvert · **CCC non démontrée NI réfutée.**
