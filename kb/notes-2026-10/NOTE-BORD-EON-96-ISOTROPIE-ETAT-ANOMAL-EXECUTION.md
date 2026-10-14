---
id: NOTE-BORD-EON-96-ISOTROPIE-ETAT-ANOMAL-EXECUTION
numero: 96
serie: I
branche: Q-M3 suite (isotropie de l'etat)
reservation: 2026-10-10T11:47 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 96)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
calibration: "[extrait] pour les enonces de S2 cites ; [derive] pour leur application a (2.17)"
gel: NOTE-BORD-EON-95-ARMEMENT-ISOTROPIE-ETAT-ANOMAL (sha256 69b0e7c7d268b75c9eef8b7bd958cfdea92ab9a81dc747b7264e13c62c079edb, 2026-10-10T11:47:50Z)
depend: [NOTE-BORD-EON-95-ARMEMENT-ISOTROPIE-ETAT-ANOMAL, NOTE-BORD-EON-94-AUDIT-FROID-Q-M3-CONCORDANCE, NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION, NOTE-BORD-EON-90-Q-M3-EXECUTION]
sources: ["arXiv:1808.08237v2 (appui, R-41 : 4 miroirs)", "arXiv:2409.18004v1 (reperage, lecture partielle)", "hep-ph/9301280 (non lu, EX-8)"]
rouvre_si:
  - "source donnant la partie sans trace complete de <T_mu nu> pour le secteur F^2 de l'anomalie en fond conformement plat ou de Sitter"
  - "modele de champs du tenseur energie-impulsion d'un champ de Maxwell classique avec couplage anomal"
  - "objection exterieure sur la lecture de S2"
---

# NOTE-96 : l'etat anomal QED a 𝓘⁺. Verdict **ISO-V3**, qualifie par ISO-V4

## 0. Resume
- **La litterature lue ne fournit pas la partie sans trace de ⟨T_μν⟩ du secteur anomal F²** (ISO-V4 sur la determination). La seule action effective exacte lue (S2) le dit elle-meme : elle est obtenue dans le sous-espace des metriques Weyl-plates et ne permet pas la variation metrique complete.
- **Elle fixe en revanche la dynamique** : l'anomalie agit comme un couplage de Maxwell qui court en ln a (S2, eq. 2.11, 3.12-3.13), et, pour l'etat naturel (vide de Bunch-Davies en de Sitter), **les fluctuations du champ restent quantiques** : aucune configuration classique coherente n'est produite (S2, eq. 4.14 et §5).
- **Consequence [derive]** : pour cet etat, ⟨T_μν⟩ est homogene et isotrope ; il tombe dans le cas homogene de NOTE-90, ou le second membre de (2.17) s'annule par symetrie. La condition d'isotropie de NOTE-92 est satisfaite **en valeur moyenne**. Elle est reportee sur l'**etat du champ de Maxwell** : satisfaite pour un etat quantique statistiquement isotrope, non garantie pour des configurations classiques coherentes (ISO-V3).
- Prediction du gel (ISO-V3) **realisee**. Inclinaison vers ISO-V2 pour les etats classiques : **plausible mais non etablie**, parce qu'elle suppose un tenseur energie-impulsion que la source ne fournit pas.

## 1. Sources (EX-7, declarees avant verdict de lecture)

| Id | Titre, auteurs, date, type | Statut | Miroirs (R-41) |
|---|---|---|---|
| **S2** | « To B or not to B: Primordial magnetic fields from Weyl anomaly », A. Benevides, A. Dabholkar, T. Kobayashi, arXiv:1808.08237v2 (8 nov. 2018), article original, JHEP 11 (2018) 039 | **appui**. Lu au texte : resume, §1, §2, §3 en entier (3.1 a 3.3), §4.1 a §4.3 (partie de Sitter), §5. Non lu : §4.4 au-dela de son debut, figures, annexes. Texte alphaXiv, sha256 de l'extraction lue `162d9aae…` | arXiv:1808.08237 ; Springer JHEP11(2018)039 ; HAL hal-01871706 ; IRIS SISSA 20.500.11767/124914 |
| **S3** | « Conformal Backreaction, Chiral and Conformal Anomalies in the Early Universe », C. Corianò, S. Lionetti, D. Melle, R. Tommasi, L. Torcellini, arXiv:2409.18004v1 (26 sept. 2024), acte de conference (MG17) | **reperage**. Lu : pages 1, 3, 4, 7 a 10, 13 a 15, 17 a 20. **Non lu : pages 2, 5, 6, 11, 12, 16.** | arXiv, alphaXiv (moins de trois verifies) |
| **S1** | A. Dolgov, « Breaking of conformal invariance and electromagnetic field generation in the universe », Phys. Rev. D48 (1993) 2499, hep-ph/9301280 | **non lu** (EX-8) ; rapporte uniquement via S2 §5 | — |

