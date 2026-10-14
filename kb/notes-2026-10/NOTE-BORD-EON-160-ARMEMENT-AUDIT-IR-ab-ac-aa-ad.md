---
id: NOTE-BORD-EON-160-ARMEMENT-AUDIT-IR-ab-ac-aa-ad
numero: 160
serie: I
branche: Q-M3 suite (audit IR-ab, IR-ac, IR-aa, IR-ad)
reservation: 2026-10-13T11:30 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 160)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (consignes aveugles, criteres, espace des verdicts et prediction figes AVANT le lancement des auditeurs)
decision: operateur (Thierry), 2026-10-13 13:23 heure de Paris (« ok pour realiser en sequence audit froid aveugle conjoint de 153/155/157/159, puis greffes NOTE-146 v3 et NOTE-138 v4, puis mise a jour de la presentation »)
objet: [NOTE-BORD-EON-153-IR-ab-LECTURE-2412.11022-2405.01024, NOTE-BORD-EON-155-IR-ac-LECTURE-FNW-RADZIKOWSKI, NOTE-BORD-EON-157-IR-aa-EXECUTION, NOTE-BORD-EON-159-IR-ad-PASSE-ADIABATIQUE-EXECUTION]
consignes:
  - "PROMPT-AVEUGLE-ABA1-LECTURE-2412.11022-2405.01024.md, sha256 aed3b9aca4981f9713a713821a01e1f45c2cb9a43692c3efccd168b7a99296a1"
  - "PROMPT-AVEUGLE-ACA1-ENONCES-HADAMARD.md, sha256 cfc13224c6384baa703a696774f128032c4f8efd707627c40f3eedf3c95726d1"
  - "PROMPT-AVEUGLE-AAA1-TENSEUR-ANISOTROPE.md, sha256 15fabbc0e5bc62e2a3d8f1a35c298ede6aeb17c2aab3efe243625c39e3b3a5dd"
  - "PROMPT-AVEUGLE-AAA2-SCRIPT.md, sha256 9867bb4b1f10335dead00fd8f59c4948be3d3fb81c561a490b1234bd7fb27098 (fichier fourni : iraa_aniso_v2.py c3a30a362ea2d7f2)"
  - "PROMPT-AVEUGLE-ADA1-NOYAU-RETARDE.md, sha256 333acea94f39d3b71ca294aa53b1e3dd256947c203079694337c7aa8232e01e4"
  - "PROMPT-AVEUGLE-ADA2-SCRIPT.md, sha256 3a80e08e2d88df9dc1e272bd6c4714da26509383313d0742a33d6f4987f576ae (fichier fourni : irad_kernel.py 3d5d52115b2839df)"
---

# NOTE-160 : armement de l'audit froid aveugle conjoint de NOTE-153 (IR-ab), 155 (IR-ac), 157 (IR-aa) et 159 (IR-ad)

## 1. Dispositif (fige)
Six auditeurs isoles, en parallele, sans acces aux notes, au registre ni aux dossiers de travail (dossiers /home/claude/audit_p1/<id>/ ; seuls les auditeurs de script recoivent le script audite) :
- **ABA-1** (lecture aveugle) : [8] 2412.11022 et [27] 2405.01024 ; coefficient du photon, contribution non locale sur le mode de de Sitter, deux sources de logarithmes, δZ, γ, Callan-Symanzik, phrases de reserve (course de G, attribution des contre-termes), statut (prouve / verifie / compare), absences ; conversion n × bκ_P²H².
- **ACA-1** (lecture aveugle) : Khavkine-Moretti 1412.5945 (Def. 15, Th. 9, Prop. 16, Rem. 23), Sanders 0903.1021 (Prop. 2.8, 4.1, Lemma 2.9, 4.6) ; role de la positivite dans la propagation et dans l'equivalence ; lacune de Radzikowski et son comblement ; attribution du theoreme de propagation ; application au demi-espace ; invariance conforme ; metadonnees Springer.
- **AAA-1** (cecite stricte) : tenseur ameliore du scalaire conforme sur un bimode, structures de phase |β|² et αβ*, decomposition, cas isotrope et anisotrope, exposant radial, cone reflechi et anisotropie, comptage s².
- **AAA-2** : audit de iraa_aniso_v2.py (seul fichier fourni), reproduction independante, controle numerique N = 3, contre-exemples.
- **ADA-1** (cecite stricte) : Bach linearise ∝ □²h, modes de de Sitter et (∂² + k²)²u = 0, noyau K_k(T), reponse adiabatique et sa limite, emission finie et lissite en τ = 0, condition de convergence, comptage s².
- **ADA-2** : audit de irad_kernel.py (seul fichier fourni), reproduction de ad-1 et ad-3 symboliques, robustesse de la regularisation de la partie finie (ad-3) et des differences finies (ad-4).

