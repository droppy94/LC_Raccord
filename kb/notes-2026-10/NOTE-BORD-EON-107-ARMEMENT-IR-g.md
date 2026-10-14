---
id: NOTE-BORD-EON-107-ARMEMENT-IR-g
numero: 107
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-g)
reservation: 2026-10-11T13:49 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 107)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-106-AUDIT-OP-IR-CONCORDANCE, NOTE-BORD-EON-102-OP-IR-EXECUTION, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
sources: ["aucune nouvelle source ; S2 et [21] deja lus (NOTE-96, NOTE-104)"]
issue_attendue: "delimitation"
rouvre_si:
  - "source persistante jusqu'a scri+ (courants classiques de charges sans masse) ou champ longitudinal (charges nettes)"
  - "retroaction, ordres superieurs en beta, etat non conforme"
---

# NOTE-107 : armement de IR-g. Un champ coherent d'origine causale reste-t-il a dominante magnetique a 𝓘⁺ ?

## 0. Origine
NOTE-106 (AU-V2) etablit que le ln a du secteur Maxwell isotrope est proportionnel a ⟨F²⟩ = 2(⟨B²⟩ − ⟨E²⟩) a 𝓘⁺, et que pour des poids E et B egaux il disparait **apres moyenne sur les directions**. La question est donc : quel etat a 𝓘⁺ produit une source causale ?

## 1. Cadre (fige)
- Repere conforme : Maxwell plat sur η < 0, 𝓘⁺ = {η = 0}, s = −η. Au premier ordre en β, la dynamique de β = 0 fixe l'etat ; β ne fait que ponderer.
- Pres de 𝓘⁺, tout mode de k fini est hors horizon (ks → 0) : u(s) = u(0) + u'(0) s + … ; la partie u(0) est **magnetique** (branche gelee), la partie u'(0) **electrique**. On note B_i(x), E_i(x) les champs du repere conforme sur la tranche η = 0.
- Modele de source causale : courant transverse localise, actif jusqu'a η_off < 0 puis eteint ; D = |η_off| ; le produit kD est le rapport k_phys/H au moment de l'extinction (mode sous-Hubble si kD > 1). Etat initial a l'extinction : configuration magnetostatique (u(η_off) = a, u'(η_off) = 0), puis evolution libre jusqu'a η = 0.
- Spectre de la source : P(k) ∝ kⁿ e^{−k/k⋆} (forme de controle ; n laisse libre, la causalite imposant un spectre bleu a petit k).
- Source coherente localisee : dipole magnetique m (courant J_k ∝ i k × m) ; ensemble de sources d'orientations aleatoires isotropes pour comparaison.
- Objet calcule : la partie logarithmique de X^M au premier ordre et sa traduction dans (2.17) (fermeture C-iso pour la partie homogene, comme NOTE-98/102).

## 2. Sous-questions
- **G-1** : quelle combinaison de B et E a 𝓘⁺ porte le terme β ln s de X^M (composante par composante, y compris les termes croises de Poynting) ? Le ln de (2.17) vient-il de la trace (⟨F²⟩) ou de la partie sans trace ?
- **G-2** : dans le modele de coupure, comment ⟨F²⟩ et la partie sans trace dependent-ils de kD ? Que donne la moyenne spectrale pour kD ≫ 1 (emission sous-Hubble) ?
- **G-3** : pour une source dipolaire coherente unique, la partie pertinente survit-elle apres moyenne sur les directions de k ? Et pour un ensemble isotrope de sources ?
- **G-4** : la dichotomie « dominante magnetique / E = B » est-elle le bon critere pour l'existence du ln Ω ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **G-V1** | Un champ coherent d'origine causale reste a dominante magnetique a 𝓘⁺ (⟨F²⟩ > 0 de facon robuste) : le ln Ω existe. |
| **G-V2** | Il tend vers E = B et le ln Ω disparait (trace et partie sans trace). |
| **G-V3** | Delimitation : la reponse depend de kD (passage de Hubble a l'extinction) et/ou de la structure de polarisation ; ni G-V1 ni G-V2 en general. |
| **G-V0** | Question mal posee : le critere « magnetique / E = B » n'est pas celui qui decide du ln Ω (objet decisif a nommer). |

Composites permis (un verdict principal, une qualification).

## 4. Prediction declaree (anti-fit)
**G-V0 qualifie G-V3** : le terme logarithmique est porte par le tenseur Q_ij = B_iB_j − E_iE_j a 𝓘⁺ (Poynting sans log) ; le ln de (2.17) vient de sa partie sans trace. Sa trace (⟨F²⟩) oscille en cos(2kD) et se moyenne vers 0, en loi de puissance de k⋆D, pour une emission sous-Hubble ; sa partie sans trace survit pour un champ coherent polarise (non nulle pour un dipole unique) et ne s'annule que pour un ensemble isotrope non polarise. « E = B » en module ne suffit donc pas a supprimer le ln Ω.

## 5. Instruments prevus
Script `ir_g.py` (sympy), empreinte avant execution. Audit froid propose ensuite (non engage).

## 6. Non-surclassement
Premier ordre en β, fond fixe, cadre S2 + [21], champs charges conformes, vide conforme. Noyau {A4 ; A2★ ; N} inchange. RG-4 non concernee.
