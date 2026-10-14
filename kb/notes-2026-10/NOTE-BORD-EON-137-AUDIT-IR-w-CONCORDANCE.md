---
id: NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE
numero: 137
serie: I
branche: Q-M3 suite (IR-w, audit)
reservation: 2026-10-12T12:50 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 137)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-136-ARMEMENT-AUDIT-IR-w (sha256 ee3442bb395f5d6fb22bb482e20a4e1b30ffc9127650205fe7566039fc02813c, sceau 2026-10-12T12:51:35Z)
rapports:
  - "audit_irw/RAPPORT-IR-w-Wa.md, sha256 3c72021ef7f93e5d8d64cf07fac533cf25841b3041ac230f56fe7a8be72390e1 (recalcul aveugle, normalisation et signe)"
  - "audit_irw/RAPPORT-IR-w-Wb.md, sha256 ac91dc7a9d58bdb2bc832c00cea6c154425c3c492aa42ff262530af65e1e77fc (lecture aveugle des sources)"
  - "audit_irw/RAPPORT-IR-w-Wc.md, sha256 2d0d1cb24e0dbe5e50149803684433b23615657c5525efc502ebff4838571676 (audit de NOTE-131)"
objet: [NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-133-IR-u-EXECUTION, NOTE-BORD-EON-135-IR-v-EXECUTION]
verdict: "W-V1"
prediction_realisee: "oui, a une reserve pres (iii)"
rouvre_si:
  - "solutions homogenes de □² singulieres sur le cone de lumiere (ln(r² − s²), 1/(r² − s²)) admises par les conditions de bord physiques de φ_h (point ouvert releve par W-c)"
  - "secteurs b'E, □R et partie non locale reexamines hors des hypotheses de NOTE-131 (reserve de W-a)"
---

# NOTE-137 : concordance de l'audit froid aveugle IR-w. Conversion, signe et NOTE-131 confirmes. Verdict **W-V1**

## 0. Resume
Trois auditeurs isoles, sans acces aux notes 123 a 135, ont rendu leur rapport. Les quatre criteres figes au gel sont satisfaits.
- **W-a** retrouve, depuis la seule trace anomale et la convention lorentzienne ⟨T_ab⟩ = −(2/√−g)δW/δg^{ab}, **Γ = 64πGb = 8bκ** (κ = 8πG), soit G/(30π) par scalaire conforme, avec un **Weyl rescale croissant**.
- **W-b** retrouve dans les sources **n = 8** pour les trois champs, au premier ordre et pour l'exposant resomme, et explique pourquoi : le contre-terme de Weyl de Woodard est egal a b.
- **W-c** juge t-1, t-2, t-3 de NOTE-131 **valides sous hypotheses** ; aucun defaut de fond dans les scripts.

