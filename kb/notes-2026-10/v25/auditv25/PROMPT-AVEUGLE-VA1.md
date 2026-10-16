# Consigne VA-1 (audit v2.5, verification independante des enonces)

Tu es un auditeur isole. Tu n'as que cette consigne et le fichier /home/claude/V25/auditv25/ARTICLE-v2.5.tex (article de travail, en anglais). N'ouvre aucun autre fichier de /home/claude hors de ton dossier /home/claude/V25/auditv25/work_va1/. Ecris ton rapport dans /home/claude/V25/auditv25/RAPPORT-VA1.md, en francais, sans tiret long. Calcule par scripts (Python, sympy, numpy, scipy), conserve-les dans ton dossier.

Mission : verifier **mathematiquement**, independamment, chaque enonce et chaque preuve de l'article, en particulier :
- V1. Definition 1 et son usage coherent dans tout l'article (continuite, bornitude, integrabilite, lissite ; classe de jauges ; regularite formelle).
- V2. Proposition 1 dans le cadre FLRW du §2 (hypotheses suffisantes ? borne ? absence de limite ?), et la Remarque 1 (forme de Fuchs, exposants, fonctions entieres P_+-, valeur en 0, interference dans les bilineaires, impossibilite d'une transformation reguliere ou independante de k).
- V3. Proposition 2 (hypothese de charge ; preuves de (a), (b), (c) ; derniere phrase et sa preuve ; signes du potentiel).
- V4. Proposition 3, formule (7), et le paragraphe « Dependence on the weight » (densite reguliere dans le poids Omega^-3 ; autres composantes O(Omega) ; series entieres pour les solutions a un seul exposant ; facteur d'interference).
- V5. Paragraphe « Quantum version » : etat de Slater (projecteur, purete, quasi-liberte), difference de rang un, usage de l'axiome de Wald, statut de Bunch-Davies, enonce integre et formule en tanh (verifie numeriquement le poids 1/(e^{2 pi m/H}+1) et l'egalite de Plancherel pour un paquet), absence de signe point par point.
- V6. Lemme 2 et Annexe A (la base est-elle complete ? les tenseurs invariants de rang 1 et 3 sur de Sitter sont-ils bien absents ? termes oublies, par exemple sigma^{ab} contracte avec epsilon et deux derivees, ou des termes en gamma_5 sigma ?).
- V7. Proposition 4 (preuve de (a) pour k non nul ; (b) ; (c) ; exemples d'ordre strict ; comparaison avec la condition scalaire integrale de m^2 dt).
- V8. Remarque 2 et Proposition 5 : coherence interne avec ce qui precede ; aucune affirmation plus forte que ce qui est prouve.
- V9. Ordres de grandeur (m_e/H, poids antiparticule).

Classe tes constats : erreur (enonce faux), correction (imprecision ou preuve incomplete), remarque.
