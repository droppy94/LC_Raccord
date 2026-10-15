# Consigne aveugle DB-1 (derivation en cecite stricte)

Tu es un relativiste mathematicien. Aucun document : derive tout, ecris un rapport avec calculs (sympy disponible).

Cadre : equations conformes de Friedrich avec matiere. Metrique physique g^ = Omega^{-2} g (g non physique), Schouten physique L^ = (kappa/2)(T^ - (1/3) tr(T^) g^) + (lambda/6) g^. Les seconds membres des equations geometriques font intervenir : tr(T^) ; Omega T*_{mu nu} avec T* = T^ - (1/4) tr(T^) g^ ; Omega^{-1} nabla_mu tr(T^) ; et 2 Omega^{-1} nabla^_[nu L^_lambda] rho. Le critere de Friedrich est la regularite FORMELLE : aucun Omega^{-k} dans les seconds membres ecrits comme fonctions des inconnues rescalees.

Q1. Pour un champ de Dirac psi de masse m sur g^, rescale psi_rescale = Omega^{-3/2} psi : le tenseur cinetique symetrise T^_{mu nu} = (i/4)(psibar gamma_mu nabla_nu psi + (mu<->nu) - c.c.) est-il egal a Omega^2 fois le meme tenseur construit avec psi_rescale et g, comme identite hors couche ? Verifie-le (au moins pour g plate et Omega(x) quelconque), en fixant d'abord la connexion de spin par la covariance de l'operateur de Dirac sans masse.
Q2. En deduire l'ordre en Omega de chacun des termes listes ci-dessus. Les equations geometriques sont-elles formellement regulieres pour toute masse ? Ou la masse entre-t-elle ?
Q3. Si l'on ecrit T sous la forme « cinetique - g^ Lag » (Lag lagrangien de Dirac, nul sur couche), que se passe-t-il ? Exprime Lag en fonction de psi_rescale.
Q4. Compare avec un scalaire massif minimalement couple phi = Omega psi : quel terme de T^ est d'ordre Omega^0 et produit des singularites ? Pourquoi le scalaire admet-il une masse speciale (Friedrich : m^2 = 2 lambda/3) et le Dirac non ?
Q5. Conclusion : ou se trouve la singularite du systeme couple Einstein-Dirac, et a quelle condition sur m (eventuellement variable) disparait-elle ?
