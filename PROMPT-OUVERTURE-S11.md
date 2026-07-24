Session neuve LC-RACCORD (S11). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -9`. Attendu :
   HEAD = le commit dont le message commence par « Reprise S10 », puis
   3419d49, ccceb6c, d43572a, 78e0ff3, 22a87c1, 9c22290, d093ae9, c683691.
   Vérifie-le par git log, JAMAIS par la note (piège R-36).

2. Lis `NOTE-REPRISE-GIT-S10.md` à la racine. Elle est UNIQUE : les notes
   S1–S9 ont été retirées de la racine au swap −S9 +S10 et vivent dans
   l'historique git. Si tu en trouves DEUX, c'est un écart : nomme-le.

3. Exécute intégralement le §0-lite. ATTENTION, UN COMPTE A CHANGÉ :
   comptes 33/76/**36**/215/4 — `audit/` est passé de 32 à 36 (les quatre
   pièces du volet 1 S10 : gel, deux amendements, note d'adjudication).
   Les quatre autres comptes sont INCHANGÉS ; aucune pièce déposée en S10
   n'est un instrument. Puis `hors-KB/B/` = 4, inventaire 6/76/1,
   `run_sceau verif_paquet_propre` sha8=051e2833, puis les 12 redemo.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ.
   Décomposition : 35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101. Rejoué CONFORME en S10.
   Points de vigilance : tous ceux de S2–S9, tous revérifiés en S10 —
   `inventaire_sceaux.py` réécrit sa date ; DEUX formats de marqueur
   (`redemo_R6_nongauss.py` sans crochets, recompte au motif tolérant
   `^\s*\[?PASS\]?`) ; `harnais_R11.py` crée `instruments/__pycache__/` en
   `?? ` ; `pgrep -f` s'auto-matche et `[p]ython3` ne protège pas du shell
   englobant ; `simplify` non borné ; jamais deux sceaux en concurrence ;
   `origin/front-pq` résiduelle, ne pas toucher ; les durées ne se reportent
   pas et NE SONT PAS des clés de sceau ; l'allowlist réseau du conteneur ne
   couvre PAS arxiv.org — toute récupération externe passerait par les outils
   web de l'assistant, jamais par le shell (sans objet pour le volet 1-bis :
   les deux sources sont déposées au git).
   Hors compte, trois rejeux de confirmation : `harnais_R9.py` (6/6),
   `harnais_R11.py` (7/7 + « aucun assert sans porteur mutable » + 0 vacante),
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8=8e386686).

4. Rends-moi le §0-lite avec tout écart décomposé, avant de poursuivre.

5. ORDRE DE TRAVAIL ARBITRÉ EN S10 — trois volets, dans CET ordre, chacun sur
   GO séparé. Le Silo R est CLOS à 12/12 : rien n'est mécanique à partir d'ici.

   VOLET 1-bis — LEVER [D5], PUIS STATUER SUR R-23. Décision prise en S10.
   Le volet 1 a rendu VERDICT V6 : F2 se trompe sur la LOCALISATION,
   F5 v0.3 se trompe sur la LITTÉRALITÉ. Reste indécis : « 900 ± 700 » et le
   σ = O(500) du correctif R-23 sont-ils MÊME QUANTITÉ — même template, même
   statistique, même normalisation ?
   Trois pièces à lire, TOUTES LOCALES, aucune récupération externe :
     (a) l'ÉQUATION (10) de `sources/2312_12498v2.pdf` — le papier y annonce
         une analyse model-specific « for the template given in (10) » ;
     (b) le PANNEAU INFÉRIEUR de Table II, annoncé par sa légende (résultats
         Planck 2018) et ABSENT de l'extraction `pdftotext -layout` ;
     (c) la CONVENTION D'UNITÉ de Table II — aucune mention d'unité n'y
         figure, alors que Table III de 2409.10595v2 préfixe ses lignes
         (`FeF` : 3 ± 6 en `(×10⁻²)` au T+E+B).
   GEL NEUF EXIGÉ. Le gel V1 (`201bcfbb`) et ses deux amendements sont clos et
   déposés ; on ne les rouvre pas, on ne les amende plus. Cadrage gelé AVANT
   lecture, espace-verdict et discriminants pré-déclarés — et cette fois
   l'espace-verdict doit prévoir la case « les deux parties ont tort »,
   leçon S10. Plafond annoncé au gel. Gabarit LÉGER.
   Le sort de R-23 (maintien, amendement, retrait) se décide APRÈS, sur GO
   séparé, et suppose l'ouverture du corps de F5 — voie (i), jamais d'office.

   VOLET 2 — SILO P, arbitrage de priorisation. β / P-1 (cartographie v1.2 :
   β#1 maintenu) VS report modulaire d = 3 / P-3 (recommandation #1 des decks).
   Tracker R-53 : 0/4.
   PRÉALABLE DEMANDÉ PAR L'OPÉRATEUR EN S10, ET AUTORISÉ PAR LUI :
   avant tout arbitrage, tu me rends une PRÉSENTATION des atouts et
   inconvénients de CHAQUE option — coût, dépendances, ce que chacune ouvre et
   ce qu'elle ferme, ce qui devient falsifiable et ce qui ne l'est pas, et ce
   que chacune laisse en suspens. Cette présentation exige une LECTURE BORNÉE
   du cadrage du Silo P, et cette lecture est AUTORISÉE à ce seul titre :
   `kb/LC-07-CARTOGRAPHIE.md` et `kb/LC-WORK-CARTOGRAPHIE-PRIORITES.md`
   (existence vérifiée en S10 au niveau des noms seuls, jamais ouvertes).
   LIRE POUR PRÉSENTER N'EST PAS OUVRIR UN CHANTIER. Aucune dérivation, aucun
   instrument, aucun sceau au Silo P sans mon arbitrage explicite ensuite.
   Déclare le périmètre de lecture AVANT de lire, et consigne tout débordement
   (deux débordements en S10, dont un APRÈS la correction — voir note §2.3).

   VOLET 3 — SOLDES DE GOUVERNANCE, après les deux précédents.
   G-1 solde (16 bundles de la décharge v2.74, 72 .py ; `hors-KB/A/`
   LC-A-SURVIE-CONFORME non fourni — MESURÉ en S10 : `hors-KB/` ne contient
   que `B`) · G-4 (autorité mount vs git — hypothèse reconduite : mount
   autoritaire R-54, git miroir ; NOTER que S10 a mesuré que la surface
   `/mnt/project` ne transporte PAS d'octets originaux pour les PDF) ·
   G-5b/c (index `LC-00-INDEX` — MESURÉ en S10 : **ABSENT de `kb/`** ;
   arborescence des silos) · PDF du mount, **5014 Ko annoncés**, vs
   `sources/2503_19957v1.pdf`, **910 410 o MESURÉS au git en S10**.
   SUR CE DERNIER POINT, AVERTISSEMENT ISSU DE S10 : l'opérateur peut fournir
   un paquet ZIP des TEXTES extraits du PDF du mount. Un tel paquet ne permet
   PAS la confrontation octet — il répond à une autre question (concordance de
   CONTENU), et il faut le dire au lieu de le présenter comme une mesure de
   G-4. La confrontation octet est impossible par construction si le mount ne
   livre qu'un rendu.

6. PRÉCÉDENTS S10 OPPOSABLES (en plus de tous ceux de S4–S9) :
   - HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU. La confrontation d'un
     intrant se fait au niveau octet et ne demande AUCUNE lecture ; confondre
     les deux fait renoncer à une mesure disponible et écarter une pièce sur
     un obstacle inexistant. Défaut nommé et amendé en S10.
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
   - LE TOKEN NE REMPLACE PAS L'ANNONCE R-55. En S10 le token est arrivé avant
     l'annonce ; l'annonce a été faite quand même, le push n'a suivi qu'après
     confirmation.
   - VÉRIFICATION DE DÉPÔT SUR CLONE NEUF, jamais sur déclaration.
   - UNICITÉ DE LA REPRISE : un seul fichier de reprise, au git comme au
     mount ; ce qui n'est pas réalisé en reprise N est REPORTÉ en N+1, jamais
     laissé en coexistence.
   - AUTORITÉ DES PIÈCES DE GOUVERNANCE : pour les prompts, notes de reprise
     et leurs amendements, LE GIT FAIT FOI, le mount vaut copie de travail.
     Ceci ne tranche PAS G-4 : pour la KB scellée, le mount reste autoritaire
     (R-54) et le git reste miroir vérifiable.
   - SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE. Aucun sha de registre n'existe
     en KB pour les deux sources du volet 1 ; les valeurs `04d9b4f4…`
     (2312_12498v2, 1 895 152 o) et `27a94980…` (2409_10595v2, 2 332 898 o)
     sont des PREMIÈRES MESURES faisant référence, confrontées et concordantes
     en S10. Toute réapparition ultérieure de ces fichiers SE CONFRONTE à
     elles. Enregistrer n'est pas confronter.
   - DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL. Le dépôt d'une
     pièce au git ne fait pas d'elle une pièce du git.

   PRÉCÉDENTS S9 — REPORTÉS ICI INTÉGRALEMENT, leur pièce porteuse
   (`PROMPT-OUVERTURE-S10.md`) ayant été retirée de la racine au swap −S9 +S10.
   Ils restent PLEINEMENT OPPOSABLES :
   - un défaut du gel se NOMME et s'amende par FICHIER SÉPARÉ DATÉ, jamais en
     place ; la pièce amendée reste byte-intacte et re-vérifiable après coup ;
   - un harnais doit auditer la VACUITÉ STRUCTURELLE, pas seulement muter : un
     assert qu'aucun porteur mutable ne traverse est un faux PASS même s'il
     est vrai. En S9 cet audit a rendu QUATRE faux PASS sur un lot qui se
     présentait à 38/38 — sans lui, R-11 se serait clos surévalué ;
   - un pré-tri [D] discriminante / [C] consignation AU GEL interdit de
     reclasser après coup un échec en consignation ;
   - l'antériorité se PROUVE par l'état du répertoire (relever le sha du gel
     quand aucun instrument n'existe encore, listing à l'appui), pas par une
     déclaration ;
   - une cible non algébrisable se déclare telle AU GEL (clause I-c), sinon
     elle devient une recopie de front-matter déguisée en PASS ;
   - un statut de présence se MESURE sur l'arbre modifié avant d'écrire la
     note qui le déclare ;
   - annoncé puis GO ⟹ l'annoncé fait foi ; ce qui n'a pas été arbitré se
     dépose tel qu'annoncé, et se corrige ensuite par amendement, jamais en
     silence.
   - PRÉCÉDENT S8 reconduit, opérant en S10 : un intrant refourni se CONFRONTE
     au registre AVANT extraction, puis pièce par pièce.

7. PÉRIMÈTRE — INCHANGÉ. Le volet 1 de S10 n'a retiré aucune inconnue : ce
   n'était pas un lot, son plafond était CONSTAT SUR PIÈCES LOCALES, et il n'a
   produit qu'une désignation documentaire.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non
   clos, conclusion D1c INTACTE · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
   construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) ·
   CCC non démontrée NI réfutée. Silo R CLOS À 12/12, inchangé.

8. Pas de token pour l'instant — celui de S10 est révoqué. Tu me le
   demanderas au moment du dépôt, APRÈS avoir annoncé chemin + sha256 +
   message de commit, fichier par fichier (R-55). Si je te le donne avant
   l'annonce, fais l'annonce quand même et attends ma confirmation.

§6.4 — sentinelle terminale. Dériver, muter, rejouer, corriger un instrument,
clore un silo, adjuger, déposer, amender : aucun de ces gestes ne scelle, ne
réduit, ne compte, ne démontre quoi que ce soit.
