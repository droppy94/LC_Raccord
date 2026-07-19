---
id: LC-WORK-A3-D1-PASSERELLE
titre: "Module A / passerelle A3 ⟷ D1 — RÉDUCTION DE COMPTAGE (paper-first, AUCUN code neuf). Teste si le pivot A3 (isotropie/dS-invariance du raccordement) est INDÉPENDANT du verrou D1 (unicité du facteur conforme). Verdict cartographié : NON indépendants — A3 et D1 contraignent le MÊME objet, la marée g₍₃₎. Sous (Def-2) A3 = dS-invariance de l'état, A3 se réduit à la détermination UN-POINT de g₍₃₎ (⟨g₃⟩=0), DÉJÀ SCELLÉE au niveau perturbatif un-point via Bunch-Davies (LC-D3-WEYL-BUNCHDAVIES). ⟹ A4 ⟹ A3-un-point : au niveau un-point, A3 est ABSORBÉ dans A4 — le compte de socles indépendants baisse d'un cran. La liberté D1 que A3 ne fixe PAS est exactement le deux-point ⟨g₃g₃⟩~k³ (LC-D3-SPECTRE-K3) = spectre primordial = l'écart A3/A4. CE QUE CE CADRAGE FAIT : réduction d'hypothèse (critère central), adossée à du scellé, sans algèbre neuve. CE QU'IL NE FAIT PAS : il n'établit pas la coïncidence AU-DELÀ du un-point perturbatif (non-linéaire = décision ouverte, hérité de WEYL-BD) ; il ne ferme PAS D1 (le deux-point k³ reste libre) ; il ne traite PAS (Def-1) σ↔g₃ (encart §5, à inventer)."
codename: LC-RACCORD
type: note de travail / cadrage papier (paper-first) — passerelle inter-postulats. Subordonnée à LC-AUDIT-VERDICT §6.4. Étage cartographie (LC-07-like), non fermeture (LC-10-like).
version: 0.3
langue: fr
date: 2026-06-09
maj: "2026-06-09 — v0.3 : GÉNÉRALISATION NON-LINÉAIRE UN-POINT relevée — enregistrement du successeur LC-D-NONLIN-VERROU v0.1 (triptyque scellé, verif_nonlin_cotton/repr/parity.py EXIT 0, 31 asserts). La généralisation non-linéaire de la réduction A4⟹A3-un-point, laissée `décision ouverte` en v0.1/v0.2 (héritée de WEYL-BD §6), est désormais `établie` AU UN-POINT, non-perturbativement (tous ordres, secteur de Weyl complet E⊕B, deux parités) : magnétique B=Cotton[g0]=0 sur fond conf. plat (parité impaire, sans représentation) ; électrique E=g₃ transverse+sans trace par Ward EXACTES (d=3 impair) ⟹ pur spin-2 ⟹ ⟨E⟩=0 (parité paire) ; cohérence de parité E vrai-tenseur / B pseudo-tenseur. §3 (Ouvert) et statut reclassent ce point de `décision ouverte` à `établi (un-point)`. RESTE OUVERT : le DEUX-POINT ⟨g₃g₃⟩~k³ (non-linéaire au deux-point), irréductible — A3/A4 NON fusionnés tout court ; D1 non clos. Mise à jour de statut additive, AUCUNE touche à l'algèbre de v0.1/v0.2. | 2026-06-09 — v0.2 : enregistrement du sceau de reconfirmation `verif_A3_D1_passerelle.py` (EXIT 0, 11/11 ASSERTS), produit après validation de la note v0.1. Le sceau rejoue, sans algèbre neuve, l'emboîtement déjà établi par les parents (verif_D3_bunchdavies.py, verif_D3_spectre_k3.py) : [1] devise commune g₃ (relation d'état BD g₃=-(i/3)k³g₀) ; [2] route A3 ⟹ ⟨g₃⟩=0 forcé par symétrie (projection TT d'un tenseur isotrope = 0) ; [3] route A4 (g₃=0) ⟹ ⟨g₃⟩=0, inclusion S_A4⊊S_A3 STRICTE ⟹ A4⟹A3-un-point (sens unique), {A3,A4}→{A4} au un-point ; [4] divergence A3/A4 = deux-point ⟨g₃g₃⟩∝k³ (SPECTRE-K3), irréductible, ne ferme pas D1. §7 : sceau optionnel marqué EXÉCUTÉ. Aucune touche à l'algèbre amont ; réduction reste `établie un-point perturbatif`, non-linéaire `décision ouverte`. | 2026-06-09 — v0.1 : cadrage initial. Verrouille (Def-2) A3 = dS-invariance de l'état de raccordement (colonne) ; encart (Def-1) A3 = isotropie dynamique σ=0 borné et tagué décision ouverte. Établit la carte emboîtée A4 ⊃ A3-un-point sur la devise commune g₍₃₎, la réduction A4 ⟹ A3-un-point (adossée à LC-D3-WEYL-BUNCHDAVIES, un-point perturbatif), le critère de réfutation, et le résidu k³ (LC-D3-SPECTRE-K3) comme écart A3/A4 au deux-point. AUCUN sceau neuf. AUCUNE touche algèbre. Propagation NON exécutée (proposée §7, à valider/déposer séparément)."
statut: "RÉDUCTION CARTOGRAPHIÉE (établie au un-point perturbatif via sceaux existants) / généralisation non-linéaire AU UN-POINT établie (LC-D-NONLIN-VERROU, non-perturbatif, deux parités) ; au DEUX-POINT (k³) décision ouverte / (Def-1) à inventer. A3 et A4 NON fusionnés au-delà du un-point (écart = k³). C7 non concerné. CCC non démontrée."
prerequis_kb: [LC-D3-WEYL-BUNCHDAVIES, LC-D3-SPECTRE-K3, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-A-SURVIE-CONFORME, LC-D-HOLOGRAPHIE-G3, LC-D3-INTERAEON-P6, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX, 02_programme-de-recherche, 03_glossaire]
fichiers_compagnons_kb: [verif_A3_D1_passerelle.py]   # sceau de reconfirmation (EXIT 0, 11/11) ; s'appuie aussi sur verif_D3_bunchdavies.py et verif_D3_spectre_k3.py (existants)
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
renvois: [LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-D3-WEYL-BUNCHDAVIES, LC-D3-SPECTRE-K3, LC-D-HOLOGRAPHIE-G3, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-AUDIT-VERDICT, LC-00-INDEX]
---

