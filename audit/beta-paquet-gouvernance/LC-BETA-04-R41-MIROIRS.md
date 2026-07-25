---
id: LC-BETA-04-R41-MIROIRS
codename: LC-RACCORD-BETA
titre: "Fiche R-41 — vérification d'identité de S8/S9/S10 sur ≥3 miroirs indépendants, AVANT toute consommation profonde. FICHE VIERGE : aucune identité n'est pré-remplie, parce qu'aucune n'est attestée sur le mount principal."
version: 0.1
langue: fr
date: 2026-07-18
statut: "VIERGE. Ne certifie rien. À remplir par exécution, jamais par mémoire."
---

# R-41 — S8 / S9 / S10

## §0 — Pourquoi cette fiche est vierge

**Les identités de S8/S9/S10 ne sont attestées NULLE PART sur `/mnt/project`** (grep
exhaustif, 2026-07-18). Elles vivent dans la **piste article** et dans la **mémoire du
pilote**. R-54 : cet accord-là compte pour **UN** témoignage, pas deux.

Les libellés que le pilote **croit** se rappeler — *Bros–Moschella* ; *Nakayama* ;
*Ghaffari–Luciano–Mantica* — sont donc des **pistes de départ pour la recherche**, **PAS**
des identités. Ils sont écrits **ici et pas ailleurs**, précisément pour qu'aucun fichier de
substance ne les porte comme acquis.

**Un article fantôme a déjà été intercepté par R-41.** La règle a mordu une fois ; elle
n'est pas décorative.

## §1 — Protocole, par source, sans exception

1. **Réclamer le PDF à l'opérateur** — le mount principal ne les porte pas.
2. **Trois miroirs INDÉPENDANTS.** Indépendants = **éditeurs distincts**, pas trois pages qui
   se recopient. Un agrégateur qui cite un préprint **n'est pas** un miroir de plus.
   *Ordre de préférence : DOI éditeur > arXiv (avec version et date) > INSPIRE/ADS > page
   institutionnelle. ResearchGate seul **ne suffit pas**.*
3. **Écrire le grade éditorial**, sans le déduire : `revu par les pairs` / `préprint` /
   `inconnu`. **Un préprint reste consommable — son grade doit être ÉCRIT, pas supposé.**
4. **Vérifier l'objet, pas le titre.** Un titre qui contient « de Sitter » ne dit **rien** sur
   la cellule `R1″∧R2″∧R4″`.
5. **Intégrité du PDF** — sha256 des octets consommés. *(Piège connu : certains PDF du mount
   sont des ZIP de JPEG+OCR — magie `PK\x03\x04` ; le sha du mount peut différer du sha
   déposé par re-zippage — bénin, mais **l'identité de contenu se confirme séparément**.)*

## §2 — Grille — à remplir par exécution

### S8
| champ | valeur |
|---|---|
| piste pilote (**non attestée**) | *Bros–Moschella* |
| titre exact | |
| auteurs | |
| identifiant (DOI / arXiv + version) | |
| date, journal | |
| grade éditorial | |
| miroir 1 (URL, date de consultation) | |
| miroir 2 | |
| miroir 3 | |
| sha256 du PDF consommé | |
| **identité CONFIRMÉE / INFIRMÉE / FANTÔME** | |

### S9
| champ | valeur |
|---|---|
| piste pilote (**non attestée**) | *Nakayama* |
| titre exact | |
| auteurs | |
| identifiant (DOI / arXiv + version) | |
| date, journal | |
| grade éditorial | |
| miroir 1 (URL, date de consultation) | |
| miroir 2 | |
| miroir 3 | |
| sha256 du PDF consommé | |
| **identité CONFIRMÉE / INFIRMÉE / FANTÔME** | |

### S10
| champ | valeur |
|---|---|
| piste pilote (**non attestée**) | *Ghaffari–Luciano–Mantica* |
| titre exact | |
| auteurs | |
| identifiant (DOI / arXiv + version) | |
| date, journal | |
| grade éditorial | |
| miroir 1 (URL, date de consultation) | |
| miroir 2 | |
| miroir 3 | |
| sha256 du PDF consommé | |
| **identité CONFIRMÉE / INFIRMÉE / FANTÔME** | |

## §3 — Après R-41, et pas avant

**R-41 rendu ⟹ `S-B1` (positionnement) autorisé. RIEN D'AUTRE.**
Confirmer une identité **n'autorise pas** la consommation profonde : elle autorise le
**classement**. La consommation exige en plus `P-8` soldé, l'amendement R-7 et le scoping
gelé et déposé (`LC-BETA-03` §3).

**Note d'accès, expérience acquise :** ResearchGate en fetch direct rend **HTTP 429** de façon
répétée ; contournement connu = passer par une page où la cible apparaît en **entrée de
citation**. Le plein texte d'une source RG-seule exige les **identifiants de l'opérateur**.
`arxiv.org` est **hors allowlist** du conteneur ⟹ **abstracts seulement** ⟹ **les PDF
viennent de l'opérateur.**

---

**§6.4.** Vérifier une identité **n'atteste que l'identité**. Ce n'est ni une lecture, ni un
verdict, ni une pertinence. `{A4 ; A2★ ; N}` **INCHANGÉ** ; **CCC non démontrée NI réfutée.**
