---
id: NOTE-BORD-EON-110-ARMEMENT-IR-i
numero: 110
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-i)
reservation: 2026-10-11T15:13 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 110)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, hypotheses, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-108-IR-g-EXECUTION, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION, NOTE-BORD-EON-109-ACTE-GREFFE-IR-d2]
sources: ["aucune ; champs d'un dipole magnetique dependant du temps : formules standard (Jackson), utilisees comme [derive] et controlees par le calcul (equations de Maxwell verifiees)"]
issue_attendue: "delimitation"
rouvre_si:
  - "fermeture non Maxwell anisotrope fixee par un modele (metrique hors orbite de Weyl, partie (b) de NOTE-98 pour une source inhomogene)"
  - "ordres superieurs en s (gradients), retroaction, ordres superieurs en beta"
---

# NOTE-110 : armement de IR-i. La loi R_ln = (3βκ/e²) Q_tf vaut-elle point par point ? Carte pour un dipole

## 0. Origine
NOTE-108 etablit, pour la **partie homogene** sous fermeture C-iso, que le ln de (2.17) vaut (3βκ/e²) × partie sans trace de Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺. Un champ coherent reel est localise. Il faut savoir si la loi tient localement et a quoi ressemble Q_tf(x) pour une source simple.

## 1. Cadre (fige)
- De Sitter, s = −η = Ω, premier ordre en β, action simplifiee de S2 (a⋆ = k/M par mode ; pour un champ localise, le terme non local est laisse de cote comme en NOTE-102, son effet etant d'ordre β² au premier ordre, NOTE-104/106).
- **Partie A (loi locale)** : mode non moyenne A_y = u(s) cos(kx), u mixte (u₀ magnetique, c electrique). Secteur non Maxwell X^R avec **fermeture locale isotrope** (hypothese H-loc) : X^R = diag(r0, r1, r1, r1)(s, x) + composante q(s, x) en (s, x), trace totale = T̂(s, x) locale, conservation exacte aux ordres controles. Developpement polyhomogene en s, dependance en x par cos(2kx), sin(2kx). Fonctions d'integration laissees libres.
- Comparaison : coefficient de ln s a l'ordre s⁰ dans toutes les composantes de R contre (3βκ/e²) Q_tf(x) **local** (non moyenne). Ordre des corrections de gradient.
- **Partie B (carte du dipole)** : dipole magnetique m(t) = m₀ ẑ f(t), f marche lisse de largeur w centree en t = −D (extinction), repere conforme plat ; champs exacts du dipole dependant du temps a t = 0 (𝓘⁺), formules au temps retarde t_r = −r. Verification des equations de Maxwell sans source hors de l'origine. Q_tf(x) dans trois regions : r < D (deja traversee par l'onde d'extinction), coquille r ≈ D, r > D (reliquat statique). Integrale angulaire et radiale par region, comparaison a NOTE-108 D1.
- Domaine de l'action plate : F² ≪ ∇²F traduit localement.

## 2. Sous-questions
- **I-1** : sous H-loc, le coefficient de ln s a l'ordre s⁰ de R est-il (3βκ/e²) Q_tf(x) point par point ? Les gradients (k) entrent-ils a l'ordre s⁰ ou seulement plus haut ? Les fonctions libres de la fermeture touchent-elles au ln ?
- **I-2** : pour le dipole eteint, quelle est la carte de Q_tf a 𝓘⁺ (trois regions) ? Le ln existe-t-il dans la boule r < D ?
- **I-3** : les integrales par region redonnent-elles la structure (4/5)(mm − ⅓m²) de NOTE-108 pour la coquille rayonnee, et quelle structure pour le reliquat statique ?
- **I-4** : H-loc est-elle necessaire ? Une contrainte anisotrope non Maxwell (donnee d'etat libre, comme c en NOTE-92) peut-elle compenser le ln localement ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **I-V1** | Sous H-loc, la loi locale tient a l'ordre s⁰ (gradients plus haut) ; pour le dipole, le ln existe partout ou le champ est non nul a 𝓘⁺ et s'annule dans la boule deja traversee par l'onde d'extinction. |
| **I-V2** | L'inhomogeneite modifie la loi a l'ordre s⁰ (gradients ou fonctions libres de la fermeture creent ou detruisent le ln) : la loi homogene ne se transporte pas localement. |
| **I-V3** | Delimitation : la loi locale depend de la fermeture du secteur non Maxwell ; une contrainte anisotrope libre peut compenser le ln, et le cadre ne la fixe pas. |
| **I-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**I-V1 qualifie I-V3** : sous H-loc la loi tient point par point a l'ordre s⁰, les gradients n'entrant qu'en s ln s ou plus haut ; carte du dipole : boule r < D sans champ (pas de ln), coquille rayonnee anisotrope (ln, integrale en (4/5)(mm − ⅓m²) × ∫m̈²), reliquat statique r > D a dominante magnetique (ln, integrale angulaire en (1/5)(mm − ⅓m²)). Mais, comme en NOTE-92, une contrainte anisotrope non Maxwell d'ordre s² ln s compenserait le ln ; sans H-loc la loi n'est pas fixee.

## 5. Instruments prevus
Script `ir_i.py` (sympy), empreinte avant execution. Audit IR-j (NOTE-108) a suivre separement.

## 6. Non-surclassement
[conv], premier ordre en β, fond fixe, cadre S2 + [21]. Noyau {A4 ; A2★ ; N} inchange. RG-4 non concernee.
