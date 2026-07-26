---
id: PROMPT-OUVERTURE-S20
titre: "Prompt d'ouverture S20. OUVERTURE EN DEUX MESSAGES : l'ordre mesurer-puis-confronter est imposé par le CANAL, et les attendus sont placés APRÈS l'ordre de mesure. Correctif nº1 de S19."
codename: LC-RACCORD
type: "prompt d'ouverture — HORS base scellée, OPÉRATIONNEL. Il ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
---

# §0. À L'OPÉRATEUR — envoie ceci en DEUX messages

**MESSAGE 1, à envoyer SEUL.** Copie ces trois lignes, et rien d'autre. Elles ne portent **aucune
valeur attendue** : les lire ne peut donc rien ancrer.

> Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique.
> Rends la sortie BRUTE de `git status` et de `git log --oneline -14`, sans commentaire.
> Puis arrête-toi et attends.

**MESSAGE 2** : l'URL de la présente pièce, une fois le message 1 rendu.

*Pourquoi.* « Mesure HEAD avant de lire ce prompt » a été violée **deux sessions sur deux**, parce
que le prompt est le seul objet qui nomme le dépôt à cloner : la consigne se contredit
performativement. **Une consigne qui régule l'ordre interne du pilote n'est pas vérifiable, donc
n'est pas une garde** (précédent S19 nº1). Le canal, lui, ne se discute pas.

**Si tu envoies tout d'un coup**, ce n'est pas grave et ce n'est pas rattrapable par la volonté :
le pilote **nomme l'inversion**, mesure quand même, et rend `git log` **avant** de citer une seule
valeur attendue. Cette dernière clause, elle, est vérifiable dans le rendu.

# §1. MESURE — aucun attendu dans cette section, c'est voulu

1. Clone sous un **chemin unique**. Vérifie `git status` : arbre propre.
2. `git log --oneline -14`. **Rends la sortie brute.**
3. `git rev-parse HEAD` et `git log -1 --format=%s`.
4. **NE CITE AUCUNE VALEUR ATTENDUE AVANT D'AVOIR RENDU CES SORTIES.**

# §2. CONFRONTATION — les attendus, maintenant

**HEAD ATTENDU** : le commit dont le message commence par « **Reprise S19** ». Ses parents
remontent par `b8c6700` (topologie des dépôts, correctif 6), `a8f3923` (quatre correctifs de
méthode), `0a102b7` (Reprise S18), `602c828`, `dc8ca29`, `7dbee86`, `2ff65f9`, `b79e3de`, `aedc9a2`.

Le sha de ce commit **n'est PAS écrit ici** : ce prompt est déposé DANS lui (**R-36**). Désignation
par le **MESSAGE**, jamais par un sha qu'une pièce ne peut pas porter. **NE PRÉSUME PAS QU'IL EST
HEAD** — un commit postérieur peut s'être intercalé, c'est arrivé en S17. En S18 et S19 la chaîne
démarrait bien à HEAD : **cela ne prouve rien pour S20.** Confronte, puis **NOMME l'écart s'il y en
a un. NE CORRIGE RIEN D'OFFICE.**

# §3. La note de reprise — UNIQUE, AUTOPORTANTE, et OPÉRATIONNELLE

`NOTE-REPRISE-GIT-S19.md`, à la racine. Elle consolide et **REMPLACE** `NOTE-REPRISE-GIT-S18.md`,
retirée au même commit et conservée dans l'historique git. Elle porte les précédents **S8 à S19**
(§7), R-55 (§7.7), G-4 borné (§8), la table de supersession (§9) et l'**audit de report S19** (§10).

**LA RACINE PORTE 4 FICHIERS. Une cinquième pièce y est un écart à nommer.** UNE SEULE note de
reprise **de la série `GIT-S<n>`** ; `kb/NOTE-REPRISE-V96.md` est d'une AUTRE série, son contenu est
absorbé au §5bis, ses octets sont **INTACTS** — **ce n'est PAS un écart**.

**NEUF EN S19 — la note est une pièce OPÉRATIONNELLE** (`audit/SCELLE-OPERATIONNEL-INSTRUCTION.md`) :
un défaut mesuré sur elle **se corrige EN PLACE**, avec bump de `version:`, entrée au champ
`recalages:` et § nommés au message de commit. **Elle ne reçoit PAS d'`AMENDEMENT-<n>`.** Les gels,
cibles gelées, verdicts et rapports rendus restent **SCELLÉS et byte-intacts** : leur régime n'a pas
bougé d'une ligne.

# §4. §0-lite — sous ses DEUX instructions, toutes deux opposables

