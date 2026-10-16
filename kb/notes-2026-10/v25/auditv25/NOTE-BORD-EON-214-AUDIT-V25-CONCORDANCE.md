---
id: NOTE-BORD-EON-214-AUDIT-V25-CONCORDANCE
numero: 214
serie: I
branche: Chantier D (audit v2.5)
reservation: 2026-10-16T15:48:49Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 214)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-213-ARMEMENT-AUDIT-V25.md (sceau NOTE-212-213-SCEAU.txt, 2026-10-16T15:55:19Z, pose avant lancement)"
rapports: "RAPPORT-VA1.md, RAPPORT-VA2.md, work_va1/, work_va2/ (empreintes au sceau NOTE-214-SCEAU.txt)"
---

# Concordance de l'audit v2.5

## 0. Deroulement
VA-1 (verification independante, article seul, scripts sympy et numeriques propres) et VA-2 (adverse, 21 references verifiees par outil sur le texte des articles). Agents isoles, sans interruption.

## 1. Constats concordants (trouves par les deux)
| Constat | VA-1 | VA-2 | Correction appliquee (v2.5 corrigee) |
|---|---|---|---|
| Remarque 1 : « interference presente si et seulement si » faux (X = 1 : aucun terme ; X = beta : ordre Omega) | E1 | C1.6 | « can be present only if », ordre Omega pour beta |
| §5 contre Remarque 2(4) : cas k = 0 (deux exposants, source nulle) | E2 | E3.2 | « for every solution with k non nul » |
| Regle de « regularite formelle » qui « distingue les deux classes » : faux (la regularite formelle porte sur les inconnues ; l'equation de Dirac reste singuliere pour les deux classes) | E3 (Def. 1(c) contre Rem. 2(1)) | E3.1 | §5 : regle sur les **sources geometriques** ; l'equation de Dirac rejette les deux classes ; Rem. 2(4) marquee « statement on solutions » ; §4.3 : le point singulier regulier ajoute a ce qui ne depend pas du poids |
| Composantes en poids poussiere : tau_0a sans interference ; c'est tau_ab/Omega qui oscille ; preciser le repere | C5 | E3.3 | paragraphe reecrit, repere orthonormal physique |
| Exemple m proportionnel a Omega^{1/2} vrai seulement sur de Sitter | C10 | E1.3 | « on de Sitter space (m proportionnel a e^{-Ht/2}) » |
| Prop. 3, reciproque (borne si coefficient nul) non prouvee hors de Sitter ; « pole simple » non defini | C1 | C1.2 | definition du pole simple (Def. 1) ; Prop. 3 enoncee sur de Sitter, preuve completee, reserve FLRW |
| Paquet a support compact dans l'image de 1 - P : incompatible en general (Hegerfeldt) | C6 | C1.4 | f = (1-P)g / norme, g a donnees a support compact ; condition integrale de k \|f\|^2 ; Plancherel en base d'helicite |
| Prop. 5(b) plus forte que le prouve (variable mass, etat autre que BD, ponctuel) | C11 | C3.5 | (b) reecrite : version classique (\|chi0+\| different de \|chi0-\|) ; version quantique restreinte (masse constante, de Sitter, BD, integree) ; terme du vide signale |
| Chapeau de la Rem. 2(2) et 2(3) (xi R-chapeau) | C12 | C4.1, C4.2 | T[psi;g] = Omega^2 T[psi-chapeau; g-chapeau] ; xi R physique |
| Lissite en eta ou en Omega | C2 | C4.6 | Def. 1 : variable precisee ; Prop. 4(c) en Omega |
| Normalisation P_+-(0) a une phase pres | C3(i) | C1.6 | ajoute |

## 2. Constats d'un seul auditeur, retenus apres verification
- **VA-1 C9** : masse effective du Lemme 2 : m_eff^2 = (m^2 + m_5^2)/(Z_1^2 - Z_2^2), avec un reechelonnement chiral non unitaire ; preuve corrigee.
- **VA-1 C8** : termes nabla psi-bar sigma nabla psi (et gamma_5) absents de l'annexe ; ajoutes et reduits a des masses constantes (identite de Ricci).
- **VA-1 C3(ii)-(iii)** : argument de la Rem. 1 sur les transformations V remplace par un argument direct (convergence) et par la preuve pour V independant de k.
- **VA-1 C4** : signes de la Prop. 3 pour m > 0 ; cas symetrique chi0+ = 0 de la Prop. 2(c) ; potentiel non integrable sur tout FLRW.
- **VA-1 C7** : « autre etat » : invariance par translation et diagonalite en helicite requises.
- **VA-1 C11 (c)** : Prop. 5(c) restreinte a de Sitter exact pour le Lemme 2 ; ailleurs, Prop. 4.
- **VA-2 E1.4** : resume (i) : « On de Sitter space » pour le point singulier regulier.
- **VA-2 E2.1** : Gurzadyan-Penrose cite au niveau [titre] : l'enonce est attribue a Markwell-Stevens, « after » GP.
- **VA-2 E2.2** : Birrell-Davies retire de la phrase sur le facteur de paires (non lu a ce niveau).
- **VA-2 E2.3** : Markwell-Stevens : « list ... among the controversial assumptions ... that they do not address ».
- **VA-2 E2.4** : Meissner-Penrose : lissite conforme sauf aux points de Hawking.
- **VA-2 C2.5, C2.6** : Allen-Lutken pour la symetrie maximale, DFMR Prop. 4.5 pour Hadamard ; « for every prescription satisfying Wald's axioms ».
- **VA-2 K2.1** : la conclusion d'Ibison (une seule composante atteint le bord) vaut a e^{-2 pi m/H} pres pour les modes de frequence positive ; signale dans « Related work ».
- **VA-2 E5.1, E5.2, C5.3, C5.4, K5.5, K5.6** : note compagnon : W,Z en suffisance ; transposition de la jauge « non tentee » (et non « ne se transpose pas ») ; equations (3.3)-(3.6) de Friedrich 2017 ; verifications de l'auditeur distinguees du script ; RJ v2 « corrige, non re-audite » ; notations chi0+-, H_Lambda.
- **VA-2 E6.1** : remarque LambdaCDM retablie (masse effective en a^{-3} satisfaisant les trois conditions de la Prop. 4 : issue ajustee, non exclue).
- **VA-2 K6.2, K6.3, K6.5** : Majorana nues singulieres (poids -1), presence de quanta de Dirac pres de scri, reserves de la section Verification, phrase sur m/H instantane : retablies.
- **VA-2 C4.3** : fonction de jauge renommee varsigma (conflit avec la constante cosmologique).
- **VA-2 E7.1, E7.2** : P = projecteur de la fonction a deux points (sous-espace occupe) ; convention des frequences a scri moins explicitee.
- **VA-2 E1.1** : explicitations standard signalees comme telles (Provenance).
- **VA-2 C1.3** : dirac_scri_check_v2_1.py = calculs de v2 avec docstring corrigee, meme sortie : dit dans Verification.

## 3. Constats non appliques ou reportes
- VA-2 C1.1 (« croissant a terme » du gel remplace par a -> infini) : ecart benin, aucune preuve n'utilise la monotonie ; declare ici.
- VA-2 K6.4 (verification numerique du facteur a cinq chiffres) : VA-1 l'a refaite (ecart relatif <= 7e-7 pour m/H <= 1) ; non reintroduite dans l'article, la reference suffit.
- VA-2 K6.6 (historique detaille des audits anterieurs) : resume conserve.
- VA-1 R9 (« Proposition 5 » non titree) : formel, inchange.

## 4. Verdict
**AU-V3** au sens strict du gel : plusieurs enonces faux tels qu'ecrits, confirmes par les deux auditeurs independamment (§1, trois premieres lignes) et des attributions au-dela du niveau de lecture (§2). Aucun ne touche les preuves des Prop. 1 a 4, le Lemme 2 ou le noyau ; tous sont corriges localement dans la v2.5 corrigee. **Prediction AU-V2 non realisee.** Entee suspendue ; le precedent (xvi bis) ne couvre pas un enonce d'article. Decision de l'operateur requise.

## 5. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. Noyau {A4 ; A2★ ; N} inchange.

## 6. Re-audit court VA-3 (ajout du 2026-10-16, apres decision de l'operateur « Re-audit court »)
Consigne PROMPT-REAUDIT-VA3.md scellee avant lancement (REAUDIT-VA3-SCEAU.txt, 2026-10-16T16:12:13Z), sur les versions corrigees `6caa5ab5db49e75c` (article) et `76250e99127c2ed2` (note). Agent isole, adverse, limite aux corrections. Rapport RAPPORT-VA3.md (`4beed89cfa9dff27`), work_va3/.

### 6.1 Verdict VA-3
- Article : toutes les corrections des §1 et §2 appliquees et justes ; calculs confirmes (m_eff, s^2, reduction sigma par Ricci sur de Sitter, Rem. 1, borne Prop. 3, Plancherel, conditions Prop. 4 pour LambdaCDM au signe pres). Aucune erreur restante parmi les points audites.
- Note compagnon : **une erreur residuelle E-1** (resume : « bounded without limit otherwise », faux pour k = 0), residu du constat concordant E2/E3.2.
- Corrections C-1 a C-6, remarques R-1 a R-8. Apres E-1 et C-1 a C-6, « entable sans nouvel audit ».

### 6.2 Traitement (diff complet : DIFF-POST-VA3-ARTICLE.txt `1eaa00e859cda4b9`, DIFF-POST-VA3-COMPANION.txt `8583303a6d9c43d1`)
Les versions vues par VA-3 ont ete reconstruites par inversion exacte des retouches (ARTICLE-v2.5-vu-VA3.tex, COMPANION-vu-VA3.tex) et retombent sur les empreintes scellees : le diff ne contient donc aucune modification hors liste.

| Constat VA-3 | Traitement |
|---|---|
| E-1 (note, resume et tableau) | « zero for k = 0, bounded without limit for solutions with both exponents and k non nul » ; ligne du tableau « both exponents, k non nul » |
| C-1 (LambdaCDM surclasse) | « not excluded by the conditions of Proposition 4 » ; m_eff proportionnel a (1+z)^3 pendant l'ere de matiere ; « not regarded as a viable option ». Ecart volontaire : l'exclusion observationnelle n'est pas affirmee, les bornes sur m_e n'ayant pas ete consultees dans ce chantier (« compatibility not examined here ») |
| C-2 (signe de m_eff) | parenthese : psi -> gamma_5 psi renverse le signe ; conditions sur \|m_eff\| |
| C-3 (annexe) | forme nabla psi-bar Gamma nabla psi ajoutee a la premiere phrase |
| C-4 (introduction) | « and, for a test field, the behaviour of the geometric sources on solutions » |
| C-5 (note, regularite formelle) | alignee sur la Def. 1(c) : « depend smoothly on Omega up to Omega = 0 » |
| C-6 (note, connexion de spin) | « the two auditors of this computation, RA-1 and RA-2 » : verifie sur RAPPORT-RA1.md (l. 92) et RAPPORT-RA2.md (l. 42-44), les deux derivent l'annulation |
| R-1 | \|theta\| -> infini, m > 0 sans perte |
| R-2 | « automatic for f = (1-P)g as above » |
| R-3 | facteur i sur le terme sigma (anti-hermitien sinon), « real as written » ; convention psi_L = (1-gamma_5)/2 psi |
| R-4 | « relative weight » |
| R-5 | « (3.7) being the Weyl equation treated above » : verifie sur NOTE-207 v2 (l. 46, 62) |
| R-6 | « has a limit » (trois occurrences), avec la precision serie entiere / continue non C^1 |
| R-7 | phrase de Provenance sur l'audit et le re-audit de la v2.5 ; note et Rem. 2 : « audited », script RJ v2 non re-audite. L'etiquette de version reste 2.5 (la version auditee n'a jamais ete diffusee) |
| R-8 | K6.5 retablie (« Proposition 1 alone … would not justify the next statement ») ; K6.2 retablie dans le perimetre (mecanisme amenant le Higgs au point m_h^2 + 4 lambda xi = 2 lambda/3) |
| hors constat | tableau final de la note en \footnotesize et ligne coupee (debordement LaTeX de 93 pt) ; aucune modification de contenu |

### 6.3 Statut
Les corrections sont locales ; aucune ne touche une preuve. Conformement au verdict VA-3, pas de nouvel audit complet. Le §2 ligne « K6.2, K6.3, K6.5 : retablies » est exact apres le present traitement (il ne l'etait pas pour la version vue par VA-3).
