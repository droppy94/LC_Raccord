---
id: LC-D-HOLOGRAPHIE-G3
titre: "Module D — ouverture : la donnée g₃ à 𝓘⁺ comme tenseur de stress holographique"
codename: LC-RACCORD
tags: [module-D, holographie, ds-cft, fefferman-graham, g3, stress-tensor, celeste, D1, bunch-davies]
type: chaînon (ouverture du module D ; point de convergence D1 + Planck)
statut: pont holographique établi (FG) / transposition dS-CFT à la CCC à inventer / sélection de l'état décision ouverte
version: 0.4
langue: fr
date: 2026-06-07
maj: "2026-06-09 — v0.4 : §3 — dualité graviton-dual de de Haro comme LEAD DE STRUCTURE pour la CFT de raccordement (propagation de LC-D-CT-DUAL v0.1, verif_D_CT_dual.py EXIT 0, étage S1/AdS). La CFT duale (Neumann/graviton-dual, dont le tenseur de stress EST le Cotton de la CFT Dirichlet) est un candidat naturel à tester en S2 (continuation dS) ; garde-fou S1 : la dualité AdS ne flippe pas C_T (W̃=−W mais C̃_T=+C_T) ⟹ le signe négatif vient de la continuation dS et/ou de S²=−1. Aucune touche algèbre. | 2026-06-09 — v0.3 : §3 — précision non-unitarité dS/CFT (propagation de LC-D-CT-REALITE v0.1, verif_D_CT_realite.py EXIT 0). « charge centrale parfois imaginaire » est le cas d=2 (c∝ℓ¹) ; en d=3 (C_T∝ℓ²) la continuation ℓ_AdS→iℓ_dS donne i²=−1 ⟹ C_T RÉEL NÉGATIF (parité de la puissance de ℓ). La réalité de C_T se rabat sur l'item « CFT de raccordement » de §3 (consolidation) ; report d'erreur NUL vers l'observable (les établi amont robustes). Aucune touche algèbre. | 2026-06-09 — v0.2 : §5 — propagation de la passerelle D1⟷E (LC-WORK-D1-E-AMPLITUDE v0.1, paper-first). Ajout : après la passerelle A3⟷D1 (un-point ⟨g₃⟩=0 absorbé dans A4) et SPECTRE-K3 (forme du deux-point ⟨g₃g₃⟩∝k³ scellée), le résidu libre de D1 = g₃=⟨T⟩ se réduit, au niveau gaussien, à UN SEUL nombre, l'amplitude A_T~(H/M_P)² ; candidat de fermeture A_T~1/C_T~1/N (charge centrale céleste C_T~N=S_dS, scaling) ⟹ le résidu de D1 retombe sur le compte N de [E]. SANS SURCLASSEMENT : forme k³ établie (sceau), lien amplitude↔N formalisable→à inventer, circularité LC-E intacte, D1 non clos. Aucune touche algèbre. | v0.1 : ouverture du module D (dictionnaire FG g₃=⟨T⟩ ; reformulation de D1 ; candidat Bunch-Davies)."
statut_id: provisoire — à enregistrer si validé
fichier_compagnon: verif_D_g3.py
renvois: [LC-A-SURVIE-CONFORME, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-E-PLANCK-RESIDUEL, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] holographie / métrique émergente — objet du chaînon"
  - "[A]/D1 facteur conforme — g₀ (source) = liberté D1 ; g₃ (VEV) = la marée à fixer"
  - "[E] retour de l'échelle — N holographique pointait déjà ici"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D — La donnée `g₃` à `𝓘⁺` comme tenseur de stress holographique

