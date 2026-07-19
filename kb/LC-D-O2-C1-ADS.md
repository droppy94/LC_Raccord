---
id: LC-D-O2-C1-ADS
titre: "Instruction de la gate C1 (existence & finitude du terme de bord de jonction) en AdS, pour le facteur α de la construction O₂. Chaînon de DÉLIMITATION sans sceau (style F2/F3/F4/G3/FACTORISATION ; lecture-structure, AUCUNE algèbre de finitude scellée). Exécute S-O2C-2(suite) sous le cadrage GELÉ LC-WORK-CADRAGE-O2-CONSTRUCTION (sha 36fc7148…ffaa28c) avec les trois corps désormais KB-locaux : FH-II 2503.09372, Horowitz–Wang 1909.11703, Liu–Santos–Wiseman 2402.04308. RÈGLE DE DÉCISION a/b/c PRÉ-ÉNONCÉE (§0, durcissement anti-fit) AVANT la synthèse-verdict. VERDICT : C1 INSTRUIT EN AdS = C1-b (objet CONDITIONNEL à un paramètre), PAS C1-a, PAS C1-c. Justification : (i) FH-II §5 fournit le flot d'interpolation à DEUX bords (Σr↔Σr+dr, types de BC forcément distincts aux deux bords = caractère D↔N) mais OMET systématiquement les termes de coin (codim-1 seulement) ⟹ Δ_𝒞 (codim-2, le coin) n'est PAS livré par FH-II ; Δ_𝒞=d marginal acquis (LC-D-O2-DELTA-C, générateur GHY éq 7.13, TT̄ dim 2d absent en d=3). (ii) LSW : Dirichlet pur N'EST PAS elliptique/bien-posé ; la bonne-position EXIGE la famille conforme à un paramètre p (métrique de bord Weyl-rescalée fixée), Anderson(p→0)↔Dirichlet(p→∞) ⟹ le joint bien-posé porte un PARAMÈTRE LIBRE p non fixé par la donnée marginale ⟹ C1-b (conditionnel), pas C1-a. (iii) HW : une infinité de conditions de coin (surface spacelike ∩ bord) DÉTERMINENT les dérivées temporelles de la métrique de bord à partir des données initiales ⟹ donnée de jonction NON librement (analytiquement) spécifiable ; liberté résiduelle NON-analytique demeure ⟹ CONTRAINTE (sur-détermination), PAS divergence ⟹ ne fait PAS basculer en C1-c, renforce le caractère conditionnel. CAVEAT VIABILITÉ (hors gate C1) : LSW exhibe des instabilités dynamiques lorentziennes hors symétrie sphérique MÊME pour p>1/6 (stable euclidien) ⟹ caveat de réalité physique, rattaché à l'aval (C2/C3 / réalité C_T), distinct de la finitude C1. SIGNAL STRUCTUREL : les conditions de coin HW vivent au coin surface-spacelike ↔ bord = MÊME LIEU géométrique que le 𝓘⁺ spacelike de G3 (β) ⟹ re-enchevêtrement α↔β/G3 DÈS le coin AdS, qui NUANCE la leverage « α indépendant de G3 » posée par LC-D-O2-FACTORISATION — consigné comme FINDING, propagation/amendement R-7 sur FACTORISATION à décider après audit froid. ANTI-CIRCULARITÉ K honorée : +i/WCH pris comme données posées ; p non fixé par WCH/Penrose (le pivot transporte le swap mais pas le −1 de Hodge, P1/Hodge/P2) ⟹ p est un VRAI paramètre neuf. PAS d'amendement R-7 pour le verdict (route la gate C1 déjà gelée vers son issue pré-déclarée C1-b, aucune nouvelle prédiction). SANS SURCLASSEMENT (§6.4) : C1-b = objet conditionnel à p ⟹ le coefficient O(1) de A_T ne serait pinçable que MODULO p ⟹ NE ferme PAS le résidu de D1 ; {A4 ; A2★ ; N} INCHANGÉ ; C1 NON tranché en dS (β=G3 différé) ; O₂ NON construit ; D1 non clos ; N non fixé ; A4 non réduit ; CCC non démontrée. Aucun sceau (aucune construction concrète finie n'émerge — fork S-O2C-2d : sans-sceau)."
codename: LC-RACCORD
tags: [O2-construction, alpha-AdS, gate-C1, C1-b, delimitation, sans-sceau, FH-II, Freelance-Holography-II, conditions-de-coin, Horowitz-Wang, Liu-Santos-Wiseman, parametre-p, deux-bords, Delta-C, terme-de-coin, well-posed, ellipticite, instabilite-non-spherique, re-enchevetrement-beta-G3, anti-circularite-K, §6.4, A4, A2star, N, perimetre-inchange]
type: "chaînon-verdict / DÉLIMITATION (lecture-structure, sans sceau) — instruction de la gate C1 en AdS pour α. Exécute S-O2C-2(suite) sous cadrage gelé. Aucun sceau, aucune algèbre de finitude scellée."
statut: "[v0.4 — POST-CHANTIER #2 / COIN-b] Le caveat « terme de coin codim-2 OMIS ⟹ C1-b par voie INDIRECTE » est désormais INSTRUIT directement : LC-D-O2-COIN (chantier #2, gel recouvrable 84d11d5c…, KB-local) confirme que le terme de coin n'est exhibé par AUCUN des 3 corps (FH-II l'omet explicitement, HW = conditions sur données, LSW = pas de coin) ⟹ C1-b atteint AUSSI par voie DIRECTE (coin NOMMÉ comme pièce manquante, non exhibé) ; p reste libre ; α NON construit ; C1^AdS reste C1-b. Fetch nommé pour ré-armement (Hayward gr-qc/9303030, LMPS 1609.00207, coin BC mixte D↔N). Note additive R-7 ; corps v0.3 conservé. {A4 ; A2★ ; N} INCHANGÉ. | [v0.3 — POST-AUDIT S-O2C-1, 3 passes : 2 aveugles CERTIFIÉES (passes 2 & 3) + 1 biaisée (passe 1)] C1 instruit en AdS = C1-b, CONVERGENCE des trois passes ; §4 RÉFUTÉ par les trois (coin AdS timelike Λ<0 ≠ 𝓘⁺ spacelike dS Λ>0) ⟹ FACTORISATION α-indépendance NON amendée. CAVEAT ÉLEVÉ (passe 3) : le terme de coin codim-2 — l'ingrédient LITTÉRAL de la gate C1 — est OMIS par FH-II ; C1-b est atteint par la VOIE INDIRECTE (Dirichlet mal posé ⟹ bonne-position via famille à paramètre p libre), PAS en exhibant un terme de coin fini ⟹ statut fermement DÉLIMITATION (pas construction) ; la finitude du terme de coin elle-même reste NON établie par les corps. Résonance notée (les conditions de coin forcent S¹×dS₂ au bord près de t=0, corps 2 p.10) : tentante, mais PAS un même-lieu (cf. §4bis). Réserves de modélisation convergentes : FH-II interpole deux rayons d'UNE SEULE surface timelike (≠ deux éons) ; LSW euclidien, Dirichlet↔conforme (Neumann ≠ Anderson) ; 3 corps AdS/cavité, cible dS/CCC ⟹ transfert AdS→dS importé (≡ β/G3). Anti-fit : gel sha hors-fichier (antériorité non-auditable, R-36). NET : séparation α (AdS, instruit = C1-b) / β (dS ≡ G3, ouvert) renforcée. PROPAGATION débloquée (GO Thierry, file-by-file). | [v0.2 — POST-AUDIT S-O2C-1, 2 passes] C1 instruit en AdS = C1-b CONFIRMÉ par DEUX passes d'audit froid indépendantes (passe 2 = aveugle CERTIFIÉE, n'avait que le bloc protocole ; passe 1 = informative NON certifiée — fuite de verdict dans les zones opérateur du prompt, mais infirmation §4 contra-fuite robuste). Convergence : terme local fini ½√(−h)T ⟹ pas C1-c ; Dirichlet pur mal posé ⟹ bonne-position via famille à paramètre p libre ⟹ pas C1-a ⟹ C1-b ; 3 lectures adverses échouent chez les deux. FINDING §4 RÉFUTÉ par les deux passes (coin AdS timelike Λ<0 ≠ 𝓘⁺ spacelike dS Λ>0 ; les lieux ne coïncident pas ⟹ l'assemblage AdS n'hérite PAS d'obstruction dS au coin) ⟹ FACTORISATION (« α indépendant de G3 ») NON amendée, tient (passe 2 : ni établie ni réfutée depuis pièces AdS-seules — c'est le rôle de β). RÉSERVES de modélisation convergentes, à porter : FH-II recolle deux coupures timelike du même AdS (≠ deux éons) ; LSW euclidien, Dirichlet↔conforme (Neumann ≠ Anderson : identification D↔N avec écart) ; 3 corps AdS/cavité, cible dS/CCC ⟹ transfert AdS→dS importé (≡ β/G3). Anti-fit : gel sha cadrage hors-fichier ⟹ antériorité non-auditable par pièce (R-36), concordance de contenu OK. NET : la séparation α (AdS, instruit = C1-b) / β (dS ≡ G3, ouvert) sort renforcée. PROPAGATION débloquée (sous GO Thierry, file-by-file). | [v0.1] délimitation (lecture-structure, S-O2C-2 suite, KB-local sur 3 corps désormais déposés ; AUCUN sceau, style F2/F3/F4/G3/FACTORISATION). VERDICT : C1 INSTRUIT EN AdS = C1-b (objet conditionnel à un paramètre p), ni C1-a ni C1-c. Règle de décision a/b/c PRÉ-ÉNONCÉE (§0) avant synthèse. Justification tripartite : FH-II §5 = flot deux-bords codim-1, coin OMIS (Δ_𝒞=d marginal acquis hors FH-II) ; LSW = bonne-position exige la famille conforme à paramètre p (Dirichlet seul non elliptique) ⟹ paramètre libre ⟹ conditionnel ⟹ C1-b ; HW = conditions de coin contraignent la donnée (liberté non-analytique résiduelle) ⟹ sur-contrainte, PAS divergence ⟹ pas C1-c. Caveat viabilité (hors C1) : instabilité dynamique non-sphérique LSW même p>1/6 ⟹ rattaché à l'aval/réalité, distinct de la finitude. Signal : coin HW = locus G3/β ⟹ re-enchevêtrement α↔β/G3 dès l'AdS, NUANCE la factorisation (finding, amendement R-7 sur FACTORISATION à décider après audit froid). Anti-circularité K : p non fixé par WCH/Penrose ⟹ vrai paramètre neuf. PAS d'amendement R-7 (route une gate gelée vers son issue pré-déclarée). SANS SURCLASSEMENT (§6.4) : C1-b ⟹ A_T pinçable seulement modulo p ⟹ NE ferme PAS le résidu D1 ; {A4 ; A2★ ; N} INCHANGÉ ; C1 non tranché en dS (β différé) ; O₂ non construit ; D1 non clos ; N non fixé ; A4 non réduit ; CCC non démontrée. PROPAGATION GATED : ré-armement OBLIGATOIRE de l'audit froid S-O2C-1 (agent séparé) AVANT toute propagation s'appuyant sur ce pont α."
version: 0.4
langue: fr
maj: "2026-06-22 — v0.4 : NOTE DE RENVOI additive (R-7) suite au chantier #2 (LC-D-O2-COIN v0.1, exécution KB-local contre le gel recouvrable 84d11d5c…760450 du cadrage dédié LC-WORK-CADRAGE-O2-COIN). Le caveat de v0.3 (« terme de coin codim-2 OMIS ⟹ C1-b par VOIE INDIRECTE, finitude du coin non exhibée ») est désormais INSTRUIT directement et confirmé : verdict COIN-b — le coin n'est exhibé par AUCUN des 3 corps (FH-II l'OMET explicitement éq. 5.1 ; HW = conditions sur données ; LSW = pas de coin, p=coeff. GHY codim-1) ⟹ C1-b atteint AUSSI par voie DIRECTE (coin NOMMÉ, non exhibé) ; p libre ; α non construit. Fetch nommé pour ré-armement. SEULE la zone statut reçoit la note v0.4 ; le corps, le sha, les comptes, les §1-§7 v0.3 sont CONSERVÉS (additif-only, record historique). AUCUN sceau (C1-ADS reste sans sceau). {A4 ; A2★ ; N} INCHANGÉ ; C1-b conditionnel ⟹ A_T modulo p ⟹ ne ferme pas D1 ; D1 non clos ; N non fixé ; A4 non réduit ; CCC non démontrée. (cf. LC-D-O2-COIN, LC-WORK-CADRAGE-O2-COIN) | 2026-06-18 — v0.3 : intégration de la PASSE 3 (deuxième passe aveugle CERTIFIÉE, via le fichier auditeur épuré PROMPT-AUDITEUR-S-O2C-1-CLEAN.md ; lancée pour contrebalancer la passe 1 biaisée). Bilan = 3 passes : 2 aveugles certifiées (2 & 3) CONVERGENTES + 1 biaisée (1, sorties contra-fuite conservées). CONVERGENCE : (1) C1-b confirmé par les DEUX passes aveugles ; (2) §4 RÉFUTÉ par les trois ; (3) réserves de modélisation identiques ; (4) anti-fit gel hors-fichier (R-36). CAVEAT ÉLEVÉ par passe 3 : le terme de coin codim-2 (ingrédient littéral de C1) est OMIS par FH-II ⟹ C1-b atteint par voie indirecte (bonne-position elliptique), finitude du coin NON exhibée ⟹ délimitation ferme (pas construction). Résonance S¹×dS₂ (corps 2 p.10) notée, NON load-bearing. ACTIONS : §7 enrichi (sous-section Passe 3 + convergence mise à jour) ; bannière §4 étendue aux 3 passes ; statut/version. FACTORISATION intouchée. NB : v0.2 (interim post-2-passes) n'a PAS été déposé en KB (Thierry a lancé passe 3 avant) ⟹ superseded par ce v0.3 avant tout dépôt ; KB passe directement de v0.1 à v0.3 (delete-then-deposit). {A4 ; A2★ ; N} INCHANGÉ ; C1-b conditionnel ⟹ A_T pinçable modulo p ⟹ ne ferme pas le résidu D1 ; D1 non clos ; N non fixé ; A4 non réduit ; CCC non démontrée. | 2026-06-18 — v0.2 : POST-AUDIT FROID S-O2C-1 (deux passes). Passe 2 = aveugle CERTIFIÉE (Thierry n'a fourni que le bloc protocole délimité par ====, aucune fuite de verdict) ⟹ CONFIRMATION indépendante de C1-b (confiance modérée-à-élevée en AdS, conditionnelle aux identifications de modélisation). Passe 1 = NON certifiée (le fichier prompt v1.1 fuitait C1-b + finding §4 dans ses zones opérateur ‘NE PAS coller’, jointes en entier) ⟹ disqualifiée comme confirmation aveugle, MAIS son infirmation de §4 est contra-fuite (robuste) et ses réserves dérivent des corps. CONVERGENCE des deux : (1) C1-b confirmé (½√(−h)T fini ⟹ pas C1-c ; Dirichlet mal posé ⟹ famille à paramètre p libre ⟹ pas C1-a) ; (2) FINDING §4 RÉFUTÉ — coin AdS timelike ≠ 𝓘⁺ spacelike dS, les lieux ne coïncident pas ⟹ pas de ré-enchevêtrement α↔β/G3 établi ⟹ FACTORISATION α-indépendance NON amendée (tient ; passe 2 : indéterminable depuis AdS-seul = exactement le périmètre de β) ; (3) RÉSERVES de modélisation convergentes (FH-II = coupures timelike du même AdS ≠ éons ; LSW euclidien Dirichlet↔conforme, Neumann≠Anderson ; transfert AdS→dS importé ≡ β) ; (4) anti-fit : gel sha hors-fichier, antériorité non-auditable (R-36). ACTIONS : bannière de réfutation ajoutée sur §4 (texte conservé) ; §7 neuf consignant les deux passes ; statut/version mis à jour. FACTORISATION intouchée. Périmètre {A4 ; A2★ ; N} INCHANGÉ ; C1-b conditionnel ⟹ A_T pinçable seulement modulo p ⟹ ne ferme pas le résidu D1 ; D1 non clos ; N non fixé ; A4 non réduit ; CCC non démontrée. | 2026-06-18 — v0.1 : création. Instruction de la gate C1 en AdS (facteur α) sous cadrage gelé LC-WORK-CADRAGE-O2-CONSTRUCTION (sha 36fc7148…ffaa28c reproduit au §0 de session), les 3 corps désormais KB-locaux (déposés par operator). §0 : règle de décision a/b/c pré-énoncée (durcissement anti-fit bon marché, décidé avec Thierry AVANT la synthèse). §1 : acquis ré-ancré (DELTA-C : Δ_𝒞=d marginal, GHY éq 7.13 ; cadrage : C1-a/b/c). §2 : lecture des corps (FH-II §5 flot deux-bords / coin omis ; HW conditions de coin ; LSW famille conforme à p + instabilité). §3 : application de la règle ⟹ VERDICT C1-b en AdS. §4 : signal structurel re-enchevêtrement α↔β/G3 (finding). §5 : sans surclassement + routage. Aucun sceau (fork S-O2C-2d : sans-sceau, aucune construction finie concrète). {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
prerequis_kb: [LC-WORK-CADRAGE-O2-CONSTRUCTION, LC-D-O2-DELTA-C, LC-D-O2-JONCTION, LC-D-O2-FACTORISATION, LC-D-F6-G3-LAMBDA-BMS, LC-WORK-BIBLIO-O2-DEUX-BORDS, LC-AUDIT-VERDICT]
tags_epistemiques: [établi (structure), délimitation, décision ouverte, à inventer, INTRANT-HOLD, fetch-levé-AdS]
---

