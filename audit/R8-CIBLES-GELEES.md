---
id: LC-AUDIT-R8-CIBLES-GELEES
titre: "Gel de cibles — lot R-8 (Silo R) : A2★ mésoscopique (modèle Gauss-Kuzmin, non-cascade) + oracle P6. Cibles figées AVANT toute redérivation, depuis les FRONT-MATTERS SEULS."
codename: LC-RACCORD
type: "document de gel — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-22
lot: R-8
session: S5
sources_du_gel: [kb/LC-D3-INTERAEON-P6.md (front-matter), kb/LC-D3-C7B-VERDICT-A2.md (front-matter), kb/LC-D-A2-NUMERIQUE.md (front-matter)]
corps_non_lus: "Les corps des trois têtes n'ont PAS été ouverts au moment du gel. Seuls les blocs YAML l'ont été."
---

# 0. Déclaration de révélation (discipline amendée post-CSE, note S3 §2)

Les front-matters de R-8 sont du **gabarit LOURD**. Ils portent, sans que
le corps soit ouvert :

- des **valeurs d'arrivée** : `⟨C_F⟩_GK = 7.18` · `κ = 0.8117` ·
  `s* = 1` vs `s_phys = 0` · oracle validé à `0.8 %` · `max 0.377` ·
  `EXIT 0/22` · sha8 `76e9257c` ;
- le **mécanisme** lui-même : dichotomie `non-cascade ⟺ ρ = 0`, loi de
  cascade `n_s ~ (1+ρ)^{N_b}` de taux `ln(1+ρ)`, mesure de Gauss-Kuzmin
  comme statistique d'ères, bornitude des exposants de Kasner, seuil
  dérivé de la mesure, structure du firewall (m1/m2/m3 + c1/c2).

**PLAFOND DE GRADE ANNONCÉ AU GEL : REPRODUIT-SOUS-RÉSERVE (E-2).**
E-1 est **exclu d'avance** pour ce lot : cibles ET mécanisme révélés.
Aucune lecture ultérieure ne pourra relever ce plafond.

# 1. Cibles gelées

| # | Cible | Statut attendu |
|---|---|---|
| **Q1** | Mesure invariante de la carte de Gauss `x ↦ {1/x}` : densité `p(x) = 1/(ln2·(1+x))` sur (0,1) | DÉRIVABLE |
| **Q2** | Transport en variable d'ère `u = 1/x ∈ (1,∞)` : `p(u) = 1/(ln2·u(u+1))` ; queue `~ 1/(ln2·u²)` | DÉRIVABLE |
| **Q3** | Seuil de convergence DÉRIVÉ DE LA MESURE : `⟨u^s⟩_GK < ∞ ⟺ s < 1` ⟹ **s\* = 1** ; `s_phys = 0 < s*` ⟹ « OC adressé », robuste au seuil | DÉRIVABLE |
| **Q4** | Exposants de Kasner en paramétrisation d'ère : `Σp = Σp² = 1` identiquement, et **bornés ∀u ≥ 1** | DÉRIVABLE |
| **Q5** | Dichotomie **non-cascade ⟺ ρ = 0** ; `ρ > 0 ⟹ n_s ~ (1+ρ)^{N_b}`, taux `= ln(1+ρ)` EXACT et **monotone** ; `ρ = 0 ⟹` production additive ⟹ `n_s` sous-exponentiel | DÉRIVABLE |
| **Q6** | `⟨C_F⟩_GK = 7.18` FINI | **FINITUDE** dérivable (Q3+Q4) ; **VALEUR 7.18** non dérivable au gel : le noyau `C_F(u)` est ABSENT des front-matters ⟹ import, ou réconciliation §2.0 post-dérivation (précédent R-2/Q6) |
| **Q7** | `ρ = 0` est un **input physique motivé** (mécanisme Garfinkle), NON dérivé d'un théorème générique 3D ⟹ soutien CONDITIONNEL à l'additivité | CONSIGNATION (verdict, pas algèbre) |
| **Q8** | Verdict C7-b : A2 **n'est pas formalisable** comme théorème depuis Garfinkle gr-qc/0312117 (« work in progress », résolution hors régime convergent) ⟹ aucune borne sous-exponentielle rigoureuse sur `n_s^gen` | CONSIGNATION (source externe) |
| **Q9** | Sceaux du lot : `verif_A2_numerique.py` EXIT 0, 22 assertions, sha8 `76e9257c`, firewall m1/m2/m3 + c1/c2 ; `verif_D3_P6_specB_oracle.py` ; `verif_D3_C7b_A2_reduction.py` | REJEU (§4) |
| **Q10** | P6 : oracle GK validé à `0.8 %` ; bang générique NON contractant `P(ε_out < κ·ε_in) = 0` ; `κ = 0.8117` (radiation-era) | Noyau `ε` ABSENT des front-matters ⟹ NON redérivable en aveugle ici ; rejeu + consignation |

# 2. Tolérances déclarées AVANT comparaison

- Identités algébriques exactes (Q1, Q2, Q4, Q5) : **exactitude symbolique**, tolérance nulle.
- Quadratures et seuils (Q3) : `rtol = 1e-9` sur les intégrales convergentes ; la divergence est établie par **critère analytique**, pas par une valeur numérique.
- Q6 (valeur 7.18) : aucune tolérance déclarée — la cible n'est pas atteignable au gel. Tout accord ultérieur serait une réconciliation, jamais un PASS.

# 3. Anti-fit

Aucun coefficient, aucune convention, aucune tolérance ne sera modifié
après lecture d'un écart. Un jeu de conventions manqué se consigne TEL
QUEL (précédent R-2/Q6). Les cibles ci-dessus sont figées par le sha256
de ce fichier, calculé avant l'écriture de l'instrument.

*§6.4 — ce gel n'établit rien. { A4 ; A2★ ; N } INCHANGÉ · A2★ ni prouvée ni réfutée · C7 non levée · CCC non démontrée NI réfutée.*
