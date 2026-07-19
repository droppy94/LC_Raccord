---
id: LC-WORK-D1-E-AMPLITUDE
titre: "Module D ⟷ E / passerelle D1⟷E — RÉDUCTION DU RÉSIDU DE D1 À UNE AMPLITUDE (paper-first, AUCUN code neuf). Consigne la réduction DÉJÀ ACQUISE par recombinaison de deux scellés : après la passerelle A3⟷D1 (un-point ⟨g₃⟩=0 absorbé dans A4, LC-WORK-A3-D1-PASSERELLE) et SPECTRE-K3 (forme du deux-point ⟨g₃g₃⟩∝k³, Δ=3, scellée, verif_D3_spectre_k3.py), le résidu libre de D1 — la donnée holographique g₃=⟨T⟩ de la CFT céleste (LC-D-HOLOGRAPHIE-G3) — se réduit, AU NIVEAU DEUX-POINT/GAUSSIEN, à UN SEUL nombre : l'amplitude A_T~(H/M_P)². Pose ensuite le CANDIDAT de fermeture A_T~1/C_T~1/N (charge centrale de la CFT céleste ~ compte holographique N=S_dS de [E]) au niveau SCALING uniquement, et son obstruction (circularité LC-E : N=S_dS présuppose ℓ_P). ⟹ candidat de réduction de comptage D1⟷E : le résidu de D1 n'est PAS indépendant du compte N de [E]. CE QUE CE CADRAGE FAIT : consigne la réduction résidu=A_T (recombinaison de scellés) ; pose le candidat D1⟷E. CE QU'IL NE FAIT PAS : ne ferme PAS D1 (A_T non fixé, circularité LC-E intacte) ; n'établit PAS le coefficient exact (scaling seul) ; ne traite PAS le non-gaussien/non-linéaire (décision ouverte héritée) ; n'établit ni dS/CFT ni la CFT de raccordement (à inventer)."
codename: LC-RACCORD
type: "note de travail / cadrage papier (paper-first) — passerelle inter-modules D1⟷E. Subordonnée à LC-AUDIT-VERDICT §6.4. Étage cartographie (LC-07-like), non fermeture (LC-10-like). Successeur logique de LC-WORK-A3-D1-PASSERELLE (suite §4 de la reprise : pivot [D])."
version: 0.3
langue: fr
date: 2026-06-09
maj: "2026-06-12 — v0.3 : renvoi (lot de propagation NONLIN-2PT) — LC-D-NONLIN-2PT v0.1 (sceau verif_nonlin_deuxpoint.py EXIT 0/41 ; audité à froid 4/4 ACQUIS, LC-AUDIT-LOG-NONLIN-2PT v0.1) : la réduction « résidu gaussien de D1 = UNE amplitude A_T » est RELEVÉE NON-PERTURBATIVEMENT — la forme du deux-point passe de établi (sceau) perturbatif TT (relation d'état BD) à établi PAR INVARIANCE (représentation, secteur de Weyl complet, deux parités ; pair : dimension 1, k³·Π^TT forcée ; impair : dimension 1 ET contact). Le caveat non-linéaire de la forme est levé ; les corrélateurs >2-pt restent décision ouverte. Note datée au §3 + renvoi au §7, additifs. Lignes amplitude/unicité INCHANGÉES ; D1 non clos ; circularité LC-E intacte ; compte {A4 ; A2★ ; N} inchangé. Aucune touche algèbre ni sceaux. | 2026-06-09 — v0.2 : renvoi — le candidat D1⟷E posé ici en `scaling` (D-ii) a été promu candidat-égalité par le cadrage LC-WORK-CT-CADRAGE puis SCELLÉ (algèbre) par LC-D-CT-ATN v0.1 (verif_D_CT_ATN.py, EXIT 0) : A_T·N=16 (deux routes convergentes, nombre pur), verrouillage C_T/N=1/(32π²). Chaîne D-ii : `scaling` → candidat-égalité (cadrage) → scellé (sceau). Le `à inventer` (valeur/réalité de C_T en dS, survie au crossover, fixation de N) et la non-fermeture de D1 sont inchangés. Aucune touche à l'algèbre. | 2026-06-09 — v0.1 : cadrage initial. (1) Consigne la réduction DÉJÀ ACQUISE « résidu de D1 = un seul nombre A_T » au niveau deux-point/gaussien — pure recombinaison de deux scellés (LC-WORK-A3-D1-PASSERELLE : ⟨g₃⟩=0 ; LC-D3-SPECTRE-K3 : ⟨g₃g₃⟩∝k³, forme scellée), via le dictionnaire g₃=⟨T⟩ de LC-D-HOLOGRAPHIE-G3 (g₀=jauge, g₃=état/VEV). AUCUNE algèbre neuve. (2) Pose le candidat de fermeture A_T~1/C_T~1/N (C_T charge centrale de la CFT céleste ~ N=S_dS de [E], scaling (ℓ_dS/ℓ_P)²) — au niveau SCALING uniquement (décision opérateur D-ii), coefficient exact NON tenté. (3) Identifie la cible : candidat de réduction de comptage D1⟷E (le résidu de D1 = le compte N de [E], non indépendant). SANS SURCLASSEMENT (§6.4) : la forme k³ est `établie (sceau)` ; le lien amplitude↔C_T↔N est `formalisable`→`à inventer` ; la circularité LC-E reste `décision ouverte` (non brisée) ; le non-gaussien/non-linéaire reste `décision ouverte` (hérité). NE ferme PAS D1. AUCUN sceau, AUCUNE touche aux chaînons existants. Propagation §6 NON exécutée (proposée, à valider/déposer séparément)."
statut: "RÉDUCTION CONSIGNÉE (résidu deux-point de D1 = amplitude A_T unique, par recombinaison de scellés). CANDIDAT D1⟷E cartographié (A_T~1/C_T~1/N, scaling) — non établi (coefficient exact à inventer ; circularité LC-E intacte). D1 NON clos. Non-gaussien/non-linéaire décision ouverte (hérité). CCC non démontrée."
prerequis_kb: [LC-WORK-A3-D1-PASSERELLE, LC-D3-SPECTRE-K3, LC-D-HOLOGRAPHIE-G3, LC-D3-WEYL-BUNCHDAVIES, LC-E-PLANCK-RESIDUEL, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX, 02_programme-de-recherche, 03_glossaire]
fichiers_compagnons_kb: []   # paper-first — AUCUN sceau neuf ; s'appuie sur les scellés existants verif_D3_spectre_k3.py, verif_D_g3.py, verif_D3_bunchdavies.py
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
renvois: [LC-WORK-A3-D1-PASSERELLE, LC-D3-SPECTRE-K3, LC-D-HOLOGRAPHIE-G3, LC-D3-WEYL-BUNCHDAVIES, LC-E-PLANCK-RESIDUEL, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-AUDIT-VERDICT, LC-00-INDEX]
---