> **Pourquoi ce chaînon ouvre [D].** Deux investigations indépendantes y mènent : le
> candidat #5 de D1 (`LC-A-D1-STABILITE-WEYL`) a montré que la fermeture de D1 doit
> venir de la **marée** `g₍₃₎` (secteur inhomogène, domaine de Weyl/D3), pas du fond ;
> et la note Planck (`LC-E-PLANCK-RESIDUEL`) a montré que le compte qui fixerait
> l'échelle est **holographique** (aire d'horizon), pas sériel. Les deux pointent vers
> le même objet : **la donnée holographique à `𝓘⁺`**. C'est le module [D].
>
> **Acquis (calculé + sourcé).** Le dictionnaire de Fefferman–Graham identifie
> **exactement** la donnée de Friedrich `(g₍₀₎, g₍₃₎)` de `LC-A` à la structure
> holographique : `g₍₀₎` = métrique de bord (**source**, = la liberté conforme de D1) ;
> `g₍₃₎` = **valeur moyenne du tenseur de stress** `⟨T_ij⟩` de la CFT céleste (donnée
> **libre**, 2 polarisations TT, = le Weyl rescalé). `[établi pour AdS ; transposé à
> dS via dS/CFT — formalisable → à inventer]`
>
> **Reformulation de D1 (le gain conceptuel).** Fixer `g₍₃₎` = **choisir l'état de la
> CFT céleste**. La sous-détermination de D1 *est* la liberté de l'état quantique du
> bord. Candidat-sélecteur naturel — agissant enfin sur le **bon** degré de liberté
> (`g₃`, la marée, pas le fond) : l'**état dS-invariant** (Bunch–Davies /
> Hartle–Hawking), qui donnerait un `g₃` unique. `[décision ouverte / à inventer]`

---

## 0. Rôle et garde-fou

Ce chaînon **ouvre** [D] ; il ne le ferme pas. Ce qui est `établi` : le dictionnaire
FG (rigoureux côté AdS) et l'identification `g₃ = ⟨T⟩`. Ce qui est `à inventer` : sa
**transposition à dS** (dS/CFT est conjecturale, CFT euclidienne non unitaire) et *a
fortiori* à la CCC. Le candidat « état de Bunch–Davies » est une **piste**, non un
résultat. On ne surclasse rien.

---

## 1. Le dictionnaire de Fefferman–Graham `[établi (AdS), sourcé]`

Près d'un bord conforme, toute métrique d'Einstein s'écrit en jauge FG
(de Haro–Skenderis–Solodukhin, CMP **217**, 595, 2001) :

$$ds^2 = \frac{\ell^2}{z^2}\Big(dz^2 + g_{ij}(z,x)\,dx^i dx^j\Big),\qquad
g(z,x) = g_{(0)} + z^2 g_{(2)} + \dots + z^d g_{(d)} + \dots$$

Structure (bord de dimension `d`) :

- **`g₍₀₎`** = métrique conforme du bord = la **source**.
- **`g₍₂ₙ₎`** (`0<n<d/2`) = tenseurs **locaux** construits à partir de `g₍₀₎` (Schouten,
  etc.) — **déterminés**.
- **`g₍d₎`** = donnée **libre** = la valeur moyenne du tenseur de stress du bord :

$$\boxed{\ \langle T_{ij}\rangle = \frac{d}{16\pi G}\,g_{(d)}\ }\quad(\text{+ anomalie, nulle si } d \text{ impair}).$$

La seule contrainte sur `g₍d₎` (dans l'expansion asymptotique) : **trace** (anomalie
conforme — nulle ici) et **divergence** (conservation / identités de Ward). Le couple
`(g₍₀₎, g₍d₎)` détermine tout le reste — c'est la **donnée de Cauchy holographique**.

**Point crucial `[sourcé]`** : le choix de la coordonnée `z` (donc le représentant
conforme `g₍₀₎`) **n'est pas unique** — c'est la **liberté de jauge conforme**. C'est
*exactement* la liberté de D1 sur `g₍₀₎`. Holographie et D1 parlent du même objet.

---

## 2. Identification à Friedrich, et le sceau `[établi]`

Le bord pertinent est `𝓘⁺` **spacelike** de de Sitter (`LC-A`) : dimension de bord
**`d = 3`** (impair). Compagnon `verif_D_g3.py` :

| sceau | résultat | lecture |
|---|---|---|
| [A] exposants radiaux FG (mode TT, indiciel `r²−dr=0`) | `{0, d} = {0, 3}` | `r=0` : `g₍₀₎` source ; `r=3` : `g₍₃₎` donnée libre |
| [B] comptage TT (`d=3`) | `6 − 1 − 3 = 2` | `g₃` = **2 polarisations** = graviton = Weyl rescalé |
| [C] de Sitter pur (planaire) | `g₍₃₎ = 0` | dS pur = **vide** ; `g₃` mesure l'écart au vide |

