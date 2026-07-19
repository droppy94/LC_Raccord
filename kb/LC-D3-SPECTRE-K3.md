---
id: LC-D3-SPECTRE-K3
titre: "Front (a) / D3 — du UN-POINT au DEUX-POINTS : la 2-points ⟨g₃g₃⟩~k³ EXPLICITÉE et le RÔLE DE N. Successeur de LC-D3-WEYL-BUNCHDAVIES (coïncidence un-point ⟨g₃⟩_BD=0). Deux résultats SCELLÉS (verif_D3_spectre_k3.py, EXIT 0) : (1) la 2-points est l'invariance d'échelle vue côté donnée radiative — chaîne 𝒫_h=const ⟺ P_{g₀}∝k⁻³ ⟺ P_{g₃}=⅑k⁶P_{g₀}∝k³ ⟺ ⟨TT⟩∝k^{2Δ-d}=k³ (Δ=d=3), dérivée de g₃=-(i/3)k³g₀ ; (2) FINDING : la variance de cisaillement ne diverge PAS en (k_UVη_*)⁴ (artefact du leading, cohérent audit C5) mais croît LOGARITHMIQUEMENT — noyau exact d'enveloppe cos²x/3 (moyenne 1/6) ⟹ Ω_σ^tot/A_T = (1/6)ln(k_UVη_*)+β∞, β∞=0,04503. Au cutoff holographique k_UVη_*=√(N/π)=ℓ_dS/ℓ_P≈1,02·10⁶¹ : Ω_σ^tot/A_T≈23,46, fini, ≪0,5 dès que A_T≪1 (H sous-Planckien). N joue DEUX rôles (cutoff log-doux + normalisation A_T~(H/M_P)²), tous deux reportés sur la circularité de LC-E (N=S_dS présuppose ℓ_P). Verdict : SPECTRE k³ CONTRÔLÉ, conditionnel à A_T≪1 et au cadre CCC — un maillon DEUX-POINTS ajouté, sans surclassement (§6.4). Porte (ii) reste close ; synthèse du front (a) INCHANGÉE."
codename: LC-RACCORD
tags: [module-D3, module-D, module-E, module-A, front-a, weyl, bunch-davies, g3, stress-tensor, ds-cft, deux-points, spectre, k3, invariance-echelle, variance, cisaillement, GWE, cutoff, N-holographique, planck, sceau]
type: chaînon (résultat — contrôle du spectre DEUX-POINTS ; successeur de LC-D3-WEYL-BUNCHDAVIES un-point ; étape papier LC-WORK-D3-SPECTRE-K3 ; SCEAU FAIT)
statut: établi (algèbre + numérique), SCEAU FAIT — (1) chaîne ⟨g₃g₃⟩~k³ dérivée et vérifiée symboliquement ; (2) finding variance LOG (pas quartique) vérifié numériquement, β∞=0,04503, C(√(N/π))≈23,46. Verdict (A)-pour-la-variance CONDITIONNEL à A_T≪1 (H sous-Planckien) et au cadre CCC. Décision ouverte / à inventer : normalisation A_T~(H/M_P)² ; fixation de N (circularité LC-E, non brisée) ; transposition non-linéaire (caveat parent).
version: 0.3
langue: fr
date: 2026-06-08
maj: "2026-06-12 — v0.3 : renvoi (lot de propagation NONLIN-2PT) — LC-D-NONLIN-2PT v0.1 (sceau verif_nonlin_deuxpoint.py EXIT 0/41 ; audité à froid 4/4 ACQUIS, LC-AUDIT-LOG-NONLIN-2PT v0.1) : la chaîne k³ de ce chaînon est REFERMÉE COMME CAS PARTICULIER du verrou de forme par invariance (secteur pair du deux-point du Weyl rescalé complet : dimension 1, forme k³·Π^TT forcée — représentation + OP 2.23 ; secteur impair : dimension 1 ET contact). Résidu libre = la SEULE amplitude A_T~1/N, cohérent avec la passerelle D1⟷E (relevée par invariance). §7 enrichi additivement. Le k³ reste la donnée de Cauchy irréductible ; D1 non clos ; compte {A4 ; A2★ ; N} inchangé. Aucune touche algèbre ni sceaux. | 2026-06-09 — v0.2 : §7 — propagation de la passerelle D1⟷E (LC-WORK-D1-E-AMPLITUDE v0.1, paper-first). Renvoi ajouté : l'amplitude A_T~(H/M_P)² — laissée décision ouverte ici — EST le résidu complet de D1 au niveau gaussien (la forme k³ étant scellée par ce chaînon, le un-point ⟨g₃⟩=0 par la passerelle A3⟷D1) ; candidat-rattachée au compte N de [E] par A_T~1/C_T~1/N (scaling). Aucune touche à l'algèbre, au sceau ni au verdict ; A_T reste décision ouverte. | v0.1 : du un-point au deux-points — chaîne ⟨g₃g₃⟩~k³ dérivée (établi algèbre) + finding variance LOG (établi numérique, β∞=0,04503, C(√(N/π))≈23,46) ; sceau verif_D3_spectre_k3.py."
statut_id: validé après sceau — à enregistrer (LC-00-INDEX) ; PROPAGER : LC-D3-WCH-GWE §8 (corriger « variance ~(k_UVη_*)⁴ » → « ~(1/6)ln, noyau exact » ; cohérent C5), LC-00-INDEX (carte + changelog), 03_glossaire (entrées spectre k³ / variance log / β∞), LC-AUDIT-VERDICT §8bis (maillon deux-points ajouté), LC-02-PROGRAMME, LC-04-REFERENCES.
fichier_compagnon: verif_D3_spectre_k3.py
prerequis_kb: [LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-D3-WCH-GWE, LC-E-PLANCK-RESIDUEL, LC-WORK-D3-SPECTRE-K3, LC-WORK-REPRISE-POST-PORTE-II, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_bunchdavies.py, verif_D3_WCH_GWE.py, verif_E_planck.py, verif_D_g3.py]
renvois: [LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-D3-WCH-GWE, LC-E-PLANCK-RESIDUEL, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[A] / front (a) — A3/A4 : ajoute un maillon DEUX-POINTS (le spectre) au contenu de la WCH ; ne dérive ni A3 ni A4."
  - "[D3] hypothèse de Weyl — du un-point ⟨g₃⟩=0 (C→0) au deux-points ⟨g₃g₃⟩~k³ (spectre)."
  - "[D] holographie — ⟨TT⟩=(d/16πG)² P_{g₃} ; le cutoff vient du compte N de [D]/[E]."
  - "[E] retour de l'échelle — N=S_dS régularise la variance (log-doux) ET normalise A_T ; circularité LC-E localisée."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·SPECTRE·k³ — La 2-points `⟨g₃g₃⟩~k³` et le rôle de `N`

> **But.** `LC-D3-WEYL-BUNCHDAVIES` a établi la **coïncidence un-point** `⟨g₃⟩_BD=0=g₃(C→0)`
> (le Weyl rescalé dérivé `E_ij=(d/2H)g₃` ⟹ `« C→0 » ⟺ « g₃→0 »`, et le vide de Bunch–Davies
> donne `⟨g₃⟩=0`). Il restait le **résidu deux-points** `⟨g₃g₃⟩~k³`, annoncé mais non
> exploité. Ce chaînon (i) **explicite** ce résidu — il dérive la chaîne qui en fait le
> **spectre primordial invariant d'échelle** vu côté donnée radiative — et (ii) **tranche** le
> rôle de la coupure `N` dans la variance de cisaillement qui en découle (entrée de
> `LC-D3-WCH-GWE` §8). Étape papier : `LC-WORK-D3-SPECTRE-K3`. Sceau : `verif_D3_spectre_k3.py`.
>
> **Verdict (calculé, `verif_D3_spectre_k3.py`, EXIT 0).**
> **(1)** `⟨g₃g₃⟩~k³` n'est **pas** une croissance UV : c'est l'invariance d'échelle, exprimée
> dans `g₃`. Chaîne dérivée de `g₃=-(i/3)k³g₀` : `𝒫_h=const ⟺ P_{g₀}∝k⁻³ ⟺ P_{g₃}=⅑k⁶P_{g₀}∝k³
> ⟺ ⟨TT⟩∝k^{2Δ-d}=k³` (`Δ=d=3`). `[établi — algèbre]`
> **(2) Finding.** La variance `Ω_σ^tot=A_T∫dx/x·g(x)` (noyau **exact** `g=(x cos x−sin x)²/(3x²)`,
> `x=kη_*`) ne diverge **pas** en `(k_UVη_*)⁴` — cela, c'était l'artefact du *leading* `(kη)⁴/27`
> (cohérent audit C5). L'enveloppe de `g` tend vers `cos²x/3` (moyenne `1/6`), d'où une croissance
> **logarithmique** : `Ω_σ^tot/A_T=(1/6)ln(k_UVη_*)+β∞`, `β∞=0,04503`. Au cutoff holographique
> `k_UVη_*=√(N/π)=ℓ_dS/ℓ_P≈1,02·10⁶¹` : `Ω_σ^tot/A_T≈23,46` — **fini, `≪0,5` dès que `A_T≪1`**.
> `[établi — numérique]`
>
> **Donc : spectre `k³` CONTRÔLÉ**, conditionnel à `A_T≪1` (`H` sous-Planckien) et au cadre CCC.
> Un maillon **deux-points** est ajouté au contenu de la WCH ; **rien n'est surclassé** (§6.4 :
> « contrôlé cond. » ≠ « dérivé »). La porte (ii) reste close ; la synthèse du front (a) est
> **inchangée**. `[décision ouverte / à inventer : A_T~(H/M_P)² ; fixation de N (circularité LC-E)]`

