# R-7 — CIBLES GELÉES (protocole §2.0, étape 1) — 2026-07-22 (session S7)

Source : front-matter SEUL de `kb/LC-D-A4-QW.md` v0.4 (sha256 du fichier
entier `ebcf3d9babdaa33b…`, 17665 octets, 159 lignes). **Corps = lignes 16
à 159, NON OUVERT** ; front-matter clos ligne 15.

Prérequis KB déclarés par la tête (`LC-WORK-CADRAGE-A4-QW`,
`LC-WORK-AMENDEMENT-R7-A4-QW-PHASE0`, `LC-D-IRREDUCTIBILITE-MOYENS`,
`LC-D3-WEYL-BUNCHDAVIES`, `LC-D-CB-WEYL-MAGNETIQUE`, `LC-D-G3-ADM-IMPORTS`)
et amendements (`…-TYPEI-CORR`) : **NON OUVERTS**, conformément à
« reprise de ZÉRO depuis `LC-D-A4-QW` SEULE » (note S6 §5.2).

Piège R-36 : ce fichier ne porte pas son propre sha ; il est calculé par
commande et consigné hors-fichier au rapport de lot.

---

## 0. PLAFOND DE GRADE — ANNONCÉ AU GEL, AVANT LA PREMIÈRE LIGNE D'INSTRUMENT

**Plafond : REPRODUIT-SOUS-RÉSERVE (E-2). E-1 est INATTEIGNABLE sur ce lot.**

Quatre motifs, nommés au gel et non rattrapables en aval :

- **M1 — le front-matter révèle le MÉCANISME.** Il n'énonce pas seulement le
  verdict W2 : il donne la chaîne causale (« le no-hair tue le Weyl NU au taux
  e^(−3Ht) — et ce taux EST la branche Δ₊=3 qui alimente g₃ ⟹ le flot
  TRANSCRIT »). C'est l'angle mort du §2.0 déjà nommé dans
  `audit/RESERVE-AVEUGLEMENT-R4-R5.md`, ici à un degré supérieur.
- **M2 — le front-matter révèle des VALEURS.** `Σq²=2/3`, `g₃=−4q_i`,
  `𝓔=−6q_i`, `𝓔=(3/2H)g₃`, `𝓑=(1/H)C[g₀]`, taux `3`, `Einstein 10⁻¹⁵`. Une
  redérivation qui « retrouve » ces nombres les a lus. Précédent R-1 (E-2 pour
  « valeurs révélées »).
- **M3 — le cœur est un THÉORÈME IMPORTÉ.** Le no-hair de Wald (1983, Λ>0,
  SEC+DEC) n'est pas redérivable en interne ; il est le socle du domaine
  établi. Précédent R-1 (Friedrich).
- **M4 — une part des cibles n'est pas une algèbre.** Q9 et Q10 (conditionnalité
  des types, réserves d'intégrité de l'audit froid) sont des ÉNONCÉS DE STATUT :
  ils se consignent, ils ne se « PASSent » pas. Toute tentative de les compter
  en PASS serait un assert tautologique — défaut E-3 au sens du CSE, précédent
  S6 §3.

Conséquence opposable : **aucun résultat de ce lot ne pourra être gradé E-1**,
quelle que soit la qualité de l'instrument. Le grade réellement atteint pourra
être INFÉRIEUR (E-3 si un assert se révèle tautologique, NON-REPRODUIT si une
cible tombe).

---

## 1. Cibles gelées

