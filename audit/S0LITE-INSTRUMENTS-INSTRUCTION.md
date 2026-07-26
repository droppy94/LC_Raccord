---
id: S0LITE-INSTRUMENTS-INSTRUCTION
titre: "Tout attendu du §0-lite porte sa COMMANDE LITTÉRALE. Un nombre sans son instrument n'est pas opposable. Arbitrage opérateur S19, correctif nº4. Complète S0LITE-IMPRESSION-INSTRUCTION sans la remplacer."
codename: LC-RACCORD
type: "instruction de conduite de session — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
---

# Les attendus portent leur instrument

## §0. Le fait mesuré

**Cinq des quatorze écarts imputables au pilote sur S14–S19 sont d'une seule et même classe :
l'instrument de comptage.**

| session | écart | instrument fautif |
|---|---|---|
| S16 | 115 consignations rendues au lieu de 101 | motif trop large |
| S17 | 11 rendu au lieu de 13 sur 52 | `grep -c` compte des **lignes** |
| S18 | 4 scripts invisibles au comptage | motif `[PASS]` aveugle aux formes sans crochets |
| S18 | `rc` faux | `rc=$?` lu **après un pipe** |
| S19 | `62` juste sous deux instruments **différents** | voir §2 |

**Le correctif partiel de S18 a fonctionné, et c'est mesuré** : le prompt S19 écrivait
`audit/ 62 (instrument = ls audit/)`, et les **7 comptes ont été justes au premier jet** en S19,
sans reprise. La présente instruction achève ce qui a marché.

## §1. INSTRUCTION

> **Tout attendu numérique du §0-lite est écrit avec la commande littérale qui le produit.
> Un nombre présenté sans sa commande n'est PAS opposable, et le pilote doit le dire au lieu de
> le confirmer.**

Table de référence, **mesurée en S19 sur clone neuf**, à recopier telle quelle dans chaque
prompt d'ouverture :

| attendu | commande littérale |
|---|---|
| `34` | `ls instruments/*.py \| wc -l` |
| `76` | `ls instruments/archives-scelees/*.py \| wc -l` |
| `62` | `ls audit/ \| wc -l` — **61 fichiers + 1 répertoire** |
| `215` | `ls kb/*.md \| wc -l` |
| `4` | `ls hors-KB/B/ \| wc -l` |
| `4` | `ls -p \| grep -v /` (racine, fichiers seuls) |
| `8` | `ls audit/beta-paquet-gouvernance/LC-BETA-* \| wc -l` |
| `6 / 76 / 1` | `python3 instruments/inventaire_sceaux.py` — **réécrit sa date, restaurer par `git checkout`** |
| `051e2833` | `python3 instruments/run_sceau.py verif_paquet_propre` |
| `271` | `grep -cE '^[[:space:]]*\[?PASS\]?'` sur la sortie de chaque redémonstration, sommé sur 12 |
| `101` | `grep -cE 'CONSIGNATION'` idem |
| `%PDF` + sha8 | `python3 -c "hashlib.sha256(...)"` — **`xxd` ABSENT**, passer par `python3` ou `od` |

**Le compte sur marqueur se confronte TOUJOURS au bilan auto-déclaré du script.** Deux valeurs
concordantes sous deux instruments distincts valent une mesure ; une seule valeur n'en vaut pas.

## §2. Le piège mesuré en S19 : un nombre vrai sous deux instruments à deux dates

- **S18** : `ls audit/` rendait **55**, `find audit/ -type f` rendait **62**, `-maxdepth 1`
  rendait 54.
- **S19** : `ls audit/` rend **62**, `find audit/ -type f` rend **69**.

**`62` est donc aujourd'hui la valeur d'un instrument, et était hier la valeur d'un autre.** Un
pilote qui confirmerait « 62 » sans nommer son instrument aurait raison pour la mauvaise raison ;
un pilote qui mesurerait par `find` nommerait un faux écart. **La classe :** *un compte n'est
vrai que sous son instrument, et la coïncidence de deux valeurs sous deux instruments n'est pas
une confirmation.*

Autre occurrence, S19 : la note S18 écrit `kb/NOTE-REPRISE-V96.md` **« citée 2 fois »** au
manifeste. Mesuré : **2 lignes, 3 occurrences.** Vrai sous `grep -c`, faux sous `grep -o`.
Nommé, non bloquant, non résolu.

## §3. L'OBJECTION, portée contre la présente instruction

La pente naturelle de ce correctif est de **scripter entièrement le §0-lite** : un
`audit/S0LITE-ATTENDUS.json` (commande → valeur attendue) et un exécuteur unique. Cette pente
doit être nommée, parce qu'elle détruirait ce que `S0LITE-IMPRESSION-INSTRUCTION` §2 a établi et
que l'opérateur a explicitement valorisé :

> *Le §0-lite est un banc de calibration du pilote autant qu'un contrôle de reproductibilité. Il
> vérifie qu'une session neuve sait compter avant de la laisser classer quoi que ce soit.*

**Un pilote qui lance un script ne se calibre pas.** Et le fait porté reste vrai : en neuf
sessions, les redémonstrations n'ont **jamais** détecté de dérive du corpus — elles n'ont
détecté que le pilote. Automatiser la partie qui n'a jamais rien trouvé, en supprimant la partie
qui a tout trouvé, serait exactement le mauvais échange.

**Résolution proposée, non exécutée ici, à arbitrer séparément** : scinder. La **détection de
dérive** (comptes, sha, `rc`) peut être scriptée. La **calibration** reste manuelle, courte, et
**déclarée comme telle** : le pilote écrit ses instruments à la main sur un sous-ensemble **tiré
par l'opérateur** et non choisi par lui. On garde le banc ; on cesse de payer douze scripts pour
l'obtenir.

## §4. Gardes d'environnement, recopiées parce qu'elles se perdent

- **`rc` se capture AVANT tout pipe.** `commande | tail` puis `rc=$?` mesure `tail`.
- **`grep -c` compte des LIGNES.** Une ligne à trois occurrences en rend une. Employer
  `grep -o | wc -l` ou `re.findall`.
- **Les chaînes `&&` s'interrompent sur un `grep -c` qui rend 0** — terminer par `|| true` quand
  le zéro est le résultat attendu.
- **Le motif `^[[:space:]]*\[?PASS\]?` couvre les deux formes.** R-1, R-2, R-6 et R-12 impriment
  **sans crochets** ; la classe est de quatre, non d'un.
- **LES MOTIFS SE BORNENT.** Un `grep -rn` non borné sur une base à front-matter kilométrique
  coûte ~15 000 tokens pour une question de trois lignes — écart S18, et c'est ce même `grep`
  qui a produit la contamination de la voie (i).
- **`xxd` ABSENT** ; `pymupdf` ABSENT ; `extract_words` mensonger sur les mathématiques
  affichées — descendre au niveau `chars`.

## §5. Ce que cette instruction ne fait pas

Elle ne retire aucun script de l'exécution, ne modifie aucun attendu, ne touche aucune valeur
cible. Elle ne scelle, ne réduit, ne compte, ne démontre rien. **CCC n'est ni démontrée ni
réfutée.**
