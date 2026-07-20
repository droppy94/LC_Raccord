---
id: LC-D-Q-DICTIONNAIRE-AB
titre: "[SUPERSEDED 2026-07-20 — verdict retiré, voir bandeau] Résultat S-QDIC-1 (DÉLIMITATION, KB-only + sceau reproductible, AUCUN sceau de finitude neuve) — dictionnaire Q↔N/ℓ pour le nœud (i) : la charge de fond Q du gaz de Coulomb porte-t-elle une puissance de ℓ qui la ferait basculer sous ℓ_AdS→iℓ_dS ? VERDICT CORRIGÉ = INDÉTERMINÉ (PAS A) : l'alternative se réduit à l'entier NON SCELLÉ p_Q (Q∝ℓ^{p_Q}) ; branche A exigerait p_Q≡0[4], NON établi (secteur dilaton non construit). L'ancien verdict « Q adimensionné ⟹ Q fixe ⟹ branche A (gate live) » est INFIRMÉ par l'audit froid : parité de c = artefact de construction (ne prouve pas p_Q=0), découplage préfacteur = tautologie (importé d'ASH), canal c→−c « fermé » = positivité déguisée contournée par la continuation imaginaire. Trois faits convergents : (1) Q entre dans le Virasoro chargé uniquement via l'improvement −Q(n+1)a_n (k3_Qsplit), génère c(Q)=1+4Q² (nombre pur, PAIR en Q, c(0)=1) — aucune puissance de ℓ ; (2) canal indirect Q↔c FERMÉ : le retournement dimensionnel c→−c (le fait dS/CFT, ce que i^{d-1} produit sur C_T,N,c_grav∝ℓ² en d=3) n'a AUCUNE solution réelle en Q (Q'=±i√(4Q²+2)/2), idem c→ic (d=2) ; (3) DÉCOUPLAGE préfacteur/Q : structure ASH (F1_spn) ⟨J^(s)J^(s)⟩=±(ℓ²/G)f(x), sous ℓ→iℓ le préfacteur bascule (−1=N→−N) mais Q∈f(x), Q∉préfacteur (vérifié). CONSÉQUENCE : branche B DISQUALIFIÉE comme raccord (Q→−Q laisse c invariante ; Q→iQ casse la réalité de P) ; la symétrie exacte (β,Q)→(−β,−Q) de l'audit est une réflexion INTERNE, non le raccord ; branche A retenue (réflexion physique = screening β→2Q−β à Q fixe, forme croisée à signe INDÉFINI déjà vérifiée ⟹ gate LIVE). RAFFINEMENT PORTÉ : le préfacteur global bascule de signe (−1 en d=3) ⟹ le gate n'est PAS vacuous (Ψ non invariant), mais la contrainte de positivité croisée hérite d'un SIGNE GLOBAL NÉGATIF en dS (« croisé ≥0 » AdS → « ≤0 » dS) à intégrer dans Cardy. CAVEATS : dictionnaire propre au niveau du PROXY spin-4 (gaz de Coulomb 2D) ; report vers la vraie fissure modulaire (Dom(Δ^{1/2}) vs Cardy sur |B⟩, d=3) = fait dur #3 du REPRISE NON levé ; c=1+4Q² dépend de la convention mais l'argument ne repose que sur la PARITÉ (robuste). SANS SURCLASSEMENT (§6.4) : délimitation, lean ≠ preuve ; NON un sceau de branche A ; audit froid neutralisé OBLIGATOIRE avant tout verrouillage ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée."
codename: LC-RACCORD
tags: [SUPERSEDED-2026-07-20, verdict-INDETERMINE-pas-A, reduction-p_Q, audit-froid-dico_Q, parite-artefact, decouplage-tautologique, canal-positivite-deguisee, module-D, noeud-i, fissure-croisee-spin4, alternative-A-B, reflexion-Q, charge-de-fond, gaz-de-Coulomb, dictionnaire, charge-centrale, c-1plus4Q2, i-power-d-1, CT-REALITE, F1-SPN, ASH, N-flip, prefacteur-global, screening, beta-2Q-beta, proxy-spin4, fissure-modulaire, delimitation, sans-sceau, §6.4, A4, A2star, N]
statut: "[v0.2 — SUPERSEDED 2026-07-20 par réduction-p_Q + audit froid ; conservé comme trace] Dictionnaire Q↔N/ℓ : verdict « branche A tranchée / gate live » RETIRÉ → INDÉTERMINÉ (PAS A). L'alternative se réduit à l'entier NON SCELLÉ p_Q (Q∝ℓ^{p_Q}) ; A exige p_Q≡0[4], non établi (dilaton non construit). AUDIT FROID de dico_Q (audit_neutral_dico.py) : les 3 « faits » de A sont non porteurs — parité de c = ARTEFACT (survit à tout poids diagonal, ne prouve pas p_Q=0), « Q∉préfacteur » = TAUTOLOGIE (ℓ²/G écrit sans Q ; indépendance réelle importée d'ASH), « c→−c sans racine réelle » = POSITIVITÉ DÉGUISÉE (continuation imaginaire Q'=±i√((1+2Q²)/2) la réalise ; Q→iQ utilisé ailleurs). Reste ACQUIS : G3-TRANSPORT ne mentionne jamais Q (pointeur A/B infirmé, correct) ; c(Q)=1+4Q² est le calcul juste de la charge centrale ; P polynôme réel deg_Q=6, impair-en-Q non nul ; D3 (Q→iQ casse réalité de P) au niveau proxy. SANS SURCLASSEMENT : {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée. Front canonique : REPRISE_..._reduction-pQ-isomorphisme-transport-C1b."
statut_id: "provisoire — à enregistrer si validé (LC-00-INDEX)"
type: "chaînon (résultat — DÉLIMITATION) : confronte la définition de Q (k3_Qsplit improvement −Q(n+1)a_n ⟹ c=1+4Q² ; k3_Qexplicit P(β,Q)) au mécanisme de basculement scellé amont (CT-REALITE : i^{d-1} sur ℓ^{d-1} ; F1_spn/ASH : N→−N préfacteur ℓ²/G). Sceau reproductible dico_Q.py (charge centrale, table transfos, canal indirect, découplage). Subordonné à LC-AUDIT-VERDICT §6.4."
fichier_compagnon: "dico_Q.py (sceau reproductible, sympy, sans réseau) — sha256 94ab8581eeac8d7af1782337eb5e5bc72c2eb5076f6e752e6663f8875b0f8d6e"
renvois: [REPRISE-fissure-croisee-spin4, LC-D-CT-REALITE, LC-D-CT-DUAL-DS, LC-D-SPN, LC-D-G3-TRANSPORT, LC-D3-SPECTRE-K3, k3_Qexplicit, k3_Qsplit, k3_shapovalov, k3_Bcross, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-AUDIT-VERDICT]
prerequis_kb: [k3_Qsplit, k3_Qexplicit, verif_D_CT_realite, verif_F1_spn, verif_spn]
tags_epistemiques: [délimitation, penche-branche-A, formalisable, décision ouverte, lecture / non scellé, audit-froid-requis]
version: 0.1
langue: fr
date: 2026-07-19
---

