---
id: LC-D3-WEYL-BUNCHDAVIES
titre: "Module D / D3 — l'hypothèse de Weyl (C→0) ⟺ l'état de Bunch–Davies ? (test sur un mode TT de dS₄)"
codename: LC-RACCORD
tags: [module-D, D3, weyl, bunch-davies, ds-cft, g3, stress-tensor, fefferman-graham, convergence, D1]
type: chaînon (test de la question dure §6 du raccord ; point de convergence D1 + D3 + [D])
statut: coïncidence WCH–BD établie au niveau un-point (perturbatif, mode TT) / convergence non-linéaire décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (index, programme [D]/[D3], glossaire, refs)
fichier_compagnon: verif_D3_bunchdavies.py
renvois: [LC-D-HOLOGRAPHIE-G3, LC-A-D1-STABILITE-WEYL, LC-A-D1-FACTEUR-CONFORME, LC-A-SURVIE-CONFORME, LC-E-PLANCK-RESIDUEL, LC-D3-WCH-GWE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D3] hypothèse de courbure de Weyl (C→0 au crossover) — objet du test"
  - "[D] holographie / g₍₃₎ = ⟨T⟩ — l'état du bord sélectionne g₍₃₎"
  - "[A]/D1 facteur conforme — la marée g₍₃₎ est le degré de liberté à fixer"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3 — L'hypothèse de Weyl (C→0) ⟺ l'état de Bunch–Davies ?

> **Question dure (§6 du raccord).** `LC-A-D1-STABILITE-WEYL` a montré que la fermeture
> de D1 doit venir de la **marée** `g₍₃₎` (secteur inhomogène, domaine de Weyl/D3), et
> `LC-D-HOLOGRAPHIE-G3` a identifié `g₍₃₎ = ⟨T⟩` d'une CFT céleste, fixé par le **choix
> d'un état** — candidat : le vide de **Bunch–Davies** (dS-invariant). D'où :
> *l'hypothèse de courbure de Weyl (D3 : `C→0` au crossover) coïncide-t-elle avec le
> choix de l'état de Bunch–Davies ?* Si oui, **D1, D3 et [D] convergent sur un seul
> principe**.
>
> **Verdict (calculé, `verif_D3_bunchdavies.py`).** **Oui — au niveau un-point.** Sur un
> mode tensoriel (TT) de de Sitter, le Weyl électrique rescalé à `𝓘⁺` est, *dérivé* (§3) :
> `E_ij = (d/2H) g₍₃₎ ᵢⱼ` (`d=3`). Donc « `C→0` » ⟺ « `g₍₃₎ → 0` ». Or l'état de
> Bunch–Davies donne `⟨g₍₃₎⟩ = 0` (vide dS-invariant, pas de condensat). **Les deux
> fixent `⟨g₍₃₎⟩ = 0`** : coïncidence. La sous-détermination de D1 est levée au niveau de
> la donnée classique, D3 est réalisée, l'état de [D] est sélectionné. **Résidu honnête** :
> au niveau deux-points, `⟨g₍₃₎ g₍₃₎⟩ ~ k³ ≠ 0` (fixé par la conformité) — aucun état n'annule
> les fluctuations, donc WCH est nécessairement une **condition un-point** (entropie), et
> le résidu `k³` est le **spectre primordial invariant d'échelle**. `[un-point établi
> (perturbatif) ; convergence non-linéaire décision ouverte]`

---

## 0. Rôle et garde-fou

Ce chaînon **teste** une équivalence (D3 ⟺ BD) ; il ne ferme pas D1 *au sens fort*. Ce
qui est `établi` (perturbatif) : (i) le lien `E_ij = (d/2H) g₍₃₎` **dérivé** sur le mode
(plus emprunté) ; (ii) la coïncidence un-point `⟨g₍₃₎⟩_{BD} = 0 = g₍₃₎(C→0)`. Ce qui
reste `décision ouverte / à inventer` : la transposition au **crossover** (deux éons
recollés ⟹ état de *raccordement*, pas un simple vide de bord), la non-unitarité de
dS/CFT, et le passage du mode TT linéaire au **non linéaire** complet. On ne surclasse
pas : « D1+D3+[D] convergent » vaut pour la donnée classique d'un mode, pas pour le
recollement non perturbatif.

---

## 1. Le cadre minimal : un mode TT de de Sitter `[formalisable]`

**Pourquoi pas FLRW.** En symétrie FLRW le tenseur de Weyl est identiquement nul
(`LC-A-D1-STABILITE-WEYL` §4 : sceau Weyl FLRW≡0 vs Kasner≠0). La question « `C→0` ? »
y est **vide** : D3 n'y a aucun contenu. Il faut donc le secteur **inhomogène/anisotrope**
où `C≠0`. Le cas le plus propre — où l'état de Bunch–Davies est défini sans ambiguïté —
est une **perturbation tensorielle (TT) de de Sitter**, un mode de graviton.

**Géométrie.** dS₄ planaire en temps conforme `η ∈ (−∞, 0⁻)`, `𝓘⁺` en `η→0⁻` :

$$\mathrm{d}s^2 = \frac{1}{H^2\eta^2}\Big(-\mathrm{d}\eta^2 + (\delta_{ij}+h_{ij})\,\mathrm{d}x^i\mathrm{d}x^j\Big),
\qquad a(\eta) = -\frac{1}{H\eta},\quad \Omega \equiv \frac1a = -H\eta.$$

Frame conforme `ĝ = a^{-2} g = (\eta_{\mathrm{Mink}} + H_{\mu\nu})` (Minkowski + perturbation).
Mode : `h_{ij}(η,x) = A\,\varepsilon_{ij}\,f(η)\,e^{i k\cdot x}`, `\varepsilon_{ij}`
transverse-sans-trace (`k` le long de `x³`, polarisation « + » : `h_{11}=−h_{22}`).

---

## 2. Mode de Bunch–Davies et expansion FG à `𝓘⁺` `[étapes 1–4 du sceau]`

**[1] Le mode BD.** L'équation du mode tensoriel de dS (`a'/a = −1/η`) est
`f'' − (2/η)f' + k^2 f = 0`. Le mode de **Bunch–Davies** (positif-fréquence quand
`η→−∞`)

