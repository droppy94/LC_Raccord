---
id: PROMPT-OUVERTURE-S21
titre: "Prompt d'ouverture S21. OUVERTURE EN DEUX MESSAGES (correctif nº1, tenu 1/1 en S20). La mesure d'ouverture est désormais TRONQUÉE À 72 CARACTÈRES — correctif nº3 REFAIT : on ne cache pas par relocalisation, on borne la projection."
codename: LC-RACCORD
type: "prompt d'ouverture — HORS base scellée, OPÉRATIONNEL. Il ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
---

# §0. À L'OPÉRATEUR — envoie ceci en DEUX messages

**MESSAGE 1, à envoyer SEUL.** Ces trois lignes ne portent **aucune valeur attendue**.

> Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique.
> Rends la sortie BRUTE de `git status` et de `git log --format='%h %<(72,trunc)%s' -14`,
> sans commentaire. Puis arrête-toi et attends.

**MESSAGE 2** : l'URL de la présente pièce, une fois le message 1 rendu.

*Pourquoi la troncature.* En S20, `git log --oneline -14` a livré **8 marqueurs sur 8** du contenu
que l'enveloppe anti-fit était censée retenir — parce que **toute la substance est dans la ligne de
sujet** (31 189 caractères de sujet contre 4 911 de corps, 11 commits sur 14 sans corps du tout).
La projection tronquée rend **34 676 → 1 190 caractères, facteur 29**, sur l'historique existant,
**sans rien réécrire et sans rien cacher** : `git log --format=%B <sha>` restitue tout, à la
demande, **après** dépôt du cadrage. Voir `audit/HISTORIQUE-PROJECTION-INSTRUCTION.md`.

# §1. MESURE — aucun attendu ici, c'est voulu

1. Clone sous un **chemin unique**. `git status` : arbre propre.
2. `git log --format='%h %<(72,trunc)%s' -14`. **Rends la sortie brute.**
3. `git rev-parse HEAD` et `git log -1 --format=%s | cut -c1-72`.
4. **NE CITE AUCUNE VALEUR ATTENDUE AVANT D'AVOIR RENDU CES SORTIES.**

# §2. CONFRONTATION

**HEAD ATTENDU** : le commit dont le sujet commence par « **Reprise S20** ». Ses parents remontent
par `6ecff56`, `7febb5f`, `85b1a0e`, `6cbc4d3`, `b8c6700`, `a8f3923`, `0a102b7`, `602c828`,
`dc8ca29`.

Le sha **n'est PAS écrit ici** : ce prompt est déposé DANS lui (**R-36**). **NE PRÉSUME PAS QU'IL
EST HEAD** — un commit postérieur peut s'être intercalé (arrivé en S17). En S18, S19 et S20 la
chaîne démarrait à HEAD : **cela ne prouve rien pour S21.** Confronte, **NOMME l'écart s'il y en a
un, NE CORRIGE RIEN D'OFFICE.**

# §3. La note de reprise — UNIQUE, AUTOPORTANTE, OPÉRATIONNELLE

`NOTE-REPRISE-GIT-S20.md`, à la racine. Elle **REMPLACE** `NOTE-REPRISE-GIT-S19.md`, retirée au même
commit et conservée dans l'historique. **LA RACINE PORTE 4 FICHIERS** ; une cinquième pièce est un
écart à nommer. UNE SEULE note de la série `GIT-S<n>` ; `kb/NOTE-REPRISE-V96.md` est d'une autre
série, **ce n'est PAS un écart**.

Pièce **OPÉRATIONNELLE** : un défaut mesuré sur elle **se corrige EN PLACE**, avec bump de
`version:`, entrée au champ `recalages:`, §§ nommés au commit. **Pas d'`AMENDEMENT-<n>`.** Gels,
cibles gelées, verdicts et rapports rendus restent **SCELLÉS et byte-intacts**.

**ARBITRAGE ATTENDU DE TOI, EN OUVERTURE** : le §7 de la note porte les précédents S8–S19 **par
coordonnée git + sha256** au lieu de les recopier, et le déclare comme **dérogation à
l'autoportance**. Motif mesuré : la masse du protocole est elle-même une source d'écarts (précédent
S19 nº10), et six correctifs S19 ont **déplacé** l'appareil sans l'alléger. **Tranche : recopie
intégrale, ou renvoi mesuré.**

