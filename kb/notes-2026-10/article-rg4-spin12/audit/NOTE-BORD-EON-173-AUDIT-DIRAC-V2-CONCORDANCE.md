---
id: NOTE-BORD-EON-173-AUDIT-DIRAC-V2-CONCORDANCE
numero: 173
serie: I
branche: Chantier D (audit article RG-4 spin 1/2 v2)
reservation: 2026-10-14T17:56 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 173)
date: 2026-10-14
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-172-ARMEMENT-AUDIT-DIRAC-V2.md, sha256 692f030de113e342, sceau NOTE-172-SCEAU.txt 2026-10-14T17:56:16Z"
rapports: "RAPPORT-DA1.md sha256 2aeac72f1c87bf23 ; RAPPORT-DA2.md sha256 7ae90ba4888608f0"
---

# Concordance de l'audit froid aveugle de l'article RG-4 spin 1/2 v2

## 0. Deroulement
Gel scelle a 17:56:16Z avant tout lancement. DA-1 (derivation en cecite stricte, consigne seule) et DA-2 (audit adverse du source v2 et du script v2) lances en parallele, isoles, sans acces au corpus ni au web. Rapports rendus vers 18:03Z (DA-1) et 18:06Z (DA-2). Aucune lecture de source nouvelle par l'assistant pendant l'audit.

## 1. Criteres

| Critere | DA-1 (aveugle) | DA-2 (adverse) | Concordance |
|---|---|---|---|
| C-1 Prop. 1 | retrouve : u = e^{i beta mu ln abs(eta)} v, v -> v0 != 0, abs(v - v0) = O(abs(eta)), pas de limite pour tout k | correct ; borne verifiee sur le systeme 4x4 (rapport < 0,87) ; forme exacte de la phase limitee a dS exact, cadre reel FLRW plat | **oui**, correction de portee |
| C-2 Prop. 2 | retrouve (a) faux en general, (b) seules les solutions particule ou antiparticule pures convergent, lambda = +- mu ln abs(eta), A_eta ~ m/(qH eta) non integrable, (c) regulier en temps physique, (d) aucune jauge avec psi_hat et A continus | correct ; **deux erreurs de signe** (potentiel transforme -e^{-1} d lambda ; A_t -> A_t + m/e) ; extension a lambda(eta, x) | **oui**, signes corriges |
| C-3 Prop. 3 | retrouve rho_hat = m a (n+ - n-) + O(1), invariant de jauge, masse au repos d'une poussiere ; difference a une particule independante de la renormalisation (verifiee sur un Fock a 3 modes) | calcul et invariance corrects ; **lacune** : les modes de frequence positive de Bunch-Davies ne sont pas purement particule a temps tardif (poids antiparticule 1/(e^{2 pi m/H}+1), 5 chiffres) ; la conclusion tient avec Omega rho_hat -> m tanh(pi m/H) norme(f)^2 > 0 | **oui**, argument quantique corrige |
| C-4 Lemme 2 | retrouve dans la classe lineaire, hermitienne, d'ordre <= 1 : masse effective constante, convergence ssi m_eff = 0 (ex. m + xi R = 0) | **faux tel qu'enonce** : contre-exemples dans la classe ecrite (terme cinetique axial Z2^2 > Z1^2, masse tachyonique ; coefficients non hermitiens, masse nilpotente ; terme de Majorana) ; correct apres restriction (action reelle, U(1)-invariante, Z1^2 > Z2^2) | **non pour l'enonce v2** ; **oui pour la classe restreinte** (les deux auditeurs) |
| C-5 Prop. 4 | retrouve (a) ssi int m dt fini, (b) ssi m = O(e^{-Ht}), (c) ssi m = Omega F(Omega) lisse ; ordre strict ; **meme exemple** m = m0 e^{-Ht/2} | correct ; manque un exemple (b) non => (c) : m = Omega (1 + Omega^{1/2}) | **oui** |
| C-6 Script | (sans objet) | conforme a la section Verification ; faiblesses de methode et de documentation (C9) | **oui**, documentation corrigee |

Hors criteres, DA-2 releve un point **bloquant** sur la Prop. 5(c) (« aucun couplage local de la classe ne change cela ») : le couplage (m - l R) psi_bar psi avec l = m/(12 H^2) annule la masse effective sur dS (et donne m_eff ~ a^{-3} sur Lambda-CDM). C'est coherent avec DA-1 Q6 (« convergence ssi m_eff = 0, par ex. m + xi R = 0 »). La Prop. 5(c) etait donc fausse telle qu'ecrite ; l'obstruction subsiste pour toute masse effective constante non nulle, et ne disparait que par ajustement fin d'une echelle nouvelle contre H_inf.

Autres points DA-2, retenus : convention de Clifford a declarer ({gamma, gamma} = -2g) ; signe du poids dans la Definition 1 ; premisse de la Prop. 5 inutile pour (a) et insuffisante pour (b) (un mode classique equilibre a rho_hat borne : la premisse doit porter sur une particule au sens de la §4.3) ; parenthese sur les equations d'Einstein conformes non justifiee ; references non verifiees par DA-2 (pas de web ; deja verifiees par titre au corpus pour 1311.0700, 1309.7248, 2503.24263).

## 2. Verdict
**AU-V3 partiel**, au sens du gel : un enonce porteur (Lemme 2, classe telle qu'ecrite en v2) est invalide, et la Prop. 5(c) qui en dependait est fausse telle qu'ecrite. **AU-V2** sur C-1, C-2, C-3, C-5, C-6 : enonces porteurs confirmes, dont deux a l'aveugle par DA-1 avec le meme exemple separateur, corrections mineures (signes, portee, argument quantique). Le Lemme 2 restreint est confirme par les deux auditeurs.

**Prediction (AU-V2) partiellement non realisee** : la correction attendue sur le Lemme 2 (cas Z1^2 = Z2^2) etait en dessous du defaut reel (classe trop large, et consequence fausse en Prop. 5(c)) ; la correction attendue sur la portee quantique est realisee, sous une forme plus precise (facteur tanh(pi m/H)).

## 3. Consequence (fixee au gel, appliquee)
AU-V3 : la greffe S26-02 v2 n'est entee que pour les enonces confirmes (NOTE-174). L'enonce invalide est retire de l'article : le Lemme 2 de la v2 est remplace par sa version restreinte, confirmee par les deux auditeurs, et la Prop. 5(c) est reecrite (« masse effective constante non nulle » ; ajustement fin signale). Article v2.1 : `dirac-mass-scri-v2.1.tex`, 8 p., toutes les corrections B1, A1 a A4, C1 a C3, C5, C8, C9 integrees ; C4 (lambda(eta, x)) et C6 integrees par mention ; C7 cosmetique (cle bibliographique) sans effet.

## 4. Ce que l'audit ne vaut pas
Deux auditeurs IA isoles, le meme jour (precedent x) : cela ne vaut pas lecture humaine exterieure. Le grade de RG-4 (refutee a titre provisoire) est inchange.

## 5. Non-surclassement
Rien de grave. p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
