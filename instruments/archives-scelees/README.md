# Archives scellées — ré-import G-1 des 72 .py déchargés (v2.74)

**Provenance.** Snapshot pré-décharge fourni par l'opérateur (2026-07-21,
`DECHARGE-72-PY-SNAPSHOT.zip`), correspondant à la décharge v2.74 du manifeste
(72 sceaux pinnés-clos retirés du mount vers bundles hors-KB).

**Gate d'intégrité franchie au ré-import.**
- 72/72 fichiers confrontés à `INDEX-DECHARGE-72.txt` : **byte-exact**, 0 absent,
  0 mismatch, 0 doublon canonique.
- Re-vérification sha256 **après** copie sous nom canonique : 72/72 conformes.
- 0 collision de nom avec les instruments LIVE (`instruments/*.py`).

**Grade — à ne pas surclasser (§6.4).** Un sha conforme n'atteste que
**l'identité des octets**, jamais un EXIT 0 ni une conclusion physique. Ces
sceaux sont des archives *pinnées-closes* : ils ne sont **pas rejoués** ici et
ne portent aucune charge de sceau LIVE tant qu'un rejeu (Silo G-3) n'a pas été
exécuté et consigné. Les sceaux LIVE restent ceux de `instruments/` racine.

**Écart résiduel après ré-import** (cités en KB, toujours absents) :
- `verif_D3_P6_bang.py` — vrai manquant, à retrouver ou requalifier ;
- `verif_D_nongauss_4pt_phase1.py` — vrai manquant (le `verif_D_nongauss_4pt.py`
  ré-importé n'est pas la phase 1) ;
- `verif_G3_admissibilite.py` — vrai manquant (`verif_G3_adm_imports.py`
  ré-importé est un autre sceau) ;
- `verif_cartographie_v11_nonregression.py` et
  `verif_manifeste_v2122_consignation.py` — **retenus hors-KB par décision
  consignée** (manifeste v2.122, capacité >100 %, R-55) : absence conforme ;
- `verif_nonlin_deuxpoint__1_.py` — citation suffixée ; le canon
  `verif_nonlin_deuxpoint.py` est présent : **pas un manquant**.

**Fait consigné, non interprété** : le snapshot contient `verif_phi_seals.py`,
non cité dans la KB du dépôt. Conservé tel quel, à qualifier par l'opérateur.