| # | cible | énoncé revendiqué par la tête |
|---|---|---|
| **Q1** | domaine établi | branche Bianchi, no-hair de Wald 1983, Λ>0, SEC+DEC — le domaine où le no-hair EST établi |
| **Q2** | taux de décroissance du Weyl NU | le no-hair tue le Weyl **nu** au taux `e^(−3Ht)` |
| **Q3** | identification de branche | ce taux **EST** la branche indicielle `Δ₊ = 3` qui alimente `g₃` ⟹ le flot **TRANSCRIT** l'anisotropie au bord au lieu de l'effacer (mécanisme du « résidu-cassant ») |
| **Q4** | secteur électrique | `𝓔 = (3/2H)·g₃` |
| **Q5** | type I vide — contrainte et résidu | `Σq² = 2/3` (exclut `q=0`) ⟹ `𝓔` **JAMAIS nul** au type I vide ; `g₃ = −4q_i` ; `𝓔 = −6q_i`, sans trace |
| **Q6** | secteur magnétique | `𝓑 = (1/H)·C[g₀]` ; **identiquement** non nul au type II : `Cotton[Nil] ≠ 0`, porté par `g₀`, **INDÉPENDANT des données** |
| **Q7** | exception isotrope (successeur [05']) | l'universalité de `g₃=−4q_i` est **RETIRÉE** : de Sitter `a_i=e^{Ht}` est le membre isotrope **vide** (`ρ=0`, `g₃=0`) ; le point `q=0=sinh^{1/3}` est isotrope **NON vide**. W2 **générique** INCHANGÉ |
| **Q8** | verdict | **W2 (résidu-cassant)** dans l'espace pré-gelé `{W1 / W2 / W3}` — le chaînon « no-hair ⟹ Weyl-rescalé-propre » **CASSE** là même où le no-hair est établi |
| **Q9** | conditionnalité (STATUT, non-algébrique) | types `{I, V, II}` calculés ; `VI/VII/VIII` **NON EXÉCUTÉS** ; racines indicielles `{0,3}` ; `d=3` impair ⟹ pas de log ; séries FG tronquées aux ordres `≤ v⁴` (piège `v⁵` détecté et contrôlé) |
| **Q10** | réserves d'audit (STATUT, non-algébrique) | assert `[10]` **semi-vacant** (arithmétique sur polynôme codé en dur ; conclusion vraie, re-dérivée par l'auditeur) ; `[06]/[07]` (FG types V/II) **non reproduits** par l'auditeur, **NON load-bearing** — W2 tient sur **type I + Nil** |
| **Q11** | sceaux (comptes exacts à rejouer) | `verif_A4_QW.py` LIVE sha8 `a4637a2c` — EXIT 0, **14/14 = 10 asserts porteurs + 4 mutations firewall** ; `verif_A4_QW_typeI_succ.py` LIVE sha8 `79f09a8c` — standalone, EXIT 0, **8/8** |
| **Q12** | garde-fou de non-surclassement | W2 = **DÉLIMITATION** de la route A4-par-𝓘⁺ ; statut de **postulat** de A4 **RENFORCÉ** ; **A4 NON réfuté** ; `{A4 ; A2★ ; N}` INCHANGÉ |

## 2. Critère d'adjudication — gelé tel qu'écrit

Une cible `Q1–Q8` est REPRODUITE si et seulement si sa valeur ou son énoncé
est obtenu par un calcul **discriminant** : coefficient sorti d'un `solve`,
d'une série ou d'un calcul tensoriel — **jamais d'une affectation littérale**
(précédent S6 §3). Toute loi de transformation se teste en **recalculant les
deux configurations**. Toute mutation de firewall doit **mordre** ; une
mutation invariante est **VACANTE** et se remplace, elle ne se compte pas.

`Q9`, `Q10`, `Q12` sont **hors décompte PASS par construction** (M4) :
consignations déclarées.

Aucune tolérance déclarée ici ne pourra être desserrée en cours de lot
(précédents R-2/Q6 et R-8/C9) : un écart se **nomme et se borne**, ou le test
est remplacé par le critère analytique prescrit **au gel**, jamais par un
seuil élargi.

## 3. Grades possibles du lot

`REPRODUIT` (inatteignable ici, cf. §0) · **`REPRODUIT-SOUS-RÉSERVE` (E-2 —
plafond)** · `NON-REPRODUIT` · défaut `E-3` si un assert se révèle tautologique.

---

*§6.4 — figer des cibles ne scelle, ne réduit, ne compte, ne démontre rien.
`{ A4 ; A2★ ; N }` INCHANGÉ · A4 non réfuté · D1 non clos · N non fixé ·
O₂ non construit · nœud (i) INDÉTERMINÉ (pas A) · CCC non démontrée NI réfutée.*
