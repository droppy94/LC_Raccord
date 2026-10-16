---
id: REPRISE-AUTOPORTANTE-2026-10-16-v12-DIRAC-POUSSIERE-ET-COUPLAGE
date: 2026-10-16
heure: 23:50 heure de Paris
programme: LC-RACCORD
destination: projet « deux bords » (piece d'ouverture unique ; remplace la v11 comme point d'entree)
nature: PIECE DE PASSATION autoportante. Reprend la v11 (valide comme piece, §3.1 a §3.6 et §7 non recopies) et ajoute quatre chantiers du 16 octobre : LB (201-205), RJ (206-210), V25 (211-215), RJ2 (216-220), plus le brouillon PSE v2. N'ajoute aucune substance.
grade: "[conv]"
supersede_comme_entree: "01-REPRISE-AUTOPORTANTE-2026-10-16-v11-ANOMALIES-FORMELLES.md (reste valide comme piece)"
dernier_numero_emis: 220
numeros_reserves: aucun
premier_numero_libre: 221
registre_en_vigueur: "REGISTRE-CENTRAL-NUMEROS-NOTES.md (D:\\temporaire, base du projet, archive git)"
depot_git: "github.com/droppy94/LC_Raccord, branche archive/notes-2026-10 ; 0cd4f4c (LB), b5dbf2a (RJ), 3983048 (V25), 81c0897 (RJ2 216-219, PSE v2), puis commit acte 220 + reprise v12"
zenodo: "v1 10.5281/zenodo.22919751 ; v2 10.5281/zenodo.23373604 ; concept 10.5281/zenodo.22919750 ; article v2.5 a deposer par l'operateur le 17 octobre"
---

# Reprise autoportante v12 : l'electron au bord, poids poussiere et couplage complet (16 octobre 2026)

## 0. Procedure d'ouverture (nouvelle discussion)
1. Lire cette piece en entier, puis la v11 pour le detail des resultats anterieurs (§3.1 a §3.6 de la v11, inchanges sauf ce que le §3 ci-dessous corrige).
2. Ouvrir le registre central : derniere ligne emise **220** ; **221 libre**.
3. Aucun audit en suspens : les chantiers LB, RJ, V25, RJ2 sont clos par leurs actes (205, 210, 215, 220).
4. Si la discussion est reliee a l'ordinateur, verifier sur `D:\temporaire` les dossiers `LB\`, `RJ\`, `V25\`, `RJ2\`, `PSE\` (racine) et le registre racine. Empreintes au §7 et aux sceaux.
5. Rappels a l'operateur, une fois chacun : (i) deposer sur Zenodo l'article v2.5 et la note compagnon (Preprint separe, ORCID) ; (ii) reformuler avec ses mots la question PSE (canevas v2) et y mettre le DOI ; (iii) relecteurs humains (v11 §9).
6. Ne rien ecrire de substantiel sans numero reserve au registre.

## 1. Statut de la CCC au 16 octobre 2026, 23h50
| Forme | Statut | Pieces |
|---|---|---|
| CCC, forme actuelle | **Refutee a titre provisoire** (RG-4), raison **resserree** par RJ et RJ2 : (1) le spineur de Dirac n'a pas de limite a scri pour toute masse constante non nulle (point singulier regulier, exposants +- i m/H ; aucune redefinition reguliere ne l'enleve) ; (2) pour une matiere generique (les deux exposants presents, k non nul), la regularite de la geometrie a scri **depend du facteur conforme**, c'est-a-dire de la regle de raccord. Le pole m/Omega de la densite d'energie n'est plus une raison : il appartient au poids radiatif Omega^-4 ; dans le poids poussiere de Friedrich (Omega^-3), la densite a une limite | NOTE-207 v2, 210, 217 v2, 220 ; article v2.5 |
| Classe a un seul exposant | Asymptotiquement que des particules (ou que des antiparticules) : sources geometriques en series entieres ; **preservee par le couplage Einstein-Dirac complet** (formel sous H1, H2 ; perturbatif a epsilon^3, deux calculs independants) ; analogue spinoriel de la poussiere de Friedrich, rho = m psibar psi > 0 ; le spineur garde la phase | NOTE-217 v2, 220 |
| CCC + M | Inchange (v11) : condition unique sur le Higgs m_h^2 + 4 lambda xi = 2 lambda/3 pour le systeme couple classique ; hors reduction : Lambda_QCD, Majorana nue, matiere noire, anomalie de trace | S27-02 v3, v4 |
| G-V3, M-V3 | Inchanges (v11) : candidats formels | NOTE-197 v2, 138 v5, 163 v3 |
| Repli acyclique | Suspendu a A2★ | |
| CCC-T | Non candidate | |
Noyau {A4 ; A2★ ; N} inchange.

