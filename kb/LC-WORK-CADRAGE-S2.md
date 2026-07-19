---
id: LC-WORK-CADRAGE-S2
titre: "Note de cadrage autoportante — ÉTAGE S2 du lead « dualité graviton-dual de de Haro » (continuation dS de la dualité). Pose le PLAN PAPER-FIRST avant tout calcul lourd, SANS algèbre scellée. Contenu : (I) ce que « seconde route INDÉPENDANTE au signe de C_T » doit vouloir dire précisément (route électrique = ℓ²→i²ℓ² ; dual AdS = même forme, garde-fou S1) ; (II) le point qui décide = la fourche R4 (éq. 65 vs éq. 90 de 0808.2054) — branche 1 « même forme » (réel négatif mais NON indépendant) vs branche 2 « ℓ/κ transforme » (indépendant mais imaginaire) ; (III) la CONTRAINTE DE COHÉRENCE « source unique du signe » qui identifie la question 2 (S²=−1 porte-t-il le i² ?) À la fourche R4, et resserre l'espace des issues vers la CONSOLIDATION (pas une nouvelle route) — avec DEUX incertitudes explicitement flaggées à lever en ouverture ; (IV) faisabilité R1 (re-dérivation dS obligatoire ; premier calcul go/no-go = carte S sur modes BD de dS) ; (V) ordre d'exécution. Réfère la substance par id ; ne duplique NI algèbre NI sceau. Subordonnée à LC-AUDIT-VERDICT §6.4."
codename: LC-RACCORD
type: "note de cadrage (autoportante) — prépare l'ÉTAGE S2 (continuation dS de la dualité de de Haro). Subordonnée à LC-AUDIT-VERDICT §6.4. Successeur logique de LC-WORK-REPRISE-POST-CT-DUAL-S1 (dont elle exécute la recommandation principale : réaliser S2). N'est PAS un chaînon : aucune algèbre, aucun sceau ; plan seulement."
version: 1.1
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v1.1 : ADDENDUM D'EXÉCUTION (additif) — étapes 1-3 du §5 FAITES. (i) levée (LC-WORK-S2-LECTURE-EQ65 : coefficient dual de branche 2 ∝ℓ^{−2}, pas ℓ^{−1}). Étape 2 GO (verif_D_CT_dual_dS.py 13/13 : carte S referme sur les modes BD, S²=−1 préservé, BD=mode propre +i). Étape 3 PERSISTANCE du garde-fou (verif_D_CT_gardefou_dS.py 14/14, firewall : C̃_T=+C_T survit). VERDICT S2 = CONSOLIDATION (branche α du §3, comme pronostiqué) — source unique du signe, pas de seconde route ; étape 4 (R4) résolue par le verdict, étape 5 (question 3) non déclenchée. Scellé dans LC-D-CT-DUAL-DS v0.1 ; clôture LC-WORK-REPRISE-POST-S2. Addendum ajouté avant l'appendice ; corps du cadrage inchangé. SANS SURCLASSEMENT (§6.4) ; périmètre {A4 ; A2★ ; N} inchangé ; CCC non démontrée. | 2026-06-10 — v1.0 : note de cadrage initiale de S2, produite après contrôle d'ouverture (versions 9/9, ancres OK, doublon LC-D-CT-REALITE v0.1 nettoyé en KB, sceau verif_D_CT_dual.py re-exécuté EXIT 0 18/18). Pose le plan paper-first de S2 et l'observation centrale : question 2 (i² structurel de S²=−1) ≡ fourche R4, ce qui resserre les issues vers la consolidation (source unique du signe), modulo deux incertitudes flaggées : (i) puissance de ℓ du coefficient dual de branche 2 (à relire éq. 65) ; (ii) persistance de la compensation du garde-fou S1 sous continuation dS (seul vrai calcul ouvert). Discipline §6.4 : AUCUN surclassement ; tout est `à inventer` / `décision ouverte` ; périmètre {A4 ; A2★ ; N} inchangé ; D1 NON clos ; (A) physique conditionnel au seul A2★ inchangé ; CCC non démontrée."
statut: "CADRAGE — à exécuter en conversation neuve sur KB propre, paper-first. AUCUN sceau, AUCUNE algèbre déposée par cette note. Verdict pronostiqué (NON acquis) : consolidation (source unique du signe + garde-fou durci) plus probable qu'une seconde route propre ; le point qui pourrait démentir = §4 étape 3 (persistance du garde-fou en dS). Périmètre {A4 ; A2★ ; N} inchangé quel que soit le verdict de S2."
prerequis_kb: [LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-CT-ATN, LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-D-NONLIN-VERROU, LC-AUDIT-VERDICT, LC-WORK-REPRISE-POST-CT-DUAL-S1]
fichiers_compagnons_kb: [verif_D_CT_dual.py, verif_D_CT_realite.py, verif_D_CT_ATN.py, "0808_2054v1.pdf (de Haro, arXiv:0808.2054 ; éq. 43-44, 51, 61-63, 65, 90, App. D éq. 139)"]
tags_epistemiques: [à inventer, décision ouverte, formalisable]
---