- `audit/S0LITE-IMPRESSION-INSTRUCTION.md` — les 12 scripts sont **TOUS exécutés intégralement** ;
  seule la **restitution** est compressée : par script `rc` + bilan auto-déclaré + compte sur
  marqueur **avec instrument déclaré**, puis les deux totaux. Rien d'autre. **Clause de dépliement :
  au premier écart, la sortie INTÉGRALE du seul script concerné est dépliée.**
- `audit/S0LITE-INSTRUMENTS-INSTRUCTION.md` — **tout attendu porte sa commande littérale. Un nombre
  sans son instrument n'est pas opposable, et tu dois le dire au lieu de le confirmer.** La table
  complète est dans cette pièce ; le §0 de la note la reprend.

Attendus, avec leur commande : `ls instruments/*.py | wc -l` **34** · `ls
instruments/archives-scelees/*.py | wc -l` **76** · `ls audit/ | wc -l` **68** (67 fichiers + 1
répertoire) · `ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l` **8** · `ls kb/*.md | wc -l`
**215** · `ls hors-KB/B/ | wc -l` **4** · `ls -p | grep -v /` **4**. `sources/` et `manifest/` sont
**HORS COMPTE, assumé par écrit**. `hors-KB/A/` est **ABSENT par construction** — pas un écart.

Puis `inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** (il **réécrit sa date** : restaurer
par `git checkout`) · `run_sceau.py verif_paquet_propre` → sha8 **`051e2833`**, rc=0 · puis les **12
redémonstrations** : **271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ depuis S9**.
Décomposition, multiensemble et **non** dans l'ordre : `35+17+16+16+12+11+6+21+40+45+16+36 = 271` ·
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`. Variantes qui comptent : `redemo_R4_CT_b.py` et
`redemo_R5_reductions_b.py` ; les v1 **ne se rejouent pas**. Motif : **`^[[:space:]]*\[?PASS\]?`** —
quatre scripts impriment **sans crochets**. Hors compte, **cinq rejeux** : `harnais_R9.py` 6/6 ·
`harnais_R11.py` 7/7 + 0 vacante (nettoyer `__pycache__/`) · `cd hors-KB/B && python3
verif_B_tracteur.py` rc=0 · `LC-WORK-GEN-PAQUET-v2_1.py --self-test` 6/6 ·
`audit/LC-BETA-CONTROLE-DEPOT.py --self-test` 8/8 — **et sans audit de vacuité, dette ouverte**.

**Intrants `sources/` au git**, 3/3 : `2312_12498v2.pdf` 1 895 152 o `04d9b4f4` · `2409_10595v2.pdf`
2 332 898 o `27a94980` · `2503_19957v1.pdf` 910 410 o `113ab4a2`.

**Intrants de la KB active — NEUF EN S19, CONFRONTÉS 4/4 AU BIT** contre le registre de corpus, et
**c'est la première fois** : `B1` `6b89e638…` 979 890 o 38 p. · `B2` `e080c5d6…` 386 010 o 14 p. ·
`B3` `1426146d…` 4 629 572 o 78 p. · `B4` `7102dcf9…` 1 223 061 o 88 p. **Vrais PDF, `%PDF` et
`%%EOF` aux octets, 0 ZIP.** La KB active porte **7 fichiers** et **aucune pièce de `kb/`**.

**GARDES D'ENVIRONNEMENT** : `rc=$?` après un pipe mesure le **dernier élément du pipe** — capturer
le `rc` **avant tout pipe** · `grep -c` compte des **LIGNES** · `|| true` quand le zéro est attendu ·
**BORNE TES MOTIFS**, un `grep -rn` non borné sur `kb/` coûte ~15 000 tokens · **`xxd` ABSENT**,
`python3` ou `od` · **`bash -c` requis** pour `diff <(…)`, qui échoue sous `/bin/sh` · `arxiv.org`
**hors** allowlist, `github.com` et `api.github.com` **dedans** · les outils web rendent du **TEXTE,
jamais des octets hachables**.

# §5. Rends-moi le §0-lite compressé, avec tout écart décomposé, AVANT de poursuivre.

# §6. CE QUE TU N'AS PLUS À ME DEMANDER

