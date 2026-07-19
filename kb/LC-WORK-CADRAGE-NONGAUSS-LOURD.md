---
id: LC-WORK-CADRAGE-NONGAUSS-LOURD
titre: "Note de travail (cadrage paper-first) — OUVRE le front §3.2 « PASSAGE LOURD du trois-point ⟨g₃g₃g₃⟩ » (décision (a) de Thierry, 2026-06-12, sur LC-WORK-REPRISE-POST-CB §3). Le passage lourd honore les QUATRE exigences contractuelles héritées (LC-AUDIT-LOG-NONGAUSS §5 ; LC-WORK-REPRISE-POST-AUDIT-NONLIN-2PT §3.2) : (E-L1) étalon Ward OP NUMÉRIQUE — tester P1'-A TELLE QU'ÉCRITE (|C_T|/N=1/(32π²) nu, slack nul), pas sa lecture dS-native ; (E-L2) forensique ε·ε*=4 vs 2 — énoncé explicite chez MP, extrait p.6 EXTENSIBLE À CE MOMENT-LÀ SEULEMENT (manifeste NONGAUSS, résidu gelé) ; (E-L3) R-7 dès le gel — amendement formel daté de toute décision de scoping réductrice post-gel ; (E-L4) périmètre S1 — perturbatif TT niveau arbre, quatre-point/boucles/non-perturbatif HORS périmètre. Le rang-3 « par invariance » (rendu formulable par LC-D-NONLIN-2PT) RECOUPE ce front et est traité ici par scoping explicite (S-L1), jamais ouvert séparément. AUCUN fetch pour produire cette note : tout est algèbre interne (chaînons scellés) ou consignations KB ([E4] : coefficients Ward OP (d−2)(d+3)=6 et d(d+2)=15 déjà en 04_references). Cibles PL gelées ici SANS fetch ; R-7 ARMÉE à la validation. Subordonnée à LC-AUDIT-VERDICT §6.4 : un secteur Ward reproduit = établi (algèbre) d'une cohérence de coefficients, JAMAIS « secteur non-gaussien fermé / D1 fermé / N fixé / CCC démontrée ». Compte {A4 ; A2★ ; N} INCHANGÉ."
codename: LC-RACCORD
type: "note de travail (cadrage paper-first) — ouvre le front §3.2 (passage lourd du trois-point). N'EST PAS un chaînon : aucune algèbre scellée, aucun sceau, AUCUN fetch ici. Subordonnée à LC-AUDIT-VERDICT §6.4. Successeur direct de LC-WORK-REPRISE-POST-CB §2/§3 et de LC-AUDIT-LOG-NONGAUSS §5."
version: 0.1
langue: fr
date: 2026-06-12
maj: "2026-06-12 — v0.1 : cadrage paper-first du passage lourd (décision (a) de Thierry). Quatre exigences contractuelles transcrites verbatim et opérationnalisées ; six décisions de scoping S-L1..S-L6 surfacées avec recommandations ; cibles PL-A..PL-D gelées SANS fetch (PL-A = P1'-A telle qu'écrite) ; protocole anti-fit bi-phase (phase 1 interne EXIT 0 AVANT tout fetch, pattern NONLIN-2PT) ; plan de sceau verif_D_nongauss_TTT_lourd.py (6 blocs A–F) ; plan d'extraits (p.6 MP + pages Ward OP, manifeste NEUF, R-10) ; audit à froid recommandé (R-14). AUCUN dépôt, AUCUN fetch, AUCUNE touche KB ici."
statut: "CADRAGE — à valider par Thierry AVANT toute exécution. R-7 ARMÉE dès la validation : les cibles §3 deviennent les libellés gelés ; toute décision de scoping réductrice ultérieure exige un amendement formel daté du libellé, dans la même session. Aucun fetch tant que la phase 1 du sceau n'est pas EXIT 0. Périmètre {A4 ; A2★ ; N} inchangé ; D1 non clos ; CCC non démontrée."
prerequis_kb: [LC-D-NONGAUSS-TTT, LC-AUDIT-LOG-NONGAUSS, LC-WORK-CADRAGE-NONGAUSS, LC-WORK-AUDIT-EXTRAITS-MANIFESTE, LC-D-NONLIN-2PT, LC-D-CT-GAMMA, LC-D-CT-ATN, LC-D3-SPECTRE-K3, LC-AUDIT-VERDICT, LC-04-REFERENCES, LC-00-INDEX]
fichiers_compagnons_kb: [verif_D_nongauss_TTT.py, verif_nonlin_deuxpoint__1_.py, EXTRAIT_1104_2846v2_MP.pdf, EXTRAIT_hepth9307010v2_OP.pdf, EXTRAIT_1603_03771v2_C24.pdf, EXTRAIT_1511_04077v2_AppC.pdf]
tags_epistemiques: [établi (algèbre), formalisable, à inventer, hors de portée, décision ouverte]
---

