---
id: LC-WORK-S2-LECTURE-EQ65
titre: "Note de relecture ciblée (paper-level, SANS sceau) — ÉTAPE 1 de LC-WORK-CADRAGE-S2 §5. Lève l'incertitude (i) du cadrage : la PUISSANCE DE ℓ du coefficient dual de la BRANCHE 2 (« seconde possibilité » de de Haro, fin §4.1 / éq. 90) est ℓ^{−2}, PAS ℓ^{−1}. Source de l'erreur de carte : le `2κ/ℓ` est le COUPLAGE transformé ℓ′/κ′ (∝ℓ^{−1}), lu par mégarde pour le COEFFICIENT du deux-points, qui en est le CARRÉ (∝ℓ^{−2}). Conséquence (révise §2/§3) : sous ℓ→iℓ (κ inerte), branche 2 donne i^{−2}=−1 ⟹ RÉEL NÉGATIF (pas imaginaire), mais le signe vient TOUJOURS de la seule opération ℓ→iℓ ⟹ NON indépendant. Les deux branches retombent sur la SOURCE UNIQUE du signe ⟹ le pronostic de consolidation du cadrage en sort PLUS net, pas affaibli ; l'« échappatoire imaginaire » de branche 2 n'existe pas telle que lue. NE touche NI (ii) (persistance du garde-fou en dS, seul calcul ouvert) NI l'étape 2 (carte S en dS, go/no-go R1), qui restent à faire. Subordonnée à LC-AUDIT-VERDICT §6.4."
codename: LC-RACCORD
type: "note de travail (relecture bibliographique, paper-level) — exécute l'ÉTAPE 1 de LC-WORK-CADRAGE-S2 §5. N'est PAS un chaînon : aucune algèbre scellée, aucun sceau. Ancre un fait de lecture (puissance de ℓ) et sa conséquence logique immédiate, par référence aux numéros d'équation/page de 0808.2054. Subordonnée à LC-AUDIT-VERDICT §6.4."
version: 1.0
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v1.0 : relecture ciblée de 0808.2054 (de Haro), pages 14/16/20, éq. 50-51, 63, 65, 90, après contrôle d'ouverture S2 (versions 8/8 prérequis, ancres OK, sceau verif_D_CT_dual.py re-exécuté EXIT 0 18/18 sur stack 3.12/sympy1.14/numpy2.4). LÈVE l'incertitude (i) du cadrage S2 : coefficient dual de branche 2 ∝ ℓ^{−2} (= (2κ/ℓ)² = 4κ²/ℓ²), confirmé visuellement (le `2κ/ℓ` est le couplage ℓ′/κ′, fin §4.1 p.14 + rappel p.20 ; le coefficient du deux-points éq.90 est ℓ²/κ²=(ℓ/κ)², donc son carré). Conséquence : branche 2 sous ℓ→iℓ → i^{−2}=−1 → réel négatif, non indépendant (signe via ℓ→iℓ au dénominateur). Discipline §6.4 : AUCUN surclassement ; paper-level, aucun sceau ; périmètre {A4 ; A2★ ; N} inchangé ; D1 NON clos ; (A) physique conditionnel au seul A2★ inchangé ; (ii) et étape 2 restent ouvertes ; CCC non démontrée."
statut: "PAPER-LEVEL, SANS SCEAU — fait de lecture ancré (puissance de ℓ de branche 2 = −2) + conséquence logique (révise §2/§3 du cadrage vers une consolidation plus nette). Incertitude (i) du cadrage = LEVÉE. Incertitude (ii) (persistance du garde-fou (−2) sous continuation dS) et étape 2 (carte S en dS, go/no-go R1) = INCHANGÉES, ouvertes. Verdict de S2 NON acquis. Périmètre {A4 ; A2★ ; N} inchangé."
prerequis_kb: [LC-WORK-CADRAGE-S2, LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-CT-ATN, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: ["0808_2054v1.pdf (de Haro, arXiv:0808.2054 ; pages 14, 16, 20 ; éq. 50-51, 63, 65, 67, 90)"]
tags_epistemiques: [décision ouverte, formalisable]
---

# Relecture éq. 65/90 — levée de l'incertitude (i) du cadrage S2

> **Étape 1 de `LC-WORK-CADRAGE-S2 §5`.** Note paper-level. Aucune algèbre scellée, aucun sceau.
> Ancre un **fait de lecture** (puissance de `ℓ`) et sa **conséquence logique immédiate** sur le
> §2/§3 du cadrage. Discipline `§6.4` : « lu » ≠ « scellé » ≠ « seconde route acquise » ≠ « D1 fermé /
> CCC démontrée ». S2 reste en `d=3`. Périmètre `{A4 ; A2★ ; N}` **inchangé**.

---

## 0. Objet et bornes `[paper-level]`

Le cadrage S2 (`§3`) flaggait **deux** incertitudes à lever en ouverture. Cette note lève la **(i)**
seule : *« la puissance de `ℓ` du coefficient dual de branche 2 est compressée depuis la carte P2 — à
relire sur éq. 65 (confirmer/infirmer `∝ℓ^{−1}`) ».* Elle **ne touche pas** :
- **(ii)** persistance de la compensation `(−2)` du garde-fou S1 sous continuation dS — **seul vrai
  calcul ouvert**, seul point pouvant démentir le `§3` (cadrage `§4` étape 3) ;
- **l'étape 2** : carte `S` en dS sur les modes BD, identité de 3e dérivée → `S²` (go/no-go R1).

---

## 1. Localisation correcte du `2κ/ℓ` `[fait de lecture — vérifié visuellement]`

Le `2κ/ℓ` **n'est pas** dans l'éq. 65. Lecture confirmée (pages JPEG 14, 16, 20 de `0808_2054v1.pdf`) :

- **Éq. 65 (p.16)** = fonctionnelle génératrice duale standard :
  `W′[h̃] = W[h] − (ℓ²/2κ²) ∫d³x h̄_{ij} C_{ij}[h̃]`. Coefficient en **`ℓ²/κ²`** (forme standard).
- **Éq. 63 (p.16)** : `⟨T̃_{ij}⟩ = −2 δW̃/δh̃^{ij} = (ℓ²/κ²) C_{ij}[g]` (le garde-fou S1 vit ici).
- **Éq. 90 (p.20)** : `⟨T_{ij}T_{kl}⟩ = (ℓ²/κ²)|p|³ Π_{ijkl} + (ip²/μ) ε_{imn}p_n Π_{jmkl}`.
  Coefficient **parité-pair `= ℓ²/κ²`** (où vit `C_T`) ; terme Cotton **parité-impair `∝ ip²/μ`** (R3).
- Le **`2κ/ℓ`** apparaît **fin §4.1 (p.14)** comme la **« seconde possibilité »** : *on définit
  `B = 2C_{ij}[h̄]` SANS le facteur `ℓ²/κ²` ; alors le **couplage** `ℓ/κ` transforme sous S-dualité
  comme `ℓ′/κ′ = ±2κ/ℓ`* — rappelé en clair après l'éq. 90 (p.20).

---

## 2. Le calcul de la puissance `[verdict (i)]`

Le coefficient du deux-points (parité-pair, éq. 90) est `ℓ²/κ² = (ℓ/κ)²` — le **carré du couplage**.
La branche 2 transforme le **couplage** `ℓ/κ → 2κ/ℓ` (∝ `ℓ^{−1}`). Donc le **coefficient dual** de
branche 2 est son carré :

`(2κ/ℓ)² = 4κ²/ℓ² ∝ ℓ^{−2}`.

> **(i) LEVÉE — la puissance de `ℓ` du coefficient dual de branche 2 est `−2`, PAS `−1`.**
> Origine de l'erreur de carte P2 : le `∝ℓ^{−1}` était le **couplage** `2κ/ℓ` lu pour le
> **coefficient** ; la compression a porté le couplage au lieu de son carré (= le `C̃_T`).

---

## 3. Conséquence logique immédiate — révise §2/§3 du cadrage `[décision ouverte → resserrée]`

Sous continuation `ℓ→iℓ`, `κ` inerte (règle `LC-D-CT-REALITE` : `κ∝√G` ne continue pas) :

| branche | coefficient | sous `ℓ→iℓ` | facteur | issue |
|---|---|---|---|---|
| 1 (même forme, éq. 90 ; `κ/ℓ` inerte) | `ℓ²/κ²` | `(iℓ)²/κ² = −ℓ²/κ²` | `i² = −1` | **réel négatif** ; **non indépendant** |
| 2 (corrigée, `∝ℓ^{−2}`) | `4κ²/ℓ²` | `4κ²/(iℓ)² = −4κ²/ℓ²` | `i^{−2} = −1` | **réel négatif** (PAS imaginaire) ; **non indépendant** |

- **Branche 2 n'est pas imaginaire** (corrige le `§2` du cadrage, qui déduisait `−i` de `ℓ^{−1}`).
- **Branche 2 n'est pas indépendante** : le signe vient **toujours** de la seule opération `ℓ→iℓ`
  (ici au dénominateur ; `i^{−2}` au lieu de `i²`, tous deux `= −1`). Critère d'indépendance du
  cadrage `§1` (« opération **différente** de `ℓ²→i²ℓ²` ») : **non satisfait** — c'est la **même**
  continuation `ℓ→iℓ`, à une puissance différente, pas une seconde source de signe.

**Effet sur le pronostic `§3` du cadrage : il en sort PLUS net, pas affaibli.** L'« échappatoire
imaginaire » que le cadrage prêtait à la branche 2 **n'existe pas telle que lue**. Les **deux**
branches retombent sur la **source unique du signe** (`ℓ→iℓ`). Il n'y a de seconde route
**indépendante** dans **aucune** des deux branches ⟹ l'issue pronostiquée **consolidation**
(verrouiller le signe sur une source unique, durcir le garde-fou ; **pas** réduire le compte) est
**renforcée** au niveau lecture.

**Argument physique convergent (de Haro, p.14) :** la branche 2 (« inverser la constante de Newton »)
**sort du régime de supergravité** et n'est fiable que si la solution originale est exacte — caveat
supplémentaire contre la branche 2 comme route propre.

**Cohérence avec le sceau `REALITE` :** aucune contradiction. `C_T(d=3) = −N/(32π²)` (réel négatif via
l'électrique `ℓ²→i²ℓ²`) est **reproduit** par branche 1 (même opération) et **retrouvé** par branche 2
(même source, dénominateur). La contrainte « source unique du signe » du `§3` tient.

---

## 4. Ce qui reste ouvert `[discipline §6.4 — NON acquis]`

- **(ii) INCHANGÉE, OUVERTE** : la compensation `(−2)` du garde-fou S1 (`C̃_T=+C_T` en AdS via
  `⟨T̃⟩=−2δW̃/δh̃`) survit-elle à la continuation dS ? **Seul vrai calcul ouvert** ; **seul point
  pouvant démentir** le `§3`. Si (ii) tombe d'une manière non prévue, une route pourrait exister :
  l'espace **n'est pas** clos par décret. La présente note ne la touche pas.
- **Étape 2 NON faite** : carte `S` en dS sur les modes BD (`(1−ikη)e^{ikη}`,
  `LC-D3-WEYL-BUNCHDAVIES`), identité de 3e dérivée analogue à éq. 44 → `S²` en dS. **Go/no-go R1** :
  si `S` ne referme pas en dS ⟹ lead `hors de portée` (verdict honnête). Petit sceau prévu
  `verif_D_CT_dual_dS.py`.
- **Verdict de S2 NON acquis.** Périmètre `{A4 ; A2★ ; N}` **inchangé** ; D1 NON clos ; (A) physique
  conditionnel au seul A2★ inchangé ; « le bang gagne » (P6 B) intact ; CCC non démontrée.

---

## Appendice — état de l'ordre d'exécution (cadrage §5)

1. ~~Relecture éq. 65/90 → lève (i)~~ **FAIT (cette note)** : coefficient branche 2 `∝ℓ^{−2}`.
2. Carte `S` en dS (go/no-go R1) — **prochaine**, petit sceau `verif_D_CT_dual_dS.py`.
3. Persistance du garde-fou sous continuation → lève (ii) — **ouvert** (le point qui peut démentir).
4. Trancher R4 au crossover (questions 1 et 2 fusionnées par §3) — après 2–3.
5. Question 3 (Dirichlet vs duale = raccordement) — seulement si 1–4 livrent une route propre.
