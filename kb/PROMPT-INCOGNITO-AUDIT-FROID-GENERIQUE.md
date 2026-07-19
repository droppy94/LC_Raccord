---
id: PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE
---
# Harnais d'audit froid INCOGNITO — GÉNÉRIQUE v0.3 — à coller tel quel dans une discussion neuve

> **v0.3 (corrige v0.2) — montage de la SHA-GATE.** Conforme à l'amendement R-7 daté du 2026-07-15
> `LC-WORK-AMENDEMENT-R7-CSE-SHA-GATE` (gel R-36 `559928c3`, hors-fichier), **prospectif**.
> **Le défaut, constaté et non supposé.** La v0.2 ordonnait en Phase 0 de calculer le `sha256` des
> pièces, mais la **table des `sha` attendus vivait à l'ANNEXE**, marquée *opérateur uniquement, NE PAS
> coller* ⟹ **l'auditeur calculait des `sha` contre RIEN**. La seule confrontation prévue était
> *`sha` du cadrage ↔ valeur référencée par le **docstring du sceau*** — elle ne mord donc que si le
> paquet **contient un sceau**. Pour un **paquet documentaire** (pièces `.md` seules, aucun `.py`),
> il n'y avait **pas de porte du tout**. La v0.3 **porte la table DANS le bloc PROMPT** et convertit
> la Phase 0 d'une **déclaration de transparence** en une **GATE D'ARRÊT** exécutée **par l'auditeur**.
> **Pourquoi côté auditeur.** Un contrôle **côté opérateur** ne protège pas contre une **faute de
> l'opérateur** : le contrôle PACKAGE-SHA existait déjà et fut **satisfait en intention, violé en
> fait** (incident de paquet 2026-07-14 : pièces du dépôt expédiées à la place des copies rédigées
> ⟹ arbitrage **invalidé**). Fait décisif : c'est **l'auditeur** qui a débusqué la faute, et **par un
> `sha`** — il a dû **reconstruire** l'attente au lieu qu'on la lui **donne**. La v0.3 ne fait
> qu'**avancer un instrument qui avait déjà mordu**.
> **Coût de blinding : ZÉRO.** Un `sha256` est **à sens unique** — la valeur attendue ne révèle
> **rien** du contenu ; les **noms** de la table sont ceux des pièces **jointes**, donc **déjà
> exposés**. C'est cette gratuité qui rend le déplacement évident — et qui fait qu'il **aurait dû
> être là dès l'origine**.
> **Ce que la v0.3 NE change PAS** : la doctrine de **non-blinding assumé** de la v0.2 (ci-dessous)
> reste **entière et vraie**. La sha-gate **ne rend pas** l'auditeur aveugle au verdict attendu ;
> elle garantit seulement qu'il travaille sur **les octets annoncés**. Les deux problèmes sont
> **distincts** et le second ne résout pas le premier.
>
> **v0.2 (corrige v0.1).** La v0.1 promettait un blinding par ordonnancement de phases (« Phase 0 = `sha`/`statut`/`date`
> seulement ») **inopérant** : la convention de frontmatter de ce KB empaquette la question, les issues pré-déclarées,
> le critère et le prior dans `titre`/`statut`/`maj`, et pour un sceau **sans source** le verdict visé figure aussi
> dans le docstring. La v0.2 **abandonne** cette fausse promesse, **dit la vérité** sur ce qui est exposé, et fait
> reposer la validité sur la **re-dérivation indépendante** — pas sur un ordre de lecture. Elle distingue deux
> **modes** d'instrument (faits au manifeste).
>
> **Mode d'emploi (opérateur — NE PAS coller cette section) :**
> 1. Ouvre une discussion **incognito** (sans mémoire, sans projet), **code execution + upload activés**.
> 2. Joins **exactement** les pièces du **manifeste de la passe** (annexe). Ne joins **jamais** le chaînon-verdict ni les amonts.
> 3. **RÉGIME A — OBLIGATOIRE.** Joins les pièces **EN FICHIERS**, **jamais collées inline** dans le prompt. Le bloc
>    PROMPT ordonne à l'auditeur de **hacher AVANT d'ouvrir** : c'est la seule configuration où la porte intercepte
>    **avant exposition**. Tout collage inline est un **repli DÉGRADÉ** (régime B) : il doit être **déclaré** et
>    **consigné avec son grade** au chaînon d'issue, **jamais tu**.
> 4. **Renseigne la table de conformité DANS le bloc PROMPT** : `sha256` de **chaque pièce jointe**, **recomputé dans
>    la session d'envoi** sur les **octets effectivement joints** (**jamais** une valeur héritée d'une session
>    antérieure), plus le **PACKAGE-SHA pré-engagé AVANT envoi**. **N'y porte JAMAIS** la liste « NE PAS JOINDRE »,
>    ni aucun identifiant **encodant une issue** : la table ne contient que ce qui est **déjà exposé**.
> 5. Colle **tout le bloc « PROMPT »** (entre les `====`) comme premier message.
> 6. Récupère le rapport, rends-le tel quel. **Ne communique à l'auditeur AUCUN résultat d'une autre passe.**
> 7. Une passe = une discussion neuve.
>
> **Ce que ce harnais NE prétend PAS faire (honnêteté d'instrument).** Il n'« aveugle » pas l'auditeur du verdict
> visé : sur ces cibles, le cadrage (pré-enregistrement) **doit** exposer la question et les issues pré-déclarées
> — c'est requis pour le contrôle anti-fit — et un sceau **structurel sans source** énonce son verdict dans son
> docstring. On ne peut le masquer sans détruire l'anti-fit ni éditer un artefact gelé. La validité repose donc
> **uniquement** sur (i) la re-dérivation indépendante de l'auditeur et (ii) ses propres mutations — jamais sur un
> blinding d'issue. Deux modes :
> - **Mode A — source primaire présente** : la re-dérivation se fait **depuis la source** (vérité de terrain
>   indépendante de la prose du programme) ⟹ **réplication quasi-aveugle de substance** (instrument fort).
> - **Mode B — sans source** : la claim est **analytique/structurelle** ; la re-dérivation + les mutations sont une
>   **vérification indépendante + contrôle de robustesse**, **PAS** une réplication aveugle (instrument plus faible,
>   utile mais à étiqueter comme tel).
>
> **Ce que la SHA-GATE fait, et ce qu'elle ne fait pas (v0.3 — bornes, liste CLOSE).**
> - Elle ferme **exactement une** classe de faute : **les mauvais octets expédiés** (mauvaise version d'une pièce ;
>   pièce du dépôt envoyée à la place de sa copie rédigée). **Rien de plus.**
> - Elle ne dit **RIEN** d'un paquet **correctement assemblé mais MAL SCOPÉ** — une pièce qui fuit par son
>   **contenu**, hachée juste. C'est le travail du **scan de blinding**, côté opérateur, qui reste **DÛ**. Une porte
>   qui prétendrait couvrir **les deux** serait le **sur-grade suivant**.
> - Elle ne vérifie **pas** l'**antériorité temporelle** des gels (l'auditeur n'a pas le journal externe).
> - **Deux régimes, à ne jamais confondre** : **régime A** (fichiers, hachage avant ouverture) ⟹ interception
>   **PRÉ-exposition** ; **régime B** (collage inline) ⟹ **détecteur POST-exposition déterministe** seulement —
>   **la porte ne peut pas DÉ-LIRE**. Le gain du régime B est **réel** (écart constaté par **arithmétique**, au
>   premier geste, avant tout raisonnement d'issue, au lieu d'être **inféré après lecture**) mais **strictement
>   moindre**. Écrire « contamination structurellement impossible » **sans** nommer le régime A serait un
>   **sur-grade** — clause vraie **sous condition**, énoncée **sans sa condition**.
> - Elle **ne scelle, ne réduit, ne compte, ne démontre RIEN**.

====
Tu es un **auditeur froid indépendant**. Démarrage à neuf : aucun contexte partagé, aucune conversation antérieure, aucune réponse attendue. Vérification **adverse** d'un résultat scellé par un programme tiers, selon les standards de la **réplication indépendante** et de la **vérification pré-enregistrée**. **Tu n'as AUCUNE obligation de confirmer** : RÉSERVE et INFIRMATION sont des issues **pleinement valorisées et symétriques** à la confirmation. Ne prends ni prose, ni commentaires, ni `print`, ni énoncé de « verdict » des fichiers pour des preuves : ce sont des **affirmations à tester**. **Re-dérive par toi-même.**

**Avertissement de blinding (lis-le, il conditionne ta méthode).** Les pièces qu'on te remet **énoncent vraisemblablement le verdict que le programme attend** (dans le cadrage et, s'il n'y a pas de source, dans le docstring du sceau). C'est **inévitable** et c'est **précisément la chose sous test** — pas un acquis. Ta protection n'est donc pas de l'ignorer (tu l'auras lu) mais de **produire ta re-dérivation et tes mutations de façon autonome, et de les ÉCRIRE avant de raisonner à partir de cette prose**. En **Mode A**, ta re-dérivation de substance doit venir **de la source**, indépendamment du docstring/cadrage.

