---
id: LC-D-NONGAUSS-TTT
titre: "Module D / front non-gaussien de D1 — le TROIS-POINT ⟨g₃g₃g₃⟩ mis sous contrôle en PASSAGE LÉGER (option (i) tranchée). Successeur de LC-D3-SPECTRE-K3 (deux-point) ; consomme le dictionnaire opérateur γ de LC-D-CT-GAMMA. Ce chaînon SCELLE (verif_D_nongauss_TTT.py, EXIT 0, 28 asserts, 6 blocs A-F, Phase 1 écrite et EXIT 0 AVANT tout fetch) : [A] ZÉRO LIBRE — la linéarité de g₃=-(i/3)k³g₀ propage la gaussianité : ⟨g₃³⟩_libre=(i/27)k₁³k₂³k₃³⟨g₀³⟩=0 IDENTIQUEMENT sur BD libre ⟹ le trois-point vit au premier ordre du vertex (la chaîne linéaire TRANSPORTE la non-gaussianité, ne la crée pas). [B] MAP γ₃ AB INITIO — γ₃≡⟨TTT⟩_canon/ψ₃=n³ générique ; Brown-York n=2 ⟹ γ₃=8 (pré-déclaration du cadrage CONFIRMÉE par dérivation, pas supposée) ; catalogue d'artefacts de mélange {2,4,8} scellé (leçon R1 généralisée). [D] COMPTAGE d=3 (fetch aveugle, OP∩MP concordants) — 2 formes paires + 1 impaire (présente en fonction d'onde, ABSENTE du bispectre) ; Einstein = 1 forme, W³ = l'autre ⟹ n_libre = 1. [E] TESTS EXACTS — (H/M_Pl)²=8π²/N (dictionnaire interne via A_T·N=16) ; le ⟨γγγ⟩ Einstein fetché (MP éq.2.11/2.20) porte (H/M_Pl)⁴ = LE CARRÉ EXACT du deux-point ⟹ amplitude 64π⁴/N², ratio (H/M_Pl)⁴/A_T²=π⁴/4 slack NUL ⟹ sous gravité d'Einstein le trois-point N'INTRODUIT AUCUN PARAMÈTRE LIBRE NEUF (anti-numérologie : 1 entrée libre N < 3 sorties appariées). [F] FIREWALL — 5 injections fausses cassent. VERDICT : CONVERGENCE (zéro libre, γ₃, dictionnaire, scaling) + CONSOLIDATION (comptage, scission Einstein/W³). L'UNIQUE liberté résiduelle = coefficient W³ ~(LH)⁴, NULLE sous Einstein pur (même conditionnalité que l'édifice) [décision ouverte]. Résidus délimités : forensique ε·ε*=4 vs 2 + étalon Ward OP numérique = PASSAGE LOURD [décision ouverte] ; quatre-point/boucles/non-perturbatif HORS périmètre (S1) ; parité impaire HORS périmètre (S2). SANS SURCLASSEMENT (§6.4) : « trois-point reproduit » = cohérence de coefficients, JAMAIS « secteur non-gaussien fermé / D1 fermé / N fixé / CCC démontrée ». Compte {A4 ; A2★ ; N} INCHANGÉ."
codename: LC-RACCORD
tags: [module-D, module-D3, front-a, non-gaussien, trois-point, g3, TTT, gamma3, maldacena-pimentel, osborn-petkou, W3, einstein, bunch-davies, ds-cft, scaling, N-holographique, anti-fit, passage-leger, sceau]
type: "chaînon (résultat — contrôle du TROIS-POINT en passage léger ; successeur de LC-D3-SPECTRE-K3 ; cadrage LC-WORK-CADRAGE-NONGAUSS v0.1 validé ; SCEAU FAIT verif_D_nongauss_TTT.py)"
statut: "établi (algèbre), SCEAU FAIT — [A] ⟨g₃³⟩_libre=0 identiquement ; [B] γ₃=8 dérivé (n³, Brown-York), catalogue {2,4,8} ; [D] comptage d=3 : 2 paires + 1 impaire (hors bispectre), OP∩MP ; [E] (H/M_Pl)²=8π²/N, ⟨γγγ⟩_R=[⟨γγ⟩]²·O(1), amplitude 64π⁴/N² pendue à N seul, ratio π⁴/4 slack nul ; [F] firewall 5 injections. VERDICT : convergence + consolidation. Décision ouverte : coefficient W³ ~(LH)⁴ (nul sous Einstein pur) ; passage lourd (forensique ε, étalon Ward OP). Hors périmètre : quatre-point/boucles (S1), parité impaire (S2). SANS SURCLASSEMENT (§6.4) ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos ; N non fixé ; CCC non démontrée."
version: 0.1
langue: fr
date: 2026-06-11
maj: "2026-06-11 — v0.1 : ouverture et clôture du passage léger du front non-gaussien (reco §3.1 de LC-WORK-REPRISE-POST-R1-RELECTURE ; option (i) tranchée par Thierry après flag du tri de provenance). Cadrage LC-WORK-CADRAGE-NONGAUSS v0.1 validé+KB AVANT exécution ; carte de conventions et cibles P1' figées SANS fetch ; Phase 1 du sceau (blocs A-C) écrite et EXIT 0 AVANT fetch ; fetch aveugle (MP 1104.2846 texte intégral ; OP hep-th/9307010 abstract ; Ward recoupée 1603.03771+1511.04077) ; Phase 3 (blocs D-F). verif_D_nongauss_TTT.py EXIT 0, 28 asserts, stack 3.12/sympy 1.14. Aucune touche aux chaînons existants. Compte {A4 ; A2★ ; N} inchangé."
statut_id: "validé après sceau (verif_D_nongauss_TTT.py déposé en KB, EXIT 0, 28 asserts) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §7, lot additif SÉPARÉ, NON exécuté ici) : 00_index (carte+changelog), 03_glossaire (entrées trois-point / γ₃ / liberté W³ / comptage 2+1), LC-AUDIT-VERDICT §8bis, 04_references (Maldacena-Pimentel 2011 ; Osborn-Petkou 1994 si absentes ; recoupements Ward), 02_programme. Audit à froid (3ᵉ conversation) prévu par le protocole du cadrage §4."
fichier_compagnon: verif_D_nongauss_TTT.py
prerequis_kb: [LC-WORK-CADRAGE-NONGAUSS, LC-D3-SPECTRE-K3, LC-D-CT-GAMMA, LC-D-CT-ATN, LC-D-HOLOGRAPHIE-G3, LC-AUDIT-LOG-NACTION-AVEUGLE, LC-WORK-REPRISE-CONSTRUCTIF-R1, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_spectre_k3.py, verif_naction_gamma_dHSS.py, verif_naction_aveugle.py, verif_D_CT_constructif.py, verif_D_CT_ATN.py]
renvois: [LC-WORK-CADRAGE-NONGAUSS, LC-D3-SPECTRE-K3, LC-D-CT-GAMMA, LC-D-CT-ATN, LC-D-NONLIN-VERROU, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] / front non-gaussien de D1 — étend le contrôle du secteur de D1 du deux-point (SPECTRE-K3, CT-ATN) au trois-point : sous Einstein, AUCUN paramètre neuf, tout est pendu à N. Ne ferme PAS le secteur non-gaussien (quatre-point, boucles, non-perturbatif hors périmètre)."
  - "[D] / dictionnaire opérateur — première consommation du verdict γ (LC-D-CT-GAMMA) : γ₃=n³=8 dérivé par la même logique Brown-York ; catalogue d'artefacts {2,4,8} opérationnel."