(a) **`LC-BETA-PAQUET.zip` et le JOURNAL V94 : SOLDÉS.** Les octets du journal **NE SE DÉPOSENT
PAS** — copie de substance, interdit dur, arbre ET historique.
(b) Les **8 pièces `LC-BETA-*` mentent par âge**, et ce n'est **pas** à corriger.
(c) **`LC-00-INDEX`** : déposé en S18 à `audit/00_index.md`, v1.78, byte-intact. **RÉSERVE
PERMANENTE** : 68 pièces le citent, 3 seulement nomment une version, max v1.64.
(d) **La KB active est bornée aux INTRANTS** (R-54, correctif 6). Elle porte 4 vrais PDF confrontés
au bit et 3 orphelines à analyser. **Elle peut servir des octets confrontables ; elle n'est pas une
mémoire** — le registre porte les sha, pas la surface. **Toute fourniture s'y annonce avec ses
octets et son sha256 AVANT d'être posée** : une fourniture de même nom **écrase sans trace**.
(e) **PARE-FEU** : aucune copie de substance au dépôt, arbre ET historique. **NE RENOMME JAMAIS UNE
PIÈCE POUR PASSER SOUS UN CONTRÔLE NOMINAL.**

# §7. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

**ITEM 1 — `R-23` AU FOND, par l'ouverture du corps de F5, voie (i).** Seul mouvement scientifique
armé, et il l'est depuis S18.

**AVANT TOUTE LECTURE : rédiger et DÉPOSER un cadrage gelé NEUF** sur `R-23` AU FOND — issues
pré-déclarées, critère de verdict écrit. `audit/F5-VOIE-I-CIBLES-GELEES.md` (S18) est **DÉFECTUEUSE
PAR PRÉMISSE FAUSSE**, reste **SCELLÉE et byte-intacte**, et **NE SERT PAS de cadrage**.

**ENVELOPPE — `audit/F5-ANTICIPATIONS-RESERVE.md`, sha256
`3200e69b24fc9edf1f552e2bb1c03f2797962b63c1eb898f63dbc9946ef19e75`.** Elle porte les anticipations
connues et le cadre déjà tranché autour de la cible. **NE L'OUVRE PAS AVANT D'AVOIR DÉPOSÉ TON
CADRAGE.** Ton cadrage **cite ce sha** ; après dépôt, tu l'ouvres, tu **re-mesures** son sha, tu le
confrontes, et tu classes chaque point en **CONFIRMATION D'ANTICIPATION** ou en **DIVERGENCE**.
Procédure : `audit/ENVELOPPE-ANTICIPATIONS-INSTRUCTION.md`. **L'ordre est vérifiable : le commit de
ton cadrage doit précéder tout usage du contenu de l'enveloppe.**

**ITEM 2 — GOUVERNANCE, non arbitré** : `G-1` (dette de fourniture `hors-KB/A/`, arbitrage (a) rendu
en S18, non exécutée) · `G-5c` · migration de `kb/` **bloquée sur G-4 volet 3** · volet de recalage
de la constitution (`kb/LC-CONST-V1` §2 périmé et scellé) · dette `M vacantes` sur
`LC-BETA-CONTROLE-DEPOT.py` · dette `instruments/concordance_mount.py` · **dette V97 : la condition
d'arrêt du boot n'a pas été exécutée depuis S14** · scission du §0-lite proposée non arbitrée · les
3 orphelines de la KB active · reports V96 §4.

**ITEM 3 — RESTES DE FOND, en dernier, INCHANGÉS** : audit froid incognito · plafond `T-b` / carte
shadow `T-a` · candidats genuine-dS armés non lus · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C`
plus étroit que son libellé · `p` libre / P-sélecteur · anti-circularité `K` · `§7quinquies` `K-B` ·
cadrage figé `37bc85e5` / gel amont `b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald · gap
résiduel `R1″ ∧ R2″ ∧ R4″`.

# §8. RÉSERVES QUI SE RECOPIENT — aucune ligne du périmètre n'est sans réserve

**CINQ** lignes (`B1` `B2` `B3` `B4` `S8`) sous **RÉSERVE PERMANENTE** de décalage
version-consommée / version-gradée · **DEUX** lignes (`S9` `S10`) sous **RÉSERVE ÉCRITE à cinq
points**. **5 + 2 = 7.** S'ajoute la **RÉSERVE DE VERSION sur `LC-00-INDEX`**. **Une ligne citée sans
sa réserve est INCOMPLÈTE.**

**La confrontation 4/4 au bit n'entame AUCUNE de ces réserves** : elle porte sur PDF-contre-OCR, la
réserve permanente sur publié-contre-préprint. Et *« aucune ligne n'est classée sur des octets
confrontables »* **reste vrai du classement rendu**, qui l'a été sur le canal OCR.

# §9. PÉRIMÈTRE — INCHANGÉ

