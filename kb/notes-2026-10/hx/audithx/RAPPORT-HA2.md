# RAPPORT HA-2 : audit adverse aveugle de NOTE-BORD-EON-186 (chantier HX)

Date : 2026-10-15. Pieces lues : PROMPT-AVEUGLE-HA2.md, NOTE-186.md, hx_check.py, hx_check_sortie.txt (rien d'autre).
Espace de travail : /tmp/claude-0/ha2/ (hx_check.py copie, sortie_rerun.txt, variantes.py, variantes_sortie.txt). sympy 1.14.0.

## 0. Reproduction

| Objet | Resultat |
|---|---|
| `python3 hx_check.py` | sortie **identique octet pour octet** a hx_check_sortie.txt |
| sha256 hx_check.py | 715b23948563b3b2496c3e6726d0a9fd062c42340e6671ccf540e30e2ee0423d |
| sha256 hx_check_sortie.txt (= rerun) | d7db9cfdf97d638456fe2928abe98ccc1f11710dd0e1468655bf58249d789bbe |

## 1. Synthese des verdicts

| Point | Verdict | En une ligne |
|---|---|---|
| G1 equation indicielle, tableau §1 | **TIENT, avec reserves** | Equation, seuils, racine double, mu complexe : exacts (reverifies independamment). Mais la clause « generique c1 != 0 » est indispensable et n'est pas portee dans le VERDICT ; la ligne M2 <= 0 « Higgs actuel » est hors domaine de validite du lineaire. |
| G2 poids conformes | **TIENT** | Yukawa 0, masse de jauge 0, m^2 abs(H)^2 -2, h.c. et doublet compris ; recalcules symboliquement. Imprecisions de notation (lambda, mu, M2 dimensionne ou non). |
| G3 reduction « aucune condition supplementaire », Friedrich | **TIENT PARTIELLEMENT** | La suffisance (H_r lisse => tout le secteur regulier) est solide. Le « equivaut » et « ssi » (necessite) sont surdits : necessite seulement pour donnees generiques homogenes, pas « par le theoreme 3.1 ». Seuils (a), (b) transferes sans preuve aux W, Z et faux pris isolement pour les neutrinos de Weinberg. Portee de l'extension Friedrich sous-declaree (systeme couple jauge-Higgs-Dirac, pas seulement O(4)). |
| G4 script | **TIENT pour ce qu'il calcule, mais annonce plus qu'il ne verifie** | Calculs (1), (2) corrects ; critere (c) correctement implemente pour donnees generiques. Mais seuils et poids conformes sont **codes en dur** (chaines imprimees / entiers additionnes), l'EDO est tapee a la main, les libelles (a), (b) different de ceux de la note, `nsimplify` de flottants peut donner un faux positif en (c). |

Aucune erreur ne renverse la conclusion centrale (« pour la regularite formelle, condition unique M2 = 2 sur le Higgs, pour donnees generiques »). Pas d'erreur grave.

## 2. G1 : equation indicielle et tableau du §1

### 2.1 Verifications reussies
- **Derivation independante** (V1) : box dans dS en temps conforme, a = -1/eta, R = 12 (H = 1), terme m^2 + xi R : equation indicielle obtenue `alpha^2 - 3 alpha + m2 + 12 xi = 0`. Concorde avec la note et confirme M2 = m_h^2/H^2 + 12 xi.
- **Identite conforme** (V3) : avec phi = Omega phi_r, l'equation rescalee est `phi_r'' + (M2 - 2) phi_r / s^2 = 0` : le seul terme singulier est (M2 - 2)/Omega^2, nul ssi M2 = 2 (= Rhat/6, soit 2 Lambda/3 avec couplage minimal). Le cas xi = 1/6, m_h = 0 donne bien M2 = 2.
- **Seuils** : (a) Re alpha_min > 0 <=> M2 > 0 ; (b) Re alpha_min >= 1 <=> M2 >= 2 ; verifies analytiquement.
- **(c) unique en M2 = 2** : preuve en une ligne, (alpha_1 - 1) + (alpha_2 - 1) = 3 - 2 = 1, deux entiers >= 0 => {0, 1} => alpha = 1, 2 => M2 = 2. Balayage V4 de tous les rationnels p/q (q <= 40, abs(M2) <= 20) : seul M2 = 2.
- **Racine double** M2 = 9/4 : h = s^{3/2}(c1 + c2 ln s), m/Omega = s^{1/2}(c1 + c2 ln s) -> 0 : (a), (b) oui, (c) non. Correct.
- **mu complexe** : m/Omega ~ s^{1/2 +- i nu}, borne, non lisse. Correct.
- **Zone 0 < M2 < 2** (V9, integration numerique du Dirac rescale a k != 0) : psi_r converge (lentement, en s^{alpha_min}) tandis que (m/Omega) psibar psi diverge (2e2 -> 2e7 pour M2 = 0,5 entre s = 1e-3 et 1e-9). L'affirmation « champ continu, energie divergente » est confirmee.
- **Lien Euler / Frobenius** : en homogene l'EDO est d'Euler, pas de log malgre des racines a difference entiere ; en inhomogene a M2 = 2, h = s (c1 cos ks + c2 sin ks) est solution exacte (V6), pas de log. Le classement (c) n'est donc pas pollue par k.

### 2.2 Erreurs et fragilites
| # | Gravite | Constat |
|---|---|---|
| G1-a | **Moyenne** | **Role de c1 = 0.** Avec c1 = 0 (donnees fines), seul s^{alpha_max} survit et (c) est satisfait pour toute la famille M2 = -(n+1)(n-2), n >= 1 : **2, 0, -4, -10, ...** (V5) ; (a) et (b) deviennent vrais pour **tout** M2 reel <= 9/4. Ex. a M2 = 0 et k != 0 : h = sin ks - ks cos ks, h/Omega = k^3 s^2/3 + ... lisse, sans log (V6). Le §5 le mentionne, mais le VERDICT, le §1 (« Seuils : ... (c) ssi M2 = 2 ») et le §4 l'enoncent sans la clause « donnees generiques ». Le « ssi » n'est vrai que sur un ouvert dense de donnees. |
| G1-b | Mineure | **Ligne M2 <= 0 « Higgs actuel ».** Pour M2 < 0, alpha_min < 0 : le mode croit vers l'avenir, h quitte le voisinage du point symetrique, l'hypothese « quartique sous-dominante » (§5) tombe. Le verdict « non » reste juste mais par un autre chemin : h -> v, m_f -> y v constante, cas « masse constante » (echec de (a)). Le tableau devrait le dire. |
| G1-c | Mineure | La forme h = c1 Omega^{3/2-mu} + c2 Omega^{3/2+mu} est invalide a mu = 0 (il faut la branche log) ; le tableau traite le cas, la formule non. |
| G1-d | Mineure | Le libelle (b) « densite d'energie rescalee bornee » n'est ni demontre dans la note ni teste par le script (qui teste « m a borne »). L'equivalence est plausible (rho_r ~ (m/Omega) psibar_r psi_r avec psi_r continu, psibar psi conserve a k = 0) mais reste une identification, non une verification. Idem (a) « champ de Dirac continu » vs script « int m dt < inf » (equivalent par Caratheodory/Gronwall, non ecrit). |

## 3. G2 : poids conformes

Conventions de la note : ghat = Omega^-2 g (ghat physique), H = Omega H_r, psi = Omega^{3/2} psi_r, A de poids 0. Recalcul symbolique (V2, Omega explicite) :

| Terme (densite sqrt(-ghat) x ...) | Poids Omega | Consequence |
|---|---|---|
| y H psibar psi (et h.c., et H~ = i sigma2 H*) | **0** | invariant ; Omega reel, H~ meme poids que H |
| g^2 abs(H)^2 ghat^{mn} A_m A_n | **0** | invariant |
| m^2 abs(H)^2 | **-2** | terme singulier Omega^-2 de Friedrich |
| lambda_h abs(H)^4 | 0 | invariant (donc regulier, contrairement a ce que suggere « sous-dominant ») |
| cubique H^3 | -1 | singulier ; absent du SM par invariance de jauge : coherent avec « mu = 0 dans (3.3) » |
| Weinberg (LH)(LH)/M | **+1** | non invariant, mais coefficient rescale -> 0 (cf. G3-c) |

Verification de l'equation de Dirac rescalee : Dhat(Omega^{3/2} psi_r) = Omega^{5/2} D psi_r et y Omega H_r Omega^{3/2} psi_r = Omega^{5/2} y H_r psi_r, donc coefficient y H_r = m_f / Omega. Correct. Pour le doublet, la composante du coefficient couplant psi_L est le doublet H_r lui-meme : lissite du coefficient <=> lissite de H_r si y != 0. Correct.

| # | Gravite | Constat |
|---|---|---|
| G2-a | Mineure | Collision de notations : **lambda** = constante cosmologique (« 2 lambda/3 ») et quartique du Higgs ; **mu** = sqrt(9/4 - M2) et coefficient cubique de Friedrich (3.3) (et parametre mu^2 du SM) ; **m_h** designe le parametre de masse au point symetrique, pas la masse physique 125 GeV. |
| G2-b | Mineure | **M2 tantot sans dimension, tantot dimensionne** : §1 « M2 = (m_h^2 + 12 xi H^2)/H^2 » vs VERDICT « M2 = ... = 2H^2 = 2 lambda/3 » et §4 « M2 >= 2H^2 ». |
| G2-c | Mineure | « compense par le terme de courbure R/6 » : il s'agit de Rhat/6 de la metrique **physique** (= 2H^2) ; l'invariance de jauge-Higgs complete suppose aussi que le terme cinetique du Higgs, non invariant seul, soit traite via l'identite conforme (box - R/6). La note ne le dit pas mais le resultat est juste. |

## 4. G3 : reduction et extension de Friedrich

### 4.1 Ce qui tient
Comptage complet (V2) : dans le systeme classique Yang-Mills + Higgs + Dirac, **tous** les couplages sont de poids 0 sauf m^2 abs(H)^2 (et le defaut xi != 1/6), qui se combinent en un unique terme (M2 - 2) Omega^-2 abs(H_r)^2. Les sources retroagissant sur le Higgs (y psibar psi, g^2 A^2 H) sont regulieres. Donc **H_r lisse => secteurs fermionique et W, Z formellement reguliers** : la suffisance est solide.

### 4.2 Erreurs
| # | Gravite | Constat |
|---|---|---|
| G3-a | **Moyenne** | **« equivaut ..., donc, par le theoreme 3.1 de Friedrich, a M2 = 2 »** (VERDICT). Un theoreme d'existence/lissite (sens M2 = 2 => H_r lisse) ne donne pas la necessite. La necessite (M2 != 2 => H_r non lisse) ne vient que de HX-1, homogene et generique ; elle est fausse pour c1 = 0 (G1-a). Formulation correcte : « M2 = 2 suffit (Friedrich, sous reserve FW-3) ; pour des donnees generiques, M2 = 2 est necessaire (HX-1, homogene) ». |
| G3-b | Moyenne | **W, Z : « reguliere ssi H_r l'est », « meme reduction que pour les fermions »**, et le §4 leur attribue les seuils (a) M2 > 0, (b) M2 >= 2. (i) Le coefficient de l'equation de Proca rescalee est g^2 abs(H_r)^2 (poids 0, sans 1/Omega, au carre), ~ s^{2 alpha - 2} : sa structure differe de m_f/Omega ; les seuils (a) et (b) des bosons ne sont ni definis ni demontres (V8 : ex. l'integrabilite en s de g^2 abs(H_r)^2 exige M2 > 5/4, pas M2 > 0 ; l'integrabilite ponderee s q donne M2 > 0 ; tout depend du critere, non fixe). (ii) abs(H_r)^2 lisse n'implique pas H_r lisse en general (« ssi » abusif) ; (iii) « masse g abs(H_r) » : abs(.) n'est pas lisse la ou H_r s'annule, c'est abs(H_r)^2 qui compte ; (iv) pres du point symetrique (H -> 0) la jauge unitaire implicite est singuliere : l'analyse doit se faire sur le doublet complet avec Goldstones (ce que fait de facto le comptage de poids, d'ou la suffisance qui tient). |
| G3-c | Mineure | **Neutrinos de Weinberg** : coefficient m_nu/Omega ~ Omega H_r^2/M ~ s^{2 alpha - 1}. Seuils propres (V7) : (a) M2 > 0 (identique), **(b) M2 >= 5/4** (pas 2), **(c) M2 = 5/4 ou M2 = 2** (deux valeurs). Le §4 attribue les memes seuils a « tout le secteur ... neutrinos compris ». Pris en conjonction avec les fermions charges, la condition de secteur redevient M2 = 2 / M2 >= 2 : la conclusion globale tient, l'enonce par particule non. |
| G3-d | Moyenne | **Portee de l'extension Friedrich (FW-3) sous-declaree.** La note cadre l'extension comme « scalaire reel -> quatre composantes reelles, potentiel O(4) ». Or le Higgs du SM est **jauge** : l'equation du doublet contient D_m = d_m - i g A_m et des sources fermioniques. Ce qu'il faut etendre est le theoreme au **systeme couple jauge-Higgs-Dirac** (et, si le theoreme 3.1 inclut la gravite, a ce systeme couple a Einstein avec un tenseur energie-impulsion non sans trace pour xi = 0). Non verifiable ici (enonce de Friedrich non fourni) ; a declarer comme tel. |
| G3-e | Mineure | « Aucune condition supplementaire » est classique : running des couplages, anomalies de trace (QCD, QED) brisent l'invariance conforme. La note isole QED (Q-M3) et QCD (baryons) mais pas le running des Yukawa / de la quartique, qui affecte aussi y H_r. A mentionner en limite. |

