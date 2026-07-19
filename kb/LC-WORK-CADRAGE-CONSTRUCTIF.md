---
id: LC-WORK-CADRAGE-CONSTRUCTIF
titre: "Cadrage paper-first du PONT CONSTRUCTIF — tester les coefficients scellés A_T·N=16 et C_T/N=1/(32π²) contre une charge centrale CONNUE INDÉPENDAMMENT. Successeur du choix de pivot de LC-WORK-REPRISE-POST-N-BETA §4 (reco : pont constructif = seul terrain du falsifiable POSITIF). Établit (i) la condition de testabilité (A_T/C_T ET N indépendants — l'axe β a échoué précisément parce qu'en dS pur C_T est VERROUILLÉE à N, CT-ATN §3) ; (ii) le critère « charge centrale connue indépendamment » = C_T calculée par une méthode DISJOINTE de la route Einstein-bulk qui a posé le coefficient (comptage de champs libres / localisation SUSY / donnée CFT établie), et ℓ^{d-1}/G côté bulk ⟹ le ratio devient une prédiction sans paramètre ; (iii) un TRI DE CIRCULARITÉ des routes candidates (R1 AdS₄ Einstein-dHSS continué ; R2 CFT₃ à C_T indépendant ; R3 dS/CFT travaillé), chacune marquée consolidation vs falsifiable-positif ; (iv) la recommandation de premier pas scellable (R1) avec son plan de sceau et sa liste de vérifications-littérature. PAS UN CHAÎNON : aucune algèbre, aucun sceau déposé. Subordonné à LC-AUDIT-VERDICT §6.4 : même un test RÉUSSI = « la route holographique reproduit un coefficient CFT établi (algèbre) », JAMAIS « D1 fermé / N fixé / CCC démontrée ». Le compte {A4 ; A2★ ; N} reste INCHANGÉ quel que soit le verdict."
codename: LC-RACCORD
tags: [module-D, module-E, pont-constructif, ds-cft, ads-cft, charge-centrale, C_T, A_T, coefficient, dHSS, falsifiable-positif, circularite, tri, cadrage, paper-first, D1]
type: "note de cadrage (paper-first) — ouvre le front « pont constructif » et POSE le plan ; ne le scelle pas. N'est PAS un chaînon. Subordonnée à LC-AUDIT-VERDICT §6.4. Successeur du choix de pivot de LC-WORK-REPRISE-POST-N-BETA §4."
statut: "CADRAGE — à valider avant tout sceau. Établit le critère de testabilité, le tri de circularité, le menu de routes (R1/R2/R3) et la reco de premier pas (R1). AUCUNE algèbre nouvelle, AUCUN sceau ici. Périmètre {A4 ; A2★ ; N} inchangé."
version: 0.2
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v0.2 : §5bis — PROTOCOLE ANTI-FIT (pré-enregistrement) + AUDIT À FROID, sur exigence de rigueur (réserve : ne pas entacher la méthodologie par du fit interne / de la circularité). Cinq verrous P1-P5 (geler la cible AVANT le fetch ; carte de normalisation déduite des définitions et non du résultat ; trois entrées non négociables i^{d-1}/N=πℓ²/G/convention M_Pl ; fetch aveugle ; firewall) + protocole d'audit à froid en conversation neuve (re-dérivation déductive de la carte, re-fetch indépendant, re-exécution, firewall). Décisions §6 tranchées : §6.1 R1 d'abord ; §6.3 viser la CONVERGENCE honnête (positif fort seulement si ancrage CFT scellé) ; §6.4 web-vérif au seul moment du sceau OK. §6.2 (normalisation) absorbée dans P2. AUCUN sceau, AUCUNE algèbre nouvelle, AUCUNE touche KB. | 2026-06-10 — v0.1 : cadrage initial du pont constructif. Identifie l'obstruction (verrouillage C_T~N en dS pur, CT-ATN §3) que toute route doit BRISER ; pose le critère d'indépendance (C_T par méthode disjointe de la route Einstein-bulk) ; trie les routes par statut de circularité ; recommande R1 (AdS₄ Einstein, coefficient dHSS continué, ancré sur un C_T CFT établi) comme premier pas scellable, le SEUL où la charge centrale de référence n'est ni conjecturale (dS/CFT) ni non-Einstein (haut-spin). Décisions de cadrage flaggées au §6. SANS SURCLASSEMENT (§6.4). Aucune touche KB."
prerequis_kb: [LC-D-CT-ATN, LC-D-CT-REALITE, LC-D-CT-DUAL-DS, LC-D-HOLOGRAPHIE-G3, LC-E-N-CROSSCHECK, LC-E-PLANCK-RESIDUEL, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: []
tags_epistemiques: [établi (algèbre), formalisable, à inventer, décision ouverte, hors de portée]
---

# Cadrage — Pont CONSTRUCTIF : tester les coefficients `16` et `1/(32π²)`

> **Pour l'instance qui ouvre le front constructif.** Note de cadrage paper-first.
> Discipline `LC-AUDIT-VERDICT §6.4` : l'objectif est de **tester deux nombres purs
> scellés** (`A_T·N=16`, `C_T/N=1/(32π²)`) contre une charge centrale **connue
> indépendamment**. Même un test **réussi** = `établi (algèbre)` d'une convergence
> de coefficients, **jamais** « D1 fermé », « `N` fixé » ou « CCC démontrée ». Le
> compte `{A4 ; A2★ ; N}` est **inchangé** quel que soit le verdict.

---

## 0. Rôle, et ce que ce cadrage n'est PAS

Ce document **ouvre** le pont constructif et en **pose le plan** ; il ne le scelle pas.
Aucune algèbre nouvelle, aucun sceau, aucune touche KB ici. Il produit quatre choses :
le **critère de testabilité** (§2), le **tri de circularité** des routes (§3-4), la
**recommandation de premier pas** (§5) et les **décisions de cadrage** à trancher (§6).

---

## 1. Le falsifiable POSITIF, précisément `[rappel de l'acquis]`

Le programme a scellé (`LC-D-CT-ATN`, `verif_D_CT_ATN.py`, EXIT 0) **deux nombres purs**,
en convention standard (`M_Pl²=(8πG)⁻¹`, spectre BD, entropie GH) :

$$A_T\cdot N = 16,\qquad \frac{C_T}{N}=\frac{1}{32\pi^2}.$$

Ce qui est `établi (algèbre)` n'est **pas** que ces nombres soient « la physique de la
CCC », mais que (i) `A_T·N` est un nombre **pur** (cancellation structurelle `H,G`) et
(ii) la route canonique [A] et la route holographique dS/CFT [D] **convergent** sur le
même `⟨|h|²⟩`. Le **coefficient** (`16`, `1/(32π²)`) est le seul falsifiable *positif*
du programme : un objet numérique qui pourrait être **faux** et qu'une mesure ou un calcul
indépendant pourrait contredire.

---

## 2. La condition de testabilité, et l'obstruction de l'axe β `[le cœur]`

**Pourquoi l'axe β ne testait rien.** En dS pur, `C_T` est **verrouillée à `N`** par
l'holographie (`CT-ATN §3` : le coefficient de `⟨TT⟩∝C_T k³` vaut `∝M_Pl²/H²`, et
`C_T/N=1/(32π²)` est constant *par scellement*). `C_T` n'est donc **pas une inconnue
indépendante** : c'est `N`, lu côté CFT. Idem `A_T=16/N`. Le ratio `C_T/N` ne **mesure**
rien — il est **posé**. C'est exactement le verdict β : consolidation, `DOF=1` (le seul
`Λ`), `LC-E-N-CROSSCHECK`.