# C1 en AdS (facteur α) — instruction sous cadrage gelé : **C1-b**

> **Délimitation, lecture-structure, SANS sceau.** Exécute `S-O2C-2(suite)` sous le cadrage gelé
> `LC-WORK-CADRAGE-O2-CONSTRUCTION` (`36fc7148…ffaa28c`), les trois corps désormais KB-locaux.
> **Verdict : `C1` instruit en AdS = `C1-b`** (objet conditionnel à un paramètre `p`).
> Périmètre `{A4 ; A2★ ; N}` **INCHANGÉ** ; ne ferme pas le résidu de D1 ; β (dS) différé (≡ G3).

## 0. Règle de décision `a/b/c` — PRÉ-ÉNONCÉE (durcissement anti-fit)

Énoncée **avant** la synthèse-verdict (§3), pour empêcher de fitter l'issue aux corps. Mappe
« FH-II §5 ⊕ conditions de coin » → trichotomie gelée du cadrage (§4 du cadrage) :

- **`C1-a` (bien défini)** ⟺ terme de bord de jonction **fini**, **sans** contre-terme neuf au-delà
  de la renormalisation holographique standard (GHY + contre-termes existants), **sans** paramètre
  libre, et problème variationnel **bien posé** sans intrant additionnel.
- **`C1-b` (conditionnel)** ⟺ finitude/bonne-position obtenues **seulement** après introduction d'un
  **terme de bord neuf** OU d'un **paramètre libre** non fixé par la donnée existante.
