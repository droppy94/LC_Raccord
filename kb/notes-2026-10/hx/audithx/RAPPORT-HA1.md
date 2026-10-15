# RAPPORT HA-1 (dérivation en cécité stricte)

Conditions : seule la consigne PROMPT-AVEUGLE-HA1.md a été lue. Aucun autre fichier, document de projet ni recherche web. Calculs vérifiés par sympy dans /tmp/claude-0/ha1/ha1.py.

## 0. Cadre et conventions

- de Sitter plat, H = 1 : a = e^t, R = 12. Temps conforme eta = -e^{-t} in (-inf, 0).
- Omega = 1/a = e^{-t} = -eta ; Omega -> 0 quand t -> +inf (bord futur I+).
- g~ = Omega^2 g_phys = métrique de Minkowski (dS plat est conformément plat) : les équations rescalées vivent sur la demi-carte eta < 0 de Minkowski, prolongeables à eta = 0.
- Poids conformes : champ_phys = Omega^w champ~, avec w(H) = 1, w(psi) = 3/2, w(A_mu) = 0. sqrt(-g) = Omega^{-4} sqrt(-g~), g^{mn} = Omega^2 g~^{mn}.

## Q1. Comportement de h près de Omega = 0

Équation linéarisée homogène : h'' + 3 h' + (m_h^2 + 12 xi) h = 0, soit h'' + 3h' + M2 h = 0.

Ansatz h = e^{lambda t} : lambda^2 + 3 lambda + M2 = 0. Comme e^{t} = 1/Omega, h ~ Omega^{Delta}, avec

    Delta_± = 3/2 ± sqrt(9/4 - M2),   Delta_- + Delta_+ = 3,   Delta_- Delta_+ = M2.

| régime | branches |
|---|---|
| M2 < 9/4 | h = A Omega^{Delta_-} + B Omega^{Delta_+} (réels, Delta_- < 3/2 < Delta_+) |
| M2 = 9/4 | h = Omega^{3/2} (A + B ln Omega) |
| M2 > 9/4 | h = Omega^{3/2} [A cos(nu ln Omega) + B sin(nu ln Omega)], nu = sqrt(M2 - 9/4) |

Cas notables : M2 = 0 donne Delta = 0, 3 (constante + Omega^3) ; M2 < 0 donne Delta_- < 0 (croissance, la linéarisation près du point symétrique cesse de valoir) ; M2 = 2 donne Delta = 1, 2, soit h = A Omega + B Omega^2 exactement (couplage conforme, par ex. m_h = 0, xi = 1/6).

Forme rescalée (vérifiée sympy) : h~ = h/Omega obéit à

    d^2 h~/d eta^2 + (M2 - 2)/Omega^2 · h~ = 0,

donc h~ ~ Omega^{Delta_± - 1}. Le coefficient de l'équation rescalée est lisse en Omega = 0 si et seulement si M2 = 2.

## Q2. Régularité de m_f = y h (données génériques : A, B ≠ 0, la branche dominante est Delta_-)

Outils : dt = -dOmega/Omega, donc int m_f dt ~ int Omega^{Delta_- - 1} dOmega, fini ssi Re Delta_- > 0. Et m_f/Omega = y (A Omega^{Delta_- - 1} + B Omega^{Delta_+ - 1}) : lisse (C^inf) en 0 ssi les deux exposants sont des entiers >= 0 sans logarithme ; leur somme vaut 1, donc (0, 1), donc Delta_- = 1, M2 = 2.

