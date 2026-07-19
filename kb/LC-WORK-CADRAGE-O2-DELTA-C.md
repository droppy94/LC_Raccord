---
id: LC-WORK-CADRAGE-O2-DELTA-C
titre: "Cadrage GELÉ (paper-first / anti-fit) du fork S-O2C-2 — extraction de la dimension d'interface Δ_𝒞 du terme de jonction, depuis le couple Freelance Holography II (2503.09372, moving boundary) ⊕ Skenderis (2312.17316, renormalisation holographique en dS). Sous-cadrage du fork S-O2C-2 de LC-WORK-CADRAGE-O2-CONSTRUCTION v0.1 (sha 36fc7148aac5). Acquis amont de S-O2C-1 (LC-D-O2-JONCTION v0.4) : C1 (existence et finitude du terme de bord de jonction) bien posé, divergence localisée en terme de contact d'interface sur 𝒞, trichotomie C1-a/b/c ⟺ signe(Δ_𝒞 − d) avec d=3, Δ_𝒞 NON fixée par aucun scellé KB. Ce fichier FIGE, AVANT lecture des corps des deux PDF désormais en KB (NON consommés) : la cible ponctuelle (Δ_𝒞), les deux intrants nommés et ce qu'on en attend, les trois cibles d'extraction T1/T2/T3 et leurs issues pré-déclarées, le critère de verdict TRIPARTITE anticipé basse-yield, le critère anti-surclassement, les forks d'exécution. SANS SURCLASSEMENT (§6.4) : un cadrage ne construit rien et ne tranche rien ; extraire Δ_𝒞 délimite/instruit C1, ne tranche pas C1 sans la transposition dS, ne construit pas O₂ (C2/C3 + transport dS restent), et NE réduit PAS {A4 ; A2★ ; N}. {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; A4 non réduit ; A2★ non tranché ; CCC non démontrée."
codename: LC-RACCORD
tags: [cadrage, gele, paper-first, anti-fit, O2, construction, S-O2C-2, Delta-C, dimension-interface, terme-de-contact, deux-bords, moving-boundary, freelance-holography, renorm-holo-dS, skenderis, transposition-dS, lien-G3, C1, gate-construction, intrant-en-kb-non-consomme, §6.4, A4, A2star, N]
type: "cadrage de fork GELÉ (sous-cadrage de S-O2C-2). Pose la cible d'extraction et la fige AVANT lecture des corps. NE construit pas O₂, NE tranche pas C1, NE ferme pas D1, NE fixe pas N, NE réduit pas A4. Subordonné à LC-WORK-CADRAGE-O2-CONSTRUCTION v0.1 et à LC-AUDIT-VERDICT §6.4. Exécution (lecture des corps + extraction) sur GO séparé."
statut: "cadrage gelé — forme figée le 2026-06-16 (sha256 reporté hors-fichier au dépôt, marqueur de gel anti-fit). Les deux intrants PDF sont EN KB mais NON consommés ; leur lecture ne se déclenche qu'au GO postérieur à la validation de CE fichier. Forks tranchés : S-O2C-2a=lecture Freelance II / extraction candidat Δ_𝒞 ; S-O2C-2b=lecture Skenderis / transport dS ; S-O2C-2c=confrontation à la trichotomie C1 ; S-O2C-2d=sceau conditionnel+firewall SSI une construction concrète émerge, sinon sans-sceau. NE tranche rien ici ; A4 non réduit ; D1 non clos ; N non fixé ; CCC non démontrée ; {A4 ; A2★ ; N} INCHANGÉ."
statut_id: provisoire — à enregistrer si validé
version: 0.1
langue: fr
date: 2026-06-16
maj: "2026-06-16 — v0.1 : création du sous-cadrage du fork S-O2C-2. Fige AVANT lecture des corps : la cible ponctuelle Δ_𝒞 (héritée de S-O2C-1, LC-D-O2-JONCTION v0.4), les deux intrants en KB non consommés (Freelance Holography II 2503.09372 = moving boundary ; Skenderis 2312.17316 = renorm holographique dS), les cibles d'extraction T1 (objet d'interface et sa dimension) / T2 (transport AdS→dS du contre-terme et de la dimension, lien G3) / T3 (confrontation à la trichotomie C1 + anti-surclassement), leurs issues pré-déclarées α/β/γ, le critère TRIPARTITE anticipé basse-yield (délimitation la plus probable), les forks S-O2C-2a..d. Anticipation honnête : la lecture extrait Δ_𝒞 en AdS OU confirme le fossé AdS→dS (≡ G3) ; elle ne construit pas O₂ à elle seule. SANS SURCLASSEMENT (§6.4) : Δ_𝒞 extrait ≠ C1 tranché ≠ O₂ construit ≠ réduction de {A4 ; A2★ ; N} ; A4 clos par le pivot ; N≡Λ hors de portée ; D1 non clos ; CCC non démontrée."
prerequis_kb: [LC-WORK-CADRAGE-O2-CONSTRUCTION, LC-D-O2-JONCTION, LC-WORK-BIBLIO-O2-DEUX-BORDS, LC-D-O2-P1, LC-D-O2-HODGE, LC-D-O2-P2, LC-D-CT-DUAL, LC-D-CT-DUAL-DS, LC-D-CT-GAMMA, LC-D3-SPECTRE-K3, LC-D-F6-G3-LAMBDA-BMS, LC-D-F5-ETAT-RACCORD, LC-WORK-BRANCHE-FALSIFIABILITE, LC-AUDIT-VERDICT]
renvois: [LC-WORK-CADRAGE-O2-CONSTRUCTION, LC-D-O2-JONCTION, LC-WORK-BIBLIO-O2-DEUX-BORDS, LC-D-F6-G3-LAMBDA-BMS, 02_programme, 03_glossaire, 04_references]
tags_epistemiques: [cadrage, à inventer, intrant-en-kb-non-consommé, décision ouverte, piste / à étayer]
---