## 2. Chronologie du 16 octobre (apres la v11)
```
16 oct.  relecture IA exterieure de l'article v2.4 (traitee comme rapport, precedent xi)
         NOTE-201/202  LB : bibliographie et argument quantique (lecture)
         NOTE-203/204/205  audit AL-1/AL-2 (AU-V3 partiel), NOTE-202 v2, acte, precedent (xvi)
         NOTE-206/207  RJ : regularisation par jauge, poids poussiere (premier etage, champ test)
         NOTE-208/209/210  audit RA-1/RA-2 (AU-V3 partiel : classe a un seul exposant analytique), NOTE-207 v2, acte, precedent (xvi bis)
         NOTE-211/212  V25 : article v2.5 (lots R1 a R4, LB, RJ) et note compagnon
         NOTE-213/214  audit VA-1/VA-2 (AU-V3), corrections ; re-audit court VA-3
         NOTE-215  acte v2.5, precedent (xvii)
         brouillon PSE v2 (canevas aligne sur la v2.5)
         NOTE-216/217  RJ2 : second etage, couplage Einstein-Dirac complet (RJ2-V1 annonce)
         NOTE-218/219  audit RB-1/RB-2 (AU-V3 : geometrie generique), NOTE-217 v2, re-audit court RB-3
         NOTE-220  acte RJ2, precedent (xvi ter)
```

## 3. Resultats porteurs du jour (tous [conv] ; audites par IA isolees ; aucun relu par un humain)

### 3.1 LB (201-205) : bibliographie et argument quantique
- Nouveaute de l'article reduite (Prop. 1, 3, 4) ; sources nouvelles contre-lues : Ibison (une seule composante atteint le bord, a e^{-2 pi m/H} pres), Bachelot, Friedrich 2016 (poussiere), Dappiaggi-Hack-Pinamonti 2010.
- Argument quantique R2 : etat quasi-libre pur Hadamard ; etat de Slater (projecteur P + \|f><f\|, f = (1-P)g normalise) ; axiome 1 de Wald (DHP 0904.0612) ; Bunch-Davies : global Hadamard (DFMR Prop. 4.5), restriction a la carte plate, identification par le bord passe ; energie integree relative a l'etat m tanh(pi m/H) \|f\|^2 (Plancherel en base d'helicite).

### 3.2 RJ (206-210) : poids poussiere, premier etage (champ test sur de Sitter)
- Identite exacte P0 : 2 Omega^-1 nabla-hat_[k L-hat_l]j = (1/2)(nabla_k tau'_lj - nabla_l tau'_kj) + Omega^-1 S_jkl, tau = Omega^-3 T(e,e) ; generalise (3.20) de Friedrich a tout tenseur.
- Noyau P1 : S = 0 si et seulement si tau est proportionnel a n n.
- Dirac : tau_00 = m B + Omega k.J, tau_0a = -Omega k_a N, tau_ab = (Omega/2)(k_a J_b + k_b J_a) ; aucun pole dans les seconds membres du secteur Einstein ; series entieres pour la classe a un seul exposant et k = 0 ; bornes sans limite (phase Omega^{+-2 i m/H}) sinon. L'equation de Dirac reste fuchsienne pour toute inconnue reguliere.

