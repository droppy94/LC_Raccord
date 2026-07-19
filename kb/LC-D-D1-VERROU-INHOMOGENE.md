---
id: LC-D-D1-VERROU-INHOMOGENE
titre: "Verdict de cadrage (VERROU-D1, secteur INHOMOGÈNE / Phase B-1) — la cible D1c3-2 du cadrage LC-WORK-CADRAGE-D1C3-INHOMOGENE (6d3baa6f…f44e433) est TRANCHÉE sur le testbed Bianchi A : NÉGATIVE. Une condition de RÉGULARITÉ au crossover NE FORCE PAS la 3-métrique rescalée â_ij de 𝓘 à être Einstein-3D ⟹ la marée future σ̌=−4·(Ricci sans-trace de â) [Tod éq.33] NE s'annule PAS ⟹ D3-régularité NE SÉLECTIONNE PAS la prescription. VERDICT = D1c3-c (POSTULAT INDÉPENDANT : issue faible de LC-D3-CROSSOVER-ANISOTROPE rendue DÉFINITIVE pour les conditions de régularité NATURELLES). AVEC SCEAU (verif_D1c3_regularite.py, EXIT 0, algèbre exacte) : [R1] régularité-Friedrich/Tod ⊉ Einstein-3D — contre-exemple CONSTRUCTIF : un â Bianchi IX squashé (anisotropie ε) admet un crossover de Tod LISSE (1309.7248 §7) avec σ̌≠0 ; donnée conforme de bord LIBRE (Friedrich 1986) ; re-dérivation |σ̌|²=128ε²+O(ε⁴), σ̌≠0 hors isotropie, raccord continu à 0 ; [R2] le candidat le plus fort « extended-WCH = Cotton→0 » ⊉ Einstein-3D non plus — la conforme-platitude (Cotton≡0 en dim 3) est STRICTEMENT plus faible que « Ricci sans-trace=0 » : contre-exemple explicite g=e^{2x}·δ₃ (Cotton≡0 calculé, MAIS Ricci sans-trace=(⅔,−⅓,−⅓)e^{−2x}≠0, donc PAS Einstein-3D, σ̌≠0). CONSÉQUENCE : AUCUNE condition de régularité NATURELLE/dérivable ne force â Einstein-3D ; la seule qui le ferait (Ricci sans-trace=0 imposé) est ≥ postuler la courbure constante = un POSTULAT INDÉPENDANT, non dérivable de A4 (firewall FW-3 : la WCH supprime le Weyl 4D de CŒUR, elle ne contraint PAS la 3-géométrie de BORD ni son Cotton). ⟹ A3 (isotropie de l'état/de â) reste socle IRRÉDUCTIBLEMENT INDÉPENDANT ; la marée g₃ est donnée libre de Friedrich ; D1 N'EST PAS fermé par la voie D3-régularité. CONVERGE avec LC-D-IRREDUCTIBILITE-MOYENS (routes internes épuisées). AVEC les deux verdicts sectoriels (D1c-2 FLRW = Δ1-b ; D1c3-2 inhomogène = D1c3-c), le verrou D1 n'admet PAS de sélecteur de prescription INTERNE (symétrique : épuisé ; inhomogène : la régularité ne sélectionne pas). RÉSIDU à inventer/hors de portée : une condition de régularité EXOTIQUE forçant Einstein-3D — bornée par FW-3 (≥ postulat indépendant). SANS SURCLASSEMENT (§6.4) : trancher D1c3-2 NE RÉDUIT RIEN — D1 reste OUVERT, le verrou est CARACTÉRISÉ (pas de sélecteur interne), pas clos ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; A4 non réduit ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "verdict de cadrage — DÉLIMITATION (secteur inhomogène, AVEC sceau verif_D1c3_regularite.py). Tranche la cible D1c3-2 du cadrage LC-WORK-CADRAGE-D1C3-INHOMOGENE sur le testbed Bianchi A : la régularité du crossover ne force pas â_ij Einstein-3D. Répond au point dynamique résiduel §4 de LC-D3-CROSSOVER-ANISOTROPE. Cartographie d'obstruction NÉGATIVE et falsifiable. Gel SHA in-fichier recouvrable (R-36)."
statut: "verdict actif — VERROU-D1 secteur inhomogène = D1c3-c (issue faible DÉFINITIVE pour la régularité naturelle). La régularité (Friedrich/Tod lisse ; Cotton→0) NE force PAS â Einstein-3D ⟹ σ̌≠0 ⟹ D3-régularité ne sélectionne pas la prescription ; A3 socle indépendant ; D1 non fermé par cette voie. Sceau verif_D1c3_regularite.py EXIT 0. Avec D1c-2 (FLRW, Δ1-b) : le verrou D1 n'a PAS de sélecteur de prescription INTERNE. Résidu (régularité exotique) borné par FW-3 (≥ postulat indépendant). SANS SURCLASSEMENT (§6.4) : D1 reste OUVERT (caractérisé, non clos) ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
statut_id: "provisoire — à enregistrer si validé (LC-00-INDEX)"
sceau: "verif_D1c3_regularite.py — EXIT 0 (algèbre exacte sympy). [R1] Milnor 3-Ricci (Bianchi IX) : |σ̌|²=128ε²+O(ε⁴), σ̌≠0 à ε=1/2, lim_{ε→0}=0, S³ ronde Einstein. [R2] Cotton(g=e^{2x}δ₃)≡0 (27 composantes) ∧ Ricci sans-trace=(⅔,−⅓,−⅓)e^{−2x}≠0. Étend verif_D1_bianchiA.py [B2] (répond à sa l.259). Pièces amont : LC-D3-CROSSOVER-ANISOTROPE §4 (point résiduel) ; Friedrich CMP 107 (1986, donnée libre) ; Tod 1309.7248 §7 ; Milnor 1976 ; Cotton/York."
tags: [module-A, module-D3, verdict, cadrage, avec-sceau, verrou-D1, secteur-inhomogene, D1c3-2, delimitation, D1c3-c, issue-faible-definitive, regularite-crossover, extension-conforme-Friedrich, donnee-libre, Tod-1309-7248, crossover-lisse, einstein-3D, Ricci-sans-trace, sigma-check, Tod-eq33, marée, g3, cotton, conforme-platitude, gap-cotton-einstein, contre-exemple-constructif, e2x-delta, bianchi-IX, squash, Milnor, WCH-etendue, A3, A4-WCH, A3-de-A4, postulat-independant, firewall-FW-3, weyl-4D-coeur, geometrie-de-bord, secteur-symetrique-epuise, pas-de-selecteur-interne, residu-exotique, borne-FW-3, IRREDUCTIBILITE-MOYENS, convergence, falsifiable-negatif, R-36, §6.4, non-surclassement, A4, A2star, N]
prerequis_kb: [LC-WORK-CADRAGE-D1C3-INHOMOGENE, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-D-D1-VERROU-FLRW, LC-WORK-CADRAGE-D1-VERROU-STABILITE-A4, LC-D3-CROSSOVER-MATCHING, LC-A-D1-FACTEUR-CONFORME, LC-D-IRREDUCTIBILITE-MOYENS]
renvois: [LC-WORK-CADRAGE-D1C3-INHOMOGENE, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-D-D1-VERROU-FLRW, LC-A-D1-FACTEUR-CONFORME, LC-D-IRREDUCTIBILITE-MOYENS, LC-00-INDEX, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, délimitation, cartographie d'obstruction, falsifiable / négatif, décision ouverte, à inventer, hors de portée]
version: 0.1
langue: fr
date: 2026-06-28
fichier_compagnon: verif_D1c3_regularite.py
maj: "2026-06-28 — v0.1 : GRAVURE du verdict de cadrage pour la cible D1c3-2 (cadrage LC-WORK-CADRAGE-D1C3-INHOMOGENE, gel 6d3baa6f…f44e433), sur GO Thierry, Phase B-1. Répond au POINT DYNAMIQUE RÉSIDUEL du §4 de LC-D3-CROSSOVER-ANISOTROPE (« prochain calcul annoncé », jamais fait) : la régularité du crossover force-t-elle â_ij Einstein-3D ? SCEAU NEUF : verif_D1c3_regularite.py (EXIT 0), qui ÉTEND verif_D1_bianchiA.py [B2] et répond à sa l.259. D1c3-1 (définition, hors-algèbre) : la « condition de régularité » testée = (a) lissité de l'extension conforme de Friedrich de â à travers 𝒞 (donnée de bord libre, Friedrich 1986) ; (b) le candidat « extended-WCH » le plus fort = Cotton→0 (conforme-platitude, analogue 3D du Weyl-4D→0) ; cible = « â Einstein-3D ⟺ Ricci sans-trace=0 ⟺ σ̌=0 ». D1c3-2 (portante Bianchi A) : [R1] régularité-Friedrich/Tod ⊉ Einstein-3D — contre-exemple CONSTRUCTIF : â squashé admet un crossover de Tod LISSE (1309.7248 §7) avec σ̌≠0 (|σ̌|²=128ε²+O(ε⁴), re-dérivé via Milnor) ; [R2] Cotton→0 ⊉ Einstein-3D — g=e^{2x}δ₃ a Cotton≡0 (calculé, 27 comp.) MAIS Ricci sans-trace=(⅔,−⅓,−⅓)e^{−2x}≠0. VERDICT = D1c3-c : aucune condition de régularité NATURELLE/dérivable ne force â Einstein-3D ; la seule qui le ferait est ≥ postuler la courbure constante = POSTULAT INDÉPENDANT non dérivable de A4 (FW-3 : la WCH supprime le Weyl 4D de cœur, pas la 3-géométrie de bord ni son Cotton) ⟹ A3 socle indépendant, issue faible de ANISOTROPE rendue DÉFINITIVE (pour la régularité naturelle), D3-régularité ne sélectionne pas la prescription, marée = donnée libre, D1 non fermé par cette voie. Avec le verdict FLRW (LC-D-D1-VERROU-FLRW, Δ1-b), BILAN : le verrou D1 n'a PAS de sélecteur de prescription INTERNE (secteur symétrique épuisé ; secteur inhomogène : la régularité ne sélectionne pas). CONVERGE avec LC-D-IRREDUCTIBILITE-MOYENS. RÉSIDU à inventer / hors de portée : une condition de régularité EXOTIQUE forçant Einstein-3D — BORNÉE par FW-3 (≥ postulat indépendant). Note de discipline (§6.4) : ce `établi` valide L'ALGÈBRE (Cotton/Ricci exacts ; contre-exemples explicites), JAMAIS une conclusion physique. Fichier neuf (additif, .md +1, id +1 ; +1 .py compagnon verif_D1c3_regularite.py). Gel SHA in-fichier recouvrable (R-36) = sha256 du présent fichier (consigné hors-fichier au dépôt). SANS SURCLASSEMENT (§6.4) : trancher D1c3-2 NE RÉDUIT RIEN — D1 reste OUVERT (verrou CARACTÉRISÉ : pas de sélecteur interne, ni symétrique ni inhomogène-par-régularité ; non clos) ; ne fixe pas N ; ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ; CCC non démontrée NI réfutée. (cf. LC-WORK-CADRAGE-D1C3-INHOMOGENE 6d3baa6f…, LC-D3-CROSSOVER-ANISOTROPE §4, LC-A-D1-BIANCHI, LC-D-D1-VERROU-FLRW, LC-A-D1-FACTEUR-CONFORME §5, LC-D-IRREDUCTIBILITE-MOYENS, Friedrich 1986, Tod 1309.7248 §7, Milnor 1976)"
---

# Verdict de cadrage — VERROU-D1, secteur INHOMOGÈNE (`D1c3-2`) : la régularité ne force PAS `â_ij` Einstein-3D

> **AVEC sceau** (`verif_D1c3_regularite.py`, **EXIT 0**). Répond au **point dynamique résiduel** du §4 de
> `LC-D3-CROSSOVER-ANISOTROPE` (« prochain calcul annoncé », jamais fait) et **étend** `verif_D1_bianchiA.py`
> [B2] (sa l.259). Cartographie d'obstruction **négative, falsifiable**. Gel SHA in-fichier **recouvrable** (R-36).

## 0. La question (`D1c3-1` + `D1c3-2`)

`σ̌ = −4·(Ricci sans-trace de â)` [Tod éq.33] ⟹ **`σ̌=0 ⟺ â Einstein-3D`** (en dim 3 : Ricci sans-trace nul
⟺ courbure constante ⟺ isotropie). **`D1c3-1` (définition)** : la « condition de régularité » testée =
**(a)** lissité de l'extension conforme de **Friedrich** de `â` à travers `𝒞` (donnée de bord **libre**,
Friedrich 1986) ; **(b)** le candidat « **extended-WCH** » le plus fort = **Cotton→0** (conforme-platitude,
analogue 3D du Weyl-4D→0). **`D1c3-2`** : l'une ou l'autre force-t-elle `â` Einstein-3D ?

