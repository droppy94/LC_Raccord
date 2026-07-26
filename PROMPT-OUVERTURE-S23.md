---
id: LC-PROMPT-OUVERTURE-S23
titre: "Ouverture S23 — pièce UNIQUE de reprise. Remplace PROMPT-OUVERTURE-S22 par swap d'unicité. Premier §0-lite sous régime B (scission), instrument non écrit : dette GESTE 0."
codename: LC-RACCORD
type: "pièce de reprise — HORS base scellée, OPÉRATIONNELLE. Elle ne scelle rien, ne compte rien, ne démontre rien."
version: 1.0
langue: fr
date: 2026-07-26
session: S22
depend_de: [CORPUS]
---

# §0. À L'OPÉRATEUR — envoie ceci en DEUX messages

**MESSAGE 1, seul.** Aucune valeur attendue ici, c'est voulu.

> Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique.
> Rends la sortie BRUTE de `git status` et de `git log --format='%h %<(72,trunc)%s' -8`,
> sans commentaire. Puis arrête-toi et attends.

**MESSAGE 2** : l'URL de la présente pièce **et le TIRAGE** — deux noms parmi les
douze redémonstrations, choisis par toi et **non annoncés d'avance**.

**Le tirage de S22 (`redemo_R6_nongauss`, `redemo_R8_A2star`) est BRÛLÉ** : il a été
rendu après que le pilote eut exécuté les douze et imprimé leurs comptes. Il ne se
rejoue pas. **Tire deux autres noms.** Un pilote qui connaît la réponse ne se calibre
pas — c'est tout l'objet du dispositif.

# §1. CE QU'IL FAUT SAVOIR AVANT DE MESURER

**HEAD attendu** : `5399961`, le commit portant cette pièce sera postérieur.
**Ne présume pas** qu'il est HEAD : confronte, **nomme l'écart, ne corrige rien
d'office**. Vérifie aussi que le sha est la **pointe de `main`** et regarde
`git ls-remote --heads` : une branche `front-pq` subsiste au distant (ancêtre,
0 commit en avance, 68 en retard — sans apport, nommée pour qu'on cesse de la
redécouvrir).

**Précédents S8–S22** : portés par **renvoi mesuré**, jamais recopiés.

| pièce retirée | commit | sha256 |
|---|---|---|
| `PROMPT-OUVERTURE-S22.md` | `5399961` | `47dbac40c6153a64839ab69e68708a284ddbd66ff49bff06512027088856cd6f` |

Restitution : `git show 5399961:PROMPT-OUVERTURE-S22.md`. Son §1 porte lui-même le
renvoi vers `d24477f` (S20/S21), qui renvoie à `6cbc4d3` (S8–S19). **La chaîne se
vérifie à chaque reprise** (règle 3) ; si une coordonnée ne résout plus, dis-le.

# §2. §0-lite — RÉGIME B, arbitré en S22

**Ce qui a changé.** Les douze redémonstrations ne se rejouent plus intégralement à
chaque ouverture. Motif mesuré en S22 : leur sortie intégrale fait **543 lignes /
68 978 caractères**, contre **543 / 68 966** mesurées en S18 — **douze caractères
d'écart en trois sessions**. Un contrôle qui rend les mêmes octets ne détecte rien du
corpus ; en dix sessions il n'a détecté que le pilote. Ce qui mord sur le fond, c'est
l'**audit froid** (cf. §5).

**GESTE 0, dette ouverte : `verif_S0lite.py` n'est PAS écrit.** Tant qu'il ne l'est
pas, le régime B n'est pas opérationnel et se conduit ainsi :

1. les **sept comptes de structure** et les **sceaux** ci-dessous se rejouent, tous ;
2. les **deux scripts tirés** s'exécutent et se comptent **à la main**, instrument
   déclaré ;
3. les **dix autres se déclarent « non rejoués », datés**. Ils ne se déduisent
   **jamais** d'un rendu court (`S0LITE-IMPRESSION-INSTRUCTION` §4). Écrire
   « 271/271 » sans les avoir exécutés, ce n'est pas mesurer, c'est **réciter cette
   pièce** — et un pilote neuf est très doué pour réciter.

**Comptes de structure** — chaque attendu porte sa commande.
`ls instruments/*.py | wc -l` **35** · `ls instruments/archives-scelees/*.py | wc -l` **76** ·
`ls audit/ | wc -l` **78** (77 fichiers + 1 répertoire) ·
`ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l` **8** · `ls kb/*.md | wc -l` **215** ·
`ls hors-KB/B/ | wc -l` **4** · `ls -p | grep -v /` **3**.
`sources/` et `manifest/` **HORS COMPTE** · `hors-KB/A/` **ABSENT par construction**.

