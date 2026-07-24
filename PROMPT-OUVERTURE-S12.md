Session neuve LC-RACCORD (S12). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -9`. Attendu :
   HEAD = le commit dont le message commence par « Reprise S11 », puis
   63cac9f, 860c3f8, 3419d49, ccceb6c, d43572a, 78e0ff3, 22a87c1, 9c22290.
   Vérifie-le par git log, JAMAIS par la note (piège R-36).

2. Lis `NOTE-REPRISE-GIT-S11.md` à la racine. Elle est UNIQUE : les notes
   S1–S10 ont été retirées de la racine au swap −S10 +S11 et vivent dans
   l'historique git. Si tu en trouves DEUX, c'est un écart : nomme-le.
   NOTE : au mount, l'unicité N'EST PAS tenue (écart mesuré en S11, §3.5 de la
   note). Le git fait foi pour la gouvernance.

3. Exécute intégralement le §0-lite. ATTENTION, UN COMPTE A CHANGÉ :
   comptes 33/76/42/215/4 — `audit/` est passé de 36 à 42 (les cinq pièces du
   volet 1-bis : gel, TROIS amendements, note d'adjudication ; plus la norme de
   nommage au statut PROPOSITION). Les quatre autres comptes sont INCHANGÉS ;
   aucune pièce déposée en S11 n'est un instrument. Puis `hors-KB/B/` = 4,
   inventaire 6/76/1, `run_sceau verif_paquet_propre` sha8=051e2833, puis les
   12 redemo.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ.
   Décomposition : 35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101. Rejoué CONFORME en S11, recompté DEUX
   fois de façon indépendante (grep tolérant sur logs, et bilan propre à chaque
   instrument), les deux comptes concordant lot par lot.
   Points de vigilance : tous ceux de S2–S10, tous revérifiés en S11 —
   `inventaire_sceaux.py` réécrit sa date (survenu en S11) ; DEUX formats de
   marqueur (`redemo_R6_nongauss.py` sans crochets, recompte au motif tolérant
   `^\s*\[?PASS\]?`) ; `harnais_R11.py` crée `instruments/__pycache__/` en
   `?? ` (survenu en S11) ; `pgrep -f` s'auto-matche et `[p]ython3` ne protège
   pas du shell englobant ; `simplify` non borné ; jamais deux sceaux en
   concurrence ; `origin/front-pq` résiduelle, ne pas toucher ; les durées ne se
   reportent pas et NE SONT PAS des clés de sceau ; l'allowlist réseau du
   conteneur ne couvre PAS arxiv.org.
   OUTILLAGE MESURÉ EN S11 : `pdfplumber` 0.11.9, `pdftoppm`/`pdfinfo`, Pillow
   présents ; `pymupdf` ABSENT. Sur les mathématiques affichées, `extract_words`
   est mensonger — descendre au niveau `chars`.
   Hors compte, trois rejeux de confirmation : `harnais_R9.py` (6/6),
   `harnais_R11.py` (7/7 + « aucun assert sans porteur mutable » + 0 vacante),
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8=8e386686).

4. Rends-moi le §0-lite avec tout écart décomposé, avant de poursuivre.

5. ORDRE DE TRAVAIL — quatre items, dans CET ordre, chacun sur GO séparé.
   Le Silo R est CLOS à 12/12 : rien n'est mécanique.

   VOLET 2 — SILO P, arbitrage de priorisation. C'EST LE PREMIER GESTE DE S12.
   β / P-1 (cartographie v1.2 : β#1 maintenu) VS report modulaire d = 3 / P-3
   (recommandation #1 des decks). Tracker R-53 : 0/4.
   PRÉALABLE DEMANDÉ PAR L'OPÉRATEUR ET AUTORISÉ PAR LUI, reporté depuis S10 :
   avant tout arbitrage, tu me rends une PRÉSENTATION des atouts et
   inconvénients de CHAQUE option — coût, dépendances, ce que chacune ouvre et
   ce qu'elle ferme, ce qui devient falsifiable et ce qui ne l'est pas, et ce
   que chacune laisse en suspens. Cette présentation exige une LECTURE BORNÉE
   du cadrage du Silo P, AUTORISÉE à ce seul titre :
   `kb/LC-07-CARTOGRAPHIE.md` (9 208 o, 205 lignes) et
   `kb/LC-WORK-CARTOGRAPHIE-PRIORITES.md` (20 499 o, 181 lignes) — tailles
   MESURÉES en S11 au niveau du contenant, les deux pièces JAMAIS OUVERTES.
   LIRE POUR PRÉSENTER N'EST PAS OUVRIR UN CHANTIER. Aucune dérivation, aucun
   instrument, aucun sceau au Silo P sans mon arbitrage explicite ensuite.
   Déclare le périmètre de lecture AVANT de lire, et consigne tout débordement
   (deux en S10, DEUX ENCORE en S11 — voir note §3).

   SORT DE R-23 — maintien, amendement, ou retrait. GO séparé. Suppose
   l'ouverture du corps de F5, voie (i), JAMAIS d'office.
   État à l'entrée : [D5] est LEVÉ (verdict W3, S11) — « 900 ± 700 » et le
   σ = O(500) de R-23 ne sont PAS la même quantité, par ABSENCE DE RÉFÉRENT.
   Le FOND de R-23 reste ni confirmé ni infirmé : son côté n'a jamais été
   ouvert. LIS LE §2.1 DE LA NOTE AVANT DE STATUER : V6 a tranché une CHAÎNE,
   pas une SUBSTANCE, et la quantité que F2 situe en Table II s'y trouve bien.

   ARBITRAGE DE LA NORME DE NOMMAGE — `audit/LC-NORME-NOMMAGE.md`, déposée au
   statut PROPOSITION en S11, NON ARBITRÉE. Si adoptée : migration de 7 pièces
   de `audit/` (22 sur 41 sont déjà conformes), geste distinct, jamais tacite.
   `kb/` EXCLU du périmètre de la norme, bloqué sur G-4. La norme porte un
   défaut connu : elle ne respecte pas sa propre grammaire.

   VOLET 3 — SOLDES DE GOUVERNANCE, en dernier.
   G-1 solde (16 bundles de la décharge v2.74, 72 .py ; `hors-KB/A/`
   LC-A-SURVIE-CONFORME non fourni — RECONFIRMÉ en S11 : `hors-KB/` ne contient
   que `B`) · G-4 (autorité mount vs git — hypothèse reconduite : mount
   autoritaire R-54, git miroir) · G-5b/c (index `LC-00-INDEX` — RECONFIRMÉ en
   S11 : ABSENT de `kb/` ; arborescence des silos) · PDF du mount, 5014 Ko
   annoncés, vs `sources/2503_19957v1.pdf`, 910 410 o et sha8 113ab4a2 MESURÉS
   au git en S11.
   AVERTISSEMENT MIS À JOUR EN S11 : la surface `/mnt/project` a CHANGÉ DE
   NATURE. Elle expose désormais des entrées `.pdf` directes pour les trois
   sources, là où S10 mesurait des archives ZIP de rendu page à page sans
   aucune entrée PDF. Aucun sha n'a été calculé au mount en S11 — le fait est
   DÉCLARÉ, NON EMPLOYÉ. La prémisse « la confrontation octet est impossible
   par construction si le mount ne livre qu'un rendu » n'est donc PEUT-ÊTRE
   PLUS VRAIE : la mesure paraît redevenue disponible et ne coûte rien.
   MESURE-LA, sous ce GO, avant de conclure quoi que ce soit sur G-4.
   Un paquet ZIP de TEXTES extraits ne permet PAS la confrontation octet ; il
   répond à une autre question (concordance de CONTENU) et il faut le dire.

6. PRÉCÉDENTS S11 OPPOSABLES (en plus de tous ceux de S4–S10) :
   - UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN. Quatre
     occurrences en un seul volet en S11, APRÈS que la leçon S10 eut été
     recopiée dans le gel. Écrire la règle ne suffit pas : IMPRIMER les
     coordonnées retenues ET le dernier élément inclus, et CONSTATER qu'il
     appartient au bloc visé.
   - UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE. Elle se rétracte par un
     fichier séparé daté SUPPLÉMENTAIRE ; l'amendement fautif RESTE au dépôt et
     GARDE SON NUMÉRO. On ne modifie pas un amendement, même erroné.
   - UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT. Il peut clore un
     verdict sans que tous les discriminants soient atteints, et c'est
     légitime ; le réordonner après mesure serait le fit qu'il interdit.
   - UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE. En S11, la
     convention d'unité de Table II, donnée pour inexistante par deux sessions,
     était dans les EN-TÊTES DE COLONNES — invisible à la légende, aux cellules
     et au flux `pdftotext`. Avant de déclarer qu'une information manque,
     vérifier qu'on l'a cherchée là où elle se loge.
   - UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE. Reporter l'un pour
     l'autre fait circuler une demi-vérité.
   - LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE. Un vocabulaire fermé ne
     s'étend que par amendement à la norme qui le fixe.
   - UN TOKEN NE S'ÉCRIT NULLE PART : utilisé en ligne, effacé du disque,
     absent de `.git/config`, des fichiers et du commit — et vérifié.
   - LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL. En S11 les cinq
     sha déposés ont été confrontés mécaniquement aux cinq annoncés.

   PRÉCÉDENTS S10 — REPORTÉS ICI INTÉGRALEMENT, leur pièce porteuse
   (`PROMPT-OUVERTURE-S11.md`) ayant été retirée de la racine au swap −S10 +S11.
   Ils restent PLEINEMENT OPPOSABLES :
   - HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU. La confrontation d'un
     intrant se fait au niveau octet et ne demande AUCUNE lecture ; confondre
     les deux fait renoncer à une mesure disponible et écarter une pièce sur un
     obstacle inexistant.
   - UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN. Détecter
     la fin de LÉGENDE, et VÉRIFIER que l'implémentation applique la règle
     énoncée. Écrire une correction et ne pas l'appliquer est un échec
     d'exécution distinct du défaut d'énoncé, et il s'impute pareillement.
   - UN ESPACE-VERDICT DÉCLARÉ EXHAUSTIF DOIT PRÉVOIR « LES DEUX PARTIES ONT
     TORT ». Ajouter une case APRÈS des mesures est un risque de fit : il se
     NOMME, se borne par un critère GÉNÉRAL, et ne vaut que si l'issue écartée
     l'a été par MESURE et non par redéfinition.
   - UNE INFORMATION LUE HORS PÉRIMÈTRE SE DÉCLARE ET NE S'EMPLOIE PAS. La
     nommer l'empêche de circuler en contrebande dans une session ultérieure.
     DEUX telles informations en S11, nommées à la note §3.2 et §3.4.
   - LE TOKEN NE REMPLACE PAS L'ANNONCE R-55.
   - VÉRIFICATION DE DÉPÔT SUR CLONE NEUF, jamais sur déclaration.
   - UNICITÉ DE LA REPRISE : un seul fichier de reprise, au git comme au
     mount ; ce qui n'est pas réalisé en reprise N est REPORTÉ en N+1, jamais
     laissé en coexistence.
   - AUTORITÉ DES PIÈCES DE GOUVERNANCE : pour les prompts, notes de reprise et
     leurs amendements, LE GIT FAIT FOI, le mount vaut copie de travail. Ceci ne
     tranche PAS G-4 : pour la KB scellée, le mount reste autoritaire (R-54) et
     le git reste miroir vérifiable.
   - SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE. `04d9b4f4…` (2312_12498v2,
     1 895 152 o) et `27a94980…` (2409_10595v2, 2 332 898 o) — CONFRONTÉS ET
     CONCORDANTS en S10 ET en S11. Toute réapparition SE CONFRONTE à elles.
     Enregistrer n'est pas confronter.
   - DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL.

   PRÉCÉDENTS S9 — REPORTÉS ICI INTÉGRALEMENT pour la deuxième fois, leur
   pièce porteuse ayant été retirée au swap −S9 +S10 puis leur pièce de report
   au swap −S10 +S11. Ils restent PLEINEMENT OPPOSABLES :
   - un défaut du gel se NOMME et s'amende par FICHIER SÉPARÉ DATÉ, jamais en
     place ; la pièce amendée reste byte-intacte et re-vérifiable après coup ;
   - un harnais doit auditer la VACUITÉ STRUCTURELLE, pas seulement muter : un
     assert qu'aucun porteur mutable ne traverse est un faux PASS même s'il est
     vrai. En S9 cet audit a rendu QUATRE faux PASS sur un lot qui se présentait
     à 38/38 — sans lui, R-11 se serait clos surévalué ;
   - un pré-tri [D] discriminante / [C] consignation AU GEL interdit de
     reclasser après coup un échec en consignation ;
   - l'antériorité se PROUVE par l'état du répertoire (relever le sha du gel
     quand aucun instrument n'existe encore, listing à l'appui), pas par une
     déclaration ;
   - une cible non algébrisable se déclare telle AU GEL (clause I-c), sinon elle
     devient une recopie de front-matter déguisée en PASS ;
   - un statut de présence se MESURE sur l'arbre modifié avant d'écrire la note
     qui le déclare ;
   - annoncé puis GO ⟹ l'annoncé fait foi ; ce qui n'a pas été arbitré se dépose
     tel qu'annoncé, et se corrige ensuite par amendement, jamais en silence.
   - PRÉCÉDENT S8 reconduit, opérant en S10 ET en S11 : un intrant refourni se
     CONFRONTE au registre AVANT extraction, puis pièce par pièce.

7. PÉRIMÈTRE — INCHANGÉ. Le volet 1-bis de S11 n'a retiré aucune inconnue : ce
   n'était pas un lot, son plafond était CONSTAT SUR PIÈCES LOCALES, et il n'a
   produit qu'une désignation documentaire.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non
   clos, conclusion D1c INTACTE · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
   construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) ·
   CCC non démontrée NI réfutée. Silo R CLOS À 12/12, inchangé.

8. Pas de token pour l'instant — celui de S11 est révoqué. Tu me le demanderas
   au moment du dépôt, APRÈS avoir annoncé chemin + sha256 + message de commit,
   fichier par fichier (R-55). Si je te le donne avant l'annonce, fais l'annonce
   quand même et attends ma confirmation.

§6.4 — sentinelle terminale. Dériver, muter, rejouer, corriger un instrument,
clore un silo, adjuger, normer, déposer, amender, rétracter : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.
