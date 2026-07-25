---
id: LC-BETA-05-RETOUR-KB
codename: LC-RACCORD-BETA
titre: "Pare-feu bidirectionnel et protocole de RETOUR du chantier β vers la KB principale. Rien de ce qui est produit ici n'a de valeur en KB avant re-vérification contre le mount principal, par l'opérateur."
version: 0.1
langue: fr
date: 2026-07-18
statut: "PROTOCOLE. Ne scelle rien. Ne dépose rien. Aucun geste ici n'est un geste en KB."
---

# Retour vers la KB — et pare-feu

## §1 — Pare-feu. Deux sens. La contamination est déjà arrivée deux fois.

**Sens 1 — β ⇏ KB.** Aucun fichier `LC-BETA-*` ni `BETA-COPIE-*` ne réside **JAMAIS** sur
`/mnt/project`. Le §0-lite de la KB principale doit **désormais** attendre :

    LC-ART   0
    BETA-*   0        <== NOUVEAU, à ajouter au contrôle de pare-feu

**Sens 2 — KB ⇏ β.** Tout fichier de ce projet qui ne commence **ni** par `LC-BETA-` **ni**
par `BETA-COPIE-` est une **contamination**. La nommer, ne pas la ranger.

*La piste article a contaminé le mount principal **au moins deux fois**. Le motif n'était
jamais la malveillance : c'était la commodité.*

## §2 — Ce que le chantier peut rendre. Au plus.

| livrable | grade | destination |
|---|---|---|
| `LC-BETA-04` rempli (R-41) | **fait vérifiable** | source d'un futur `LC-WORK-R41-*` en KB |
| positionnement `S-B1` | **classement, stérile** | source d'un futur `LC-WORK-POSITIONNEMENT-*` |
| amendement R-7 (si `S-B2` armé) | **prospectif** | à geler ET déposer **en KB**, avant lecture |
| scoping gelé | **cibles** | à déposer **en KB**, avant lecture |
| **patch additif** de `LC-D-G3-TRANSPORT` (→ v0.5) | **délimitation** | KB, par l'opérateur |
| brouillon de sceau `.py` | **BROUILLON** | **rejeu obligatoire sur le mount principal** |

**Le chantier ne rend PAS** : un sceau valide, un PKG-SHA de la KB, une consignation au
manifeste, un verdict opposable sans audit froid.

## §3 — Le retour, dans l'ordre. L'opérateur exécute tout.

1. **Re-vérifier le gel de dossier contre le mount.** Les 35 copies datent du **2026-07-18 /
   V94 / v2.121**. **Si la KB a bougé depuis, le dossier a menti** — pas par faute, par
   **âge**. Comparer canon↔sha256 avec le manifeste courant **AVANT** d'exploiter quoi que ce
   soit. *(`LC-BETA-PAQUET-GEL.md` liste exactement ce qu'il faut comparer.)*
2. **Rejouer** tout `.py` produit **sur le mount principal**, stack principal, en
   **avant-plan** *(défaut #2 : `setsid` meurt en silence)*.
3. **Audit froid incognito** si le verdict bouge. Pilote **disqualifié nommément**, camp caché,
   exclusions listées. *En cas de discordance pilote/incognito : **l'incognito l'emporte**.*
4. **Patch ADDITIF uniquement.** Zéro ligne de corps perdue, vérifié par `difflib`.
   Suppressions confinées à `{version, maj, statut}`. Ancres `str_replace` vérifiées
   `count == 1`.
5. **Dépôt fichier par fichier, GO explicite pour chacun.** Puis brackets, puis consignation
   au manifeste, puis swap du journal.
6. **R-36** : les gels se consignent **hors-fichier**, à la table nom↔sha de l'opérateur.
7. **R-53** : si le verdict bouge, **le tracker bouge** — et **`LC-D-IRREDUCTIBILITE-MOYENS`
   doit être ré-examiné**, pas présumé intact. Une clôture n'est valide que **tant que** ses
   critères tiennent.

## §4 — Le cas le plus probable, et il est complet

**`S-B1` classe les trois sources en `C-iii`/`C-iv` ⟹ `S-B2` n'est pas armé.**

Alors le chantier rend : la **fiche R-41**, le **positionnement**, et **une ligne** au
dossier β — *les trois sources de la piste article ne comblent pas la cellule
`R1″∧R2″∧R4″`*. **C'est une délimitation. C'est complet. Ce n'est pas un échec.**

Et le chantier **se referme**, au lieu de chercher une raison de continuer.

*Le coût du chantier est alors : trois identités vérifiées et une hypothèse du pilote
réfutée. **Réfuter une hypothèse du pilote est le meilleur usage connu de ce programme.***

## §5 — Condition de dissolution

Si, après `S-B1`, aucune source n'est en `C-i`/`C-ii` **et** aucun levier neuf n'est nommé,
**le chantier n'a plus d'objet** ⟹ **le proposer à la dissolution**, plutôt que le laisser
vivre. Un chantier ouvert sans objet **produit du travail, pas du résultat** — et il finit
par fabriquer sa propre pertinence.

**La décision de dissoudre appartient à l'opérateur, jamais au pilote** *(même structure que
`D-d`)*.

---

**§6.4 — sentinelle.** Rendre un livrable ne le dépose pas (`R-55`). Déposer ne répare pas
(`P-9`). `{A4 ; A2★ ; N}` **INCHANGÉ** ; **β `T-b`, SEUL facteur d'O₂ ouvert** ; `R-53 0/4` ;
**CCC n'est ni démontrée ni réfutée.**
