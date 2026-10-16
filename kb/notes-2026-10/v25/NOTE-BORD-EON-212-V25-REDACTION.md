---
id: NOTE-BORD-EON-212-V25-REDACTION
numero: 212
serie: I
branche: Chantier D (article v2.5)
reservation: 2026-10-16T15:48:49Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 212)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-211-ARMEMENT-V25.md sha256 d61dccd059a10a4d (sceau NOTE-211-SCEAU.txt, 2026-10-16T15:49:14Z)"
pieces: "dirac-mass-scri-v2.5.tex et .pdf (11 pages) ; companion-formal-regularity.tex et .pdf (4 pages) ; scripts v2.4 relances (sorties identiques octet pour octet) ; empreintes au sceau NOTE-212-213-SCEAU.txt"
---

# Redaction de la v2.5

## 1. Correspondance avec le gel
| Point du gel | Ou dans la v2.5 | Etat |
|---|---|---|
| R1.1 notions de regularite, classe de jauges, regularite formelle | Definition 1 (a), (b), (c) | fait |
| R1.2 hypotheses FLRW | §2 (a C^1, a -> infini, integrale de dt/a finie, Omega = 1/a) ; Prop. 1 et 4 avec theta = integrale de m dt | fait |
| R1.3 hypothese de charge (Prop. 2) | §4.2, premier paragraphe | fait |
| R1.4 coefficient de la Prop. 3 annulable, sans signe fixe | Prop. 3 | fait |
| R1.5 preuve de la Prop. 4(a) pour k non nul | preuve de la Prop. 4 (monotonie de theta) | fait |
| R1.6 base des operateurs du Lemme 2 | Annexe A | fait |
| R1.7 contradiction du §6 v2.4 (Higgs) | §5, fin : renvoi a la Remarque 2(3) | fait |
| R1.8 versions et parametres des scripts | section Verification (Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, DOP853, tolerances, parametres ; sorties reproduites octet pour octet le 16 octobre) | fait |
| R2 argument quantique | §4.3 « Quantum version » | fait |
| R3 Remarque raccourcie, note compagnon | Remarque 2 (quatre points) ; note compagnon de 4 pages (ED, HX, FW3, RJ, scripts et statut d'audit) | fait |
| R4 bibliographie | 25 references, toutes dans la liste du gel ; titre de Meissner-Penrose corrige ; Friedrich 2015 publie ; paragraphe « Related work » ; nouveaute reduite (§1 et §6) | fait |
| RJ | Remarque 1 (Fuchs), paragraphe « Dependence on the weight », Remarque 2(4), Prop. 5(b) reformulee et paragraphe qui suit | fait |

## 2. Ecarts et choix declares
- Le resume ne dit plus « nous prouvons trois enonces » ; il nomme ce qui est connu (forme asymptotique) et ce qui depend du poids.
- Prop. 2, derniere phrase : preuve reecrite (un potentiel regulier donne lambda' borne, donc integrable, et (a) s'applique), plus courte que celle de la v2.4.
- Mason-Nicolas 2004 et 2012 cites par leurs titres seulement (niveau [titre] de NOTE-202 v2), sans attribution de contenu ; l'enonce « champs sans masse » est porte par Pham 2021 [resume].
- Kanno-Sasaki-Tanaka, Szabados, Loran, Roy (S20) non cites : non relus (FW-1).
- Ordres de grandeur : ajout du poids antiparticule de Bunch-Davies pour l'electron (inferieur a e^{-10^39}), calcul immediat.
- La note compagnon reprend les resultats entes (NOTE-184, 189, 194, 210) sans nouveau calcul ; elle est en anglais, comme l'article.

## 3. Verdict de redaction (provisoire, avant audit)
V25-V1 ou V25-V2 selon l'audit ; aucun ecart de fond declare.

## 4. Non-surclassement
Redaction par IA, non relue par un humain ; audit froid requis (FW-4 du gel). Noyau {A4 ; A2★ ; N} inchange.
