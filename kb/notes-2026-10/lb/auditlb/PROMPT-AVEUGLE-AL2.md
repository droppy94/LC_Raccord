# Consigne AL-2 (audit LB, lecture adverse)

Tu es un auditeur adverse isole. Pieces : /home/claude/LB/NOTE-BORD-EON-202-LB-EXECUTION.md (une note d'execution d'une lecture bibliographique, faite par une IA) et /home/claude/LB/auditlb/EXTRAIT-ARTICLE-v2.4-props.tex (extrait de l'article concerne). Ne lis aucun autre fichier de /home/claude. Travaille dans /home/claude/LB/auditlb/work_al2/ et ecris ton rapport dans /home/claude/LB/auditlb/RAPPORT-AL2.md, en francais, sans tiret long.

Outils : base d'articles alphaXiv (charge-la par ToolSearch « select:mcp__alphaXiv__answer_pdf_queries,mcp__alphaXiv__discover_papers,mcp__alphaXiv__get_paper_content »), WebSearch, WebFetch. Ne cite aucune reference de memoire.

Ta mission est de trouver ce qui est faux, surestime ou manquant :
- E1. Pour chaque source S1 a S16 : identifiant et titre exacts (verifie-les), et l'attribution faite par la note est-elle contenue dans la partie lue ? Le niveau de lecture declare est-il plausible ? Signale toute attribution fausse ou excessive.
- E2. Lemme 3.1 de arXiv:1902.09144 : la note affirme qu'il contient le contenu analytique de la Prop. 1 de l'article. Verifie par le changement de variables, et dis si c'est exact, trop fort ou trop faible.
- E3. Argument quantique (LB-4) : (a) l'axiome 1 de arXiv:0904.0612 est-il cite exactement ? (b) la derivation « etat de Slater quasi-libre, difference de rang un » est-elle correcte (hypotheses : etat pur, f dans l'image de 1 - P, normalisation, lissite de f, signe de la fonction a deux points) ? (c) l'argument « la restriction d'un etat Hadamard global a la carte plate est Hadamard » est-il correct ? (d) la conclusion « l'argument n'a pas besoin de Bunch-Davies, seul le chiffre tanh en depend » est-elle juste, compte tenu de ce que dit l'article ?
- E4. Nouveaute : cherche activement (au moins six requetes documentees, dont la litterature CCC de Tod, Lubbe, Nurowski, Newman, Penrose, et la litterature sur les champs de Dirac massifs en de Sitter, l'asymptotique et la diffusion conforme) un travail contenant l'equivalent d'une des Prop. 2, 3, 4 de l'extrait. Un tel travail ferait basculer le verdict.
- E5. Verdicts LB-1 a LB-4 et global : sont-ils justifies par la note ? Propose une correction motivee si non.
- E6. Propositions §3 de la note pour l'article : l'une d'elles est-elle fausse, ou en manque-t-il une ?

Classe tes constats en : erreur (renverse une attribution ou un verdict), correction (precise), complement (reference a ajouter).
