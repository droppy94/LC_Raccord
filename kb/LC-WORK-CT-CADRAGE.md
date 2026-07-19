---
id: LC-WORK-CT-CADRAGE
titre: "Module D / dS-CFT — CADRAGE PAPER-FIRST de la CHARGE CENTRALE C_T d'une CFT₃ à 𝓘⁺ : « C_T est-elle déterminée (normalisation / unitarité / anomalie / holographie) ou libre ? ». Chantier différé M1 de LC-WORK-REPRISE-POST-D1-E. AUCUN sceau neuf (paper-first). RÉSULTAT DU TRI : (1) la FORME du deux-point ⟨TT⟩∝k³ (Δ=d=3) est `établie` (sceau SPECTRE-K3) ; toute la liberté résiduelle de D1 au niveau gaussien est l'unique scalaire C_T. (2) Tri des quatre mécanismes : normalisation conforme NE fixe que la forme (C_T libre dans une CFT₃ abstraite) ; ANOMALIE INDISPONIBLE (d=3 impair, pas d'anomalie de trace — `établi` négatif net) ; UNITARITÉ ne borne que le signe (C_T>0), pas la valeur, ET tombe en dS/CFT (non-unitaire) ; seule la DUALITÉ HOLOGRAPHIQUE détermine C_T, via C_T~ℓ^{d-1}/G~(ℓ_dS/ℓ_P)²~N. ⟹ C_T n'est PAS une inconnue indépendante : holographiquement VERROUILLÉE à N (même mécanisme déterminant que N lui-même, pas seulement même scaling). (3) FINDING (calculé, cancellation H,G) : A_T·N est un NOMBRE PUR ; en convention standard (spectre tensoriel BD 𝒫_h=(2/π²)(H/M_Pl)² + entropie GH S_dS=π/(GH²)) A_T·N=16. Promotion de D-ii : le lien A_T~1/C_T~1/N passe de `scaling` à candidat-ÉGALITÉ à coefficient `formalisable`/calculable (16 standard, π en convention lâche — la cancellation H,G est, elle, insensible à la convention). CE QUE LE CADRAGE NE FAIT PAS : ne ferme PAS D1 (circularité LC-E intacte ; non-unitarité dS/CFT C_T imaginaire/négatif sous continuation `à inventer` ; CFT de raccordement non construite `à inventer`) ; ne scelle RIEN ; n'établit PAS que la relation inflationnaire standard survit à la transposition dS/CFT-au-crossover (`à inventer`)."
codename: LC-RACCORD
type: "note de travail / cadrage papier (paper-first) — détermination de la charge centrale C_T en dS/CFT (d=3, 𝓘⁺). Subordonnée à LC-AUDIT-VERDICT §6.4. Étage cartographie (LC-07-like), non fermeture (LC-10-like). Chantier différé M1 de LC-WORK-REPRISE-POST-D1-E ; successeur logique de LC-WORK-D1-E-AMPLITUDE (instruit son coefficient A_T(C_T))."
version: 0.2
langue: fr
date: 2026-06-09
maj: "2026-06-09 — v0.2 : renvoi (statut) — le candidat-égalité A_T=16/N posé ici (§3, promotion D-ii) est désormais SCELLÉ par LC-D-CT-ATN v0.1 (verif_D_CT_ATN.py, EXIT 0) : deux routes indépendantes (canonique BD + holographique dS/CFT) CONVERGENT, A_T·N=16 (nombre pur, H,G se simplifient), verrouillage C_T/N=1/(32π²) confirmé par calcul (au-delà de la vérif symbolique légère de ce cadrage). Le `à inventer` (valeur/réalité de C_T en dS, survie au crossover, fixation de N) est inchangé ; D1 non clos. Aucune touche à l'algèbre du cadrage. | 2026-06-09 — v0.1 : cadrage initial du chantier M1. (1) Sépare la FORME (⟨TT⟩∝k³, Δ=3, `établie` par SPECTRE-K3) de la NORMALISATION C_T (= toute la liberté résiduelle de D1 au gaussien). (2) Trie les quatre mécanismes susceptibles de fixer C_T (normalisation conforme / anomalie / unitarité / holographie) : seul l'holographique détermine C_T, en le verrouillant à N (C_T~ℓ^{d-1}/G~N) ; l'anomalie est INDISPONIBLE en d=3 impair (`établi` négatif). ⟹ C_T n'ajoute aucune inconnue indépendante. (3) FINDING calculé (cancellation H,G ; vérifié symboliquement) : A_T·N est un nombre pur, =16 en convention standard. PROMOTION DE D-ii (décision opérateur 2026-06-09, option 1) : A_T~1/C_T~1/N passe de `scaling` à candidat-ÉGALITÉ à coefficient `formalisable`/calculable, caveats conventions (16 std / π lâche ; cancellation H,G insensible) + transposition. SANS SURCLASSEMENT (§6.4) : forme k³ `établie (sceau)` ; verrouillage holographique de C_T à N `formalisable` ; valeur exacte de C_T en dS et survie de la relation au crossover `à inventer` ; circularité LC-E `décision ouverte` (non brisée) ; non-unitarité dS/CFT `à inventer`. NE ferme PAS D1. AUCUN sceau neuf, AUCUNE touche aux chaînons existants. Propagation §7 NON exécutée (proposée)."
statut: "CADRAGE C_T POSÉ. Tri établi : C_T NON libre — holographiquement verrouillée à N (anomalie indisponible en d=3 ; unitarité ne borne que le signe et tombe en dS/CFT ; normalisation conforme ne fixe que la forme). D-ii PROMU : A_T·N nombre pur (=16 convention standard) ⟹ candidat-égalité à coefficient `formalisable`/calculable. D1 NON clos (circularité LC-E intacte ; non-unitarité dS/CFT et transposition au crossover `à inventer`). CCC non démontrée. Aucun sceau."
prerequis_kb: [LC-WORK-D1-E-AMPLITUDE, LC-D-HOLOGRAPHIE-G3, LC-D3-SPECTRE-K3, LC-D3-WEYL-BUNCHDAVIES, LC-E-PLANCK-RESIDUEL, LC-A-D1-FACTEUR-CONFORME, LC-WORK-A3-D1-PASSERELLE, LC-AUDIT-VERDICT, LC-00-INDEX, 02_programme-de-recherche, 03_glossaire, 04_references]
fichiers_compagnons_kb: []   # paper-first — AUCUN sceau neuf. Le finding A_T·N=16 est une vérification symbolique légère (cancellation H,G), NON un sceau verif_*.py déposé ; s'adosse aux scellés existants verif_D3_spectre_k3.py, verif_D_g3.py, verif_D3_bunchdavies.py, verif_E_planck.py.
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
renvois: [LC-D-CT-ATN, LC-WORK-D1-E-AMPLITUDE, LC-D-HOLOGRAPHIE-G3, LC-D3-SPECTRE-K3, LC-D3-WEYL-BUNCHDAVIES, LC-E-PLANCK-RESIDUEL, LC-A-D1-FACTEUR-CONFORME, LC-WORK-A3-D1-PASSERELLE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-AUDIT-VERDICT, LC-00-INDEX, LC-04-REFERENCES]
---

