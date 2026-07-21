# Rejeu des sceaux sur le layout git (G-2)

**Convention constatée (2026-07-21)** : les sceaux résolvent leurs fichiers
KB relativement au répertoire courant (convention du mount `/mnt/project`,
layout plat). Sur ce dépôt, la KB vit sous `kb/` ⟹ un sceau lancé depuis la
racine échoue (cas témoin : `verif_paquet_propre.py`, « paquet introuvable »).

**Correctif — le lanceur, jamais un patch** :

    python3 instruments/run_sceau.py NOM[.py] [--kb-root DIR] [--timeout S] [-- args…]

`run_sceau.py` exécute le sceau avec cwd = racine KB (`$LC_KB_ROOT` ou
`kb/`), le résout dans `instruments/` puis `archives-scelees/`, et imprime
une ligne CONSIGNATION (nom, zone LIVE/ARCHIVE, sha8, rc, durée). **Aucun
octet de sceau n'est modifié** : les sha8 restent conformes au manifeste —
validation du 2026-07-21 : `verif_paquet_propre` → sha8 `051e2833` rc 0 ·
`verif_A4_QW` → sha8 `a4637a2c` rc 0, tous deux **égaux aux sha8 consignés
au §9ter du manifeste** ; `verif_G3_admissibilite` [ARCHIVE] rc 0.

Canaris lourds (`verif_nonlin_parity`, `verif_D3_P6_specB_oracle`,
`verif_A2_numerique`, `diag_bounces`) : ≥ 600 s — prévoir `--timeout`
en conséquence ; leur rejeu systématique relève du harnais G-3.

§6.4 : un rc 0 via ce lanceur atteste UNE exécution sur CE clone ; il ne
rejoue aucune gate, ne requalifie aucun grade, ne scelle, ne réduit, ne
compte, ne démontre rien.
