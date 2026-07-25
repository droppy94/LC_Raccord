---
id: LC-WORK-REGISTRE-CORPUS-AMENDEMENT-1
titre: "Amendement 1 au registre de corpus — CINQ PREMIÈRES MESURES des corps d'assaut β (arbitrage opérateur « mesurer maintenant », 2026-07-25) et CONFRONTATION D'OCTETS du journal V94, seule entrée non reconstituable du paquet β. Le registre reste BYTE-INTACT."
codename: LC-RACCORD
type: "amendement daté. Il ne modifie pas le registre en place. Il n'atteste ni un titre, ni des auteurs, ni un DOI, ni un grade — seulement des octets mesurés, et l'aveu de ce que ces mesures ne peuvent pas faire."
version: 1.0
langue: fr
date: 2026-07-25
session: S17
---

# Amendement 1 au registre de corpus

## 0. Pourquoi cet amendement existe

Deux arbitrages d'opérateur du 2026-07-25 :

1. **§3 du registre — « sha NON MESURÉS » des cinq corps d'assaut : MESURER MAINTENANT.**
   L'option « réserve permanente » a été **explicitement écartée**.
2. Le **journal V94**, seule entrée du paquet β sans contrepartie `kb/`, a été **fourni en
   octets** par l'opérateur.

Le registre `audit/LC-WORK-REGISTRE-CORPUS.md` n'est **pas modifié**. Un défaut de portée se
nomme par fichier séparé daté (précédents S8/S9).

## 1. LES CINQ CORPS D'ASSAUT — PREMIÈRES MESURES

Livrés par l'opérateur dans une archive unique. **Atelier séparé**, hors dépôt, hors mount,
hors répertoire de paquet gelé (précédents S15 nº2 et nº3). `%PDF` en tête et `%%EOF` en
queue : **5/5**.

| identifiant | version LIVRÉE | octets | sha256 | p. | assaut d'origine |
|---|---|---|---|---|---|
| `arXiv:0808.2054` | **v1** | 251 186 | `fcfebce6a898003855f36c325f6805f81748eea28ba86d93aa466d46eafb42d9` | 32 | `S-G3T-4b` (de Haro) |
| `arXiv:2007.06800` | **v4** | 2 521 998 | `5be89da3493def54d9592db5338cbf76a015332caa78aea2eb72ce87483b1909` | 57 | `S-G3T-2` (wedge, AdS/BCFT) |
| `arXiv:2409.08709` | **v4** | 723 288 | `d5e3a1de38c6e12cf50f64d85262f819a1e73a1677c079084ec498abcdc4aa4f` | 26 | `S-G3T-4b` (ST) |
| `arXiv:2412.00183` | **v1** | 1 140 406 | `eb3ddc9c8a8b4906299a655bc6c581c7596775075bb126c301b9c8decb9c4e7a` | 51 | `S-G3T-3b` |
| `arXiv:2606.09170` | **v2** | 537 107 | `3d8580a515c9873f9b880525f8609e76427e18413f8cb0222e9d29c63261eecd` | 35 | `S-G3T-3b` |

### 1.1 Identité lue DANS LES OCTETS D'ABORD — 5/5 concordantes avec l'attribution du registre

| identifiant | auteurs / titre lus dans les octets | attribution registre §3 |
|---|---|---|
| `0808.2054` | **Sebastian de Haro** (Utrecht, ITP-UU-08/49 · SPIN-08/39) — *Dual Gravitons in AdS4/CFT3 and the Holographic Cotton Tensor* | « de Haro » ✓ |
| `2007.06800` | Akal, Kusuki, Takayanagi, Wei (YITP Kyoto, IPMU) — *Codimension two holography for wedges* | « wedge, AdS/BCFT » ✓ |
| `2409.08709` | **Silverstein, Torroba** — *Timelike-bounded dS4 holography from a solvable sector of the T² deformation* | « ST » ✓ |
| `2412.00183` | Salehi Vaziri (Amsterdam) — *A non-perturbative construction of the de Sitter late-time boundary* | `S-G3T-3b` ✓ |
| `2606.09170` | Hao, Ouyang, Ran (Jilin) — *Stress Tensor Deformations in dS/CFT: Mixed Boundary Conditions, Spectrum Flow and Pseudo Entropy* | `S-G3T-3b` ✓ |

**Ordre R-54 tenu** : identité lue dans les octets, jamais obtenue par recherche puis soumise
à confirmation.

### 1.2 CE QUE CES MESURES NE FONT PAS — et c'est plus lourd que le registre ne l'annonçait

