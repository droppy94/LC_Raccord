---
id: LC-BETA-02-ETAT-BETA
codename: LC-RACCORD-BETA
titre: "État du front β au gel du dossier (2026-07-18, depuis V94 / manifeste v2.121). INDEX : dit où regarder, pas ce qui est vrai. Chaque ligne porte sa provenance. Toute valeur est une DÉCLARATION À VÉRIFIER contre BETA-COPIE-LC-D-G3-TRANSPORT.md, jamais une source."
version: 0.1
langue: fr
date: 2026-07-18
grade: "INDEX. Ne scelle rien, ne fait foi de rien. La tête copiée arbitre ; le mount principal arbitre la tête (R-54). Court PAR CONSTRUCTION."
---

# β — état gelé au 2026-07-18

> **Lire d'abord.** Ce fichier est un **index**. Il a été rédigé par **le pilote**, dont V94
> établit qu'il est **le témoin le plus faible**. Chaque affirmation ci-dessous renvoie à une
> copie byte-exacte. **En cas de désaccord, la copie gagne. En cas de doute sur la copie, le
> mount principal gagne.**

## §1 — Ce que β est, exactement

**β = le transport `AdS→dS` de l'objet de jonction (Robin mixte `D↔N`, graviton, **deux
bords**, contact fini `Δ_𝒞`) depuis Λ<0 vers le raccord à `𝓘⁺` **spacelike** (Λ>0).**

- `I-O2 = α ∧ β` — factorisation du résidu de construction d'O₂.
  `C1^dS = C1^AdS(α) ∘ transport(β)` ; `C2`/`C3` en aval héritent des deux facteurs.
  *[`BETA-COPIE-LC-D-O2-FACTORISATION.md` §3]*
- **`α` est SOLDÉ** : `α = C1-b` **POSITIF**, `p` **LIBRE** — le facteur de coin est une
  **famille à un paramètre**, pas une construction unique.
  *[`BETA-COPIE-LC-D-O2-COIN-TRANSMISSION.md` v0.3, R-50/51/52]*
- ⟹ **le résidu d'O₂ se réduit EXACTEMENT et uniquement à `β ≡ G3`.**
  *[`FACTORISATION` bannière v0.2 — le corollaire v0.1 « α resterait » est PÉRIMÉ]*
- **`β ≡ G3-a`** (tranche unique η→0⁻, pas de feuilletage retardé, Λ-BMS non standard) ; et
  **`G3-b`** pointe **en retour** vers O₂ ⟹ **O₂-construction n'est PAS indépendante de G3.**
  *[`FACTORISATION` §5 ; `BETA-COPIE-LC-D-F6-G3-LAMBDA-BMS.md`]*

## §2 — Verdict courant : `T-b`. Quatre assauts, zéro réduction.

| étape | ce qui a été consommé | ce qui en est sorti |
|---|---|---|
| `S-G3T-1` | KB-only, aucun fetch | **`T-b`** — mur en **`TG-3`** (carte shadow **renormalisée**, graviton deux-bords, **non exhibée**) |
| `S-G3T-2` | wedge `2007.06800` | **`T-b`**, mur **re-situé** — deux-bords existe, mais **AdS/BCFT N-N codim-2**, pas dS-marginale |
| `S-G3T-3b` | `2606.09170`, `2412.00183` | **`T-b`** — **`R4′ ✓✓`** : le dictionnaire dS genuine au `𝓘⁺` **n'est PAS perdu** ⟹ **réfute** la jambe pessimiste du wedge ; mais `R3′ ✗` (graviton propageant absent), `R2′ ✗` |
| `S-G3T-4b` | `2409.08709` (ST) **+** `0808.2054` (de Haro) | **`T-b`** — **`R3″ ✓ ACQUIS`** (graviton propageant **livré** en dS₄) ; `R1″ ✗`, `R2″ ✗`, `R4″ ✗` |
| `§7quinquies` | levier admissibilité (gel `b3a7e84a`) | **`PRESCRIPTION-DÉPENDANT`** (`K-B`, cold-confirmé) — **ne décide dans AUCUN sens** ; import irréductible **MAINTENU** |

