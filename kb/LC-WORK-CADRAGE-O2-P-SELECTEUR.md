---
id: LC-WORK-CADRAGE-O2-P-SELECTEUR
titre: "Cadrage GELÉ (anti-fit R-7) du fork KB-only sur le facteur α d O₂ — LA SÉLECTION DE p★ EST-ELLE DANS LE PÉRIMÈTRE DE β ? Question posée APRÈS la classification FINALE de α en C1-b POSITIF avec p ≡ b LIBRE (LC-D-O2-COIN-TRANSMISSION v0.3, fetch A_c consommé) et le routage C1^dS = C1^AdS(α) ∘ transport(β) (LC-D-O2-FACTORISATION §3). ENJEU EXACT : l amendement v0.2 (R-53) de FACTORISATION affirme « résidu d O₂ = β ≡ G3 SEUL ». Cette affirmation présuppose que le transport AdS→dS FIXERAIT p. Ce cadrage GÈLE l espace-verdict de cette présupposition — il ne la tranche pas. Espace-verdict {P-1 ABSORBÉ ; P-2 SÉPARÉ ; P-3 INDÉTERMINÉ} + discriminants D1-D3 + mapping EXCLUSIF + firewalls F#1-F#5 + bornes b1-b6, figés AVANT toute algèbre et AVANT toute lecture de corps. RÉGIME STRICTEMENT KB-ONLY, ZÉRO DROIT DE FETCH. CONJECTURE DU PILOTE DÉCLARÉE en §0bis (doctrine de non-blinding assumé) et EXPLICITEMENT SOUMISE au mandat d auditeur. Adjudication RÉSERVÉE au CSE souverain incognito — PILOTE DISQUALIFIÉ. Défauts Δ1 relevés sur le cadrage 32b76fd5 traités ici en PROSPECTIF : espace-verdict SYMÉTRIQUE (toutes les issues au conditionnel), mapping EXCLUSIF (partition), AUCUNE conjonction auto-satisfaite, §2 factuellement vérifié sur le mount. SANS SURCLASSEMENT (§6.4) : geler un espace-verdict ne scelle/réduit/compte/démontre RIEN. {A4 ; A2★ ; N} INCHANGÉ ; O₂ non construit ; D1 non clos ; N non fixé ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "cadrage de front GELÉ (R-7). Pose la question et fige l espace-verdict AVANT toute algèbre. NE tranche RIEN, NE construit PAS O₂, NE rouvre PAS le pivot O₂ (clos négatif), NE re-gèle NI ne rectifie l amendement v0.2 de FACTORISATION. Subordonné à LC-AUDIT-VERDICT §6.4, au cadrage gelé LC-WORK-CADRAGE-O2-CONSTRUCTION (36fc7148) dont les gates C1/C2/C3 sont HÉRITÉES et NON re-gelées, et à la règle R-53. Exécution sur GO séparé, APRÈS gate CSE-1 en aveugle."
statut: "cadrage GELÉ — forme figée AVANT toute algèbre et AVANT toute lecture de corps. Algèbre NON exécutée. Espace-verdict NON tranché. Pivot O₂ NON rouvert. {A4 ; A2★ ; N} INCHANGÉ."
version: "0.1"
langue: fr
date: "2026-07-15"
gel_R36: "consigné HORS-FICHIER, horodaté 2026-07-15 (R-36 : ce fichier n embarque PAS son propre sha)"
prerequis_kb: [LC-WORK-CADRAGE-O2-CONSTRUCTION, LC-D-O2-FACTORISATION, LC-D-O2-COIN-TRANSMISSION, LC-D-O2-COIN, LC-D-O2-C1-ADS, LC-D-O2-DELTA-C, LC-D-F5-ETAT-RACCORD, LC-D-F6-G3-LAMBDA-BMS, LC-D-G3-TRANSPORT, LC-D-IRREDUCTIBILITE-MOYENS]
tags: [cadrage, gel-R7, O2-construction, facteur-alpha, selecteur-p, p-libre, C1-b, routage, espace-verdict-symetrique, mapping-exclusif, KB-only, zero-fetch, CSE-1-aveugle, pilote-disqualifie, R-53, §6.4, non-surclassement]
---

