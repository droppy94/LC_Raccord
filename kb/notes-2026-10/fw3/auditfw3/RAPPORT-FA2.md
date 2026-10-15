# RAPPORT FA-2 : audit adverse de NOTE-BORD-EON-191 (FW3), fw3_check.py et fw3_check_sortie.txt

**Avertissement de reprise.** Ce rapport reprend le travail d'une premiere instance FA-2 (meme role, meme consigne) interrompue par une limite de quota avant redaction. Ses variantes (dossier `work_fa2/` : `fw3_fa2_lib.py`, `var_E2_*`, `var_E3_*`, `var_E3c_*`, `var_E4_*`, `var_E5_*`) ont ete relues de facon critique ligne a ligne, puis re-executees (sorties de controle dans `work_fa2/rerun/`). L'instance de reprise a ajoute trois variantes : `var_E1_conventions.py`, `var_E2b_point_fixe_S.py`, `var_E4b_poids_general.py` (sorties `var_E1_sortie.txt`, `var_E2b_sortie.txt`, `var_E4b_sortie.txt`). Perimetre lu : la consigne FA-2, son annexe FA-1, la note 191, le script et sa sortie. Rien d'autre dans `/home/claude/FW3` n'a ete ouvert.

## 0. Reproduction et etat des variantes

