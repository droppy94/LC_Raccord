---
id: LC-PROMPT-OUVERTURE-S22
titre: "Ouverture S22 — pièce UNIQUE de reprise. Remplace la paire prompt + note de reprise, fusionnée en S21."
codename: LC-RACCORD
type: "pièce de reprise — HORS base scellée, OPÉRATIONNELLE. Elle ne scelle rien, ne compte rien, ne démontre rien."
version: 1.0
langue: fr
date: 2026-07-26
session: S21
depend_de: [CORPUS]
---

# §0. À L'OPÉRATEUR — envoie ceci en DEUX messages

**MESSAGE 1, seul.** Aucune valeur attendue ici, c'est voulu.

> Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique.
> Rends la sortie BRUTE de `git status` et de `git log --format='%h %<(72,trunc)%s' -8`,
> sans commentaire. Puis arrête-toi et attends.

**MESSAGE 2** : l'URL de la présente pièce, une fois le message 1 rendu.

**NEUF EN S21 — pièce UNIQUE.** Cette pièce remplace la paire
`PROMPT-OUVERTURE-S<n>` + `NOTE-REPRISE-GIT-S<n>`, qui se recouvraient. Motif :
S21 a retiré 412 802 caractères de redondance du corpus ; garder deux fichiers
de reprise qui se répètent aurait été la même maladie. La racine porte
**3 fichiers**.

# §1. CE QU'IL FAUT SAVOIR AVANT DE MESURER

**HEAD attendu** : le commit portant cette pièce. Le sha n'est pas écrit ici —
elle est déposée dedans. **Ne présume pas qu'il est HEAD** : un commit postérieur
peut s'être intercalé. Confronte, **nomme l'écart, ne corrige rien d'office**.

**Précédents S8–S21** : portés par **renvoi mesuré**, arbitrage rendu en S21.
Ils ne se recopient pas.

| pièce retirée | commit | sha256 |
|---|---|---|
| `NOTE-REPRISE-GIT-S20.md` | `d24477f` | `3cfada1ed1947925d88719959de97929c8a54b1ff6723c99d218e24bac6298d7` |
| `PROMPT-OUVERTURE-S21.md` | `d24477f` | `840781a1bdc8ed244b953c4d738c5c5c6f6779483c36e160ab50bb7e7543ed75` |

Restitution : `git show d24477f:NOTE-REPRISE-GIT-S20.md`. Le §7 de cette pièce
porte les titres opposables S8–S19 et renvoie lui-même à `6cbc4d3`.

# §2. §0-lite — attendus, chacun avec sa commande

`ls instruments/*.py | wc -l` **35** · `ls instruments/archives-scelees/*.py | wc -l` **76** ·
`ls audit/ | wc -l` **78** (77 fichiers + 1 répertoire) ·
`ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l` **8** · `ls kb/*.md | wc -l` **215** ·
`ls hors-KB/B/ | wc -l` **4** · `ls -p | grep -v /` **3**.
`sources/` et `manifest/` **HORS COMPTE** · `hors-KB/A/` **ABSENT par construction**.

`inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** (réécrit sa date :
`git checkout`) · `run_sceau.py verif_paquet_propre` → sha8 **`051e2833`**, rc 0 ·
**12 redémonstrations : 271/271 PASS + 101 consignations, 12/12 rc 0 — INCHANGÉ
depuis S9.** Décomposition : `35+17+16+16+12+11+6+21+40+45+16+36 = 271` ·
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`. Variantes qui comptent : `redemo_R4_CT_b.py`,
`redemo_R5_reductions_b.py`. Motif : `^[[:space:]]*\[?PASS\]?` — quatre scripts
impriment **sans crochets**.

Cinq rejeux hors compte : `harnais_R9` 6/6 · `harnais_R11` 7/7 + 0 vacante ·
`verif_B_tracteur` rc 0 · `LC-WORK-GEN-PAQUET-v2_1 --self-test` 6/6 ·
`LC-BETA-CONTROLE-DEPOT --self-test` 8/8, **dette de vacuité OUVERTE**.

**Intrants `sources/` 3/3** : `2312_12498v2.pdf` 1 895 152 o `04d9b4f4` ·
`2409_10595v2.pdf` 2 332 898 o `27a94980` · `2503_19957v1.pdf` 910 410 o `113ab4a2`.

**Instrument neuf** : `python3 instruments/audit_identifiants.py` →
**272 id uniques · 0 mal formé · 0 collision · 35 sans front-matter · 2 `parent:`**.
`--self-test` → **16/16**.

Régime d'impression : `audit/S0LITE-IMPRESSION-INSTRUCTION.md` (12 scripts tous
exécutés, restitution compressée, dépliement au premier écart) et
`audit/S0LITE-INSTRUMENTS-INSTRUCTION.md` v1.1.

**GARDES** : `rc` se capture **AVANT tout pipe** · `grep -c` compte des **LIGNES** ·
`|| true` quand le zéro est attendu · **BORNE TES MOTIFS** · **`xxd` ABSENT**,
`python3` ou `od` · `arxiv.org` **hors** allowlist, `github.com` **dedans**.

# §3. CE QUE S21 A FAIT — cinq dépôts

