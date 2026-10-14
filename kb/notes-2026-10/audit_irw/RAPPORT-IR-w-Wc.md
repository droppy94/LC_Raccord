# RAPPORT W-c : audit aveugle de t-1, t-2, t-3 et de leurs scripts

Date : 2026-10-12. Perimetre lu : /home/claude/audit_wc/ uniquement (plus le prompt de consigne). Outils : python3, sympy 1.14.0, travail dans /home/claude/audit_wc/work/.
Etiquettes : [calcule] = obtenu par execution sympy ; [derive] = raisonnement analytique (comptage de puissances, identites).

## 0. Empreintes

| Fichier audite | SHA-256 attendu | SHA-256 constate | Statut |
|---|---|---|---|
| irt_a.py | 97ca3732...93d95b | 97ca373277844327960a23bcbd43b06035752a018c911afb772036e32993d95b | OK |
| irt_a_ctrl.py | 62b96e1c...ffdae37 | 62b96e1cc4df53223d85e52bae766e33430e16c2dbd2302bb35380f82ffdae37 | OK |
| irt_gamma_phi.py | 0d3f44cd...8b1e064 | 0d3f44cdde18ca5b5b17a8e7342e1c38ca27142fbf7aa4a29c917fe4f8b1e064 | OK |

Scripts et sorties produits par l'audit (dans work/) :

| Fichier | SHA-256 |
|---|---|
| wc_t1_indep.py | b9f16836cd2ac22c3be0932634371278855fcdd31fe557507c7278bbd148e2bb |
| wc_t23_indep.py | 3501edcef525ab890a5be67c4d4755a9555262a88b479860ca781349bf18c261 |
| wc_t3_cone.py | f8175a8fb1d86ee22f5e34a49a2c2f3d26c71464dfa4fe83c496cbef7c23d332 |
| out_irt_a.txt | f3dddad520071f333e1523b1c770f8df627a4ab087f4002a0d4a20edd99dbea4 |
| out_irt_a_ctrl.txt | 0aeff1d9268fc30cc5ce8941ff8c9e79fb478e0143e2cf74bbe46ab42a4286d0 |
| out_irt_gamma_phi.txt | 26e0979ebd557bf00599858c560bfd907f9285299a54a62d1d16fbba3b1569ca |
| out_wc_t1_indep_c2.txt | 4f481d188749607ad94de15993742cb6d21378ba68ff426696a17f51975724de |
| out_wc_t1_indep_cm12.txt | 0fe14b727c9970ec227118b560e24e67a4e533913507086dd941de7568c4243e |
| out_wc_t23_indep.txt | ec4a0f0202e09839a0ec7f175d48a39ae7831f9a922da75aa7e6b1f8e89b2d25 |
| out_wc_t3_cone.txt | c51d192d50ad77ef56042dc71f7bebfcc87a4c731cb633355e27fc34c52020eb |

