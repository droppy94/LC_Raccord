---
id: LC-BETA-PAQUET-CONCORDANCE
titre: "Table de concordance du paquet β — les 43 entrées, leur sha256, et la contrepartie `kb/` de chaque copie. REMPLACE la refourniture du ZIP : le paquet se RECONSTRUIT depuis le dépôt, il ne s'y recopie pas."
codename: LC-RACCORD
type: "table de concordance. Elle n'atteste ni une physique, ni un verdict, ni une pertinence — seulement des octets et des correspondances."
version: 1.0
langue: fr
date: 2026-07-25
session: S16
---

# Concordance du paquet β — pour ne plus jamais le refournir

## 0. Pourquoi cette table et pas les octets

Le dépôt interdit **toute COPIE DE SUBSTANCE, arbre ET historique**
(`NOTE-REPRISE-GIT-S15` §5.3), et `audit/LC-BETA-CONTROLE-DEPOT.py` en fait un
contrôle mordant : **zéro `BETA-COPIE-*` en arbre, zéro en historique**, sinon
`exit != 0`. Renommer une pièce pour passer sous ce contrôle est la faute
**commise trois fois** (précédent S15 nº1). Elle ne sera pas commise une quatrième.

**MESURE DE S16, indépendante** : sur les 35 copies, **34 sont BYTE-IDENTIQUES**
à leur original `kb/`, **0 DIVERGENTE**, **1 sans contrepartie**.
⟹ **La substance du paquet est DÉJÀ au dépôt.** Ce qui manquait n'était pas les
octets, c'était **la table qui dit lesquels**.

## 1. Contenant

| objet | valeur |
|---|---|
| `LC-BETA-PAQUET.zip` | 328497 o, sha256 `bbfee7b5782e0f92858fe81196337ce4bf118ae283c003f577f0d139ee47b5f4` |
| entrées | 43 = 35 `BETA-COPIE-*` + 8 `LC-BETA-*` |

**Le sha du ZIP n'atteste que le ZIP.** `PKG_SHA_BETA_8` porte, lui, sur le
**contenu courant d'un répertoire** — précédent S15 nº3 : **un gel sur un
répertoire vivant n'est pas un gel.** Cette table ne dépend d'aucun répertoire.

## 2. Les 35 copies — reconstructibles depuis `kb/`

Procédure : `cp kb/<original> <atelier>/BETA-COPIE-<original>` pour chaque ligne
marquée BYTE-IDENTIQUE, puis confronter au sha256 ci-dessous.