Conclusion : la donnée `(g₍₀₎, g₍₃₎)` de Friedrich (`LC-A` §2b) **est** la donnée
holographique FG. `g₍₃₎` (Weyl rescalé TT, 2 composantes, `décision ouverte` dans D1)
= `⟨T_ij⟩` de la CFT céleste. `d = 3` impair ⟹ pas d'anomalie ⟹ `⟨T⟩` traceless et
conservé — un tenseur de stress conforme « propre ».

---

## 3. dS/CFT — le cadre, honnêtement `[formalisable → à inventer]`

Le dictionnaire FG est **établi** pour AdS (`Λ<0`, bord timelike, CFT lorentzienne
unitaire). Ici `Λ>0`, bord `𝓘⁺` **spacelike** : c'est le régime **dS/CFT**
(Strominger 2001 ; Maldacena 2002). La CFT vit sur la **sphère céleste euclidienne**
à `𝓘⁺`, et `g₍₃₎ = ⟨T⟩` y est la valeur moyenne du tenseur de stress dans un **état**
donné. Réserves `[à ne pas perdre]` :

- dS/CFT est **conjecturale** (bien moins établie qu'AdS/CFT) : CFT **euclidienne, non
  unitaire**, charge centrale parfois imaginaire, dictionnaire des poids subtil.
- Sa **transposition à la CCC** (où `𝒞` recolle deux éons, pas un seul bord
  asymptotique) est `à inventer` : il faut une CFT de *raccordement*, pas seulement
  de bord.
- **Précision (`LC-D-CT-REALITE`, sceau `verif_D_CT_realite.py`)** : « charge centrale parfois
  imaginaire » est le cas `d=2` (`c∝ℓ¹`) ; en `d=3` (`C_T∝ℓ²`), la continuation `ℓ_AdS→iℓ_dS`
  donne `i²=−1` ⟹ `C_T` **réel négatif** (parité de la puissance de `ℓ`). Trancher si ce `C_T<0`
  obstrue le raccordement **revient** à construire/exclure la CFT de raccordement ci-dessus
  (consolidation) ; l'observable est insensible au signe (report d'erreur nul).

**Lead de structure — dualité graviton-dual (S1, `LC-D-CT-DUAL`).** La dualité graviton-dual de de Haro (arXiv:0808.2054) fait de la **CFT duale** (Neumann / graviton-dual, dont le tenseur de stress **est** le Cotton de la CFT Dirichlet) un **candidat naturel** pour cette CFT de raccordement. Étage S1 (AdS) scellé : `S²=−1` (vp `±i`) ; **garde-fou** — la dualité AdS **ne flippe pas** `C_T` (`W̃=−W` mais `C̃_T=+C_T`) ⟹ le signe négatif de `C_T` vient de la continuation dS (`i^{d-1}`) et/ou de `S²=−1`, à tester en S2 (continuation dS).

Mais — et c'est l'intérêt — c'est le **bon cadre** : il agit sur `g₃` (la marée), le
degré de liberté que stabilité (fond) et Planck (échelle) ne touchaient pas.

---

## 4. La reformulation de D1, et un candidat enfin bien placé

Le dictionnaire transforme l'énoncé de D1 :

$$\underbrace{\text{« quelle prescription fixe le facteur conforme ? »}}_{\text{D1, géométrique}}
\;\Longleftrightarrow\;
\underbrace{\text{« quel état fixe } \langle T\rangle = g_{(3)} \text{ ? »}}_{\text{D, holographique}}$$

- `g₍₀₎` (la liberté conforme de D1) = **jauge** = choix de représentant / cadre.
- `g₍₃₎` (la donnée dynamique non fixée) = **état** = `⟨T⟩` de la CFT céleste.

