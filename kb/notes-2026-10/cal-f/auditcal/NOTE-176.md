---
id: NOTE-BORD-EON-176-CAL-F-EXECUTION
numero: 176
serie: I
branche: Chantier D / critere (2.17) (calibration CAL-F)
reservation: 2026-10-15T14:33 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 176)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-175-ARMEMENT-CAL-F.md, sha256 f67e3f906320e180, sceau NOTE-175-SCEAU.txt 2026-10-15T14:33:36Z (l'en-tete du gel porte 14:40 par ecriture anticipee ; le sceau et le registre font foi : 14:33)"
source: "H. Friedrich, arXiv:1311.0700v2, texte integral via alphaXiv, archive src/SOURCE-1311.0700-fulltext.txt"
script: "cal_f.py et cal_f_sortie.txt (empreintes au sceau de cloture)"
---

# CAL-F, execution : le critere (2.17) et les champs massifs

## VERDICT : CAL-V2 (avec composante CAL-V1 sur la calibration)
- La calibration **reussit** : l'implementation du corpus (derivee covariante complete, `irr_c.py`) est correcte ; le pole que l'assistant croyait trouver au point de Friedrich venait d'un calcul de tete fait avec des derivees partielles (erreur reproduite au script, §2.3).
- La **regle de comptage** telle que resumee dans NOTE-163 (« T ~ s^p ⟹ R ~ s^(p-2), pole ssi p = 1 ») est **imprecise** : c'est un comptage generique, qui surestime pour les sources homogenes et isotropes conservees (exactement nulles). Le pole de G-V3 a ete etabli par calcul covariant explicite, pas par la regle : **G-V3 n'est pas affecte**.
- Pour une matiere **massive**, le critere de Friedrich ne se reduit pas a (2.17) : son theoreme 3.1 porte sur le **systeme couple entier**, equation de matiere comprise, et la singularite du scalaire est d'abord dans l'equation de matiere (3.11). C'est l'amendement : pour le Dirac, l'obstruction au sens de Friedrich est le **coefficient m/Omega de l'equation de Dirac rescalee**.
- Prediction (CAL-V2, informee) **realisee** pour le verdict principal ; **non realisee** pour F-2 dans (2.17) (la poussiere homogene y donne zero, pas un terme a residu m n0) ; realisee sous une autre forme (terme d'ordre Omega^-1 de residu m, dans l'equation de matiere).

## 1. F-0 : ce que dit la source (extraits verbatim, src/SOURCE-1311.0700-fulltext.txt)
- (2.17) : « ∇_μ W^μ_ρνλ = 2 Ω^-1 ∇̂_[ν L̂_λ]ρ », avec « ∇̂_ρ L̂_μν = (κ/2) ∇̂_ρ(T̂_μν − (1/3) T̂ ĝ_μν) » ; les chapeaux designent la metrique **physique** et sa connexion ; « T*_ρμ = T̂_ρμ − (1/4) T̂ ĝ_ρμ » dans (2.14)-(2.15) (homonymie avec le T* ≡ Ω^-2 T̂ de (3.7), deja signalee par NOTE-90).
- Equation de matiere rescalee (3.11) : « □_g ψ − (1/6) R ψ = Ω^-2 (m² − (2/3) λ) ψ + (κ/6) T* ψ + 4 ψ³ U(Ωψ) + Ω ψ⁴ U′(Ωψ) », avec ψ = Ω^-1 φ ; « Its most conspicuous feature, however, is the first term on the right hand side, which is singular where Ω → 0. »
- Theoreme 3.1 : le systeme couple (2.13)-(2.19), (3.11) « is regular in the sense that on the right hand sides of the equations no terms of the form Ω^-k, k > 0, occur [...] If and only if the single condition m² = (2/3) λ » ; preuve : « Critical are equations (2.16), (2.17) », ou les termes en Ω^-1 se combinent en multiples de (m²/3 − λ/18).
- Lecture : le critere de Friedrich est la **regularite de tous les seconds membres en inconnues rescalees**, equation de matiere comprise ; (2.17) n'en est qu'une partie.

## 2. F-1 : calibration (script cal_f.py, metrique physique de dS, H = 1)
1. **Fluide homogene isotrope quelconque** : la source de (2.17) vaut −κ(η ρ′ − 3(ρ + p))/(6η⁴) sur les composantes (i, 0, i), c'est-a-dire un multiple de l'equation de conservation ; **nulle sur couche**. Derivation analytique : L̂ = A uu + B ĝ avec A = (κ/2)(ρ + p), B = κρ/6, et ∇̂_[ν L̂_λ]ρ = −(AH + Ḃ) u_[ν h_λ]ρ, nul par ρ̇ = −3H(ρ + p). Reflet de la platitude conforme de FLRW (W = 0).
2. **Scalaire homogene minimalement couple, masse quelconque, sur couche** : source de (2.17) **identiquement nulle**. Il n'y a donc aucune contradiction avec le theoreme 3.1 : pour un scalaire homogene, (2.17) ne voit rien ; la singularite (m² − 2λ/3) passe par (3.11) et, pour un scalaire inhomogene, par les termes de (2.16)-(2.17) que Friedrich exhibe.
3. **Le calcul de tete reproduit** : avec des derivees partielles (sans Christoffel), au point m² = 2, h = φ0 s + φ1 s², on obtient −2κ φ0 φ1/(3s) − κ φ1² : le faux pole annonce au gel. Erreur de l'assistant, identifiee.
4. **Poussiere homogene** ρ = m n0 Ω³ : source de (2.17) identiquement nulle.

## 3. F-2 : le gaz de Dirac massif
- **(2.17), cas homogene** (particules au repos a temps tardif, k = 0) : la contribution est celle d'une poussiere conservee, **nulle**. Le pole m/Ω de la densite d'energie rescalee (article, Prop. 3 ; greffe G-D1-b) est donc une obstruction **au sens du critere du corpus** (Ω^-4 T, texte litteral de RG-4), **pas** au sens de (2.17) pour une source homogene.
- **Equation de matiere** : l'equation de Dirac rescalee (iγ^μ∂_μ − m/Ω) ψ̂ = 0 porte un coefficient d'ordre Ω^-1, de residu m. C'est l'analogue spin 1/2 exact du premier terme de (3.11). Le terme scalaire s'annule pour une masse speciale (m² = 2λ/3) parce qu'il depend de m² − 2λ/3 ; le terme spinoriel ne depend que de m (Lemme 2 de l'article : aucun couplage de courbure de la classe ne le compense sans annuler m_eff) : **aucune masse constante non nulle ne rend l'equation de Dirac reguliere au sens de Friedrich**. Avec masse variable, regularite du coefficient ssi m = Ω μ, μ lisse (Prop. 4(c) de l'article).
- **Non traite** : la source de (2.17) pour un mode de Dirac inhomogene (k ≠ 0), ou les termes croises oscillent en e^{2i(m/H) ln Ω} et dont les derivees peuvent produire des facteurs m/Ω ; la regularite des equations geometriques (2.13)-(2.16) pour m = Ω μ. Declare ouvert.

## 4. F-3 : consequences (propositions de greffe, non entees ; FW-2, FW-5)
- **G-CAL-a (NOTE-163, table « Cadre et conventions », ligne Comptage)** : remplacer « pole si et seulement si p = 1 et Y(0) ≠ 0 » par « comptage generique : pole possible seulement si p ≤ 1 ; l'existence et le residu se calculent par derivee covariante explicite (sources homogenes isotropes conservees : contribution nulle). Le pole de G-V3 est etabli par calcul covariant explicite (irr_c.py, re-derive a l'aveugle NOTE-128) ». G-V3 inchange.
- **G-D1-e (S26-02 v2 §7, portee sur RG-4)** : le fondement de RG-4 a deux lectures. (i) Critere du corpus (texte litteral de RG-4, trace rescalee Ω^-4 T) : pole m/Ω de la densite d'energie (G-D1-b), invariant de jauge. (ii) Critere de Friedrich (regularite du systeme couple) : coefficient m/Ω de l'equation de Dirac rescalee, analogue spin 1/2 de (3.11), sans masse speciale. La phrase de G-D1 « le pole G-D1-b [...] fondement mieux etabli » doit etre precisee : (2.17) ne voit pas une poussiere homogene. RG-4 reste declenchee sous les deux lectures.
- **Article (v2.2)** : ajouter que, dans la formulation de Friedrich, la condition pertinente est la Prop. 4(c) (coefficient lisse), et que c'est la le veritable « counterpart spin 1/2 » du theoreme 3.1 : le scalaire admet une masse speciale, le spineur aucune ; la Prop. 5(b) (tenseur rescale borne) est un critere distinct, que (2.17) ne requiert pas pour une source homogene.

## 5. Passe adverse interne (ne vaut pas audit)
1. « Le test homogene ne dit rien du cas inhomogene, ou Friedrich trouve des termes singuliers pour le scalaire. » Exact ; c'est pourquoi F-2 pour k ≠ 0 est declare ouvert, et pourquoi l'obstruction retenue est celle de l'equation de matiere, qui ne depend pas de k.
2. « Une redefinition des inconnues (jauge singuliere) pourrait absorber m/Ω. » La jauge λ = (m/H) ln Ω deplace le coefficient singulier dans le potentiel (A_η ~ 1/Ω) : le systeme Dirac-Maxwell garde un coefficient singulier (Prop. 2 de l'article). Le critere de Friedrich est formule pour un choix d'inconnues fixe (ψ = Ω^-1 φ) ; le notre (ψ̂ = Ω^-3/2 ψ) est le poids conforme standard.
3. « La regle de NOTE-163 a ete auditee (NOTE-137) ». L'audit portait sur les calculs explicites, qui sont justes ; la phrase de synthese est un resume plus fort que les calculs.

## 6. Non-surclassement
Rien de grave. G-V3 inchange. RG-4 inchangee (refutee a titre provisoire). p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
