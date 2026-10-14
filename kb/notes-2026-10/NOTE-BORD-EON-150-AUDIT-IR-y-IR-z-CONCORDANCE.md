---
id: NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE
numero: 150
serie: I
branche: Q-M3 suite (audit IR-y et IR-z)
reservation: 2026-10-12T15:36 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 150)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-149-ARMEMENT-AUDIT-IR-y-IR-z (sha256 eb058f6f19f99042916b4a537d15e70117aeb8b2305b0ac3e121e8483b80a98d, sceau 2026-10-12T15:36:56Z)
rapports:
  - "audit_ya1/RAPPORT-YA1.md, sha256 17b4a143ede091092dc09fe7b7bba0d0b7e8b7e86ac2483d66bdad46004ccc3f (derivation en cecite stricte ; scripts ya1_q1_homogene.py, ya1_q2_support_singulier.py, ya1_q3q4_prolongement.py)"
  - "audit_ya2/RAPPORT-YA2.md, sha256 a5cc90f16f2dfff3e6e4be831edd6ac07047ca2faf6b91b56a48ab9599c9f153 (audit du script, reproduction repro_ya2.py)"
  - "audit_za1/RAPPORT-ZA1.md, sha256 b081ee5de22e027938eb3b03f2a34bf623a32b898ab09c5d28da77cd68da3155 (lecture aveugle, extraits E01 a E14, conversion_za1.py)"
objet: [NOTE-BORD-EON-146-IR-y-EXECUTION, NOTE-BORD-EON-148-IR-z-LECTURE-2501.01972]
verdict: "AU-V2 pour NOTE-146 (correction d'objet en y-1, conclusion renforcee) ; AU-V1 pour NOTE-148 (deux precisions)"
prediction_realisee: "oui pour les verdicts ; la correction d'objet de y-1 n'etait pas predite"
rouvre_si:
  - "lecture des sources (Fulling-Narcowich-Wald 1981, Radzikowski 1996) contredisant l'enonce de propagation ou le role de la positivite"
  - "etat anisotrope homogene du champ conforme : partie sans trace de T^w a l'ordre zero, non instruite"
---

# NOTE-150 : concordance de l'audit froid aveugle de NOTE-146 et NOTE-148. Conclusions confirmees et renforcees ; une erreur d'objet dans NOTE-146 (le terme αβ* du tenseur conforme s'annule) ; NOTE-148 fidele. Verdicts **AU-V2 (146)**, **AU-V1 (148)**

## 0. Resume
- **Hadamard ⟹ regulier en 𝓘⁺, retrouve en cecite stricte** (YA-1) avec une preuve plus forte que celle de NOTE-146 : pour tout etat quasi-libre Hadamard sur le demi-espace, w se prolonge en bisolution C^∞ sur R⁴ × R⁴, **regularite jointe** comprise (probleme de Cauchy des bisolutions, formule de Kirchhoff, E ⊗ E sur des donnees lisses ; ou tranche temporelle + propagation de Hadamard). Aucun etat Hadamard n'a ∂∂w|coinc ~ 1/η. Point nouveau : la **positivite** est necessaire au passage local-vers-global (l'exemple H + w_αβ* seul, non positif, est localement Hadamard pres de la diagonale mais porte le cone reflechi).
- **Cone reflechi retrouve deux fois** (YA-1, YA-2) : w_αβ*(x, x′) = G(x, Rx′), Rx′ = (−η′, x′), structure de charge image ; forme fermee 1/(4π²(r² − (η + η′ − i0)²)) ; non Hadamard pour toute loi de puissance ; Hadamard ⟺ β_k a decroissance rapide (YA-1 montre la necessite par les moments de la mesure positive k|β_k|² dk).
- **Erreur d'objet dans NOTE-146 y-1** (YA-2, [calcule]) : pour le scalaire conforme (ξ = 1/6) en etat homogene **isotrope**, le terme αβ* de ⟨T_μν⟩ est **identiquement nul** (T₀₀ pour tout ξ, T_ij proportionnel a ξ − 1/6) ; T^w se reduit au terme |β|², independant de η. Ce que iry_state_v2.py calcule est la limite de coincidence de ⟨φ²⟩ (ou la pression a ξ ≠ 1/6), pas T^w. L'exposant |η|^(N−4) et le cas critique N = 3 valent pour ⟨∂∂w⟩|coinc et pour la pression non conforme, avec un coefficient Γ(4−N) cos(π(4−N)/2 + φ) : 1/η ssi N = 3 **et** sin φ ≠ 0 (regulier si αβ* reel). La conclusion de NOTE-146 n'en est que renforcee : a l'ordre zero en ε, aucun etat homogene isotrope du champ conforme ne produit de T̂ ~ s¹, Hadamard ou non ; a l'ordre ε, c'est la regularite jointe de w (YA-1) qui tranche.
- **Script** (YA-2) : s'execute, mais presque tout est imprime en dur ; annotations fausses (signe du 1/η, parite, etiquette « N = 1 », classe « |.|^(N−4) » au lieu de C^(N−2) sur le cone, [calcule] sur des lignes non calculees) ; coupure infrarouge obligatoire pour N ≥ 4. Aucun contre-exemple : phases lineaires ou oscillantes deplacent la singularite (poles en η₀, ±l/2), supports compacts donnent des fonctions entieres.
- **NOTE-148 fidele** (ZA-1) : eq. 35, 42, 46 relevees ; n = 8 pour les trois especes (photon par les rapports 1/2 et 1/12) ; « suggests », « explains », « permits », ni demonstration ni verification a deux boucles ; absences confirmees (independance de jauge, a → ∞, e-folds, rupture). Deux precisions : (i) les resultats de Sitter (35)-(37) sont **lus a partir de [6] et [8] par proportionnalite, non recalcules** par la source ; (ii) la jauge de Lorentz locale est fixee par le vierbein symetrique (p. 3), aucune fixation de jauge gravitationnelle n'est discutee ; le terme κ²H² du glissement (37) est une constante non resommee.

