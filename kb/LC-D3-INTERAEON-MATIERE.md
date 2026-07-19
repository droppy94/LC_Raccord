---
id: LC-D3-INTERAEON-MATIERE
titre: "Front (a) / P7 — brancher la matière CCC (σ̌, φ) sur la carte κ : σ̌ est la SEULE pièce capable de retourner κ, et seulement dans la conjonction (signe opposé à ³S)∧(redshift lent) ; φ est isotrope (borné) ; le verdict se réduit à DEUX paramètres de Tod"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, isotropisation, inter-eon, bianchi-IX, P7, stress-anisotrope, sigma-check, phantom, tod, kappa]
type: chaînon (exécution du chantier P7 de LC-WORK-REPRISE-INTERAEON §4.2 ; raffine LC-D3-INTERAEON-KAPPA)
statut: résultat d'ordre dominant établi (réduction algébrique du sort de κ à 2 paramètres ; contrainte conservée 1e-14 ; φ isotrope) / le signe de σ̌ et l'exposant de redshift p restent décision ouverte (Tod 33 à re-vérifier)
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (met à jour LC-D3-INTERAEON-KAPPA §5 ; LC-02 ; LC-AUDIT-VERDICT ; glossaire)
fichier_compagnon: [verif_D3_interaeon_matiere.py, verif_D3_interaeon_kappa.py]
prerequis_kb: [LC-D3-INTERAEON-KAPPA, LC-WORK-REPRISE-INTERAEON, LC-A-D1-BIANCHI, LC-D3-CROSSOVER-ANISOTROPE, LC-WORK-CADRAGE-INTERAEON, LC-AUDIT-VERDICT]
renvois: [LC-D3-INTERAEON-KAPPA, LC-WORK-REPRISE-INTERAEON, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-D3-CROSSOVER-ANISOTROPE, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] / front (a) — A3 pivot ; P7 teste si la matière CCC tue l'attraction dynamique"
  - "[D3] hypothèse de Weyl — σ̌ = −4·(Ricci sans-trace de 𝓘), la marée future est le sujet"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Interaeon·Matière — P7 : la matière CCC sur la carte κ