---

## 0. Rôle et garde-fou

Ce chaînon **explicite** un résidu et **tranche** un rôle ; il ne ferme pas le front (a). Ce
qui est `établi (algèbre+numérique)` : la chaîne `k³` et le finding log-variance, tous deux
scellés. Ce qui reste `décision ouverte / à inventer` : l'**amplitude** `A_T~(H/M_P)²`, la
**fixation de `N`** (la circularité de `LC-E` n'est **pas** brisée, seulement *localisée*), et
la **transposition non-linéaire** au crossover (caveat de `LC-D3-WEYL-BUNCHDAVIES §0`, intact).
Discipline `LC-AUDIT-VERDICT §6.4` : un `établi` de chaînon = « l'algèbre/le numérique sont
corrects ET le sceau reproduit les cibles », jamais « la physique de la CCC est établie ».

---

## 1. La chaîne `⟨g₃g₃⟩~k³` — trois visages d'un seul spectre `[établi — algèbre]`

Le point de départ est la relation d'état BD, **déterministe par mode** (FG du mode de
Bunch–Davies, sceau parent `verif_D3_bunchdavies.py` bloc [3], ré-vérifiée ici bloc [1]) :

$$g_{(3)}(k) = -\tfrac{i}{3}\,k^3\,g_{(0)}(k)\qquad(\text{par polarisation}).$$

