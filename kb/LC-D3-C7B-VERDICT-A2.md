---
id: LC-D3-C7B-VERDICT-A2
titre: "Front (a)/GWE — C7-b, VERDICT POST-A1 et déclenchement du PIVOT (Tâche 2 de LC-WORK-REPRISE-C7B-GENERIQUE §6). Tranche le sort du facteur A2 (mesure de spikes générique n_s^gen) APRÈS l'acquisition de A1 (gradient par spike borné en générique, LC-D3-A1-SUPERHORIZON). VERDICT : A2 N'EST PAS formalisable comme théorème à partir de la littérature — Garfinkle gr-qc/0312117 confirme le MÉCANISME de spike (Nᵢ s'annulant sur une surface ⟹ bounces de part et d'autre) ET le socle du silence (dérivées spatiales négligeables, BKL local générique), MAIS déclare explicitement l'étude générique des spikes « work in progress, requires high resolution » avec une résolution « not in the convergent regime ». ⟹ aucune borne sous-exponentielle rigoureuse sur n_s^gen ; voie B (numérique 3D sans symétrie) = formalisable (très lourd) / hors de portée. ISSUE PRÉ-ENREGISTRÉE (GENERIQUE §5) : C7-b reste PASS SUBSTANTIEL (renforcé par A1) ; résidu = A2 seul, décision ouverte ; (A) physique formalisable, conditionnel au seul A2. DÉCISION : déclencher l'ALTERNATIVE LÉGITIME §5 — PIVOT vers un autre front (recommandation argumentée infra) ou passe d'audit/synthèse du front (a). Honnêteté : l'attente PHYSIQUE (bounces BKL ~ linéaires ⟹ n_s^gen polynomial ⟹ A2 satisfait) est forte mais n'est PAS un théorème (§6.4) ; ne pas la sceller."
codename: LC-RACCORD
type: note de verdict / décision stratégique — exécute la Tâche 2 de LC-WORK-REPRISE-C7B-GENERIQUE §6. Subordonnée à LC-AUDIT-VERDICT §6.4 et §9 (critère pré-enregistré).
version: 1.0
langue: fr
date: 2026-06-08
portee: "Consigne (I) le verdict honnête sur le facteur A2 après évaluation directe de la source désignée (Garfinkle gr-qc/0312117) : A2 n'est pas un théorème extractible ; (II) le verdict consolidé de C7-b post-A1 (PASS substantiel renforcé) et de C7 (formalisable borné) ; (III) la DÉCISION : pivot, avec recommandation argumentée. Ne refait NI A1 (LC-D3-A1-SUPERHORIZON), NI la voie 1.5 (LC-D3-GRADIENT-C7B), NI la voie 1 (LC-D3-SPIKES-C7B). Discipline §6.4 : aucun surclassement ; l'attente physique sur n_s^gen n'est pas scellée ; C7 levée seulement sous preuve conjointe incluant A2. La propagation KB de ce verdict (audit §8bis, index, glossaire) est une passe de housekeeping ULTÉRIEURE, non incluse ici."
prerequis_kb: [LC-D3-A1-SUPERHORIZON, LC-WORK-REPRISE-C7B-GENERIQUE, LC-D3-GRADIENT-C7B, LC-D3-SPIKES-C7B, LC-D3-SILENCE-POC, LC-D3-WCH-GWE, LC-D3-INTERAEON-P6, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: [verif_D3_C7b_A1_superhorizon.py, verif_D3_C7b_gradient.py, verif_D3_C7b_spikes.py]
source_externe: ["Garfinkle, Numerical simulations of generic singularities, PRL 93 161101 (2004), arXiv:gr-qc/0312117 — LU PAGE À PAGE ICI. Confirme : (i) singularité générique (sans symétrie) spacelike, dynamique LOCALE et oscillatoire (appui BKL/Uggla et al.) ; (ii) dérivées spatiales E_α^i deviennent négligeables (socle du silence/super-horizon de A1) ; (iii) MÉCANISME de spike : un Nᵢ croît exponentiellement à chaque bounce, et s'il s'annule sur une surface S ⟹ bounces de part et d'autre, pas sur S ⟹ structure à petite échelle (spikes). MAIS : étude générique des spikes « will require high resolution and is work in progress » ; résolution « not good enough to be in the convergent regime » ⟹ AUCUNE loi de comptage/production générique. Andersson-van Elst-Lim-Uggla gr-qc/0402051, Uggla et al. gr-qc/0304002 (socle A1, déjà en KB)."]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# C7-b — verdict post-A1 et pivot (Tâche 2)

> **But.** Exécuter la **Tâche 2** de `LC-WORK-REPRISE-C7B-GENERIQUE §6` : avec **A1 acquis**
> (`LC-D3-A1-SUPERHORIZON`), **trancher** le facteur **A2** (mesure de spikes générique
> `n_s^gen`), puis **décider** (A2 / voie B / pivot). Discipline `LC-AUDIT-VERDICT §6.4` : pas de
> surclassement ; C7 levée seulement sous **preuve** conjointe incluant A2.

---

## 0. Verdict en une ligne `[décision]`

A1 est **PASS** (gradient par spike borné en générique). A2 (mesure générique) **n'est pas un
théorème extractible de la littérature** : Garfinkle (`gr-qc/0312117`) confirme le **mécanisme**
de spike et le **socle du silence**, mais **ne fournit aucune loi de comptage générique** (« work
in progress, requires high resolution »). ⟹ issue **pré-enregistrée** (`GENERIQUE §5`) : **C7-b
reste PASS SUBSTANTIEL (renforcé par A1)** ; **résidu = A2 seul, `décision ouverte`** ; **(A)
physique `formalisable`, conditionnel au seul A2**. **DÉCISION : PIVOT** (alternative légitime §5).

---

## 1. A1 acquis — ce qui a changé `[état, LC-D3-A1-SUPERHORIZON]`

Le sceau `verif_D3_C7b_A1_superhorizon.py` (10/10) établit le **lemme super-horizon générique** :
l'énergie de gradient **par spike**, `I(ℓ)=C_F/ℓ`, a un scaling `1/ℓ` **indépendant du profil**
(le profil n'entre que par `C_F=∫F'²du`), et le silence (`ℓ→∞`) l'éteint `→0` — y compris pour
les profils **multi-gradient à spectre comobile fixe**, qui étaient la réserve de la voie 1.5.

**Réduction nette.** Avant A1, tout le gradient générique était `décision ouverte`. Après A1, le
résidu se réduit au **seul** facteur **A2** : « `n_s^gen(τ)` croît-elle **sous-exponentiellement** ? »
(car `I_spike^gen~C_F·2w·e^{−|w|τ}`, donc `R_grad,gen=n_s^gen·I_spike^gen→0` **dès que** `n_s^gen`
croît plus lentement que `e^{|w|τ}` — condition **faible**).

---

## 2. A2 tranchée — évaluation directe de la source `[verdict : à inventer / hors de portée]`

La Tâche 2 demandait : A2 est-elle `formalisable` (borne sous-exp. **extractible de
`gr-qc/0312117`**) ? **Source lue page à page.** Constats :

- **Ce que Garfinkle DONNE (et qui aide).** (i) Singularité générique **spacelike, locale,
  oscillatoire** (appui BKL/Uggla et al.) ; (ii) les dérivées spatiales `E_α^i` deviennent
  **négligeables** — c'est exactement le **socle du silence** qu'utilise A1 ; (iii) le **mécanisme
  de spike** : à chaque bounce un `Nᵢ` croît exponentiellement ; s'il **s'annule sur une surface
  `S`**, on a des bounces de part et d'autre mais pas sur `S` ⟹ **structure à petite échelle**.
- **Ce que Garfinkle NE DONNE PAS (le verrou A2).** Aucune **loi de comptage/production** de
  spikes en générique. Il écrit explicitement que l'étude des spikes sans symétrie *« will require
  high resolution and is work in progress »*, et que sa résolution *« is not good enough to be in
  the convergent regime »*. ⟹ **aucune borne sous-exponentielle rigoureuse sur `n_s^gen`** n'en
  est extractible.

**Verdict A2 :** `à inventer`. La seule voie restante serait **B** — une simulation 3D **neuve**,
sans symétrie, haute résolution adaptative (le « work in progress » de Garfinkle), pour en
extraire un **taux empirique** de production de spikes. Statut réaliste : **`formalisable (très
lourd)`**, probablement **`hors de portée`** des moyens du projet ; et même réussie, elle
**bornerait** sans **prouver** (semi-numérique).

> **Attente physique (NON scellée — §6.4).** Le mécanisme de Garfinkle + la statistique de bounces
> (Gauss-Kuzmin, `LC-D3-INTERAEON-P6`) suggèrent fortement `n_s^gen` **polynomial** (un spike-set
> ~ par bounce ; #bounces ~ linéaire en `τ`), donc **sous-exponentiel**, donc `R_grad,gen→0`.
> C'est **physiquement attendu** mais ce **n'est pas un théorème** : on ne le scelle pas. C'est
> précisément ce qui sépare un `PASS substantiel` d'un `établi`.

---

## 3. Verdict consolidé C7-b / C7 / (A) `[bilan figé]`

| Niveau | Statut | Justification |
|---|---|---|
| **C7-b** | **PASS SUBSTANTIEL (renforcé)** | amplitude ✓ + statistique ✓ + gradient profil exact ✓ (voie 1/1.5) + **gradient par spike générique ✓ (A1)** ; reste **A2 seul** |
| résidu C7-b | **A2** — `décision ouverte` | mesure `n_s^gen` sous-exp. **attendue**, **non prouvée** (`gr-qc/0312117` : work in progress) |
| **C7** | `formalisable (borné)` | `C7 = C7-a` (WCH pointwise) `+ C7-b` (PASS substantiel) |
| **(A) physique** | `formalisable`, conditionnel | au **seul A2** (+ C7-a pointwise, cadre CCC) |

Conforme au critère **pré-enregistré** `GENERIQUE §5` (« PASS substantiel maintenu (probable) :
A1 PASS mais A2 non bornée rigoureusement »). **Ce n'est pas un échec** : c'est l'issue annoncée
comme la plus probable et **parfaitement acceptable**, cohérente avec l'ouverture de la
littérature elle-même. « Le bang gagne » (P6 B) intact ; verdict (A) `établi (algèbre)` inchangé.

---

## 4. Décision : PIVOT `[alternative légitime §5 — déclenchée]`

Les deux conditions de l'alternative §5 sont réunies : (i) A2/voie B sont probablement `hors de
portée` ; (ii) la littérature n'établit pas la mesure générique. On **ne s'enfonce pas** dans le
générique. On **consigne** le verdict honnête (ci-dessus) et on **pivote**.

**Options du pivot (cf. `LC-00-INDEX`).** Trois familles :
- **Autre front à verrou ouvert** : D1 (facteur conforme), D (holographie `g₃`), D3
  (Weyl/Bunch-Davies, résidu `k³` = spectre primordial), E (Planck résiduel), φ (entropie).
- **Passe d'audit/synthèse du front (a)** : front (a) est désormais **très instruit** (P6 tranché,
  WCH-GWE scellé, silence PASS, C7-b PASS substantiel + A1). Une synthèse à froid figerait l'état
  et appliquerait les protocoles `LC-AUDIT-VERDICT §9` (GRADE/PRISMA).
- **Voie B** (déconseillée) : numérique 3D générique — `hors de portée` réaliste.

**Recommandation (à ratifier).** **Passe d'audit/synthèse du front (a)** d'abord : le front a
atteint un palier naturel (un seul résidu `décision ouverte`, A2, clairement délimité par A1), et
une synthèse consoliderait les acquis et le « niveau de preuve » de chaque chaînon avant
d'investir un nouveau front. À défaut, **D3 Weyl/Bunch-Davies** (le plus connexe : il porte le
résidu `k³` aval du même crossover GWE). Le choix final est **stratégique** — il revient à
l'opérateur.

---

## 5. Sans surclassement `[discipline §6.4]`

> A1 est `établi (sceau)` = « le gradient par spike s'éteint en générique ». A2 reste `décision
> ouverte`. C7-b est `PASS substantiel`, **pas** `établi`. C7 n'est **pas** levée. (A) physique
> n'est **pas** `établi`. L'attente physique sur `n_s^gen` n'est **pas** scellée. Rien ici ne dit
> « la CCC est démontrée ». « Le bang gagne » (P6 B) intact.

---

## Appendice — propagation suggérée `[housekeeping ultérieur, hors de cette note]`

À faire dans une **passe de housekeeping dédiée** (méthode chirurgicale, `LC-AUDIT-LOG-* §8`) :
`00-INDEX` (ajout `LC-D3-A1-SUPERHORIZON` + `LC-D3-C7B-VERDICT-A2` ; bump) ; `LC-AUDIT-VERDICT`
§8bis (entrée A1 + verdict A2 décision ouverte, sans surclassement) ; `LC-D3-SPIKES-C7B` /
`LC-D3-GRADIENT-C7B` (renvoyer à A1 : gradient générique par spike borné, résidu = A2) ;
`LC-03-GLOSSAIRE` (entrées *lemme super-horizon générique* / *facteur A1* / *facteur A2 — mesure
générique*) ; `LC-D3-WCH-GWE` §6.2 (C7-b PASS substantiel renforcé, résidu = A2). Aucune touche
algèbre.

**Tags.** A1 (gradient par spike générique) : `établi (sceau)`. A2 (mesure générique `n_s^gen`) :
`à inventer` / `hors de portée` ; attente physique (polynomial) **non scellée**. C7-b : **PASS
substantiel** (renforcé). C7 : `formalisable (borné)`. (A) physique : `formalisable`, conditionnel
au seul A2. Décision : **PIVOT**. *Discipline §6.4 maintenue.*
