---
id: LC-WORK-D3-SPECTRE-K3
titre: "Tâche 1 du pivot post-porte (ii) — EXPLICITER la 2-points ⟨g₃g₃⟩~k³ et le RÔLE DE N. Étape papier (avant sceau, Tâche 2) du front D3 Weyl/Bunch-Davies recommandé par LC-WORK-REPRISE-POST-PORTE-II §4. Deux livrables : (1) la chaîne ⟨g₃g₃⟩~k³ DÉRIVÉE depuis la relation d'état BD g₃=-(i/3)k³g₀ — trois visages d'UN spectre invariant d'échelle (𝒫_h=const ⟺ P_{g₀}∝k⁻³ ⟺ P_{g₃}∝k³ ⟺ ⟨TT⟩∝k³, Δ=3) ; (2) le rôle de N comme régulateur UV de l'intégrale de variance — résultat NEUF : avec le noyau EXACT (pas le leading (kη)⁴), la variance ne diverge PAS en (k_UVη_*)⁴ mais croît LOGARITHMIQUEMENT (enveloppe cos²x/3, moyenne 1/6) : Ω_σ^tot/A_T ≈ (1/6)ln(k_UVη_*)+0.045, donc ≈23 au cutoff Planck/N (√(N/π)~10⁶¹) — fini, ≪0.5 pour A_T≪1 (H sous-Planckien). N joue donc DEUX rôles (cutoff log-doux + normalisation A_T) et les deux se reportent sur la circularité de LC-E (N=S_dS présuppose ℓ_P). Vérifié numériquement (sera scellé en Tâche 2). Référence la substance par id ; ne duplique ni les sceaux ni l'algèbre des parents."
codename: LC-RACCORD
type: note de travail (étape papier — Tâche 1) — subordonnée à LC-WORK-REPRISE-POST-PORTE-II §4, à LC-AUDIT-VERDICT §6.4/§9, à LC-WORK-AUDIT-FROID §12.
version: 0.1
langue: fr
date: 2026-06-08
statut: paper établi (chaîne k³ + finding log-variance, vérifiés numériquement) — sceau à déposer en Tâche 2 ; normalisation A_T et fixation de N restent décision ouverte / à inventer (circularité LC-E).
prerequis_kb: [LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-D3-WCH-GWE, LC-E-PLANCK-RESIDUEL, LC-WORK-REPRISE-POST-PORTE-II, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_bunchdavies.py, verif_D3_WCH_GWE.py, verif_D_g3.py, verif_E_planck.py]
fichier_compagnon_vise: "verif_D3_spectre_k3.py (Tâche 2 — étend verif_D3_bunchdavies.py + verif_D3_WCH_GWE.py)"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# Tâche 1 — la 2-points `⟨g₃g₃⟩~k³` et le rôle de `N`

> **Position.** Étape **papier** du front recommandé par `LC-WORK-REPRISE-POST-PORTE-II §4`
> (pivot post-porte (ii), close sur `neutre`/`répulseur`). La porte (ii) reste close ; la
> synthèse du front (a) reste **inchangée** ; on ne rouvre ni A2 ni A3. On passe de la
> **coïncidence un-point** `⟨g₃⟩_BD=0` (acquise, `LC-D3-WEYL-BUNCHDAVIES`) au **contrôle du
> spectre** (la 2-points). Discipline `LC-AUDIT-VERDICT §6.4` : un `établi (algèbre)` ici ne
> dit jamais « la physique CCC est établie ». Le sceau correspondant est la **Tâche 2**.

---

## 0. Rôle et garde-fou

