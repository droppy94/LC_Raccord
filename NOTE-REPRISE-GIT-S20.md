---
id: NOTE-REPRISE-GIT-S20
titre: "Note de reprise S20 — UNIQUE, autoportante, OPÉRATIONNELLE. Swap d'unicité −NOTE-REPRISE-GIT-S19 −PROMPT-OUVERTURE-S20, précédé d'un AUDIT DE REPORT item par item (§9). S20 a produit UN MOUVEMENT SCIENTIFIQUE — R-23 n'est pas soldée, elle est SUSPENDUE À OB — après six séances de méthode."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée, OPÉRATIONNELLE. Elle se recale en place et ne reçoit pas d'AMENDEMENT-<n>. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
recalages: "(aucun à ce jour)"
---

# Note de reprise S20

## §0. ATTENDUS DU §0-lite — chacun avec sa commande littérale

`ls instruments/*.py | wc -l` **34** · `ls instruments/archives-scelees/*.py | wc -l` **76** ·
`ls audit/ | wc -l` **73** (72 fichiers + 1 répertoire) ·
`ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l` **8** · `ls kb/*.md | wc -l` **215** ·
`ls hors-KB/B/ | wc -l` **4** · `ls -p | grep -v /` **4**.
`sources/` et `manifest/` **HORS COMPTE, assumé**. `hors-KB/A/` **ABSENT par construction**.

`python3 instruments/inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** (réécrit sa date :
restaurer par `git checkout`) · `python3 instruments/run_sceau.py verif_paquet_propre` → sha8
**`051e2833`**, rc 0 · **12 redémonstrations : 271/271 PASS + 101 consignations, 12/12 rc 0 —
INCHANGÉ depuis S9.** Décomposition, multiensemble : `35+17+16+16+12+11+6+21+40+45+16+36 = 271` ·
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`. Variantes qui comptent : `redemo_R4_CT_b.py`,
`redemo_R5_reductions_b.py` ; les v1 **ne se rejouent pas**. Motif :
`^[[:space:]]*\[?PASS\]?` — quatre scripts impriment **sans crochets**.

Cinq rejeux hors compte : `harnais_R9.py` 6/6 · `harnais_R11.py` 7/7 + **0 vacante** (nettoyer
`__pycache__/`) · `cd hors-KB/B && python3 verif_B_tracteur.py` rc 0 ·
`instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` 6/6 ·
`audit/LC-BETA-CONTROLE-DEPOT.py --self-test` 8/8 — **sans audit de vacuité, dette OUVERTE**.
Sixième, confronté en S20 : `instruments/archives-scelees/verif_F5_scaling.py` rc 0, **19
assertions**, coefficient O(1) libre.

**Intrants `sources/` 3/3** : `2312_12498v2.pdf` 1 895 152 o `04d9b4f4` · `2409_10595v2.pdf`
2 332 898 o `27a94980` · `2503_19957v1.pdf` 910 410 o `113ab4a2`.

**KB ACTIVE — L'ATTENDU DE S20 ÉTAIT FAUX, NE LE RECOPIE PAS.** Le prompt S20 annonçait 4 vrais PDF
confrontés au bit. **Mesuré en S20 : 0/4.** Les quatre `.pdf` sont des **ZIP** (`50 4b 03 04`),
image + OCR par page + `manifest.json` sans sha de source — l'état du mount de S17. Pagination
**38 · 14 · 78 · 88 conforme 4/4**, octets **0/4**. Cause établie : `mtime` époque zéro
(`1979-12-31`) ⟹ **la surface est re-matérialisée à la construction du conteneur**, elle ne sert pas
les octets stockés. **AUCUN ATTENDU NE DOIT PLUS PORTER DE sha256 POUR LA KB ACTIVE.** La clause du
correctif 6 — *« elle peut désormais servir des octets confrontables »* — est **FAUSSE** : vraie
d'une matérialisation, une fois, inscrite comme propriété générale.

## §1. LE MOUVEMENT DE S20 — `R-23` n'est pas soldée

Voie (i) AU FOND ouverte sur GO, cadrage gelé **déposé avant lecture** (`85b1a0e`), enveloppe
ouverte **après**, corps de F5 lu **ensuite**. Ordre vérifiable dans l'historique.

- **`C-1` = (a) CONTINGENTE.** L'`inconfrontable` de la Table III est **levable**, et F5 écrit sa
  condition de levée : *« deviendront confrontables dès que `O₂` fournira le coefficient `W³` —
  renvoi-avant, PAS une fermeture »* ; `OB ⊂ O₂` *« rend la Table III confrontable »* ; **`L3` non
  déclenché** exclut le cas structurel. ⟹ **`R-23` EST SUSPENDUE À `OB`**, jamais soldée.
  **DÉLIMITATION**, aucune réduction.
