---
id: NOTE-BORD-EON-196-ARMEMENT-AF
numero: 196
serie: I
branche: G-V3 / Q-M3 (regularite formelle des termes anomaux ; chantier AF)
reservation: 2026-10-16T13:58:01Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 196)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant tout calcul : les termes locaux de Wess-Zumino b sigma C^2 (G-V3) et sigma F^2 (M-V3) au sens formel de Friedrich"
decision: "operateur (Thierry), 2026-10-16 15:52 Paris : « ok [...] pour continuer le programme » ; lecture retenue : pistes 4 et 3 du §11 de la reprise v10, traitees ensemble par la methode formelle de FW3"
amont: "NOTE-125 v2 (pole sur le mode de dS), NOTE-128 (audit), NOTE-133 (reduction d'ordre), NOTE-163 v2 (greffe G-CAL-a : point de lecture « autres inconnues lisses »), NOTE-98 (log de M-V3, champ uniforme), NOTE-108 v2 / 113 / 114 (critere sur solution <B_iB_j>_tf = <E_iE_j>_tf), NOTE-191 v2 (methode formelle en jets)"
---

# Gel AF : G-V3 et M-V3 au sens formel de Friedrich

## 0. Objet
G-V3 a ete etabli en evaluant le second membre de (2.17) sur une solution (mode tensoriel de de Sitter, NOTE-125). La greffe G-CAL-a (NOTE-163 v2) nomme la faiblesse logique : « un pole du second membre de (2.17) evalue sur une solution prouve l'irregularite au sens de Friedrich si les autres inconnues sont lisses sur cette solution », alors que W diverge en ln au premier ordre (NOTE-128). Le critere de Friedrich est **formel** (seconds membres comme fonctions des inconnues). Le chantier FW3 (NOTE-191 v2) a mis en place la methode en jets. Le present chantier ecrit le pole de G-V3, et le log de M-V3, comme des proprietes **formelles** des seconds membres, independantes de toute solution. Pertinence pour CCC + M : a M2 = 2, la masse physique des fermions charges y Omega H_r tend vers 0 a scri ; l'anomalie de trace QED des charges legeres y est celle du cas sans masse (Q-M3).

## 1. Cadre fixe
- Conventions de Friedrich (signature (-,+,+,+), ghat = Omega^-2 g) ; relations (2.14), (2.15) (facteur Omega^-1, precedent xiv), (3.8) ; procedure en jets de NOTE-191 v2.
- Premier ordre en perturbation autour de g = eta (de Sitter conformement plat) : termes lineaires en W (ou en F F pour AF-2) ; produits de deux quantites du premier ordre (L W, S W, matiere x W) ecartes ; a cet ordre, d_a d_b Omega = s eta_ab, d_c s = 0, n.n = -lambda/3 + 2 Omega s.
- **AF-1 (partie c)** : T_ab = c0 b nabla^c nabla^d (sigma C_acbd) + O(courbure^2), sigma = -ln Omega, That_ab = Omega^2 T_ab (convention et c0 de irr_c.py, NOTE-125 : c0 = -8 avec le c0 du script ; le signe suit la convention de T, NOTE-128). **Substitution formelle C_acbd = Omega W_acbd** (definition de Friedrich), W tenseur de Weyl generique (symetries de Weyl, trace nulle) et ses derivees jusqu'a l'ordre 3 comme inconnues independantes (jets). **Reduction d'ordre** (NOTE-133) : la divergence d^d W_abcd est remplacee par sa valeur d'ordre zero en b, J_abc (vide : J = 0 ; matiere classique : J regulier, FW3).
- **AF-2 (sigma F^2)** : terme de Wess-Zumino beta_* Int sqrt(g) sigma F_ab F^ab (forme de S2, NOTE-98 : S_B = -(beta~/2e^2) Int sqrt(g) Omega[g] F^2), beta_* symbolique. F (poids 0) et ses derivees comme inconnues. Equation de Maxwell modifiee rescalee ; That = beta_* (ln Omega) Omega^2 M_ab[F; eta] + Maxwell classique, M tenseur de Maxwell (sans trace).

