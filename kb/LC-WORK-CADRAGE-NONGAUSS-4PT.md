---
id: LC-WORK-CADRAGE-NONGAUSS-4PT
titre: "CADRAGE (paper-first, R-7) — le QUATRE-POINT ⟨g₃g₃g₃g₃⟩ : dernier ordre ouvert de la jambe AMPLITUDE de D1. Route (B) du pivot FACTEUR-CONFORME. Successeur de LC-D-NONGAUSS-TTT (3-pt scellé : ≥4-pt explicitement HORS-périmètre S1). QUESTION FIGÉE : sous gravité d'Einstein, le 4-point arbre TT reste-t-il PENDU À N (aucun constant indépendant neuf, comme 2-pt et 3-pt), ou un nouveau degré de liberté apparaît-il ? TRICHOTOMIE PRÉ-ENREGISTRÉE B4-a/b/c (avant toute algèbre/fetch). PRÉDICTIONS FIGÉES : scaling connexe ∝(H/M_Pl)⁶=N⁻³ (extrapolation du pattern scellé 2-pt N⁻¹ / 3-pt N⁻²) ; γ₄≡n⁴=16 (Brown-York n=2, À CONFIRMER par dérivation, NON supposé) ; le 4-point libre de g₀ porte une part DÉCONNECTÉE non nulle (Wick) — feature de méthode, distincte du 3-pt où ⟨g₀³⟩=0. ZÉRO CALCUL ICI. SANS SURCLASSEMENT (§6.4) : cadrer ne scelle/réduit rien ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé (≡Λ) ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "cadrage (work-active, paper-first, R-7) — carte de conventions + cibles P-figées + trichotomie pré-enregistrée. NE scelle rien, NE vote pas, AUCUNE algèbre. À GELER (sha consigné au dépôt) AVANT toute exécution."
statut: "cadrage PRÊT À GELER — route (B) ordre ≥4. Objet, trichotomie, prédictions et protocole figés. Aucune algèbre, aucun fetch effectué. Le sceau (verif_D_nongauss_4pt.py, à produire) viendra APRÈS gel + GO."
statut_id: "provisoire — à enregistrer si validé/gelé (LC-00-INDEX)"
version: 0.1
langue: fr
date: 2026-06-28
maj: "2026-06-28 — v0.1 : création du cadrage de la route (B) (ordre ≥4 de l'amplitude), sur GO Thierry après pivot FACTEUR-CONFORME → (B). Reprend le gabarit anti-fit de LC-WORK-CADRAGE-NONGAUSS (3-pt). Cibles P-B1..P-B5 figées SANS fetch ; trichotomie B4-a/b/c pré-enregistrée ; pièces amont gelées par sha (§7). ZÉRO algèbre. §6.4/R-7/R-53 portés. À geler (sha du présent fichier consigné au dépôt) avant Phase 1."
tags: [module-D, module-A, module-E, cadrage, paper-first, R-7, anti-fit, verrou-D1, jambe-amplitude, quatre-point, 4pt, g3, TTTT, gamma4, deconnecte-connexe, scaling-N, einstein, W3, W4, ds-cft, osborn-petkou, comptage-d3, trichotomie-pre-enregistree, B4-a, B4-b, B4-c, hors-perimetre-S1-leve, R-53, §6.4, non-surclassement, A4, A2star, N]
prerequis_kb: [LC-D-NONGAUSS-TTT, LC-D-NONGAUSS-TTT-LOURD, LC-D-D1-VERROU-AMPLITUDE, LC-D-CT-ATN, LC-D-CT-GAMMA, LC-D3-SPECTRE-K3, LC-D-HOLOGRAPHIE-G3, LC-D-NONLIN-2PT, LC-WORK-CADRAGE-NONGAUSS, LC-D-D1-VERROU-DELIMITATION, LC-D-IRREDUCTIBILITE-MOYENS]
renvois: [LC-D-NONGAUSS-TTT, LC-D-D1-VERROU-AMPLITUDE, LC-A-D1-FACTEUR-CONFORME, LC-00-INDEX, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [formalisable, décision ouverte, à inventer, hors de portée]
---

# CADRAGE (R-7) — le quatre-point `⟨g₃g₃g₃g₃⟩` : l'amplitude de D1 reste-t-elle pendue à `N` à l'ordre 4 ?

> **Paper-first, anti-fit (R-7).** Carte de conventions, cibles **figées sans fetch**, trichotomie
> **pré-enregistrée**. **AUCUNE algèbre ici.** À **geler** (sha du présent fichier consigné au dépôt)
> **avant** la Phase 1 du sceau. **§6.4** : cadrer ne scelle/réduit rien.

## 0. Rôle et garde-fou `[discipline §6.4 / R-7]`

La jambe **amplitude** de D1 est cartographiée **`|≤3-pt`** (`LC-D-D1-VERROU-AMPLITUDE`) : 2-pt et 3-pt
**scellés et pendus à `N`** (`A_T·N=16` ; `⟨g₃³⟩` Einstein `=64π⁴/N²`, slack nul). Le **≥4-pt** est
**« ouvert-acknowledgé »** : `N`-lié *par Ward/OPE* mais **non scellé séparément** (`LC-D-NONGAUSS-TTT`
le met explicitement **hors-périmètre S1**). Ce cadrage **ouvre S1 au seul 4-point arbre TT**. Il **ne
ferme pas** le secteur non-gaussien (boucles, non-perturbatif, parité impaire restent hors périmètre),
**ne ferme pas** D1, **ne fixe pas** `N`.

## 1. Objet et question figée `[formalisable]`

- **Objet** : le **quatre-point connexe** `⟨g₃g₃g₃g₃⟩_c` de la marée de Weyl rescalée `g₃` (≡ `⟨T⟩`
  céleste via `LC-D-HOLOGRAPHIE-G3`), au **niveau arbre**, en **perturbatif TT** (même scoping que le
  3-pt, ordre `+1`).
- **Question (figée)** : *sous gravité d'Einstein, le 4-point arbre TT introduit-il un **constant
  indépendant neuf** (non fixé par `N`/`C_T`), ou est-il **entièrement pendu à `N`** comme les ordres
  inférieurs ?*
- **Enjeu réduction** : si pendu à `N` ⟹ la jambe amplitude s'étend au 4-pt (réduction de la liberté de
  D1 prolongée, cœur `{A4 ; A2★ ; N}` inchangé). Si constant neuf ⟹ l'amplitude **n'est pas** entièrement
  absorbée dans `N` à cet ordre (résidu libre authentique — réouverture partielle de la jambe amplitude).