- **`C-2` = (b) ENREGISTRÉ**, et **CONFIRMATION D'ANTICIPATION** — pré-empté par l'enveloppe,
  déclaré avant lecture. F5 écrit *« exactement comme l'audit F2 l'avait établi »*, F2 écrit
  *« renvoi-avant F5 »* : **circularité de renvoi**. Confirmé par F5 lui-même —
  `LC-AUDIT-LOG-F5` §4 range *« héritage R-23 (AUDIT-LOG-F2) »* parmi les intrants **NON RE-JUGÉS**.
- **`C-3` = (a) LEVIER ÉCRIT.** Valeur manquante nommée — les `(a,b,c)` du Weyl cubique depuis le
  `⟨TTT⟩` de la CFT de raccordement ; bloqueur localisé — `O₂`, CL mixte **Dirichlet ↔ Neumann** au
  `𝒞`, réciprocité conforme de Penrose.

**GÉNÉALOGIE DU MOT `soldée`, comptée** : **0** dans le chaînon F5 · **0** dans son cadrage · **0**
dans les deux instructions d'audit · **1** dans `LC-AUDIT-LOG-F5` — **dans sa consigne de
propagation, trois lignes après le paragraphe qui déclare `R-23` non re-jugée** · **24** dans
`LC-WORK-PROPAGATION-LOG-F5`. **Effet de transport, jamais un résultat.**

**Chaînage, sans surclassement** : `R-23 ⊂ OB ⊂ O₂`, et β `T-b` est le seul facteur d'`O₂` ouvert
⟹ `R-23` est **en aval de β `T-b`**. Consolidation. Elle **change de nom, pas de statut**.

## §2. CE QUI A ÉTÉ DÉPOSÉ EN S20 — quatre commits

| commit | contenu |
|---|---|
| `85b1a0e` | `audit/R23-AU-FOND-CIBLES-GELEES.md` — cadrage gelé neuf, avant toute lecture |
| `7febb5f` | `audit/R23-AU-FOND-VERDICT.md` + `-AMENDEMENT-1.md` |
| `6ecff56` | `audit/REGISTRES-OPERATIONNELS-INSTRUCTION.md` + recalage de 4 registres `kb/` |
| *(présent)* | `audit/HISTORIQUE-PROJECTION-INSTRUCTION.md` + swap note/prompt |

**PREMIER RECALAGE EN PLACE DE PIÈCES `kb/`** : `02_programme` v1.29 · `04_references` v1.30 ·
`AUD` v1.72 · `IDX_v211` v2.12. `ls kb/*.md` = **215, INCHANGÉ**. Confronté au bit sur clone neuf
**et** sur la KB active après pose : **4/4**.

## §3. ARBITRAGES OPÉRATEUR RENDUS EN S20

1. **Les registres `kb/` sont OPÉRATIONNELS**, pas scellés — ils se recalent en place sous les trois
   obligations du correctif nº2. Gels, cibles gelées, verdicts et rapports rendus **non concernés**.
2. **Le correctif nº3 se REFAIT, ne s'ajuste pas.** Exécuté : `HISTORIQUE-PROJECTION-INSTRUCTION`.
3. Recalage `soldée` → `suspendue à OB` **exécuté au corps**, 4 occurrences ; **6 laissées intactes
   en changelog**.

## §4. RÈGLES NEUVES, opposables — PRÉCÉDENTS S20

1. **DANS UNE PIÈCE OPÉRATIONNELLE, LE CHANGELOG N'EST PAS RECALABLE.** Un changelog dit ce qui a
   été **écrit**, jamais ce qui est **vrai**. Toucher un `maj:`, un `recalages:` ou tout journal daté
   est un **écart**, pas une correction. La portée d'un recalage s'arrête **au corps**.
2. **UN MOT ABSENT DE TOUTES LES PIÈCES DE SCIENCE ET PRÉSENT DANS TOUTES LES PIÈCES DE PROPAGATION
   N'EST PAS UN RÉSULTAT — C'EST UN EFFET DE TRANSPORT.**
3. **DÉPLACER UN CONTENU CONTAMINANT NE LE RETIRE PAS DU DÉPÔT.** Tant qu'une pièce lisible en porte
   une copie, l'enveloppe ne scelle rien. **On ne cache pas par relocalisation ; on borne la
   projection.**
