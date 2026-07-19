---
id: LC-WORK-AMENDEMENT-R7-NOTE07-CSE-REDACTION
titre: "Amendement R-7 DATÉ — rédaction MINIMALE, ÉNUMÉRÉE et PRÉ-ENGAGÉE d'un identifiant fuyant dans les COPIES du paquet CSE de NOTE-07. Motif : le nom de fichier `LC-D-F6-BORDEON-VA` ENCODE l'issue d'une adjudication VOISINE (même corpus BORD-EON, mêmes étiquettes {V-A..V-D}) et figure DANS le cadrage GELÉ (`32b76fd5`, borne b2 + renvois) ainsi que dans la note de gate (`89f9da27`, §6.4 + renvois) ⟹ l'exclusion de la pièce `LC-D-F6-BORDEON-VA` du paquet est INOPÉRANTE, la fuite passe par le texte gelé lui-même. PORTÉE STRICTEMENT PROSPECTIVE et MONOTONE-SÛRE : la rédaction RETIRE un prior directionnel, n'en ajoute AUCUN ; elle ne touche NI §3 (espace-verdict {V-A..V-D}), NI §4 (D1–D5 + mapping figé), NI §5 (F#1–F#4) du cadrage — invariants LOAD-BEARING conservés TELS QU'ÉCRITS. Le mount est INTOUCHÉ ; le gel `32b76fd5` demeure l'autorité, INTACT, NON re-gelé. SANS SURCLASSEMENT (§6.4) : amender une règle d'exposition ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé (≡Λ, terminus ouvert) ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 daté (décision de scope postérieure à un gel, formalisée AVANT exécution) — n'adjuge pas, n'importe pas, ne fetch pas, ne re-gèle pas le cadrage amendé"
statut: "AMENDEMENT DATÉ 2026-07-14 — PRÉ-ENGAGÉ AVANT tout envoi du paquet CSE NOTE-07 (R-7 anti-fit : aucune décision de scope après lecture d'un résultat ; ici, AUCUN rapport d'auditeur n'existe, AUCUNE issue {V-A..V-D} n'est tranchée, l'adjudication est PENDANTE). Amende le cadrage `LC-WORK-CADRAGE-BORDEON-NOTE07-FUSION-N` (gel R-36 `32b76fd5`, INTACT, NON re-gelé) sur le SEUL point de l'EXPOSITION des pièces à l'auditeur incognito — PAS sur son contenu normatif. Le cadrage sur le mount reste l'autorité et n'est PAS modifié. Adjudication de substance RÉSERVÉE au CSE souverain incognito ; pilote DISQUALIFIÉ ; en cas de discordance, l'incognito prévaut. {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
version: "0.1"
langue: fr
date: "2026-07-14"
gel_R36: "ce fichier N'EMBARQUE PAS son propre sha256 (anti-auto-référence). Le gel R-7/R-36 est horodaté HORS-FICHIER au dépôt, byte-exact livrable==mount."
tags: [amendement, R-7, anti-fit, date, pre-engage, gel-R-36, NOTE-07, BORD-EON, CSE, incognito-souverain, pilote-disqualifie, zero-fuite, fuite-par-identifiant, ancrage, redaction-enumeree, transparence-exposition, monotone-sur, prospectif, R-54, §6.4, non-surclassement]
renvois: [LC-WORK-CADRAGE-BORDEON-NOTE07-FUSION-N, LC-WORK-R41-NOTE07-MIROIRS, PROMPT-INCOGNITO-NOTE07-FUSION-N, PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE, PROMPT-INCOGNITO-A2STAR-P1-ORHO, NOTE-BORD-EON-07_V1dia1b-fusion-memoire, NOTE-BORD-EON-06_V1dia1-weyl-verdict]
maj: "2026-07-14 — v0.1 : création sur GO Thierry, session V79, APRÈS §0-full (7/7 sceaux LIVE EXIT 0) et APRÈS lectures R-54 (gels `32b76fd5` et `89f9da27` VÉRIFIÉS BYTE-EXACT sur le mount), AVANT tout envoi CSE. Fuite débusquée par SCAN DE BLINDING AUTOMATIQUE sur les 6 pièces JOINDRE. §6.4 : {A4 ; A2★ ; N} INCHANGÉ ; aucune issue {V-A..V-D} tranchée ; N non fixé (≡Λ) ; CCC non démontrée NI réfutée."
---

