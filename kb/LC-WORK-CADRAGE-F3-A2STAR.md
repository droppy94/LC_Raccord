---
id: LC-WORK-CADRAGE-F3-A2STAR
titre: "Cadrage paper-first du front F3 (branche FALSIFIABILITÉ, rang 2) — SUBSTANTIATION d'A2★. Cherche à confronter la SEULE maille non scellée d'A2★ — la NON-CASCADE (yield de charge de gradient par bounce borné + pas de prolifération exponentielle de surfaces de spike) — à la statistique RIGOUREUSE des singularités génériques (billards cosmologiques de Damour–Henneaux–Nicolai ; statistique d'ères de Khalatnikov–Lifshitz–Sinai–Khanin–Shchur ; Garfinkle gr-qc/0312117). NE refait PAS la réduction A2→A2★ (LC-WORK-A2-CONJECTURE, déjà faite) NI ses deux maillons NON-A2★ déjà SCELLÉS (verif_D3_C7b_A2_reduction.py EXIT 0/16 : déduction §4 + N_b(τ) sous-exp.). GEL de l'énoncé exact de sous-exponentialité ET des cibles F3-G1..G4 AVANT toute extraction/fetch (protocole anti-fit). F3 est le SEUL front pouvant faire BOUGER le périmètre {A4 ; A2★ ; N} (substantier A2★ ⟹ décision ouverte → formalisable ; la réfuter ⟹ casse la chaîne (A)-physique). AUCUN sceau, AUCUNE algèbre neuve, AUCUN fetch dans ce document : il fixe la prédiction, le plan d'extraction et le critère de réfutation, à valider par Thierry AVANT exécution. Issue honnête la plus probable (cohérente avec LC-D3-C7B-VERDICT-A2) : A2★ reste décision ouverte — la littérature ne ferme pas la statistique générique des spikes (« work in progress ») — F3 DÉLIMITE alors comme F1, sans réduction du compte."
codename: LC-RACCORD
tags: [cadrage, paper-first, F3, branche-falsifiabilite, A2star, spikes, non-cascade, BKL, billards-cosmologiques, Damour-Henneaux-Nicolai, Gauss-Kuzmin, carte-de-Gauss, Garfinkle, statistique-eres, anti-fit, gel, R-7, §6.4]
type: "note de travail / cadrage papier (paper-first) — ouverture du front F3. Subordonnée à LC-AUDIT-VERDICT §6.4. Étage cartographie/substantiation, NON fermeture. AUCUN sceau, AUCUN fetch dans ce document : il GÈLE l'énoncé et les cibles avant l'extraction."
statut: "cadrage / décision ouverte — énoncé A2★ et cibles GELÉS (F3-G1..G4, §2 byte-identique v0.1→v0.2), plan et critère posés, scopings ADOPTÉS (§8 : S-F3-1..4 tranchés ; Garfinkle PRÉSENT en KB). NE déplace rien, NE scelle rien. Le test lui-même (extraction littérature + confrontation) est l'étape SUIVANTE, sur GO de Thierry. Périmètre {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée."
version: 0.2
langue: fr
maj: "2026-06-13 — v0.2 : RECTIFICATION (R-7) — Garfinkle gr-qc/0312117 est PRÉSENT en KB (0312117v4.pdf, PDF natif 4 p.) ; le « ABSENT, à re-fetcher » de v0.1 était une erreur de scan (latence de mount). S-F3-2 corrigé : lecture LOCALE, aucun fetch. Les 4 décisions de scoping §8 (S-F3-1 LC-09 = outil mathématique seul ; S-F3-2 Garfinkle local ciblé ; S-F3-3 extraction ciblée DHN/ères ; S-F3-4 sceau conditionné à l'issue) sont ADOPTÉES (intrant : GO Thierry). GEL §2 (énoncé A2★ + cibles F3-G1..G4) INTACT byte-identique — anti-fit préservé. Aucun sceau, aucune algèbre neuve, aucun fetch. {A4 ; A2★ ; N} INCHANGÉ. | 2026-06-13 — v0.1 : ouverture F3 (rang 2) en reprise post-F1. Gel formel de l'énoncé exact de sous-exponentialité (A2★ tel qu'écrit en LC-WORK-A2-CONJECTURE §4, repris à l'identique sous R-7) et des cibles F3-G1 (mesure n_s^gen sous-exp.), F3-G2 (charge par spike C_F bornée — non-cascade), F3-G3 (yield de charge par bounce O(1) borné), F3-G4 (taux N_b sous-exp. — DÉJÀ SCELLÉ maillon B, rappel non-testé-neuf). Plan d'extraction : Garfinkle gr-qc/0312117 ; DHN cosmological billiards hep-th/0212256 (neuf) ; KLSKS statistique d'ères (neuf). Obstacles documentés OA (Garfinkle : pas de régime convergent), OB (gap billard mini-superspace ↔ production de structure spatiale), OC (lien u_ère → charge C_F non établi), OD (LC-09 = carte de Gauss au sens φ, boîte à outils mathématique seulement, PAS un pont physique φ↔BKL). Critère de réfutation = R1/R2/R3 pré-enregistrés (LC-WORK-A2-CONJECTURE §5, repris). SANS SURCLASSEMENT (§6.4) : le test, quel qu'en soit l'issue, substantie/délimite A2★ comme objet falsifiable, PAS « A2★ prouvée / C7 levée / CCC démontrée » ; compte {A4 ; A2★ ; N} INCHANGÉ tant qu'A2★ n'est ni prouvée ni réfutée."
prerequis_kb: [LC-WORK-A2-CONJECTURE, LC-D3-C7B-VERDICT-A2, LC-D3-A1-SUPERHORIZON, LC-D3-INTERAEON-P6, LC-D3-GRADIENT-C7B, LC-D3-SPIKES-C7B, LC-WORK-BRANCHE-FALSIFIABILITE, LC-AUDIT-VERDICT]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte, piste / à étayer]
---

