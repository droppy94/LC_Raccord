---
id: LC-WORK-AMENDEMENT-R7-A4-QW-TYPEI-CORR
codename: LC-RACCORD
titre: "Amendement R-7 (gel de spec de CORRECTION) — retrait d'un sur-grade dans le verdict scellé LC-D-A4-QW v0.2 : l'assert [05] affirme le résidu électrique 𝓔 « ≠0 sur TOUTE la famille » type-I vide (jambe CSE-5 : « g₃=−4q_i UNIVERSEL »). FAUX : de Sitter (a_i=e^{Ht}) EST le membre isotrope vide (ρ=0, shear=0, g₃=0), atteint comme limite shear→0 (time-shift t→t+c : q_i^eff=q_i·e^{−3c}, |𝓔|²∝e^{−6c}→0). Le point q=0 de la paramétrisation (a_i=sinh^{1/3}(3t)) est isotrope mais NON vide (ρ=3/sinh²(3t)>0) — mauvais point. Cet amendement GÈLE la spec du successeur [05'] et son critère d'acceptation AVANT construction du sceau successeur et AVANT re-audit incognito (anti-fit auditable). INVARIANT DUR : W2 (résidu-cassant, GÉNÉRIQUE) est PRÉSERVÉ — seul le mot « universel/toute la famille » tombe ; A4 non réfuté ; {A4 ; A2★ ; N} INCHANGÉ ; §6.4 terminal."
type: "amendement R-7 (gel de spec de correction). N'embarque PAS son gel SHA (R-36 : consigné hors-fichier par l'opérateur). Ne modifie AUCUN objet scellé : verif_A4_QW.py (sha a4637a2c) reste FIGÉ (§10, pas de mutation en place)."
statut: "PROPOSÉ au gel. Étape 1/5 de la piste (A) (conflit #1). Étapes 2-5 (sceau successeur, patch additif §8, prompt incognito CSE-5, propagation) GELÉES par ce freeze — aucune non engagée avant gel SHA + GO opérateur."
version: 1.0
langue: fr
date: 2026-07-13
amende: LC-D-A4-QW (v0.2, tête scellée CSE-5-soldée) — assert porteur [05] et lecture de [F1] qui l'alimente
ne_modifie_pas: [verif_A4_QW.py (sha a4637a2c — FIGÉ), cadrage 91a50391, amendement b60baef0, espace-verdict {W1/W2/W3}]
prerequis_kb: [LC-D-A4-QW, LC-WORK-CADRAGE-A4-QW, LC-WORK-AMENDEMENT-R7-A4-QW-PHASE0, LC-D-IRREDUCTIBILITE-MOYENS]
tags: [amendement, R-7, R-36, R-54, A4, Q-W, W2, type-I, de-Sitter, sur-grade, CSE-5-repasse, §10, §6.4, anti-fit]
---

# Amendement R-7 — correction du sur-grade type-I dans LC-D-A4-QW (spec gelée du successeur [05'])

> **Ce qui est gelé** (AVANT toute construction) : (i) l'énoncé exact retiré ; (ii) l'énoncé
> corrigé [05'] et son critère d'acceptation en code ; (iii) les invariants préservés ; (iv) le
> plan de piste. **R-36** : le gel SHA de cet amendement est consigné HORS-FICHIER (opérateur).
> **§10** : le sceau audité `a4637a2c` n'est PAS muté en place — un successeur porte [05'] sous
> nouveau sha. **§6.4** : correction d'un sur-grade, AUCUNE réduction, AUCUN renversement.

## 1. Objet corrigé (verbatim scellé, R-54 lu sur mount)

Sceau `verif_A4_QW.py` (sha `a4637a2c`), assert **[05]** :

    # [05] type I vide : g₃ = 0 IMPOSSIBLE (Σq²=2/3 exclut q=0) ⟹ résidu 𝓔 sur TOUTE la famille
    check('[05] type I vide : {q=0} ∩ {contrainte} = ∅ ⟹ lim 𝓔 = (3/2H)g₃ ≠ 0 sur toute la famille', …)