# Cadrage GELÉ — la sélection de `p★` est-elle DANS le périmètre de `β` ?

## 0. Rôle et garde-fous `[§6.4 + anti-fit R-7 + R-53]`

Ce fichier **pose une question et fige l espace de ses réponses**. Il ne l instruit pas. Aucune
algèbre n a été faite ; aucune source hors KB n a été lue. **Le gel précède le calcul** : c est la
seule raison d être de ce document.

**Ce qui est HÉRITÉ et NON re-gelé** : les gates `C1 / C2 / C3` et le critère tripartite du cadrage
`36fc7148` (§4, §5) ; le contrôle anti-circularité `K` (§4). Ils sont **cités**, jamais reformulés.

**Ce qui est NEUF** : une question de **structure du routage**, distincte des gates elles-mêmes.

---

## 0bis. DÉCLARATION DE CONJECTURE DU PILOTE `[transparence d exposition — À VÉRIFIER, PAS À CROIRE]`

> **Le pilote a formé une conjecture AVANT ce gel, et elle est écrite dans la conversation de
> session.** Elle est donc **irrécupérablement antérieure** au cadrage. La cacher serait pire que la
> déclarer : elle ressortirait à la lecture du fil.
>
> **Conjecture du pilote : P-2.** Le pilote croit que `p` resterait libre après transport, et donc que
> la branche `CONSTRUCTION` du critère gelé `36fc7148` §5 serait **inatteignable par cette voie**.
>
> **CE QUE L AUDITEUR DOIT EN FAIRE.** Ceci est une **DÉCLARATION, pas un fait** — **vérifie-la**.
> Trois obligations explicites :
> **(1)** Si l espace-verdict, les discriminants, le mapping ou les firewalls ci-dessous **favorisent**
> P-2 par leur **rédaction** plutôt que par leur **contenu**, c est un **DÉFAUT À CONSIGNER**, et
> l auditeur le consigne — même si l issue reste P-2.
> **(2)** Le pilote **note en propre** un risque de fit spécifique : la conjecture P-2 **réinstaurerait**,
> sur un axe différent, un corollaire que l amendement v0.2 de `LC-D-O2-FACTORISATION` avait
> **RETIRÉ**. Vouloir avoir eu raison contre un amendement qui vous a corrigé est un **motif connu**.
> **La charge est donc LOURDE sur P-2**, et **légère sur P-1**.
> **(3)** Le pilote est **DISQUALIFIÉ** pour l adjudication. **En cas de discordance, l incognito
> prévaut.**

---

## 1. La cible figée `[question — NE PAS reformuler]`

> **Q.** La **sélection d une valeur `p★`** du paramètre libre du facteur de coin est-elle **contenue
> dans le périmètre de `β`** (le transport `AdS → dS`), **ou** constitue-t-elle un **intrant distinct
> de `β`** ?

**Pourquoi la question existe.** L amendement v0.2 (R-53) de `LC-D-O2-FACTORISATION` conclut :
« résidu d O₂ = `β` ≡ G3 **SEUL** ». Cette conclusion est **valide si et seulement si** la liberté de
`p` est **absorbée** par `β`. Ce cadrage **ne conteste pas** l amendement : il **isole sa
présupposition** et gèle l espace de son verdict.

**Ce que la question N EST PAS.** Elle ne demande **pas** si `β` est résoluble (c est G3, hors
périmètre ici). Elle ne demande **pas** de **valeur** de `p★`. Elle ne demande **pas** de trancher
`C2` ni `C3`.

---

## 2. Socle hérité `[factuel — RELU SUR LE MOUNT, non re-dérivé]`

Énoncés **vérifiés par lecture directe des têtes** (R-54), à la date de ce gel :