# LC-WORK · Cadrage F3 — substantiation d'A2★ (non-cascade)

> **Pour l'opérateur.** Ce document **ouvre** le front F3 de la branche FALSIFIABILITÉ (rang 2). Il
> exécute la discipline **anti-fit** : il **GÈLE** l'énoncé exact de sous-exponentialité et les
> cibles (§2) **avant** toute extraction de la littérature ou tout fetch. Le test proprement dit
> (confrontation à la statistique rigoureuse des singularités génériques) est l'**étape suivante**,
> sur GO, en séquence *blind fetch → commit → reconcile*. **Rien ici n'est scellé, rien n'est
> fetché.**

---

## 0. Rôle et garde-fou `[discipline §6.4 + R-7]`

F3 est le front de **substantiation d'A2★** appelé par `LC-WORK-BRANCHE-FALSIFIABILITE` (fiche F3,
rang 2). Il est le **seul** front catalogué pouvant faire **bouger** le périmètre irréductible
`{A4 ; A2★ ; N}` : substantier A2★ la porterait de `décision ouverte` vers
`formalisable`/`établi sous principes` ; la **réfuter** casserait la chaîne (A)-physique. Les deux
sont des résultats réels touchant un item gelé.

**Position exacte dans la chaîne A2 `[crucial — éviter le doublon].`** La séquence acquise est :

```
A2 (mesure de spikes générique, objet non structuré)          [LC-D3-C7B-VERDICT-A2 : `à inventer`]
   │ réduction (LC-WORK-A2-CONJECTURE)
   ▼
A2★ : Q(τ)=Σ_spikes C_F = o(e^{|w|τ})  ⟺ R_grad,gen→0          [conjecture nommée, falsifiable]
   ├── maillon A : déduction §4 (Q sous-exp ⟹ R→0, raccord A1)  ───── SCELLÉ  verif_D3_C7b_A2_reduction.py (EXIT 0)
   ├── maillon B : N_b(τ) sous-exp. (oracle Gauss-Kuzmin, P6)    ───── SCELLÉ  (idem ; N_b≈1,60·n·ln n, R²=0,9998)
   └── maille C  : NON-CASCADE (yield/bounce borné + pas de        ◄──── NON SCELLÉE  ⟸  C'EST L'OBJET DE F3
                   prolifération exponentielle de surfaces)
```

F3 **ne refait ni** la réduction A2→A2★ **ni** les maillons A/B (déjà scellés). Il attaque **la
seule maille C**, et **seulement** par confrontation à la **littérature rigoureuse** — il ne
prétend pas la prouver par algèbre interne (ce serait `hors de portée`, cf. `VERDICT-A2`).