Cette note **explicite** deux objets et **n'en scelle aucun** (le sceau est la Tâche 2). Ce
qui devient `établi (papier, vérifié numériquement)` : (1) la chaîne `⟨g₃g₃⟩~k³` comme
réécriture du spectre invariant d'échelle dans la variable `g₃` ; (2) le **finding** sur le
rôle de `N` — la variance de cisaillement est **log-divergente** (et non quartique) en la
coupure UV avec le noyau exact. Ce qui reste `décision ouverte / à inventer` : la
**normalisation d'amplitude** `A_T` et la **fixation de `N`** (circularité `LC-E` non brisée),
ainsi que la transposition non-linéaire au crossover (caveat parent inchangé). On ne surclasse
rien : un spectre *contrôlé* conditionnellement à `A_T≪1` et à `N` n'est pas un spectre *dérivé*.

---

## 1. Les quatre briques `[référence par id — ne pas reprouver]`

- **`LC-D3-WEYL-BUNCHDAVIES`** : sur un mode TT de dS₄, Weyl électrique rescalé **dérivé**
  `E_ij=(d/2H)g₃` (`d=3`) ⟹ `« C→0 » ⟺ « g₃→0 »` ; **un-point** `⟨g₃⟩_BD=0` (coïncidence,
  ferme D1 au niveau classique) ; **résidu deux-points** `⟨g₃g₃⟩~k³` annoncé. Relation d'état
  BD `g₃=-(i/3)k³g₀` (sceau `verif_D3_bunchdavies.py`, bloc [3], `assert` passe).
- **`LC-D-HOLOGRAPHIE-G3`** : `⟨T_ij⟩=(d/16πG)g₃`, `d=3` impair ⟹ pas d'anomalie ⟹ `⟨T⟩`
  traceless + conservé. Fixer `g₃` = choisir l'**état** de la CFT céleste. `g₀`=source/jauge,
  `g₃`=VEV libre (2 polar. TT).