## 5. G4 : le script

| # | Gravite | Constat |
|---|---|---|
| G4-a | **Moyenne** | **Seuils non calcules** : la ligne « thresholds » est une **chaine imprimee** ; le script n'echantillonne que 11 valeurs de M2. « (c) only M2 = 2 » n'est pas verifie par le script (je l'ai demontre et balaye en V4 : vrai). |
| G4-b | **Moyenne** | **Poids conformes codes en dur** (`w_sqrtg = -4`, `yuk = w_sqrtg + 1 + 3`, ...) : addition d'entiers saisis a la main, aucune transformation symbolique. La sortie (3) n'est donc pas une verification. Idem « rescaled Dirac mass coefficient » (simple print). Le resultat est neanmoins juste (V2 recalcule symboliquement). |
| G4-c | Mineure | **EDO tapee a la main** (`h'' - (2/s) h' + M2 h/s^2`), non derivee de la metrique. Juste (V1 la derive de box_dS). |
| G4-d | Mineure | **Libelles divergents** : script (a) « int m dt < inf », (b) « m a bounded » ; note (a) « champ de Dirac continu », (b) « densite d'energie rescalee bornee ». Le passage de l'un a l'autre n'est ni code ni ecrit (cf. G1-d). |
| G4-e | Mineure | **Critere (c)** : bien implemente pour donnees generiques (exclut log, exige Im = 0 et alpha - 1 entier >= 0 pour les deux racines). Exiger les deux racines equivaut ici a exiger alpha_min seule (car alpha_min = 1 force M2 = 2). Il **n'implemente pas** le cas c1 = 0 (V5 l'ajoute). |
| G4-f | Mineure (robustesse) | `classify` applique `nsimplify` a l'entree : un flottant voisin est arrondi au rationnel. `classify(1.999999999999)` et `classify(2.0000000000001)` renvoient **(c) = True** (faux positif). Sans effet sur la sortie publiee (entrees rationnelles). `is_integer` peut renvoyer None (traite comme False par `and`/`all` : sans faux positif constate). |
| G4-g | Information | Pas d'assertion : le script n'echoue jamais ; il affiche. Un audit CI ne peut rien en tirer automatiquement. |

