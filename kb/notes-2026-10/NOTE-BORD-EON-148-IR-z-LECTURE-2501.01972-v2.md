---
id: NOTE-BORD-EON-148-IR-z-LECTURE-2501.01972
numero: 148
serie: I
branche: Q-M3 suite (IR-z, lecture)
reservation: 2026-10-12T15:20 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 148)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 236ac4d33f286ed4822236e7340907059e07c2696cb7418969b1cc311ef5244d (conservee)"
greffe: "IR-z entee le 2026-10-12 par NOTE-BORD-EON-151 (precisions de l'audit froid aveugle NOTE-150, AU-V1)"
audit: "NOTE-BORD-EON-149 (gel) / NOTE-BORD-EON-150 (concordance) : AU-V1 ; eq. 35, 42, 46 et n = 8 retrouves en lecture aveugle (ZA-1) ; mots de la source releves"
gel: NOTE-BORD-EON-147-ARMEMENT-IR-z-LECTURE-2501.01972 (sha256 aa6b20dd6a8ff2ddbcaf2d948ca1457b80a41bf984b641d025924787a2ddac01, sceau 2026-10-12T15:20:43Z)
sources:
  - "FW : A. J. Foraci, R. P. Woodard, Resumming Fermion Loops for Inflationary Gravity, arXiv:2501.01972v1 [gr-qc], 27 decembre 2024, UFIFT-QG-24-09, prepublication ; texte integral (10 pages) lu via alphaXiv le 2026-10-12 ; extraits src/SOURCE-2501.01972v1-extraits.txt, sha256 85071439611a27d21f26bc3d2f696bbc859d056401f1ea252ca70ba1b9a50ebf"
instruments:
  - "irz_conv.py, sha256 6b5ccfec0f80bc6dedf2dec6d36f9db52053ce842f04ce1748e06f214246ca12, EXIT 0, sortie irz_conv_sortie.txt (dafbc1bb2ed23675)"
depend: [NOTE-BORD-EON-147-ARMEMENT-IR-z-LECTURE-2501.01972, NOTE-BORD-EON-135-IR-v-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-133-IR-u-EXECUTION]
verdict: "Z-V1 qualifie Z-V2"
prediction_realisee: "oui, sauf z-3 (jauge non discutee par la source)"
rouvre_si:
  - "audit froid"
  - "lecture de [8] Foraci-Woodard 2412.11022 (photon, source de l'eq. 35) ou de [27] Miao-Tsamis-Woodard 2405.01024 (renormalisation de champ du graviton, source de l'eq. 39)"
---

# NOTE-148 : IR-z. La source primaire confirme le coefficient 8bκ et la puissance a^(8bκH²) ; la resommation y est un procede de groupe de renormalisation presente par « suggests », sans controle d'ordre superieur. Verdict **Z-V1 qualifie Z-V2** (v2 : voir greffe)

> **Greffe IR-z (v2, 2026-10-12).** Precisions issues de l'audit froid aveugle NOTE-150 (AU-V1 ; rapport ZA-1 b081ee5de22e0279…). Aucun resultat porteur modifie ; verdict inchange.
> 1. [ajout IR-z] Les resultats de Sitter (35)-(37) ne sont pas recalcules par la source : ils sont **lus a partir de [6] (Wang-Woodard 2015) et [8] (Foraci-Woodard 2412.11022) par le facteur de proportionnalite 1/2** (« we can read off the 1-loop solutions for Dirac from those for Maxwell », p. 7). La justification du coefficient de Dirac repose donc sur la chaine Maxwell ; [8] devient la lecture prioritaire pour remonter la justification (piste §6).
> 2. [ajout IR-z] La jauge fixee par la source est la **jauge de Lorentz locale** (vierbein symetrique, p. 3) ; aucune fixation de jauge gravitationnelle n'est discutee (l'operateur de Lichnerowicz (34) est utilise sans terme de jauge). Le point z-3 « jauge non discutee » se lit : independance de jauge gravitationnelle non discutee.
> 3. [ajout IR-z] Le terme en κ_W²H² du glissement gravitationnel (37) est une constante, non resommee ; le photon n'a pas d'equation propre, seulement les rapports « Dirac = 1/2 EM » et « MCC = 1/12 EM » (eq. 45).

