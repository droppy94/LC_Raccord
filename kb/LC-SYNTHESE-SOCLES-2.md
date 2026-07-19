---
id: LC-SYNTHESE-SOCLES-2
titre: "SYNTHÈSE PROGRAMME-WIDE, SECONDE ÉDITION / recompte des socles après les QUATORZE mouvements postérieurs à LC-SYNTHESE-SOCLES v1.0 (cinq blocs : invariance rangs 1-2-3 ; non-gaussien léger+lourd ; conventions/C_T ; c_B ; N≡Λ). Calquée sur la première édition (paper-first, AUCUN sceau neuf, AUCUNE algèbre neuve). Fige : (I) le squelette actualisé ; (II) le RECOMPTE avant→après — RÉSULTAT CENTRAL : ZÉRO réduction de comptage nouvelle, le périmètre {A4 ; A2★ ; N} est VÉRIFIÉ INCHANGÉ sur les quatorze mouvements ; le gain est en NIVEAU DE PREUVE (élévations par invariance, rangs 1-2-3), en EXTENSION (le trois-point pendu à N seul sous Einstein), en CONSOLIDATION (γ, κ, N_action, signe/réalité de C_T, c_B) et en ROBUSTESSE (trois cycles d'audit à froid 4/4 ACQUIS, registre R-1→R-16) ; (III) le tableau GRADE actualisé avec relèvements explicites ; (IV) la traçabilité ISO 19011 — 23 sceaux RÉ-EXÉCUTÉS ce jour, tous EXIT 0 ; (V) RoB 2 + PRISMA, enrichis du pilier audits-à-froid ; (VI) socles irréductibles, dettes SOLDÉES (R-2, R-4, R-11, exigence §5-léger, résidu p.6) et résidus TOUJOURS ouverts ; (VII) ce que le programme AFFIRME vs ne PROUVE PAS. Discipline §6.4 de bout en bout : un `établi (algèbre)` n'est JAMAIS « la CCC est établie ». D1 NON clos ; N NON fixé ; la circularité LC-E NON brisée ; (A) physique conditionnel au seul A2★ INCHANGÉ ; la CCC n'est PAS démontrée."
codename: LC-RACCORD
type: "note de synthèse / verdict — livrable du choix de front de LC-WORK-REPRISE-POST-AUDIT-NONGAUSS-LOURD §3 (option 1, tranchée par Thierry 2026-06-12). Subordonnée à LC-AUDIT-VERDICT §6.4 et §9. Seconde édition du recompte programme-wide ; la première édition LC-SYNTHESE-SOCLES v1.0 reste GELÉE (snapshot du palier 2026-06-09), référencée comme état « avant »."
version: 1.0
langue: fr
date: 2026-06-12
maj: "2026-06-12 — v1.0 : seconde édition. Cadrage paper-first validé en conversation (S-SYN-1a nouveau fichier ; S-SYN-2a quatorze mouvements ; S-SYN-3b rejeu = 5 sceaux de la 1ʳᵉ édition + 16 du delta + les 2 lourds rejoués au §0 d'ouverture, total 23, tous EXIT 0 ; S-SYN-4a pas d'audit à froid de la synthèse, réversible ; S-SYN-5a propagation minimale carte + bullet §8bis). Ne refait NI l'algèbre NI les sceaux (référencés par id). Aucun fetch. Discipline §6.4 : recompte = cartographie honnête, NON démonstration."
portee: "Consigne, en un seul document, l'état FIGÉ du programme après la clôture du cycle lourd (scellement + audit 4/4 + propagation v1.42/v1.40/v1.32/v1.15/v1.21) : (I) squelette ; (II) recompte avant(=v1.0 du 2026-06-09)→après, par blocs, avec la nature du gain (élévation de grade / extension / consolidation / solde de dette — JAMAIS réduction de comptage nouvelle) ; (III) GRADE par maillon avec relèvements ; (IV) traçabilité ISO 19011 (23 rejeux ce jour) ; (V) RoB 2 / PRISMA + pilier audits ; (VI) périmètre {A4 ; A2★ ; N} vérifié inchangé, dettes soldées, résidus ouverts ; (VII) affirme / ne prouve pas."
prerequis_kb: [LC-SYNTHESE-SOCLES, LC-AUDIT-VERDICT, LC-D-NONLIN-VERROU, LC-D-CT-REALITE, LC-D-CT-DUAL, LC-D-CT-DUAL-DS, LC-E-N-CROSSCHECK, LC-AUDIT-LOG-NACTION-AVEUGLE, LC-AUDIT-LOG-NACTION-ALPHA, LC-D-CT-GAMMA, LC-WORK-REPRISE-CONSTRUCTIF-R1, LC-D-NONGAUSS-TTT, LC-AUDIT-LOG-NONGAUSS, LC-D-NONLIN-2PT, LC-AUDIT-LOG-NONLIN-2PT, LC-D-CB-WEYL-MAGNETIQUE, LC-D-NONGAUSS-TTT-LOURD, LC-AUDIT-LOG-NONGAUSS-LOURD, LC-D3-SPECTRE-K3, LC-D-CT-ATN, LC-E-PLANCK-RESIDUEL, LC-00-INDEX, 03_glossaire, 04_references]
fichiers_compagnons_kb: [verif_D_CT_ATN.py, verif_A3_D1_passerelle.py, verif_D3_spectre_k3.py, verif_E_planck.py, verif_D3_C7b_A2_reduction.py, verif_nonlin_cotton.py, verif_nonlin_repr.py, verif_nonlin_parity.py, verif_D_CT_realite.py, verif_D_CT_dual.py, verif_D_CT_dual_dS.py, verif_D_CT_gardefou_dS.py, verif_E_N_crosscheck.py, verif_naction_aveugle.py, verif_naction_firewall.py, verif_naction_alpha.py, verif_naction_gamma_dHSS.py, verif_D_CT_constructif.py, verif_D_nongauss_TTT.py, verif_nonlin_deuxpoint.py, verif_cb_weyl_magnetique.py, verif_D_nongauss_TTT_lourd.py, verif_D_nongauss_TTT_lourd_phase1.py]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# Synthèse programme-wide — seconde édition (recompte après quatorze mouvements)