**Candidat-sélecteur (le bon secteur, enfin).** Dans une théorie sur dS, il existe un
état **privilégié** : le vide **de Bunch–Davies** (= Hartle–Hawking euclidien),
l'unique état dS-invariant régulier. S'il existe une CFT céleste de raccordement, son
état de Bunch–Davies fournirait un `⟨T⟩` — donc un `g₍₃₎` — **unique**. Contrairement
aux candidats #5 (stabilité, secteur de fond) et Planck (échelle), celui-ci agit sur
`g₃` lui-même. C'est le candidat le plus principiel à ce jour pour fermer D1.

> **Statut honnête.** `décision ouverte / à inventer`. Existence et unicité d'une CFT
> céleste de raccordement non établies ; le vide de Bunch–Davies au crossover (où deux
> éons se recollent) n'est pas construit ; et la non-unitarité de dS/CFT pourrait
> obstruer l'unicité. Mais la **cible** est juste, et c'est un progrès : on a déplacé
> D1 d'un choix géométrique opaque vers un choix d'**état quantique**, où la physique
> connaît des principes de sélection (vide invariant).

<svg width="100%" viewBox="0 0 660 290" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Dictionnaire holographique à 𝓘⁺ : g₀ = jauge/source, g₃ = état/⟨T⟩</title>
  <desc>Le bord 𝓘⁺ spacelike de de Sitter (dimension 3) porte une CFT céleste euclidienne. La donnée de Friedrich (g0, g3) s'identifie à la donnée holographique : g0 est la métrique de bord, source, qui correspond à la liberté de jauge conforme de D1 ; g3 est la valeur moyenne du tenseur de stress, donnée libre à 2 polarisations, le Weyl rescalé, fixée par le choix de l'état de la CFT. Reformulation de D1 : choisir g3 revient à choisir l'état, et le candidat est l'état de Bunch-Davies dS-invariant.</desc>
  <line x1="60" y1="70" x2="600" y2="70" stroke="#534AB7" stroke-width="2.5"/>
  <text x="330" y="56" text-anchor="middle" font-size="13" font-weight="500" fill="#3C3489">𝓘⁺ spacelike (bord d=3) — CFT céleste euclidienne</text>
  <rect x="70" y="92" width="240" height="92" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="190" y="116" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">g₍₀₎ — SOURCE</text>
  <text x="190" y="138" text-anchor="middle" font-size="11.5" fill="#3d3d3a">métrique de bord / exposant 0</text>
  <text x="190" y="158" text-anchor="middle" font-size="11.5" fill="#0F6E56">= jauge conforme</text>
  <text x="190" y="176" text-anchor="middle" font-size="11.5" fill="#0F6E56">= liberté D1 sur g₀</text>
  <rect x="350" y="92" width="240" height="92" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="470" y="116" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">g₍₃₎ — VEV ⟨T_ij⟩</text>
  <text x="470" y="138" text-anchor="middle" font-size="11.5" fill="#3d3d3a">libre / exposant 3 / 2 polar.</text>
  <text x="470" y="158" text-anchor="middle" font-size="11.5" fill="#993C1D">= Weyl rescalé (la marée)</text>
  <text x="470" y="176" text-anchor="middle" font-size="11.5" fill="#993C1D">= état de la CFT</text>
  <text x="330" y="214" text-anchor="middle" font-size="12" fill="#3C3489">⟨T_ij⟩ = (d/16πG) g₍₃₎   —   D1 ⟺ « quel état fixe ⟨T⟩ ? »</text>
  <text x="330" y="240" text-anchor="middle" font-size="12" font-weight="500" fill="#A32D2D">candidat : état de Bunch–Davies (dS-invariant) → g₃ unique</text>
  <text x="330" y="262" text-anchor="middle" font-size="11" fill="#73726c">agit sur la marée g₃ (bon secteur) — vs stabilité (fond) / Planck (échelle)</text>
</svg>

---

## 5. Conséquences pour le programme

- **D1 reçoit sa formulation la plus nette** : non plus « quelle prescription
  géométrique ? » mais « quel **état** de la CFT céleste ? ». Le degré de liberté
  est nommé (`⟨T⟩`), et le secteur est le bon (marée `g₃`).
