---
id: NOTE-BORD-EON-157-IR-aa-EXECUTION
numero: 157
serie: I
branche: Q-M3 suite (IR-aa)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 157)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-156-ARMEMENT-IR-aa (sha256 3b23e317086a5dfea05054418dd7002b7c90fbbf6d63c950ceed302c70d90a65, sceau 2026-10-13T11:02:23Z)
instruments:
  - "iraa_aniso.py, sha256 f4ca1ff8eda56362ab830bc7b01363afeb126ec5ffec52ebc95ae26f0dccbf26, EXIT 0, sortie iraa_aniso_sortie.txt (cd58a18584bba0f5) ; defaut : controle numerique aa-2 par quadrature non oscillante (valeurs fausses 2,34 ; 6,30 ; −0,47) ; conserve (R-55)"
  - "iraa_aniso_v2.py, sha256 c3a30a362ea2d7f2b1bee80ae292b5507123e2471892a287e1de8c3811fc32a1, EXIT 0, sortie iraa_aniso_v2_sortie.txt (8afe1323b8720781) ; version de reference (quadrature oscillante quadosc + forme fermee)"
depend: [NOTE-BORD-EON-156-ARMEMENT-IR-aa, NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE, NOTE-BORD-EON-131-IR-t-EXECUTION]
verdict: "AA-V1 ⊕ AA-V2"
prediction_realisee: "oui"
rouvre_si:
  - "audit froid"
  - "etat non quasi-libre ; champ non conforme ; anisotropie inhomogene"
---

# NOTE-157 : IR-aa. Pour le scalaire conforme en etat homogene anisotrope, le terme αβ* du tenseur est **purement sans trace et purement anisotrope** (T₀₀ = T₀ᵢ = 0, partie isotrope nulle) ; il est entier en η pour tout etat Hadamard, et ne porte un 1/η (pole d'ordre ε⁰, propre, non compensateur) que pour l'etat non Hadamard N = 3. Verdict **AA-V1 ⊕ AA-V2**

## 0. Resume
- **aa-1** [calcule] : tenseur ameliore (ξ = 1/6) par separation de points sur un bimode ; terme αβ* (phase e^(−ik(η+η′))) : **T₀₀ = 0, T₀ᵢ = 0, T_ij = e^(−2ikη)(k_i k_j − ⅓k²δ_ij)** (facteur 1/(2k(2π)³) omis) : trace nulle, partie isotrope nulle, **seule la partie sans trace survit**, et elle survit pour chaque mode. La moyenne angulaire isotrope l'annule (YA-2 retrouve, et precise : c'est toute la structure, pas seulement la trace). Terme |β|² (phase e^(ik(η−η′))) : T₀₀ = k², T_ij = k_i k_j, independant de η (T̂ ~ s² exactement). Le flux T₀ᵢ est nul meme pour un αβ* a partie impaire : la prediction aa-1 sur T₀ᵢ est **fausse** (sans consequence).
- **aa-2** [calcule] : T_ij^tf(η) = ∫d³k/(2k(2π)³) 2Re[αβ*(k⃗) e^(−2ikη)] (k_i k_j − ⅓k²δ_ij). Pour αβ* = k^(−N) Y₂(k̂) e^(iφ) : integrale radiale ∫dk k^(3−N) e^(−2ikη) = Γ(4−N)(2iη)^(N−4) : |η|^(N−4), log pour N = 4, **1/η pour N = 3** (controle numerique v2 : η·I → 1/2, I = 1/(2η) + …, concordant avec la forme fermee 2η/(a² + 4η²) ; l'annotation « attendu −1/2 » du script est une coquille de signe, meme coquille qu'en NOTE-146 v2, la valeur est juste). Decroissance gaussienne : combinaison de erfc(iLη) et exp(−L²η²), **entiere en η**.
- **aa-3** [derive] : αβ* = f(k̂) (homogene de degre 0 en k) : le terme αβ* de w(x, x′) est l'operateur pseudo-differentiel d'ordre 0 de symbole f(k̂) applique a G_M(x, Rx′), Rx′ = (−η′, x′) ; un tel operateur preserve le front d'onde : la singularite sur le **cone reflechi** (η + η′)² = |x − x′|² est conservee. Pour une decroissance polynomiale dans une direction quelconque, l'etat n'est pas Hadamard ; Hadamard ssi decroissance rapide dans toutes les directions, et alors T_ij^tf est entier. **Critere de NOTE-146 v2 y-2 inchange par l'anisotropie.**
- **aa-4** [calcule + derive] : T̂ = s² T_plat ~ s^(N−2) Q_ij. (i) Etat Hadamard anisotrope : T̂ ~ s² × lisse : **rien**. (ii) Etat N = 3 anisotrope (non Hadamard) : T̂ ~ s¹ Q_ij, Q_ij ≠ 0 : **pole d'ordre ε⁰** dans R de (2.17), independant de l'onde (nouvelle obstruction propre a cet etat, non une compensation). (iii) Compenser le pole d'ordre ε de G-V3 exigerait Q_ij accorde a W_E,ij (reglage fin a l'ordre ε), dans un etat de toute facon non Hadamard : meme pathologie que NOTE-140 v2 et 146 v2.
- **aa-5** [derive] : Dirac et Maxwell partagent la mesure d³k/2k, la phase e^(−ik(η+η′)) et un tenseur sans trace ; les facteurs de polarisation modifient Q_ij, non l'exposant ; conclusion identique.