# LC-WORK · Cadrage `C_T` — la charge centrale céleste est-elle déterminée ou libre ?

> **Question (chantier M1).** La passerelle D1⟷E (`LC-WORK-D1-E-AMPLITUDE`) a réduit le résidu
> gaussien de D1 à **un seul nombre**, l'amplitude `A_T`, et l'a rattaché au compte `N` de `[E]`
> par `A_T~1/C_T~1/N` — **au niveau scaling uniquement** (décision D-ii). Restait la question
> de fond : la **charge centrale** `C_T` de la CFT céleste (`d=3`, 𝓘⁺, dS/CFT) est-elle
> *déterminée* par un principe (normalisation / unitarité / anomalie / holographie), ou
> *libre* ? Si déterminée ⟹ `A_T` fixé (conditionnel à la circularité LC-E) ; si libre ⟹ `A_T`
> reste `décision ouverte`, mais la réduction « résidu = `A_T` » demeure acquise.
>
> **Verdict cartographié.** **(1)** La **forme** `⟨TT⟩∝k³` (`Δ=d=3`) est `établie` (sceau
> `SPECTRE-K3`) ; toute la liberté résiduelle de D1 au gaussien est l'unique scalaire `C_T`.
> **(2)** Des quatre mécanismes, **seule la dualité holographique détermine `C_T`** — et elle le
> **verrouille à `N`** (`C_T~ℓ^{d-1}/G~(ℓ_dS/ℓ_P)²~N`). L'**anomalie est indisponible** (`d=3`
> impair, `établi` négatif net) ; l'**unitarité** ne borne que le signe (et tombe en dS/CFT
> non-unitaire) ; la **normalisation conforme** ne fixe que la forme. ⟹ `C_T` n'ajoute **aucune
> inconnue indépendante**. **(3)** *Finding* (calculé) : `A_T·N` est un **nombre pur**
> (cancellation `H,G`), `=16` en convention standard ⟹ le lien `A_T~1/N` passe de `scaling` à
> **candidat-égalité à coefficient `formalisable`/calculable**.
>
> **Réduction d'hypothèse, pas fermeture de D1** : circularité LC-E intacte ; valeur exacte de
> `C_T` en dS et survie de la relation au crossover `à inventer`.

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce document est un **cadrage** (étage `LC-07`-like), au même titre que `LC-WORK-A2-CONJECTURE`
(C7-b/A2), `LC-WORK-A3-D1-PASSERELLE` (A3/D1) et `LC-WORK-D1-E-AMPLITUDE` (D1⟷E, son parent
direct). Il **instruit** une question (« qu'est-ce qui fixe `C_T` ? ») et **trie** ; il **ne
ferme pas** D1 et ne scelle rien. Discipline `LC-AUDIT-VERDICT §6.4` : un `établi` atteste une
signature/algèbre, jamais « la physique de la CCC est établie ».

**Ce qui est scellé (adossé, aucun sceau neuf)** : la **forme** `⟨g₃g₃⟩∝k³` / `⟨TT⟩∝k^{2Δ-d}`,
`Δ=d=3` (`verif_D3_spectre_k3.py`) ; le dictionnaire `g₃=⟨T⟩`, `d=3` impair ⟹ traceless +
conservé (`verif_D_g3.py`) ; la relation d'état BD `g₃=-(i/3)k³g₀` (`verif_D3_bunchdavies.py`) ;
l'entropie/compte `N=S_dS` (`verif_E_planck.py`).

**Choix de périmètre verrouillés (opérateur, 2026-06-09).**
- **(CT-i)** Paper-first : **aucun** sceau dS/CFT neuf. Le *finding* `A_T·N=16` est une
  **vérification symbolique légère** (cancellation `H,G`), pas un `verif_*.py` déposé.
- **(CT-ii)** Le *finding* `A_T·N=16` est consigné comme **candidat-égalité** : il **promeut**
  D-ii (de `scaling` vers coefficient `formalisable`/calculable), **bien tagué**, avec caveats
  conventions + transposition. (Option 1 de la décision d'ouverture ; l'option « sceller
  maintenant » a été écartée — paper-first d'abord.)
- **Cible = instruire le coefficient `A_T(C_T)`** (le « chantier différé M1 » de la reprise),
  donc trier `C_T` : `établi` / `formalisable` / `à inventer`.

---

## 1. Séparer la FORME de la NORMALISATION `[le bon découpage]`

Pour toute CFT de dimension `d`, la symétrie conforme fixe **entièrement la forme** du deux-point
du tenseur de stress, à un seul scalaire global près — la **charge centrale** `C_T` :

$$\langle T_{ij}(x)\,T_{kl}(0)\rangle = \frac{C_T}{|x|^{2d}}\,\mathcal I_{ij,kl}(\hat x),
\qquad \mathcal I_{ij,kl}\ \text{structure tensorielle fixée par conformité.}$$

En `d=3` à 𝓘⁺, c'est exactement le `⟨TT⟩∝k^{2Δ-d}=k³` (`Δ=3`) **scellé** par `SPECTRE-K3`.
Donc le découpage est net :

| Pièce du deux-point | Contenu | Statut |
|---|---|---|
| **forme** (`∝k³`, structure `𝓘`) | invariance d'échelle côté `g₃` | **`établi (sceau)`** (`SPECTRE-K3`) |
| **normalisation** `C_T` | le **seul** scalaire libre | objet du présent cadrage |

⟹ **Toute la liberté résiduelle de D1 au niveau gaussien est ce seul nombre `C_T`** (équivalent à
`A_T` via `A_T~1/C_T`, cf. §3). « Qu'est-ce qui fixe `C_T` ? » est donc *la* question — pas une
parmi d'autres.

---

## 2. Tri des quatre mécanismes `[le cœur du cadrage]`

Quatre principes pourraient en théorie fixer `C_T`. On les passe un par un.

**(a) Normalisation par la symétrie conforme seule — NE fixe que la forme.** La conformité
détermine la structure `𝓘_{ij,kl}` et l'exposant (`Δ=d=3`), **pas** le coefficient `C_T`. Dans une
CFT₃ *abstraite*, `C_T` est une **donnée libre, dépendante de la théorie** (chaque CFT a son
`C_T`). `[établi — négatif : la conformité seule laisse `C_T` libre]`

**(b) Anomalie conforme — INDISPONIBLE en `d=3`.** En `d` **pair** (`d=2,4`), une charge centrale
apparaît dans l'**anomalie de trace** `⟨T^i_i⟩∝(\text{invariants de courbure})` et s'y trouve donc
*protégée/reliée* à une donnée géométrique. En `d=3` **impair**, il n'y a **pas d'anomalie de
trace** — déjà acquis (`HOLOGRAPHIE-G3 §2 [C]` : `d=3` impair ⟹ `⟨T⟩` traceless **et** conservé,
« propre »). La route « charge centrale ↔ anomalie » des `d=2,4` **n'existe tout simplement pas
ici**. C'est un acquis **négatif net** : l'anomalie ne peut pas fixer `C_T` en `d=3`.
`[établi — négatif net]`

**(c) Unitarité — ne borne que le signe, et tombe en dS/CFT.** Dans une CFT *unitaire*,
l'unitarité impose `C_T>0` (et des bornes de type collisionneur conforme), mais **ne fixe pas la
valeur** — elle contraint un signe, pas un nombre. Pis : en **dS/CFT**, la CFT céleste est
**euclidienne non-unitaire** (`HOLOGRAPHIE-G3 §3`) ⟹ même cette contrainte de positivité **tombe**
(sous continuation `ℓ_{AdS}→iℓ_{dS}`, `C_T` peut devenir **imaginaire/négatif** — réalisé dès
`d=2` : `c~iℓ_dS/G`, Strominger). `[établi — négatif + caveat dS]`

**(d) Dualité holographique — le seul mécanisme qui DÉTERMINE `C_T`.** Si la CFT céleste est
duale à la **gravité de fond** (A)dS, alors le tenseur de stress holographique
`⟨T⟩=(d/16πG)g_{(d)}` (dictionnaire FG, `HOLOGRAPHIE-G3 §1`) **normalise** `C_T` par la donnée
gravitationnelle du bulk :

$$\boxed{\;C_T \;=\; (\text{coeff})\;\frac{\ell^{\,d-1}}{G_N}
\;\overset{d=3}{\sim}\;\Big(\frac{\ell_{dS}}{\ell_P}\Big)^{2}\;\sim\; N=S_{dS}.\;}$$

C'est la **même relation** (`entropie / charge centrale ~ ℓ^{d-1}/G`) qui *définit* `N` dans
`LC-E`. `[formalisable` (scaling standard) → `à inventer` (coefficient exact en dS)`]`

**Conclusion du tri.** Trois mécanismes sur quatre échouent — dont deux comme `établi` négatif,
l'anomalie **décisivement** (indisponible en `d=3`). Le seul qui détermine `C_T` est
l'**holographique**, et il le fait **en le verrouillant à `N`** :

$$\boxed{\;C_T \text{ n'est PAS un paramètre libre indépendant : il est holographiquement
verrouillé à } N \text{ — même mécanisme déterminant que } N \text{ lui-même.}\;}$$

C'est le **raffinement réel** par rapport à D-ii : `A_T~1/C_T~1/N` n'était posé que comme *scaling
dimensionnel* ; le tri montre que ce lien repose sur le **mécanisme déterminant** (la relation
`ℓ^{d-1}/G`), donc que `C_T` **n'ajoute aucune inconnue indépendante** — il *est* le compte `N`,
vu côté CFT. Le « troisième objet sur `N` » (l'amplitude `A_T`, via `C_T`) est ainsi confirmé
**structurellement**, pas par coïncidence numérique.

<svg width="100%" viewBox="0 0 680 340" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Tri des quatre mécanismes susceptibles de fixer la charge centrale C_T en d=3</title>
  <desc>La forme du deux-point du tenseur de stress (proportionnelle à k cube, Delta egal d egal 3) est scellée ; reste la normalisation C_T. Quatre mécanismes sont testés. La normalisation par la conformité seule ne fixe que la forme, laissant C_T libre. L'anomalie conforme est indisponible en dimension 3 impaire (pas d'anomalie de trace) : acquis négatif net. L'unitarité ne borne que le signe C_T positif, pas la valeur, et tombe en dS sur CFT non unitaire. Seule la dualité holographique détermine C_T, par la relation C_T proportionnel à ell puissance d moins un sur G, c'est-à-dire C_T de l'ordre de N, l'entropie de de Sitter. Donc C_T est verrouillé à N et n'ajoute aucune inconnue indépendante.</desc>
  <rect x="40" y="20" width="600" height="40" rx="9" fill="#EEEAF8" stroke="#534AB7" stroke-width="0.7"/>
  <text x="340" y="38" text-anchor="middle" font-size="12.5" font-weight="500" fill="#3C3489">⟨TT⟩ ∝ k³  (Δ=d=3) — FORME `établie` (sceau SPECTRE-K3)</text>
  <text x="340" y="54" text-anchor="middle" font-size="11" fill="#73726c">reste un seul scalaire : la NORMALISATION C_T  =  toute la liberté résiduelle de D1 (gaussien)</text>
  <rect x="40" y="80" width="290" height="56" rx="9" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="185" y="101" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">(a) normalisation conforme</text>
  <text x="185" y="121" text-anchor="middle" font-size="11" fill="#3d3d3a">fixe la forme, PAS C_T → C_T libre</text>
  <rect x="350" y="80" width="290" height="56" rx="9" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="495" y="101" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">(b) anomalie conforme</text>
  <text x="495" y="121" text-anchor="middle" font-size="11" fill="#3d3d3a">INDISPONIBLE (d=3 impair) — négatif net</text>
  <rect x="40" y="146" width="290" height="56" rx="9" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="185" y="167" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">(c) unitarité</text>
  <text x="185" y="187" text-anchor="middle" font-size="11" fill="#3d3d3a">borne le signe, pas la valeur ; tombe en dS</text>
  <rect x="350" y="146" width="290" height="56" rx="9" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.9"/>
  <text x="495" y="167" text-anchor="middle" font-size="12" font-weight="500" fill="#0F6E56">(d) dualité holographique ✓</text>
  <text x="495" y="187" text-anchor="middle" font-size="11" fill="#0F6E56">C_T = (coeff) ℓ^{d-1}/G ∼ N</text>
  <rect x="120" y="222" width="440" height="48" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.9"/>
  <text x="340" y="243" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">C_T VERROUILLÉE à N (même mécanisme déterminant que N)</text>
  <text x="340" y="261" text-anchor="middle" font-size="11" fill="#0F6E56">⟹ aucune inconnue indépendante : C_T = le compte N, côté CFT</text>
  <text x="340" y="294" text-anchor="middle" font-size="11.5" fill="#A32D2D">D1 NON clos : circularité LC-E intacte · C_T en dS imaginaire/négatif (`à inventer`) · CFT de raccordement non construite</text>
  <text x="340" y="316" text-anchor="middle" font-size="11" fill="#73726c">finding §3 : A_T·N = nombre pur (cancellation H,G) = 16 (convention standard) ⟹ candidat-égalité, coefficient `formalisable`</text>
</svg>

---

## 3. Le *finding* — le coefficient n'est pas `à inventer` de zéro `[calculé ; candidat-égalité]`

Le produit `A_T·N` est plus parlant que chaque facteur, car il **élimine** la dépendance en
`{H,G}`. Avec la normalisation standard du **spectre tensoriel de Bunch–Davies** (QFT-sur-dS,
l'état déjà en jeu) et l'**entropie de Gibbons–Hawking** :

$$A_T=\mathcal P_h=\frac{2}{\pi^2}\Big(\frac{H}{M_{\rm Pl}}\Big)^2=\frac{16\,G H^2}{\pi}
\quad(M_{\rm Pl}^2=(8\pi G)^{-1}),\qquad
N=S_{dS}=\frac{\rm Aire}{4G}=\frac{\pi}{G H^2},$$

$$\boxed{\;A_T\cdot N \;=\; 16\quad\text{(nombre pur — } H \text{ et } G \text{ se simplifient).}\;}$$

*Vérification (symbolique, sympy ; cancellation explicite).* `A_T=16GH²/π`, `N=π/(GH²)`,
`A_T·N=16`, `free_symbols(A_T·N)=∅`. En convention « lâche » (`M_P²=1/G`, `A_T≡(H/M_P)²` sans
préfacteur) on obtient `A_T·N=π` — **le coefficient dépend de la convention, mais la cancellation
`H,G` n'en dépend pas** (c'est structurel : `A_T` et `N` sont deux monômes `GH²` à puissances
opposées).

**Conséquence épistémique — scission propre du « coefficient `à inventer` » de D-ii.**

| Sous-question | Statut |
|---|---|
| coefficient de `A_T` en `(H/M_P)²` | **`établi`** (spectre tensoriel BD, QFT-sur-dS standard) |
| coefficient de `C_T` en `ℓ^{d-1}/G` **en dS** | `formalisable` (scaling) → `à inventer` (valeur exacte, continuation `ℓ_{AdS}→iℓ_{dS}`) |
| **`A_T·N` lui-même** | **`formalisable` et calculable** (`=16` convention standard) — **pas** `à inventer` de zéro |
| **survie de la relation au crossover** (dS/CFT-CCC) | **`à inventer`** (transposition, `HOLOGRAPHIE-G3 §3`) |

**Promotion de D-ii `[décision opérateur, option 1]`.** Le lien `A_T~1/C_T~1/N`, posé en
`scaling` par la passerelle, est **promu** au rang de **candidat-égalité à coefficient
`formalisable`/calculable** :

$$A_T = \frac{16}{N}\quad[\text{convention standard ; candidat-égalité, non scellé}],
\qquad\text{robuste : } A_T\cdot N=O(1)\ \text{pur}.$$

*Caveats à ne pas perdre* : (i) le **16** est convention-dépendant (la cancellation, non) ; (ii)
la relation suppose que le **spectre BD standard + l'entropie GH** s'appliquent au **crossover**
de la CCC (où la « phase inflationnaire » est la fin dS du vieil éon) — c'est précisément la
transposition `à inventer` ; (iii) ce n'est **pas** un sceau (paper-first, CT-i).

---

## 4. Les obstructions qui empêchent toujours de fermer D1 `[inchangées]`

Trois, à ne pas surclasser :

1. **Circularité LC-E intacte.** `C_T~N=S_dS=(ℓ_dS/ℓ_P)²` **présuppose `ℓ_P`**
   (`PLANCK-RESIDUEL §3`). Verrouiller `A_T` à `C_T` (et le coefficient `=16`) **ne fixe ni l'un
   ni l'autre** : ça les tient ensemble. « Qu'est-ce qui fixe `N` ? » reste la question dure et
   l'effet de levier maximal (un compte, désormais **trois** résidus : `ℓ_P`, `A_T`, cutoff de
   variance). `[décision ouverte]`
2. **Non-unitarité dS/CFT.** Sous continuation, `C_T` devient **imaginaire/négatif** (déjà en
   `d=2`). « `C_T` déterminé » ne signifie **pas** « `C_T` est une charge centrale unitaire
   propre » : sa réalité/son signe sont gouvernés par la continuation dS. `[à inventer]`
3. **CFT de raccordement non construite.** `𝒞` recolle **deux éons**, pas un bord asymptotique
   unique (`HOLOGRAPHIE-G3 §3`). La dualité holographique invoquée en §2(d) vaut pour un bord dS ;
   sa version « raccordement » reste à bâtir. `[à inventer]`

---

## 5. Critère de réfutation `[falsifiabilité]`

Le candidat « `C_T` verrouillé à `N` / `A_T=16/N` » **casserait** si l'on exhibait :

- un **principe fixant `A_T` indépendamment** de la donnée holographique de bulk (`N`/`C_T`) —
  alors `A_T` et `N` redeviendraient indépendants et le verrouillage tomberait (la réduction
  « résidu = `A_T` » du §1 **resterait** acquise, `A_T` simplement libre) ; **ou**
- une CFT céleste de raccordement **sans `C_T` bien défini** (non-unitarité plus sévère qu'un
  signe : pas de normalisation du deux-point) — alors le mécanisme (d) échoue.

**Test de cohérence positif `[la cible d'un futur sceau dS/CFT]`.** Un vrai sceau dS/CFT devrait
**reproduire** `A_T·N=O(1)` (idéalement le `16` standard, ou sa version continuée correcte). Un
désaccord exposerait précisément le **fossé dS/CFT ↔ inflation** au crossover — résultat utile
dans les deux sens. **Statut** : aucun contre-exemple connu ; le scaling `C_T~N~(ℓ_dS/ℓ_P)²` est
standard ; la part non établie est isolée dans (i) la valeur exacte/réalité de `C_T` en dS et
(ii) la circularité LC-E.

---

## 6. Ce que ce cadrage FAIT vs NE FAIT PAS `[honnêteté §6.4]`

**FAIT.** (i) **Sépare** la forme (`établie`, sceau) de la normalisation `C_T` (le seul résidu
gaussien). (ii) **Trie** les quatre mécanismes : anomalie **indisponible** (`d=3`, `établi`
négatif net), unitarité **borne le signe seulement** (et tombe en dS), normalisation conforme
**fixe la forme seulement**, **holographie** détermine `C_T` **en le verrouillant à `N`**. (iii)
**Établit** que `C_T` n'ajoute **aucune inconnue indépendante** (même mécanisme déterminant que
`N`). (iv) **Calcule** `A_T·N` = nombre pur (`=16` standard) et **promeut** D-ii (scaling →
candidat-égalité à coefficient `formalisable`).