`g₀` est la source libre (mode constant à `𝓘⁺`), `g₃` la donnée radiative TT. La **statistique**
vient de l'état quantique BD, qui dote `g₀` d'un spectre de **strain invariant d'échelle** :

$$\mathcal P_h(k)\equiv\frac{k^3}{2\pi^2}\langle|g_{(0)}|^2\rangle=\text{const}\equiv A_T
\;\Longleftrightarrow\; P_{g_{(0)}}\propto k^{-3}.$$

En propageant par `|g₃/g₀|²=k⁶/9` puis par le dictionnaire holographique `⟨T⟩=(d/16πG)g₃`
(`LC-D-HOLOGRAPHIE-G3`) :

$$\boxed{\;P_{g_{(3)}}=\tfrac19 k^6 P_{g_{(0)}}\propto k^3,\qquad
\langle T T\rangle=\Big(\tfrac{d}{16\pi G}\Big)^2 P_{g_{(3)}}\propto k^{2\Delta-d}=k^3\quad(\Delta=d=3).\;}$$

Vérifié au sceau (bloc [1]) par dérivée logarithmique `k\,\partial_k\ln P=3` (insensible aux
constantes). **Lecture :** les trois énoncés — `𝒫_h=const`, `P_{g₃}∝k³`, `⟨TT⟩∝k³` — sont **le
même spectre invariant d'échelle**, exprimé dans la source `g₀`, dans la donnée radiative `g₃`,
ou dans le stress `⟨T⟩`. Le `k³` côté `g₃` n'est **pas** une croissance UV : c'est l'invariance
d'échelle, la puissance de `k` ne traçant que le changement de variable. La **dichotomie**
(`LC-D3-WCH-GWE §5`) est nette : le **un-point** `⟨g₃⟩=0` = la WCH réalisée ; le **deux-points**
`k³` = le spectre qui pondère la variance — c'est lui que ce chaînon met sous contrôle.