# LC-WORK · Cadrage du fork S-O2C-2 — extraire Δ_𝒞, la dimension de l'opérateur d'interface

> **Statut.** Cadrage **gelé** (paper-first / anti-fit). Il **fige la cible
> d'extraction avant** toute lecture des corps des deux PDF (désormais en KB,
> **NON consommés**). Il **ne construit pas** O₂, **ne tranche pas** C1,
> **ne ferme pas** D1, **ne fixe pas** N, **ne réduit pas** A4. Le sha256 de la
> forme figée est reporté **hors-fichier** au dépôt (marqueur de gel anti-fit).
> Exécution (lecture + extraction) sur **GO séparé**.

---

## 0. Rôle, garde-fous `[§6.4 + anti-fit + R-7]`

- **Étage.** Sous-cadrage du fork **S-O2C-2** de `LC-WORK-CADRAGE-O2-CONSTRUCTION`
  v0.1 (sha `36fc7148aac5`). « Mieux poser la lecture », pas une construction.
- **Anti-fit — point dur.** Les deux intrants sont **en KB mais NON consommés**.
  Les cibles d'extraction (§3), leurs issues pré-déclarées et le critère de verdict
  (§4) sont figés **ici, avant** d'ouvrir un seul corps. Tout écart à une cible gelée
  lors de la lecture = **R-7 daté**. L'ordre cadrage-figé → lecture est non négociable.
- **Non-surclassement (§6.4).** Même une extraction **propre** de Δ_𝒞 :
  - **ne tranche C1** que si le transport dS (T2) tient **aussi** et que la
    trichotomie `signe(Δ_𝒞 − d)` se lit sans ambiguïté ;
  - **ne construit pas** O₂ — **C2** (coefficient O(1) de `A_T`) et **C3** (`W³` via
    `⟨TTT⟩`) restent **non posées en interne** (option S-O2C-1 bis) et exigent l'objet
    de jonction complet, pas seulement la dimension de son opérateur ;
  - **ne réduit pas** `{A4 ; A2★ ; N}` — A4 clos par le pivot, `N ≡ Λ` hors de portée,
    A2★ séparé.
- **R-7 / additivité.** Aucun déplacement de fichier ; aucune touche aux chaînons amont
  ni aux sceaux. Patchs ultérieurs strictement additifs (suppr. ⊆ {version, maj, statut}).

---

## 1. La cible héritée de S-O2C-1 `[ponctuelle, figée]`

S-O2C-1 (`LC-D-O2-JONCTION` v0.4) a **posé** C1 sans intrant et **resserré** le manque :

- **C1 bien posé.** Extrémités scellées — Dirichlet (`g₀` fixé, `g₃`=VEV) côté éon n ;
  Neumann (`g₃`=0 par WCH, `g₀` libre) côté éon n+1 ; dualité `S²=−1` vp `±i`
  (`CT-DUAL`) ; sens D→N fixé par WCH.
