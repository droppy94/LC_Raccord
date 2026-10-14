# Prompt ADA-1 : noyau retarde non local et onde de de Sitter, derivation aveugle (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_p1/ada1/ (rien sous /mnt/user-data/, /home/claude/work/, ni dans d'autres dossiers audit_*). Pas de recherche bibliographique. Travaille avec sympy ou mpmath dans /home/claude/audit_p1/ada1/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Cadre
Espace de Minkowski R^4 (signature -+++, coordonnees tau, x, y, z) portant une perturbation metrique eps h, avec h_yy = -h_zz = u(tau) cos(k x), autres composantes nulles. On considere l'equation u'' - (2/tau) u' + k^2 u = 0 (tau < 0), dont on note u_A et u_B deux solutions independantes a determiner. On considere l'operateur lineaire non local T_ab[h] = ln(-box/mu^2) B_ab[h], ou B_ab[h] = d^c d^d C_acbd[h] est le tenseur de Bach linearise (C = Weyl linearise de eta + eps h) et ln(-box/mu^2) agit par son noyau RETARDE (prescription omega -> omega + i0 dans ln((k^2 - omega^2)/mu^2) a vecteur d'onde spatial k fixe).

## Questions
1. [calcule] Montre que pour h transverse et sans trace, B_ab[h] est proportionnel a box^2 h_ab et donne le coefficient. Trouve u_A, u_B (solutions explicites de l'equation ci-dessus) et calcule (d_tau^2 + k^2)^2 u pour chacune. Qu'en deduis-tu pour B[h] sur ces solutions ?
2. [derive] Donne le noyau temporel K_k(T) (transformee de Fourier inverse retardee de ln((k^2 - (omega + i0)^2)/mu^2)) : support, singularite en T = 0, comportement en T -> infini, partie locale (proportionnelle a delta(T)).
3. [calcule] Histoire adiabatique : u_eps(tau) = e^{eps tau} u_A(tau), eps > 0. Calcule B_eps = (d^2 + k^2)^2 u_eps a l'ordre eps. Evalue numeriquement (mpmath, k = 1) la reponse retardee non locale R_eps(tau0) = Int_{-inf}^{tau0} K_k(tau0 - tau') B_eps(tau') dtau' en tau0 = 0 pour eps = 0.1, 0.01, 0.001 (choisis et declare ta regularisation de la singularite en T = 0, par exemple partie finie de Hadamard). Quelle est la limite eps -> 0 ? Donne une borne analytique en eps.
4. [calcule] Histoire a emission finie : u = S(tau) u_A(tau) avec S une fonction de transition C^infini valant 0 pour tau < tau0 et 1 pour tau > tau0 + delta (choisis tau0 = -6, delta = 2, k = 1). Ou B[h] est-il non nul ? Calcule numeriquement R(tau) pour tau = -2, -1, -0.5, -0.1, 0 ; R est-elle lisse en tau = 0 ? Sa valeur en 0 est-elle nulle ? Depend-elle de tau0 ?
5. [derive] Enonce la condition sur l'histoire de u (ou sur B[h]) pour que R(tau) converge et soit lisse au voisinage de tau = 0. Si l'on pose T-hat = s^2 R(-s), s > 0, quel est le premier ordre en s de T-hat, et peut-il y avoir un terme lineaire en s ?

Rends un rapport structure dans /home/claude/audit_p1/ada1/RAPPORT-ADA1.md, avec les empreintes sha256 de tes scripts et sorties.
