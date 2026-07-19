# LC-SCEAU-S2-CACHE — CACHE DES SCEAUX EXECUTABLES

codename: LC-RACCORD | v1.0 | 2026-07-16 | session V87
statut: **actif**. Regi par LC-CONST-V1 §4.1 (amendee 2026-07-16).
grade: **INSTRUMENT.** Ne scelle rien, ne vote rien, ne fait foi de rien.
       En ecart avec le mount : **LE MOUNT A RAISON** (R-54).

## §1 — CE QUE CE FICHIER EST

La consignation **hors-fichier** (R-36) des sceaux S2. Pour chaque `.py` du mount :
sa cle `sha256( sha_py || sha_stack || sha_entrees_declarees )`, son `EXIT`, sa duree,
sa date, et le fait qu'il ait ete constate **en avant-plan**.

**Regle (§4.1).** Un sceau S2 est **acquis et le reste** tant que la cle est inchangee.
Rejeu **obligatoire ssi** la cle bouge. Sinon : **jamais**. Rejouer une fonction
deterministe sur des entrees gelees ne teste que la gelure des entrees — que la cle
teste mieux, et en ~40 ms.

**Ce que ce fichier N'atteste PAS (§4.2).** Un sha conforme n'atteste que **les octets**,
JAMAIS un EXIT 0, JAMAIS une conclusion physique. Les EXIT ci-dessous sont attestes par
leur **constat**, date et en avant-plan — pas par leur sha.

## §2 — POURQUOI CE FICHIER NE RECREE PAS LA BOUCLE §6.1

Ce cache est un `.md` : il est **hache dans le paquet**, donc son depot deplace le PKG-SHA.
Ce n'est **pas** un cout recurrent, et c'est le point :

> le cache ne change QUE lorsqu'un `.py`, la stack, ou une entree declaree change
> — c'est-a-dire **exactement** quand le PKG-SHA a **deja** bouge pour cette raison.

La consignation du cache est donc **coportee** par un mouvement qui devait de toute facon
etre consigne. Elle n'ajoute **aucune ceremonie propre**. Un cache qui bougerait a chaque
session serait, lui, une boucle §6.1 — celui-ci ne bouge que sur evenement reel.

## §3 — DEFAUT FONDATEUR, CONSIGNE ET NON ESCAMOTE

Ce cache existe parce que le mecanisme qu'il remplace **produisait des preuves incompletes
en silence**. Constat V87, 2026-07-16 :

- la chaine `setsid` du boot annonce « canaris_lances : 2 process » ;
- `verif_nonlin_parity` a fini (`EXIT=0`, T0+162s) ;
- `verif_D3_P6_specB_oracle` a ete **tue a ~T0+199s sans ecrire d'`EXIT=`** ;
- `FINI` **absent** ; 0 process vivant a T0+2282s.

Le `setsid` **n'a pas survecu** entre deux appels d'outil. Un §0-full « frais » se serait
donc atteste sur une **chaine morte**. Second constat : le boot facture « >=600s chacun » ;
les durees reelles sont **160s et 133s**. La facture etait fausse d'un facteur ~4.

**Consequence de grade :** les 7 EXIT ci-dessous ont ete rejoues **en avant-plan** en V87,
y compris `nonlin` dont l'`EXIT=0` detache etait pourtant valide. Amorcer un cache cru
indefiniment depuis un mecanisme dont la defaillance est prouvee aurait mis un defaut
connu **a la racine de l'arbre**.

## §4 — ENTREES DECLAREES (§4.1) — un ACTE, jamais une inference

Sonde du 2026-07-16 sur les 7 `.py` (motif `open|Path|glob|listdir|.md|/mnt/|import verif`) :
**6/7 sont des fonctions pures** (`sha_entrees` = vide). Exception **unique et nommee** :
`verif_paquet_propre.py`, qui lit `LC-WORK-NACTION-AVEUGLE-PAQUET.md` (l.106, `open(PKG)`)
et exige `cwd=/mnt/project`. Cette entree est **elle-meme hachee dans le paquet** : toute
modification deplace le PKG-SHA. **L'exception s'auto-signale.**

**Obligation permanente.** Tout nouveau `.py` **declare ses entrees** a son depot.
Un `.py` dont les entrees ne sont pas declarees **n'est PAS scellable S2** — le comparateur
le classe `NON SCELLABLE`, et c'est un defaut a consigner, pas un acquis a presumer.

### §4bis — INSTRUMENTS EXCLUS DE S2 (ajout v1.1, 2026-07-16)

Un **instrument** n'asserte aucune physique et ne scelle rien : il n'y a rien a rejouer,
rien a attester. Il est **hors S2**. Liste **nommee** :

| instrument | motif |
|---|---|
| `sceau_s2.py` | le comparateur lui-meme |

**L'exclusion est par NOMS EXPLICITES, jamais par motif**, et c'est la lecon : un motif
(`^sceau_`, `*_s2.py`) avalerait **en silence** tout fichier futur ainsi nomme. Ajouter une
ligne a cette table est une **DECISION**, visible et contestable.