# §4. §0-lite — attendus, chacun avec sa commande

`ls instruments/*.py | wc -l` **34** · `ls instruments/archives-scelees/*.py | wc -l` **76** ·
`ls audit/ | wc -l` **73** (72 fichiers + 1 répertoire) ·
`ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l` **8** · `ls kb/*.md | wc -l` **215** ·
`ls hors-KB/B/ | wc -l` **4** · `ls -p | grep -v /` **4**. `sources/` et `manifest/` **HORS COMPTE**.
`hors-KB/A/` **ABSENT par construction**.

`inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** (réécrit sa date : `git checkout`) ·
`run_sceau.py verif_paquet_propre` → sha8 **`051e2833`**, rc 0 · **12 redémonstrations : 271/271
PASS + 101 consignations, 12/12 rc 0 — INCHANGÉ depuis S9.** Décomposition (multiensemble) :
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` · `5+5+6+6+8+7+3+10+14+10+8+19 = 101`. Variantes qui
comptent : `redemo_R4_CT_b.py`, `redemo_R5_reductions_b.py`. Motif :
`^[[:space:]]*\[?PASS\]?` — quatre scripts impriment **sans crochets**.
Cinq rejeux hors compte : `harnais_R9` 6/6 · `harnais_R11` 7/7 + 0 vacante · `verif_B_tracteur`
rc 0 · `LC-WORK-GEN-PAQUET-v2_1 --self-test` 6/6 · `LC-BETA-CONTROLE-DEPOT --self-test` 8/8,
**dette de vacuité OUVERTE**.

**Intrants `sources/` 3/3** : `2312_12498v2.pdf` 1 895 152 o `04d9b4f4` · `2409_10595v2.pdf`
2 332 898 o `27a94980` · `2503_19957v1.pdf` 910 410 o `113ab4a2`.

**KB ACTIVE — AUCUN sha256 N'EST ATTENDU, ET C'EST DÉFINITIF.** S20 a mesuré 0/4 contre l'attendu de
S19 : les quatre `.pdf` sont des **ZIP** OCR, `mtime` époque zéro ⟹ **la surface est
re-matérialisée par session**. Elle est un **canal de LECTURE**, jamais de hachage. Elle porte
**11 fichiers** au dernier relevé (7 + les 4 registres recalés). **N'en fais pas un attendu.**

# §5. Rends-moi le §0-lite compressé, tout écart décomposé, AVANT de poursuivre.