| Piece | Re-execution | Resultat |
|---|---|---|
| `fw3_check.py` (original, non modifie) | `rerun/fw3_check_sortie_rerun.txt`, 54 s | sortie identique octet pour octet (hors lignes vides) a `fw3_check_sortie.txt`. La note annonce 43 s : ecart de machine, sans portee. |
| `fw3_check_copie.py` (copie de la 1re instance) | `diff` | identique a l'original |
| `var_E5_coefficient_main.py` | `rerun/var_E5_sortie_rerun.txt` | identique a `var_E5_sortie.txt` |
| `var_E3c_sensibilite.py` | `rerun/var_E3c_sortie_rerun.txt`, 95 s | identique a `var_E3c_sortie.txt` |
| `var_E4_poids_conforme.py` | `rerun/var_E4_sortie_rerun.txt` | parties w = 1, 2, 0, 1/2 identiques ; la partie « w symbolique » et la partie « jauge singuliere » **ne terminent pas** (tuees a 600 s, `powsimp` sur Omega^w). La sortie de la 1re instance etait donc tronquee ; remplacee par `var_E4b` (voir E4). |
| `var_E3_YetDeuxComposantes.py` | `rerun/var_E3_sortie_rerun.txt`, 142 s | identique a `var_E3_sortie.txt` (hors temps d'execution) |
| `var_E2_substitutions.py` | non relance (219 s) | code relu ; il reutilise `fw3_fa2_lib.py`, dont le mode `orig` reproduit exactement C1 et C2 de l'original (verifie par E2 (i), (ii-a)). |

**Relecture de `fw3_fa2_lib.py`.** Copie parametree fidele de l'original (memes Christoffel, meme tenseur, meme `cotton_source`, meme reduction), avec quatre ajouts : (i) `DDS_FACTOR` (facteur Omega ou Omega^-1 dans (2.15)) ; (ii) `n_comp` composantes complexes, quartique lambda_h (Sum |H_i|^2)^2 ; (iii) `add_Y` : Omega^2 Y_ab, Y symetrique generique avec derivees dY generiques ; (iv) `cubic` (mu phi^3 ou mu |H|^3) et `majorana_like` (M Omega eta_ab B). `reduce_nn` accepte le choix de la variable eliminee et multiplie par Omega^6 (au lieu de 4) avant division polynomiale. Je n'y ai trouve aucune erreur.

---

## E1. Conventions

Verification independante dans `var_E1_conventions.py` (Omega(x) fonction **generique**, ghat = Omega^-2 eta, calcul direct des Christoffel et de Ricci, sans aucun code de la note). Sortie `var_E1_sortie.txt` :

| Relation | Resultat |
|---|---|
| Gammahat^a_bc = -(delta^a_b n_c + delta^a_c n_b - eta_bc n^a)/Omega | True |
| Rhat_ab = 2 Omega^-1 dd Omega + (Omega^-1 box Omega - 3 Omega^-2 \|dOmega\|^2) eta | True |
| Rhat = Omega^2 (6 Omega^-1 box Omega - 12 Omega^-2 \|dOmega\|^2) | True |
| de Sitter Omega = -sqrt(lambda/3) t : Rhat_ab - Rhat ghat/2 + lambda ghat = 0, Rhat = 4 lambda, \|dOmega\|^2 = -lambda/3 | True (signe de la convention de Friedrich : lambda > 0 donne dS et scri du genre espace) |
| (2.14) avec That **defini** par Einstein et s := box Omega / 4 (g plat) | identite True |
| (3.8) \|dOmega\|^2 = -lambda/3 + 2 Omega s + (kappa/12) That (trace physique = Omega^2 Str) | identite True |
| (2.15) avec facteur **Omega^-1** devant d_c That | identite **True** |
| (2.15) avec facteur **Omega^+1** devant d_c That (forme du script et de la consigne FA-1) | identite **False** |

Derivation a la main de (2.15), qui confirme : en derivant 2 Omega s = \|dOmega\|^2 + lambda/3 - (kappa/12) That et en utilisant (2.14),

    2 n_c s + 2 Omega d_c s = 2 n^a (s eta_ac - Omega L_ac + (kappa/2) Omega T*_ac) - (kappa/12) d_c That
    =>  d_c s = - n^a L_ac + (kappa/2) n^a T*_ac - (kappa/24) Omega^-1 d_c That.

**Constat E1-a (erreur reelle, sans incidence).** `fw3_check.py`, fonction `dds`, ecrit `- kap/24*W*(2*W*n[c]*Str + W**2*dStr[c])`, soit -(kappa/24) Omega d_c(Omega^2 Str) : le facteur correct est Omega^-1. La forme fautive figure deja dans la consigne FA-1 ((2.15) « - (kappa/24) Omega nablahat_a That ») : l'erreur vient donc de l'armement, et le script l'a reprise telle quelle. Elle rend (2.15) incoherente avec (3.8) a l'ordre Omega^2. Effet sur les conclusions : nul (E2 (ii) : coefficients Omega^-3, Omega^-2, Omega^-1 identiques avec les deux facteurs), parce que ce terme est d'ordre Omega^0 (forme correcte) ou Omega^2 (forme fautive) et n'entre dans la source qu'a travers des facteurs f = O(Omega^2).

**Tenseur d'energie-impulsion.** Recalcul a la main a partir de L = -ghat^{ab}(D_a H)* D_b H - V - xi Rhat \|H\|^2 : T_ab = -2 (-g)^{-1/2} delta(sqrt(-g) L)/delta g^{ab} donne

    T_ab = (D_a H)* D_b H + (D_b H)* D_a H - ghat_ab (\|DH\|^2 + V) + 2 xi (Ghat_ab + ghat_ab boxhat - nablahat_a nablahat_b) \|H\|^2,

ce qui est exactement le code (`Vxi_base = 2*absH2`, terme xi (Ghat f + ghat box f - nabla nabla f)). Pour le scalaire reel, T de Friedrich (3.2) avec 1/2. Coherent avec H = (phi_1 + i phi_2)/sqrt 2.

**Une erreur de signe ou de facteur change-t-elle la combinaison ?** Oui, et de facon detectable : le coefficient final est 2 beta + alpha n.n (voir E5) ; changer le signe d'Einstein (lambda -> -lambda) ou le facteur 2 du terme xi deplacerait 4 lambda xi ou 2 lambda/3 ; mais toutes les conventions effectivement codees sont confirmees ci-dessus, et la calibration C1 (theoreme 3.1, m^2 = 2 lambda/3) ainsi que la calibration xi = 1/6, m = 0 contraignent les deux coefficients independamment. La seule erreur trouvee (E1-a) ne touche pas la combinaison.

---

## E2. Procedure formelle

**Ordre des substitutions.** Dans `Jet.D`, la derivee de n_a est remplacee par (2.14) et celle de s par (2.15) au moment meme de la derivation ; la reduction modulo (3.8) est appliquee en fin de chaine, comme division polynomiale en n0 apres multiplication par Omega^K (K = 4 dans l'original ; plus basse puissance avant reduction : -2, donc K suffit, `var_E2_sortie.txt`). Le generateur contient bien les termes 2 Omega s et (kappa/12) Omega^2 Str, si bien qu'un terme n0^2 Omega^-2 alimente correctement les ordres Omega^-1 (via -2 s) et Omega^0 (via Str). Le reste de la division est unique a variable eliminee fixee.

**Invariance par rapport au choix de la variable eliminee.** E2 (iii) : reduction par n1^2 au lieu de n0^2, memes conclusions K-6 (True, True, True).

**Facteur de (2.15).** E2 (ii-a)/(ii-b) : coefficients singuliers identiques (« identiques : True »).

**Circularite des symboles generiques S_ab, Str.** C'est le point adverse principal de E2 : avec xi != 0, That contient des derivees secondes de Omega (via Ghat, boxhat, nablahat nablahat), donc depend a priori de S = T* lui-meme. `var_E2b_point_fixe_S.py` mesure cette dependance (`var_E2b_sortie.txt`) :

- avant reduction, That_ab ne contient **ni S_ab, ni L_ab, ni s, ni Str** : les termes en dd Omega s'annulent exactement dans xi (Ghat f + ghat boxhat f - nablahat nablahat f). Verification a la main avec f = Omega^2 F : Ghat f contient 2 Omega F dd Omega - 2 Omega F box Omega eta ; -nablahat nablahat f contient -2 Omega F dd Omega ; ghat boxhat f contient +2 Omega F box Omega eta. Somme nulle.
- apres reduction modulo (3.8), s entre dans That a l'ordre Omega^1 et Str a l'ordre Omega^2 (dans That_ab comme dans Omega^-2 That).

Donc l'equation implicite Str = Omega^-2 That[jets ; s, Str] est de la forme Str = A + Omega s B + Omega^2 C Str, resolue par Str = (A + Omega s B)/(1 - Omega^2 C), reguliere ; et S_ab est une fonction explicite des jets, de s et de Str. Il n'y a **pas de circularite vicieuse**. De plus (E2 (v)) aucun des symboles S, dS, Str, s, L, dL n'apparait dans les coefficients singuliers : leur traitement generique est sans effet sur le verdict.

**Remarque.** La note (§2) dit que les termes xi sont « exprimes par (2.3), (2.4), (2.14) ». C'est exact dans le code, mais (2.14) s'y annule identiquement ; seul (3.8) agit. Precision, pas erreur.

---

## E3. Variante avec Omega^2 Y_ab, deux composantes, controles de sensibilite

**Relecture du code.** `add_Y` ajoute Omega^2 Y_ab a That avec Y symetrique generique et dY generique ; la derivation de Omega^2 Y produit bien 2 Omega n_c Y + Omega^2 dY (regle de `Jet`). Y ne depend pas de n : c'est conforme a la partie D, ou That_D = Omega^2 T[psi_r ; eta, A] hors couche (verifie True dans la sortie originale) ; un Y generique couvre aussi la trace non nulle hors couche du tenseur de Dirac a masse de Yukawa. `n_comp = 2` ajoute une seconde composante avec le meme A et le quartique croise lambda_h (\|H_1\|^2 + \|H_2\|^2)^2. Le mode (2.15) utilise est la forme correcte (Omega^-1).

**(a) et (b), `var_E3_sortie.txt`** (re-execution : `rerun/var_E3_sortie_rerun.txt`) :

    (b) Omega^-2 == (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) (p^2 + p2^2 + q^2 + q2^2) n_[nu eta_lambda]rho : True
    (b) a m^2 + 4 lambda xi = 2 lambda/3 : Omega^-2 nul : True ; Omega^-1 nul : True ; aucun Omega^-3 ou moins : True
    symboles singuliers : p, q, p2, q2, leurs derivees premieres, n, kappa, lambda, m, xi (ni Y, ni A, ni lambda_h)
    exemple Omega^-1 : kappa (12 lambda xi - 2 lambda + 3 m^2)(p dp_1 + q dq_1 + p2 dp2_1 + q2 dq2_1)/18

**K-6 est satisfait.** Le doublet (somme sur les composantes) et le tenseur cinetique de Dirac (sous la forme generique Omega^2 Y) ne modifient ni la puissance dominante, ni le coefficient, ni l'annulation de Omega^-1.

**(c) Controles de sensibilite, `var_E3c_sortie.txt` (reproduit)** :

| Ajout | Omega^-2 a la condition | Omega^-1 a la condition | Coefficient residuel |
|---|---|---|---|
| mu phi^3, scalaire reel (exclu par th. 3.1) | nul | **non nul** | kappa mu n_1 p^3 / 2 |
| mu \|H\|^3, Higgs complet | nul | **non nul** | sqrt 2 kappa mu n_1 (p^2+q^2)^{3/2} / 8 |
| M Omega eta_ab B (type Majorana nue dans ghat Lag) | nul | **non nul** | -kappa M B n_1 / 2 |

La procedure detecte donc les singularites attendues : elle n'est pas aveugle. Reserve : le terme « Majorana-like » est une modelisation (ghat_ab M psi^T C psi = M Omega eta_ab B, B bilineaire rescale generique), pas un calcul spinoriel complet ; il teste la sensibilite du compteur, ce qui est l'objet du point (c).

---

## E4. Le sens « seulement si »

**Non-nullite.** Le coefficient de Omega^-2 de (2.17) vaut (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) Sum_i phi_i^2 n_[nu eta_lambda]rho. Sur scri, n.n = -lambda/3 != 0, donc n != 0 et n_[nu eta_lambda]rho n'est pas identiquement nul ; Sum phi_i^2 est une inconnue generique. Le coefficient est donc une fonction non nulle des inconnues des que kappa != 0 et m^2 + 4 lambda xi != 2 lambda/3. Il s'annule evidemment sur les donnees particulieres H_r = 0 sur scri : le « seulement si » est formel (au sens de Friedrich), pas un enonce sur toute solution. Si kappa = 0 (champ test), la singularite geometrique disparait mais celle de l'equation de Higgs subsiste : la condition reste necessaire.

**Changement de poids conforme.** La partie « w symbolique » de `var_E4` ne termine pas ; je l'ai remplacee par une formule fermee derivee a la main, puis verifiee contre le calcul en jets pour w = 0, 1/2, 1, 2, 3, 5/2 (`var_E4b_poids_general.py`, `var_E4b_sortie.txt`, tout True). Avec H = Omega^w h et la normalisation qui donne a box_D h le coefficient 1 (seule normalisation qui conserve la partie principale) :

    Omega^-(w+2) [boxhat_D - m^2 - xi Rhat](Omega^w h)
      = box_D h - Omega^-2 [m^2 + 4 lambda xi - (lambda/3) w (3 - w)] h + Omega^-1 2 (w - 1) [n^a D_a h + w s h] + O(1).

Lecture :

| Choix | Omega^-2 | Omega^-1 |
|---|---|---|
| w = 1 (note) | m^2 + 4 lambda xi - 2 lambda/3 | 0 identiquement |
| w racine de (lambda/3) w(3-w) = m^2 + 4 lambda xi, w != 1 | 0 | 2(w-1) n^a D_a h + ..., non nul (n.Dh jet independant) |
| w = 2 | m^2 + 4 lambda xi - 2 lambda/3 | 2(n.Dh + 2 s h), non nul |

Aucun poids ne retire tous les termes singuliers hors de la condition : le seul poids sans Omega^-1 est w = 1, qui impose la condition. (Pour w non entier, l'inconnue h n'est d'ailleurs plus un champ lisse attendu.) On reconnait les exposants de de Sitter Delta(3 - Delta) = M2, M2 = 2 donnant Delta = 1, 2 entiers.

**Jauge singuliere.** Le coefficient singulier de (2.17) ne depend que de Sum phi_i^2 = 2 \|H_r\|^2, invariant par H_r -> e^{i e chi} H_r (verifie, `var_E4b` (3)) ; et les coefficients singuliers ne contiennent pas A (sortie originale, E3). Aucune transformation de jauge, meme singuliere (chi = c ln Omega), ne peut donc le retirer. La variante « A -> A + c n/Omega sans rotation de H » de la 1re instance n'etait de toute facon pas une transformation de jauge ; sa non-terminaison est sans consequence.

**Limite residuelle.** Une redefinition des inconnues geometriques (par exemple W' = W + Omega^-1 X) n'a pas ete examinee ; elle introduirait une inconnue singuliere et sort du cadre de Friedrich. Je la signale sans la compter comme objection.

---

## E5. Origine du terme xi

**Equation de Higgs.** boxhat_D H = (m^2 + xi Rhat) H + ..., et (boxhat - Rhat/6)(Omega h) = Omega^3 box h (sortie originale, partie B, True). Donc le coefficient de Omega^-2 est m^2 + (xi - 1/6) Rhat |_{Rhat = 4 lambda} = m^2 + 4 lambda xi - 2 lambda/3. Verifie aussi par `var_E4b` (w = 1).

**Equation (2.17), recalcul a la main.** A l'ordre dominant (D_a H -> n_a h, n.n -> -lambda/3, Ghat -> -lambda ghat, f = 2 Omega^2 \|h\|^2 avec \|h\|^2 constant a cet ordre), en notant |h|^2 = \|H_r\|^2 :

    Tmin_ab  = \|h\|^2 [2 n_a n_b - eta_ab (n.n + m^2)]
    Txi_ab   = xi [ -lambda eta_ab 2\|h\|^2 + (ghat boxhat - nablahat nablahat)(f) ]  avec  (ghat boxhat - nablahat nablahat) f -> -6 n_a n_b (2\|h\|^2)
    T^(0)_ab = \|h\|^2 [ (2 - 12 xi) n_a n_b - eta_ab (m^2 + 2 lambda xi - lambda/3) ]
    trace    = \|h\|^2 [ 2 lambda/3 - 4 lambda xi - 4 m^2 ]
    L^(0)_ab = (kappa/2) \|h\|^2 [ (2 - 12 xi) n_a n_b + eta_ab (m^2/3 - 2 lambda xi/3 + lambda/9) ]  =: alpha n_a n_b + beta eta_ab
    (partie (kappa/2)(T - (1/3) trace ghat) de Lhat ; le terme (lambda/6) ghat a une derivee nablahat nulle)

Le terme de Christoffel de 2 Omega^-1 nablahat_[nu L_lambda]rho donne, pour L = alpha n n + beta eta, la structure Omega^-2 (2 beta + alpha n.n) (n_nu eta_lambda rho - n_lambda eta_nu rho), et

    2 beta + alpha n.n = (kappa/2) \|h\|^2 [ 2m^2/3 - 4 lambda xi/3 + 2 lambda/9 - 2 lambda/3 + 4 lambda xi ]
                       = (kappa/3) \|h\|^2 (m^2 + 4 lambda xi - 2 lambda/3).

D'ou le coefficient (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3)(p^2 + q^2) n_[nu eta_lambda]rho : K-3 retrouve. La part en xi a deux origines dans (2.17) : le terme Ghat f (via beta : -(2/3) kappa lambda xi \|h\|^2) et le terme d'amelioration -nablahat nablahat f + ghat boxhat f (via alpha n.n : +2 kappa lambda xi \|h\|^2), total (4/3) kappa lambda xi \|h\|^2 = (kappa/3) 4 lambda xi \|h\|^2. Dans l'equation de Higgs, elle vient de xi Rhat avec Rhat = 4 lambda. **Meme coefficient 4 lambda xi dans les deux secteurs : confirme.**

`var_E5_coefficient_main.py` (relu : n'utilise ni la classe Jet ni `cotton_source` ; Ghat calcule par la forme (2.3)) donne le meme resultat (True ; trace d'ordre 0 -(p^2+q^2)(6 lambda xi - lambda + 6 m^2)/3, egale a la mienne ; sortie reproduite). La ligne « attendu ... signe selon eta_00 » de sa sortie est un commentaire inacheve de la 1re instance ; la valeur imprimee 2 kappa lambda (p^2+q^2) n_1 / 3 pour le coefficient de xi est coherente avec (kappa/18)(12 lambda) (p^2+q^2) n_1.

---

## E6. Surdits, faiblesses et limites

| # | Phrase ou element | Statut |
|---|---|---|
| 1 | En-tete et docstring : (2.15) avec facteur Omega | **Erreur** (E1-a) ; sans incidence (E2). A corriger dans le script et dans la consigne d'armement. |
| 2 | §1 : « La condition mu = 0 du theoreme 3.1 (pas de terme cubique) est automatique par invariance de jauge » | **Inexact.** \|H\|^3 est invariant de jauge et produit une singularite Omega^-1 (E3c (c2)). L'exclusion vient de l'invariance de jauge **et** de la polynomialite (analyticite en H, H*) du potentiel : un polynome invariant par U(1) est fonction de \|H\|^2. |
| 3 | §1 : « - (xi - 1/6) kappa T* H_r ... avec T* = Omega^-2 That » | Notation fautive : il s'agit de la trace Str = Omega^-2 That (scalaire), pas de T*_ab (sans trace). |
| 4 | Partie (A) du script : rapport des poids = 1 | **Tautologique** : `sp.simplify(W**-4*W**2*W**2)` code les poids a la main ; ce n'est pas un calcul. Le resultat est vrai (identite connue en dim 4) mais non verifie par le script. Idem pour le courant de Dirac (chaine imprimee). |
| 5 | Partie (D) : « constant-mass control ... order 1 » | **Tautologique** : `Poly(Om^-2*Om^4*(1/Om)*Om^3).monoms()[0][0] - 3` est une arithmetique ad hoc (le -3 est retire a la main). Le resultat Omega^1 est correct (ghat m psibar psi = Omega^-2 m Omega^3 psibar_r psi_r) mais « controle reproduit » est surdit. |
| 6 | §2 : « Doublet : ... une composante complexe suffit » | Non verifie par le script ; **verifie par l'audit** (E3 (b)). |
| 7 | §2 : « Dirac cinetique ... (2.17) regulier (comptage ED partie D) » | Non verifie dans la partie C ; **verifie par l'audit** sous la forme generique Omega^2 Y_ab (E3 (a)). |
| 8 | Groupe non abelien | Annonce honnetement comme non verifie (§5). L'argument est plausible (coefficients singuliers sans A, D_a H -> n_a h independant de A, YM conformement invariant en dim 4) ; non verifie symboliquement par l'audit non plus. |
| 9 | Yukawa avec H complexe | Le lagrangien psibar(i gamma.D - y H)psi n'est pas hermitien pour H complexe ; la partie D utilise h_r **reel**. La structure correcte (y H psibar P_R psi + h.c., ou doublet) a les memes poids ; pas de consequence sur le comptage, mais la formule de la note est schematique (elle le dit pour l'equation de Higgs, pas pour la partie D). |
| 10 | « Le theoreme 3.1 est reproduit (sens si et seulement si) » | Reproduit pour V = m^2 phi^2/2 + lambda_h phi^4 seulement ; les autres clauses du theoreme sur le potentiel ne sont testees que via le controle cubique de l'audit (E3c (c1)). Formulation un peu large. |
| 11 | (2.13), (2.14), (2.15) reguliers ; « (2.16) implique par (2.17) » | Argumente, non calcule par le script. Plausible (That = Omega^2 Str, T*_ab regulier), non contredit. |
| 12 | Majorana nue « poids -1, coefficient M/Omega » ; Weinberg « suffisance » | Hors resultat, non calcules par le script. Majorana : la singularite dans (2.17) est confirmee par E3c (c3) (modele). Weinberg : comptage Omega^-1 (Omega^2 h^2 / Lambda) = Omega h^2/Lambda plausible, non verifie. |
| 13 | References a NOTE-176/178/183, ED, DB-1/DB-2, HX, S27-02 | Non verifiables dans cet audit (consigne d'isolement). Les phrases qui en dependent (« reserve M1 n'est plus necessaire », « combinaison de NOTE-176/178 retrouvee ») ne sont pas auditees. |
| 14 | Duree « 43 s » | 54 s ici ; sans portee. |

Rien dans la sortie du script ne contredit le verdict de la note ; les surdits relevees portent sur des justifications (points 2, 4, 5) ou des extensions non calculees par le script (6, 7), que l'audit a soit corrigees, soit verifiees.

---

## Criteres

| Critere | Statut | Source |
|---|---|---|
| K-1 J^nu = Omega^4 j_r^nu, courant de Higgs sans dOmega | Higgs : verifie (calcul reel, partie A). Dirac : comptage de poids correct mais imprime, non calcule (E6-4) | sortie originale |
| K-2 coefficient Higgs m^2 + 4 lambda xi - 2 lambda/3 | verifie | partie B, `var_E4b` (w = 1), E5 |
| K-3 coefficient Omega^-2 de (2.17), sans A, F, lambda_h, y | verifie | partie C2, `var_E5`, calcul a la main E5 |
| K-4 Omega^-1 nul a la condition | verifie | C2, E2 (ii-b), (iii) |
| K-5 Dirac y H_r ; ghat Lag_D d'ordre Omega^2 contre Omega^1 | verifie (identites hors couche reelles) ; controle Omega^1 tautologique (E6-5) mais exact | partie D |
| K-6 variante Omega^2 Y + deux composantes | **verifie** | `var_E3` (b) |

---

## Verdict : CONFIRME AVEC CORRECTIONS

Le resultat central de NOTE-191 tient sous audit adverse : le systeme couple YM-Higgs-Dirac-Einstein, en inconnues rescalees (A, Omega^-1 H, Omega^-3/2 psi), est formellement regulier au sens de Friedrich si et seulement si m_h^2 + 4 lambda xi = 2 lambda/3 ; la meme combinaison gouverne l'equation de Higgs et (2.17) (Omega^-2 et Omega^-1) ; K-1 a K-6 sont satisfaits ; la procedure est sensible (cubique, Majorana) ; le « seulement si » resiste aux changements de poids conforme et de jauge ; la substitution par symboles generiques n'est pas circulaire.

Corrections demandees avant ente :
1. Corriger (2.15) dans `fw3_check.py` (et dans la consigne d'armement) : facteur Omega^-1, non Omega ; mentionner que la correction ne change aucun coefficient singulier (E1, E2).
2. Remplacer « mu = 0 automatique par invariance de jauge » par « par invariance de jauge et polynomialite du potentiel (un terme \|H\|^3 produirait une singularite Omega^-1) ».
3. Corriger la notation « T* = Omega^-2 That » dans l'equation de Higgs (il s'agit de la trace Str).
4. Requalifier la partie (A) (poids YM, courant de Dirac) et le « constant-mass control » comme comptages de poids, non comme verifications symboliques.
5. Citer l'audit pour le doublet et le tenseur de Dirac dans la partie C (E3), au lieu de les presenter comme etablis par le script ; maintenir non abelien, Weinberg et (2.16) en limites.
