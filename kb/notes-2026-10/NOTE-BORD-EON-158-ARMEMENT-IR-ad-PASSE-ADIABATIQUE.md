---
id: NOTE-BORD-EON-158-ARMEMENT-IR-ad-PASSE-ADIABATIQUE
numero: 158
serie: I
branche: Q-M3 suite (IR-ad, passe adiabatique)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 158)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, sous-questions, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-13 12:53 heure de Paris (« traite les elements marques en priorite 1 », piste 4 de la reprise v2 §5.1)
depend: [NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-125-IR-r-EXECUTION (v2), NOTE-BORD-EON-133-IR-u-EXECUTION, NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION (v3)]
issue_attendue: "delimitation (l'hypothese de cadre « passe adiabatique » de NOTE-131 t-2 est-elle necessaire, et que devient-elle ?)"
rouvre_si:
  - "audit froid de NOTE-159"
  - "forme du facteur de forme non locale autre que ln(−□/μ²) sur le Weyl (termes d'Euler non locaux, ordre superieur en courbure)"
  - "histoire de l'onde non couverte par le cadre (source dans le futur de τ, ou sur 𝓘⁺ meme)"
---

# NOTE-158 : armement de IR-ad. Le noyau retarde de Γ[g] converge-t-il sur l'histoire de l'onde, et son tenseur est-il lisse en 𝓘⁺ ?

## 0. Origine
NOTE-131 (t-2) : la partie non locale Γ[g] de l'action effective donne, a l'ordre ε, un tenseur de la forme (noyau retarde invariant par translation du repere plat, type ∂∂ ln(−□/μ²) C[h]) applique a toute l'histoire de h sur ]−∞, τ]. La conclusion « T̂_Γ = s² × lisse, pas de pole » y est posee sous deux hypotheses : l'etat regulier (levee par IR-y, NOTE-146 v2 : tout etat Hadamard convient) et la **convergence du noyau retarde**, « qui exige une preparation adiabatique dans le passe lointain, ou les modes du repere plat croissent comme s ». Cette seconde hypothese est restee de cadre (reprise v2 §3.5, §5.1). Il s'agit de l'instruire : la convergence est-elle acquise pour l'onde de de Sitter exacte, sous quelle condition sur son histoire, et le resultat est-il lisse a travers 𝓘⁺ ?

## 1. Cadre (fige)
- Repere plat g = η + εh, h_yy = −h_zz = u(τ) cos kx, τ = η = −s ; u₀ = A(cos kτ − kτ sin kτ) + B(sin kτ + kτ cos kτ) a un signe pres selon l'orientation de τ (forme de NOTE-125 v2 / reprise §4.3 avec s = −τ), solutions de u″ − (2/τ)u′ + k²u = 0 (mode tensoriel de de Sitter en temps conforme). Ces modes **croissent lineairement** en |τ| pour τ → −∞ (passe lointain de l'eon).
- Partie non locale de l'action effective a une boucle des champs conformes a l'ordre quadratique en courbure, forme de Barvinsky-Vilkovisky dans le repere plat : Γ⁽²⁾[g] = (b/2)∫ C_abcd ln(−□/μ²) C^abcd + (termes d'Euler, non locaux, sans contribution a R a cet ordre : hors cadre, cf. rouvre_si) ; la constante b est celle de l'anomalie (NOTE-137). Variation a l'ordre ε (linearisation sur η) : T_ab^Γ = c_b ln(−□/μ²) B_ab[h], ou B_ab[h] = ∂^c∂^d C_acbd[h] est le tenseur de Bach linearise (dans l'espace plat, ln(−□) et ∂∂ commutent), c_b = constante numerique × b (le signe et le facteur ne comptent pas pour la question de convergence et de lissite ; a noter).
- Prescription **retardee** (in-in) : ln(−□/μ²) agit par le noyau retarde ; pour un mode spatial cos kx, c'est la convolution temporelle par K_k(T), transformee de Fourier inverse de ln((k² − (ω + i0)²)/μ²).
- Comptage (NOTE-131 t-2) : T̂ = s² T_Γ ; pole dans R de (2.17) ssi T̂ ~ s¹ Y, Y(0) ≠ 0 ; un T_Γ lisse en τ = 0 donne T̂ ~ s² : rien.
- Fait a verifier au calcul (ad-1) et central : pour l'onde de de Sitter exacte, le Bach de ĝ est nul (metrique d'Einstein a l'ordre ε), et le Bach est conformement covariant de poids tel que B[g] = 0 aussi dans le repere plat : **B_ab[h] ≡ 0** pour u = u₀. Le tenseur T_Γ a l'ordre ε est donc formellement « ln(−□) × 0 » ; mais le mode u₀ est a la frequence ω = ±k ou ln(k² − ω²) diverge : produit 0 × ∞ a regulariser. C'est exactement la ou l'hypothese de « passe adiabatique » intervient.
- Trois histoires de l'onde sont considerees : (H-a) adiabatique : u_ε(τ) = e^(ετ) u₀(τ), ε → 0⁺ (commutation en douceur dans le passe lointain) ; (H-b) brusque : u(τ) = θ(τ − τ₀) u₀(τ) + (raccord lisse sur un intervalle fini [τ₀, τ₀ + δ]) avec τ₀ < 0 fixe (onde emise a un temps fini) ; (H-c) generique : u = u₀ + v avec v une deviation lisse a support compact dans le passe (B[v] ≠ 0 sur un compact).

