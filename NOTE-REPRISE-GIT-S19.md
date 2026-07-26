---
id: NOTE-REPRISE-GIT-S19
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S19 (2026-07-26). Consolide et REMPLACE NOTE-REPRISE-GIT-S18 ; les notes S9-S18 vivent dans l'historique git. PIÈCE OPÉRATIONNELLE au sens de SCELLE-OPERATIONNEL-INSTRUCTION : elle se RECALE EN PLACE, elle ne s'amende pas par fichier séparé. ACQUIS S19 : recensement des écarts S14-S19 et la propriété qui les discrimine ; SIX correctifs de méthode déposés ; la KB active mesurée, partitionnée et bornée aux intrants ; les quatre corps de l'ensemble B CONFRONTÉS 4/4 AU BIT. AUCUNE gate ouverte, AUCUN verdict touché."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée, OPÉRATIONNELLE. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S18.md, retirée de la racine au même commit que PROMPT-OUVERTURE-S19.md, après AUDIT DE REPORT item par item (§10)."
regime_de_pieces: "OPÉRATIONNELLE. Un défaut mesuré sur cette note se CORRIGE EN PLACE, avec bump de version:, entrée au champ recalages:, et § nommés au message de commit. Elle ne reçoit PAS d'AMENDEMENT-<n>. Corps : audit/SCELLE-OPERATIONNEL-INSTRUCTION.md."
recalages: "S19 — §0.4 SURFACES : l'énoncé S18 « les sept .pdf du mount sont des ZIP » et « canal de HACHAGE nul » est PÉRIMÉ par mesure (4 vrais PDF, 0 ZIP, 4/4 confrontés au bit). S19 — §6.3 : quatre lignes de la note S18 étaient contredites par son propre §5ter (LC-00-INDEX, G-1, sort de R-23, sources/ hors compte), recalées ici. S19 — §9 : la table de supersession portait audit/ 55 et une racine périmée, recalée. S19 — titre H1 : la note S18 s'intitulait « Note de reprise S17 », défaut d'âge non reconduit."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S19 », À VÉRIFIER PAR `git log`, JAMAIS par cette note — ET SANS PRÉSUMER QU'IL EST HEAD (précédent S17 nº1 ; en S18 et S19 la chaîne démarrait bien à HEAD, ce qui ne prouve rien pour S20). Ses parents remontent par b8c6700 (topologie des dépôts, correctif 6), a8f3923 (quatre correctifs de méthode), 0a102b7 (Reprise S18), 602c828, dc8ca29, 7dbee86, 2ff65f9, b79e3de, aedc9a2."
regle_unicite: "UN SEUL fichier de reprise DE LA SÉRIE GIT-S<n>, au git comme à la KB active. La borne à la série est ÉCRITE depuis S18 : kb/NOTE-REPRISE-V96.md est d'une AUTRE série, ses octets sont INTACTS (6 116 o, sha8 5b194dc2), son contenu est absorbé au §10bis C de la note S18 et reporté ici au §5bis. Ce n'est PAS un écart. Mesuré en S19 : la KB active ne porte plus AUCUNE note de reprise, ni aucune pièce de kb/."
autorite: "RÉGIME G-4, CLOS : le git est l'espace de consignation et FAIT FOI pour la gouvernance et les résultats. R-54 est BORNÉ AUX INTRANTS depuis S19 (correctif 6) : la KB active fait foi pour les seuls corps sources que le pare-feu interdit de déposer. Corps : audit/TOPOLOGIE-DEPOTS-INSTRUCTION.md."
---

# Note de reprise S19 — état, acquis, prochain geste

> **Pourquoi cette note est plus courte que la précédente.** La note S18 pesait 53 691 o, et la
> lecture obligatoire d'ouverture 68 173 o — à 1 % près le poids du §0-lite qu'on avait comprimé
> d'un facteur 11 pour libérer ce budget. **La masse d'un protocole est elle-même une source
> d'écarts** (précédent S19). Le corpus de conduite vit désormais dans des pièces `audit/`
> déposées, opposables et **recalables en place** ; la note cesse d'être leur seul porteur. Elle
> reste **autoportante** au sens strict — elle ne renvoie à **aucune note antérieure** — mais elle
> renvoie aux pièces déposées, par chemin, et c'est ce qui la tient courte.

## §0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S19

