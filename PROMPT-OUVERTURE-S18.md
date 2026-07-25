Session neuve LC-RACCORD (S18). Ouvre sur contexte plein, ne dépose rien sans GO.

1. Clone `https://github.com/droppy94/LC_Raccord.git` sous un chemin unique,
   vérifie `git status` (arbre propre) et `git log --oneline -10`.
   ATTENDU : le commit dont le message commence par « Reprise S17 », puis
   `7dbee86` (S-B1 rendu), `2ff65f9` (pièce de nommage S17), `b79e3de`
   (amendement 1 à S16), `aedc9a2` (Reprise S16), `11e924e` (P-0 rendu),
   `5f9874c` (Reprise S15), `20290b1`, `1c90daf`.
   Le sha de ce commit n'est PAS écrit ici : ce prompt est déposé DANS lui et ne
   peut pas le connaître (R-36). Désignation par le MESSAGE, jamais par un sha
   qu'une pièce ne peut pas porter.
   **NE PRÉSUME PAS QU'IL EST HEAD.** R-36 interdit à une pièce de porter son
   propre sha ; il ne l'autorise PAS à affirmer qu'elle est au sommet. Un commit
   postérieur peut s'être intercalé — C'EST ARRIVÉ EN S17, et la clause de
   position du prompt S16 n'a été vraie que 524 secondes.
   MESURE HEAD PAR `git log` AVANT de lire ce prompt, puis CONFRONTE, puis NOMME
   l'écart s'il y en a un. NE CORRIGE RIEN D'OFFICE.
   La fenêtre `-10` est dimensionnée pour absorber deux commits intercalés ; si
   la chaîne annoncée déborde, c'est un fait à nommer, pas à contourner.

2. Lis `NOTE-REPRISE-GIT-S17.md`, à la racine. Elle est UNIQUE et AUTOPORTANTE :
   elle consolide et REMPLACE `NOTE-REPRISE-GIT-S16.md` ET son `AMENDEMENT-1`,
   toutes deux retirées de la racine au même commit et conservées dans
   l'historique git. Elle porte INTÉGRALEMENT les précédents S8 à S17 (§7), la
   procédure R-55 (§7.9), le régime G-4 SOLDÉ (§8), la table de supersession
   (§9) et l'AUDIT DE REPORT du retrait (§10).
   Si tu trouves DEUX notes de reprise en racine, c'est un écart : nomme-le.
   Un amendement daté n'est pas une seconde note.
   LA RACINE PORTE 4 FICHIERS. Une cinquième pièce y est un écart à nommer.