## 6. Liste des erreurs par gravite

**Graves** : aucune.

**Moyennes** (5)
1. G1-a / G3-a : « ssi M2 = 2 » et « equivaut, par Friedrich » enonces sans la clause « donnees generiques » ; avec c1 = 0, (c) vaut pour M2 in {2, 0, -4, -10, ...} et (a), (b) pour tout M2 <= 9/4. Friedrich ne donne que la suffisance.
2. G3-b : W, Z : seuils (a)/(b) transferes sans preuve, coefficient g^2 abs(H_r)^2 de structure differente, « ssi » abusif, jauge unitaire singuliere au point symetrique.
3. G3-d : extension de Friedrich a declarer pour le systeme couple jauge-Higgs-Dirac (pas seulement un potentiel O(4)).
4. G4-a : seuils imprimes, non calcules.
5. G4-b : poids conformes codes en dur.

**Mineures** (11)
G1-b (ligne tachyonique hors domaine lineaire), G1-c (formule a mu = 0), G1-d (libelles (a)/(b) identifies sans preuve), G2-a (collisions lambda, mu, m_h), G2-b (M2 dimensionne ou non), G2-c (Rhat/6 physique, terme cinetique), G3-c (neutrinos : (b) M2 >= 5/4, (c) M2 in {5/4, 2}), G3-e (running et anomalies hors QED), G4-c (EDO a la main), G4-d (libelles script vs note), G4-e/f (c1 = 0 non implemente ; faux positif nsimplify sur flottants).

## 7. Corrections proposees (pour S27-02 v2)
- VERDICT et §1/§4 : remplacer « equivaut ... a M2 = 2 » par « M2 = 2 suffit (Friedrich, FW-3) ; est necessaire pour donnees generiques (HX-1) ; ensemble exceptionnel c1 = 0 : M2 = -(n+1)(n-2) ».
- §3 : restreindre HX-3 a la suffisance ; retirer les seuils (a)/(b) pour W, Z ou les deriver ; ecrire abs(H_r)^2.
- §4 : seuils neutrinos propres (b) M2 >= 5/4, (c) M2 in {5/4, 2}, en precisant que la conjonction du secteur redonne M2 = 2.
- §2/§5 : FW-3 = extension au systeme couple jauge-Higgs-Dirac (et Einstein si pertinent).
- Notation : Lambda (cosmologique) vs lambda_h ; mu_F (Friedrich) ; M2 sans dimension partout.
- Script : calculer les seuils (resolution symbolique des inegalites), deriver l'EDO de la metrique, faire les poids symboliquement (cf. variantes.py V1-V3), ajouter des `assert`, ajouter le cas c1 = 0, refuser les flottants dans `classify`.