- **`C1-c` (obstruction)** ⟺ **divergence irréductible** du terme de coin, OU bonne-position
  **impossible** pour tout choix de condition de bord, OU conditions de coin **interdisant tout**
  datum de jonction libre admissible.

**Clauses d'arête (pré-engagées) :**
1. Un **paramètre `p`** paramétrant une famille de conditions de bord bien-posées **compte comme
   paramètre libre** ⟹ pousse en `C1-b` (pas `C1-a`), **sauf** si la condition de raccord
   (WCH/Penrose/état +i) **fixe** `p` indépendamment (à vérifier sous anti-circularité K : +i/WCH
   sont des **données posées**, jamais utilisées pour *fabriquer* le fixage).
2. Des **conditions de coin** qui **contraignent** (ôtent la liberté analytique) sans produire de
   **divergence** sont une **sur-contrainte** ⟹ caveat, **pas** `C1-c` — `C1-c` seulement si elles
   **interdisent** le datum libre requis par la jonction.
3. Une **instabilité dynamique** de l'objet résultant est une question de **viabilité physique**,
   **distincte** de l'existence/finitude du terme de bord ⟹ **n'entre pas** dans `a/b/c` ; consignée
   comme caveat aval.

## 1. Acquis ré-ancré (KB, non re-dérivé)

