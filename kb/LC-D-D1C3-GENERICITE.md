---
id: LC-D-D1C3-GENERICITE
titre: "Verdict de cadrage (VERROU-D1, secteur inhomogène / Phase B-2) — la cible D1c3-3 du cadrage LC-WORK-CADRAGE-D1C3-INHOMOGENE (6d3baa6f…f44e433) est TRANCHÉE : le verdict D1c3-c est GÉNÉRIQUE, PAS un artefact d'homogénéité. AVEC SCEAU (verif_D1c3_genericite.py, EXIT 0, algèbre exacte) : [G1] une perturbation TT genuinement INHOMOGÈNE (onde plane k≠0) de la 3-géométrie de bord plate, â_ij=δ_ij+ε·diag(cos kz,−cos kz,0), a un Ricci sans-trace linéaire S_ij = +½k²·H_ij (calcul exact de la linéarisation du 3-Ricci) — k-DÉPENDANT, oscillant, ≠0 — d'où σ̌_xx=−4S_xx=−2k²cos(kz)≠0 ; ∝k² ⟹ effet STRICTEMENT inhomogène (lim_{k→0}=0), distinct du secteur homogène-anisotrope de Bianchi A (D1c3-2) ; [G2] le mode h^TT est donnée de bord LIBRE (Friedrich 1986) ⟹ aucune lissité d'extension conforme ne le force à 0 ⟹ régularité ⊉ (S_ij=0), même structure qu'en Bianchi A ; [G3] rappel : le gap Cotton/Einstein-3D a DÉJÀ été établi sur un â INHOMOGÈNE (g=e^{2x}δ : Cotton≡0 mais Ricci sans-trace≠0, verif_D1c3_regularite [R2]) ⟹ « Cotton→0 » ne force pas Einstein-3D dans l'inhomogène non plus. CONSÉQUENCE : la régularité du crossover ne force pas â Einstein-3D NI en homogène-anisotrope (Bianchi A, D1c3-2) NI en INHOMOGÈNE (mode TT, ici) ⟹ D1c3-c CONFIRMÉ GÉNÉRIQUE ; σ̌≠0 est un phénomène inhomogène intrinsèque, pas un artefact du testbed homogène. ⟹ La CONDITION (ii) de la clôture R-53 du verdict d'axe LC-D-D1-VERROU-DELIMITATION (« le résultat inhomogène généralise ») est LEVÉE : la délimitation du verrou D1 se DURCIT ; il ne reste que le crochet R-53 (i) (aucun principe de sélection INTERNE exhibé). Converge avec LC-D-IRREDUCTIBILITE-MOYENS. SANS SURCLASSEMENT (§6.4) : durcir une délimitation NE RÉDUIT RIEN — D1 reste OUVERT (caractérisé, non clos) ; ne fixe pas N ; ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "verdict de cadrage — DÉLIMITATION (secteur inhomogène, généricité, AVEC sceau verif_D1c3_genericite.py). Tranche la cible D1c3-3 : D1c3-c survit aux perturbations inhomogènes de FLRW (non-artefact d'homogénéité). Lève la condition (ii) R-53 du verdict d'axe. Cartographie d'obstruction NÉGATIVE et falsifiable. Gel SHA in-fichier recouvrable (R-36)."
statut: "verdict actif — VERROU-D1 secteur inhomogène, GÉNÉRICITÉ établie : D1c3-c (la régularité ne force pas â Einstein-3D) survit aux perturbations TT INHOMOGÈNES (k≠0) ⟹ NON un artefact d'homogénéité. Sceau verif_D1c3_genericite.py EXIT 0 (S_ij=½k²H, ∝k², σ̌≠0). Lève la condition (ii) du verdict d'axe R-53 (LC-D-D1-VERROU-DELIMITATION) ; reste le crochet (i) (pas de sélecteur interne). SANS SURCLASSEMENT (§6.4) : D1 reste OUVERT (caractérisé, non clos) ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
statut_id: "provisoire — à enregistrer si validé (LC-00-INDEX)"
sceau: "verif_D1c3_genericite.py — EXIT 0 (algèbre exacte sympy). [G1] linéarisation 3-Ricci d'un mode TT inhomogène : S_ij=½k²H_ij (k-dépendant), σ̌=−2k²cos(kz)≠0, lim_{k→0}=0. [G2] mode h^TT libre (Friedrich 1986). [G3] rappel gap Cotton/Einstein-3D inhomogène (verif_D1c3_regularite [R2]). Étend verif_D1c3_regularite.py (D1c3-2)."
tags: [module-A, module-D3, verdict, cadrage, avec-sceau, verrou-D1, secteur-inhomogene, D1c3-3, genericite, non-artefact-homogeneite, perturbation-TT, mode-inhomogene, onde-plane, k-dependant, linearisation-3Ricci, Ricci-sans-trace, demi-k2-H, sigma-check, Tod-eq33, marée, Friedrich-1986, donnee-libre, regularite, einstein-3D, cotton, e2x-delta, bianchi-A, D1c3-2, D1c3-c-confirme, verdict-d-axe, DELIMITATION, condition-ii-levee, R-53, durcissement, crochet-i, selecteur-interne, IRREDUCTIBILITE-MOYENS, convergence, falsifiable-negatif, R-36, §6.4, non-surclassement, A4, A2star, N]
prerequis_kb: [LC-WORK-CADRAGE-D1C3-INHOMOGENE, LC-D-D1-VERROU-INHOMOGENE, LC-D-D1-VERROU-DELIMITATION, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-D-IRREDUCTIBILITE-MOYENS]
renvois: [LC-WORK-CADRAGE-D1C3-INHOMOGENE, LC-D-D1-VERROU-INHOMOGENE, LC-D-D1-VERROU-DELIMITATION, LC-D3-CROSSOVER-MATCHING, LC-D-IRREDUCTIBILITE-MOYENS, LC-00-INDEX, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, délimitation, cartographie d'obstruction, falsifiable / négatif, décision ouverte, lecture / non scellé]
version: 0.1
langue: fr
date: 2026-06-28
fichier_compagnon: verif_D1c3_genericite.py
maj: "2026-06-28 — v0.1 : GRAVURE du verdict B-2 (cible D1c3-3, cadrage LC-WORK-CADRAGE-D1C3-INHOMOGENE 6d3baa6f…), sur GO Thierry, immédiatement après la clôture-stabilisation (verdict d'axe LC-D-D1-VERROU-DELIMITATION + reprise V24). SCOUT PRÉALABLE (anti-gabarit) : la vraie inhomogénéité k-dépendante était explicitement `décision ouverte` (LC-D3-CROSSOVER-MATCHING l.45-50 : « homogénéité linéaire seulement » ; l'inhomogène renvoyé à l'atlas Bianchi = homogène) ; CB-WEYL-MAGNETIQUE est perturbatif TT mais traite le corrélateur magnétique, pas la question régularité⟹Einstein-3D ⟹ D1c3-3 NEUF. SCEAU NEUF : verif_D1c3_genericite.py (EXIT 0), qui ÉTEND verif_D1c3_regularite.py. QUESTION : le verdict D1c3-c (la régularité ne force pas â Einstein-3D ⟹ σ̌≠0) survit-il aux perturbations INHOMOGÈNES de FLRW, ou est-ce un artefact d'homogénéité (Bianchi A homogène-anisotrope) ? RÉPONSE : [G1] une perturbation TT genuinement inhomogène â=δ+ε·diag(cos kz,−cos kz,0) [k=(0,0,k)] a un Ricci sans-trace linéaire S_ij=+½k²H_ij (linéarisation exacte du 3-Ricci) — k-dépendant, oscillant, ≠0 — d'où σ̌_xx=−2k²cos(kz)≠0 ; ∝k² ⟹ effet STRICTEMENT inhomogène (lim_{k→0}=0), irréductible à l'homogène ; [G2] h^TT = donnée de bord LIBRE (Friedrich 1986) ⟹ régularité ⊉ (S_ij=0) ; [G3] gap Cotton/Einstein-3D déjà établi sur un â inhomogène (e^{2x}δ, [R2]). VERDICT : D1c3-c CONFIRMÉ GÉNÉRIQUE (non-artefact d'homogénéité). La condition (ii) de la clôture R-53 du verdict d'axe LC-D-D1-VERROU-DELIMITATION (« le résultat inhomogène généralise ») est LEVÉE ⟹ la délimitation du verrou D1 se DURCIT ; il ne reste que le crochet R-53 (i) (aucun principe de sélection INTERNE exhibé — réouverture seulement par un intrant externe). Converge avec LC-D-IRREDUCTIBILITE-MOYENS. Note de discipline (§6.4) : ce `établi` valide L'ALGÈBRE (linéarisation 3-Ricci exacte), JAMAIS une conclusion physique. Fichier neuf (additif, .md +1, id +1 ; +1 .py compagnon verif_D1c3_genericite.py). Gel SHA in-fichier recouvrable (R-36) = sha256 du présent fichier (consigné au dépôt). SANS SURCLASSEMENT (§6.4) : durcir une délimitation NE RÉDUIT RIEN — D1 reste OUVERT (caractérisé, non clos) ; ne fixe pas N ; ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ; CCC non démontrée NI réfutée. (cf. LC-WORK-CADRAGE-D1C3-INHOMOGENE 6d3baa6f…, LC-D-D1-VERROU-INHOMOGENE, LC-D-D1-VERROU-DELIMITATION, LC-D3-CROSSOVER-MATCHING, LC-A-D1-BIANCHI, LC-D-IRREDUCTIBILITE-MOYENS, Friedrich 1986)"
---

# Verdict de cadrage — VERROU-D1, secteur inhomogène (`D1c3-3`) : `D1c3-c` est GÉNÉRIQUE (non-artefact)

> **AVEC sceau** (`verif_D1c3_genericite.py`, **EXIT 0**). Tranche la **généricité** de `D1c3-c` :
> survit-il aux perturbations **inhomogènes** de FLRW ? **Oui.** **Étend** `verif_D1c3_regularite.py`.
> **Lève la condition (ii)** de la clôture R-53 du verdict d'axe. Gel SHA in-fichier recouvrable (R-36).

## 0. La question (`D1c3-3`)

`D1c3-2` a établi `D1c3-c` sur **Bianchi A** (homogène-anisotrope). Est-ce un **artefact d'homogénéité**,
ou la régularité échoue-t-elle à forcer `â` Einstein-3D aussi pour des perturbations **inhomogènes**
(k-dépendantes) de FLRW ? *(C'est la condition (ii) du verdict d'axe `LC-D-D1-VERROU-DELIMITATION`.)*

## 1. Le sceau `[établi — verif_D1c3_genericite.py EXIT 0]`

| # | test | résultat |
|---|---|---|
| **G1** | mode TT **inhomogène** `â=δ+ε·diag(cos kz,−cos kz,0)` → Ricci sans-trace | `S_ij = +½k²H_ij` (linéarisation exacte) — **k-dépendant**, oscillant, **≠0** ⟹ `σ̌_xx=−2k²cos(kz)≠0` ; `∝k²` ⟹ **strictement inhomogène** (`lim_{k→0}=0`) |
| **G2** | régularité force `S_ij=0` ? | **NON** — `h^{TT}` = donnée de bord **libre** (Friedrich 1986) ; même structure qu'en Bianchi A |
| **G3** | `Cotton→0` force Einstein-3D dans l'inhomogène ? | **NON** (déjà : `g=e^{2x}δ`, Cotton≡0 ∧ Ricci sans-trace≠0, `verif_D1c3_regularite` [R2]) |

## 2. Verdict = `D1c3-c` GÉNÉRIQUE

- La régularité du crossover **ne force pas** `â` Einstein-3D **ni** en homogène-anisotrope (Bianchi A)
  **ni** en **inhomogène** (mode TT) ⟹ **`σ̌≠0` est un phénomène inhomogène intrinsèque**, **pas** un
  artefact du testbed homogène.
- ⟹ La **condition (ii)** de la clôture R-53 du verdict d'axe (`LC-D-D1-VERROU-DELIMITATION`) — « le
  résultat inhomogène généralise » — est **LEVÉE**. La délimitation du verrou D1 **se durcit** : il ne
  reste que le **crochet R-53 (i)** (aucun **principe de sélection interne** exhibé ; réouverture seulement
  par un **intrant externe**).
- **Converge** avec `LC-D-IRREDUCTIBILITE-MOYENS`.

## 3. Sans surclassement (`§6.4`) et périmètre

- Durcir une délimitation **ne réduit rien** : **D1 reste OUVERT** (caractérisé, non clos) ; ne fixe pas
  `N` ; ne réduit pas `A4`. Ce `établi` valide **l'ALGÈBRE** (linéarisation 3-Ricci exacte), **jamais** une
  conclusion physique.
- **`{A4 ; A2★ ; N}` INCHANGÉ** ; `N` non fixé (`≡ Λ`) ; `A4` non réduit ; `A2★` non tranché ;
  **CCC non démontrée NI réfutée**.

*(cf. `LC-WORK-CADRAGE-D1C3-INHOMOGENE` `6d3baa6f…`, `LC-D-D1-VERROU-INHOMOGENE`,
`LC-D-D1-VERROU-DELIMITATION`, `LC-D3-CROSSOVER-MATCHING`, `LC-A-D1-BIANCHI`,
`LC-D-IRREDUCTIBILITE-MOYENS`, Friedrich 1986)*