## 2. Ce que disent les sources [extrait]

### S2
1. **(2.11), (2.12)** : pour une metrique Weyl-plate `g = e^{2Ω_S} η` (chez S2, Ω_S est le facteur de Weyl, Ω_S = ln a en FLRW ; **homonymie avec le Ω du corpus**, qui vaut 1/a), la partie anomale de l'action effective a une boucle est `S_B = −(β̃/2e²) ∫ d⁴x Ω_S F_μν F^μν`, indices leves par η.
2. **Note 4** (texte integral) : « In the space of metrics, this action is evaluated in the subspace of Weyl-flat metrics. For this reason it is beyond the reach of this method to compute the equations of motion for the background metric which requires a functional variation with respect to g_μν even in directions orthogonal to the Weyl orbits. »
3. **(3.12), (3.13)** : action simplifiee `S = −¼ ∫ I(τ)² F²`, `I² = e⁻² [1 + 2β̃ log(a/a⋆)]` ; equation de mode (3.14) `u'' + 2(I'/I) u' + k² u = 0`.
4. **§2** : cadre de fermions charges **sans masse** (« quarks and leptons are massless »), et §4 : « the scale factor dependence does not "switch off", as long as there are massless particles around ».
5. **(4.14)** : en de Sitter, vide de Bunch-Davies, hors horizon : `κ_k ∼ 1/(2 cos(π β̃))`, independant du temps, d'ordre un pour β̃ petit : « the time-dependence induced by the Weyl anomaly is not sufficient for converting vacuum fluctuations of the gauge field into classical ones ».
6. **(4.15)** : le nombre de photons instantane croit hors horizon comme `a^{2β̃}` (approximation en loi de puissance, valable pour β̃ petit).
7. **§5** : « the Weyl anomaly does not give rise to coherent magnetic fields in the universe » ; les travaux originaux (dont S1) approximaient I² par une loi de puissance, ce que S2 juge incorrect.

### S3 (pages lues seulement)
8. **(2.5)** : la trace anomale generale contient `b₄ F_μν F^μν`. L'action anomale construite dans les pages lues ne porte que sur E et C² (secteur gravitationnel) ; **aucun tenseur energie-impulsion du secteur F² n'y est derive**. Constat de silence sur l'objet, borne aux pages lues.

## 3. Reponses aux sous-questions