---

## 2. Le finding : la variance est **logarithmique**, pas quartique `[établi — numérique]`

La quantité physique du front (a) est la **variance de cisaillement** sommée sur le spectre
(entrée de `LC-D3-WCH-GWE §8`) :

$$\Omega_\sigma^{\rm tot}\simeq A_T\!\int^{x_{\rm UV}}\!\frac{dx}{x}\,g(x),\qquad
g(x)=\frac{(x\cos x-\sin x)^2}{3x^2},\quad x=k\eta_*,$$

où `g(x)` est le noyau **exact** par mode (`LC-D3-WCH-GWE §1/§8bis`, max `0,3767` à `x≈2,744`),
`A_T` la normalisation invariante d'échelle, `x_UV=k_{\rm UV}\eta_*` la coupure. Le `(kη)⁴/27`
n'est que le *leading* `x≪1`.

**Le point neuf (corrige une lecture du §8 parent).** L'enveloppe grand-`x` de `g` n'est **pas**
décroissante : le terme dominant `x\cos x` du numérateur compense le `x²` du dénominateur, d'où
`g(x)→\cos^2x/3` (oscillant, moyenne `1/6`). La variance ne diverge donc **pas** en `x_UV⁴`
(divergence du *leading*, sans réalité) mais croît **logarithmiquement** :

$$\boxed{\;\Omega_\sigma^{\rm tot}/A_T=\int^{x_{\rm UV}}\frac{dx}{x}\,g(x)=\tfrac16\ln x_{\rm UV}+\beta_\infty,
\qquad \beta_\infty=0{,}04503.\;}$$

L'intercept `β∞=∫_0^1\frac{dx}{x}g+∫_1^\infty\frac{dx}{x}(g-\tfrac16)` est calculé de façon robuste
(décomposition d'enveloppe ; la queue oscillatoire `∝\cos(2x)/x` décroît en `1/x`). Sceau (blocs [2]/[3]) :

| `x_UV=k_UVη_*` | `C(x_UV)=Ω_σ^tot/A_T` (exact) | `(1/6)ln x_UV` | *leading* `(x_UV)⁴/108` (artefact) |
|---|---|---|---|
| `10¹` | `0,436` | `0,384` | `93` |
| `10³` | `1,196` | `1,151` | `9·10⁹` |
| `10⁶` | `2,348` | `2,303` | `9·10²¹` |
| `10²⁰` | `7,72` | `7,68` | `9·10⁷⁷` |
| `10⁶⁰` | `23,07` | `23,03` | `9·10²³⁷` |

La loi `C=(1/6)ln x_UV+β∞` reproduit la quadrature directe à `<10⁻²` sur la plage fiable
(`x_UV≤10⁴`) ; au-delà, la quadrature directe décroche (≈`x_UV/2π` oscillations) et seule la loi
est fiable. **Le noyau exact réduit une divergence `x_UV⁴` à une croissance `\tfrac16\ln x_UV`.**

---

## 3. Le rôle de `N` `[cutoff log-doux établi ; A_T et fixation de N : décision ouverte]`

`N≡S_dS=3π/(Λℓ_P²)~3,3·10¹²²` (`LC-E-PLANCK-RESIDUEL`) intervient **deux fois** :

1. **Coupure UV de la variance.** Le bord céleste porte `N` degrés de liberté **finis**
   (`LC-E`/`LC-D`, même bord `𝓘⁺`) ⟹ longueur d'onde minimale `~ℓ_P`, soit
   `x_UV=√(N/π)=ℓ_dS/ℓ_P≈1,02·10⁶¹` (vérifié identiques au sceau, bloc [4]). D'où

$$\Omega_\sigma^{\rm tot}/A_T=\tfrac16\ln\!\big(\sqrt{N/\pi}\big)+\beta_\infty\approx 23{,}46.$$

   La dépendance du verdict (A) à la coupure est **logarithmique** — extrêmement douce. C'est un
   **durcissement** de `LC-D3-WCH-GWE` : non seulement chaque mode est en (A) (`≤0,377`), mais la
   variance sommée ne croît que comme `\ln N`. `[établi — numérique]`
2. **Normalisation d'amplitude.** `A_T=\mathcal P_h\sim(H/M_P)^2` (au facteur conforme près du
   raccord CCC) rattache `A_T` au **même cercle** `{Λ,H,ℓ_P,N}` de `LC-E`. `[décision ouverte]`

