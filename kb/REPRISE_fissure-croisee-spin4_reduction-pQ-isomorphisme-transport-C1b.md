# REPRISE — Nœud (i), fissure croisée spin-4 : réduction à l'entier `p_Q` / isomorphisme au transport C1-b — VERDICT **INDÉTERMINÉ (pas A)**

> **Statut de fichier — RECONSTRUCTION (2026-07-20).** Ce fichier était **annoncé** comme « reprise active » par `GLOSSAIRE_..._reduction-pQ` (v1.69, 2026-07-19) mais **n'avait jamais été produit** (front fantôme). Il est **reconstruit fidèlement** à partir de trois sources, chacune étiquetée dans le corps :
> - **[G]** le stub GLOSSAIRE réduction-`p_Q` — **autoritaire** sur le verdict et le ternaire `p_Q` ;
> - **[L]** la lignée du nœud (i) : `pont-KMS` (gate croisé `M_ab`=C1-b), `DICTIONNAIRE-AB` (cadre + faits durs #1–#3), `bracket_unitarite_spin4`, `AUDIT-Q-reflexion` ;
> - **[A]** l'audit froid neutralisé de `dico_Q.py` (sceau `audit_neutral_dico.py`, sha256 `e2a42b4b…ef044`, 2026-07-20) — **postérieur** au glossaire, il **corrobore** la démotion.
>
> **Supersession.** Ce fichier **supersède** `REPRISE_..._DICTIONNAIRE-AB.md` (verdict « branche A tranchée / gate live » **retiré**) et son nœud-résultat `LC-D-Q-DICTIONNAIRE-AB.md` (marqués superseded le 2026-07-20).
> **Nœuds référencés — statut de vérification (2026-07-20).** `LC-D-O2-P-SELECTEUR`, `LC-D-O2-DELTA-C`, `LC-D-CT-DUAL-DS` : relus et confrontés au §2.2 — **CONFIRMÉS**. `02_programme` Module [E] (secteur dilaton, porte `p_Q`) : relu — **CONFIRMÉ** (§2.1). **Toutes les références du front sont désormais KB-vérifiées.**

---

## 0. Statut en une page

- **Nœud (i) : toujours OUVERT.** Le gate `C1-b` n'est ni scellé ni fermé.
- **Verdict de l'alternative : INDÉTERMINÉ (pas A).** [G] Ni « branche A tranchée » (démoti du DICTIONNAIRE-AB), ni B, ni (iii) : l'alternative se **réduit à un unique entier non scellé** `p_Q`.
- **La réduction (le mouvement central).** [G] `Q ∝ ℓ^{p_Q}`. Sous la règle scellée `CT-REALITE` (`i^{p}`, parité de `ℓ`), l'alternative binaire A/B devient **ternaire** :
  - `p_Q ≡ 0 [4]` → **A (gate LIVE)** ;
  - `p_Q ≡ 2 [4]` → **B (gate VACUOUS)** ;
  - `p_Q` **impair** → **(iii)** : `Q` imaginaire, **réalité de `P(β,Q)` cassée**.
- **`p_Q` NON scellé.** [G ; KB✓] Sa détermination vit dans le **secteur dilaton** = `02_programme` **Module [E]**, que le programme classe *« échelle posée, non dérivée »*, *« hypothèse de travail »*, statut *« à inventer / hors de portée (CCC quantique requise) »*. Module [E] **redirige explicitement vers [D]** (le champ d'échelle `Ω`/D1 et `ℓ_P` pointent vers la donnée holographique `g₃`) — donc `p_Q` route vers la **même donnée** que le report modulaire `d=3` (§5.2). Corpus épuisé sans le fixer.
- **L'opération physique correcte.** [G] Le raccord AdS→dS **n'est pas** `φ→−φ` (la prémisse de branche B est **fausse**) mais `ℓ_AdS → i ℓ_dS` + shadow/Legendre.
- **Isomorphisme au transport.** [G] A/B/(iii) = **instance du transport AdS→dS renormalisé au pas C1-b** (`LC-D-G3-TRANSPORT` = T-b ; `LC-D-O2-DELTA-C` T2 shadow-bloqué au C1-b), même intrant que le poids `b` d'Odak-Speziale du `P-SELECTEUR` (P-3/HOLD, invariance ou non sous `Λ<0 → Λ>0`).
- **Le lean qui NE transfère pas.** [G] `CT-DUAL-DS` (`C̃_T = +C_T`, graviton sign-préservant) est **inter-secteur, non transférable à `Q`** : la puissance de `ℓ` de `Q` manque, le secteur dilaton n'est pas construit.
- **Corroboration par audit froid [A].** L'ancien verdict « branche A » reposait sur trois « faits » de `dico_Q` supposés établir `p_Q = 0`. L'audit montre qu'**aucun ne le fait** — ils sont artefact / tautologie / positivité déguisée (§2.3). **L'audit et le ternaire `p_Q` sont la même structure** : le canal `c→−c` « fermé sans racine réelle » du DICTIONNAIRE **est** la branche `(iii)` (continuation imaginaire de `Q`), et non une preuve de `p_Q = 0`.
- **Discipline §6.4.** [G] Réduire/consolider **ne construit rien**. `β ≡ G3` reste le **seul facteur d'O₂ ouvert**. `{A4 ; A2★ ; N}` **INCHANGÉ** ; O₂ non construit ; `β` non résolu ; D1 non clos ; `N` non fixé ; CCC non démontrée. **AUCUN sceau, AUCUNE algèbre neuve.**

---

## 1. Cadre correct de (i) — le gate est le CROISÉ (reporté de `pont-KMS` / `DICTIONNAIRE`, inchangé) [L]

Énoncé correct du gate (inchangé, `pont-KMS §1c`) :
$$\boxed{\ \mathcal T_4\ge0\iff\langle B|\,W_4^{(1)}W_4^{(2)}|B\rangle\ge0\ (\text{terme croisé côté 1}\leftrightarrow\text{côté 2})\ =\ \text{réflexion-positivité spin-4 de }|B\rangle\ =\ \text{C1-b}.\ }$$

- La densité **diagonale** $\tilde G_B^{+}=\sum_a|B_a|^2 g_a^{(4)}(\nu)$ est positive **gratuitement** (norme de Hilbert) : **non scellante**. Piège d'objet.
- $\text{Dom}(\Delta^{1/2})\ni|B\rangle$ = convergence de Cardy au seul module $\ell=2\pi$ : **nécessaire-à-définir**, ne scelle rien.
- Le vrai sceau est la positivité **croisée** = Cardy. Question (i) : le cône de $M_{ab}=\langle\langle a|W_4^{(1)}W_4^{(2)}|b\rangle\rangle$ contient-il **strictement** le cône de Cardy (⟹ Voie 2 ouverte) ou coïncide-t-il (⟹ `fermé, gated-C1-b`) ?
- **Contrôles non triviaux** (reportés) : lockstep §5.4 (croisé sign-incertain **exactement quand** $\gamma_4^{\text{eff}}=1-\mathcal T_4\notin\{0,1\}$) ; avertissement MPR (spin 2 : $\mathcal T+\mathcal R=1$ tous positifs ; « plus élaboré pour les symétries étendues » = notre cas).

---

## 2. La réduction `p_Q` et son verdict

### 2.1 De l'alternative binaire au ternaire sur un entier [G]

La question opérationnelle du DICTIONNAIRE — « `Q` porte-t-il une puissance de `ℓ` qui basculerait sous `ℓ_AdS→iℓ_dS` ? » — est la **bonne** question, mais sa réponse n'est pas « non » : c'est **un entier `p_Q`** (`Q ∝ ℓ^{p_Q}`) qui reste à déterminer. La règle scellée `CT-REALITE` (facteur `i^{p}`, gouverné par la **parité de `ℓ`**, `c₀`-indépendant) transforme le sort de `Q` en fonction de `p_Q mod 4` :

| `p_Q mod 4` | facteur `i^{p_Q}` | sort de `Q` | branche |
|---|---|---|---|
| `0` | `+1` | fixe, réel | **A — gate LIVE** |
| `2` | `−1` | retourné, réel | **B — gate VACUOUS** |
| `1, 3` (impair) | `±i` | imaginaire | **(iii) — réalité de `P` cassée** |

**Où vit `p_Q` [KB✓ Module [E]].** L'entier `p_Q` = la puissance de `ℓ` que la charge de fond acquiert dans le **secteur d'échelle physique** = `02_programme` **Module [E]** (dilaton). Ce secteur est classé par le programme *« échelle posée, non dérivée »*, *« hypothèse de travail »*, *« à inventer / hors de portée (CCC quantique requise) »*, et **redirigé vers [D]** (holographie `g₃`). ⟹ `p_Q` **non scellé** n'est pas un trou temporaire : il tient à un secteur non construit, dont la construction route vers la **même donnée `g₃`** que le report modulaire `d=3` (§5.2). C'est la racine commune du verdict INDÉTERMINÉ.

### 2.2 Isomorphisme au transport C1-b [G ; KB-vérifié 2026-07-20]

A/B/(iii) n'est pas un problème isolé : c'est une **instance du transport AdS→dS renormalisé au pas C1-b**. Points d'ancrage (les trois nœuds ci-dessous **relus et confirmés** cette session) :

- **`LC-D-G3-TRANSPORT` = T-b** : transporte le graviton deux-bords spin-2, **ne mentionne jamais `Q`** — pointeur A/B du DICTIONNAIRE correctement infirmé.
- **`LC-D-O2-DELTA-C` (S-O2C-2) = T2 bloqué au C1-b** ✓ : `Δ_𝒞=d` (marginal, générateur = trace GHY) extrait en AdS ⟹ C1-b ; **transport dS BLOQUÉ** car la carte D↔N = Legendre = `Δ↔shadow` **s'effondre dès que la renormalisation est requise** (régime C1-b), contre-termes AdS projetés hors, Skenderis mono-bord/scalaires (graviton non traité).
- **`LC-D-O2-P-SELECTEUR` = P-3, adjugé** ✓ : verdict **P-3 (INDÉTERMINÉ, HOLD)**, **adjugé le 2026-07-17** par le CSE-2 souverain (locus α = **A-1**, P-3 confirmée). Intrant nommé **identique** au nôtre : « construction du transport AdS→dS au pas C1-b renormalisé, OU démonstration positive, indépendante de `β`, de l'**invariance ou non du poids `b` d'Odak-Speziale sous `Λ<0 → Λ>0`** ». C'est la question `p_Q` instanciée pour le poids d'O₂.
- **`LC-D-CT-DUAL-DS` = lean sign-préservant, NON transférable** ✓ : scelle `C̃_T=+C_T` (graviton) en dS. **Mécanisme = la machinerie `p_Q` elle-même** : `i^{d-1}` attaché **au seul préfacteur `ℓ^{d-1}`** (même puissance pour `C_T` et `C̃_T`), les facteurs sans `ℓ` (le `−2`, le `−` relatif) **non continués** ⟹ rapport `+1` invariant ; **firewall** : injecter (à tort) un `i` sur le `−2` basculerait à `C̃_T=−C_T` ⟹ résultat **sensible à la puissance de `ℓ`, non tautologique**. Ceci **valide** le fait que tout se joue sur `p_Q`. Le lean est **inter-secteur** (graviton, `p=d−1=2`) et **non transférable à `Q`** : la puissance de `ℓ` de `Q` (`p_Q`) est un **secteur distinct, non construit**.

### 2.3 Corroboration par l'audit froid de `dico_Q` [A]

L'ancien verdict « branche A » (DICTIONNAIRE §2.2) posait trois « faits convergents » supposés établir `p_Q = 0`. Audit neutralisé (`audit_neutral_dico.py`, incognito, adversarial) : **aucun n'établit `p_Q = 0`**.

| « fait » branche A (DICTIONNAIRE) | ce qu'il prétendait | verdict d'audit |
|---|---|---|
| parité de `c(Q)=1+4Q²` | `Q` adimensionné ⟹ `p_Q=0` | **artefact** : survit à tout poids diagonal (`c=w₁/2+2w₂Q²`), forcée par `Q` linéaire sur un monôme orthogonal. Ne dit **rien** de `p_Q`. |
| `Q∉` préfacteur `ℓ²/G` | découplage vérifié | **tautologie** : `ℓ²/G` est écrit à la main sans `Q`. L'indépendance réelle est **importée d'ASH 1108.5735**, non vérifiée par `dico`. |
| `c→−c` sans racine réelle | canal `Q↔c` fermé | **positivité déguisée** : la continuation imaginaire `Q'=±i√((1+2Q²)/2)` réalise `c→−c` **exactement**. |

**Le point de fusion.** Cette dernière ligne **est** la branche `(iii)` : « quitter l'axe réel » = `Q` imaginaire = `p_Q` impair = réalité de `P` cassée (audit D3 : `Im P(β,iQ)≠0`). Le DICTIONNAIRE traitait `Q→iQ` comme illégitime (D2/D3) tout en s'appuyant sur `ℓ→iℓ` — **deux poids, deux mesures**, corrigé ici : `ℓ` se continue (géométrie), `Q` ne se continue réel que **si** `p_Q` pair, ce qui **n'est pas établi**. L'audit ne donne **aucune** évidence pour B ; il retire l'évidence-de-A et laisse **INDÉTERMINÉ**.

---

## 3. Faits durs subsistants (contre le programme, toute lecture) [L, inchangés]

1. **Mauvais opérateur.** `β→−β` à `Q` fixe n'est aucune réflexion candidate. À jeter.
2. **`Ψ` pas conforme propre.** `N=‖K3⁺‖²` pas fonction de `x` seul ⟹ pas descendant covariant d'une famille unique ; **`|K3⁺⟩` est-il le bon objet à réfléchir ?**
3. **Proxy vs vraie fissure — LE caveat de fond.** La forme croisée sur `|K3⁺⟩` est un **proxy spin-4** (gaz de Coulomb 2D). La fissure (i) est **modulaire** (`Dom(Δ^{1/2})` vs Cardy sur `|B⟩`, raccord `d=3`). **Le report modulaire `d=3` reste à faire** — c'est l'arbitre du nœud, non levé.

> **Note d'audit [A] sur le socle de calcul.** `dico_Q.py` reste **correct et reproductible** ; ses checks sont majoritairement **garantis par construction** (parité, `Q→−Q`/`(β,Q)→(−β,−Q)` sur `c`, non-racine réelle, préfacteur). Genuinement informatifs : la valeur de `P`, `deg_Q(P)=6`, partie impaire non nulle, `Im P(β,iQ)≠0`. La « forme fermée `P=f(β(β−2Q))` » narrée dans le bloc D des scripts neutres est **fausse** (réfutée par leur propre code : `N−cand(x)≠0`, résidu `7212·Q+…`) — hygiène : ne pas la ré-asserter.

---

## 4. Acquis — ce qu'il ne faut PAS rouvrir [L]

- **R1–R12** (`verrouillé`) : `G=1097/648`, bracket `[1/6π,1/4π]`, bord haut inconditionnel (R6 bulk), bord bas `formalisable, gated-C1-b`.
- **Niveau 4** : `W_4=4v_2−3v_3−2v_5`, Gram `diag(4,3,8,4,24)`, `‖W_4‖²=216`, `B=−1/9`, fraction `1/3`.
- **Chargé `Q`** (`k3_Qsplit`/`k3_Qexplicit`) : `Λ_4(Q)` conservé ; `‖W_4(Q)‖²`, `frac^inv(Q)→1/3`, `P(β,0)=β²(27β⁸−180β⁶+6β⁴+1136β²+108)`. **Intacts.**
- **Volet neutre** (`k3_Bcross`) : collage gaussien ⟹ `𝒯_4≥0` SOS ⟹ signe irréductiblement non gaussien. **Acquis** (redirige, ne scelle rien).
- **`c(Q)=1+4Q²`** : calcul **juste** de la charge centrale. Mais sa **parité ne porte pas** le découplage (audit).
- **Pointeur `G3-TRANSPORT` infirmé** : lu, ne mentionne jamais `Q` (correct, à conserver).

---

## 5. Prochaines briques (avec garde-fous)

1. **Déterminer `p_Q` (le seul vrai verrou de A/B/(iii)).** [G ; KB✓] Cela **exige de construire le secteur dilaton** (`02_programme` Module [E]), que le programme classe *« posée, non dérivée / à inventer / hors de portée (CCC quantique requise) »*. Sans lui, le verdict reste INDÉTERMINÉ. **Mais** Module [E] **redirige vers [D]** (échelle `Ω`/`ℓ_P` → donnée holographique `g₃`) : la détermination de `p_Q` route donc vers la **même donnée `g₃`** que le report modulaire `d=3` (#2). ⟹ Attaquer #2 est aussi la voie vers `p_Q`.
2. **Report modulaire (fait dur #3) — l'arbitre accessible.** [L] Vérifier si le croisé sur `|K3⁺⟩` (proxy 2D) capture (i) [`Dom(Δ^{1/2})` vs Cardy sur `|B⟩`, `d=3`], ou attaquer (i) directement sur `|B⟩`, en évitant l'écueil #2. Puisque le proxy ne tranche pas `p_Q`, c'est `d=3` qui décide.
3. **Croisé `M_ab` avec intertwiner correct + signe global.** [L] Construire la forme croisée avec l'opérateur de réflexion `V_β↔V_{2Q−β}` unitaire (**PAS** le `(−1)^len` naïf), en intégrant le signe global `−1` du préfacteur dS (`d=3`). → **audit froid obligatoire**.
4. **Nœuds rapportés — TOUS vérifiés (2026-07-20).** `P-SELECTEUR`, `O2-DELTA-C`, `CT-DUAL-DS` (§2.2) et `02_programme` Module [E] (§2.1/§0) relus et confirmés. Plus aucune affirmation du front n'est adossée à du non-lu.
5. **Nœud (ii) en veille.** Dégradation signée `O(γ_4^eff)` de la balance détaillée : peut rouvrir même si (i) reste gaté. Ne pas oublier.

---

## 6. Statut épistémique (charte L-001 / §6.4)

- **verrouillé :** R1–R12 ; `G=1097/648` ; bracket `[1/6π,1/4π]` ; bord haut inconditionnel ; `c(Q)=1+4Q²` (calcul). **Intact.**
- **cadre correct (formalisable) :** gate = croisé `M_ab` = C1-b ; `Dom(Δ^{1/2})` nécessaire-à-définir, non scellant.
- **réduction (délimitation, lean ≠ preuve) :** A/B → ternaire A/B/(iii) sur `p_Q` ; isomorphisme au transport C1-b.
- **négatif net :** ANEC spin-4 ; pas de raccourci kinématique ; `β→−β` mauvais opérateur ; parité de `c` non porteuse (audit) ; forme-en-`x` fausse (audit).
- **verdict :** **INDÉTERMINÉ (pas A)** — `p_Q` non scellé, secteur dilaton non construit.
- **ouvert (périmètre irréductible `{A4;A2★;N}` — NE PAS chiffrer) :** `𝒯_4`, `N≡Λ`, gap SG. `β≡G3` = seul facteur O₂ ouvert. D1 non clos ; CCC non démontrée.

---

## 7. Annexe — swap KB à opérer

1. **Reprise active** : ce fichier. Marquer `REPRISE_..._DICTIONNAIRE-AB.md` **superseded** (fait 2026-07-20) ; idem nœud-résultat `LC-D-Q-DICTIONNAIRE-AB.md`.
2. **Sceau d'audit** : enregistrer `audit_neutral_dico.py` (sha256 `e2a42b4b…ef044`) en compagnon de la note d'audit ; `dico_Q.py` reste en KB (calcul correct, rôle corrigé : « ne tranche pas »).
3. **Glossaire** : l'entrée réduction-`p_Q` (v1.69) est **cohérente** avec ce fichier ; ajouter une ligne `maj` datée 2026-07-20 « front `reduction-pQ` matérialisé + corroboré par audit froid `dico_Q` ; DICTIONNAIRE-AB superseded ».
4. **Ne PAS toucher** : faits durs #1–#3, R1–R12, `k3_shapovalov/Qsplit/Qexplicit/Bcross`, corps du DOSSIER (A1–A4). `{A4 ; A2★ ; N}` **INCHANGÉ**.
5. **Nœuds rapportés** : `P-SELECTEUR`, `O2-DELTA-C`, `CT-DUAL-DS`, `02_programme` Module [E] — **tous vérifiés le 2026-07-20**. Aucune référence non relue ne subsiste.

*Fin de reprise. Le nœud (i) reste le nœud décisif ; l'alternative est réduite à l'entier non scellé `p_Q` (secteur dilaton non construit) ⟹ INDÉTERMINÉ (pas A). Arbitre accessible : report modulaire `d=3` (#3). Ne pas chiffrer `{A4 ; A2★ ; N}`. Tout nouvel objet de positivité → audit froid neutralisé obligatoire.*
