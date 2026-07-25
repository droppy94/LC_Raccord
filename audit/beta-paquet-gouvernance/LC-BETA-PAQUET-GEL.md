---
id: LC-BETA-PAQUET-GEL
codename: LC-RACCORD-BETA
titre: "Manifeste du GEL DE DOSSIER β — 35 copies BYTE-EXACTES du mount principal, gelées au 2026-07-18 depuis l'état V94 / manifeste v2.121 / PKG-SHA principal 2b56338f (déclaré, à constater). Chaque ligne : nom canon ↔ sha256 des octets copiés. Le sha est celui du fichier du mount, canon-normalisé (suffixes __N_ du mount retirés)."
version: 0.1
langue: fr
date: 2026-07-18
grade: "MANIFESTE. N'atteste QUE des octets. N'atteste NI une physique, NI une actualité. R-36 : ce fichier ne porte PAS le PKG-SHA-BETA du paquet — il est consigné hors-fichier."
---

# Gel de dossier β — manifeste

> **Ce que ce manifeste permet, et c'est son seul intérêt :** comparer, ligne à ligne,
> `canon ↔ sha256` avec le manifeste courant de la KB principale. **Un sha qui diffère = la
> KB a bougé depuis le gel ⟹ la copie ment PAR ÂGE.** Le mount principal arbitre (R-54).
>
> **Vérification :** `python3 LC-BETA-BOOT.py` — attendu : 35 / `absents 0` / `alterees 0` /
> pare-feu `0/0`, et `PKG_SHA_BETA_8` égal à la valeur consignée **hors-fichier**.


## Tête du front β — LA pièce

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-G3-TRANSPORT.md` | `5a52ff9384974c9fcf4c53864cc11e2c0b99b40969d94bb618c67b1eb8821260` | 56146 |

## Structure d'O₂ : pourquoi β est seul

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-O2-FACTORISATION.md` | `7277ba6a13660d1d6a7d2c33a1d37ec3d071f30d9b8fbc4aeac46f15c12e9812` | 22906 |
| `LC-D-O2-COIN-TRANSMISSION.md` | `1b0e8276de84392cbf98e8af4fd4c631f81dd1ec56fc36bd355ce2c9000fbe9b` | 37241 |
| `LC-D-F6-G3-LAMBDA-BMS.md` | `4c84be568ab626c6e582f2ae1b5a29f150bf5ba36886a7c375796548470dc7eb` | 17055 |
| `LC-D-IRREDUCTIBILITE-MOYENS.md` | `3d1bd3d36fb9f83e485b592be317bbfdeee6f53326ce8218744e01c2dcba44f5` | 63914 |

## Le pivot Δ-C et son audit de fidélité

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-O2-DELTA-C.md` | `078a96a7230bcff0543f2adb4ccc13d1808df063c2519475cac235b4d5a92396` | 12068 |
| `LC-D-S7-FIDELITE-DELTAC.md` | `5ec402100e7b233bd951d8b850ef51fe799d7652253a506903e83e61ee52f2a4` | 11488 |

## Le levier d'admissibilité

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-G3-ADMISSIBILITE.md` | `f5a770e7e8c8289de6f41595567db23711bef51fd589624134f6705d4264a111` | 19147 |
| `LC-D-G3-ADM-IMPORTS.md` | `9c55868feac7f17592fa9d61d334497c762c7e974b3cc0a1ee69f05e7b465a2e` | 20268 |
| `LC-D-G3-KPS-KB.md` | `d8b31cdbc7e2d314c19586eca7c79d721f6643bf5ca32b81e06da97cbb04cbf7` | 12930 |
| `LC-D-G3-M4-CHAINON.md` | `93d3911ce1bcff5a7f790e95d09abbe8c17e92fb6f61f85d51b6d348aa07fe72` | 13287 |
| `LC-D-G3-GAP-STDEF.md` | `b90301de496eb3f1d6294a1199aff7d7d8dffd7382275b15337381cafb1bc66f` | 7377 |