# Cadrage — ÉTAGE S2 : continuation dS de la dualité de de Haro

> **Pour l'instance qui exécute S2.** Note de cadrage autoportante. Recharge `prerequis_kb` à la demande.
> Discipline `LC-AUDIT-VERDICT §6.4` : cette note ne porte **aucune** algèbre et **aucun** sceau ;
> c'est un plan. « Dualité dS reproduite » ≠ « seconde route au signe acquise » ≠ « D1 fermé / CCC
> démontrée ». S2 reste en `d=3` (toujours citer la dimension). Périmètre `{A4 ; A2★ ; N}` **inchangé**
> quel que soit le verdict ; D1 non clos ; (A) physique conditionnel au seul A2★ inchangé.

---

## 0. Où l'on en est `[contexte — déjà en KB]`

- **S1 (AdS) clos et scellé** (`LC-D-CT-DUAL` v0.2, `verif_D_CT_dual.py` EXIT 0, 18/18) : dualité des
  EOM `S=[[0,−1],[1,0]]`, `S²=−𝟙` (vp `±i`) ; **garde-fou** `C̃_T=+C_T` **en AdS** (le `−` de `W̃=−W`
  compensé par le `−2` de `⟨T̃⟩`) ; dictionnaire `C_T↔ℓ²/κ²↔N`, facteur de convention `=4`.
- **Route électrique `[A]` scellée** (`LC-D-CT-REALITE`) : `C_T∝ℓ^{d-1}/G` ; continuation
  `ℓ_AdS→iℓ_dS` attache `i^{d-1}` ⟹ `d=3` **réel négatif**, `C_T(d=3)=−N/(32π²)`.
- **Modes dS disponibles** (`LC-D3-WEYL-BUNCHDAVIES`) : mode TT de dS₄, `f''−(2/η)f'+k²f=0`, mode de
  Bunch–Davies `∝(1−ikη)e^{ikη}` ; `E_ij=(d/2H)g₍₃₎`.
- **S2 = le vrai `à inventer`** : continuer la dualité au bulk **dS₄** et tester l'existence d'une
  **seconde route, indépendante**, au signe de `C_T`.

---

## 1. Ce que « seconde route INDÉPENDANTE » doit vouloir dire `[définition — verrou logique]`

Le signe de la route électrique vient d'**une seule** opération : `ℓ² → (iℓ)² = −ℓ²` (`i²=−1` en
`d=3`). En AdS, le secteur dual donne le **même** coefficient `ℓ²/κ²` (éq. 90, *« the dual two-point
takes the same form »*) — c'est le garde-fou S1 (`C̃_T=+C_T`). Donc une route dual n'est
**indépendante** que si, sous continuation dS, elle livre le signe par une opération **différente**
de `ℓ²→i²ℓ²`. Sinon : route électrique déguisée ⟹ `consolidation`, **pas** réduction du compte.

---

## 2. Le point qui décide tout : la fourche R4 (éq. 65 vs éq. 90) `[décision ouverte]`

Deux branches pour le coefficient dual de **parité-paire** (où vit `C̃_T` ; **pas** le Cotton, qui
est parité-impaire `∝1/μ` — risque R3) :

- **Branche 1 — « même forme » (éq. 90).** Coefficient dual `= ℓ²/κ²`. Sous `ℓ→iℓ` : même
  `i²=−1`. ⟹ réel négatif **OUI**, indépendant **NON** (même `ℓ²` continué).
- **Branche 2 — « seconde possibilité » (éq. 65, `ℓ/κ` transforme sous `S`).** Coefficient dual
  `∝ 2κ/ℓ`, donc `∝ ℓ^{−1}`. Sous `ℓ→iℓ` (`κ∝√G` **ne continue pas** — règle de `REALITE`) :
  facteur `i^{−1}=−i`. ⟹ indépendant **OUI**, réel négatif **NON** (imaginaire).

---

## 3. Contrainte de cohérence « source unique du signe » `[observation centrale du cadrage]`