3. Exécute intégralement le §0-lite. UN SEUL COMPTE A CHANGÉ depuis S16 :
   `instruments/*.py` 34 · `instruments/archives-scelees/*.py` 76 ·
   `audit/` 55 (RECALÉ : 50 + 5 pièces S17) · `kb/*.md` 215 · `hors-KB/B/` 4 ·
   `sources/` 4 (hors compte) ·
   `audit/beta-paquet-gouvernance/` 8 pièces `LC-BETA-*`.
   Puis `inventaire_sceaux.py` → 6 LIVE / 76 ARCHIVE / 1 ABSENT ;
   `run_sceau.py verif_paquet_propre` → sha8 `051e2833`, rc=0 ;
   puis les 12 redémonstrations.
   Attendu global : 271/271 PASS + 101 consignations, 12/12 rc = 0 — INCHANGÉ
   depuis S9. Décomposition, MULTIENSEMBLE et NON dans l'ordre R-1..R-12 :
   35+17+16+16+12+11+6+21+40+45+16+36 = 271 ;
   5+5+6+6+8+7+3+10+14+10+8+19 = 101.
   REJOUÉES ET CONFORMES EN S17.
   RECOMPTE : compter sur le MARQUEUR EN TÊTE DE LIGNE, puis confronter au bilan
   auto-déclaré de chaque script — 12/12 concordants en S17. R8, R10 et R11 le
   libellent différemment (accents, tirets), ce n'est PAS un écart. Le piège de
   S16 (115 au lieu de 101) ne s'est pas reproduit sous le motif S17 : cela ne
   prouve rien sur le piège, seulement que le motif n'était pas le même.
   DÉCLARE TON INSTRUMENT, pas seulement ton résultat.
   Les variantes qui comptent pour R4 et R5 sont `redemo_R4_CT_b.py` et
   `redemo_R5_reductions_b.py` ; les v1 restent au dépôt et NE SE REJOUENT PAS.
   Hors compte, CINQ rejeux de confirmation, tous CONFORMES en S17 :
   `harnais_R9.py` (6/6) · `harnais_R11.py` (7/7 + 0 vacante) ·
   `cd hors-KB/B && python3 verif_B_tracteur.py` (rc=0, sha8 `8e386686`) ·
   `instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` (6/6, sha256
   `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`) ·
   `audit/LC-BETA-CONTROLE-DEPOT.py --self-test` (8/8, rc=0).
   Intrants `sources/`, CONFRONTÉS ET CONCORDANTS en S17, vrais PDF (`%PDF`) :
   `2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` ·
   `2409_10595v2.pdf` 2 332 898 o sha8 `27a94980` ·
   `2503_19957v1.pdf`   910 410 o sha8 `113ab4a2`.
   Vigilances : toutes celles de S2–S17, portées par la note §0.5.
   RAPPELS : l'allowlist réseau de `bash` NE COUVRE PAS arxiv.org ; `github.com`
   EST couvert ; les outils de recherche/fetch web sont un canal SÉPARÉ, non
   soumis à cette allowlist — et il rend du TEXTE, JAMAIS des octets hachables,
   MESURÉ DEUX FOIS (S16, S17). `xxd` ABSENT : `python3` ou `od`.
   `rc=$?` après un pipe mesure le DERNIER élément du pipe.
   NEUF S17 : `grep -c` compte des LIGNES, pas des occurrences — employer
   `grep -o | wc -l` ou `re.findall`. Une chaîne `&&` s'interrompt sur un
   `grep -c` qui rend 0 : terminer par `|| true` quand le zéro est attendu.

4. Rends-moi le §0-lite avec tout écart décomposé, AVANT de poursuivre.

5. CE QUE TU N'AS PLUS À ME DEMANDER — lis la note §4 et §5bis.
   (a) `LC-BETA-PAQUET.zip` : NE PLUS LE RÉCLAMER. Le paquet est SOLDÉ —
       8 pièces `LC-BETA-*` déposées byte-intactes, 34 `BETA-COPIE-*`
       reconstructibles par `audit/LC-BETA-PAQUET-CONCORDANCE.md`, et le journal
       V94 BYTE-CONFRONTÉ en S17 (`b11347732e…a691c`, 12 623 o). IL N'Y A PLUS
       DE TROU. Paquet ARCHIVE byte-gelée, jamais rejoué, atelier séparé.
   (b) JOURNAL V94 : NE PLUS LE RÉCLAMER. Il est confronté, et ses OCTETS NE SE
       DÉPOSENT PAS — copie de substance, interdit dur, arbre ET historique.
       Il reste mount-seul de droit sous G-4.
   (c) LES 8 PIÈCES MENTENT PAR ÂGE et ce n'est PAS à corriger : `LC-BETA-BOOT.py`
       l.103 et `LC-BETA-00` §6 écrivent que P-8 n'est pas soldé — FAUX depuis
       `cad358a`. Défaut SUR-RESTRICTIF, non bloquant, NOMMÉ à
       `audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md`, JAMAIS corrigé en place.
   (d) LES CORPS : `audit/LC-WORK-REGISTRE-CORPUS.md` + son `AMENDEMENT-1`
       portent identifiant canonique, version, sha256 et procédure. Les CINQ
       corps d'assaut ont désormais des PREMIÈRES MESURES (amendement §1).
       ATTENTION : le registre §3 N'A JAMAIS PORTÉ DE COLONNE DE VERSION — on ne
       sait pas quelle version chaque assaut a lue, donc ces sha NE RENDENT PAS
       les verdicts `S-G3T-*` traçables rétroactivement.
   (e) PARE-FEU, portée réelle mesurée à sa SOURCE (`LC-BETA-05` §1) : aucun
       `LC-BETA-*` ni `BETA-COPIE-*` ne réside JAMAIS sur `/mnt/project`.
       Ce qui reste interdit au dépôt, dur : toute COPIE DE SUBSTANCE, arbre ET
       historique. NE RENOMME JAMAIS UNE PIÈCE POUR PASSER SOUS UN CONTRÔLE
       NOMINAL.
   (f) LE MOUNT : ses `.pdf` sont des ZIP (`50 4b 03 04`). OUVRE-LES. Chacun
       porte une image ET un texte OCR par page, plus un `manifest.json` SANS
       sha de source. C'est un canal de LECTURE fidèle et de HACHAGE nul.
       « Ne sert pas les octets » ≠ « ne sert rien » : trois sessions ont lu la
       seconde dans la première. `NOTE-REPRISE-GIT-S13.md` a été RETIRÉE du
       mount par l'opérateur, constaté par mesure en S17.

