---
id: LC-08-SERIALITE
titre: "La sérialité du devenir comme primitif"
codename: LC-RACCORD
langue: fr
version: 0.4
date: 2026-06-07
maj: "2026-06-07 — v0.2 : dérivation depuis le flot modulaire (§6). v0.3 : bascule — volet d'agent décision ouverte → formalisable (quantification). v0.4 : résidu KMB clos (LC-10 §1.4 bis) — la carte composite k→métallique(k) est `établi` sous la propriété de scission. Le volet d'agent passe à `établi sous principes` (quantification + scission/indépendance) ; plus aucun lemme fini ouvert. φ dérivé de {mono-paramétricité modulaire + quantification}."
statut_id: provisoire — à aligner sur l'index réel du projet
statut_global: volet temporel formalisable (mono-paramétricité du flot modulaire) / volet d'agent ÉTABLI SOUS PRINCIPES (Trotterisation Gauss–Seidel sous quantification ; spectre composite sous scission ; cf. LC-09 v0.3, LC-10 v0.2)
type: note fondationnelle
modules_rattachement:
  - "cadre / fondations (LC-01)"
  - "ossature géométrique (LC-02)"
  - "reformulation modulaire / temps thermique (KMS, Connes–Rovelli)"
renvois:
  - LC-01-CADRE
  - LC-02-OSSATURE
  - LC-05-PHI-ENTROPIE
  - LC-06-CINEMATIQUE
  - LC-07-CARTOGRAPHIE
  - LC-09-GAUSS-SEIDEL
  - LC-10-FERMETURE
tags_epistemiques:
  - établi
  - formalisable
  - à inventer
  - hors de portée
  - décision ouverte
---

# LC-08 — La sérialité du devenir comme primitif

> **Clé de voûte.** Plutôt que poser séparément « $c$ fini » *et* « interaction
> sérielle », on pose **un seul primitif** — la sérialité du devenir — et on lit
> les deux en aval. Statut initial : `décision ouverte` assumée. **Mise à jour
> v0.4** : le volet temporel est `formalisable` (mono-paramétricité du flot
> modulaire, §6) et le volet d'agent **`établi sous principes`** — la quantification
> de l'interaction ferme la Trotterisation Gauss–Seidel, et la propriété de scission
> ferme le spectre composite (`LC-09` v0.3, `LC-10` v0.2). Le primitif n'est donc
> plus *assumé* mais *dérivé* de la structure quantique-modulaire ; plus aucun lemme
> *fini* ouvert, seulement deux conditions principielles (quantification ; scission),
> chacune auto-sélective. Le nœud élémentaire φ est inconditionnel.

---

## 0. Rôle

Cette note place sous LC-05/06/07 leur hypothèse commune. Le calcul de LC-07
montre que $\varphi$ exige un bundle micro-causal **sériel**, et que la finitude
de $c$ ne le donne pas seule. Au lieu de traiter ça comme deux postulats
indépendants, on les unifie en un primitif unique, et on l'**assume**
explicitement. C'est l'option « cartographier puis assumer » — ici, on assume.

---

## 1. Le primitif

> **Énoncé.** *Le devenir advient un acte indivisible à la fois.*

Deux volets indissociables :

- **volet temporel** — la cause est strictement avant l'effet ; un saut causal
  $=$ un tick. Le devenir est *séquentiel*.
- **volet d'agent** — un nœud n'engage qu'**une** interaction par tick
  (atomicité, comptabilité par-nœud).

Le primitif est la version **forte** : acte indivisible *temporellement et par
agent*. `[décision ouverte — posé, non dérivé]`

---

## 2. Volet temporel → $c$ fini

Devenir séquentiel = délai minimal non nul par saut causal = **vitesse de
propagation finie**, $c=\ell/\tau$. Équivalence conceptuelle :

$$\text{« $c$ fini » (relativiste)} \;\Longleftrightarrow\; \text{« la causation est séquentielle » (ontologique).}$$

Devenir simultané ⟺ $c\to\infty$. Ici, $c$ fini **découle** du primitif — l'ordre
d'explication que suggérait l'inversion. `[formalisable]`

---

## 3. Volet d'agent → $\varphi$

Un nœud sériel, contraint d'espacer ses émissions (un enfant par tick + un repos
réfractaire), reproduit la substitution de Fibonacci $\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}$
→ $\varphi$. Précisément, $\varphi$ = bundle {par-nœud, REST $=1$, naissance
active}, intersection du pinceau réfractaire $x^{k+1}=x^k+1$ et du pinceau
métallique $x^2=dx+1$. `[établi étant donné le bundle ; cf. LC-05, LC-07]`

---

## 4. Le point dur : l'agent ne se déduit pas du temporel