- **`LC-D3-WCH-GWE`** : le résidu `⟨g₃g₃⟩~k³` = strain primordial `𝒫_h~const` (invariant
  d'échelle `A_T`) est l'**entrée spectrale** de l'intégrale de variance (§8 bloc [7]). Acquis
  central : le mode régulier **exact** plafonne à `Ω_σ/ε²=(x cos x−sin x)²/(3x²)≤0.377<0.5
  ∀ kη` — **régime (A) par mode, à toute échelle** (le « basculement à `kη~1.9` » est un
  ARTEFACT du *leading* `(kη)⁴/27`, audit C5).
- **`LC-E-PLANCK-RESIDUEL`** : `N≡S_dS=3π/(Λℓ_P²)~3,3·10¹²²` est **holographique** (cellules
  d'horizon), pas sériel ; `ℓ_P=√(3π/ΛN)` ; **circularité non brisée** (`N` présuppose `ℓ_P`).
  Même bord `𝓘⁺` que `g₃`.

---

## 2. La 2-points `⟨g₃g₃⟩~k³`, EXPLICITÉE `[établi — papier]`

**Point de départ (acquis).** Pour le mode de Bunch–Davies, l'expansion FG donne la relation
d'état **déterministe par mode** (sceau parent, bloc [3]) :

$$g_{(3)}(k) = -\tfrac{i}{3}\,k^3\,g_{(0)}(k)\qquad(\text{par polarisation}).$$

`g₀` est la donnée libre (la source/le mode constant à `𝓘⁺`) ; `g₃` est la donnée radiative
TT. La relation `g₃∝k³g₀` est **algébrique**, pas statistique : elle lie deux coefficients d'UN
mode. La **statistique** vient de l'état quantique BD, qui dote `g₀` d'un spectre.

**La chaîne (trois visages d'un seul spectre).** Le vide de Bunch–Davies donne au mode
tensoriel un spectre de **strain invariant d'échelle** (résultat standard dS, graviton sans
masse) :

$$\mathcal P_h(k)\;\equiv\;\frac{k^3}{2\pi^2}\,\langle |g_{(0)}(k)|^2\rangle \;=\; \text{const}
\;\equiv\; A_T \qquad\Longleftrightarrow\qquad P_{g_{(0)}}(k)\;\propto\;k^{-3}.$$

En propageant par `g₃=-(i/3)k³g₀` (donc `|g₃|²=\tfrac19 k^6|g₀|²`) :

$$\boxed{\;P_{g_{(3)}}(k)\;=\;\tfrac19\,k^6\,P_{g_{(0)}}(k)\;\propto\;k^6\cdot k^{-3}\;=\;k^3\;}$$

et via le dictionnaire holographique `⟨T⟩=(d/16πG)g₃` (`LC-D`) :

$$\langle T(k)\,T(-k)\rangle \;=\;\Big(\tfrac{d}{16\pi G}\Big)^2 P_{g_{(3)}}(k)\;\propto\;k^3
\;=\;k^{\,2\Delta-d}\quad(\Delta=d=3),$$

**exactement** le scaling conforme d'un opérateur `Δ=3` sur un bord `d=3`. Les trois énoncés —
`𝒫_h=const`, `P_{g₃}∝k³`, `⟨TT⟩∝k³` — sont **le même spectre invariant d'échelle**, exprimé
dans la source `g₀`, dans la donnée radiative `g₃`, ou dans le stress `⟨T⟩`. Le `k³` de `g₃`
n'est pas « une croissance UV » : c'est l'invariance d'échelle vue côté `g₃` (la puissance de
`k` ne fait que tracer le changement de variable).

> **Lecture (dichotomie un-point / deux-points, `LC-D3-WCH-GWE` §5).** Le **un-point**
> `⟨g₃⟩=0` = la WCH réalisée (le `Ω_σ` que voit le noyau homogène ⟹ régime (A)). Le
> **deux-points** `k³` = le spectre dont la **forme** pondère les modes dans la variance — c'est
> lui, et lui seul, que cette note met sous contrôle.

---

## 3. Le rôle de `N` `[finding neuf + report sur LC-E]`

`N` intervient **deux fois**, et il faut les séparer proprement.

### 3.1 — `N` comme régulateur UV de la variance `[finding : log, pas quartique]`

La quantité physique du front (a) n'est pas un mode isolé mais la **variance de cisaillement**
sommée sur le spectre :

$$\Omega_\sigma^{\rm tot}\;\simeq\;A_T\!\int^{x_{\rm UV}}\!\frac{dx}{x}\;g(x),\qquad
g(x)\equiv\frac{(x\cos x-\sin x)^2}{3x^2},\quad x\equiv k\eta_*.$$

`g(x)` est le **noyau exact** par mode (`LC-D3-WCH-GWE` §1/§8), `A_T` la normalisation
invariante d'échelle, `x_UV=k_{\rm UV}\eta_*` la coupure. Le `(kη)⁴/27` du §8 n'est que le
*leading* `x≪1` de `g`.

**Le point neuf (corrige une lecture du §8 parent).** L'enveloppe grand-`x` de `g` n'est **pas**
décroissante : `g(x)→cos²x/3` (oscillant, moyenne `1/6`), car le terme dominant `x\cos x` du
numérateur compense le `x²` du dénominateur. Donc l'intégrale n'est **pas** dominée par l'UV en
`x_UV⁴` (cela, c'était l'artefact du *leading*, qui croît sans borne) : elle croît
**logarithmiquement** :

$$\boxed{\;\Omega_\sigma^{\rm tot}/A_T\;=\;\int^{x_{\rm UV}}\!\frac{dx}{x}\,g(x)\;\simeq\;
\tfrac16\ln x_{\rm UV}\;+\;0{,}045\;}$$

Vérifié numériquement (sera scellé en Tâche 2) :

| `x_UV=k_UVη_*` | `C(x_UV)` exact | `(1/6)ln x_UV` | leading `(x_UV)⁴/108` |
|---|---|---|---|
| `10¹` | `0,436` | `0,384` | `0,93` |
| `10³` | `1,196` | `1,151` | `9,3·10⁹` |
| `10⁶` | `2,285` | `2,303` | `9,3·10²¹` |
| `10²⁰` | `7,72` | `7,68` | `≈10⁷⁷` |
| `10⁶⁰` | `23,06` | `23,03` | `≈10²³⁷` |

La colonne `leading` (divergente, artefact) est conservée pour montrer le **contraste** : le
noyau exact réduit une divergence `x_UV⁴` à une croissance `\tfrac16\ln x_UV`. *(max `g=0,3767`
à `x≈2,744` ; petit `x` : `g→x⁴/27` ; moyenne d'enveloppe sur `[50,150]` `=0,166≈1/6` — tous
reproduits.)*

**La coupure, c'est `N`.** Le bord céleste porte `N=S_dS` degrés de liberté **finis**
(`LC-E`/`LC-D`) ⟹ la plus courte longueur d'onde est `~ℓ_P`, soit
`x_UV=k_{\rm UV}\eta_*\simeq\ell_{\rm dS}/\ell_P=\sqrt{N/\pi}`. Avec `N~3,3·10¹²²` :
`x_UV\simeq1,0·10⁶¹` ⟹

$$\Omega_\sigma^{\rm tot}/A_T\;\simeq\;\tfrac16\ln(10^{61})+0{,}045\;\approx\;23.$$

Donc la dépendance du verdict (A) à la coupure spectrale est **logarithmique** — extrêmement
douce. C'est un **durcissement** de l'acquis `LC-D3-WCH-GWE` : non seulement chaque mode est en
(A) (`≤0,377`), mais la **variance sommée** ne diverge que comme `\ln N`.

### 3.2 — `N` comme normalisation d'amplitude `[décision ouverte]`

`A_T=\mathcal P_h` est fixé par l'échelle du crossover, `A_T\sim(H/M_P)^2` (au facteur conforme
près du raccord CCC). Cela rattache `A_T` au **même cercle** `{Λ,H,ℓ_P,N}` de `LC-E` : `ℓ_P`
n'est fixé qu'avec `N`, lui-même `=S_dS` qui présuppose `ℓ_P`. **La circularité de `LC-E` n'est
pas brisée par ce front** ; elle est seulement *localisée* : tout le contenu non établi du
spectre se reporte sur `A_T` (amplitude) et sur `x_UV=√(N/π)` (coupure log-douce).

### 3.3 — Bilan `N`

| rôle de `N` | effet sur le verdict (A) | statut |
|---|---|---|
| coupure UV `x_UV=√(N/π)` | `Ω_σ^tot/A_T≈\tfrac16\ln√(N/π)≈23` (log-doux) | **`établi` (papier+num.)** |
| normalisation `A_T~(H/M_P)²` | facteur global ; (A) ssi `A_T≪1` (H sous-Planckien) | `décision ouverte` |
| fixation de `N` elle-même | aucune (circularité `LC-E`) | **`à inventer / hors de portée`** |

---

## 4. Conséquence pour le verdict (A) `[sans surclassement]`

Pour un crossover à `H` **sous-Planckien** (`A_T≪1`), `Ω_σ^tot≈23\,A_T≪0,5` : le spectre est
**contrôlé**, le régime (A) tient pour la **variance** (pas seulement par mode). C'est le contenu
neuf que la coïncidence un-point ne donnait pas : un énoncé sur le **deux-points**.

**Ce que cela ne dit pas (`§6.4`).** (i) `A_T` n'est pas *dérivé* — il vaut `(H/M_P)²`, et ni
`H` ni `ℓ_P` ne sont fixés indépendamment (`LC-E`). (ii) `N` n'est pas brisé. (iii) Le caveat
non-linéaire / crossover du parent (`LC-D3-WEYL-BUNCHDAVIES §0`, `LC-D3-WCH-GWE §6.2/C7) reste
entier. Donc : **« le spectre k³ est contrôlé conditionnellement à `A_T≪1` et au cadre CCC »**,
non « le spectre est dérivé ». La synthèse du front (a) ne change pas ; on **ajoute** un maillon
deux-points, on ne promeut rien.

---

## 5. Critère pré-enregistré + spec du sceau (Tâche 2) `[à figer avant de coder]`

**Fichier visé.** `verif_D3_spectre_k3.py`, extension de `verif_D3_bunchdavies.py`
(relation d'état `g₃=-(i/3)k³g₀`, déjà scellée) et de `verif_D3_WCH_GWE.py` (noyau `g(x)`,
déjà scellé). Blocs neufs :

1. **Chaîne spectrale (symbolique).** Poser `P_{g₀}∝k⁻³` (invariance d'échelle), propager par
   `g₃=-(i/3)k³g₀`, `assert` `P_{g₃}∝k³` ; `assert` `2Δ−d=3` (`Δ=d=3`) ⟹ `⟨TT⟩∝k³` cohérent.
2. **Variance exacte (numérique) — le cœur.** `C(x_UV)=∫_{x_IR}^{x_UV} dx/x · g(x)` ;
   `assert` croissance log : ajuster `C≈α ln x_UV+β`, `assert |α−1/6|<10⁻²` et `β` stable ;
   `assert` enveloppe `⟨g⟩_[50,150]≈1/6` ; `assert max g=0,3767±10⁻³` à `x≈2,744`.
3. **Contraste leading/exact.** `assert` `(x_UV)⁴/108` diverge tandis que `C(x_UV)` reste `O(ln)`
   (reproduire la table §3.1) — scelle que la divergence quartique du §8 parent est un artefact.
4. **Cible physique.** `x_UV=√(N/π)`, `N=S_dS=3π/(Λℓ_P²)` (réutiliser `verif_E_planck.py`) ;
   `assert` `C(x_UV)≈23±1` ; reporter explicitement la circularité `N↦ℓ_P` (commentaire, pas
   `assert`).

**Verdicts possibles (pré-enregistrés).**
- *Spectre contrôlé* : `C` log-borné + `A_T≪1` ⟹ (A) pour la variance — **acquis de physique
  neuve** (`établi (algèbre)`), conditionnel à `A_T` et au cadre.
- *Sensibilité forte à `N`* : si l'enveloppe n'était pas `1/6` (erreur de noyau) ⟹ revoir le
  pont `LC-D3-WCH-GWE` §1 — non attendu (vérifié ici).
- *Report sur `A_T`/`N`* : la part non établie est isolée dans l'amplitude et la coupure
  (`décision ouverte`, circularité `LC-E`) — l'issue **attendue**.

**Housekeeping à prévoir (Tâche 3, après sceau).** Enregistrer `LC-D3-SPECTRE-K3` (note de
résultat) ; corriger dans `LC-D3-WCH-GWE §8` la lecture « variance `~(k_UVη_*)⁴` » en
« `~\tfrac16\ln(k_UVη_*)` (noyau exact) ; la forme quartique est *leading* » (cohérent C5) ;
glossaire (entrée *spectre `k³` / variance log*). **Aucune touche** à l'algèbre des parents ni
au verdict figé de la synthèse.

---

## 6. Honnêteté et tags `[discipline]`

- **On reste post-porte (ii).** La porte (ii) est close (`neutre`/`répulseur`, `det J*=1`) ; ce
  front est **indépendant** d'elle et de l'attracteur. A4 socle ; (A) `formalisable` cond. A2 —
  inchangé.
- **Établi ici :** la chaîne `𝒫_h=const⟺P_{g₃}∝k³⟺⟨TT⟩∝k³` (papier) ; le finding
  log-variance `Ω_σ^tot/A_T≈\tfrac16\ln x_UV` (papier + numérique, à sceller).
- **Décision ouverte / à inventer :** normalisation `A_T~(H/M_P)²` ; fixation de `N`
  (circularité `LC-E`) ; transposition non-linéaire (caveat parent).
- **Pas de surclassement (`§6.4`).** « Spectre contrôlé cond. `A_T≪1` » ≠ « spectre dérivé ».
  « `Ω_σ^tot` fini » ≠ « la CCC est établie ».

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