- **Divergence localisée.** Chaque bord seul a une renorm de de Haro **finie**
  (`CT-GAMMA`) ⟹ toute divergence du terme de jonction est un **terme de contact
  d'interface** sur `𝒞`.
- **Trichotomie ⟹ un seul nombre.** `C1-a/b/c ⟺ signe(Δ_𝒞 − d)`, `d=3` :
  `Δ_𝒞 > d` → fini sans contre-terme (**C1-a**) ; `Δ_𝒞 = d` → fini après 1 contre-terme
  (**C1-b**) ; `Δ_𝒞 < d` → divergence (**C1-c**). **Aucun scellé KB ne fixe `Δ_𝒞`**
  (le secteur scellé fixe `Δ_T = d` via `SPECTRE-K3`, **pas** `Δ_𝒞`, qui naît du couplage
  des deux quantifications duales à travers `𝒞`).

**Cible de S-O2C-2 = extraire `Δ_𝒞`** (dimension de l'opérateur d'interface le plus
relevant porté par le terme de jonction) **et** statuer sur sa **transposabilité en dS**.

---

## 2. Les deux intrants `[EN KB, NON consommés — nommés avant lecture]`

> **I-O2 (volet « objet d'interface »)** — **Freelance Holography II**,
> `2503_09372v2.pdf` `[EN KB, NON consommé]`. Lead identifié à la passe S-O2C-2
> (`LC-WORK-BIBLIO-O2-DEUX-BORDS` v1.1 §G) : descendant direct de Compère-Marolf, le
> mécanisme **« moving boundary »** = transport d'une condition aux limites d'un bord
> vers un autre — l'analogue formel le plus proche du recollement D→N à travers `𝒞`.
> **Plus proche que** Barvinsky-Nesterov. Cadre attendu : **AdS (Λ<0)**.

> **I-O2 (volet « transport dS »)** — **Skenderis**, `2312_17316v2.pdf`
> `[EN KB, NON consommé]`. Lead identifié à la passe S-O2C-2 : **renormalisation
> holographique en dS** = pont candidat AdS→dS pour le contre-terme et l'assignation
> de dimension. C'est le maillon du **double-blocage (2)** de S-O2C-1 (technos
> candidates toutes AdS ; raccord en dS ⟹ transport non acquis ≡ obstruction **G3**,
> `LC-D-F6-G3-LAMBDA-BMS`).

Les deux PDF sont en **PDF natif** (lecture locale directe ; pas de fetch réseau).
Leur statut `[NON consommé]` ne se lève qu'au **GO postérieur** à la validation de CE fichier.

---

## 3. Cibles d'extraction `[figées AVANT lecture — issues pré-déclarées]`

### T1 — l'objet d'interface et sa dimension `[depuis Freelance II 2503.09372]`
Extraire, dans le formalisme **moving boundary** : (a) **l'opérateur localisé sur le
bord mobile / l'interface** qui implémente le transport d'une CL d'un bord vers l'autre
(candidat à l'opérateur d'interface du terme de jonction) ; (b) **si le formalisme lui
assigne une dimension d'échelle** ; (c) **est-ce le plus relevant** porté par le terme de
contact. **Cible numérique** : `Δ_𝒞` et son rapport à `d=3`.
- **T1-α** : l'opérateur d'interface est exhibé **avec** une dimension ⟹ `Δ_𝒞`
  extractible ⟹ confrontable à la trichotomie (→ T3).
- **T1-β** : opérateur exhibé mais dimension **non fixée / dépendante du contexte**
  ⟹ `Δ_𝒞` **borné**, pas pinçable ⟹ **délimitation**.
- **T1-γ** : construction **AdS-only sans opérateur d'interface dimensionné**
  transposable ⟹ extraction **bloquée** sur ce lead ⟹ bascule sur T2/G3.

### T2 — transport AdS→dS `[depuis Skenderis 2312.17316 ; ≡ obstruction G3]`
Statuer sur ce que la renorm holographique dS **fournit / ne fournit pas** : (a) une
**carte AdS→dS** du contre-terme et de l'**assignation de dimension** survit-elle au
changement de signe `Λ>0` ; (b) s'étend-elle à un **terme de contact à deux bords**
(jonction), ou seulement à **un** bord dS.
- **T2-α** : carte AdS→dS **propre** du contre-terme/dimension ⟹ obstruction G3
  **levée pour ce terme de contact** ⟹ `Δ_𝒞` transportable en dS.
