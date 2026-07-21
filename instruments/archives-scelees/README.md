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

**Sceaux retrouvés — apport opérateur du 2026-07-21** (hors INDEX-DECHARGE-72,
gate d'intégrité : sha256 vérifié post-copie ; rejeu consigné, sans surclassement) :
- `verif_D_nongauss_4pt_phase1.py` (`1aa3f051`) — rejoué **EXIT 0** ;
- `verif_G3_admissibilite.py` (`010a0562`, v2 DURCI post-audit froid, fourni
  suffixé `__4_`) — rejoué **ALL ASSERTIONS PASSED** ;
- `verif_cartographie_v11_nonregression.py` (`81e1914b`) — `--selftest`
  **FIREWALL OK 7/7** (l'exécution pleine confronte v1.0 mount ↔ v1.1) ;
- `verif_manifeste_v2122_consignation.py` (`5349ad47`) — `--selftest`
  **FIREWALL OK** (l'exécution pleine requiert le mount R-54). Ces deux
  derniers étaient *retenus hors-KB* au mount (v2.122, capacité, R-55) ;
  leur dépôt **git** ne modifie pas cette décision côté mount.
Un rejeu ici atteste une exécution du 2026-07-21 sur ce clone ; il ne
requalifie aucun grade et ne rejoue aucune gate.

**Doublons consignés (même apport, 0 dépôt)** : `verif_D3_P6_poc_specA__1_`,
`verif_D3_P6_specB_poc`, `verif_D3_P6_specB_supp__1_` = byte-identiques aux
archives ; `verif_D3_P6_specB_oracle__2_` = byte-identique au sceau **LIVE**
(`162696c1`, conforme au sha8 du manifeste).

**Écart résiduel** (cité en KB, toujours absent) :
- `verif_D3_P6_bang.py` — 1 citation ; **recherche opérateur négative
  (2026-07-21)** : introuvable en archive. À requalifier au lot R-8 du
  lotissement (réécriture sous protocole §2.0, ou requalification de la
  citation si la tête ne l'exige plus) ;
- `verif_nonlin_deuxpoint__1_.py` — citation suffixée ; le canon
  `verif_nonlin_deuxpoint.py` est présent : **pas un manquant**.

**Fait consigné, non interprété** : le snapshot contient `verif_phi_seals.py`,
non cité dans la KB du dépôt. Conservé tel quel, à qualifier par l'opérateur.