tags_epistemiques: [établi (algèbre), formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·NONGAUSS·TTT — Le trois-point `⟨g₃g₃g₃⟩` : sous Einstein, aucun paramètre neuf (passage léger)

> **But.** Étendre le contrôle du secteur de D1 du deux-point (forme `k³` scellée
> `LC-D3-SPECTRE-K3` ; amplitude `A_T·N=16` ; `C_T/N=1/(32π²)`) au **trois-point**, en
> consommant le dictionnaire opérateur `γ` verrouillé (`LC-D-CT-GAMMA`). Cadrage paper-first
> `LC-WORK-CADRAGE-NONGAUSS` v0.1 (carte de conventions et cibles P1' **figées sans fetch**) ;
> tri de provenance conduit, **option (i) passage léger** tranchée. Sceau :
> `verif_D_nongauss_TTT.py` (EXIT 0, 28 asserts ; Phase 1 écrite et EXIT 0 **avant** fetch).
>
> **Verdict (calculé).**
> **[A] Zéro libre** `[établi — algèbre]`. `⟨g₃g₃g₃⟩_libre = (i/27)k₁³k₂³k₃³⟨g₀³⟩ = 0`
> identiquement sur BD libre — le trois-point vit au **premier ordre du vertex** ; la chaîne
> linéaire `g₃=-(i/3)k³g₀` transporte la non-gaussianité, ne la crée pas.
> **[B] Map `γ₃` ab initio** `[établi — algèbre]`. `γ₃ ≡ ⟨TTT⟩`canon`/ψ₃ = n³` générique ;
> Brown–York `n=2` ⟹ **`γ₃=8`** — la pré-déclaration du cadrage est **confirmée par la
> dérivation**, pas supposée. Catalogue d'artefacts de mélange `{2,4,8}` scellé.
> **[D] Comptage `d=3`** `[établi — algèbre, comparandum externe]`. Fetch aveugle, OP∩MP
> concordants : **2 formes paires + 1 impaire** (présente en fonction d'onde, **absente du
> bispectre**) ; Einstein = 1 forme, `W³` = l'autre ⟹ `n_libre = 1`.
> **[E] Tests exacts** `[établi — algèbre]`. `(H/M_Pl)² = 8π²/N` (via `A_T·N=16`) ; le
> `⟨γγγ⟩` Einstein fetché (MP éq. 2.11/2.20) porte `(H/M_Pl)⁴` = **le carré exact** du
> deux-point ⟹ amplitude `64π⁴/N²`, ratio `(H/M_Pl)⁴/A_T² = π⁴/4` **slack nul**. Sous
> gravité d'Einstein, le trois-point **n'introduit aucun paramètre libre neuf**
> (anti-numérologie : 1 entrée libre `N` < 3 sorties appariées).
> **[F] Firewall.** 5 injections fausses (×2 sur `A_T·N`, ratio `π⁴/2`, `n=1`, comptage 3,
> puissances 3/6) **cassent** toutes.
>
> **Verdict : CONVERGENCE** (zéro libre, `γ₃`, dictionnaire, scaling) **+ CONSOLIDATION**
> (comptage, scission Einstein/`W³`). L'**unique liberté résiduelle** est le coefficient
> `W³ ~ (LH)⁴`, **nulle sous Einstein pur** — même conditionnalité que le reste de
> l'édifice. `[décision ouverte]`

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce chaînon **enregistre un résultat scellé** : le trois-point tensoriel, au niveau arbre et
en perturbatif TT (scoping S1), est **entièrement pendu à `N`** sous gravité d'Einstein —
aucune liberté neuve. Ce qu'il **n'est pas** : il ne ferme **pas** le secteur non-gaussien
(le quatre-point, les boucles, le non-perturbatif sont **hors périmètre**), ne ferme pas
`D1`, ne fixe pas `N`, ne démontre pas CCC, et ne réduit pas le compte `{A4 ; A2★ ; N}`.
La conditionnalité « gravité d'Einstein » (coefficient `W³` nul) est la **même** que celle
portée par tout l'édifice holographique — elle est ici **rendue explicite et mesurable**
(le coefficient `W³` est précisément ce qu'un trois-point observé mesurerait).

---

## 1. Le zéro du secteur libre, et la scission `[établi — algèbre ; bloc A]`

La relation d'état BD `g₃=-(i/3)k³g₀` est linéaire ⟹ sur l'état BD libre (gaussien),
`⟨g₃g₃g₃⟩_libre = (i/27)\,k_1^3k_2^3k_3^3\,\langle g_0g_0g_0\rangle = 0` **identiquement**
(cible P1'-C, tenue). Le trois-point se scinde donc : le **secteur de contact/Ward** est
fixé par le deux-point scellé (aucun contenu neuf) ; le **secteur dynamique** (vertex
cubique) est le seul datum non-gaussien authentique — c'est lui que [D]-[E] contrôlent.

## 2. La map `γ₃ = 8`, dérivée `[établi — algèbre ; bloc B]`

Par la même logique que `LC-D-CT-GAMMA [B]` : `k` insertions de `T = n\,δW/δg` donnent
`⟨T\cdots T⟩`canon` = n^k\,δ^kW` ⟹ `γ_k = n^k`. Brown–York `n=2` (unique, scellé GAMMA [E])
⟹ `γ=4` (recoupé) et **`γ₃=8`**. Le **catalogue d'artefacts de mélange** `{2,4,8}` est
scellé : tout facteur pur de cette liste dans une comparaison est un candidat mélange de
conventions, à vérifier **avant** tout NO-GO — la leçon R1, désormais outillée d'avance.

## 3. Comptage et scission (fetch aveugle) `[établi — comparandum ; bloc D]`

Maldacena–Pimentel (texte intégral) ∩ Osborn–Petkou (abstract), **concordants** : en `d=3`,
la forme générale du trois-point de `T` (≡ `⟨γγγ⟩` dS, MP le disent explicitement) compte
**2 formes paires + 1 impaire** ; l'impaire est présente dans la fonction d'onde mais
**absente du bispectre**. La gravité d'Einstein produit **une** des deux formes paires ;
`W³` produit l'autre, de taille relative `(LH)⁴`. Donc `n_libre = 2 − 1 = 1` : le pattern
du cadrage §1.2 est confirmé, et la liberté unique est **identifiée et nommée**.

## 4. Les tests exacts `[établi — algèbre ; bloc E]`

Jambe interne : `A_T = 16/N = 2H²/(π²M_Pl²)` (scellé) ⟹ `(H/M_Pl)² = 8π²/N` **exact**.
Jambe fetchée : le `⟨γγγ⟩_R` de MP (éq. 2.11) porte `(H/M_Pl)⁴` — **le carré exact** —
avec une kinématique sans `M_Pl` ; MP consignent `f_{NL}`gravity` ≡ ⟨γγγ⟩/⟨γγ⟩² = O(1)`.
D'où :

$$\langle\gamma\gamma\gamma\rangle_R \;\propto\; \Big(\frac{H}{M_{Pl}}\Big)^{\!4}
= \Big(\frac{8\pi^2}{N}\Big)^{\!2} = \frac{64\pi^4}{N^2},\qquad
\frac{(H/M_{Pl})^4}{A_T^2} = \frac{\pi^4}{4}\ \text{(slack nul)}.$$

**Une** entrée libre (`N`) contre **trois** sorties appariées (amplitude deux-point,
amplitude trois-point, scaling `O(1)`) : le critère anti-numérologie est tenu. Cible P1'-B
**tenue**. Cible P1'-A : **tenue dans sa lecture dS-native** (le pinning « aucun nombre neuf
au trois-point » est établi par la chaîne exacte) ; sa lecture CFT-Ward **numérique**
(étalon OP avec valeurs de champs libres + forensique `ε·ε*=4` vs 2) est **non testée ici**,
délimitée vers le passage lourd. `[décision ouverte]`

## 5. Format de chaînon

- **Hypothèse testée.** « Le trois-point `⟨g₃g₃g₃⟩` introduit-il un paramètre libre neuf,
  ou est-il pendu à `N` ? » — Réponse scellée : sous Einstein, **pendu à `N` seul** ; la
  liberté unique est le coefficient `W³`, nul sous Einstein pur.
- **Outil.** Relation d'état BD (FG) ; dictionnaire `γ` (`LC-D-CT-GAMMA`) généralisé en
  `γ_k=n^k` ; candidat-égalité `A_T·N=16` (`CT-ATN`) ; fetch aveugle MP/OP ; protocole
  anti-fit P1'-P5' du cadrage. Sceau `verif_D_nongauss_TTT.py` (sympy ; 28 asserts).
- **Critère de réfutation.** *Issue « paramètre neuf »* : si l'amplitude Einstein avait
  exigé une échelle hors `N` ⟹ échec du critère de réduction, consigné. **Non observé** :
  `(H/M_Pl)⁴` = carré exact. *Issue « artefact de convention »* : neutralisée d'avance par
  le catalogue `{2,4,8}` et la restriction aux ratios insensibles à `ε·ε*`.
- **Verdict.** **Convergence** (A, B, E) **+ consolidation** (D), `[établi — algèbre]`,
  conditionnel aux prescriptions exhibées et à la gravité d'Einstein. Résidus délimités :
  passage lourd (forensique `ε`, étalon Ward OP) `[décision ouverte]` ; coefficient `W³`
  `[décision ouverte]` ; quatre-point/boucles/non-perturbatif et parité impaire
  **hors périmètre** (S1/S2).

---

## 6. Ce que cela change — et ne change pas — pour le programme

**Change.** Le secteur de D1 est désormais contrôlé jusqu'au trois-point inclus : forme
`k³` (deux-point), amplitude `16/N`, et maintenant amplitude trois-point `64π⁴/N²` — la
**même** unique grandeur `N` porte tout, et la première consommation du dictionnaire `γ`
hors de sa session d'origine a fonctionné sans accroc (le catalogue `{2,4,8}` a servi de
garde-fou opérationnel). La conditionnalité Einstein, jusqu'ici implicite, est **nommée et
falsifiable** (coefficient `W³`).

**Ne change pas.** `D1` non clos (le non-gaussien complet excède le trois-point) ; `N` non
fixé (circularité `LC-E` intacte) ; A3/A4 non dérivés ; A2★ seul levier du front (a) ;
pont φ↔CCC aspirationnel ; **CCC non démontrée**. Compte `{A4 ; A2★ ; N}` **inchangé**.

---

## 7. Propagation / housekeeping `[à appliquer — lot additif SÉPARÉ, NON exécuté ici]`

1. **`00_index`** — ligne carte (`LC-D-NONGAUSS-TTT`, module D, trois-point) + changelog.
2. **`03_glossaire`** — entrées : *trois-point `⟨g₃g₃g₃⟩`* (zéro libre ; amplitude
   `64π⁴/N²` sous Einstein) ; *`γ₃`* (`=n³=8`, map opérateur trois-point) ; *catalogue
   d'artefacts `{2,4,8}`* ; *liberté `W³`* (`~(LH)⁴`, nulle sous Einstein pur) ;
   *comptage `2+1` (d=3)*.
3. **`LC-AUDIT-VERDICT §8bis`** — bullet : trois-point contrôlé en passage léger
   (convergence + consolidation, sans surclassement ; conditionnalité Einstein nommée).
4. **`04_references`** — ajouter si absentes : Maldacena & Pimentel, JHEP **09** (2011) 045
   (arXiv:1104.2846) ; Osborn & Petkou, Ann. Phys. **231** (1994) 311 (hep-th/9307010) ;
   recoupements Ward : arXiv:1603.03771 (éq. C.24), arXiv:1511.04077 (App. C).
5. **`02_programme`** — renvoi (front non-gaussien : passage léger fait ; passage lourd =
   upgrade optionnel délimité).

**Audit à froid** (3ᵉ conversation, protocole du cadrage §4) : re-dériver `γ₃` et le
dictionnaire `(H/M_Pl)²=8π²/N` hors contexte, re-fetch MP/OP, re-exécuter le sceau,
vérifier que le firewall casse.

---

## 8. Renvois, glossaire, références

**Renvois.** `LC-WORK-CADRAGE-NONGAUSS` (cadrage, carte figée, P1'-P5') ;
`LC-D3-SPECTRE-K3` (deux-point, parent direct) ; `LC-D-CT-GAMMA` (`γ`, consommé) ;
`LC-D-CT-ATN` (`A_T·N=16`) ; `LC-D-NONLIN-VERROU` (un-point tous ordres — la pile
un/deux/trois-points est désormais : exact / scellé / contrôlé-léger) ;
`LC-AUDIT-VERDICT §6.4` (discipline).

**Références (fetchées ce chaînon).** Maldacena & Pimentel, *On graviton non-gaussianities
during inflation*, JHEP **09** (2011) 045, arXiv:1104.2846 — éq. 2.6, 2.11, 2.18, 2.20 ;
comptage 2+1 ; bispectre sans parité impaire (leurs réfs 1106.3228, 1108.0175). Osborn &
Petkou, Ann. Phys. **231** (1994) 311, hep-th/9307010 — comptage d=3 ; base (â,b̂,ĉ) ;
Ward `C_T = 4S_d[(d−2)(d+3)â−2b̂−(d+1)ĉ]/(d(d+2))` (recoupée arXiv:1603.03771,
arXiv:1511.04077).

---

## Appendice — Légende des tags épistémiques
`établi (algèbre)` : algèbre correcte + cibles reproduites — JAMAIS « CCC établie ».
`formalisable` : chemin de dérivation identifié, non encore scellé.
`décision ouverte` : objet non tranché, ni établi ni réfuté.
`à inventer` : outil/loi manquant, à construire.
`hors de portée` : hors des moyens actuels (ex. `N≡Λ`).
