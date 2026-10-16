# RAPPORT RA-1 (audit RJ, cecite stricte)

Auditeur isole. Seules sources : la consigne PROMPT-AVEUGLE-RA1.md et mes propres scripts.
Scripts et sorties dans `/home/claude/RJ/auditrj/work_ra1/` :

| Script | Objet | Resultat |
|---|---|---|
| `q1_q2_schouten.py` | Q1 : verification exacte de la decomposition ; Q2 : noyau | True ; rang 9, noyau de dimension 1 |
| `q3_dirac_T.py` | Q3 : derivation de T de Dirac sur FLRW, conservation, forme explicite | 5 verifications True |
| `q4_numerique.py` (+ `q4_sortie.txt`) | Q4, Q5, Q6 : integration numerique des modes, ordres, frequence | voir tableaux |

Conventions : signature (-,+,+,+), g = Omega^2 g-hat, n_a = d_a Omega, n^a = g^{ab} n_b, kappa = 1.

---

## Q1. Partie singuliere de 2 Omega^{-1} nabla-hat_[k L-hat_l]j

### Traduction du poids en composantes

Dans un repere g-orthonormal e_j, e-hat_j = Omega e_j et
tau_jk = Omega^{-3} T-hat(Omega e_j, Omega e_k) = Omega^{-1} T-hat(e_j, e_k).
Donc, en composantes coordonnees, avec tau indice par g :

    T-hat_ab = Omega tau_ab,    T-hat = g-hat^{ab} T-hat_ab = Omega^3 tau,    tau = g^{ab} tau_ab.

