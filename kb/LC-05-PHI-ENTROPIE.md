---
id: LC-05-PHI-ENTROPIE
titre: "Sélection variationnelle du nombre d'or — dérivation entropique de la constante de croissance"
codename: LC-RACCORD
tags: [phi, entropie, dynamique-symbolique, parry, kms, objet-transverse, sous-programme-phi]
statut: établi (principe variationnel, étant donné REST=1) / sélection du bundle : décision ouverte DANS CE DOCUMENT, close conditionnellement en aval (LC-09 v0.3 / LC-10 v0.2 : « établi sous principes ») — voir §0.1
version: 0.5
langue: fr
maj: "2026-06-07 — v0.5 : réconciliation avec la fermeture du verrou φ (LC-09/LC-10). Ajout du §0.1 (statut post-fermeture, avec garde-fou de portée) et de marqueurs de renvoi en §6/§7/§7-bis/§8 : la sélection du bundle, traitée ici comme `décision ouverte`, a reçu en aval une clôture *conditionnelle* (`établi sous principes`, sous quantification + scission). Le résultat variationnel propre à ce document (φ = débit d'entropie maximal étant donné REST=1) est inchangé et reste `établi`. v0.4 : harmonisation front-matter ; renvoi LC-08."
renvois: [LC-01-CADRE, LC-02-OSSATURE, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-06-CINEMATIQUE, LC-07-CARTOGRAPHIE, LC-08-SERIALITE, LC-09-GAUSS-SEIDEL, LC-10-FERMETURE]
modules_rattachement: ["RG (flot, points fixes)", "reformulation modulaire de la cohérence (Tomita–Takesaki / KMS)"]
historique:
  - "v0.2 : tableau §7 corrigé (famille du gap minimal) ; §7-bis « k=1 dérivé de c » et §8 « FERMÉ » = surinterprétation."
  - "v0.3 : §6 H2, §7, §7-bis, §8 réalignés sur LC-06 v0.2 / LC-07."
  - "v0.4 : harmonisation front-matter LC-RACCORD ; renvoi LC-08."
  - "v0.5 : réconciliation post-fermeture (§0.1 + marqueurs §6–8). La `décision ouverte` du bundle est close *conditionnellement* en aval (LC-09/LC-10) ; l'analyse de non-dérivation de §6–8 reste exacte (c fini ⇏ φ) ; le résultat variationnel reste `établi`. Lève la contradiction LC-05 ↔ LC-10 relevée en revue à froid."
---

# LC-05 — Sélection variationnelle du nombre d'or

> **Résultat central.** Sur un branchement à *réfractarité d'un pas*, le débit
> d'entropie est maximisé en un point unique où la constante de croissance vaut
> exactement le nombre d'or $\varphi$. La constante $\varphi$ n'est donc pas
> *posée* : elle *sort* d'un principe variationnel comme racine de
> Perron–Frobenius. La portée et les limites de cette dérivation sont auditées
> en §6–7.

---

## 0. Position dans le programme

Ce document fige une dérivation interne au programme `LC-RACCORD` :
montrer que la constante de croissance $\varphi$ de l'ossature géométrique
(arbre du nombre d'or, cf. LC-02-OSSATURE) peut être **sélectionnée par un
principe d'entropie maximale** plutôt qu'introduite à la main. L'enjeu
méthodologique est de transformer une intuition de parcimonie (« moindre
effort ») en théorème (§4), puis d'en délimiter honnêtement la validité (§6).

Le pont avec la colonne vertébrale modulaire du programme (états KMS, flot de
Tomita–Takesaki, temps thermique de Connes–Rovelli) est posé en §5 : l'état
d'équilibre du formalisme thermodynamique qui réalise l'extrémum est l'ombre
classique d'un état KMS. C'est ce qui rend ce résultat *partie intégrante* de
l'hypothèse de Connes et non un appendice combinatoire.

---

## 0.1 Statut post-fermeture du verrou φ (réconciliation v0.5) `[lire avant §6–8]`

Ce document a été rédigé **avant** la fermeture du verrou de sérialité d'agent
(LC-09, LC-10). Ses §6, §7, §7-bis et §8 concluent que la sélection de la
profondeur réfractaire $k=1$ — donc de $\varphi$ — est une **`décision ouverte`**
(un *postulat physique sur le bundle micro-causal*, non dérivé de la finitude de
$c$). **Cette analyse reste exacte** : $c$ fini ne donne que la discrétisation, et
le résultat variationnel propre à ce document ($\varphi$ = débit d'entropie maximal
*étant donné* REST $=1$) demeure `établi`.

Ce qui a changé **en aval** : LC-09/LC-10 proposent un **principe physique** qui
sélectionne le bundle — la **quantification de l'interaction** (sauts mono-canal ⟹
Trotterisation Gauss–Seidel) —, fermant la sélection de $\varphi$ au statut
**`établi sous principes`** (sous deux conditions auto-sélectives : quantification ;
scission / indépendance des canaux). La charge de preuve déplacée par §6
(« pourquoi $\varphi$ ? » → « quel bundle ? ») a donc reçu une réponse
*conditionnelle*. Les §6–8 ci-dessous sont **conservés tels quels** comme l'analyse
pré-fermeture (non circulaire et toujours valide) ; leurs tags `décision ouverte`
portent désormais le marqueur « → close conditionnellement en aval ».