## 2. Trichotomie PRÉ-ENREGISTRÉE (avant toute algèbre/fetch) `[anti-fit]`

| issue | énoncé | conséquence programme |
|---|---|---|
| **B4-a — RATTACHÉ-`N`** | sous Einstein pur, le 4-pt connexe arbre TT est **entièrement pendu à `N`** (amplitude `∝N⁻³`, coefficient `O(1)` apparié ; aucun constant indépendant neuf). Les seules libertés sont des coefficients d'**invariants de Weyl d'ordre supérieur** (`W⁴`, `W²∇²`, …), **nuls sous Einstein pur** — **même conditionnalité que `W³`**. | jambe amplitude prolongée au 4-pt ; **réduction tenue** ; cœur inchangé |
| **B4-b — CONSTANT-NEUF (délimitation)** | même sous Einstein pur, le 4-pt exige **≥1 constant indépendant** non fixé par `N`/`C_T` (p.ex. coefficient OPE de `⟨TTTT⟩` libre par Ward/contraintes conformes `d=3`). | l'amplitude **n'est pas** entièrement absorbée dans `N` au 4-pt ; **liberté neuve** identifiée et nommée |
| **B4-c — HORS-PORTÉE-INTERNE** | le contenu non-gaussien authentique au 4-pt n'est **pas décidable** par les moyens internes (arbre/perturbatif TT) — requiert boucles/non-perturbatif ou un **intrant externe** (comptage CFT `d=3` indisponible sans hypothèse). | **délimitation par hors-portée** (analogue de la jambe sélection) |

