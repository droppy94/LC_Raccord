---
id: S0LITE-IMPRESSION-INSTRUCTION
titre: "Régime d'impression du §0-lite — les 12 redémonstrations restent TOUTES exécutées intégralement ; seule leur RESTITUTION est compressée. Arbitrage opérateur S18, voie (i)."
codename: LC-RACCORD
type: "instruction de conduite de session. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
session: S18
---

# Régime d'impression du §0-lite

## 1. Le fait mesuré qui motive l'instruction

Sortie **intégrale** des 12 scripts, mesurée en S18 : **543 lignes / 68 966 caractères**,
soit ≈ **17 000 tokens**. La même exécution, restituée en rc + bilan + totaux : ≈ **1 500**.
**Facteur 11.** Durée machine inchangée dans les deux cas (~21 s pour les trois plus gros).

**Le coût n'est donc PAS une propriété du §0-lite : c'est un choix d'instrument du pilote.**

## 2. Ce que le §0-lite détecte réellement — et ce n'est pas ce que son libellé annonce

Bilan **271/271 + 101, INCHANGÉ depuis S9 — neuf sessions.** Les redémonstrations n'ont
**jamais** détecté une dérive du corpus. Ce qu'elles ont détecté, à chaque fois, c'est le
**pilote** :

| session | détecté | nature |
|---|---|---|
| S16 | 115 consignations au lieu de 101 | motif de comptage faux |
| S17 | `grep -c` compte des lignes | instrument faux |
| S18 | 4 scripts impriment **sans crochets** | instrument faux |
| S18 | `rc` lu **après un pipe** | instrument faux |

**Le §0-lite est un banc de calibration du pilote autant qu'un contrôle de reproductibilité.**
Il vérifie qu'une session neuve sait compter **avant** de la laisser classer quoi que ce soit.
C'est cette fonction que l'instruction préserve intégralement.

## 3. INSTRUCTION — applicable au prompt d'ouverture S19 et suivants

**Les 12 scripts sont TOUS exécutés, intégralement. Rien n'est retiré de l'exécution.**

Sont imprimés, et rien d'autre :

1. par script : **`rc`** et le **bilan auto-déclaré** tel que le script l'écrit ;
2. par script : le **compte sur marqueur en tête de ligne**, avec **l'instrument déclaré** ;
3. les **deux totaux** et leur décomposition ;
4. les 5 rejeux de confirmation : **rc + valeur attendue**, une ligne chacun.

**N'est PAS imprimé** : le corps des sorties.

**Clause de dépliement.** Dès qu'un écart apparaît — marqueur ≠ bilan auto-déclaré, `rc ≠ 0`,
total ≠ 271/101 — la sortie **intégrale du seul script concerné** est dépliée et rendue.
La compression porte sur le silence, jamais sur l'écart.

## 4. Gardes

- **`rc` se capture AVANT tout pipe.** `commande | tail` puis `rc=$?` mesure `tail`.
- **L'instrument de comptage se déclare**, pas seulement son résultat. Le motif
  `^[[:space:]]*\[?PASS\]?` couvre les deux formes : R-1, R-2, R-6 et R-12 impriment
  **sans crochets** — la leçon §0.5 n'en nommait qu'un, la classe est de **quatre**.
- **Compresser n'est pas rejouer moins.** Un §0-lite non exécuté se déclare
  « non rejoué », daté ; il ne se déduit jamais d'un rendu court.

## 5. Ce que cette instruction ne fait pas

Compresser un rendu ne scelle, ne réduit, ne compte, ne démontre rien. Aucun attendu n'est
modifié, aucun script retiré, aucune valeur cible touchée.
