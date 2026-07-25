Session neuve LC-RACCORD (S15). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -6`.
   ATTENDU : HEAD = le commit dont le message commence par « Reprise S14 »,
   puis `b4af0c5` (swap d'unicité), `8caafa7` (amendement 1 à S13),
   `09d9e2a` (Reprise S13), `cad358a` (Sold P-8), `af97865` (Reprise S11).
   Le sha de HEAD n'est PAS écrit ici : ce prompt est déposé DANS ce commit et
   ne peut pas le connaître (R-36). Désignation par le MESSAGE, jamais par un
   sha qu'une pièce ne peut pas porter.
   VÉRIFIE-LE PAR `git log`, JAMAIS PAR UNE NOTE (piège R-36). En S14 le piège
   a MORDU : S13 annonçait HEAD = cad358a « tant que S13 n'est pas déposée »,
   alors qu'elle l'était — une note peut mentir par âge SUR SON PROPRE ATTENDU.

2. Lis `NOTE-REPRISE-GIT-S14.md`, à la racine. Elle est UNIQUE et
   AUTOPORTANTE : elle consolide et REMPLACE NOTE-REPRISE-GIT-S13.md et son
   AMENDEMENT-1, retirés de la racine au même commit et conservés dans
   l'historique git. Elle porte INTÉGRALEMENT les précédents S8 à S14 (§7),
   la procédure R-55 (§7.6), le régime G-4 SOLDÉ (§8) et la table de
   supersession (§9).
   Si tu trouves DEUX notes de reprise en racine, c'est un écart : nomme-le.
   Un amendement daté n'est pas une seconde note.

3. Exécute intégralement le §0-lite. AUCUN COMPTE N'A CHANGÉ depuis S13 :
   `instruments/*.py` 34 · `instruments/archives-scelees/*.py` 76 ·
   `audit/` 42 · `kb/*.md` 215 · `hors-KB/B/` 4 · `sources/` 4 (hors compte).
   Puis `inventaire_sceaux.py` → 6 LIVE / 76 ARCHIVE / 1 ABSENT ;
   `run_sceau.py verif_paquet_propre` → sha8 `051e2833`, rc=0 ;
   puis les 12 redémonstrations.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ
   depuis S9. Décomposition pour recompte indépendant :
   35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101.
   NON REJOUÉES EN S14 (S14 n'a touché à aucune redémonstration) : leur dernier
   rejeu conforme date de S12. À REJOUER EN S15.
   Hors compte, quatre rejeux de confirmation, tous CONFORMES en S14 :
   `harnais_R9.py` (6/6 mordantes) · `harnais_R11.py` (7/7 + 0 vacante) ·
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8 `8e386686`) ·
   `instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` (6/6, sha256
   `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`).
   Intrants `sources/`, CONFRONTÉS ET CONCORDANTS en S14, vrais PDF (`%PDF`) :
   `2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` ·
   `2409_10595v2.pdf` 2 332 898 o sha8 `27a94980` ·
   `2503_19957v1.pdf`   910 410 o sha8 `113ab4a2`.
   Vigilances : toutes celles de S2–S14, portées par l'amendement 1 §5.
   RAPPEL : l'allowlist réseau de `bash` NE COUVRE PAS arxiv.org ; `github.com`
   EST couvert ; les outils de recherche/fetch web sont un canal SÉPARÉ, non
   soumis à cette allowlist — la fiche R-41 dit le contraire, c'est un défaut
   d'âge, corrigé par l'amendement de périmètre β §3 (mount).

4. Rends-moi le §0-lite avec tout écart décomposé, AVANT de poursuivre.

5. ÉTAT DU CHANTIER β — lis la note S14 §2, §3 et §6.1 avant tout geste.
   β est TIRABLE (P-8 soldé) mais JAMAIS D'OFFICE. Le dossier LC-BETA
   (packaging + journal V94) est MOUNT-SEUL : je te le fournis. Vérifié en S14 :
   `LC-BETA-BOOT.py` rc=0, 42 hachés, 35 copies, 0 absente, 0 altérée,
   pare-feu 0/0, `PKG_SHA_BETA_8 = dc276129`. Le gel de dossier NE MENT PAS
   PAR ÂGE : 34/35 copies byte-identiques au `kb/` du dépôt, 0 divergente,
   seule absente `LC-JOURNAL-V94.md` (mount-seul, conforme au régime G-4).
   PARE-FEU : aucun fichier `LC-BETA-*` ni `BETA-COPIE-*` ne réside JAMAIS sur
   le mount principal ni au dépôt. Le paquet vit dans son projet séparé.

6. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

   ITEM 1 — DÉCOMPOSER L'ÉCART DES 4 CORPS β. BLOQUANT pour S-B1.
   Le registre de première mesure du 2026-07-24 (amendement de périmètre β §1)
   donne : `2503_09372v2` 979 890 o `6b89e638…` · `1909_11703v2` 386 010 o
   `e080c5d6…` · `2402_04308v2` 4 629 572 o `1426146d…` · `2312_17316v2`
   1 223 061 o `7102dcf9…`. Ces valeurs ne sont PAS re-confrontables : le mount
   sert aujourd'hui des ARCHIVES ZIP de JPEG+OCR (magie `PK\x03\x04`) aux mêmes
   noms, de tailles 3 à 10 fois supérieures. Fait déjà consigné à `3419d49`
   (S10, « homonymes du mount ») et `af97865` (S11, « la surface a CHANGÉ DE
   NATURE »). NE PAS le re-présenter comme une découverte : S14 l'a fait, c'est
   un écart imputable au pilote. L'opérateur fournit les PDF ORIGINAUX ;
   confronte, décompose, puis corrige le §1 de l'amendement de périmètre.

   ITEM 2 — P-0 (R-41) sur les SEPT sources du périmètre arbitré.
   Ensemble A : S8/S9/S10 (pistes *Bros–Moschella*, *Nakayama*,
   *Ghaffari–Luciano–Mantica*) — identités attestées NULLE PART, PDF absents,
   à réclamer à l'opérateur. NE PAS identifier par recherche puis faire
   confirmer : ce serait un seul témoignage corrélé. L'issue FANTÔME est
   ouverte et honorable.
   Ensemble B : les 4 corps. §1.5 acquis (sous réserve de l'item 1) ; restent
   ≥3 miroirs INDÉPENDANTS (éditeurs distincts), grade éditorial ÉCRIT, et
   vérification de l'OBJET, pas du titre.
   ANTÉRIORITÉ : Skenderis (`2312.17316`) est DÉJÀ adjugé au dossier — scalaire
   MONO-bord, muet sur le graviton deux-bords. Le classer sous la grille PUIS
   confronter ; ne jamais l'importer comme acquis (ce serait FB-2/FB-3 non
   franchis), ne jamais le reclasser en ignorant le dossier.

   ITEM 3 — GELER ET DÉPOSER l'amendement de périmètre β, AVANT toute lecture.
   Sans dépôt antérieur auditable par un tiers, tout classement est du FIT.
   NON ARBITRÉ, à me poser : la DISSOLUTION PAR ENSEMBLE (proposition §4 de
   l'amendement). Sans elle, passer de 3 à 7 sources affaiblit mécaniquement la
   condition de dissolution de `LC-BETA-05` §5, et laisse l'ensemble B masquer
   une éventuelle réfutation de l'ensemble A.

   ITEM 4 — S-B1, positionnement STÉRILE, espace `C-i`/`C-ii`/`C-iii`/`C-iv`
   gelé, par source indépendamment. HORS anti-fit parce qu'il ne teste RIEN :
   sa protection est sa stérilité. S'il commence à conclure sur la physique, il
   a violé son régime.
   ISSUE ANTICIPÉE, DATÉE D'AVANT : A en `C-iii`/`C-iv` pour les trois ;
   B sans aucune ligne en `C-i`, au plus une en `C-ii` ; S-B2 NON ARMÉ ;
   chantier refermé sur une DÉLIMITATION — issue COMPLÈTE, pas un échec.

   ITEM 5 — S-B2 seulement si les CINQ conditions cumulatives de
   `LC-BETA-03` §3 sont vraies, dont « au moins une source en C-i ou C-ii ».
   Alors seulement : amendement R-7 nommant LA CLASSE DÉSIGNÉE et elle seule,
   scoping gelé, livraison séquencée par le générateur v2.1 — c'est là, et pas
   avant, que P-9 MESURERA P-8.
   ATTENTION D'ORDRE : l'amendement R-7 et le scoping sont des conditions
   d'ARMEMENT de S-B2, PAS des préalables à R-41 ni à S-B1. Les écrire avant
   S-B1 obligerait à nommer une classe non encore établie — c'est le fit.
   S14 s'est trompée sur ce point et l'a corrigé ; ne le refais pas.

   ITEM 6 — RESTE DE GOUVERNANCE, en dernier.
   Norme de nommage (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION, NON ARBITRÉE ;
   concerne aussi `LC-WORK-GEN-PAQUET-v2_1.py`, qui porte une version dans son
   nom) · G-1 (16 bundles décharge v2.74, 72 `.py` ; `hors-KB/A/` non fourni) ·
   G-5b/c (`LC-00-INDEX` ABSENT de `kb/`) · sort de R-23 (MAINTIEN, corps de F5
   NON OUVERT, [D5] LEVÉ / W3 intact, GO séparé, voie (i) jamais d'office) ·
   `sources/` est « hors compte » au §0-lite, donc sa dérive n'est pas
   détectée : à faire entrer dans le compte, ou à assumer explicitement ·
   REGISTRE DE CORPUS : le corpus des résultats CALCULÉS est au dépôt et
   reproductible ; celui des résultats LUS ne l'est pas (les corps consommés
   par les assauts β — `2007.06800`, `2606.09170`, `2412.00183`, `2409.08709`,
   `0808.2054` — sont ABSENTS du git). Sous G-4 ce n'est pas une faute
   rétroactive, mais ça se paiera à la première bascule de branche. La solution
   proposée, NON ARBITRÉE : déposer un `LC-WORK-REGISTRE-CORPUS` (identifiant
   canonique + version + sha256 + procédure de récupération + assaut d'origine),
   PAS les octets — le dépôt est PUBLIC, les licences arXiv sont hétérogènes, et
   git conserve tout blob binaire pour toujours.

7. PÉRIMÈTRE — INCHANGÉ. S14 n'a produit AUCUN mouvement scientifique :
   aucune source lue, aucune gate tirée, aucun verdict touché.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non
   clos, conclusion D1c INTACTE · N non fixé (≡ Λ, R-53 : 0/4) · O₂ non
   construit · β `T-b`, NON RÉSOLU, SEUL facteur d'O₂ ouvert · G3-a non levé ·
   nœud (i) INDÉTERMINÉ (pas A) · Silo R CLOS À 12/12 · CCC non démontrée NI
   réfutée. Plafond réaliste de β : DÉLIMITATION (T-b), rendement EN BAISSE.
   T-a exigerait la carte shadow renormalisée dS-genuine graviton deux-bords,
   NON EXHIBÉE à ce jour.

8. PRÉCÉDENTS S14, opposables, en plus de tous ceux de S4–S13 (portés par
   `NOTE-REPRISE-GIT-S14.md` §7) :
   - CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE, et elle
     est survenue DEUX FOIS en S14 (HEAD attendu ; homonymes ZIP du mount
     présentés comme découverte alors qu'ils sont consignés depuis S10).
     Le dépôt se mesure, il ne se déduit pas.
   - UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA
     DEMANDER. En S14 le pilote a imprimé `PKG_SHA_BETA_8` avant de réclamer la
     valeur hors-fichier : la confirmation obtenue est indistinguable d'un écho,
     donc NON OPPOSABLE (R-36, R-54). Demander D'ABORD, comparer ENSUITE.
   - UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM. Une pièce
     périmée peut être la PIÈCE DE REPORT d'autres sessions ; l'héritage par
     formule ne suffit plus dès qu'on retire le porteur (précédent 860c3f8,
     appliqué en S14 avant le swap −S11 −PROMPT-S12).
   - LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR. Identité de commit distincte.
   - UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS. G-4 gouverne les bascules
     à venir ; l'existant reste, et on ne réorganise pas le dépôt d'office.

9. Pas de token pour l'instant — celui de S14 est révoqué. Tu me le demanderas
   au moment du dépôt, APRÈS avoir annoncé chemin + sha256 complet + message de
   commit, FICHIER PAR FICHIER (R-55). Si je te le donne AVANT l'annonce, fais
   l'annonce quand même et attends ma confirmation. Après push : confrontation
   des sha déposés aux sha annoncés PAR `diff`, SUR CLONE NEUF, jamais à l'œil ;
   puis vérification que le token est à 0 dans l'arbre, dans `.git/config` et
   dans les commits.

§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, cadrer, geler, classer,
déposer, retirer, amender : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. β `T-b`, non résolu, SEUL facteur d'O₂
ouvert. CCC n'est ni démontrée ni réfutée.