### 3.3 Article v2.5 (211-215)
- Article « dirac-mass-scri » v2.5 (12 p.) et note compagnon « Formal regularity ... : computations » (4 p.) entes. Changements principaux : resume (i) a (iv) recadre ; Def. 1 (notions de regularite, pole simple) ; Prop. 3 sur de Sitter, poids radiatif contre poids poussiere ; argument quantique R2 ; Lemme 2 (m_eff^2 = (m^2 + m_5^2)/(Z_1^2 - Z_2^2), remise a l'echelle chirale) ; Prop. 4 et remarque LambdaCDM (non exclue par les conditions, m_eff proportionnel a (1+z)^3, non retenue comme option viable) ; Rem. 2 (regularite formelle et sources sur solution) ; Prop. 5 (consequences pour CCC comme conditions sur une regle de raccord choisie).
- Audit : AU-V3 (enonces faux tels qu'ecrits, attributions au-dela du niveau de lecture), corrections, re-audit court VA-3 (article sans erreur restante ; une erreur residuelle dans la note, corrigee) ; ecart volontaire sur C-1 (pas d'affirmation d'exclusion observationnelle).

### 3.4 RJ2 (216-220) : second etage, systeme couple
- **Lemmes** (deux derivations independantes) : tau = Omega T_c pour un facteur conforme quelconque ; sur une solution de Fuchs, la partie singuliere du tenseur est exactement (m/Omega)(psibar psi) n n/\|n\|^2 dans tout repere ; termes croises nuls dans psibar psi ; donc aucune relation regularisante n'est necessaire pour les seconds membres de matiere.
- Exposant de Fuchs constant sur scri par (3.3) ; **lapse nul sur scri** ; seul canal de resonance (logarithme dans le spineur) a epsilon^3 : le lapse sur scri.
- **Classe a un seul exposant preservee** par le couplage : formellement sous H1 (coordonnees (Omega, x), e_0 parallele a nabla Omega) et H2 (resolubilite formelle, hypothese nouvelle non demontree) ; perturbativement a epsilon^3 sur de Sitter (quatre modes, deux jauges, deux jeux de vecteurs d'onde ; auditeur RB-1 dans ses propres jauges).
- **Classe generique** : sans pole ni logarithme a epsilon^3 ; Weyl rescale continu, pas C^1 ; Schouten et courbure scalaire de la metrique conforme **sans limite en jauge longitudinale, avec limite en jauge B** (decalage nul, trace spatiale nulle) : le passage d'une jauge a l'autre a Omega fixe est un changement de facteur conforme theta = 1 + O(Omega^{2 +- 2 i mu}).
- Erreur de la v1 (E1) consignee : l'argument formel supposait une equation d'evolution pour toute inconnue geometrique ; L_00 est fixe par (3.5) et perd un ordre.

### 3.5 Question PSE (canevas v2)
Une seule question (litterature et notion de regularite pour un spineur massif pres d'un scri de genre espace) ; le pole rattache au choix du poids ; point singulier regulier et interference au centre. A reformuler par l'operateur (regle du site sur les textes produits par IA, a verifier : page gen-ai-policy inaccessible depuis l'environnement). Fichier `QUESTION-PSE-DIRAC-SCRI-v2-brouillon.md`.

## 4. Audits du jour
| Chantier | Gel d'audit | Concordance | Re-audit | Acte |
|---|---|---|---|---|
| LB | 203 | 204 : AU-V3 partiel | contre-lecture de l'executant | 205, precedent (xvi) |
| RJ | 208 | 209 : AU-V3 partiel (erreur renforcant le verdict) | non | 210, precedent (xvi bis) |
| V25 | 213 | 214 : AU-V3 | VA-3 | 215, precedent (xvii) |
| RJ2 | 218 | 219 : AU-V3 (clause generique) | RB-3 | 220, precedent (xvi ter) |
Les quatre audits du jour ont abouti a AU-V3 (partiel pour LB et RJ) : chacun a trouve des erreurs sur des enonces ecrits ; les resultats principaux ont tenu.

## 5. Rien en suspens
Aucun gel ouvert, aucun audit en cours, aucun numero reserve. Prochain chantier : reservation 221 et gel.

## 6. Depots
| Depot | Etat |
|---|---|
| Zenodo | v1, v2 publies ; **article v2.5 + note compagnon a deposer** (operateur, 17 oct.) |
| Git | `archive/notes-2026-10`, `kb/notes-2026-10/` : `lb/`, `rj/`, `v25/`, `rj2/`, `pse/` ; commits 0cd4f4c, b5dbf2a, 3983048, 81c0897, puis acte 220 et cette reprise |
| D:\temporaire | `LB\`, `RJ\`, `V25\` (article v2.5 tex et pdf, note compagnon, scripts, `auditv25\`), `RJ2\` (216-220, scripts v1 et v2, `v2runs\`, `auditrj2\` avec RB-1, RB-2, RB-3 et leurs dossiers de travail), `PSE\`, registre racine |
| Base du projet (`claude/...`) | notes 201-220, article v2.5 tex, note compagnon tex, brouillon PSE v2, cette reprise |
| Lecture exterieure | aucun relecteur humain ; question PSE non publiee |

Acces techniques : inchanges (v11 §6). Ajout : ne jamais lancer `pkill -f` avec un motif qui figure dans la commande elle-meme (le shell se tue) ; pour les calculs SymPy longs, eviter `simplify` sur des fonctions generiques et deriver directement la forme lineaire, controlee ensuite contre la forme complete.

## 7. Pieces et empreintes (sha256, 16 premiers caracteres)
| Piece | Empreinte |
|---|---|
| NOTE-202 v2 (LB) ; NOTE-205 | `428750bb02c3d948` ; `540fd58c18ed3d22` |
| NOTE-207 v2 (RJ) ; rj_check_v2.py ; NOTE-210 | `3172b4ceeeba36dd` ; `bda4f1c2ba1533fc` ; `5a4ce940557cb010` |
| Article v2.5 tex / pdf (12 p.) | `7140d3538416841b` / `99a5971916e37bbf` |
| Note compagnon tex / pdf (4 p.) | `11bed3f3f3c40dea` / `0be01b0d07fea1da` |
| NOTE-214 ; RAPPORT-VA3 ; NOTE-215 | `07143e1948613e75` ; `4beed89cfa9dff27` ; `57b072b765eae5bc` |
| NOTE-216 (gel RJ2) ; NOTE-217 v1 ; NOTE-217 v2 | `4127534b32e0ae79` ; `9fdf5d619104418d` ; `78ec0038d3d770fb` |
| rj2_ops.py (v2) ; rj2_test_v2.py | `d20f83ee40dfa30b` ; `13fdc57c21d608d1` |
| RAPPORT-RB1 ; RB2 ; RB3 | `4cf5761eb69f5490` ; `82e76029f5391ea1` ; `b42387358e0d4663` |
| NOTE-219 (finale) ; NOTE-220 | `be5b60fa19b47d70` ; `c506d841dc468f92` |
| Question PSE v2 (canevas) | `7181f47a7fc0827e` |
| Sceaux | LB : `NOTE-201-SCEAU` a `NOTE-205-SCEAU` ; RJ : `NOTE-206-SCEAU` a `NOTE-210-SCEAU` ; V25 : `NOTE-211-SCEAU`, `NOTE-212-213-SCEAU`, `NOTE-214-SCEAU`, `REAUDIT-VA3-SCEAU`, `NOTE-215-SCEAU` ; RJ2 : `NOTE-216-SCEAU`, `NOTE-217-SCEAU`, `NOTE-217-v2-SCEAU`, `NOTE-218-SCEAU`, `NOTE-219-SCEAU`, `REAUDIT-RB3-SCEAU`, `NOTE-220-SCEAU` |

## 8. Protocole et precedents
Inchanges (v11 §8), plus :
- (xvi) Un AU-V3 sur une note de lecture peut etre leve par l'operateur apres une v2 et une contre-lecture des sources nouvelles.
- (xvi bis) Etendu a une note de calcul quand l'erreur renforce le verdict, etablie independamment par les deux auditeurs et verifiee par un script v2 scelle.
- (xvi ter) Etendu a une note de calcul dont l'erreur affaiblit une clause sans toucher le resultat principal : resultat principal etabli par les deux auditeurs ; v2 restreinte et fondee sur un calcul scelle reproduisant les deux ; re-audit court scelle sans erreur restante ; decision de l'operateur.
- (xvii) Un AU-V3 sur un article peut etre leve sans nouvel audit complet apres un re-audit court scelle, si le diff entre la version re-auditee (empreinte scellee) et la version entee est archive et ne contient rien hors liste.
- Lecon de methode du jour : chacun des quatre audits a trouve une erreur sur un enonce ecrit (portee, attribution ou clause) alors que les calculs principaux tenaient ; le re-audit court cible est efficace ; les controles positifs (injecter le defaut cherche) doivent faire partie de l'execution, pas seulement de l'audit.

## 9. Pistes (aucune engagee)
1. **Jauge conforme de Friedrich (R prescrit) pour la classe generique** : la geometrie y a-t-elle une limite ? Lien direct avec la regle de raccord CCC (que fixe-t-elle a scri ?).
2. **H2** : resolubilite formelle des equations conformes dans la jauge (Omega, x) ; ou transposition dans la jauge de Friedrich.
3. **Ordre epsilon^4 et au-dela** ; existence non lineaire pour la classe a un seul exposant (theorie fuchsienne a exposants complexes).
4. **Article v2.6** : Rem. 2(4) selon NOTE-217 v2 §5 (texte reformule par RB-3), apres le depot de la v2.5.
5. **Lecture humaine** (priorite) : Zenodo v2.5, PSE, relecteurs (v11 §9).
6. Inchanges de v11 : partie a (Euler) et Gamma[g] formels ; (2.17) pour k non nul ; reflexion sur scri ; Q-M3 ; OA-2 sur ROMEO.

## 10. Preferences de l'operateur (a appliquer)
Francais ; pas de tiret long ni de tournures d'IA ; illustrer quand c'est utile ; fichiers remis par envoi de fichier, la base du projet servant a la persistance ; analyse factuelle d'abord sur les questions disputees ; courriel utilise seulement pour l'attribution ; git par add_repo, jamais de jeton colle.

## 11. Non-surclassement
Cette piece compile ; elle ne grave rien. RG-4 refutee a titre provisoire, raison resserree ; classe a un seul exposant preservee (formel conditionnel, perturbatif) ; G-V3 et M-V3 candidats formels ; CCC + M ouverte sous la condition du Higgs ; CCC-T non candidate ; repli suspendu a A2★. Noyau {A4 ; A2★ ; N} inchange. Aucun audit par IA ne vaut lecture humaine.