- **Gate `C1`** (cadrage gelé) = existence + finitude d'un **terme de bord de jonction** au raccord
  D↔N à deux bords ; issues `a/b/c` ci-dessus.
- **`Δ_𝒞 = d` (marginal)** et générateur D↔N = trace GHY `W_{N→D}=−(1/2)√−h T` (FH-II éq 7.13) ;
  `TT̄` (dim `2d`) **absent en `d=3`** (coeff `(d−3)/2=0`) — acquis `LC-D-O2-DELTA-C` (instruisait
  déjà `C1-b` côté déformation **mono-bord**).
- **Acquis non re-dérivable** (cadrage §2-A) : `A_T~1/C_T~1/N` coeff `O(1)` libre ; jonction `D→N` ;
  `S²=−1` vp `±i` ; comptage W³-GPY `2+1` sans coefficient. **Clos non ré-ouvrable** (§2-B) : pivot
  A4 négatif (P1/Hodge/P2), état `+i` **posé** non dérivé.

## 2. Lecture des corps (KB-local, lecture-structure)

- **FH-II `2503.09372` (§5).** Construit le **flot d'interpolation à deux bords** (`Σr ↔ Σr+dr`),
  « completing the program of FH-II ». Établit que **le même type de condition ne peut être imposé
  simultanément aux deux bords** (caractère D↔N forcé). **MAIS omet systématiquement les termes de
  coin** (« we have omitted the corner terms », « neglecting corner terms as before » ; codim-1
  seulement). ⟹ FH-II livre le **squelette deux-bords codim-1**, **pas** `Δ_𝒞` (codim-2, le coin).