**Sceaux** · `inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT**, rc 0 (réécrit
sa date : `git checkout`) · `run_sceau.py verif_paquet_propre` → sha8 **`051e2833`**, rc 0.

**Espace des identifiants** · `python3 instruments/audit_identifiants.py` →
**306 pièces · 271 id uniques · 0 mal formé · 0 collision · 35 sans front-matter ·
2 `parent:`**. `--self-test` → **16/16**.

> **RECALAGE S22, à ne pas re-commettre.** Le §2 de `PROMPT-OUVERTURE-S22`
> **et le corps du commit `ca5993c`** portaient **272**. La valeur juste après
> `ca5993c` est **271** : ce commit retire deux pièces à `id:` et en ajoute une, soit
> −1. L'attendu avait été recalé sur trois de ses quatre termes et pas sur celui-là.
> **Le corps de `ca5993c` reste faux et n'est pas corrigeable** (un message de commit
> ne se réécrit pas) : il est nommé ici, une fois pour toutes.

**Redémonstrations, valeurs de référence** — **271 PASS + 101 consignations, 12/12 rc 0,
INCHANGÉ depuis S9.** Décomposition : `35+17+16+16+12+11+6+21+40+45+16+36 = 271` ·
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`. **L'ordre de cette décomposition n'est PAS
R-1…R-12** — le présumer produit dix faux écarts (mesuré, S22). C'est l'appariement
`(PASS, CONSIGNATION)` script par script qui l'établit, non le total. Variantes qui
comptent : `redemo_R4_CT_b.py`, `redemo_R5_reductions_b.py`. Motif :
`^[[:space:]]*\[?PASS\]?` — quatre scripts impriment **sans crochets**.

**Cinq rejeux hors compte** : `harnais_R9` 6/6 · `harnais_R11` 7/7 + 0 vacante ·
`verif_B_tracteur` rc 0 · `LC-WORK-GEN-PAQUET-v2_1 --self-test` 6/6 ·
`LC-BETA-CONTROLE-DEPOT --self-test` 8/8, **dette de vacuité OUVERTE**.

**Intrants `sources/` 3/3** : `2312_12498v2.pdf` 1 895 152 o `04d9b4f4` ·
`2409_10595v2.pdf` 2 332 898 o `27a94980` · `2503_19957v1.pdf` 910 410 o `113ab4a2`.

**GARDES** : `rc` se capture **AVANT tout pipe** · `grep -c` compte des **LIGNES**
(`AUD.md` porte des lignes de 4 731 caractères : `G3` y est sur 22 lignes et
**114 occurrences**) · `|| true` quand le zéro est attendu · **BORNE TES MOTIFS** ·
**`xxd` ABSENT**, `python3` ou `od` · **`arxiv.org` HORS allowlist**, `github.com`
dedans — *tout front fetch-gated est inexécutable ici*.

# §3. CE QUE S22 A FAIT — un dépôt, deux audits froids

| commit | objet |
|---|---|
| `5399961` | surfaces et régimes absorbés dans `TOPOLOGIE-DEPOTS` v1.1 ; §4 passe de 7 à 6 règles |

**Deux passes d'audit froid**, instance incognito séparée, paquet sans zone-verdict.
Elles ont corrigé le pilote **deux fois sur le fond** et il faut le lire comme un
résultat du dispositif, pas comme un incident.

**Un dépôt annoncé puis RETIRÉ.** Le pilote allait déposer une entrée `recalages:`
dans `kb/LC-WORK-CADRAGE-C1-ADMISSIBILITE.md` pour « consigner » son gel R-36. Or le
sha256 de ce fichier **EST** le gel — `b6fbb703`, cité par **13 porteurs**, dont un
qui écrit « INTACT, **NON re-gelé** ». Le patch aurait détruit le gel qu'il prétendait
consigner. **Cause : le pilote avait ce sha sous les yeux et n'a jamais fait la
recherche inverse.** D'où la garde du §6.

# §4. RÈGLES ARBITRÉES S21–S22 — opposables, SIX

1. **Amont seul, aval calculé.** Une pièce déclare `depend_de:`, jamais ce qui dépend
   d'elle. Clé = `id:`. Détail : `audit/CONVENTION-DEPENDANCES.md`.
2. **Un recalage de métadonnée ne fait pas avancer `version:`** ; il se consigne au
   champ `recalages:`, daté et motivé. *Substance ⟹ `version:` avance.*
3. **Renvoi mesuré** plutôt que recopie, à condition que la coordonnée résolve —
   vérifiée à chaque reprise.