**Défaut conservateur déclaré** : l'issue *par défaut* attendue est **B4-a** (cohérence avec le pattern
2-pt/3-pt). L'issue *« excitante »* serait **B4-b** (liberté neuve). La discipline anti-fit exige
d'**écrire la re-dérivation AVANT** de lire tout comparandum, et de **valoriser symétriquement** les trois
issues : un résultat B4-b ou B4-c est **aussi recevable** que B4-a.

## 3. Conventions et PRÉ-DÉCLARATIONS figées (sans fetch) `[anti-fit — à confirmer, non supposé]`

- **P-B1 (zéro/scission).** Le 4-pt **libre** de `g₀` porte une part **déconnectée non nulle** (Wick :
  produits de 2-pts) — *feature structurelle de méthode*, distincte du 3-pt (`⟨g₀³⟩=0`). Le **connexe**
  `⟨g₃⁴⟩_c` est le **seul datum non-gaussien authentique** ; la part déconnectée est fixée par le 2-pt
  scellé (aucun contenu neuf). **À établir en Phase 1.**
- **P-B2 (map `γ₄`).** Par la logique `LC-D-CT-GAMMA` généralisée `γ_k=n^k` : Brown-York `n=2` ⟹
  **prédiction `γ₄=16`**. À **dériver** (non supposée). Le **catalogue d'artefacts de mélange** s'étend
  `{2,4,8,16}` — tout facteur pur de cette liste dans une comparaison = candidat-mélange à neutraliser
  **avant** tout NO-GO (leçon R1 outillée).
- **P-B3 (scaling).** Extrapolation du pattern scellé (`2-pt ∝(H/M_Pl)²=N⁻¹` ; `3-pt ∝(H/M_Pl)⁴=N⁻²`) ⟹
  **prédiction connexe `∝(H/M_Pl)⁶=(8π²/N)³=512π⁶/N³`**. Test : sous Einstein, le 4-pt connexe arbre
  doit porter `N⁻³` avec coefficient `O(1)` apparié ⟹ **aucune entrée libre neuve** (anti-numérologie :
  1 entrée `N` < nombre de sorties appariées). À **confirmer/réfuter**.
- **P-B4 (comptage).** La cible-comparandum est le **nombre de structures tensorielles indépendantes
  parité-paire de `⟨TTTT⟩` en `d=3`** (CFT), et la part **produite par Einstein** (contact quartique +
  échange cubique×cubique) vs le **reste** (`W³`-échange, `W⁴`-contact…). `n_libre(4-pt)` = total − Einstein.
  **Comptage figé comme cible AVANT fetch** ; valeur **non pré-supposée**.