## 2. Criteres (figes)
- **C-1 (153, ab-1, ab-2)** : ABA-1 retrouve le coefficient du photon (n = 8), γ = −κ_W²H²/(80π²) depuis c₂, exposant = −2γ, γ_MMC = 3GH²/(20π) ; δZ = D[2(D−1)c₁ − c₂]κ²H².
- **C-2 (153, ab-3, ab-4, ab-6)** : ABA-1 releve l'appariement ln μ / ln a (eq. 5/6), les deux sources de logarithmes et l'absence de queue du photon, l'absence de verification a deux boucles, et les deux reserves de [27] (course de G ignoree ; attribution « convenient ») ; releve « the nonlocal contribution vanishes » et l'identite (∂₀ + ik)²∂₀u₀ = 0 ; « endless phase of de Sitter ».
- **C-3 (155, ac-1, ac-2, ac-3)** : ACA-1 retrouve : propagation (Prop. 16 (b), Rem. 23) sans positivite ; equivalence et lissite de la difference (Th. 9) pour des etats ; lacune de Radzikowski Th. 5.1 comblee par Sahlmann-Verch 2001 (et S1) ; attribution de la propagation a Fulling-Sweeny-Wald 1978 ([24]).
- **C-4 (155, ac-4)** : ACA-1 reconstruit l'application au demi-espace avec la positivite au seul pas d'equivalence / difference (prolongement de Cauchy positif) ; aucune hypothese supplementaire au-dela de « le prolongement est l'etat de memes donnees de Cauchy ».
- **C-5 (157, aa-1, aa-2)** : AAA-1 et AAA-2 retrouvent, pour le terme αβ* : T₀₀ = T₀ᵢ = 0, T_ij ∝ e^(−2ikη)(k_i k_j − ⅓k²δ_ij) (trace nulle, partie isotrope nulle) ; |β|² independant de η ; I(η) ~ |η|^(N−4), 1/η pour N = 3, entiere pour gaussienne ; AAA-2 releve que l'annotation « attendu −1/2 » est fausse de signe (valeur η·I → +1/2).
- **C-6 (157, aa-3, aa-5)** : AAA-1 retrouve que l'anisotropie (multiplicateur homogene de degre 0) ne change pas le critere du cone reflechi ; AAA-2 ne trouve aucun contre-exemple (1/η avec decroissance rapide).
- **C-7 (159, ad-1, ad-2, ad-3 symbolique)** : ADA-1 et ADA-2 retrouvent B = −¼□²h, (∂² + k²)²u = 0 pour les deux modes, B_ε = ∓8εk³e^(ετ)(sin, cos) + O(ε²), noyau −2[θcos(kT)/T]₊ + local.
- **C-8 (159, ad-3 numerique, ad-4)** : ADA-1 trouve R_ε → 0 (avec sa propre regularisation) ; ADA-2 confirme la robustesse de R_ε → 0 a l'echelle de la partie finie ; ADA-1 et ADA-2 trouvent R lisse en τ = 0, finie, non nulle, dependante de τ₀ pour l'emission finie.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Criteres de la note satisfaits sans correction : note confirmee. |
| **AU-V2** | Criteres satisfaits avec corrections de detail ou precisions (annotation, attribution, hypothese a expliciter, regularisation a declarer) : greffe v2 proposee, verdict de la note inchange. |
| **AU-V3** | Un critere porteur echoue (coefficient different ; propagation exigeant la positivite au sens ou y-3 serait incomplet ; contre-exemple Hadamard a 1/η ; R_ε ne tendant pas vers 0 ou R non lisse) : verdict de la note a reexaminer. |
| **AU-V0** | Audit inexploitable (a nommer), relance. |

Un verdict par note ; composites permis.

## 4. Prediction declaree (anti-fit)
**AU-V1 pour 153 ; AU-V2 pour 155 ; AU-V2 pour 157 ; AU-V2 pour 159.**
- ABA-1 retrouvera C-1 et C-2 ; il pourra relever une reserve supplementaire de [27] non notee par 153 (par exemple l'extension conservee (69) « by no means unique », hors cadre) ou noter que [8] n'est qu'une prepublication.
- ACA-1 retrouvera C-3 et C-4 ; precision probable : la Prop. 16 est enoncee pour un etat « with ω₂ ∈ D′ » mais sa preuve n'utilise que la bisolution (Rem. 23) ; il pourra relever que [70] de S1 (non lu) est la seconde reference de propagation, et que l'application au demi-espace suppose que le demi-espace soit globalement hyperbolique comme espace-temps (vrai) : precisions a porter en v2 de 155.
- AAA-1 retrouvera C-5 et C-6 ; AAA-2 relevera la coquille de signe de l'annotation et pourra relever que le script n'imprime pas la mesure 1/(2k(2π)³) ni ne verifie la conservation : precisions v2 de 157.
- ADA-1 retrouvera C-7 ; pour C-8, sa valeur de R_ε dependra de sa regularisation mais tendra vers 0 ; ADA-2 relevera que la partie finie « a l'echelle 1 » introduit un terme local ∝ B(τ₀) dependant de l'echelle, lui-meme O(ε), sans effet sur la limite ; il pourra relever que les differences finies sur e^(−1/t) sont bruitees (valeurs ±300) et proposer un calcul symbolique de B sur la transition : precisions v2 de 159, conclusion inchangee.

## 5. Procedure
Dossiers /home/claude/audit_p1/{aba1, aca1, aaa1, aaa2, ada1, ada2} ; rapports sauvegardes avec empreintes ; NOTE-161 confronte les criteres ; aucune correction de 153, 155, 157, 159 avant NOTE-161 ; greffes eventuelles entees par NOTE-162 avec 146 v3 et 138 v4.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v3) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange.