# LC-WORK · Passerelle D1 ⟷ E — réduction du résidu de D1 à une amplitude

> **Question.** Après la passerelle A3⟷D1 et SPECTRE-K3, que reste-t-il de libre dans D1
> (verrou du module A : unicité du facteur conforme) ? Et cette liberté résiduelle est-elle
> **indépendante** du compte holographique `N` de `[E]`, ou contrainte par lui ? Si lié, le
> **compte de postulats irréductibles baisse encore** — critère central.
>
> **Verdict cartographié.** **(1) Réduction acquise.** Le dictionnaire `g₃=⟨T⟩`
> (`LC-D-HOLOGRAPHIE-G3`) fait de `g₀` la **jauge** (que D1 ne fixe pas) et de `g₃` l'**état**
> de la CFT céleste = la liberté de D1. La passerelle A3⟷D1 fixe le **un-point** (`⟨g₃⟩=0`) ;
> `SPECTRE-K3` scelle la **forme** du deux-point (`⟨g₃g₃⟩∝k³`, `Δ=3`). Il ne reste donc, **au
> niveau deux-point/gaussien**, qu'**un seul nombre** : l'amplitude `A_T~(H/M_P)²`. **(2)
> Candidat de fermeture.** En dS/CFT, `A_T ~ 1/C_T ~ 1/N` (`C_T` charge centrale de la CFT
> céleste `~ N=S_dS`, scaling `(ℓ_dS/ℓ_P)²`). **⟹ le résidu de D1 retombe sur le compte `N` de
> `[E]`** : candidat de réduction `D1⟷E`. **Réduction d'hypothèse, pas fermeture de D1** (le
> coefficient exact est `à inventer` ; la circularité LC-E reste `décision ouverte`).

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce document est un **cadrage** (étage `LC-07`-like), au même titre que `LC-WORK-A3-D1-PASSERELLE`
(pour A3/D1) et `LC-WORK-A2-CONJECTURE` (pour C7-b/A2). Il **consigne** une réduction déjà
acquise et **isole** une dépendance entre modules ; il **ne ferme pas** D1 et ne lève rien.
Présenter « D1 fermé » ou « `A_T` fixé » comme acquis serait une surinterprétation du type corrigé
en `LC-05` v0.2→v0.3. La forme `⟨g₃g₃⟩∝k³` est un `établi (sceau)` (`verif_D3_spectre_k3.py`) ;
le lien `A_T ↔ C_T ↔ N` est `formalisable` (scaling) → `à inventer` (coefficient, normalisation
dS/CFT au raccordement) ; la circularité de `LC-E` (`N=S_dS` présuppose `ℓ_P`) n'est **pas brisée**.