4. **UNE TABLE DE FOURNITURE NE SE PUBLIE QU'APRÈS QUE LA SOURCE EST POUSSÉE** et son sha re-mesuré
   sur clone neuf. Une table qui désigne des octets non déposés n'indique pas où les prendre : elle
   invite à les prendre ailleurs. **Écart S20 du pilote, et le plus coûteux.**
5. **LA CONFRONTATION D'UNE FOURNITURE SE FAIT APRÈS LA POSE, SUR LE MOUNT, PAR LE PILOTE.**
   L'annonce d'avant ne peut pas voir un renommage qui n'a pas eu lieu. Amende la garde de
   `b8c6700`, qui visait le mauvais moment.
6. **UNE ANNONCE QUI RECOPIE LA TABLE DU PILOTE N'EST PAS UNE MESURE** — un instrument rapporté deux
   fois n'est pas deux instruments.
7. **UN LOT RASSEMBLÉ PAR SOUS-CHAÎNE DE NOM DE FICHIER N'EST PAS UN LOT THÉMATIQUE.** Le tri se
   fait par `codename`, jamais par le nom. **DEUX `F5`** — le front LC-RACCORD et la série `F.51` /
   l'index `POST_F5` du corpus **QCCC**, projet distinct. Troisième collision après `D5` et `W3`.
8. **`CONFIRMATION` / `DIVERGENCE` EST UNE PARTITION INCOMPLÈTE** — il manque **`NON ANTICIPÉ`**.
9. **UNE SURFACE PEUT CHANGER SANS QUE PERSONNE N'AGISSE.** La KB active est re-matérialisée par
   session ; deux sessions voient deux contenus sous le même nom, sans geste ni trace.

## §5. SIX ÉCARTS PILOTE S20, déclarés

1. Écriture sur la KB active (`touch`), retirée, cardinal remesuré.
2. `grep` non borné sur `kb/02_programme.md` — ~15 000 tokens, garde connue.
3. Ré-import des cinq points contaminants par la porte laissée ouverte du correctif nº3.
4. `verif_F5_scaling.py` déclaré absent sur une correspondance fausse — il est en
   `instruments/archives-scelees/`.
5. **« `kb/` est SCELLÉ » appliqué plus large que le texte du correctif nº2**, qui borne le régime
   aux pièces scellées.
6. **Table de fourniture publiée avant que la source existe** — a conduit l'opérateur à poser dans
   sa KB `02_programme` **v1.19** et `04_references` **v1.0**, neuf et vingt-neuf bumps en arrière.
   Détecté par mesure, corrigé, KB confrontée 4/4 après reprise.

## §6. RÉSERVES QUI SE RECOPIENT — aucune ligne du périmètre n'est sans réserve

**CINQ** lignes (`B1` `B2` `B3` `B4` `S8`) sous **RÉSERVE PERMANENTE** version-consommée /
version-gradée · **DEUX** (`S9` `S10`) sous **RÉSERVE ÉCRITE à cinq points**. **5 + 2 = 7.**
S'ajoute la **RÉSERVE DE VERSION sur `LC-00-INDEX`**.

**DEUX RÉSERVES NEUVES sur F5, écrites par son propre audit froid et ABSENTES DU DÉPÔT** :
(1) **chronologie réelle d'écriture NON VÉRIFIABLE** (cadrage + 3 versions le même jour), et la
présence de « 0,53 » dans le cadrage pré-fetch est *expliquée mais NON CERTIFIABLE* (`R-27`) ;
(2) **`R-7` vérifiée par le journal `maj`, PAS par diff** — v0.1/v0.2 absentes du paquet.
**Une ligne F5 citée sans elles est INCOMPLÈTE.**

Et : *« aucune ligne n'est classée sur des octets confrontables »* **reste vrai du classement rendu**.

## §7. PRÉCÉDENTS S8–S19 — portés par renvoi mesuré, et c'est une DÉROGATION déclarée

Les précédents antérieurs sont au §7 de `NOTE-REPRISE-GIT-S19.md`, **retirée au présent commit et
conservée dans l'historique git** : commit `6cbc4d3`, sha256
`d5b57ae65a0717856261332e7493e129671d8c05a2e97643ba2a5f3ab00fb205`, 49 286 o. Restitution :
`git show 6cbc4d3:NOTE-REPRISE-GIT-S19.md`.

**DÉROGATION À L'AUTOPORTANCE, DÉCLARÉE ET SOUMISE À ARBITRAGE.** La règle d'unicité veut une note
qui porte tout. Le précédent S19 nº10 mesure que *la masse d'un protocole est elle-même une source
d'écarts*, et S19 a mesuré que six correctifs **déplacent** l'appareil sans l'alléger. Le pilote
S20 **propose** de porter les précédents antérieurs par **coordonnée git + sha256** plutôt que par
recopie, et le **déclare** au lieu de le faire en silence. **L'opérateur tranche en S21.**

