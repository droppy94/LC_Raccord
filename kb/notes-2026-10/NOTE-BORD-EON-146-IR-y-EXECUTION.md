---
id: NOTE-BORD-EON-146-IR-y-EXECUTION
numero: 146
serie: I
branche: Q-M3 suite (IR-y)
reservation: 2026-10-12T15:08 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 146)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-145-ARMEMENT-IR-y (sha256 c7579805a86e8aec6bbbb1ea50cb54b9315a0302b500a60c9825b303ad9423f4, sceau 2026-10-12T15:08:07Z)
instruments:
  - "iry_state.py, sha256 d9475bd992d18f783910977ede4a55b92500094c29f75495a703639d960a92fa, 2026-10-12T15:09:00Z : EXIT 1 (sympy absent) puis EXIT 0 apres installation ; sortie iry_state_sortie.txt (129bafcb73345db0) ; defauts : integrale y-2 laissee non evaluee, controle numerique y-1 vise la partie cos (coefficient nul) au lieu de la partie sin ; conserve (R-55)"
  - "iry_state_v2.py, sha256 b72b70f006d24678eb4fb3bf79df22700060eb50cd7bc8bd759a61112647e2e0, 2026-10-12T15:09:47Z : EXIT 0, sortie iry_state_v2_sortie.txt (39621a8963eeb36e) ; version de reference"
depend: [NOTE-BORD-EON-145-ARMEMENT-IR-y, NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-140-IR-x-EXECUTION (v2), NOTE-BORD-EON-144-ACTE-REVISION-LIBELLE-G-V3]
verdict: "Y-V1 qualifie Y-V2"
prediction_realisee: "oui"
rouvre_si:
  - "audit froid"
  - "lecture des sources (E1)-(E4) contredisant un enonce utilise en y-3"
  - "etat non quasi-libre a fonction a deux points non Hadamard microlocale ; champ non conforme"
---

# NOTE-146 : IR-y. Pour un champ conforme, tout etat Hadamard est regulier en 𝓘⁺ ; seul un etat non Hadamard (cone reflechi) compenserait le pole. Verdict **Y-V1 qualifie Y-V2**

## 0. Resume
- **y-1** [calcule] : dans la classe homogene de Bogoliubov, la partie d'etat du tenseur du repere plat se comporte en T^w ~ |η|^(N−4) quand α_k β_k* ~ k^(−N) (ln |η| pour N = 4) ; pour une decroissance rapide (gaussienne), w et T^w sont des fonctions **entieres** de η. **Seul N = 3 donne T_plat ~ 1/η**, donc T̂ ~ s¹ et un pole.
- **y-2** [calcule] : le terme α β* de w(x, x′) est la fonction de Wightman de Minkowski entre x et le point reflechi (−η′, x′), convoluee par la transformee de α β* : support singulier sur le **cone reflechi** (η + η′)² = |x − x′|², qui rencontre le domaine η, η′ < 0 (exemple : η = η′ = −1, |x − x′| = 2). Pour toute decroissance polynomiale la singularite est d'ordre fini, jamais lisse : etat **non Hadamard**. Pour une decroissance rapide, w est lisse partout, y compris a travers η = 0.
- **y-3** [derive] : argument general par prolongement : un etat Hadamard sur l'eon l'est au voisinage de la surface de Cauchy η = −ε de Minkowski ; par propagation de la condition de Hadamard (E1) ou par propagation des singularites pour □ (E4), son prolongement est Hadamard sur tout Minkowski et w est lisse a travers η = 0. **Hadamard ⟹ regulier en 𝓘⁺.**
- **y-4** [calcule + derive] : T̂ = s² T_plat ~ s^(N−2) ; pole ssi N = 3, qui est non Hadamard. Dans tout etat Hadamard, T̂_Γ ~ s² × lisse : pas de pole.
- **y-5** [derive] : meme pathologie que NOTE-140 : la compensation exigerait un etat singulier sur une hypersurface nulle du volume.
- **L'hypothese d'etat de NOTE-131 est levee** : la classe de G-V3 devient « WZ integrable + Γ[g] dans un etat Hadamard ». Qualification Y-V2 : y-3 repose sur des enonces exterieurs cites de memoire.

