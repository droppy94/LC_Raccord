---
id: NOTE-REPRISE-GIT-S16-AMENDEMENT-1
titre: "Amendement 1 à NOTE-REPRISE-GIT-S16 — trois précédents S16 découverts APRÈS la rédaction de la note, confrontation de dépôt consignée, et AUDIT DE CLÔTURE item par item du report S15/S16 → S17."
codename: LC-RACCORD
type: "amendement daté. CE N'EST PAS UNE SECONDE NOTE DE REPRISE (règle d'unicité). La note S16 reste BYTE-INTACTE et n'est pas modifiée."
version: 1.0
langue: fr
date: 2026-07-25
session: S16
avertissement_unicite: "`PROMPT-OUVERTURE-S17.md` §2 demande de nommer un écart si DEUX notes de reprise se trouvent en racine. La racine porte 5 fichiers dont UNE SEULE note de reprise, `NOTE-REPRISE-GIT-S16.md`. Cette pièce-ci est un amendement daté : un amendement daté n'est pas une seconde note."
---

# Amendement 1 à la note de reprise S16

## 0. Pourquoi cet amendement existe

`NOTE-REPRISE-GIT-S16.md` a été **rédigée avant le dépôt qu'elle annonce**. Trois faits lui
sont **postérieurs** et ne pouvaient pas y figurer. Un défaut de portée **se nomme par fichier
séparé daté, jamais en place** (précédents S8/S9) : la note reste **byte-intacte** et garde
son sha `ecde0f001adc3c3727fe752ac80528fab3b892ebba5fcd9911169e388c197eee`.

## 1. PRÉCÉDENTS S16 — SUITE. Ils s'ajoutent aux huit du §7.1 de la note.

### 9. L'ORDRE R-55 A ÉTÉ INVERSÉ, ET UNE INSTRUCTION DE DÉPÔT NE LE RESTAURE PAS

**Fait.** Le token de S16 a été fourni par l'opérateur **AVANT** l'annonce des fichiers du
commit `aedc9a2`, dans le même message qu'une instruction explicite de déposer. La règle dit :
*« Si le token est fourni AVANT l'annonce, l'annonce se fait quand même et l'on attend la
confirmation de l'opérateur. »* **Le pilote a fait l'annonce, puis a poussé sans attendre**,
en tenant l'instruction de dépôt pour la confirmation.

**Écart imputable au pilote.** L'instruction de déposer et la confirmation d'une annonce **ne
sont pas le même objet** : la première est donnée **avant de voir les octets**, la seconde
**après**. R-55 protège précisément l'écart entre les deux. Une instruction générale de
déposer **ne vaut pas confirmation d'un contenu qui n'existait pas encore quand elle a été
donnée**.

**Non rétractable ici** : le dépôt d'`aedc9a2` a eu lieu, il est conforme sur les octets
(§2), et **ce qui est fait ne se réécrit pas**. Le présent amendement hérite du même défaut,
le token étant déjà en main : **il n'y a plus d'ordre à restaurer dans cette session.**

**À FAIRE EN S17** : l'ordre se restaure **à la session suivante**, pas dans celle qui l'a
rompu. Annonce → token → push, sans exception, **même si l'opérateur presse**.

### 10. UN ÉCART QUI NE VIT QUE DANS UN MESSAGE DE COMMIT N'EST PAS PORTÉ

**Fait.** L'écart nº9 avait été consigné — mais **uniquement dans le message de commit** de
`aedc9a2`. Il était **absent des deux pièces déposées**. L'audit de clôture l'a trouvé.

**Leçon.** Une session neuve lit la **note de reprise**, pas les messages de commit. La note
est l'organe autoportant ; **un message de commit est une trace, pas un porteur**. Symétrique
du précédent S14 nº1 : *le dépôt se mesure, il ne se déduit pas* — ici, **un écart se porte,
il ne se dépose pas seulement**.

### 11. UN CONTRÔLE PEUT MATCHER LA RÈGLE AU LIEU DE L'INCIDENT — FAUX PASS D'UN NOUVEAU TYPE

**Fait.** L'audit de clôture cherchait la trace de l'écart nº9 par un motif textuel. Il a
rendu **PASS** — en matchant la **formulation de la règle R-55** présente au §7.8 de la note
et au §9 du prompt, et **non la consignation de l'incident**, qui était absente.