## Socles holographiques amont (données POSÉES, non re-dérivées)

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-HOLOGRAPHIE-G3.md` | `759583cb5c6a8eab903582383971f15a1919358a90c64f51005c1c8eb36941f3` | 17161 |
| `LC-D-CT-DUAL.md` | `2b13e4c440d55e36c0d0237fe8c9b529339af8e25ec6fc6ec896fe5fe10c430e` | 37926 |
| `LC-D-CT-DUAL-DS.md` | `f70062c1057426dbb679d79e5626dacd5420b37ef13e353b44d3ace9a4f7c463` | 18072 |
| `LC-D-CT-REALITE.md` | `6e90ab7231c2a7ebe065b31b894484d873ed6cddf3e514a29de501baad53f62f` | 26078 |
| `LC-D-CT-GAMMA.md` | `e3f4de56207bece2dd1c236418bd9d42af402c19912a6fbd912916cf94fe9156` | 20490 |
| `LC-D3-SPECTRE-K3.md` | `6f5c1738540d4908a324456657328211e6975fa6f6fb2dac005f762bfe908550` | 24776 |
| `LC-D-F5-ETAT-RACCORD.md` | `9b3d23a69008041e979a4bafd4fd3731c7d2439174dd5bded016187e00848735` | 30423 |

## Chaîne O₂ (contexte de construction)

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-D-O2-C1-ADS.md` | `a32b2186a3633ea6e1160531843fe2a003109f922ae06727f97e05de45907301` | 29206 |
| `LC-D-O2-JONCTION.md` | `b5e017b5eea898376250028df2150b25e1fe1607e4880c9d9a12363f0482ad87` | 32840 |
| `LC-D-O2-P2.md` | `259bd1c7ecf079607f83c95b2497636938d75a6ebfb9fc098412d48aac4274fe` | 18987 |
| `LC-D-O2-P-SELECTEUR.md` | `1f1270fc3d2c3137785f079ae238936a78fc31dff00489630745af90926029f0` | 34691 |

## Cadrages GELÉS amont — l'audit anti-fit en dépend

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-WORK-CADRAGE-G3-TRANSPORT.md` | `b5276e68b61366dbf79caa0a7ea91da4f7ce4c69ed87670646b4a0bcb8f175eb` | 18424 |
| `LC-WORK-CADRAGE-G3-HORS-WEDGE.md` | `37bc85e52547ae60e54101e021f65594fb85b33817a6cb69039ef30efdc1e73f` | 20668 |
| `LC-WORK-CADRAGE-G3-DS4-GRAVITON.md` | `c2e91dcb98575db0ca13f86ded023abd21cf52949b0a06b02db1e89c0bb29089` | 25514 |
| `LC-WORK-CADRAGE-G3-ADMISSIBILITE.md` | `d3e1afc7f3da67976ffeee8a4df99e29c653d94e024b89455caf430a9f075a83` | 21992 |
| `LC-WORK-CADRAGE-G3-ADM-IMPORTS.md` | `8ed11d5f4fce7235e4abb533c1f5235d891c6ef0aa23347da61768157e3310d0` | 9381 |
| `LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION.md` | `172c3730e99425007f26160e7ceb7683f0365dd011f2a1873f12464780e041e8` | 16945 |
| `LC-WORK-CADRAGE-G3-M4-CHAINON.md` | `2d4f167ec70cf13441ca8703566edc806175fc3b78392909a642e72d5e3ae4fb` | 11211 |

## Gouvernance — le chantier doit être autoportant sur ses règles

| fichier (canon) | sha256 des octets | o |
|---|---|---|
| `LC-CONST-V1.md` | `a56c8cde2462925f138f93dc05e2e0c8edae67969c7546f72d2530f2f73e2cd7` | 15919 |
| `LC-JOURNAL-V94.md` | `b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c` | 12623 |
| `LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE.md` | `cc856f675801f241f119574318a16b4d0832eb5d24d6d15f056172e8b6af7830` | 19967 |
| `LC-WORK-AMENDEMENT-R7-PACKAGE-SHA-CONVENTION.md` | `eea2152cdc52899eb4932c39c36c4f796176ca870cadb883723f8d8d7e3a399d` | 15090 |
| `LC-WORK-R41-BORDEON-MIROIRS.md` | `61862243ca7143a41d50493571c02b24184141a498c0864edff0c2a776332d0d` | 9565 |

---

**Total : 35 fichiers, 781776 octets.** Aucun `.py` de sceau n'est
copié : un sceau ne vaut que **rejoué sur le mount principal**, jamais sur une copie.

**§6.4.** Copier des octets ne scelle, ne réduit, ne compte, ne démontre **RIEN**.
`{A4 ; A2★ ; N}` **INCHANGÉ** ; β `T-b`, SEUL facteur d'O₂ ouvert ; `R-53 0/4` ;
**CCC n'est ni démontrée ni réfutée.**