# LC-WORK · Passerelle A3 ⟷ D1 — réduction de comptage

> **Question.** A3 (pivot du front (a) : isotropie/dS-invariance du raccordement) et D1
> (verrou du module A : unicité du facteur conforme au crossover) sont-ils des postulats
> **indépendants**, ou l'un contraint-il l'autre ? Si lié, le **compte de postulats
> irréductibles baisse** — critère central du programme.
>
> **Verdict cartographié (Def-2).** **NON indépendants.** A3, A4 et D1 contraignent **le
> même objet** : la marée `g₍₃₎` (Weyl rescalé / donnée TT de Friedrich). Sous (Def-2)
> [A3 = dS-invariance de l'état], A3 **se réduit** à la détermination *un-point* de cette
> marée, `⟨g₃⟩ = 0` — **déjà scellée au niveau perturbatif un-point** (`LC-D3-WEYL-BUNCHDAVIES`).
> Donc **A4 ⟹ A3-un-point** : au niveau un-point, **A3 est absorbé dans A4**. La liberté
> D1 que A3 ne fixe pas est exactement le **deux-point `⟨g₃g₃⟩ ~ k³`** (`LC-D3-SPECTRE-K3`),
> qui est aussi l'écart entre A3 et A4. **Réduction d'hypothèse, pas fermeture de D1.**

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce document est un **cadrage** (étage `LC-07`-like), au même titre que `LC-WORK-A2-CONJECTURE`
l'était pour C7-b/A2. Il **isole** une dépendance entre postulats et **réduit** un compte ;
il **ne ferme pas** D1 et ne lève rien. Présenter « A3 = A4 » comme acquis hors du un-point
perturbatif serait une surinterprétation du type corrigé en `LC-05` v0.2→v0.3. La coïncidence
sous-jacente (`⟨g₃⟩_{BD}=0=g₃(C→0)`) est un `établi (sceau)` *perturbatif un-point* (WEYL-BD) ;
sa portée non-linéaire reste `décision ouverte` — exactement la réserve de WEYL-BD §6.

**Choix de périmètre verrouillé (opérateur, 2026-06-09).**
- **(Def-2) A3 = dS-invariance de l'état de raccordement** → **colonne** de la passerelle.
- **(Def-1) A3 = isotropie dynamique (`σ=0`)** → **encart §5**, cartographié, **non traité**.
- **Cible = réduction de comptage** (A3 absorbé dans A4 au un-point), non simple diagnostic.

---

## 1. La devise commune — tout passe par la marée `g₍₃₎` `[recoupement de 3 maillons scellés]`

La donnée conforme près d'un `𝓘` spacelike (Friedrich, `LC-A-SURVIE-CONFORME` §2b) est le
couple `(g₍₀₎, g₍₃₎)` : `g₍₀₎` = 3-métrique conforme (la « forme »), `g₍₃₎` = tenseur TT
= Weyl rescalé (la « marée » / contenu radiatif). Les trois objets s'y projettent ainsi :

- **D1** (`LC-A-D1-FACTEUR-CONFORME` §3 + `LC-A-D1-STABILITE-WEYL`).
  La réciprocité `Ω̂Ω̌=−1` fixe le **background** et la **classe conforme `g₍₀₎`**, **pas**
  `g₍₃₎`. `STABILITE-WEYL` décompose en outre D1 en **fond `(m,λ)` ⊥ marée `g₍₃₎`** : la
  stabilité inter-éons fixe le fond à la relation `m̂λ̂ = 9k²/4`, et « la fermeture, si elle
  existe, vient du secteur inhomogène `g₍₃₎` » (domaine D3/[D]). **⟹ la liberté résiduelle
  de D1 = `g₍₃₎`.** `[établi]`
- **A4 (WCH)** : `C_{abcd} → 0` au crossover ⟺ `g₍₃₎ → 0` (champ complet). Contrainte
  **directe** sur `g₍₃₎`. `[définition du socle]`
- **A3 (dS-invariance, Def-2)** : sur un mode TT de dS₄, le Weyl électrique rescalé est
  **dérivé** `E_{ij} = (d/2H) g₃` (Δ=d=3 ; `LC-D3-WEYL-BUNCHDAVIES`), et l'état de
  Bunch-Davies (dS-invariant, sans condensat) donne `⟨g₃⟩ = 0`. **⟹ A3 contraint le
  un-point de `g₍₃₎`.** `[établi un-point, perturbatif]`

**Conséquence structurelle.** A3, A4, D1 ne touchent pas des pièces *différentes* de
`(g₀, g₃)` : ils contraignent **tous `g₃`**, à des niveaux **emboîtés**.

| Postulat | Contrainte sur `g₃` | Niveau | Statut KB |
|---|---|---|---|
| **A4** (WCH) | `g₃ → 0` (champ complet) | le plus fort | socle posé |
| **A3** (dS-inv, Def-2) | `⟨g₃⟩ = 0` (moyenne / un-point) | strictement plus faible | **`établi` un-point** (`verif_D3_bunchdavies.py`) |
| **D1** | application complète `ĝ₃ ↦ ǧ₃` | tout `g₃` | **verrou ouvert** |

*(C'est pourquoi (Def-2) est la bonne colonne : le lien A3→`g₃` y est direct et déjà scellé,
là où (Def-1) exigerait un maillon σ↔`g₃` neuf — cf. §5.)*

---

## 2. La réduction — `A4 ⟹ A3-un-point` `[le mouvement de comptage]`

L'emboîtement du §1 se lit comme une **implication**, pas une simple coïncidence :

$$\boxed{\;\text{A4 : } g_3 \to 0 \;\;\Longrightarrow\;\; \langle g_3\rangle = 0 \;:\; \text{A3-un-point}\;}$$

Trivialement : si la WCH force le champ `g₃` entier vers `0`, sa moyenne `⟨g₃⟩` est `0` *a
fortiori*. Donc **poser A4 délivre gratuitement le contenu un-point de A3** : au niveau
un-point, **A3 n'est pas un postulat indépendant** — il est **absorbé dans A4**.

**Direction et asymétrie `[à ne pas perdre]`.** L'implication est **à sens unique** :
- `A4 ⟹ A3-un-point` (✓, ci-dessus) ;
- `A3 ⇏ A4` : la dS-invariance ne donne que `⟨g₃⟩=0` (un-point), **pas** `g₃→0` (champ
  complet). A3 laisse vivre la variance.

Donc on ne fusionne **pas** A3 et A4 *tout court* ; on établit que **le contenu un-point de
A3 est redondant** dès qu'on tient A4. Le compte `{A3, A4}` de socles **indépendants** passe,
*au niveau un-point*, à `{A4}`. C'est la réduction visée.

**Renfort indépendant du sceau `[formalisable]`.** La nullité `⟨g₃⟩=0` sous dS-invariance
n'est pas qu'un fait perturbatif calculé : `g₃` est un tenseur TT symétrique de rang 2, et un
**one-point function dS-invariant** d'un tel objet doit être un tenseur TT invariant sous le
groupe d'isométrie maximal — qui **n'existe pas non nul** (aucune direction privilégiée).
`⟨g₃⟩=0` est donc *forcé par la symétrie*, ce qui suggère que la réduction survit au-delà du
mode unique testé. **Mais** ce renfort reste `formalisable` (non scellé non-linéairement) — il
ne **promeut pas** la réduction au-delà du `établi un-point`.

---

## 3. Ce qui est SCELLÉ vs OUVERT `[traçabilité]`

**Scellé (adossé, aucun sceau neuf) :**
- `A3-un-point : ⟨g₃⟩_{BD} = 0` — `établi (sceau)` perturbatif, `verif_D3_bunchdavies.py`
  (`LC-D3-WEYL-BUNCHDAVIES`). Mode TT de dS₄, Δ=3.
- `A4-un-point : g₃(C→0)=0 ⟹ ⟨g₃⟩=0` — même sceau (`E=(d/2H)g₃`).
- **Coïncidence `⟨g₃⟩_{BD}=0=g₃(C→0)`** — `établi un-point` (WEYL-BD verdict).
- **Résidu deux-point `⟨g₃g₃⟩ ~ k³`** — `établi (sceau)`, `verif_D3_spectre_k3.py`
  (`LC-D3-SPECTRE-K3`), Δ=3, variance log (non quartique, artefact leading C5).

**Ouvert (non franchi par ce cadrage) :**
- **Généralisation non-linéaire** de la coïncidence un-point (au-delà du mode TT perturbatif) :
  `décision ouverte`, hérité tel quel de WEYL-BD §6. La réduction du §2 est **strictement
  un-point perturbatif**.
  > **MISE À JOUR `[2026-06-09]`** : la généralisation **non-perturbative AU UN-POINT** est
  > désormais `établie` (`LC-D-NONLIN-VERROU`, triptyque scellé) — sous A3, le un-point du Weyl
  > rescalé **complet** (`E∝g₃` ⊕ `B∝Cotton`) s'annule **exactement (tous ordres)** sur les **deux
  > parités** : magnétique `Cotton=0` sur fond conf. plat ; électrique pur spin-2 par les **Ward
  > exactes** en `d=3`. Ce point passe donc de `décision ouverte` à **`établi (un-point)`**.
  > **Reste ouvert** : le **deux-point** `⟨g₃g₃⟩∝k³` (non-linéaire au deux-point), **irréductible**
  > — A3/A4 non fusionnés *tout court*.
- **L'écart A3/A4 au deux-point** : A3 (dS-inv) **ne tue pas** `⟨g₃g₃⟩~k³` ; A4-complet, si.
  Cet écart **est** le spectre primordial (`SPECTRE-K3`). Il **ne disparaît pas** par la
  réduction — il est ce qui reste irréductible. `[décision ouverte ; = donnée de Cauchy [D]]`
- **(Def-1)** : voir §5.

---

## 4. Critère de réfutation `[falsifiabilité]`

La réduction `A4 ⟹ A3-un-point` (Def-2) **casserait** si A3 portait du contenu un-point
**indépendant** de `⟨g₃⟩=0` — concrètement :

$$\text{REFUTATION : } \exists \text{ état dS-invariant (BD-like) avec } \langle g_3\rangle \neq 0
\;\;(\text{condensat de marée}).$$

Un tel état rendrait A3 (dS-inv) porteur d'une contrainte un-point que A4 ne fournit pas,
brisant l'absorption. **Statut** : exclu par `verif_D3_bunchdavies.py` (BD : pas de condensat,
`⟨g₃⟩=0`) **et** par l'argument de symétrie du §2 (pas de tenseur TT invariant non nul). Aucun
contre-exemple connu. La réduction tient au niveau testé.