# Amendement R-7 — rédaction d'un identifiant fuyant (paquet CSE NOTE-07)

> **Nature de l'acte.** Décision de **scope** prise **après** le gel `32b76fd5` ⟹ R-7 impose un
> **amendement daté**, **pré-engagé avant exécution**. Cet amendement **n'adjuge rien**, ne touche
> **aucun** invariant normatif du cadrage, et **ne modifie pas le mount**.

## §1 — Le défaut constaté (fait, non interprétation)

Le paquet CSE exclut délibérément la pièce `LC-D-F6-BORDEON-VA` — chaînon d'**issue** d'une
adjudication **voisine** (même corpus BORD-EON, **même espace-verdict** {V-A ; V-B ; V-C ; V-D}) —
au motif d'**ancrage** : un auditeur informé que la précédente a atterri sur **V-A** est ancré vers
V-A sur celle-ci.

**Le scan de blinding automatique établit que cette exclusion est INOPÉRANTE.** L'identifiant
`LC-D-F6-BORDEON-VA` **encode l'issue dans son nom** et figure **dans deux pièces JOINDRE** :

| Pièce | Locus | Occurrence |
|---|---|---|
| Cadrage `32b76fd5` (**GELÉ**) | front-matter l.8 | `renvois: [… LC-D-F6-BORDEON-VA …]` |
| Cadrage `32b76fd5` (**GELÉ**) | §7 **borne b2**, l.152 | « … et le chaînon `LC-D-F6-BORDEON-VA` restent intacts §10 » |
| Note de gate `89f9da27` | front-matter l.8 | `renvois: [… LC-D-F6-BORDEON-VA …]` |
| Note de gate `89f9da27` | §6.4 terminal, l.134 | « … et le chaînon `LC-D-F6-BORDEON-VA` » |

