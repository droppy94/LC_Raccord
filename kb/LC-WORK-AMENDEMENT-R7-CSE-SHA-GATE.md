---
id: LC-WORK-AMENDEMENT-R7-CSE-SHA-GATE
titre: "Amendement R-7 DATÉ — la SHA-GATE : porter la TABLE DES SHA ATTENDUS DANS le bloc PROMPT et convertir la Phase 0 d'une DÉCLARATION DE TRANSPARENCE en une GATE D'ARRÊT exécutée PAR L'AUDITEUR. Motif : dans le harnais NOTE-07 v1.1 (gel `5ef7f848`) comme dans la doctrine générique `PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE` v0.2, la Phase 0 ORDONNE à l'auditeur de calculer le `sha256` de chaque pièce — mais la table de référence vit à l'ANNEXE, marquée OPÉRATEUR UNIQUEMENT, NE PAS COLLER ⟹ l'auditeur calcule des `sha` CONTRE RIEN. Réponse directe à l'INCIDENT DE PAQUET V80 (passe #1 expédiée avec les fichiers du mount au lieu des copies rédigées ⟹ fuite de l'issue voisine ⟹ arbitrage INVALIDÉ), où le `sha` FUT l'instrument décisif mais arriva TARD, l'auditeur ayant dû RECONSTRUIRE l'attente au lieu qu'on la lui DONNE. DEUX RÉGIMES GRADÉS SÉPARÉMENT, sur arbitrage opérateur : régime A (livraison PAR FICHIERS, hachage AVANT ouverture) = interception PRÉ-EXPOSITION ; régime B (collage inline) = DÉTECTEUR POST-EXPOSITION DÉTERMINISTE, gain réel mais STRICTEMENT MOINDRE — la porte ne peut pas DÉ-LIRE. Le régime A est rendu OBLIGATOIRE (§7-1) de sorte que le claim fort TIENNE PAR CONSTRUCTION. RETIRE au passage un SUR-GRADE de `LC-WORK-REPRISE-V82` §5 (« contamination structurellement impossible », écrit SANS sa condition — vrai en régime A, FAUX en régime B ; même famille que le sur-grade A4-QW « universel »). R-7 ANTI-FIT TRIVIALEMENT SATISFAIT : AUCUNE adjudication n'est pendante à cette date (NOTE-07 SOLDÉE, chaînon V-B `9f797f9d` déposé) ⟹ l'amendement NE PEUT PAS être fitté à un résultat qui n'existe pas. PROSPECTIF, MONOTONE-SÛR, ZÉRO-FUITE (un `sha` est à sens unique ⟹ coût de blinding NUL). SANS SURCLASSEMENT (§6.4) : poser une porte de conformité ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 daté (règle d'EXPOSITION posée AVANT toute adjudication future) — n'adjuge pas, n'importe pas, ne fetch pas, ne re-gèle aucun cadrage, ne touche aucun espace-verdict"
statut: "AMENDEMENT DATÉ 2026-07-15 — PROSPECTIF, opposable au PROCHAIN paquet CSE (au premier chef le front G3). R-7 anti-fit TRIVIALEMENT satisfait : aucune adjudication PENDANTE à cette date, aucun rapport d'auditeur n'existe, aucune issue n'est en attente ⟹ position anti-fit la plus forte structurellement disponible. Amende les INSTRUCTIONS D'EXPOSITION de `PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE` et du harnais `PROMPT-INCOGNITO-NOTE07-FUSION-N` (instances à mettre en conformité). Les gels `32b76fd5` (espace-verdict), `89f9da27` (gate R-41), `588d09f5` (rédaction), `5ef7f848` (harnais v1.1) restent INTACTS et NON re-gelés. AUCUN effet sur V-B ni sur le chaînon `LC-D-F6-NOTE07-VB` — adjudication SOLDÉE, rétroactivité INTERDITE. {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée NI réfutée."
version: "0.1"
langue: fr
date: "2026-07-15"
gel_R36: "ce fichier N'EMBARQUE PAS son propre sha256 (anti-auto-référence). Le gel R-7/R-36 est horodaté HORS-FICHIER au dépôt, byte-exact livrable==mount à vérifier au retour."
tags: [amendement, R-7, anti-fit, prospectif, date, gel-R-36, sha-gate, gate-arret, CSE, incognito-souverain, pilote-disqualifie, zero-fuite, transfert-de-charge, incident-paquet-V80, deux-regimes, sur-grade-retire, regime-A-obligatoire, monotone-sur, R-54, R-55, V62, §6.4, non-surclassement]
renvois: [PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE, PROMPT-INCOGNITO-NOTE07-FUSION-N, LC-WORK-AMENDEMENT-R7-NOTE07-CSE-REDACTION, LC-WORK-CADRAGE-BORDEON-NOTE07-FUSION-N, LC-WORK-R41-NOTE07-MIROIRS, LC-D-F6-NOTE07-VB, LC-WORK-REPRISE-V82-POST-CHAINON-VB, LC-WORK-AMENDEMENT-R7-A4-QW-TYPEI-CORR, PROMPT-INCOGNITO-A2STAR-P1-ORHO]
maj: "2026-07-15 — v0.1 : création sur GO Thierry, session V83, APRÈS §0-lite VERT (PKG-SHA `5eacf768`, 194 = 187 + 7, 0 doublon, parité 5/5/7 Δ=0, firewall VERT par `ls`) et APRÈS lectures R-54 sur le mount (harnais v1.1 Phase 0 l.96-101 + ANNEXE l.149 ; doctrine générique v0.2 Phase 0 l.46 ; chaînon V-B). DÉFAUT CONSTATÉ PAR LECTURE, non supposé : la table des `sha` est en ANNEXE OPÉRATEUR ⟹ Phase 0 n'est pas une porte. ARBITRAGE OPÉRATEUR : deux régimes gradés séparément + régime A (livraison par fichiers) OBLIGATOIRE. SUR-GRADE RETIRÉ de la note de reprise V82 §5 (clause vraie sous condition, écrite sans sa condition) — la note est un INDEX, non une source (R-54), sa formulation n'avait rien scellé. BORNES ÉCRITES (§8) : la porte ferme EXACTEMENT la classe V80 (les mauvais octets expédiés) et RIEN de plus ; le scan de blinding reste DÛ et INCHANGÉ. §6.4 : poser une porte ne scelle/réduit/compte/démontre rien ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
---