**Tout attendu porte sa commande.** Un nombre sans son instrument n'est pas opposable.
Table complète : `audit/S0LITE-INSTRUMENTS-INSTRUCTION.md`. Régime d'impression :
`audit/S0LITE-IMPRESSION-INSTRUCTION.md` — les 12 scripts sont TOUS exécutés, seule la
restitution est compressée, **clause de dépliement au premier écart**.

    ls instruments/*.py | wc -l                       34
    ls instruments/archives-scelees/*.py | wc -l       76
    ls audit/ | wc -l                                 68     (67 fichiers + 1 répertoire)
    ls audit/beta-paquet-gouvernance/LC-BETA-* | wc -l  8
    ls kb/*.md | wc -l                               215
    ls hors-KB/B/ | wc -l                              4
    ls -p | grep -v /                                  4     racine, UNE seule note de reprise

`sources/` (4) et `manifest/` (1) sont **HORS COMPTE, assumé par écrit**
(`audit/SOURCES-MANIFEST-RESERVE.md`) : leur CARDINAL n'est pas surveillé, le CONTENU des 3 PDF
l'est au §0.3. `hors-KB/` ne porte que `B/` — **`hors-KB/A/` est ABSENT du dépôt, par
construction**, dette G-1 ouverte, **pas un écart**.

Puis `python3 instruments/inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** (il
**réécrit sa date** : restaurer par `git checkout`) ; `python3 instruments/run_sceau.py
verif_paquet_propre` → sha8 **`051e2833`**, **rc=0**.

**PIÈGE D'INSTRUMENT, mesuré en S19.** `62` était la valeur de `ls audit/` en S19 et celle de
`find audit/ -type f` en S18. Deux valeurs égales sous deux instruments **ne se confirment pas**.
Déclare ton instrument, pas seulement ton résultat.

### §0.1 Les 12 redémonstrations — bilan INCHANGÉ depuis S9, dix sessions

**271/271 PASS + 101 consignations, 12/12 rc = 0.** Décomposition pour recompte indépendant,
**multiensemble et NON dans l'ordre** :
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` · `5+5+6+6+8+7+3+10+14+10+8+19 = 101`.

**REJOUÉES ET CONFORMES EN S19, 12/12 marqueur ≡ bilan auto-déclaré, zéro écart.** Par script :
R-1 6/3 · R-2 12/8 · R-3 16/6 · **R-4b 35/5** · **R-5b 17/5** · R-6 16/6 · R-7 45/10 · R-8 21/10 ·
R-9 16/8 · R-10 40/14 · R-11 36/19 · R-12 11/7.

Variantes qui comptent : `redemo_R4_CT_b.py` et `redemo_R5_reductions_b.py`. Les v1 restent au
dépôt et **ne se rejouent pas**. Motif de comptage : **`^[[:space:]]*\[?PASS\]?`** — R-1, R-2, R-6
et R-12 impriment **sans crochets**, la classe est de **quatre**. R-8, R-10 et R-11 libellent leur
bilan différemment (accents, tirets) : **ce n'est pas un écart**.

### §0.2 Rejeux de confirmation hors compte — 5/5 CONFORMES en S19

`harnais_R9.py` **6/6 mordantes**, rc=0 · `harnais_R11.py` **7/7 mordantes + 0 vacante**, rc=0,
crée `instruments/__pycache__/` **à nettoyer** · `cd hors-KB/B && python3 verif_B_tracteur.py`
rc=0, sha8 **`8e386686`** du FICHIER (il n'imprime aucun sha) ·
`instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` **6/6**, sha256
`7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9` ·
`audit/LC-BETA-CONTROLE-DEPOT.py --self-test` **8/8 mordantes**, rc=0 — **et SANS audit de
vacuité, dette ouverte** (`audit/GARDES-VACUITE-INSTRUCTION.md`).

### §0.3 Intrants `sources/` au git — 3/3 CONCORDANTS en S19, vrais PDF

`2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` · `2409_10595v2.pdf` 2 332 898 o sha8 `27a94980` ·
`2503_19957v1.pdf` 910 410 o sha8 `113ab4a2`. `%PDF` lu aux octets, 3/3.

### §0.3bis Intrants de la KB active — **CONFRONTÉS 4/4 AU BIT, et c'est NEUF**

Contre `audit/LC-WORK-REGISTRE-CORPUS.md`, tous vrais PDF, `%PDF` et `%%EOF` aux octets :

| ligne | fichier | sha256 | octets | pages |
|---|---|---|---|---|
| `B1` | `2503_09372v2.pdf` | `6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62` | 979 890 | 38 |
| `B2` | `1909_11703v2.pdf` | `e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7` | 386 010 | 14 |
| `B3` | `2402_04308v2.pdf` | `1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2` | 4 629 572 | 78 |
| `B4` | `2312_17316v2.pdf` | `7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541` | 1 223 061 | 88 |

La pagination `38 · 14 · 78 · 88` **recoupe** celle établie par le canal OCR en S17 : aucune
substitution n'a eu lieu entre les deux époques. **Ce que cela n'est PAS** : le classement `C-iii`
de ces quatre lignes a été rendu **sur le canal OCR** ; ces octets ne le refont ni ne le
confirment, et *« aucune ligne n'est classée sur des octets confrontables »* **reste vrai du
classement rendu**. La **réserve permanente du §2.4 n'est pas entamée d'un mot** : elle porte sur
publié-contre-préprint, pas sur PDF-contre-OCR.

### §0.4 SURFACES — **RECALÉ EN S19** (premier recalage sous le correctif 2)

**PÉRIMÉ** : l'énoncé de la note S18 selon lequel *les sept `.pdf` du mount sont des ZIP* et que
*le mount est un canal de LECTURE fidèle et un canal de HACHAGE nul*.

**MESURÉ EN S19** : la KB active porte **7 fichiers** — 4 vrais PDF confrontés au bit, **0 ZIP** —
et une masse de **7,3 Mo** contre 48,5 Mo à l'ouverture de la séance. Cardinal au cours de la
séance : **27 → 14 → 8 → 7**. **Intersection avec `kb/` : 0.**

Le précédent S17 nº2 — *un contenant non ouvert n'est pas un contenant mesuré* — **reste debout** ;
c'est sa prémisse factuelle qui est dépassée. Et la nuance à conserver : **la KB active peut
désormais servir des octets confrontables ; elle n'est toujours pas une mémoire** — la
confrontation ne vaut que parce que le **REGISTRE** porte les sha, la surface n'en garde aucun.

### §0.5 Leçons d'environnement opposables (S2–S19, toutes maintenues)

`setsid nohup` pour rejeu long ; **`ls audit/` et non `ls audit/*.md`** ; jamais deux sceaux dans
le même arbre ; les durées ne sont pas des clés de sceau ; `origin/front-pq` résiduelle et bénigne ;
`inventaire_sceaux.py` **réécrit sa date** ; `harnais_R11.py` crée `__pycache__/` ; `pgrep -f`
s'auto-matche ; `simplify` non borné ; `pdfplumber` 0.11.9, `pdftoppm`/`pdfinfo`/`pdftotext`/`unzip`
présents, Pillow présente, **`pymupdf` ABSENT**, `extract_words` **mensonger** sur les mathématiques
affichées — descendre au niveau `chars` ; **`xxd` ABSENT** — `python3` ou `od`.

- **`rc=$?` après un pipe mesure le DERNIER élément du pipe** — capturer le `rc` AVANT tout pipe.
- **`grep -c` compte des LIGNES, pas des occurrences** — `grep -o | wc -l` ou `re.findall`.
- **Les chaînes `&&` s'interrompent sur un `grep -c` qui rend 0** — `|| true` quand le zéro est
  attendu.
- **LES MOTIFS SE BORNENT.** Un `grep -rn` non borné sur `kb/` rend ~15 000 tokens pour une
  question de trois lignes — et c'est ce `grep` qui a produit la contamination de S18.
- **NEUF S19 — `bash -c` est requis pour la substitution de processus.** `diff <(…)` échoue sous
  `/bin/sh` (« Syntax error: "(" unexpected ») : deux occurrences en S19, rattrapées.
- **NEUF S19 — `api.github.com` est dans l'allowlist**, et un token se vérifie révoqué par un
  **401** sur `GET /user`. **Ne demande pas un état que tu peux mesurer.**
- **Réseau** : `arxiv.org` **HORS** allowlist `bash`, `github.com` et `api.github.com` **DEDANS**.
  Les outils web sont un **canal SÉPARÉ** qui rend du **TEXTE, jamais des octets hachables**.
- **Token** : en ligne, jamais au disque, jamais dans `.git/config`, jamais dans un commit, et
  **vérifié à 0** y compris dans le contenu de **tous** les blobs. **Un token par dépôt, arrivant
  APRÈS son annonce, révoqué après usage et la révocation MESURÉE.**
- **Identité de commit** : `LC-RACCORD pilote S<n> <pilote-s<n>@lc-raccord.local>`. **Le pilote ne
  signe JAMAIS du nom de l'opérateur.**

## §1. Historique des acquis (S9 → S19), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2) ; volet 1 (V6) et volet 1-bis (`[D5]` LEVÉ, `W3`) clos et
  déposés.
- **S12** : VOLET 2 arbitré = β/P-1 ; sort de R-23 = MAINTIEN.
- **S13** : β ouvert sous discipline ; brouillon de cadrage ÉCARTÉ ; **P-8 SOLDÉ** (`cad358a`).
- **S14** : G-4 TRANCHÉ ; périmètre de `S-B1` arbitré aux deux ensembles ; swap d'unicité.
- **S15** : §0-lite intégral ; registre des 4 corps β re-confronté 4/4 ; arbitrages nº1 et nº2 ;
  amendement de périmètre nº2 déposé ⟹ **R-7 SATISFAIT** ; contrôle dépôt déposé.
- **S16** : **P-0 (R-41) RENDU sur les SEPT sources**, issue fantôme écartée par mesure **0/7** ;
  arbitrage nº3 ; registre de corpus déposé ; boucle de refourniture COUPÉE.
- **S17** : **`S-B1` RENDU** ; **nature réelle du mount établie** ; six arbitrages ; **paquet β
  SOLDÉ** (journal V94 byte-confronté) ; cinq corps d'assaut mesurés ; norme de nommage ADOPTÉE.
- **S18** : sept arbitrages de gouvernance ; **`LC-00-INDEX` déposé** ; §0-lite RECADRÉ ; **F5 voie
  (i) ouverte et ARRÊTÉE sur prémisse fausse** ; **deux `D5` et trois `W3`** mesurés.
- **S19 — SÉANCE DE MÉTHODE, ET ELLE A MESURÉ.** Recensement des écarts S14–S19 et **la propriété
  qui les discrimine** ; **six correctifs déposés** ; **KB active mesurée, partitionnée, bornée aux
  intrants** ; **ensemble B confronté 4/4 au bit**. Détail au §5ter.

## §2. P-0 (R-41) — RENDU. Corps : `audit/LC-BETA-04-P0-RENDU-SEPT-SOURCES.md`.

Sept lignes identifiées, **issue fantôme écartée par mesure 0/7**. Grades écrits sur cinq lignes :
SciPost Phys. Core 8 075 · JHEP 01(2020)155 · JHEP 06(2024)044 · JHEP 05(2024)053 ·
Rev. Math. Phys. 8 327-392. `S9` et `S10` : **préprints arXiv non arbitrés**, arXiv seul.

### §2.1 ARBITRAGE nº3 et sa RÉSERVE ÉCRITE — se recopie avec `S9` et `S10`, jamais séparée

1. **Aucun comité de lecture ne s'est prononcé.**
2. **§1.2 n'est pas satisfait à la lettre** — classables **par arbitrage d'opérateur**, non par
   satisfaction du critère. **La distinction ne s'efface pas avec le temps.**
3. **Un seul éditeur atteste.** arXiv. Aucune contrepartie indépendante.
4. **Réversible par l'événement, dans les deux sens.** Publication ⟹ la ligne SE RE-CONFRONTE ;
   retrait ou remplacement ⟹ retour sous `SUSPENDU`.
5. **Ce n'est pas un défaut de recherche.** L'écart est une propriété des objets.

**État au 2026-07-26** : ni retrait ni remplacement constaté. **Ni `S9` ni `S10` ne retombent sous
`SUSPENDU`.**

### §2.2 Écart de version `S10` — NOMMÉ, NON RÉSOLU

Registre et P-0 §3 déclarent les octets consommés en **v2 daté 09/07/2026** ; le tampon récupéré
porte **`08 Jul 2026`**. **Un jour d'écart.** Réconciliation plausible existante — soumission
contre annonce — **non retenue**. **Ce qui est établi : v2 existe.**

### §2.3 ARBITRAGE — LIMITE grade-publié / octets-préprint : **RÉSERVE PERMANENTE**

Le grade porte sur l'**article publié**, les octets consommés sont le **préprint**, les deux
versions **n'ont jamais été confrontées**, sur **cinq lignes** : `B1` `B2` `B3` `B4` `S8`. **On
n'ira pas chercher les octets publiés.** La limite se porte **indéfiniment**.
**La confrontation 4/4 du §0.3bis ne l'entame PAS** : autre objet.

> **AUCUNE LIGNE DU PÉRIMÈTRE N'EST SANS RÉSERVE.** **5** lignes sous réserve de décalage
> version-consommée / version-gradée (`B1` `B2` `B3` `B4` `S8`) · **2** lignes sous réserve
> d'absence de grade (`S9` `S10`). **5 + 2 = 7.** S'ajoute la **RÉSERVE DE VERSION sur
> `LC-00-INDEX`** (68 pièces le citent, 3 seulement nomment une version, max v1.64 contre v1.78
> déposée — `audit/INDEX-VERSIONS-RESERVE.md`). **Une ligne citée sans sa réserve est INCOMPLÈTE.**

## §3. `S-B1` — RENDU. Corps : `audit/LC-BETA-SB1-RAPPORT.md` + son `AMENDEMENT-1`.

`S-B1` **classe**. Il n'a confronté aucune cible, ouvert aucune gate, conclu sur aucune physique.
**Sa protection est sa stérilité.** L'espace `C-i`…`C-iv` gelé à `LC-BETA-03` §2 est **inchangé**.

**RÉPARTITION FINALE — `C-i` 0 · `C-ii` 0 · `C-iii` 6 · `C-iv` 1**

| ligne | classe | canal du CLASSEMENT | pare-feu mordant |
|---|---|---|---|
| `B1` `2503.09372v2` | `C-iii` | mount OCR, 38 p. | `FB-2`, `FB-4` |
| `B2` `1909.11703v2` | `C-iii` | mount OCR, 14 p. | `FB-2` |
| `B3` `2402.04308v2` | `C-iii` | mount OCR, 78 p. | `FB-2` **à la lettre**, `FB-4`, `FB-1` en vigilance |
| `B4` `2312.17316v2` | `C-iii` | mount OCR, 88 p. | `FB-3`, `FB-2` |
| `S8` `gr-qc/9511019` | `C-iii` | P-0 octets + web | — |
| `S9` `2602.15275v2` | `C-iii` **+ réserve §2.1** | P-0 octets + web | `FB-3` en vigilance |
| `S10` `2605.11821v2` | **`C-iv`** **+ réserve §2.1** | P-0 octets + web | hors-domaine |

**ANTÉRIORITÉ, mesurée sur les SEPT** : `B1` 15 · `B2` 10 · `B3` 11 · `B4` 21 · `S8` 0 · `S9` 0 ·
`S10` 0 fichiers `kb/`. `B3` est inscrite **consommée** comme `LSW 2402.04308`, fournissant la
**famille `p`** du coin de transmission. Ordre classer-puis-confronter **tenu sur les quatre**.

**DÉLIMITATION À CONTENU NOMMÉ.** Condition 3 de `LC-BETA-03` §3 **FAUSSE** ⟹ **`S-B2` NON ARMÉ**,
issue **complète et non échec**. Approche la plus serrée : **`B3`**, famille de conditions de bord
bien posée avec critère de stabilité de modes — la **forme** du levier — mais en cavité
euclidienne finie, entre les deux points fixes `D` et `N`.

> **LEVIER FALSIFIABLE — ce qu'il faudrait pour `C-ii`, et qui manque à `B3` SÉPARÉMENT :**
> **lorentzien** · au **`𝓘⁺` genuine sans cutoff** · sur une **jonction à deux faces** · pour un
> **graviton d'Einstein propageant**. Une source portant les quatre **basculerait le classement**.

**ARBITRAGES** : `C-iv` **EST une classe réelle** (écart nº2 du rapport **REJETÉ et CONSERVÉ** — un
écart rejeté se date, il ne s'efface pas) · **règle de lecture établie** : *les exemples de `C-iii`
sont illustratifs à l'intérieur de l'arène de β ; le rattachement se juge sur l'objet mesuré,
jamais sur la présence d'un mot dans une liste d'exemples* · **`S10` → `C-iv` par l'ARÈNE**, avec
clause de réversibilité si un lien est **exhibé**. Largeur de `C-iii` : **amendement PROSPECTIF**
(`audit/GRILLE-BETA-CIII-INSTRUCTION.md`), **`S-B1` NON rejugé** — le défaut est de RÉSOLUTION, non
de logique. **Aucune source n'est écartée pour non-fourniture d'octets** ; `SUSPENDU` ne s'applique
à personne. **Issue anticipée confirmée 4/4 et NON RETOUCHÉE** — son prix reste sa date.

## §4. PAQUET β — SOLDÉ et ARCHIVE. Cinq corps d'assaut mesurés.

**ARCHIVE BYTE-GELÉE**, jamais rejoué, atelier séparé assumé. Le défaut « un gel sur un répertoire
vivant n'est pas un gel » **reste nommé**, clos par le statut ARCHIVE. **43 entrées soldées** : 8
pièces `LC-BETA-*` byte-intactes sous `audit/beta-paquet-gouvernance/` + 34 `BETA-COPIE-*`
reconstructibles par `audit/LC-BETA-PAQUET-CONCORDANCE.md` + 1 byte-confrontée.

**Journal V94 — CONFRONTATION D'OCTETS CONCORDANTE** : 12 623 o, sha256
`b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c`, identique à la table.
**LES OCTETS NE SE DÉPOSENT PAS** — copie de substance, **interdit dur, arbre ET historique**. Le
fichier arrive nommé `LC-JOURNAL-V94.md` : **ne renomme JAMAIS une pièce pour passer sous un
contrôle nominal.** Ce qui est déposé, c'est la confrontation.

**Cinq corps d'assaut, premières mesures** (`LC-WORK-REGISTRE-CORPUS-AMENDEMENT-1`) :
`0808.2054v1` `fcfebce6…` 251 186 o · `2007.06800v4` `5be89da3…` 2 521 998 o · `2409.08709v4`
`d5e3a1de…` 723 288 o · `2412.00183v1` `eb3ddc9c…` 1 140 406 o · `2606.09170v2` `3d8580a5…`
537 107 o. `%PDF`/`%%EOF` 5/5, identité lue dans les octets d'abord, **5/5 concordante**.
**Les cinq corps N'ONT PAS ÉTÉ LUS.** Registre §3 : **DEUX colonnes de version**, dont
`NON DÉTERMINABLE` sur les cinq lignes (`LC-WORK-REGISTRE-CORPUS-AMENDEMENT-2`) — **les verdicts
`S-G3T-*` ne deviennent PAS traçables rétroactivement.**

## §5. P-8 / P-9 · norme de nommage · absorption V96

**P-8 SOLDÉ ET DÉPOSÉ** (`cad358a`) : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`, auto-test **6/6**,
rejoué CONFORME en S15, S16, S17 **et S19**. **P-9 opposable** : le dépôt d'un instrument n'atteste
que son existence ; **sa valeur se mesure À LA PROCHAINE GATE**. Les 8 pièces `LC-BETA-*`
**mentent par âge** sur ce point — défaut **sur-restrictif, non bloquant**, nommé à
`audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md`, **jamais corrigé en place**.

**Norme de nommage ADOPTÉE** (`audit/LC-NORME-NOMMAGE.md` + `AMENDEMENT-1`). Grammaire
`<SUJET>-<TYPE>[-AMENDEMENT-<n>]`, TYPE du vocabulaire **fermé**, ASCII majuscules et tiret seul,
**contrôle §4 mécanique : nom sans extension ≡ champ `id:`**. Périmètre liant : `audit/`,
`instruments/`, `hors-KB/`, racine — **`kb/` EXCLU**. `PROMPT-OUVERTURE-S<n>` et
`NOTE-REPRISE-GIT-S<n>` sont des **exceptions NOMMÉES** au §5, TYPE-premier, qui **ne s'étendent à
aucune autre pièce**. **Défaut nommé non corrigé** : la norme ne satisfait pas sa propre grammaire.
**Les 5 pièces déposées en S19 sont conformes 5/5 au contrôle §4.**

### §5bis Contenu de `kb/NOTE-REPRISE-V96.md`, absorbé par report audité — OCTETS INTACTS

- **Discipline de boot** : R-54 · R-55 · **R-36 (aucun fichier haché n'embarque son propre PKG)** ·
  §6.4.
- **Protocole V97, opposable** : recomputer le **PKG de la KB active** (`LC-WORK-BOOT-SESSION*.py`)
  · relire la valeur de clôture au **manifeste v2.124** · continuité OK ⟺ **PKG recomputé == PKG
  déclaré** ; écart non nommé ⟹ **STOP**. **MESURÉ EN S19 : cette condition n'a été exécutée dans
  AUCUNE des cinq dernières sessions ; le script est au git et ABSENT de la KB active. Dette
  OUVERTE, désormais mesurable. Rien n'est conclu de son issue.**
- **Clôture V96** : P-8 SOLDÉ · front `p_Q` matérialisé, **NON PRIORISÉ** (gate §A levée sur la
  SEULE condition (i) ; (ii) proxy porteur et (iii) question sharp `d=3` **non levées**) · GLO
  v1.74→v1.75, fork glossaire résolu côté KB · contamination `verre_fraicheur_3d.jpg` retirée.
- **Invariants** : `{ A4 ; A2★ ; N }` INCHANGÉ · R-53 **0/4** · `O₂` non construit · β **`T-b`,
  SEUL facteur d'`O₂` ouvert, DÉBLOQUÉ par P-8** · α = **C1-b** · D1 non clos.
- **Ouverts pour V97** : substance β **DÉBLOQUÉE** · `p_Q` non priorisé · copie opérateur hors-KB
  `03_glossaire` **v1.70 STALE** à re-sync · **`D-01`/`D-08` non mesurés (P-9)** · **Q A/B** non
  tranchée · **§9.4 append-only rouvert** · **bump boot v1.3→v1.4 DIFFÉRÉ** (l'attendu imprimé dit
  « instruments_exclus 4 » quand le réel est **6** — défaut d'âge nommé).
- **Règle de séquence, opposable** : la consignation est le **DERNIER** geste · le PKG de clôture se
  calcule **UNE seule fois**, après tous les dépôts hachés · **rien de haché** n'est déposé après ·
  le PKG est porté par le **MANIFESTE**, jamais par la reprise.

## §5ter. S18 et S19 — acquis

### §5ter.1 S18 — sept arbitrages, et un ARRÊT SUR PRÉMISSE FAUSSE

Déposés à `602c828` : `audit/00_index.md` (**`LC-00-INDEX` v1.78, 236 461 o**, byte-intact) ·
`INDEX-VERSIONS-RESERVE` · `S0LITE-IMPRESSION-INSTRUCTION` · `SOURCES-MANIFEST-RESERVE` ·
`LC-WORK-REGISTRE-CORPUS-AMENDEMENT-2` · `GRILLE-BETA-CIII-INSTRUCTION` ·
`F5-VOIE-I-CIBLES-GELEES`. **7/7 confrontés au bit sur clone neuf**, token à 0 sur 622 objets.
`LC-00-INDEX` n'a **JAMAIS** fait partie des 215 scellés : son absence était une **exclusion de
construction**, et **résoudre un renvoi n'est pas le rendre traçable**.

**F5 voie (i) OUVERTE ET ARRÊTÉE à sa première cible, sur PRÉMISSE FAUSSE.** Le corps de F5 n'a
**pas** été lu en substance. `audit/F5-VOIE-I-CIBLES-GELEES.md` est **DÉFECTUEUSE, SCELLÉE,
byte-intacte, et ne sert PAS de cadrage.** **Le cadre déjà tranché autour de la cible — `[D5]`
levé, la désambiguïsation `W3`, les deux `D5` et trois `W3` — et les anticipations connues sont en
ENVELOPPE** : voir §6.1.

### §5ter.2 S19 — le recensement, et la propriété qui discrimine

**Recensé sur S14→S19 : ~14 écarts imputables au pilote, ~13 imputables aux pièces ou au
protocole.** La part de l'opérateur n'est pas la plus petite. Et les deux parts se concentrent
chacune dans **une seule classe** : côté pilote **l'instrument de comptage** (5 sur 14), côté
pièces **le défaut d'âge des pièces opérationnelles**.

> **LA PROPRIÉTÉ QUI DISCRIMINE : LA VÉRIFIABILITÉ.** Les règles qui portent sur un **artefact**
> tiennent — R-55 a été inversée en S16, restaurée en S17, tenue en S17, S18 et S19, et son
> exception est désormais pré-armée. Les règles qui régulent l'**ordre interne du pilote**
> échouent, **et à 100 %** — « mesure HEAD avant de lire ce prompt » a été violée 2 fois sur 2,
> parce que le prompt est le seul objet qui nomme le dépôt à cloner : **la consigne se contredit
> performativement.** Trois propriétés ont fermé la classe R-55 : le mode de défaillance est
> **nommé**, l'exception est **pré-armée**, le respect est **vérifiable après coup**.

**Le poids mesuré du protocole** : lecture obligatoire d'ouverture en S19 = **68 173 o**, contre
**68 966 o** pour la sortie §0-lite comprimée d'un facteur 11 afin de libérer ce budget. Et
**cinq séances consécutives sans mouvement scientifique** (S15, S16, S17, S18, S19). Les deux
lectures sont vraies et aucune n'annule l'autre : **zéro faux acquis en cinq sessions est le
produit de cette discipline**, et **la masse du dispositif est elle-même devenue une source
d'écarts**.

**MESURE DE CLÔTURE — elle contredit une attente du pilote, et elle est portée telle quelle.**
`PROMPT-OUVERTURE-S20` pèse **14 528 o**, contre 11 220 o pour celui de S19 : **+29 %**, parce que
le correctif 1 y ajoute son §0, le correctif 4 sa table de commandes, le correctif 3 sa procédure
d'enveloppe, et son §10 douze précédents neufs. La présente note **ne peut pas porter sa propre
taille** — **R-36 s'étend à toute mesure d'une pièce sur elle-même, pas seulement à son sha** : la
valeur inscrite modifie l'objet mesuré, et aucun point fixe n'existe. Elle est **mesurée au dépôt et
annoncée avec son sha256**. Ordre de grandeur du total : **~63 kO contre 64 911 o en S19**, soit une
réduction de **quelques pour cent, non de moitié**. Chaque ajout se justifie séparément ; leur somme
est plus lourde. **C'est la démonstration empirique du précédent nº10 par la séance même qui l'a
écrit** : six correctifs qui suppriment des classes d'écarts n'allègent pas l'appareil, ils le
déplacent. Le point de réglage n'a pas bougé du côté espéré. **À re-mesurer en S20, pas à espérer.**

### §5ter.3 S19 — les six correctifs déposés

| nº | pièce | objet |
|---|---|---|
| 2 | `audit/SCELLE-OPERATIONNEL-INSTRUCTION.md` | partition SCELLÉ / OPÉRATIONNEL ; recalage en place sous trois obligations de traçabilité |
| 4 | `audit/S0LITE-INSTRUMENTS-INSTRUCTION.md` | tout attendu porte sa commande ; un nombre sans instrument n'est pas opposable |
| 5 | `audit/GARDES-VACUITE-INSTRUCTION.md` | `N mordantes` **et** `M vacantes` ; un `M` absent est un écart |
| 3 | `audit/ENVELOPPE-ANTICIPATIONS-INSTRUCTION.md` | les anticipations sortent de la lecture obligatoire ; procédure en cinq pas |
| 6 | `audit/TOPOLOGIE-DEPOTS-INSTRUCTION.md` | CINQ dépôts ; **R-54 borné aux INTRANTS** |
| 1 | `PROMPT-OUVERTURE-S20.md` | ouverture en deux messages ; attendus placés **après** l'ordre de mesure |

Déposés à `a8f3923` (4/4 confrontés au bit, token 0 sur 450 blobs) et `b8c6700` (1/1 confronté,
token 0 sur 451 blobs).

### §5ter.4 S19 — la KB active, mesurée et bornée

**R-54 est BORNÉ AUX INTRANTS.** Motif mesuré, non argumenté : sur les deux seules pièces où les
deux surfaces avaient divergé — `R10-REDEMONSTRATION.md` et `redemo_R10_nonlin.py`, divergence
**cosmétique et non sémantique**, qu'**aucun instrument du dépôt ne pouvait voir** — c'est la
version **git** qui s'exécute et rend le `40/14` conforme. **Le §2 de `kb/LC-CONST-V1` énumère
QUATRE dépôts dont le git est absent** : deux topologies de mémoire sont en vigueur et aucune n'a
été écrite comme remplaçant l'autre. La table des **cinq** dépôts est au correctif 6, qui **nomme
le §2 périmé sans le toucher** — défaut d'âge **inévitable et assumé**, la constitution étant
scellée. **Sa cible « 25–35 fichiers » est PÉRIMÉE ; sept fichiers n'est pas un déficit.**

**Trois pièces orphelines subsistent à la KB active, MAINTENUES en place, ANALYSE À FAIRE** :
`CCC_presentation.html` 44 824 o · `CSE-R4R5-PAQUET-INCOGNITO.md` 32 783 o — et *audit froid
incognito* est le premier des restes de fond · `LC-WORK-GEN-PAQUET-CSE2.txt` 18 609 o.

## §6. PROCHAIN GESTE ET RESTE À FAIRE

### §6.1 `R-23` AU FOND — ARMÉE, NON OUVERTE. GO séparé, jamais d'office.

**Premier geste, avant toute lecture : rédiger et DÉPOSER un cadrage gelé NEUF** portant sur
**`R-23` AU FOND**, par l'ouverture du corps de F5, voie (i). Issues pré-déclarées, critère de
verdict écrit, **avant** toute lecture du corps.

**ENVELOPPE — `audit/F5-ANTICIPATIONS-RESERVE.md`, sha256
`3200e69b24fc9edf1f552e2bb1c03f2797962b63c1eb898f63dbc9946ef19e75`.** Elle porte les anticipations
connues et le cadre déjà tranché autour de la cible. **NE L'OUVRE PAS avant d'avoir déposé ton
cadrage.** Le cadrage **cite ce sha** ; après dépôt, l'enveloppe est ouverte, son sha **re-mesuré
et confronté**, et chaque point classé en **CONFIRMATION D'ANTICIPATION** ou en **DIVERGENCE**.
Procédure : `audit/ENVELOPPE-ANTICIPATIONS-INSTRUCTION.md`.

**Le pilote S19 était contaminé** — les cinq points lui sont arrivés par la lecture obligatoire de
la note S18, avant que l'enveloppe n'existe. **Si tu les as déjà lus, dis-le et liste-les en tête
de ton cadrage comme non créditables.**

### §6.2 Rendus, à ne pas rouvrir sans GO ni gel neuf

**`S-B1` RENDU** · **`S-B2` NON ARMÉ — c'est un RÉSULTAT, pas un reste-à-faire** ; il ne s'arme que
si une source portant les **quatre qualificatifs du §3** entre au périmètre, ce qui exigerait un
amendement de périmètre daté · **assauts `S-G3T-*`** non rouverts · **dissolution** arbitrée PAR
ENSEMBLE, avec clause de non-classifiabilité et de levier falsifiable — **une clôture d'ensemble se
rédige comme une DÉLIMITATION À CONTENU NOMMÉ, jamais comme un changement de statut.**

### §6.3 GOUVERNANCE — ce qui reste NON ARBITRÉ, recalé en S19

- **`G-1`** : 16 bundles décharge v2.74, 72 `.py` ; `hors-KB/A/` **mesuré ABSENT du dépôt** ;
  arbitrage (a) rendu en S18 = **FOURNITURE par l'opérateur, NON EXÉCUTÉE, dette OUVERTE**.
- **`G-5c`** : arborescence des silos. **`G-5b` est CLOS** par le dépôt de `LC-00-INDEX` en S18.
- **`R-23`** : **ARMÉE**, cadrage neuf requis (§6.1). Non arbitrée.
- **Migration de `kb/`** : **BLOQUÉE sur G-4, volet 3.** Le correctif 6 a retiré un *motif* devenu
  faux (le miroir vide) ; il n'a pas rendu la migration décidée.
- **Volet de recalage de la constitution** : NEUF EN S19. `kb/LC-CONST-V1` §2 est périmé et scellé.
  Le nommer sans le corriger est le mécanisme dont on vient de mesurer le coût. NON OUVERT.
- **Dette `audit/LC-BETA-CONTROLE-DEPOT.py`** : déclarer son `M vacantes`. Échoit **à la prochaine
  gate qui l'emploie** (P-9). NON EXÉCUTÉE.
- **Dette `instruments/concordance_mount.py`** : hacher la KB active contre le clone, déclarer
  `identiques / divergents / exclusifs`, auto-test mordant **et** vacuité. NON ÉCRIT.
- **Dette V97** : exécuter la condition d'arrêt du boot (§5bis). NON EXÉCUTÉE depuis S14.
- **Scission du §0-lite** : détection de dérive scriptable / calibration manuelle sur sous-ensemble
  **tiré par l'opérateur**. Proposée au correctif 4, **NON ARBITRÉE.**
- **Trois orphelines de la KB active** : analyse à faire (§5ter.4).
- Reports V96 §4 (§5bis) : `p_Q` non priorisé · `03_glossaire` v1.70 STALE · `D-01`/`D-08` non
  mesurés · Q A/B non tranchée · §9.4 append-only rouvert · bump boot v1.3→v1.4 différé.
- **Largeur de `C-iv` / `C-iii`** : classe réelle arbitrée, largeur non retouchée. Le déséquilibre
  subsiste ; la règle de lecture du §3 le compense sans le supprimer.

### §6.4 RESTES DE FOND, portés depuis S15 — INCHANGÉS

Audit froid incognito · plafond `T-b` / carte shadow `T-a` (non exhibée) · candidats genuine-dS
armés non lus + amendement nº3 daté · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C` plus étroit que
son libellé · `p` libre / P-sélecteur · anti-circularité `K` (Bunch-Davies, WCH) · `§7quinquies`
`K-B` prescription-dépendant · levier NOMMÉ NON ARMÉ · cadrage figé `37bc85e5` / gel amont
`b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald · gap résiduel `R1″ ∧ R2″ ∧ R4″`.

## §7. Discipline et précédents opposables — PORTÉS INTÉGRALEMENT

### §7.0 Précédents S19

1. **UNE CONSIGNE QUI RÉGULE L'ORDRE INTERNE DU PILOTE N'EST PAS VÉRIFIABLE, DONC N'EST PAS UNE
   GARDE.** Elle se remplace par une consigne portant sur un artefact ou sur l'ordre d'un rendu.
2. **UNE PIÈCE NON SCELLÉE N'A PAS BESOIN D'ÊTRE BYTE-INTACTE.** L'historique git fait l'audit, et
   mieux qu'une chaîne d'amendements.
3. **UNE NOTE AUTOPORTANTE QUI SE CONTREDIT N'EST PAS AUTOPORTANTE.**
4. **UN DISPOSITIF ANTI-FIT ÉCRIT DANS UNE PIÈCE À LECTURE OBLIGATOIRE DEVIENT UN VECTEUR DE
   CONTAMINATION.**
5. **UNE SURFACE SANS VERSION, SANS SHA ET SANS HISTORIQUE N'EST PAS UNE MÉMOIRE.**
6. **SUR UNE SURFACE SANS VERSION, UNE FOURNITURE DE MÊME NOM EST UNE OPÉRATION DESTRUCTRICE SANS
   TRACE.** Toute fourniture s'annonce avec ses octets et son sha256 **avant** d'être posée.
7. **DEUX SURFACES QUI PORTENT LE MÊME NOM SANS CONTRÔLE DE CONCORDANCE DIVERGENT SANS QUE
   PERSONNE NE LE SACHE.**
8. **UNE CONSIGNE DE RETRAIT SE DONNE PAR NOM DE FICHIER, JAMAIS PAR PROPRIÉTÉ** — surtout quand la
   propriété est partagée par l'ensemble entier. Écart S19 du pilote.
9. **UNE QUESTION POSÉE À L'OPÉRATEUR SUR UN FAIT MESURABLE EST UN INSTRUMENT NON EMPLOYÉ.** Écart
   S19 du pilote, commis deux fois sur la révocation d'un token.
10. **LA MASSE D'UN PROTOCOLE EST ELLE-MÊME UNE SOURCE D'ÉCARTS.** Chaque règle neuve est une pièce
    de plus à lire, à recopier avec sa réserve, et à vieillir.
11. **UNE COÏNCIDENCE DE VALEURS SOUS DEUX INSTRUMENTS N'EST PAS UNE CONFIRMATION.**
12. **UN VOCABULAIRE NE S'INTRODUIT PAS PAR L'USAGE.** Le pilote S19 a employé « sas » sans le
    déclarer comme proposition ; c'est la forme, par un rendu, de ce que la norme interdit par un
    fichier.
13. **R-36 S'ÉTEND À TOUTE MESURE D'UNE PIÈCE SUR ELLE-MÊME, PAS SEULEMENT À SON SHA.** Une pièce
    qui inscrit sa propre taille modifie l'objet mesuré : aucun point fixe n'existe. La mesure se
    porte HORS de la pièce — à l'annonce, au message de commit, ou dans une pièce tierce.

### §7.1 Précédents S18

- **UN OBJET LEVÉ SOUS SON PROPRE GEL NE SE RÉ-INSTRUIT PAS PAR UNE VOIE QUE CE GEL EXCLUAIT.**
- **DEUX OBJETS DE MÊME ÉCRITURE NE SONT PAS UN OBJET.**
- **UN CADRAGE PEUT ÊTRE DÉFECTUEUX SANS ÊTRE FAUX** : prémisse fausse ⟹ toutes ses issues.
- **UN COMPTE N'EST VRAI QUE SOUS SON INSTRUMENT.**
- **UNE GARDE INUTILE N'EST PAS UNE GARDE FAUSSE.**
- **UN ITEM DE RESTE-À-FAIRE PEUT ÊTRE ÉCRIT TROP LARGE.**
- **UNE PIÈCE ABSENTE PEUT ÊTRE ABSENTE PAR CONSTRUCTION.**
- **RÉSOUDRE UN RENVOI N'EST PAS LE RENDRE TRAÇABLE.**
- **UNE CLASSE QUI ABSORBE NE CLASSE PAS.**
- **LES MOTIFS SE BORNENT.**

### §7.2 Précédents S17

1. **UNE PIÈCE NE PEUT PAS DAVANTAGE CONNAÎTRE SA POSITION QUE SON SHA.** R-36 interdit de porter
   son propre sha ; **il n'autorise pas à affirmer qu'on est à HEAD.** Corps :
   `audit/LC-PROMPT-S17-DEFAUTS-DAGE.md`.
2. **UN CONTENANT NON OUVERT N'EST PAS UN CONTENANT MESURÉ.**
3. **LE NOM D'UN CONTENANT NE DÉCRIT PAS SON CONTENU.**
4. **UN ARBITRAGE INEXÉCUTABLE NE SE DÉGRADE PAS EN SILENCE.**
5. **UNE ANTÉRIORITÉ SIGNALÉE SUR UNE LIGNE NE DIT RIEN DES AUTRES.**
6. **LE TOKEN CONFIRME L'ANNONCE, PAS UNE VERSION AMÉLIORÉE.**
7. **UN INSTRUMENT DE COMPTAGE COMPTE CE QU'IL COMPTE.**
8. **UN ÉCART REJETÉ NE S'EFFACE PAS, IL SE DATE.**
9. **UNE MESURE SANS VERSION NE CONFRONTE RIEN.**

### §7.3 Précédents S16

1. **UN INSTRUMENT DE MESURE SE MESURE AUSSI.**
2. **IDENTIFIER DANS LES OCTETS D'ABORD, CHERCHER ENSUITE.**
3. **UN GRADE ÉDITORIAL NE SE TRANSFÈRE PAS D'UNE VERSION À UNE AUTRE.**
4. **UNE RÈGLE QUI NE PRÉVOIT PAS LE CAS SE PORTE À L'OPÉRATEUR, ELLE NE S'ÉTIRE PAS. UN GO N'EST
   PAS UN ARBITRAGE.**
5. **NE PAS DÉPOSER LES OCTETS QUAND LE REGISTRE SUFFIT.**
6. **QUAND UNE RÈGLE GÊNE, LA MESURER PLUTÔT QUE LA CONTOURNER.**
7. **`rc=$?` APRÈS UN PIPE NE MESURE PAS CE QU'ON CROIT.**
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS.**
9. **L'ORDRE R-55 A ÉTÉ INVERSÉ, ET UNE INSTRUCTION DE DÉPÔT NE LE RESTAURE PAS.**
10. **UN ÉCART QUI NE VIT QUE DANS UN MESSAGE DE COMMIT N'EST PAS PORTÉ.**
11. **UN CONTRÔLE PEUT MATCHER LA RÈGLE AU LIEU DE L'INCIDENT — FAUX PASS D'UN TYPE NEUF.**

### §7.4 Précédents S15

1. **UNE RÈGLE SE MESURE À SA SOURCE, PAS À SA GLOSE.**
2. **UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE.**
3. **UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL.**
4. **UNE CONFRONTATION PAYÉE SE PRÉSERVE HORS SURFACE TOURNANTE.**
5. **UN ZIP DE TRANSPORT N'EST PAS UN ZIP DE SUBSTITUTION.**
6. **UN CONTRÔLE QUI PASSE SUR L'ENSEMBLE VIDE EST UN FAUX PASS** — et sa réciproque. Les deux
   gardes sont nécessaires.
7. **UN GO N'EST PAS UN ARBITRAGE.**
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS** après une réussite partielle.

### §7.5 Précédents S14

1. **CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE. Le dépôt se mesure, il ne
   se déduit pas.**
2. **UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA DEMANDER.**
3. **UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM.**
4. **LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR.**
5. **UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS.**
6. **UN ORDRE DE CONDITIONS NE SE COMPRIME PAS.**

### §7.6 Précédents S13 · S11 · S10 · S9 · S8

**S13** — un chantier « à ouvrir » peut être DÉJÀ cadré : lire le dossier AVANT de rédiger un
cadrage neuf, **un brouillon rédigé dans l'ignorance du dossier se JETTE** · un prérequis bloquant
peut vivre dans le dossier : **le chercher** · un repérage peut faire remonter de la substance :
**le déclarer** · un instrument mandaté se construit **à la LETTRE du mandat** et **se prouve par
un AUTO-TEST MORDANT** · un dépôt fait avancer HEAD : **recaler §0-lite dans la reprise**.

**S11** — 1. un critère de bornage non confronté au cas d'espèce ne borne rien · 2. **une correction
peut être fausse, et aggravante** ; elle se rétracte par un fichier daté supplémentaire, l'amendement
fautif **reste et garde son numéro** · 3. un ordre de résolution figé au gel protège du fit ·
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE** · 5. un verdict sur une chaîne ne
réfute pas une substance · 6. le fait accompli d'un fichier ne crée pas un type · 7. **un token ne
s'écrit nulle part, et c'est vérifié** · 8. **la confrontation de dépôt se fait par `diff`, pas à
l'œil**.

**S10** — 1. hacher un contenant n'est pas lire un contenu · 2. un bornage par numéro de ligne ou
fin de page ne borne rien · 3. un espace-verdict déclaré exhaustif doit prévoir le cas qu'il n'a pas
prévu · 4. une information lue hors périmètre se déclare et ne s'emploie pas · 5. le token ne
remplace pas l'annonce R-55 · 6. **vérification de dépôt sur CLONE NEUF**, jamais sur déclaration ·
7. unicité de la reprise · 8. autorité des pièces de gouvernance : le git fait foi · 9. **sha de
première mesure faisant référence ; enregistrer n'est pas confronter** · 10. déposer au miroir
n'autorise pas à retirer de l'original.

**S9/S8** — un défaut du gel se nomme et s'amende par **fichier séparé daté**, jamais en place, sur
une pièce **SCELLÉE** · un harnais doit auditer la **VACUITÉ STRUCTURELLE** : en S9, **quatre faux
PASS** sur un lot qui se présentait à 38/38 · un pré-tri `[D]`/`[C]` **au gel** interdit de
reclasser après coup · **l'antériorité se PROUVE par l'état du répertoire** · une cible non
algébrisable se déclare **au gel** · un statut de présence se **MESURE** avant d'écrire la note ·
**annoncé puis GO ⟹ l'annoncé fait foi** · **un intrant refourni se CONFRONTE au registre AVANT
extraction**.

### §7.7 Procédure R-55 de dépôt

**Ordre non négociable** : annonce **chemin + sha256 complet + message de commit**, **fichier par
fichier, retraits compris**, PUIS token, PUIS push. **Si le token arrive AVANT l'annonce, l'annonce
se fait quand même et l'on attend la confirmation.** Une instruction de déposer **n'est pas** la
confirmation d'une annonce. Push par **URL ÉPHÉMÈRE**, jamais `git remote set-url`. Après push :
confrontation des sha déposés aux sha annoncés **par `diff`, sur clone neuf** ; vérification du
token à **0** dans l'arbre, `.git/config`, les messages **et le contenu de TOUS les blobs**
(`git rev-list --objects --all`) ; **révocation MESURÉE par un 401 sur `api.github.com`** — ne pas
la demander. **Un token par dépôt.** Autres : **lire pour présenter n'est pas ouvrir** · **une
divergence se nomme et se tranche par l'opérateur** · **borner AVANT de lire**.

## §8. G-4 — SOLDÉ, et BORNÉ EN S19

> Le **git** est l'espace de consignation et **FAIT FOI** pour la gouvernance et les résultats,
> **plus le matériel permettant à un tiers de REPRODUIRE**. La **KB active** est l'espace vivant,
> **borné aux INTRANTS depuis S19**. **Bascule** à l'épuisement d'une branche, après **audit froid
> incognito**. **Portée PROSPECTIVE : l'existant reste en place.**

Le journal V94 **reste mount-seul de droit** : sa fourniture ponctuelle a soldé une **vérification**,
pas ouvert un dépôt. **G-4 est clos** ; la **migration de `kb/` reste bloquée sur son volet 3**.

## §9. Table de supersession — ce qui a été ÉCARTÉ

| Point | Ancien (périmé) | Retenu S19 |
|---|---|---|
| HEAD attendu | commit « Reprise S18 » | **commit « Reprise S19 », vérifié par `git log`, SANS présumer qu'il est HEAD** |
| `audit/` | 62 | **68** |
| Racine | note S18 + PROMPT-S19 | **note S19 + PROMPT-S20**, 4 fichiers |
| Régime des pièces | byte-intactité pour toutes | **SCELLÉ byte-intact / OPÉRATIONNEL recalé en place** |
| Attendus du §0-lite | nombres | **nombres + commande littérale** |
| Gardes | `N mordantes` | **`N mordantes` + `M vacantes`** |
| Anticipations | écrites dans la note | **en ENVELOPPE, sha cité, contenu non lu avant dépôt du cadrage** |
| Dépôts | quatre (`LC-CONST-V1` §2, sans le git) | **CINQ, le git y entre et FAIT FOI** |
| R-54 | le mount est autoritaire | **BORNÉ AUX INTRANTS** |
| KB active | 27 fichiers, ZIP-OCR, hachage nul | **7 fichiers, 4 vrais PDF, CONFRONTÉS 4/4 AU BIT** |
| Cible KB active | 25–35 fichiers | **PÉRIMÉE — le strict nécessaire, sans plancher** |
| Ouverture | « mesure avant de lire » | **deux messages ; attendus placés APRÈS l'ordre de mesure** |
| `G-5b` | `LC-00-INDEX` absent | **CLOS, déposé en S18** |

## §10. AUDIT DE REPORT — S19, item par item, AVANT retrait

Vérifié dans les pièces **effectivement déposées**, non par déclaration.

### A. `NOTE-REPRISE-GIT-S18.md` — RETIRÉE de la racine, conservée dans l'historique git

Reporté ici intégralement : §0 attendus et recalages → §0, **recalés** · §0.1 les 12
redémonstrations et leur décomposition → §0.1 · §0.2 les cinq rejeux → §0.2 · §0.3 intrants →
§0.3 · §0.4 surfaces → §0.4, **RECALÉ par mesure** · §0.5 leçons → §0.5, **augmentées de trois** ·
§1 historique → §1, **prolongé à S19** · §2 P-0 et la réserve à cinq points → §2 · §2.4 réserve
permanente → §2.3 · §3 `S-B1`, répartition, antériorité, levier, arbitrages → §3 · §4 paquet β et
journal V94 et cinq corps → §4 · §5 P-8/P-9 → §5 · §5bis norme de nommage → §5 · §5ter S18 →
§5ter.1 · §6 restes à faire → §6.3, **recalé sur quatre lignes** · §6.4 restes de fond → §6.4,
**inchangés** · §7 précédents S8–S18 → §7.1–7.6, **intégralement** · §7.9 R-55 → §7.7, **précisée
de la révocation mesurée** · §8 G-4 → §8, **borné** · §9 supersession → §9, **recalée** · §10 et
§10bis audits de report → absorbés par le présent §10 · §10bis C absorption V96 → §5bis,
**intégralement** · §11 périmètre → §11.
**Aucun item écarté sans être recopié.**

**QUATRE DÉFAUTS D'ÂGE DE LA NOTE S18, nommés et NON reconduits** : titre H1 « Note de reprise
S17 » · §0 titré « RECALÉS EN S17 » alors qu'il portait le recalage S18 · §9 portant `audit/ 55` et
une racine périmée, contredits par son propre §0 · **§6.3, quatre lignes contredites par son propre
§5ter** (`LC-00-INDEX` ABSENT, `G-1` non fourni, sort de `R-23` MAINTIEN, `sources/` NON ARBITRÉ).
**Sous le correctif 2, ils ne sont pas amendés par fichier séparé : ils sont recalés.**

### B. `PROMPT-OUVERTURE-S19.md` — RETIRÉ de la racine au même commit

Ses §1 à §10 sont portés par la présente note ou par `PROMPT-OUVERTURE-S20.md`. **Ce prompt n'a
présenté AUCUN défaut d'âge** : son attendu de HEAD était juste, sa chaîne de dix commits
intégralement présente et **démarrant bien à HEAD**, ses sept comptes exacts, son sceau et son
inventaire conformes. **C'est le premier prompt d'ouverture sans défaut d'âge depuis S16.** Le seul
écart de l'ouverture est du pilote : **l'inversion d'ordre**, et elle est **structurelle** (§5ter.2).

### C. Écarts S19 imputables au pilote — trois, portés

1. **Ordre d'ouverture inversé.** Prompt lu avant mesure de HEAD, garde anti-ancrage non armée.
   **Cause structurelle établie** : le prompt est le seul objet qui nomme le dépôt. Correctif 1
   déposé. Sans effet sur le résultat ; écart quand même.
2. **Consigne de retrait donnée par PROPRIÉTÉ et non par nom** — « les 3 ZIP-OCR » dans une surface
   où les sept `.pdf` étaient tous des ZIP-OCR. A conduit au retrait de `B2`, `B3`, `B4` au lieu des
   trois duplicatas. **Conséquence nulle** — l'opérateur a replacé les vrais PDF, meilleurs — mais
   l'écart tient. Même classe que le défaut « sort de R-23 » du prompt S18.
3. **Question posée à l'opérateur sur un fait mesurable**, deux fois : la révocation d'un token,
   alors que `api.github.com` est dans l'allowlist et que S15 avait établi la méthode du 401.

### D. Écarts S19 NON imputables au pilote

4. **Quatre défauts d'âge de la note S18** (§10 A).
5. **Divergence de provenance 622 / 626 objets** entre la note S18 §5ter.1 et le registre de la
   discussion S18. **Le déposé fait foi : 622.** Nommée, non résolue.
6. **« `NOTE-REPRISE-V96` citée 2 fois » au manifeste** : mesuré **2 lignes, 3 occurrences**. Vrai
   sous `grep -c`, faux sous `grep -o`. Nommé, non résolu.
7. **Divergence de deux surfaces sur `R10-REDEMONSTRATION.md` et `redemo_R10_nonlin.py`**,
   cosmétique et non sémantique, **qu'aucun instrument du dépôt ne pouvait voir**. Résolue par
   retrait ; la classe reste, et son instrument est une dette (§6.3).

## §11. PÉRIMÈTRE — INCHANGÉ

S19 a produit de la **MÉTHODE** et **une confrontation d'octets**, aucun mouvement scientifique :
aucune gate tirée, aucun verdict touché, aucune source consommée en substance, aucun sceau modifié.

`{ A4 ; A2★ ; N }` **INCHANGÉ** · `[B]` = B-PAUVRE · `W2` = DÉLIMITATION, `A4` **NON** réfuté,
postulat RENFORCÉ · `A2★` décision ouverte, `C7` non levée · `D1` **non clos**, conclusion `D1c`
**INTACTE** · `N` non fixé (≡ Λ, R-53 : **0/4**) · `O₂` **non construit** · β **`T-b`, NON RÉSOLU,
SEUL facteur d'`O₂` ouvert**, DÉBLOQUÉ par P-8 · α = `C1-b` · `G3-a` non levé · nœud (i)
**INDÉTERMINÉ** (pas A) · Silo R **CLOS à 12/12** · **CCC non démontrée NI réfutée.**

Plafond réaliste de β : **DÉLIMITATION (`T-b`)**, rendement **EN BAISSE**. `T-a` exigerait la carte
shadow renormalisée dS-genuine graviton deux-bords, **NON EXHIBÉE**.

---

*§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, classer, délimiter, arbitrer,
déposer, retirer, recaler, absorber, borner : aucun de ces gestes ne scelle, ne réduit, ne compte,
ne démontre quoi que ce soit. Un sha256 atteste des octets, jamais un titre, des auteurs, un DOI ni
un grade. Une confrontation 4/4 au bit atteste que les octets sont ceux du registre, jamais que le
classement rendu sur un autre canal était juste. Six correctifs de méthode ne rapprochent d'aucune
physique — ils rendent seulement le prochain geste moins susceptible d'être faux. β `T-b`, non
résolu, SEUL facteur d'`O₂` ouvert. **CCC n'est ni démontrée ni réfutée.***