Titres opposables, portés ici en une ligne chacun (texte complet au renvoi) :

**S19** — consigne régulant l'ordre interne du pilote ≠ garde · pièce non scellée ≠ byte-intacte ·
note autoportante qui se contredit · dispositif anti-fit devenu vecteur · surface sans version ≠
mémoire · fourniture de même nom = destruction sans trace · deux surfaces sans concordance divergent
· retrait par nom jamais par propriété · question sur un fait mesurable = instrument non employé ·
masse du protocole = source d'écarts · coïncidence sous deux instruments ≠ confirmation · vocabulaire
ne s'introduit pas par l'usage · R-36 s'étend à toute mesure d'une pièce sur elle-même.
**S18** — objet levé sous son gel ne se ré-instruit pas · deux objets de même écriture ≠ un objet ·
cadrage défectueux sans être faux · un compte n'est vrai que sous son instrument · garde inutile ≠
garde fausse · reste-à-faire écrit trop large · absence par construction · résoudre un renvoi ≠ le
rendre traçable · classe qui absorbe ne classe pas · les motifs se bornent.
**S17** — une pièce ne connaît pas sa position · contenant non ouvert ≠ contenant mesuré · le nom
d'un contenant ne décrit pas son contenu · arbitrage inexécutable ne se dégrade pas en silence ·
antériorité sur une ligne ne dit rien des autres · le token confirme l'annonce, pas une version
améliorée · un instrument compte ce qu'il compte · un écart rejeté se date · mesure sans version ne
confronte rien.
**S16** — un instrument se mesure aussi · identifier dans les octets d'abord · un grade ne se
transfère pas d'une version à l'autre · ne pas déposer les octets quand le registre suffit · mesurer
la règle plutôt que la contourner · `rc=$?` après un pipe · une issue anticipée ne se retouche pas ·
l'ordre R-55 ne se restaure pas par une instruction de dépôt · un écart qui ne vit qu'en message de
commit n'est pas porté · un contrôle peut matcher la règle au lieu de l'incident.
**S15** — une règle se mesure à sa source, pas à sa glose · pare-feu nominal ≠ protection · gel sur
répertoire vivant ≠ gel · confrontation payée se préserve hors surface tournante · ZIP de transport
≠ ZIP de substitution · contrôle qui passe sur l'ensemble vide = faux PASS · un GO n'est pas un
arbitrage.
**S14** — une vérification se brûle si on publie sa valeur attendue · un retrait se précède d'un
audit de report item par item · le pilote ne signe pas du nom de l'opérateur · un arbitrage
prospectif ne se rétroapplique pas · un ordre de conditions ne se comprime pas.
**S13 · S11 · S10 · S9 · S8** — bloc porté **uniquement** par le renvoi ci-dessus ; le pilote S20
**n'en a lu qu'une ligne** (*une absence constatée par extraction n'est pas une absence*) et **ne
recopie pas ce qu'il n'a pas lu**.

## §8. PROCÉDURE DE DÉPÔT — R-55, inchangée

Annonce **AVANT** le token : **chemin + sha256 complet + message de commit, FICHIER PAR FICHIER,
RETRAITS COMPRIS**. Un token donné avant l'annonce **n'est pas** une confirmation ; faire l'annonce
quand même et attendre. **Une instruction de déposer n'est pas la confirmation d'une annonce.**
Push par **URL éphémère**, jamais `git remote set-url`. Après push : `diff` sur **clone neuf** ;
token à **0** dans l'arbre, `.git/config`, les messages **et le contenu de TOUS les blobs**
(`git rev-list --objects --all`) ; puis **révocation MESURÉE** par un **401** sur
`GET https://api.github.com/user` — elle ne se demande pas. **Un token par dépôt.** Le message de
commit ne s'enrichit **pas d'un mot** après l'annonce. Identité :
`LC-RACCORD pilote S<n> <pilote-s<n>@lc-raccord.local>`. **Le pilote ne signe jamais du nom de
l'opérateur.**

## §9. AUDIT DE REPORT — item par item, avant retrait

| item de `NOTE-REPRISE-GIT-S19` / `PROMPT-OUVERTURE-S20` | report |
|---|---|
| attendus §0-lite + commandes littérales | **§0**, recalés (`audit/` 68 → 73) |
| KB active, 4 PDF confrontés au bit | **§0** — **RETOURNÉ**, 0/4, attendu déclaré faux |
| `R-23` armée sur voie (i) | **§1** — **TRANCHÉE**, suspendue à `OB` |
| réserves 5 + 2 = 7 + `LC-00-INDEX` | **§6**, plus deux réserves neuves |
| précédents S8–S19 | **§7**, par renvoi mesuré, dérogation déclarée |
| procédure R-55 | **§8**, intégrale |
| `ITEM 2` gouvernance, `ITEM 3` restes de fond | **§10**, aucun entamé |
| enveloppe / correctif nº3 | remplacé par `HISTORIQUE-PROJECTION-INSTRUCTION` |
| `LC-BETA-PAQUET.zip`, journal V94, 8 pièces `LC-BETA-*`, `LC-00-INDEX`, pare-feu | **§10**, inchangés |

## §10. RESTE-À-FAIRE ET OUVERTS

**Dettes ouvertes, non exécutées** — `G-1` (fourniture `hors-KB/A/`) · `G-5c` · migration de `kb/`
bloquée sur `G-4` volet 3 · recalage de `kb/LC-CONST-V1` §2 (périmé, scellé) · dette `M vacantes`
sur `LC-BETA-CONTROLE-DEPOT.py` · dette `instruments/concordance_mount.py` · **dette V97** : la
condition d'arrêt du boot n'a pas été exécutée depuis S14 · scission du §0-lite proposée non arbitrée
· les 3 orphelines de la KB active · reports V96 §4.

**NEUF EN S20 — dette de fourniture, échafaudage F5**, six pièces présentes chez l'opérateur et
absentes du dépôt, **non déposées** car cela déplacerait les 215 scellés et le manifeste `v2.124` :
`LC-AUDIT-LOG-F5` 14 022 o `925051c1` · `LC-WORK-AUDIT-FROID-F5` 18 062 o `f74db9a1` ·
`LC-WORK-AUDIT-FROID-F5-PASSE4-ROUTES` 8 443 o `c28ea22e` · `LC-WORK-PROPAGATION-LOG-F5` 31 563 o
`abcaba94` · `LC-WORK-REPRISE-POST-PROPAGATION-F5` 7 148 o `c5245fb9` ·
`LC-WORK-REPRISE-POST-PROPAGATION-F5-APPLIQUEE` 10 750 o `d60640f0`. **Arbitrage opérateur requis.**

**NEUF EN S20 — défauts nommés, non corrigés** : front-matter YAML **invalide** sur `AUD`,
`IDX_v211`, `LC-WORK-BRANCHE-FALSIFIABILITE` (second `maj:` imbriqué), **antériorité prouvée** ·
`IDX_v211.md` porte `v211` au nom quand `version:` vaut `2.12`, **non renommé** · le manifeste
`v2.124` ne cite que **7** noms de `.md` sur 215 ⟹ **l'appartenance à l'ensemble scellé n'est pas
établissable par mesure**.

**ITEM 2 — GOUVERNANCE**, aucun entamé, ci-dessus.
**ITEM 3 — RESTES DE FOND**, aucun entamé : audit froid incognito · plafond `T-b` / carte shadow
`T-a` · candidats genuine-dS armés non lus · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C` plus
étroit que son libellé · `p` libre / P-sélecteur · anti-circularité `K` · `§7quinquies` `K-B` ·
cadrage figé `37bc85e5` / gel amont `b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald · gap
résiduel `R1″ ∧ R2″ ∧ R4″`.

## §11. PÉRIMÈTRE

`{ A4 ; A2★ ; N }` **INCHANGÉ** · `[B]` = B-PAUVRE · `W2` = DÉLIMITATION, `A4` NON réfuté · `A2★`
décision ouverte, `C7` non levée · `D1` non clos, `D1c` INTACTE · `N` non fixé (≡ Λ, R-53 : 0/4) ·
`O₂` **non construit** · β **`T-b`, NON RÉSOLU, SEUL facteur d'`O₂` ouvert** · α = `C1-b` · `G3-a`
non levé · nœud (i) **TRANCHÉ EN DÉLIMITATION** · Silo R **CLOS à 12/12** · `W³` **SANS VALEUR** ·
**CCC non démontrée NI réfutée.**

---

**§6.4 — sentinelle terminale.** Cloner, mesurer, rejouer, confronter, classer, délimiter, arbitrer,
déposer, retirer, recaler, borner, requalifier une dette : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit. Requalifier `R-23` de *soldée* en *suspendue à `OB`* ne
construit pas `O₂`, ne dérive aucun `(a,b,c)`, ne fixe pas `N`, ne convertit aucune borne. **Une
dette qui change de nom reste une dette.** β `T-b`, non résolu, SEUL facteur d'`O₂` ouvert.
**CCC n'est ni démontrée ni réfutée.**
