# REJEU-SCEAUX — rapport du harnais G-3 (généré par `instruments/rejeu_sceaux.py`)

Date de génération : 2026-07-21 19:33:16 · dépôt : layout git (KB sous `kb/`), lanceur G-2 (cwd = racine KB, zéro octet de sceau modifié).

## Bilan

- Sceaux rejoués : **83** (7 LIVE, 76 ARCHIVE)
- Issues : **82 RC0** · **0 RC!=0** · **1 INEXECUTABLE-ICI** (délimitation d'environnement, PAS un échec)

## Confrontation §9ter (les 7 sceaux LIVE du manifeste v2.124)

| sceau | sha8 §9ter | sha8 clone | conforme | rc | issue |
|---|---|---|---|---|---|
| verif_paquet_propre.py | 051e2833 | 051e2833 | OUI | 0 | RC0 |
| verif_nonlin_parity.py | 9df8e53e | 9df8e53e | OUI | 0 | RC0 |
| verif_D3_P6_specB_oracle.py | 162696c1 | 162696c1 | OUI | 0 | RC0 |
| verif_A2_numerique.py | 76e9257c | 76e9257c | OUI | 0 | RC0 |
| diag_bounces.py | 804b7f9b | 804b7f9b | OUI | 0 | RC0 |
| verif_A4_QW.py | a4637a2c | a4637a2c | OUI | 0 | RC0 |
| verif_A4_QW_typeI_succ.py | 79f09a8c | 79f09a8c | OUI | 0 | RC0 |

Rappel de grade : un sha8 conforme n'atteste que l'identité des octets ; un rc 0 n'atteste qu'UNE exécution sur CE clone à CETTE date (G-3c).

## Sceaux LIVE

| sceau | sha8 | rc | durée (s) | timeout (s) | issue | date |
|---|---|---|---|---|---|---|
| diag_bounces.py | 804b7f9b | 0 | 5.7 | 900 | RC0 | 2026-07-21 19:26:34 |
| verif_A2_numerique.py | 76e9257c | 0 | 1.0 | 900 | RC0 | 2026-07-21 19:26:29 |
| verif_A4_QW.py | a4637a2c | 0 | 2.4 | 300 | RC0 | 2026-07-21 19:02:52 |
| verif_A4_QW_typeI_succ.py | 79f09a8c | 0 | 1.4 | 300 | RC0 | 2026-07-21 19:02:53 |
| verif_D3_P6_specB_oracle.py | 162696c1 | 0 | 111.8 | 900 | RC0 | 2026-07-21 19:26:28 |
| verif_nonlin_parity.py | 9df8e53e | 0 | 125.9 | 900 | RC0 | 2026-07-21 19:24:36 |
| verif_paquet_propre.py | 051e2833 | 0 | 0.3 | 300 | RC0 | 2026-07-21 19:02:49 |

## ARCHIVES

| sceau | sha8 | rc | durée (s) | timeout (s) | issue | date |
|---|---|---|---|---|---|---|
| verif_A3_D1_passerelle.py | 08f2d4e9 | 0 | 0.8 | 120 | RC0 | 2026-07-21 19:27:28 |
| verif_D1_atlas.py | 9ec5bc60 | 0 | 0.1 | 120 | RC0 | 2026-07-21 19:27:28 |
| verif_D1_bianchiA.py | 8b46efb0 | 0 | 5.2 | 120 | RC0 | 2026-07-21 19:27:33 |
| verif_D1_bianchiIX_domain.py | 8bfa323b | 0 | 1.2 | 120 | RC0 | 2026-07-21 19:27:34 |
| verif_D1_einstein3d.py | 3a864d9e | 0 | 5.1 | 120 | RC0 | 2026-07-21 19:27:39 |
| verif_D1_facteur.py | fed811ea | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:27:40 |
| verif_D1_stabilite.py | 41509a9f | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:27:40 |
| verif_D1c3_genericite.py | b615d6b4 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:27:41 |
| verif_D1c3_regularite.py | 3fc462fe | 0 | 4.0 | 120 | RC0 | 2026-07-21 19:27:45 |
| verif_D3_A_horizon.py | c363c0c4 | 0 | 27.7 | 120 | RC0 | 2026-07-21 19:28:13 |
| verif_D3_B_curvature.py | e52965c8 | 0 | 14.1 | 120 | RC0 | 2026-07-21 19:28:27 |
| verif_D3_C7b_A1_superhorizon.py | f52d7c16 | 0 | 1.2 | 120 | RC0 | 2026-07-21 19:28:28 |
| verif_D3_C7b_A2_reduction.py | ee03c385 | 0 | 2.1 | 120 | RC0 | 2026-07-21 19:28:30 |
| verif_D3_C7b_gradient.py | d993d972 | 0 | 1.2 | 120 | RC0 | 2026-07-21 19:28:31 |
| verif_D3_C7b_spikes.py | f68fcf75 | 0 | 36.8 | 120 | RC0 | 2026-07-21 19:29:08 |
| verif_D3_C_decoupling.py | e5d45c1e | 0 | 9.0 | 120 | RC0 | 2026-07-21 19:29:17 |
| verif_D3_P6_poc_specA.py | 74b015af | 0 | 6.8 | 120 | RC0 | 2026-07-21 19:29:24 |
| verif_D3_P6_specB_poc.py | 66c745c8 | 0 | 9.6 | 120 | RC0 | 2026-07-21 19:29:33 |
| verif_D3_P6_specB_supp.py | 8a0e2e49 | 0 | 19.3 | 120 | RC0 | 2026-07-21 19:29:53 |
| verif_D3_WCH_GWE.py | 664660ee | 0 | 1.1 | 120 | RC0 | 2026-07-21 19:29:54 |
| verif_D3_backreaction.py | 665e6ca0 | 0 | 1.8 | 120 | RC0 | 2026-07-21 19:29:56 |
| verif_D3_bunchdavies.py | 7f269735 | 0 | 0.8 | 120 | RC0 | 2026-07-21 19:29:56 |
| verif_D3_cancellation.py | 45f755b6 | 0 | 1.6 | 120 | RC0 | 2026-07-21 19:29:58 |
| verif_D3_crossover_attracteur.py | 66b856a6 | 0 | 0.1 | 120 | RC0 | 2026-07-21 19:29:58 |
| verif_D3_crossover_attracteur_stress.py | 2ea50c84 | 0 | 0.1 | 120 | RC0 | 2026-07-21 19:29:58 |
| verif_D3_crossover_matching.py | 1a40baa3 | 0 | 1.1 | 120 | RC0 | 2026-07-21 19:29:59 |
| verif_D3_crossover_stabilite.py | 5dc65037 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:00 |
| verif_D3_interaeon_convergence.py | 349177c3 | 0 | 10.0 | 120 | RC0 | 2026-07-21 19:30:10 |
| verif_D3_interaeon_kappa.py | 3905e4f6 | 0 | 2.5 | 120 | RC0 | 2026-07-21 19:30:12 |
| verif_D3_interaeon_matiere.py | 06fbc400 | 0 | 31.0 | 120 | RC0 | 2026-07-21 19:30:43 |
| verif_D3_interaeon_poc.py | 42943791 | 0 | 0.9 | 120 | RC0 | 2026-07-21 19:30:44 |
| verif_D3_spectre_k3.py | 706e97cc | 0 | 1.0 | 120 | RC0 | 2026-07-21 19:30:45 |
| verif_D_CT_ATN.py | 73bc2e8d | 0 | 0.6 | 120 | RC0 | 2026-07-21 19:30:46 |
| verif_D_CT_constructif.py | ca246879 | 0 | 0.7 | 120 | RC0 | 2026-07-21 19:30:46 |
| verif_D_CT_dual.py | 3df20802 | 0 | 0.7 | 120 | RC0 | 2026-07-21 19:30:47 |
| verif_D_CT_dual_dS.py | a96561c9 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:30:48 |
| verif_D_CT_gardefou_dS.py | f83f001b | 0 | 0.3 | 120 | RC0 | 2026-07-21 19:30:48 |
| verif_D_CT_realite.py | 140bc8f3 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:30:48 |
| verif_D_g3.py | cb2d6e1c | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:49 |
| verif_D_nongauss_4pt.py | a46e4f6a | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:49 |
| verif_D_nongauss_4pt_phase1.py | 1aa3f051 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:50 |
| verif_D_nongauss_TTT.py | c06f6f51 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:50 |
| verif_D_nongauss_TTT_lourd.py | 2cb93432 | 0 | 0.8 | 120 | RC0 | 2026-07-21 19:30:51 |
| verif_D_nongauss_TTT_lourd_phase1.py | e494c8c6 | 0 | 0.6 | 120 | RC0 | 2026-07-21 19:30:51 |
| verif_D_w3_gpy.py | b01432de | 0 | 0.0 | 120 | RC0 | 2026-07-21 19:30:52 |
| verif_E_N_crosscheck.py | 63407a12 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:52 |
| verif_E_planck.py | 0934497c | 0 | 0.1 | 120 | RC0 | 2026-07-21 19:30:52 |
| verif_F1_spn.py | 19a4931e | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:52 |
| verif_F4_principiel.py | 9947b8ed | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:30:53 |
| verif_F5_scaling.py | a959f137 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:30:53 |
| verif_F6_memoire_cisaillement.py | 23a7d264 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:30:54 |
| verif_G3_adm_imports.py | a0b962c8 | 0 | 1.6 | 120 | RC0 | 2026-07-21 19:30:55 |
| verif_G3_admissibilite.py | 010a0562 | 0 | 0.6 | 120 | RC0 | 2026-07-21 19:30:56 |
| verif_G3_m4_chainon.py | 9486b7b2 | 0 | 22.3 | 120 | RC0 | 2026-07-21 19:31:18 |
| verif_O2_P1.py | 6b23b2ae | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:19 |
| verif_O2_P1b_soperation.py | 57905430 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:31:19 |
| verif_O2_P2.py | f2b110e8 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:20 |
| verif_O2_bprime.py | 4c8d186c | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:20 |
| verif_O2_bprime_AUDIT.py | 95c51287 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:20 |
| verif_O2_coin_transmission_ac.py | 0acf575d | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:21 |
| verif_O2_coin_transmission_fetch.py | 7539188d | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:21 |
| verif_O2_hodge.py | 421d5f29 | 0 | 0.3 | 120 | RC0 | 2026-07-21 19:31:22 |
| verif_cartographie_v11_nonregression.py | 81e1914b | 1 | 0.0 | 120 | INEXECUTABLE-ICI (env: mnt/project) | 2026-07-21 19:31:22 |
| verif_cb_weyl_magnetique.py | e1bef559 | 0 | 1.4 | 120 | RC0 | 2026-07-21 19:31:23 |
| verif_gamma_nstar_ads4.py | 367d2ddb | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:31:24 |
| verif_manifeste_v2122_consignation.py | 5349ad47 | 0 | 0.0 | 120 | RC0 | 2026-07-21 19:31:24 |
| verif_moduleA_scri.py | 690eb4c7 | 0 | 1.4 | 120 | RC0 | 2026-07-21 19:31:25 |
| verif_naction_alpha.py | 80005547 | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:31:25 |
| verif_naction_aveugle.py | 1468672c | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:31:26 |
| verif_naction_firewall.py | d985390d | 0 | 0.5 | 120 | RC0 | 2026-07-21 19:31:26 |
| verif_naction_gamma_dHSS.py | d318ffe0 | 0 | 0.4 | 120 | RC0 | 2026-07-21 19:31:27 |
| verif_nonlin_cotton.py | b218f974 | 0 | 60.9 | 120 | RC0 | 2026-07-21 19:32:28 |
| verif_nonlin_deuxpoint.py | 1e40f5e8 | 0 | 6.0 | 120 | RC0 | 2026-07-21 19:32:34 |
| verif_nonlin_repr.py | 98f34c75 | 0 | 0.7 | 120 | RC0 | 2026-07-21 19:32:34 |
| verif_phi_seals.py | 5a1d16a2 | 0 | 40.8 | 120 | RC0 | 2026-07-21 19:33:15 |
| verif_spn.py | d34031f0 | 0 | 0.3 | 120 | RC0 | 2026-07-21 19:33:16 |

## §6.4 — grade, à ne jamais surclasser (G-3c)

Un rc 0 sur le clone atteste UNE exécution sur CE clone à CETTE date. Il ne rejoue aucune gate, ne requalifie aucun grade du mount, ne re-scelle rien. Un rc != 0 sur une ARCHIVE se consigne et s'instruit au lot R-n correspondant — il ne « casse » rien par lui-même. INEXECUTABLE-ICI est une délimitation d'environnement (dépendance mount, réseau coupé, timeout court), pas un échec. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