4. **Surfaces et régimes** : `audit/TOPOLOGIE-DEPOTS-INSTRUCTION` v1.1, §1 et §1bis.
   Renvoi mesuré, non recopie. Six dépôts ; `KB active /mnt/project ≡ mount` ; Drive
   **en voie d'abandon**, condition de retrait opposable ; réserve §1ter.
5. **Un gel se prouve par le push**, horodaté côté serveur — ni la date du fichier ni
   celle du commit. Les données sous test ne sont pas dans le mount pendant qu'on gèle
   un critère sur elles.
6. **Solde nul** : ajouter une règle exige d'en retirer ou d'en fusionner une.

# §5. PROCHAIN GESTE — ordre revu par la mesure

**L'AUDIT FROID EST LA MÉTHODE** (arbitrage opérateur S22 ; c'est une réaffirmation,
`LC-WORK-CADRAGE-C1-ADMISSIBILITE` §6 la portait déjà : *pilote disqualifié pour la
substance ; instance incognito séparée, conversation distincte ; paquet sans
zone-verdict ; incognito souverain*). **Régler pour la passe aveugle : conversation
neuve, HORS projet** (le mount porte un état distinct), **exécution de code activée
avec réseau**, aucune précision de l'opérateur dans le fil.

**GESTE 0 — `verif_S0lite.py`** (comptes, sha, `rc`, totaux) + **fusion** de
`S0LITE-IMPRESSION-INSTRUCTION` et `S0LITE-INSTRUMENTS-INSTRUCTION`, qui se recouvrent
et dont la table de référence de la seconde est fausse sur trois lignes (`34`/`77`/`4`
contre `35`/`78`/`3`). Rend le régime B opérationnel.

**GESTE A — réparer `m4 VACANT`.** Seul défaut de propagation **établi** du lot G3 :
`kb/LC-D-G3-ADM-IMPORTS.md` (5 occurrences, l. 3, 6, 10, 175, 185) et
`kb/LC-D-G3-GAP-STDEF.md` (l. 109) affirment encore la réserve `m4` vacante, alors que
`LC-D-G3-M4-CHAINON` v1.1 et `LC-D-G3-ADMISSIBILITE` v1.5 l'ont **levée le 2026-07-06**.
Les deux sont éditables et déclarent l'amont. *`LC-WORK-CADRAGE-G3-M4-CHAINON` porte
la même phrase et n'est PAS un défaut : cadrage gelé = propagation impossible.*

**GESTE C — arbitrer règle 2 ↔ lecture du mount.** `bcaaaee` a fait avancer quatre
`version:` (`02_programme`, `04_references`, `AUD`, `IDX`) pour un déménagement de
journal, sans employer `recalages:` — champ que **4 fichiers** portent dans tout le
dépôt. Or la règle 4 fait vérifier le mount **par lecture de `version:`**. Réserve
gravée, **nommée non levée**, à `TOPOLOGIE-DEPOTS` §1ter.

**GESTE 1 — À RE-SPÉCIFIER OU ABANDONNER.** L'instrument de graphe viserait
`depend_de:`, déclaré par **2 fichiers réels sur 306** ; l'usage de fait est
`prerequis_kb:`, **165 fichiers, 1 366 arêtes, 158 pendantes, 84 cibles distinctes**.
La convention absorbe `parent:` (2 pièces) et ne dit **rien** des 165. Le construire
en l'état instrumenterait un champ que personne ne renseigne.

**GESTE 2** — `audit/REGISTRE-DEPENDANCES-SCELLEES.md` est **absent** : les 35 pièces
scellées n'ont aucun lieu où déclarer leur amont.

**PIÈCES FIGÉES PAR CONSTRUCTION — quatrième catégorie, découverte en S22.** Un statut
peut être périmé **nécessairement**, sans négligence, parce que le recaler détruirait
le gel dont il est la contrepartie. Ne pas éditer ; **amender par pièce datée externe**
(précédent : `LC-WORK-AMENDEMENT-R7-C1-FONCTION-SDS`). Concernées :
`LC-WORK-CADRAGE-C1-ADMISSIBILITE` (gel `b6fbb703` ; son `titre:` dit « GELÉ », son
`statut:` dit « candidat au gel » ; elle ignore son propre gel) et
`LC-D-G3-ADMISSIBILITE` v1.6 (gel `f5a770e7` ; `titre:`, `tags:`, `tags_epistemiques:`
et le chapeau restés en v1.4 alors que le corps porte le patch v1.5 — coût non consigné
de la méthode « PATCH ADDITIF »).