> **Nature de ce document.** Une **cartographie honnête** du programme entier au 2026-06-12,
> pas une démonstration. La première édition (`LC-SYNTHESE-SOCLES` v1.0, gelée) avait figé le
> palier du 2026-06-09 : trois réductions de comptage consécutives, convergence du secteur
> gaussien/holographique sur le seul compte `N`. Cette seconde édition fige le palier suivant,
> après **quatorze mouvements** (carte `00_index` v1.29→v1.42) regroupés en **cinq blocs**, et
> répond à la question d'audit centrale : **le périmètre `{A4 ; A2★ ; N}` a-t-il bougé ?
> Réponse vérifiée : NON, inchangé partout.** Méthode : `LC-AUDIT-VERDICT §9` (ISO 19011 /
> GRADE / RoB 2 / PRISMA), posture adverse-bienveillante. Règle d'or tenue : **aucun
> `établi (algèbre)` n'est vendu comme `établi` de physique** (§6.4).

---

## 0. Verdict en une ligne `[à figer]`

Depuis la première édition, le programme n'a opéré **aucune réduction de comptage nouvelle** :
le périmètre irréductible reste **`{ A4 (socle posé) ; A2★ (résidu unique de (A), décision
ouverte) ; N (le seul compte libre) }`** — et c'est précisément ce que les quatorze mouvements
**vérifient un à un**. Le gain de la période est d'une autre nature, en quatre volets :
**(1) élévation de grade** — le verrouillage du secteur de Weyl passe de `établi perturbatif TT`
à **`établi par invariance`** aux rangs 1 (un-point, exact tous ordres, deux parités), 2 (forme
`k³·Π^TT` forcée par représentation) et 3 (deux classes S₃×P, graduation 2/6 ≡ Einstein/`W³`) ;
**(2) extension** — le **trois-point** `⟨γγγ⟩_R=[⟨γγ⟩]²·O(1)` est pendu à `N` **seul** sous
Einstein (amplitude `64π⁴/N²`, zéro paramètre libre neuf), passages léger ET lourd audités ;
**(3) consolidation** — les conventions sont épinglées et dérivées (map `γ=4` canonique forcée,
dictionnaire `κ=24/π²`, `N_action=γ/4`, `c_B=1/H` dérivé, signe/réalité de `C_T` à source
unique, report d'erreur nul sur `𝒫`) ; **(4) robustesse** — **trois cycles d'audit à froid
incognito, 4 passes chacun, 12/12 CONFIRMATION, zéro rétro-ajustement**, registre permanent
R-1→R-16. S'y ajoute **un acquis falsifiable négatif** : le deux-point de vide inter-éon n'est
**pas** le spectre CMB (`A_T=16/S_dS≈5·10⁻¹²² ≪ 10⁻¹⁰`), et la consolidation « fixer `N` ≡
fixer `Λ` » (problème de la constante cosmologique, `hors de portée`). **D1 n'est pas clos ;
`N` n'est pas fixé ; la circularité `LC-E` n'est pas brisée ; (A) physique reste conditionnel
au seul A2★ — INCHANGÉ ; la CCC n'est pas démontrée.**

---

## 1. Squelette actualisé `[les deux édifices, inchangés — le secteur D enrichi]`

Les **deux édifices** de la première édition (§6.5) sont inchangés ; tout le mouvement de la
période vit dans l'édifice I, module [D]/[E] :

```
ÉDIFICE I — arc CCC / holographie
   [A] survie conforme ──> D1 (facteur conforme) ── front (a) : (A) `formalisable`, cond. SEUL A2★  [INTACT]
        │
        └─ module [D]/[D3]/[E] : g₃=⟨T⟩ ; ⟨g₃g₃⟩∝k³ ; N=S_dS ; A_T·N=16 ; C_T∝N   [état v1.0, gelé]
              │
              ▼  ===== LES CINQ BLOCS DE LA PÉRIODE (v1.29→v1.42) =====
   (B1) INVARIANCE r1/r2/r3 : un-point=0 EXACT tous ordres, 2 parités (NONLIN-VERROU) ;
        forme 2-pt k³·Π^TT FORCÉE, dim paire=1, impair=contact (NONLIN-2PT, AUDIT 4/4) ;
        rang 3 : 2 classes S₃×P, graduation 2/6 ≡ Einstein/W³ (LOURD PL-D).     [élévation de grade]
   (B2) NON-GAUSSIEN : ⟨γγγ⟩_R=[⟨γγ⟩]²·O(1) sous Einstein ; 64π⁴/N² ; n_libre=1 (W³)
        — passage léger (AUDIT 4/4) + passage lourd telle-qu'imprimée (AUDIT 4/4). [extension : N porte le 3-pt]
   (B3) CONVENTIONS/C_T : κ=24/π² (dictionnaire, aveugle) ; γ=4 canonique FORCÉ, γ=1 nu,
        N_action=γ/4 ; magnitude β=M_Pl²/4 ⊥ map ; d=3 RÉEL NÉGATIF, report d'erreur NUL ;
        dual S1/S2 : C̃_T=+C_T, source UNIQUE du signe ; re-lecture R1 (facteur 4 = map γ). [consolidation]
   (B4) c_B=1/H DÉRIVÉ (jamais posé) ; couple 𝓔=(3/2H)g₃ | 𝓑=(1/H)C[g₀] ; équipartition
        exacte en unités programme ⟹ R-11 levé PAR DÉRIVATION ; dichotomie état/géométrie. [consolidation]
   (B5) N≡Λ : aucun cross-check indépendant (tout est f(N) par scellement) ; fixer N ≡ fixer Λ ;
        acquis falsifiable NÉGATIF : vide inter-éon ≠ CMB (écart ~10¹¹¹).        [consolidation + négatif]
              ▼
   ⟹ {A4 ; A2★ ; N} VÉRIFIÉ INCHANGÉ sur les quatorze mouvements. Rien n'entre, rien ne sort.

ÉDIFICE II — arc φ « sérialité » : NON touché par la période ; pont φ↔CCC ASPIRATIONNEL (§6.5).
```

**Lecture.** La première édition montrait le périmètre qui **se resserre** (plusieurs inconnues
→ une). Cette édition montre le périmètre qui **tient** : sous trois audits adverses et sept
sceaux nouveaux, rien n'a dû y être réintroduit, et rien n'en est sorti. C'est un résultat de
**stabilité du recompte**, pas de fermeture.

---

## 2. Le recompte `[avant → après — la nature exacte du gain]`

**« Avant »** = l'état figé de la première édition (2026-06-09) : secteur gaussien convergé sur
`N` ; `A_T=16/N` ; `C_T/N=1/(32π²)` ; `ℓ_P=√(3π/ΛN)` ; cutoff `√(N/π)` ; verrouillage
**perturbatif TT** ; non-gaussien `décision ouverte` non travaillée.

| Bloc | Avant (état v1.0) | Après (v1.42) | Nature du gain |
|---|---|---|---|
| **B1 — invariance** | `A4⟹A3-un-pt` `établi (sceau)` **perturbatif** ; forme `k³` `établi (sceau)` mode TT ; généralisation non-linéaire `décision ouverte` | rang 1 : un-point nul **exact, tous ordres, 2 parités** ; rang 2 : forme **forcée par représentation** (secteur Weyl complet) ; rang 3 : graduation 2/6 recoupe Einstein/`W³` ; front « rang-3 par invariance » **ABSORBÉ** | **élévation de grade** (perturbatif → par invariance) — pas de réduction de comptage |
| **B2 — non-gaussien** | `>2-pt` `décision ouverte`, non travaillé | `⟨γγγ⟩_R` pendu à `N` seul sous Einstein (`64π⁴/N²`, slack nul `π⁴/4`) ; `n_libre=1` = coefficient `W³~(LH)⁴` ; léger + lourd (telle-qu'imprimée) audités 4/4 ×2 | **extension du domaine de `N`** (le 3-pt s'y rabat) — la liberté `W³` reste `décision ouverte` |
| **B3 — conventions/C_T** | `C_T` réalité `à inventer` ; signe via continuation seule ; facteur 4 de R1 `décision ouverte` ; normalisation OP non raccordée | `d=3` **réel négatif**, report d'erreur **nul** sur `𝒫` ; dual S1/S2 : **source unique** du signe (pas de 2ᵉ route) ; `κ=24/π²` dictionnaire dérivé à l'aveugle ; `γ=4` forcé (Brown-York ×2), `N_action=γ/4` étiquette ; facteur 4 de R1 **= la map γ** ([C] lu convergence) ; magnitude `β=M_Pl²/4` **disjointe** de la map | **consolidation** (rien ne sort du compte ; la chaîne `C_T` est blindée convention par convention). Inclut **une auto-correction tracée** : surclassement v1.35 **rétracté** v1.36 (§AF) puis résolu proprement par γ — la discipline §6.4 a mordu |
| **B4 — c_B** | équipartition vraie « en unités de dualité » (scoping R-11 attaché) | `c_B=1/H` **dérivé** de la définition du Weyl rescalé ; équipartition exacte **aussi en unités programme** ; **R-11 levé par dérivation** ; promesse C2pt-4 fermée | **consolidation + solde de dette** (0 entrée libre < 2 sorties) |
| **B5 — N** | « qu'est-ce qui fixe `N` ? » `hors de portée` sans principe neuf | **aucun cross-check indépendant possible** : `{N, A_T, C_T, cutoff, Λ}` = 1 seul intrant libre à `ℓ_P` fixe ⟹ fixer `N` **≡** fixer `Λ` ; acquis **falsifiable négatif** : `A_T=16/S_dS≈5·10⁻¹²² ≪ A_T^obs≲10⁻¹⁰` ⟹ le 2-pt de vide inter-éon **n'est pas** le spectre CMB | **consolidation de la circularité** (plus chargée, plus chiffrée) + **un négatif net** qui ferme un pont empirique naïf |

**Dettes SOLDÉES par la période** (ce sont des soldes, pas des réductions) : **R-2** (map
`⟨TT⟩∝F`, close route α) ; **R-4** (`ε·ε*=4` exhibé verbatim MP p.6) ; **R-11** (c_B dérivé) ;
**exigence §5 du log léger** (PL-A tenue telle qu'écrite, P1'-A plus « dS-native seulement ») ;
**résidu p.6 du manifeste léger** (levé). Le registre R-1→R-16 est intégralement adjugé
(errata R-1/R-9 consignés, chaînons non réécrits ; règles permanentes au §5).

**Mouvement net.** Zéro inconnue retirée, zéro inconnue ajoutée. La formule de la première
édition reste mot pour mot :

$$\boxed{\;\text{« qu'est-ce qui fixe } N \text{ ? » fixerait } \ell_P,\ A_T=16/N,\ \text{le cutoff }\sqrt{N/\pi},\ C_T\ \text{— ET désormais l'amplitude du trois-point } 64\pi^4/N^2.\;}$$

avec un terme de plus à droite, et l'équivalence nouvelle : **cette question est le problème
de la constante cosmologique** (`N≡Λ`, `hors de portée` sans principe neuf).

---

## 3. Tableau GRADE actualisé `[niveau de preuve par maillon — relèvements explicites]`

*Mêmes conventions que la première édition. Les lignes marquées **↑** sont des relèvements de
grade depuis v1.0 ; **+** des maillons nouveaux ; **=** inchangés (rappelés pour le périmètre).*

| Maillon | Résultat | Niveau de preuve | Déclassement | Conditionnalité |
|---|---|---|---|---|
| **↑ verrou un-point (r1)** | un-point du Weyl **complet** (E⊕B) nul **exactement, tous ordres, 2 parités** sous A3 | **`établi` (au un-point)** — triptyque `verif_nonlin_{cotton,repr,parity}` 12+14+5 | spécifique `d=3` | conditionnel à A3 ; A3/A4 **non fusionnés** (le 2-pt `k³` reste l'écart irréductible) |
| **↑ verrou deux-point (r2)** | forme `k³·Π^TT` **forcée par invariance** (dim paire=1 ; impair=contact) ; « résidu gaussien de D1 = `A_T` » relevé | **`établi par invariance`** (`verif_nonlin_deuxpoint` 41 ; **AUDIT 4/4 ACQUIS**, 3 routes indépendantes) | indirectness (entrées amont scellées) | conditionnel à A3, relation BD, `C_T∝N`, `γ=n²` ; le `k³` **reste la donnée de Cauchy** pendue à `N` |
| **+ trois-point (léger+lourd, r3)** | `⟨γγγ⟩_R=[⟨γγ⟩]²·O(1)` sous Einstein ; `(H/M_Pl)⁴/A_T²=π⁴/4` **exact** ; amplitude `64π⁴/N²` ; rang 3 gradué 2/6 ≡ Einstein/`W³` ; PL-A..PL-D **telles qu'écrites** | **`établi (algèbre)`** (sceaux 28 et 34=15+19 asserts ; **DEUX AUDITS 4/4 ACQUIS**) | indirectness (niveau arbre ; ordre dominant) | conditionnel aux scellés amont **et à Einstein** ; liberté unique = coefficient `W³~(LH)⁴` `décision ouverte` ; 4-pt/boucles **hors périmètre** (S1) |
| **+ c_B** | `𝓑=(1/H)·C[g₀]`, `c_B=1/H` **dérivé**, signe compris ; équipartition exacte en unités programme ; R-11 levé | **`établi (algèbre)`** (`verif_cb_weyl_magnetique` 26) | perturbatif TT BD ; `d=3` | conditionnel à BD ; consolidation, **pas** de réduction |
| **+ map γ / dictionnaire κ / N_action** | `γ_canon=4` **forcé** (T Brown-York ×2) ; `γ=1` conventionnel (nu) ; `N_action=γ/4` ; `κ=24/π²` dérivé **à l'aveugle** (étalon scalaire externe) ; magnitude `β=M_Pl²/4` **disjointe** (forcée par `𝒫`) ; facteur 4 de R1 = la map | **`établi (algèbre)`** (`gamma_dHSS` 18 ; `aveugle` 17 + `firewall` 23 ; `alpha` 23, flag ERRATUM v1.1 ; `constructif` flag TRANCHÉ v1.1, [C]=convergence en convention nue) | — | conditionnel aux prescriptions exhibées (éq. 63 ; `Σεε=Π` ; `|Im F|` ancré sur `𝒫`) ; consolidations |
| **+ réalité/signe de `C_T`** | `d=3` **réel négatif** (`i^{d-1}`, c0-indépendant) ; **report d'erreur NUL** sur `𝒫` ; dual S1/S2 : `C̃_T=+C_T`, **source unique** du signe | **`établi (algèbre)`** (`realite` 20 ; `dual` 18 ; `dual_dS` 13 + `gardefou_dS` 14) | dS/CFT **non-unitaire** isolée | la **validité physique** de `C_T<0` se rabat sur « CFT de raccordement » `décision ouverte` ; **pas** de 2ᵉ route au signe |
| **+ N≡Λ** | aucun cross-check indépendant ; fixer `N` ≡ fixer `Λ` ; **négatif** : vide inter-éon ≠ CMB (écart ~10¹¹¹) | **`établi (algèbre)`** (`E_N_crosscheck` 19) — consolidation + acquis négatif | — | le falsifiable **positif** (coefficients 16 ; 1/(32π²)) exigerait un accès indépendant à `A_T/C_T` vs `N` |
| **= forme `⟨g₃g₃⟩∝k³`** | `Δ=d=3` ; variance LOG au cutoff `√(N/π)` | `établi (sceau)` — désormais **adossé au rang 2** | mode TT, dS₄ | `A_T≪1` |
| **= R1/R2/R3 (1ʳᵉ édition)** | `{A3,A4}→{A4}` au un-pt ; résidu gaussien = `A_T` ; `A_T·N=16` ; `C_T/N=1/(32π²)` | inchangés ; sceaux **re-rejoués ce jour** | (cf. 1ʳᵉ édition) | (cf. 1ʳᵉ édition) |
| **= N = S_dS** | compte holographique (≈`3,28·10¹²²`) | `établi (algèbre)` ; fixation `décision ouverte` — **désormais ≡ Λ** | — | `hors de portée` sans principe neuf |
| **= A4 (WCH)** | socle ; porte (ii) close | **socle posé** | — | dériver A4 `à inventer` |
| **= A2★** | non-cascade | **`à inventer` / `décision ouverte`** — **INTOUCHÉ par les 14 mouvements** | — | seul résidu de (A) ; falsifiable |
| **= (A) physique** | isotropisation | **`formalisable`**, cond. au **seul A2★** — **INCHANGÉ** | conditionnalité | A2★ + socles |
| **= arc φ** | math exacte / physique non instanciée | inchangé (§6.3/§6.5) | indirectness | pont **aspirationnel** |

> **Discipline §6.4 (rappel).** « Élévation par invariance » et « audité 4/4 ACQUIS » qualifient
> la **solidité de l'algèbre et de la provenance**, jamais la physique. La somme des cinq blocs
> ne ferme rien : D1 ouvert, `N` non fixé, A2★ non scellé, A3/A4 posés.

---

## 4. ISO 19011 — traçabilité `[23 sceaux ré-exécutés ce jour]`

Rejeu du 2026-06-12 (Python 3.12, sympy 1.14 / numpy 2.4 / scipy 1.17), option S-SYN-3b :
les **5 sceaux de la première édition** + les **16 du delta** + les **2 du cycle lourd**
(rejoués au §0 d'ouverture avec vérification sha256 exacte et byte-identité du segment de
phase 1, 9 704 octets, occurrence unique — consignés ici, non répétés). Les 11 sceaux du front
(a) restent tracés à `LC-D3-FRONT-A-SYNTHESE` (non répétés, front intouché depuis).

| Sceau | Rejeu | Atteste (résumé) |
|---|---|---|
| `verif_D_CT_ATN.py` | **EXIT 0** | `A_T·N=16` ; `C_T/N=1/32π²` (1ʳᵉ éd.) |
| `verif_A3_D1_passerelle.py` | **EXIT 0** (11/11) | `A4⟹A3-un-pt` (1ʳᵉ éd.) |
| `verif_D3_spectre_k3.py` | **EXIT 0** | forme `k³`, variance LOG (1ʳᵉ éd.) |
| `verif_E_planck.py` | **EXIT 0** | `N=S_dS`, `N=π·N_time²` (1ʳᵉ éd.) |
| `verif_D3_C7b_A2_reduction.py` | **EXIT 0** (16/16) | C7-b réduit au seul A2★ (1ʳᵉ éd.) |
| `verif_nonlin_cotton.py` / `_repr.py` / `_parity.py` | **EXIT 0** (12/12 ; 14/14 ; 5/5) | verrou un-point rang 1, deux parités |
| `verif_D_CT_realite.py` | **EXIT 0** (20) | `d=3` réel négatif ; report d'erreur nul |
| `verif_D_CT_dual.py` / `_dual_dS.py` / `_gardefou_dS.py` | **EXIT 0** (18 ; 13/13 ; 14/14) | dualité S1/S2 ; `C̃_T=+C_T` ; firewall |
| `verif_E_N_crosscheck.py` | **EXIT 0** (19/19) | `N≡Λ` ; négatif inter-éon≠CMB |
| `verif_naction_aveugle.py` / `_firewall.py` | **EXIT 0** (17 ; 23) | `κ=24/π²` à l'aveugle ; statut impulsion dérivé |
| `verif_naction_alpha.py` (flag ERRATUM v1.1) | **EXIT 0** (23) | `f_Π=1`, `f_W=4`, `N_action=1/4` (lecture §AF) |
| `verif_naction_gamma_dHSS.py` | **EXIT 0** (18) | `γ=4` forcé ; magnitude ⊥ map |
| `verif_D_CT_constructif.py` (flag TRANCHÉ v1.1) | **EXIT 0** | [B]+[D] passent ; [C] = convergence en convention nue |
| `verif_D_nongauss_TTT.py` | **EXIT 0** (28) — sha `c06f6f51…d6a3bd6` **conforme carte** | 3-pt léger, blocs A–F |
| `verif_nonlin_deuxpoint.py` | **EXIT 0** (41=27+14) — sha `1e40f5e8…eedde` **conforme carte** | verrou rang 2 |
| `verif_cb_weyl_magnetique.py` | **EXIT 0** (26) — sha `e1bef559…344f` **conforme carte** | `c_B=1/H` |
| `verif_D_nongauss_TTT_lourd.py` + `_phase1.py` | **EXIT 0** (34 ; 15) au §0 — sha `2cb93432…46923` / `e494c8c6…294b` **exacts** ; byte-identité 9 704 o. | 3-pt lourd, PL-A..PL-D |

**Constat ISO 19011.** Traçabilité **intègre** : chaque maillon gradué `établi` au §3 correspond
à un sceau qui **passe à la ré-exécution ce jour** — 23/23 EXIT 0, zéro divergence de sha sur
les valeurs consignées en carte. Les deux flags (`ERRATUM v1.1`, `TRANCHÉ v1.1`) sont des
annotations docstring-only attendues (§0.4 de la note de reprise) ; sorties et asserts
strictement inchangés. Exception déclarée héritée de la 1ʳᵉ édition : R2 (D1⟷E) reste
paper-first sans sceau propre (recombinaison) ; aucun `établi` orphelin.

---

## 5. RoB 2 & PRISMA `[stress-test + complétude — le pilier nouveau : les audits à froid]`

**Le fait de robustesse dominant de la période** : trois cycles d'audit à froid incognito
(§4.1 : les instances disqualifiées ne s'auto-auditent pas), quatre passes indépendantes
chacun, **12/12 CONFIRMATION, zéro rétro-ajustement** :

- **NONGAUSS (léger)** — registre R-1→R-8 ; adjudication P1'-A (défaut **procédural** réel ⟹
  règle **R-7** : amendement formel des cibles gelées à toute décision de scoping) ;
- **NONLIN-2PT** — registre R-9→R-14 ; premier audit vérifiant R-7 **mot à mot** (« zéro
  amendement » 4/4) ; re-dérivations par **trois routes indépendantes** ; leçons **R-10**
  (dépôts de phase en fichiers distincts) et **R-14** (inventaire d'ouverture) ;
- **NONGAUSS-LOURD** — premier cycle exerçant **R-7+R-10+R-14 simultanément** + §0bis (PDF en
  trois temps) ; conformité « telle qu'imprimée » **au caractère près**, sha par page ; **≥11
  mutations réelles cassantes** dont chirurgicales (firewall **étagé**) ; règles **R-15**
  (table scan↔imprimé obligatoire) et **R-16(b)** (mutations propres des auditeurs, ≥2).

S'ajoute une **auto-correction documentée** (v1.35→v1.36, §AF) : un surclassement détecté par
audit et **rétracté**, puis le point résolu proprement (γ). Au sens RoB 2, c'est un test
**positif** du dispositif : la discipline ne se contente pas d'exister, elle a mordu.

- **RoB 2 — sceaux** : la quasi-totalité des sceaux nouveaux est **symbolique (sympy)** —
  immunisée aux biais de solveur/troncature. Le risque résiduel reste la **sélection de
  convention**, désormais **explicitement dérivée** maillon par maillon (γ, κ, c_B) plutôt que
  posée : le périmètre de ce risque s'est **réduit**. Les firewalls sont systématiques (5-6
  injections cassantes par sceau ; mutations chirurgicales aux audits).
- **PRISMA** : toutes les sources consommées par la période sont **en KB**
  (`04_references` v1.15 : OP hep-th/9307010 avec (5.5)/(5.6)/(5.12)/(5.13)/(6.42) telles
  qu'écrites SOLDÉES ; MP 1104.2846 v2 avec p.6/(2.6) ; Ward 1603.03771 + 1511.04077 ;
  de Haro 0808.2054) ⟹ **non-édit motivé** (aucune référence neuve requise par cette
  synthèse). La source manquante qui changerait un verdict reste celle d'A2★ (loi de comptage
  générique de spikes), **déclarée manquante par la littérature elle-même** — inchangé.

---

## 6. Socles, dettes soldées & résidus `[le périmètre — vérifié inchangé]`

**Socles irréductibles (posés, NON dérivés)** — inchangés :
- **A4 — WCH (Penrose).** Socle posé ; porte (ii) close ; absorbe le contenu un-point d'A3,
  désormais **exactement, tous ordres** (rang 1).
- **A2★ — non-cascade.** Seul résidu de (A) physique ; `décision ouverte` / `à inventer` ;
  **intouché par les quatorze mouvements** (qui vivent tous au module [D]/[E]).

**Le compte unique (libre)** — inchangé, plus chargé :
- **`N=S_dS`.** Porte `ℓ_P`, `A_T=16/N`, le cutoff `√(N/π)`, `C_T` — **et désormais
  l'amplitude du trois-point `64π⁴/N²`**. Sa fixation **≡ fixer `Λ`** (`E-N-CROSSCHECK`) :
  `hors de portée` sans principe nouveau. Circularité `LC-E` **non brisée**.

**Dettes SOLDÉES par la période** (rappel §2) : R-2 ; R-4 ; R-11 ; exigence §5-léger ;
résidu p.6. Errata R-1/R-9 consignés (chaînons gelés, correctifs en propagation).

**Résidus explicitement ouverts (ne PAS sceller)** — l'état net :
- **amplitude `A_T~1/N`** — **LA** décision ouverte du secteur (le candidat-égalité `A_T=16/N`
  est scellé comme algèbre, sa **réalité physique** pend à la fixation de `N`) ;
- **coefficient `W³~(LH)⁴`** `décision ouverte` (nul sous Einstein pur) — l'unique liberté du
  trois-point ;
- **`(a,b,c)` propres / CFT de raccordement** `décision ouverte` (porte aussi la validité
  physique de `C_T<0`, non-unitarité isolée) — adjugé pré-gel au cycle lourd, ouvert ;
- **quatre-point / boucles / non-perturbatif** hors périmètre (S1) ;
- **survie au crossover** `à inventer` ; **sélection de `Σ`** ;
- **pont φ↔CCC** `aspirationnel` (édifice II non relié) ;
- micro-items catalogués non bloquants (§0.4 de la note de reprise) : patch statut-only du
  chaînon lourd + instruction ; purge interface du doublon `LC-02-PROGRAMME`.

*Note de périmètre :* tous les résidus du secteur D ci-dessus sont **adossés à `N`**, donc à la
circularité `LC-E` — la convergence de la première édition s'est **renforcée**, pas déplacée.

---

## 7. Ce que le programme AFFIRME vs ne PROUVE PAS `[honnêteté]`

**Le programme AFFIRME (avec sceaux ré-exécutés ce jour et trois audits 4/4) :**
- que le verrouillage du secteur de Weyl tient **par invariance** aux rangs 1, 2 et 3
  (un-point exact ; forme du deux-point forcée ; classes du trois-point graduées Einstein/`W³`) ;
- que le **trois-point** se rabat sur `N` seul sous Einstein (`64π⁴/N²`, slack nul), aux
  passages léger et lourd, conformité « telle qu'imprimée » vérifiée au caractère près ;
- que les conventions de la chaîne `C_T` (γ, κ, N_action, c_B, signe, réalité) sont **dérivées
  et épinglées**, avec report d'erreur nul sur l'observable `𝒫` ;
- que le périmètre **`{A4 ; A2★ ; N}` est resté inchangé** sous quatorze mouvements et trois
  audits adverses — et que fixer `N` **est** le problème de la constante cosmologique ;
- un **négatif falsifiable** : le deux-point de vide inter-éon n'est pas le spectre CMB.

**Le programme NE PROUVE PAS :**
- que `N` est **fixé** (circularité intacte, désormais ≡ `Λ`) — donc pas que `A_T`, `C_T`,
  `ℓ_P` ou l'amplitude du 3-pt ont une valeur dérivée ;
- que A3/A4 sont **dérivables** (socles posés) ; que A2★ est **borné** ;
- que `C_T<0` a une **validité physique** en dS (non-unitarité isolée, rabattue sur la CFT de
  raccordement, non levée) ;
- que le coefficient `W³` est nul **autrement que par hypothèse Einstein** ;
- que quoi que ce soit survit au **crossover**, au **quatre-point**, aux **boucles** ;
- donc **pas** « la CCC est vraie ». Les acquis de la période sont des élévations de grade,
  des extensions et des consolidations **de comptage**, conditionnels, à l'ordre dominant.

---

## 8. Verdict figé & suite `[clôture]`

> **Le recompte est stable.** Quatorze mouvements, sept chaînons nouveaux, trois cycles d'audit
> à froid 12/12, vingt-trois sceaux rejoués EXIT 0 : le périmètre irréductible de l'arc CCC est
> **vérifié inchangé** à **`{ A4 ; A2★ ; N }`**, l'inconnue centrale reste **un seul nombre,
> `N`**, dont la fixation est désormais identifiée au **problème de la constante
> cosmologique**. Le verrouillage gaussien est passé **par invariance** (rangs 1-2-3) et le
> trois-point s'est rabattu sur `N`. **D1 non clos ; `N` non fixé ; (A) physique conditionnel
> au seul A2★ — INCHANGÉ ; CCC non démontrée.** C'est une contribution à la **comptabilité de
> la conjecture**, plus robuste qu'à la première édition, pas plus fermée.

**Suites possibles (non tranchées ici — opérateur).** Le menu est **mince** (note de reprise
§3) : **(a)** A2★ — veille bornée (`hors de portée en interne`) ; Σ en dernier recours ;
**(b)** décisions ouvertes du secteur D (`(a,b,c)` propres ; coefficient `W³` ; amplitude
`A_T~1/N`) — toutes adossées à `N` ; **(c)** `N≡Λ` frontal — `hors de portée` sans principe
nouveau ; **(d)** micro-items cosmétiques (statut-only ; purge doublon). Aucun front technique
borné et sceau-able n'est identifié à date dans le périmètre interne : c'est une information de
synthèse en soi.

---

## Appendice — légende des tags épistémiques
`établi` (théorème, ou sceau symbolique/numérique qui passe — **jamais** « la CCC est vraie ») ·
`établi par invariance` (forme forcée par la représentation, conditionnelle aux entrées amont) ·
`formalisable` (programme clair, non exécuté) · `à inventer` (pont conjecturé) · `hors de portée`
(au-delà des moyens actuels) · `décision ouverte` (choix de modélisation reporté/assumé).
*Rappel d'audit : un `établi (algèbre)` = « l'algèbre est correcte + cibles reproduites », jamais
« la physique est établie » tant que `N` n'est pas fixé, A2★ non scellé, et A3/A4 posés.*