- **Horowitz–Wang `1909.11703`.** Une **infinité de conditions de coin** là où une surface
  **spacelike** rencontre le bord conforme AdS : elles **déterminent toutes les dérivées
  temporelles** de la métrique de bord à partir des données initiales ⟹ la donnée de bord **n'est
  pas librement analytique** (« there is still freedom… but it cannot be analytic »). **Contrainte
  de compatibilité**, pas divergence ; liberté **non-analytique** résiduelle.
- **Liu–Santos–Wiseman `2402.04308`.** **Dirichlet pur n'est pas elliptique/bien-posé** ; il existe
  une **famille à un paramètre `p`** de conditions conformes bien-posées (métrique de bord
  **Weyl-rescalée** fixée), avec Anderson(`p→0`) et Dirichlet(`p→∞`) en limites. Stable en euclidien
  pour `p>1/6` ; **instable dynamiquement (lorentzien) hors symétrie sphérique même pour `p>1/6`**.

## 3. Application de la règle → **VERDICT : `C1-b` en AdS**

1. **Finitude (codim-1)** : `Δ_𝒞=d` marginal, `TT̄` absent en `d=3` ⟹ **pas de divergence
   irréductible** côté déformation de bord ⟹ **exclut `C1-c`** par la voie codim-1.
2. **Bonne-position du joint mixte** : le joint est une condition **mixte D↔(N/conforme)**. LSW :
   Dirichlet seul **non bien-posé** ; bonne-position ⟹ **famille conforme à paramètre `p`**. Par la
   **clause 1**, `p` est un **paramètre libre** ⟹ l'objet bien-posé est **conditionnel à `p`** ⟹
   **`C1-b`**, **pas `C1-a`**. Anti-circularité K : ni WCH/Penrose ni l'état `+i` ne fixent `p` (le
   pivot transporte le **swap** mais **pas** le `−1` de Hodge — P1/Hodge/P2) ⟹ `p` est un **vrai
   paramètre neuf**, non manufacturé.