(work/ contient aussi des copies a l'identique des trois scripts audites, memes empreintes, executees sur place.)

## 1. Audit point par point des scripts

### 1.1 irt_a.py (t-1) et irt_a_ctrl.py (controle)

Les deux fichiers ne different que par la ligne 54 (coefficient 2 contre -1/2 devant sigma Delta4 sigma).

| Point | Verdict | Commentaire |
|---|---|---|
| Metrique de reference g = diag(-1,1,1+eP,1+eQ), sigma = -ln s, ghat = e^{2 sigma} g = s^-2 g | OK | coherent avec ghat = s^-2(eta + e h). |
| g^-1 : (1+eP)^-1 = 1 - eP + e^2 P^2 | OK | exact a l'ordre e^2 [derive]. |
| sqrt(-det g) = 1 + e(P+Q)/2 + e^2(PQ/4 - (P^2+Q^2)/8) | OK | verifie : sqrt(1+a), a = e(P+Q) + e^2 PQ [derive]. |
| Troncature N2 = 2 avant Euler-Lagrange | OK | dS/dP a l'ordre e^2 = e * (dS/dg_yy a l'ordre lineaire) : il faut et il suffit de garder e^2 dans la densite (termes P^2, PQ inclus). |
| Christoffel, Riemann R^a_bcd = d_c Gam^a_bd - ..., Ricci R_bd = R^a_bad | OK | conventions MTW. |
| Riem^2, Ric^2 par contractions diagonales | OK | legitime car g et g^-1 sont diagonales. |
| E = Riem^2 - 4 Ric^2 + R^2 | OK | |
| box f, Hessienne | OK | |
| Delta4 = box^2 + 2 R^{ab} nabla_a nabla_b - (2/3) R box + (1/3) nabla^a R nabla_a | OK | c'est la forme developpee de nabla_a(nabla^a nabla^b + 2R^{ab} - (2/3) R g^{ab}) nabla_b (le terme 2 (nabla_a R^{ab}) nabla_b = (nabla^b R) nabla_b combine a -(2/3) donne 1/3) [derive]. Identite covariante, independante de la signature. |
| Coefficient 2 devant sigma Delta4 sigma | OK | integrabilite : sqrt(ghat)(Ehat - (2/3) box_hat Rhat) = sqrt(g)(E - (2/3) box R + 4 Delta4 sigma), et delta(2 sigma Delta4 sigma) = 4 Delta4 sigma (Delta4 autoadjoint) [derive]. |
| Variation : euler_equations sur P | OK | donne dS/dP = e dS/dg_yy ; ordre e^0 verifie nul [calcule]. |
| Normalisation T_hat_yy = s^2 g_yy^2 (2/sqrt g) dS/dg_yy | OK | T_hat^{ab} = (2/sqrt ghat) dS/dghat_ab a sigma fixe, dghat = s^-2 dg, sqrt ghat = s^-4 sqrt g, donc T_hat_ab = s^2 g_ac g_bd (2/sqrt g) dS/dg_cd [derive]. |
| Signe "fixe par le fond" | OK (avec remarque) | sgn = +1 est la convention standard T_ab = -(2/sqrt g) dS/dg^ab = +(2/sqrt g) dS/dg_ab, et c'est elle qui donne +6 ghat. Independamment : la trace vaut (1/sqrt ghat) dS/dsigma = Ehat - (2/3) box_hat Rhat = 24 sur de Sitter (H = 1), donc T_hat = 6 ghat si T_hat est proportionnel a ghat [derive]. Remarque : le test d'ordre e est insensible au signe (il teste la proportionnalite T1/delta ghat = T0/ghat) ; le choix du signe par le fond n'est donc pas circulaire pour la conclusion "sans effet sur R". |
| Couverture : seule la composante yy est testee | DEFAUT mineur | justifiable par symetrie (au premier ordre, seules les composantes de spin 2 dans le plan (y,z) peuvent etre non nulles, et T_zz = -T_yy par y <-> z) [derive], mais non verifie par le script. Comble par wc_t1_indep.py (ss, sx, xx, yy, zz) [calcule]. |
| Code mort (ligne 64 `Tyy_up = 2*tr(ELs/e if False else 0)`, E0, E1 non utilises) | DEFAUT cosmetique | sans effet sur le resultat. |
| Sorties | OK | irt_a : fond 6/s^2, ordre e = 6 u cos kx / s^2, residu 0 (sgn = +1) [calcule]. Controle : fond 17/(2 s^2), residu d'ordre e non nul avec des termes k^2 s^2 [calcule]. |

Hypothese de portee (pas un defaut du script, mais a nommer pour t-1) : on ne varie que le terme de Wess-Zumino Gamma_WZ[g, sigma] = W[ghat] - W[g]. La contribution de W[g] (action effective non locale de la reference eta + e h) et les parties c (Weyl^2) et box R de l'anomalie sont hors champ.

### 1.2 irt_gamma_phi.py (t-2, t-3)

| Point | Verdict | Commentaire |
|---|---|---|
| Christoffel de ghat = e^{2 sigma} eta par la formule conforme | OK | Gam^a_bc = delta^a_b d_c sigma + delta^a_c d_b sigma - eta_bc eta^{am} d_m sigma. Retrouve par calcul direct depuis ghat dans wc_t23_indep.py [calcule]. |
| L = (kap/2)(T - ghat trT/3), trT = ghat^{ab} T_ab | OK | |
| R_{rho nu lam} = s^-1 (nabla_nu L_{lam rho} - nabla_lam L_{nu rho}), nu < lam | OK | antisymetrie en (nu, lam) exploitee. |
| Trace et divergence controlees | OK | |
| `lowest()` | OK sous condition | valable car y(s) polynomial et cos kx independant de s. |
| t-2 : ansatz Y_yy = -Y_zz = y(s) cos kx | OK | automatiquement conserve et sans trace (verifie : div = 0, trace = 0) [calcule]. |
| Generalisation annoncee dans la docstring ("toute contribution s^2 * tenseur lisse") | DEFAUT de couverture | non testee par le script (un seul ansatz). Vraie par comptage de puissances (section 2.2) [derive], confirmee par les contre-exemples [calcule]. |
| t-3 (a) : -d_s^2(-d_s^2 ln s) | OK | = -6/s^4. Sur l'espace-temps 4D, box_eta = -d_s^2 + Laplacien ; ln s ne depend que de s, donc box_eta^2 ln s = d_s^4 ln s = -6/s^4, sans dependance en x, y, z [calcule, verifie en 4D complet]. |
| t-3 (b) : Riemann linearise, Ricci, Weyl | OK | formules standard ; Weyl sans trace verifie [calcule]. |
| t-3 (b) : T = 8b d^c d^d (phi_h C_acbd) | OK | conserve en eta par antisymetrie de C en (a,c), sans trace ; T_hat = s^2 T est le poids conforme correct d'un tenseur sans trace conserve (Omega = 1/s) [derive]. |
| t-3 (b) : famille phi_h = c1 s + c2 s^2 + c3 s^3 + c4 (x^2 + s^2) | DEFAUT de couverture | 4 parametres polynomiaux seulement ; l'affirmation porte sur tout phi_h lisse. Elargi dans wc_t23_indep.py (famille d'ondes avec dependance en y) et par l'argument general (section 2.3). |