**Chaîne inférentielle** : espace-verdict {V-A..V-D} remis à l'auditeur **+** fichier nommé
`…-BORDEON-VA` **+** qualifié de « **le chaînon** » (motif exact du chaînon d'**issue**) ⟹ l'issue
voisine **V-A** est reconstituée en une inférence. **La fuite passe par le texte gelé lui-même.**

## §2 — Pourquoi un amendement est requis (et non un simple caviardage)

La note de reprise V79 §4.1 et le cadrage §6 imposent l'adjudication contre l'espace-verdict
**TEL QU'ÉCRIT — jamais reformulé**. Rédiger un identifiant dans les copies remises à l'auditeur
est une **décision de scope postérieure au gel** ⟹ **R-7 exige un amendement daté** (borne b1 du
cadrage : « aucun élargissement/rétrécissement … sans amendement R-7 daté »).

**Pré-engagement attesté** : cet amendement est rédigé **avant** tout envoi, **avant** l'existence
de tout rapport d'auditeur, **avant** que la moindre issue {V-A..V-D} soit tranchée. Il ne peut
donc pas être un ajustement post-résultat.

## §3 — La rédaction autorisée (ÉNUMÉRÉE, EXHAUSTIVE, CLOSE)

**Substitution unique autorisée**, sur la **chaîne littérale** :

    LC-D-F6-BORDEON-VA   →   [CHAÎNON-VOISIN-RÉDIGÉ]

**Loci — liste CLOSE (4)** : cadrage front-matter `renvois` ; cadrage §7 b2 ; note de gate
front-matter `renvois` ; note de gate §6.4 terminal. **Aucun autre locus. Aucune autre chaîne.**

**Périmètre d'application** : **copies du paquet CSE UNIQUEMENT**. Le **mount est INTOUCHÉ** ; les
fichiers `LC-WORK-CADRAGE-BORDEON-NOTE07-FUSION-N` et `LC-WORK-R41-NOTE07-MIROIRS` conservent leurs
sha `32b76fd5` et `89f9da27`, **INTACTS**, et demeurent **l'autorité** (R-54). Le cadrage n'est
**NI modifié NI re-gelé**.

## §4 — Invariants LOAD-BEARING conservés TELS QU'ÉCRITS (non touchés)

- **§3 du cadrage — espace-verdict {V-A ; V-B ; V-C ; V-D}** : **INTACT**, verbatim.
- **§4 du cadrage — discriminants D1–D5 + mapping figé** : **INTACT**, verbatim.
- **§5 du cadrage — firewalls F#1–F#4** : **INTACT**, verbatim.
- **§7 bornes b1–b5** : **INTACTES** ; seule l'**étiquette** de b2 est rédigée. **Le sens de b2 est
  intégralement préservé** : « les sceaux du cœur et le chaînon voisin restent intacts §10 quelle
  que soit l'issue » — la borne protège les sceaux, elle continue de le faire.
- **§2 de la note de gate — C-1/C-2/C-3** et **§3 — faits (f1)–(f6)** : **INTACTS**, verbatim,
  toujours **sans mapping** vers D1–D5.

## §5 — Monotonie et sûreté

- **Prospectif.** S'applique aux copies d'un paquet **non encore envoyé**. Ne reclasse **aucune**
  adjudication souveraine antérieure. **Aucun re-audit** déclenché.
- **Monotone-sûr.** La rédaction **RETIRE** un prior directionnel (vers V-A) et **n'en ajoute
  aucun**. Elle ne peut donc pas *fabriquer* une issue : elle **élargit** l'espace effectivement
  ouvert à l'auditeur, elle ne le rétrécit pas. Un verdict rendu **sans** l'ancrage est **a fortiori**
  au moins aussi robuste qu'un verdict rendu **avec**.
- **Asymétrie non traitée, CONSIGNÉE.** Le cadrage `32b76fd5` **n'est pas anti-fit-symétrique**
  (bornes b4/b5 posent un **défaut** ; V-A est libellé assertivement ; V-C porte une charge
  unilatérale lourde). Cet amendement **ne corrige PAS** cette asymétrie — la corriger **serait**
  une reformulation R-7 illégitime. Elle est traitée par **transparence d'exposition** : le harnais
  la **déclare** et charge l'auditeur d'**adjuger en Phase 3 si ce défaut est un firewall légitime
  ou un fit**. Le pilote **ne tranche pas** ce point.

## §6 — Obligations d'exécution (opposables au paquet)

1. **Déclaration à l'auditeur.** Le harnais **doit** indiquer qu'**un identifiant a été rédigé pour
   prévenir un ancrage sur une adjudication voisine**, que la rédaction est **énumérée**, et qu'elle
   **ne touche ni l'espace-verdict, ni les discriminants, ni le mapping, ni les firewalls**.
   **Rien n'est dissimulé à l'auditeur quant à l'existence de la rédaction.**
2. **Re-scan obligatoire.** Scan de blinding automatique **rejoué sur les copies rédigées** ; sortie
   attendue : **0 occurrence** de `BORDEON-VA` sur les 6 pièces.
3. **PACKAGE-SHA recomputé** sur les **copies rédigées** (le PACKAGE-SHA provisoire `e69a3686`,
   calculé sur les pièces **non rédigées**, est **PÉRIMÉ** par cet amendement).
4. **Attestation hors-fichier** des sha des copies rédigées, au dépôt.
5. **Toute rédaction hors des 4 loci énumérés au §3 est INTERDITE** et exigerait un **nouvel**
   amendement daté.

---
> **SANS SURCLASSEMENT (§6.4).** Amender une règle d'**exposition** ne scelle/réduit/compte/démontre
> **RIEN**. Le cadrage `32b76fd5` reste **l'autorité**, **INTACT**, **NON re-gelé** ; le mount est
> **INTOUCHÉ**. **AUCUNE issue {V-A..V-D} n'est tranchée** ; le pilote est **DISQUALIFIÉ** pour le
> faire ; l'adjudication de substance reste **PENDANTE** (CSE souverain incognito ; en cas de
> discordance pilote/incognito, **l'incognito prévaut**). Charge de preuve **V-C INCHANGÉE**
> (re-dériver `D3 = I-a`, fixation de N **non-circulaire** échappant au collapse `N ≡ S_dS`,
> load-bearing **contre le survey scellé**, avant de heurter **F#1**). `{A4 ; A2★ ; N}` **INCHANGÉ** ;
> D1 non clos ; **N non fixé** (≡Λ, terminus ouvert — voie A close, clôture R-53 conditionnelle
> **0/4**) ; O₂ non construit ; voie H ∉ périmètre ; β T-b ; A4 route par-𝓘⁺ délimitée (W2), postulat
> renforcé, **NON réfuté** ; A2★ parqué pending OA ; **CCC non démontrée NI réfutée**.