*[tout : `BETA-COPIE-LC-D-G3-TRANSPORT.md`, `statut` + `maj` + §7bis/§7ter/§7quater/§7quinquies]*

## §3 — Le mur, nommé. C'est là que le chantier arrive.

**Cœur = la caveat d'admissibilité de de Haro (p.3).** Le graviton **mixed/Neumann** est
admissible **UNIQUEMENT** : (i) dans la **fenêtre BF / Ishibashi-Wald**, **OU** (ii) si la
théorie a un **CUTOFF**. Sinon le mode lent est **non-normalisable** ⟹ forcé **Dirichlet**.

Les deux voies réalisent **chacune une branche** :

- **ST `2409.08709`** = branche **CUTOFF** (timelike-bounded, temps fini, T² à cutoff) ⟹
  **échoue `R4″`** (genuine `𝓘⁺` sans cutoff).
- **de Haro `0808.2054`** = branche **fenêtre AdS₄** (l'objet renormalisé **EXISTE** :
  `⟨T_ij⟩ = 3ℓ²/16πG · g₍₃₎` ↔ Cotton, marginal Δ=3) ⟹ **échoue le dS-genuine**.

**La cellule `R1″ ∧ R2″ ∧ R3″ ∧ R4″` n'est livrée par AUCUNE construction.** Chaque candidat
ne couvre qu'un **sous-ensemble PROPRE**. `R3″` étant acquis, le **gap résiduel = une seule
cellule : `R1″ ∧ R2″ ∧ R4″`** — le plus net jamais atteint.

- **`R1″`** — jonction **DEUX-FACES** genuine. ✗ (de Haro = D/N comme deux **points fixes** à
  **UN** bord ; ST = tranche de Cauchy **mono-bord**).
- **`R2″`** — carte shadow `g₍₀₎↔g₍₃₎` **RENORMALISÉE** au pas **marginal**. ✗ au pas genuine
  (existe renormalisée en **AdS₄** ; ST livre une carte **régularisée**, pas les contre-termes
  au `𝓘⁺`).
- **`R4″`** — dS₄ **genuine** `𝓘⁺` **sans cutoff**. ✗.

**Pourquoi `T-b` et non `T-c`.** Déclarer le verrou définitif exigerait de **PROUVER**
l'absence de version renormalisée pour le graviton deux-bords en dS genuine. La caveat est un
**lean structurel FORT** (couverture bilatérale par sous-ensembles propres + non-normalisabilité
du mode lent sans cutoff) — un **quasi-théorème**. **Lean ≠ preuve.** *[`TRANSPORT` v0.4]*

## §4 — Le levier nommé. NON armé.

> **Une PREUVE d'(in)admissibilité du graviton propageant `mixed-BC` **deux-faces** au `𝓘⁺`
> **genuine**, **SANS cutoff**.**
> **Non-admissible ⟹ `T-c`.** **Admissible ⟹ une construction neuve à bâtir.**

C'est **la** question du chantier. Elle exige un **amendement R-7 daté** — elle n'est pas
couverte par les gels existants. *[`TRANSPORT` v0.4, « prochain levier NOMMÉ (NON armé) »]*

**Déjà tenté, déjà rendu :** le levier `§7quinquies` visait cette admissibilité et a rendu
**`K-B` = PRESCRIPTION-DÉPENDANT** (Marolf-Morrison **HORS-DOMAINE** en frame planaire/`𝓘⁺` ;
divergence de bord `𝓘⁻`/`𝓘⁺`) ⟹ **le levier n'a décidé dans aucun sens**, germe `T-c` **ni
renforcé ni converti**. *[`BETA-COPIE-LC-D-G3-KPS-KB.md`]* **Ne pas le rejouer en croyant
l'ouvrir.**