- **T2-β** : renorm dS **mono-bord** fournie, mais **pas** le contact à deux bords /
  pas la jonction ⟹ transport de `Δ_𝒞` en dS **reste ouvert** ≡ **G3 persiste**.
- **T2-γ** : **aucune** structure transposable ⟹ transport dS **bloqué**, G3 tient.

### T3 — confrontation à la trichotomie C1 + anti-surclassement `[figé]`
Confronter le `Δ_𝒞` extrait (ou borné, ou bloqué) à `signe(Δ_𝒞 − d)`, `d=3`, et **pré-déclarer**
ce qui ne constitue PAS un surclassement :
- `Δ_𝒞` extrait en AdS **seul** (T1-α ∧ T2-β/γ) ⟹ **délimitation** : C1 instruit en AdS,
  **non tranché en dS** (le régime physique du raccord) ; gap relocalisé sur G3.
- `Δ_𝒞` extrait **et** transporté (T1-α ∧ T2-α) ⟹ **C1 tranché** (a/b/c selon le signe) —
  **et rien de plus** : C2/C3 restent, O₂ **non construit**, compte **inchangé**.
- échec d'extraction (T1-β/γ) ⟹ délimitation faible ou **reste HOLD** sur ce lead.

---

## 4. Critère de verdict `[TRIPARTITE — figé, anticipé basse-yield]`

- **CONSTRUCTION** : exclue à ce fork — S-O2C-2 vise `Δ_𝒞`, pas l'objet de jonction
  complet (C2/C3 non posées). Le mieux atteignable = **C1 tranché**, qui reste un
  **sous-résultat**, jamais « O₂ construit ».
- **DÉLIMITATION (issue la plus probable)** : `Δ_𝒞` extrait en AdS, transport dS partiel
  ou bloqué (T2-β/γ) ⟹ C1 instruit, gap resserré sur G3 ; compte **inchangé**. Cohérent
  avec le double-blocage de S-O2C-1.
- **INTRANT-HOLD résiduel** : si les corps ne fournissent ni l'opérateur d'interface
  dimensionné (T1-γ) ni le transport (T2-γ) ⟹ le lead se referme, le manque reste nommé.

**Anti-surclassement (figé).** `Δ_𝒞 extrait` ≠ `C1 tranché` (exige T2-α) ≠ `O₂ construit`
(exige C2 ∧ C3) ≠ `réduction de {A4 ; A2★ ; N}` (A4 clos par le pivot ; N≡Λ hors de
portée ; A2★ séparé). Tout passage à `établi` exige **algèbre réelle + firewall mordant
+ audit froid** AVANT enregistrement.

---

## 5. Forks d'exécution `[figés]`

- **S-O2C-2a** — lecture du corps de **Freelance II** `2503.09372` ; extraction du
  candidat opérateur d'interface + dimension (T1) ; cibles gelées, tout écart = R-7 daté.
- **S-O2C-2b** — lecture du corps de **Skenderis** `2312.17316` ; évaluation du transport
  AdS→dS du contre-terme/dimension (T2).
- **S-O2C-2c** — confrontation du `Δ_𝒞` (extrait/borné/bloqué) à la trichotomie C1 (T3) ;
  verdict (le plus probablement **délimitation**).
- **S-O2C-2d** `[conditionnel]` — **SSI** un terme de bord de jonction concret, fini, à
  `Δ_𝒞` fixé **et** transporté en dS émerge : armer un **sceau réversible + firewall**
  (mutations cassantes réelles candidates : signe de `Δ_𝒞 − d` inversé ; contre-terme dS
  omis ; terme de contact à deux bords réduit à un seul bord). **Sinon : sans-sceau**
  (délimitation), comme F2/F3/F4.

---

## 6. Non-surclassement (§6.4) `[rappel terminal]`

Cadrer ne consomme aucune source et ne tranche rien. Extraire `Δ_𝒞` **instruit** C1 ;
ne le **tranche** qu'avec le transport dS (T2-α) ; ne **construit** pas O₂ (C2/C3 + objet
complet) ; et NE **réduit** PAS `{A4 ; A2★ ; N}`. Le pivot a clos la route A4 ; ce fork ne
la ré-ouvre pas. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; N non fixé (≡ Λ) ;
A4 non réduit ; A2★ non tranché ; CCC non démontrée.
