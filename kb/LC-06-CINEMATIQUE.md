---
id: LC-06-CINEMATIQUE
titre: "Cinématique micro-causale et sélection du bundle — ce que la finitude de c impose vraiment"
codename: LC-RACCORD
langue: fr
version: 0.2
date: 2026-06-07
statut_id: provisoire — à aligner sur l'index réel du projet
statut_global: formalisable (la discrétisation) / décision ouverte (le bundle)
modules_rattachement:
  - "ossature géométrique (constante de branchement, cf. LC-02)"
  - "module reformulation modulaire / KMS (le tick comme paramètre de flot)"
renvois:
  - LC-01-CADRE
  - LC-02-OSSATURE
  - LC-03-GLOSSAIRE
  - LC-04-REFERENCES
  - LC-05-PHI-ENTROPIE
  - LC-07-CARTOGRAPHIE
journal:
  - "v0.1 : dérivation autour de l'axe « aller simple / aller-retour » — ERRONÉE."
  - "v0.2 : axe corrigé en « par-nœud / par-arête » + « convention du nouveau-né » ; le « FERMÉ » de LC-05 §8 est retiré ; voir LC-07 pour la carte complète."
tags_epistemiques:
  - établi
  - formalisable
  - à inventer
  - hors de portée
  - décision ouverte
---

# LC-06 — Cinématique micro-causale et sélection du bundle

> **Résultat (v0.2, corrigé).** La finitude de $c$ impose la **discrétisation**
> (un tick fini), mais **ne sélectionne pas $\varphi$** à elle seule. $\varphi$
> exige un *bundle micro-causal* précis — {sériel par-nœud, REST $=1$, nouveau-né
> actif} — qui est un **postulat physique**, pas une conséquence cinématique.
> Le « verrou fermé » annoncé en v0.1 était une surinterprétation : il est
> retiré. La carte complète des bundles vit dans LC-07.

---

## 0. Avertissement de révision

La v0.1 prétendait dériver $k=1$ de la finitude de $c$ via l'axe « aller simple
vs aller-retour ». Le calcul micro-causal explicite (LC-07) montre que cet axe
est **le mauvais** : le sens du signal n'est pas le levier. Les vrais leviers
sont la **comptabilité** (par-nœud vs par-arête) et la **convention de
naissance**. Ce document est réécrit autour de ces axes ; le « FERMÉ » de
LC-05 §8 redevient une **décision ouverte**.

---

## 1. Ce que la finitude de c impose : la discrétisation

$B$ invariant ⟹ vitesse unique $c$ ; pas de réseau unique $\ell$ ⟹ une échelle
de temps $\tau=\ell/c$. La discrétisation (un tick $=\tau$) est ainsi une
conséquence directe et **robuste** de $c$ fini : si $c\to\infty$, $\tau\to0$ et
la discrétisation se dissout (régime trivial $\lambda=2$). `[formalisable]`

> **Caveat (cohérence inter-doc).** L'unicité de l'échelle de temps présuppose
> que $c$ et $\ell$ sont les *seules* grandeurs. Or LC-05 §3 introduit un taux
> d'expansion $H$. Si $H$ est libre, il y a deux échelles et $\tau$ n'est plus
> unique. L'argument de §1 **présuppose donc $H$ lié à la construction**
> ($H=\ln\lambda/\tau$) — décision encore ouverte, couplée à celle-ci.

Ce que $c$ fini **n'impose pas** : la valeur de la constante de croissance
$\lambda$. Celle-ci dépend du *bundle* micro-causal (§2–4).

---

## 2. Le bon axe : comptabilité et naissance

Automate génératif minimal (« chaque interaction agrège un nœud ») : un nœud
porte une phase $p$ ; il **tire** quand $p=0$, **émet un enfant** (phase initiale
$c_0$), puis se remet à $p=\text{REST}$ et redescend chaque tick. Les leviers qui
fixent $\lambda$ :

- **A1 — Comptabilité.** *Par nœud* (atomicité : le nœud sérialise, 1
  émission/tick) **vs** *par arête* (le nœud multiplexe sur ses $d$ arêtes).
  **C'est l'axe décisif.** `[décision ouverte]`
