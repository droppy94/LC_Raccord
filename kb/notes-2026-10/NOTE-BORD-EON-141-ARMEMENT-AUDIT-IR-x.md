---
id: NOTE-BORD-EON-141-ARMEMENT-AUDIT-IR-x
numero: 141
serie: I
branche: Q-M3 suite (IR-x, audit)
reservation: 2026-10-12T13:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 141)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (consignes aveugles, criteres, espace des verdicts et prediction figes AVANT le lancement des auditeurs)
decision: operateur (Thierry), 2026-10-12 15:22 heure de Paris
objet: [NOTE-BORD-EON-140-IR-x-EXECUTION]
consignes:
  - "PROMPT-AVEUGLE-XA1-DERIVATION.md, sha256 e838c6768ddc2ce5bf9d6e127f560c0499f7ca99a13e23b1fea40ba099bfe617"
  - "PROMPT-AVEUGLE-XA2-SCRIPT.md, sha256 9332c420cd020ae8173790cc0fac7f884e1c0b5a368a24484dd217ed33894d6a"
---

# NOTE-141 : armement de l'audit froid aveugle court de NOTE-140

## 1. Dispositif (fige)
Deux auditeurs isoles, en parallele, sans acces aux notes ni au registre :
- **XA-1** : derivation aveugle de la question d'EDP seule (aucune mention de G-V3, de la CCC ni du pole) : un ln s le long de s = 0 est-il possible pour une solution de □² = 0 ; calcul formel et argument general avec enonce et hypotheses du theoreme ; solutions de cone, sommet sur et hors du bord ; classes echappant a la conclusion.
- **XA-2** : audit du script irx_cone.py (x-1 a x-4), reproduction independante de x-2 et x-3, contre-exemples (sommet hors du bord, correcteurs non entiers ou ln² s, superpositions).

## 2. Criteres (figes)
- **C-1 (x-3)** : XA-1 (a) et XA-2 retrouvent c_n = 0 pour tous les n testes.
- **C-2 (argument general)** : XA-1 (b) donne un theoreme applicable a la classe des solutions distributionnelles temperees en 1/s, qui exclut α ln s sur un ouvert de s = 0.
- **C-3 (x-2)** : XA-2 retrouve l'absence de pole hors du sommet et une divergence sur le cone.
- **C-4 (contre-exemples)** : aucun contre-exemple produisant un ln s (ou un pole dans R) sur un ouvert de s = 0 dans la classe distributionnelle temperee ; les ensembles exceptionnels sont de mesure nulle (points, spheres).

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **XA-V1** | C-1 a C-4 satisfaits sans correction : NOTE-140 confirmee. |
| **XA-V2** | C-1, C-3, C-4 satisfaits ; l'argument general de NOTE-140 (« propagation des singularites ») doit etre reformule ou complete (theoreme different, hypothese de classe a nommer), ou les ensembles exceptionnels doivent etre elargis (spheres pour sommets hors du bord) : precision en v2, conclusion inchangee. |
| **XA-V3** | Un contre-exemple dans la classe distributionnelle temperee produit un ln s ou un pole sur un ouvert de s = 0 : X-V1 tombe. |
| **XA-V0** | Audit inexploitable (a nommer), relance. |

## 4. Prediction declaree (anti-fit)
**XA-V2.** La conclusion de NOTE-140 sera confirmee, mais l'argument general sera reformule : le resultat pertinent est plutot la regularite d'une solution par rapport a la variable normale a une hypersurface non caracteristique (une solution distributionnelle temperee est C^∞ en s a valeurs distributions, jusqu'au bord), que la propagation du front d'onde, qui est un enonce interieur. Les sommets hors du bord ajouteront des spheres de mesure nulle a l'ensemble exceptionnel. Les classes non temperees (hyperfonctions, croissance exponentielle des donnees de Fourier) pourront echapper formellement, sans etat physique associe.

## 5. Procedure
Rapports sauvegardes avec empreintes ; NOTE-142 confronte les criteres ; aucune correction de NOTE-140 avant NOTE-142.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138) et M-V3 candidats non graves ; noyau inchange.