## 0. Resume
- **z-1** [extrait, calcule] : eq. (35), C_0i0j → C^tree {1 + κ_W²H²/(80π²) ln a}, κ_W² = 16πG ; converti : **GH²/(5π) = 8bκH²** pour le fermion de Dirac. Scalaire conforme, eq. (46) : κ_W²H²/(480π²) = GH²/(30π) = 8bκH². Photon : « 1/2 fois la contribution de l'electromagnetisme » (p. 6) : 2G/(5π). Les trois coefficients de NOTE-133/137 sont **retrouves a la source** (irz_conv.py).
- **z-2** [extrait] : equation de Callan-Symanzik (41) avec γ = ∂ln(1+δZ)/∂ln μ² = −κ_W²H²/(160π²) (eq. 40), δZ = D[2(D−1)c₁ − c₂]κ²H² (eq. 39, renormalisation de champ du graviton, empruntee a [27]), β_G = 0 a cet ordre, ∂/∂ln μ remplace par ∂/∂ln a au nom de la relation (38) entre μ et a dans l'auto-energie renormalisee ; resultat eq. (42) : **C_0i0j → C^tree × a^(κ_W²H²/(80π²))**, exposant = −2γ = coefficient du log [calcule].
- **z-3** [extrait] : regularisation dimensionnelle, contre-termes BPHZ (R² et C², c₁ = 0 par transversalite-tracelessness), formalisme in-in de Schwinger-Keldysh (eq. 32-33), propagateur du vide de Minkowski du repere conforme (eq. 8) ; la partie non logarithmique (termes en κ²/a²r²) n'est pas resommee ; **aucune discussion de l'independance de jauge**.
- **z-4** [extrait] : « for as long as the de Sitter phase persists » (resume) ; « During a prolonged period of de Sitter inflation, the secular 1-loop corrections [...] must eventually overwhelm the tree order result. At this point perturbation theory breaks down and one must invoke a nonperturbative resummation scheme » ; **aucune mention** d'une limite a → ∞, d'un nombre maximal d'e-folds ou d'une echelle de rupture.
- **z-5** [extrait] : scalaire conforme traite en conclusion (eq. 45-47) ; photon renvoye a [6] et [8] ; reponse a une masse ponctuelle : Ψ = GM/(ar){1 + κ_W²/(120π²a²r²) + κ_W²H²/(80π²) ln(aHr)}, resommee en (aHr)^(κ_W²H²/(80π²)) (eq. 36, 43) ; glissement gravitationnel Ψ + Φ (eq. 37).
- **z-6** [extrait] : la resommation est introduite par « This suggests that the secular logarithms can be resummed using a variant of the renormalization group » et conclue par « the renormalization group explains the secular factors [...] and even permits their resummation » ; aucune verification a deux boucles ; statut : **procede motive par la structure des contre-termes, non demontre**.

## 1. Table de concordance [calcule] (irz_conv.py, EXIT 0)
| Espece | FW (κ_W² = 16πG) | 8bκ (programme) | Egal |
|---|---|---|---|
| Dirac (eq. 35, 42) | G/(5π) | G/(5π) | oui |
| Scalaire conforme (eq. 46) | G/(30π) | G/(30π) | oui |
| Photon (2 × Dirac, p. 6) | 2G/(5π) | 2G/(5π) | oui |
| Exposant (42) = −2γ (40) | | | oui |

## 2. Lecture [derive]
1. **Ancrage.** La chaine NOTE-133 (γ = 8, calcule) → NOTE-135 (lecture de la revue) → NOTE-137 (n = 8 a l'aveugle, c₂ Woodard = b HHR) est fermee a la source primaire : le coefficient du logarithme et l'exposant resomme y figurent explicitement pour le fermion et le scalaire, et par le rapport 1/2 pour le photon. L'identification structurelle de NOTE-137 (c₂ = b) se lit dans les eq. (26) et (39)-(40) : l'exposant est fixe par le seul contre-terme de Weyl.
2. **Statut de la puissance.** La source ne demontre pas la forme a^p : elle l'obtient en appliquant l'equation de Callan-Symanzik d'une theorie renormalisable a un calcul BPHZ d'une theorie non renormalisable, avec la substitution ln μ → ln a justifiee par l'eq. (38), et une fonction β nulle « to the order we are working ». Elle le dit avec « suggests » et « a variant of the renormalization group ». La clause « resomme » de G-V3 est donc [extrait] quant a sa forme et a son exposant, mais **conjecturale selon la source elle-meme** quant a sa validite au-dela des logarithmes dominants : qualification Z-V2.
3. **Validite temporelle.** « For as long as the de Sitter phase persists » est la seule borne declaree ; la source ne commente ni la limite a → ∞ ni un seuil p ln a ~ 1. L'usage que fait G-V3 de la puissance en 𝓘⁺ (limite Ω → 0) est donc une **extrapolation du programme**, deja consignee comme telle dans NOTE-138 (§2.4 : « formel dans son domaine ») ; rien dans la source ne la contredit ni ne la soutient.
4. **Etat et jauge.** L'etat est celui du propagateur (8), vide de Minkowski du repere conforme (vide conforme), transporte par l'invariance conforme du lagrangien de Dirac (eq. 6) ; coherent avec l'etat Hadamard de NOTE-146. La jauge n'est pas discutee : la revue 2501.05077 (NOTE-135) en traitait ; la source primaire non. Point z-3 partiellement non realise.
5. **Spin-off utile.** L'eq. (36) donne au potentiel newtonien le meme exposant que le Weyl electrique, avec ln(aHr) : le secteur scalaire (potentiel) porte la meme dimension anormale. Non exploite ici ; a consigner comme piste eventuelle (reponse d'une masse a 𝓘⁺).