| copie | original `kb/` | sha256 (commun) | issue |
|---|---|---|---|
| `BETA-COPIE-LC-CONST-V1.md` | `kb/LC-CONST-V1.md` | `a56c8cde2462925f138f93dc05e2e0c8edae67969c7546f72d2530f2f73e2cd7` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-CT-DUAL-DS.md` | `kb/LC-D-CT-DUAL-DS.md` | `f70062c1057426dbb679d79e5626dacd5420b37ef13e353b44d3ace9a4f7c463` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-CT-DUAL.md` | `kb/LC-D-CT-DUAL.md` | `2b13e4c440d55e36c0d0237fe8c9b529339af8e25ec6fc6ec896fe5fe10c430e` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-CT-GAMMA.md` | `kb/LC-D-CT-GAMMA.md` | `e3f4de56207bece2dd1c236418bd9d42af402c19912a6fbd912916cf94fe9156` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-CT-REALITE.md` | `kb/LC-D-CT-REALITE.md` | `6e90ab7231c2a7ebe065b31b894484d873ed6cddf3e514a29de501baad53f62f` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-F5-ETAT-RACCORD.md` | `kb/LC-D-F5-ETAT-RACCORD.md` | `9b3d23a69008041e979a4bafd4fd3731c7d2439174dd5bded016187e00848735` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-F6-G3-LAMBDA-BMS.md` | `kb/LC-D-F6-G3-LAMBDA-BMS.md` | `4c84be568ab626c6e582f2ae1b5a29f150bf5ba36886a7c375796548470dc7eb` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-ADM-IMPORTS.md` | `kb/LC-D-G3-ADM-IMPORTS.md` | `9c55868feac7f17592fa9d61d334497c762c7e974b3cc0a1ee69f05e7b465a2e` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-ADMISSIBILITE.md` | `kb/LC-D-G3-ADMISSIBILITE.md` | `f5a770e7e8c8289de6f41595567db23711bef51fd589624134f6705d4264a111` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-GAP-STDEF.md` | `kb/LC-D-G3-GAP-STDEF.md` | `b90301de496eb3f1d6294a1199aff7d7d8dffd7382275b15337381cafb1bc66f` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-KPS-KB.md` | `kb/LC-D-G3-KPS-KB.md` | `d8b31cdbc7e2d314c19586eca7c79d721f6643bf5ca32b81e06da97cbb04cbf7` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-M4-CHAINON.md` | `kb/LC-D-G3-M4-CHAINON.md` | `93d3911ce1bcff5a7f790e95d09abbe8c17e92fb6f61f85d51b6d348aa07fe72` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-G3-TRANSPORT.md` | `kb/LC-D-G3-TRANSPORT.md` | `5a52ff9384974c9fcf4c53864cc11e2c0b99b40969d94bb618c67b1eb8821260` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-HOLOGRAPHIE-G3.md` | `kb/LC-D-HOLOGRAPHIE-G3.md` | `759583cb5c6a8eab903582383971f15a1919358a90c64f51005c1c8eb36941f3` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-IRREDUCTIBILITE-MOYENS.md` | `kb/LC-D-IRREDUCTIBILITE-MOYENS.md` | `3d1bd3d36fb9f83e485b592be317bbfdeee6f53326ce8218744e01c2dcba44f5` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-C1-ADS.md` | `kb/LC-D-O2-C1-ADS.md` | `a32b2186a3633ea6e1160531843fe2a003109f922ae06727f97e05de45907301` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-COIN-TRANSMISSION.md` | `kb/LC-D-O2-COIN-TRANSMISSION.md` | `1b0e8276de84392cbf98e8af4fd4c631f81dd1ec56fc36bd355ce2c9000fbe9b` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-DELTA-C.md` | `kb/LC-D-O2-DELTA-C.md` | `078a96a7230bcff0543f2adb4ccc13d1808df063c2519475cac235b4d5a92396` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-FACTORISATION.md` | `kb/LC-D-O2-FACTORISATION.md` | `7277ba6a13660d1d6a7d2c33a1d37ec3d071f30d9b8fbc4aeac46f15c12e9812` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-JONCTION.md` | `kb/LC-D-O2-JONCTION.md` | `b5e017b5eea898376250028df2150b25e1fe1607e4880c9d9a12363f0482ad87` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-P-SELECTEUR.md` | `kb/LC-D-O2-P-SELECTEUR.md` | `1f1270fc3d2c3137785f079ae238936a78fc31dff00489630745af90926029f0` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-O2-P2.md` | `kb/LC-D-O2-P2.md` | `259bd1c7ecf079607f83c95b2497636938d75a6ebfb9fc098412d48aac4274fe` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D-S7-FIDELITE-DELTAC.md` | `kb/LC-D-S7-FIDELITE-DELTAC.md` | `5ec402100e7b233bd951d8b850ef51fe799d7652253a506903e83e61ee52f2a4` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-D3-SPECTRE-K3.md` | `kb/LC-D3-SPECTRE-K3.md` | `6f5c1738540d4908a324456657328211e6975fa6f6fb2dac005f762bfe908550` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-JOURNAL-V94.md` | — | `b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c` | **SANS CONTREPARTIE `kb/`** |
| `BETA-COPIE-LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE.md` | `kb/LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE.md` | `cc856f675801f241f119574318a16b4d0832eb5d24d6d15f056172e8b6af7830` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-AMENDEMENT-R7-PACKAGE-SHA-CONVENTION.md` | `kb/LC-WORK-AMENDEMENT-R7-PACKAGE-SHA-CONVENTION.md` | `eea2152cdc52899eb4932c39c36c4f796176ca870cadb883723f8d8d7e3a399d` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-ADM-IMPORTS.md` | `kb/LC-WORK-CADRAGE-G3-ADM-IMPORTS.md` | `8ed11d5f4fce7235e4abb533c1f5235d891c6ef0aa23347da61768157e3310d0` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-ADMISSIBILITE.md` | `kb/LC-WORK-CADRAGE-G3-ADMISSIBILITE.md` | `d3e1afc7f3da67976ffeee8a4df99e29c653d94e024b89455caf430a9f075a83` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-DS4-GRAVITON.md` | `kb/LC-WORK-CADRAGE-G3-DS4-GRAVITON.md` | `c2e91dcb98575db0ca13f86ded023abd21cf52949b0a06b02db1e89c0bb29089` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-HORS-WEDGE.md` | `kb/LC-WORK-CADRAGE-G3-HORS-WEDGE.md` | `37bc85e52547ae60e54101e021f65594fb85b33817a6cb69039ef30efdc1e73f` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION.md` | `kb/LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION.md` | `172c3730e99425007f26160e7ceb7683f0365dd011f2a1873f12464780e041e8` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-M4-CHAINON.md` | `kb/LC-WORK-CADRAGE-G3-M4-CHAINON.md` | `2d4f167ec70cf13441ca8703566edc806175fc3b78392909a642e72d5e3ae4fb` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-CADRAGE-G3-TRANSPORT.md` | `kb/LC-WORK-CADRAGE-G3-TRANSPORT.md` | `b5276e68b61366dbf79caa0a7ea91da4f7ce4c69ed87670646b4a0bcb8f175eb` | **BYTE-IDENTIQUE** |
| `BETA-COPIE-LC-WORK-R41-BORDEON-MIROIRS.md` | `kb/LC-WORK-R41-BORDEON-MIROIRS.md` | `61862243ca7143a41d50493571c02b24184141a498c0864edff0c2a776332d0d` | **BYTE-IDENTIQUE** |