**Garde-fou.** Quel que soit le résultat, F3 produit au mieux soit une **substantiation
principielle externe** d'A2★ (⟹ `établi sous principes (externe)`, candidate à réduction du
compte), soit une **délimitation** (A2★ reste `décision ouverte`, littérature non concluante —
comme F1), soit une **réfutation** (R1/R2/R3, §6). Cela **ne** vaut **jamais**, en soi, « C7 levée
/ (A) établie / D1 clos / N fixé / CCC démontrée ». **R-7 active dès la validation de ce gel** :
l'énoncé A2★ et les cibles F3-G1..G4 sont tenus **tels qu'écrits**, **zéro amendement** sans
consignation formelle.

---

## 1. La question F3, située `[le seul levier sur le périmètre]`

`LC-D3-C7B-VERDICT-A2` a tranché : A2 **n'est pas un théorème extractible** de la littérature.
Garfinkle (`gr-qc/0312117`) confirme le **mécanisme** de spike (un `Nᵢ` s'annulant sur une
surface `S` ⟹ bounces de part et d'autre ⟹ naissance d'une structure de spike) et le **socle du
silence** (dérivées spatiales négligeables, BKL local générique), mais déclare explicitement
l'étude **générique** des spikes « *work in progress, requires high resolution* », résolution
« *not in the convergent regime* » ⟹ **aucune loi de comptage/production générique**.

`LC-WORK-A2-CONJECTURE` a alors transformé ce trou non structuré en **une** conjecture scalaire
unique (A2★) et **scellé tout ce qui ne dépend pas de la non-cascade**. Il reste **une** maille :
la **non-cascade** (maille C). F3 demande :