Le garde-fou S1 dit qu'**en AdS** le `i²` de `S²=−1` (vp `±i`) **n'entre pas** dans `C_T` (compensé
par le `−2` de `⟨T̃⟩`). Or `C_T(d=3)` est réel négatif, scellé via l'électrique. La cohérence
**interdit de compter le `i²` deux fois** : si S2 trouvait que `S²=−1` réinjecte un `i²` sous
continuation dS *en plus* du `ℓ→iℓ` électrique, alors `(−1)(−1)=+1` ⟹ `C_T>0`, **contradiction**
avec le sceau `REALITE`.

**Conséquence (le cœur du cadrage).** La **question 2** (« `S²=−1` porte-t-il le `i²`
structurellement ? ») et la **fourche R4** sont **la même décision** :

- **(α)** le `i²` reste dans `ℓ→iℓ` seul, le garde-fou **persiste** en dS ⟹ dual **confirmatoire**
  (= branche 1), pas de route indépendante, signe à **source unique** (continuation de `ℓ²`) ;
- **(β)** la continuation dS **brise** la compensation, `S²=−1` devient la source du signe ⟹
  l'électrique ne doit alors **plus** flipper ⟹ branche 2 ⟹ coefficient `∝1/ℓ` ⟹ **imaginaire**.

Dans les deux cas : **pas de seconde route propre vers un réel négatif** — soit non indépendante
(α), soit imaginaire (β). ⟹ **L'issue la plus probable de S2 est une `consolidation`** : verrouiller
le signe sur une **source unique** et **durcir le garde-fou**, **pas** ajouter une route. C'est un
verdict §6.4 valide (consolidation, **pas** réduction du compte `{A4 ; A2★ ; N}`).

**DEUX incertitudes à lever en ouverture (ce cadrage est paper-level, NON scellé) :**
- **(i)** la **puissance de `ℓ`** du coefficient dual de branche 2 (`2κ/ℓ`) est compressée depuis la
  carte de lecture P2 — **à relire sur éq. 65** de `0808_2054v1.pdf` (confirmer/infirmer `∝ℓ^{−1}`).
- **(ii)** la **persistance de la compensation** du garde-fou S1 sous continuation dS n'a **rien
  d'évident** — c'est le **seul vrai calcul ouvert** et le seul point qui peut **démentir** le
  pronostic du §3. Si (ii) tombe d'une manière non prévue ici, une route pourrait exister :
  l'espace n'est **pas** clos par décret.

---

## 4. Faisabilité R1 (risque central) et premier calcul go/no-go `[à inventer]`

De Haro est en **AdS₄** et **diffère explicitement** notre cas (§4.7, `λ<0` : *« we leave for the
future »*). ⟹ `S²=−1` et `W̃=−W` sont **à re-dériver en dS₄**, **pas** à transposer. Espoir : la
dualité **algébrique** des EOM (éq. 43-44) repose sur la structure d'**oscillation radiale**
(`f_a=cos u+u sin u`, `f_b=u cos u−sin u`, `u=|p|r`), dont les analogues dS sont les modes BD
(`(1−ikη)e^{ikη}`, en KB `WEYL-BUNCHDAVIES`).

**Premier calcul de S2 (paper, puis petit sceau `verif_D_CT_dual_dS.py`) :** une **identité de 3e
dérivée** analogue à éq. 44 referme-t-elle sur les modes BD de dS, et avec quel `S²` ? **Go/no-go** :
si la carte `S` ne referme pas en dS ⟹ le lead s'arrête (`hors de portée`, verdict honnête). Si elle
referme ⟹ lire `S²` et brancher §2–§3.

**Contrôle croisé :** **App. D** de de Haro (solution lorentzienne, `r³`, `i` explicite dans le
secteur de jauge, éq. 139) est le morceau le plus proche de notre signature — vérifier si ce `i`
se relie au `i²` recherché.

---

## 5. Ordre d'exécution proposé `[conversation neuve, KB propre, paper-first]`

1. **Relecture ciblée** de `0808.2054` éq. **65** et **90** → lève l'incertitude **(i)** (puissance
   de `ℓ` des deux branches).
2. **Carte `S` en dS** : identité de 3e dérivée sur les modes BD → `S²` en dS (**go/no-go**, R1).
   Petit sceau `verif_D_CT_dual_dS.py`.
3. **Persistance du garde-fou** sous continuation : la compensation `(−2)` survit-elle ? → lève
   **(ii)** (le seul point qui peut démentir le §3).