> **Garde-fou de portée `[à ne jamais perdre]`.** « établi sous principes » est
> mérité pour (i) le **nœud élémentaire** $\varphi$ ($k=1$ ; ancrage rigoureux
> Bisognano–Wichmann sur le wedge) et (ii) $\varphi$ comme **fait de dynamique
> symbolique** (golden-mean shift, mesure de Parry — le contenu `établi` du présent
> document). La **transposition** de la machinerie modulaire-QFT (Tomita–Takesaki,
> propriété de scission en type III₁, entropie relative d'Araki) à *cette*
> construction n'est, elle, **pas instanciée** : aucune CFT sur S², aucun
> hamiltonien modulaire explicite, aucune algèbre III₁ construite ; les sceaux
> numériques de clôture (LC-10 §1.4 bis) tournent en dimension finie (type I), où
> l'additivité utilisée est automatique. Son **applicabilité** reste donc
> `formalisable` → `à inventer`. La clôture de $\varphi$ est **réelle au plan
> symbolique et au nœud élémentaire**, *conditionnelle au plan QFT*. Ne pas
> sur-lire « $\varphi$ dérivé » comme une dérivation QFT achevée. (Détail :
> LC-10 §1.4 bis — résidu KMB, jouet type I ; §2.2 — point dur B.4, non-unicité des
> unravelings.)

---

## 1. Construction et décisions verrouillées

### 1.1 Système A / système B invariant

On modélise l'interaction d'un système $A$ avec un système $B$ **invariant**
(la « lumière frontière » : la structure nulle, la vitesse limite de
propagation de l'information). $B$ fournit le cône invariant ; $A$ est ce qui
se construit, génération après génération, à l'intérieur. Chaque interaction
$A \leftrightarrow B$ amorce une nouvelle relation, agrégée à ses
prédécesseurs.

### 1.2 Décision V1 — l'arbre du nombre d'or `[verrouillé]`

L'ossature est l'**arbre $\varphi$-branchant**, engendré par la substitution
du nombre d'or (golden-mean shift) :

$$a \mapsto ab, \qquad b \mapsto a.$$

Un nœud de type $a$ porte deux enfants ($a$ et $b$), un nœud de type $b$ en
porte un ($a$). La matrice de substitution est

$$M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\lambda_{\mathrm{PF}}(M) = \varphi = \tfrac{1+\sqrt 5}{2} \approx 1{,}6180.$$

Le nombre de nœuds à la génération $n$ vaut $F_n$ (Fibonacci) et croît comme
$\varphi^{\,n}$. Le *branching number* (au sens de Lyons) vaut exactement
$\varphi$. `[établi]`

Conséquence : propagation **isotrope** au sens de l'homogénéité (auto-similaire
sous la substitution, aucune direction privilégiée), géométrie
**Gromov-hyperbolique** (croissance exponentielle des boules), bord à l'infini
$\partial T$. L'isotropie ici n'est *pas* euclidienne.

### 1.3 Décision V2 — règle d'accès causal `[verrouillé]`

$X_n$ accède à l'information de $X_0$ **tant que** leur séparation reste en deçà
de l'horizon causal ; au-delà, le lien dynamique est coupé (cf. §3). Cette règle
fixe le sens causal de la propagation (passé → futur dans le référentiel
étudié).

---

## 2. Géométrie et spectre induits

| Objet | Sur l'arbre $\varphi$-branchant | Statut |
|---|---|---|
| Croissance des boules | $\sim \varphi^{\,r}$ (exponentielle) | `établi` |
| Courbure effective | négative (hyperbolique, type réseau de Bethe) | `établi` |
| Spectre (adjacence) | **bande** a.c. $\approx[-2\sqrt\varphi,\,2\sqrt\varphi]\approx[-2{,}54,\,2{,}54]$ | `formalisable` |
| Mesure spectrale | type Kesten | `établi` (arbre régulier) / `formalisable` (substitution) |
| Transport | balistique (états étendus, pas de localisation géométrique) | `établi` |
| Bord à l'infini $\partial T$ | **ensemble de Cantor** (chemins infinis descendants) | `établi` |

**Distance spectrale = distance causale.** La fonction de Green décroît
exponentiellement avec la distance de graphe, $G(X_0,X_n;E)\sim
\varphi^{-n/2}$ au centre de bande. La « distance informationnelle »
($-\ln$ de la corrélation) est donc proportionnelle à la distance de graphe,
de pente $\tfrac12\ln\varphi \approx 0{,}241$ (longueur de corrélation
$\xi \approx 4$ arêtes). Les deux métriques **coïncident** — ce que le choix de
l'arbre (vs. la chaîne quasi-périodique à spectre de Cantor) rend possible.
`[formalisable, quasi établi]`

**Relogement de Cantor.** Le choix de l'arbre déplace la structure de Cantor du
*spectre* (où elle aurait vécu pour la chaîne) vers le *bord conforme*
$\partial T$. Les îles asymptotiques (§3) sont des ouverts-fermés de
$\partial T$ — pont naturel avec l'holographie céleste de LC-01-CADRE.
`[formalisable]`

---

## 3. Horizon : mécanisme de de Sitter

La croissance $\varphi^{\,n}$ **est** une expansion de de Sitter. Avec facteur
d'échelle $a_n = \varphi^{\,n}$ et un tick par génération ($c=1$), le temps
conforme s'incrémente de $\mathrm{d}\eta = a_n^{-1} = \varphi^{-n}$, et
**converge** :

$$\eta_\infty = \sum_{k\ge 0}\varphi^{-k}
= \frac{1}{1-\varphi^{-1}} = \frac{1}{2-\varphi} = \varphi^2 \approx 2{,}618.$$

L'horizon des événements comobile depuis la génération $n$ vaut alors, en
nombre d'arêtes :

$$\boxed{\;\Delta\chi_{\mathrm{hor}}(n) = \eta_\infty - \eta_n
= \varphi^{\,2-n}\;}$$

Dès $n=2$ l'horizon vaut exactement 1 arête ; au-delà il passe sous l'arête.
Le **gel causal** est donc rapide et inévitable lorsque l'expansion est liée à
la croissance ($H=\ln\varphi$). `[formalisable — hypothèses explicites : $a_n=\varphi^n$, un tick/génération]`

**Îles.** Une fois les horizons refermés, les systèmes se fragmentent en
composantes connexes sous la relation d'**atteignabilité future** (plus de
borne supérieure commune), tout en restant connexes sous l'ordre **ancestral**
(borne inférieure commune, racine unique). D'où la réponse au paradoxe
apparent : *globalement liés par l'héritage, localement séparés pour
l'interaction future*. Ce sont deux ordres distincts sur le même poset, sans
contradiction. Structure de patches de de Sitter. `[formalisable]`

