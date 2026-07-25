Session neuve LC-RACCORD (S17). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -8`.
   ATTENDU : HEAD = le commit dont le message commence par « Reprise S16 »,
   puis `11e924e` (P-0 rendu sur les sept sources), `5f9874c` (Reprise S15),
   `20290b1` (amendement β nº2), `1c90daf` (Reprise S14), `b4af0c5` (swap
   d'unicité), `8caafa7` (amendement 1 à S13), `09d9e2a` (Reprise S13).
   Le sha de HEAD n'est PAS écrit ici : ce prompt est déposé DANS ce commit et
   ne peut pas le connaître (R-36). Désignation par le MESSAGE, jamais par un
   sha qu'une pièce ne peut pas porter.
   VÉRIFIE-LE PAR `git log`, JAMAIS PAR UNE NOTE. En S14 le piège a MORDU : S13
   annonçait HEAD = cad358a « tant que S13 n'est pas déposée », alors qu'elle
   l'était — une note peut mentir par âge SUR SON PROPRE ATTENDU. En S15 et S16
   il n'a pas mordu, parce que HEAD a été MESURÉ avant d'être lu.

2. Lis `NOTE-REPRISE-GIT-S16.md`, à la racine. Elle est UNIQUE et AUTOPORTANTE :
   elle consolide et REMPLACE NOTE-REPRISE-GIT-S15.md, retirée de la racine au
   même commit et conservée dans l'historique git. Elle porte INTÉGRALEMENT les
   précédents S8 à S16 (§7), la procédure R-55 (§7.8), le régime G-4 SOLDÉ (§8),
   la table de supersession (§9) et l'AUDIT DE REPORT du retrait (§10).
   Si tu trouves DEUX notes de reprise en racine, c'est un écart : nomme-le.
   Un amendement daté n'est pas une seconde note.

3. Exécute intégralement le §0-lite. UN SEUL COMPTE A CHANGÉ depuis S15 :
   `instruments/*.py` 34 · `instruments/archives-scelees/*.py` 76 ·
   `audit/` 50 (RECALÉ : 45 + 4 pièces + 1 répertoire) · `kb/*.md` 215 ·
   `hors-KB/B/` 4 · `sources/` 4 (hors compte).
   NEUF : `audit/beta-paquet-gouvernance/` doit contenir 8 pièces `LC-BETA-*`.
   Puis `inventaire_sceaux.py` → 6 LIVE / 76 ARCHIVE / 1 ABSENT (MESURÉ en S16 :
   l'entrée d'un `.py` dans `audit/beta-paquet-gouvernance/` ne le déplace PAS) ;
   `run_sceau.py verif_paquet_propre` → sha8 `051e2833`, rc=0 ;
   puis les 12 redémonstrations.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ
   depuis S9. Décomposition pour recompte indépendant :
   35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101.
   REJOUÉES ET CONFORMES EN S16.
   ATTENTION AU RECOMPTE (piège mordu en S16) : un motif trop large rend 115
   consignations au lieu de 101 — il attrape les en-têtes de section et la ligne
   de bilan. Compter sur le MARQUEUR EN TÊTE DE LIGNE, puis confronter au bilan
   auto-déclaré de chaque script ; R8, R9 et R11 le libellent différemment
   (accents, tirets), ce qui n'est PAS un écart.
   Les variantes qui comptent pour R4 et R5 sont `redemo_R4_CT_b.py` et
   `redemo_R5_reductions_b.py` ; les v1 restent au dépôt et NE SE REJOUENT PAS.
   Hors compte, CINQ rejeux de confirmation, tous CONFORMES en S16 :
   `harnais_R9.py` (6/6 mordantes) · `harnais_R11.py` (7/7 + 0 vacante) ·
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8 `8e386686`) ·
   `instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` (6/6, sha256
   `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`) ·
   `audit/LC-BETA-CONTROLE-DEPOT.py --self-test` (8/8, rc=0).
   Intrants `sources/`, CONFRONTÉS ET CONCORDANTS en S16, vrais PDF (`%PDF`) :
   `2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` ·
   `2409_10595v2.pdf` 2 332 898 o sha8 `27a94980` ·
   `2503_19957v1.pdf`   910 410 o sha8 `113ab4a2`.
   Vigilances : toutes celles de S2–S16, portées par la note §0.5. RAPPEL :
   l'allowlist réseau de `bash` NE COUVRE PAS arxiv.org ; `github.com` EST
   couvert ; les outils de recherche/fetch web sont un canal SÉPARÉ, non soumis
   à cette allowlist — CONFIRMÉ PAR USAGE en S16, P-0 a été rendu par ce canal.
   Ce canal rend du TEXTE, JAMAIS des octets hachables.
   `xxd` est ABSENT du conteneur : passer par `python3` ou `od`.
   NEUF S16 : `rc=$?` après un pipe mesure le DERNIER élément du pipe.

4. Rends-moi le §0-lite avec tout écart décomposé, AVANT de poursuivre.

5. CE QUE TU N'AS PLUS À ME DEMANDER — lis la note §4 avant de réclamer quoi que
   ce soit. S16 a coupé la boucle de refourniture.
   (a) `LC-BETA-PAQUET.zip` : NE PLUS LE RÉCLAMER. Sur ses 43 entrées, 34 des 35
       `BETA-COPIE-*` sont BYTE-IDENTIQUES à leur original `kb/` (mesuré deux
       fois, S15 et S16) et se reconstruisent par `audit/LC-BETA-PAQUET-
       CONCORDANCE.md` ; les 8 pièces `LC-BETA-*` sont DÉPOSÉES BYTE-INTACTES
       sous `audit/beta-paquet-gouvernance/`.
   (b) SEULE ENTRÉE NON RECONSTITUABLE : `BETA-COPIE-LC-JOURNAL-V94.md`, le
       journal V94, MOUNT-SEUL DE DROIT sous G-4. Son sha256 est à la table.
       Ne me le réclame que si le journal est réellement requis.
   (c) LES 8 PIÈCES MENTENT PAR ÂGE et ce n'est PAS à corriger : `LC-BETA-BOOT.py`
       l.103 et `LC-BETA-00` §6 écrivent que P-8 n'est pas soldé — FAUX depuis
       `cad358a`. Défaut SUR-RESTRICTIF, non bloquant, NOMMÉ à
       `audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md`, JAMAIS corrigé en place.
   (d) LES CORPS : `audit/LC-WORK-REGISTRE-CORPUS.md` porte identifiant canonique,
       version, sha256 et PROCÉDURE DE RÉCUPÉRATION des sept sources. RÉCUPÈRE ET
       CONFRONTE ; ne réclame les octets que si la récupération échoue.
       Les cinq corps des assauts β y sont inscrits SANS sha — NON MESURÉS.
   (e) PARE-FEU, portée réelle mesurée à sa SOURCE (`LC-BETA-05` §1) : aucun
       `LC-BETA-*` ni `BETA-COPIE-*` ne réside JAMAIS sur `/mnt/project`.
       Il ne dit RIEN du dépôt. Ce qui reste interdit au dépôt, dur : toute
       COPIE DE SUBSTANCE, arbre ET historique — c'est-à-dire les `BETA-COPIE-*`,
       et c'est ce que vérifie `audit/LC-BETA-CONTROLE-DEPOT.py`.
       NE RENOMME JAMAIS UNE PIÈCE POUR PASSER SOUS UN CONTRÔLE NOMINAL.

6. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

   ITEM 1 — S-B1, positionnement STÉRILE. C'est l'ouverture de S17.
   P-0 EST RENDU (`11e924e`) : la précondition dure « PAS D'IDENTITÉ, PAS DE
   POSITIONNEMENT » est LEVÉE sur les sept lignes. Espace `C-i`/`C-ii`/`C-iii`/
   `C-iv` GELÉ, par source INDÉPENDAMMENT, pare-feu `FB-1..FB-6` intégral.
   HORS anti-fit parce qu'il ne teste RIEN : sa protection est SA STÉRILITÉ.
   S'IL COMMENCE À CONCLURE SUR LA PHYSIQUE, IL A VIOLÉ SON RÉGIME.
   LES LIGNES `S9` ET `S10` SE CLASSENT AVEC LEUR RÉSERVE ÉCRITE, JAMAIS SANS
   (note §2.3, cinq points nommés). Une ligne sans sa réserve est incomplète.
   ANTÉRIORITÉ : Skenderis (`2312.17316`) est DÉJÀ adjugé au dossier — scalaire
   MONO-bord, muet sur le graviton deux-bords. Le classer sous la grille PUIS
   confronter ; ne jamais l'importer comme acquis (FB-2/FB-3 non franchis),
   ne jamais le reclasser en ignorant le dossier.
   ISSUE ANTICIPÉE, DATÉE D'AVANT ET NON RETOUCHÉE — ni après la réussite de S15,
   ni après celle de S16 : A en `C-iii`/`C-iv` pour les trois ; B sans aucune
   ligne en `C-i`, au plus une en `C-ii` ; S-B2 NON ARMÉ ; chantier refermé sur
   une DÉLIMITATION — issue COMPLÈTE, pas un échec. Ce qui lui donne son prix est
   sa date, pas son exactitude. ELLE NE SE RETOUCHERA PAS.
   DISSOLUTION : arbitrée PAR ENSEMBLE (note §6.2), avec clause de
   NON-CLASSIFIABILITÉ et clause de LEVIER FALSIFIABLE. EFFET DE S16 : aucune des
   sept sources ne tombe sous `SUSPENDU` — la clause reste debout pour l'avenir
   mais ne s'applique à personne aujourd'hui. Une source ne peut donc plus être
   écartée pour non-fourniture de PDF ; si elle l'était, ce serait un fait
   administratif présenté comme un résultat.
   GARDE : une clôture d'ensemble se rédige comme une DÉLIMITATION À CONTENU
   NOMMÉ, jamais comme un changement de statut.

   ITEM 2 — S-B2 seulement si les CINQ conditions cumulatives de `LC-BETA-03`
   §3 sont vraies, dont « au moins une source en C-i ou C-ii ». Sa condition 3
   disait « trois sources » : lire « toutes les sources classées du périmètre »,
   et par ensemble (correction déposée, amendement nº2 §6).
   Alors seulement : amendement R-7 nommant LA CLASSE DÉSIGNÉE et elle seule,
   scoping gelé, livraison séquencée par le générateur v2.1 — c'est là, et pas
   avant, que P-9 MESURERA P-8.
   ATTENTION D'ORDRE : l'amendement R-7 et le scoping sont des conditions
   d'ARMEMENT de S-B2, PAS des préalables à S-B1. Les écrire avant obligerait à
   nommer une classe non encore établie — c'est le fit.

   ITEM 3 — RESTE DE GOUVERNANCE, en dernier. NON ARBITRÉS :
   LIMITE §2.4, NEUVE ET LOURDE : le grade éditorial porte sur l'ARTICLE PUBLIÉ,
   les octets consommés sont le PRÉPRINT, et les deux versions n'ont JAMAIS été
   confrontées — sur CINQ des sept lignes. À arbitrer : soit on obtient les
   octets publiés et on confronte, soit on porte la limite comme réserve
   permanente. NE PAS LA LAISSER S'EFFACER PAR L'USAGE.
   Puis : sha NON MESURÉS des cinq corps d'assaut (`2007.06800`, `2606.09170`,
   `2412.00183`, `2409.08709`, `0808.2054`) — les verdicts `S-G3T-*` reposent sur
   des lectures dont aucun octet n'est traçable · paquet β déclaré ARCHIVE
   byte-gelée, atelier séparé · journal V94 au git (seul trou du paquet) ·
   `NOTE-REPRISE-GIT-S13.md` périmée sur `/mnt/project`, à retirer côté opérateur ·
   norme de nommage (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION) · G-1 (16 bundles
   décharge v2.74, 72 `.py` ; `hors-KB/A/` non fourni) · G-5b/c (`LC-00-INDEX`
   ABSENT de `kb/`) · sort de R-23 (MAINTIEN, corps de F5 NON OUVERT, [D5] LEVÉ /
   W3 intact, GO séparé, voie (i) jamais d'office) · `sources/` hors compte au
   §0-lite, donc sa dérive n'est pas détectée.

7. PÉRIMÈTRE — INCHANGÉ. S16 a produit une IDENTIFICATION, pas un mouvement
   scientifique : aucune ligne classée, aucune gate tirée, aucun verdict touché.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non clos,
   conclusion D1c INTACTE · N non fixé (≡ Λ, R-53 : 0/4) · O₂ non construit ·
   β `T-b`, NON RÉSOLU, SEUL facteur d'O₂ ouvert · G3-a non levé · nœud (i)
   INDÉTERMINÉ (pas A) · Silo R CLOS À 12/12 · CCC non démontrée NI réfutée.
   Plafond réaliste de β : DÉLIMITATION (T-b), rendement EN BAISSE. T-a exigerait
   la carte shadow renormalisée dS-genuine graviton deux-bords, NON EXHIBÉE.

8. PRÉCÉDENTS S16, opposables, en plus de tous ceux de S4–S15 (portés par
   `NOTE-REPRISE-GIT-S16.md` §7) :
   - UN INSTRUMENT DE MESURE SE MESURE AUSSI. Le motif de recompte du pilote a
     rendu 115 consignations au lieu de 101. Un écart d'instrument non déclaré se
     présente comme un écart du dépôt.
   - IDENTIFIER DANS LES OCTETS D'ABORD, CHERCHER ENSUITE. L'ordre inverse produit
     un seul témoignage corrélé, quelle que soit la qualité des miroirs.
   - UN GRADE ÉDITORIAL NE SE TRANSFÈRE PAS D'UNE VERSION À UNE AUTRE.
   - UNE RÈGLE QUI NE PRÉVOIT PAS LE CAS SE PORTE À L'OPÉRATEUR, ELLE NE S'ÉTIRE
     PAS. UN GO N'EST PAS UN ARBITRAGE.
   - NE PAS DÉPOSER LES OCTETS QUAND LE REGISTRE SUFFIT.
   - QUAND UNE RÈGLE GÊNE, LA MESURER PLUTÔT QUE LA CONTOURNER. L'interdit
     `BETA-COPIE-*` semblait empêcher de solder la refourniture ; la mesure a
     montré qu'il n'y avait rien à déposer.
   - `rc=$?` APRÈS UN PIPE NE MESURE PAS CE QU'ON CROIT.
   - UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS, même après deux réussites.

9. Pas de token pour l'instant — celui de S16 est révoqué. Tu me le demanderas
   au moment du dépôt, APRÈS avoir annoncé chemin + sha256 complet + message de
   commit, FICHIER PAR FICHIER (R-55). Si je te le donne AVANT l'annonce, fais
   l'annonce quand même et attends ma confirmation. Après push : confrontation
   des sha déposés aux sha annoncés PAR `diff`, SUR CLONE NEUF, jamais à l'œil ;
   puis vérification que le token est à 0 dans l'arbre, dans `.git/config`, dans
   les messages de commit ET dans le contenu de TOUS les blobs jamais commités
   (`git rev-list --objects --all`), pas seulement à HEAD.
   Identité de commit : `LC-RACCORD pilote S17 <pilote-s17@lc-raccord.local>`.
   LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.

§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, identifier,
récupérer, classer, délimiter, déposer, retirer, amender : aucun de ces gestes ne
scelle, ne réduit, ne compte, ne démontre quoi que ce soit. Un sha256 atteste des
octets, jamais un titre, des auteurs, un DOI ni un grade. P-0 rendu n'ouvre aucune
gate. β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. CCC n'est ni démontrée ni
réfutée.