4. **Trancher R4** au crossover CCC ⟹ répond conjointement à la **question 1** (indépendance) et à la
   **question 2** (`i²` structurel — fusionnées par §3).
5. **Question 3** (Dirichlet vs duale = raccordement, R2) **seulement si** 1–4 livrent une route
   propre ; sinon elle reste `décision ouverte` sur l'item « CFT de raccordement »
   (`LC-D-HOLOGRAPHIE-G3 §3` : la CFT duale en est un candidat de structure).

---

## 6. Garde-fous `[discipline §6.4 — portés tout du long]`

- **S2 reste en `d=3`** (parité de `ℓ^{d-1}` ; `S²=−1` en `d=3`) — toujours citer la dimension.
- **Un `−` de fonctionnelle ne vaut pas un flip** tant que le préfacteur de la définition de
  l'opérateur dual n'a pas été vérifié (méthode P1, `LC-D-CT-DUAL`).
- **Distinguer** coefficient de **Cotton** (parité-impaire, `∝1/μ`) de `C̃_T` (parité-paire) — le
  signe vit dans le parité-pair de `T̃` (R3).
- **« Reproduit en dS » ≠ « seconde route acquise » ≠ « D1 fermé / CCC démontrée ».** Périmètre
  `{A4 ; A2★ ; N}` **inchangé** quel que soit le verdict. (A) physique conditionnel au seul A2★
  inchangé. « Le bang gagne » (P6 B) intact.
- **Consolidation ≠ réduction du compte.** Le verdict pronostiqué (§3) est une consolidation ; s'il
  se confirme, il **ne réduit pas** le compte — il verrouille le signe sur une source unique.

---

## 7. Addendum d'exécution `[ajouté 2026-06-10 — étapes 1-3 faites, S2 clos]`

Le cadrage ci-dessus a été **exécuté** (étapes 1-3 du §5) :
- **(i) levée** (`LC-WORK-S2-LECTURE-EQ65`) : le coefficient dual de branche 2 est `∝ℓ^{−2}` (= `(2κ/ℓ)²`, le `2κ/ℓ` étant le **couplage** `ℓ′/κ′`, pas le coefficient), **pas** `ℓ^{−1}` ⟹ branche 2 sous `ℓ→iℓ` donne `i^{−2}=−1` = **réel négatif, non indépendant** ⟹ pronostic §3 **renforcé**.
- **Étape 2 GO** (`verif_D_CT_dual_dS.py`, 13/13) : la carte `S` **referme** sur les modes BD (EOM dS de même forme que l'EOM radiale AdS ; `S²=−1` préservé ; BD `= f_a−i f_b` = mode propre `+i`).
- **Étape 3 PERSISTANCE** (`verif_D_CT_gardefou_dS.py`, 14/14, firewall) : le garde-fou **survit** en dS (`i^{d-1}` porté identiquement ; `−2` et `−` relatif sans `ℓ` non continués ⟹ `C̃_T=+C_T`).

**Verdict S2 : CONSOLIDATION** (branche **α** du §3, comme pronostiqué) — source **unique** du signe, **pas** de seconde route indépendante. **Étape 4 (R4)** résolue **par** le verdict ; **étape 5 (question 3)** non déclenchée (reste `décision ouverte` sur l'item « CFT de raccordement »). Scellé dans `LC-D-CT-DUAL-DS` v0.1 ; clôture consignée dans `LC-WORK-REPRISE-POST-S2`. Périmètre `{A4 ; A2★ ; N}` **inchangé** ; CCC non démontrée.

---

## Appendice — fil rouge `[orientation]`

Le projet teste, maillon par maillon, si la CCC de Penrose peut être rendue **cohérente** en
**réduisant le nombre d'hypothèses/nombres indépendants** (jamais en « prouvant » la CCC). S1 a posé
la base AdS de la dualité graviton-dual et un garde-fou de signe. S2 est l'étage où ce lead **paie ou
non** : continuer la dualité au bulk dS₄ et trancher si le secteur magnétique/dual donne une
**seconde route, indépendante**, au signe de `C_T`. Le cadrage ci-dessus suggère — **sans le sceller**
— que l'issue la plus probable est **consolidante** (source unique du signe, garde-fou durci) plutôt
qu'une nouvelle route, le seul point réellement ouvert étant la persistance du garde-fou sous
continuation dS (§4 étape 3). *Discipline §6.4 de bout en bout ; S2 à inventer ; D1 non clos ;
circularité LC-E non brisée ; A3/A4 non fusionnés ; la CCC n'est pas démontrée.*