**INDÉTERMINÉ PAR DÉFAUT DE RÉFÉRENCE, non par défaut de mesure** : « LOT UNIQUE DE
RÉSOLUTION » et « décision plafond opérateur » n'ont **qu'une occurrence chacun** dans
tout le dépôt — celle qui les met en question. Aucune pièce n'énumère le lot ni ne
consigne la décision. **Ne pas ré-auditer sans avoir d'abord nommé la composition du
lot, ou déclaré qu'elle est inconnue.** Corollaire mesuré : « KB au plafond » est
**faux** depuis v2.74 — 180 porteurs contre un plafond historique de 242.

**DETTES OUVERTES, non entamées** : fourniture F5 (6 pièces) · `NOTE-BORD-EON-01…05` et
`LC-WORK-REPRISE-POST-G3T-1…4`, sur le Drive, **jamais déposées** — désormais adossées
à la condition de retrait du Drive (règle 4) · copies divergentes · gouvernance (`G-1`,
`G-5c`, dette V97, front-matter YAML invalide sur trois registres, manifeste citant 7
noms sur 215) · les **onze défauts `D-01..D-11`** de `LC-D-G3-KPS-KB` v0.1 (2026-07-17),
correctif `D-01` dû : ils ne sont pas perdus (6 porteurs, dont `NOTE-REPRISE-V96` et le
manifeste) mais **absents du registre de la série S** — dette de migration V→S.
*Non-défaut, réglé : `IDX_v211.md` porte `version: 2.13` ; la clé opposable est `id:`
(`LC-00-INDEX`), le nom de fichier est décoration.*

**FOND — non entamé, et c'est le seul qui compte** : plafond `T-b` / carte shadow `T-a` ·
routes α/δ · DESI DR2 · `Δ-C` · anti-circularité `K` · gap `R1″ ∧ R2″ ∧ R4″`.
**Le seul levier KB-only nommé et exécutable ici** : les imports
**`{I1 Δ₋=0 ; I5 Δ₊=3 ; I3 ; I4}`** (provenance SFG-1 / DELTA-C), auxquels le
`T-c`-conditionnel de `LC-D-G3-ADMISSIBILITE` est suspendu. Les établir convertirait un
conditionnel en résultat. Aucun autre geste du §5 n'entame `β`.

# §6. DÉPÔT — R-55

**GARDE NEUVE, S22 — AVANT TOUTE ANNONCE, RECHERCHE INVERSE SUR LE SHA.** Pour chaque
fichier à toucher : `grep -rlF "<sha8 actuel>" --include='*.md' --include='*.py'
--include='*.json' .`. **Si le compte n'est pas 0, le sha du fichier EST un gel** et le
fichier ne se modifie pas. Une commande, deux secondes ; son absence a coûté un dépôt
annoncé et retiré. *C'est une garde, pas une règle : le §4 reste à six.*

Annonce **AVANT** le token : **chemin + sha256 complet + message de commit, FICHIER PAR
FICHIER, RETRAITS COMPRIS** — retraits de **règles** compris. Token donné avant
l'annonce : **fais l'annonce quand même et attends**. *Une instruction de déposer n'est
pas la confirmation d'une annonce.* Push par **URL ÉPHÉMÈRE**, jamais
`git remote set-url`. Après push : `diff` sur **clone neuf** ; token à **0** dans
l'arbre, `.git/config`, les messages, **tous les blobs** et le **reflog** ; puis
révocation.

**La révocation se DEMANDE et se MESURE.** `DELETE /personal-access-tokens/self` rend
**404** — remesuré S22 : le pilote ne peut pas révoquer un PAT fine-grained. Il mesure
le **401** sur `GET https://api.github.com/user` après que l'opérateur a révoqué.
**UN TOKEN PAR DÉPÔT.**

**Le sujet du commit est ≤ 72 caractères et purement désignatif ; la substance va dans
le CORPS.** Le message ne s'enrichit pas d'un mot après l'annonce.

Identité : `LC-RACCORD pilote S23 <pilote-s23@lc-raccord.local>`.
**LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.**

---

**§6.4 — sentinelle terminale.** Cloner, mesurer, apurer, requalifier, conventionner,
articuler deux taxonomies, faire auditer : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. **S22 a rangé une topologie de surfaces et s'est
fait corriger deux fois — elle n'a pas avancé d'un pas sur la question scientifique.**
`R-23` reste **suspendue à `OB`**. `W³` est toujours **SANS VALEUR**. `O₂` n'est pas
construite. β `T-b`, non résolu, **SEUL facteur d'`O₂` ouvert**.
**CCC n'est ni démontrée ni réfutée.**