> **⚠ SUPERSEDED (2026-07-20).** Verdict « branche A tranchée / gate live » **retiré**. Deux routes indépendantes le remplacent par **INDÉTERMINÉ (pas A)** :
> 1. **Front ultérieur (réduction-`p_Q`, GLOSSAIRE v1.69).** L'alternative se réduit à l'entier **non scellé** `p_Q` (`Q ∝ ℓ^{p_Q}`) : `p_Q≡0[4]→`A, `≡2[4]→`B, impair→(iii). A n'est retenue que si `p_Q≡0[4]`, **non établi** (secteur dilaton non construit). Front canonique : `REPRISE_fissure-croisee-spin4_reduction-pQ-isomorphisme-transport-C1b.md`.
> 2. **Audit froid neutralisé de `dico_Q.py` (sceau `audit_neutral_dico.py`).** Les **trois « faits convergents »** de branche A sont chacun **non porteurs** : (1) la **parité de `c`** est un **artefact de construction** — elle survit à tout poids diagonal (`c=w₁/2+2w₂Q²`), forcée par `Q` linéaire sur un monôme orthogonal ; **elle n'établit PAS l'adimensionnalité** (= `p_Q=0`). (2) « `Q∉préfacteur` » est **tautologique** : `ℓ²/G` est écrit à la main sans `Q` ; le vrai contenu (indépendance de `Q` d'ASH 1108.5735) est **importé**, non vérifié ici. (3) « canal `c→−c` fermé (pas de racine réelle) » est de la **positivité déguisée** : la continuation imaginaire `Q'=±i√((1+2Q²)/2)` réalise `c→−c` **exactement**, et le fichier **utilise** `Q→iQ` ailleurs (D2/D3) — « pas de racine réelle » = « il faut quitter l'axe réel », ce que `ℓ→iℓ` fait précisément. Seul appui réel du traitement `Q` réel : **D3** (`Q→iQ` casse la réalité de `P`), énoncé **au niveau du proxy** seulement.
> **Conséquence de cohérence :** ce nœud est conservé comme **trace** ; le calcul `dico_Q.py` reste **correct et reproductible** mais **ne tranche rien** (checks majoritairement garantis par construction). Corps ci-dessous **inchangé** (abstract YAML title/statut corrigés en tête ; §3/§4 annotés).

# LC-D · S-QDIC-1 — dictionnaire `Q↔N/ℓ` : ~~`Q` fixe ⟹ branche A (gate live)~~ → **INDÉTERMINÉ (pas A)** [SUPERSEDED]

## 0. Objet

Le REPRISE `fissure-croisee-spin4_AUDIT-Q-reflexion` posait le nœud (i) comme **alternative binaire A/B**, tranchée par une donnée géométrique externe : *l'asymétrie AdS→dS assigne-t-elle à la charge de fond `Q` un signe opposé aux deux versants ?* — renvoyée à `LC-D-G3-TRANSPORT v0.4`. Ce nœud **résout la question par calcul de dictionnaire**, pas par lecture.

Question opérationnelle : **`Q` porte-t-il une dépendance en `ℓ` qui le ferait basculer sous `ℓ_AdS→iℓ_dS`** (mécanisme `i^{d-1}` de `CT-REALITE`, retournement `N→−N` de `F1_spn`) ?

## 1. Le pointeur `G3-TRANSPORT` est infirmé

`LC-D-G3-TRANSPORT v0.4` (KB) **ne fixe pas le sort de `Q`** : zéro occurrence de `Q`, charge de fond, dilaton, gaz de Coulomb, `β→2Q−β`. Il transporte le **joint graviton deux-bords D↔N (spin-2)**, verdict `T-b`. Homonymie : son « facteur `β ≡ G3-a` » (facteur d'O₂) **n'est pas** le `β` du gaz de Coulomb (`V_β`). Seul recoupement (TG-2) : le sort du **signe `C_T`** (`i^{d-1}`, `d=3` réel négatif) — le mécanisme, pas son application à `Q`.

## 2. Verdict du dictionnaire — trois faits convergents (sceau `dico_Q.py`)

1. **`Q` adimensionné.** Entre dans le Virasoro chargé uniquement via l'improvement `−Q(n+1)a_n` (`k3_Qsplit` : `L_{-2}|0⟩=½a_{-1}²+Q a_{-2}`) ; génère `c(Q)=1+4Q²` — **nombre pur, PAIR en `Q`**, `c(0)=1`. Aucune puissance de `ℓ`.
2. **Canal indirect `Q↔c` FERMÉ.** Le retournement dimensionnel `c→−c` (le fait dS/CFT, ce que `i^{d-1}` produit sur `C_T,N,c_grav∝ℓ²`) **n'a aucune solution réelle** en `Q` : `Q'=±i√(4Q²+2)/2`. Idem `c→ic` (`d=2`). La charge de fond interne ne peut pas absorber le basculement de la charge centrale.
3. **Découplage préfacteur/`Q`.** Structure ASH (`F1_spn`) : `⟨J^(s)J^(s)⟩=±(ℓ²/G)f(x)`. Sous `ℓ→iℓ`, le préfacteur `ℓ²/G→−ℓ²/G` (`−1 = N→−N`) ; **`Q∈f(x)`, `Q∉préfacteur`** (vérifié). Le basculement de signe higher-spin est un **préfacteur global**, pas `Q`.

**Table (effet sur `P=‖K3(Q)⁺‖²` et sur `c`) :**

| transformation | `δP=0` | `δc=0` | lecture |
|---|---|---|---|
| `Q→−Q` (branche B) | non | **oui** | retourne `Q` mais **pas** `c` ⟹ incohérent comme raccord |
| `Q→iQ` (timelike/dS) | non | non | **casse la réalité** de `P` |
| `β→2Q−β` (screening, `Q` fixe) | non | oui | réflexion **interne** à `Q` fixe (branche A) |
| `(β,Q)→(−β,−Q)` (audit) | **oui** | oui | seule symétrie exacte de `P` ; **interne**, pas le raccord |

## 3. ~~Conséquence — A/B tranchée en faveur de A (gate live)~~ [RETIRÉ — voir bandeau]

> **Correction (audit froid).** Cette section supposait que les 3 faits du §2 établissaient « `Q` fixe ». L'audit montre qu'aucun ne le fait (parité = artefact ; découplage = tautologie ; canal = positivité déguisée contournée par continuation imaginaire). Verdict corrigé : **INDÉTERMINÉ (pas A)**, réduit à l'entier non scellé `p_Q`. Le texte ci-dessous est **trace**.

~~**Le raccord laisse `Q` fixe ⟹ branche A ⟹ gate `C1-b` LIVE.** Branche B **disqualifiée comme raccord**.~~ La symétrie `(β,Q)→(−β,−Q)` de l'audit est **interne**, non le raccord — l'audit avait raison de tuer `R_D:β→−β`, mais sa conclusion « gate vacuous » supposait la branche B, ici écartée. Réflexion physique retenue = **screening `β→2Q−β`** à `Q` fixe ; forme croisée à **signe indéfini** (déjà vérifiée, REPRISE §2.3) ⟹ live.

**Raffinement porté :** le préfacteur global bascule de signe (`−1`, `d=3`). Le gate n'est **pas** vacuous (`Ψ` non invariant), mais la contrainte de positivité croisée hérite d'un **signe global négatif en dS** (« croisé `≥0` » AdS → « `≤0` » dS). À intégrer dans Cardy comme signe global.

## 4. Caveats & discipline

- **Dimension.** Dictionnaire propre au niveau du **proxy spin-4** (gaz de Coulomb 2D). Raccord physique `d=3`. Report vers la **fissure modulaire** (`Dom(Δ^{1/2})` vs Cardy sur `|B⟩`) = **fait dur #3** du REPRISE, **non levé**.
- **Convention de `c` — CORRIGÉ.** ~~argument robuste car ne dépend que de la parité~~. L'audit froid réfute : la **parité de `c` est un artefact de construction** (elle survit à tout poids diagonal, forcée par `Q` linéaire sur un monôme orthogonal) ; **elle ne prouve pas l'adimensionnalité** (`p_Q=0`). `c(Q)=1+4Q²` reste le calcul juste de la charge centrale, mais sa parité **ne porte pas** le découplage.
- **§6.4.** Délimitation, **lean ≠ preuve**. NON un sceau de branche A. **Audit froid neutralisé obligatoire** avant tout verrouillage. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; N non fixé ; CCC non démontrée.

## 5. Ancres numériques (non-régression, `dico_Q.py`)

- `c(Q)=1+4Q²` ; `c(−Q)−c(Q)=0` (pair) ; `c(0)=1`.
- `P` : `P_odd≠0` (impair en `Q` non nul) ; `deg_Q(P)=6`.
- `Q→−Q` : `δP≠0`, `δc=0`. `β→2Q−β` : `δP≠0`, `δc=0`. `(β,Q)→(−β,−Q)` : `δP=0`, `δc=0`.
- `P(β,iQ)` : ni réel ni `=P`.
- `c→−c` : racines `Q'=±i√(4Q²+2)/2` (non réelles).
- Préfacteur ASH `ℓ²/G` sous `ℓ→iℓ` : facteur `−1` ; `Q∉` préfacteur.