---

## 4. La fonctionnelle d'entropie et son extrémum

> C'est le cœur du document : la dérivation de $\varphi$.

### 4.1 Alphabet et contrainte

Par nœud et par tick, deux symboles : `1` (le nœud interagit / branche), `0`
(il se repose). **Contrainte unique :** pas de `11` — un nœud qui vient
d'interagir ne peut pas réinteragir au tick suivant. C'est une *réfractarité
d'un pas*. (Origine physique candidate : la vitesse limite — voir §6–7.)

### 4.2 La fonctionnelle

Mesure de Markov la plus générale sur le sous-décalage : depuis `0`, brancher
avec probabilité $p$, se reposer avec $1-p$ ; depuis `1`, transition forcée
vers `0`. Distribution stationnaire $\pi_0 = \tfrac{1}{1+p}$,
$\pi_1 = \tfrac{p}{1+p}$. Le débit d'entropie de Kolmogorov–Sinai par tick est :

$$h(p) \;=\; \frac{-\,p\ln p \;-\;(1-p)\ln(1-p)}{1+p}.$$

Lecture : le numérateur est l'entropie du choix en `0` ; le dénominateur
$(1+p)$ est le **prix de la réfractarité** — chaque `1` traîne un `0` forcé qui
ne porte aucune entropie et dilue le débit.

