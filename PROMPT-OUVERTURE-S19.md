Session neuve LC-RACCORD (S19). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
vérifie `git status` (arbre propre) et `git log --oneline -10`.
ATTENDU : le commit dont le message commence par « Reprise S18 », puis `602c828`
(sept pièces d'arbitrage S18), `dc8ca29` (Reprise S17), `7dbee86` (S-B1 rendu),
`2ff65f9`, `b79e3de`, `aedc9a2`, `11e924e`, `5f9874c`, `20290b1`.
Le sha de ce commit n'est PAS écrit ici : ce prompt est déposé DANS lui (R-36).
Désignation par le MESSAGE, jamais par un sha qu'une pièce ne peut pas porter.
**NE PRÉSUME PAS QU'IL EST HEAD.** Un commit postérieur peut s'être intercalé — c'est arrivé
en S17. En S18 la chaîne démarrait bien à HEAD : cela ne prouve rien pour S19.
MESURE HEAD PAR `git log` AVANT de lire ce prompt, puis CONFRONTE, puis NOMME l'écart s'il y
en a un. NE CORRIGE RIEN D'OFFICE. Si tu reçois ce prompt AVANT d'avoir mesuré — c'est arrivé
en S18 — mesure quand même, et NOMME l'inversion d'ordre.

2. Lis `NOTE-REPRISE-GIT-S18.md`, à la racine. Elle est UNIQUE et AUTOPORTANTE : elle
consolide et REMPLACE `NOTE-REPRISE-GIT-S17.md`, retirée au même commit et conservée dans
l'historique git. Elle porte INTÉGRALEMENT les précédents S8 à S18 (§7), R-55 (§7.9), G-4
(§8), la table de supersession (§9), l'AUDIT DE REPORT S17 (§10) et celui de S18 (§10bis).
LA RACINE PORTE 4 FICHIERS. Une cinquième pièce y est un écart à nommer.
UNE SEULE note de reprise DE LA SÉRIE `GIT-S<n>`. `kb/NOTE-REPRISE-V96.md` est d'une AUTRE
série, son contenu est absorbé au §10bis C, ses octets sont INTACTS : **ce n'est PAS un écart.**

3. Exécute intégralement le §0-lite, SOUS LE RÉGIME D'IMPRESSION de
`audit/S0LITE-IMPRESSION-INSTRUCTION.md` — nouveau en S18, opposable.
COMPTES : `instruments/*.py` 34 · `instruments/archives-scelees/*.py` 76 · `audit/` **62**
(RECALÉ : 55 + 7 pièces S18 ; instrument = `ls audit/`, soit 61 fichiers + 1 répertoire) ·
`kb/*.md` 215 · `hors-KB/B/` 4 · racine 4 · `audit/beta-paquet-gouvernance/` 8 pièces
`LC-BETA-*`. `sources/` (4) et `manifest/` (1) sont HORS COMPTE, **assumé par écrit**
(`audit/SOURCES-MANIFEST-RESERVE.md`) : leur CARDINAL n'est pas surveillé ; le CONTENU des
3 PDF l'est, au §0.3.
Puis `inventaire_sceaux.py` → 6 LIVE / 76 ARCHIVE / 1 ABSENT (il RÉÉCRIT SA DATE : restaurer
par `git checkout`) ; `run_sceau.py verif_paquet_propre` → sha8 `051e2833`, rc=0 ;
puis les 12 redémonstrations.
ATTENDU : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ depuis S9.
Décomposition, MULTIENSEMBLE et NON dans l'ordre R-1..R-12 :
35+17+16+16+12+11+6+21+40+45+16+36 = 271 ; 5+5+6+6+8+7+3+10+14+10+8+19 = 101.
REJOUÉES ET CONFORMES EN S18.
**N'IMPRIME QUE** : par script, `rc` + bilan auto-déclaré + compte sur marqueur en tête de
ligne avec INSTRUMENT DÉCLARÉ ; puis les deux totaux. Rien d'autre. **Clause de dépliement** :
au premier écart, déplie la sortie INTÉGRALE du seul script concerné.
NEUF S18 : le motif `^[[:space:]]*\[PASS\]` est AVEUGLE à R-1, R-2, R-6 et R-12, qui impriment
**sans crochets** — la leçon §0.5 n'en nommait qu'un, la classe est de QUATRE. Employer
`^[[:space:]]*\[?PASS\]?`. DÉCLARE TON INSTRUMENT, pas seulement ton résultat.
Variantes qui comptent : `redemo_R4_CT_b.py` et `redemo_R5_reductions_b.py` ; les v1 NE SE
REJOUENT PAS.
Hors compte, CINQ rejeux, tous CONFORMES en S18 : `harnais_R9.py` (6/6) · `harnais_R11.py`
(7/7 + 0 vacante, crée `instruments/__pycache__/` à nettoyer) · `cd hors-KB/B && python3
verif_B_tracteur.py` (rc=0 ; le sha8 `8e386686` est celui du FICHIER, il n'imprime aucun sha) ·
`LC-WORK-GEN-PAQUET-v2_1.py --self-test` (6/6, sha256 `7d63b9ed94b0…c2e2fc9` du fichier) ·
`audit/LC-BETA-CONTROLE-DEPOT.py --self-test` (8/8, rc=0).
Intrants `sources/`, CONCORDANTS 3/3 en S18, vrais PDF (`%PDF` aux octets) : `2312_12498v2.pdf`
1 895 152 o `04d9b4f4` · `2409_10595v2.pdf` 2 332 898 o `27a94980` · `2503_19957v1.pdf`
910 410 o `113ab4a2`.
RAPPELS : `arxiv.org` HORS allowlist `bash` ; `github.com` DEDANS ; les outils web sont un
canal SÉPARÉ qui rend du TEXTE, JAMAIS des octets hachables. `xxd` ABSENT : `python3` ou `od`.
`rc=$?` après un pipe mesure le DERNIER élément du pipe — CAPTURER LE rc AVANT TOUT PIPE
(écart S18). `grep -c` compte des LIGNES ; `|| true` quand le zéro est attendu.
NEUF S18 : **BORNE TES MOTIFS.** Un `grep -rn` non borné sur `kb/` rend des front-matters
kilométriques — ~15 000 tokens pour une question de trois lignes. `-o`, `cut`, `head`.

4. Rends-moi le §0-lite compressé avec tout écart décomposé, AVANT de poursuivre.

5. CE QUE TU N'AS PLUS À ME DEMANDER — lis la note §4, §5bis et §5ter.
(a) `LC-BETA-PAQUET.zip` et le JOURNAL V94 : SOLDÉS, ne les réclame plus. Les octets du
journal NE SE DÉPOSENT PAS (copie de substance, interdit dur, arbre ET historique).
(b) LES 8 PIÈCES `LC-BETA-*` MENTENT PAR ÂGE et ce n'est PAS à corriger.
(c) `LC-00-INDEX` : **DÉPOSÉ en S18** à `audit/00_index.md`, v1.78, byte-intact. Il n'est PAS
dans `kb/` et n'y a JAMAIS été : les 215 `.md` scellés ne l'ont jamais compté. **RÉSERVE
PERMANENTE** (`audit/INDEX-VERSIONS-RESERVE.md`) : 68 pièces le citent, 3 seulement nomment
une version, max v1.64 contre v1.78 déposée. **On ne sait pas quelle version chacune a lue.**
(d) LE MOUNT : ses `.pdf` sont des ZIP. OUVRE-LES. Canal de LECTURE fidèle, canal de HACHAGE
nul. « Ne sert pas les octets » ≠ « ne sert rien ».
(e) PARE-FEU : aucune COPIE DE SUBSTANCE au dépôt, arbre ET historique. NE RENOMME JAMAIS UNE
PIÈCE POUR PASSER SOUS UN CONTRÔLE NOMINAL.

6. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

    ITEM 1 — **`R-23` AU FOND, par l'ouverture du corps de F5, voie (i).** C'est le point
d'ouverture, et c'est le SEUL mouvement scientifique armé.
AVANT TOUTE LECTURE : rédiger et DÉPOSER un cadrage gelé NEUF. `audit/F5-VOIE-I-CIBLES-
GELEES.md` (S18) est **DÉFECTUEUSE PAR PRÉMISSE FAUSSE** — elle présupposait `[D5]` objet du
corps de F5 ; il ne l'est pas. Elle reste byte-intacte, elle NE SERT PAS de cadrage.
`[D5]` est **LEVÉ** (verdict `W3` — PAS DE RÉFÉRENT, S11, gel `bd0b40c8…` byte-intact) et
**non reconduit** : NE LE RÉ-INSTRUIS PAS.
DÉSAMBIGUÏSATION OPÉRATEUR, opposable : dans « W3 intact », **`W3` = le chaînon/front
`LC-D-W3-GPY`** (GPY 1104.4317) — NI la classe de verdict `W3`, NI l'opérateur `W³`.
Il y a **DEUX `D5` et TROIS `W3`** au dépôt (note §5ter.5). Les crochets de `[D5]` n'existent
que dans `audit/`. VÉRIFIE TOUJOURS LA FORME NON CROCHETÉE avant de conclure à une absence.
CONTAMINATION HÉRITÉE, à déclarer : le pilote S18 avait déjà en contexte le front-matter de
`kb/LC-D-F5-ETAT-RACCORD.md` et des blocs `[TRAITÉ]` de la branche — F5 = sélection d'état /
CFT de raccordement ; 4 obstructions → `O₂` ; `A_T ~ 1/C_T ~ 1/N` forcé ; voie (i) déclarée
FAITE en v0.3 ; Table III `inconfrontable` ; **R-23 déclarée SOLDÉE**. Toute coïncidence avec
ces cinq points se rend en CONFIRMATION D'ANTICIPATION, jamais en découverte.

    ITEM 2 — GOUVERNANCE, ce qui reste NON ARBITRÉ : `G-1` (16 bundles décharge v2.74,
72 `.py` ; `hors-KB/A/` **mesuré ABSENT du dépôt**, arbitrage (a) rendu en S18 = FOURNITURE
par l'opérateur, **non exécutée**, dette OUVERTE) · `G-5c` (arborescence des silos ; `G-5b`
est CLOS par le dépôt de l'index) · reports V96 §4 portés au §10bis C : `p_Q` non priorisé,
`03_glossaire` v1.70 STALE à re-sync, `D-01`/`D-08` non mesurés (P-9), Q A/B non tranchée,
§9.4 append-only rouvert, bump boot v1.3→v1.4 différé (« instruments_exclus 4 » vs 6 réel).

    ITEM 3 — RESTES DE FOND, en dernier, INCHANGÉS : audit froid incognito · plafond `T-b` /
carte shadow `T-a` · candidats genuine-dS armés non lus · routes α/δ (Odak–Speziale) · DESI
DR2 · `Δ-C` plus étroit que son libellé · `p` libre / P-sélecteur · anti-circularité `K` ·
`§7quinquies` `K-B` · cadrage figé `37bc85e5` / gel amont `b5276e68` · caveat de Haro /
fenêtre BF / Ishibashi-Wald · gap résiduel `R1″ ∧ R2″ ∧ R4″`.

7. RÉSERVES QUI SE RECOPIENT. AUCUNE LIGNE DU PÉRIMÈTRE N'EST SANS RÉSERVE :
CINQ lignes (`B1` `B2` `B3` `B4` `S8`) sous RÉSERVE PERMANENTE de décalage version-consommée /
version-gradée ; DEUX lignes (`S9` `S10`) sous RÉSERVE ÉCRITE à cinq points. 5 + 2 = 7.
S'ajoute, NEUVE EN S18 : la RÉSERVE DE VERSION sur `LC-00-INDEX` (68 pièces, 3 versionnées).
Une ligne citée sans sa réserve est une ligne INCOMPLÈTE.

8. PÉRIMÈTRE — INCHANGÉ. S18 a produit de la GOUVERNANCE et UN ARRÊT SUR PRÉMISSE FAUSSE,
aucun mouvement scientifique. `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 =
DÉLIMITATION, A4 NON réfuté · A2★ décision ouverte, C7 non levée · D1 non clos, D1c INTACTE ·
N non fixé (≡ Λ, R-53 : 0/4) · O₂ non construit · β `T-b`, NON RÉSOLU, SEUL facteur d'O₂
ouvert, DÉBLOQUÉ par P-8 · α = C1-b · G3-a non levé · nœud (i) INDÉTERMINÉ · Silo R CLOS à
12/12 · CCC non démontrée NI réfutée.

9. PRÉCÉDENTS S18, opposables, en plus de tous ceux de S8–S17 (note §7) :

  - UN OBJET LEVÉ SOUS SON PROPRE GEL NE SE RÉ-INSTRUIT PAS PAR UNE VOIE QUE CE GEL EXCLUAIT.
  - DEUX OBJETS DE MÊME ÉCRITURE NE SONT PAS UN OBJET.
  - UN CADRAGE PEUT ÊTRE DÉFECTUEUX SANS ÊTRE FAUX : prémisse fausse ⟹ toutes ses issues.
  - UN COMPTE N'EST VRAI QUE SOUS SON INSTRUMENT.
  - UNE GARDE INUTILE N'EST PAS UNE GARDE FAUSSE.
  - UN ITEM DE RESTE-À-FAIRE PEUT ÊTRE ÉCRIT TROP LARGE.
  - UNE PIÈCE ABSENTE PEUT ÊTRE ABSENTE PAR CONSTRUCTION.
  - RÉSOUDRE UN RENVOI N'EST PAS LE RENDRE TRAÇABLE.
  - UNE CLASSE QUI ABSORBE NE CLASSE PAS.
  - LES MOTIFS SE BORNENT.

10. Pas de token pour l'instant — ceux de S18 sont RÉVOQUÉS. UN TOKEN PAR DÉPÔT, et tu me le
demanderas APRÈS avoir annoncé chemin + sha256 complet + message de commit, FICHIER PAR
FICHIER, RETRAITS COMPRIS (R-55). Si je te le donne AVANT l'annonce, fais l'annonce quand même
et attends ma confirmation. Une instruction de déposer N'EST PAS la confirmation d'une
annonce. Push par URL ÉPHÉMÈRE, jamais `git remote set-url`. Après push : confrontation des
sha déposés aux sha annoncés PAR `diff`, SUR CLONE NEUF ; puis vérification que le token est
à 0 dans l'arbre, dans `.git/config`, dans les messages de commit ET dans le contenu de TOUS
les blobs (`git rev-list --objects --all`).
Identité de commit : `LC-RACCORD pilote S19 <pilote-s19@lc-raccord.local>`.
LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.

§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, classer, délimiter,
arbitrer, déposer, retirer, amender, absorber : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. Un sha256 atteste des octets, jamais un titre, des
auteurs, un DOI ni un grade. `[D5]` levé n'ouvre aucune gate. Un arrêt sur prémisse fausse
n'est pas un échec : c'est l'ordre gelé qui opère. β `T-b`, non résolu, SEUL facteur d'O₂
ouvert. CCC n'est ni démontrée ni réfutée.