**Choix de périmètre verrouillés (opérateur, 2026-06-09).**
- **(D-i)** La réduction « résidu de D1 = `A_T` » est traitée comme **acquise** — elle ne fait que
  **recombiner deux scellés** (passerelle + SPECTRE-K3) via le dictionnaire HOLOGRAPHIE-G3.
  Elle est **consignée** ici (§1), non re-démontrée.
- **(D-ii)** Le candidat `A_T~1/C_T~1/N` est posé au niveau **scaling uniquement** ; le coefficient
  exact (sceau dS/CFT) **n'est pas tenté** dans ce cadrage — étape ultérieure si priorisée.
- **Cible = réduction de comptage** (`D1⟷E`), non simple diagnostic.

---

## 1. La réduction acquise — `résidu(D1) = {A_T}` `[recombinaison de deux scellés]`

Le dictionnaire holographique (`LC-D-HOLOGRAPHIE-G3` §1-§4) éclate la liberté de D1 en deux
pièces de natures distinctes :

- **`g₍₀₎` = source = jauge conforme.** C'est le choix de représentant / cadre — la liberté de
  D1 sur le fond, *que D1 ne fixe pas* (et que la stabilité inter-éons `m̂λ̂=9k²/4` épuise côté
  fond, `LC-A-D1-STABILITE-WEYL`). Ce n'est **pas** un degré de liberté dynamique résiduel.
- **`g₍₃₎` = VEV = état de la CFT céleste** = `⟨T_ij⟩ = (d/16πG)\,g₍₃₎`. C'est la **donnée libre**
  (Weyl rescalé TT, 2 polarisations), la **marée** — le vrai résidu dynamique de D1.

La liberté résiduelle de D1 est donc l'**état** de la CFT céleste, caractérisé par ses
corrélateurs de `g₃`. On les emboîte par ordre :

| Corrélateur de `g₃` | Statut | Source |
|---|---|---|
| **un-point** `⟨g₃⟩` | **`=0`** (fixé) | passerelle A3⟷D1 (BD/dS-inv ; absorbé dans A4) |
| **deux-point** `⟨g₃g₃⟩` | **forme `∝k³` (`Δ=3`) scellée** ; libre **seulement en amplitude** | `LC-D3-SPECTRE-K3` (`verif_D3_spectre_k3.py`) |
| **>2-point** (non-gaussien) | non traité | `décision ouverte` (non-linéaire, hérité) |

Au niveau **deux-point / gaussien**, tout est donc déterminé sauf un facteur d'échelle global :

$$\boxed{\;\text{résidu}(D1)\big|_{\text{2-pt}} \;=\; \{A_T\}\;\;\text{(un seul nombre)},\qquad
\mathcal P_h(k)=\frac{k^3}{2\pi^2}\langle|g_{(0)}|^2\rangle \equiv A_T = \text{const}.\;}$$

**Lecture.** La sous-détermination de D1, jadis « une prescription géométrique opaque », puis
« une fonction à deux points », est ramenée — par pure recombinaison de scellés — à **une seule
amplitude** `A_T~(H/M_P)²`. C'est la réduction `[acquise, (D-i)]`, sans algèbre neuve. *Réserve
explicite* : « résidu = `A_T` » vaut **au niveau gaussien** ; le contenu non-gaussien (corrélateurs
`>2`) est la `décision ouverte` non-linéaire héritée de `WEYL-BD §6`, **non absorbée ici**.

