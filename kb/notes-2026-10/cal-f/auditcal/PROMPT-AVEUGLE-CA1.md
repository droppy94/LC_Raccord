# Consigne aveugle CA-1 (derivation en cecite stricte)

Tu es un relativiste. Aucun document ne t'est fourni sauf cette consigne ; derive tout toi-meme et ecris un rapport avec les calculs (tu peux utiliser sympy).

Cadre : equations conformes de Friedrich. Metrique physique g^ (chapeau), facteur conforme Omega, metrique non physique g = Omega^2 g^. Tenseur de Schouten physique L^ = (kappa/2)(T^ - (1/3) tr(T^) g^) + (lambda/6) g^. L'une des equations du systeme est
   nabla_mu W^mu_{rho nu lambda} = 2 Omega^{-1} nabla^_[nu L^_lambda] rho      (E)
ou nabla^ est la connexion de g^.

Q1. Sur de Sitter physique (H = 1, coordonnees conformes eta < 0, g^ = eta^{-2}(-d eta^2 + dx^2), Omega = -eta), calcule le second membre de (E) pour un fluide parfait test homogene et isotrope de densite rho(eta) et pression p(eta). Quand s'annule-t-il ?
Q2. Meme question pour un champ scalaire test homogene minimalement couple de masse m quelconque, sur couche (equation de Klein-Gordon satisfaite). Le resultat depend-il de m ?
Q3. Refais Q2 en remplacant, par erreur volontaire, les derivees covariantes par des derivees partielles, pour h = phi0 s + phi1 s^2 (s = -eta) et m^2 = 2. Qu'obtiens-tu ?
Q4. Pour un champ de Dirac de masse m sur ce fond, rescale avec le poids conforme 3/2 (psi_rescale = Omega^{-3/2} psi), ecris l'equation rescalee. Compare a la situation d'un scalaire massif rescale avec le poids 1, ou l'equation rescalee contient un terme Omega^{-2}(m^2 - 2 lambda/3) psi (resultat de Friedrich). Existe-t-il, pour le Dirac, une masse constante non nulle qui rende l'equation rescalee reguliere en Omega = 0 ? Un couplage local a la courbure (masse effective constante sur dS exact) peut-il y parvenir sans annuler la masse effective ?
Q5. Une regle de comptage dit : « si T ~ s^p Y avec Y lisse, alors le second membre de (E) est ~ s^(p-2), et il y a un pole ssi p = 1 ». Est-elle exacte ? Donne un contre-exemple ou une preuve.

Rends un rapport autoportant avec une reponse nette par question.