# Amendement R-7 — la sha-gate (paquets CSE, prospectif)

> **Ce fichier ne juge rien.** Il ne touche **aucun** espace-verdict, **aucune** cible gelée,
> **aucun** discriminant. Il amende **les instructions d'exposition** d'un paquet d'audit :
> **qui** exécute le contrôle de conformité, **avec quelle attente**, et **à quel moment**.

## §1 — Le défaut constaté (fait, non interprétation)

Relu sur le mount (R-54), le harnais `PROMPT-INCOGNITO-NOTE07-FUSION-N` v1.1 (gel `5ef7f848`)
ordonne, **dans le bloc PROMPT** :

> *Phase 0 — Transparence d'exposition + mécanique. […] Calcule le `sha256` de **chaque** pièce jointe.*

Et la table des `sha` attendus vit **hors** du bloc PROMPT :

> *ANNEXE — Manifeste de pièces (**OPÉRATEUR UNIQUEMENT — NE PAS COLLER**)*

**Conséquence mécanique** : l'auditeur calcule des `sha` **contre rien**. Il n'a **aucune attente**
à confronter. La Phase 0 est une **déclaration de transparence** — elle n'est **pas** une porte.

Même trou dans la doctrine générique `PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE` v0.2 : la seule
confrontation prévue est *compare le `sha` du cadrage à la valeur référencée par le **docstring du
sceau*** — **inopérante pour un paquet SANS sceau**, ce qui était exactement le cas de NOTE-07
(6 pièces documentaires, 0 `.py`).