## 1. Resultats [calcule] (iry_state_v2.py)
| Sous-question | Resultat |
|---|---|
| y-1 (a), α β* gaussien | I₁(η), I₃(η) : combinaisons de erf(iLη) et exp(−L²η²), entieres en η |
| y-1 (b), α β* = k^(−N) e^(iφ) | ∫dk k^(m−N) e^(2ikη) ~ Γ(m−N+1) e^(±iπ(m−N+1)/2)/(2|η|)^(m−N+1) ; T^w (m = 3) ~ |η|^(N−4) ; N = 4 : ln |η| ; N ≥ 5 : C^(N−5), non lisse |
| y-1, controle numerique N = 3, m = 3 | η × ∫dk sin(2kη) e^(−k/1000) = 0,49999, 0,49995, 0,49969 pour η = −0,1, −0,05, −0,02 : → 1/2, soit T^w = 1/(2η) + … (l'annotation « −1/2 » du script est une coquille de signe, la valeur est juste) |
| y-2, α β* = 1 | ∫d³k/(2k(2π)³) e^(−ik(η+η′)) e^(ik·(x−x′)) = (1/4π²)/(|x − x′|² − (η + η′)²) : cone reflechi |
| y-2, N = 1 (mesure k dk, regularisation e^(−ak), a → 0) | ∫dk sin(kr) cos(kT) = r/(r² − T²) : singulier en r = T |
| y-4 | T̂ ~ s^(N−2) ; pole ssi N = 3 |

## 2. Lecture [derive]
1. **Classe homogene.** Pour un etat gaussien homogene, la seule partie de w sensible a η = 0 est le terme d'interference α β* e^(−ik(η+η′)). Sa regularite en η → 0 est celle de la transformee de Fourier de α β* : rapide ⟺ lisse. Or la condition de Hadamard sur le domaine η < 0 exige, par y-2, que le cone reflechi ne porte aucune singularite, donc que α β* soit a decroissance rapide. Dans cette classe, **Hadamard ⟺ regulier en 𝓘⁺** [calcule, modulo la definition microlocale de Hadamard].
2. **Classe generale.** (E1) [cite de memoire] : si ω₂ est Hadamard au voisinage d'une surface de Cauchy, elle l'est sur tout le domaine de dependance ; la surface η = −ε est de Cauchy pour Minkowski entier ; le prolongement de w par le probleme de Cauchy (bisolution) existe (Cauchy hyperbolique, meme argument que NOTE-142) et est Hadamard sur Minkowski, donc w est lisse a travers η = 0. Variante (E4) : une singularite de w(·, x′) portee par η = 0 se propagerait le long des bicaracteristiques nulles de □, qui entrent dans η < 0, en contradiction avec la lissite sur le domaine. Dans les deux cas, **Hadamard ⟹ regulier**. Le pas de la fonction a une variable a la fonction a deux variables (regularite jointe pres de la diagonale sur η = 0) est couvert par (E1), non par (E4) seul : c'est le point a verifier a la lecture.
3. **Champ conforme et repere.** Le transport du vide conforme et de la condition de Hadamard entre ĝ et g est l'enonce (E3) ; le terme anomal local du transport est celui de WZ, deja compte. Pour Dirac et Maxwell, la structure (mesure d³k/2k, phase e^(−ik(η+η′)), cone reflechi) est identique ; les facteurs de polarisation ne changent pas l'exposant.
4. **Ordre ε.** Le tenseur d'ordre ε de Γ[g] = noyau retarde de Minkowski (lisse hors coincidence, singularite integrable) applique a h entier en s, plus termes lineaires en ∂∂w lisses : lisse en η = 0 ; T̂ ~ s². Le comptage de NOTE-131 t-2 s'applique.
5. **Parallele.** NOTE-140 : φ_h compensateur singulier sur un cone nul du volume. IR-y : etat compensateur singulier sur le cone reflechi, hypersurface nulle du volume. Dans les deux secteurs, compenser le pole exige de sortir de la classe Hadamard.

```
   etat du repere plat (champ conforme)        w a travers eta = 0      T-hat_Gamma      pole ?
   ------------------------------------------------------------------------------------------
   alpha beta* a decroissance rapide (Hadamard)  entiere                 s^2 x lisse      non
   alpha beta* ~ k^-N, N >= 5 (non Hadamard)     C^(N-5)                 s^(N-2)          non
   alpha beta* ~ k^-4 (non Hadamard)             ln                      s^2 ln s         non
   alpha beta* ~ k^-3 (non Hadamard)             1/eta                   s^1              OUI (seul cas)
   Hadamard general                              lisse (E1 / E4)         s^2 x lisse      non
```

## 3. Verdict
**Y-V1 qualifie Y-V2.**
- **Y-V1** : pour un champ conforme, tout etat Hadamard sur l'eon est regulier en 𝓘⁺ dans le repere plat ; T̂_Γ ~ s² × lisse ; aucun etat admissible ne compense le pole ; le seul comportement compensateur (T_plat ~ 1/η, N = 3) est non Hadamard, singulier sur une hypersurface nulle du volume. L'hypothese d'etat de NOTE-131 est levee : classe de G-V3 « **WZ integrable + Γ[g] dans un etat Hadamard** ».
- **Y-V2** (qualification) : l'argument general y-3 repose sur (E1) ou (E4), cites de memoire (Fulling-Narcowich-Wald 1981, Radzikowski 1996, Hormander) ; dans la classe homogene, le resultat est calcule.

## 4. Confrontation a la prediction
Prediction (NOTE-145 §4) : y-1 exposant |η|^(N−4), N = 3 critique [**realise**] ; y-2 cone reflechi, non Hadamard pour toute loi de puissance, Hadamard ssi rapide [**realise**] ; y-3 [derive] via (E1)/(E4) [**realise**, avec la precision du §2.2 sur la regularite jointe] ; y-4 T̂ ~ s² en etat Hadamard [**realise**] ; y-5 parallele [**realise**]. **Prediction realisee.**

## 5. Consequences (rien n'est grave)
- Classe de G-V3 : « WZ integrable + Γ[g] dans un etat Hadamard » ; les hypotheses restantes sont de **cadre** (fond de Sitter exact, premier ordre en ε et bκ, une boucle, passe adiabatique pour la convergence du noyau retarde, resommation non demontree), non d'etat.
- Libelle de NOTE-138 v2 : a reviser une fois cette note auditee (remplacer « Γ[g] etat regulier » par « Γ[g] etat Hadamard »). Non fait ici.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- **Audit froid** de NOTE-146 (y-1, y-2 en cecite stricte ; audit du script ; verification de l'enonce (E1) sur source).
- **Lecture sous gel** de Fulling-Narcowich-Wald 1981 et Radzikowski 1996 (lever la qualification Y-V2).
- Lecture de Foraci-Woodard 2501.01972 (piste 3 de la sequence).

## 7. Non-surclassement
[conv], non audite. Etats quasi-libres ; champ scalaire conforme comme representant ; premier ordre en ε ; enonces (E1)-(E4) cites de memoire (EX-8), numeros et dates non certifies. La convergence du noyau retarde (passe adiabatique) reste une hypothese de cadre.
