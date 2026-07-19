---
id: LC-07-CARTOGRAPHIE
titre: "Cartographie des constantes de croissance micro-causales — la carte avant le postulat"
codename: LC-RACCORD
langue: fr
version: 0.2
date: 2026-06-07
statut_id: provisoire — à aligner sur l'index réel du projet
statut_global: établi (la carte {bundle → λ}) / sélection du bundle close ailleurs (établi sous principes — cf. LC-08/09/10)
maj: "2026-06-07 — v0.1 : carte décidable {bundle → λ}, deux pinceaux, atlas de réfutation. v0.2 : renvois LC-08/09/10 ajoutés. La carte reste `établi` et délibérément non engageante ; mais la « décision ouverte (le bundle) » qu'elle laissait est désormais close en aval — le bundle sériel par-nœud est `établi sous principes` (quantification + scission, LC-10). Le statut épistémique §5 est annoté en conséquence ; contenu de la carte inchangé."
modules_rattachement:
  - "ossature géométrique (constante de branchement, cf. LC-02)"
renvois:
  - LC-02-OSSATURE
  - LC-05-PHI-ENTROPIE
  - LC-06-CINEMATIQUE
  - LC-08-SERIALITE
  - LC-09-GAUSS-SEIDEL
  - LC-10-FERMETURE
  - LC-03-GLOSSAIRE
  - LC-04-REFERENCES
tags_epistemiques:
  - établi
  - formalisable
  - à inventer
  - hors de portée
note_methodo: >
  Document délibérément NON engageant : il cartographie la fonction
  {bundle micro-causal → constante de croissance λ} comme résultat décidable en
  soi, sans trancher quel bundle modélise « l'interaction ». La sélection du
  bundle est reportée (tag « décision ouverte »).
---

# LC-07 — Cartographie des constantes de croissance micro-causales

> **Thèse.** La fonction {règle micro-causale → constante de croissance $\lambda$}
> est un **théorème, calculable exactement**. $\varphi$ n'en est qu'**un point**,
> situé au croisement de deux familles à un paramètre. On dresse la carte ; on
> n'assume aucun bundle.

---

## 0. Pourquoi cartographier avant d'assumer

LC-05 dérive $\varphi$ d'un principe d'entropie *étant donné* l'interdit `11`.
LC-06 prétendait dériver cet interdit ($k=1$) de la finitude de $c$, via l'axe
« aller simple / aller-retour ». Le calcul micro-causal (présent document)
montre que **cet axe était le mauvais** : ce qui sélectionne $\varphi$ est le
couple {comptabilité par-nœud, convention du nouveau-né}, pas le sens du signal.
Avant de réécrire un postulat, on fige donc la carte complète des possibilités —
ce qui est *décidable* — et on isole proprement ce qui restera un *choix*.

---

## 1. Les axes de l'espace des conventions

L'automate génératif minimal (« chaque interaction agrège un nouveau nœud ») :
un nœud porte une phase $p$ ; il **tire** quand $p=0$, **émet un enfant** (phase
initiale $c_0$), puis se remet à $p=\text{REST}$ et redescend chaque tick. Quatre
conventions :

- **comptabilité** : *par nœud* (atomicité, le nœud sérialise — 1 émission/tick)
  vs *par arête* (le nœud multiplexe sur ses $d$ arêtes) ;
- **REST** : nombre de ticks réfractaires après un tir ;
- **$c_0$** : le nouveau-né est *actif* ($c_0=0$, tire dès sa naissance) ou se
  *repose* ($c_0\ge1$) ;
