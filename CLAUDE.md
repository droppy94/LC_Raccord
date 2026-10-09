# CLAUDE.md — conventions de travail

Ce dépôt consigne un programme de recherche en physique théorique. Lis `cadre/CADRE-HAUTEUR.md` avant toute action de fond : c'est le document de référence, il porte le constat fondateur et les douze lots.

**Ce dépôt ne contient que du validé.** Le travail vivant reste au mount. Rien n'entre ici sans passer les contrôles ci-dessous.

---

## 1 · Interdits — sans exception

- **Ne jamais déclarer une réduction du noyau `{ A4 ; A2★ ; N }`.** Il est inchangé. Si un calcul semble le réduire, c'est presque toujours un sur-classement : signale-le, ne l'écris pas.
- ~~**Ne jamais conclure sur la CCC.** Elle n'est ni démontrée ni réfutée, et ce programme ne vise pas à trancher.~~ *Remplacé par le §1 bis (décision opérateur du 2026-10-09).*
- **Ne jamais surclasser un statut.** Sceller une algèbre n'atteste QUE cette algèbre. Sceller une prédiction numérique n'atteste QUE ce nombre, jamais l'algèbre qui l'a produite.
- **Ne jamais modifier un fichier sous `seals/`.** Le répertoire est en ajout seul, y compris pour corriger une erreur : on ajoute un successeur, on gèle le fautif en l'état.
- **Ne jamais ajouter un générateur à A_mix** pour faire tomber un résultat dans l'ensemble-cible. C'est le pattern P5. Si un résultat n'y tombe qu'après élargissement, c'est un résultat négatif.
- **Ne jamais réécrire l'historique** : pas de `rebase`, pas de `--amend`, pas de `push --force` sur une branche partagée. Les corrections passent par `git notes` ou par un successeur daté.

---

## 1 bis · Précédence des règles (décision opérateur du 2026-10-09)

Reprend le §5.4 bis de `01-REPRISE-AUTOPORTANTE-2026-10-09-ETAT-CCC.md`.

- En cas de conflit, **les règles postérieures au 23 septembre 2026 prévalent** sur ce fichier : EX-7, EX-8, EX-9 (`ACTE-ADOPTION-EX7-EX8-EX9-2026-09-23.md`), RG v2 (`ACTE-ADOPTION-RG-ARRET-v2-2026-09-23.md`) et la lecture stricte de RG-4 (`ACTE-DECISION-RG4-LECTURE-STRICTE-2026-09-23.md`).
- L'interdit « ne jamais conclure sur la CCC » est **remplacé** par la distinction obligatoire :
  - **CCC (forme actuelle)** : réfutée à titre provisoire (RG-4 déclenchée le 2026-09-23 ; passe au grade établi après une lecture extérieure de S26-02 §2.3 sans objection emportante) ;
  - **CCC + M** (mécanisme M annulant la masse des fermions massifs près de 𝓘⁺) : hypothèse ouverte, spécifiée (S27-02).
- Formule imposée : « la CCC exige une physique absente du Modèle standard ; sous la règle adoptée, cette exigence non satisfaite la réfute dans sa forme actuelle ».
- Inchangés : le noyau `{ A4 ; A2★ ; N }`, le non-surclassement, R-53 (toute clôture reste conditionnelle : RG-4 rouvre si la lecture extérieure objecte ou si M est réalisé).

---

## 2 · Calibration — extrait vs dérivé

Contrainte propre au travail avec un modèle, actée après deux rétractations en trois tours dans la session `2 bords` : *ce qui est extrait directement d'une source est solide ; ce qui est déduit en enchaînant deux ou trois pas passe régulièrement sous le contrôle du modèle.*

Toute affirmation portée au dépôt est donc marquée :

- `[extrait]` — lu directement dans une source identifiée, avec la référence. Vérifiable vite.
- `[dérivé]` — obtenu en enchaînant des pas. **Piste à recalculer, jamais scellable en l'état.**
- `[calculé]` — produit par un script du dépôt qui repasse en EXIT 0.

Un `[dérivé]` ne devient `[calculé]` que par recomputation indépendante. Il ne devient jamais `[extrait]`.

---

## 3 · Front-matter obligatoire

Tout `.md` de substance (hors `README`, `CLAUDE.md`, gabarits) porte :