## 1. Confrontation aux criteres (figes, NOTE-136 §2)
| Critere | Exigence | Resultat | Statut |
|---|---|---|---|
| **C-1 (module)** | \|Γ\| = 8bκ, valeur exacte | W-a : Γ = 64πGb = 8bκ, par serie et par solution exacte (Ci, Si) [calcule par l'auditeur] | **satisfait** |
| **C-2 (signe)** | Weyl rescale croissant, convention physique | W-a : terme local W ⊃ +b∫√−g σC², T_ab = −8b ∂^c∂^d(σC_acbd), Γ > 0, croissance [derive + calcule par l'auditeur] | **satisfait** |
| **C-3 (sources)** | n = 8 pour trois champs ; transposabilite au Weyl rescale | W-b : n = 8 (scalaire, Dirac, photon), S1 et S2 concordants ; facteur relatif transposable, W^tree fini en 𝓘⁺ [extrait + calcule + derive par l'auditeur] | **satisfait** |
| **C-4 (NOTE-131)** | t-1, t-2, t-3 valides | W-c : t-1 valide sous hypotheses (deux implementations, toutes composantes) ; t-2 valide, enonce a preciser ; t-3 (a) valide, (b) valide sous hypothese de regularite | **satisfait** |

## 2. Points de detail des rapports
### 2.1 W-a [rapporte]
- Coefficient du terme local : **+b**, sans facteur 2 ; controle √−ĝĈ² = √−g C² a l'ordre ε².
- T̂_yy[u₀] = 4bk³ s (A sin ks − B cos ks) = 8b C_sysy[u₀], sans ln s. C'est l'oppose exact du resultat de NOTE-133 en convention de calcul c₀ = +8 : la convention physique est bien c₀ = −8, comme NOTE-133 l'affirmait.
- Mecanisme : le log vient d'une **resonance** entre une source ∝ s et la solution homogene en s³, non du σ explicite (le terme en σ s'annule sur u₀, Bach nul). Concorde avec NOTE-125 (R-E).
- La donnee A ne produit de log **a aucun ordre** en s (NOTE-133 l'avait etabli a l'ordre s⁰ seulement).
- Independance en k : le log est en ln(Hs), pas en ln(ks).
- Reserve : seul le terme σC² est inclus ; les secteurs b'E, □R et la partie non locale pourraient ajouter des logs du meme ordre.

### 2.2 W-b [rapporte]
- Conventions des sources : κ_W² = 16πG ; h perturbe la metrique rescalee g̃ = a⁻²g ; C^tree ∝ a⁻¹, d'ou W = a C̃ → constante finie a l'arbre, et divergence a une boucle.
- Raison structurelle de n = 8 : c₂(Woodard) = b(HHR), δZ = −4c₂κ_W²H², Γ = −2γ = 8bκH².
- Coquilles internes a S2 (eq. 153, 57, titre §4.2.2, c₁ du MMC), sans effet sur n pour les trois champs conformes.
- Reserve : la limite a → ∞ extrapole hors du domaine enonce (« as long as the de Sitter phase persists », logarithmes dominants).

### 2.3 W-c [rapporte]
- t-1 : T̂ = 6ĝ pour **toutes** les composantes (ss, sx, xx, yy, zz), au fond et a l'ordre ε ; le controle −½ discrimine au fond et a l'ordre ε.
- t-2 : pour p = 2, l'absence de pole tient des que Y et ∂Y sont bornes ; **ni la conservation ni la trace nulle ne sont necessaires**. Pour p = 1, pole si et seulement si Y(0) ≠ 0.
- t-3 : aucun mode homogene de □² singulier **uniforme** en s ; mais des solutions singulieres **portees par le cone de lumiere** (1/(r² − s²), s/(r² − s²), ln(r² − s²)) existent ; exclues par l'hypothese de regularite, leur effet sur R n'a pas ete calcule. **Point ouvert.**

## 3. Lecture [derive]
1. La conversion sur laquelle reposait la chaine (NOTE-136 §0) est confirmee par une derivation de bout en bout qui ne passe ni par la litterature ni par la convention c₀ du gel de NOTE-124 : le module (8bκ) et le signe (croissance) sont etablis a l'aveugle.
2. La concordance avec Foraci-Litos-Woodard et Woodard 2025 n'est pas une coincidence numerique : W-b identifie l'egalite c₂ = b qui la rend structurelle.
3. La reserve de W-a sur les autres secteurs est celle que NOTE-131 traitait (partie a = 6aĝ, partie non locale reguliere sous hypothese d'etat) ; W-c confirme ces resultats. Elle reste une hypothese de classe, non une lacune nouvelle.
4. Le point ouvert de W-c (solutions de cone) touche l'hypothese d'etat de NOTE-131 : un φ_h portant une singularite sur un cone de lumiere correspond a un etat non regulier ; il est a instruire avant toute gravure.

```
   chaine G-V3 apres IR-w
   ───────────────────────────────────────────────────────────────
   pole de (2.17)        NOTE-125 v2, retrouve a l'aveugle (NOTE-128)
   non compense          NOTE-131, confirme a l'aveugle (W-c)
   gamma = 8, croissance NOTE-133, recalcule a l'aveugle (W-a)
   litterature n = 8     NOTE-133/135, relu a l'aveugle (W-b)
   resomme Omega^-8bkH2  NOTE-135 (prescription, logs dominants)
   ───────────────────────────────────────────────────────────────
   ouvert : solutions de cone de phi_h ; autres secteurs hors classe
```

## 4. Verdict
**W-V1.** C-1 a C-4 satisfaits. Conversion des normalisations, signe physique et NOTE-131 confirmes a l'aveugle. G-V3 consolide au premier ordre et sous la prescription de resommation.

## 5. Confrontation a la prediction
Prediction (NOTE-136 §4) : W-V1 [**realise**] ; (i) ambiguite de signe signalee et tranchee vers la croissance [**realise**] ; (ii) caractere de prescription de la resommation releve [**realise**] ; (iii) t-2 reposant sur la conservation et la trace nulle [**non realise** : W-c montre que la regularite suffit, la conservation et la trace ne sont pas necessaires] ; risque d'un facteur de normalisation (C-1) [**non materialise**].

## 6. Consequences
- **Aucune correction requise** de NOTE-131, 133 ou 135. Precisions a porter lors d'une eventuelle version v2 (sans urgence) :
  - NOTE-131 t-2 : remplacer « sans trace, conserve » par « Y et ∂Y bornes en s = 0 » comme hypothese suffisante ;
  - NOTE-133 : « A ne produit de log a aucun ordre en s » (W-a) ; mecanisme de resonance ;
  - NOTE-133/135 : signe physique etabli (c₀ = −8, W ⊃ +b∫σC²), non plus seulement suppose.
- **Point ouvert nouveau** : solutions de cone de □² pour φ_h ; leur admissibilite et leur effet sur R.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 restent des candidats non graves : la gravure releve d'un acte de l'operateur.

## 7. Pistes
- **Acte** de libelle de G-V3 (NOTE-133 §6, NOTE-135 §6) et de la convention de signe physique, avec reexamen explicite de la convention lisse face a un exposant ~10⁻¹²².
- **IR-x** : instruction des solutions de cone de φ_h (admissibilite, effet sur R).
- Lecture de Foraci-Woodard 2501.01972 (source primaire des resommations), sous gel.

## 8. Non-surclassement
[conv]. Audit par agents isoles du meme systeme : independance de chaine, non independance humaine. Premier ordre, fond de Sitter, classe « WZ integrable + Γ[g] etat regulier + φ_h lisse ».