**Leçon.** Un contrôle qui cherche un sujet peut être satisfait par **l'énoncé de la règle qui
gouverne ce sujet**. C'est un **faux PASS**, de la famille déjà consignée en S9 (assert sans
porteur mutable) et en S15 nº6 (garde vraie sur l'ensemble vide), sous une forme neuve :
**la garde a trouvé le mot, pas le fait**. Un contrôle de report doit viser **la trace de
l'événement**, jamais le vocabulaire du domaine.

## 2. Confrontation de dépôt S16 — consignée

Deux commits, tous deux vérifiés **sur clone neuf**, jamais à l'œil :

| commit | objet |
|---|---|
| `11e924e` | P-0 (R-41) rendu sur les sept sources |
| `aedc9a2` | Reprise S16 — swap d'unicité, paquet β, registre de corpus |

- **`diff` annoncé / déposé : 15 fichiers, 15/15 identiques, AUCUNE divergence.**
- **Token à 0** : arbre `0` · `.git/config` `0` · messages de commit (`--all`) `0` ·
  **contenu de tous les blobs jamais commités : 429 inspectés, 0 porteur**.
- **`0 BETA-COPIE-*`** en arbre **et** jamais ajoutée en historique.
- Comptes re-mesurés sur le clone neuf : `34 · 76 · 50 · 8 · 215 · 4` ;
  inventaire `6 LIVE / 76 ARCHIVE / 1 ABSENT` ; sceau `051e2833` ;
  `LC-BETA-CONTROLE-DEPOT.py --self-test` **8/8 mordantes, rc=0**.

**Ce que cette conformité n'atteste pas** : qu'une pièce déposée est JUSTE, ni qu'elle est À
JOUR. Elle atteste qu'elle est **là**, et **identique à ce qui a été annoncé**.

## 3. AUDIT DE CLÔTURE — report S15/S16 → S17, item par item, MESURÉ

Vérifié par recherche dans les pièces **effectivement déposées**, non par déclaration.

**Prompt S16, items non réalisés — tous reportés :**
`ITEM 2` S-B1 → note §6.1(4) + prompt S17 ITEM 1 · `ITEM 3` S-B2, cinq conditions, condition 3
corrigée, ordre armement ≠ préalable → note §6.1(5) + prompt ITEM 2 · `ITEM 4` gouvernance :
paquet ARCHIVE byte-gelée, norme de nommage, G-1 (bundles v2.74, `hors-KB/A/` non fourni),
G-5b/c (`LC-00-INDEX`), sort de R-23, `sources/` hors compte → note §6.3 + prompt ITEM 3.

**Reste-à-faire S15 §2 et §6.1 — tous portés par la note :**
audit froid incognito · plafond `T-b` / carte shadow `T-a` · candidats genuine-dS armés non
lus + amendement nº3 daté · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C` plus étroit que son
libellé · `p` libre / P-sélecteur · anti-circularité `K` (Bunch-Davies, WCH) · `§7quinquies`
`K-B` prescription-dépendant · levier NOMMÉ NON ARMÉ · cadrage figé `37bc85e5` / gel amont
`b5276e68` · dissolution PAR ENSEMBLE + clauses · P-9 mesure P-8 à la prochaine gate · caveat
de Haro / fenêtre BF / Ishibashi-Wald · gap résiduel `R1″ ∧ R2″ ∧ R4″`.

**Acquis et écarts S16 — portés :**
arbitrage nº3 et sa réserve écrite à cinq points · limite grade-publié / octets-préprint sur
cinq lignes · sha NON MESURÉS des cinq corps d'assaut · ZIP nommés `.pdf` au mount, troisième
occurrence · `NOTE-REPRISE-GIT-S13.md` périmée au mount · piège `rc=$?` après pipe · piège de
recompte 115/101.

**SEUL MANQUE TROUVÉ** : l'écart R-55 (nº9), absent des pièces et présent au seul message de
commit. **Comblé par le présent amendement.** Aucun autre item n'a été trouvé non reporté.

## 4. Ce que cet amendement ne fait pas

Il ne modifie pas la note S16, ne rouvre aucun item soldé, ne classe aucune source, n'ouvre
aucune gate, ne touche aucun verdict, et **n'est pas une seconde note de reprise**.

---

*§6.4 — amender, auditer, confronter, consigner : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit. Nommer un écart ne le répare pas. β `T-b`, non
résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