---

## 2. Le candidat de fermeture — `A_T ~ 1/C_T ~ 1/N` `[le mouvement de comptage, scaling]`

Reste la question : **`A_T` est-il fixé, ou libre ?** Le cadre `[D]` fournit un candidat
naturel — la **charge centrale** `C_T` de la CFT céleste. En dS/CFT (bord `d=3` à `𝓘⁺`,
`LC-D-HOLOGRAPHIE-G3` §3), le deux-point du tenseur de stress est fixé en forme et **normalisé
par `C_T`** : `⟨T T⟩ ~ C_T/|x|^{2d}`. Or, par scaling :

$$C_T \sim \Big(\frac{\ell_{dS}}{\ell_P}\Big)^{d-1}=\Big(\frac{\ell_{dS}}{\ell_P}\Big)^2,
\qquad
N = S_{dS} \sim \Big(\frac{\ell_{dS}}{\ell_P}\Big)^2,
\qquad
A_T \sim \Big(\frac{H}{M_P}\Big)^2 \sim \Big(\frac{\ell_P}{\ell_{dS}}\Big)^2,$$

d'où la relation centrale, **au niveau scaling** (cohérente avec le cutoff `√(N/π)=ℓ_dS/ℓ_P` de
`SPECTRE-K3`) :

$$\boxed{\;A_T \;\sim\; \frac{1}{C_T}\;\sim\;\frac{1}{N}\;}\qquad [\text{scaling ; (D-ii)}].$$

**Le mouvement.** Si dS/CFT **normalise `C_T`** (un nombre fixé par la théorie gravitationnelle),
alors `A_T` est fixé ⟹ le dernier nombre de D1 est déterminé. Mais `C_T ~ N = S_dS` **réimporte
exactement la circularité de `LC-E`** (`N=S_dS` présuppose `ℓ_P`). La fermeture serait donc
**conditionnelle** à cette circularité, qui n'est **pas brisée** ici.

**Le gain, même sans fermeture.** Indépendamment de savoir si `C_T` est *fixé*, la relation
`A_T ~ 1/C_T ~ 1/N` dit que **le résidu d'amplitude de D1 est le même objet que le compte `N` de
`[E]`** : ils ne sont **pas indépendants**. C'est le mouvement de comptage `D1⟷E`, transposé de la
passerelle `A3⟷D1` : un postulat (ici un *nombre libre*) de moins, à confirmer. Le compte de
degrés de liberté indépendants `{A_T(D1), N([E])}` passe, au niveau scaling, à `{N}`.

**Direction et asymétrie `[à ne pas perdre]`.** Le lien est porté par le **scaling**, pas (encore)
par une égalité avec coefficient. `A_T ~ 1/N` est un **candidat** : il dit que *si* `N` est fixé,
*alors* `A_T` l'est, et réciproquement — mais ne **fixe** ni l'un ni l'autre (la circularité LC-E
les tient ensemble sans les déterminer). On ne ferme donc **pas** D1 ; on **rattache** son résidu
au compte de `[E]`.

---

## 3. Triage `[forme / amplitude / unicité / non-gaussien]`

| Étage du résidu de D1 | Contenu | Statut |
|---|---|---|
| **forme du 2-pt** (`∝k³`, `Δ=3`) | invariance d'échelle côté `g₃` | **`établi (sceau)`** (`SPECTRE-K3`) |
| **amplitude `A_T`** | le seul nombre libre (gaussien) | candidat `A_T~1/C_T~1/N` : `formalisable` (scaling) → `à inventer` (coefficient, normalisation dS/CFT) ; **obstruction = circularité LC-E** |
| **unicité de l'état** | BD ⟹ `⟨T⟩` unique ? | `décision ouverte` (non-unitarité dS/CFT ; CFT de raccordement non construite — `HOLOGRAPHIE-G3 §3-4`) |
| **non-gaussien** (`>2-pt`) | corrélateurs supérieurs | `décision ouverte` (non-linéaire, **hérité** `WEYL-BD §6`) |

