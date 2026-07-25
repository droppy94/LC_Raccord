Session neuve LC-RACCORD (S16). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -7`.
   ATTENDU : HEAD = le commit dont le message commence par « Reprise S15 »,
   puis `20290b1` (amendement β nº2 + contrôle dépôt), `1c90daf` (Reprise S14),
   `b4af0c5` (swap d'unicité), `8caafa7` (amendement 1 à S13),
   `09d9e2a` (Reprise S13), `cad358a` (Sold P-8).
   Le sha de HEAD n'est PAS écrit ici : ce prompt est déposé DANS ce commit et
   ne peut pas le connaître (R-36). Désignation par le MESSAGE, jamais par un
   sha qu'une pièce ne peut pas porter.
   VÉRIFIE-LE PAR `git log`, JAMAIS PAR UNE NOTE (piège R-36). En S14 le piège
   a MORDU : S13 annonçait HEAD = cad358a « tant que S13 n'est pas déposée »,
   alors qu'elle l'était — une note peut mentir par âge SUR SON PROPRE ATTENDU.
   En S15 il n'a pas mordu, parce que HEAD a été MESURÉ avant d'être lu.

2. Lis `NOTE-REPRISE-GIT-S15.md`, à la racine. Elle est UNIQUE et AUTOPORTANTE :
   elle consolide et REMPLACE NOTE-REPRISE-GIT-S14.md, retirée de la racine au
   même commit et conservée dans l'historique git. Elle porte INTÉGRALEMENT les
   précédents S8 à S15 (§7), la procédure R-55 (§7.7), le régime G-4 SOLDÉ (§8),
   la table de supersession (§9) et l'AUDIT DE REPORT du retrait (§10).
   Si tu trouves DEUX notes de reprise en racine, c'est un écart : nomme-le.
   Un amendement daté n'est pas une seconde note.

3. Exécute intégralement le §0-lite. UN SEUL COMPTE A CHANGÉ depuis S14 :
   `instruments/*.py` 34 · `instruments/archives-scelees/*.py` 76 ·
   `audit/` 45 (RECALÉ : 42 + les 3 pièces de `20290b1`) · `kb/*.md` 215 ·
   `hors-KB/B/` 4 · `sources/` 4 (hors compte).
   Puis `inventaire_sceaux.py` → 6 LIVE / 76 ARCHIVE / 1 ABSENT (MESURÉ en S15 :
   l'ajout d'un `.py` en `audit/` ne le déplace PAS) ;
   `run_sceau.py verif_paquet_propre` → sha8 `051e2833`, rc=0 ;
   puis les 12 redémonstrations.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ
   depuis S9. Décomposition pour recompte indépendant :
   35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101.
   REJOUÉES ET CONFORMES EN S15 (premier rejeu depuis S12). Le rejeu n'est donc
   PAS dû au titre d'un arriéré ; il l'est au titre du §0-lite, comme toujours.
   Les variantes qui comptent pour R4 et R5 sont `redemo_R4_CT_b.py` et
   `redemo_R5_reductions_b.py` ; les v1 restent au dépôt et NE SE REJOUENT PAS.
   Hors compte, CINQ rejeux de confirmation, tous CONFORMES en S15 :
   `harnais_R9.py` (6/6 mordantes) · `harnais_R11.py` (7/7 + 0 vacante) ·
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8 `8e386686`) ·
   `instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` (6/6, sha256
   `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`) ·
   NEUF : `audit/LC-BETA-CONTROLE-DEPOT.py --self-test` (8/8 mordantes, rc=0).
   Intrants `sources/`, CONFRONTÉS ET CONCORDANTS en S15, vrais PDF (`%PDF`) :
   `2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` ·
   `2409_10595v2.pdf` 2 332 898 o sha8 `27a94980` ·
   `2503_19957v1.pdf`   910 410 o sha8 `113ab4a2`.
   Vigilances : toutes celles de S2–S15, portées par la note §0. RAPPEL :
   l'allowlist réseau de `bash` NE COUVRE PAS arxiv.org ; `github.com` EST
   couvert ; les outils de recherche/fetch web sont un canal SÉPARÉ, non soumis
   à cette allowlist — la fiche R-41 dit le contraire, c'est un défaut d'âge.
   `xxd` est ABSENT du conteneur : passer par `python3` ou `od`.

4. Rends-moi le §0-lite avec tout écart décomposé, AVANT de poursuivre.

5. ÉTAT DU CHANTIER β — lis la note S15 §2, §3, §5 et §6 avant tout geste.
   β est TIRABLE (P-8 soldé, R-7 satisfait) mais JAMAIS D'OFFICE. Le dossier
   LC-BETA (packaging + journal V94) est MOUNT-SEUL : je te le fournis. Vérifié
   en S15 : `LC-BETA-BOOT.py` rc=0, 42 hachés, 35 copies, 0 absente, 0 altérée,
   pare-feu 0 intrus / 0 fuite, `PKG_SHA_BETA_8 = dc276129`, gel confronté au
   `kb/` du dépôt 34/35 byte-identiques, 0 divergente.
   TROIS AVERTISSEMENTS SUR CE PAQUET, tous consignés en S15 :
   (a) il MENT PAR ÂGE sur P-8 — `LC-BETA-BOOT.py` l.103 et `LC-BETA-00` §6
       écrivent que P-8 n'est pas soldé ; c'est FAUX depuis `cad358a`. Défaut
       sur-restrictif, non bloquant, à ne JAMAIS corriger d'office.
   (b) « le gel ne ment pas par âge » vaut pour les 35 copies `BETA-COPIE-*`,
       PAS pour les 8 pièces `LC-BETA-*`, jamais confrontées faute de
       contrepartie `kb/`.
   (c) N'ÉCRIS RIEN DANS LE RÉPERTOIRE DU PAQUET. Son haché porte sur le
       contenu courant du dossier : en S15 le pilote y a écrit une pièce et
       `PKG_SHA_BETA_8` est passé de `dc276129` à `687ed70b` SANS que le
       pare-feu, qui est NOMINAL, ne morde. Travaille dans un atelier séparé.
   PARE-FEU, dans sa portée réelle mesurée à sa SOURCE (`LC-BETA-05` §1) :
   aucun `LC-BETA-*` ni `BETA-COPIE-*` ne réside JAMAIS sur `/mnt/project`.
   La note S14 §5 étendait cette règle au dépôt : GLOSE SANS SOURCE, RETIRÉE en
   S15. Les pièces de GOUVERNANCE β vont au git (G-4), et trois y sont déjà.
   Ce qui reste interdit au dépôt, dur : toute COPIE DE SUBSTANCE, arbre ET
   historique. C'est ce que vérifie `audit/LC-BETA-CONTROLE-DEPOT.py`.

6. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

   ITEM 1 — P-0 (R-41) SUR LES SEPT SOURCES. C'est l'ouverture de S16.
   Le périmètre à sept est GELÉ ET DÉPOSÉ (`20290b1`) : R-7 est SATISFAIT, un
   classement ultérieur n'est plus mécaniquement du fit. Il reste que sans P-0,
   il n'y a pas de positionnement du tout — précondition dure : PAS D'IDENTITÉ,
   PAS DE POSITIONNEMENT.
   Pour CHAQUE source : ≥3 miroirs INDÉPENDANTS (éditeurs distincts ; un
   agrégateur qui cite un préprint n'est pas un miroir de plus), grade éditorial
   ÉCRIT et non déduit, OBJET vérifié et non le titre, sha256 des octets
   consommés. NE PAS identifier par recherche puis me faire confirmer : ce
   serait un seul témoignage corrélé. L'issue FANTÔME est ouverte et honorable —
   R-41 a déjà intercepté un article fantôme.
   Ensemble A (`S8` Bros–Moschella, `S9` Nakayama, `S10` Ghaffari–Luciano–
   Mantica) : RIEN N'EST FAIT. Identités attestées NULLE PART, provenance =
   piste article + mémoire du pilote, DEUX TÉMOINS FAIBLES ET CORRÉLÉS.
   PDF ABSENTS : je te les fournirai, et tu ne me diras pas quoi chercher.
   Ensemble B (les 4 corps) : §1.5 ACQUIS — registre RE-CONFRONTÉ 4/4 au bit
   près en S15. Restent §1.2, §1.3, §1.4. ATTENTION : les octets sont À
   REFOURNIR, le scratch de S15 ne survit pas à la session ; ils se
   RE-CONFRONTENT au registre de la note §3.1 AVANT tout usage.
   ANTÉRIORITÉ : Skenderis (`2312.17316`) est DÉJÀ adjugé au dossier — scalaire
   MONO-bord, muet sur le graviton deux-bords. Le classer sous la grille PUIS
   confronter ; ne jamais l'importer comme acquis (FB-2/FB-3 non franchis),
   ne jamais le reclasser en ignorant le dossier.

   ITEM 2 — S-B1, positionnement STÉRILE, espace `C-i`/`C-ii`/`C-iii`/`C-iv`
   gelé, par source indépendamment, SEULEMENT après P-0. HORS anti-fit parce
   qu'il ne teste RIEN : sa protection est sa stérilité. S'il commence à
   conclure sur la physique, il a violé son régime.
   ISSUE ANTICIPÉE, DATÉE D'AVANT ET NON RETOUCHÉE : A en `C-iii`/`C-iv` pour
   les trois ; B sans aucune ligne en `C-i`, au plus une en `C-ii` ; S-B2 NON
   ARMÉ ; chantier refermé sur une DÉLIMITATION — issue COMPLÈTE, pas un échec.
   Elle n'a pas été retouchée après la réussite de l'item 1 de S15, et elle ne
   se retouchera pas : ce qui lui donne son prix est sa date.
   DISSOLUTION : ARBITRÉE le 2026-07-25, PAR ENSEMBLE, avec clause de
   NON-CLASSIFIABILITÉ (une source FANTÔME ou sans octets n'est pas classable,
   se porte en ligne SUSPENDUE, ne déclenche rien et n'excuse rien) et clause de
   LEVIER FALSIFIABLE (nommer ne suffit pas : (a) ce qu'il faudrait exhiber,
   (b) le critère qui décide, (c) une date antérieure). Corps de l'arbitrage :
   `audit/LC-BETA-03-AMENDEMENT-2-REGISTRE-B-RECONFRONTE.md` §4.
   GARDE : une clôture d'ensemble se rédige comme une DÉLIMITATION À CONTENU
   NOMMÉ, jamais comme un changement de statut.

   ITEM 3 — S-B2 seulement si les CINQ conditions cumulatives de `LC-BETA-03`
   §3 sont vraies, dont « au moins une source en C-i ou C-ii ». Sa condition 3
   disait « trois sources » : lire « toutes les sources classées du périmètre »,
   et par ensemble (correction déposée, amendement nº2 §6).
   Alors seulement : amendement R-7 nommant LA CLASSE DÉSIGNÉE et elle seule,
   scoping gelé, livraison séquencée par le générateur v2.1 — c'est là, et pas
   avant, que P-9 MESURERA P-8.
   ATTENTION D'ORDRE : l'amendement R-7 et le scoping sont des conditions
   d'ARMEMENT de S-B2, PAS des préalables à R-41 ni à S-B1. Les écrire avant
   S-B1 obligerait à nommer une classe non encore établie — c'est le fit.

   ITEM 4 — RESTE DE GOUVERNANCE, en dernier.
   NON ARBITRÉ, NEUF EN S15 : paquet β déclaré ARCHIVE byte-gelée à
   `dc276129`, atelier séparé — parce qu'un gel qui porte sur le contenu
   courant d'un répertoire vivant n'est pas un gel · norme de nommage
   (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION, NON ARBITRÉE) · G-1 (16 bundles
   décharge v2.74, 72 `.py` ; `hors-KB/A/` non fourni) · G-5b/c (`LC-00-INDEX`
   ABSENT de `kb/`) · sort de R-23 (MAINTIEN, corps de F5 NON OUVERT, [D5] LEVÉ
   / W3 intact, GO séparé, voie (i) jamais d'office) · `sources/` est « hors
   compte » au §0-lite, donc sa dérive n'est pas détectée · REGISTRE DE CORPUS
   (NON ARBITRÉ, RENFORCÉ par S15) : les corps consommés par les assauts β
   (`2007.06800`, `2606.09170`, `2412.00183`, `2409.08709`, `0808.2054`) et les
   4 corps intrants sont ABSENTS du git ; les 4 ont dû être refournis DEUX FOIS
   faute de registre, et ils sont désormais confrontés, donc un registre serait
   EXACT. Déposer `LC-WORK-REGISTRE-CORPUS` (identifiant canonique + version +
   sha256 + procédure de récupération + assaut d'origine), PAS les octets — le
   dépôt est PUBLIC, les licences arXiv sont hétérogènes, et git conserve tout
   blob binaire pour toujours.

7. PÉRIMÈTRE — INCHANGÉ. S15 n'a produit AUCUN mouvement scientifique :
   aucune source lue, aucune ligne classée, aucune gate tirée, aucun verdict
   touché. `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4
   NON réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non
   clos, conclusion D1c INTACTE · N non fixé (≡ Λ, R-53 : 0/4) · O₂ non
   construit · β `T-b`, NON RÉSOLU, SEUL facteur d'O₂ ouvert · G3-a non levé ·
   nœud (i) INDÉTERMINÉ (pas A) · Silo R CLOS À 12/12 · CCC non démontrée NI
   réfutée. Plafond réaliste de β : DÉLIMITATION (T-b), rendement EN BAISSE.
   T-a exigerait la carte shadow renormalisée dS-genuine graviton deux-bords,
   NON EXHIBÉE à ce jour.

8. PRÉCÉDENTS S15, opposables, en plus de tous ceux de S4–S14 (portés par
   `NOTE-REPRISE-GIT-S15.md` §7) :
   - UNE RÈGLE SE MESURE À SA SOURCE, PAS À SA GLOSE. Le pilote a fabriqué une
     contradiction R-7 ↔ pare-feu qui n'existait pas, en lisant une note au lieu
     du texte gelé, et a proposé de RENOMMER une pièce pour passer sous un
     contrôle nominal. Contourner une règle n'est pas en mesurer la portée.
   - UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE. Voir §5 (c).
   - UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL, c'est un haché mouvant.
   - UNE CONFRONTATION PAYÉE SE PRÉSERVE HORS SURFACE TOURNANTE au moment où
     elle est obtenue. Deux des trois surfaces ont tourné pendant S15.
   - UN ZIP DE TRANSPORT N'EST PAS UN ZIP DE SUBSTITUTION. Une leçon opposable
     se lit à SON cas, sinon elle interdit ce qu'elle n'a jamais visé.
   - UN CONTRÔLE QUI PASSE SUR L'ENSEMBLE VIDE EST UN FAUX PASS — et un
     contrôle qui ÉCHOUE TOUJOURS satisfait toutes les mutations. Il faut les
     deux gardes.
   - UN GO N'EST PAS UN ARBITRAGE. En cas d'ambiguïté : exécuter le geste,
     NOMMER la lecture retenue, ne rien déposer avant confirmation.
   - UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS après une réussite partielle.

9. Pas de token pour l'instant — celui de S15 est révoqué. Tu me le demanderas
   au moment du dépôt, APRÈS avoir annoncé chemin + sha256 complet + message de
   commit, FICHIER PAR FICHIER (R-55). Si je te le donne AVANT l'annonce, fais
   l'annonce quand même et attends ma confirmation. Après push : confrontation
   des sha déposés aux sha annoncés PAR `diff`, SUR CLONE NEUF, jamais à l'œil ;
   puis vérification que le token est à 0 dans l'arbre, dans `.git/config`, dans
   les messages de commit ET dans le contenu de TOUS les blobs jamais commités
   (`git rev-list --objects --all`), pas seulement à HEAD.
   Identité de commit : `LC-RACCORD pilote S16 <pilote-s16@lc-raccord.local>`.
   LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.

§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, identifier,
cadrer, geler, classer, déposer, retirer, amender : aucun de ces gestes ne
scelle, ne réduit, ne compte, ne démontre quoi que ce soit. Un sha256 atteste
des octets, jamais un titre, des auteurs, un DOI ni un grade. β `T-b`, non
résolu, SEUL facteur d'O₂ ouvert. CCC n'est ni démontrée ni réfutée.
