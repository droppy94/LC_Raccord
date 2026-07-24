Session neuve LC-RACCORD (S10). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -9`. Attendu :
   HEAD = le commit dont le message commence par « Reprise S9 », puis
   d093ae9, c683691, ea1287d, 54a3a12, 6001027, b24cd65, 7e245d2, f415070.
   Vérifie-le par git log, JAMAIS par la note (piège R-36).

2. Lis `NOTE-REPRISE-GIT-S9.md` à la racine, PUIS
   `NOTE-REPRISE-GIT-S9-AMENDEMENT-1.md` — la note est byte-intacte,
   l'amendement porte la leçon d'environnement manquante.

3. Exécute intégralement le §0-lite : comptes 33/76/32/215/4 + `hors-KB/B/` = 4,
   inventaire 6/76/1, `run_sceau verif_paquet_propre` sha8=051e2833, puis les
   12 redemo. Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0.
   Décomposition : 35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101. Vérifié sur clone neuf après le dépôt S9.
   Points de vigilance :
   - `inventaire_sceaux.py` réécrit sa ligne de date (bénin,
     `git checkout -- audit/INVENTAIRE-SCEAUX.md`) ;
   - DEUX formats de marqueur : `redemo_R6_nongauss.py` imprime `PASS` sans
     crochets — recompte au motif tolérant `^\s*\[?PASS\]?` et son pendant,
     sinon un lot conforme sort à 0/0 ;
   - `harnais_R11.py` crée `instruments/__pycache__/` (entrée NON SUIVIE,
     `?? `, pas un `M`) — `rm -rf instruments/__pycache__` après le rejeu ;
   - `pgrep -f` s'auto-matche ; ET le motif `[p]ython3` ne protège PAS du
     shell englobant (la ligne de commande du `/bin/sh -c` parent contient
     la chaîne cherchée) — sonder dans un appel SÉPARÉ et court ;
   - un `simplify` non borné peut coûter 14 min là où substituer la
     contrainte d'abord coûte 1,6 s ;
   - jamais deux sceaux en concurrence dans le même arbre ; les durées ne
     sont pas des clés de sceau ; `origin/front-pq` résiduelle, ne pas toucher.
   Hors compte §0-lite, trois rejeux de confirmation :
   `harnais_R9.py` (6/6 mordantes), `harnais_R11.py` (7/7 mordantes + « aucun
   assert sans porteur mutable »), `cd hors-KB/B && python3 verif_B_tracteur.py`
   (rc=0, sha8=8e386686).

4. Rends-moi le §0-lite avec tout écart décomposé, avant de poursuivre.

5. ORDRE DE TRAVAIL ARBITRÉ EN S9 — trois volets, dans CET ordre, chacun sur
   GO séparé. Le Silo R est CLOS à 12/12 : aucun lot de redémonstration ne
   reste, rien n'est mécanique à partir d'ici.

   VOLET 1 — RÉOUVERTURE CIBLÉE F2/F5 sur la consignation (a) de R-11.
   Objet : deux têtes du dépôt se contredisent sur un même chiffre.
   `LC-D-F2-TTT-PLANCK` porte « f^ttt_NL = 900 ± 700 » comme lecture de
   2312.12498 Table II ; `LC-D-F5-ETAT-RACCORD` v0.3 (correctif R-23) déclare
   ce chiffre NON LITTÉRAL dans la source, caractérisation approximative d'un
   σ = O(500) sur le template gauge-field/axion FFe. R-11 l'a CONSIGNÉ et
   NON ARBITRÉ, corps fermés.
   VOIE ARBITRÉE EN S9, décision prise, ne pas la rouvrir :
     (ii) FETCH CIBLÉ de 2312.12498 Table II, sous CADRAGE GELÉ AVANT LECTURE
          (anti-fit : l'espace-verdict et les discriminants sont figés avant
          que la source ne soit consommée) ;
     puis AU BESOIN SEULEMENT (i) ouverture du corps de F2 et/ou F5, si la
          source seule ne tranche pas la provenance du chiffre.
     (iii) « laisser en l'état » est ÉCARTÉ.

   CONTRAINTE D'INTRANT — MESURÉE sur clone neuf en S9, à ne pas croire sur
   parole, à re-mesurer :
     `2312_12498v2.pdf` est ABSENT du miroir git (`sources/` ne contient que
     `2503_19957v1.pdf` + README). La tête `LC-D-F2-TTT-PLANCK` le déclare
     pourtant en `fichiers_compagnons_kb`, aux côtés de `2409_10595v2.pdf`
     également absent. Ces pièces vivent donc AU MOUNT (autoritaire, R-54),
     pas au dépôt. Le « fetch » de la voie (ii) est en réalité, par ordre de
     préférence :
       (a) fourniture de `2312_12498v2.pdf` depuis le mount, en intrant ;
       (b) à défaut, récupération externe — NOTER que l'allowlist réseau du
           conteneur d'exécution ne couvre PAS arxiv.org : une récupération
           doit passer par les outils web de l'assistant, pas par le shell.
     Dans les deux cas, PRÉCÉDENT S8 OPPOSABLE : un intrant refourni se
     CONFRONTE au registre AVANT extraction (sha256 de l'archive/du fichier),
     puis pièce par pièce. Et le cadrage est gelé AVANT que le fichier ne soit
     lu, pas après.

   Gabarit attendu : LÉGER. Ce n'est PAS un lot de redémonstration — le Silo R
   est clos — mais une ADJUDICATION DOCUMENTAIRE : quel énoncé, de F2 ou de
   F5, dit juste sur la provenance de « 900 ± 700 ». Cadrage gelé AVANT
   lecture, espace-verdict pré-déclaré, plafond de grade annoncé au gel.
   Issue attendue honnête : l'une des deux têtes porte une lecture inexacte,
   OU les deux sont compatibles et l'écart est de formulation. Aucune issue ne
   réduit le compte.

   VOLET 2 — SILO P, arbitrage de priorisation.
   β / P-1 (cartographie v1.2 : β#1 maintenu) VS report modulaire d = 3 / P-3
   (recommandation #1 des decks). Le choix m'appartient ; sans décision
   explicite de ma part, RIEN ne s'ouvre au Silo P. Tracker R-53 : 0/4.

   VOLET 3 — SOLDES DE GOUVERNANCE, après les deux précédents.
   G-1 solde (16 bundles de la décharge v2.74, 72 .py ; `hors-KB/A/`
   LC-A-SURVIE-CONFORME non fourni) · G-4 (autorité mount vs git — hypothèse
   reconduite : mount autoritaire R-54, git miroir vérifiable) · G-5b/c
   (index `LC-00-INDEX`, arborescence des silos) · PDF du mount (5014 Ko) vs
   `sources/2503_19957v1.pdf`, confrontation non exécutée.

6. PRÉCÉDENTS S9 OPPOSABLES (en plus de tous ceux de S4–S8) :
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

7. PÉRIMÈTRE — INCHANGÉ. Le Silo R est clos à 12/12 SANS retirer une seule
   inconnue : c'est ce que la cible transverse T-1 de R-11 a vérifié, et
   c'est le résultat le plus important de S9. « Branche FALSIFIABILITÉ
   épuisée » = constat de NON-EXISTENCE d'un front borné et sceau-able
   restant, invérifiable par instrument, JAMAIS un acquis.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non
   clos · N non fixé (≡Λ, R-53 : 0/4) · O₂ non construit (β ≡ G3 seul facteur
   ouvert) · nœud (i) INDÉTERMINÉ (pas A) · CCC non démontrée NI réfutée.

8. Pas de token pour l'instant — celui de S9 est révoqué. Tu me le
   demanderas au moment du dépôt, après avoir annoncé chemin + sha256 +
   message de commit, fichier par fichier (R-55).

§6.4 — sentinelle terminale. Dériver, muter, rejouer, corriger un instrument,
clore un silo, déposer, amender : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit.