> **Cible.** `LC-D3-INTERAEON-KAPPA` a établi (ordre dominant) que la carte d'anisotropie
> inter-éon est contractante, `ε_{n+1}=κ ε_n`, `κ≈0.81<1`, mais **avec P7 (matière CCC exacte)
> EXCLU**. Sa subtilité §5.2 désignait le **stress anisotrope σ̌** comme « le candidat le plus
> sérieux pour faire κ≥1 — à tester en priorité ». Ce chaînon exécute ce test (chantier §4.2
> de `LC-WORK-REPRISE-INTERAEON`).
>
> **Verdict (ordre dominant, établi ; sceau `verif_D3_interaeon_matiere.py`).** Branchée sur
> le noyau (Bianchi IX + radiation + Λ, conditions GO, `σ(0)=0` de Tod), la matière CCC donne :
> **(1)** Le **champ phantom φ** (Tod éq. 13) est un scalaire **homogène** ⟹ stress **isotrope**
> ⟹ il **ne source pas** le cisaillement : il ne module `κ` que par l'histoire d'expansion
> (`ρ_φ`), donc d'un montant **borné par le balayage `Λ/ρ`** déjà scellé (`κ∈[0.70,0.94]`).
> **φ ne peut pas, seul, faire `κ≥1`.** **(2)** Le **stress anisotrope σ̌** (Tod éq. 33,
> `σ̌=−4·³S` de la forme de bang — ancré sur `LC-A-D1-BIANCHI` [B2], `|σ̌|²=128ε²`) est **la
> seule pièce capable de retourner `κ`**. Avec sa back-réaction `σ:Π` (contrainte conservée
> `1e-14` ⟹ trajectoires d'Einstein propres), le sort de `κ` se réduit à **deux paramètres** :
> le **signe** de σ̌ relativement à ³S, et la **loi de redshift** `p` du stress. **`κ≥1`
> (mort de l'attraction) n'arrive QUE dans la conjonction (signe opposé) ∧ (redshift lent
> `p≲2`)** ; signe renforçant ⟹ `κ` baisse (0.24) ; redshift radiation (`p=4`) ⟹ même le signe
> opposé garde `κ≈0.95<1`. **La question décisive du front (a) est donc ISOLÉE en deux nombres
> précis de Tod, bornée, mais non tranchée** (signe de Tod 33 dans le repère du cisaillement +
> scaling de σ̌ à re-vérifier sur le papier). `[ordre dominant ; signe & p : décision ouverte]`

---

## 0. Rôle et garde-fou

Ce chaînon **raffine** `LC-D3-INTERAEON-KAPPA` en levant l'exclusion P7 pour les deux pièces
`formalisables` (σ̌, φ) ; la « DM » de Penrose (terme de trace) reste `à inventer` et en
réserve. **Garde-fou `[à ne pas perdre]`** : ce qui est `établi` ici est **algébrique** — la
*réduction* du sort de κ à deux paramètres, le rôle isotrope de φ, la conservation de la
contrainte. Le **signe physique** de σ̌ et l'**exposant `p`** ne sont **pas** déterminés par ce
calcul ; ils exigent une lecture fine de Tod 33 (convention de signe dans le repère du
cisaillement) et du scaling de σ̌. Discipline d'audit (`LC-AUDIT-VERDICT` §6.4) : *un `établi` =
« l'algèbre est correcte », jamais « la physique de la CCC est établie ».*

---

## 1. Le dispositif `[établi — algèbre]`

**Noyau inchangé** (`verif_D3_interaeon_kappa.py`, reproduit en contrôle : `κ_nu=0.812` ✓).
**Ajouts P7** (compagnon `verif_D3_interaeon_matiere.py`) :

- **Stress anisotrope** dans l'équation du cisaillement :
  $$\frac{d\sigma_i}{dN} = -3\sigma_i - \frac{{}^3S_i}{H} + \frac{\Pi_i}{H},\qquad
    \Pi_i(N) = c_\Pi\,\check\sigma_i(\varepsilon_n)\,e^{-pN},$$
  avec le **seed fixé par Tod (pas de coupling libre)** : `σ̌_i = −4·³S_i(forme de bang)`
  (éq. 33), auto-vérifié `|σ̌|²=128ε²+O(ε⁴)` contre `LC-A-D1-BIANCHI` [B2]. `c_Π=±1` teste le
  **signe** ; `p` la **loi de redshift**.
- **Back-réaction** (identité de Bianchi contractée, Ellis) : `dρ/dN = −4ρ − (σ_iΠ_i)/H`.
  **Conséquence cruciale** : avec ce terme, la contrainte `3H²=ρ+Λ+σ²−½³R` est conservée à
  `4·10⁻¹⁴` (sans lui elle dérive à `6·10⁻³` : l'insertion ad hoc de σ̌ n'était pas une
  solution d'Einstein — *le terme de travail est obligatoire*).
- **Champ phantom φ** (Tod éq. 13, `φ̈+2H²φ=⅙sφ³`) : porté en e-fold, contribue `ρ_φ=½φ̇²+V`
  à Friedmann. **Scalaire homogène ⟹ pas de stress anisotrope.**

---

## 2. Résultat (1) : φ est isotrope — effet borné `[établi]`

Un champ scalaire homogène n'a **aucune part sans-trace** : il **ne peut pas** sourcer le
cisaillement. Son seul levier sur `κ` est `ρ_φ`, qui modifie l'histoire d'expansion (le rapport
effectif `Λ/ρ`). Or `LC-D3-INTERAEON-KAPPA` §3 a **déjà scellé** que `κ` varie dans `[0.70,0.94]`
sur tout le balayage `Λ/ρ`. Le sceau confirme : `κ(φ)` reste dans cette fourchette
(`0.59–0.78` pour les amplitudes testées — *dans* l'enveloppe). **φ ne peut pas faire `κ≥1`.**
La « DM » de Penrose (trace, `O(Ť⁻¹)`) est `à inventer`, sous-dominante, en réserve.

$$\boxed{\ \varphi \text{ (Tod 13) : stress isotrope} \Rightarrow \text{module } \kappa \text{ via l'histoire seulement} \Rightarrow \text{borné par } [0.70,0.94].\ }$$

---

## 3. Résultat (2) : σ̌ est le seul levier — réduction à deux paramètres `[établi / décision ouverte]`

**Structure-clé.** `σ̌ = −4·³S(forme de bang)` : le stress anisotrope **EST** la source de
courbure elle-même (à `−4` près). Le sort de `κ` dépend donc de :

| paramètre | effet sur `κ` (ε≈0.81 nu) | lecture |
|---|---|---|
| **signe** `c_Π=+1` (renforce −³S/H), `p=2` | `0.81 → 0.24` | rappel **renforcé** ; mais **non-linéaire** (lin~0.6, dépassement, `κ` non-monotone en amplitude) |
| **signe** `c_Π=−1` (oppose −³S/H), `p=2` | `0.81 → 1.57` | rappel **affaibli** ⟹ **BASCULE >1** (carte reste linéaire) |
| **redshift** `p=4` (radiation), `c_Π=−1` | `→ 0.95` | **NE bascule PAS** : reste `<1` |
| **redshift** `p=0` (gelé), tout signe | `≫1` | **non physique** (Π ne décroît jamais) — à écarter |

$$\boxed{\ \kappa\ge 1 \iff (\text{signe de } \check\sigma \text{ oppose } {}^3S)\ \wedge\ (\text{redshift lent } p\lesssim 2).\ }$$

**Lecture.** L'attraction inter-éon (κ<1) **survit génériquement** à la matière CCC : le seul
moyen de la tuer est la **conjonction** d'un signe opposé *et* d'un redshift lent. Avec un
redshift de type radiation (`p=4`, naturel pour un stress anisotrope de fluide radiatif), même
le signe opposé garde `κ<1`. **Le verdict de l'issue faible vs attraction se réduit donc à deux
nombres de Tod, désormais localisés et bornés** — mais **non tranchés** par le présent calcul.

---

## 4. Ce qui closerait le point `[décision ouverte]`

1. **Le signe de σ̌** relativement à ³S dans l'équation du cisaillement : re-lire Tod éq. 33
   dans le repère orthonormé du cisaillement (convention de signe `σ̌_ij` vs `R^(â)`-sans-trace).
2. **L'exposant `p`** : dériver proprement le redshift du stress anisotrope (fluide radiatif
   free-streaming `p=4` ? marée gelée `p=2` ?) — décide si la bascule est même possible.
3. **La back-réaction** est obligatoire (sinon contrainte cassée) : tout traitement futur doit
   l'inclure. La fermeture matière complète (la « DM » de trace de Penrose, conservée) reste
   `à inventer` (Tod s'arrête ; Markwell-Stevens : part sans-trace sans interprétation physique).

---

## 5. Format de chaînon standard

- **Zone ambiguë.** « `κ<1` est `ordre dominant` (P7 exclu). Le stress anisotrope σ̌, qui EST
  ~ l'anisotropie de 𝓘, retourne-t-il `κ` (issue faible renforcée) ou non ? »
- **Hypothèse testée.** Brancher σ̌ (Tod 33) + φ (Tod 13) sur le noyau change le signe/magnitude
  de `κ`.
- **Outil.** Noyau Bianchi IX + radiation + Λ ; seed σ̌=−4³S ancré [B2] ; back-réaction σ:Π
  (Ellis) ; φ en e-fold (Tod 13). Sceau `verif_D3_interaeon_matiere.py` (contrainte `1e-14`).
- **Critère de réfutation.** Si σ̌ faisait `κ≥1` de manière **robuste** (tout signe, tout `p`),
  l'attraction inter-éon serait tuée par la matière (issue faible pure). — **Non réalisé** :
  `κ≥1` exige la conjonction (signe opposé)∧(redshift lent) ; sinon `κ<1` persiste.
- **Verdict.** **φ borné (isotrope) ; σ̌ = seul levier ; sort de κ réduit à 2 paramètres de
  Tod, bornés, non tranchés.** L'attraction `κ<1` survit génériquement ; sa mort exige une
  conjonction précise. `[ordre dominant établi ; signe & p : décision ouverte]`

---

## 6. Renvois, glossaire, références

**Renvois.** **Met à jour `LC-D3-INTERAEON-KAPPA` §5** (P7 partiellement levé : φ borné, σ̌
réduit à 2 paramètres) ; `LC-WORK-REPRISE-INTERAEON` §4.2 (chantier exécuté), §5.2 (subtilité
σ̌ tranchée en « réduction à 2 paramètres ») ; `LC-A-D1-BIANCHI` [B2] (seed σ̌, `|σ̌|²=128ε²`) ;
`LC-A-D1-FACTEUR-CONFORME` (φ, prescription) ; `LC-D3-CROSSOVER-ANISOTROPE` (issue faible) ;
`LC-AUDIT-VERDICT` §6.4. Chantiers **restants** du front (a) : P6 (bang/Mixmaster), itération
`∏κ_n` (couplage à `verif_D1_atlas.py`).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Stress anisotrope σ̌ (Tod 33)* : `σ̌=−4·(Ricci sans-trace de 𝓘)` ; branché au cisaillement,
  c'est le seul levier capable de retourner `κ` ; effet contrôlé par (signe, redshift `p`).
- *Back-réaction σ:Π* : terme `−σ_iΠ_i/H` dans la conservation ; **obligatoire** pour conserver
  la contrainte (sinon dérive `1e-3`).
- *Rôle isotrope de φ* : un scalaire homogène ne source pas le cisaillement ; il ne module `κ`
  que via l'histoire d'expansion, dans l'enveloppe `[0.70,0.94]`.

**Références (`LC-04`).**
- **K. P. Tod**, arXiv:1309.7248 (2015) — éq. 13 (φ), 24 (`σ(0)=0`), 27 (`ρ∝Ť⁻²`), 33 (σ̌).
  **Signe de 33 et scaling de σ̌ à re-vérifier.**
- **G. F. R. Ellis** & coll. — back-réaction cisaillement/stress anisotrope (conservation).
- **R. M. Wald**, PRD 28 (1983) ; **Wainwright-Ellis** (1997) ; **Milnor** Adv.Math.21 (1976).
- **Markwell & Stevens**, GRG 55, 93 (2023) — part sans-trace « without physical interpretation ».

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : `établi` porte sur l'ALGÈBRE (réduction à 2 paramètres,
contrainte conservée, φ isotrope), à l'ORDRE DOMINANT ; le signe de σ̌ et l'exposant `p`
restent `décision ouverte`. Jamais « la physique de la CCC est établie ».*