### 4.3 L'extrémum

$$p^\star = \frac{1}{\varphi^2} = 2-\varphi \approx 0{,}3820,
\qquad
h(p^\star) = \ln\varphi \approx 0{,}4812\ \text{nat}.$$

De façon équivalente, les **cotes** optimales repos/branchement valent le
nombre d'or :

$$\frac{1-p^\star}{p^\star} = \varphi.$$

Comparaison : **sans** contrainte, l'optimum serait $p=\tfrac12$ et le débit
$\ln 2 \approx 0{,}6931$. La réfractarité abaisse le maximum de $\ln 2$ à
$\ln\varphi$. **$\varphi$ est le prix prélevé par la contrainte d'un pas sur le
désordre maximal.** (Vérification numérique : appendice A.)

### 4.4 Le théorème sous-jacent `[établi]`

Ce n'est pas une coïncidence arithmétique. Par le **principe variationnel du
formalisme thermodynamique** (Ruelle–Bowen), pour un sous-décalage de type
fini :

$$\sup_{\mu}\, h_\mu \;=\; h_{\mathrm{top}} \;=\; \ln \lambda_{\mathrm{PF}},$$

et le supremum est atteint par une **unique** mesure invariante, la **mesure de
Parry**. Ici $\lambda_{\mathrm{PF}}=\varphi$ ; la mesure de Parry a pour
transitions $P_{00}=1/\varphi$, $P_{01}=1/\varphi^2$, $P_{10}=1$, $P_{11}=0$,
soit précisément $p^\star=1/\varphi^2$. La tranche markovienne $h(p)$ de §4.2
ne fait que réaliser à la main ce que le théorème garantit.

---

## 5. Pont avec l'hypothèse de Connes

Ce qui rattache le résultat à la colonne modulaire du programme :

