# R-5 — REDÉMONSTRATION « trois réductions ⟹ { A4 ; A2★ ; N } » — rapport de lot (2026-07-21)

Protocole §2.0 du lotissement, exécuté dans l'ordre.

## 1. Gel de cible (étape 1)

`audit/R5-CIBLES-GELEES.md` — **sha256
9b84e80003b5e76c96d770f5a7155f5471fd8f3b367e44b8de71b828e45a103a** —
7 cibles (P1–P7) extraites des SEULS front-matters de
LC-WORK-A3-D1-PASSERELLE v0.3 et LC-WORK-D1-E-AMPLITUDE v0.3 ; la
troisième réduction (sceau C_T) renvoie au lot R-4 (REPRODUIT,
gel 044dc749). Corps de dérivation NON lus.

## 2. Redérivation indépendante (étape 2)

`instruments/redemo_R5_reductions.py` — **18/18 PASS, EXIT 0**, premier
passage sans correction d'instrument. Redérivés de bout en bout :
- **P1** — la relation d'état BD g₃=−(i/3)k³g₀ tombe du développement en
  série du mode (1+ikη)e^{−ikη} (coefficient η³), avec contrôles η¹=0 et
  η²=k²g₀/2 ;
- **P2** — Π^TT explicite en 3D sur c·δ_ij : zéro identiquement (un
  isotrope est pure trace) ⟹ A3 force ⟨g₃⟩=0 ;
- **P3** — inclusion STRICTE par témoin : l'état BD lui-même a ⟨g₃⟩=0
  (∈S_A3) mais ⟨g₃g₃⟩=k⁶𝒫₀/9≠0 (∉S_A4) ⟹ A4⟹A3-un-point, sens unique ;
- **P4** — ⟨g₃g₃⟩=(2H²/9M_Pl²)·k³ par recombinaison P1×𝒫₀ (𝒫₀
  redémontrée en R-4/T1) ; Δ=3 ; invariance d'échelle vérifiée sous
  k→λk ;
- **P5** — un champ gaussien = (moyenne, deux-point) ; moyenne fixée
  (P2/P3), forme fixée (P4) ⟹ résidu = UN nombre = A_T=(2/π²)(H/M_Pl)² ;
- **P6** — A_T·N=16 re-vérifié (renvoi R-4).

## 3. Réconciliation — un point consigné

**P7 est une recombinaison, pas une algèbre neuve** : la conclusion de
comptage « arc gaussien ⟹ { A4 ; A2★ ; N } » est portée par les jambes
algébriques P1–P6 + R-4 ; son assert dans le script est une CONSIGNATION
du mapping (les inconnues restantes après fixation du un-point, de la
forme et de l'amplitude), non une dérivation. C'est conforme à la nature
des têtes elles-mêmes (« paper-first, AUCUN code neuf », réduction de
comptage). Aucun écart de cible ; aucun incident d'instrument.

Note d'ordre : la jambe P4 redémontre au passage la forme k³ du spectre
— elle pré-couvre une partie du lot R-3 (LC-D3-SPECTRE-K3), qui restera
à compléter sur ses cibles propres (Bunch–Davies, oracle).

## 4. Sceaux (étape 3) — rejoués au harnais G-3 (2026-07-21, RC0)

| sceau | rôle | sha8 | issue |
|---|---|---|---|
| verif_A3_D1_passerelle.py | sceau de reconfirmation du lot | 08f2d4e9 | RC0 |
| verif_D3_bunchdavies.py | parent (relation d'état BD) | 7f269735 | RC0 |
| verif_D3_spectre_k3.py | parent (forme k³) | 706e97cc | RC0 |
| verif_nonlin_deuxpoint.py | relève non-perturbative (v0.3) | 1e40f5e8 | RC0 |
| verif_nonlin_cotton.py / _repr.py | triptyque un-point non-linéaire | b218f974 / 98f34c75 | RC0 |

## 5. Grade (étape 4)

**REPRODUIT** — 7/7 cibles gelées reproduites (18 asserts, dont les
jambes algébriques P1–P6 redérivées indépendamment), sceaux rejoués
verts, une consignation de nature (P7 = recombinaison). Issue conforme
aux têtes ⟹ pas d'audit froid déclenché (§2.0-5).

## 6. §6.4 — sans surclassement

« REPRODUIT » = algèbre correcte + cibles reproduites, sous hypothèses
explicites — JAMAIS « A3 et A4 fusionnés » (l'écart k³ est irréductible
au deux-point), JAMAIS « D1 fermé » (N non fixé, circularité LC-E
intacte), JAMAIS « CCC démontrée ». Réduire le comptage n'est pas
fermer. { A4 ; A2★ ; N } INCHANGÉ · nœud (i) INDÉTERMINÉ (pas A) ·
CCC non démontrée NI réfutée.