Tête `LC-D-A4-QW` §2 (table type I) : « ≠0 sur TOUTE la famille » ; §8 (jambe CSE-5, auditeur) :
« g₃ = diag(−4q_i) **universel** (pas seulement générique) ». C'est le **sur-grade** : la clause
d'universalité/« toute la famille ».

Lecture solidaire : l'assert **[F1]** (« q=0 imposé ⟹ contrainte du vide violée −1/3≠0 ») reste
**correct comme firewall anti-circularité** (imposer q=0 en ENTRÉE bas-Weyl viole bien la
contrainte), mais NE justifie PAS la conclusion d'universalité de [05] : il exclut le point q=0 de
la paramétrisation, non le membre isotrope vide pertinent (de Sitter, §2).

## 2. Constat (pré-vérification pilote — SymPy, ground-truth ; NON adjudicateur)

Re-dérivé en autonomie (le pilote signale, il n'adjuge pas ; l'adjudication = CSE-5 incognito §5) :

- **de Sitter `a_i=e^{Ht}`** : vide+Λ exact (`ρ=0`), isotrope (`shear=0`) ⟹ `g₃=0`, `lim 𝓔 = 0`.
  C'est LE membre isotrope vide de la famille type-I.
- **Point `q=0`** de `a_i=sinh^{1/3}(3t)·tanh^{q_i}(3t/2)` : isotrope mais `ρ=3/sinh²(3t)>0` —
  **NON vide** (FLRW à source). L'exclusion `{q=0}∩{Σq²=2/3}=∅` de [05] écarte donc le MAUVAIS
  point isotrope et ne teste jamais de Sitter.
- **Amplitude de shear LIBRE** : `t→t+c` renormalise `q_i → q_i^eff = q_i·e^{−3c}` ; la contrainte
  `Σq²=2/3` (re-dérivée : `rho=0 ⟺ q1²+q1q2+q2²=1/3`) ne fixe la magnitude qu'en UNE tranche.
  `|𝓔|² ∝ e^{−6c}` balaie `(0,∞)` ; de Sitter = limite `c→+∞` (`shear→0`, `g₃→0`, `𝓔→0`).
- **Résidu rigide ∝ shear** : `𝓔 = (3/2H)·diag(−4q_i^eff)` ⟹ non nul ssi `shear≠0`.

## 3. Spec gelée du successeur [05'] (cible EXACTE + critère d'acceptation)

L'assert successeur **[05']** doit vérifier EN CODE, sur représentation indépendante admise :

- (a) de Sitter `a_i=e^{Ht}` est vide+Λ (`Einstein+Λ≡0`, `ρ=0`) et isotrope (`shear=0`) ⟹ `𝓔=0` ;
- (b) `q=0` (`a_i=sinh^{1/3}(3t)`) est isotrope mais `ρ>0` (NON vide) — ce n'est PAS de Sitter ;
- (c) sous `t→t+c` : `q_i^eff=q_i·e^{−3c}` et `lim_{c→+∞} 𝓔(q_i^eff)=0` ;
- (d) `𝓔 = (3/2H)·diag(−4q_i^eff) ≠ 0` pour tout `shear≠0` (toute la famille ANISOTROPE).