1. **État d'équilibre = état KMS.** Les états d'équilibre du formalisme
   thermodynamique (mesures de Gibbs / Parry) sont l'analogue classique exact
   des états KMS. Le principe variationnel (max d'entropie, ou de pression) est
   l'ombre classique de la condition KMS. `[établi]`

2. **Temps thermique (Connes–Rovelli).** Dans le programme, le « temps » émerge
   du flot modulaire de Tomita–Takesaki de l'état sur l'algèbre d'observables.
   Le *tick* de la construction (un pas de propagation à la vitesse limite) est
   le candidat naturel pour s'identifier au paramètre du flot modulaire ; alors
   $\ln\varphi$ est la **densité d'entropie de l'état KMS** associé. `[à inventer — c'est le pont à construire]`

3. **Type III et horizons.** En théorie quantique des champs, l'algèbre à
   travers un horizon est de type III$_1$ ; le flot modulaire y est le flot de
   bord / de de Sitter. Les îles de §3 correspondraient à la factorisation de
   l'algèbre à travers l'horizon des événements. `[établi en AQFT ; application ici formalisable]`

4. **Cohérence avec LC-02-OSSATURE.** Le « modular detailed balance KMS » qui
   apparaît dans le durcissement V3 du champ dissipatif $D_x$ (Carlen–Maas
   gradient flow) est *la même condition KMS* que celle invoquée ici. Les deux
   sections doivent partager une entrée de glossaire commune (cf. §9).

---

## 6. Audit épistémique : dérivé vs posé

**Dérivé (solide, non circulaire).** *Étant donnés* l'alphabet
{brancher, reposer} et l'interdit d'un pas, le débit d'entropie maximal vaut
$\ln\varphi$, atteint par une mesure unique. $\varphi$ **sort** du calcul comme
racine de Perron ; il n'y entre pas. Aucune hypothèse « Fibonacci » n'est faite
à ce stade.

**Posé (les deux hypothèses porteuses).**

- **H1 — principe.** Le bon objet à extrémiser est le *débit* d'entropie par
  tick (et non l'entropie par branchement, qui donnerait autre chose).
  Défendable (« macroétat le plus générique par unité de temps de
  propagation »), mais c'est un choix. `[formalisable]`
- **H2 — contrainte.** La réfractarité est d'**exactement un pas**. C'est elle
  qui fixe $\varphi$. Pour une profondeur $k$, on obtient la racine de Perron de
  l'équation maîtresse $x^{k+1}=x^k+1$, *décroissant* de $\varphi$ ($k=1$) vers
  $1$ ($k\to\infty$) ; le cas sans contrainte ($k=0$) donne $2$. $\varphi$ est
  donc le **maximum des cas réfractaires** ($k\ge1$). H2 **n'est pas dérivée**
  de la finitude de $c$ : $c$ fini ne donne que la discrétisation (le tick). La
  valeur $k=1$ — et donc $\varphi$ — exige un **bundle micro-causal posé**
  {sériel par-nœud, REST $=1$, naissance active} ; la carte complète des bundles
  est en LC-07. `[décision ouverte ici → close conditionnellement en aval : LC-09/LC-10, « établi sous principes » sous quantification + scission ; cf. §0.1]`

**Non-circularité.** La dérivation ne produit pas $\varphi$ « à partir de
rien » : elle **déplace la charge de la preuve** de « pourquoi $\varphi$ ? »
vers « quel bundle micro-causal ? » (cf. LC-07). C'est un progrès réel — la
question résiduelle est physique et à choix fini, donc attaquable — mais ce
n'est **pas** une démonstration au sens fort : $\varphi$ reste conditionnel au
bundle sériel à naissance active.
*(Mise à jour v0.5 : la « question résiduelle physique » — quel bundle ? — a depuis
reçu une réponse **principielle** (la quantification de l'interaction) en
LC-09/LC-10, portant la sélection à `établi sous principes`. La non-circularité
ci-dessus est ainsi confortée, pas infirmée ; cf. §0.1.)*

---

## 7. Verdict et prédiction réfutable

**Verdict.** « Moindre effort → théorème » est recevable **si et seulement si**
(i) on adopte le max de débit d'entropie comme principe (H1, énonçable), et
(ii) on fixe la profondeur réfractaire $k=1$. (i) est une convention
raisonnable ; (ii) **n'est pas dérivée de la finitude de $c$** — $c$ fini ne
donne que la discrétisation. $k=1$ (et donc $\varphi$) résulte d'un **bundle
micro-causal posé** {sériel par-nœud, REST $=1$, naissance active} ; tout autre
bundle déplace $\varphi$ (par-arête → moyennes métalliques $\ge$ argent ;
naissance au repos → $\sqrt2$ ; REST $\ge2$ → supergolden …). Voir LC-06 v0.2 et
la carte LC-07. Le statut honnête est donc **parcimonie falsifiable conditionnée
à un postulat nommé**, *pas* un théorème au sens fort.
*(Mise à jour v0.5 : le « postulat nommé » — le bundle sériel — est désormais
**sélectionné par un principe physique** (quantification de l'interaction) en
LC-09/LC-10, ce qui porte la sélection à `établi sous principes` (sous
quantification + scission). Le verdict ci-dessus reste exact en tant qu'analyse
*indépendante de ce principe* : sans lui, $\varphi$ demeure conditionnel au bundle.
Le résultat variationnel (φ = débit d'entropie maximal étant donné REST $=1$) est,
lui, inchangé et `établi`. Cf. §0.1.)*

**Prédiction réfutable.** La constante de croissance est la **racine de Perron de
l'équation maîtresse** $x^{k+1}=x^k+1$ (le « pinceau réfractaire »), où $k$ =
profondeur réfractaire (gap minimal entre interactions, en ticks) :

| profondeur réfractaire | $k$ | équation | $\lambda_k$ | $\ln\lambda_k$ |
|---|---|---|---|---|
| aucune contrainte | 0 | $x=2$ | $2$ | $0{,}693$ |
| **un pas** (REST $=1$) | **1** | $x^2=x+1$ | $\varphi\approx1{,}618$ | $0{,}481$ |
| deux pas (REST $=2$) | 2 | $x^3=x^2+1$ | $\psi\approx1{,}466$ (supergolden) | $0{,}382$ |
| … | $\to\infty$ | | $\to1$ | $\to0$ |

Ce tableau n'est qu'**un** des deux pinceaux : varier le parallélisme (par-arête,
degré $d$) donne le **pinceau métallique** $x^2=dx+1$ (or, argent, bronze …).
$\varphi$ est l'intersection des deux. Carte complète et atlas de réfutation :
**LC-07**.

> **Note historique (v0.1 → v0.3).** v0.1 : mauvaise famille (« pas de run de `1`
> trop long », $\lambda\nearrow2$, faux « tribonacci $1{,}839$ »). v0.2 : famille
> du gap minimal ($\lambda\searrow1$, $k=2=\psi\approx1{,}466$). v0.3 : on retire
> l'attribution de $k$ à un « délai aller simple / aller-retour » — cet axe ne
> contrôle pas $k$ (cf. LC-06 v0.2 / LC-07).

Énoncé réfutable (corrigé) : $\varphi$ est la signature d'un **bundle sériel
par-nœud à naissance active, REST $=1$** ; un bundle parallèle par-arête prédit
une moyenne métallique $\ge$ argent, jamais $\varphi$.

---

## 7-bis. Ce que la cinématique impose (et ce qu'elle n'impose pas)

**Imposé (robuste).** $B$ invariant ⟹ vitesse unique $c$ ; pas de réseau $\ell$
⟹ échelle de temps $\tau=\ell/c$ ⟹ **discrétisation** (un tick). Si
$c\to\infty$, $\tau\to0$ et la discrétisation se dissout (régime trivial
$\lambda=2$). `[formalisable]` *(Caveat : l'unicité de l'échelle présuppose $H$
lié à la construction — cf. décision ouverte §8.)*

**Non imposé.** La valeur de $\lambda$. La finitude de $c$ ne sélectionne **pas**
$k=1$. Le calcul micro-causal explicite (LC-07) montre que $\lambda$ dépend d'un
*bundle* à trois leviers : comptabilité **par-nœud / par-arête** (décisif),
convention de **naissance** ($c_0$), et **REST**. $\varphi$ correspond au seul
bundle {sériel par-nœud, REST $=1$, naissance active} ; il est l'intersection du
pinceau réfractaire $x^{k+1}=x^k+1$ et du pinceau métallique $x^2=dx+1$.

**Statut.** $\varphi$ est donc un **postulat physique sur ce qu'est une
interaction** (acte sériel d'un nœud, descendance immédiatement active), non une
conséquence cinématique de $c$ fini. `[décision ouverte ici → close conditionnellement en aval : LC-09/LC-10 (« établi sous principes »), le « postulat sur ce qu'est une interaction » étant identifié à la quantification ; cf. §0.1]`

> **Rectification v0.3.** La v0.2 présentait ici une « dérivation de $k=1$ » via
> l'axe « sens unique / aller-retour ». Cet axe est erroné (il ne contrôle pas
> $k$). Détail, illustration sériel-vs-parallèle et carte : **LC-06 v0.2** et
> **LC-07**.

---

## 8. Décisions ouvertes / prochain verrou

- **[DÉCISION OUVERTE en v0.3 → CLOSE CONDITIONNELLEMENT en v0.5]** Choix du
  **bundle micro-causal** qui fixe $\lambda$ : comptabilité par-nœud (→ $\varphi$)
  vs par-arête (→ moyennes métalliques) ; naissance active (→ $\varphi$) vs au repos
  (→ $\sqrt2$) ; REST (→ $\varphi$, $\psi$, …). $c$ fini ne tranche pas. *(Le
  « FERMÉ » de la v0.2 était une surinterprétation ; la réouverture v0.3 était
  correcte.)* **Mise à jour v0.5** : la sélection du bundle a reçu une **clôture
  principielle** en LC-09/LC-10 — la **quantification de l'interaction** sélectionne
  {sériel par-nœud, naissance active} (sauts mono-canal ⟹ Gauss–Seidel), et la
  **scission** ferme le spectre composite. Statut porté à **`établi sous principes`**
  (conditions auto-sélectives : quantification ; scission). Subsiste comme *vraie*
  décision/limite : l'**applicabilité** de la transposition QFT à cette construction
  (`formalisable → à inventer`, cf. garde-fou §0.1). Carte : LC-07.
- **[OUVERT — seule `décision ouverte` encore *active* de la pile φ]** $H = \ln\varphi$
  (expansion liée à la construction) **ou** $H$ libre (gel graduel) ? Le résultat
  d'horizon §3 suppose le premier. (Cf. LC-06 §1 caveat, LC-00 encadré.)
- **[OUVERT]** Opérateur d'**adjacence** (bande centrée) ou **laplacien** (gap
  spectral = masse effective) ? Affecte la pente $\tfrac12\ln\varphi$ de §2.
- **[À FORMALISER]** Construire explicitement le pont KMS de §5.2 (tick ↔ flot
  modulaire). *(v0.5 : partiellement abouti — la mono-paramétricité du flot modulaire
  dérive le volet temporel, LC-08 §6 ; l'identification précise tick ⇄ temps thermique
  de Connes–Rovelli reste `à inventer`.)*

---

## 9. Renvois et entrées de glossaire à créer

**Renvois.**

- LC-01-CADRE — holographie céleste, bord conforme (relogement de Cantor, §2).
- LC-02-OSSATURE — arbre / fibré de Hilbert ; champ dissipatif $D_x$ et KMS
  modular detailed balance (§5.4).
- LC-03-GLOSSAIRE — entrées à ajouter ci-dessous.
- LC-04-REFERENCES — références ci-dessous.

**Entrées de glossaire à rédiger (LC-03).**

- *Golden-mean shift* / sous-décalage du nombre d'or.
- *Mesure de Parry* (mesure de Markov d'entropie maximale).
- *Valeur propre de Perron–Frobenius* ; *branching number* (Lyons).
- *État d'équilibre / pression* (formalisme thermodynamique).
- *Condition KMS* ; *flot modulaire de Tomita–Takesaki* ; *temps thermique*.
- *Réfractarité* (contrainte d'un pas).

**Références à intégrer (LC-04).**

- W. Parry, *Intrinsic Markov chains*, Trans. AMS (1964) — mesure de Parry.
- D. Ruelle, *Thermodynamic Formalism* (1978).
- R. Bowen, *Equilibrium States and the Ergodic Theory of Anosov Diffeomorphisms* (1975).
- D. Lind & B. Marcus, *An Introduction to Symbolic Dynamics and Coding* (1995).
- A. Connes & C. Rovelli, *Von Neumann algebra automorphisms and time–thermodynamics relation…*, Class. Quantum Grav. 11 (1994).
- R. Lyons, *Random walks and percolation on trees*, Ann. Probab. (1990) — branching number.
- H. Kesten, *Symmetric random walks on groups*, Trans. AMS (1959) — mesure spectrale sur arbres.

---

## Appendice A — Vérification de l'extrémum

Condition de stationnarité de $h(p)=N(p)/D(p)$ avec $N=-p\ln p-(1-p)\ln(1-p)$,
$D=1+p$ :

$$h'(p)=0 \iff N'(p)\,(1+p) = N(p), \qquad N'(p)=\ln\frac{1-p}{p}.$$

En $p^\star=1/\varphi^2$ : $1-p^\star = 1/\varphi$ (car $\varphi^2-1=\varphi$),
donc $\dfrac{1-p^\star}{p^\star}=\varphi$ et $N'(p^\star)=\ln\varphi$. Alors

$$\text{membre gauche} = (1+\varphi^{-2})\ln\varphi = \frac{\varphi^2+1}{\varphi^2}\ln\varphi,
\qquad
N(p^\star) = \frac{\varphi+2}{\varphi^2}\ln\varphi.$$

Comme $\varphi^2+1 = \varphi+2$, les deux membres sont égaux. La condition
d'extrémalité se réduit donc exactement à $\dfrac{1-p}{p}=\varphi$, et la valeur
extrémale est $h(p^\star)=\ln\varphi$. $\square$

Valeurs de contrôle : $h(0{,}30)\approx0{,}470$ ; $h(p^\star)\approx0{,}4812$ ;
$h(0{,}50)\approx0{,}4621$ ; $\ln\varphi=0{,}48121\ldots$

## Appendice B — Légende des tags épistémiques

- `établi` — théorème ou fait standard, démontré dans la littérature.
- `formalisable` — programme clair, outils identifiés, exécution non faite.
- `à inventer` — pont conjecturé, sans preuve ni construction.
- `hors de portée` — au-delà des moyens actuels du programme.
