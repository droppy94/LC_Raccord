# Prompt YA-2 : audit d'un script et reproduction independante (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_ya2/ (rien sous /mnt/user-data/, /home/claude/iry/, /home/claude/irz/, /home/claude/auditY/, ni dans d'autres dossiers audit_*). Travaille en python3 (sympy, mpmath installes) dans /home/claude/audit_ya2/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Objet
Le script /home/claude/audit_ya2/iry_state_v2.py. Il pretend etablir, pour un champ scalaire conforme sur le demi-espace η < 0 de Minkowski et un etat gaussien homogene de Bogoliubov, (y-1) le comportement en η → 0⁻ de la partie dependante de l'etat du tenseur, T^w ~ |η|^(N−4) quand α β* ~ k^(−N), avec 1/η pour N = 3 seulement, et une fonction entiere pour une decroissance gaussienne ; (y-2) que le terme α β* de la fonction a deux points est singulier sur le « cone reflechi » (η + η′)² = |x − x′|², qui rencontre le domaine η, η′ < 0 ; (y-4) qu'avec T̂ = s² T_plat (s = −η), un terme T̂ ~ s¹ n'apparait que pour N = 3.

## Taches
1. Calcule l'empreinte sha256 du script, lis-le, execute-le, et compare la sortie a ce qu'il pretend.
2. Reproduis independamment (ton propre code) : les integrales ∫_0^∞ dk k^m f(k) e^(−2ikη) pour f gaussienne et f = k^(−N) (regularisation a justifier), m = 1 et 3 ; la forme fermee de ∫ d³k/(2k(2π)³) e^(−ik(η+η′)) e^(ik·(x−x′)) ; le comportement de T^w pour N = 2, 3, 4, 5, 6.
3. Cherche des erreurs : signes, regularisations non justifiees, conclusions non etayees par le calcul, annotations fausses dans les messages imprimes, cas limites oublies (N non entier, phase φ, |β|² non negligeable, terme |β|² de w).
4. Contre-exemples : existe-t-il une famille α β* qui donne T^w ~ 1/η sans que la fonction a deux points soit singuliere dans le domaine η, η′ < 0 ? Examine en particulier des α β* oscillants ou a support compact en k.
5. Verdict sur chaque pretention (y-1, y-2, y-4) : retrouvee, retrouvee avec correction, ou infirmee.

Rends un rapport structure dans /home/claude/audit_ya2/RAPPORT-YA2.md, avec les empreintes sha256 de tes scripts et sorties.