> **La statistique RIGOUREUSE de la dynamique BKL générique (billards cosmologiques + mesure
> d'ères) contraint-elle le _yield de charge de gradient par bounce_ et la _production de surfaces
> de spike_ de façon à _substantier_ (ou _réfuter_) la non-cascade — donc A2★ ?**

C'est l'analogue, côté A2★, du test F1 côté coefficients : on cherche un **accès indépendant** à la
grandeur gelée (ici `Q(τ)`) dans un corpus où elle est calculable/bornée par principe.

---

## 2. GEL DE L'ÉNONCÉ ET DES CIBLES `[AVANT toute extraction / tout fetch — 2026-06-13]`

> Ces énoncés sont **figés maintenant**, issus de chaînons **déjà scellés/cadrés**. Ils ne seront
> **pas** ajustés après lecture de la littérature. Toute décision de scoping réductrice ⟹
> amendement **formel** consigné (R-7).

**Énoncé exact de sous-exponentialité (A2★, repris à l'identique de `LC-WORK-A2-CONJECTURE §4`) :**

```
A2★ (non-cascade) :  Q(τ) = Σ_{spikes actifs / horizon} C_F  =  o(e^{|w|τ})   (τ → bang)
  forme suffisante et physiquement attendue :  Q(τ) ≤ A · N_b(τ)^p ,  A,p = O(1)
  où  C_F = ∫(dF/du)² du  (charge de gradient O(1) par spike, dépend du profil)
       w  = taux du profil exact de Lim (ℓ(τ)=cosh(wτ)/w, 0710.0628)
       N_b(τ) = nombre de bounces BKL jusqu'à la profondeur τ
```

| Cible | Énoncé gelé | Réfutation associée | Statut programme | Substantiable dans la littérature rigoureuse ? |
|---|---|---|---|---|
| **F3-G1** (mesure) | `n_s^gen(τ)` (# surfaces de spike actives/horizon) **sous-exponentiel** : `n_s^gen = o(e^{cτ})`, idéalement polynomial en `N_b` | **R1** : `n_s^gen ~ e^{cτ}, c>0` | maille C, non scellée | à tester (Garfinkle « work in progress ») |
| **F3-G2** (charge/spike, non-cascade) | `C_F` par spike **borné `O(1)`** ; pas de régénération sous-horizon faisant **diverger** `C_F` | **R2** : `Σ C_F ~ e^{|w|τ}` ou plus vite | maille C, non scellée | à tester (cascade = brèche nommée par A1) |
| **F3-G3** (yield/bounce) | charge de spike engendrée **par bounce** = `O(1)` **bornée**, cohérente avec la marche aléatoire `O(1)` par bounce de l'oracle | **R3** : yield/bounce croissant avec la profondeur | maille C, non scellée | à tester (DHN billiards / mesure d'ères) |
| **F3-G4** (taux de bounces) | `N_b(τ)` **sous-exponentiel** (quasi-linéaire `~n·ln n`) | — | **DÉJÀ SCELLÉ** (maillon B) | **acquis** — rappel non-testé-neuf |

**Composition gelée :** `A2★  ⟸  (F3-G1 sous-exp.) × (F3-G2 bornée)  avec  (F3-G4 acquis)`. Le
produit `Q = n_s · ⟨C_F⟩` est sous-exponentiel **ssi** la mesure (G1) **et** la charge par spike
(G2) le sont, le taux de bounces (G4) étant déjà sous-exponentiel.

> **F3-G4 est l'analogue de F1-G3** : une cible **déjà acquise**, rappelée pour la complétude de la
> composition, **non re-testée** par F3 (anti-double-comptage).

---

## 3. Ce qui est DÉJÀ acquis — NE PAS refaire `[maillons scellés / cadrés]`

- **Réduction A2 → A2★** : faite (`LC-WORK-A2-CONJECTURE`). F3 part de l'énoncé A2★, ne le re-dérive
  pas.
- **Maillon A** (déduction `Q` sous-exp. ⟹ `R_grad,gen→0`, raccord exact à A1, contrôle de seuil
  `Q=e^{wt} ⟹ R↛0`) : **scellé** (`verif_D3_C7b_A2_reduction.py`, EXIT 0, 16/16).
- **Maillon B** (`N_b(τ)` sous-exponentiel le long de l'oracle de Gauss-Kuzmin ;
  `N_b≈1,60·n·ln n`, `R²=0,9998`, `ln(N_b)/n→0`) : **scellé** (idem). ⟹ **F3-G4 acquis**.
- **A1** (gradient par spike `I=C_F/ℓ`, scaling `1/ℓ` universel, `I→0` hors cascade) :
  **scellé** (`LC-D3-A1-SUPERHORIZON`).
- **Oracle physique BKL** (« le bang gagne », marche `O(1)` par bounce, pas d'emballement) :
  **scellé** (`LC-D3-INTERAEON-P6`). ⟹ c'est **l'oracle pertinent pour A2★**, et **non** LC-09
  (cf. OD/§8).

---

## 4. Plan d'extraction `[étape SUIVANTE — sur GO ; séquence anti-fit imposée]`

> Séquence **imposée** (branche FALSIFIABILITÉ §protocole) : *blind fetch → commit value →
> reconcile*. Confrontation **après** gel ci-dessus. Séparation incognito si une passe froide est
> requise.

1. **Garfinkle, `gr-qc/0312117`** (PRL 93 161101, 2004). *Statut KB : **PRÉSENT** (`0312117v4.pdf`,
   PDF natif 4 p. — lecture **locale**, **aucun fetch**). Déjà évalué par `VERDICT-A2` contre A2
   **non structuré** ; ici **re-confronté à A2★ structurée** (maille C).* Cible d'extraction :
   toute borne, même heuristique, sur la **production de surfaces de spike** et le **régime de
   convergence** ⟹ F3-G1, F3-G3.
2. **Damour–Henneaux–Nicolai, « Cosmological billiards », `hep-th/0212256`** (Class. Quantum Grav.
   20 (2003) R145). *Neuf — non en KB.* Cible : le formalisme **billard** (dynamique d'ères comme
   réflexions sur des murs de Weyl/courbure dans l'espace des échelles), sa **mesure invariante**
   (carte de Gauss / Gauss-Kuzmin sur les paramètres d'ère), et ce qu'il dit — ou **ne dit pas** —
   sur la **production de structure spatiale** (spikes) ⟹ F3-G3, et **OB** (le gap mini-superspace
   ↔ inhomogénéité).
3. **Khalatnikov–Lifshitz–Sinai–Khanin–Shchur (~1985), statistique d'ères Mixmaster.** *Neuf — non
   en KB ; cité dans `source_externe` de `A2-CONJECTURE` comme « à ajouter à 04_references si A2★
   sealée ».* Cible : la **distribution stationnaire** des paramètres d'ère (Gauss-Kuzmin) et les
   **taux de mélange** ⟹ borne sur la fréquence/intensité des événements générateurs de spike,
   F3-G3.
4. **(en KB, rappel)** Lim `0710.0628` (profil exact, `C_F^Lim=2π·A²`) ; Andersson–van Elst–Lim–
   Uggla `gr-qc/0402051` (silence). **Aucun fetch neuf** — bornes de référence pour `C_F`.

**Sortie attendue de l'étape d'exécution :** un chaînon `LC-D-F3-A2STAR` (ou verdict
`LC-D3-F3-VERDICT`) consignant, pour chaque cible gelée, *concordant / non concordant / non
concluant*, sans surclassement. Sceau candidat **seulement** si une borne rigoureuse émerge
(improbable, cf. §7) ; sinon délimitation documentée (pas de sceau neuf, comme l'aurait été un F1
non branché).

---

## 5. Obstacles documentés `[à confronter — pré-enregistrés]`

- **OA — Pas de régime convergent (Garfinkle).** L'étude générique des spikes est déclarée « work
  in progress » ; aucune loi de comptage n'en est extractible **par construction**. ⟹ F3-G1
  restera très probablement **non concluant** par cette source seule (c'est le constat de
  `VERDICT-A2`, ici re-confronté à A2★ structurée, pas contourné).
- **OB — Gap mini-superspace ↔ structure spatiale.** Les billards cosmologiques (DHN) décrivent la
  dynamique des **degrés d'échelle/anisotropie** (réflexions sur murs), dans un cadre **local/
  ultralocal**. Les **spikes sont des inhomogénéités spatiales** (gradients sur une surface `S`).
  Le formalisme billard borne la dynamique d'**ère**, mais le **pont ère → charge de gradient
  spatiale `C_F`** n'est **pas** fourni par DHN. C'est l'analogue F3 de l'obstacle O1 de F1 (le
  formalisme accède à la structure mais peut-être pas au coefficient visé).
- **OC — Lien `u_ère → C_F` non établi.** Même en disposant de la distribution de Gauss-Kuzmin des
  paramètres d'ère `u`, l'application `u → C_F(spike)` (charge de gradient engendrée par un bounce
  d'ère donné) n'est pas dans la littérature. Sans elle, `Q = Σ C_F` reste **non bornable**
  rigoureusement même si `N_b` et `u` sont contrôlés.
- **OD — `LC-09-GAUSS-SEIDEL` est un FAUX AMI `[scoping critique, cf. §8].`** LC-09 traite la
  **sérialité d'agent du sous-programme φ** (Gauss–Seidel vs Jacobi du flot modulaire → moyennes
  métalliques / Fibonacci → `φ`). L'objet mathématique **commun** avec BKL est la **carte de
  Gauss** `x↦{1/x}` et sa **mesure de Gauss-Kuzmin** ; mais l'**application physique** de LC-09
  (φ) est **distincte** de l'application BKL (statistique d'ères du deep-bang). LC-09 est donc une
  **boîte à outils mathématique** réutilisable (ergodicité, mesure stationnaire, taux de mélange de
  la carte de Gauss), **jamais** un pont physique φ↔BKL. Confondre les deux serait une
  **consolidation illusoire** (le pont φ↔CCC est `hors de portée`, et le programme distingue
  strictement convergence vs consolidation). **L'oracle BKL pertinent reste `LC-D3-INTERAEON-P6`.**

---

## 6. Critère de réfutation `[pré-enregistré — repris de LC-WORK-A2-CONJECTURE §5, R-7]`

A2★ serait **réfutée** (et C7-b rouvert) par l'un des constats suivants, issu d'une simulation
générique 3D sans symétrie ou d'un argument analytique rigoureux :

- **R1 — Prolifération exponentielle de spikes** : `n_s^gen(τ) ~ e^{cτ}, c>0` (réfute F3-G1).
- **R2 — Cascade de charge** : `C_F` par spike divergeant par régénération sous-horizon, `Σ C_F ~
  e^{|w|τ}` ou plus vite (réfute F3-G2 ; brèche nommée par A1).
- **R3 — Yield par bounce non borné** : charge de spike engendrée **par bounce** croissant avec la
  profondeur, contredisant la marche `O(1)` par bounce de l'oracle (réfute F3-G3).

**Soutien (non preuve).** Mécanisme de Garfinkle + oracle scellé (marche `O(1)`/bounce) + `N_b`
sous-exp. (maillon B) rendent A2★ **physiquement attendue**. Aucune de ces pièces ne **prouve**
l'absence de cascade en générique — c'est précisément ce que F3 va sonder, en sachant que la
littérature **ne le ferme pas** (OA).

---

## 7. Issue honnête anticipée + statut épistémique `[discipline §6.4 — sans surclassement]`

- **Issue la plus probable (≈ comme F1) :** **délimitation**. La littérature rigoureuse contraint
  la dynamique d'**ère** (Gauss-Kuzmin, `N_b` sous-exp. — déjà acquis) mais **ne borne pas** la
  **production de charge de gradient spatiale** par bounce (OA/OB/OC). ⟹ A2★ reste `décision
  ouverte`, **mieux située** (on saura *quelle pièce précise manque* : le pont `u → C_F`).
  Périmètre `{A4 ; A2★ ; N}` **INCHANGÉ**.
- **Issue favorable (peu probable) :** une borne rigoureuse sur le yield/bounce (DHN + statistique
  d'ères) suffisamment forte pour impliquer `Q = o(e^{|w|τ})` ⟹ A2★ `établi sous principes
  (externe)` ⟹ **candidate à réduction** de `{A4 ; A2★ ; N}` (à auditer froidement avant tout
  décompte).
- **Issue défavorable :** un constat R1/R2/R3 ⟹ A2★ **réfutée** ⟹ chaîne (A)-physique cassée
  (résultat réel, négatif, à propager).
- **Tag de sortie :** `établi sous principes (externe)` (favorable) / `décision ouverte` mieux
  située (probable) / `réfutée` (défavorable). **Jamais** « C7 levée » sur la seule base de F3 sans
  audit froid.

---

## 8. Décisions de scoping à trancher `[surfacées AVANT exécution]`

1. **S-F3-1 (OD) — usage de `LC-09-GAUSS-SEIDEL`.** Réinjecter LC-09 **uniquement** comme boîte à
   outils mathématique (carte de Gauss / Gauss-Kuzmin : mesure stationnaire, ergodicité, mélange),
   **sans** prétendre à un pont physique φ↔BKL. *Recommandation : OUI, avec note R-7 explicitant la
   distinction.* **ADOPTÉ.**
2. **S-F3-2 — Garfinkle.** `gr-qc/0312117` **présent en KB** (`0312117v4.pdf`, PDF natif 4 p.) ⟹
   **aucun re-fetch** ; lecture **locale** ciblée sur la production de spikes (F3-G1/G3), pour
   confronter à **A2★ structurée** (l'évaluation antérieure de `VERDICT-A2` visait A2 non
   structuré). **ADOPTÉ.**
3. **S-F3-3 — profondeur sur DHN / statistique d'ères.** Extraction **ciblée** (mesure d'ère +
   énoncé explicite sur la production de structure spatiale) vs revue large. *Recommandation :
   ciblée — l'enjeu est précisément le pont `u → C_F` (OC), pas une revue des billards.*
   **ADOPTÉ.**
4. **S-F3-4 — sceau ou pas.** Ne sceller un `verif_F3_*` **que si** une borne rigoureuse émerge
   (issue favorable). Sinon, délimitation documentée sans sceau neuf (comme un F1 non branché).
   *Recommandation : conditionner le sceau à l'issue.* **ADOPTÉ.**

---

## 9. Garde-fou / discipline `[autoportant]`

- **§6.4** : `établi (algèbre)` / `établi sous principes` atteste l'algèbre + les cibles, **jamais**
  « CCC démontrée / C7 levée / D1 clos / N fixé ». F3, hors issue favorable auditée, est une
  **substantiation/délimitation**, **pas** une réduction du compte.
- **Anti-fit** : énoncé A2★ et cibles F3-G1..G4 **gelés ci-dessus, avant tout fetch** ; séquence
  *blind fetch → commit → reconcile* ; séparation incognito pour toute passe froide.
- **Anti-doublon** : F3 **n'attaque que la maille C** (non-cascade) ; maillons A/B **déjà scellés**,
  réduction A2→A2★ **déjà faite** — non refaits.
- **Anti-consolidation illusoire** : OD — LC-09 = outil mathématique, pas pont physique φ↔BKL.
- **R-7** : dès la validation de ce gel, aucun déplacement de fichier sans vérifier les renvois
  (chaînons / logs / sceaux .py) ; ancres `count==1`, diffs et frontmatter validés à la propagation.

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`établi sous principes (externe)` : substantié par un résultat externe rigoureux, sous ses hypothèses — à auditer froidement avant tout décompte.
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. simulation générique 3D sans symétrie ; pont φ↔CCC).
`piste / à étayer` : lead biblio/exploratoire (branche FALSIFIABILITÉ) — jamais `établi`.