**L'incident V80** (consigné, non rationalisé) : la passe #1 fut expédiée avec **les fichiers du
mount** au lieu des **copies rédigées** ⟹ fuite de l'issue voisine ⟹ faits E1–E7 **recevables**,
**arbitrage INVALIDÉ**.

**Le fait décisif, et il retourne le dossier** : c'est **l'auditeur** qui a débusqué la
contamination, et **par un `sha`** — le chaînon `LC-D-F6-NOTE07-VB` l'écrit : *le `sha` du cadrage
reçu **égal au gel original** `32b76fd5` ⟹ **preuve arithmétique** qu'aucune rédaction n'avait eu
lieu* (avec 0 marqueur annoncé et 4 occurrences là où 2 étaient promises).

⟹ **Le `sha` était DÉJÀ l'instrument décisif.** Il est arrivé **tard** pour une seule raison :
l'auditeur a dû **reconstruire** l'attente au lieu qu'on la lui **donne**. La sha-gate n'invente
rien — elle **avance un instrument qui a déjà mordu**.

**Un contrôle qui n'est pas une PORTE n'est pas un contrôle.**

## §2 — Pourquoi un amendement, et non un contrôle opérateur de plus

Le harnais v1.1 **porte déjà** un contrôle PACKAGE-SHA (*Contrôles avant envoi (opérateur)*, item 4).
Il est **côté pilote**. En passe #1 il fut **satisfait en intention** et **violé en fait**.

**Un contrôle côté pilote ne protège pas contre une faute du pilote.** C'est la leçon structurelle
de V80, et c'est la même que celle de R-55 en V81 (*la règle a mordu contre son auteur*). Le seul
contrôle qui mord contre le pilote est celui qui est **exécuté par l'auditeur**, avec une attente
qu'il **n'a pas fabriquée lui-même**.

⟹ Déplacer la table dans le PROMPT **n'est pas un déménagement cosmétique** : c'est un
**TRANSFERT DE CHARGE** du pilote (**disqualifié**) vers l'auditeur (**souverain**). Cela requiert
un amendement **daté** parce que cela modifie **ce qui est exposé** à l'instance qui juge — même
nature que l'amendement de rédaction `588d09f5`.

## §3 — La sha-gate — ÉNUMÉRÉE, EXHAUSTIVE, CLOSE

**Table de conformité de paquet**, portée **DANS le bloc PROMPT**, au-dessus du protocole,
contenant **exactement** ceci et **rien d'autre** :

- **(a)** une rangée **par pièce JOINTE** : étiquette (`J1..Jn`), **nom tel qu'exposé**, **nature**
  ∈ {`INTÉGRAL` ; `EXTRAIT` ; `COPIE RÉDIGÉE`}, et le **`sha256` attendu des OCTETS EFFECTIVEMENT
  JOINTS** ;
- **(b)** le **PACKAGE-SHA** = `sha256` des `sha` **triés** des pièces jointes, **pré-engagé
  hors-fichier AVANT envoi** ;