3. **Conditions de coin (HW)** : contraignent la donnée de jonction (liberté **non-analytique**
   résiduelle), **sans divergence**. Par la **clause 2** ⟹ **sur-contrainte**, **pas `C1-c`** ;
   renforce le caractère **conditionnel** (le datum de jonction existe mais est contraint).

**⟹ `C1` instruit en AdS = `C1-b`** : terme de bord de jonction **fini mais conditionnel à un
paramètre `p`** (et à des conditions de coin contraignantes). Ni bien-défini libre (`C1-a`), ni
obstruction irréductible (`C1-c`).

**Caveat viabilité (hors gate C1, clause 3).** L'instabilité dynamique **non-sphérique** de LSW
(même `p>1/6`) menace la **réalité physique** de l'objet conditionnel ; rattachée à l'**aval**
(`C2`/`C3`, réalité de `C_T<0`), **distincte** de la finitude `C1`. Consignée, non comptée dans
`a/b/c`.

## 4. Signal structurel — re-enchevêtrement `α ↔ β/G3` (finding)

> **⚠ RÉFUTÉ par l'audit froid S-O2C-1 (passes 1, 2 & 3, 2026-06-18) — voir §7.** Les TROIS passes
> indépendantes infirment ce finding : le coin de Horowitz–Wang vit à un **bord timelike** (AdS,
> `Λ<0`), tandis que `𝓘⁺` est **spacelike** (`Λ>0`) — **les deux lieux ne coïncident pas
> géométriquement** ⟹ l'assemblage AdS **n'hérite pas** d'obstruction de transport `Λ>0` au coin.
> Mon analogie « même lieu » était **erronée**. **Conséquence** : la conséquence-clé de
> `LC-D-O2-FACTORISATION` (« leverage O₂ indépendante de G3 = `α` seul ») **TIENT** et n'est **PAS
> amendée** ; `α` reste tenu pour indépendant de `β` (passe 2 : depuis des pièces AdS-seules,
> l'indépendance dS n'est « ni établie ni réfutée » — ce qui est exactement le périmètre de `β`/G3,
> non de `α`). **Le texte ci-dessous est conservé pour traçabilité mais ne vaut plus comme finding.**

Les conditions de coin HW vivent au coin **surface-spacelike ↔ bord**. Dans la jonction inter-éons,
ce coin **est** le `𝒞`/scri **spacelike** — **le même lieu géométrique** que le `𝓘⁺` spacelike de
**G3** (`β`). ⟹ Le facteur `α` (assemblage **AdS**) **hérite déjà**, au coin, d'une contrainte
**géométriquement co-localisée avec `β/G3`**. Cela **nuance** la conséquence-clé de
`LC-D-O2-FACTORISATION` (« la leverage O₂ indépendante de G3 = `α` seul ») : `α` n'est peut-être pas
**aussi indépendant** de `β` que la factorisation logique le suggérait.