**Defaut fondateur de §4bis — 10e entree a la dette d'instrument du pilote.**
`sceau_s2.py` **v1.0 se scannait lui-meme**, ne se trouvait pas au cache, se declarait
`NON SCELLABLE`, et rendait **`rc=1` A PERPETUITE**. Un boot testant `rc` aurait donc
toujours echoue ==> on aurait appris a **ignorer son verdict**, ce qui est pire qu'aucun
verdict. **MEME FAMILLE que la 8e** (le scan qui se matche lui-meme) **et la 9e**
(`pkill -f verif_` qui a tue son propre shell) : **troisieme occurrence du meme motif.**
Le pilote l'avait ecrite dans le corps de la constitution et l'a reproduite dans la foulee.

**Verification de non-regression (v1.1, 2026-07-16) :** injection d'un `.py` intrus non
declare ==> toujours classe `NON SCELLABLE`, `rc=1`. **L'exclusion n'absout que ce qu'elle
nomme.**

## §5 — USAGE

    python3 sceau_s2.py     # comparateur. Ne rejoue rien. Dit quoi rejouer. D decide.

`EXIT 0` = tous acquis. `EXIT 1` = au moins un rejeu du. `EXIT 2` = cache absent/illisible.

## §6 — DONNEES

```json
{
 "cpu": 1,
 "date": "2026-07-16",
 "entrees": {
  "diag_bounces.py": [],
  "verif_A2_numerique.py": [],
  "verif_A4_QW.py": [],
  "verif_A4_QW_typeI_succ.py": [],
  "verif_D3_P6_specB_oracle.py": [],
  "verif_nonlin_parity.py": [],
  "verif_paquet_propre.py": [
   "LC-WORK-NACTION-AVEUGLE-PAQUET.md"
  ]
 },
 "sceaux": {
  "diag_bounces.py": {
   "cle": "4d504f297a8d736e981f2d3b82245ef599002ab95ffc05bc319eb9b4cc10cc47",
   "date": "2026-07-16",
   "duree_s": 7,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "804b7f9bf9453762a81d85933a5a823135dd985252d27a4b511f1d58486588d4"
  },
  "verif_A2_numerique.py": {
   "cle": "1ab0a6e3dac71ce5e7934d6a1d22802f09216f12b2edcb2733c32c2143636881",
   "date": "2026-07-16",
   "duree_s": 1,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "76e9257cfdd337b684c22222d55c5533c233d39196adf1e3466405737d345b44"
  },
  "verif_A4_QW.py": {
   "cle": "7d195a1ae2ea9b91c4a01b9b4cf166467ff1db75106cc4dae9f8960959332fc6",
   "date": "2026-07-16",
   "duree_s": 3,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "a4637a2cd07e2f0437be64743c084b2172cd4497ccd1bd9a42ce54c9d7257387"
  },
  "verif_A4_QW_typeI_succ.py": {
   "cle": "a18893e367a121297d974fa2977c37ee4e05d76b46854714b9029d5ec0880134",
   "date": "2026-07-16",
   "duree_s": 2,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "79f09a8c5b30a7ac426c5c7f8a67c332120a1ae3e8968e283364318c34a46f5c"
  },
  "verif_D3_P6_specB_oracle.py": {
   "cle": "1c75b7229da0b142a1c9f5b99209b97a0fd9decb4224ad432111e807f7795779",
   "date": "2026-07-16",
   "duree_s": 133,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "162696c131f55ea2325f668a214476709a7d80271b7bcc5f88349a9772f146a1"
  },
  "verif_nonlin_parity.py": {
   "cle": "870f33bbbc78ac94ef365cdf5f238c27b2ff4083250199abb38a04485b2e8224",
   "date": "2026-07-16",
   "duree_s": 160,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [],
   "sha_py": "9df8e53e8f529fa8a0803547b09162fb34d15ba79b37c4d1836442a7238896a7"
  },
  "verif_paquet_propre.py": {
   "cle": "eac1727aa90e2097306aeee23da16570c9c8009e2e027fc33d320d29df9004de",
   "date": "2026-07-16",
   "duree_s": 0,
   "exit": 0,
   "mode": "avant-plan",
   "session": "V87",
   "sha_entrees": [
    "635e2c6546a158554bc81648ba6224c0600a13517baff2b4af32c52d82a05a13"
   ],
   "sha_py": "051e28335c1409f49c75fd30d1c67d50fbcdb0ad3227a8c71668492d9c3ab6db"
  }
 },
 "schema": "LC-SCEAU-S2-CACHE/1.0",
 "session": "V87",
 "sha_stack": "2a578f377f99a9ab4bac54156c76dc7143610b61618f8f11b1c5aed4e52bb622",
 "stack": "3.12.3/1.14.0/2.4.4/1.17.1/3.6.1"
}
```

## §7 — §6.4 SENTINELLE

Cacher des sceaux, comparer des cles, rejouer sept scripts : cela **NE SCELLE, NE REDUIT,
NE COMPTE, NE DEMONTRE RIEN**. `{A4 ; A2* ; N}` **INCHANGE**. Pivot O2 clos negatif.
Tetes scellees = autorite, intactes. CCC non demontree NI refutee.
`etabli (algebre)` atteste l'algebre correcte, **jamais** une conclusion physique.