**34 reconstructibles · 1 non reconstructible.**

## 3. LE TROU, nommé

`BETA-COPIE-LC-JOURNAL-V94.md` n'a **aucune contrepartie `kb/`** : le journal V94
est **MOUNT-SEUL DE DROIT** sous G-4 (`NOTE-REPRISE-GIT-S15` §5.1, §8). C'est la
**seule** entrée des 43 que ce dépôt ne permet pas de reconstituer.

Son sha256 est consigné ci-dessus : une réapparition **SE CONFRONTE**, elle ne
s'enregistre pas. **Je ne le dépose pas d'office** — G-4 l'a placé au mount, et un
arbitrage prospectif ne se rétroapplique pas. **Bascule possible sur GO opérateur.**

## 4. Les 8 pièces `LC-BETA-*` — DÉPOSÉES en S16

Aucune contrepartie `kb/`, donc rien à reconstruire : elles sont **déposées
byte-intactes** sous `audit/beta-paquet-gouvernance/`, au titre de l'**arbitrage
nº2** (« les pièces de GOUVERNANCE β vont au git »). Elles ne sont **pas** des
copies de substance : la partition 35/8 est **mesurée**, pas nominale.

| pièce | o | sha256 |
|---|---|---|
| `LC-BETA-00-PROMPT-PROJET.md` | 9236 | `e55db548a84724ee973bb82aaaf0cbeb6fea9aa2a1fd9d32a15ee997f5de57b7` |
| `LC-BETA-01-README.md` | 4634 | `1f18b2837ded2f16d207afdcaa39158c512f6a24a4c58c42a3a56bcfa015665c` |
| `LC-BETA-02-ETAT-BETA.md` | 8896 | `32c4e30651482a31685ac52e6d19c841dedb8fc2e6eaec3d992276107df05028` |
| `LC-BETA-03-CADRAGE.md` | 6765 | `1797922d7bccee00af67c697a4f1be8da558fd7af2cbeba18381d2d1b03579fe` |
| `LC-BETA-04-R41-MIROIRS.md` | 4358 | `078d5323a31f665660c9fa051ef273366b2a6ba2d170dfb4ef78f555aae3b2c8` |
| `LC-BETA-05-RETOUR-KB.md` | 4678 | `a6586b1ad9d99131eaef23c0f0760a561715957edc663197a2f63a4316496830` |
| `LC-BETA-BOOT.py` | 4327 | `5d5aa25f4288dfb94bfd40a23a8b766eae116a63b9d1b3c196c9f107a1202c76` |
| `LC-BETA-PAQUET-GEL.md` | 6179 | `2c8a3bd38f4df4151eda987404d8f386ea13fb59f00219ddfe315fb9c5e40659` |

**DÉPOSÉES AVEC LEUR DÉFAUT, NON CORRIGÉES.** Voir
`audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md` : elles **mentent par âge** sur P-8. Un
défaut du gel **se nomme par fichier séparé daté, jamais en place** ; la pièce
amendée **reste byte-intacte** (précédent S8/S9).

## 5. Ce que cette table ne fait pas

Elle ne rejoue pas `LC-BETA-BOOT.py`, ne recalcule pas `PKG_SHA_BETA_8`, n'atteste
aucune identité éditoriale et ne classe aucune source.

---

*§6.4 — concorder des octets ne scelle rien, ne réduit rien, ne démontre rien.
β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. CCC n'est ni démontrée ni réfutée.*
