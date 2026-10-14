---
id: NOTE-BORD-EON-118-IR-k-EXECUTION
numero: 118
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-k)
reservation: 2026-10-11T16:11 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 118)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 17d0fd95a495d41478b75c5fc82c8f4621687f70b1c7ef9b37fe5452859e69e4 (conservee)"
greffe: "IR-m-c entee le 2026-10-11 par NOTE-BORD-EON-121 (corrections de l'audit froid aveugle NOTE-120, AU-V2)"
audit: "NOTE-BORD-EON-119 (gel) / NOTE-BORD-EON-120 (concordance) : AU-V2 ; tenseurs T^(b) et loi par X^M seul retrouves en cecite stricte par M-a3 ; absence de log dans T^(b) etendue par M-b a des familles non diagonales"
gel: NOTE-BORD-EON-117-ARMEMENT-IR-k (sha256 e4e862322e80a4563624d755a9b149557374a243417a46a846cbcf3b838c0410, 2026-10-11T16:12:17Z)
instruments:
  - "ir_k.py, sha256 d58327fe5149ecaf7a69d17b997414375e7aab865cb1c3283feb185b48e7ac40, 2026-10-11T16:13:21Z : EXIT 0, sortie ir_k_sortie.txt"
  - "ir_k_affichage.py, sha256 ff8cbab65034da49d36cc878698979c6f58228ef3d5c0ed8c924dc85884536db, 2026-10-11T16:17:32Z : EXIT 0 (affichage des T_i, meme calcul)"
  - "ir_k_ctrl.py, sha256 1ef8a3ba6c9458ea8bb14cefd10214db76bb428ca0dc5bf3bbd08b1141005fd5, 2026-10-11T16:18:54Z : EXIT 0 (partie C du gel)"
