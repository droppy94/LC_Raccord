# AMENDEMENT 1 à la NOTE-REPRISE-GIT-S9 — daté, post-dépôt

Note amendée : `NOTE-REPRISE-GIT-S9.md`, sha256
688bca50d676eccb491257dc0c9ff0505870055acf92afb90265b2536105d35c
La note reste BYTE-INTACTE. Cet amendement est un fichier séparé.
Émis le 2026-07-24, APRÈS le dépôt (commit `9c22290`), sur GO opérateur.

## Objet — leçon d'environnement manquante, imputable au pilote

Constatée à la vérification post-dépôt sur clone neuf, donc APRÈS écriture
de la note : elle n'y figure pas et doit être opposable en S10.

**`instruments/harnais_R11.py` crée `instruments/__pycache__/` en
s'exécutant.** Le harnais importe et recharge le module
`redemo_R11_falsifiabilite` pour muter ses porteurs ; Python écrit alors le
bytecode compilé dans `instruments/__pycache__/`.

Conséquence pour le §0-lite S10 : après le rejeu hors compte de
`harnais_R11.py`, `git status --porcelain` sortira

    ?? instruments/__pycache__/

**Ce n'est PAS une modification de fichier suivi** — rien de tracké n'est
touché, à la différence de l'écart bénin de `inventaire_sceaux.py` qui
réécrit sa ligne de date (`M audit/INVENTAIRE-SCEAUX.md`). C'est une entrée
NON SUIVIE. Mais un §0-lite qui exige « arbre propre » la verra, et sans la
présente ligne l'opérateur de S10 la découvrirait sans filet.

**Traitement** : `rm -rf instruments/__pycache__` — sans effet sur le dépôt,
sans `git checkout`. À faire APRÈS le rejeu du harnais, avant tout contrôle
d'arbre propre.

**Imputation** : effet de bord de l'instrument déposé en S9, non anticipé au
gel R-11. Défaut du pilote, pas du dépôt.

## Ce que cet amendement N'EST PAS

- Ce n'est PAS une modification des attendus §0-lite : 12 redemo,
  271/271 PASS + 101 consignations, 12/12 rc = 0, comptes 33/76/32/215/4,
  inventaire 6/76/1, sceau 051e2833 — tous INCHANGÉS et vérifiés sur clone
  neuf après dépôt.
- Ce n'est PAS un `.gitignore` : l'option a été écartée sur arbitrage
  opérateur au profit du schéma d'amendement, cohérent avec le précédent S9
  (un défaut se nomme par fichier séparé daté, la pièce amendée reste
  byte-intacte).

*§6.4 — amender une note ne scelle, ne réduit, ne compte, ne démontre rien.*