**Ce que doit faire le constructif.** Le test n'a de sens que dans un cadre où

$$\boxed{\;C_T \text{ (ou } A_T)\ \text{ET}\ N\ \text{sont des intrants INDÉPENDANTS.}\;}$$

Concrètement : `C_T` calculée par une **méthode disjointe** de la route Einstein-bulk qui
a servi à poser le coefficient (comptage de champs libres ; localisation SUSY ; donnée CFT
établie / vérifiée), **et** `ℓ^{d-1}/G` (l'analogue de `N`) calculé côté bulk. Alors
`C_T/(ℓ^{d-1}/G)` devient une **prédiction sans paramètre** : `1/(32π²)` (modulo le facteur
de continuation, déjà cadré par `REALITE`) **tient ou ne tient pas**. Voilà le falsifiable.

> **Garde-fou de circularité (à porter sur chaque route).** Si la charge centrale de
> référence a été calculée *par la même route Einstein-bulk / le même dictionnaire dHSS*
> qui a posé `1/(32π²)`, alors la comparer à `1/(32π²)` est une **consolidation**, pas un
> test. Le falsifiable-positif exige une **source disjointe** pour `C_T`.

---

## 3. Tri de circularité — la grille de lecture `[méthodologie §6.4]`

Toute route candidate se classe par la **provenance** de sa charge centrale de référence :

| Provenance de `C_T` de référence | Statut du test | Pourquoi |
|---|---|---|
| Même dictionnaire dHSS / route Einstein-bulk qui a posé `1/(32π²)` | **consolidation** | tautologie : on compare le nombre à lui-même |
| Route holographique **distincte** (p. ex. fonction d'onde dS vs 2ⁿᵈ variation d'action AdS), **mais** cadre holographique commun | **convergence** (falsifiable faible) | non tautologique mais non disjoint ; analogue au test [A]/[D] de CT-ATN |
| Méthode **CFT-native** disjointe (champs libres / localisation SUSY), dual vérifié | **falsifiable POSITIF fort** | `C_T` et `ℓ^{d-1}/G` indépendants ⟹ vrai test |

C'est cette grille qui décide si une route mérite un sceau ou retombe en consolidation.

---

## 4. Menu des routes candidates `[avec statut de circularité]`

**R1 — AdS₄ Einstein, coefficient dHSS continué `[recommandé — premier pas]`.**
Comparer `1/(32π²)` au coefficient **établi** de `C_T` pour une CFT₃ duale à la gravité
d'Einstein en AdS₄ (de Haro–Skenderis–Solodukhin ; forme `C_T^{AdS}=κ_3·ℓ²/G`, `κ_3`
nombre pur). Test : la continuation `ℓ_AdS→iℓ_dS` (règle `i^{d-1}`, `REALITE`) de `κ_3`
reproduit-elle `C_T/N=1/(32π²)` avec `N=π ℓ_dS²/G` (aire-entropie) ?
- **Statut.** *Au minimum* **convergence** (la voie dS-fonction-d'onde de `CT-ATN [D]` vs
  la voie AdS-2ⁿᵈ-variation de dHSS sont des calculs distincts) ; **falsifiable-positif**
  *si et seulement si* le `κ_3` de dHSS est lui-même **ancré sur une donnée CFT vérifiée**
  (free-field counting d=3 ; ou `C_T` d'ABJM par localisation, dual Einstein à grand `N,k`).
  C'est le point à établir au sceau.
- **Pourquoi en premier.** C'est la **seule** route dont la charge centrale de référence
  est **établie** (AdS/CFT, non conjecturale) **et** Einstein (le bon graviton). dS/CFT et
  haut-spin (R3) sont l'un conjectural, l'autre non-Einstein.
- **Risque.** Si l'on montre que la voie dS-fonction-d'onde **dérive de** dHSS (et non d'un
  calcul disjoint), R1 chute en pure consolidation ⟹ il faut alors basculer sur R2.

**R2 — CFT₃ à `C_T` indépendant `[falsifiable-positif fort, plus coûteux]`.**
Choisir une CFT₃ dont `C_T` est connu par une méthode **CFT-native** (comptage de champs
libres ; localisation SUSY) et dont le dual gravitationnel est **Einstein** (p. ex. ABJM à
grand `N,k`). Comparer `C_T/(ℓ²/G)` à `1/(32π²)`.
- **Statut.** Le **vrai** falsifiable-positif (sources disjointes).
- **Risque.** Les duals à `C_T` le plus proprement indépendant (haut-spin / champs libres)
  ne sont **pas** Einstein — leur `C_T` est celui du secteur haut-spin, pas du graviton
  `A_T`/`C_T` du programme ⟹ il faut un dual **strongly-coupled SUSY** (ABJM) où la
  localisation donne `C_T` **et** le dual est Einstein. Cadrage plus lourd.

**R3 — exemple dS/CFT travaillé `[le plus aligné CCC, le plus conjectural]`.**
Un modèle dS₄/CFT₃ explicite (type Anninos–Hartman–Strominger, Sp(N)/champs libres) où
`C_T` est calculable côté CFT euclidienne.
- **Statut.** Le plus **proche de la CCC** (vrai `Λ>0`) ; mais dS/CFT est **conjectural**
  (`HOLOGRAPHIE-G3 §3`) et ces modèles sont **haut-spin**, pas Einstein.
- **Risque.** Double : conjectural + mauvais secteur (haut-spin). À garder en réserve.

---

## 5. Recommandation de premier pas scellable `[R1, paper-first puis sceau]`

**Premier pas = R1, en deux temps.**

1. **Tri de provenance (paper, AVANT sceau).** Tracer, dans `CT-ATN [D]`, si le coefficient
   `1/(32π²)` a été obtenu par un calcul **dS-native** (fonction d'onde, `𝒫=1/(2|Im F|)`)
   **indépendant** du `κ_3` de dHSS, ou s'il en est une réécriture. *Lecture préliminaire*
   (`CT-ATN §2-3`) : la voie [D] part de la fonction d'onde `F=(M_Pl²/4)a²(H'/H)` et de la
   prescription de Maldacena — c'est un calcul dS, **pas** une injection de `κ_3`. Donc R1
   est *a priori* au moins **convergence**, possiblement **positif** ⟹ GO pour le sceau.
   *(Ce tri est l'analogue du tri de `CT-CADRAGE` ; il décide R1 vs bascule R2.)*

2. **Sceau R1 `verif_D_CT_constructif.py` (à écrire après validation du tri).** Contenu visé :
   - `[A]` poser `κ_3` (dHSS, AdS₄, `d=3`) — **à vérifier en littérature** (valeur exacte de
     `C_T^{AdS}=κ_3·ℓ²/G` en `d=3` ; de Haro–Skenderis–Solodukhin 2001 ; recoupement
     Buchel–Myers et al. ; et l'ancrage `κ_3`↔donnée CFT vérifiée pour qualifier le statut) ;
   - `[B]` continuer `ℓ_AdS→iℓ_dS` (`i^{d-1}=i²=−1`, `REALITE`) et identifier `N=π ℓ_dS²/G` ;
   - `[C]` test : `κ_3` continué `⟹ C_T/N =?= 1/(32π²)` (assertion centrale) ;
   - `[D]` **firewall** : injecter un `κ_3` faux (×2, ou mauvaise puissance de `ℓ`) doit
     **casser** l'égalité ⟹ test sensible, non tautologique ;
   - bilan + verdict `établi (algèbre)` borné par §6.4.

   Cible numérique de contrôle (paper) : `C_T/N=1/(32π²)` avec `N=π ℓ²/G` impose
   `κ_3=1/(32π)` côté AdS continué — c'est le nombre que la littérature dHSS doit livrer
   (ou réfuter). **À web-vérifier au sceau**, pas avant.

---

## 5bis. Protocole anti-fit (pré-enregistrement) + audit à froid `[exigence de rigueur]`

Le risque que R1 doit exclure : que la convergence `C_T/N=1/(32π²)` soit **fabriquée** par
un choix de conventions (normalisation de `⟨TT⟩`, facteurs de polarisation, identification
`N↔ℓ²/G`, facteur de continuation) ajusté *après* avoir vu la valeur dHSS. C'est le **fit
interne**. Cinq verrous :

- **P1 — geler la cible AVANT toute web-vérification.** Inscrire dans le sceau, avant le
  fetch : la prédiction `κ₃^{cont}=1/(32π)` (≡ `C_T/N=1/(32π²)`) ; le critère de succès =
  égalité **exacte** (slack algébrique **nul**) ; le verdict d'écart = **NO-GO informatif**
  (aucun rattrapage par convention).
- **P2 — carte de normalisation DÉDUITE des définitions, pas du résultat.** Le dictionnaire
  entre la normalisation de `⟨T_{ij}T_{kl}⟩` de dHSS et celle du programme se dérive de la
  **définition** de `C_T` (coefficient de la structure tensorielle standard `d=3`), écrite et
  figée **avant** le fetch. Aucune liberté résiduelle choisie pour faire coller.
- **P3 — trois entrées non négociables.** (i) continuation `i^{d-1}` (`REALITE`, scellée,
  zéro liberté) ; (ii) `N=Aire/4G=π ℓ²/G`, **même** identification géométrique côté AdS ;
  (iii) convention `M_Pl=(8πG)^{−1/2}` tracée.
- **P4 — web-vérification « aveugle ».** Le critère étant gelé (P1-P3), la valeur dHSS est
  insérée **mécaniquement** : le fetch ne peut que **valider ou réfuter**, jamais reparamétrer.
- **P5 — firewall obligatoire** (déjà prévu, bloc [D]). Injecter un `κ₃` faux (×2, mauvaise
  puissance de `ℓ`) doit **casser** l'égalité ⟹ pouvoir discriminant prouvé.

**Audit à froid `[conversation neuve dédiée — pratique LC-WORK-AUDIT-FROID]`.** Le verdict de
R1 n'est **acquis** qu'après ré-audit par une instance **sans contexte** qui : (a) re-dérive
la carte de normalisation (P2) à partir des seules définitions, sans que cette dérivation
**utilise** la cible ; (b) re-fetch la valeur dHSS indépendamment ; (c) re-exécute le sceau
(EXIT 0) ; (d) vérifie que le firewall casse. Garantie anti-fit : si la carte a été
**rétro-ajustée**, l'auditeur à froid la re-dérive autrement et le verdict tombe. La cible
étant publiée, l'auditeur n'en est pas aveugle — ce qui est audité est que la carte est
**déductive** (dérivable des définitions sans passer par la cible), donc le sceau doit la
porter **explicitement et déductivement**, auditable hors contexte.

---

## 6. Décisions de cadrage `[état]`

> **Tranchées (2026-06-10).** §6.1 = **R1 d'abord**. §6.3 = viser la **convergence honnête**
> (positif fort seulement si l'ancrage CFT est scellé). §6.4 = web-vérif dHSS **au seul moment
> du sceau**, OK. §6.2 (normalisation) = **absorbée dans P2** (carte déduite des définitions).

1. **Route de départ.** R1 — R2 en bascule **si** le tri §5.1 fait chuter R1 en consolidation.
   **[tranché : R1]**
2. **Normalisation de `C_T`.** Ramener dHSS et le programme à la même normalisation de
   `⟨T_{ij}T_{kl}⟩`. **[absorbé dans P2 : carte déduite des définitions, figée avant fetch]**
3. **Statut visé.** Verdict réaliste = **« convergence »** (falsifiable faible, analogue
   [A]/[D]) ; **« positif fort »** seulement si l'ancrage `κ₃`↔donnée-CFT-vérifiée est scellé.
   **[tranché : viser la convergence ; anti-fit P1-P5 porté]**
4. **Web-vérification.** Valeur exacte de `C_T^{AdS₄}` (dHSS) web-vérifiée **au moment du
   sceau** (P4, aveugle), pas avant. **[tranché : OK]**

---

## 7. Garde-fous portés `[discipline §6.4]`

- **Test réussi ≠ surclassement.** Même `C_T/N=1/(32π²)` confirmé contre dHSS = `établi
  (algèbre)` d'une convergence de coefficients. **Jamais** « `N` fixé » (il reste lu sur `Λ`,
  `LC-E-N-CROSSCHECK`), « D1 fermé », ou « CCC démontrée ».
- **Compte inchangé.** `{A4 ; A2★ ; N}` n'est ni réduit ni augmenté par ce front.
- **Circularité explicite.** Chaque route porte son statut (consolidation / convergence /
  positif fort) ; aucun glissement silencieux d'un cran vers le haut.
- **Inchangés.** D1 non clos ; (A) physique conditionnel au seul A2★ ; « le bang gagne »
  (P6 B) ; A3/A4 non fusionnés ; circularité LC-E non brisée ; **CCC non démontrée**.