- **P-B5 (diagrammes).** Sous Einstein, le 4-pt connexe arbre = **contact quartique** (expansion de
  l'action d'Einstein à l'ordre 4) **+ échange** (vertex cubique × propagateur graviton × vertex cubique).
  **Aucun** de ces deux n'apporte de constant libre (tout est dans l'action d'Einstein). À **vérifier**.

## 4. Méthode / testbed `[formalisable, borné]`

1. **Phase 1 (écrite + EXIT 0 AVANT tout fetch)** : relation d'état BD `g₃=-(i/3)k³g₀` ; scission
   connexe/déconnecté (P-B1) ; dérivation `γ₄` (P-B2) ; prédiction de scaling `N⁻³` (P-B3) posée comme
   cible. Machinerie **réécrite** (ne pas réutiliser les routines internes d'un sceau existant sans
   re-dérivation).
2. **Fetch aveugle** : comptage `⟨TTTT⟩` `d=3` (comparandum externe — candidats : Osborn-Petkou ;
   littérature `⟨TTTT⟩` CFT 3D / graviton 4-pt dS), **après** Phase 1 gelée.
3. **Phase 3 (comparaison)** : `n_libre`, scission Einstein/`W`-supérieur, test de scaling, slack.
4. **Firewall** : ≥5 injections fausses (sur `γ₄`, l'exposant de `N`, le comptage, le coefficient
   `O(1)`, la scission) doivent **casser** le sceau.

## 5. Protocole anti-fit (R-7) `[obligatoire]`

- **Gel du présent cadrage** : sha256 consigné au dépôt **avant** la Phase 1. Toute décision de scoping
  **post-gel** exige un **amendement daté** (R-7).
- **Cibles P-B1..P-B5 figées** ci-dessus, sans fetch.
- **Trichotomie B4-a/b/c figée** ci-dessus.
- **Phase 1 écrite et EXIT 0 avant fetch** (protection contre le fit au comparandum).
- **Audit à froid** (instance incognito séparée, pilote disqualifié) : re-dériver `γ₄`, le scaling et la
  scission hors contexte, re-fetch le comptage, re-exécuter le sceau, vérifier le mordant du firewall.

## 6. Critères de réfutation (kill) `[falsifiable]`

- **Kill-1 (réduction)** : si l'amplitude Einstein du 4-pt connexe exige une **échelle hors `N`** ⟹ **B4-b**
  (consigné, non masqué).
- **Kill-2 (comptage)** : si `n_libre(4-pt)` > (structures Einstein) **même sous Einstein pur** ⟹ liberté
  neuve ⟹ **B4-b**.
- **Kill-3 (hors-portée)** : si le connexe arbre TT ne **clôt pas** le datum non-gaussien au 4-pt (part
  essentielle en boucles/non-perturbatif) ⟹ **B4-c**.
- **Kill-4 (artefact convention)** : neutralisé d'avance par le catalogue `{2,4,8,16}` et les ratios
  insensibles à `ε·ε*`.

## 7. Pièces amont GELÉES (sha — référence, intactes ce cadrage) `[R-7]`

| pièce | sha256 (16) | rôle |
|---|---|---|
| `verif_D_nongauss_TTT.py` | `c06f6f514076cd03` | sceau 3-pt (parent direct) |
| `LC-D-NONGAUSS-TTT.md` | `6795c6b1bddf7609` | verdict 3-pt (≥4 hors-S1) |
| `verif_D_nongauss_TTT_lourd.py` | `2cb9343235d34d06` | passage lourd 3-pt (κ) |
| `LC-D-NONGAUSS-TTT-LOURD.md` | `9cd5bf91e9c0ad11` | verdict lourd 3-pt |
| `verif_D_CT_ATN.py` | `73bc2e8d7ab43b58` | `A_T·N=16` ; `C_T/N=1/(32π²)` |
| `LC-D-CT-ATN.md` | `aca05092d78420f8` | rattachement amplitude↔`N` |
| `LC-D-CT-GAMMA.md` | `e3f4de56207bece2` | dictionnaire `γ_k=n^k` |
| `LC-D3-SPECTRE-K3.md` | `6f5c1738540d4908` | forme 2-pt `~k³` |
| `LC-D-HOLOGRAPHIE-G3.md` | `759583cb5c6a8eab` | dictionnaire `g₃=⟨T⟩` |
| `LC-D-NONLIN-2PT.md` | `ccbd7229d808734a` | 2-pt non-perturbatif |
| `LC-D-D1-VERROU-AMPLITUDE.md` | `1d4f10a8c38cd152` | jambe amplitude (`|≤3-pt`) |
| `LC-WORK-CADRAGE-NONGAUSS.md` | `22fb1fe7e7d7db55` | gabarit anti-fit (parent) |

## 8. Sans surclassement (`§6.4`), `R-7`, `R-53`

- **Cadrer ne scelle/réduit rien.** Le sceau et le verdict viendront **après** gel + GO.
- Quelle que soit l'issue : **B4-a** prolonge l'absorption dans `N` (réduit la liberté de D1, **pas** le
  cœur) ; **B4-b/c** sont des **délimitations** (aucune réduction). Dans tous les cas
  **`{A4 ; A2★ ; N}` INCHANGÉ** ; `D1` non clos ; `N` non fixé (`≡Λ`) ; `A4` non réduit ; `A2★` non
  tranché ; **CCC non démontrée NI réfutée**.
- **`R-53`** : toute clôture issue de ce cadrage sera **conditionnelle/recouvrable** (un intrant externe
  ou un ordre supérieur la rouvrirait).