| M2 | Delta_- | (a) int m_f dt fini | (b) m_f borné | (c) m_f/Omega lisse |
|---|---|---|---|---|
| M2 < 0 | < 0 | non | non (diverge) | non |
| M2 = 0 | 0 | non (divergence linéaire en t) | oui (tend vers yA) | non (~ Omega^{-1}) |
| 0 < M2 < 2 | ]0, 1[ | oui | oui | non (~ Omega^{Delta_- - 1} diverge) |
| M2 = 2 | 1 | oui | oui | **oui** : m_f/Omega = y(A + B Omega), polynomial exact |
| 2 < M2 < 9/4 | ]1, 3/2[ | oui | oui | non : continu, tend vers 0, seulement Hölder C^{0, Delta_- - 1}, pas C^1 |
| M2 = 9/4 | 3/2 | oui (int Omega^{1/2} ln Omega = -4/9) | oui | non : Omega^{1/2} ln Omega, continu, pas C^1 |
| M2 > 9/4 | 3/2 ± i nu | oui | oui | non : Omega^{1/2} cos(nu ln Omega + phi), continu, dérivée ~ Omega^{-1/2} oscillante |

Bilan : (a) ssi M2 > 0 ; (b) ssi M2 >= 0 ; (c) ssi M2 = 2.

Remarque hors généricité (A = 0) : m_f/Omega = y B Omega^{Delta_+ - 1} est lisse si Delta_+ = k entier >= 2, soit M2 = k(3 - k) in {2, 0, -4, -10, ...}. Mais pour k ≠ 2 le coefficient (M2 - 2)/Omega^2 de l'équation de h~ reste singulier : solution lisse ne veut pas dire équation lisse, et la donnée est ajustée finement.

## Q3. Invariance conforme des termes

Puissance de Omega qui reste devant chaque densité lagrangienne, exprimée avec g~ et les champs tildés :

| terme | puissance | statut |
|---|---|---|
| Yukawa sqrt(-g) y H psibar psi | -4 + 1 + 2·(3/2) = 0 | invariant |
| masse W, Z sqrt(-g) g^{mn} g^2 \|H\|^2 A_m A_n | -4 + 2 + 2 + 0 = 0 | invariant |
| F^2 (Yang-Mills) | -4 + 4 = 0 | invariant |
| lambda \|H\|^4 | -4 + 4 = 0 | invariant |
| m_h^2 \|H\|^2 | -4 + 2 = -2 | **non invariant** : coefficient m_h^2/Omega^2 |
| cinétique + xi R \|H\|^2 | invariant seulement si xi = 1/6 ; sinon reste (6xi - 1)·(terme en Omega^{-2}) | combiné avec m_h^2 en (M2 - 2)/Omega^2 |

Équation de Dirac : pour g~ = Omega^2 g, Dslash_{g~}(Omega^{-3/2} psi) = Omega^{-5/2} Dslash_g psi (vérifié sur la partie temporelle avec la connexion de spin de a^2 eta). Donc

    (i gamma~ · nabla~ - m_f/Omega) psi~ = 0,   coefficient de masse rescalé = m_f/Omega = y h~.

Bosons W, Z : Maxwell/Yang-Mills invariant en dimension 4, le terme de masse aussi ; l'équation rescalée est nabla~_m F~^{mn} = m~_W^2 A~^n avec m~_W = m_W/Omega = (g/2) h~ (et m~_Z = (sqrt(g^2 + g'^2)/2) h~).

## Q4. Conclusion

Le secteur fermionique et de jauge **n'ajoute aucune condition**. Tous ses coefficients de masse rescalés valent (constante) × h~ : y h~ pour Dirac, (g/2) h~ pour W, etc. Dès que l'équation du Higgs rescalée a des coefficients lisses (M2 = 2, c'est-à-dire m_h^2 + 12 xi = 2 H^2), h~ est lisse (h~ = A + B Omega en linéaire ; avec lambda h~^3 l'EDO reste régulière en eta = 0 sur Minkowski), donc tous ces coefficients le sont. Réciproquement, exiger que m_f/Omega soit lisse pour des données génériques redonne exactement M2 = 2 (Q2c) : la condition fermionique est équivalente à celle du Higgs, pas indépendante. Toute la non-invariance du secteur classique minimal est concentrée dans l'unique terme m_h^2 |H|^2 (et xi ≠ 1/6), d'où l'unique condition.

Schéma :

    m_h^2 + 12 xi = 2  ==>  h~ lisse  ==>  y h~ (Dirac), g h~/2 (W,Z) lisses
          ^                                          |
          +------ (données génériques) <-------------+

Masses qui échappent à la réduction :
1. **m_h elle-même** : c'est le seul paramètre massique du MS classique ; elle n'est pas « réduite », elle porte la condition.
2. **Masses hadroniques issues de QCD** (Lambda_QCD, transmutation dimensionnelle, anomalie de trace) : l'essentiel de la masse du proton ne vient pas de Yukawa.
3. **Brisures quantiques de l'invariance de Weyl** : courses des couplages y, g, lambda (anomalie de trace) ; l'argument est classique.
4. **Au-delà du MS minimal** : une masse de Majorana nue M nu_R nu_R a la puissance -1 (coefficient M/Omega, singulier) et échappe ; en revanche l'opérateur de Weinberg (HL)^2/Lambda a la puissance +1 (coefficient Omega/Lambda, lisse) et n'ajoute rien.
5. Hypothèse cachée : le Higgs doit tendre vers le point symétrique. Dans le vide brisé (h -> v constant), m_f = y v et m_f/Omega diverge ; la réduction ne vaut pas.

Les masses nulles (photon, gluons) sont trivialement compatibles.
