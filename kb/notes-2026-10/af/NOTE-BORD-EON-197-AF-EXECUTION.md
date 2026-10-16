---
id: NOTE-BORD-EON-197-AF-EXECUTION
numero: 197
serie: I
branche: G-V3 / Q-M3 (chantier AF, regularite formelle des termes anomaux)
reservation: 2026-10-16T13:58:01Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 197)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-196-ARMEMENT-AF.md, sha256 4a31479204b535eb, sceau NOTE-196-SCEAU.txt 2026-10-16T14:00:04Z"
script: "af_check.py (v2, reference) et af_check_sortie.txt ; v1 conservee (af_check_v1_defectueux.py et sa sortie : signe de la partie spatiale du Weyl, symboles de calibration sans attribut reel, jets de F manquants) ; empreintes au sceau de cloture"
---

# AF, execution : G-V3 et M-V3 au sens formel de Friedrich

## VERDICT : AF-V1. Prediction (informee) realisee, y compris (iii), declaree faible.
Les deux candidats deviennent des irregularites **formelles** des seconds membres, au sens du theoreme 3.1 de Friedrich, independantes de toute solution :
- **G-V3** : le second membre de (2.17) contient le terme **-kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho) / Omega**, avec E^n_ab = n^c n^d W_acbd. Son coefficient est une fonction des seules inconnues (n, W) ; il ne s'annule que si la partie electrique de W relative a n est nulle. Le systeme est formellement regulier si et seulement si b = 0.
- **M-V3** : l'equation de Maxwell rescalee recoit un **pole** d^a F_ab = 4 e^2 beta_* n^a F_ab / Omega + O(beta_*^2), plus fort que le log de M-V3. Le second membre de (2.17) contient du ln Omega, et tous ses coefficients ne s'annulent que si F = 0 a scri (champs reels). Le systeme est formellement regulier si et seulement si beta_* = 0, ou F = 0 au bord.
La reserve G-CAL-a (NOTE-163 v2 : « un pole sur une solution prouve l'irregularite si les autres inconnues sont lisses ») est levee : le pole est un terme formel du second membre.

## 1. AF-1 : partie c, b sigma C^2 (script, partie AF-1)
Cadre du gel : premier ordre autour de g = eta ; C = Omega W (W tenseur de Weyl generique, parametre par E_ij, B_ij relativement a l'axe x0, traces et identite cyclique verifiees) ; d_a d_b Omega = s eta_ab, d s = 0, (3.8) a l'ordre zero ; jets de W jusqu'a l'ordre 3.
- **Identite hors couche** : d^c d^d (Omega W_acbd) = n^d D_bda + n^c D_acb + Omega d^c D_acb + (d^c d^d Omega) W_acbd, avec D_abc = d^d W_abcd la divergence. Le dernier terme vaut s eta^cd W_acbd = 0 (trace nulle) a cet ordre. **La partie en ln Omega de T est donc sigma x Lin(D, dD)**.
- That est sans trace (identite) ; sa plus basse puissance est Omega^1, de coefficient **exactement -c0 b E^n_ab** (concorde avec « That_ij = -+ 8 b Omega W_sisj », NOTE-128).
- **Second membre de (2.17)** : plus basse puissance **Omega^-1**, aucun Omega^-2 ; coefficient **exactement** -kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho) sur les 24 composantes ; il ne depend que de (n, E, B, lambda), pas des jets de divergence.
- **Logarithmes** : 72 termes, aux ordres Omega^0 ln Omega, Omega ln Omega, Omega^2 ln Omega. Les contraintes de divergence ont ete resolues sur les jets d'ordre 1, 2 et 3 (16, 58 et 136 variables eliminees) : **tous les termes en ln Omega s'annulent quand div W = 0**. Dans le vide, apres reduction d'ordre (NOTE-133), il n'y a pas de log a l'ordre b. Avec une matiere classique (div W = J != 0), il reste ln Omega x Lin(J), d'ordre kappa^2 b (concorde avec S-b, NOTE-128).
- **Calibration (AF-3 i)** : sur n = (1,0,0,0), avec E_yy = e et c0 = -8 (c0 de irr_c.py), le pole de R_ysy vaut 8 b kappa e / Omega. Avec e = W_E,yy|scri = -B k^3 cos kx / 2 (irr_c_ctrl), on obtient **-4 b kappa B k^3 cos kx / Omega, valeur exacte de NOTE-125**.

## 2. AF-2 : sigma F^2 (script, partie AF-2)
Couplage effectif 1/e^2_eff = 1/e^2 - 4 beta_* sigma, forme de S2 (NOTE-98 : beta_* = -beta~/(2e^2)).
- **Equation de Maxwell rescalee** : d^a [(1/e^2 - 4 beta_* sigma) F_ab] = 0 donne, au premier ordre en beta_*, d^a F_ab = 4 e^2 beta_* n^a F_ab / Omega. Le **pole Omega^-1 dans l'equation de matiere** a pour coefficient la partie electrique de F relative a n.
- That = (1/e^2 + 4 beta_* ln Omega) Omega^2 M_ab[F ; eta], M sans trace. Le second membre de (2.17) a pour plus basse puissance Omega^0, avec des logs a Omega^0 ln Omega et Omega ln Omega. Le coefficient de Omega^0 ln Omega vaut **exactement** kappa beta_* [6 (n_nu M_lambda rho - n_lambda M_nu rho) + 2 (eta_lambda rho (n.M)_nu - eta_nu rho (n.M)_lambda)].
- **Calibration (AF-3 ii)** : sur le champ uniforme F_12 = B0, n = (1,0,0,0), on obtient **exactement** les coefficients de NOTE-98 : -kappa beta~ B0^2/e^2 sur (1,0,1) et (2,0,2), +2 kappa beta~ B0^2/e^2 sur (3,0,3).
- **Condition d'annulation (AF-3 iii)**, dans le repere de n : les coefficients de ln Omega sont des combinaisons de (E_iE_j + B_iB_j)_tf (partie spatiale sans trace du tenseur de Maxwell) et du vecteur de Poynting E x B. Tous s'annulent si et seulement si les deux sont nuls. Les seules solutions sont complexes (B = +- i E). Pour des champs reels, S = EE^T + BB^T est semi-defini positif de rang au plus 2 : S_tf = 0 force S = 0, donc **E = B = 0**.
- **Comparaison avec NOTE-113/114** (critere sur solution <B_iB_j>_tf = <E_iE_j>_tf, verifie par les ondes d'helicite pure) : la condition formelle est **plus forte**. La difference vient de la distinction formel / sur solution (precedent xii) : sur une solution, F lui-meme recoit, par le pole de l'equation de Maxwell, des corrections en ln Omega qui peuvent compenser celles de (2.17) ; le critere de Friedrich ne l'admet pas.

## 3. AF-4 : bilan
| Canal | Ou est la singularite formelle | Coefficient | Regulier ssi |
|---|---|---|---|
| G-V3 (b sigma C^2) | (2.17), Omega^-1 | -kappa c0 b n_[nu E^n_lambda]rho (x2) | b = 0 (ou E^n = 0 au bord) |
| M-V3 (sigma F^2) | equation de Maxwell, Omega^-1 ; (2.17), ln Omega | 4 e^2 beta_* n^a F_ab ; kappa beta_* (6 n_[nu M_lambda]rho ..., + 2 eta ...) | beta_* = 0 (ou F = 0 au bord) |
- G-V3 et M-V3 sont des enonces formels du type du theoreme 3.1 : le premier pour tout champ conforme (b > 0), le second pour la matiere chargee sans masse au bord (beta != 0 ; dans CCC + M a M2 = 2, la masse physique y Omega H_r tend vers 0, ce qui correspond au cadre C-M1 de Q-M3).
- Sur solution, le pole formel de G-V3 *produit* la divergence en ln de W (NOTE-133) : il n'y a pas de contradiction. La faiblesse logique relevee par G-CAL-a disparait, puisque l'irregularite ne suppose plus que les autres inconnues soient lisses.
- Pour CCC + M, le cadre de NOTE-98 (« aucun champ electromagnetique classique coherent ne doit atteindre scri ») devient, au sens formel : **aucun champ electromagnetique non nul a scri**, sous C-M1.

## 4. Limites
- Premier ordre en perturbation autour de g = eta (de Sitter conformement plat) ; produits L W, S W ecartes.
- Partie c de Wess-Zumino : forme fermee lineaire c0 b d d (sigma C) ; les termes en R^cd sigma C_acbd, d'ordre 2, sont ecartes. Sous forme formelle, ils contiendraient Omega ln Omega x L W : irreguliers aussi, mais a l'ordre suivant.
- Partie a (Euler) de Wess-Zumino non traitee au sens formel (NOTE-131 sur solution reste en vigueur) ; partie non locale Gamma[g] non traitee formellement (classe Hadamard sur solution, NOTE-146 v3).
- AF-2 : champ F classique (ou valeur moyenne) ; etats quantiques, termes non locaux de S2 (S_flat) et completion non WZ hors champ (comme NOTE-98 §3).
- Le facteur c0 (et donc le signe) suit la convention de T (NOTE-128) ; l'existence du pole n'en depend pas.
- Resommation, jauge gravitationnelle (objection 1 de NOTE-163) : non touchees.

## 5. Propositions (non entees ; audit d'abord)
- **NOTE-163 v3** (piece d'appareil pour le relecteur) : remplacer le point de lecture G-CAL-a par l'enonce formel (§1) et ajouter une ligne a la chaine : « pas 2 bis : le pole est un terme formel de (2.17), de coefficient -kappa c0 b n_[nu E^n_lambda]rho (NOTE-197) ».
- **NOTE-138 v5** (libelle de G-V3) : ajouter « formellement, au sens du theoreme 3.1 de Friedrich : le systeme conforme couple a l'action anomale locale est regulier ssi b = 0 ».
- **S27-02 v4 ou note Q-M3** : M-V3 au sens formel (pole de l'equation de Maxwell ; ln Omega dans (2.17) ; regulier ssi beta = 0 ou F = 0 au bord, sous C-M1).

## 6. Non-surclassement
Rien de grave. G-V3 reste un candidat (desormais formel, au premier ordre) ; M-V3 un candidat conditionnel (C-M1). RG-4 refutee a titre provisoire ; CCC + M ouverte ; p_Q non fixe, N non chiffre, noyau {A4 ; A2★ ; N} inchange.