| Sous-question | Reponse | Grade |
|---|---|---|
| **I-1** inventaire | Un modele exact lu : S2 (couplage de Maxwell courant en ln a, metriques Weyl-plates). S3 ne traite pas le secteur F². S1 non lu. | [extrait] |
| **I-2** determination de la partie sans trace | **Non fournie** : S2 l'exclut explicitement (note 4). Le modele fixe la dynamique du champ de Maxwell, pas ⟨T_μν⟩ complet. | [extrait] |
| **I-3** isotropie | Pour le vide de Bunch-Davies, le champ reste quantique (κ = O(1)) ; l'etat est statistiquement homogene et isotrope, donc ⟨T_μν⟩ aussi. Pour un tel ⟨T⟩, le cas homogene de NOTE-90 s'applique : second membre de (2.17) nul par symetrie. Pour des champs classiques coherents (d'autres origines), aucune source lue ne donne la partie logarithmique ; la reprise route κ §4 etablit seulement qu'aucun champ de Maxwell classique non nul n'est isotrope en un point. | S2 [extrait] ; application [derive] |
| **I-4** regime | Le cadre de S2 (fermions sans masse, couplage qui court tant qu'il reste des particules sans masse) est celui de C-M1. S2 traite de Sitter avec un nombre fini d'e-folds ; le comportement a 𝓘⁺ exact (a → ∞) n'y est pas etudie : la croissance en `a^{2β̃}` du nombre de photons (point 6) n'y est pas bornee. | [extrait] + reserve |

## 4. Verdict
- **ISO-V3 realise** : l'isotropie requise par NOTE-92 est une propriete de l'etat du champ de Maxwell. Satisfaite en valeur moyenne pour l'etat naturel (Bunch-Davies, reste quantique selon S2) ; non garantie pour des configurations classiques coherentes.
- **Qualification ISO-V4** : aucune source lue ne donne la partie sans trace de ⟨T_μν⟩ du secteur F² ; S2 l'exclut de sa methode. Le passage « etat isotrope ⟹ ⟨T⟩ isotrope » est [derive] (symetrie de l'etat), non lu.
- Prediction (ISO-V3) realisee ; inclinaison ISO-V2 pour les etats classiques non etablie.

## 5. Portee sur Q-M3 et CCC + M
- Q-M3(a) est **precisee une fois de plus** : sous C-M1, au niveau lineaire, le canal de jauge est compatible avec la regularite de (2.17) **pour un contenu electromagnetique quantique et statistiquement isotrope pres de 𝓘⁺** (cas couvert par S2 pour l'etat de Bunch-Davies). Le cas ouvert est celui des **champs classiques coherents** qui survivraient jusqu'a 𝓘⁺.
- Remarque [derive], a instruire, non un verdict : un champ magnetique coherent garde des composantes d'ordre un dans le cadre conforme (F_[g] regulier), donc ne se dilue pas « hors » du probleme ; si sa contribution logarithmique suivait son tenseur de Maxwell, l'argument de rang du corpus la rendrait anisotrope. Cette chaine suppose un tenseur energie-impulsion qu'aucune source lue ne donne.
- Aucune incompatibilite etablie (pas de M-V3). CCC + M reste une hypothese ouverte ; la condition d'etat de NOTE-92 se lit maintenant : « pas de champ electromagnetique classique coherent a 𝓘⁺ », sous reserve de la chaine ci-dessus.

## 6. Passe adverse interne (ne vaut pas audit froid)
1. « Une seule source en appui. » Exact ; S2 est la seule lue qui traite exactement l'objet ; S3 est muette sur F² dans les pages lues ; S1 non lue. Le verdict est borne en consequence (ISO-V4).
2. « L'homonymie Ω. » Chez S2, Ω est le facteur de Weyl (ln a) ; dans le corpus, Ω est le facteur conforme (1/a). Inscrite au §2.1 ; a ajouter au registre d'homonymie (proposition ISO-a).
3. « Le passage a la valeur moyenne. » NOTE-92 traite une source classique par mode de Fourier ; un etat statistiquement homogene n'a pas de mode e^{ikx} en moyenne. Les fluctuations de ⟨T⟩ (bruit stochastique) ne sont pas traitees : reserve nommee.
4. « De Sitter jusqu'a 𝓘⁺. » S2 ne suit pas a → ∞ ; la croissance en a^{2β̃} n'y est pas bornee (§3, I-4) ; la valeur de κ_k reste d'ordre un selon (4.14), mais ce point n'est pas verifie a l'infini.

## 7. Greffes proposees (non entees)
- **ISO-a** : registre d'homonymie : « Ω (Benevides-Dabholkar-Kobayashi 2018) = facteur de Weyl, ln a ; Ω (corpus, Friedrich) = facteur conforme, 1/a ».
- **ISO-b** : specification de CCC + M (S27-02 §C) : ajouter (v) « contenu electromagnetique quantique statistiquement isotrope a 𝓘⁺ ; champs classiques coherents non couverts » (NOTE-92, NOTE-96).

## 8. Non-surclassement
[conv], lecture d'une source en appui, non auditee a froid. RG-4 inchangee. CCC + M : hypothese ouverte. Noyau {A4 ; A2★ ; N} inchange.