## 1. Resultats [calcule] (iraa_aniso_v2.py, EXIT 0)
| Terme | T₀₀ | T₀ᵢ | T_ij | Trace | Dependance en η |
|---|---|---|---|---|---|
| αβ* (e^(−ik(η+η′))) | 0 | 0 | e^(−2ikη)(k_i k_j − ⅓k²δ_ij) | 0 | e^(−2ikη) |
| \|β\|² (e^(ik(η−η′))) | k² | k_i (hors diagonale nul apres moyenne paire) | k_i k_j | 0 | aucune |

| αβ* radial | I(η) = ∫dk k^(3−N) e^(−2ikη) | T̂ ~ |
|---|---|---|
| decroissance rapide | entiere en η | s² |
| k^(−N), N ≥ 5 | C^(N−5) | s^(N−2) |
| k^(−4) | ln | s² ln s |
| k^(−3) (sin φ ≠ 0) | 1/(2iη) : 1/η | **s¹ Q_ij : pole propre d'ordre ε⁰** |

```
   etat homogene du scalaire conforme, ordre eps^0          T^w_ij (partie sans trace)      pole (2.17) ?
   -------------------------------------------------------------------------------------------------
   isotrope, quelconque                                     0 (toute structure alpha beta*)   non (YA-2)
   anisotrope, Hadamard (rapide)                            Q_ij x entiere(eta)                non
   anisotrope, non Hadamard N >= 4                          Q_ij x (C^(N-5) ou ln)             non
   anisotrope, non Hadamard N = 3                           Q_ij / eta                         OUI, ordre eps^0, propre
   -------------------------------------------------------------------------------------------------
   compensation du pole d'ordre eps de G-V3 : reglage fin Q_ij ~ W_E,ij dans un etat non Hadamard seulement
```

## 2. Lecture [derive]
1. La structure T_ij^(αβ*) ∝ (k_i k_j − ⅓k²δ_ij) explique d'un coup la correction YA-2 : pour un champ conforme, le terme d'interference des modes positifs et negatifs ne porte ni energie, ni flux, ni pression isotrope, seulement une **anisotropie de pression** ; un etat isotrope l'efface identiquement.
2. L'anisotropie ne cree aucune classe nouvelle d'etats admissibles : le critere de Hadamard (cone reflechi) est insensible a la dependance angulaire de αβ*. Dans la classe Hadamard, T̂_Γ ~ s² a l'ordre zero comme a l'ordre ε (NOTE-146 v2).
3. Le seul etat qui produise un s¹ a l'ordre zero (N = 3 anisotrope) est non Hadamard et porte son propre pole, independant de l'onde ; il ne « compense » rien par lui-meme ; en faire un compensateur exigerait un reglage fin a l'ordre ε. Le point releve par YA-2 est clos : il n'ouvre pas de breche dans G-V3, il ajoute une ligne a la table des compensateurs impossibles.

## 3. Verdict
**AA-V1 ⊕ AA-V2.**
- **AA-V1** : aucun etat homogene anisotrope Hadamard ne produit de T̂ ~ s¹ a l'ordre zero ni ne compense le pole ; classe de G-V3 inchangee.
- **AA-V2** : l'etat non Hadamard N = 3 anisotrope produit un pole propre d'ordre ε⁰, independant de l'onde ; consigne dans la table des compensateurs impossibles.

## 4. Confrontation a la prediction
Prediction (NOTE-156 §4) : aa-1 [**realise** pour la structure sans trace et la nullite isotrope ; **non realise** pour T₀ᵢ, qui est nul] ; aa-2 [**realise**] ; aa-3 [**realise**] ; aa-4 [**realise**] ; aa-5 [**realise**, derive]. Verdict predit AA-V1 ⊕ AA-V2 : **realise**.

## 5. Consequences (rien n'est grave)
- Table « qu'est-ce qui compense le pole G-V3 ? » (reprise v2 §3.4) : ligne a ajouter « etat homogene anisotrope : Hadamard, rien ; non Hadamard N = 3, pole propre d'ordre ε⁰, non compensateur (157) ».
- NOTE-146 v2 `rouvre_si` (point anisotrope) : clos par cette note (greffe v3 proposee avec IR-ac, non entee).
- Libelle de G-V3 (NOTE-138 v3) : inchange.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 6. Pistes
- Audit froid de NOTE-157 (re-derivation aveugle du tenseur αβ* sur un bimode ; script).
- Etats anisotropes **inhomogenes** (hors cadre : la structure de cone reflechi se transporte, mais le comptage local differe) : non arme.

## 7. Non-surclassement
[conv], non audite. Etats quasi-libres homogenes ; scalaire conforme ; ordre zero en ε ; transposition a Dirac et Maxwell [derive]. G-V3 reste un candidat non grave.