*(Réfutation du programme, distincte : si l'on montrait que `A3-complet` requiert plus que
`⟨g₃⟩=0` ET que ce surplus n'est pas couvert par A4, alors A3 redeviendrait partiellement
indépendant — mais cela vivrait dans le deux-point, qui est déjà compté comme résidu k³.)*

---

## 5. Encart (Def-1) — A3 = isotropie dynamique `σ=0` `[cartographié, NON traité — à inventer]`

Sous **(Def-1)** [A3 = `σ=0`, usage front (a) / porte (i) `Einstein-3D ⟺ A3`,
`LC-D3-CROSSOVER-EINSTEIN3D`], le lien à la marée `g₍₃₎` **n'est pas direct** : il faut un
maillon supplémentaire reliant l'**anisotropie classique du raccordement** (`σ`, cisaillement)
à la **donnée TT `g₃`**. Ce maillon :
- touche le **secteur inhomogène complet** (anisotropie ↦ donnée de Cauchy TT), domaine encore
  ouvert de **D3 / [D]** ;
- ferait basculer la note de `formalisable` (adossé) vers `à inventer` (travail neuf) ;
- pourrait *ne pas* se scellér sans le crossover inhomogène complet (cf. portée FLRW-seule de
  l'atlas D1, `LC-A-D1-FACTEUR-CONFORME` §4-bis « portée honnête »).

**Décision** : maillon `σ ↔ g₃` **tagué `à inventer`**, laissé hors de cette note. S'il devient
prioritaire, c'est un **chantier nommé propre** (candidat pivot D3/[D] ultérieur), non une dette
diluée ici. *Note* : `STABILITE-WEYL` observe déjà que dans le secteur **symétrique** FLRW,
`C ≡ 0` (Weyl nul) — donc (Def-1) et la marée `g₃` y sont **dégénérés** ; l'enjeu (Def-1) ne
mord que **hors symétrie**, ce qui confirme qu'il appartient au secteur inhomogène.

---

## 6. Ce que ce cadrage FAIT vs NE FAIT PAS `[honnêteté §6.4]`

**FAIT.** Réduit le **nombre de postulats indépendants** : `{A3, A4}` → `{A4}` **au niveau
un-point** (A3-un-point absorbé dans A4), adossé à des sceaux existants, **sans algèbre neuve**.
Identifie proprement l'écart résiduel A3/A4 comme le **deux-point `k³`** déjà caractérisé
(`SPECTRE-K3`). Relit la chaîne `D1 (liberté = g₃) → A4 (g₃→0) → A3-un-point (⟨g₃⟩=0)` comme une
hiérarchie de contraintes sur **un seul objet**.

**NE FAIT PAS.** (i) N'établit **pas** la coïncidence au-delà du **un-point perturbatif**
(non-linéaire = `décision ouverte`, WEYL-BD §6). (ii) Ne **ferme pas** D1 : le deux-point `k³`
reste la liberté ouverte (= donnée de Cauchy holographique de [D]). (iii) Ne fusionne **pas**
A3 et A4 *tout court* (l'implication est à sens unique ; ils divergent au deux-point).
(iv) Ne traite **pas** (Def-1) (encart §5). (v) Ne touche **aucune** algèbre ; « le bang gagne »
(P6 B) intact ; C7/A2★ inchangés. **Réduction d'hypothèse ≠ démonstration de la CCC.**

---

## 7. Propagation suggérée `[NON exécutée — à valider/déposer séparément]`

Si la réduction est validée, propagation **additive** (jamais réécriture d'historique) :
- `LC-D3-FRONT-A-SYNTHESE §6` : reformuler le bloc « socles » — A3 listé comme **réductible au
  un-point à A4** (renvoi à cette note), A4 + résidu `k³` portant la charge irréductible.
- `LC-AUDIT-VERDICT §8bis` : bullet daté « passerelle A3⟷D1 : A3-un-point ⟸ A4 (réduction
  cartographiée, un-point perturbatif) ; écart = k³ ; D1 non clos ».
- `LC-A-D1-FACTEUR-CONFORME §5` : ajouter, en candidat-sélecteur, le fait que A3/A4 fixent déjà
  le **un-point** de `g₃` (la prescription D1 ne reste à inventer que pour le **deux-point**).
- `00-INDEX` (carte + changelog) ; `03-GLOSSAIRE` (entrée « passerelle A3⟷D1 / réduction un-point »).
- **Sceau optionnel — FAIT `[exécuté 2026-06-09]`** : `verif_A3_D1_passerelle.py` (EXIT 0,
  **11/11 ASSERTS**), reconfirmation pure sur le mode TT : (a) `⟨g₃⟩=0` par les deux routes
  (A3 par symétrie, A4 par `g₃=0`), (b) emboîtement strict `S_A4⊊S_A3` ⟹ `A4⟹A3-un-point`,
  (c) `⟨g₃g₃⟩~k³` comme divergence A3/A4 — aucune algèbre neuve. *(Spec initiale, conservée
  pour trace :)* sceau léger reconfirmant, sur le mode TT, (a) `⟨g₃⟩=0` par les deux routes,
  (b) `⟨g₃g₃⟩~k³` comme divergence A3/A4 — pure reconfirmation d'emboîtement, aucune algèbre neuve.

---

## 8. Renvois & glossaire

**Renvois.** `LC-D3-WEYL-BUNCHDAVIES` (coïncidence un-point) ; `LC-D3-SPECTRE-K3` (deux-point
k³) ; `LC-A-D1-STABILITE-WEYL` (décomposition fond ⊥ marée) ; `LC-A-D1-FACTEUR-CONFORME`
(verrou D1, liberté = g₃) ; `LC-D-HOLOGRAPHIE-G3` (g₃ = donnée de Cauchy [D]) ;
`LC-D3-FRONT-A-SYNTHESE` (socles A3/A4) ; `LC-D3-CROSSOVER-EINSTEIN3D` (porte (i), Def-1).

**Glossaire à ajouter (`LC-03`).**
- *Passerelle A3 ⟷ D1 / réduction un-point* : A3 (dS-inv) = détermination un-point de la marée
  g₃ ⟹ A4 ⟹ A3-un-point ; écart A3/A4 = deux-point k³.
- *(Def-1) vs (Def-2) de A3* : isotropie dynamique σ=0 (secteur inhomogène, à inventer) vs
  dS-invariance de l'état (un-point scellé via BD).

---

## Appendice — tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`). Ici : réduction `établie (sceau)` au **un-point perturbatif** ;
généralisation `décision ouverte` ; (Def-1) `à inventer` ; D1 non clos.
