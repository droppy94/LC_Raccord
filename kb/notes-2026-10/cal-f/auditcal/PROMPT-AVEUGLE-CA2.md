# Consigne aveugle CA-2 (audit adverse)

Tu es relecteur adverse. Pieces (seules lisibles) :
- /home/claude/article-rg4/cal/auditcal/NOTE-176.md (note a auditer)
- /home/claude/article-rg4/cal/auditcal/cal_f.py et cal_f_sortie.txt (script et sortie)
- /home/claude/article-rg4/cal/auditcal/SOURCE-1311.0700-fulltext.txt (texte integral extrait de Friedrich, arXiv:1311.0700 ; extraction brute, formules eclatees sur plusieurs lignes)

Taches :
E1. Les citations de la source dans la note (§1) sont-elles fideles ? En particulier : forme de (2.17), (3.11), enonce du theoreme 3.1 (« regular [...] If and only if the single condition m^2 = (2/3) lambda »), et l'affirmation que le critere de Friedrich porte sur le systeme couple entier, equation de matiere comprise.
E2. Le script : implemente-t-il correctement la derivee covariante sur dS physique et la source de (2.17) ? Les resultats (1)-(4) sont-ils justes ? Execute-le (python3, sympy installe) et modifie une copie pour tester d'autres cas si utile.
E3. L'affirmation centrale de §3 : pour le Dirac, l'obstruction au sens de Friedrich est le coefficient m/Omega de l'equation rescalee, sans masse speciale ; est-ce correct et proportionne ? Y a-t-il une redefinition d'inconnues qui l'eviterait ?
E4. Les greffes proposees §4 (G-CAL-a, G-D1-e, article v2.2) sont-elles justifiees par ce qui est etabli, ni plus ni moins ?
Rends des verdicts (correct / correction mineure / faux / non demontre) et une liste d'erreurs par gravite.