- **(s1)** `LC-WORK-CADRAGE-O2-CONSTRUCTION` (gel `36fc7148`) §4 définit `C1-a` = *terme fini sans
  contre-terme neuf ⟹ objet **bien défini*** ; `C1-b` = *fini seulement après contre-terme neuf ⟹
  objet **conditionnel (paramètre)*** ; `C1-c` = *divergence irréductible ⟹ obstruction*.
- **(s2)** Le même §5 définit `CONSTRUCTION (au mieux)` = `C1-a ∧ C2-a ∧ C3-a`.
- **(s3)** `LC-D-O2-FACTORISATION` §3 pose le routage `C1^dS = C1^AdS(α) ∘ transport(β)`, et
  `C2, C3` **en aval de `C1`** ⟹ héritent de `(α ∧ β)`.
- **(s4)** `LC-D-O2-COIN-TRANSMISSION` v0.3 classe `α` : **`C1-b` POSITIF**, `p ≡ b` **LIBRE**,
  **classification FINALE** du facteur de coin sur l axe α — *famille à un paramètre, PAS une
  construction unique* ; bonne-position **et** finitude tiennent **∀p** ⟹ **aucun `p★` isolé**.
  `Φ` identifié = moment ADM sans-trace `Π̄_⟨μν⟩` (charge de York). **AUCUN sceau** (S-O2C-4-3 non armé).
- **(s5)** Le sélecteur candidat **`A_c(p)·log z`** (anomalie conforme p-dépendante, hypothèse v0.2
  R-48) est **RÉFUTÉ** : Gustavsson `1911.04178` donne une anomalie conforme **indépendante de k**.
- **(s6)** `LC-D-O2-COIN` v0.2 note que `p` reste libre et que **`η` est géométrique**.
- **(s7)** `LC-D-O2-DELTA-C` : `Δ_𝒞 = d` (marginal) en AdS ; **transport dS BLOQUÉ** (Skenderis
  `2312.17316`) — contre-termes AdS projetés hors ; **pas de version renormalisée de la carte
  D↔N / shadow au pas marginal**.
- **(s8)** `LC-D-O2-FACTORISATION` porte, dans son **corps imprimé**, un §4 (« α FETCH-GATED ») et un
  §5 (« α resterait / même G3 résolu ne suffirait pas ») que sa **propre bannière v0.2 déclare
  PÉRIMÉS**. **Fait consigné, non exploité** : ce cadrage ne s appuie sur **aucune** de ces deux
  clauses, ni dans un sens ni dans l autre.

**Contrôle de véracité du §2** (défaut Δ1-(i) de `32b76fd5`, traité en prospectif) : chacun des
énoncés (s1)–(s8) est **relu sur le mount**, non repris d un index. Aucun énoncé de ce §2 n affirme
qu une pièce n a pas été consommée.

---

## 3. Espace-verdict `[FIGÉ — SYMÉTRIQUE, toutes les issues au CONDITIONNEL]`

> **Contrainte de rédaction, appliquée** (défaut Δ1-(ii) de `32b76fd5`) : **aucune issue n est
> libellée à l indicatif quand une autre est au conditionnel.** Les trois sont au **même mode**.

- **P-1 — ABSORBÉ.** La sélection de `p★` **serait** entièrement contenue dans `β` : le transport
  `AdS → dS`, correctement construit, **fixerait** `p`. ⟹ le résidu d O₂ **resterait** `β` SEUL ;
  l amendement v0.2 **tiendrait tel qu écrit**.
- **P-2 — SÉPARÉ.** La sélection de `p★` **serait** un intrant **distinct** de `β`, non couvert par le
  transport. ⟹ le résidu d O₂ **serait** `β ∧ σ` (σ = sélecteur de `p`) ; l amendement v0.2 **serait
  trop fort** et **exigerait** un amendement daté **postérieur** ; la branche `CONSTRUCTION` de (s2)
  **deviendrait inatteignable par cette voie**.