**Traitement disciplinaire.** Consigné ici comme **FINDING**, **sans surclassement** et **sans
réécriture silencieuse** de FACTORISATION (R-7). Décision d'un **amendement R-7 daté** sur
`LC-D-O2-FACTORISATION` (et propagation) **différée à après l'audit froid** `S-O2C-1` ré-armé — c'est
typiquement le genre de jonction logique qu'un audit indépendant doit confirmer avant propagation.

## 5. Sans surclassement (§6.4) + routage

- **Routage** (cadrage) : `C1^{dS} = C1^{AdS}(α) ∘ transport(β)`. Ce chaînon **instruit `C1^{AdS}`
  = `C1-b`**. `transport(β)` reste **≡ G3, différé**. ⟹ **`C1` NON tranché en dS.**
- **`C1-b` ⟹** le coefficient `O(1)` de `A_T` ne serait pinçable que **modulo `p`** (et modulo `N`) :
  la construction **NE FERME PAS** le résidu de D1 — elle le rend **conditionnel à un paramètre
  neuf**. `C2` (coeff `O(1)`) et `C3` (`⟨TTT⟩`→W³) restent **en aval**, désormais **eux aussi
  conditionnels à `p`**.
- **Aucune réduction de compte.** `{A4 ; A2★ ; N}` **INCHANGÉ** ; A4 non réduit (clos par le pivot) ;
  D1 non clos ; `N` non fixé (≡ Λ) ; A2★ non tranché ; **CCC non démontrée**.
- **Anti-fit.** Règle `a/b/c` **pré-énoncée** (§0) ; route la gate **déjà gelée** vers son issue
  **pré-déclarée** `C1-b`, **aucune nouvelle prédiction** ⟹ **pas d'amendement R-7** pour le verdict.
  Le seul item susceptible d'amendement (§4, re-enchevêtrement) concerne un **chaînon antérieur**
  (FACTORISATION) et est **différé à l'audit froid**.
- **Sceau.** Aucun (fork `S-O2C-2d` : sceau **seulement si** une construction concrète finie émerge ;
  ici l'issue est **conditionnelle** ⟹ **sans-sceau**, style F2/F3/F4/G3/FACTORISATION).

## 6. Dette ouverte / suite

- **Avant toute propagation** de ce verdict (vers `00_index`, `03_glossaire`, `LC-AUDIT-VERDICT`,
  `BRANCHE-FALSIFIABILITE`) : **ré-armement OBLIGATOIRE de l'audit froid `S-O2C-1`** (agent séparé,
  incognito) — porte spécialement sur (a) la qualification `C1-b` (le `p` de LSW est-il vraiment non
  fixé par la donnée de raccord ?) et (b) le finding §4 (re-enchevêtrement `α↔β/G3`).
- **`C2`/`C3` en aval** : désormais conditionnels à `p`. Question neuve pour `C2` : la condition de
  raccord (WCH/+i) **sélectionne-t-elle** une valeur de `p` admissible (sans fabrication, K) ? Si
  oui, `C1-b` pourrait se **resserrer** vers un sous-cas — à instruire séparément (cadrage/fork
  dédié décidé par Thierry).
- **`β` (dS)** : inchangé, **≡ G3 différé**. Le finding §4 suggère que `transport(β)` pourrait
  intervenir **plus tôt** que prévu (dès le coin AdS) — à confronter en G3.

## 7. Audit froid S-O2C-1 — trois passes (2026-06-18)

**Passe 2 — aveugle CERTIFIÉE (instrument propre).** Ne disposait que du **bloc protocole** (délimité
par `====`), sans aucune zone opérateur ⟹ verdict du programme non exposé. Re-dérivation indépendante
depuis les 3 corps + 3 lectures adverses. **Verdict : CONFIRMATION de `C1-b`** (confiance
*modérée-à-élevée dans le régime AdS*, conditionnelle aux identifications de modélisation). Justif. :
terme local fini `½√(−h)T` (pas de divergence) ⟹ `C1-c` écartée ; Dirichlet pur **non-elliptique**
(preuve de Donder, mode courte-longueur survivant) ⟹ bonne-position via **famille à un paramètre `p`
libre** (coefficient GHY ; `p→0` Anderson, `p→∞` Dirichlet) ⟹ `C1-a` écartée ⟹ **`C1-b`**.

