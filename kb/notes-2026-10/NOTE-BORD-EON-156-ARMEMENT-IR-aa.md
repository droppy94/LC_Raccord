---
id: NOTE-BORD-EON-156-ARMEMENT-IR-aa
numero: 156
serie: I
branche: Q-M3 suite (IR-aa)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 156)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, sous-questions, espace des verdicts et prediction figes AVANT tout calcul)
decision: operateur (Thierry), 2026-10-13 12:53 heure de Paris (« traite les elements marques en priorite 1 », piste 3 de la reprise v2 §5.1)
depend: [NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE, NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-125-IR-r-EXECUTION (v2)]
issue_attendue: "delimitation (etat homogene anisotrope a l'ordre zero : nouvelle obstruction, compensation, ou rien)"
rouvre_si:
  - "audit froid de NOTE-157"
  - "etat non quasi-libre ; champ non conforme ; anisotropie non homogene (inhomogene)"
---

# NOTE-156 : armement de IR-aa. La partie sans trace de T^w, pour un etat homogene anisotrope du champ conforme a l'ordre zero, produit-elle un terme en s¹ dans (2.17) ?

## 0. Origine
L'audit YA-2 (NOTE-150) a corrige l'objet de NOTE-146 v1 : pour le scalaire conforme (ξ = 1/6) en etat homogene **isotrope**, le terme αβ* de ⟨T_μν⟩ est identiquement nul a l'ordre zero en ε, de sorte que T^w est constant en η et T̂ = s² T^w ne porte aucun s¹. YA-2 a releve le point non instruit : pour un etat homogene **anisotrope** (coefficients de Bogoliubov dependant de la direction k̂), la partie sans trace de T_ij n'a aucune raison de s'annuler par moyenne angulaire ; elle est la seule survivante a ξ = 1/6. NOTE-146 v2 l'a portee en `rouvre_si`. Question : dans cette classe, existe-t-il un etat qui produise T̂ ~ s¹ a l'ordre zero (terme polaire independant de l'onde, donc **nouvelle obstruction** de type G-V3 d'ordre ε⁰), ou qui compense le pole d'ordre ε de G-V3, et cet etat est-il admissible (Hadamard) ?

## 1. Cadre (fige)
- Scalaire conforme φ (ξ = 1/6) sur Minkowski du repere plat (g = η, ordre zero en ε), s = −η > 0 sur l'eon, 𝓘⁺ = {η = 0}. Tenseur ameliore : T_μν = ∂_μφ∂_νφ − ½η_μν(∂φ)² − (1/6)(∂_μ∂_ν − η_μν□)φ² (signature −+++ ; □ = −∂_η² + Δ) ; sans trace sur couche.
- Etat quasi-libre homogene de Bogoliubov : modes φ_k = [α(k⃗) e^(−ikη) + β(k⃗) e^(ikη)] e^(ik⃗·x⃗)/√(2k(2π)³), |α|² − |β|² = 1, α et β dependant de la **direction** k̂ et du module k. Fonction a deux points w(x, x′) = ω₂ − H ; la partie dependant de l'etat de w est ∫d³k/(2k(2π)³) [ (|α|²+|β|²−1) e^(−ik(η−η′)) + ... + α β* e^(−ik(η+η′)) + c.c. ] e^(ik⃗·(x⃗−x⃗′)) (forme exacte a ecrire dans le script).
- Comptage (NOTE-131 t-2, 146 v2 y-4) : T̂ = s² T_plat ; pole dans R de (2.17) ssi T̂ ~ s¹ Y avec Y(0) ≠ 0, c'est-a-dire T_plat ~ 1/η ; un terme s² × lisse ne donne rien ; un terme s² × (1/η) × anisotrope donne s¹ × anisotrope.
- Admissibilite (NOTE-146 v2 y-2) : le terme αβ* de w(x, x′) est singulier sur le cone reflechi (η + η′)² = |x⃗ − x⃗′|² pour toute decroissance polynomiale de αβ* en k ; Hadamard ssi αβ* a decroissance rapide (pour chaque direction). L'anisotropie ne change pas ce critere (a verifier au calcul, aa-3).
- Convention de signe physique Carroll-Wald (NOTE-138) ; H = 1.