# Cadrage — PASSAGE LOURD du trois-point `⟨g₃g₃g₃⟩` ; contrat honoré telle-qu'écrite

> **Pour validation AVANT exécution.** Décision (a) de Thierry (2026-06-12) sur le menu
> de `LC-WORK-REPRISE-POST-CB §3`. **Aucun fetch n'a été fait** pour produire cette note :
> tout ce qui suit est algèbre interne (chaînons scellés) ou consignation KB existante.
> En particulier la **p.6 de MP n'a pas été lue** (résidu gelé du manifeste NONGAUSS,
> extensible au sceau seulement, E-L2) et les PDF n'ont pas été ouverts. Discipline
> `LC-AUDIT-VERDICT §6.4` portée tout du long.

---

## 0. Mandat — les QUATRE exigences contractuelles `[héritées, transcrites verbatim]`

Le passage lourd n'est pas un front libre : il exécute un **contrat** écrit par l'audit à
froid du passage léger (`LC-AUDIT-LOG-NONGAUSS §5`) et porté inchangé par trois notes de
reprise successives. Les quatre exigences, opérationnalisées :

- **(E-L1) Étalon Ward OP numérique.** Source (log §5, verbatim) : « tout futur passage
  lourd testera **P1'-A telle qu'écrite** (`|C_T|/N = 1/(32π²)`, étalon Ward OP
  numérique), pas sa lecture dS-native ». Opérationnalisation : le secteur Ward/contact de
  `⟨TTT⟩` doit être ancré sur les **coefficients Ward d'OP avec leurs valeurs numériques**
  — en `d=3` : `(d−2)(d+3)=6` et `d(d+2)=15`, déjà consignés en KB (`04_references`,
  renvoi [E4], « étalon numérique = passage lourd, exigence telle-qu'écrite ») — et
  reproduire `|C_T|/N=1/(32π²)` (convention **nue**, γ=1) avec **slack nul**. Le test du
  léger (« pinning par la chaîne exacte ») ne compte pas : ici l'étalon est la formule
  d'OP **telle qu'imprimée**, valeurs comprises.
- **(E-L2) Forensique `ε·ε*`.** Source (R-4, requalification d'audit) : « `ε·ε*=4`
  **cohérent** avec le facteur 4 de l'éq. 2.6 ; énoncé explicite à vérifier au passage
  lourd (p.6) ». Opérationnalisation : exhiber **verbatim** l'énoncé de normalisation des
  polarisations chez MP (attendu p.6 de 1104.2846), trancher **4 vs 2**, et vérifier que
  le verdict est **absorbé par le catalogue d'artefacts `{2,4,8}`** sans toucher aux
  ratios scellés du léger (qui étaient construits insensibles à `ε·ε*` — propriété à
  re-vérifier explicitement, et tout impact consigné tel quel). L'extrait p.6 est
  **extensible à ce moment-là seulement** (manifeste NONGAUSS, résidu gelé).
- **(E-L3) R-7 dès le gel.** Règle permanente (VERDICT §8bis) : toute décision de scoping
  qui réduit le périmètre de test d'une cible gelée doit s'accompagner d'un **amendement
  formel et daté du libellé de la cible, dans la même session** que la décision. R-7 est
  **armée à la validation de cette note** (le gel = §3 ci-dessous). C'est la leçon
  procédurale P1'-A : la bifurcation dS-native du léger était pré-fetch et tracée, mais le
  libellé non amendé — défaut réel, non reproduit ici.
- **(E-L4) Périmètre S1.** Perturbatif TT, niveau arbre, premier ordre du vertex.
  **Quatre-point, boucles, non-perturbatif : HORS périmètre** (héritage S1 de
  `LC-WORK-CADRAGE-NONGAUSS §0`, inchangé). Tout débordement = violation de périmètre,
  pas un bonus.

**Recoupement déclaré.** Le rang-3 « **par invariance** » — l'analogue trois-point du
verrou de forme `LC-D-NONLIN-2PT` (comptage de représentation : dimension de l'espace des
formes invariantes) — a été rendu **formulable** par le rang 2 et **recoupe ce front**.
Les notes de reprise interdisent de l'ouvrir séparément sans cadrage explicite : il est
donc **tranché ici** (S-L1), dans un sens ou dans l'autre.

---

## 1. Objet, dérivé sur papier `[aucun fetch ; tout vient des chaînons scellés]`

**Ce que le léger a laissé.** `LC-D-NONGAUSS-TTT` v0.1 a scellé : `⟨g₃³⟩_libre=0`
(la chaîne linéaire transporte) ; `γ₃=n³=8` (Brown-York, catalogue `{2,4,8}`) ; comptage
`d=3` = **2 formes paires + 1 impaire hors bispectre** (MP∩OP) ; amplitude Einstein
`64π⁴/N²` pendue à `N` seul, ratio `(H/M_Pl)⁴/A_T²=π⁴/4` slack nul. Ce qui n'a **pas**
été testé : l'ancrage **CFT-Ward numérique** de P1'-A (lecture dS-native seulement) et
l'énoncé explicite `ε·ε*`.

**Ce que le lourd ajoute — et seulement cela.** Deux jambes, plus une optionnelle :

1. **Jambe Ward (E-L1).** En CFT, les identités de Ward de difféomorphisme lient le
   secteur de **contact** de `⟨TTT⟩` au deux-point `⟨TT⟩` : les coefficients des termes
   de contact sont des multiples **fixés** de `C_T`, avec des facteurs purement
   cinématiques que OP donne en `d` général — c'est là que vivent `(d−2)(d+3)` et
   `d(d+2)`. Côté programme, le deux-point est scellé : forme `k³·Π^TT`
   (`LC-D3-SPECTRE-K3`, re-verrouillée par invariance `LC-D-NONLIN-2PT`), amplitude
   `|C_T|/N=1/(32π²)` nue (`LC-D-CT-ATN`, convention `LC-D-CT-GAMMA`). Le test lourd :
   écrire le secteur Ward de `⟨TTT⟩` **dans l'appareil d'OP, valeurs numériques
   comprises**, y injecter le `C_T` du programme, et vérifier la refermeture **slack
   nul** sur `1/(32π²)`. Aucun nombre neuf n'a le droit d'apparaître : si la refermeture
   exige un coefficient ad hoc, c'est un **échec consigné tel quel**.
2. **Jambe forensique (E-L2).** Localiser chez MP l'énoncé de normalisation
   `Σ_s ε^s_{ij} ε^{s*}_{kl}` (attendu p.6), trancher 4 vs 2 verbatim, et re-dériver
   l'insensibilité des ratios scellés (léger) à ce choix — ou consigner l'impact.
3. **Jambe invariance (optionnelle, S-L1).** Analogue rang 3 du verrou de forme :
   montrer par théorie des représentations (petit groupe, parité) que l'espace des
   structures invariantes du trois-point TT (`Δ=d=3`) a la dimension **déjà scellée par
   comptage** au léger (2 paires ; l'impaire hors bispectre), sans consommer MP/OP —
   puis recouper. C'est une dérivation **interne** (phase 1), pas un fetch.

**Ce que le lourd n'est pas.** Pas une re-dérivation du bispectre complet de MP ; pas un
calcul de vertex cubique ab initio (hors mandat, coût non contractuel) ; pas une attaque
du coefficient `W³` (qui reste `décision ouverte`, nul sous Einstein pur) ; rien au
quatre-point (S1).

---

## 2. Décisions de scoping `[S-L1..S-L6 — à trancher à la validation]`

- **(S-L1) Jambe invariance rang 3 : INCLUSE ou non ?**
  - **(a) INCLUSE** comme bloc de phase 1 du même sceau (recommandé). Motifs : le menu
    interdit de l'ouvrir séparément sans cadrage — ce cadrage **est** le véhicule prévu ;
    la machinerie SVT/représentation du rang 2 se transpose ; elle fournit une **route
    interne indépendante** vers le comptage 2+1, ce qui blinde la jambe Ward (le comptage
    n'est alors plus suspendu au seul fetch MP∩OP du léger).
  - (b) EXCLUE — reste `décision ouverte`, le lourd se limite strictement à E-L1/E-L2.
  - **Recommandation : (a).** Si (a), la cible PL-D (§3) est active ; si (b), PL-D est
    retirée **avant gel** (pas d'amendement nécessaire : la décision précède le gel).
- **(S-L2) Parité au lourd.** La jambe Ward (E-L1) porte sur le secteur **pair**
  (le bispectre ; l'impaire en est absente, scellé au léger). Si S-L1(a), la jambe
  invariance couvre **les deux parités** au niveau du comptage (comme le rang 2).
  **Recommandation : pair pour Ward, deux parités pour l'invariance** — c'est l'héritage
  S2 du léger, inchangé pour le bispectre.
- **(S-L3) Véhicule : chaînon NEUF.** `LC-D-NONGAUSS-TTT` **reste v0.1** (baseline
  d'audit gelée, byte-identique) ; le lourd produit un chaînon successeur
  `LC-D-NONGAUSS-TTT-LOURD` v0.1 + sceau `verif_D_nongauss_TTT_lourd.py`. Pattern c_B /
  NONLIN-2PT. **Recommandation : oui** (aucune alternative sérieuse : amender le chaînon
  audité violerait la discipline de gel).
- **(S-L4) Audit à froid : COMMANDÉ.** Contrairement à c_B (déductif, coût faible), le
  lourd consomme des fetchs neufs (p.6 MP, pages Ward OP) et teste une cible
  contractuelle telle-qu'écrite : profil typique d'audit. Protocole (a)-(f) avec (f)
  conformité R-7 ; **R-14 applicable** (contrôle d'inventaire d'ouverture dans
  l'instruction). **Recommandation : oui**, 3-4 passes incognito, session(s) dédiée(s).
- **(S-L5) Extraits : manifeste NEUF.** Extension p.6 MP (E-L2) + pages Ward d'OP
  (numéros déterminés au fetch, découpe mécanique, sha consignés) ⟹ nouveau manifeste
  `LC-WORK-AUDIT-EXTRAITS-MANIFESTE-LOURD` + `EXTRAIT_*.pdf` neufs. Le manifeste NONGAUSS
  v0.1 **n'est pas réécrit** (R-10 : dépôts distincts, jamais d'écrasement).
  **Recommandation : oui.**
- **(S-L6) Bi-phase stricte (pattern NONLIN-2PT).** Phase 1 interne (non-régressions du
  léger + appareil Ward symbolique côté programme + jambe invariance si S-L1a) écrite et
  **EXIT 0 AVANT tout fetch**, déposée en **fichier distinct** (R-10, byte-identité des
  asserts de phase 1 vérifiable a posteriori) ; phase 2 = fetch (OP Ward numérique, MP
  p.6) + refermetures. **Recommandation : oui** (non négociable en pratique : c'est la
  seule architecture qui rende E-L1 anti-fit).

---

## 3. CIBLES PRÉ-ENREGISTRÉES `[PL — GELÉES ICI, SANS FETCH ; R-7 armée dessus]`

- **PL-A (= P1'-A telle qu'écrite — exact, slack nul).** Le secteur Ward de `⟨TTT⟩`,
  exprimé dans l'appareil d'Osborn-Petkos **avec les coefficients Ward numériques tels
  qu'imprimés** (en `d=3` : `(d−2)(d+3)=6`, `d(d+2)=15` — consignés [E4]), une fois les
  maps de convention figées appliquées (nue, `γ₃=8` canonique↔nu, catalogue `{2,4,8}`),
  doit reproduire `|C_T|/N = 1/(32π²)` (nu), **exactement, slack nul**. Aucun coefficient
  libre n'est introduit pour faire passer la refermeture.
- **PL-B (forensique `ε` — verbatim, tranchée).** L'énoncé explicite de la normalisation
  des polarisations chez MP est exhibé verbatim (attendu p.6 ; si l'énoncé est ailleurs,
  la page réelle est consignée sans pénalité) et tranche `ε·ε* = 4` **ou** `2`. Le
  verdict, quel qu'il soit, est absorbé par le catalogue `{2,4,8}` ; l'insensibilité des
  ratios scellés du léger à `ε·ε*` est re-dérivée explicitement. Si un ratio scellé
  s'avère sensible : **échec consigné tel quel** (pas de rattrapage).
- **PL-C (non-régression du léger — exact).** `γ₃=8` ; `(H/M_Pl)⁴/A_T²=π⁴/4` slack nul ;
  `⟨g₃³⟩_libre=0` identiquement — re-vérifiés dans le sceau lourd, valeurs inchangées.
- **PL-D (invariance rang 3 — active si S-L1a).** L'espace des structures invariantes du
  trois-point TT (`Δ=d=3`, niveau arbre) dérivé par représentation **sans consommer
  MP/OP** a pour dimension le comptage déjà scellé : **2 formes paires**, la forme
  impaire étant hors bispectre. Recoupement avec le comptage fetché du léger = contrôle,
  pas découverte.

**Ce que les cibles ne sont pas.** PL-A..D sont les prédictions du programme, gelées
avant tout fetch ; les sources (OP, MP) sont les comparanda, pas les cibles. Tout
ajustement post-fetch d'un libellé PL = violation R-7, point.

**Issues de réfutation pré-enregistrées.** PL-A échoue si la refermeture exige un nombre
hors `{N, coefficients OP imprimés, catalogue {2,4,8}}` ⟹ consigner « ancrage Ward non
établi », le léger reste vrai tel qu'écrit (sa lecture dS-native n'est pas rétractée par
un échec du lourd). PL-B échoue si aucun énoncé explicite n'existe chez MP ⟹ R-4 reste
« cohérent », requalification consignée, pas inventée. PL-D échoue si la dimension
interne diffère du comptage fetché ⟹ conflit consigné, arbitrage = décision ouverte.

---

## 4. Protocole anti-fit `[hérité, durci]`

1. **Bi-phase matérialisée dans le script** (S-L6) : phase 1 interne EXIT 0 avant tout
   fetch ; dépôt de phase en fichier distinct (R-10) ; asserts de phase 1 byte-identiques
   dans la version finale.
2. **Cibles gelées = §3 de cette note**, à la validation. R-7 armée : tout scoping
   réducteur post-gel ⟹ amendement formel daté du libellé, même session.
3. **Fetch tracé** : pages consommées listées au manifeste neuf (S-L5), sha256 des
   extraits, découpe mécanique ; p.6 MP étendue à ce moment-là seulement (E-L2).
4. **Mutation pilote** avant tout verdict : au moins une injection fausse vérifiée
   cassante hors sceau (pattern c_B), puis firewall dans le sceau.
5. **Tri de provenance** : chaque nombre du sceau étiqueté interne / fetché / convention ;
   le dictionnaire `N`-holographique reste infetchable (contrôle hérité de l'audit léger).
6. **Audit à froid** (S-L4) : instruction autoportante avec contrôle d'inventaire
   d'ouverture (R-14) et volet (f) conformité R-7.

---

## 5. Plan de sceau `verif_D_nongauss_TTT_lourd.py` `[6 blocs A–F, bi-phase]`

- **[A] (phase 1)** Non-régressions PL-C : `γ₃=8`, `π⁴/4`, `⟨g₃³⟩_libre=0` (symbolique).
- **[B] (phase 1)** Appareil Ward côté programme : identités de Ward de difféo sur le
  secteur de contact de `⟨TTT⟩` écrites symboliquement à partir du deux-point scellé
  `k³·Π^TT` + `C_T` nu ; coefficients laissés **symboliques** (aucune valeur OP ici).
  Si S-L1a : **[B']** jambe invariance PL-D (petit groupe, deux parités, dimension).
- **— GEL DE PHASE : dépôt fichier distinct, EXIT 0 requis — puis seulement :**
- **[C] (phase 2, fetch OP)** Étalon Ward numérique PL-A : coefficients `6`, `15`
  telle-qu'écrite (extraits, sha) ; injection du `C_T` programme ; refermeture
  `|C_T|/N=1/(32π²)` slack nul.
- **[D] (phase 2, fetch MP)** Forensique PL-B : énoncé `ε·ε*` verbatim p.6, verdict
  4 vs 2, absorption catalogue, insensibilité des ratios re-dérivée.
- **[E]** Anti-numérologie / DoF : 0 entrée libre neuve ; sorties appariées comptées.
- **[F]** Firewall : injections cassantes — `C_T` faussé ; coefficient Ward `6→7` ;
  `ε·ε*` flippé 4↔2 là où il doit mordre ; `n≠2` ; `d≠3`. Chaque injection doit casser
  un assert identifié.

**Livrables du cycle** (validation fichier par fichier, pattern habituel) : ce cadrage ;
dépôt de phase 1 ; sceau final ; chaînon `LC-D-NONGAUSS-TTT-LOURD` v0.1 ; manifeste +
extraits neufs ; instruction d'audit (si S-L4 oui) ; puis lot de propagation et note de
reprise en clôture.

---

## 6. Garde-fous `[§6.4 — non négociables]`

Un PASS intégral du lourd se lira : « **ancrage Ward numérique reproduit + forensique
tranchée** — `établi (algèbre)`, conditionnel aux entrées amont scellées (`A_T·N=16`,
`n=2`, relation BD, convention nue) et à la gravité d'Einstein ». **Jamais** : « secteur
non-gaussien fermé / D1 clos / N fixé / CCC démontrée ». La liberté `W³~(LH)⁴` reste
`décision ouverte` ; le quatre-point hors périmètre ; l'amplitude `A_T~1/N` reste LA
décision ouverte du secteur. Compte **{A4 ; A2★ ; N} INCHANGÉ** quel que soit le verdict.
