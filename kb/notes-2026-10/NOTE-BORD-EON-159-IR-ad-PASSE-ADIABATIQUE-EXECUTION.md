---
id: NOTE-BORD-EON-159-IR-ad-PASSE-ADIABATIQUE-EXECUTION
numero: 159
serie: I
branche: Q-M3 suite (IR-ad, passe adiabatique)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 159)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-158-ARMEMENT-IR-ad-PASSE-ADIABATIQUE (sha256 657eedff30065256dedf62c86da7c5bbbfa4d324ae28fa110c648caed92389f7, sceau 2026-10-13T11:02:23Z)
instruments:
  - "irad_kernel.py, sha256 3d5d52115b2839dffdb7ca2ff41071ec604cdf1bd9b50ebb981a528f90b7e46b, EXIT 0, sortie irad_kernel_sortie.txt ; sympy (ad-1, ad-3 symbolique), mpmath (ad-2 controle, ad-3 et ad-4 numeriques, 15 decimales)"
lecture_hors_gel_declaree: "Foraci-Woodard arXiv:2412.11022 eq. (37)-(39) et (49)-(50), lue sous le gel de NOTE-152 (IR-ab), citee ici comme appui exterieur ; extraits src/SOURCE-2412.11022v1-extraits.txt (12b9a99d285f7598)"
depend: [NOTE-BORD-EON-158-ARMEMENT-IR-ad-PASSE-ADIABATIQUE, NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-153-IR-ab-LECTURE-2412.11022-2405.01024]
verdict: "AD-V1 qualifie AD-V2"
prediction_realisee: "oui"
rouvre_si:
  - "audit froid"
  - "facteur de forme non local autre que ln(−□/μ²) sur le Weyl ; ordre superieur en courbure"
  - "source B[h] non integrable ou non lisse au voisinage de scri+ (hors cadre de G-V3)"
---

# NOTE-159 : IR-ad. Sur l'onde de de Sitter exacte, la source du noyau non local est identiquement nulle (Bach = 0) ; en limite adiabatique la reponse est nulle, pour une emission a temps fini elle est lisse et finie en 𝓘⁺ ; dans tous les cas T̂_Γ ~ s² et l'hypothese « passe adiabatique » se remplace par une condition explicite sur l'histoire de l'onde. Verdict **AD-V1 qualifie AD-V2**