## 2. Sous-questions
- **aa-1 (structure)** : calculer ⟨T_μν⟩^w pour l'etat ci-dessus a l'ordre zero en ε, separer le terme |β|² (independant de η) et le terme αβ* (dependant de η), et donner la forme de la partie sans trace spatiale T_ij − ⅓δ_ij T_kk du terme αβ*. Prediction : elle est proportionnelle a ∫d³k k (k̂_i k̂_j − ⅓δ_ij) Re[αβ*(k⃗) e^(−2ikη)] (a un facteur numerique pres), tandis que la partie isotrope du terme αβ* s'annule identiquement (retrouve YA-2). Verifier la trace nulle et la conservation. Calculer aussi T_0i (flux) : attendu ∝ ∫d³k k k̂_i Im ou Re[αβ* e^(−2ikη)], non nul pour un αβ* a partie impaire en k̂.
- **aa-2 (comportement en η → 0)** : pour αβ*(k⃗) = k^(−N) Y(k̂) e^(iφ) avec Y de moment ℓ = 2 (partie sans trace), comportement de T_ij^tf en η → 0⁻ : attendu |η|^(N−4) (ln pour N = 4), donc **1/η pour N = 3** (sin φ ≠ 0) ; pour une decroissance rapide, entier en η.
- **aa-3 (admissibilite)** : le critere de Hadamard de y-2 (cone reflechi) est-il inchange par l'anisotropie ? Attendu : oui, le terme αβ* reste G(x, Rx′) convolue par la transformee de αβ*(k⃗) ; une decroissance polynomiale dans une direction suffit a creer une singularite hors diagonale ; Hadamard ssi decroissance rapide dans toutes les directions, et alors T_ij^tf est entier en η.
- **aa-4 (effet sur (2.17))** : (i) etat Hadamard anisotrope : T̂ ~ s² × lisse, **rien** ; (ii) etat N = 3 anisotrope (non Hadamard) : T̂ ~ s¹ × Y_ij(k̂-moyenne), donc un **pole d'ordre ε⁰** dans R de (2.17), independant de l'onde : ce serait une obstruction supplementaire, non une compensation ; (iii) compenser le pole d'ordre ε de G-V3 exigerait d'accorder la partie sans trace de l'etat a W_E (reglage fin a l'ordre ε), dans un etat de toute facon non Hadamard.
- **aa-5 (transposition)** : le resultat vaut-il pour Dirac et Maxwell ? Attendu : meme structure (mesure d³k/2k, phase e^(−ik(η+η′)), facteurs de polarisation), meme exposant ; conclusion identique, [derive].

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AA-V1** | Aucun etat homogene anisotrope **Hadamard** du champ conforme ne produit de T̂ ~ s¹ a l'ordre zero ni ne compense le pole ; la partie sans trace survit mais est entiere en η pour une decroissance rapide ; classe de G-V3 « WZ integrable + Γ[g] dans un etat Hadamard » **inchangee**. |
| **AA-V2** | Comme AA-V1, et de plus l'etat non Hadamard N = 3 anisotrope produit un pole d'ordre ε⁰ independant de l'onde : **nouvelle obstruction** dans la classe non Hadamard, qui n'affecte pas G-V3 (classe Hadamard) mais s'ajoute a la liste des « compensateurs impossibles » ; a consigner. |
| **AA-V3** | Il existe un etat **Hadamard** anisotrope donnant T̂ ~ s¹ a l'ordre zero (par exemple parce que l'anisotropie modifie le critere du cone reflechi) : obstruction nouvelle d'ordre ε⁰ **et** compensation possible de G-V3 par reglage : libelle de G-V3 a reviser. |
| **AA-V4** | La partie sans trace du terme αβ* s'annule aussi pour un etat anisotrope (structure du tenseur ameliore) : point de YA-2 clos par le calcul, rien a consigner. |
| **AA-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**AA-V1 ⊕ AA-V2.**
- aa-1 : partie sans trace ∝ ∫d³k k (k̂_i k̂_j − ⅓δ_ij) Re[αβ* e^(−2ikη)] ; partie isotrope du terme αβ* nulle (YA-2 retrouve) ; trace nulle ; conservation verifiee ; T_0i non nul pour une partie impaire.
- aa-2 : |η|^(N−4) ; 1/η ssi N = 3 et sin φ ≠ 0 ; entier pour une decroissance rapide.
- aa-3 : critere inchange ; Hadamard ssi decroissance rapide dans toutes les directions.
- aa-4 : (i) rien ; (ii) pole d'ordre ε⁰ pour N = 3 anisotrope, non Hadamard ; (iii) compensation = reglage fin dans un etat non Hadamard.
- aa-5 : transposition [derive].
- Consequence : classe de G-V3 inchangee ; table « qu'est-ce qui compense le pole » de la reprise v2 §3.4 completee d'une ligne « etat homogene anisotrope Hadamard : rien ; non Hadamard N = 3 : pole propre d'ordre ε⁰, non compensateur ».

## 5. Instruments prevus
Script `iraa_aniso.py` (sympy ; mpmath pour un controle numerique), empreinte avant execution : aa-1 (tenseur ameliore sur le mode, somme sur k⃗ avec αβ*(k⃗) general, decomposition en trace et sans trace, conservation), aa-2 (integrale radiale ∫dk k^(3−N) e^(−2ikη) et son exposant ; controle numerique N = 3), aa-3 (forme fermee du terme αβ* pour αβ* = Y₂(k̂) : singularite sur le cone reflechi), aa-4 (comptage s² T_plat). Aucune lecture de source.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v3) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Etats quasi-libres homogenes ; scalaire conforme comme representant ; ordre zero en ε.