6. ORDRE DE TRAVAIL — chacun sur GO séparé. Rien n'est mécanique.

   ITEM 1 — RIEN DU CHANTIER β N'EST À REPRENDRE. C'est le point d'ouverture.
   `S-B1` est RENDU (`7dbee86` + amendement) : `C-i` 0 · `C-ii` 0 · `C-iii` 6 ·
   `C-iv` 1. `S-B2` est NON ARMÉ, et c'est un RÉSULTAT, pas un reste-à-faire.
   Le chantier est refermé sur une DÉLIMITATION À CONTENU NOMMÉ.
   NE LE ROUVRE PAS D'OFFICE. Il ne se rouvre que si une source portant LES
   QUATRE qualificatifs du levier — lorentzien · `𝓘⁺` genuine sans cutoff ·
   jonction à deux faces · graviton d'Einstein propageant — entre au périmètre,
   ce qui exigerait un amendement de périmètre DATÉ.
   GARDE : ne présente jamais l'absence d'une telle source comme un résultat de
   physique. C'est une délimitation, et elle est datée.

   ITEM 2 — GOUVERNANCE, QUATRE ITEMS NON ARBITRÉS, hérités et jamais tranchés :
   `G-1` (16 bundles décharge v2.74, 72 `.py` ; `hors-KB/A/` non fourni) ·
   `G-5b/c` (`LC-00-INDEX` ABSENT de `kb/`, arborescence des silos) ·
   SORT DE R-23 (MAINTIEN, corps de F5 NON OUVERT, `[D5]` LEVÉ / W3 intact, GO
   séparé, voie (i), jamais d'office) · `sources/` HORS COMPTE au §0-lite, donc
   sa dérive n'est pas détectée.
   NEUFS EN S17, à porter : la COLONNE DE VERSION absente du registre §3 (la
   structure du registre est à amender) ; la LARGEUR DE `C-iii` non retouchée
   après l'arbitrage rendant `C-iv` réelle — le déséquilibre subsiste, la règle
   de lecture de la note §3.5 le compense sans le supprimer.

   ITEM 3 — RESTES DE FOND, en dernier, tous INCHANGÉS : audit froid incognito ·
   plafond `T-b` / carte shadow `T-a` non exhibée · candidats genuine-dS armés
   non lus · routes α/δ (Odak–Speziale) · DESI DR2 · `Δ-C` plus étroit que son
   libellé · `p` libre / P-sélecteur · anti-circularité `K` · `§7quinquies`
   `K-B` prescription-dépendant · cadrage figé `37bc85e5` / gel amont
   `b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald · gap résiduel
   `R1″ ∧ R2″ ∧ R4″`.

7. RÉSERVES QUI SE RECOPIENT — ne les laisse pas s'effacer par l'usage.
   AUCUNE LIGNE DU PÉRIMÈTRE N'EST SANS RÉSERVE :
   CINQ lignes (`B1` `B2` `B3` `B4` `S8`) sous RÉSERVE PERMANENTE de décalage
   version-consommée / version-gradée — arbitrée en S17, elle ne se lève pas ;
   DEUX lignes (`S9` `S10`) sous RÉSERVE ÉCRITE à cinq points, absence de grade.
   5 + 2 = 7. Une ligne citée sans sa réserve est une ligne INCOMPLÈTE.

8. PÉRIMÈTRE — INCHANGÉ. S17 a produit un POSITIONNEMENT, pas un mouvement
   scientifique : aucune gate tirée, aucun verdict touché.
   `{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
   réfuté · A2★ décision ouverte, C7 non levée · D1 non clos, D1c INTACTE ·
   N non fixé (≡ Λ, R-53 : 0/4) · O₂ non construit · β `T-b`, NON RÉSOLU, SEUL
   facteur d'O₂ ouvert · G3-a non levé · nœud (i) INDÉTERMINÉ · Silo R CLOS à
   12/12 · CCC non démontrée NI réfutée.

9. PRÉCÉDENTS S17, opposables, en plus de tous ceux de S8–S16 (note §7) :
   - UNE PIÈCE NE PEUT PAS DAVANTAGE CONNAÎTRE SA POSITION QUE SON SHA.
   - UN CONTENANT NON OUVERT N'EST PAS UN CONTENANT MESURÉ.
   - LE NOM D'UN CONTENANT NE DÉCRIT PAS SON CONTENU. Trois fois en S17.
   - UN ARBITRAGE INEXÉCUTABLE NE SE DÉGRADE PAS EN SILENCE : il se rend à
     l'opérateur, il ne se réinterprète pas.
   - UNE ANTÉRIORITÉ SIGNALÉE SUR UNE LIGNE NE DIT RIEN DES AUTRES.
   - LE TOKEN CONFIRME L'ANNONCE, PAS UNE VERSION AMÉLIORÉE.
   - UN INSTRUMENT DE COMPTAGE COMPTE CE QU'IL COMPTE (`grep -c` = lignes).
   - UN ÉCART REJETÉ NE S'EFFACE PAS, IL SE DATE.
   - UNE MESURE SANS VERSION NE CONFRONTE RIEN.

10. Pas de token pour l'instant — ceux de S17 sont révoqués. UN TOKEN PAR DÉPÔT,
    et tu me le demanderas APRÈS avoir annoncé chemin + sha256 complet + message
    de commit, FICHIER PAR FICHIER, RETRAITS COMPRIS (R-55). Si je te le donne
    AVANT l'annonce, fais l'annonce quand même et attends ma confirmation. Une
    instruction de déposer N'EST PAS la confirmation d'une annonce. Après push :
    confrontation des sha déposés aux sha annoncés PAR `diff`, SUR CLONE NEUF ;
    puis vérification que le token est à 0 dans l'arbre, dans `.git/config`,
    dans les messages de commit ET dans le contenu de TOUS les blobs jamais
    commités (`git rev-list --objects --all`).
    Identité de commit : `LC-RACCORD pilote S18 <pilote-s18@lc-raccord.local>`.
    LE PILOTE NE SIGNE JAMAIS DU NOM DE L'OPÉRATEUR.

§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, classer, délimiter,
arbitrer, déposer, retirer, amender : aucun de ces gestes ne scelle, ne réduit, ne compte, ne
démontre quoi que ce soit. Un sha256 atteste des octets, jamais un titre, des auteurs, un DOI
ni un grade. `S-B1` rendu n'ouvre aucune gate ; `S-B2` non armé n'est pas un échec. β `T-b`,
non résolu, SEUL facteur d'O₂ ouvert. CCC n'est ni démontrée ni réfutée.
