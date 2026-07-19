---
id: LC-WORK-TRACE-EXPORT-QCCC-V1
titre: Trace du prêt LC-EXPORT-QCCC-v1 — export figé v2.44 vers le programme d'instruction QCCC (flux unidirectionnel, §6.4 propagé)
version: 1.0
statut: work-trace — prêt EXÉCUTÉ 2026-07-05 ; pièce de traçabilité, HORS-CARTE IDX ; aucun gel, aucune cible, aucun verdict
maj: 2026-07-05 — v1.0 création (décision opérateur 2026-07-05 : instruction du cadre QCCC en PROJET SÉPARÉ, appuyé sur un prêt figé de LC-RACCORD)
tags: [export, pret, tracabilite, EXPORT-SHA, contrat-interface, flux-unidirectionnel, §6.4, non-surclassement]
---

# Trace du prêt LC-EXPORT-QCCC-v1

## 1. Objet
Le programme LC-RACCORD a prêté au programme d'instruction QCCC (« projet séparé »,
groupe emprunteur distinct) un paquet figé de contraintes, de tests et de méthodes,
afin que le cadre QCCC (développement spectral a0/a2/a4, N_F = 96, condition
f4 = pi²/2) soit instruit à l'orée des résultats LC-RACCORD, SANS saturer la présente
KB et SANS contamination croisée des pilotes.

## 2. Ce qui a été prêté (composition)
- Source : instantané v2.44 du paquet gelé, PKG-SHA
  `35f929f1f368fc638161ca86eedabc20deff5783d3051fc797d8e493df76adcc`.
- 109 fichiers + manifeste d'export = 33 `.md` + 76 `.py`, en 4 paquets :
  PKG-1 SOCLE-CONTRAINTES (16 dossiers : SOCLES-4, IRREDUCTIBILITE, dossier N≡Λ,
  dossier D1 complet dont D1-IMPOSSIBILITE-INFO, verrous d'amplitude ; + LES 76
  SCEAUX en noms canoniques + STACK-SPEC) ; PKG-2 PORTES-CRIBLES (C1, portrait
  Q1-Q8, crible ext-B, exemplaire F2, cadrage bascule N↔Λ) ; PKG-3 DISCIPLINE
  (01/02, prompt audit froid, modèle d'amendement R-7, GLO, recette PKG-SHA
  transposable) ; PKG-4 CONTRAT (contrat d'interface, 8 articles).
- Pièces PRODUITES pour l'export (hors-KB, 5) : STACK-SPEC, RECETTE-PKG-SHA,
  NOTE-VERIF-PAQUET, CATALOGUE, LC-EXPORT-CONTRAT-INTERFACE.

## 3. Intégrité consignée
- Contrôle croisé à l'export : 104/104 pièces KB byte-exactes vs manifeste v2.44
  (103 via table §2/§3 ; le chaînon `LC-D-D1-IMPOSSIBILITE-INFO`, rangée absente de
  la table — lag documentaire du lot v2.44, mount autoritaire — vérifié via le sha
  du journal maj `afeb956b…a0ef`). 0 mismatch.
- EXPORT-SHA (recette PKG-SHA, manifeste d'export exclu) =
  `0c787de5d5a945ec5081fa45c6d4de3d3d49e71652a815b35b8958dcf78e97c9`.
- Archive livrée `LC-EXPORT-QCCC-v1.zip`, sha256 =
  `a92d3eace1188996ff127f03bb85894673d76f880a6a7047c10901d632be8889`
  (archive détenue opérateur, hors-KB).

## 4. Conditions du prêt (résumé opposable ; le texte intégral fait foi)
Contrat `LC-EXPORT-CONTRAT-INTERFACE` v1.0, 8 articles : instantané figé v2.44 et
citation avec grade verbatim (art. 1) ; non-surclassement §6.4 propagé à tout
document dérivé (art. 2) ; conditionnalité R-53, signalement sans réouverture
unilatérale (art. 3) ; rejeu obligatoire des 76 sceaux, EXIT 0, échec signalé sans
modification (art. 4) ; FLUX STRICTEMENT UNIDIRECTIONNEL, toute remontée passe par
le canal normal (veille → instruction dédiée → gel R-7 → porte C1 → algèbre →
sceau → audit froid), disqualification croisée des pilotes, aucune écriture croisée
de KB (art. 5) ; obligations d'instruction : anti-fit sur prédictions NEUVES
seulement, C1 en aveugle sur la chaîne a0→ΩΛ, déclaration de la résiduelle
d'entrée (R-a/R-b/R-c) pour toute clause de sélection de Ω type D(n+1)=r4·D(n),
comptage honnête incluant N_F=96 (art. 6) ; traçabilité et retransmission
intégrale (art. 7) ; pérennité de l'instantané, errata sans retrait (art. 8).

## 5. Effets sur LC-RACCORD
AUCUN. Le prêt n'emporte ni endorsement ni co-signature ; aucun résultat QCCC
n'entre en KB par l'effet du prêt ; les veilles et la porte C1 restent l'unique
canal de remontée. Aucun gel consommé, aucune cible figée, aucun front touché.

---
§6.4 — prêter des contraintes, des tests et des méthodes ne scelle rien, ne compte
rien, ne réduit rien ; `{A4 ; A2★ ; N}` INCHANGÉ ; D1 non clos ; N non fixé (≡Λ) ;
A4 non réduit ; A2★ non tranché ; O₂ non construit ; β reste T-b ; CCC non
démontrée NI réfutée.
