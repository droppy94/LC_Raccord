# Prompt S-c : audit de lecture (fidelite des extraits et de leur interpretation)

Tu es un auditeur froid. Lis uniquement les fichiers de /home/claude/audit_sc/ : trois textes sources (SOURCE-1309.7248v2-texte.txt, SOURCE-1311.0700-texte-alphaxiv.txt, SOURCE-2503.24263v1-texte.txt). Ne cherche pas d'autres fichiers sur le disque. Tu peux, si une formule est illisible dans le texte, consulter les pages arXiv correspondantes par recherche web, en le signalant. Reponds en francais, sans tirets longs. Etiquettes : [extrait] (citation exacte avec localisation), [derive].

## Affirmations de lecture soumises a l'audit
**Tod, The equations of Conformal Cyclic Cosmology (1309.7248v2)**
- T1 : la metrique conforme commune aux eons est « assumed to be smooth » (hypothese, pas resultat).
- T2 : l'egalite des trois tenseurs de Weyl et l'identite de Bianchi forcent leur annulation sur Σ (renvoi a l'appendice B12 de Penrose).
- T3 : hypothese reciproque Ω̌Ω̂ = −1 et ǧ = Ω̂⁻⁴ĝ : la metrique de l'eon suivant est definie par celle du precedent, non obtenue en prolongeant les equations conformes.
- T4 : les resultats de Friedrich invoques concernent des sources a tenseur energie-impulsion sans trace.
- T5 : le developpement de Starobinsky ne contient que des puissances ; aucun terme logarithmique n'est envisage.
- T6 : Tod juge ses resultats satisfaisants aux deux premiers ordres du temps d'apres-Bang ; ses developpements d'apres-Bang contiennent des puissances demi-entieres du temps propre.

**Meissner et Penrose, The Physics of Conformal Cyclic Cosmology (2503.24263v1)**
- MP1 : le raccord est « conformally smooth », sauf en un ensemble discret de points (points de Hawking).
- MP2 : la structure conforme, et non la structure metrique, est lisse au raccord.
- MP3 : « it is an assumption of CCC that the conformal geometry is smooth along X ».
- MP4 : la lissite sert d'outil (loi de conservation masse-energie, isotropie locale initiale) ; la quantite transportee est le Weyl rescale de poids −1, fini a 𝓘⁺.
- MP5 : l'approche du raccord est dominee par une epoque d'ondes gravitationnelles, pour laquelle « The Einstein equations do not carry full information » ; rien n'est dit des electrons ni du Higgs.

**Friedrich, Smooth non-zero rest-mass evolution across time-like infinity (1311.0700)**
- F1 : les champs a tenseur sans trace obeissant a des equations conformement covariantes traversent la frontiere conforme.
- F2 : le prolongement lisse des equations conformes au-dela du raccord donne une solution qui se contracte, et non un Big Bang.
- F3 : Friedrich ecrit que les transitions vers un Big Bang peuvent s'accompagner de pertes de lissite et qu'une exigence de lissite trop stricte peut empecher de les modeliser.
- F4 : regularite au sens du theoreme 3.1 : « no terms of the form Ω⁻ᵏ » et seconds membres fonctions lisses des inconnues.
- F5 : en homogene conformement plat, les equations (2.16) et (2.17) sont trivialement satisfaites.

**Interpretation soumise a l'audit**
- I1 : aucune des trois sources ne fixe une classe de regularite finie (C^k) pour le raccord, ni n'envisage de termes logarithmiques (Ωᵏ ln Ω) a 𝓘⁺.
- I2 : la lissite est, chez Tod et chez Meissner et Penrose, une hypothese de definition de la CCC, non un resultat demontre.

## Mission
1. Pour chaque affirmation : FIDELE / INEXACTE / HORS CONTEXTE, avec citation exacte et localisation.
2. Cherche dans les trois textes tout passage qui **contredirait** T1 a F5, I1 ou I2 : classe de regularite explicite, mention de logarithmes, de regularite finie, de masses au raccord.
3. Signale les passages pertinents omis.

Rends un rapport structure.
