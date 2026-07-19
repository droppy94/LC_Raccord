---
id: LC-D-D1-VERROU-FLRW
titre: "Verdict de cadrage (VERROU-D1, secteur FLRW) — la cible D1c-2 du cadrage LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4 (69770677…548f691) est TRANCHÉE en FLRW : NÉGATIVE. Le candidat-sélecteur #5 (stabilité inter-éons) NE FERME PAS D1 dans le secteur symétrique, ET son ancrage candidat à A4 n'y est pas réalisable. VERDICT = Δ1-b (DÉLIMITATION BORNÉE, défaut du critère tripartite), avec glissement Δ1-c sur le lien A4. SANS SCEAU (cartographique, aucune algèbre neuve : consolide le sceau verif_D1_stabilite.py — rejoué EXIT 0 cette session, 4 assertions — et verif_D1_atlas.py EXIT 0, déjà scellés, et le nœud LC-A-D1-STABILITE-WEYL v0.1). TROIS MURS SCELLÉS en FLRW (le seul résultat ici NEUF vs LC-A-D1-STABILITE-WEYL = le 4e, l'ancrage A4) : (1) RELATION ≠ VALEURS — exiger la stabilité (non-emballement de (mᵢ,λᵢ) sous la carte de Markwell-Stevens éq.14) ⟹ une seule contrainte m̂λ̂ = 9k²/4 (droite fixe entière, Jacobien non-hyperbolique val.propre 1 double, runaway géométrique hors d'elle) ; sur cette droite c₁=√(2λ̂/3k) VARIE encore (famille à 1 paramètre) ⟹ #5 réduit la liberté mais ne fixe PAS c₁ (firewall F-c confirmé scellé) ; (2) DÉGÉNÉRESCENCE k=0 — à univers spatialement plat (NOTRE cas, Λ>0), #5 est VACANT : Penrose-55d (c₁²=2λ̂/3k) diverge, la droite fixe dégénère en m̂λ̂=0 triviale, et Tod (c₁=(λ̂/m̂)^{1/4}) est stable d'office mais SACRIFIE λ̂=λ ⟹ #5 ne sélectionne rien à k=0 ; (3) #5 ⊥ WEYL en FLRW — C_abcd ≡ 0 (FLRW conformément plat, indép. de (m,λ)) tandis que C≠0 en Kasner (sourcé par l'anisotropie, vide) ⟹ secteur de FOND (m,λ) ⊥ secteur de MARÉE (g₃) dans le symétrique ; D3 (Weyl) y est vacant, le pont #5→D3 ne tient pas. (4) ANCRAGE A4 — NEUF — « A4 ⟹ #5 » est MORT en FLRW : la seule lecture de A4 non-vacante hors-symétrie (Weyl→0) est ⊥ au secteur (m,λ) où vit #5 (puisque C≡0 en FLRW) ; les deux autres lectures heurtent le firewall gelé — entropie S_grav≡f(Weyl) = F-a (circulaire G1-c scellé, LC-D-F4-A4-PRINCIPIEL) ; nettoyage-𝓘⁺ par no-hair = F-b (verrouillage A4-nœud-source, A4←{N≡Λ ; β/O₂ ; no-hair générique externe ; évaporation BH QG}, LC-D-IRREDUCTIBILITE-MOYENS) ; côté stabilité de A4 déjà classé F-d (sélection ≠ dérivation, G1-b). REDIRECTION (convergente avec LC-A-D1-STABILITE-WEYL §5, déjà gravée) : le secteur symétrique est ÉPUISÉ (tout y est cartographié [atlas], marginal [stabilité], vacant [Weyl] ou verrouillé [A4]) ; le seul degré de liberté restant = g₃ (la marée, Weyl rescalé), où D3 a un contenu réel ⟹ la route ouverte = D1c-3 HORS-FLRW / D3 (Weyl→0) INHOMOGÈNE, qui SUBSUME le fork candidat #3 du cadrage. RÉSULTAT RÉEL, NÉGATIF, FALSIFIABLE (prédiction conditionnelle CCC+Penrose+stabilité : m̂λ̂=9k²/4 reliant densité de radiation, Λ et courbure — non une fermeture). SANS SURCLASSEMENT (§6.4) : trancher D1c-2 en FLRW NE RÉDUIT RIEN — n'incrémente aucun compte au-delà du sceau déjà existant, ne ferme pas D1 (le verrou reste OUVERT, déplacé vers l'inhomogène), ne fixe pas N, ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "verdict de cadrage — DÉLIMITATION (secteur FLRW, SANS sceau). Tranche la cible D1c-2 du cadrage LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4 en consolidant des pièces déjà scellées (verif_D1_stabilite.py, verif_D1_atlas.py) et un nœud déjà gravé (LC-A-D1-STABILITE-WEYL). Cartographie négative et falsifiable. Gel SHA in-fichier recouvrable (R-36)."
statut: "verdict actif — VERROU-D1 secteur FLRW = Δ1-b (délimitation bornée ; glissement Δ1-c sur l'ancrage A4). Candidat #5 NE FERME PAS D1 en symétrie (relation ≠ valeurs ; vacant k=0 ; ⊥ Weyl) ; « A4 ⟹ #5 » non réalisable en FLRW (Weyl→0 vacant car ⊥ fond ; entropie F-a circulaire ; no-hair F-b verrouillé). Secteur symétrique ÉPUISÉ. Redirection vers D1c-3 hors-FLRW / D3-inhomogène (subsume fork #3). SANS SURCLASSEMENT (§6.4) : D1 reste OUVERT (déplacé) ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
statut_id: "provisoire — à enregistrer si validé (LC-00-INDEX)"
sceau: "AUCUN (verdict cartographique sans algèbre neuve). Pièces amont SCELLÉES rejouées cette session : verif_D1_stabilite.py (EXIT 0, 4 assertions stabilité/Weyl) ; verif_D1_atlas.py (EXIT 0, 4 assertions atlas/runaway). Nœud amont gravé : LC-A-D1-STABILITE-WEYL v0.1 (verdict établi). Firewall amont : LC-D-F4-A4-PRINCIPIEL (G1-b/G1-c) ; LC-D-IRREDUCTIBILITE-MOYENS (A4 nœud-source)."
tags: [module-A, module-D, verdict, cadrage, verrou-D1, facteur-conforme, secteur-FLRW, delimitation, Delta1-b, Delta1-c, candidat-5, stabilite-inter-eons, relation-vs-valeurs, m-lambda, 9k2sur4, droite-fixe, Jacobien-non-hyperbolique, valeur-propre-1, runaway, c1, degenerescence-k0, univers-plat, Penrose-55d, Tod-2015, Weyl, C-abcd, conformement-plat, Kasner, secteur-fond, secteur-maree, g3, D3, ancrage-A4, A4-mort-FLRW, firewall, F-a, F-b, F-c, F-d, circularite-G1c, verrouillage, noeud-source, IRREDUCTIBILITE-MOYENS, F4-A4-PRINCIPIEL, redirection, D1c-3, hors-FLRW, inhomogene, fork-candidat-3, secteur-symetrique-epuise, falsifiable-negatif, prediction-conditionnelle, sans-sceau, R-36, §6.4, non-surclassement, perimetre-irreductible, A4, A2star, N]
prerequis_kb: [LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4, LC-A-D1-STABILITE-WEYL, LC-A-D1-FACTEUR-CONFORME, LC-D-F4-A4-PRINCIPIEL, LC-D-IRREDUCTIBILITE-MOYENS, LC-D3-SPECTRE-K3, LC-WORK-A3-D1-PASSERELLE]
renvois: [LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4, LC-A-D1-STABILITE-WEYL, LC-A-D1-FACTEUR-CONFORME, LC-D-F4-A4-PRINCIPIEL, LC-D-IRREDUCTIBILITE-MOYENS, LC-D3-SPECTRE-K3, LC-00-INDEX, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, délimitation, cartographie d'obstruction, falsifiable / négatif, lecture / non scellé, décision ouverte]
version: 0.1
langue: fr
date: 2026-06-28
maj: "2026-06-28 — v0.1 : GRAVURE du verdict de cadrage pour le secteur FLRW de la cible D1c-2 (cadrage LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4, gel 69770677…548f691), sur GO Thierry, en consolidation AVANT amendement-pivot. AUCUNE algèbre neuve : le verdict CONSOLIDE des pièces déjà scellées/gravées et y SUPERPOSE le seul angle neuf du cadrage (l'ancrage A4). Pièces rejouées cette session : verif_D1_stabilite.py EXIT 0 (4 assertions ; carte de Markwell-Stevens éq.14, invariant mλ, droite fixe m̂λ̂=9k²/4, Jacobien val.propre 1 double, runaway hors d'elle ; Weyl C≡0 FLRW vs C≠0 Kasner) ; verif_D1_atlas.py EXIT 0 (4 assertions ; 3 prescriptions convergent Ω̂=c₁â, c₁=√(2λ̂/3k) sur la droite). Nœud amont déjà gravé : LC-A-D1-STABILITE-WEYL v0.1 (2026-06-07), verdict établi « #5 ne ferme pas D1 ». CE QUE CE FICHIER AJOUTE (neuf vs le nœud) : la cible D1c-2 posait aussi « #5 est-il DÉRIVABLE de A4 ? » (absent du nœud, propre au cadrage) — réponse en FLRW : NON réalisable, car (i) la lecture A4=Weyl→0 est ⊥ au secteur de fond (m,λ) où vit #5 (C≡0 en FLRW), donc vacante ; (ii) la lecture A4=faible entropie est F-a (circulaire G1-c scellé) ; (iii) la lecture A4=no-hair-𝓘⁺ est F-b (verrouillage A4-nœud-source per IRREDUCTIBILITE-MOYENS) ; (iv) le côté stabilité de A4 est F-d (sélection ≠ dérivation, G1-b). VERDICT = Δ1-b (délimitation bornée, défaut du critère tripartite du cadrage), avec glissement Δ1-c sur le lien A4. REDIRECTION : secteur symétrique ÉPUISÉ ⟹ route ouverte = D1c-3 hors-FLRW / D3 (Weyl→0) inhomogène (secteur de marée g₃), qui SUBSUME le fork candidat #3 — convergente avec la redirection DÉJÀ gravée en LC-A-D1-STABILITE-WEYL §5. Note de discipline : ce verdict ferme la cible D1c-2 du cadrage SANS rouvrir le sceau existant ; l'amendement-pivot (fichier compagnon LC-WORK-AMENDEMENT-R7-D1-PIVOT-D1C3) DATE le passage à la Phase B. Fichier neuf (additif, .md +1, id +1 ; aucun .py, aucun sceau). Gel SHA in-fichier recouvrable (R-36) = sha256 du présent fichier (valeur consignée hors-fichier au dépôt). SANS SURCLASSEMENT (§6.4) : trancher D1c-2 en FLRW NE RÉDUIT RIEN — D1 reste OUVERT (verrou déplacé vers l'inhomogène, non clos) ; ne fixe pas N ; ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ; CCC non démontrée NI réfutée. (cf. LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4, LC-A-D1-STABILITE-WEYL v0.1, LC-A-D1-FACTEUR-CONFORME v0.4 §4-bis/§5, LC-D-F4-A4-PRINCIPIEL v0.2, LC-D-IRREDUCTIBILITE-MOYENS v0.1, LC-D3-SPECTRE-K3)"
---

# Verdict de cadrage — VERROU-D1, secteur FLRW : la cible `D1c-2` est NÉGATIVE (`Δ1-b`)

> **Cartographique, SANS sceau.** Consolide des pièces **déjà scellées** (`verif_D1_stabilite.py`,
> `verif_D1_atlas.py` — rejouées **EXIT 0** cette session) et un nœud **déjà gravé**
> (`LC-A-D1-STABILITE-WEYL` v0.1), et y **superpose le seul angle neuf** du cadrage : l'**ancrage A4**.
> **Aucune algèbre neuve.** Gel SHA in-fichier **recouvrable** (R-36).

## 0. Ce que ce verdict tranche

Cible **`D1c-2`** du cadrage `69770677…548f691` : « en FLRW radiation, `A4` ⟹ `#5` ⟹ **`c₁` unique** ? ».
**Réponse : NON.** Le candidat #5 (stabilité inter-éons) **ne ferme pas D1** dans le secteur symétrique,
**et** son ancrage candidat à A4 n'y est pas réalisable. Verdict = **`Δ1-b`** (délimitation bornée),
glissement **`Δ1-c`** sur le lien A4.

## 1. Trois murs scellés (secteur symétrique) `[établi — verif_D1_stabilite EXIT 0]`

| # | mur | contenu | firewall |
|---|---|---|---|
| 1 | **relation ≠ valeurs** | stabilité ⟹ `m̂λ̂ = 9k²/4` (droite fixe, Jacobien non-hyperbolique μ=1 double, runaway hors d'elle) ; `c₁=√(2λ̂/3k)` **varie** sur la droite (famille à 1 paramètre) | **F-c** |
| 2 | **dégénérescence `k=0`** | univers plat (**notre cas**) : Penrose-55d diverge, droite fixe → triviale, Tod stable d'office mais sacrifie `λ̂=λ` ⟹ #5 **vacant** | — |
| 3 | **#5 ⊥ Weyl** | `C_abcd ≡ 0` en FLRW (conf. plat, indép. `(m,λ)`) vs `C≠0` Kasner (anisotropie) ⟹ fond `(m,λ)` ⊥ marée `g₃` ; D3 vacant ici | — |

⟹ #5 **réduit** la liberté (de « un `c₁` » à « une relation `m̂λ̂` ») mais **n'atteint pas** la fermeture.
*(Déjà gravé : `LC-A-D1-STABILITE-WEYL`.)*

## 2. L'ancrage A4 — le seul angle NEUF (vs le nœud existant)

La cible `D1c-2` posait en plus : **« `#5` est-il DÉRIVABLE de `A4` ? »**. En FLRW, **mort à tous les liens** :

- **A4 = Weyl→0** : ⊥ au secteur `(m,λ)` où vit #5 (puisque `C≡0` en FLRW) ⟹ **vacant**.
- **A4 = faible entropie** (`S_grav≡f(Weyl)`) : **`F-a`** — circulaire `G1-c` scellé (`LC-D-F4-A4-PRINCIPIEL`).
- **A4 = nettoyage-`𝓘⁺` (no-hair)** : **`F-b`** — verrouillage A4-nœud-source, `A4←{N≡Λ ; β/O₂ ; no-hair
  générique externe ; évaporation BH QG}` (`LC-D-IRREDUCTIBILITE-MOYENS`).
- côté stabilité de A4 : **`F-d`** — sélection ≠ dérivation (`G1-b`).

⟹ `Δ1-b` **renforcé**, avec glissement **`Δ1-c`** (la seule « dérivation » de #5 disponible serait
circulaire ou verrouillée).

## 3. Verdict & redirection

- **Verdict `D1c-2` (FLRW) = `Δ1-b`** (délimitation bornée, défaut du critère tripartite). Résultat
  **réel, négatif, falsifiable** (prédiction conditionnelle CCC+Penrose+stabilité : `m̂λ̂=9k²/4` reliant
  densité de radiation, `Λ` et courbure — **pas** une fermeture).
- **Secteur symétrique ÉPUISÉ** : tout y est cartographié (atlas), marginal (stabilité), vacant (Weyl) ou
  verrouillé (A4).
- **Route ouverte = `D1c-3` HORS-FLRW / D3 (Weyl→0) INHOMOGÈNE** (secteur de marée `g₃`), qui **subsume le
  fork candidat #3** du cadrage — **convergente** avec la redirection **déjà gravée**
  (`LC-A-D1-STABILITE-WEYL` §5 : « D3-inhomogène promu route principielle »).

## 4. Sans surclassement (`§6.4`) et périmètre

- Trancher `D1c-2` en FLRW **ne réduit rien** : **D1 reste OUVERT** (verrou **déplacé** vers l'inhomogène,
  non clos) ; ne fixe pas `N` ; ne réduit pas `A4`.
- **`{A4 ; A2★ ; N}` INCHANGÉ** ; `N` non fixé (`≡ Λ`) ; `A4` non réduit ; `A2★` non tranché ;
  **CCC non démontrée NI réfutée**.

*(cf. `LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4` `69770677…`, `LC-A-D1-STABILITE-WEYL` v0.1,
`LC-A-D1-FACTEUR-CONFORME` v0.4 §4-bis/§5, `LC-D-F4-A4-PRINCIPIEL` v0.2 (G1-b/G1-c),
`LC-D-IRREDUCTIBILITE-MOYENS` v0.1 (A4 nœud-source), `LC-D3-SPECTRE-K3`)*