## 1. Confrontation aux criteres (figes, NOTE-149 §2)
| Critere | Resultat | Statut |
|---|---|---|
| **C-1 (y-1)** | YA-1 : exposant N−4, 1/η pour N = 3 (coefficient sin φ/(4π²η)), entiere pour decroissance rapide, retrouves pour ∂∂w|coinc et la pression ; YA-2 : idem pour ⟨φ²⟩ et la pression a ξ ≠ 1/6, **mais T^w conforme isotrope sans terme αβ*** | **satisfait avec correction d'objet** |
| **C-2 (y-2)** | YA-1 et YA-2 : cone reflechi |x − x′| = |η + η′|, dans le domaine, singularite d'ordre fini pour k^(−N) ; Hadamard ⟺ decroissance rapide (necessite demontree par YA-1) | **satisfait** |
| **C-3 (y-3)** | YA-1 : prolongement C^∞ jointe par Cauchy des bisolutions (Kirchhoff) ou tranche temporelle (Dimock) + FNW/Radzikowski ; positivite necessaire au local-vers-global | **satisfait, theoreme plus fort que celui de NOTE-146** |
| **C-4 (contre-exemples)** | YA-2 : aucun ; argument general par propagation des singularites de l'equation des ondes en (η + η′, x − x′) | **satisfait** |
| **C-5 (z-1, z-2)** | ZA-1 : eq. 35, 46, rapports 1/2 et 1/12 ; n = 8, coefficient (N_S + 6N_F + 12N_V)κ_P²H²/(240π²) ; a^p, p = coefficient du log | **satisfait** |
| **C-6 (z-3, z-4, z-6)** | ZA-1 : Callan-Symanzik (41), γ (40), δZ (39) importee de [27] et [8], β = 0, (38) ; mots releves ; absences confirmees | **satisfait** |

## 2. Points de detail [rapporte]
### 2.1 YA-1
- Partie oscillante J(η) = (1/2π²)∫k³ Re[αβ* e^(−2ikη)]dk : entre dans ∂_η∂_η′w avec le signe −, dans Σ∂_i∂_i′w avec +, disparait de la densite d'energie mais non de la pression (coherent avec YA-2 : nulle a ξ = 1/6 par l'amelioration).
- Divergence logarithmique de ∂²w sur le cone reflechi verifiee numeriquement (pente ln10/(4π²)).
- Etats de classe (b) : deux violations de Hadamard, le cone reflechi (αβ*) et une singularite de frequence negative sur le cone reel (|β|² ~ k^(−2N)).
- Etats a 1/η : WF(ω₂) ⊄ C⁺, etats adiabatiques d'ordre fini ; la divergence est un artefact du choix d'etat, non du bord.
- Vigilance : tous les theoremes cites de memoire ; hypotheses a verifier sur source.

### 2.2 YA-2
- Reproduction independante (repro_ya2.py) : integrales gaussiennes et k^(−N) retrouvees ; forme fermee du terme αβ* verifiee ; comportements N = 2 a 6 ; logs aux N pairs (N = 4 : ln ; N = 6 : η² ln).
- Annulation a ξ = 1/6 [calcule] : T₀₀ sans terme αβ* pour tout ξ ; T_ij ∝ (ξ − 1/6) ; seule la partie sans trace d'un etat **anisotrope** survivrait a ξ = 1/6 (non instruit ; porte en `rouvre_si`).
- Le terme |β|² est lui aussi non lisse (cone ordinaire) pour une decroissance en puissance.
- y-4 : pour le champ conforme isotrope, T̂ ~ s² exactement, jamais s¹ ; a ξ ≠ 1/6, s¹ ssi N = 3 et sin φ ≠ 0.

### 2.3 ZA-1
- Type : prepublication, aucune mention de journal ; κ² = 16πG (eq. 2).
- Photon : pas d'equation propre ; « Dirac = 1/2 EM », « MCC = 1/12 EM » ; EM conforme en D = 4 seulement.
- Potentiel newtonien : meme exposant que le Weyl electrique, argument aHr (eq. 36, 43) ; slip (37) constant.