## 2. Sous-questions
- **ad-1 (Bach nul)** : verifier B_ab[h] ∝ □²h_ab pour h TT dans l'espace plat et (∂_τ² + k²)² u₀ = 0 pour les deux solutions A et B (identite de de Sitter). Donner le coefficient.
- **ad-2 (noyau)** : forme explicite de K_k(T) : attendu K_k(T) = −2[θ(T) cos(kT)/T]₊ + c(μ, k) δ(T) (la partie en δ est locale, proportionnelle a B, donc nulle sur u₀) ; comportement en T → ∞ en 1/T.
- **ad-3 (H-a, adiabatique)** : calculer B_ε = (∂_τ² + k²)² u_ε a l'ordre ε (attendu : B_ε = ε × e^(ετ) × (combinaison de sin kτ, cos kτ, τ sin kτ) + O(ε²)) et la reponse retardee R_ε(τ) = ∫_{−∞}^{τ} K_k(τ − τ′) B_ε(τ′) dτ′ pour τ ≤ 0. Prediction : R_ε(τ) = O(ε ln(1/ε)) → **0** quand ε → 0, uniformement pour τ dans un voisinage de 0 ; dans la limite adiabatique le tenseur d'ordre ε de Γ[g] est **nul** pour l'onde exacte. Controle numerique (mpmath) pour ε = 10⁻¹, 10⁻², 10⁻³ a τ = 0 et τ = −1.
- **ad-4 (H-b, brusque)** : pour une emission a temps fini τ₀ < 0 avec raccord lisse, B[h] est a support dans [τ₀, τ₀ + δ] ; la reponse R(τ) = ∫ K_k(τ − τ′) B(τ′) dτ′ est, pour τ > τ₀ + δ, une fonction **lisse** de τ (K_k lisse pour T > 0), en particulier a travers τ = 0 ; sa valeur en τ = 0 est finie et generiquement non nulle (queue non locale ~ cos(k(τ − τ₀))/(τ − τ₀)). Donc T̂_Γ = s² × lisse : **pas de pole**. Calcul explicite pour un raccord polynomial ou gaussien.
- **ad-5 (H-c, critere general)** : enoncer la condition de convergence : ∫_{−∞}^{τ} |B[h](τ′)| / (1 + |τ − τ′|) dτ′ < ∞, satisfaite des que B[h] est integrable avec poids 1/|τ′| dans le passe, c'est-a-dire des que h est solution de l'equation de de Sitter linearisee (Bach nul) hors d'une region du passe ou B est integrable ; et la lissite en τ = 0 : acquise des que B est lisse au voisinage de τ = 0 (convolution d'une distribution a singularite integrable en T = 0 avec une fonction lisse). Reformuler l'hypothese de cadre « passe adiabatique » en condition explicite sur l'histoire de l'onde.
- **ad-6 (cas pathologique)** : quelle histoire produirait un T_Γ non lisse ou un terme s¹ en τ = 0 ? Attendu : seulement une source B[h] non lisse ou non integrable au voisinage de τ = 0 lui-meme (onde emise sur 𝓘⁺, ou h non solution de l'equation de de Sitter au voisinage de 𝓘⁺), c'est-a-dire hors du cadre « onde gravitationnelle a donnee electrique non nulle en 𝓘⁺ » de G-V3.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AD-V1** | Pour l'onde de de Sitter exacte, B[h] ≡ 0 ; dans la limite adiabatique le tenseur d'ordre ε de Γ[g] est nul ; pour toute histoire a source B integrable dans le passe et lisse pres de 𝓘⁺, T_Γ est lisse en τ = 0 et T̂_Γ ~ s² : pas de pole. L'hypothese de cadre « passe adiabatique » est **remplacee** par une condition explicite et physique sur l'histoire de l'onde (solution de de Sitter hors d'une region integrable du passe), satisfaite par toute onde emise a temps fini ; la liste des hypotheses de cadre de G-V3 s'en trouve reduite. |
| **AD-V2** | Comme AD-V1 pour la lissite en τ = 0 (pas de pole dans tous les cas), mais la **valeur** finie du tenseur en 𝓘⁺ depend de l'histoire (non universelle) ; sans effet sur G-V3 ; hypothese reformulee, avec cette dependance notee. |
| **AD-V3** | La reponse retardee ne converge pas, ou n'est pas lisse en τ = 0, pour une histoire physique (H-a ou H-b) : l'hypothese de cadre est **necessaire et non triviale** ; a maintenir telle quelle, avec le mecanisme identifie. |
| **AD-V4** | Une histoire physique produit un terme s¹ a valeur non nulle en 𝓘⁺ (pole d'ordre ε de Γ[g]) : compensation ou renforcement du pole G-V3 selon le signe : libelle a reviser. |
| **AD-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**AD-V1 qualifie AD-V2.**
- ad-1 : B ∝ □²h pour h TT, coefficient −¼ ; (∂² + k²)² u₀ = 0 pour A et B.
- ad-2 : K_k(T) = −2[θ(T) cos(kT)/T]₊ + (local) ; decroissance en 1/T.
- ad-3 : B_ε = O(ε) ; R_ε(τ) = O(ε ln(1/ε)) → 0 ; controle numerique concordant (rapport R_ε/ε ln(1/ε) borne).
- ad-4 : reponse lisse a travers τ = 0, valeur finie non nulle, dependante de τ₀ et du raccord (d'ou la qualification AD-V2).
- ad-5 : condition de convergence enoncee ; hypothese reformulee : « h est solution de l'equation de de Sitter linearisee au voisinage de 𝓘⁺ et sa source B[h] est integrable (avec poids 1/|τ|) dans le passe ».
- ad-6 : seule une source sur 𝓘⁺ meme (hors cadre) donnerait un terme non lisse.
- Consequence : la liste §3.5 de la reprise v2 remplace « passe adiabatique (convergence du noyau retarde) » par la condition explicite ; G-V3 inchange.

## 5. Instruments prevus
Script `irad_kernel.py` (sympy ; mpmath), empreinte avant execution : ad-1 (Bach linearise sur h TT, identite de de Sitter), ad-2 (transformee de Fourier du logarithme, forme du noyau), ad-3 (B_ε symbolique ; integrale numerique R_ε(τ) pour trois ε), ad-4 (raccord lisse explicite, reponse en τ = 0 et derivees), ad-5 (comptage). Aucune lecture de source.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v3) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Forme ln(−□) du facteur de forme sur le Weyl prise comme cadre ; premier ordre en ε ; une boucle ; mode tensoriel.