- **$d$** : degré (nombre de canaux d'émission), pertinent en par-arête.

La constante de croissance $\lambda$ est le **rayon spectral de la matrice de
Leslie sur les phases**. C'est exact (pas simulé) et c'est un théorème :
`[établi]`.

---

## 2. La carte (atlas des points calculés)

### 2.1 Par nœud (atomicité, 1 enfant/tick)

| REST | $c_0$ | équation caractéristique | $\lambda$ | nom |
|---|---|---|---|---|
| 1 | 0 | $x^2=x+1$ | $1{,}618034$ | $\varphi$ — nombre d'or |
| 1 | 1 | $x^2=2$ | $1{,}414214$ | $\sqrt2$ |
| 2 | 0 | $x^3=x^2+1$ | $1{,}465571$ | $\psi$ — supergolden |
| 2 | 1 | $x^3=x+1$ | $1{,}324718$ | $\rho$ — nombre plastique |
| 2 | 2 | $x^3=2$ | $1{,}259921$ | $2^{1/3}$ |

### 2.2 Par arête (chaque arête libre tire)

| $d$ | REST | $c_0$ | équation | $\lambda$ | nom |
|---|---|---|---|---|---|
| 2 | 1 | 0 | $x^2=2x+1$ | $2{,}414214$ | $\delta_S=1+\sqrt2$ — argent |
| 2 | 1 | 1 | $x^2=3$ | $1{,}732051$ | $\sqrt3$ |
| 3 | 1 | 0 | $x^2=3x+1$ | $3{,}302776$ | $\tfrac{3+\sqrt{13}}2$ — bronze |
| 3 | 1 | 1 | — | $2{,}000000$ | $2$ |

---

## 3. La structure cachée : deux pinceaux qui se croisent en $\varphi$

Le résultat marquant de la carte : à **nouveau-né actif** ($c_0=0$), $\varphi$
est exactement l'**intersection de deux familles à un paramètre**.

**Pinceau réfractaire** (sériel, $c_0=0$, on fait varier REST $=k$) :

$$x^{\,k+1}=x^{\,k}+1 \quad\Rightarrow\quad \varphi,\ \psi,\ \dots\ \to 1.$$

C'est exactement l'équation maîtresse de LC-06. `[établi]`

**Pinceau métallique** (REST=1, $c_0=0$, on fait varier le parallélisme $d$) :

$$x^{2}=d\,x+1 \quad\Rightarrow\quad \lambda = \frac{d+\sqrt{d^2+4}}{2}\ =\ \text{$d$-ième moyenne métallique.}$$

- $d=1$ (sériel / par-nœud) → **or** $\varphi$,
- $d=2$ (par-arête degré 2) → **argent** $1+\sqrt2$,
- $d=3$ (par-arête degré 3) → **bronze** $\tfrac{3+\sqrt{13}}2 \approx 3{,}303$.

Le **degré de parallélisme = l'indice de la moyenne métallique**. Contraste de
fractions continues : or $=[1;1,1,\dots]$, argent $=[2;2,2,\dots]$.

$$\boxed{\;\varphi = \text{moyenne métallique}(1) = \text{pinceau réfractaire}(k=1)\;}$$

$\varphi$ est donc le **point de croisement unique** : sériel *et* réfractarité
d'un pas. Tout écart sur l'un ou l'autre axe quitte $\varphi$.

---

## 4. Lire la carte (atlas de réfutation)

La carte se lit dans les deux sens. Observer/dériver $\lambda$ contraint le
bundle :

- $\lambda=\varphi$ ⟹ {sériel par-nœud, REST=1, nouveau-né actif}.
- $\lambda=1+\sqrt2$ (argent) ⟹ par-arête degré 2 (multiplexage).
- $\lambda=\sqrt2$ ⟹ par-nœud, REST=1, mais **nouveau-né au repos**.
- $\lambda=\psi$ (supergolden) ⟹ sériel, REST=2.

Réfutabilité nette : une micro-causalité **parallèle par arête** prédit une
moyenne métallique $\ge$ argent, **jamais** $\varphi$. Une convention de
naissance « le nouveau-né se repose » prédit $\sqrt2$. La structure dorée n'est
donc compatible qu'avec un bundle micro-causal **sériel et à naissance active**.

---

## 5. Statut épistémique (ce que la carte fait et ne fait pas)

**Décidé** `[établi]` : la fonction {bundle → $\lambda$} ; chaque cellule a une
équation caractéristique en forme close ; l'atlas est exact (rayons spectraux de
Leslie). Le pinceau réfractaire et le pinceau métallique sont des théorèmes.

**Non assumé** `[décision ouverte → close en aval]` : *quel* bundle modélise
« l'interaction ». La carte ne le tranche pas — c'est délibéré. Ce n'est plus
« à inventer » (on a l'énumération nommée), mais un **postulat physique à justifier**
le jour où l'on voudra fixer $\lambda$.
> **Mise à jour (LC-08/09/10).** Ce postulat a été justifié en aval : le bundle
> {sériel par-nœud, REST $=1$, naissance active} est sélectionné par la
> **quantification de l'interaction** (sauts mono-canal = Gauss–Seidel) et son spectre
> composite fermé par la **propriété de scission**. La carte reste non engageante par
> construction ; mais le point $\lambda=\varphi$ qu'elle situe est désormais
> `établi sous principes` (cf. LC-10).

**Limite** : l'atlas §2 est un échantillon représentatif, non exhaustif (points
$(d,\text{REST},c_0)$ calculés). Les deux pinceaux §3 sont, eux, des familles
complètes.

---

## 6. Conséquence pour LC-06 `[à corriger]`

LC-06 §3/§5 articule la dérivation autour de l'axe **aller simple / aller-retour**.
Le présent calcul le **supersède** : le bon axe est **par-nœud / par-arête** plus
**convention du nouveau-né**. Le « FERMÉ » de LC-05 §8 et la dérivation de LC-06
doivent être ramenés à : « $\varphi$ exige le bundle sériel-naissance-active —
postulat à assumer, non conséquence cinématique de $c$ fini ». Révision de LC-06
recommandée (ou rétrogradation au profit de ce document) ; non effectuée ici pour
respecter la consigne « cartographier avant d'assumer ».

---

## 7. Renvois, glossaire, références

**Renvois.** LC-05 (entropie / $\varphi$), LC-06 (cinématique, à réviser), LC-02
(constante de branchement de l'ossature).

**Glossaire à ajouter (LC-03).**

- *Moyennes métalliques* : $x^2=nx+1$, racine $\tfrac{n+\sqrt{n^2+4}}2$ (or, argent, bronze).
- *Nombre plastique* $\rho$ ($x^3=x+1$), *supergolden* $\psi$ ($x^3=x^2+1$).
- *Comptabilité par-nœud vs par-arête* ; *atomicité causale* ; *convention de naissance* ($c_0$).
- *Pinceau réfractaire* $x^{k+1}=x^k+1$ ; *pinceau métallique* $x^2=dx+1$.

**Références (LC-04).**

- D. Lind & B. Marcus, *An Introduction to Symbolic Dynamics and Coding* (1995).
- V. W. de Spinadel, *The metallic means family* (1999).
- Suites OEIS : A000045 (Fibonacci/or), A000129 (Pell/argent), A000931 (Padovan/plastique).

---

## Appendice — Légende des tags épistémiques

- `établi` — théorème ou fait standard.
- `formalisable` — programme clair, exécution non faite.
- `à inventer` — pont conjecturé, sans preuve.
- `hors de portée` — au-delà des moyens actuels.
- `décision ouverte` — choix de modélisation explicitement reporté.