| commit | objet |
|---|---|
| `bcaaaee` | apuration du front-matter — 9 pièces, 305 748 car. de journal déplacés en archive |
| `c9c6a73` | `instruments/audit_identifiants.py`, auto-test mordant 16/16 |
| `5483e25` | `audit/00_index.md` requalifié en instantané S18, collision d'`id:` levée |
| `59b8179` | `id:` assignés aux notes BORD-EON 06 et 07 |
| `d24477f` | `audit/CONVENTION-DEPENDANCES.md` |

**412 802 caractères** de journal de versions ne se rechargent plus à l'ouverture.
Aucun octet scellé touché. Tous les dépôts confrontés sur clone neuf, sha à sha.

# §4. RÈGLES ARBITRÉES EN S21 — opposables

1. **Amont seul, aval calculé.** Une pièce déclare `depend_de:`, jamais ce qui
   dépend d'elle. Clé = `id:`. Détail : `audit/CONVENTION-DEPENDANCES.md`.
2. **Un recalage de métadonnée ne fait pas avancer `version:`** ; il se consigne
   au champ `recalages:`, daté et motivé.
3. **Renvoi mesuré** plutôt que recopie pour les précédents antérieurs, à
   condition que la coordonnée résolve — vérifiée à chaque reprise.
4. **Trois surfaces, trois régimes.** `git` porte l'identité — c'est la seule où
   un sha vaut quelque chose. Le **mount** est un canal de **lecture** : il
   refabrique ce qu'il sert (les `.pdf` y sont des ZIP d'images, `mtime` 1980),
   **aucun sha n'y est attendu, et c'est définitif** ; on y vérifie **par lecture**
   du champ `version:`. Le **Drive** est prohibé pendant une période de gel —
   **interdiction, non barrière** : son échec est silencieux.
5. **Drive, versions** : `modifiedTime` fait foi, l'indice `(1)`, `(2)` est le
   raccourci lisible. **Taille identique au précédent = redépôt, pas version.**
6. **Un gel se prouve par le push**, horodaté côté serveur — ni la date du
   fichier ni celle du commit, que le rédacteur choisit. Les données sous test ne
   sont pas dans le mount pendant qu'on gèle un critère sur elles.
7. **Solde nul** : ajouter une règle exige d'en retirer ou d'en fusionner une.

# §5. PROCHAIN GESTE, puis le reste

**GESTE 1 — l'instrument de graphe.** Il n'a plus qu'à implémenter le §6 de la
convention : cycles · fermeture aval · **arêtes pendantes** · **propagation
impossible** (aval scellé ⟹ amendement daté, pas mise à jour) · couverture.
Auto-test mordant obligatoire, avec batterie de mutation — en S21, un auto-test
à 14/14 s'est révélé vacant sur un contrôle, et c'est le mutant qui l'a dit.

**GESTE 2 — le registre des scellées**, `audit/REGISTRE-DEPENDANCES-SCELLEES.md`,
35 pièces. Demande de lire chaque gel pour établir ses dépendances : c'est du
travail de fond, pas de l'hygiène.

**GESTE 3 — annotation de la branche active**, puis champ obligatoire à la touche.

**DETTES OUVERTES, non entamées** : fourniture F5 (6 pièces, §10 de la note S20) ·
`NOTE-BORD-EON-01…05` et `LC-WORK-REPRISE-POST-G3T-1…4`, qui existent sur le
Drive et n'ont **jamais été déposées** · copies divergentes du Drive sous un même
numéro de version · gouvernance non arbitrée (`G-1`, `G-5c`, dette V97, front-matter
YAML invalide sur trois registres, manifeste qui ne cite que 7 noms sur 215).

**FOND, en dernier et toujours pas entamé** : plafond `T-b` / carte shadow `T-a` ·
routes α/δ · DESI DR2 · `Δ-C` · anti-circularité `K` · gap `R1″ ∧ R2″ ∧ R4″`.

# §6. DÉPÔT — R-55

Annonce **AVANT** le token : **chemin + sha256 complet + message de commit,
FICHIER PAR FICHIER, RETRAITS COMPRIS**. Token donné avant l'annonce : **fais
l'annonce quand même et attends**. *Une instruction de déposer n'est pas la
confirmation d'une annonce.* Push par **URL ÉPHÉMÈRE**, jamais
`git remote set-url`. Après push : `diff` sur **clone neuf** ; token à **0** dans
l'arbre, `.git/config`, les messages **et tous les blobs** ; puis révocation.

**La révocation se DEMANDE et se MESURE.** Mesuré en S21 :
`DELETE /personal-access-tokens/self` rend **404** — le pilote ne peut pas
révoquer un PAT fine-grained. Il mesure le **401** sur `GET https://api.github.com/user`
après que l'opérateur a révoqué. **UN TOKEN PAR DÉPÔT.**

**Le sujet du commit est ≤ 72 caractères et purement désignatif ; la substance va
dans le CORPS.** Le message ne s'enrichit pas d'un mot après l'annonce.

Identité : `LC-RACCORD pilote S22 <pilote-s22@lc-raccord.local>`.
**LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.**

---

**§6.4 — sentinelle terminale.** Cloner, mesurer, apurer, requalifier, conventionner,
déposer : aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que
ce soit. S21 a retiré de la redondance et rangé un espace de noms — **elle n'a pas
avancé d'un pas sur la question scientifique**. `R-23` reste **suspendue à `OB`**.
`W³` est toujours **SANS VALEUR**. `O₂` n'est pas construite. β `T-b`, non résolu,
**SEUL facteur d'`O₂` ouvert**, et aucun geste du §5 ne l'entame.
**CCC n'est ni démontrée ni réfutée.**
