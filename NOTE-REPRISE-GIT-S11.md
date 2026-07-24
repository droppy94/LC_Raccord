---
id: NOTE-REPRISE-GIT-S11
titre: "Note de reprise autoportante — fin de session S11 (2026-07-24) : VOLET 1-bis clos et déposé ([D5] LEVÉ, verdict W3). Volets 2 et 3 INTACTS, non entamés. Prochain geste : S12 s'ouvre sur le VOLET 2, présentation atouts/inconvénients du Silo P avant arbitrage."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-24
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S11 » ; le vérifier par git log, JAMAIS par cette note."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise, au git comme au mount. Les notes S1–S10 sont retirées de la racine et vivent dans l'historique git. Tout ce qui n'est pas réalisé en reprise N est REPORTÉ en reprise N+1 — jamais laissé en coexistence."
autorite: "Pour les pièces de GOUVERNANCE (prompts d'ouverture, notes de reprise, amendements de l'un ou l'autre), le DÉPÔT GIT FAIT FOI. Le mount vaut copie de travail. Ceci ne tranche PAS G-4 : pour la KB scellée, le mount reste autoritaire (R-54) et le git reste miroir vérifiable."
---

# Note de reprise S11 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -9   # attendu : HEAD = « Reprise S11 … », puis
                           #   63cac9f, 860c3f8, 3419d49, ccceb6c,
                           #   d43572a, 78e0ff3, 22a87c1, 9c22290
    ls instruments/*.py | wc -l                    # attendu : 33 (INCHANGÉ)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76 (INCHANGÉ)
    ls audit/ | wc -l                              # attendu : 42  <-- CHANGÉ
                                                   #   (36 en S10, + les 5 pièces
                                                   #    du volet 1-bis, + la
                                                   #    norme de nommage)
    ls kb/*.md | wc -l                             # attendu : 215 (INCHANGÉ)
    ls hors-KB/B/ | wc -l                          # attendu : 4 (INCHANGÉ)
    ls sources/ | wc -l                            # attendu : 4 (hors compte)
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE /
                                                   #   76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre    # sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py               # 35/35 PASS +  5 cons.
    python3 instruments/redemo_R5_reductions_b.py       # 17/17 PASS +  5 cons.
    python3 instruments/redemo_R3_spectre.py            # 16/16 PASS +  6 cons.
    python3 instruments/redemo_R6_nongauss.py           # 16/16 PASS +  6 cons.
    python3 instruments/redemo_R2_D1.py                 # 12/12 PASS +  8 cons.
    python3 instruments/redemo_R12_O2.py                # 11/11 PASS +  7 cons.
    python3 instruments/redemo_R1_moduleA.py            #   6/6 PASS +  3 cons.
    python3 instruments/redemo_R8_A2star.py             # 21/21 PASS + 10 cons.
    python3 instruments/redemo_R10_nonlin.py            # 40/40 PASS + 14 cons.
    python3 instruments/redemo_R7_A4QW.py               # 45/45 PASS + 10 cons.
    python3 instruments/redemo_R9_tracteur.py           # 16/16 PASS +  8 cons.
    python3 instruments/redemo_R11_falsifiabilite.py    # 36/36 PASS + 19 cons.

**Total attendu : 271/271 PASS + 101 consignations, 12/12 rc = 0. INCHANGÉ.**
Aucune des six pièces déposées en S11 n'est un instrument.

**L'addition est DÉCOMPOSÉE, pas supposée** — REJOUÉE en S11 sur clone neuf et
recomptée DEUX fois de façon indépendante (grep au motif tolérant sur les logs,
et ligne de bilan propre à chaque instrument), les deux comptes concordant lot
par lot :

    PASS  : 35 + 17 + 16 + 16 + 12 + 11 + 6 + 21 + 40 + 45 + 16 + 36 = 271
    CONS. :  5 +  5 +  6 +  6 +  8 +  7 + 3 + 10 + 14 + 10 +  8 + 19 = 101

Hors compte §0-lite, trois rejeux de confirmation, tous CONFORMES en S11 :

    python3 instruments/harnais_R9.py     # « HARNAIS R-9 : 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py    # « HARNAIS R-11 : 7/7 mordantes »
                                          #   + « aucun assert sans porteur mutable »
                                          #   + « VACANTES detectees : 0 », rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py    # rc=0, sha8=8e386686

Les cinq sceaux ARCHIVE de R-11, sha8 CONFRONTÉS en S11 et concordants (non
rejoués, jamais deux dans le même arbre) : `verif_F1_spn` 19a4931e ;
`verif_F4_principiel` 9947b8ed ; `verif_F5_scaling` a959f137 ;
`verif_F6_memoire_cisaillement` 23a7d264 ; `verif_D3_WCH_GWE` 664660ee.

Tout écart est à décomposer AVANT de poursuivre (leçon V62).

### Leçons d'environnement opposables

Toutes celles de S2–S10 MAINTENUES, et toutes revérifiées en S11 :
rejeu long en `setsid nohup` ; répertoire de logs créé en appel séparé ;
`ls audit/` et non `ls audit/*.md` ; jamais deux sceaux en concurrence ; les
durées ne se reportent pas et ne sont pas des clés de sceau ;
`origin/front-pq` résiduelle, ne pas toucher ; `inventaire_sceaux.py` réécrit
sa ligne de date (**survenu en S11**, restauré par `git checkout --`) ; DEUX
formats de marqueur, recompte au motif tolérant `^\s*\[?PASS\]?`
(**confirmé en S11**) ; `harnais_R11.py` crée `instruments/__pycache__/` en
`?? ` (**survenu en S11**) ; `[p]ython3` ne protège pas du shell englobant ;
`simplify` non borné ; l'allowlist réseau ne couvre pas arxiv.org.

**NOUVELLE — S11, outillage :** `pdfplumber` 0.11.9, `pdftoppm`/`pdfinfo`,
Pillow sont disponibles ; `pymupdf` ne l'est pas. Une extraction de texte
bornée à une boîte (`page.crop(bbox).extract_text()`) et un recadrage raster
aux mêmes coordonnées réalisent le MÊME bornage ; la seconde sert de contrôle
de transcription. Sur les mathématiques affichées, `extract_words` est
mensonger et il faut descendre au niveau `chars`.

## 1. Ce qui a été fait en S11 (sur GO opérateur, R-55 tenu)

1. **§0-lite S10 rejoué CONFORME sur toute la ligne**, aucun écart :
   271/271 PASS, 101 consignations, 12/12 rc = 0, comptes 33/76/36/215/4,
   inventaire 6/76/1, sceau 051e2833, trois rejeux de confirmation conformes.
   Intrants du volet 1 CONFRONTÉS aux sha de première mesure : `04d9b4f4`
   (1 895 152 o) et `27a94980` (2 332 898 o), **concordants**.
2. **VOLET 1-bis CLOS ET DÉPOSÉ** (`63cac9f`) — **[D5] LEVÉ, VERDICT W3.**
   Voir §2.
3. **Norme de nommage** rédigée et déposée **au statut PROPOSITION**, non
   arbitrée. Voir §4.
4. Le commit qui dépose la présente note (swap −S10 +S11).

## 2. VOLET 1-bis — [D5] levé, verdict W3

**« 900 ± 700 » et le σ = O(500) du correctif R-23 ne sont PAS la même
quantité.** Tranché NÉGATIVEMENT, par ABSENCE DE RÉFÉRENT.

**Le fait décisif.** Table II de 2312.12498v2 **PORTE une convention d'unité**
— contrairement à ce qu'annonçait le prompt S11. Elle n'est ni dans la légende
ni dans les cellules : elle est dans les **EN-TÊTES DE COLONNES**, qui tabulent
`10⁻² f_NL^{ttt,+}` | `10⁻² f_NL^{ttt,−}` | `10⁻² f_NL^{ttt}`. Le nombre
imprimé vaut 10⁻² f_NL : **f_NL = 100 × la valeur tabulée**. L'extraction en
flux ne restitue pas cette ligne comme un en-tête, d'où le constat d'absence
des sessions antérieures.

**Panneau inférieur** (Planck 2018, pipeline SEVEM), lu en périmètre :

    T only     4 ± 17     90 ± 100     6 ± 16
    E only    75 ± 75   −790 ± 830    70 ± 75
    T + E     16 ± 14      2 ± 20     13 ± 12

Dispersions : 12 à 830 en tabulé, 1 200 à 83 000 en f_NL. **Aucune dispersion
d'ordre 500 à l'une ou l'autre normalisation** (la plus proche est 1 200 en
f_NL, 12 en tabulé). [D5-d] négatif ⟹ W3 par l'ordre de résolution FIGÉ au gel
avant lecture.

**Gel `bd0b40c8`** figé AVANT toute lecture, antériorité prouvée par l'état du
répertoire (le gel seul, aucune coupe, aucun rendu), **byte-intact de bout en
bout**, re-vérifié après chaque écriture. Espace-verdict à CINQ cases
pré-déclaré, incluant la case « aucune des deux lectures » ; aucune case
ajoutée après mesure. Plafond CONSTAT SUR PIÈCES LOCALES annoncé au gel,
atteint, non dépassé. Comparateur Table III de 2409.10595v2 autorisé mais
**NON CONSOMMÉ**.

### 2.1 QUALIFICATION DE V6 — V6 n'est PAS rouvert

V6 a tranché la **LITTÉRALITÉ** et reste vrai comme tel : la chaîne
« 900 ± 700 » ne s'imprime pas dans Table II. Mais sous la convention mesurée
en S11, le fiduciaire ttt équilatéral, mesuré **± 7** en S10, vaut **± 700 en
f_NL** — la seconde moitié exacte de « 900 ± 700 ».

**La QUANTITÉ que F2 situe en Table II s'y trouve ; c'est sa CHAÎNE qui ne s'y
trouve pas.** V6 ne réfute pas la substance et NE DOIT PAS être reporté comme
s'il le faisait. La valeur centrale 900 n'est pas reconstructible en périmètre.

### 2.2 Ce que le verdict ne dit pas

Le **FOND de R-23** reste ni confirmé ni infirmé : le côté R-23 n'a jamais été
ouvert, il n'entre que tel que le prompt le rapporte (une dispersion d'ordre
500, sans template, sans statistique, sans normalisation déclarés). Corps ET
front-matter de F5 **JAMAIS ouverts**. L'origine du « O(500) » n'est ni mesurée
ni affirmée.

**[D5-a] partiellement NON MESURABLE** (clause I-c pré-déclarée) : le bloc
d'affichage de l'équation (10) livre une structure d'HÉLICITÉ (trois δ^K fixant
λᵢ = +2, trois tenseurs de polarisation contractés cycliquement) ; sa
dépendance en FORME est hors coupe. [D5-b] non atteint, l'ordre gelé ne
l'appelle pas.

## 3. Écarts de S11 — six, décomposés

1. **§5.5 du gel DÉGÉNÉRÉ.** La borne « première ligne à la marge gauche du
   corps » désignait l'équation elle-même (301,7 pt contre marge 302,0).
   Nommée, amendement 1.
2. **DÉBORDEMENT n° 1** : ligne fiduciaire du panneau SUPÉRIEUR de Table II,
   lue en croyant couper les en-têtes, alors que les filets déjà mesurés
   disaient qu'elle était sous le filet d'en-tête. **CONSIGNÉE, NON EMPLOYÉE.**
   Le verdict n'en dépend pas.
3. **AMENDEMENT 2 FAUX, ET AGGRAVANT.** Son critère (« la prose atteint la
   marge de justification ») classait comme affichage la DERNIÈRE ligne d'un
   paragraphe, qui par construction ne l'atteint pas. Il a élargi la coupe au
   lieu de la borner. **Rétracté par l'amendement 3**, jamais modifié en place.
4. **DÉBORDEMENT n° 2** : deux lignes de prose précédant l'équation (10),
   entrées par cette coupe élargie. **CONSIGNÉES, NON EMPLOYÉES.**
5. **UNICITÉ DE LA REPRISE NON TENUE AU MOUNT.** Mesuré par listing en S11 :
   `/mnt/project` porte `NOTE-REPRISE-GIT-S9.md` ET
   `NOTE-REPRISE-GIT-S9-AMENDEMENT-1.md`, et **ne porte pas** la note S10. Deux
   pièces de reprise coexistent au mount, et ce sont les périmées. Sans effet
   sur les attendus (le git fait foi pour la gouvernance), mais c'est
   l'incident S9 reparu de l'autre côté du canal.
6. **LA SURFACE DU MOUNT A CHANGÉ DE NATURE.** Fait DÉCLARÉ, **NON EMPLOYÉ** :
   `/mnt/project` expose désormais des entrées `.pdf` directes pour les trois
   sources, là où S10 a mesuré des archives ZIP de rendu page à page sans
   aucune entrée PDF. Aucun sha n'a été calculé au mount. La prémisse du volet
   3 (« la confrontation octet est impossible par construction si le mount ne
   livre qu'un rendu ») repose donc sur un état qui n'est peut-être plus celui
   d'aujourd'hui. **À mesurer sous le GO du volet 3, pas avant.**

Les quatre premiers sont imputables au pilote. **Quatre occurrences de la même
leçon de bornage dans un seul volet, dont une où ma correction a aggravé le
défaut qu'elle prétendait corriger** — et cela APRÈS avoir recopié la leçon S10
dans mon propre gel.

## 4. Norme de nommage — PROPOSITION déposée, NON ARBITRÉE

Demandée par l'opérateur en S11 (« ce n'est pas l'opérateur qui choisit les
noms de fichiers, ce sont les sessions, et c'est la foire »). Constat mesuré
sur `audit/` : le mot de TYPE change de position (`GEL-R11.md` /
`CSE-R4R5-GEL.md`) ; deux notes d'adjudication de même famille ont l'ordre
INVERSE l'une de l'autre ; un fichier sur 41 est en snake_case.

Grammaire proposée : **`<SUJET>-<TYPE>[-AMENDEMENT-<n>].<ext>`**, sujet en
tête, type en queue, tiret seul séparateur, ASCII majuscules, vocabulaire de
TYPE **fermé**, version en front-matter et jamais dans le nom, et une règle
mécaniquement vérifiable : **le nom sans extension est identique au champ
`id:`**. Deux exceptions NOMMÉES (`PROMPT-OUVERTURE-S<n>`,
`NOTE-REPRISE-GIT-S<n>`), maintenues parce qu'elles sont citées littéralement
par la règle d'unicité et le piège R-36.

**Non arbitrée. Elle ne renomme rien.** La migration porterait sur 7 pièces de
`audit/` ; 22 sur 41 sont déjà conformes. **`kb/` est EXCLU** : la KB scellée
est sous R-54, le mount autoritaire et le git miroir — renommer côté miroir
romprait la relation de miroir. Une migration de `kb/` est **bloquée sur G-4**.

Défaut connu et assumé : la norme elle-même ne respecte pas sa grammaire
(`LC-NORME-NOMMAGE.md` devrait être `NOMMAGE-NORME.md`). Soumis, non tranché.

## 5. Ce qui reste — REPORTÉ EN S12, rien n'est perdu

- **SORT DE R-23** (maintien / amendement / retrait). GO séparé. Suppose
  l'ouverture du corps de F5 — **voie (i), jamais d'office**.
- **VOLET 2 — SILO P, arbitrage**, précédé de la PRÉSENTATION atouts /
  inconvénients demandée par l'opérateur. β / P-1 (cartographie v1.2 : β#1
  maintenu) VS report modulaire d = 3 / P-3 (recommandation #1 des decks).
  Tracker R-53 : 0/4. Pièces autorisées à la lecture bornée, **MESURÉES en S11
  au niveau du contenant, JAMAIS OUVERTES** : `kb/LC-07-CARTOGRAPHIE.md`
  (9 208 o, 205 lignes) et `kb/LC-WORK-CARTOGRAPHIE-PRIORITES.md` (20 499 o,
  181 lignes).
- **VOLET 3 — SOLDES DE GOUVERNANCE.** G-1 solde (16 bundles de la décharge
  v2.74, 72 .py ; `hors-KB/A/` non fourni — RECONFIRMÉ en S11 : `hors-KB/` ne
  contient que `B`) · G-4 (autorité mount vs git ; voir l'écart 6 du §3) ·
  G-5b/c (index `LC-00-INDEX` — RECONFIRMÉ en S11 : **ABSENT de `kb/`**) ·
  PDF du mount, 5014 Ko annoncés, vs `sources/2503_19957v1.pdf`, **910 410 o,
  sha8 113ab4a2, MESURÉS au git en S11**.
- **ARBITRAGE DE LA NORME DE NOMMAGE**, et le cas échéant migration des 7
  pièces de `audit/` — geste distinct, jamais tacite.
- **RÉVOCATION DU TOKEN S11**, à la main de l'opérateur.

## 6. Périmètre — INCHANGÉ

Le volet 1-bis n'a retiré aucune inconnue : ce n'était pas un lot, son plafond
était CONSTAT SUR PIÈCES LOCALES, et il n'a produit qu'une désignation
documentaire.

`{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · **D1 non
clos**, conclusion **D1c intacte** · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) · **CCC
non démontrée NI réfutée**.

**Silo R : clos à 12/12**, INCHANGÉ.

## 7. Règles et précédents arrêtés en S11 — opposables

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.**
   Quatre occurrences en un volet. Écrire la règle ne suffit pas : il faut
   IMPRIMER les coordonnées retenues et le dernier élément inclus, et
   CONSTATER qu'il appartient au bloc visé.
2. **UNE CORRECTION PEUT ÊTRE FAUSSE.** Elle se rétracte par un fichier séparé
   daté supplémentaire ; l'amendement fautif RESTE au dépôt et garde son
   numéro. On ne modifie pas un amendement, même erroné.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.** Il peut clore un
   verdict sans que tous les discriminants soient atteints, et c'est légitime :
   le réordonner après mesure serait le fit qu'il interdit.
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.** Une
   convention d'unité peut vivre dans les EN-TÊTES, invisible à la légende, aux
   cellules, et au flux `pdftotext`. Avant de déclarer qu'une information
   manque, vérifier qu'on l'a cherchée là où elle se loge.
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.** Reporter l'un
   pour l'autre fait circuler une demi-vérité.
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.** Un vocabulaire fermé
   ne s'étend que par amendement à la norme.
7. **R-55 tenu en S11** : annonce chemin + sha256 complet + message, fichier
   par fichier, PUIS token, PUIS push. Les cinq sha déposés ont été confrontés
   par `diff` aux cinq annoncés, sur clone neuf — pas à l'œil.
8. **UN TOKEN NE S'ÉCRIT NULLE PART.** Utilisé en ligne, effacé du disque,
   absent de `.git/config`, des fichiers et du commit — vérifié.
9. Tous les précédents S4–S10 restent PLEINEMENT OPPOSABLES.

---

*§6.4 — rejouer, geler, couper, lire, adjuger, amender, rétracter, normer,
déposer, clôturer : aucun de ces gestes ne scelle, ne réduit, ne compte, ne
démontre quoi que ce soit.*