## §5 — S8 / S9 / S10 — ET C'EST ICI QUE JE DOIS ÊTRE HONNÊTE

**Ce que le mount principal porte, vérifié :**
- `LC-CONST-V1` §10 : « **Consommation profonde S8 / S9 / S10 (locus β, piste article)** ».
- `LC-JOURNAL-V94` §6 ACTION #3 (c) : « **S8/S9/S10** [locus β, **track-article**, **opérateur
  fournit les PDF**] » — **menu, décision opérateur, AUCUN geste obligé**.

**Ce que le mount principal NE porte PAS :** *(grep exhaustif du mount, 2026-07-18)*
- **les identités** des trois sources. Les noms **Bros–Moschella**, **Nakayama**,
  **Ghaffari–Luciano–Mantica** **n'apparaissent nulle part** sur `/mnt/project`. Ils viennent
  de la **piste article** et de la **mémoire du pilote** — **deux témoins faibles, et
  corrélés**.
- **la moindre attestation qu'ils touchent la cellule `R1″∧R2″∧R4″`.**

**Le piège, nommé.** Ces sources ont été retenues comme **pertinentes pour la SYNTHÈSE du
locus β dans l'article** (adjudication P-C : nouveauté de **synthèse/assemblage**). **Une
source utile à un article n'est pas une source qui comble un gap de KB.** Présumer le
contraire serait exactement le **fit** : choisir la cible après avoir choisi la source.

⟹ **P-0 (R-41) et P-1 (positionnement stérile) ne sont pas des formalités.** Ils existent
parce que la pertinence de S8/S9/S10 **pour ce mur-là** est **une hypothèse du pilote, non
vérifiée**. **L'issue « les trois sources sont hors-domaine pour la cellule » est ouverte,
et elle est honorable.**

## §6 — Risques amont, déclarés

- **Prérequis dS asymptotique.** Tout le transport suppose Λ>0 asymptotique. **DESI DR2
  (2025)** met sous tension la constance de Λ. Si Λ n'est pas constant, β **ne s'ouvre pas** —
  la question **change**. *[`TRANSPORT`, « risque amont, positionnement séparé »]*
- **`Δ-C` est le pivot, et son libellé a été audité.** `S7` a rendu **`S-2` = FIDÈLE MAIS PLUS
  ÉTROIT** : le blocage n'est **pas établi au secteur graviton** — celui-là même qui intéresse
  le programme. *[`BETA-COPIE-LC-D-S7-FIDELITE-DELTAC.md`]* **Le pivot `T2b` est donc plus
  étroit que son libellé ne le laissait croire. En tenir compte, ou refaire la même erreur.**
- **`p` reste libre.** Même β résolu ⟹ `C1` dS **conditionnel à `p`** — et le **P-sélecteur**
  est **PENDANT sous constat BIAISÉ**. **Ne pas s'appuyer dessus.**

## §7 — Anti-circularité `K` — verrou permanent

β **prend** l'état `+i` (Bunch-Davies — `LC-D-O2-P2`) et **WCH** (sens `D→N` —
`LC-D-O2-JONCTION`) comme **données POSÉES**. Il ne les **dérive pas** d'O₂. Aucune cible du
chantier ne peut présupposer `A4` comme **résultat**. *[`FACTORISATION` §0]*

---

**§6.4 — sentinelle.** Résumer un mur ne le déplace pas. `{A4 ; A2★ ; N}` **INCHANGÉ** ;
`O₂` non construit ; **β `T-b`, non résolu, SEUL facteur d'O₂ ouvert** ; `G3-a` non levé ;
`D1` non clos ; `N` non fixé ; `A4` non réduit ; `A2★` non tranché ; **`R-53 0/4`**.
**CCC n'est ni démontrée ni réfutée.**