## 2. Reproduction independante

### 2.1 t-1 (wc_t1_indep.py)

Choix deliberement differents de irt_a.py : densite integree par parties
sqrt(g)[sigma E - (2/3) R box sigma + c4((box sigma)^2 - 2 R^{ab} d_a sigma d_b sigma + (2/3) R (d sigma)^2)]
(meme equation d'Euler-Lagrange, densite differente) ; mode substitue avant variation ; fonction test F inseree dans chaque composante ; operateur d'Euler ecrit a la main ; g^-1 par serie de Neumann et sqrt(g) par serie automatique.

| c4 | composante | T_hat fond | (T_hat - 6 ghat) ordre e^0 | ordre e^1 |
|---|---|---|---|---|
| 2 | yy, zz, xx | 6/s^2 | 0 | 0 |
| 2 | ss | -6/s^2 | 0 | 0 |
| 2 | sx | 0 | 0 | 0 |
| -1/2 | yy, zz, xx | 17/(2 s^2) | 5/(2 s^2) | yy, zz : non nul (termes k^2 s^2) ; xx : 0 |
| -1/2 | ss | 3/(2 s^2) | 15/(2 s^2) | 0 |

[calcule] Le fond T_hat = 6 ghat et l'egalite d'ordre e, delta T_hat = 6 delta ghat, sont reproduits pour TOUTES les composantes. Le controle -1/2 reproduit exactement le residu yy de irt_a_ctrl.py. Le controle discrimine deux fois : fond non proportionnel a ghat (17/2 contre 3/2) et ordre e non proportionnel.

Consequence [derive] : T_hat = 6 ghat exactement a l'ordre e donne L_hat = (kap/2)(6 - 8) ghat = -kap ghat, nabla_hat ghat = 0, donc R = 0 de (2.17). Sans effet sur R.

### 2.2 t-2 (wc_t23_indep.py)

Comptage de puissances [derive] : L_hat = O(s^p) (le terme ghat trT_hat est du meme ordre que T_hat, car ghat ~ s^-2 et trT_hat ~ s^2 T_hat). Gam_hat = O(1/s), donc nabla_hat L_hat = O(s^(p-1)) et R = O(s^(p-2)). Pour p = 2 : R = O(1), sans aucune hypothese de conservation ni de trace, pourvu que Y et dY soient bornes en s = 0. Pour p = 1 : pole possible, de coefficient lineaire en Y(0).

Resultats [calcule] :

| Cas | trace | conserve | pole 1/s |
|---|---|---|---|
| p = 1, y generique | 0 | oui | OUI : s R_ysy -> kap y0 cos kx |
| p = 2, y generique | 0 | oui | non (R_ysy -> 3 kap y0 cos kx / 2, fini) |
| p = 1, y0 = 0 | 0 | oui | non (c'est en fait p = 2) |
| p = 2, Y_ss seul | non | non | non |
| p = 2, Y_sx seul | 0 | non | non |
| p = 2, Y_yy = Y_zz | non | non | non |
| p = 2, Y = w eta (pure trace) | non | non | non |
| p = 1, Y0 constant symetrique general (10 composantes) | | | pole sauf si Y0 = 0 (seule solution) |
| p = 2, Y = y0 ln s (non lisse) | 0 | oui | pas de pole, mais divergence logarithmique de R |
| p = 3/2 (non entier) | 0 | oui | pas de pole, mais divergence en s^-1/2 |

### 2.3 t-3

(a) [calcule] box_eta^2 ln s = -6/s^4 en 4D complet, sans dependance spatiale. Valide.

(b) Argument general [derive] : C (Weyl du mode) est lisse en s (u entier en s) ; si phi_h est lisse (C^3 suffit), T = 8b d d(phi_h C) est lisse, T_hat = s^2 T est de la forme s^2 x (tenseur lisse), donc pas de pole par 2.2. Reproduction [calcule] : famille du script et famille d'ondes [(c1 + c2 s) cos qs + (c3 + c4 s) sin qs] cos qy (box^2 = 0, dependance en y, composantes hors diagonale generees) : aucun pole, R fini en s = 0.

## 3. Contre-exemples

1. **t-2, s^2 Y non conserve ou avec trace** : aucun pole dans les quatre cas testes [calcule], conformement au comptage [derive]. Les hypotheses "conserve, sans trace" ne sont pas necessaires a la moitie "p = 2" de t-2 ; l'hypothese efficace est la regularite de Y.
2. **t-2, p = 1 avec y0 = 0** : pas de pole [calcule]. La moitie "p = 1 donne un pole" exige y0 = Y(s=0) non nul. Pour Y0 constant general, le pole ne disparait que pour Y0 = 0 [calcule], donc il n'existe pas de direction exceptionnelle sans pole a p = 1.
3. **t-3, phi_h non lisse** :
   - s^2 ln s : box^2 = -2/s^2, s^3 ln s : box^2 = 6/s [calcule]. Ni l'un ni l'autre n'est solution de box^2 = 0 ; ils ne sont donc pas des contre-exemples admissibles. Injectes quand meme, ils ne produisent pas de pole pour ce mode [calcule].
   - ln s (soit -sigma) : box^2 = -6/s^4, et produit un pole : s R_ysy -> -4 B b k^3 kap cos kx [calcule]. Cela illustre que l'absence de pole tient a la regularite de phi_h, et que la partie ln s doit etre exclue de phi_h (ce que t-3 (a) assure : ln s n'est pas homogene).
4. **Mode homogene de box^2 singulier en s = 0 ?**
   - Dependance en s seule : solutions = polynomes cubiques [calcule]. Par mode de Fourier spatial : f = (C1 + C2 s) sin qs + (C3 + C4 s) cos qs [calcule], entieres en s. Plus generalement, s = 0 n'est pas un point singulier de l'operateur a coefficients constants box^2 : une solution a donnees de Cauchy lisses sur une tranche s = s0 > 0 reste lisse a travers s = 0 [derive]. Pour s^alpha cos qx, box^2 = 0 identiquement exige q = 0 et alpha dans {0,1,2,3} [calcule]. Aucun mode homogene a pole uniforme en s.
   - Il existe des solutions singulieres portees par le cone de lumiere : 1/(r^2 - s^2), s/(r^2 - s^2), ln(r^2 - s^2), toutes avec box^2 = 0 [calcule]. Elles ne sont pas lisses ; ln(r^2 - s^2) se comporte comme 2 ln s + i pi sur l'axe r = 0 seulement. Exclues par l'hypothese "phi_h lisse" ; leur effet sur R (sur le cone et l'axe) n'a pas ete calcule. Point ouvert si phi_h physique est fixe par des conditions de bord qui admettent ce type de structure (forme de fonction de Green).

## 4. Jugements

| Affirmation | Verdict | Hypotheses |
|---|---|---|
| **t-1** | VALIDE SOUS HYPOTHESES | (H1) seul le terme Wess-Zumino de la partie Euler est varie, a sigma fixe ; la contribution de W[eta + e h] et les parties c (Weyl^2) et box R sont hors champ. (H2) coefficient a = 1 et convention T_ab = +(2/sqrt g) dS/dg_ab. (H3) ordre e, mode tensoriel donne. Sous ces hypotheses : T_hat = 6 ghat pour toutes les composantes, au fond et a l'ordre e [calcule, deux implementations independantes], donc R = 0 [derive]. Le controle -1/2 discrimine [calcule]. |
| **t-2** | VALIDE SOUS HYPOTHESES (enonce a preciser) | p = 1 : pole si et seulement si Y(s=0) non nul (y0 non nul) ; pour y0 = 0 pas de pole. p = 2 : pas de pole pour tout Y tel que Y et dY soient bornes en s = 0 ; conservation et trace nulle ne sont pas necessaires. Un Y non lisse (ln s) ou p non entier (3/2) donne une divergence non polaire. |
| **t-3** | (a) VALIDE ; (b) VALIDE SOUS HYPOTHESES | (a) box_eta^2 ln s = -6/s^4 en 4D [calcule]. (b) phi_h lisse en s = 0 (C^3 suffit) [derive], verifie sur deux familles [calcule] ; la preuve par le script seul (4 parametres) est insuffisante, l'argument general la complete. Aucun mode homogene a pole uniforme ; les solutions singulieres sur le cone sont exclues par l'hypothese de regularite et restent non instruites. |

Defauts releves dans les scripts : aucun defaut de fond. Defauts mineurs : couverture de t-1 limitee a yy (irt_a.py), docstring de t-2 plus generale que le test, famille phi_h restreinte en t-3 (b), code mort dans irt_a.py et irt_a_ctrl.py.
