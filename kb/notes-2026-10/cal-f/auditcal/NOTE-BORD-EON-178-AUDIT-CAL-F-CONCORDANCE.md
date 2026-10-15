---
id: NOTE-BORD-EON-178-AUDIT-CAL-F-CONCORDANCE
numero: 178
serie: I
branche: Chantier D / critere (2.17) (audit CAL-F)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-177-ARMEMENT-AUDIT-CAL-F.md (sceau NOTE-176-177-SCEAU.txt, pose avant lancement)"
rapports: "RAPPORT-CA1.md sha256 23c05df6e2a96701 ; RAPPORT-CA2.md sha256 5280ddf372ec3e54"
---

# Concordance de l'audit CAL-F

## 1. Criteres
| Critere | CA-1 (cecite stricte) | CA-2 (adverse) | Concordance |
|---|---|---|---|
| K-1 source fidele | (sans objet) | fidele pour (2.17), (3.11), portee du th. 3.1 sur le systeme couple ; **erreur** : la combinaison finale des termes en Ω^-1 est (1/3)(m² − 2λ/3), pas (m²/3 − λ/18) (qui sont des morceaux) ; citation du th. 3.1 tronquee (« smooth function of the unknowns ») ; hypothese μ = 0 non rappelee | **oui**, corrections |
| K-2 nullite pour fluide homogene conserve et scalaire homogene de masse quelconque | retrouve : RHS ∝ equation de continuite ; scalaire : ∝ φ'·KG[φ], nul sur couche pour tout m | confirme ; mais le test homogene **ne voit pas la masse** : il valide la derivee covariante, pas la detection de la singularite de Friedrich | **oui** sur le calcul ; **non** sur la portee « calibration reussie » |
| K-3 faux pole par derivees partielles | retrouve (plus un faux pole λ/(3s⁴) de ∂g) | confirme | **oui** |
| K-4 Dirac : coefficient m/Ω, sans masse speciale | retrouve γ^a∂_a ψ_r = (m/Ω) ψ_r ; solutions s^{±im} bornees non lisses ; aucune masse constante non nulle, aucun couplage de courbure sans annuler m_eff | confirme, **renforce** (T4 : solutions Ω^{±im/H} non lisses, donc aucune redefinition lisse des inconnues ne regularise ; une phase U(1) donne un terme en γ^μ, pas l'identite) ; « exact analogue » et « au sens de Friedrich » a requalifier en « critere de Friedrich transpose a l'equation de matiere » | **oui**, requalifie |
| K-5 regle de comptage non exacte | **fausse dans les deux sens** : poussiere p = 1 → 0 ; φ = x (sans masse, p = 0) → pole double −κ/(3s²) ; φ = x s^Δ → pole non entier pour 0 < m² < 2, absent a m² = 2 | « ni necessaire ni suffisant » de chercher un pole sur couche ; T3 : a m² = 2 source O(1) (calibration positive inhomogene), a m² = 35/16 source ~ s^{1/2} | **oui**, plus fort que NOTE-176 |
| K-6 greffes proportionnees | (sans objet) | G-CAL-a : correction mineure ; **G-D1-e : la phrase « (2.17) ne voit pas une poussiere homogene » confond valeur sur couche et regularite formelle (grave)** ; article v2.2 : « (2.17) ne requiert pas la Prop. 5(b) » et « veritable counterpart du th. 3.1 » **non demontres** | **non** pour G-D1-e et v2.2 tels que proposes |

## 2. Verdict
**AU-V3 partiel** (K-6 : la greffe G-D1-e et la clause v2.2 telles que proposees en NOTE-176 reposent sur une confusion entre valeur du second membre sur une solution et regularite formelle des seconds membres, qui est le critere du theoreme 3.1). **AU-V2** sur K-1 a K-5 : calculs confirmes, deux fois a l'aveugle pour K-2, K-3, K-4 ; K-5 confirme et aggrave. La « calibration reussie » de NOTE-176 est requalifiee : CAL-F valide la derivee covariante et la nullite pour les sources homogenes conservees ; la calibration positive au sens de Friedrich est fournie par CA-1 (φ = x s^Δ) et CA-2 (T3) dans le cas inhomogene, ou le point m² = 2 est bien distingue.
Prediction (AU-V2) **partiellement non realisee** : le defaut principal n'etait pas la ou il etait attendu (formulation de K-4) mais dans le statut des enonces sur couche.

## 3. Consequences (gel NOTE-177, appliquees par l'acte NOTE-179)
- **G-CAL-a** entee, corrigee : la regle est une borne superieure en composantes de coordonnees ; contre-exemples des deux cotes ; le pole de G-V3 vient d'un calcul explicite. Point de lecture ajoute : un pole sur couche prouve l'irregularite si les autres inconnues sont lisses ; la reciproque est fausse.
- **G-D1-e** entee **reecrite** : (i) critere du corpus (texte de RG-4, Ω^-4 T) : pole m/Ω de la densite d'energie rescalee ; (ii) critere de Friedrich **transpose a l'equation de matiere** (regularite formelle) : coefficient m/Ω de l'equation de Dirac rescalee, present pour toute masse constante non nulle, non eliminable par redefinition lisse des inconnues ; le systeme couple Einstein-Dirac n'est pas traite. La phrase sur la poussiere dans (2.17) est **retiree**.
- **Article v2.2** : ajout d'un paragraphe sur (ii) avec les memes reserves ; aucune affirmation sur ce que (2.17) requiert ou non de la Prop. 5(b).
- **Point nomme pour G-V3, sans changement** : le pole de G-V3 est un pole du second membre de (2.17) evalue sur une solution ; il prouve l'irregularite au sens de Friedrich pourvu que les autres inconnues soient lisses sur cette solution. NOTE-128 note que, au premier ordre, W diverge en ln : cette hypothese est donc a regarder dans la relecture humaine de G-V3 (ajoute aux objections anticipees de NOTE-163 v2).

## 4. Non-surclassement
Un audit par IA ne vaut pas lecture humaine. G-V3 et RG-4 gardent leur grade. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