**Scellé (adossé, aucun sceau neuf) :** forme `⟨g₃g₃⟩∝k³` (`verif_D3_spectre_k3.py`) ; dictionnaire
`g₃=⟨T⟩` (`verif_D_g3.py`) ; relation d'état BD `g₃=-(i/3)k³g₀` (`verif_D3_bunchdavies.py`).
**Ouvert (non franchi ici) :** coefficient exact `A_T(C_T)` ; fixation de `N` (circularité LC-E,
non brisée) ; unicité de l'état ; non-gaussien.

**Relevé (2026-06-12, `LC-D-NONLIN-2PT` v0.1, audité à froid 4/4 ACQUIS,
`LC-AUDIT-LOG-NONLIN-2PT`).** La réduction du §1 — « résidu gaussien de D1 = **une**
amplitude `A_T` » — reposait sur la relation d'état BD (perturbative, TT) ; elle est
désormais **relevée non-perturbativement** : la ligne « forme du 2-pt » du tableau
ci-dessus passe de `établi (sceau)` *perturbatif TT* à **`établi` par invariance**
(comptage de représentation, secteur de Weyl complet, deux parités — secteur pair :
dimension 1, forme `k³·Π^TT` forcée ; secteur impair : dimension 1 ET contact, aucune
amplitude radiative neuve). Le caveat « non-linéaire » de la ligne *non-gaussien* est
ainsi levé **pour la forme du deux-point** (les corrélateurs `>2-pt` restent
`décision ouverte`). Sans surclassement : seule la **forme** est verrouillée ; les
lignes *amplitude* et *unicité* du tableau sont **inchangées** ; D1 non clos ;
circularité LC-E intacte.

---

## 4. Critère de réfutation `[falsifiabilité]`

Le candidat de réduction `D1⟷E` (`A_T~1/N`) **casserait** si l'on exhibait :

$$\text{REFUTATION : un principe fixant } A_T \text{ INDÉPENDAMMENT de } N/C_T,$$

c.-à-d. une prescription d'amplitude sans référence au compte holographique — alors `A_T` et `N`
redeviendraient indépendants et le rattachement tomberait. **Ou** : si la CFT céleste de
raccordement n'admettait **pas** de `C_T` bien défini (obstruction de non-unitarité dS/CFT) — alors
le candidat de fermeture échoue, mais la **réduction du §1 (`résidu=A_T`) reste acquise** : `A_T`
demeurerait simplement *libre*, sans être rattaché à `[E]`.

**Statut.** Le scaling `C_T ~ N ~ (ℓ_dS/ℓ_P)²` est standard en dS/CFT ; aucun contre-exemple connu.
La part non établie est isolée dans (i) le **coefficient exact** et (ii) la **circularité LC-E**.
Le candidat tient au niveau testé (scaling).

---

## 5. Ce que ce cadrage FAIT vs NE FAIT PAS `[honnêteté §6.4]`

**FAIT.** (i) **Consigne** la réduction « résidu de D1 (deux-point/gaussien) = un seul nombre `A_T` »
— recombinaison de deux scellés (passerelle ⟨g₃⟩=0 + SPECTRE-K3 forme k³) via le dictionnaire
`g₃=⟨T⟩`, **sans algèbre neuve**. (ii) **Pose** le candidat `A_T~1/C_T~1/N` identifiant le résidu
d'amplitude de D1 au **compte `N` de `[E]`** : candidat de réduction de comptage `D1⟷E`. (iii)
**Trie** proprement forme / amplitude / unicité / non-gaussien.

**NE FAIT PAS.** (i) Ne **ferme pas** D1 : `A_T` n'est **pas** fixé (coefficient `à inventer` ;
circularité LC-E intacte). (ii) N'établit **pas** le coefficient exact — **scaling seul** (D-ii).
(iii) Ne traite **pas** le non-gaussien / non-linéaire (`décision ouverte` héritée). (iv)
N'établit **ni** dS/CFT **ni** la CFT de raccordement (`à inventer`, `HOLOGRAPHIE-G3 §3`). (v) Ne
**brise pas** la circularité de `LC-E`. (vi) Ne touche **aucune** algèbre ; « le bang gagne »
(P6 B) intact ; A3/A4, C7/A2★ inchangés ; (A) physique conditionnel au seul A2★ **INCHANGÉ**.
**Réduction d'hypothèse ≠ démonstration de la CCC.**

---