depend: [NOTE-BORD-EON-117-ARMEMENT-IR-k, NOTE-BORD-EON-111-IR-i-EXECUTION, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
verdict: "K-V1 qualifie K-V3"
prediction_realisee: "oui, avec un renforcement (§5)"
rouvre_si:
  - "[v2] partie invariante de Weyl W non lisse en s = 0 ou singuliere sur les modes a impulsion nulle (facteur de forme non local F ln(box/mu^2) F) (K-D1, K-D3)"
  - "[v2] retroaction metrique : terme gravitationnel de l'anomalie en phi C^2, nul sur le fond, donnant ln s x d^4 h sur fond perturbe (K-D2)"
  - "ordres superieurs en beta"
---

# NOTE-118 : IR-k. La completion de Riegert rend H-loc inutile pour le log. Verdict **K-V1 qualifie K-V3** (v2 : voir greffe)

> **Greffe IR-m-c (v2, 2026-10-11).** Corrections issues de l'audit froid aveugle NOTE-120 (AU-V2). Les resultats porteurs sont inchanges et renforces :
> - K-A (divergence de X^M sans log), K-B (T^(b) sans log ni φ) et K-C (loi par X^M seul) ont ete retrouves en cecite stricte par M-a3.
> - Par covariance de Weyl (g = e^{2σ}ḡ, σ = −ln s = φ), on a √g(Δ₄φ − F₄/4) = −¼√ḡ F̄₄ : **φ disparait identiquement**, et la densite d'ordre lineaire vaut (1/6)□_η R^(1)[h] (M-a3, M-b).
> - M-b a verifie l'absence de log sur une famille **non diagonale dependant de (s, x, y)** (H_sx, H_xy, H_zz).
>
> Qualifications de K-V3, remplacees ainsi :
> 1. **Ajout K-D1 (lissite de W)** : le tenseur plat du secteur invariant de Weyl doit etre lisse en s = 0. Sans cette hypothese, X′ = s² ln s · diag(0, 0, f, −f)(x), conserve et sans trace, donnerait un log anisotrope (3κ/2) f ln s (M-b). La conservation seule ne l'exclut pas.
> 2. **Ajout K-D2 (fond fixe)** : tous les tenseurs sont evalues sur le fond. Le terme gravitationnel de l'action anomale en charge de Weyl, ∫√g φ C², est nul sur le fond (C = 0), mais donne ln s × ∂⁴h (structure de type Bach) a l'ordre lineaire en h (M-b, indep_K_weyl). Il n'appartient pas a S_b tel que gele en NOTE-117. Il n'intervient qu'avec une retroaction metrique, donc a un ordre superieur en κ [derive]. Piste IR-r.
> 3. **Ajout K-D3 (regularite de W)** : si W contient un facteur de forme non local du type F ln(□/μ²) F, il est singulier sur des ondes a impulsion nulle, ce qui est le cas des ondes planes du mode. La regularite de T^W est alors une hypothese, non un resultat (M-a3).
> 4. **Retire** : « famille de metriques diagonale » (le resultat sur T^(b) vaut pour tout H, M-b [calcule]) et « etat de ψ causal et lisse » (consequence de l'equation : □_η²ψ = −J est regulier a travers η = 0).
> 5. **Reformule** : « variation de W hors orbite de Weyl ». Si W est exactement invariant de Weyl, T^W[g] = s²T^W[η] vaut pour toute variation (M-a3) ; la vraie hypothese est la regularite de W (K-D3).
> 6. **Precision** (§1B) : T_2 = T_3 decoule de la symetrie y ↔ z de la famille et n'est pas un controle. Le contenu est covariant : T^(b) ∝ (∂_μ∂_ν − η_μν□)□ψ, donc T_yy = T_zz et T_yz = 0 pour J(s, x).

## 0. Resume
Le tenseur energie-impulsion de la partie (b) de la completion de Riegert se reduit, pres de 𝓘⁺, a des derivees **plates** du champ auxiliaire ψ (□_η²ψ = −J). Le facteur conforme φ = −ln s y disparait entierement. Il n'y a donc ni log ni puissance negative de s, et ce tenseur ne voit le champ qu'a travers le scalaire J = √g F², donc pas sa polarisation. Par ailleurs, la loi R_ln(x) = (3βκ/e²) Q_tf(x) se retrouve **avec le seul secteur Maxwell**, sans aucun secteur non Maxwell, et la divergence de ce secteur est sans log. Le log de (2.17) ne depend donc pas de la fermeture : H-loc n'etait pas necessaire. Aucune completion de la classe « Riegert + partie invariante de Weyl a tenseur plat lisse » ne peut le compenser **sur fond fixe** [corrige IR-m : hypotheses K-D1 a K-D3 de la greffe].

## 1. Resultats [calcule]

### A. Divergence du secteur Maxwell (ir_k_sortie.txt)
Pour le mode mixte non moyenne, au premier ordre en β : ∇^μ X^M_μν + ¼ ∂_ν(I²) F² = 0 pour les quatre composantes (identite exacte sur couche), et le coefficient de ln s dans ∇^μ X^M_μν est **0**. La conservation n'exige aucun terme logarithmique dans le secteur non Maxwell.

### B. Partie (b) de Riegert, famille g = s⁻² diag(−1, 1 + εh₁, 1 + εh₂, 1 + εh₃)(s, x)
- Fond : Δ₄(−ln s) − F₄/4 = 0, F₄ = 24 (de Sitter, H = 1).
- Densite d'action au premier ordre en ε : 8 termes. Equations d'Euler-Lagrange (T_i = δS_b/δh_i, d'ou T_ii = 2s² T_i en composantes coordonnees) :

| | Expression exacte |
|---|---|
| T_1 (x) | −(1/6)∂_s⁴ψ + (1/6)∂_s²∂_x²ψ |
| T_2 (y) = T_3 (z) | −(1/6)∂_s⁴ψ − (1/6)∂_x⁴ψ + (1/3)∂_s²∂_x²ψ |

- Aucun log(s), **aucune trace de φ** : ce sont des derivees plates de ψ.
- T_2 − T_3 = 0 : la partie (b) ne distingue pas y et z, alors que Q_tf du mode les distingue (B selon z, E selon y). [corrige IR-m] Cette egalite vient de la symetrie de la famille et n'est pas un controle ; le contenu est la forme covariante T^(b) ∝ (∂_μ∂_ν − η_μν□)□ψ.
- Avec ψ lisse (ψ = Σ s^j a_j(x)) : plus basse puissance de s dans T_i = s⁰, donc T_ii ~ s², du meme ordre que la partie non logarithmique de X^M ; aucune puissance negative.
- Anisotropie T_1 − T_2 a l'ordre s⁰ : (∂_x⁴a₀ − 2∂_x²a₂)/6, fixee par les gradients de ψ, donc de J.

### C. La loi ne vient que du secteur Maxwell (ir_k_ctrl_sortie.txt)
R calcule avec T = X^M seul (aucun secteur non Maxwell) : coefficients de ln s a l'ordre s⁰ egaux a (3βκ/e²) Q_tf(x) pour (i, s, i), **ecart 0**, aucun autre log.

## 2. Lecture [derive]
1. **K-1** : T^(b) est sans log parce que φ = −ln s n'y entre pas (seules des derivees plates de ψ apparaissent, signe de l'invariance de Weyl de √g Δ₄) et parce que ψ, solution causale de □_η²ψ = −J avec J analytique pres de η = 0, est lisse en η = 0. Pour la partie invariante de Weyl W, T^W[g] = s² T^W[η] evalue sur des champs du repere plat lisses : sans log, sous l'hypothese que la variation hors orbite respecte l'invariance de Weyl. [corrige IR-m] Si W est exactement invariant de Weyl, la relation vaut pour toute variation ; l'hypothese reelle est que W soit lisse en s = 0 et regulier sur les modes a impulsion nulle (K-D1, K-D3).
2. **K-2** : T^(b) ne depend du champ que par J (un scalaire) et ne porte que des anisotropies de gradient (∂_i∂_jψ) ; il ne peut pas reproduire l'anisotropie de polarisation Q_tf (exemple : y ↔ z).
3. **K-3** : la divergence de X^M est sans log ; aucune contrainte logarithmique n'est imposee au reste. Comme R est lineaire en T, son log a l'ordre s⁰ ne provient que des termes logarithmiques de T, c'est-a-dire de X^M seul.
4. **K-4** : T^(b) n'apporte que des termes en s² (non logarithmiques) dans les composantes T_ii ; il modifie les constantes de R a l'ordre s⁰, pas son log, et ne cree pas de pole.

```
   T total = X^M (part (a))   +   T^(b) (Riegert)   +   T^W (invariant de Weyl)
             porte I² ~ ln s      derivees plates de ψ     s² × T^W[η] lisse
             log = −2β(T_B−T_E)   pas de ln, pas de φ      pas de ln
                    │                    │                        │
                    └──────── R(2.17) a l'ordre s⁰ ───────────────┘
                     ln s : (3βκ/e²) Q_tf(x), venu de X^M seul
```

## 3. Verdict
**K-V1 qualifie K-V3.**
- K-V1 : dans la classe « Riegert + invariant de Weyl a tenseur plat lisse », le secteur non Maxwell est sans log et aveugle a la polarisation ; il ne peut pas compenser le log ; la loi locale tient sans H-loc.
- Qualification K-V3 [corrige IR-m] : K-D1, le tenseur plat de W est lisse en s = 0 ; K-D2, fond fixe (le terme gravitationnel en φC² donne un log des que la metrique reagit) ; K-D3, W est regulier sur les modes a impulsion nulle. Les qualifications « famille diagonale » et « etat de ψ causal et lisse » de la v1 sont retirees.

## 4. Consequence sur NOTE-111
H-loc est **levee** comme hypothese pour le coefficient du log : la loi R_ln(x) = (3βκ/e²) Q_tf(x) vaut localement pour toute completion de la classe. H-loc reste une hypothese pour les termes **non** logarithmiques de R (constantes), que T^(b) modifie.

## 5. Confrontation a la prediction
Prediction (NOTE-117 §4) : « K-V1 qualifie K-V3 ; φ seulement derive, ψ lisse, pas de log ; T^(b)_yy = T^(b)_zz ; divergence de X^M sans log ; qualification : puissances de s possiblement singulieres et W hors orbite ». **Realisee**, avec un renforcement : φ ne figure **pas du tout** dans T^(b) (pas seulement derive), et les puissances de s ne sont pas singulieres (T_ii ~ s²). [corrige IR-m] La qualification porte sur la lissite et la regularite de W (K-D1, K-D3) et sur le fond fixe (K-D2) ; la famille de metriques et l'etat de ψ ne sont pas des restrictions.

## 6. Portee sur Q-M3 et CCC + M
- Avec NOTE-116 : pour une source causale generique, Q_tf ≠ 0 et le ln Ω de (2.17) est present ; et, par la presente note, aucune completion de la classe consideree ne le compense.
- M-V3 (incompatibilite du canal de jauge anomal avec la regularite de (2.17) pour un champ coherent generique) se trouve renforce comme candidat. Ses conditions restantes sont : cadre S2 + [21] (champs charges conformes, vide conforme, in-in), premier ordre en β, fond fixe sans retroaction (K-D2), lissite et regularite de W (K-D1, K-D3) [corrige IR-m], source causale generique (Q_tf ≠ 0), et le fait que la regularite de (2.17) soit bien le critere pertinent de CCC + M. **Rien n'est grave** ; l'audit froid a ete conduit (NOTE-120, AU-V2) [corrige IR-m] ; une lecture exterieure reste prealable a toute promotion. RG-4 inchangee.

## 7. Greffes proposees (non entees)
- **IR-m** : audit froid aveugle conjoint de NOTE-111, NOTE-116 et NOTE-118. [corrige IR-m] Conduit : NOTE-119/120, AU-V2.
- **IR-n** : etendre B a une famille de perturbations metriques generales. [corrige IR-m] Levee pour T^(b) par l'audit (M-b, familles non diagonales en (s, x, y)).
- **IR-o** : [corrige IR-m] reformulee : regularite de la partie invariante de Weyl sur les modes a impulsion nulle (facteurs de forme non locaux), K-D3.
- **IR-r** [ajout IR-m] : retroaction metrique, terme gravitationnel en φC² (K-D2).

## 8. Non-surclassement
[conv], audite par NOTE-120 (AU-V2) [corrige IR-m]. Premier ordre en β, fond fixe, cadre S2 + [21], completion de Riegert. Noyau {A4 ; A2★ ; N} inchange.