**La circularité de `LC-E` n'est pas brisée** — elle est **localisée** : toute la part non
établie du spectre se reporte sur `A_T` (amplitude) et sur `x_UV=√(N/π)` (coupure log-douce), et
`N=S_dS=(ℓ_dS/ℓ_P)²` présuppose `ℓ_P`. `[à inventer / hors de portée — LC-E §3]`

| rôle de `N` | effet sur le verdict (A) | statut |
|---|---|---|
| coupure UV `x_UV=√(N/π)` | `Ω_σ^tot/A_T≈\tfrac16\ln√(N/π)≈23,5` (log-doux) | **`établi` (num.)** |
| normalisation `A_T~(H/M_P)²` | facteur global ; (A) ssi `A_T≪1` | `décision ouverte` |
| fixation de `N` elle-même | aucune (circularité `LC-E`) | **`à inventer / hors de portée`** |

---

## 4. Conséquence pour le programme `[sans surclassement]`

Pour un crossover à `H` **sous-Planckien** (`A_T≪1`), `Ω_σ^tot≈23,5\,A_T≪0,5` : le spectre est
**contrôlé**, le régime (A) tient pour la **variance** (pas seulement par mode). C'est le contenu
neuf que la coïncidence un-point ne donnait pas — un énoncé sur le **deux-points**.

- **[D3] (du un-point au deux-points).** `LC-D3-WEYL-BUNCHDAVIES` donnait `⟨g₃⟩=0` (WCH réalisée
  au niveau classique) ; ce chaînon contrôle `⟨g₃g₃⟩` (le spectre). La WCH reste une condition
  **un-point/entropie** (Penrose) ; le résidu deux-points est **borné** et log-doux, non un
  obstacle.
- **[A] / front (a).** Maillon deux-points **ajouté** ; A3/A4 **non** dérivés, **non** rouverts.
  (A) reste `formalisable` conditionnel au seul A2 — **inchangé**.
- **[E] (échelle).** Le rôle de `N` est précisé : régulateur log-doux **et** normalisation
  `A_T` ; les deux reportés sur `LC-E` (circularité non brisée). Pas de progrès sur la fixation
  de `N` — ce n'était pas l'objet.
- **`LC-D3-WCH-GWE`.** Le finding **corrige** la lecture du §8 (« variance `~(k_UVη_*)⁴` ») en
  « `~\tfrac16\ln(k_UVη_*)` (noyau exact) ; la forme quartique est *leading* » — cohérent C5.

**Ce que cela ne dit pas (§6.4).** `A_T` n'est pas dérivé ; `N` n'est pas brisé ; le caveat
non-linéaire est entier. Donc « le spectre `k³` est **contrôlé** cond. `A_T≪1` et cadre CCC »,
non « le spectre est **dérivé** ». La porte (ii) reste close ; la synthèse du front (a) ne change pas.