- **A2 — Convention de naissance.** Le nouveau-né est *actif* ($c_0=0$, tire dès
  sa naissance) **vs** *au repos* ($c_0\ge1$). `[décision ouverte]`
- **A3 — REST.** Nombre de ticks réfractaires après un tir. `[décision ouverte]`

(L'axe « aller simple / aller-retour » de la v0.1 ne figure plus : il ne contrôle
aucune de ces constantes.)

---

## 3. Sériel vs parallèle : l'illustration du bon axe

La distinction par-nœud / par-arête se voit directement sur le motif d'émission
d'un nœud :

<svg width="100%" viewBox="0 0 680 320" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Sériel (par nœud) vs parallèle (par arête)</title>
  <desc>En comptabilité par nœud, un nœud émet en série un enfant tous les deux ticks, ce qui donne la croissance dorée phi. En comptabilité par arête, le nœud multiplexe sur deux arêtes décalées et émet à chaque tick, ce qui donne la croissance argent 1 plus racine de 2.</desc>
  <line x1="40" y1="40" x2="40" y2="280" stroke="#D3D1C7" stroke-width="0.5"/>
  <text x="60" y="40" font-size="14" font-weight="500" fill="#3d3d3a">par nœud (sériel) — un seul canal</text>
  <circle cx="70" cy="95" r="10" fill="#534AB7"/>
  <text x="90" y="99" font-size="12" fill="#3C3489">nœud x</text>
  <circle cx="180" cy="95" r="7" fill="#1D9E75"/>
  <circle cx="216" cy="95" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="252" cy="95" r="7" fill="#1D9E75"/>
  <circle cx="288" cy="95" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="324" cy="95" r="7" fill="#1D9E75"/>
  <circle cx="360" cy="95" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <text x="400" y="92" font-size="12" fill="#0F6E56">● émet  ○ repos</text>
  <text x="400" y="108" font-size="12" fill="#73726c">1 enfant / 2 ticks</text>
  <text x="60" y="140" font-size="14" font-weight="500" fill="#0F6E56">x² = x + 1  →  λ = φ ≈ 1,618  (or)</text>
  <line x1="40" y1="170" x2="640" y2="170" stroke="#D3D1C7" stroke-width="0.5"/>
  <text x="60" y="195" font-size="14" font-weight="500" fill="#3d3d3a">par arête (parallèle, d = 2) — deux canaux décalés</text>
  <circle cx="180" cy="230" r="7" fill="#D85A30"/>
  <circle cx="216" cy="230" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="252" cy="230" r="7" fill="#D85A30"/>
  <circle cx="288" cy="230" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <text x="120" y="234" font-size="12" text-anchor="end" fill="#993C1D">arête 1</text>
  <circle cx="180" cy="258" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="216" cy="258" r="7" fill="#D85A30"/>
  <circle cx="252" cy="258" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="288" cy="258" r="7" fill="#D85A30"/>
  <text x="120" y="262" font-size="12" text-anchor="end" fill="#993C1D">arête 2</text>
  <text x="330" y="246" font-size="12" fill="#73726c">combiné : émission à chaque tick</text>
  <text x="60" y="300" font-size="14" font-weight="500" fill="#993C1D">x² = 2x + 1  →  λ = 1+√2 ≈ 2,414  (argent)</text>
</svg>

*Fig. — Le nœud sériel (par-nœud) émet un enfant tous les deux ticks → or. En
multiplexant sur deux arêtes décalées (par-arête, d=2), il émet à chaque tick →
argent. Le degré de parallélisme fixe l'indice de la moyenne métallique.*

---

## 4. Les deux pinceaux et leur croisement en φ

À nouveau-né actif ($c_0=0$), $\varphi$ est l'**intersection de deux familles** :

**Pinceau réfractaire** (sériel, REST $=k$ variable) :

$$x^{\,k+1}=x^{\,k}+1 \;\Rightarrow\; \varphi,\ \psi\ (\text{supergolden}),\ \dots\ \to 1.$$

**Pinceau métallique** (REST $=1$, parallélisme $d$ variable) :

$$x^{2}=d\,x+1 \;\Rightarrow\; \lambda=\frac{d+\sqrt{d^2+4}}{2}\quad(\text{$d$-ième moyenne métallique}).$$