**Passe 3 — aveugle CERTIFIÉE (instrument propre, fichier auditeur épuré).** Lancée pour
contrebalancer la passe 1 biaisée, avec le **fichier protocole nettoyé** (`PROMPT-AUDITEUR-S-O2C-1-CLEAN.md`,
zéro zone opérateur, zéro fuite de verdict). Re-dérivation indépendante depuis les 3 corps + 3 lectures
adverses. **Verdict : `C1-b`, confiance modérée.** Converge avec passe 2 sur tout. **Apport propre,
remonté ici** : passe 3 souligne que le **terme de coin codim-2 — l'ingrédient *littéralement* demandé
par la gate C1 — est OMIS** par FH-II (p.13, p.22) ⟹ `C1-b` est atteint par la **voie indirecte**
(Dirichlet mal posé ⟹ bonne-position via famille à paramètre `p`), **PAS** en exhibant un terme de coin
fini ⟹ **la finitude du terme de coin elle-même n'est PAS établie** par les corps. Note aussi une
**résonance** : les conditions de coin (corps 2, p.10) **forcent `S¹×dS₂`** dans la métrique de bord
près de `t=0` — *tentant* vis-à-vis de la cible dS, mais l'auditeur le qualifie de **résonance, pas de
coïncidence de lieux** (cohérent avec §4bis et avec la mention bubble-of-nothing de passe 1).

**Passe 1 — NON certifiée (instrument compromis), conservée pour ses sorties contra-fuite.** Le prompt
v1.1 fourni en entier **fuitait `C1-b` et le finding §4** dans ses zones opérateur (« NE PAS coller »
non contraignantes quand tout le `.md` est joint). ⟹ **disqualifiée** comme confirmation aveugle.
Restent **robustes** : (i) son **infirmation de §4** (contra-fuite : un auditeur biaisé aurait
*confirmé* la thèse exposée ; il l'a infirmée) ; (ii) ses **réserves dérivées des corps**.

**Convergence des trois passes (2 aveugles certifiées + 1 biaisée) :**
1. **`C1-b` confirmé** par les **deux passes aveugles certifiées** (2 & 3) + la biaisée.
2. **Finding §4 RÉFUTÉ** (les trois) : coin AdS *timelike* ≠ `𝓘⁺` *spacelike* dS ; lieux non
   coïncidents ⟹ pas de ré-enchevêtrement `α↔β/G3` établi ⟹ **FACTORISATION non amendée** (α-indép.
   tient ; passes 2 & 3 : indéterminable depuis AdS-seul = périmètre de `β`).
3. **Réserves de modélisation convergentes** (à porter comme nuances, pas surclassement) : FH-II
   interpole **deux rayons d'UNE SEULE surface timelike** du même AdS (≠ deux éons) et **omet** le coin
   codim-2 ; LSW est **euclidien**, traite **Dirichlet↔conforme** (**Neumann ≠ Anderson** : écart) ;
   les 3 corps sont **AdS / cavité / euclidien**, la cible est **dS/CCC** ⟹ **transfert AdS→dS importé**
   (≡ `β`/G3, non établi par les pièces).
4. **CAVEAT ÉLEVÉ (passe 3)** : le **terme de coin codim-2 — objet littéral de C1 — est OMIS** ⟹ `C1-b`
   repose sur la **bonne-position elliptique** (voie indirecte), **pas** sur une finitude de coin
   *exhibée* ⟹ verdict fermement **DÉLIMITATION**, la finitude du coin restant **non établie**.
5. **Anti-fit** : gel `sha` du cadrage **hors-fichier** ⟹ **antériorité non-auditable** par pièce
   (R-36) ; concordance de **contenu** docstring↔cadrage **OK** (les trois passes la confirment).

**Lecture épistémique.** `C1-b` est le verdict du **facteur `α` (AdS)** : un terme de bord de jonction
**fini mais conditionnel à un paramètre `p`**, établi par la voie **bonne-position elliptique** (PAS
par un terme de coin fini *exhibé* — FH-II l'omet). Il **ne transfère pas** automatiquement au joint
dS/CCC : ce transfert **est** `β ≡ G3`, ouvert. Les réserves des auditeurs **renforcent** ainsi la
séparation `α`/`β` posée par FACTORISATION, au lieu de la fragiliser.

**Sans surclassement.** `C1-b` conditionnel ⟹ `A_T` pinçable seulement **modulo `p`** ⟹ **ne ferme
pas** le résidu de D1. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; `N` non fixé ; A4 non réduit ;
A2★ non tranché ; **CCC non démontrée**.