## 1. Le sceau `[établi — verif_D1c3_regularite.py EXIT 0]`

| # | test | résultat |
|---|---|---|
| **R1** | régularité-Friedrich/Tod ⟹ Einstein-3D ? | **NON** — contre-exemple **constructif** : `â` squashé admet un crossover de **Tod LISSE** (1309.7248 §7) avec `σ̌≠0` ; `|σ̌|²=128ε²+O(ε⁴)`, `σ̌≠0` hors isotropie, raccord continu à 0. Donnée conforme de bord **libre** (Friedrich 1986) |
| **R2** | « Cotton→0 » ⟹ Einstein-3D ? | **NON** — `g=e^{2x}δ₃` : **Cotton≡0** (conforme-plat, 27 comp. calculées) **mais** Ricci sans-trace `=(⅔,−⅓,−⅓)e^{−2x} ≠ 0` ⟹ **PAS** Einstein-3D, `σ̌≠0` |

⟹ La conforme-platitude (Cotton=0) est **strictement plus faible** que Einstein-3D (Ricci sans-trace=0).

## 2. Verdict = `D1c3-c` (postulat indépendant)

- **Aucune condition de régularité NATURELLE/dérivable** (Friedrich lisse ; Cotton→0) **ne force** `â`
  Einstein-3D. La seule qui le ferait (Ricci sans-trace=0 imposé) est **≥ postuler la courbure constante**
  = un **POSTULAT INDÉPENDANT**, **non dérivable de A4** (**FW-3** : la WCH supprime le **Weyl 4D de cœur**,
  elle ne contraint **pas** la **3-géométrie de bord** ni son Cotton).
