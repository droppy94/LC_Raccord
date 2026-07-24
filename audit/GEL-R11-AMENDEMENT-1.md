# AMENDEMENT 1 au GEL-R11 — daté, AVANT la première ligne d'instrument

Gel amendé : `GEL-R11.md`, sha256 298e2094ffdffc853118564d328b4faead57dcb5eefbf554c5f63e9b3cccd21d
Le fichier gelé reste BYTE-INTACT. Cet amendement est un fichier séparé.
Émis le 2026-07-24, avant l'existence de `redemo_R11_falsifiabilite.py`.

## Défaut constaté — imputable au pilote, pas au dépôt

Cible F4-1, telle que gelée :

> « pour toute S_grav ≡ f(w) STRICTEMENT MONOTONE **décroissante** sur
>   w ∈ [0,∞) […] : argmin global de f sur [0,∞) est atteint en w=0 »

L'énoncé est FAUX comme écrit. Si f est strictement décroissante sur
[0,∞), son infimum est atteint en w → ∞, jamais en w=0. La cible, prise
littéralement, serait réfutée par n'importe quel f décroissant — et la
réfuter n'établirait RIEN sur la circularité de la voie entropie-de-Weyl,
qui est le fond de F4.

Le sens visé est l'inverse et est contraint par la physique de l'argument :
l'entropie gravitationnelle CROÎT avec l'invariant de Weyl (Penrose), donc
« S_grav minimale ⟺ w = 0 ⟺ A4 » exige f **croissante**.

## Amendement

F4-1 est lu, pour l'exécution :

> pour toute S_grav ≡ f(w) STRICTEMENT MONOTONE **CROISSANTE** sur
> w ∈ [0,∞), w invariant de Weyl ≥ 0 : l'argmin global de f sur [0,∞) est
> atteint en w = 0. Vérifié sur ≥ 5 functionals f distincts, ab initio.

F4-2 et F4-3 sont INCHANGÉS. F4-3 (firewall) devient de ce fait le test de
non-vacuité de F4-1 : sur un f NON monotone, l'argmin doit quitter w=0.

## Ce que cet amendement N'EST PAS

- Ce n'est PAS un desserrage de tolérance : aucun seuil, aucune tolérance
  numérique n'est touché.
- Ce n'est PAS un élargissement de cible : le nombre de cibles [D] de l'axe
  F4 reste 3, le nombre de consignations reste 1.
- Ce n'est PAS rétroactif sur un résultat : aucun résultat n'existe encore.

## Antériorité

L'antériorité reste auditable : `GEL-R11.md` (298e2094) et le présent
amendement portent tous deux un sha, et le répertoire R11/ ne contient
aucun instrument à l'instant où ce fichier est écrit. La correction est
donc datée AVANT dérivation, et non découverte après un échec.

## Consignation obligatoire au rapport

Ce défaut sera porté au rapport R-11 comme **écart de gel NOMMÉ, imputable
au pilote**, au même titre qu'un écart d'instrument. Un gel qui contient
une erreur d'énoncé est un gel défectueux, même corrigé à temps.
