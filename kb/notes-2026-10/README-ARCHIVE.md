# Archive du mount « deux bords », notes 89 à 164 (9 au 13 octobre 2026)

Statut : **archive brute, [conv], hors CI.** Rien ici n'est « validé » au sens du CLAUDE.md du dépôt (pas de front-matter, pas d'entrée manifest, pas de source au registre du dépôt). Cette branche n'a pas vocation à être fusionnée dans `main` ; elle fixe un état daté du travail conduit en session, avec ses sceaux, pour qu'un relecteur extérieur puisse remonter chaque affirmation à sa pièce.

Déposée le 2026-10-14 depuis le dossier de travail `D:\temporaire` (copie d'aller-retour conteneur ↔ poste), sur la branche `archive/notes-2026-10`.

## Ce que contient le dossier

| Famille | Fichiers | Rôle |
|---|---|---|
| `NOTE-BORD-EON-089 … 164*.md` | 173 (versions v1/v2/v3/v4 conservées) | Notes de bord : armements (gels R-7), exécutions, concordances d'audit, actes de greffe et de décision, synthèses 163 (G-V3) et 164 (RG-4) |
| `NOTE-nnn-SCEAU*.txt` | 70 | Sceaux : sha256 des pièces + horodatage UTC, posés avant tout fetch/calcul pour les gels |
| `REGISTRE-CENTRAL-NUMEROS-NOTES.md` | 1 | Registre central des numéros (fait foi, R-54) ; état au 2026-10-13, premier numéro libre 165 |
| `01-REPRISE-AUTOPORTANTE-2026-10-1x*.md` | 5 | Pièces d'ouverture successives ; la v4 du 13 octobre est le point d'entrée |
| `PROMPT-AVEUGLE-*.md` | 30 | Prompts remis aux auditeurs isolés (audits froids aveugles) |
| `RAPPORT-*.md` (racine) et `audit_*/` | 14 dossiers | Rapports et dossiers de travail des auditeurs (scripts, sorties, SHA256SUMS) |
| `*.py`, `*_sortie.txt`, `*.out`, `*.py.txt` (racine) | ~110 | Scripts d'exécution des chantiers et leurs sorties ; les versions défectueuses sont conservées (R-55) |
| `src/SOURCE-*-extraits.txt` | 9 | Extraits verbatim courts des sources lues, avec métadonnées éditeur |

Les scripts sont des pièces de contrôle, pas des instruments : exécutés une fois sous gel, sortie archivée à côté. Les relancer ne fait pas partie du protocole.

## Ce qui a été volontairement laissé hors archive

- Les textes intégraux de prépublications récupérés pour lecture (`SOURCE-*-texte*.txt`, `audit_wb/work/S2-fulltext-alphaxiv.txt`, cinq fichiers, 60 à 105 Ko chacun). Ils restent sur le poste ; l'archive ne garde que les extraits. Les sceaux NOTE-104, 123 et 137 qui les référencent ne sont donc vérifiables ici que partiellement.
- Les PDF, archives zip, bundles et le reste de `D:\temporaire` (paquets antérieurs, QCCC, QOM, livrables OA-2), hors périmètre 89-164.
- Les instantanés intermédiaires du registre (`REGISTRE-vNNN-emis.md`, `REG-vNN.md`) nommés par les sceaux 98 à 118 : ils n'existaient plus sur le poste au moment du dépôt ; seul l'état final du registre est présent.

## Vérification des sceaux au moment du dépôt

Contrôle fait le 2026-10-14 sur les 530 fichiers copiés, en recalculant chaque sha256 cité par un fichier `NOTE-*-SCEAU*.txt` :

| Résultat | Nombre | Lecture |
|---|---|---|
| Empreinte conforme | 400 | Pièce identique à celle scellée |
| Fichier absent de l'archive | 24 | Les instantanés du registre et les textes intégraux listés ci-dessus |
| Empreinte différente | 6 | Quatre renvois au registre central depuis les sceaux 90-96 (le registre a évolué jusqu'à 164 : attendu) ; `audit_wb/SHA256SUMS.txt` cité par NOTE-150 ; `audit_ir_m/ma1/q2_profil_a_r.png` cité par NOTE-120 (figure, écart non expliqué, consigné tel quel) |

Les deux derniers écarts sont rapportés, pas corrigés : la règle est de ne rien réécrire dans une archive.

## Comment lire

1. `01-REPRISE-AUTOPORTANTE-2026-10-13-v4-G-V3-CADRE-FERME-AUDITE.md` : état du programme, règles, chaîne G-V3.
2. `NOTE-BORD-EON-163-SYNTHESE-G-V3-LECTURE-EXTERIEURE.md` puis `…-164-SYNTHESE-RG4-…` : synthèses écrites pour un relecteur humain extérieur, avec objections anticipées.
3. Pour une affirmation donnée : registre → numéro de note → note → sceau → script et sortie → rapport d'audit.

Libellé G-V3 en vigueur : `NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION-v4.md` (acte NOTE-162). Tout reste provisoire tant qu'une lecture humaine extérieure n'a pas eu lieu.