(Controle poussiere : U-hat_a = Omega^{-1} U_a, rho-hat = Omega^3 rho, d'ou T-hat_ab = Omega rho U_a U_b. Coherent.)

Alors

    L-hat_ab = (Omega/2) S_ab + (lambda/6) Omega^{-2} g_ab,     S_ab := tau_ab - (1/3) tau g_ab.

### Changement de connexion

g-hat = e^{2 phi} g avec phi = -ln Omega, donc d_a phi = -n_a/Omega et
C^m_kl = delta^m_k phi_l + delta^m_l phi_k - g_kl phi^m.
Le terme lambda disparait (nabla-hat g-hat = 0). Pour S symetrique, apres antisymetrisation en [kl] :

    nabla-hat_[k S_l]j = nabla_[k S_l]j + Omega^{-1} ( n_[k S_l]j - g_j[k S_l]m n^m ),

et la derivee du prefacteur Omega/2 donne (1/2) n_[k S_l]j. Au total :

    2 Omega^{-1} nabla-hat_[k L-hat_l]j  =  nabla_[k S_l]j   +   Omega^{-1} A_klj

    A_klj = 2 n_[k S_l]j - g_j[k S_l]m n^m
          = 2 n_[k tau_l]j - g_j[k tau_l]m n^m + tau g_j[k n_l].

| Partie | Expression | Contenu |
|---|---|---|
| singuliere (sans derivee de tau) | Omega^{-1} A(tau, n) | algebrique, lineaire en tau et en n |
| restante (reguliere) | nabla_[k S_l]j, S = tau - (tau/3) g | derivees premieres de tau, connexion de g, aucun Omega explicite |

lambda n'apparait nulle part.

### Verification independante

`q1_q2_schouten.py` : g = Minkowski, Omega = 2 + t/3 + x^2/5 - yz/7 + tx/11, dix composantes tau_ab polynomiales aleatoires (non conservees : l'identite est algebrique), lambda symbolique. Calcul direct des Christoffel de g-hat = Omega^{-2} g, de L-hat, de nabla-hat_[k L-hat_l]j, et comparaison composante par composante (24 x 4) avec la formule. Difference simplifiee identiquement nulle : **True**.

---

## Q2. Tau qui annulent la partie singuliere (n de genre temps)

Contraction j-k de A = 0 : (S n)_l = (2 tau / 3) n_l. Reinjection puis contraction par n^k :

    tau_lj = tau n_l n_j / n^2 ,   soit   tau_lj = rho nu_l nu_j,   nu = n / sqrt(-n^2),  rho = -tau quelconque.

Reciproquement, tau = rho nu nu annule A (verifie symboliquement pour n quelconque). Dans un repere ou n est proportionnel a dt, l'application lineaire tau -> A est de **rang 9** sur les 10 composantes, noyau engendre par tau_00 seul (script).

    Ensemble annulateur = { rho nu (x) nu : rho fonction scalaire arbitraire }  (fibre de dimension 1 en chaque point)

Interpretation : le poids poussiere de Friedrich n'est sans pole que pour une **poussiere comobile avec la normale conforme** n (flot orthogonal aux hypersurfaces Omega = cte, type flot de Hubble). Toute pression, tout flux de chaleur tau_0a (dans le repere de nu), toute contrainte anisotrope ou toute poussiere inclinee par rapport a n produit un terme en Omega^{-1}, sauf si ces composantes s'annulent au moins en O(Omega).

```
   tau  =   rho nu nu   +   q (flux)  +   pi (contraintes spatiales)
            |               |               |
            noyau de A      9 directions qui alimentent Omega^{-1} A
```

---

## Q3. Mode de Dirac test sur de Sitter

### Tenseur d'energie-impulsion (derive dans `q3_dirac_T.py`)

Action (calcul fait en (+,-,-,-), representation de Dirac standard ; les composantes a deux indices bas sont les memes en (-,+,+,+) car T^{mn} est le meme objet et on abaisse deux fois) :

    L = sqrt(-g) [ (i/2)(psibar gamma^m D_m psi - D_m psibar gamma^m psi) - m psibar psi ]

Variation par rapport a la tetrade, avec L = 0 sur couche :

    T-hat_mn = (i/4) [ psibar gamma_(m D_n) psi - D_(m psibar gamma_n) psi ] x 2 (symetrise).

Verifications symboliques, a(eta) quelconque, tetrade e^mu_A = a^{-1} delta, connexion de spin calculee a partir de la tetrade :

| Test | Resultat |
|---|---|
| (1) Dirac courbe pour psi = a^{-3/2} u e^{ik.x} equivaut a i u' = (alpha.k + beta m a) u | True |
| (2) T-hat_mn = a^{-2} T^flat_mn[u] (gamma plates, derivees ordinaires) | True |
| (3) nabla-hat^m T-hat_mn = 0 sur couche | True |
| (4) T^flat_00 = u^+ H u, T^flat_0a = -k_a u^+ u, T^flat_ab = (k_a J_b + k_b J_a)/2, J_a = u^+ alpha_a u | True |
| trace de T^flat = m a ubar u | True |

Avec e-hat_j = Omega d_j : tau_jk = Omega^{-1} T-hat_jk = Omega^{-1} a^{-2} T^flat_jk, soit **tau_jk = Omega T^flat_jk[u]** :

    tau_00 = Omega u^+ H u = m u^+ beta u + Omega k.J
    tau_0a = -Omega k_a |u|^2
    tau_ab = (Omega/2)(k_a J_b + k_b J_a)

### Comportement quand Omega -> 0

Omega = -H eta, m a = m/Omega, mu := m/H. Pres de Omega = 0 : i u' ~ beta (m/Omega) u, d'ou u = Omega^{i mu beta} chi, chi -> chi0 (correction O(Omega), voir Q5). Avec chi0 = chi0+ + chi0- (espaces propres beta = +1, -1) et alpha qui echange ces espaces :

    u^+ beta u = chi^+ beta chi          (pas de phase)
    |u|^2      = constante exacte        (H hermitien)
    J_a        = chi^+ alpha_a Omega^{2 i mu beta} chi = 2 Re( chi0-^+ alpha_a chi0+ Omega^{2 i mu} ) + O(Omega)

| Composante | Ordre | Terme dominant | Oscillation exp(i c ln Omega) |
|---|---|---|---|
| tau_00 | Omega^0 | m (abs(chi0+)^2 - abs(chi0-)^2) | non au dominant ; oui a l'ordre Omega (Omega^{1 +- 2 i mu}) |
| tau_0a | Omega^1 | -Omega k_a abs(chi0)^2 (exact) | non, jamais |
| tau_ab | Omega^1 | Omega (k_a J_b + k_b J_a)/2 | **oui, des l'ordre dominant** |

    c = +- 2 m / H

Amplitude de l'oscillation proportionnelle a k et a chi0-^+ alpha chi0+ : interference des deux secteurs beta = +1 et -1 (exposants de Frobenius +i mu et -i mu). Verification numerique (Q4 (a)) : frequence mesuree c = 2.604 pour 2 mu = 2.6 (resolution du balayage).

---

## Q4. Limite de la partie singuliere Omega^{-1} A quand Omega -> 0

Lecture retenue : la partie singuliere de Q1, c'est-a-dire le terme Omega^{-1} A(tau, n) effectivement present dans l'equation (le facteur Omega^{-1} explicite). Remarque en fin de section pour la lecture litterale Omega^{-2} A.

Avec n = d Omega = -H d eta (n de genre temps, nu proportionnel a d eta), les composantes non nulles de A (k<l) sont (sortie symbolique) :

    A_[0a]0 = -(H/2) tau_0a
    A_[0a]b = -H tau_ab (a != b),   A_[0a]a = -(H/2)(tau_aa - somme des deux autres tau_bb)
    A_[ab]c = combinaisons de -(H/2) tau_0c et (H/2) tau_0c

tau_00 n'apparait pas (Q2). Donc Omega^{-1} A est une combinaison lineaire de **tau_0a / Omega = -k_a |u|^2** (constante) et de **tau_ab / Omega = (k_a J_b + k_b J_a)/2**.

### Analyse

| Cas | tau_ab / Omega | Omega^{-1} A | Limite |
|---|---|---|---|
| (a) generique | O(1), oscille en exp(+-2 i mu ln Omega) | O(1), borne, oscillant | **non** (oscillation log-periodique non amortie) |
| (b) chi0 dans beta = +1 | O(Omega), serie entiere | constante + O(Omega), serie entiere | **oui**, limite = contribution de tau_0a/Omega = -k_a abs(chi0)^2 |
| (c) k = 0 | 0 exactement | 0 exactement | **oui**, nulle |

Justification de (b) : le systeme d u / d Omega = (i/H)(alpha.k + beta m/Omega) u a un point singulier regulier en Omega = 0 de residu i mu beta, exposants +i mu et -i mu, dont la difference 2 i mu n'est pas entiere : pas de logarithme, et la solution d'exposant +i mu s'ecrit u = Omega^{i mu} P(Omega), P serie entiere (entiere meme). Toute forme bilineaire u^+ X u = P^+ X P est alors une serie entiere en Omega : la phase se compense. Concretement chi- = (i/H) alpha.k chi0+ Omega^{1+2 i mu}/(1+2 i mu) + ..., d'ou J = O(Omega) sans oscillation. Meme conclusion pour chi0 dans beta = -1.

Justification de (c) : pour k = 0, tau_0a = tau_ab = 0 identiquement, tau = rho nu nu avec rho = m ubar u constant : on est exactement dans le noyau de Q2. Toute la partie reguliere s'annule aussi (tau_00 constant).

### Verification numerique (`q4_numerique.py`, H = 1, m = 1.3, k = (0.7, -0.4, 0.5), DOP853, rtol 1e-12)

Integration en s = ln Omega de d chi/ds = (i/H) Omega (alpha.k) Omega^{2 i mu beta} chi. Test de serie entiere : residu d'un ajustement polynomial de degre 4 en Omega sur chaque decade.

| Cas | max abs(Omega^{-1} A), Omega in [1e-8,1e-7] | residu fit polynomial | tau_ab/Omega | Diagnostic |
|---|---|---|---|---|
| (a) generique | 1.58 (meme valeur sur toutes les decades) | 0.65 | 1.82, residu 0.78 | borne, oscille, c mesure = 2.604 |
| (b) beta = +1 | 0.526 | 1.8e-13 | 5e-8 | serie entiere ; (Sing - lim)/Omega = 0.370314 constant de 1e-6 a 1e-3 |
| (b') beta = -1 | 2.44 | 7.6e-13 | 2.4e-7 | serie entiere |
| (c) k = 0 | 0 | 0 | 0 | identiquement nul |
| controle m = 0 | 1.55 | 3e-14 | 1.86, residu 3e-14 | serie entiere (cas conforme) |

Ecart entre Omega^{-1} A (Omega = 1e-6) et la limite predite (contribution tau_0a seule) en (b) : 3.7e-7, soit O(Omega) comme attendu.

Remarque (lecture litterale Omega^{-2} A) : elle diverge des que k != 0, en Omega^{-1} dans les trois cas (a), (b) via tau_0a/Omega^2 = -k_a abs(u)^2 / Omega ; seule la reponse (c) (nulle) subsiste. Ce n'est pas le terme present dans l'equation du Weyl rescale.

---

## Q5. Equation pour chi et regularisation par transformation unitaire

Avec u = exp(i beta mu ln Omega) chi, le terme de masse se compense exactement et

    i d chi / d eta = (alpha.k) Omega^{2 i mu beta} chi ,     soit   d chi/d Omega = (i/H)(alpha.k) Omega^{2 i mu beta} chi.

Coefficient : borne (norme abs(k)), mais **sans limite** en Omega -> 0 : ses blocs hors diagonale valent alpha.k exp(+-2 i mu ln Omega) (element (1,3) numerique : 0.41-0.28i, 0.19-0.46i, -0.10-0.49i, -0.36-0.35i pour Omega = 1e-2, 1e-4, 1e-6, 1e-8). Ce n'est pas une serie entiere en Omega. (L'integrabilite en Omega donne neanmoins chi -> chi0 avec chi - chi0 = O(Omega).)

**Peut-on choisir u = V(eta) chi, V unitaire, pour que les coefficients soient des series entieres en Omega pour tout k ? Non, avec V regulier.**

1. Argument de monodromie (V serie entiere en Omega, inversible en 0). Le systeme d'origine a en Omega = 0 un point singulier regulier d'exposants +-i mu, monodromie exp(-2 pi mu beta) != 1 pour m != 0. Un changement de jauge holomorphe inversible ne modifie les exposants que d'entiers et conserve la classe de monodromie. Un systeme a coefficients holomorphes a une monodromie triviale. Contradiction.
2. V independant de k (lecture "pour tout k"). Le nouveau coefficient est K = V^+(alpha.k)V + K0, K0 = V^+(beta m/Omega)V - i V^+V'. Lineaire en k : il faut K0 et V^+ alpha V reguliers. K0 regulier impose V = Omega^{i mu beta} W avec W solution d'une EDO holomorphe, donc W serie entiere unitaire inversible. Alors V^+ alpha V = W^+ alpha Omega^{2 i mu beta} W, regulier seulement si alpha Omega^{2 i mu beta} l'est : faux pour mu != 0.
3. V non regulier. Pour k fixe, V = propagateur exact Phi_k = P_k(Omega) Omega^{i mu beta} (unitaire) rend le coefficient nul, mais V porte lui-meme Omega^{i mu beta}, depend de k, et ne change rien a la physique : tau est un bilineaire invariant sous u = V chi, et ce sont ses composantes, pas l'equation pour chi, qui alimentent l'equation du Weyl. Les termes exp(+-2 i mu ln Omega) de tau sont donc **intrinseques** (invariants de jauge) ; ils traduisent la difference des exposants 2 i m/H.

---

## Q6. Conclusion

**Poles.** Dans le poids poussiere de Friedrich et la jauge g = Minkowski, Omega = -H eta, n = d Omega, il ne reste **aucun pole en 1/Omega** pour le mode de Dirac test :
- le second membre s'ecrit nabla_[k S_l]j + Omega^{-1} A(tau, n) ;
- A ne voit que tau_0a et tau_ab, qui sont O(Omega) (le terme O(1), tau_00, est exactement de type poussiere comobile, dans le noyau de Q2) ;
- donc Omega^{-1} A = O(1), et la partie reguliere est O(1) aussi (d tau_00/d eta = -H k.J, d tau_ab/d eta borne).

**Obstruction residuelle** a la regularite formelle (seconds membres series entieres en Omega) : des termes d'ordre Omega^0, **log-periodiques**, en

    exp(+- 2 i (m/H) ln Omega),   c = 2 m/H,

d'amplitude proportionnelle a k et a chi0-^+ alpha chi0+. Ils apparaissent a la fois dans Omega^{-1} A (via tau_ab/Omega) et dans la partie reguliere (via d tau_00/d eta et d tau_ab/d eta). Il n'y a pas de ln Omega non oscillant (exposants non resonants). Origine : interference des deux secteurs de Frobenius beta = +-1, d'exposants +-i m/H ; l'obstruction est invariante sous toute redefinition unitaire du spineur (Q5).

| Situation | Second membre serie entiere en Omega ? |
|---|---|
| generique, m != 0, k != 0 | non : O(1) borne, oscillant en exp(+-2 i (m/H) ln Omega) |
| chi0 dans un seul espace propre de beta | oui |
| k = 0 | oui (second membre identiquement nul) |
| m = 0 (conforme) | oui |

Critere de regularite pour un mode : m = 0, ou k = 0, ou donnee asymptotique chi0 polarisee dans un seul espace propre de beta. Pour une superposition de modes, les termes croises entre un mode beta = +1 et un mode beta = -1 portent aussi Omega^{+-2 i mu} : il faut que **tous** les modes soient dans le meme secteur (extrapolation directe du calcul mode par mode, non verifiee numeriquement ici).

Limite de portee : resultats etablis pour un champ test sur fond de Sitter fixe, dans un repere ou le poids poussiere s'applique tel que defini ; la retroaction et le choix d'autres poids conformes (par exemple Omega^{-4}, adapte au cas sans masse) n'ont pas ete examines.
