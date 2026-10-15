---
id: REPRISE-AUTOPORTANTE-2026-10-15-v8-DIRAC-ET-CALIBRATION
date: 2026-10-15
heure: 17:25 heure de Paris
programme: LC-RACCORD
destination: projet « deux bords » (piece d'ouverture unique ; remplace la reprise v7 du 2026-10-14 comme point d'entree)
nature: PIECE DE PASSATION autoportante. Reprend la v7 par reference et compile tout ce qui a ete produit du 14 octobre 17h45 au 15 octobre 17h (depot Zenodo v2, article RG-4 spin 1/2 v1 a v2.2, deux audits, greffes S26-02 v2 et v3, calibration CAL-F, NOTE-163 v2, brouillon de question Physics Stack Exchange ; NOTE-171 a 179). N'ajoute aucune substance.
grade: "[conv]"
supersede_comme_entree: "01-REPRISE-AUTOPORTANTE-2026-10-14-v7-CCC-T-AUDITEE.md (reste valide comme piece ; §1, §4, §5, §6 completes ici)"
premier_numero_libre: 180
registre_en_vigueur: "REGISTRE-CENTRAL-NUMEROS-NOTES.md (D:\\temporaire, base du projet, archive git)"
depot_git: "github.com/droppy94/LC_Raccord, branche archive/notes-2026-10 ; d7bd863 (14 oct., 168-170, reprise v7) puis commit du 15 oct. (171-179, reprise v8)"
zenodo: "v1 10.5281/zenodo.22919751 ; v2 10.5281/zenodo.23373604 (14 oct., publie) ; concept 10.5281/zenodo.22919750"
---

# Reprise autoportante v8 : l'electron au bord, la calibration du critere (15 octobre 2026)

## 0. Procedure d'ouverture
1. Lire cette piece ; pour l'amont, la reprise v7 (14 oct.) et la v4 (13 oct.).
2. Ouvrir le registre : derniere ligne emise **179**, **180 libre**.
3. Si la discussion est reliee a l'ordinateur, verifier sur `D:\temporaire` : `ARTICLE-RG4-SPIN12\` (article v1 a v2.2, scripts, `audit\`), `CAL-F\` (175 a 179, source Friedrich, scripts, rapports), `S26-02-VERDICT-CHANTIER-D-v2.md` et `-v3.md`, registre, journal des depots. Empreintes : au registre et aux sceaux `NOTE-172-SCEAU.txt`, `NOTE-173-174-SCEAU.txt`, `NOTE-175-SCEAU.txt`, `NOTE-176-177-SCEAU.txt`, `NOTE-178-179-SCEAU.txt`.
4. Rappels a l'operateur, une fois : (i) publier la question Physics Stack Exchange (brouillon `QUESTION-PSE-DIRAC-SCRI-brouillon.md`, a reformuler par lui, lien article a deposer) et transmettre le lien ; (ii) deposer l'article v2.2 sur Zenodo comme enregistrement separe (Preprint) si l'on veut un lien stable ; (iii) relecteurs humains (inchange).
5. Ne rien ecrire de substantiel sans numero reserve au registre.

## 1. Statut de la CCC au 15 octobre 2026
| Forme | Statut | Pieces |
|---|---|---|
| CCC, forme actuelle | **Refutee a titre provisoire** (RG-4, lecture stricte). Fondement precise sous **deux lectures du critere** : (i) corpus (Omega^-4 T) : pole m/Omega de la densite d'energie rescalee de l'electron, invariant de jauge ; (ii) Friedrich transpose a l'equation de matiere : coefficient m/Omega de l'equation de Dirac rescalee, singulier pour toute masse constante non nulle, sans masse speciale (contrairement au scalaire), non eliminable par redefinition lisse des inconnues. Systeme couple Einstein-Dirac non traite. | S26-02 v3 (§7, §8), NOTE-171 v2.2, NOTE-172 a 179 |
| CCC + M | Hypothese ouverte ; condition quantitative ajoutee : une masse qui « s'efface » doit decroitre au moins comme 1/a pour une densite d'energie rescalee bornee, comme Omega fois une fonction lisse pour un coefficient lisse ; continuite du champ ssi int m dt fini | article Prop. 4, S26-02 v2 G-D1-d |
| G-V3 | Inchange (candidat, non grave). La regle de comptage de NOTE-163 est corrigee (G-CAL-a : borne superieure seulement), sans effet sur la chaine, etablie par calculs covariants explicites. Point nomme pour le relecteur humain : un pole de (2.17) sur une solution prouve l'irregularite si les autres inconnues sont lisses (W diverge en ln au premier ordre, NOTE-128) | NOTE-163 v2, NOTE-178 |
| Repli acyclique, CCC-T | Inchanges (v7) | |