- $d=1$ (sériel) → **or** $\varphi$ ; $d=2$ → **argent** $1+\sqrt2$ ; $d=3$ →
  **bronze** $\tfrac{3+\sqrt{13}}2$.

$$\boxed{\;\varphi=\text{métallique}(1)=\text{réfractaire}(k=1)\;}$$

$\varphi$ est le **point de croisement unique** : sériel **et** réfractarité d'un
pas, nouveau-né actif. `[établi — calculé exactement, cf. LC-07]`

La convention de naissance déplace hors des pinceaux : par-nœud REST $=1$ mais
nouveau-né *au repos* donne $\sqrt2$, pas $\varphi$.

---

## 5. Le résidu : un postulat, pas une cinématique

Ce que $c$ fini laisse ouvert se résume à **choisir le bundle** :

1. **A1** : l'interaction est-elle un acte *sériel du nœud* (par-nœud) ou un
   multiplexage sur les canaux (par-arête) ? Sériel → famille dorée ; parallèle
   degré $d$ → moyenne métallique($d$) $\ge$ argent.
2. **A2** : la descendance naît-elle *active* ou *au repos* ? Actif → $\varphi$ ;
   repos → $\sqrt2$.
3. **A3** : REST $=1$ ($\varphi$) ou plus (supergolden, …) ?

Aucun de ces choix n'est forcé par la finitude de $c$. **$\varphi$ exige le
bundle {sériel par-nœud, REST $=1$, nouveau-né actif}**, et ce bundle est un
*postulat physique sur ce qu'est une interaction* — à assumer et justifier, non
à déduire de $c$. `[décision ouverte]`

---

## 6. Énoncé réfutable (corrigé)

$$\boxed{\;\varphi \iff \text{micro-causalité sérielle par-nœud, REST}=1,\ \text{naissance active}.\;}$$

- Micro-causalité **parallèle par arête** ⟹ moyenne métallique $\ge 1+\sqrt2$
  (argent), **jamais** $\varphi$.
- Naissance **au repos** ⟹ $\sqrt2$.
- REST $\ge 2$ ⟹ supergolden $\psi$, plastique $\rho$, … selon la naissance.

Toute dérivation/observation imposant l'une de ces alternatives **réfute** la
sélection de $\varphi$ par cette voie. La structure dorée n'est compatible
qu'avec un substrat micro-causal sériel à naissance active.

---

## 7. Chaîne complète (corrigée)

$$
B \text{ invariant} \;\Rightarrow\; \tau=\tfrac{\ell}{c}\ \text{(discrétisation, robuste)}
\;\Rightarrow\; \lambda=\lambda(\text{bundle})
$$
$$
\text{bundle} = \{\text{sériel par-nœud, REST}=1, c_0=0\} \;\Rightarrow\; \lambda=\varphi\quad(\textbf{postulat, non cinématique}).
$$

Statut : la discrétisation est `formalisable` ; la fonction {bundle → $\lambda$}
est `établi` (LC-07) ; le **choix** du bundle est `décision ouverte`.

---

## 8. Renvois et glossaire

**Renvois.** LC-07 (carte complète {bundle → $\lambda$}, atlas de réfutation) ;
LC-05 (principe variationnel, $\varphi$ comme débit d'entropie maximal *étant
donné* REST $=1$) ; LC-02 (ossature, constante de branchement) ; LC-01 (structure
nulle / cadre).

**Glossaire à ajouter (LC-03).**

- *Comptabilité par-nœud vs par-arête* ; *atomicité causale* ; *convention de naissance* ($c_0$).
- *Pinceau réfractaire* $x^{k+1}=x^k+1$ ; *pinceau métallique* $x^2=dx+1$.
- *Moyennes métalliques* (or, argent, bronze) ; *supergolden* $\psi$ ; *plastique* $\rho$.

---

## Appendice — Légende des tags épistémiques

- `établi` — théorème ou fait standard.
- `formalisable` — programme clair, exécution non faite.
- `à inventer` — pont conjecturé, sans preuve.
- `hors de portée` — au-delà des moyens actuels.
- `décision ouverte` — choix de modélisation explicitement reporté.
