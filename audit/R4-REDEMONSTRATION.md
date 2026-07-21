# R-4 — REDÉMONSTRATION « C_T ∝ N ; A_T·N=16 » — rapport de lot (2026-07-21)

Protocole §2.0 du lotissement, exécuté dans l'ordre.

## 1. Gel de cible (étape 1)

`audit/R4-CIBLES-GELEES.md` — **sha256
044dc74995bfee38518b71e7a25e5a6743c67e596fd3c3a009c69643948a0908** —
13 cibles (T1–T13) extraites des SEULS front-matters de LC-D-CT-ATN v0.2,
LC-D-CT-REALITE v0.2, LC-D-CT-DUAL v0.7, LC-D-CT-DUAL-DS v0.1,
LC-D-CT-GAMMA v0.1, figées AVANT toute redérivation. Corps de dérivation
d'origine NON lus (dérivation aveugle).

## 2. Redérivation indépendante (étape 2)

`instruments/redemo_R4_CT.py` — sympy, depuis les prémisses nommées
(dS₄, M_Pl réduit, G=1/(8πM_Pl²), ℓ=1/H, κ²=8πG, d=3, Bunch–Davies,
μ=(M_Pl/2)a·h). **32/32 PASS, EXIT 0.** Les deux routes (canonique par
modes BD ; holographique par 𝒫=1/(2|Im F|) sur l'action on-shell)
convergent sur le MÊME ⟨|h|²⟩=2H²/(M_Pl²k³), redérivé de bout en bout ;
A_T·N=16 tombe par cancellation structurelle de H et G ; le firewall n
(γ=n², n=2 unique) et le firewall du garde-fou de signe (retrait du −2
⟹ flip) mordent.

## 3. Réconciliation — deux points consignés, aucun écart de cible

- **(a) Représentation de la carte S (T10/T11).** En aveugle, l'action de
  S sur les FONCTIONS (f_a,f_b)↦(−f_b,f_a) induit S^T sur les
  coefficients et donne BD mode propre **−i** ; la cible « mode propre
  +i » est reproduite avec S agissant sur le VECTEUR DE COEFFICIENTS
  (S·c = i·c, vérifié). Le signe de la valeur propre est un choix de
  représentation (±i s'échangent sous S↔S^T) ; S²=−𝟙, le caractère
  ±i, et tout l'aval sont INSENSIBLES à ce choix. Consigné, sans effet.
- **(b) Chaîne de signe du garde-fou (T12).** La première chaîne aveugle
  (double application du préfacteur −2 sur W̃) donne un flip ; la lecture
  qui reproduit la cible est celle du NOYAU DE RÉPONSE (⟨T̃⟩=−2δW̃/δh̃,
  noyau δ⟨T̃⟩/δh̃ comparé à δ⟨T⟩/δh) — le − de W̃ est compensé UNE fois
  par le −2 de l'éq.63. Sous cette lecture, C̃_T=+C_T est reproduit et
  le firewall (sans le −2 ⟹ flip) morde. La formalisation exécutable de
  la tête est le sceau `verif_D_CT_dual.py` (bloc B), rejoué RC0.
- Incident d'instrument bénin : deux identités exigeaient une réécriture
  exponentielle explicite pour que sympy conclue (simplify seul
  insuffisant) — instrument, pas algèbre.

## 4. Sceaux (étape 3) — rejoués au harnais G-3 (2026-07-21, RC0)

| sceau | zone | sha8 | issue |
|---|---|---|---|
| verif_D_CT_ATN.py | ARCHIVE | 73bc2e8d | RC0 |
| verif_D_CT_dual.py | ARCHIVE | 3df20802 | RC0 |
| verif_D_CT_dual_dS.py | ARCHIVE | a96561c9 | RC0 |
| verif_D_CT_gardefou_dS.py | ARCHIVE | f83f001b | RC0 |
| verif_D_CT_realite.py | ARCHIVE | 140bc8f3 | RC0 |
| verif_D_CT_constructif.py | ARCHIVE | ca246879 | RC0 |
| verif_naction_gamma_dHSS.py | ARCHIVE | d318ffe0 | RC0 |

## 5. Grade (étape 4)

**REPRODUIT** — 13/13 cibles gelées reproduites par redérivation
indépendante (32 asserts), sceaux d'origine rejoués verts sur le clone,
deux points de réconciliation consignés (représentation ; lecture du
noyau de réponse), aucun écart numérique ni algébrique.

L'issue étant conforme aux têtes scellées, aucun audit froid n'est
déclenché (§2.0-5 : obligatoire seulement si l'issue diffère).

## 6. §6.4 — sans surclassement

« REPRODUIT » = algèbre correcte + cibles reproduites, sous hypothèses
explicites (Bunch–Davies, conventions nommées, GIVEN les intrants des
têtes) — JAMAIS « D1 fermé », « N fixé » ni « CCC démontrée ». La
circularité LC-E (fixation de N) est INCHANGÉE ; la survie au crossover
est INCHANGÉE ; { A4 ; A2★ ; N } INCHANGÉ · nœud (i) INDÉTERMINÉ
(pas A) · CCC non démontrée NI réfutée.