**LE REGISTRE §3 N'A JAMAIS PORTÉ DE COLONNE DE VERSION.** Les cinq corps y sont inscrits en
identifiants nus. **On ne sait donc pas quelle version chaque assaut a lue.**

Le registre annonçait, à son §3, qu'une re-mesure produirait « des sha de **première mesure**,
pas des confrontations ». **C'est vrai, et insuffisant.** Il faut écrire le degré au-dessus :

> **On ne peut même pas affirmer que les versions mesurées ici sont celles qui ont été lues.**

**Les verdicts `S-G3T-*` ne deviennent PAS traçables rétroactivement.** Ils gagnent une
référence **à compter d'ici**, et rien de plus. L'écart que le registre annonçait comme
« se paiera à la première bascule de branche » n'est pas effacé : il est **borné et daté**.

**Ces cinq sha font référence à compter de cette pièce.** Toute mesure ultérieure les
confrontera ; celle-ci ne confronte rien.

### 1.3 Ce que je n'ai pas fait

**Les cinq corps N'ONT PAS ÉTÉ LUS.** L'arbitrage disait *mesurer*, pas *consommer*. Rouvrir
un assaut `S-G3T-*` exige son propre gel et son propre GO.

**Fait signalé, NON EXPLOITÉ** : `2606.09170v2` porte « Mixed Boundary Conditions » en dS/CFT
**dans son titre**. C'est un corps d'**assaut**, pas une ligne du périmètre `S-B1`, et `FB-2`
enregistre déjà qu'il a fait tomber `F3′` et `F3″`. **`S-B1` n'est pas rouvert par cette
pièce.**

## 2. JOURNAL V94 — CONFRONTATION D'OCTETS, CONCORDANTE AU BIT PRÈS

| | sha256 | octets |
|---|---|---|
| **octets fournis** par l'opérateur | `b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c` | 12 623 |
| **déclaré** à `audit/LC-BETA-PAQUET-CONCORDANCE.md`, ligne `BETA-COPIE-LC-JOURNAL-V94.md` | `b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c` | — |

**CONCORDANT.** C'est la **première confrontation d'octets de la session S17** : tout le reste
— les sept lignes du périmètre `S-B1`, les quatre archives du mount — n'a été confronté qu'en
**contenu**.

**Conséquence sur le paquet β : il est intégralement soldé.** 43 entrées = **8** pièces
`LC-BETA-*` déposées byte-intactes + **35** `BETA-COPIE-*`, dont **34** reconstructibles par la
table de concordance et **1** sans contrepartie `kb/` — le journal V94, **désormais
byte-confronté**. **Il n'y a plus de trou.**

### 2.1 LES OCTETS DU JOURNAL NE SONT PAS DÉPOSÉS, ET C'EST UN INTERDIT DUR

`BETA-COPIE-LC-JOURNAL-V94.md` est une **copie de substance**. Le pare-feu, à sa portée réelle
mesurée à sa source (`LC-BETA-05` §1), et le prompt S17 §5(e) : toute copie de substance est
**interdite au dépôt, ARBRE ET HISTORIQUE**.

Le fichier a été fourni sous le nom `LC-JOURNAL-V94.md`. **Le déposer sous ce nom serait
exactement le geste interdit** : *ne renomme jamais une pièce pour passer sous un contrôle
nominal*. **Ce qui est déposé, c'est la confrontation. Pas les octets.**

Le journal reste **mount-seul de droit sous G-4**. Sa fourniture ponctuelle par l'opérateur ne
change pas son régime : elle **solde une vérification**, elle n'ouvre pas un dépôt.

## 3. Faits de surface, nommés

- **Compte déclaré ≠ compte mesuré.** L'opérateur annonce « les 4 fichiers pdf requis » ;
  l'archive en porte **5**, et ce sont les cinq demandés. **Livraison complète** — l'écart est
  en faveur de la livraison, et il se nomme quand même.
- **Le nom d'un conteneur ne décrit pas son contenu.** L'archive s'appelle
  `2409_08709v4.zip` et transporte **cinq** corpus. **Troisième occurrence en S17** du même
  motif, après les sept `.pdf` du mount qui étaient des ZIP.

## 4. Ce que cet amendement ne fait pas

Il ne modifie pas `audit/LC-WORK-REGISTRE-CORPUS.md`, ne dépose aucun octet, ne rouvre aucun
assaut, ne classe aucune source, n'ouvre aucune gate, ne touche aucun verdict, et **ne rend
traçable aucun verdict passé**.

---

*§6.4 — hacher, dater, confronter, inscrire : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. Un sha de première mesure n'atteste que lui-même.
β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