```
   chaine de G-V3, clause resommee
   ----------------------------------------------------------------------------------------
   NOTE-133  gamma = 8, calcule (transport)                      [calcule]
   NOTE-135  revue Woodard 2025 : a^p, p = 8 b kappa H^2         [extrait, revue]
   NOTE-137  n = 8 a l'aveugle ; c_2 = b                         [calcule, aveugle]
   NOTE-148  source primaire FW : eq. 35, 42, 46 ; "suggests"    [extrait, source primaire]
   ----------------------------------------------------------------------------------------
   forme et exposant : ancres ; validite de la resommation : procede, non demontree ;
   limite a -> infini : extrapolation du programme (NOTE-138 §2.4), non traitee par la source
```

## 3. Verdict
**Z-V1 qualifie Z-V2.**
- **Z-V1** : la source donne 1 + c ln a avec c = 8bκ = G/(5π) pour le fermion (et G/(30π) pour le scalaire, 2G/(5π) pour le photon par le rapport 1/2), et la resommation a^p, p = c, par groupe de renormalisation (Callan-Symanzik, γ de la renormalisation de champ du graviton, β = 0, ln μ → ln a) ; la forme Ω^(−ε) de G-V3 est ancree a la source primaire.
- **Z-V2** (qualification) : la resommation est un procede presente par « suggests », sans controle d'ordre superieur ; la validite est declaree « tant que la phase de Sitter persiste », sans enonce sur la limite a → ∞. Le libelle de G-V3 doit porter : « sous la prescription de resommation de Woodard (groupe de renormalisation, logarithmes dominants, non verifiee a l'ordre superieur selon la source) ».

## 4. Confrontation a la prediction
Prediction (NOTE-147 §4) : z-1 [**realise**] ; z-2 [**realise**] ; z-3 [**partiellement realise** : BPHZ, in-in, vide conforme, non-resommation des termes finis confirmes ; discussion de jauge **absente**, contrairement a la prediction] ; z-4 [**realise**] ; z-5 [**realise**, le scalaire est traite dans la source meme, pas seulement renvoye] ; z-6 [**realise**]. Prediction realisee, a l'exception de la discussion de jauge.

## 5. Consequences (rien n'est grave)
- Libelle de G-V3 (NOTE-138 v2) : la clause resommee peut etre precisee lors d'une prochaine revision : « (Foraci-Woodard 2501.01972, eq. 42 ; procede de groupe de renormalisation, non verifie a l'ordre superieur) ». Non fait ici.
- Chaine 133/135/137 : aucune correction ; NOTE-135 §7 (« source primaire non lue ») est levee.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- Audit froid de NOTE-146 (IR-y) et de NOTE-148 (lecture aveugle des eq. 35, 40-42, 46 ; conversion).
- Lecture de [8] 2412.11022 (photon, source de l'eq. 35) et de [27] 2405.01024 (renormalisation de champ δZ, source de l'eq. 39), sous gel, si l'on veut remonter la justification du procede.
- Piste nouvelle, non armee : reponse a une masse ponctuelle a 𝓘⁺ (eq. 36, 43), meme exposant que le Weyl electrique.

## 7. Non-surclassement
[conv], audite (NOTE-150, AU-V1). Lecture d'une prepublication (pas de reference de revue relevee, EX-7). Les conversions sont [calcule] ; les enonces de statut (z-6) sont les mots de la source.
