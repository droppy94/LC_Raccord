---
id: LC-BETA-DEFAUTS-DAGE-PAQUET
titre: "Défauts d'âge des 8 pièces `LC-BETA-*` déposées en S16 — NOMMÉS par fichier séparé daté. Les pièces restent BYTE-INTACTES et gardent leur texte."
codename: LC-RACCORD
type: "amendement de nomination. Il ne corrige rien en place et n'autorise personne à le faire."
version: 1.0
langue: fr
date: 2026-07-25
session: S16
---

# Défauts d'âge du paquet β — nommés, non corrigés

## 0. Règle appliquée

**Un défaut du gel se nomme et s'amende par FICHIER SÉPARÉ DATÉ, jamais en place ;
la pièce amendée reste BYTE-INTACTE** (précédents S8/S9). Les 8 pièces déposées
sous `audit/beta-paquet-gouvernance/` le sont **avec leurs défauts**, sans une
seule modification d'octet. Leurs sha256 figurent à
`audit/LC-BETA-PAQUET-CONCORDANCE.md` §4 et sont vérifiables.

## 1. DÉFAUT nº1 — P-8 déclaré NON SOLDÉ. C'est FAUX.

**Porteurs** : `LC-BETA-BOOT.py` ligne 103 · `LC-BETA-00-PROMPT-PROJET.md` §6.

Ces deux textes, gelés au 2026-07-18, écrivent que le prérequis **P-8 n'est pas
soldé**. **P-8 est SOLDÉ ET DÉPOSÉ depuis `cad358a`** : générateur
`instruments/LC-WORK-GEN-PAQUET-v2_1.py`, sha256
`7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`, auto-test
**6/6 gardes mordantes**, rejoué CONFORME en S15 **et en S16**.

**Nature du défaut : SUR-RESTRICTIF.** Il interdit plus que nécessaire, donc il
**ne peut pas produire un faux acquis** — seulement un faux blocage. **NON BLOQUANT.**

**IL NE SE CORRIGE JAMAIS D'OFFICE.** Une correction en place détruirait la
byte-intégrité qui fait tout le prix du gel, et corrigerait un texte daté avec de
l'information qu'il ne pouvait pas porter.

**P-9 rappelé** : le dépôt de l'instrument n'atteste **que son existence**. Sa
valeur **se mesure À LA PROCHAINE GATE**. Écrire l'instrument ne solde pas la gate.

## 2. DÉFAUT nº2 — « le gel ne ment pas par âge » : VRAI des copies, FAUX de ces 8

L'assertion vaut pour les **35 `BETA-COPIE-*`**, qui ont une contrepartie `kb/` et
sont donc **confrontables** — et confrontées : **34/35 byte-identiques, 0 divergente**
(mesure S15, **RE-MESURÉE indépendamment en S16**).

Elle est **FAUSSE des 8 `LC-BETA-*`** : sans contrepartie `kb/`, elles n'ont
**jamais été confrontées à rien**. **C'est là que vit le défaut nº1.**

**Retournement consigné, et c'est le motif du dépôt de S16** : une pièce mount-seul
que rien ne confronte **peut mentir indéfiniment** ; sous contrôle de version, un
mensonge par âge **devient visible par `diff`**. Le dépôt de ces 8 pièces ne les
rend pas vraies — **il les rend falsifiables**.

## 3. DÉFAUT nº3 — le gel porte sur un répertoire vivant

`PKG_SHA_BETA` hache **le contenu courant d'un répertoire**. En S15 le pilote a
écrit une pièce dans ce répertoire : `PKG_SHA_BETA_8` est passé de `dc276129` à
`687ed70b`, `N_haches` de 42 à 43, **et `LC-BETA-BOOT.py` a rendu rc=0** — le
pare-feu, **NOMINAL**, n'a pas mordu.

**UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL, c'est un haché mouvant.**
**UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE.**

`audit/LC-BETA-PAQUET-CONCORDANCE.md` **ne dépend d'aucun répertoire** : elle porte
sur des octets nommés un par un. Elle ne guérit pas le défaut ; elle **ne le
reproduit pas**.

Statut de la proposition « paquet = ARCHIVE byte-gelée, atelier séparé » :
**NON ARBITRÉE.** Sans arbitrage, le régime actuel reste **avec son défaut déclaré**.

## 4. Ce que ce fichier ne fait pas

Il ne modifie aucune pièce, ne relève aucun blocage, ne rejoue pas
`LC-BETA-BOOT.py`, ne recalcule pas `PKG_SHA_BETA_8`, et n'autorise aucune
correction d'office. **Nommer un défaut n'est pas le réparer.**

---

*§6.4 — nommer un défaut ne scelle, ne réduit, ne compte, ne démontre rien.
β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. CCC n'est ni démontrée ni réfutée.*