## 3. Lecture [derive]
1. **NOTE-146.** La conclusion Y-V1 tient et se renforce : (i) l'argument general est plus fort (regularite jointe etablie par construction, sans passer par la propagation des singularites) ; (ii) a l'ordre zero, le champ conforme isotrope ne porte meme pas de terme d'etat dependant de η. La correction d'objet est reelle : le §0 y-1, le §1 et le schema de NOTE-146 parlent de « T^w » la ou il s'agit de ⟨∂∂w⟩|coinc (ou de ⟨φ²⟩) ; la logique de comptage (quel exposant donnerait s¹) reste juste pour les quantites qui entrent a l'ordre ε. La qualification Y-V2 (theoremes cites de memoire) subsiste ; elle est precisee : la positivite de l'etat est une hypothese du passage local-vers-global, et la version purement locale de la forme de Hadamard ne suffit pas.
2. **NOTE-148.** Aucune correction ; deux precisions utiles : la source ne recalcule pas (35)-(37) mais les lit a partir de [6] et [8], ce qui deplace la justification du coefficient de Dirac vers la chaine Maxwell ([8] = Foraci-Woodard 2412.11022) ; la jauge discutee est la jauge de Lorentz locale, non la jauge gravitationnelle.
3. **Script iry_state_v2.py** : a requalifier comme illustration des integrales de Fourier, non comme calcul de T^w ; les resultats imprimes en dur doivent etre soit calcules, soit etiquetes [derive].

```
   audit de NOTE-146 / NOTE-148
   -------------------------------------------------------------------------------
   Hadamard => w C^inf jointe a travers eta = 0      retrouve, renforce (YA-1)
   cone reflechi, Hadamard <=> decroissance rapide   retrouve deux fois (YA-1, YA-2)
   T^w du scalaire conforme isotrope : terme alpha beta* = 0   correction d'objet (YA-2)
   exposant N-4, 1/eta ssi N = 3 (et sin phi != 0)  retrouve pour <dd w>, <phi^2>, pression
   contre-exemples                                   aucun (YA-2)
   NOTE-148 : eq. 35/42/46, n = 8, "suggests"        retrouve (ZA-1) ; (35)-(37) lues de [6],[8]
   -------------------------------------------------------------------------------
```

## 4. Verdict
- **NOTE-146 : AU-V2.** C-1 a C-4 satisfaits, avec une correction d'objet (y-1 porte sur ⟨∂∂w⟩|coinc, ⟨φ²⟩ et la pression non conforme, non sur T^w du scalaire conforme isotrope, dont le terme αβ* est nul), un argument general renforce (regularite jointe, positivite), et des corrections d'annotation du script. Verdict Y-V1 qualifie Y-V2 **inchange** ; greffe NOTE-146 v2 proposee.
- **NOTE-148 : AU-V1.** C-5 et C-6 satisfaits sans correction ; deux precisions a porter en v2 (lecture de (35)-(37) a partir de [6] et [8] ; jauge de Lorentz locale). Verdict Z-V1 qualifie Z-V2 inchange.

## 5. Confrontation a la prediction
Prediction (NOTE-149 §4) : AU-V2 pour 146 [**realise**, mais pour une raison plus substantielle que predite : correction d'objet et non seulement precision de theoreme] ; AU-V1 ou AU-V2 pour 148 [**realise**, AU-V1] ; YA-1 nommant FNW ou Hormander et qualifiant la regularite jointe [**realise**, et la regularite jointe est etablie plutot que qualifiee] ; YA-2 relevant la coquille de signe [**realise**, plus l'annulation a ξ = 1/6, non predite] ; ZA-1 retrouvant n = 8 et « suggests », avec une absence nouvelle [**realise** : lecture par proportionnalite, jauge de Lorentz].

## 6. Consequences (rien n'est grave)
- Greffes proposees, non entees : **NOTE-146 v2** (objet de y-1 ; argument general : Cauchy des bisolutions, regularite jointe, positivite ; schema ; annotations du script, iry_state_v2 requalifie) ; **NOTE-148 v2** (deux precisions).
- Classe de G-V3 confirmee : « WZ integrable + Γ[g] dans un etat Hadamard » ; libelle NOTE-138 a reviser (v3) avec cette classe et la clause resommee precisee (NOTE-148).
- Point nouveau, non instruit : partie sans trace de T^w pour un etat homogene **anisotrope** du champ conforme a l'ordre zero (YA-2) ; a l'ordre ε, couvert par la regularite jointe.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 7. Non-surclassement
[conv]. Audit par agents isoles du meme systeme ; theoremes cites de memoire par les auditeurs (Kirchhoff, Dimock, Fulling-Narcowich-Wald, Radzikowski-Verch, Hormander), numeros non certifies ; la lecture de la source par ZA-1 est une lecture d'extraits via alphaXiv.