`audit/S0LITE-IMPRESSION-INSTRUCTION.md` (12 scripts **tous exécutés**, restitution compressée,
clause de dépliement au premier écart) et `audit/S0LITE-INSTRUMENTS-INSTRUCTION.md` (**tout attendu
porte sa commande ; un nombre sans son instrument n'est pas opposable**). **Défaut d'âge connu de
cette seconde pièce : sa table porte `62` pour `ls audit/`, valeur périmée. Pièce OPÉRATIONNELLE,
recalable en place.**

**GARDES D'ENVIRONNEMENT** : `rc` se capture **AVANT tout pipe** · `grep -c` compte des **LIGNES** ·
`|| true` quand le zéro est attendu · **BORNE TES MOTIFS** — un `grep` non borné sur `kb/` coûte
~15 000 tokens, écart S20 · **`xxd` ABSENT**, `python3` ou `od` · **`bash -c`** requis pour
`diff <(…)` · `arxiv.org` **hors** allowlist, `github.com` et `api.github.com` **dedans** · les
outils web rendent du **TEXTE, jamais des octets hachables**.

# §6. CE QUE TU N'AS PLUS À DEMANDER

(a) `LC-BETA-PAQUET.zip` et journal V94 **SOLDÉS** ; les octets du journal **ne se déposent pas**.
(b) Les 8 pièces `LC-BETA-*` **mentent par âge**, ce n'est **pas** à corriger.
(c) `LC-00-INDEX` déposé en S18 (`audit/00_index.md`, v1.78) — **RÉSERVE PERMANENTE** de version.
(d) **`R-23` est SUSPENDUE À `OB`**, tranché en S20, verdict `07225d4d…` + amendement. Ne la rejuge
pas ; le mot `soldée` ne subsiste qu'en **changelog**, où il dit vrai.
(e) **PARE-FEU** : aucune copie de substance au dépôt, arbre ET historique. **NE RENOMME JAMAIS UNE
PIÈCE POUR PASSER SOUS UN CONTRÔLE NOMINAL.**

# §7. ORDRE DE TRAVAIL — chacun sur GO séparé

**ITEM 0 — l'arbitrage du §3** (recopie intégrale ou renvoi mesuré). Deux minutes, il conditionne la
forme de la note S21.

**ITEM 1 — DETTE DE FOURNITURE, échafaudage F5.** Six pièces listées au §10 de la note, avec octets
et sha, présentes chez l'opérateur, **absentes du dépôt**. Les déposer déplace les 215 scellés et le
manifeste `v2.124`. **Arbitrage opérateur, puis exécution.** C'est la dette la plus mûre : elle a
une liste, des sha, et un motif — `LC-AUDIT-LOG-F5` porte deux réserves sur F5 qui n'existent nulle
part au dépôt.

**ITEM 2 — GOUVERNANCE**, non arbitrés : `G-1` · `G-5c` · migration `kb/` sur `G-4` volet 3 ·
recalage de `kb/LC-CONST-V1` §2 · dette `M vacantes` · `concordance_mount.py` · **dette V97, boot
non exécuté depuis S14** · scission du §0-lite · 3 orphelines de la KB active · reports V96 §4 ·
**front-matter YAML invalide sur trois registres** · **le manifeste ne cite que 7 noms sur 215.**

**ITEM 3 — RESTES DE FOND, en dernier** : audit froid incognito · plafond `T-b` / carte shadow
`T-a` · candidats genuine-dS armés non lus · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C` plus
étroit que son libellé · `p` libre / P-sélecteur · anti-circularité `K` · `§7quinquies` `K-B` ·
cadrage figé `37bc85e5` / gel amont `b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald · gap
résiduel `R1″ ∧ R2″ ∧ R4″`.

**β `T-b` reste le SEUL facteur d'`O₂` ouvert, et `O₂` commande à la fois `D1` et la falsifiabilité.
Aucun ITEM ci-dessus ne l'entame.**

# §8. DÉPÔT — R-55

Pas de token pour l'instant ; **ceux de S20 sont à révoquer, et la révocation se MESURE** par un
**401** sur `GET https://api.github.com/user` — elle ne se demande pas. **UN TOKEN PAR DÉPÔT**,
demandé **APRÈS** annonce de **chemin + sha256 complet + message de commit, FICHIER PAR FICHIER,
RETRAITS COMPRIS**. Token donné avant l'annonce : **fais l'annonce quand même et attends**. *Une
instruction de déposer n'est pas la confirmation d'une annonce.* Push par **URL ÉPHÉMÈRE**, jamais
`git remote set-url`. Après push : `diff` sur **clone neuf** ; token à **0** dans l'arbre,
`.git/config`, les messages **et le contenu de TOUS les blobs** ; puis révocation mesurée.
**Le message de commit ne s'enrichit pas d'un mot après l'annonce.**

**NEUF, correctif nº3 volet B** : **le SUJET du commit est ≤ 72 caractères et purement désignatif ;
toute la substance va dans le CORPS.** Premier dépôt conforme : celui qui porte la présente pièce.

**UNE TABLE DE FOURNITURE NE SE PUBLIE QU'APRÈS QUE LA SOURCE EST POUSSÉE** et son sha re-mesuré sur
clone neuf — écart S20, le plus coûteux. **Et la confrontation d'une fourniture à la KB active se
fait APRÈS la pose, sur le mount, par le pilote** : l'annonce d'avant ne voit pas un renommage qui
n'a pas eu lieu.

Identité : `LC-RACCORD pilote S21 <pilote-s21@lc-raccord.local>`.
**LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.**

---

**§6.4 — sentinelle terminale.** Cloner, mesurer, rejouer, confronter, classer, délimiter, arbitrer,
déposer, retirer, recaler, borner, requalifier une dette : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit. S20 a requalifié `R-23` de *soldée* en *suspendue à `OB`* —
**une dette qui change de nom reste une dette**, et `W³` est toujours **SANS VALEUR**. `O₂` n'est
pas construite. β `T-b`, non résolu, **SEUL facteur d'`O₂` ouvert**. **CCC n'est ni démontrée ni
réfutée.**