**Énoncé [05'] gelé** (à substituer, successeur seul) :

    [05'] type I vide : 𝓔 = (3/2H)·diag(−4q_i^eff) est NON NUL sur toute la famille ANISOTROPE
          (shear≠0) et NUL au SEUL point de Sitter (limite shear→0, c→+∞) ; le point q=0
          (a_i=sinh^{1/3}(3t)) est isotrope mais NON vide (ρ=3/sinh²(3t)>0), donc pas de Sitter.

**Critère d'acceptation** : successeur EXIT 0 avec (a)-(d) vérifiés ; assert d'universalité SUPPRIMÉ
(aucun `sur toute la famille`/`universel` sans la carve-out de Sitter). Toute autre modification de
la logique porteuse (taux 3, `g₃=−4q_i`, secteur magnétique Nil, indicielle {0,3}) = HORS SCOPE de
cet amendement (inchangée).

## 4. Invariants préservés (bornes dures)

- **W2 (résidu-cassant, GÉNÉRIQUE) INCHANGÉ** : le résidu survit sur toute la famille anisotrope
  (mesure pleine du secteur anisotrope) ; le chaînon `no-hair ⟹ Weyl-rescalé-propre` casse
  toujours. Le retrait ne concerne QUE la clause d'universalité (le point de Sitter, `shear=0`).
- **§6.4** : `établi (algèbre)` ≠ physique ; A4 NON réfuté (statut de postulat toujours RENFORCÉ,
  concordant SFG-3) ; `{A4 ; A2★ ; N}` INCHANGÉ ; D1 non clos ; N ≡Λ ; O₂ non construit ; β T-b ;
  CCC ni démontrée NI réfutée.
- **Secteur magnétique** (Cotton[Nil]≠0 au type II) et **types V/II** : NON touchés ; W2 tenait
  déjà sur type I (électrique) + Nil (magnétique) — il tient a fortiori.

## 5. Plan de piste (étapes 2-5, GELÉES par ce freeze)

2. **Sceau successeur** implémentant [05'] au spec §3 (nouveau sha ; `a4637a2c` INTACT).
   `.py` 6→7 ⟹ **§0-full OBLIGATOIRE** au lot de dépôt.
3. **Patch additif** `LC-D-A4-QW` §8 : consigner la réserve d'intégrité type-I (à côté de [10]
   semi-vacant), pointeurs vers cet amendement + successeur ; sceau frozen inchangé ; suppressions
   ⊆ {version, maj, statut} ; zéro ligne de corps perdue ; ancres count==1 ; diff après.
4. **Prompt incognito CSE-5** (souverain, Mode B, blind, PACKAGE-SHA) : re-dériver (a)-(d) en
   autonomie contre la spec §3 gelée. Pilote DISQUALIFIÉ pour adjuger.
5. **Propagation** (CSE-6 / IDX / GLO / AUD / manifeste) SEULEMENT après concordance incognito.

## 6. Anti-fit (transparence, R-7)

Auditable en **contenu** : spec §3 gelée AVANT sceau successeur + AVANT re-audit ; sceau audité
`a4637a2c` non muté (§10). Chronologie : la pré-vérification pilote (SymPy §2) PRÉCÈDE ce gel
(nécessaire pour établir que le conflit est réel) — elle SIGNALE, l'adjudication reste l'incognito
CSE-5 contre la spec gelée. Gel SHA hors-fichier (R-36), limite standard.

## 7. Méta — second point de calibration (consigner tel quel, non load-bearing)

Le sur-grade générique→**universel** a été introduit/ratifié par l'**audit froid LLM (CSE-5)**
(§8 tête : « universel (pas seulement générique) »), c.-à-d. la couche LLM a poussé dans le sens
du SUR-GRADING — le mode de défaillance même que la discipline prétend intercepter. La correction
vient d'une lecture indépendante + re-dérivation. C'est un **deuxième point de données** (après
[10]) montrant que la couche humaine/indépendante mord là où la couche LLM sur-grade. À consigner
au §8 comme tel, ni plus ni moins (ne renforce ni ne réduit aucun compte).

---

*Fin de LC-WORK-AMENDEMENT-R7-A4-QW-TYPEI-CORR v1.0. PROPOSÉ au gel. Étapes 2-5 gelées.
R-36 : gel SHA hors-fichier. §10 : sceau a4637a2c INTACT. §6.4 : W2 préservé, aucune réduction.*