## 2. Questions figees
- **AF-1.** Developpement de Laurent (puissances de Omega et ln Omega) de That_ab et du second membre de (2.17), comme fonctions des inconnues (n, s, W et jets, J). Quelle est la plus basse puissance ? Son coefficient est-il une fonction non identiquement nulle des inconnues, et laquelle (structure en n et E_ab = n^c n^d W_acbd) ? Les termes en ln Omega sont-ils tous proportionnels a la divergence de W (donc nuls dans le vide apres reduction d'ordre, presents en J avec matiere classique) ?
- **AF-2.** L'equation de Maxwell rescalee, avec le terme sigma F^2, a-t-elle un second membre formellement singulier (Omega^-1, de coefficient lie a n^a F_ab) ? Coefficient de ln Omega dans (2.17), comme fonction de (n, F) : non identiquement nul ? Condition algebrique de son annulation.
- **AF-3 (calibration et concordance).** (i) Le coefficient formel de AF-1 evalue sur le mode de NOTE-125 redonne-t-il R_ysy|pole = -4 b kappa B k^3 cos kx / s (c0 du script) ? (ii) Le coefficient formel de AF-2 evalue sur le champ magnetique uniforme de NOTE-98 redonne-t-il les coefficients de ln Omega (-kappa beta~ B0^2/e^2 sur (1,0,1), (2,0,2) ; +2 x sur (3,0,3)) a la normalisation pres ? (iii) Comment la condition formelle d'AF-2 se compare-t-elle au critere sur solution de NOTE-113/114 (<B_iB_j>_tf = <E_iE_j>_tf) : identique, plus forte, ou differente ?
- **AF-4 (bilan).** G-V3 et M-V3 deviennent-ils des enonces formels au sens du theoreme 3.1 (regulier ssi b = 0 ; ssi beta_* = 0), levant la reserve G-CAL-a ? Ce qui reste hors champ.

## 3. Espace de verdicts
- **AF-V0** : non concluant (coefficient non isole, calibration impossible).
- **AF-V1** : G-V3 et M-V3 sont des irregularites formelles : (2.17) porte un terme Omega^-1 (AF-1) et un terme ln Omega ou plus singulier (AF-2) dont les coefficients sont des fonctions non identiquement nulles des inconnues ; calibrations (i) et (ii) reussies ; la reserve G-CAL-a est levee.
- **AF-V2** : un seul des deux est formel (l'autre n'existe que sur solution, ou ses coefficients s'annulent formellement).
- **AF-V3** : les coefficients formels s'annulent identiquement ; le pole de NOTE-125 provient de l'evaluation sur une solution non lisse ; G-V3 doit etre reformule.
- **AF-V4** : la calibration (i) ou (ii) echoue (incoherence avec NOTE-125 ou NOTE-98) : revision obligatoire de la chaine.

## 4. Prediction (informee, precedent ix)
**AF-V1.** Motifs ecrits avant tout calcul : (AF-1) d d sigma = -s eta/Omega + n n/Omega^2 et d sigma = -n/Omega ; avec C = Omega W, (d d sigma) C ~ n n W/Omega et 2 (d sigma)(d C) ~ -2 n n W/Omega - 2 n dW : T = c0 b [-E/Omega - (n^c d^d + n^d d^c) W_acbd + ...], That = -c0 b Omega E + O(Omega^2) (concorde avec « That_ij = -+ 8 b Omega W_sisj », NOTE-128), d'ou un terme Omega^-1 dans (2.17) de coefficient proportionnel a kappa c0 b et a une combinaison de n et E ; les termes en ln Omega viennent de sigma d d C : ils contiennent d d Omega . W (trace nulle : 0 a cet ordre), n . div W et Omega d div W : nuls dans le vide apres reduction d'ordre, ln Omega x J avec matiere classique (concorde avec S-b, NOTE-128). (AF-2) la variation de beta_* sigma F^2 donne une equation de Maxwell d^a F_ab = (beta_*' n^a F_ab)/Omega + ... : **pole Omega^-1 dans l'equation de matiere**, de coefficient la partie electrique de F relative a n (plus fort que le log de M-V3) ; dans (2.17), ln Omega x kappa beta_* x (combinaison de n et M). (AF-3) (i) et (ii) reussies ; (iii) **incertain** : le critere formel porte sur F au point (algebrique), celui de NOTE-113 sur une solution ou F lui-meme recoit des corrections en ln ; prediction declaree faible : la condition formelle est plus forte que celle de NOTE-113.

## 5. Firewall
- FW-1 : regularite formelle (seconds membres en fonction des inconnues, en jets), jamais une valeur sur solution, sauf pour les calibrations AF-3 (i), (ii), declarees comme telles.
- FW-2 : identites verifiees symboliquement (script scelle avec sa sortie) ; la reduction d'ordre est appliquee par resolution lineaire explicite des contraintes de divergence sur les jets, pas par simplification a la main.
- FW-3 : calibrations obligatoires (AF-3 (i), (ii)) avant toute conclusion.
- FW-4 : audit froid aveugle (cecite stricte + adverse) avant toute greffe ; equations de la source recopiees depuis l'extrait archive et verifiees par script avant le gel d'audit (precedent xiv).
- FW-5 : aucune modification de NOTE-138 v4, NOTE-163 v2 ni S27-02 dans ce chantier ; propositions seulement.
- FW-6 : hors champ declare : partie a (Euler) de Wess-Zumino au sens formel (le resultat sur solution NOTE-131 reste en vigueur) ; partie non locale Gamma[g] (classe Hadamard, NOTE-146 v3) ; ordre superieur en perturbation ; existence ; resommation ; jauge gravitationnelle (objection 1 de NOTE-163).

## 6. Non-surclassement
Rien de grave. G-V3 candidat, M-V3 candidat conditionnel ; RG-4 refutee a titre provisoire ; CCC + M ouverte ; p_Q non fixe, N non chiffre, noyau {A4 ; A2★ ; N} inchange.