## 2. Ce qui a ete fait (14 oct. 17h45 au 15 oct. 17h)
```
14 oct. soir  question « bord vu comme crunch, rebond ? »  : reponse hors registre (trois lectures ; seule la reflexion sur 𝓘⁺ est non instruite)
              Zenodo v2 publie (DOI 23373604) ; metadonnees reecrites ; role « Producer » retire de la v1
              NOTE-171  article RG-4 spin 1/2 v1 (anglais, 7 p.)
              relecture ChatGPT (IA exterieure, precedent xi) -> v2 : jauge, densite d'energie, masse variable, conclusion conditionnelle
              NOTE-172/173  audit aveugle DA-1/DA-2 : Prop. 1-4 confirmees ; Lemme 2 trop large et Prop. 5(c) fausse -> v2.1
              NOTE-174  acte : greffe G-D1 (S26-02 v2)
              base du projet nettoyee (109 doublons et reprises intermediaires retires, toutes presentes sur D: et git)
15 oct.       brouillon de question Physics Stack Exchange
              NOTE-175/176  CAL-F : calibration de (2.17) sur le scalaire de Friedrich ; calcul de tete faux (derivees partielles) ; regle de comptage imprecise
              NOTE-177/178  audit aveugle CA-1/CA-2 : calculs confirmes ; confusion « valeur sur couche / regularite formelle » relevee -> G-D1-e reecrite
              NOTE-179  acte : G-CAL-a (NOTE-163 v2), G-D1-e (S26-02 v3), article v2.2
```

## 3. Resultats porteurs (toutes [conv], audites par IA isolees, non relus par un humain)
- **Dirac test sur dS** (article v2.2) : norme constante ; u = exp(i beta (m/H) ln Omega) chi, chi -> chi_0 ; pas de limite (Prop. 1). Jauge : pour une particule tardive, phase retirable par lambda = -mt, potentiel a pole non integrable dans le repere conforme ; aucune jauge ou champ et potentiel sont continus (Prop. 2). Densite d'energie rescalee : pole m/Omega, version une particule tanh(pi m/H) pour Bunch-Davies (Prop. 3). Couplages locaux (classe restreinte) : masse effective constante (Lemme 2). Masse variable : trois conditions strictement ordonnees (Prop. 4). Remarque Friedrich transposee.
- **Critere (2.17)** : derivee covariante physique ; nul pour toute source homogene isotrope conservee ; regle « pole ssi p = 1 » fausse dans les deux sens ; le critere de Friedrich est formel (seconds membres en fonction des inconnues), une valeur sur couche ne le remplace pas (precedents xii).

## 4. Depots
| Depot | Etat |
|---|---|
| Zenodo | v1 et v2 publies ; v1 sans role « Producer » ; article v2.2 non depose |
| Git | archive/notes-2026-10 : commit du 15 oct. (171 a 179, articles, CAL-F, reprise v8) |
| D:\temporaire | a jour (registre, ARTICLE-RG4-SPIN12, CAL-F, S26-02 v2/v3, journal des depots, metadonnees Zenodo v2) |
| Base du projet | a jour ; ~1,4 Mo sur 2 Mo apres nettoyage |
| Lecture exterieure | question PSE a publier par l'operateur ; aucun relecteur humain |

## 5. Pistes (aucune engagee)
1. **Lecture humaine** (priorite 1) : publication de la question PSE ; relecteurs RG-4 et G-V3 (NOTE-164, NOTE-163 v2).
2. **Dirac couple** : equations geometriques du systeme Einstein-Dirac au sens formel de Friedrich ; source de (2.17) pour k != 0.
3. **G-V3** : examiner l'hypothese « autres inconnues lisses » au regard de la divergence en ln de W (point nomme NOTE-178/179).
4. **Croisement S27 x Prop. 4** (prepare, non arme) : avec h ~ Omega^{3/2 - mu} (S27), m_e = y h satisfait Prop. 4(a) pour m_h^2 > 0, 4(b) ssi m_h^2 >= 2H^2, 4(c) ssi m_h^2 = 2H^2 ; a instruire avec le critere formel (precedent xii).
5. **Reflexion sur 𝓘⁺** (lecture 2 de la reponse du 14 oct.) : condition de bord reflechissante, prediction Z2 sans gain.
6. Inchanges de v7 : cadre residuel G-V3, chaine M-V3, OA-2 sur ROMEO.

## 6. Precedents nouveaux
- (xi) Relecture par une IA exterieure : traitee comme un rapport, objection par objection, corrections auditees avant entee ; ne vaut ni lecture humaine ni audit.
- (xii) Calibration sur un cas a reponse connue avant toute extension d'un critere ; une valeur sur couche ne remplace pas un critere formel.
- (xiii) Un lien de jauge U(1) peut deplacer une singularite de la matiere vers le potentiel : les obstructions se formulent de facon invariante (paire champ et potentiel, densite d'energie, coefficient d'equation).

## 7. Non-surclassement
Cette piece compile ; elle ne grave rien. RG-4 refutee a titre provisoire ; G-V3 candidat non grave ; CCC + M ouverte ; CCC-T non candidate ; repli suspendu a A2★. Noyau {A4 ; A2★ ; N} inchange. Aucun audit par IA ne vaut lecture humaine.