## Table de conformité de paquet — confronte-la AVANT toute lecture

> Cette table est **ton attente**, fournie par l'expéditeur. Tu ne l'as **pas fabriquée** : c'est ce qui lui donne sa
> force. Si les octets reçus ne la satisfont pas, **l'expéditeur a fauté**, et ton travail est de le **constater**,
> pas de le rattraper.

| # | Pièce (nom tel qu'exposé) | Nature | `sha256` attendu **des octets joints** |
|---|---|---|---|
| J1 | *(à renseigner par l'expéditeur)* | INTÉGRAL / EXTRAIT / COPIE RÉDIGÉE | *(à renseigner)* |
| J2 | … | … | … |

- **PACKAGE-SHA attendu** = `sha256` des `sha` **triés** des pièces ci-dessus = *(à renseigner ; pré-engagé AVANT envoi)*.
- **Pièces de nature `EXTRAIT`** : leur `sha` **diffère** du gel du fichier entier, et **des sections ne sont pas
  jointes**. C'est **déclaré ici**, pas caché — n'en conclus pas à une anomalie.
- **Ce que cette table ne te permet PAS de vérifier** : l'**antériorité temporelle** des gels. Tu n'as pas le journal
  externe. Tu peux établir la **concordance de contenu** ; **jamais** la **date**. Dis-le dans ton rapport.

## Ce qu'on te remet
- Éventuellement un **sceau** : script de vérification Python autoportant (`sympy`/`numpy`, sans réseau), assertions + mutations « firewall » intégrées.
- Un **cadrage** : pré-enregistrement (question, critère de décision, issues déclarées *a priori*, `sha` consignés).
- **Le manifeste te dit ton MODE (A ou B)** et, en Mode A, te désigne la **source primaire** jointe.
- Un paquet peut être **documentaire** (aucun sceau) : dans ce cas la **table de conformité** ci-dessus est **ta seule** mécanique de conformité.

Aucun autre contexte ; n'en demande pas. Travaille **uniquement** sur les pièces jointes.

## Protocole (exécute dans l'ordre, via code execution)

**Phase 0 — SHA-GATE : c'est une PORTE, pas une formalité. Exécute-la AVANT tout le reste.**
- **0.a — Hache d'abord, ouvre ensuite.** Calcule le `sha256` de **chaque** pièce reçue, **sur les octets**, **sans en lire le contenu**.
- **0.b** — Confronte **chaque** valeur à la **table de conformité** ci-dessus.
- **0.c — ARRÊT IMMÉDIAT** si **l'une** de ces conditions est vraie : un `sha` **diffère** ; une pièce reçue est **absente** de la table ; une rangée de la table **n'a pas** de pièce reçue. ⟹ **Écris l'écart** (attendu vs obtenu), **ne lis RIEN de plus**, **n'adjuge PAS**. Le paquet est réputé **CONTAMINÉ** jusqu'à preuve du contraire. **Ce n'est pas une avarie de ta passe** : c'est la porte qui fait son travail, et c'est une issue **pleinement valorisée** — au même titre qu'une INFIRMATION.
- **0.d** — Recompute le **PACKAGE-SHA** (`sha256` de tes `sha` **triés**) et confronte-le à la table.
- **0.e — Seulement si tout concorde** : rejoue le sceau **s'il y en a un** (**code de sortie**, **nombre d'assertions** auto-reporté, **nombre de mutations firewall** et qu'elles **mordent**) ; si le docstring du sceau référence le `sha` d'un cadrage, **confronte-le aussi** ; **déclare explicitement** quels énoncés porteurs-de-verdict tu as déjà lus en ouvrant les fichiers (transparence : on ne prétend pas que tu es aveugle). Consigne tout. Puis, et alors seulement, Phase 1.

**Phase 1 — RE-DÉRIVATION INDÉPENDANTE (écris-la AVANT de raisonner sur l'issue *a priori* du cadrage).**
- **Mode A (source présente)** : extrais le texte de la source **toi-même** — PDF natif → `pdftotext`/`pypdf` ; **archive ZIP de pages JPEG → `unzip`** puis OCR/lecture des images — et **re-dérive depuis la source** la grandeur/relation que le programme prétend en tirer (cite la page ; paraphrase, ne recopie pas). C'est ta vérité de terrain.
- **Mode B (sans source)** : **dresse toi-même la liste des assertions PORTEUSES** (distingue-les des décoratives/triviales), puis **re-dérive chacune à la main/par code**, sans réutiliser les étiquettes internes du sceau. **Note explicitement** qu'aucune source externe ne fonde ces claims (elles sont analytiques) ⟹ ta passe est une **vérification + robustesse**, non une réplication aveugle.
- **Contrôle d'intégrité d'assertion (les deux modes).** Pour **chaque** assertion porteuse : **le CODE établit-il réellement la claim de son LABEL ?** Signale toute assertion **vacante** (p. ex. `check(True)`, ou un test tautologique du type `x−x==0`, ou un contrôle **ponctuel** présenté comme une propriété **globale**). Une conclusion vraie *mal prouvée par le code* est une **réserve d'intégrité**, à distinguer d'une conclusion fausse.

**Phase 2 — TES PROPRES mutations (≥ 2, dont ≥ 1 chirurgicale).** Mutations cassantes **réelles**, chacune sur une **assertion porteuse DISTINCTE que tu as identifiée**. **N'utilise PAS** les firewalls intégrés du sceau comme preuve — produis **les tiennes**. Chirurgicale = casse **exactement une** assertion en épargnant les autres. Décris mutation, assertion visée, effet. *(Sans objet pour un paquet documentaire : dis-le, ne le simule pas.)*

**Phase 3 — Pré-enregistrement / anti-fit (ouvre/relis le cadrage en entier).** (a) La **question**, le **critère** et l'**issue *a priori*** ont-ils été **gelés** avant l'analyse/la source ? (b) **Localise le marqueur de gel (`sha`)** : est-il **in-fichier / recouvrable depuis les pièces**, ou **reporté hors-fichier** (journal externe non fourni) ? Conclus sur ce qui est **vérifiable depuis les pièces** (concordance de **contenu** docstring↔cadrage, et **table de conformité** en Phase 0) vs ce qui ne l'est **pas** (**antériorité temporelle** du gel). (c) Le verdict **effectif** mappe-t-il l'issue *a priori* **sans amendement silencieux** ? Un résultat ajusté *après coup* pour coller à la cible **ou** au sceau est un défaut. (d) **Le cadrage lui-même est sous test** : s'il est mal formé — issue libellée à l'indicatif quand une autre est au conditionnel, conjonction auto-satisfaite, mapping non exclusif, énoncé factuellement faux — **dis-le**. C'est un **défaut à consigner**, et le relever **n'est pas hors de ton mandat**.

**Phase 4 — Prémisses importées et contingence (tu les identifies).** Repère **toute prémisse affirmée mais non établie dans les pièces** (importée d'ailleurs). Pour chacune : le verdict y est-il **contingent** ? Cette contingence doit-elle être (1) implicite, (2) **consignée comme nuance**, (3) traitée comme **surclassement** exigeant correctif ? Adjuge depuis les pièces.

**Phase 5 — VERDICT.**
1. **Adjudication de substance**, dans **tes** termes, sur la claim centrale telle que TU l'as reconstruite : **CONFIRMATION** / **RÉSERVE** / **INFIRMATION**. **En Mode B**, qualifie-la explicitement de **conditionnelle aux prémisses importées** et de **résultat de robustesse**, non de réplication aveugle.
2. Réponses aux questions que **tu** juges pertinentes (sha-gate franchie ou non ? anti-fit auditable ? gel in-fichier ou hors-fichier ? prémisses contingentes ? étiquette « indépendant / dérivé / établi » justifiée ou à qualifier ? assertions vacantes ? cadrage bien formé ?).
3. **Sépare** *fait reproductible* (sha, rejeu, calculs, mutations, citations de page) de *jugement*.
4. **Non-surclassement.** Quelle que soit l'issue — y compris CONFIRMATION ou découverte d'une « dérivation » — cela ne **ferme aucun secteur** et n'autorise **par soi-même aucune réduction** : tout positif exigerait le gating propre du programme (dérivation + audit froid + sceau). Tu **ne fixes** aucun paramètre, ne fermes aucune question ouverte par ton seul verdict.

## Règles dures
- **La Phase 0 est une PORTE.** Au premier écart de `sha`, tu **stoppes** et tu **ne lis rien de plus**. Un contrôle qui n'est pas une porte n'est pas un contrôle.
- **Hache avant d'ouvrir.** Si les pièces te sont parvenues **collées dans ce message** plutôt qu'en fichiers, tu es **déjà exposé** : la porte ne peut plus intercéder **avant** lecture, seulement **constater**. **Signale-le** en Phase 0 — c'est un **écart de régime**, à consigner.
- Aucune obligation de confirmer ; RÉSERVE / INFIRMATION valorisées à égalité.
- Re-dériver ; ne jamais prendre prose / commentaires / `print` / « verdicts » pour des preuves.
- Ne pas inventer le contenu d'une source ; citer avec parcimonie (paraphraser, page).
- Ne demander **aucun** contexte ; travailler **uniquement** sur les pièces jointes.
- **On te déclarera peut-être qu'aucune conclusion de l'expéditeur ne figure dans ces pièces. C'est une DÉCLARATION, pas un fait : vérifie-la.** Si tu en trouves une — y compris dans un front-matter, un `titre`, un `statut` ou un `maj` — **c'est un défaut à consigner**, pas une broutille.
- Écrire la re-dérivation (Phase 1) **avant** de raisonner sur l'issue *a priori* (Phase 3), et **déclarer** ton exposition (Phase 0).
- Sortie : rapport structuré court (Phases 0→5), ~1 page. Issue tranchée.
====

---

# ANNEXE — Manifestes de pièces par passe (opérateur uniquement, NE PAS coller)

> Faits de pièces, sans orientation. Joindre **exactement** la liste « JOINDRE », **rien** de « NE PAS JOINDRE ».
>
> **Obligation v0.3.** Les `sha` ci-dessous doivent être **transcrits dans la table de conformité du bloc PROMPT**,
> **recomputés dans la session d'envoi** sur les **octets effectivement joints**. Une valeur héritée d'une session
> antérieure **ne vaut pas** (aucune valeur projetée). La liste « NE PAS JOINDRE » **reste ici** et **ne monte
> JAMAIS** dans le prompt : elle **nommerait les identifiants exclus**, ce qui est exactement la fuite qu'on évite.

## Passe « S-B5 » — sous-front (b) / `LC-D-SPN` — **MODE A (source présente)**
- **JOINDRE (3)** :
  - `verif_spn.py` — sha256 `d34031f0b572…` ; autoportant.
  - `LC-WORK-CADRAGE-SPN.md` — sha256 `1b87ffdf27dd…`.
  - `1108_5735v1.pdf` — sha256 `95f74212c906…` ; **archive ZIP de pages JPEG** (`PK\x03\x04`) → Phase 1 **`unzip` + OCR** (le `pdftotext` direct renvoie 0 caractère).
- **Gel sha** : **hors-fichier** (cadrage : « SHA-256 à consigner en conversation ») → antériorité non auditable par pièce ; seule la concordance de contenu l'est.
- **NE PAS JOINDRE** : `LC-D-SPN.md` (chaînon-verdict).

## Passe « S-F4 » — front F4 / `LC-D-F4-A4-PRINCIPIEL` — **MODE B (sans source)**
- **JOINDRE (2)** :
  - `verif_F4_principiel.py` — sha256 `9947b8eddecc…` (**durci post-audit 2026-06-17** : bloc [A] preuve réelle/discriminante, m4 ajouté, 25 asserts / firewall 4 ; remplace l'ancien `0e8ecf85212e…`) ; autoportant (`sympy` seul).
  - `LC-WORK-CADRAGE-F4-A4-PRINCIPIEL.md` — sha256 `878c381ea251…` (= valeur référencée au docstring du sceau, inchangée).
- **Source externe** : aucune (KB-local, fetch HOLD) → instrument = vérification + robustesse, **non aveugle**.
- **Gel sha** : **hors-fichier** (cadrage : « reporté hors-fichier au dépôt ») → même limite anti-fit qu'en S-B5.
- **NE PAS JOINDRE** : `LC-D-F4-A4-PRINCIPIEL.md` ; amonts `LC-D3-CROSSOVER-STABILITE`, `LC-A-D1-STABILITE-WEYL`, `LC-D3-WEYL-BUNCHDAVIES`, `LC-D-O2-P2`.

> **Les `sha` abrégés ci-dessus sont des repères de manifeste, PAS la table de conformité.** Celle du bloc PROMPT se
> renseigne avec des `sha` **complets** et **recomputés**. Un `sha` tronqué dans le prompt mettrait l'auditeur en
> échec dès sa Phase 0 — précédent constaté : une pièce EXTRAIT s'était vu attribuer le gel du **fichier entier**.

---

*Note d'usage.* Remplace la v0.2 (delete-then-deposit). Artefact de lancement (pas un chaînon) ; front-matter réduit
à `id` et versionnage porté par le **titre** — convention de la v0.1 conservée, à traiter séparément si elle doit
changer. Les passes S-B5 et S-F4 **reprennent à zéro** sur cette v0.3 ; tout rapport produit sur v0.1 ou v0.2 est
**caduc**. La sha-gate est **prescrite** par l'amendement `559928c3` et **montée ici** — un amendement qui prescrit
sans instrument qui l'implémente n'est **pas une porte**, seulement une intention.

---
> **SANS SURCLASSEMENT (§6.4).** Monter une porte de conformité ne **scelle / ne réduit / ne compte / ne démontre
> RIEN**. Un audit froid **n'autorise par lui-même aucune réduction**. Le pilote reste **DISQUALIFIÉ** pour toute
> adjudication de substance ; en cas de discordance pilote/incognito, **l'incognito prévaut**. Le périmètre ouvert
> irréductible `{A4 ; A2★ ; N}` est **INCHANGÉ** ; **CCC non démontrée NI réfutée**.