```yaml
---
id: L4-P1.4                          # unique, stable, jamais réutilisé
titre: "Formule unifiée du spectre de la lemniscate"
statut: "[P-neg]"                    # [P] [P-as] [P-neg] [R] [H] | établi | délimitation | décision-ouverte
programme: QCCC-RP                   # QCCC-RP | LC-RACCORD | CADRE
lot: 1                               # numéro de lot du cadre, si applicable
date: 2026-07-26
calibration: "[calculé]"             # [extrait] | [dérivé] | [calculé]
hauteur: {k: 4, H: 3, delta: 0.25}   # OBLIGATOIRE si le fichier contient une forme close
verif: tools/verif/verif_L4P1.py     # OBLIGATOIRE si statut = [P]
depend: [ncg, act, sch]              # ids amont, doivent exister dans le dépôt
sources: ["arXiv:0907.5542v4"]       # doivent figurer au registre avec ≥3 miroirs
rouvre_si:                           # OBLIGATOIRE si statut clos ou [P-neg]
  - "générateurs dérivés (Lot 5)"
  - "5 ∈ A_mix (Lot 2)"
issue_attendue: "délimitation"       # déclarée AVANT le travail, jamais éditée après
---
```

`issue_attendue` est écrite avant d'ouvrir le front et n'est plus touchée. Si le résultat diffère, c'est le corps du document qui le dit — pas le champ.

---

## 4 · Les six règles appliquées ici

| Règle | En pratique dans ce dépôt |
|---|---|
| **R-7** anti-fit | L'espace des verdicts est commité et horodaté **avant** le commit du calcul. Toute modification est un amendement daté, jamais une réécriture. |
| **R-H** hauteur déclarée | Aucune forme close sans `hauteur: {k, H, delta}` gelée avant la recherche. Voir `tools/hauteur.py`. |
| **§6.4** non-surclassement | Chaque livrable répète le garde-fou en pied de page. Un statut ne monte jamais sans nouveau matériel. |
| **R-41** ≥ 3 miroirs | Aucune source consommée sans fiche au registre `sources/registre.yaml` portant ≥ 3 miroirs vérifiés. |
| **R-53** clôtures conditionnelles | Aucune fermeture définitive : `rouvre_si` est obligatoire. |
| **R-55** pas d'actif fantôme | Un travail non commité n'existe pas. Il se consigne « à réécrire », jamais « livré ». |

La CI (`.github/workflows/regles.yml`) fait échouer le build sur chacune de ces règles. **Ne contourne jamais un échec de CI en assouplissant la règle** : soit le fichier se corrige, soit le résultat n'est pas prêt.

---

## 5 · Arborescence

```
cadre/          le document de référence et ses versions
seals/          AJOUT SEUL — états scellés, jamais modifiés
decisions/      verdicts au format ADR, numérotés, immuables
sources/        registre exhaustif des sources externes (fiches, pas de PDF)
lots/           travail par lot du programme (lots/lot-01-hauteur/…)
tools/          scripts réutilisables
tools/verif/    scripts de vérification, un par résultat [P], EXIT 0 requis
schema/         schémas de validation du front-matter
```

**Le mount reste l'atelier.** Les PDF arXiv, les sorties intermédiaires et les fronts en cours y vivent. Ne rapatrie ici que ce qui est validé — et jamais les PDF eux-mêmes : le registre porte identifiant, version, hash et miroirs, ce qui suffit à la reproductibilité et évite la redistribution d'œuvres sous licence non exclusive.

---

## 6 · Commits et tags

- Message : `<type>(<lot|programme>): <objet>` — types `seal`, `adr`, `lot`, `source`, `tool`, `cadre`, `fix`.
- Un commit = un fait. Pas de commit fourre-tout.
- **Sceau** = tag annoté et signé, jamais déplacé : `git tag -s seal/W2/v1 -m "verdict W2 — résidu générique"`.
- **Horodatage opposable** sur tout gel d'espace de verdicts : `ots stamp` sur le fichier avant le commit du calcul. C'est ce qui rend R-7 vérifiable par un tiers au lieu d'être auto-attesté.
- **Correction** : `git notes add` sur le commit fautif. Jamais `--amend`.

---

## 7 · Quand tu ne sais pas

Dis-le et arrête-toi. Ce programme a une valeur exactement proportionnelle à son refus de conclure. Une délimitation propre vaut mieux qu'une réduction espérée, et l'issue honnête attendue de la plupart des lots est *une délimitation de plus* — c'est écrit d'avance dans le cadre, précisément pour que personne n'ait à se forcer à trouver mieux.

---

*Garde-fou : `{ A4 ; A2★ ; N }` inchangé · CCC (forme actuelle) réfutée à titre provisoire (RG-4, 2026-09-23) ; CCC + M hypothèse ouverte · V100 borne toute force probante QCCC-RP tant que le Lot 5 n'a pas rendu.*