- **P-3 — INDÉTERMINÉ.** Les définitions gelées et les acquis KB **ne suffiraient pas** à décider si
  `p★` est dans le périmètre de `β`. ⟹ **HOLD**, intrant **nommé**, aucune algèbre poussée au-delà.

**Exhaustivité déclarée** : `{P-1 ; P-2 ; P-3}` couvre l espace. Toute issue hors de ces trois exige
un **amendement R-7 daté**.

---

## 4. Discriminants et mapping `[FIGÉS — mapping EXCLUSIF, partition]`

**D1 — NATURE de `p`** *(indice, NON décisif — déclaré tel)* :
`(i)` géométrique / cinématique · `(ii)` d état / dynamique · `(iii)` indéterminée.

**D2 — LOCUS du sélecteur** *(décisif)* :
`(i)` **intérieur** à `β` — la sélection de `p★` serait une conséquence de la **seule** continuation
`Λ<0 → Λ>0` et de la structure du raccord à `𝓘⁺` spacelike ;
`(ii)` **extérieur** à `β` — la sélection exigerait une **donnée neuve** (état, prescription,
condition de bord supplémentaire) qui **n est pas** le transport ;
`(iii)` **indéterminé**.

**D3 — TESTABILITÉ KB** *(décisif)* :
`(i)` les définitions gelées + acquis KB **suffisent** à trancher D2 ;
`(ii)` elles **ne suffisent pas**.

**Mapping figé, EXCLUSIF et EXHAUSTIF** (défaut Δ1-(iv) de `32b76fd5`, traité en prospectif — la
partition est faite **sur D2 × D3**, chaque branche portant la négation des autres) :

| condition | issue |
|---|---|
| `D3=(ii)` **∨** `D2=(iii)` | **P-3** |
| `¬[D3=(ii) ∨ D2=(iii)]` **∧** `D2=(i)` | **P-1** |
| `¬[D3=(ii) ∨ D2=(iii)]` **∧** `D2=(ii)` | **P-2** |

**Contrôle d auto-satisfaction** (défaut Δ1-(iii) de `32b76fd5`, traité en prospectif) : **aucune
branche n a d antécédent vrai par construction.** `D2=(i)` et `D2=(ii)` sont **mutuellement
exclusifs et non vides a priori** ; `D1` **n entre dans aucune condition** — il est **explicitement
retiré du mapping** pour qu il ne puisse pas forcer une issue par transitivité.

---

## 5. Firewalls `[FIGÉS]`

- **F#1 — anti-circularité `K`** (héritée de `36fc7148` §4, **non reformulée**) : aucun sélecteur ne
  peut présupposer **A4 / WCH** ni l état `+i` comme **résultat**. Ils entrent comme **données
  posées**. Un sélecteur qui « dérive » A4 ou `+i` est **circulaire ⟹ rejeté**.
- **F#2 — le pivot O₂ est CLOS NÉGATIF** (P1/Hodge discordance ; P2 discordance). Ce cadrage **ne le
  rouvre pas** et **ne peut s appuyer sur (C-O2) forte**.
- **F#3 — `(b′)` est RÉFUTÉ** (`s = (−1)^d` = artefact d épissure ; le `−1` vient du **carré de
  Hodge**, source unique du signe). **Aucune reprise** de la parité de `w`.
- **F#4 — le sélecteur `A_c(p)·log z` est RÉFUTÉ** (s5). **Ne pas le ré-armer** sans amendement daté.
- **F#5 — ZÉRO FETCH.** Régime **strictement KB-only**. Toute lecture de corps hors KB exige un
  **amendement R-7 daté et prospectif**. `arxiv.org` hors allowlist ⟹ contrainte **matérielle**, pas
  seulement réglementaire.

---

## 6. Bornes de portée `[FIGÉES — b1..b6]`