$$\boxed{\;c\ \text{fini}\ \not\Rightarrow\ \text{sérialité d'agent}\;}$$

Contre-exemple (calculé, LC-07) : le modèle **par-arête** est temporellement
séquentiel (un saut/tick, donc $c$ fini) **et pourtant** parallèle par nœud → il
donne l'**argent** $1+\sqrt2$, pas $\varphi$. Le volet d'agent doit donc figurer
**explicitement** dans le primitif ; il n'est pas un acquis gratuit de $c$ fini.
**C'est exactement pourquoi le statut est « assumé, non dérivé ».** `[établi]`

### Architecture

<svg width="100%" viewBox="0 0 680 350" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>La sérialité du devenir comme primitif : deux volets</title>
  <desc>La sérialité du devenir, primitif, a deux volets. Le volet temporel équivaut à c fini. Le volet d'agent donne phi sous REST=1 et naissance active. c fini n'implique pas le volet d'agent : le par-arête est parallèle mais a c fini et donne l'argent.</desc>
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
  </defs>
  <rect x="230" y="24" width="220" height="52" rx="10" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text x="340" y="46" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">sérialité du devenir</text>
  <text x="340" y="64" text-anchor="middle" font-size="12" fill="#534AB7">un acte indivisible à la fois</text>
  <line x1="300" y1="76" x2="190" y2="126" stroke="#73726c" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="380" y1="76" x2="490" y2="126" stroke="#73726c" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="70" y="128" width="220" height="52" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.5"/>
  <text x="180" y="150" text-anchor="middle" font-size="14" font-weight="500" fill="#0F6E56">volet temporel</text>
  <text x="180" y="168" text-anchor="middle" font-size="12" fill="#1D9E75">1 saut = 1 tick</text>
  <rect x="390" y="128" width="220" height="52" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.5"/>
  <text x="500" y="150" text-anchor="middle" font-size="14" font-weight="500" fill="#993C1D">volet d'agent</text>
  <text x="500" y="168" text-anchor="middle" font-size="12" fill="#D85A30">1 interaction / nœud / tick</text>
  <line x1="180" y1="180" x2="180" y2="230" stroke="#73726c" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
  <text x="196" y="208" font-size="12" fill="#0F6E56">équivaut à</text>
  <line x1="500" y1="180" x2="500" y2="230" stroke="#73726c" stroke-width="1.5" marker-end="url(#ar)"/>
  <text x="516" y="208" font-size="12" fill="#993C1D">si REST=1</text>
  <rect x="100" y="232" width="160" height="48" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.5"/>
  <text x="180" y="261" text-anchor="middle" font-size="14" font-weight="500" fill="#0F6E56">c fini</text>
  <rect x="420" y="232" width="160" height="48" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.5"/>
  <text x="500" y="252" text-anchor="middle" font-size="14" font-weight="500" fill="#993C1D">φ</text>
  <text x="500" y="270" text-anchor="middle" font-size="12" fill="#D85A30">naissance active</text>
  <line x1="262" y1="256" x2="416" y2="256" stroke="#A32D2D" stroke-width="1.5" stroke-dasharray="6 4"/>
  <line x1="333" y1="249" x2="345" y2="263" stroke="#A32D2D" stroke-width="2"/>
  <line x1="345" y1="249" x2="333" y2="263" stroke="#A32D2D" stroke-width="2"/>
  <text x="339" y="305" text-anchor="middle" font-size="12" fill="#A32D2D">c fini ⇏ agent : le par-arête est parallèle mais a c fini → argent</text>
</svg>

*Fig. — Un primitif, deux volets. Le volet temporel équivaut à $c$ fini ; le
volet d'agent livre $\varphi$. La non-implication (rouge) impose d'inclure le
volet d'agent dans le primitif lui-même.*

---

## 5. Pourquoi un primitif plutôt que deux postulats

- **Économie.** Un primitif unique remplace deux postulats indépendants ($c$
  fini + interaction sérielle).
- **Falsifiabilité.** Un substrat **par-arête** prédirait une moyenne métallique
  $\ge$ argent, **jamais** $\varphi$. Le primitif est donc réfutable.
- **Soudure au programme.**
  - *Ensembles causaux* : la croissance séquentielle classique fait naître les
    éléments *un à la fois* ; « order + number » (Sorkin). Le primitif **est** la
    posture des causal sets. `[établi]`
  - *Connes–Rovelli* : le temps thermique émerge du flot modulaire ; le « un acte
    à la fois » serait l'ombre discrète du tick modulaire. `[à inventer — identification précise]`
  - *(Whitehead)* : « les multiples deviennent un et sont augmentés d'un » — le
    devenir comme procès sériel. (Repère culturel, non technique.)

---

## 6. Tentative de dérivation depuis le flot modulaire (résultat partiel)

**Cible.** Faire passer le primitif de `décision ouverte` à `formalisable` en
dérivant ses deux volets du caractère **mono-paramétrique** du flot modulaire
$\sigma_t$ de Tomita–Takesaki (temps thermique de Connes–Rovelli).

**Volet temporel — dérivé.** $\sigma_t : \mathbb{R} \to \mathrm{Aut}(M)$ est un
groupe à **un** paramètre, de générateur unique (Stone : $K=-\ln\Delta$). Un état
définit *un* flot, donc *une* horloge totalement ordonnée. L'ordering temporel
séquentiel — cœur ontologique du volet temporel — **découle** de la
mono-paramétricité (la métrique « $c$ fini » n'ajoutant que la discrétisation
spatiale de LC-06). `[formalisable]`

**Volet d'agent — non dérivé.** La mono-paramétricité ne donne **pas** « un acte
par nœud par tick » : (i) $\sigma_t$ est un automorphisme *global*, agissant sur
tout $M$ à la fois — structurellement *parallèle* ; (ii) le générateur unique
$K=\sum_e K_e$ peut coupler plusieurs arêtes par unité de temps ; (iii) les
hamiltoniens modulaires sont génériquement **non locaux** (type III$_1$ : flot
ergodique, sans projections minimales, aucun atome), ce qui pousse vers le
*parallèle*. « Un paramètre de temps » $\neq$ « un acte par nœud » : la
mono-paramétricité contraint l'horloge, pas la valence de l'action.
`[échec — la valence n'est pas contrainte]`

**Résidu resserré.** La sérialité d'agent équivaut au choix d'une discrétisation
**séquentielle (Gauss–Seidel)** de $e^{iKt}$ — une arête à la fois, sur l'état
mis à jour — contre **parallèle (Jacobi)** — toutes les arêtes d'un coup, sur
l'ancien état. Même flot continu, combinatoire discrète différente :
Gauss–Seidel → $\varphi$, Jacobi → moyennes métalliques (= par-nœud / par-arête
de LC-07). Le posit passe de « sériel » (vague) à **« le flot modulaire se
Trotterise séquentiellement »** (précis, formalisable).

**Soudure.** Ce résidu coïncide avec les ensembles causaux : la croissance
séquentielle classique (Rideout–Sorkin) ajoute les éléments *un à la fois* —
c'est déjà, littéralement, une discrétisation Gauss–Seidel. `[établi côté CST]`

**Bilan (v0.2 → v0.4).** En v0.2, `LC-08` ne basculait pas entièrement : volet
temporel `formalisable` (mono-paramétricité), volet d'agent `décision ouverte`
*resserrée* (verrou Gauss–Seidel/Jacobi). **Mise à jour v0.4 — bascule complète.**
Le verrou a été fermé (`LC-09` v0.3, `LC-10-FERMETURE`) : la **quantification de
l'interaction** impose le déroulement par sauts mono-canal ($P(\ge 2\text{
sauts}/dt) = O(dt^2)$, table d'Itô diagonale), qui *est* la Trotterisation
**Gauss–Seidel** (sceau B.5 : φ vs argent), et la **propriété de scission** ferme la
carte composite $k\to$ métallique$(k)$ (résidu KMB clos, `LC-10` §1.4 bis). Le
**volet d'agent passe donc à `établi sous principes`**. $\varphi$ est dérivé de
{mono-paramétricité modulaire + quantification}. Plus aucun lemme *fini* ouvert ;
subsistent deux **conditions principielles** (quantification ; scission), ni libres
ni flous, chacune auto-sélective — et le nœud élémentaire φ est inconditionnel
(cf. `LC-10` §3).

---

## 7. Renvois et glossaire

**Renvois.** LC-09 (le dernier verrou : Gauss–Seidel vs Jacobi, route
quantification) ; LC-07 (carte {bundle → $\lambda$}, contre-exemple par-arête) ;
LC-06 (cinématique : $c$ fini ⟹ discrétisation, pas $\varphi$) ; LC-05 (principe
variationnel) ; LC-02 (ossature) ; LC-01 (cadre).

**Glossaire à ajouter (LC-03).**

- *Sérialité du devenir* (primitif) ; *volet temporel* ; *volet d'agent*.
- *Devenir séquentiel* ⟺ $c$ fini.
- *Trotterisation Gauss–Seidel (séquentielle) vs Jacobi (parallèle)* du flot modulaire — sélectionne `φ` vs moyennes métalliques (§6).
- (rappel) *comptabilité par-nœud vs par-arête*.

---

## Appendice — Légende des tags épistémiques

- `établi` — théorème ou fait standard.
- `formalisable` — programme clair, exécution non faite.
- `à inventer` — pont conjecturé, sans preuve.
- `hors de portée` — au-delà des moyens actuels.
- `décision ouverte` — choix de modélisation explicitement reporté ou assumé.
