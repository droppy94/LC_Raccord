# LC-RACCORD — dépôt versionné (prototype)

Miroir git du patrimoine documentaire LC-RACCORD. **Le mount `/mnt/project` reste
autoritaire pour le travail vif (R-54)** ; ce dépôt est le moteur de versioning
(diff / historique / branches / merge) et l'archive lisible.

## Correspondance avec la discipline existante
- `PKG-SHA` du manifeste  ≡  intégrité par hash (rôle du SHA de commit)
- manifeste `LC-WORK-AUDIT-PAQUET-GEL`  ≡  journal de commits
- patchs additifs  ≡  commits
- registre de sortie  ≡  blobs retirés

## Arborescence
- `kb/`           entrées de connaissance (.md)
- `instruments/`  scripts (.py : boot, sceau, générateurs, sceaux verif)
- `manifest/`     manifeste de gel (journal)

## Démonstration incluse : résolution du fork glossaire
La branche `front-pq` (matérialisation p_Q, v1.70) et `main` (axe γ, v1.74)
ont divergé à v1.69. Le merge résout le conflit de version/maj → **glossaire v1.75
(γ + p_Q)**, byte-identique au mount. Voir `git log --graph` et le commit de merge.