- **b1** — **Aucune issue ne réduit** `{A4 ; A2★ ; N}`. Aucune issue ne fixe `N`, ne clôt `D1`, ne
  construit `O₂`, ne résout `G3`.
- **b2** — Les **têtes scellées restent l AUTORITÉ, INTACTES**. **Aucune issue ne déclenche de
  re-audit** d un sceau existant.
- **b3** — **P-2 n est PAS « O₂ impossible ».** C est : *la branche `CONSTRUCTION` du critère gelé
  serait inatteignable **par CETTE voie***. Une **délimitation**, pas une obstruction. Une autre voie
  d assemblage resterait concevable.
- **b4** — **P-1 n est PAS « O₂ construit » ni « β résolu ».** C est : *le routage de l amendement
  v0.2 tiendrait*. `β` resterait **entier**, et `β ≡ G3` **reste fetch-gated**.
- **b5** — L amendement v0.2 de `FACTORISATION` est **INTACT, NON re-gelé, NON rectifié** par ce
  cadrage. **Seule** une issue **P-2** ouvrirait la voie à un amendement **daté et POSTÉRIEUR** — qui
  serait alors écrit **après** l issue, **jamais avant**, et **jamais rétroactivement**.
- **b6** — **Le pilote est DISQUALIFIÉ pour l adjudication.** Elle est **RÉSERVÉE au CSE souverain
  incognito**. En cas de **discordance pilote / incognito**, **l INCOGNITO PRÉVAUT**.

---

## 7. Régime d exécution `[figé — ordre CONTRAINT]`

1. **Dépôt de ce cadrage** sur le mount + **gel R-36 hors-fichier**. *(Rien ne commence avant.)*
2. **Gate CSE-1 EN AVEUGLE** sur ce cadrage : paquet autoportant zéro-fuite, **pilote disqualifié**,
   **doctrine v0.3 applicable — régime A OBLIGATOIRE** (livraison **par fichiers**, table des sha
   **DANS le prompt**, Phase 0 = **gate d ARRÊT**). Objet de la gate : *la question est-elle
   non-tautologique, et l espace-verdict est-il honnête ?* **Aucune substance transmise.**
3. **Algèbre KB-only**, contre le mapping du §4 **TEL QU ÉCRIT** — **zéro amendement des cibles**.
4. **Chaînon-verdict**, puis **CSE souverain incognito**.

**Prérequis bloquant, rappelé** : le **§0-full est PÉRIMÉ** (celui de V80 a été consommé par le CSE
qu il gatait). **Tout verdict majeur exige un §0-full FRAIS** — canaris lourds `verif_nonlin_parity`
et `verif_D3_P6_specB_oracle` en `setsid` détaché **dès l ouverture** (≥600s, 1 CPU). **Le cadrage
n en exige pas ; le verdict, si.**

**Issue attendue, PRÉ-DÉCLARÉE** (précédent : cadrage F6 §2 ; réserve opérateur de #2) : *l issue
honnête attendue est une **DÉLIMITATION**.* Ce fork s engage pour **savoir si le routage de
l amendement v0.2 tient**, **PAS** pour espérer une réduction. **Aucune issue ne réduit le compte.**

---

**§6.4 (sentinelle terminale)** — geler un espace-verdict / isoler une présupposition / déclarer une
conjecture / router un facteur **ne scelle / ne réduit / ne compte / ne démontre RIEN**. `α = C1-b`
**n est pas** « O₂ construit ». « Le routage tient » **n est pas** « β est résolu ». Une délimitation
atteste une **structure**, jamais une conclusion physique. Les têtes scellées restent l **AUTORITÉ,
INTACTES**. Le pivot O₂ reste **CLOS NÉGATIF**. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; `N` non
fixé (`≡ Λ`, terminus ouvert — clôture **R-53 conditionnelle 0/4 INCHANGÉE**) ; O₂ **non construit** ;
`β` **non résolu** ; A4 **non réduit** ; A2★ **non tranché** ; **CCC non démontrée NI réfutée**.