S19 a produit de la **MÉTHODE** et **une confrontation d'octets**, aucun mouvement scientifique.
`{ A4 ; A2★ ; N }` **INCHANGÉ** · `[B]` = B-PAUVRE · `W2` = DÉLIMITATION, `A4` NON réfuté · `A2★`
décision ouverte, `C7` non levée · `D1` non clos, `D1c` INTACTE · `N` non fixé (≡ Λ, R-53 : 0/4) ·
`O₂` non construit · β **`T-b`, NON RÉSOLU, SEUL facteur d'`O₂` ouvert**, débloqué par P-8 ·
α = `C1-b` · `G3-a` non levé · nœud (i) INDÉTERMINÉ · Silo R **CLOS à 12/12** · **CCC non démontrée
NI réfutée.**

# §10. PRÉCÉDENTS S19, opposables, en plus de tous ceux de S8–S18 (note §7)

- **UNE CONSIGNE QUI RÉGULE L'ORDRE INTERNE DU PILOTE N'EST PAS UNE GARDE.**
- **UNE PIÈCE NON SCELLÉE N'A PAS BESOIN D'ÊTRE BYTE-INTACTE.**
- **UNE NOTE AUTOPORTANTE QUI SE CONTREDIT N'EST PAS AUTOPORTANTE.**
- **UN DISPOSITIF ANTI-FIT À LECTURE OBLIGATOIRE DEVIENT UN VECTEUR DE CONTAMINATION.**
- **UNE SURFACE SANS VERSION, SANS SHA ET SANS HISTORIQUE N'EST PAS UNE MÉMOIRE.**
- **SUR UNE TELLE SURFACE, UNE FOURNITURE DE MÊME NOM EST UNE OPÉRATION DESTRUCTRICE SANS TRACE.**
- **DEUX SURFACES DE MÊME NOM SANS CONTRÔLE DE CONCORDANCE DIVERGENT SANS QUE PERSONNE NE LE SACHE.**
- **UNE CONSIGNE DE RETRAIT SE DONNE PAR NOM DE FICHIER, JAMAIS PAR PROPRIÉTÉ.**
- **UNE QUESTION POSÉE À L'OPÉRATEUR SUR UN FAIT MESURABLE EST UN INSTRUMENT NON EMPLOYÉ.**
- **LA MASSE D'UN PROTOCOLE EST ELLE-MÊME UNE SOURCE D'ÉCARTS.**
- **UNE COÏNCIDENCE DE VALEURS SOUS DEUX INSTRUMENTS N'EST PAS UNE CONFIRMATION.**
- **UN VOCABULAIRE NE S'INTRODUIT PAS PAR L'USAGE.**
- **R-36 S'ÉTEND À TOUTE MESURE D'UNE PIÈCE SUR ELLE-MÊME, PAS SEULEMENT À SON SHA.**

# §11. DÉPÔT

Pas de token pour l'instant — **ceux de S19 sont RÉVOQUÉS**, et la révocation se **MESURE** par un
**401** sur `GET https://api.github.com/user`, elle ne se demande pas. **UN TOKEN PAR DÉPÔT**, et tu
me le demanderas **APRÈS** avoir annoncé **chemin + sha256 complet + message de commit, FICHIER PAR
FICHIER, RETRAITS COMPRIS**. Si je te le donne AVANT l'annonce, **fais l'annonce quand même** et
attends ma confirmation. **Une instruction de déposer N'EST PAS la confirmation d'une annonce.**
Push par **URL ÉPHÉMÈRE**, jamais `git remote set-url`. Après push : confrontation des sha déposés
aux sha annoncés **par `diff`, sur CLONE NEUF** ; puis token à **0** dans l'arbre, `.git/config`, les
messages de commit **ET le contenu de TOUS les blobs** (`git rev-list --objects --all`) ; puis
révocation mesurée. **Le message de commit ne s'enrichit pas d'un mot après l'annonce.**

Identité de commit : `LC-RACCORD pilote S20 <pilote-s20@lc-raccord.local>`.
**LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.**

---

**§6.4 — sentinelle terminale.** Cloner, mesurer, rejouer, confronter, classer, délimiter, arbitrer,
déposer, retirer, recaler, borner : aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre
quoi que ce soit. Un sha256 atteste des octets, jamais un titre, des auteurs, un DOI ni un grade.
Une confrontation 4/4 au bit atteste que les octets sont ceux du registre, jamais qu'un classement
rendu sur un autre canal était juste. Six correctifs de méthode ne rapprochent d'aucune physique.
**Cinq séances consécutives sans mouvement scientifique : S20 s'ouvre sur le seul geste qui en
serait un.** β `T-b`, non résolu, SEUL facteur d'`O₂` ouvert. **CCC n'est ni démontrée ni réfutée.**
