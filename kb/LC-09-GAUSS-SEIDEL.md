---
id: LC-09-GAUSS-SEIDEL
titre: "Gauss–Seidel vs Jacobi — le dernier verrou de la sérialité d'agent"
codename: LC-RACCORD
tags: [verrou, gauss-seidel, jacobi, quantification, born, margolus-levitin, sous-programme-phi]
statut: verrou fermé sous DEUX PRINCIPES (cf. LC-10 v0.2) — Lemme A établi (nœud élémentaire, cas wedge ; spectre composite, sous scission) ; Lemme B établi sous quantification ; plus de lemme fini ouvert
version: 0.3
langue: fr
maj: "2026-06-07 — v0.1 : inventaire des principes. v0.2 : fermeture des deux lemmes de §5 (cf. LC-10). v0.3 : résidu KMB clos (LC-10 §1.4 bis) — la carte composite k→métallique(k) passe à `établi` sous la propriété de scission (Buchholz–Wichmann/Doplicher–Longo). Lemme A entièrement clos (nœud élémentaire φ + spectre composite). Plus aucun lemme fini ouvert ; deux conditions principielles subsistent (quantification ; scission). Volet d'agent → établi sous principes."
renvois: [LC-10-FERMETURE, LC-05-PHI-ENTROPIE, LC-06-CINEMATIQUE, LC-07-CARTOGRAPHIE, LC-08-SERIALITE, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-09 — Le dernier verrou de la sérialité d'agent

> **Enjeu.** LC-08 §6 a resserré le volet d'agent en un posit précis : *« le flot
> modulaire se Trotterise séquentiellement (Gauss–Seidel) »*. Le fermer ferait
> basculer ce volet de `décision ouverte` à `formalisable` (voire `établi`), et
> avec lui la sélection de $\varphi$. Ce document pose le verrou et fait
> l'inventaire honnête des principes candidats. **Verdict** : un seul tient — la
> **quantification de l'interaction** — qui ferait de $\varphi$ la signature du
> *quantum*, les moyennes métalliques étant celle du *classique*.

---

## 1. Énoncé du verrou

La même équation $e^{iKt}$ (flot modulaire) se discrétise de deux façons :

- **Gauss–Seidel** (séquentiel) : on traite **une arête à la fois**, sur l'état
  **mis à jour**. Émissions ordonnées dans le temps → un enfant par tick →
  substitution de Fibonacci → $\boxed{\varphi}$.
- **Jacobi** (parallèle) : on traite **toutes les arêtes d'un coup**, sur
  l'**ancien** état. Diffusion simultanée → $d$ enfants par cycle → **moyennes
  métalliques** (argent, bronze …).

Les deux convergent vers le même flot continu ; seule diffère la **combinatoire
discrète** (cf. LC-07, par-nœud = Gauss–Seidel, par-arête = Jacobi). Le verrou :
**quel principe physique impose Gauss–Seidel ?**

Le distingueur opérationnel : en Gauss–Seidel, l'émission vers un partenaire
*utilise l'état déjà modifié* par l'émission précédente (dépendance séquentielle,
**un partenaire à la fois**) ; en Jacobi, toutes les émissions sont mutuellement
aveugles (**diffusion vers tous**). La question se ramène donc à : *l'acte
élémentaire d'un nœud est-il dirigé vers un seul partenaire (séquentiel) ou
diffusé vers tout son voisinage (parallèle) ?*

---

## 2. Inventaire des principes candidats

| Principe candidat | Force-t-il Gauss–Seidel ? | Verdict |
|---|---|---|
| **Atomicité causale** (événements sans structure interne) | Non : un point peut *diffuser* en parallèle (source ponctuelle isotrope = broadcast). | insuffisant |
| **Mono-paramétricité** (globale ou locale) du flot modulaire | Non : une horloge unique fait avancer ses sous-structures *ensemble* (le problème se récursive : LC-08 §6). | insuffisant |
| **Invariance de Lorentz / ligne d'univers unique** | Ordonne les événements co-localisés (timelike), mais n'interdit pas qu'un *seul* acte atteigne plusieurs partenaires. | insuffisant |
| **Limite quantique de vitesse** (Margolus–Levitin / Lloyd) | Oui *en régime d'énergie minimale* : énergie finie ⟹ taux d'opérations fini ⟹ étalement temporel des actes. | partiel (régime) |
| **Quantification de l'interaction** (un quantum indivisible → un seul partenaire par événement ; règle de Born) | **Oui** : un quantum ne se scinde pas ; il va à un partenaire, puis au suivant — séquentiel. | **candidat fort** |

Le détail des trois échecs et du partiel est en annexe ; le candidat fort suit.

---

## 3. La route forte : la quantification de l'interaction

L'élément qui distingue proprement Gauss–Seidel de Jacobi n'est ni la
mono-paramétricité, ni l'atomicité géométrique, mais la **divisibilité de
l'acte** :

- **Couplage classique de champ** — l'acte est *divisible* : un nœud couple
  simultanément à tout son voisinage (une source ponctuelle rayonne dans toutes
  les directions à la fois). C'est **Jacobi** → moyennes métalliques.
- **Quantum d'interaction** — l'acte est *indivisible* : un quantum unique est
  émis/absorbé par **un** partenaire (un photon est détecté par *un* détecteur,
  pas scindé ; la règle de Born sélectionne *un* résultat). Le nœud adresse un
  partenaire, puis — au tick suivant, sur son état modifié — le suivant. C'est
  **Gauss–Seidel** → $\varphi$.

<svg width="100%" viewBox="0 0 680 250" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Quantum (un partenaire, séquentiel) vs classique (diffusion, parallèle)</title>
  <desc>À gauche, un nœud émet un quantum vers un seul partenaire au tick t puis un autre au tick t+1 : séquentiel, Gauss–Seidel, phi. À droite, un nœud diffuse vers tous ses partenaires d'un coup : parallèle, Jacobi, moyennes métalliques.</desc>
  <defs>
    <marker id="aq" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
  </defs>
  <text x="170" y="32" text-anchor="middle" font-size="14" font-weight="500" fill="#0F6E56">quantique — un partenaire / tick</text>
  <circle cx="120" cy="120" r="11" fill="#534AB7"/>
  <circle cx="220" cy="80" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="240" cy="160" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <line x1="131" y1="116" x2="210" y2="84" stroke="#1D9E75" stroke-width="2.5" marker-end="url(#aq)"/>
  <text x="172" y="92" font-size="12" fill="#0F6E56">tick t</text>
  <line x1="131" y1="124" x2="230" y2="156" stroke="#1D9E75" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#aq)"/>
  <text x="178" y="150" font-size="12" fill="#1D9E75">tick t+1</text>
  <text x="170" y="210" text-anchor="middle" font-size="13" fill="#0F6E56">séquentiel = Gauss–Seidel → φ</text>
  <line x1="350" y1="40" x2="350" y2="220" stroke="#D3D1C7" stroke-width="0.5"/>
  <text x="520" y="32" text-anchor="middle" font-size="14" font-weight="500" fill="#993C1D">classique — diffusion vers tous</text>
  <circle cx="470" cy="120" r="11" fill="#534AB7"/>
  <circle cx="570" cy="70" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="590" cy="120" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <circle cx="570" cy="170" r="7" fill="none" stroke="#73726c" stroke-width="1"/>
  <line x1="481" y1="115" x2="560" y2="74" stroke="#D85A30" stroke-width="2" marker-end="url(#aq)"/>
  <line x1="482" y1="120" x2="580" y2="120" stroke="#D85A30" stroke-width="2" marker-end="url(#aq)"/>
  <line x1="481" y1="125" x2="560" y2="166" stroke="#D85A30" stroke-width="2" marker-end="url(#aq)"/>
  <text x="520" y="100" font-size="12" fill="#993C1D">même tick</text>
  <text x="520" y="210" text-anchor="middle" font-size="13" fill="#993C1D">parallèle = Jacobi → métalliques</text>
</svg>

*Fig. — Quantum indivisible (un partenaire, séquentiel, Gauss–Seidel → $\varphi$)
vs couplage classique de champ (diffusion simultanée, Jacobi → métalliques).*

**Punchline.** $\varphi$ serait alors la **signature de la nature quantique
(indivisible, un-partenaire, séquentielle) de l'interaction** ; les moyennes
métalliques, celle d'un couplage **classique** de champ. Le verrou se ferme — au
sens fort — *si* l'on adopte la quantification de l'interaction, qui n'est pas un
posit libre mais le cœur de la mécanique quantique (discrétude du quantum + règle
de Born = un résultat par événement). `[formalisable]`

C'est l'issue la plus **soudée au programme** possible : elle relie $\varphi$ à
la quantification elle-même — donc à la colonne modulaire/KMS de LC-RACCORD, où
l'énergie (le hamiltonien modulaire $K$) et la thermalité (KMS) gouvernent
précisément les échanges de quanta.

---

## 4. Renfort : la limite quantique de vitesse

La quantification *qualitative* (un quantum/un partenaire) est renforcée
*quantitativement* par la **limite de Margolus–Levitin** : un système d'énergie
moyenne $E$ effectue au plus $\sim 2E/\pi\hbar$ opérations orthogonales par
seconde. Un nœud d'énergie finie ne peut donc **pas** réaliser une infinité
d'actes simultanés : ils s'étalent dans le temps. Au régime **minimal** (un
quantum d'action par tick, $E$ minimale, $\langle K\rangle$ d'un seul mode), on
obtient *exactement* un acte par tick = Gauss–Seidel strict → $\varphi$.
`[formalisable — régime d'énergie minimale]`

Lien au programme : $E = \langle K\rangle$ (énergie modulaire) ; le tick
$\tau=\ell/c$ et la limite ML fixent ensemble le nombre d'actes/tick. Le nœud
élémentaire = énergie minimale = un quantum/tick.

---

## 5. Les deux lemmes — traités en LC-10 (mise à jour v0.2)

> **Statut v0.2.** Les deux lemmes ci-dessous ont été exécutés dans
> **`LC-10-FERMETURE`** (mandat `LC-WORK-VERROU-PHI`). Résumé des promotions :

1. **Lemme de Trotterisation** `[à inventer → formalisable sous quantification]` :
   « interaction quantifiée (un quantum → un partenaire) » impose la discrétisation
   **Gauss–Seidel** du flot modulaire. *Établi* : déroulement GKLS en sauts
   quantiques ⟹ $P(\ge 2\text{ sauts}/dt) = O(dt^2)$ ⟹ sauts **mono-canal**
   (table d'Itô diagonale de Hudson–Parthasarathy $dA_e dA_f^\dagger =
   \delta_{ef}dt$) ; la séquence de sauts = produit de Trotter **ordonné** =
   Gauss–Seidel. *Conditionnel* (point dur B.4) : la non-unicité des déroulements
   (sauts vs diffusion continue) exige un **sélecteur** — qui *est* la
   quantification (sauts de quanta discrets, pas mesure homodyne). Sceau numérique
   B.5 : sauts mono-canal → $\varphi$, additif $d{=}2$ → argent (PASS).
   (Détail : `LC-10` §2.)
2. **Lemme de régime** `[établi — nœud élémentaire (cas wedge) + spectre composite (sous scission)]` :
   le nœud fondamental est en régime d'un quantum/tick. *Établi* : test de
   consistance A.3.3 ($\pi\hbar/2E_{\min} = \ell/c \Leftrightarrow E_{\min}\tau =
   \pi\hbar/2$) + identification $k = n = d$ (niveau d'excitation = degré de
   parallélisme métallique). *Transposition III₁* (A.4) : Margolus–Levitin
   (moyenne, échoue sans fondamental) remplacé par **Mandelstam–Tamm** (variance,
   survit), ancré rigoureusement dans le cas **wedge** via Bisognano–Wichmann
   (Unruh). *Carte composite — close* (`LC-10` §1.4 bis) : $k\to$ métallique$(k)$
   est `établi` sous la **propriété de scission** (Buchholz–Wichmann/Doplicher–Longo),
   via l'extensivité exacte de l'entropie relative d'Araki et la métrique de
   **Kubo–Mori–Bogoliubov** (Hessienne de $S_{\text{rel}}$, bloc-additive). (Détail :
   `LC-10` §1.)

**Conséquence.** Le volet d'agent de `LC-08` passe à **`établi sous principes`**, et
$\varphi$ devient **dérivé** de {mono-paramétricité modulaire + quantification}.
Plus aucun lemme *fini* ouvert ; subsistent deux **conditions principielles** —
quantification (sélecteur d'unraveling) et scission (indépendance des canaux) —, ni
libres ni flous, chacune auto-sélective. Le nœud élémentaire φ est, lui,
inconditionnel. Voir `LC-10` §3.

---

## 6. Falsifiabilité et conséquence

$$\boxed{\;\varphi \;=\; \text{signature d'une interaction QUANTIQUE (indivisible, un-partenaire, séquentielle).}\;}$$

- Un substrat à **couplage classique de champ** (diffusion) prédirait une
  moyenne métallique $\ge$ argent — **réfutation** de la sélection de $\varphi$
  par cette voie.
- Réciproquement, observer $\varphi$ *confirmerait* le caractère quantique
  indivisible de l'interaction élémentaire.

Conséquence sur la pile (v0.3) : **le verrou se ferme sous deux principes** (cf.
`LC-10`), donc **LC-08 bascule** — volet d'agent `décision ouverte` → `établi sous
principes` —, et toute la chaîne `LC-05 → LC-09` se lit comme une dérivation de
$\varphi$ à partir de {mono-paramétricité modulaire (volet temporel) + quantification
de l'interaction (volet d'agent)} — soit, en un mot, **à partir de la structure
quantique-modulaire elle-même**. Plus aucun lemme *fini* n'est ouvert (le résidu KMB
est clos, `LC-10` §1.4 bis) ; la fermeture reste *conditionnelle* à deux conditions
principielles (scission/indépendance ; quantification), non à des
posits libres.

---

## 7. Annexe — pourquoi les trois premiers principes échouent

- **Atomicité.** Un événement sans structure interne peut tout de même *sourcer*
  un champ diffusant vers tous ses voisins (broadcast). La structurelessness
  n'interdit pas la divisibilité de l'acte. → insuffisant.
- **Mono-paramétricité.** Donne *une* horloge (globale ou locale), mais le flot
  $e^{iKt}$ fait avancer toutes les sous-structures *ensemble* ; appliquer
  l'argument au niveau du nœud le récursive sans le résoudre (LC-08 §6). →
  insuffisant.
- **Lorentz / ligne d'univers.** Deux événements co-localisés (timelike) sont
  ordonnés — mais cela n'empêche pas qu'**un seul** acte atteigne plusieurs
  partenaires (le parallélisme est dans le champ émis, pas dans l'ordre des
  événements du nœud). → insuffisant pour le *nombre de partenaires*.

C'est précisément ce que la quantification résout : elle borne le nombre de
partenaires *par acte* à un.

---

## 8. Renvois et glossaire

**Renvois.** LC-08 (primitif ; §6 = origine de ce verrou) ; LC-07 (carte
Gauss–Seidel/Jacobi → φ/métalliques) ; LC-06, LC-05 ; colonne modulaire/KMS
(LC-02, LC-01).

**Glossaire à ajouter (LC-03).**

- *Verrou Gauss–Seidel* : principe imposant la Trotterisation séquentielle.
- *Quantification de l'interaction* (un quantum → un partenaire ; règle de Born)
  comme sélecteur de Gauss–Seidel.
- *Limite de Margolus–Levitin* : borne $2E/\pi\hbar$ sur le taux d'opérations.

**Références (LC-04, à vérifier).**

- N. Margolus & L. B. Levitin, « The maximum speed of dynamical evolution »,
  Physica D 120 (1998).
- S. Lloyd, « Ultimate physical limits to computation », Nature 406 (2000).
- R. D. Sorkin / Rideout–Sorkin — croissance séquentielle classique (Gauss–Seidel
  côté ensembles causaux).

---

## Appendice — Légende des tags épistémiques

- `établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
  (cf. LC-00-INDEX).