- **(c)** l'énoncé **explicite** de ce que l'auditeur **ne peut pas** vérifier : l'**antériorité
  temporelle** des gels (il n'a pas le journal externe) ;
- **(d)** pour toute pièce `EXTRAIT` : la mention **explicite** que son `sha` **diffère** du gel du
  fichier entier, et que des sections **ne sont pas jointes**.

**INTERDITS dans la table (liste CLOSE)** :

- **(e)** toute rangée pour une pièce **NON jointe** ;
- **(f)** la liste **NE PAS JOINDRE** — elle **nommerait les identifiants exclus**, ce qui est
  précisément le motif de l'amendement `588d09f5` ;
- **(g)** tout identifiant **encodant une issue** ;
- **(h)** toute valeur **PROJETÉE** : un `sha` non recomputé **dans la session d'envoi** n'entre pas
  dans la table (leçon V62 / R-55).

**La Phase 0 devient une GATE D'ARRÊT**, dans cet ordre, **avant toute autre phase** :

- **0.a** — **hacher** chaque pièce reçue ;
- **0.b** — **confronter** à la table ;
- **0.c** — **ARRÊT IMMÉDIAT** si : un `sha` diffère **OU** une pièce reçue est absente de la table
  **OU** une rangée de la table n'a pas de pièce reçue. ⟹ **écrire l'écart**, **ne rien lire de
  plus**, **ne pas adjuger**. Le paquet est réputé **CONTAMINÉ** jusqu'à preuve du contraire ;
- **0.d** — **recomputer** le PACKAGE-SHA, le confronter ;
- **0.e** — **seulement si tout concorde** : déclaration d'exposition, puis Phase 1.

## §4 — LES DEUX RÉGIMES, gradés séparément (arbitrage opérateur 2026-07-15)

**Régime A — livraison PAR FICHIERS, hachage AVANT ouverture.**
La porte intercepte **PRÉ-EXPOSITION**. **Grade** : la contamination **par mauvais octets** ne peut
**pas** être franchie sans être vue — quand l'auditeur s'arrête, **il n'a rien lu**.

**Régime B — collage INLINE des pièces dans le prompt.**
L'auditeur est **déjà exposé** au moment où il calcule le premier `sha`. **La porte ne peut pas
DÉ-LIRE.** **Grade** : **détecteur POST-EXPOSITION DÉTERMINISTE** — l'écart est constaté par
**arithmétique**, **au premier geste**, **avant tout raisonnement d'issue**, au lieu d'être
**inféré après lecture** (V80). Gain **réel**, mais **strictement moindre**.

⟹ **Le régime A est OBLIGATOIRE** (§7-1). Le régime B est un **repli dégradé** : s'il est employé,
l'**écart de grade** doit être **consigné au chaînon d'issue**, **jamais tu**.

### §4bis — Sur-grade RETIRÉ (consigné, non escamoté)

`LC-WORK-REPRISE-V82` §5 écrit : *« La contamination devient **structurellement impossible**,
interceptée **AVANT** exposition au lieu d'être constatée après. »* — **sans sa condition**.

La clause est **VRAIE en régime A** et **FAUSSE en régime B**. Défaut de la **même famille** que le
sur-grade A4-QW **« universel »** (une clause vraie **sous condition**, écrite **sans sa condition** ;
cf. amendement `7ec75a22`). Le présent amendement **retire le sur-grade** en posant la condition
comme **OBLIGATION**, de sorte que le claim fort **tienne par construction** au lieu d'être
**supposé**.

La note V82 est un **INDEX**, **non une source** (R-54) : sa formulation **n'avait rien scellé**,
aucune rectification de gel n'est requise.

## §5 — Invariants LOAD-BEARING conservés TELS QU'ÉCRITS (non touchés)

- **Aucun espace-verdict touché** : `{V-A..V-D}`, `D1–D5`, mapping, `F#1–F#4` du gel `32b76fd5`
  restent **INTACTS** et **NON re-gelés**.
- Les **cibles et critères** de **tout** cadrage gelé : **INTOUCHÉS**.
- `588d09f5` (rédaction) **INTACT**, **NON re-gelé** — la sha-gate le **sert** : la table porte le
  `sha` des **copies RÉDIGÉES**, jamais celui du mount.
- `89f9da27` (gate R-41) **INTACT**, **NON re-gelé**.
- La **disqualification du pilote** : **INCHANGÉE**, et **renforcée** (§2).
- **V-B** et le chaînon `LC-D-F6-NOTE07-VB` (`9f797f9d`) : **AUCUN effet** — adjudication
  **SOLDÉE**, rétroactivité **INTERDITE**.
- **§9ter**, sceaux, **§10** : **intouchés**.

## §6 — Monotonie, sûreté, zéro-fuite

- **(i) MONOTONE-SÛR.** N'ajoute qu'une **condition d'ARRÊT**. Elle ne peut que **réduire** ce que
  l'auditeur lit. Elle ne **retire aucun prior** et n'en **ajoute aucun**. Elle ne peut **pas**
  changer un verdict — seulement **empêcher qu'un verdict soit rendu sur un paquet faux**.
- **(ii) ZÉRO-FUITE, argumenté.** Un `sha256` est **à sens unique** : la valeur attendue ne révèle
  **rien** du contenu. Les **noms** de la table sont ceux des pièces **jointes**, donc **déjà
  exposés**. ⟹ **coût de blinding = ZÉRO**. C'est cette propriété qui rend le déplacement
  **gratuit** — et c'est pourquoi il **aurait dû être fait dès l'origine**.
- **(iii) ANTI-FIT TRIVIAL.** **Aucune adjudication n'est pendante** à cette date : NOTE-07 est
  **soldée**, le chaînon V-B est **déposé**. L'amendement **ne peut pas être fitté à un résultat qui
  n'existe pas**. C'est la position anti-fit **la plus forte structurellement disponible**.
- **(iv) PROSPECTIF.** Opposable au **prochain** paquet CSE (au premier chef le front **G3**).
  **Jamais rétroactif.**

## §7 — Obligations d'exécution (opposables au paquet)

1. **RÉGIME A OBLIGATOIRE** : les pièces sont livrées **EN FICHIERS** ; le prompt **ordonne**
   *hache d'abord, ouvre ensuite*. Tout collage **inline** est un **repli** qui doit être
   **déclaré** et **consigné avec son grade dégradé** (§4).
2. La **table de conformité** figure **DANS le bloc PROMPT**, **au-dessus** du protocole.
3. **Tous** les `sha` de la table sont **recomputés DANS la session d'envoi**, sur les **octets
   effectivement joints**. **Aucune valeur projetée** (V62 / R-55). Un `sha` hérité d'une session
   antérieure **ne vaut pas**.
4. **PACKAGE-SHA** **pré-engagé hors-fichier AVANT envoi**, attesté, et **porté dans la table**.
5. Le contrôle opérateur PACKAGE-SHA est **CONSERVÉ** : la sha-gate **ne le remplace pas**, elle le
   **double côté auditeur** (§2).
6. **INTERDIT** d'enrichir la table hors des items **(a)–(d)** de §3. Toute extension exige un
   **NOUVEL amendement daté**.
7. Le **scan de blinding** reste **DÛ** et **INCHANGÉ** (§8-b2).

## §8 — Ce que la sha-gate NE fait PAS (bornes, liste CLOSE)

- **b1.** Elle ferme **exactement** la classe d'incident V80 = **les mauvais octets expédiés**.
  **Rien de plus.**
- **b2.** Elle ne dit **rien** d'un paquet **correctement assemblé mais MAL SCOPÉ** (une pièce qui
  fuit par son **contenu**, hachée juste). C'est le travail du **scan de blinding**, côté opérateur,
  qui reste **dû**. Une porte qui prétendrait couvrir **les deux** serait **le sur-grade suivant**.
- **b3.** Elle ne vérifie **pas** l'**antériorité** des gels — à **dire** dans la table (§3-(c)).
- **b4.** En **régime B**, elle **ne dé-lit pas** (§4).
- **b5.** Elle **ne scelle, ne réduit, ne compte, ne démontre RIEN**.

---
> **SANS SURCLASSEMENT (§6.4).** Poser une porte de conformité de paquet **ne scelle / ne réduit /
> ne compte / ne démontre RIEN**. Les têtes scellées restent l'**AUTORITÉ**, **INTACTES**. Le pilote
> reste **DISQUALIFIÉ** pour toute adjudication de substance ; en cas de discordance
> pilote/incognito, **l'incognito prévaut**. Le périmètre ouvert irréductible `{A4 ; A2★ ; N}` est
> **INCHANGÉ** ; `D1` non clos ; `N` non fixé (≡ Λ, terminus ouvert — voie A close, clôture **R-53
> conditionnelle 0/4 INCHANGÉE**) ; `O₂` non construit ; voie H ∉ périmètre ; `β` **T-b** ; A4 route
> par-`𝓘⁺` délimitée (W2), postulat renforcé, **NON réfuté** ; A2★ parqué pending OA ;
> **CCC non démontrée NI réfutée**.