$$f(\eta) = (1 + i k\eta)\,e^{-i k\eta}$$

en est solution (vérifié symboliquement : le résidu est `0`). `[établi]`

**[2] Expansion de Fefferman–Graham** près de `𝓘⁺` (`η→0`), de `ĝ_{ij} = δ_{ij} + h_{ij}` :

$$f(\eta) = \underbrace{A}_{g_{(0)}} + 0\cdot\eta + \underbrace{\tfrac{A k^2}{2}}_{g_{(2)}}\eta^2
+ \underbrace{\Big(-\tfrac{i A k^3}{3}\Big)}_{g_{(3)}}\eta^3 + \dots$$

Pas de terme `η¹`, **pas de log** (`d=3` impair ⟹ pas d'anomalie). `[établi]`

**[3] Local ⊥ libre.** `g_{(2)}/g_{(0)} = k^2/2` est **polynomial** en `k` (opérateur
local `−\tfrac12\nabla^2` ; on vérifie `g_{(2)} = \tfrac12 k^2 g_{(0)}` = la réponse de
Schouten du fond). `g_{(3)}/g_{(0)} = -\tfrac{i}{3}k^3` contient `|k|=\sqrt{k^2}` :
**non local** — la donnée radiative **libre**. La relation d'état BD est

$$\boxed{\ g_{(3)}(k) = -\tfrac{i}{3}\,k^3\,g_{(0)}(k)\ }\qquad(\text{par polarisation}).$$

**[4] dS/CFT.** Bord `d=3` (`𝓘⁺` spacelike) ; graviton sans masse ⟹ opérateur dual =
tenseur de stress, `Δ = d = 3`. La 2-points conforme `⟨T T⟩(k) ~ k^{2Δ-d} = k^3` —
cohérent avec `g_{(3)} ∝ k^3`. Comptage TT (`d=3`) : `6 − 1 − 3 = 2` polarisations.
`[établi]`

---

## 3. Le Weyl électrique, **dérivé** : `E_ij = (d/2H) g₍₃₎` `[le cœur de v0.1]`

> *Révision sur v1.0 du sceau* : le lien « Weyl rescalé électrique = `g₍₃₎` » n'est plus
> **importé** (de `LC-A`) mais **dérivé** sur le mode, par calcul du tenseur de Weyl
> linéarisé. Aucune entrée externe sur `g₍₃₎` n'est requise.

**(a) Fond.** dS planaire pure est conformément plate : sceau `C_{0101}=0` (Weyl de fond
nul). Tout le Weyl est donc dans la perturbation.

**(b) Weyl linéarisé du mode TT.** Riemann linéarisé (tout-bas, fond Minkowski du frame
conforme) `R_{\mu\nu\alpha\beta}=\tfrac12(\partial_\nu\partial_\alpha H_{\mu\beta}
+\partial_\mu\partial_\beta H_{\nu\alpha}-\partial_\mu\partial_\alpha H_{\nu\beta}
-\partial_\nu\partial_\beta H_{\mu\alpha})$ ⟹ Ricci, puis Weyl `n=4`. Résultats (sceau) :

- Ricci scalaire linéarisé `R = 0` (TT).
- `Ĉ_{0101} = \tfrac{i}{2} A\,k^3\,\eta\,e^{i k(x^3-\eta)}`, `Ĉ_{0202} = -Ĉ_{0101}`
  (sans trace) ; **`Ĉ_{0102}=Ĉ_{0103}=Ĉ_{0303}=0`** : la partie électrique est
  **transverse-sans-trace, 2 polarisations** — la signature du graviton.
- En série, `Ĉ_{0101} = \tfrac{i}{2}k^3\eta + \tfrac12 k^4\eta^2 - \tfrac{i}{4}k^5\eta^3 + \dots`
  : **démarre à `η¹`** ⟹ les pièces locales `g_{(0)}` (`η⁰`) et `g_{(2)}` (`η²`) sont
  **annulées** par l'opérateur de Weyl. Calcul de la décomposition fond⊥marée
  (`STABILITE-WEYL`) : seul le secteur radiatif survit.

**(c) Rescaling à `𝓘⁺`.** Le Weyl électrique physique vaut `E_{ij} = \hat C_{0i0j}` (les
facteurs `Ω` de `C^{\text{phys}}` et de `u^0_{\text{phys}}` s'annulent). On rescale par
`Ω = -H\eta` et on prend `η→0` :

$$\boxed{\ E_{ij}\big|_{\mathcal I^+} \;=\; \frac{d}{2H}\,g_{(3)\,ij}\ }\qquad(d=3),$$

constante de proportionnalité **finie, indépendante de `k` et de `x`** (sceau :
`E^{\text{resc}}_{11}/g_{(3)\,11} = 3/(2H)`). Le `k^3` est identique des deux côtés :
`E_{ij}` et `g_{(3)\,ij}` sont **le même datum TT radiatif**. La dimension de bord `d`
réapparaît, comme dans le dictionnaire `⟨T_{ij}⟩ = (d/16\pi G) g_{(3)}` — trois visages
du même objet (`E`, `g_{(3)}`, `⟨T⟩`).

$$\Rightarrow\quad \text{« } C\to 0 \text{ au crossover »}\ \Longleftrightarrow\ \text{« } g_{(3)}\to 0 \text{ ».}$$

---

## 4. Le test : `g₍₃₎(C→0)` vs `g₍₃₎(BD)` — deux niveaux `[étape 6]`

| niveau | D3 (`C→0`) | Bunch–Davies | comparaison |
|---|---|---|---|
| **un-point** (classique) | `g₍₃₎ = 0` | `⟨g₍₃₎⟩ = 0` (vide dS-invariant, pas de condensat) | **coïncidence** |
| **deux-points** (fluctuation) | — | `⟨g₍₃₎ g₍₃₎⟩ ~ k³` (conforme, `Δ=3`) | résidu `≠0` |

**Un-point — coïncidence.** Via §3, `⟨g₍₃₎⟩ = 0 ⟺ ⟨E_{ij}⟩ = 0 ⟺ ⟨C⟩ → 0` au nouveau
Big Bang. L'état de Bunch–Davies *réalise* l'hypothèse de Weyl pour la **métrique
classique émergente**. Donc :

$$\boxed{\ \text{nouvel éon né dans le vide de Bunch–Davies}\ \Rightarrow\
\langle g_{(3)}\rangle\ \text{unique}\ =0\ :\ \text{ferme D1, fonde D3, instancie [D].}\ }$$

**Deux-points — résidu irréductible (et fécond).** `⟨g₍₃₎ g₍₃₎⟩ ~ k³ ≠ 0` : *aucun* état
non trivial n'annule les fluctuations. « `C ≡ 0` y compris fluctuations » est donc
**impossible** — l'hypothèse de Weyl ne peut être qu'une condition **un-point /
coarse-grained**, ce qui est *exactement* la justification **thermodynamique** de Penrose
(faible *entropie* gravitationnelle, pas champ identiquement nul). Le résidu `k³` est le
**spectre primordial invariant d'échelle** (graviton/scalaire de Bunch–Davies) — un point
de contact direct avec la fenêtre empirique de `[E]` (CMB).

---

## 5. Conséquences pour le programme

- **D1 (fermeture, niveau classique).** La sous-détermination de D1 = liberté de l'état
  du bord (`LC-D`). Le vide de BD fixe `⟨g₍₃₎⟩ = 0` : donnée classique **unique**. C'est
  la première fermeture de D1 agissant sur le **bon** secteur (la marée `g₍₃₎`), après les
  échecs du fond (#5 stabilité) et de l'échelle (Planck).
- **D3 (fondation).** L'hypothèse de Weyl cesse d'être un *posit* : elle est **réalisée**
  par le choix d'état (BD), et son statut correct (un-point/entropie) est éclairci par le
  résidu `k³`.
- **[D] (instanciation).** L'état de la CFT céleste qui engendre la métrique est nommé :
  le vide dS-invariant.
- **Convergence.** `D1 ⊕ D3 ⊕ [D]` se rejoignent sur un énoncé unique — *le nouvel éon
  naît dans le vide de Bunch–Davies* — modulo le recollement non linéaire.
- **Front (a) / crossover (aval `[LC-D3-WCH-GWE v0.2]`).** Le résidu deux-points
  `⟨g₍₃₎ g₍₃₎⟩~k³` (= strain primordial `𝒫_h=k³⟨h₀²⟩~const`, invariant d'échelle `A_T`) est
  précisément l'**entrée spectrale** de l'intégrale de variance de `LC-D3-WCH-GWE` §8 (bloc [7]) :
  c'est lui qui fixe le poids des modes dans `Ω_σ^tot~(k_UV η_*)⁴/108·A_T`. La dichotomie
  un-point / deux-points trouve ici son emploi : le **un-point** (`⟨g₃⟩=0`) = le `Ω_σ` petit que
  voit le noyau homogène ⟹ régime (A) ; le **deux-points** (`k³`) = le spectre dont la **forme
  au-delà du pic CGB** est le verrou restant (`décision ouverte`) du verdict (A).

<svg width="100%" viewBox="0 0 680 350" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>D3 (C→0) ⟺ Bunch–Davies : coïncidence un-point, résidu deux-points</title>
  <desc>Bandeau supérieur : le Weyl électrique rescalé à scri+ est dérivé égal à (d sur 2H) fois g3, ce qui rend C tend vers 0 équivalent à g3 tend vers 0. À gauche, panneau un-point : la valeur moyenne de g3 dans le vide de Bunch-Davies est nulle, égale à g3 imposé par C tend vers 0 ; coïncidence ; les trois principes D1, D3 et module D convergent sur l'énoncé « le nouvel éon naît dans le vide de Bunch-Davies ». À droite, panneau deux-points : la fonction à deux points de g3 se comporte comme k cube, non nulle ; aucun état n'annule les fluctuations ; l'hypothèse de Weyl est donc une condition un-point d'entropie, et le résidu k cube est le spectre primordial invariant d'échelle, en contact avec le CMB et le module E.</desc>
  <rect x="40" y="20" width="600" height="46" rx="9" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.8"/>
  <text x="340" y="40" text-anchor="middle" font-size="13" font-weight="500" fill="#3C3489">Weyl dérivé (mode TT) :  E_ij = (d/2H) g₍₃₎    ⟹    « C→0 »  ⟺  « g₍₃₎→0 »</text>
  <text x="340" y="58" text-anchor="middle" font-size="11" fill="#73726c">g₍₀₎ (source) et g₍₂₎ (Schouten, local) annulés par l'opérateur de Weyl ; reste la marée g₍₃₎</text>
  <rect x="40" y="86" width="290" height="232" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="185" y="112" text-anchor="middle" font-size="13.5" font-weight="500" fill="#0F6E56">UN-POINT — coïncidence</text>
  <text x="185" y="140" text-anchor="middle" font-size="12" fill="#3d3d3a">⟨g₍₃₎⟩₍BD₎ = 0  =  g₍₃₎(C→0)</text>
  <text x="185" y="160" text-anchor="middle" font-size="11" fill="#73726c">vide dS-invariant, pas de condensat</text>
  <text x="185" y="196" text-anchor="middle" font-size="12" fill="#0F6E56">D1   ·   D3   ·   [D]</text>
  <line x1="120" y1="206" x2="185" y2="232" stroke="#1D9E75" stroke-width="1.4"/>
  <line x1="185" y1="206" x2="185" y2="232" stroke="#1D9E75" stroke-width="1.4"/>
  <line x1="250" y1="206" x2="185" y2="232" stroke="#1D9E75" stroke-width="1.4"/>
  <text x="185" y="252" text-anchor="middle" font-size="11.5" font-weight="500" fill="#0F6E56">convergent sur :</text>
  <text x="185" y="276" text-anchor="middle" font-size="11.5" fill="#3C3489">« le nouvel éon naît</text>
  <text x="185" y="292" text-anchor="middle" font-size="11.5" fill="#3C3489">dans le vide de Bunch–Davies »</text>
  <rect x="350" y="86" width="290" height="232" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="495" y="112" text-anchor="middle" font-size="13.5" font-weight="500" fill="#993C1D">DEUX-POINTS — résidu</text>
  <text x="495" y="140" text-anchor="middle" font-size="12" fill="#3d3d3a">⟨g₍₃₎ g₍₃₎⟩₍BD₎ ~ k³  ≠ 0</text>
  <text x="495" y="160" text-anchor="middle" font-size="11" fill="#73726c">fixé par la conformité (Δ=3)</text>
  <text x="495" y="192" text-anchor="middle" font-size="11.5" fill="#993C1D">aucun état n'annule la fluctuation</text>
  <text x="495" y="214" text-anchor="middle" font-size="11.5" fill="#3d3d3a">⟹ WCH = condition un-point</text>
  <text x="495" y="230" text-anchor="middle" font-size="11" fill="#73726c">(entropie — lecture de Penrose)</text>
  <text x="495" y="266" text-anchor="middle" font-size="11.5" font-weight="500" fill="#993C1D">résidu k³ = spectre primordial</text>
  <text x="495" y="286" text-anchor="middle" font-size="11.5" fill="#993C1D">invariant d'échelle</text>
  <text x="495" y="302" text-anchor="middle" font-size="11" fill="#73726c">contact [E] / CMB</text>
</svg>

*Fig. — Le test D3 ⟺ BD. Le Weyl rescalé dérivé (bandeau) ramène D3 à une condition sur
`g₍₃₎`. Un-point (vert) : BD et `C→0` coïncident (`⟨g₍₃₎⟩=0`), faisant converger D1, D3,
[D]. Deux-points (orange) : le résidu conforme `k³` est irréductible — WCH n'est qu'une
condition d'entropie, et le résidu est le spectre primordial.*

---

## 6. Format de chaînon

- **Hypothèse testée.** « L'hypothèse de courbure de Weyl (`C→0` au crossover) coïncide
  avec le choix de l'état de Bunch–Davies ; si oui, D1+D3+[D] convergent. »
- **Outil.** Mode TT de dS₄ ; mode de Bunch–Davies ; expansion de Fefferman–Graham à
  `𝓘⁺` ; **Weyl linéarisé dérivé** (Riemann linéarisé → Ricci → Weyl `n=4`) ; rescaling
  `Ω=−Hη` ; un-point vs deux-points conforme. Sceau `verif_D3_bunchdavies.py` (sympy).
- **Critère de réfutation.** *Issue « écart »* : si `C→0` et BD donnaient des `g₍₃₎`
  différents (au niveau un-point), ce seraient deux principes distincts et la convergence
  tomberait. **Non observé** : les deux fixent `⟨g₍₃₎⟩ = 0`. *Réfutation forte de la
  convergence* : montrer qu'aucune CFT céleste de **raccordement** n'existe au crossover,
  ou que la non-unitarité de dS/CFT interdit un vide de BD bien défini.
- **Verdict.** Lien `E_ij=(d/2H)g₍₃₎` **dérivé** `[établi, perturbatif]`. Coïncidence
  un-point `⟨g₍₃₎⟩_{BD}=0=g₍₃₎(C→0)` `[établi, perturbatif]` ⟹ **D1+D3+[D] convergent**.
  Résidu deux-points `k³` `[établi]` ⟹ WCH = condition un-point + spectre primordial.
  Transposition au crossover non linéaire `[décision ouverte / à inventer]`.

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-A-D1-STABILITE-WEYL` (redirection vers la marée `g₍₃₎` ; fond⊥marée ;
Weyl FLRW≡0 — pourquoi le cadre inhomogène) ; `LC-D-HOLOGRAPHIE-G3` (`g₍₃₎=⟨T⟩` ; fixer
`g₍₃₎` = choisir l'état) ; `LC-A-SURVIE-CONFORME` (données `(g₍₀₎,g₍₃₎)` de Friedrich) ;
`LC-A-D1-FACTEUR-CONFORME` (sous-détermination de D1) ; `LC-E-PLANCK-RESIDUEL` (même bord
`𝓘⁺`, fluctuations ↔ compte holographique). Le lien `g₍₃₎` = Weyl rescalé, jadis admis
de `LC-A`, est désormais **dérivé** ici (§3).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Mode tensoriel de Bunch–Davies* : `f(η)=(1+ikη)e^{−ikη}`, solution TT de dS, vide
  dS-invariant ; donne `⟨g₍₃₎⟩=0` et `⟨g₍₃₎g₍₃₎⟩~k³`.
- *Weyl électrique rescalé à `𝓘⁺` (dérivé)* : `E_ij=(d/2H)g₍₃₎` ; `g₍₀₎`,`g₍₂₎` annulés ;
  `E` = la donnée radiative TT (= la marée). `C→0 ⟺ g₍₃₎→0`.
- *Coïncidence WCH–Bunch–Davies (un-point)* : `⟨g₍₃₎⟩_{BD}=0=g₍₃₎(C→0)` ⟹ convergence
  D1+D3+[D] sur « nouvel éon né dans le vide de BD ».
- *Résidu conforme `k³`* : `⟨g₍₃₎g₍₃₎⟩~k³` irréductible ⟹ WCH = condition un-point
  (entropie) ; résidu = spectre primordial invariant d'échelle.

**Références (`LC-04`, en KB v1.8 — toutes `confirmé`).** Bunch & Davies, Proc. R. Soc.
Lond. A **360**, 117 (1978) ; de Haro–Skenderis–Solodukhin, CMP **217**, 595 (2001) ;
Strominger, JHEP **10** (2001) 034 ; Maldacena, JHEP **05** (2003) 013. (Weyl rescalé :
dérivé au §3 ; cadre Friedrich `(g₍₀₎,g₍₃₎)` : `LC-A`.)

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
