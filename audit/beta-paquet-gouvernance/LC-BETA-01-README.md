---
id: LC-BETA-01-README
codename: LC-RACCORD-BETA
titre: "Mode d'emploi opérateur — paquet autoportant du chantier β. Ce que le paquet est, ce qu'il n'est pas, ce qu'il faut décider AVANT de l'ouvrir."
version: 0.1
langue: fr
date: 2026-07-18
---

# Paquet β — mode d'emploi

## §1 — Ce que vous avez

**43 fichiers.** 8 écrits pour le chantier (`LC-BETA-*`) + **35 copies byte-exactes** du mount
principal (`BETA-COPIE-*`), gelées au **2026-07-18**, état **V94 / manifeste v2.121**.

| fichier | rôle |
|---|---|
| `LC-BETA-00-PROMPT-PROJET.md` | **à coller comme prompt du nouveau projet**. Régime, rôles, règles autoportantes, ordre des phases |
| `LC-BETA-01-README.md` | ce fichier |
| `LC-BETA-02-ETAT-BETA.md` | l'état du front β — **index à vérifier**, provenance par ligne |
| `LC-BETA-03-CADRAGE.md` | **projet** de cadrage — **à geler et déposer AVANT toute lecture** |
| `LC-BETA-04-R41-MIROIRS.md` | fiche R-41 **vierge** pour S8/S9/S10 |
| `LC-BETA-05-RETOUR-KB.md` | pare-feu + protocole de retour + condition de dissolution |
| `LC-BETA-PAQUET-GEL.md` | manifeste : 35 × `canon ↔ sha256` |
| `LC-BETA-BOOT.py` | §0-lite-β, autoportant, sans réseau ni mount |
| `BETA-COPIE-*` (35) | le dossier gelé |

## §2 — Trois décisions qui vous appartiennent, avant d'ouvrir quoi que ce soit

1. **Le chantier doit-il exister ?** V94 §6 ACTION #3 classe S8/S9/S10 en **menu, décision
   opérateur, AUCUN geste obligé**. Ouvrir un chantier dédié **crée de l'inertie** : un
   chantier ouvert cherche à produire. `LC-BETA-05` §5 porte une **condition de dissolution**
   écrite d'avance — c'est le contrepoids, il ne vaut que si vous l'appliquez.
2. **`P-8` d'abord ?** Le mandat `P-8` est **dû avant toute gate future** (V94 §4). La
   consommation de S8/S9/S10 **est** une gate. En l'état, **le chantier peut être cadré mais
   ne peut pas tirer**. Deux ordres possibles : `P-8` puis β, ou β cadré-en-attente. **Tirer
   sans `P-8` referait exactement ce que V94 a consigné contre le pilote.**
3. **Le régime.** Le paquet est **CONSOMMATEUR** (`LC-BETA-00` §2). Un régime **FORK** — deux
   KB vives — casserait la gouvernance d'intégrité. Si vous voulez autre chose, **dites-le
   avant**, pas après le premier dépôt.

## §3 — Ouverture, dans l'ordre

1. Créer le projet, coller `LC-BETA-00-PROMPT-PROJET.md` en prompt de projet.
2. Y déposer les **43 fichiers**.
3. `python3 LC-BETA-BOOT.py` — attendu **42 hachés** *(le manifeste s'exclut lui-même)*,
   `absents 0`, `alterees 0`, pare-feu `0/0`, et `PKG_SHA_BETA_8` **égal à la valeur que je
   vous ai donnée hors-fichier** (R-36 : elle n'est écrite dans **aucun** fichier du paquet).
4. **Ajouter `BETA-* 0` au pare-feu du §0-lite de la KB principale.**
5. `P-0` (R-41) → `P-1` (positionnement stérile) → **STOP et décision**.

## §4 — Ce que ce paquet n'est pas

- **Pas à jour par construction.** Il **fige** un état daté. Dès que la KB bouge, **il ment
  par âge** — pas par faute. `LC-BETA-PAQUET-GEL.md` existe pour que ce mensonge soit
  **détectable en une commande**, pas pour l'empêcher.
- **Pas une autorité.** C'est un **cinquième index**. Les quatre précédents ont été
  **convaincus de faux**. **Le mount principal arbitre** (R-54).
- **Pas une réparation.** Écrire un paquet ne solde ni `P-8`, ni `D-01`, ni `D-08` (`P-9`).

## §5 — Deux défauts de ce paquet, contre moi

1. **Les identités de S8/S9/S10 ne sont pas attestées sur le mount principal.** Grep
   exhaustif, 2026-07-18 : les noms *Bros–Moschella*, *Nakayama*, *Ghaffari–Luciano–Mantica*
   **n'y figurent nulle part**. Ils viennent de la **piste article** et de **ma mémoire** —
   R-54 : **un** témoignage, pas deux. Le deck de présentation que j'ai livré hier les
   affiche pourtant **comme un fait** sur sa diapositive « Axes suivis ». **C'est une
   assertion non sourcée sur le mount, et elle est de moi.** Elle est ici **cantonnée** à la
   fiche R-41, en **piste**, jamais en donnée.
2. **La pertinence de ces sources pour la cellule `R1″∧R2″∧R4″` est une hypothèse du pilote.**
   Elles ont été retenues pour la **synthèse d'un article**, pas contre ce mur. Le paquet est
   donc bâti pour que **`C-iii`/`C-iv` (hors-domaine) soit une issue pleine**, déclarée
   d'avance comme l'attendu.

---

**§6.4.** Préparer un paquet ne scelle, ne réduit, ne compte, ne démontre **RIEN**.
`{A4 ; A2★ ; N}` **INCHANGÉ** ; **β `T-b`, non résolu, SEUL facteur d'O₂ ouvert** ;
`R-53 0/4` ; **CCC n'est ni démontrée ni réfutée.**