**NE FAIT PAS.** (i) Ne **ferme pas** D1 : `A_T` (et `N`) **non fixés** — circularité LC-E
intacte. (ii) Ne **scelle rien** (paper-first, CT-i ; le `16` est une vérif symbolique légère,
pas un `verif_*.py`). (iii) N'établit **pas** la valeur exacte/réalité de `C_T` en dS
(`à inventer` : non-unitarité, continuation). (iv) N'établit **pas** que la relation
inflationnaire standard **survit** à la transposition dS/CFT-au-crossover (`à inventer`). (v) Ne
construit **pas** la CFT de raccordement. (vi) Ne touche **aucune** algèbre ni aucun chaînon ;
« le bang gagne » (P6 B) intact ; A3/A4, C7/A2★ inchangés ; **(A) physique conditionnel au seul
A2★ INCHANGÉ**. **Réduction d'hypothèse ≠ démonstration de la CCC.**

---

## 7. Propagation suggérée `[NON exécutée — à valider/déposer séparément]`

Si le cadrage est validé, propagation **additive** (jamais réécriture d'historique) :
- `LC-D-HOLOGRAPHIE-G3 §5` : noter que `C_T` est **holographiquement verrouillée à `N`** (seul
  mécanisme déterminant ; anomalie indisponible en `d=3`), donc n'ajoute pas d'inconnue ; renvoi
  au candidat-égalité `A_T=16/N` (convention standard).
- `LC-D3-SPECTRE-K3` (renvoi) : l'amplitude `A_T` — `décision ouverte` là-bas — est candidate à
  `A_T=16/N` (coefficient `formalisable`, non scellé), cohérent avec le cutoff `√(N/π)`.
- `LC-E-PLANCK-RESIDUEL §3` : préciser que le rattachement `A_T~1/N` est promu candidat-égalité
  (`A_T·N=O(1)` pur, `=16` standard) ; circularité **non aggravée** (un compte `N`, le coefficient
  ne le fixe pas).
- `LC-WORK-D1-E-AMPLITUDE` (renvoi) : D-ii **promu** (scaling → candidat-égalité), via ce cadrage.
- `LC-AUDIT-VERDICT §8bis` : bullet daté « cadrage `C_T` : déterminée par holographie (verrouillée
  à `N`), non libre ; anomalie indisponible (`d=3`) ; `A_T·N=O(1)` pur (`=16` std), candidat-égalité ;
  D1 non clos ; valeur de `C_T` en dS + transposition `à inventer` ».
- `00-INDEX` (carte + changelog) ; `03-GLOSSAIRE` (entrées « charge centrale céleste `C_T`
  (verrouillée à `N`) » et « candidat-égalité `A_T=16/N` ») ; `02-PROGRAMME`, `04-REFERENCES`
  (réfs déjà en KB : Strominger 2001, Maldacena 2003, dHSS 2001, Gibbons–Hawking 1977 ; +
  normalisation `C_T` holographique — réf. à confirmer).
- **Sceau optionnel — `[à inventer, NON inclus]`** : un sceau de normalisation dS/CFT calculant
  la **valeur/réalité** de `C_T` continuée et **testant `A_T·N=16`** ; hors périmètre (CT-i),
  étape ultérieure si priorisée.

---

## 8. Renvois & glossaire

**Renvois.** `LC-D-CT-ATN` (le **sceau** de ce cadrage : candidat-égalité `A_T=16/N` confirmé
par deux routes, verrouillage `C_T∝N` — `verif_D_CT_ATN.py`) ; `LC-WORK-D1-E-AMPLITUDE` (passerelle D1⟷E ; D-ii — le parent direct, dont ce
cadrage instruit le coefficient) ; `LC-D-HOLOGRAPHIE-G3` (dictionnaire `g₃=⟨T⟩`, `d=3` impair,
dS/CFT, `C_T` charge centrale céleste) ; `LC-D3-SPECTRE-K3` (forme `∝k³` scellée, cutoff `√(N/π)`,
amplitude `A_T` ouverte) ; `LC-D3-WEYL-BUNCHDAVIES` (relation d'état BD, caveat non-linéaire) ;
`LC-E-PLANCK-RESIDUEL` (`N=S_dS`, circularité — l'obstruction centrale) ; `LC-A-D1-FACTEUR-CONFORME`
(verrou D1) ; `LC-WORK-A3-D1-PASSERELLE` (un-point `⟨g₃⟩=0`) ; `LC-AUDIT-VERDICT §6.4` (discipline).

**Glossaire à ajouter (`LC-03`).**
- *Charge centrale céleste `C_T` (verrouillée à `N`)* : en dS/CFT (`d=3`), `C_T` n'est fixée ni
  par la conformité (forme seule), ni par l'anomalie (indisponible, `d` impair), ni par
  l'unitarité (signe seul, tombe en dS) — seulement par l'**holographie** : `C_T~ℓ^{d-1}/G~N`.
  N'ajoute donc aucune inconnue indépendante.
- *Candidat-égalité `A_T=16/N`* : `A_T·N` est un nombre pur (cancellation `H,G`) ; en convention
  standard (spectre tensoriel BD + entropie GH) `=16`. Promotion de D-ii (scaling →
  coefficient `formalisable`/calculable) ; non scellé ; transposition dS/CFT-au-crossover `à inventer`.

---

## Appendice — tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`). Ici : forme `⟨TT⟩∝k³` `établie (sceau)` ; tri des mécanismes `établi`
(dont anomalie indisponible, négatif net) ; verrouillage holographique `C_T~N` `formalisable` ;
`A_T·N=O(1)` pur `formalisable`/calculable (`=16` std) — candidat-égalité ; valeur/réalité de
`C_T` en dS + survie au crossover `à inventer` ; circularité LC-E `décision ouverte` (non brisée) ;
D1 non clos.