- ⟹ **A3** (isotropie de l'état / de `â`) reste socle **irréductiblement indépendant** ; l'**issue faible**
  de `LC-D3-CROSSOVER-ANISOTROPE` est rendue **DÉFINITIVE** (pour la régularité naturelle) ; **D3-régularité
  ne sélectionne pas** la prescription ; la marée `g₃` est **donnée libre** ⟹ **D1 non fermé** par cette voie.
- **Résidu** `[à inventer / hors de portée]` : une condition de régularité **exotique** forçant Einstein-3D
  — **bornée par FW-3** (≥ postulat indépendant).

## 3. Conséquence — bilan du verrou D1

- Avec le verdict **FLRW** (`LC-D-D1-VERROU-FLRW`, **Δ1-b**) et le présent (**inhomogène**, **D1c3-c**) :
  le verrou D1 **n'admet PAS de sélecteur de prescription INTERNE** — secteur symétrique **épuisé** ;
  secteur inhomogène : la régularité **ne sélectionne pas**.
- **Converge** avec `LC-D-IRREDUCTIBILITE-MOYENS` : les routes **internes** de fermeture de D1 sont
  **caractérisées comme épuisées** ; seul un **intrant externe** (un principe de sélection neuf, ou un
  postulat assumé) pourrait bouger le verdict.

## 4. Sans surclassement (`§6.4`) et périmètre

- Trancher `D1c3-2` **ne réduit rien** : **D1 reste OUVERT** — le verrou est désormais **caractérisé**
  (pas de sélecteur interne, ni symétrique ni inhomogène-par-régularité), **non clos** ; ne fixe pas `N` ;
  ne réduit pas `A4`.
- Ce `établi` valide **l'ALGÈBRE** (Cotton/Ricci exacts ; contre-exemples explicites), **jamais** une
  conclusion physique.
- **`{A4 ; A2★ ; N}` INCHANGÉ** ; `N` non fixé (`≡ Λ`) ; `A4` non réduit ; `A2★` non tranché ;
  **CCC non démontrée NI réfutée**.

*(cf. `LC-WORK-CADRAGE-D1C3-INHOMOGENE` `6d3baa6f…`, `LC-D3-CROSSOVER-ANISOTROPE` §4, `LC-A-D1-BIANCHI`,
`LC-D-D1-VERROU-FLRW`, `LC-A-D1-FACTEUR-CONFORME` §5, `LC-D-IRREDUCTIBILITE-MOYENS`, Friedrich 1986,
Tod `1309.7248` §7, Milnor 1976)*