## 0. Resume
- **ad-1** [calcule] : pour h TT sur fond plat, le Bach linearise vaut **B_ab = −¼ □² h_ab** (composantes tt, tx, xx nulles, B_zz = −B_yy) ; pour les deux modes de de Sitter u_A = cos kτ + kτ sin kτ, u_B = sin kτ − kτ cos kτ (residu de l'equation u″ − (2/τ)u′ + k²u = 0 : zero), (∂² + k²)u = 2k² cos kτ (resp. 2k² sin kτ) et **(∂² + k²)² u = 0**. Donc **B[h] ≡ 0** sur toute l'histoire de l'onde exacte : la source du noyau non local est nulle, et T_Γ^(ε) = ln(−□/μ²) B[h] est formellement 0 × ∞ aux frequences ω = ±k.
- **ad-2** [derive, controle] : K_k(T) = −2[θ(T) cos(kT)/T]₊ + c(μ, k) δ(T) ; retarde, decroissance en 1/T ; la partie δ est locale (∝ B, nulle sur u₀) ; controle de Frullani ∫₀^∞ (cos aT − cos bT)/T dT = ln(b/a) a 10⁻¹⁴.
- **ad-3 (H-a)** [calcule] : u_ε = e^(ετ)u₀ : B_ε = e^(ετ)(−8εk³ sin kτ) + O(ε²) (mode A ; +8εk³ cos kτ pour B). Reponse retardee non locale R_ε(τ₀) (k = 1, regularisation de Hadamard a l'echelle 1) : τ₀ = 0 : −1,23 ; −0,127 ; −0,0126 pour ε = 10⁻¹, 10⁻², 10⁻³ (lineaire en ε) ; τ₀ = −1 : −0,72 ; −0,25 ; −0,041. **R_ε → 0** quand ε → 0 ; la borne O(ε ln(1/ε)) du gel est respectee (le rapport R_ε/(ε ln(1/ε)) reste borne, entre 1,8 et 5,9), et la convergence est en fait O(ε) en τ₀ = 0. Dans la limite adiabatique, le tenseur d'ordre ε de Γ[g] est **nul** pour l'onde exacte.
- **ad-4 (H-b)** [calcule] : u = S(τ)u₀ avec S transition C^∞ de 0 a 1 sur [τ₀, τ₀ + δ] = [−6, −4] : B[h] a support dans [−6, −4] ; R(τ) = ∫K_k(τ − τ′)B(τ′)dτ′ : −3,32 ; −1,23 ; −0,32 ; 0,28 ; 0,396 ; 0,408 pour τ = −2 ; −1 ; −0,5 ; −0,1 ; −0,01 ; 0. **Lisse a travers τ = 0** (convolution d'un noyau C^∞ pour T ≥ 2 avec une source C^∞ a support compact), valeur finie **non nulle** en 𝓘⁺, dependante de τ₀ et du raccord.
- **ad-5** [derive] : T̂_Γ = s² R(−s), R lisse en 0 : T̂ ~ s² R(0) + O(s³), **aucun s¹**, pas de pole. Condition de convergence : ∫_{−∞}^{τ} |B(τ′)|/(1 + |τ − τ′|) dτ′ < ∞, satisfaite des que B[h] est integrable a poids 1/|τ′| dans le passe ; lissite en 𝓘⁺ des que B est lisse au voisinage de τ = 0. **Reformulation de l'hypothese** : « h est solution de l'equation de de Sitter linearisee (Bach nul) au voisinage de 𝓘⁺, et sa source B[h] est integrable a poids 1/|τ| dans le passe » ; condition satisfaite par toute onde emise a temps fini et par toute commutation adiabatique.
- **ad-6** [derive] : seule une source B[h] non lisse ou non integrable **au voisinage de 𝓘⁺ meme** (onde emise sur 𝓘⁺, ou h non solution pres de 𝓘⁺) donnerait un T_Γ non lisse ; c'est hors du cadre de G-V3 (« onde gravitationnelle a donnee electrique non nulle en 𝓘⁺ » suppose h solution pres de 𝓘⁺).
- **Appui exterieur** [extrait, lecture hors gel declaree] : Foraci-Woodard 2412.11022 ecrit le noyau non local f_B = ∂⁴{θ(Δη − Δr)(ln[μ²(Δη² − Δr²)] − 1)} (eq. 39), et montre (eq. 49-50) que « the nonlocal contribution vanishes » sur le mode de de Sitter u₀ = (1 + ikη)e^(−ikη) par l'identite (∂₀ + ik)²∂₀u₀ = 0 ; le logarithme seculaire vient du seul terme local 8π ln(aa′)δ⁴. C'est exactement ad-1 et ad-3 (la source calcule au premier ordre en κ² ce que le programme loge dans WZ).

## 1. Resultats [calcule] (irad_kernel.py, EXIT 0)
| Sous-question | Resultat |
|---|---|
| ad-1 | B_ab = −¼□²h_ab ; (∂² + k²)²u_A = (∂² + k²)²u_B = 0 |
| ad-2 | K_k(T) = −2[θ(T)cos(kT)/T]₊ + c δ(T) ; Frullani verifie |
| ad-3 | B_ε = ∓8εk³ e^(ετ)(sin, cos)(kτ) + O(ε²) ; R_ε(0) = −1,23 ; −0,127 ; −0,0126 (ε = 10⁻¹, 10⁻², 10⁻³) → 0 |
| ad-4 | R(0) = 0,408 (τ₀ = −6, δ = 2, k = 1) ; R lisse en 0 |
| ad-5 | T̂ ~ s² R(0) : pas de s¹ |

```
   histoire de l'onde h (repere plat)          source B[h] = -1/4 box^2 h      reponse R(tau) pres de scri+     T-hat_Gamma     pole ?
   ----------------------------------------------------------------------------------------------------------------------------------
   (H-a) de Sitter exacte, commutation adiabatique   O(eps) e^{eps tau}, -> 0       R_eps -> 0                        0               non
   (H-b) emission a temps fini tau0, raccord lisse   C^inf, support compact         lisse, finie, non nulle           s^2 R(0)        non
   (H-c) deviation lisse a support compact           C^inf, support compact         lisse, finie                      s^2 x lisse     non
   source non integrable ou non lisse pres de scri+  (hors cadre)                   non lisse                         ?               hors cadre
```

## 2. Lecture [derive]
1. **Pourquoi l'hypothese etait inoffensive.** Le noyau non local n'agit pas sur h mais sur son Bach linearise, qui est nul pour toute solution de l'equation de de Sitter. La « croissance lineaire des modes dans le passe » (NOTE-131) ne porte donc aucune source : la convergence ne se pose que pour l'ecart a la solution exacte (commutation, emission), qui est de taille controlee et localise dans le passe.
2. **Limite adiabatique.** R_ε → 0 : la reponse non locale a une onde de de Sitter preparee adiabatiquement est nulle, en accord avec le « nonlocal contribution vanishes » de la source exterieure. La dependance en μ (terme δ, local) est elle aussi proportionnelle a B, donc nulle ; c'est la raison de fond de « la dependance en μ est locale (∝ Bach, nul sur couche) » de NOTE-131.
3. **Emission a temps fini.** La reponse est une queue non locale, lisse et finie en 𝓘⁺, dependante de l'histoire (d'ou la qualification AD-V2) ; elle entre dans T̂ au niveau s² et ne touche pas (2.17) au niveau polaire. Elle n'est pas universelle, mais elle est **reguliere** : c'est tout ce que G-V3 requiert.
4. **Hypothese de cadre reduite.** La liste §3.5 de la reprise v2 peut remplacer « passe adiabatique (convergence du noyau retarde) » par la condition explicite d'ad-5 ; cette condition est une propriete de l'onde (solution pres de 𝓘⁺, source integrable dans le passe), non une hypothese sur l'etat ni sur la theorie.

## 3. Verdict
**AD-V1 qualifie AD-V2.**
- **AD-V1** : B[h] ≡ 0 sur l'onde exacte ; reponse nulle en limite adiabatique ; T_Γ lisse en 𝓘⁺ et T̂_Γ ~ s² pour toute histoire a source integrable dans le passe et lisse pres de 𝓘⁺ ; hypothese « passe adiabatique » remplacee par une condition explicite et physique sur l'histoire de l'onde.
- **AD-V2** (qualification) : la valeur finie de T̂_Γ/s² en 𝓘⁺ depend de l'histoire (τ₀, raccord) ; sans effet sur G-V3.

## 4. Confrontation a la prediction
Prediction (NOTE-158 §4) : ad-1 [**realise**, coefficient −¼] ; ad-2 [**realise**] ; ad-3 [**realise** : R_ε → 0, borne O(ε ln(1/ε)) respectee, taux O(ε) en τ₀ = 0] ; ad-4 [**realise**] ; ad-5 [**realise**] ; ad-6 [**realise**]. Verdict predit AD-V1 qualifie AD-V2 : **realise**.

## 5. Consequences (rien n'est grave)
- Hypotheses de cadre de G-V3 (reprise v2 §3.5, NOTE-138 v3 §1.3) : « passe adiabatique (convergence du noyau retarde) » → « onde solution de l'equation de de Sitter linearisee pres de 𝓘⁺, source B[h] integrable dans le passe » (revision du libelle proposee, non entee).
- NOTE-131 `rouvre_si` (« noyau retarde non convergent ») : clos par cette note dans le cadre ln(−□) sur le Weyl.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- Audit froid de NOTE-159 (Bach linearise a l'aveugle ; identite de de Sitter ; noyau ; limite adiabatique).
- Termes d'Euler non locaux et ordre superieur en courbure dans Γ[g] (cadre, non arme).
- Revision du libelle de G-V3 (NOTE-138 v4) integrant IR-ab, IR-ac, IR-aa, IR-ad, apres audits.

## 7. Non-surclassement
[conv], non audite. Forme ln(−□/μ²) sur le Weyl ; premier ordre en ε ; une boucle ; mode tensoriel ; regularisation de Hadamard a l'echelle 1 pour la partie finie du noyau (terme local, ∝ B). G-V3 reste un candidat non grave.
