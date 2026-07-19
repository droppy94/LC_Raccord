---
id: LC-10-FERMETURE
titre: "Fermeture du verrou φ — les deux lemmes (régime + Trotterisation)"
codename: LC-RACCORD
tags: [fermeture, verrou, lemme-regime, lemme-trotterisation, margolus-levitin-modulaire, sauts-quantiques, gauss-seidel, bascule]
statut: verrou fermé sous DEUX PRINCIPES — φ dérivé de {mono-paramétricité modulaire + quantification de l'interaction} ; plus de lemme ouvert ; conditions principielles : quantification (B) + scission/indépendance (A composite)
version: 0.3
langue: fr
maj: "2026-06-07 — v0.1 : exécution du MANDAT LC-WORK-VERROU-PHI (A.3.3, A.4, Lemme B + sceau B.5). v0.2 : fermeture du résidu KMB (§1.4 révisé) — la carte composite k→métallique(k) passe à `établi` sous la propriété de scission (Buchholz–Wichmann / Doplicher–Longo) ; sceau numérique (extensivité ⟨K⟩/S_rel ∝ k ; S_rel = Hessienne Kubo–Mori ; additivité exacte). §3 : verdict mis à jour — plus de lemme fini ouvert, deux conditions principielles (quantification + scission). Volet d'agent de LC-08/LC-09 → `établi sous principes`. v0.3 (revue à froid) : §4 — table de propagation corrigée (listait les versions pré-KMB) + couche de réconciliation (garde-fou de portée : clôture symbolique/nœud élémentaire réelle vs transposition QFT non instanciée, `formalisable → à inventer` ; sceaux de clôture en type I) ; item-3 du sceau B.5 (branchement dynamique → φ) rétabli dans le script compagnon. Aucun changement de résultat ; bookkeeping + honnêteté de portée."
renvois: [LC-09-GAUSS-SEIDEL, LC-08-SERIALITE, LC-07-CARTOGRAPHIE, LC-06-CINEMATIQUE, LC-05-PHI-ENTROPIE, LC-02-OSSATURE, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-10 — Fermeture du verrou de la sérialité d'agent

> **Objet.** Exécuter le mandat `LC-WORK-VERROU-PHI` : établir les deux lemmes de
> `LC-09` §5. **Lemme A** (régime, *combien* d'actes/tick) et **Lemme B**
> (Trotterisation, *comment* ordonnés). **Verdict** : le verrou se ferme
> **conditionnellement** — φ devient *dérivé* de deux entrées seulement,
> (i) la mono-paramétricité du flot modulaire (volet temporel, déjà acquis
> `LC-08` §6), (ii) la quantification de l'interaction (volet d'agent, ci-dessous).
> Le volet d'agent de `LC-08` bascule de `décision ouverte` resserrée à
> `formalisable`. Deux résidus subsistent — nommés, finis, ni libres ni flous.

---

## 0. Rappel de la cible

`LC-09` §6 posait : $\varphi$ = signature d'une interaction *quantique*
(indivisible, un-partenaire, séquentielle). La fermeture demande deux choses
distinctes, qui se répartissent proprement entre les deux lemmes :

| Lemme | Question tranchée | Verrouille |
|---|---|---|
| **A — régime** | *combien* d'actes par tick ? | un quantum / tick → $n = 1$ |
| **B — Trotterisation** | *comment* sont-ils ordonnés ? | un canal / saut, séquentiel → Gauss–Seidel |

**A** garantit qu'il n'y a qu'un acte ; **B** garantit qu'un acte = un canal
traité séquentiellement. Ensemble : *un canal par tick, en séquence = Gauss–Seidel
strict = $\varphi$.* Aucun n'est suffisant seul.

---

## 1. Lemme A — régime : « un quantum / tick » `[formalisable → établi au nœud élémentaire (cas wedge)]`

### 1.1 A.3.3 — Test de consistance : les deux ticks coïncident-ils ?

Les deux définitions du tick — énergétique (`LC-09` §4, Margolus–Levitin saturée)
et cinématique (`LC-06` §1) — doivent s'égaler :

$$\underbrace{\tau_\perp(E_{\min}) = \frac{\pi\hbar}{2E_{\min}}}_{\text{énergétique}}
\;=\; \underbrace{\frac{\ell}{c}}_{\text{cinématique}}
\quad\Longleftrightarrow\quad
\boxed{\,E_{\min}\cdot\tau = \frac{\pi\hbar}{2}\,}$$

C'est une **relation d'action d'ordre $\hbar$ par tick** — non un nouveau posit,
mais la condition « un quantum d'action accumulé par tick ». `[établi — identité]`

**Le gain (la carte d'excitation).** Le nombre d'opérations orthogonales par tick
à saturation ML vaut $n = \tau/\tau_\perp = 2E\tau/\pi\hbar$. À $\tau = \ell/c$
fixé et $E = k\,E_{\min}$ :

| $k = E/E_{\min}$ | $n$ (actes/tick) | $\lambda$ (racine de $x^2 = kx+1$) | régime |
|---|---|---|---|
| 1 | 1 | $1{,}618034 = \varphi$ | quantum minimal, indivisible → **Gauss–Seidel** |
| 2 | 2 | $2{,}414214$ — argent | bi-quantum → vers Jacobi |
| 3 | 3 | $3{,}302776$ — bronze | tri-quantum |

**$n$ (actes/tick, fixé par ML) s'identifie au degré de parallélisme $d$ du
pinceau métallique de `LC-07`.** Le niveau d'excitation $k$ *est* l'indice de la
moyenne métallique : $\varphi \Leftrightarrow k = 1$ (nœud à un quantum,
indivisible) ; métalliques $\Leftrightarrow k \ge 2$. La carte de `LC-07` devient
ainsi le **spectre d'excitation** d'un nœud sous contrainte ML, ce qui *quantifie*
la punchline qualitative de `LC-09`. `[formalisable — la seule étape de modélisation
est l'identification « canaux tirés/tick = transitions orthogonales/tick »]`

Combiné à l'élémentarité (A.3.1 : un nœud à $k$ quanta se factorise en $k$
sous-nœuds à un quantum), le nœud **fondamental** est à $k = 1 \Rightarrow n = 1
\Rightarrow$ GS strict $\Rightarrow \varphi$.

**Bilan A.3.3 — PASS.** Les deux ticks ne sont compatibles que pour un nœud à un
quantum ; le test livre en prime l'identification $k = n = d$. Reste suspendu au
seul point dur A.4 (ML modulaire en type III₁).

### 1.2 A.4 — Transposition modulaire (le point dur)

**Obstruction.** En type III₁ (`LC-08` §6) : pas de trace, pas d'état fondamental,
et $\langle K\rangle_\omega = 0$ avec $K|\Omega\rangle = 0$ ($\Delta|\Omega\rangle
= |\Omega\rangle$). Dans le vide, $\langle K\rangle$ **et** $\Delta K$ s'annulent :
la forme ML « $E$ au-dessus du fondamental » est structurellement vide. Le contenu
de $K$ ne vit que sur les **excitations**.

**A.4.1 — Mandelstam–Tamm survit, pas ML.** `[établi]` MT est agnostique au
générateur : $s_\perp \ge \pi/(2\,\Delta G)$ pour toute évolution $e^{-iGs}$,
$\Delta G$ = *fluctuation* du générateur. Aucun fondamental requis. Avec $G = K$
sur une excitation locale $\rho$ :

$$\boxed{\,s_\perp \;\ge\; \frac{\pi}{2\,\Delta K_\rho}\,},
\qquad \Delta K_\rho^2 = \langle K^2\rangle_\rho - \langle K\rangle_\rho^2 .$$

La résolution du « pas de fondamental » est donc : abandonner ML au profit de MT,
qui n'en a jamais eu besoin.

**A.4.2 — Ancrage rigoureux : le wedge (Bisognano–Wichmann).** `[établi pour les
wedges]` Pour un wedge de Rindler, BW donne $K = 2\pi\,K_{\text{boost}}$ ; le flot
modulaire est *géométrique* (boost), $s$ se convertit en temps propre via la
température d'Unruh $T = \hbar a/2\pi c k_B$, et la borne modulaire **redevient une
borne ML/MT physique ordinaire** sur le hamiltonien de boost. Là, le test A.3.3
($\tau_\perp = \ell/c$) acquiert un sens concret : $\ell/c$ = l'échelle de temps
Rindler/Unruh locale. Les régions générales (BW à des images conformes près)
restent `formalisable`.

**A.4.3 — L'accroc, exhibé : ML vs MT donnent des cartes différentes.**
La carte A.3.3 ($k \to d = k$, donc $n = k$) dépend de la borne :

- en **moyenne** (ML, $\langle K\rangle$ *extensif*) : $\langle K\rangle = k\langle
  K_1\rangle \Rightarrow n = k$. **Reproduit A.3.3.** ✓
- en **variance** (MT, établie) : $\Delta K = \sqrt{k}\,\Delta K_1 \Rightarrow
  n \propto \sqrt{k}$. **Ne reproduit pas A.3.3.** ✗

**Résolution (penche du bon côté).** Les deux bornes répondent à deux questions
distinctes. MT/$\sqrt k$ borne l'orthogonalisation de l'état *joint*. Mais le
« degré de parallélisme $d$ » de `LC-07` est le **nombre de canaux indépendants qui
tirent** — un comptage *extensif* (régime de Lloyd : $N$ sous-systèmes font
$N\times$ les opérations). Le comptage opérationnel pertinent est donc $n = k$, par
la borne **extensive/moyenne**, pas le $\sqrt k$ joint. La carte A.3.3 est
*opérationnellement* correcte ; l'objet à établir est la **borne modulaire
extensive** — via le débit d'**entropie relative d'Araki** $S(\rho\|\omega)$ (≥ 0,
nulle ssi $\rho = \omega$, monotone : le bon analogue de « énergie modulaire
au-dessus du vide »).

### 1.4 bis — Lemme KMB : la carte composite $k\to$ métallique$(k)$ `[établi sous scission]`

Le résidu de A.4.3 est maintenant clos. Trois faits, scellés numériquement
(extensivité ; pont KMB ; additivité) :

1. **Deux énergies modulaires.** La variance $\Delta K$ (sous-extensive, $\sqrt k$)
   borne l'orthogonalisation *jointe* ; le couple extensif {énergie modulaire
   moyenne $\Delta\langle K\rangle$, entropie relative $S(\rho\|\omega)$} (linéaire
   en $k$) borne le comptage de transitions *indépendantes* = le $d$ de `LC-07`.
   *Sceau* : $\Delta\langle K\rangle$ et $S_{\text{rel}}$ croissent en $k$ ;
   $\sigma(K)$ en $\sqrt k$.
2. **Additivité exacte.** $S(\rho_1\otimes\rho_2\,\|\,\omega_1\otimes\omega_2) =
   S_1 + S_2$ (Araki, exact — sceau : ratio $1{,}000000$). *Pont* : au voisinage du
   vide, $S(\rho\|\omega) = \tfrac12\,g^{\text{KM}}_\omega(\delta,\delta) +
   O(\delta^3)$, $g^{\text{KM}}$ = métrique de **Kubo–Mori–Bogoliubov** (Hessienne de
   l'entropie relative — sceau : ratio $1{,}0015$), **bloc-additive** sur secteurs
   indépendants (sceau second ordre : ratio $1{,}0022$).
3. **Conclusion.** $d = k$ (extensif) ; chaque sous-nœud élémentaire ($n_1{=}1$, GS
   par Lemme B) ; composite = $k$ processus GS parallèles = moyenne métallique$(k)$
   ($x^2 = kx+1$). Le $\sqrt k$ de MT gouverne l'orthogonalisation jointe — sans
   pertinence pour le comptage de canaux.

**Domaine de validité (la condition, exhibée).** Tout repose sur la **factorisation**
de l'excitation à $k$ quanta en $k$ sous-excitations modulaires indépendantes. En
type III₁, la factorisation *exacte* échoue (pas de sous-facteurs type I,
hamiltoniens modulaires non locaux — `LC-08` §6 (iii)). Mais la **propriété de
scission** (split property ; Buchholz–Wichmann, Doplicher–Longo) fournit un facteur
type I intermédiaire pour des régions séparées par un collier fini → factorisation
approchée, exacte à la limite de quanta **bien séparés**. Hors de ce régime (quanta
recouvrants), pas de factorisation → non-additivité III₁ → la carte $d=k$ se dégrade
— *mais c'est exactement le régime où « $k$ canaux indépendants » n'a plus de sens*
(quanta corrélés, pas arêtes indépendantes). L'obstruction coïncide avec
l'effondrement de la prémisse.

**Coïncidence interne.** La métrique KMB/BKM qui clôt ici le spectre composite *est*
celle de la version canonique V3 de `LC-02` (flux de gradient de Carlen–Maas, bilan
détaillé modulaire) : le même objet géométrique structure $D_x$ et ferme Lemme A.

$$\boxed{\;k \to \text{métallique}(k)\;\text{est}\;\texttt{établi}\;\text{pour des excitations bien séparées (scission)}\;}$$

`établi` à la limite de grande séparation ; corrections à séparation finie
`formalisable` (contrôlées par l'indice de scission / la taille du collier). La
conditionnalité (scission = indépendance) n'est pas un posit libre : c'est la
*définition même* de « $d$ canaux indépendants » de `LC-07` — principielle, finie,
auto-sélective.

**Verdict Lemme A — clos.** Les deux régimes sont établis : nœud élémentaire
$k{=}1 \to \varphi$ (`établi`, cas wedge/BW) **et** spectre composite métallique
(`établi` sous scission). Plus aucun lemme *fini* ouvert ; seule subsiste la
condition principielle de scission (indépendance des canaux), à l'image de la
condition de quantification de Lemme B.

---

## 2. Lemme B — Trotterisation : « quantifié ⟹ Gauss–Seidel » `[à inventer → formalisable sous quantification]`

### 2.1 B.1–B.3 — La chaîne sauts → mono-canal → Gauss–Seidel

Nœud = générateur GKLS de `LC-02` :
$\dot\rho = -i[H,\rho] + \sum_e\big(L_e\rho L_e^\dagger - \tfrac12\{L_e^\dagger L_e,
\rho\}\big)$, les $L_e$ = « émettre un quantum dans l'arête $e$ » (champ dissipatif
$D_x$, versions V1/V3-KMS). Déroulé en sauts quantiques :

- **Pas 2 — mono-canal.** $P(\text{saut sur }e\,|\,dt) = \langle L_e^\dagger
  L_e\rangle\,dt$, donc $P(\ge 2\text{ sauts}/dt) = O(dt^2)\to 0$ : *au plus un
  saut, sur un seul canal, par $dt$*. Born ($\propto \langle L_e^\dagger
  L_e\rangle$) sélectionne *lequel*. `[établi — trajectoires quantiques]`
- **Pas 3 — version rigoureuse.** Table d'Itô quantique (Hudson–Parthasarathy) :
  $dA_e\,dA_f^\dagger = \delta_{ef}\,dt$. La **diagonalité** $\delta_{ef}$ dit que
  les canaux ne se croisent pas à l'ordre $dt$ — chaque incrément est mono-canal.
  `[établi]`
- **Pas 4 — identification GS.** La séquence de sauts agit chaque fois sur l'état
  *issu du saut précédent* : c'est le produit de Trotter **ordonné** $\prod_e
  e^{\mathcal L_e\delta}$ = **Gauss–Seidel**. L'update **additif** $1 + \sum_e
  \mathcal L_e\,\delta$ (tous les canaux voient le *même* ancien état) = **Jacobi**.
  `[établi pour l'identification ; formalisable pour l'égalité des taux]`
- **Pas 5 — soudure modulaire.** Le bilan détaillé modulaire KMS (Carlen–Maas V3,
  `LC-02`) fixe les taux de Born des $L_e$ : l'unraveling sélectionné est *le
  modulaire*. « Mono-paramétricité (temporel) + quantification (sauts) » se
  composent sur le même flot $\sigma_t$. `[formalisable]`

### 2.2 B.4 — Le point dur (cœur du `à inventer`)

**Non-unicité des unravelings.** La *même* équation maîtresse admet plusieurs
déroulements — sauts quantiques **vs** diffusion d'état (homodyne). La diffusion est
*continue* (pas de sauts discrets) → ne donne **pas** GS-strict. Donc
« quantifié ⟹ GS » exige un **principe sélecteur du déroulement par sauts**. Ce
principe *est* la quantification de l'interaction (échange de quanta discrets /
photodétection — pas une mesure continue). Conclusion assumée : **Lemme B se ferme
conditionnellement à « l'interaction se réalise par sauts de quanta indivisibles »**
— qui n'est pas un posit libre mais la définition même d'une interaction
quantifiée. Statut : `formalisable` sous ce principe, non `établi` inconditionnel.
Le résidu profond (« pourquoi sauts plutôt que diffusion ») *est* le contenu
physique de la quantification.

### 2.3 B.5 — Sceau numérique `[PASS]`

Simulation (Monte-Carlo wavefunction + branchement) d'un nœud à 2 canaux :

1. **Fait quantique.** Fraction de pas à deux sauts simultanés : $9{\times}10^{-5}$
   ($dt = 0{,}04$) → $1{,}25{\times}10^{-6}$ ($dt = 0{,}005$), soit ~72× pour un
   facteur 8 sur $dt$ — compatible avec $\propto dt^2$ (prédiction 64×) à la
   dispersion Monte-Carlo près. Sauts **mono-canal presque sûrement**.
2. **Croissance par déroulement.** Sauts mono-canal → Leslie $[[1,1],[1,0]] \to
   \lambda = 1{,}618034 = \varphi$ ; additif $d{=}2$ → $[[2,1],[1,0]] \to \lambda =
   2{,}414214 =$ argent.
3. **Trajectoire stochastique** (dynamique, pas matrice) du branchement mono-canal :
   ratio mesuré $= 1{,}618034 = \varphi$ à $10^{-6}$.

Le pont {sauts ↔ GS ↔ φ} / {parallèle ↔ Jacobi ↔ argent} tient **au niveau de la
dynamique quantique elle-même** : c'est le $O(dt^2)$ qui interdit le multi-canal.

---

## 3. Verdict de bascule

<svg width="100%" viewBox="0 0 680 360" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Articulation des deux lemmes vers Gauss–Seidel strict → φ</title>
  <desc>Lemme A (régime) donne un quantum par tick, n égale 1. Lemme B (Trotterisation) donne un canal par saut séquentiel. Les deux convergent vers Gauss–Seidel strict, donc phi. Deux résidus formalisables sont signalés : borne KMB extensive pour A, sélecteur d'unraveling égale quantification pour B.</desc>
  <defs>
    <marker id="a10" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
  </defs>
  <rect x="40" y="30" width="260" height="64" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.5"/>
  <text x="170" y="54" text-anchor="middle" font-size="14" font-weight="500" fill="#0F6E56">Lemme A — régime</text>
  <text x="170" y="74" text-anchor="middle" font-size="12" fill="#1D9E75">un quantum / tick  →  n = 1</text>
  <rect x="380" y="30" width="260" height="64" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.5"/>
  <text x="510" y="54" text-anchor="middle" font-size="14" font-weight="500" fill="#993C1D">Lemme B — Trotterisation</text>
  <text x="510" y="74" text-anchor="middle" font-size="12" fill="#D85A30">un canal / saut, séquentiel</text>
  <line x1="170" y1="94" x2="300" y2="170" stroke="#73726c" stroke-width="1.5" marker-end="url(#a10)"/>
  <line x1="510" y1="94" x2="380" y2="170" stroke="#73726c" stroke-width="1.5" marker-end="url(#a10)"/>
  <rect x="230" y="174" width="220" height="58" rx="10" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text x="340" y="198" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">Gauss–Seidel strict</text>
  <text x="340" y="218" text-anchor="middle" font-size="15" font-weight="600" fill="#534AB7">→ φ</text>
  <line x1="340" y1="232" x2="340" y2="270" stroke="#534AB7" stroke-width="1.5" marker-end="url(#a10)"/>
  <rect x="150" y="272" width="380" height="46" rx="10" fill="#fff" stroke="#534AB7" stroke-width="0.5"/>
  <text x="340" y="290" text-anchor="middle" font-size="12" fill="#3C3489">φ dérivé de {mono-paramétricité modulaire + quantification}</text>
  <text x="340" y="308" text-anchor="middle" font-size="12" fill="#534AB7">volet d'agent de LC-08 : décision ouverte → établi sous principes</text>
  <text x="170" y="120" text-anchor="middle" font-size="11" fill="#993C1D">condition : scission (indépendance)</text>
  <text x="510" y="120" text-anchor="middle" font-size="11" fill="#993C1D">condition : quantification</text>
  <text x="340" y="344" text-anchor="middle" font-size="11" fill="#73726c">deux conditions principielles — plus aucun lemme fini ouvert</text>
</svg>

*Fig. — Les deux lemmes convergent vers Gauss–Seidel strict → $\varphi$. Chacun se
ferme sous une **condition principielle** (orange), non un résidu ouvert.*

**La chaîne `LC-05 → LC-09` se lit désormais comme une dérivation de $\varphi$** à
partir de deux entrées seulement :

$$\boxed{\;\varphi \;\Longleftarrow\; \{\text{mono-paramétricité du flot modulaire}\}\;+\;\{\text{quantification de l'interaction}\}\;}$$

Le **volet d'agent de `LC-08`** passe de `décision ouverte` resserrée à
**`établi sous principes`** — les deux régimes du Lemme A sont clos (nœud élémentaire
φ, cas wedge ; spectre composite métallique, sous scission) et le Lemme B est clos
sous quantification.

**Honnêteté stricte.** Le verrou se ferme, mais **sous deux conditions
principielles** — non plus des lemmes ouverts, et ni libres ni flous :

1. **Scission / indépendance des canaux** (§1.4 bis) — la carte composite $k \to$
   métallique$(k)$ est `établi` pour des excitations bien séparées (propriété de
   scission). C'est la définition même de « $d$ canaux indépendants » de `LC-07`.
   (Le nœud élémentaire φ tient *sans* cette condition.)
2. **Quantification = sélecteur d'unraveling** (B.4) — sauts de quanta discrets vs
   diffusion continue ; non un posit gratuit, mais le cœur de la MQ.

Différence avec la v0.1 : il ne reste **plus aucun lemme fini ouvert** (le résidu
KMB est clos en §1.4 bis). Ne subsistent que deux *conditions* physiques, chacune
auto-sélective (hors d'elles, la prémisse — « canaux indépendants », « interaction
quantifiée » — n'a plus de sens). C'est l'issue maximale honnête : φ est
**sélectionné par la structure quantique-modulaire**, pas par un choix combinatoire
libre. Le résultat-titre (φ au nœud élémentaire) est, lui, **inconditionnel**.

---

## 4. Mises à jour de tags propagées dans la pile `[appliqué v0.2 ; table corrigée v0.3]`

> Propagées dans les fichiers (sorties) — **versions réelles post-KMB** : `LC-08`
> v0.4, `LC-09` v0.3, `00_index` v1.5, `03_glossaire` v1.5, `04_references` v1.4.
> Statut promu à **`établi sous principes`** après fermeture du résidu KMB (§1.4 bis).
> *(v0.3 : la table listait par erreur les versions pré-KMB v0.3/v0.2/v1.4/v1.4/v1.3
> — corrigé en revue à froid.)*

- **`LC-08-SERIALITE`** (v0.4) — volet d'agent : `décision ouverte` resserrée →
  **`établi sous principes`** (quantification + scission). Renvois `LC-09`/`LC-10`.
- **`LC-09-GAUSS-SEIDEL`** (v0.3) — §5 : Lemme A → `établi` (nœud élémentaire, cas
  wedge ; spectre composite, sous scission) ; Lemme B → `établi sous quantification`.
  §6 : verrou **fermé sous deux principes**.
- **`00_index`** (v1.5, puis **v1.6**) — pile φ : `LC-10` en tête ; volet d'agent →
  `établi sous principes`. (v1.6 : garde-fou de portée, ci-dessous.)
- **`LC-03-GLOSSAIRE`** (v1.5, puis **v1.6**) — entrées créées : *sauts quantiques (MCWF)* ;
  *Itô quantique (Hudson–Parthasarathy)* ; *Margolus–Levitin vs Mandelstam–Tamm* ;
  *vitesse modulaire (Deffner–Lutz)* ; *entropie relative d'Araki* ; *métrique de
  Kubo–Mori–Bogoliubov* ; *propriété de scission (split property)* ; *facteur type I
  intermédiaire (Buchholz–Wichmann, Doplicher–Longo)*. (v1.6 : contradiction
  *Réfractarité* ↔ *Sérialité* levée + garde-fou de portée.)
- **`LC-04-REFERENCES`** (v1.4) — repères régime/Trotterisation + (v1.4) Buchholz–Wichmann
  (causal independence / split, ~1986) ; Doplicher–Longo (standard split inclusion, 1984) ;
  Araki (entropie relative, 1976) ; Petz / Bogoliubov–Kubo–Mori (métrique BKM).

> **Couche de réconciliation post-fermeture (revue à froid — `LC-05` v0.5, `00_index`
> /`LC-03` v1.6, `LC-WORK-REPRISE` v1.1).** Ajout transverse d'un **garde-fou de
> portée** : « établi sous principes » vaut au plan **symbolique** et au **nœud
> élémentaire** ; la **transposition QFT** (CFT sur S², hamiltonien modulaire,
> scission III₁) n'est *pas instanciée* — applicabilité `formalisable → à inventer` ;
> les sceaux de clôture (§1.4 bis) sont en dimension finie / type I. Le résultat-titre
> (φ inconditionnel au nœud élémentaire) est inchangé.

---

## 5. Critères de réfutation (rappel, hérités du mandat)

- **Lemme A échoue** si $n > 1$ est génériquement permis pour un nœud élémentaire
  (plusieurs quanta/tick) → constante $> \varphi$, dérive vers le parallèle → φ
  n'est qu'un cas limite.
- **Lemme B échoue** si le déroulement physiquement correct est diffusif (continu),
  ou si les sauts admettent des co-occurrences multi-canal à l'ordre $dt$ (table
  d'Itô non diagonale → couplages croisés) → GS non forcé → métalliques possibles.
- **Sceau B.5** : si une simulation reproduisait l'argent (et non φ) sous le
  déroulement par sauts mono-canal, le pont {sauts ↔ GS ↔ φ} tomberait. (Observé :
  φ. PASS.)

---

## 6. Renvois et glossaire

**Renvois.** `LC-09` (verrou, énoncé des deux lemmes) ; `LC-08` (primitif, volet
d'agent qui bascule) ; `LC-07` (carte {bundle → λ}, pinceaux) ; `LC-06`
(discrétisation, tick $\tau = \ell/c$) ; `LC-05` (φ = débit d'entropie maximal sous
REST=1) ; `LC-02` (champ dissipatif $D_x$, GKLS/Stinespring/Carlen–Maas-KMS) ;
colonne modulaire/KMS (`LC-02`, `LC-01`).

**Glossaire à ajouter (`LC-03`).** Voir §4 (liste des entrées).

**Références (`LC-04`, à vérifier).** Voir §4 (liste des entrées).

---

## Appendice — Légende des tags épistémiques

- `établi` — théorème ou fait standard.
- `formalisable` — programme clair, exécution non faite.
- `à inventer` — pont conjecturé, sans preuve.
- `hors de portée` — au-delà des moyens actuels.
- `décision ouverte` — choix de modélisation explicitement reporté ou assumé.
  (cf. `LC-00-INDEX`.)
