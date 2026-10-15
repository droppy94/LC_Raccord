---
id: NOTE-BORD-EON-172-ARMEMENT-AUDIT-DIRAC-V2
numero: 172
serie: I
branche: Chantier D (article RG-4 spin 1/2, audit)
reservation: 2026-10-14T17:56 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 172)
date: 2026-10-14
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL d'audit froid aveugle de l'article RG-4 spin 1/2 v2 (NOTE-171 v2), scelle avant tout lancement"
decision: operateur (Thierry), 2026-10-14 19:54 heure de Paris (« ok pour tes propositions et pour l'armement »)
---

# Gel : audit froid aveugle de l'article « A massive Dirac field at future conformal infinity » (v2)

## 0. Objet et motif
La v2 de l'article (NOTE-171 v2, sha256 `d2a0a3abe81f8c81`) ajoute des enonces neufs au corpus, obtenus en seance le 14 octobre apres une relecture critique par une IA exterieure (ChatGPT), qui ne vaut pas lecture humaine : dependance de jauge (Prop. 2), obstruction invariante de jauge sur la densite d'energie rescalee (Prop. 3), lemme de couplage (Lemme 2), masse variable (Prop. 4). Ces enonces conditionnent la greffe S26-02 v2 proposee (acte prevu NOTE-174). Precedent (x) : audit le jour meme par deux auditeurs isoles.

## 1. Auditeurs et consignes (scellees ci-dessous)
- **DA-1, derivation en cecite stricte** : ne voit ni l'article, ni le script, ni le corpus ; derive seul les reponses a Q1-Q6. Consigne `PROMPT-AVEUGLE-DA1.md`, sha256 `083b4b77390ac4fa`.
- **DA-2, audit adverse** : lit le source v2 et le script v2, les execute et les attaque (E1-E7). Ne voit pas le corpus. Consigne `PROMPT-AVEUGLE-DA2.md`, sha256 `44406fd6417ac025`. Pieces : `dirac-mass-scri-v2.tex` `d2a0a3abe81f8c81`, `dirac_scri_check_v2.py` `aae42b1b8c08d4d0`.

## 2. Criteres de concordance (fixes avant lecture des rapports)
| Critere | Enonce porteur | Concordance si |
|---|---|---|
| C-1 | Prop. 1 : norme constante, u = exp(i beta (m/H) ln Omega) chi, chi converge, pas de limite pour m != 0 | DA-1 et DA-2 l'obtiennent / le valident |
| C-2 | Prop. 2 : (a) jauge a potentiel integrable : pas de limite ; (b) solution mixte : aucune jauge ; (c) solution particule : limite dans la jauge lambda = (m/H) ln Omega = -mt, potentiel a pole non integrable ; pas de jauge ou psi_hat et A sont continus | idem, y compris la lecture physique reguliere |
| C-3 | Prop. 3 : Omega rho_hat -> m(abs(chi+)^2 - abs(chi-)^2), pole m/Omega invariant de jauge ; difference a une particule sans ambiguite de renormalisation | idem |
| C-4 | Lemme 2 : couplages locaux d'ordre <= 1 sur dS exact = masse constante (chirale) | idem, ou contre-exemple dans la classe |
| C-5 | Prop. 4 : (a) continuite ssi int m dt fini ; (b) densite bornee ssi m a borne ; (c) lissite ssi m = Omega mu ; ordre strict ; exemple Omega^{1/2} | idem |
| C-6 | Script : conforme a la section Verification | DA-2 |

## 3. Espace de verdicts
- **AU-V0** : audit non concluant (rapports inexploitables ou hors sujet).
- **AU-V1** : concordance totale sur C-1 a C-6, aucune correction de fond.
- **AU-V2** : concordance sur les enonces porteurs, corrections mineures (formulation, constante, hypothese a expliciter).
- **AU-V3** : au moins un enonce porteur invalide ou non demontre ; la greffe S26-02 v2 est suspendue sur ce point.

## 4. Prediction (anti-ajustement)
**AU-V2** : enonces porteurs confirmes ; corrections attendues sur la formulation du Lemme 2 (classe des couplages, cas Z1^2 = Z2^2) et sur la portee quantique de la Prop. 3 (etats non quasi-libres). Desirable pour l'article : AU-V1 ; a combattre.

## 5. Consequence fixee d'avance
- AU-V1 ou AU-V2 : la greffe S26-02 v2 est entee par acte (NOTE-174), avec les corrections ; l'article passe en v2.1 si corrections.
- AU-V3 : la greffe est entee seulement pour les enonces confirmes ; l'enonce invalide est retire de l'article.

## 6. Firewall
Aucun auditeur ne voit le corpus ni cette note ; aucune lecture de source nouvelle n'est faite par l'assistant pendant l'audit ; le resultat d'audit IA ne vaut pas lecture humaine exterieure et ne change pas le grade de RG-4 (refutee a titre provisoire).

## 7. Non-surclassement
Rien de grave. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
