---
id: NOTE-BORD-EON-109-ACTE-GREFFE-IR-d2
numero: 109
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-d'')
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 872b9b271820fb6320d28a65372f41733f2c9d4489f881c6bee3880c19d51613 (conservee)"
greffe: "IR-d''' entee le 2026-10-11 par NOTE-BORD-EON-114 (corrections de l'audit NOTE-113, AU-V3 partiel)"
nature: "acte d'entee de greffes (aucun calcul, aucune lecture nouvelle, pas de gel requis)"
depend: [NOTE-BORD-EON-104-IR-a-LECTURE-REF21, NOTE-BORD-EON-106-AUDIT-OP-IR-CONCORDANCE, NOTE-BORD-EON-108-IR-g-EXECUTION]
---

# NOTE-109 : acte d'entee de la greffe IR-d'' sur NOTE-102, NOTE-104, NOTE-106

## 1. Regle suivie
Les versions v1 scellees sont **conservees intactes** (empreintes inchangees). Chaque note recoit une version v2 qui porte : en-tete `version: 2`, `remplace` (empreinte v1), `greffe` ; un encadre « Greffe IR-d'' » sous le titre listant les corrections et leur origine ; des marques `[corrige IR-d'']` ou `[precise IR-d'']` aux endroits touches. Le texte v1 n'est pas efface ailleurs.

## 2. Table des greffes

| Note | v1 (sha256) | v2 (sha256) | Corrections | Origine |
|---|---|---|---|---|
| NOTE-102 | ea774ca54e2e5c03… | 4bc0b72978987e46… | residu d'ordre β² ; operateur tranche par [21], qualification reduite a u₀ ≪ k ; critere d'etat Q_tf ; sorties tautologiques ou codees en dur etiquetees ; terme s² ln s reel mais ligne incomplete ; robustesse (seuls les logs) ; branche electrique ∝ 1/I² ; coincidence uniforme formelle | NOTE-104, NOTE-106, NOTE-108 |
| NOTE-104 | 95df64c4be1837b0… | 47b25752fb16efdb… | D1 reformule (aucun terme en H² dans l'operateur, hypotheses nommees, contre-exemple PTW non lu) ; L3 limite a R³ ; nuances L1, L4, L5 ; D3 precise ; D4 par Q_tf | NOTE-106, NOTE-108 |
| NOTE-106 | d89e75b2dd670f69… | 1e4ec7837ce86d65… | critere ⟨F²⟩ remplace par Q_tf pour le ln de (2.17) ; lecture du §2 ; conditions de M-V3 ; greffes | NOTE-108 |

## 3. Etat consolide apres greffe
Dans le cadre S2 + [21] (Weyl-plat exact, champs charges conformes, vide conforme, in-in), au premier ordre en β et pour la partie homogene sous C-iso :
- la loi est tensorielle : R_isj(ln) = (3βκ/e²)(Q_ij − ⅓δ_ij tr Q), convention s = −τ (NOTE-113) ;
- l'operateur du terme non local est le d'Alembertien plat du repere conforme ; aucun terme en H² ;
- le ln Ω de (2.17) vaut (3βκ/e²) × partie sans trace de ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺ ;
- [corrige IR-d''' :] il est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺ (NOTE-113) ; il s'annule pour une onde progressive circulaire, une onde stationnaire helicoidale a Q = 0, un faisceau non polarise, un ensemble isotrope ; il est present pour un reliquat magnetostatique, un dipole rayonne, une onde lineaire ou elliptique ;
- reserve : domaine de validite de l'action plate (u₀ ≪ k ; champ uniforme hors domaine) ; traitement inhomogene ; NOTE-108 auditee (NOTE-113, AU-V3 partiel), corrigee par NOTE-114.

## 4. Non-surclassement
Acte editorial, [conv]. Aucun verdict modifie hors ceux que les notes sources ont deja rendus. Noyau {A4 ; A2★ ; N} inchange. RG-4 inchangee.