- **[E] et [D] se rejoignent** : le compte holographique `N` (note Planck) et la donnée
  `g₃` vivent sur le **même bord** `𝓘⁺`. `N` ~ entropie d'horizon, `g₃` ~ stress de la
  CFT : deux facettes de la même CFT céleste.
- **Pont vers D3 (Weyl)** : `g₃` *est* le Weyl rescalé. L'hypothèse de Weyl (`C→0` au
  crossover) devient une **condition sur l'état** : « état de stress nul / minimal au
  Big Bang ». Bunch–Davies (vide) réalise `⟨T⟩` minimal — **D3 et le candidat d'état
  pourraient coïncider**. (À tester — c'est la prochaine question dure.)
- **Le résidu de D1 est réduit à une amplitude `[passerelle D1⟷E, 2026-06-09]`.** Après la
  passerelle A3⟷D1 (un-point `⟨g₃⟩=0` absorbé dans A4) et `SPECTRE-K3` (forme du deux-point
  `⟨g₃g₃⟩∝k³`, `Δ=3`, scellée), la liberté de D1 sur `g₃=⟨T⟩` se réduit, **au niveau
  gaussien, à un seul nombre** : l'amplitude `A_T~(H/M_P)²`. Candidat de fermeture via la
  **charge centrale** de la CFT céleste : `A_T ~ 1/C_T ~ 1/N` (scaling `C_T~N=S_dS~(ℓ_dS/ℓ_P)²`)
  — le résidu de D1 **retombe sur le compte `N` de `[E]`**. `[formalisable (scaling) → à inventer
  (coefficient) ; D1 non clos ; voir LC-WORK-D1-E-AMPLITUDE]`

---

## 6. Format de chaînon

- **Hypothèse.** La donnée libre `g₃` de D1 est le tenseur de stress d'une CFT céleste ;
  un état privilégié la fixe.
- **Outil.** Dictionnaire de Fefferman–Graham (FG) ; dS/CFT ; expansion à `𝓘⁺`
  spacelike ; état de Bunch–Davies.
- **Critère de réfutation.** Si l'on montre qu'aucune CFT céleste cohérente n'existe au
  raccordement, ou qu'aucun état n'y fixe `g₃` de façon unique, la route holographique
  de fermeture de D1 échoue (D1 resterait ouvert, à attaquer autrement).
- **Verdict.** Pont FG `g₃=⟨T⟩` **établi** (côté AdS) ; transposition dS/CCC
  `à inventer` ; sélection par l'état `décision ouverte`. **[D] est ouvert sur la bonne
  cible ; le candidat « Bunch–Davies » est le plus principiel rencontré.**

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-A-SURVIE-CONFORME` (donnée `(g₀,g₃)` de Friedrich) ; `LC-A-D1`
(g₃ = donnée libre de D1) ; `LC-A-D1-STABILITE-WEYL` (redirection vers la marée g₃) ;
`LC-E-PLANCK-RESIDUEL` (N holographique, même bord) ; module `[D3]` Weyl (g₃ = Weyl
rescalé).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Dictionnaire de Fefferman–Graham* : `g₍₀₎` source, `g₍d₎=⟨T⟩` VEV libre,
  `⟨T_ij⟩=(d/16πG)g₍d₎`.
- *Tenseur de stress holographique / CFT céleste* : `g₃ = ⟨T⟩` à `𝓘⁺` ; fixer `g₃` =
  choisir l'état.
- *dS/CFT* : holographie à `Λ>0`, CFT euclidienne sur la sphère céleste (conjecturale).
- *État de Bunch–Davies (Hartle–Hawking)* : vide dS-invariant ; candidat-sélecteur de
  D1 agissant sur `g₃`.

**Références (`LC-04`).** de Haro, Skenderis & Solodukhin, *Holographic reconstruction
of spacetime…*, Commun. Math. Phys. **217**, 595 (2001) `[confirmé]` ; Strominger,
*The dS/CFT correspondence*, JHEP (2001) `[à vérifier]` ; Maldacena, *Non-Gaussian
features…* (dS/CFT) (2002) `[à vérifier]` ; Bunch & Davies (1978), vide de Sitter
`[à vérifier]` ; (rappel) Friedrich 1986 (donnée conforme).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