<svg width="100%" viewBox="0 0 680 350" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Du un-point au deux-points : chaîne k³ et variance logarithmique</title>
  <desc>À gauche : la chaîne. Le spectre de strain P_h est invariant d'échelle (constant) ; c'est équivalent à P_g0 proportionnel à k puissance moins 3, à P_g3 proportionnel à k cube, et à la fonction à deux points du tenseur de stress proportionnelle à k cube, avec dimension conforme 3. Quatre visages d'un seul spectre. À droite : la variance de cisaillement Omega_sigma sur A_T. Avec le noyau leading en (k eta) puissance 4, elle diverge en (k_UV eta)^4, ce qui est un artefact. Avec le noyau exact, l'enveloppe tend vers cos carré sur 3, de moyenne un sixième, et la variance croît seulement comme un sixième du logarithme de k_UV eta plus 0,045. Au cutoff holographique racine de N sur pi, environ 10 puissance 61, la variance sur A_T vaut environ 23,5, donc bien inférieure à 0,5 dès que A_T est petit.</desc>
  <rect x="40" y="20" width="600" height="44" rx="9" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.8"/>
  <text x="340" y="40" text-anchor="middle" font-size="13" font-weight="500" fill="#3C3489">Relation d'état BD :  g₃ = −(i/3) k³ g₀    ⟹    le DEUX-POINTS est l'invariance d'échelle vue côté g₃</text>
  <text x="340" y="57" text-anchor="middle" font-size="11" fill="#73726c">successeur du UN-POINT ⟨g₃⟩_BD = 0 (LC-D3-WEYL-BUNCHDAVIES)</text>
  <rect x="40" y="84" width="285" height="234" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="182" y="110" text-anchor="middle" font-size="13.5" font-weight="500" fill="#0F6E56">CHAÎNE — un seul spectre</text>
  <text x="182" y="140" text-anchor="middle" font-size="12" fill="#3d3d3a">𝒫_h = const   (invariant d'échelle)</text>
  <text x="182" y="162" text-anchor="middle" font-size="12" fill="#0F6E56">⟺  P_g₀ ∝ k⁻³</text>
  <text x="182" y="184" text-anchor="middle" font-size="12" fill="#0F6E56">⟺  P_g₃ = ⅑k⁶P_g₀ ∝ k³</text>
  <text x="182" y="206" text-anchor="middle" font-size="12" fill="#0F6E56">⟺  ⟨TT⟩ ∝ k^{2Δ−d} = k³</text>
  <text x="182" y="226" text-anchor="middle" font-size="11" fill="#73726c">(Δ = d = 3, dS/CFT)</text>
  <text x="182" y="258" text-anchor="middle" font-size="11.5" fill="#0F6E56">le k³ = invariance d'échelle</text>
  <text x="182" y="274" text-anchor="middle" font-size="11.5" fill="#0F6E56">côté donnée radiative</text>
  <text x="182" y="298" text-anchor="middle" font-size="11" fill="#73726c">[établi — algèbre]</text>
  <rect x="355" y="84" width="285" height="234" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="497" y="110" text-anchor="middle" font-size="13.5" font-weight="500" fill="#993C1D">VARIANCE — log, pas quartique</text>
  <text x="497" y="138" text-anchor="middle" font-size="11.5" fill="#A32D2D">leading (kη)⁴/27 :  ∝ (k_UVη)⁴  → ∞</text>
  <text x="497" y="154" text-anchor="middle" font-size="10.5" fill="#73726c">(ARTEFACT de troncature — audit C5)</text>
  <text x="497" y="182" text-anchor="middle" font-size="11.5" fill="#993C1D">exact : enveloppe → cos²x/3 (moy. 1/6)</text>
  <text x="497" y="206" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">Ω_σ^tot/A_T = ⅙ ln(k_UVη_*) + 0,045</text>
  <text x="497" y="236" text-anchor="middle" font-size="11.5" fill="#3d3d3a">cutoff N : k_UVη_* = √(N/π) ≈ 10⁶¹</text>
  <text x="497" y="258" text-anchor="middle" font-size="12" font-weight="500" fill="#0F6E56">⟹ Ω_σ^tot/A_T ≈ 23,5</text>
  <text x="497" y="278" text-anchor="middle" font-size="11.5" fill="#0F6E56">≪ 0,5  si  A_T ≪ 1  ⟹ régime (A)</text>
  <text x="497" y="300" text-anchor="middle" font-size="11" fill="#73726c">A_T, N : décision ouverte (circularité LC-E)</text>
</svg>

*Fig. — Du un-point au deux-points. À gauche (vert) : `⟨g₃g₃⟩~k³` est l'invariance d'échelle
exprimée dans `g₃` — quatre visages d'un spectre. À droite (orange) : la variance de cisaillement
croît `\tfrac16\ln(k_UVη_*)` (noyau exact), non `(k_UVη_*)⁴` (artefact *leading*) ; au cutoff
holographique `√(N/π)` elle vaut `≈23,5`, donc `≪0,5` dès que `A_T≪1`. Spectre `k³` contrôlé,
conditionnel à `A_T` et au cadre CCC.*

---

## 5. Format de chaînon

- **Hypothèse testée.** « Le résidu deux-points `⟨g₃g₃⟩~k³` (spectre primordial) est-il
  *contrôlé* — borné, régularisable — sur l'état de Bunch–Davies, et compatible avec le régime
  (A) du pont GWE ? »
- **Outil.** Relation d'état BD `g₃=-(i/3)k³g₀` (FG, `LC-D3-WEYL-BUNCHDAVIES`) ; dictionnaire
  holographique `⟨T⟩=(d/16πG)g₃` (`LC-D-HOLOGRAPHIE-G3`) ; noyau exact `g(x)` (`LC-D3-WCH-GWE`) ;
  compte `N=S_dS` (`LC-E-PLANCK-RESIDUEL`). Sceau `verif_D3_spectre_k3.py` (sympy + numpy/scipy).
- **Critère de réfutation.** *Issue « divergence non régularisable »* : si la variance divergeait
  plus vite que toute coupure raisonnable (p.ex. `(k_UVη_*)⁴` réel) ⟹ l'approche un-point
  échouerait. **Non observé** : noyau exact ⟹ croissance `\tfrac16\ln`, finie au cutoff `N`.
  *Issue « dépendance forte à `N` »* : reportée sur `LC-E` — la dépendance est **log-douce**, la
  part non établie isolée dans `A_T` et la fixation de `N`.
- **Verdict.** Chaîne `⟨g₃g₃⟩~k³` **dérivée** `[établi — algèbre]` ; variance **logarithmique**
  (pas quartique), `C(√(N/π))≈23,46` `[établi — numérique]` ⟹ **spectre `k³` contrôlé**,
  conditionnel à `A_T≪1` et au cadre CCC. Normalisation `A_T` et fixation de `N`
  `[décision ouverte / à inventer]`. Transposition non-linéaire `[décision ouverte]` (caveat parent).

---

## 6. Propagation / housekeeping `[à appliquer — note de reprise séparée]`

À l'enregistrement (cf. `statut_id`), la propagation KB **n'est pas faite** ici (ce fichier est
la note de résultat). À traiter dans une note de reprise/housekeeping dédiée :

1. **`LC-D3-WCH-GWE` §8 / §8 lecture du scan** — **correction de fond** : remplacer
   « variance `Ω_σ^tot~(k_UVη_*)⁴/108·A_T` » par « `~\tfrac16\ln(k_UVη_*)·A_T+β∞·A_T` (noyau
   **exact**) ; la forme quartique est *leading*, hors domaine » — **cohérent audit C5** (même
   nature d'artefact que le « basculement `kη~1,9` »). **Aucune touche** à l'algèbre du pont
   `Ω_σ=(kη)⁴ε²/27` (correcte dans son domaine) ni au verdict (A) par mode.
2. **`LC-00-INDEX`** — nouvelle ligne carte (`LC-D3-SPECTRE-K3`, front (a)/D3, deux-points) +
   changelog (du un-point au deux-points ; finding log-variance ; `C(√(N/π))≈23,5`).
3. **`03_glossaire`** — entrées : *spectre `k³` (deux-points)* ; *variance de cisaillement
   (log, non quartique)* ; *intercept `β∞=0,045`* ; *cutoff holographique `√(N/π)=ℓ_dS/ℓ_P`*.
4. **`LC-AUDIT-VERDICT` §8bis** — bullet : maillon **deux-points** ajouté au contenu de la WCH
   (sans surclassement ; A3/A4 non dérivés).
5. **`LC-02-PROGRAMME`, `LC-04-REFERENCES`** — renvois (réfs déjà en KB : BD 1978, dHSS 2001,
   Strominger 2001, Maldacena 2003 ; Gibbons–Hawking pour `N`).

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D3-WEYL-BUNCHDAVIES` (un-point `⟨g₃⟩=0`, `E_ij=(d/2H)g₃`, relation d'état BD —
le parent direct) ; `LC-D-HOLOGRAPHIE-G3` (`⟨T⟩=(d/16πG)g₃`, `d=3` impair) ; `LC-D3-WCH-GWE`
(noyau exact `g(x)`, pont GWE, entrée spectrale §8 — corrigé par ce chaînon) ;
`LC-E-PLANCK-RESIDUEL` (`N=S_dS`, circularité) ; `LC-D3-FRONT-A-SYNTHESE` (verdict figé,
**inchangé**) ; `LC-WORK-D3-SPECTRE-K3` (étape papier) ; `LC-WORK-D1-E-AMPLITUDE` (passerelle
D1⟷E : l'amplitude `A_T` est le **résidu complet de D1 au niveau gaussien**, la forme `k³`
étant scellée ici ; rattachée à `N` de `[E]` par `A_T~1/C_T~1/N`) ; `LC-AUDIT-VERDICT §6.4`
(discipline).

**Renvoi (2026-06-12, lot de propagation NONLIN-2PT).** `LC-D-NONLIN-2PT` v0.1 (audité à
froid 4/4 ACQUIS, `LC-AUDIT-LOG-NONLIN-2PT`) : la chaîne `k³` scellée ici est **refermée
comme cas particulier** du verrou de forme par invariance — le secteur pair du deux-point
du Weyl rescalé complet est de **dimension 1** et sa forme `k³·Π^TT` est **forcée**
(représentation + OP 2.23), ce qui contient la dérivation du présent chaînon comme
instance ; le secteur impair est de dimension 1 ET contact (aucune amplitude radiative
neuve). Le résidu libre se réduit à la **seule amplitude** `A_T~1/N` (cohérent avec la
passerelle D1⟷E ci-dessus, désormais relevée **par invariance**). Sans surclassement :
le `k³` reste la donnée de Cauchy irréductible pendue à `N` seul ; D1 non clos.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Spectre `k³` / deux-points `⟨g₃g₃⟩`* : invariance d'échelle vue côté donnée radiative ;
  `𝒫_h=const ⟺ P_{g₃}∝k³ ⟺ ⟨TT⟩∝k^{2Δ-d}` (`Δ=d=3`).
- *Variance de cisaillement (log, non quartique)* : `Ω_σ^tot/A_T=\tfrac16\ln(k_UVη_*)+β∞`,
  `β∞=0,045` (noyau exact ; le `(k_UVη_*)⁴` du *leading* est un artefact, C5).
- *Cutoff holographique* : `x_UV=√(N/π)=ℓ_dS/ℓ_P` ; `N=S_dS` (cellules d'horizon, `LC-E`/`LC-D`).

**Références (`LC-04`, en KB).** Bunch & Davies, Proc. R. Soc. A **360**, 117 (1978) ;
de Haro–Skenderis–Solodukhin, CMP **217**, 595 (2001) ; Strominger, JHEP **10** (2001) 034 ;
Maldacena, JHEP **05** (2003) 013 ; Gibbons–Hawking, Phys. Rev. D **15**, 2738 (1977) (`N=S_dS`) ;
Meissner–Penrose, arXiv:2503.24263 (2025) (pont GWE / noyau).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