## 6. Propagation suggérée `[NON exécutée — à valider/déposer séparément]`

Si la réduction est validée, propagation **additive** (jamais réécriture d'historique) :
- `LC-D-HOLOGRAPHIE-G3 §5` : ajouter que le résidu de D1, après passerelle + SPECTRE-K3, est
  **un seul nombre `A_T`**, candidat-rattaché au compte `N` de `[E]` (`A_T~1/C_T~1/N`, scaling).
- `LC-D3-SPECTRE-K3` (renvoi) : noter que l'amplitude `A_T` — laissée `décision ouverte` — est
  **le résidu complet de D1 au niveau gaussien** (renvoi à cette note).
- `LC-E-PLANCK-RESIDUEL` : noter le rattachement `A_T~1/N` (le compte `N` porte aussi l'amplitude
  primordiale ; circularité localisée, non aggravée).
- `LC-AUDIT-VERDICT §8bis` : bullet daté « passerelle D1⟷E : résidu de D1 = `A_T` (gaussien) ;
  candidat `A_T~1/C_T~1/N` rattachant D1 à `[E]` (scaling) ; D1 non clos ; coefficient à inventer ».
- `LC-A-D1-FACTEUR-CONFORME §5` : préciser que la prescription D1 ne reste `à inventer` que pour
  **une amplitude** (et non plus un deux-point), candidat-fixée par `C_T~N`.
- `00-INDEX` (carte + changelog) ; `03-GLOSSAIRE` (entrées « passerelle D1⟷E / résidu = A_T » et
  « charge centrale céleste `C_T ~ N` »).
- **Sceau optionnel — `[à inventer, NON inclus]`** : un sceau de normalisation dS/CFT fixant le
  **coefficient** de `A_T(C_T)` ; hors périmètre (D-ii), étape ultérieure si priorisée.

---

## 7. Renvois & glossaire

**Renvois.** `LC-D-CT-ATN` (sceau aval : D-ii scellé — `A_T=16/N`, deux routes, `C_T∝N`) ;
`LC-WORK-CT-CADRAGE` (cadrage aval : tri des mécanismes + promotion D-ii) ;
`LC-WORK-A3-D1-PASSERELLE` (un-point `⟨g₃⟩=0` absorbé dans A4 — le parent direct) ;
`LC-D3-SPECTRE-K3` (forme du deux-point `∝k³` scellée ; amplitude `A_T` ouverte) ;
`LC-D-HOLOGRAPHIE-G3` (dictionnaire `g₃=⟨T⟩`, `g₀`=jauge, `C_T` charge centrale céleste) ;
`LC-D3-WEYL-BUNCHDAVIES` (relation d'état BD, caveat non-linéaire) ; `LC-E-PLANCK-RESIDUEL`
(`N=S_dS`, circularité) ; `LC-A-D1-FACTEUR-CONFORME` / `LC-A-D1-STABILITE-WEYL` (verrou D1,
fond ⊥ marée) ; `LC-AUDIT-VERDICT §6.4` (discipline).
**Ajout (2026-06-12)** : `LC-D-NONLIN-2PT` + `LC-AUDIT-LOG-NONLIN-2PT` (verrou de forme
du deux-point par invariance, rang 2, audité 4/4 ACQUIS — relève la présente réduction
au non-perturbatif, cf. note du §3).

**Glossaire à ajouter (`LC-03`).**
- *Passerelle D1 ⟷ E / résidu = `A_T`* : après passerelle A3⟷D1 (un-point) et SPECTRE-K3 (forme
  k³), le résidu libre de D1 au niveau gaussien est l'unique amplitude `A_T~(H/M_P)²`.
- *Charge centrale céleste `C_T ~ N`* : en dS/CFT (`d=3`), `C_T~(ℓ_dS/ℓ_P)²~N=S_dS` ⟹
  `A_T~1/C_T~1/N` (scaling) ; candidat rattachant le résidu de D1 au compte holographique de `[E]`.

---

## Appendice — tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`). Ici : forme `⟨g₃g₃⟩∝k³` `établie (sceau)` ; réduction `résidu=A_T`
**consignée** (recombinaison de scellés) ; lien `A_T~1/C_T~1/N` `formalisable` (scaling) →
`à inventer` (coefficient) ; unicité de l'état + non-gaussien `décision ouverte` ; D1 non clos.
