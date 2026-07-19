---
id: LC-D-G3-M4-CHAINON
codename: LC-RACCORD
titre: "Chaînon-verdict m4-CHAÎNON (étape (b) de la séquence a→b sur β≡G3) — remplit le m4-chaînon laissé VACANT par LC-D-G3-ADMISSIBILITE v1.4. VERDICT (espace figé du cadrage §4) : SYMÉTRIQUE au sens du STATUT BINAIRE, AVEC m4 NON VACANT. La branche Δ₊=3 (g₍ₙ₎ Neumann/VEV, spin-2 TT sous-dominant) a, au sens de la norme FG-symplectique ∫z^{1-d}|f|²dz (d=3, μ=z^{-2}), un statut de (non-)normalisabilité L²-strict IDENTIQUE dans les deux signes de l'équation d'Einstein : convergente au bord z→0 (intégrande z⁴), DIVERGENTE dans le bulk z→∞ des DEUX côtés ⟹ NON-normalisable L²-strict AdS ET dS. MAIS la sign(Λ)-symétrie de l'INDICIEL {0,3} (établie au sceau a0b962c8) est CASSÉE au niveau du TAUX de divergence : loi EXPONENTIELLE en AdS (I_{3/2}, pente log(N)/b→2k) vs loi LINÉAIRE en dS (J_{3/2}, N∼b/(πk)). Le sceau TESTE donc désormais genuine-dS (m4 non vacant) — contrairement à a0b962c8/010a0562 — mais le test NE fournit PAS de verrou β propre (statut de normalisabilité inchangé par le passage AdS→dS). CONFIRMÉ par audit froid indépendant (passe S-m4-bis, Mode B, CONFIRMATION conditionnelle aux prémisses importées), après un premier tour S-m4 (RÉSERVE) ayant motivé le durcissement du sceau. ATTESTATION : établi (algèbre) — algèbre correcte et cibles reproduites indépendamment, RIEN de plus. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; β reste T-b ; N non fixé (≡Λ) ; O₂ non construit ; CCC non démontrée NI réfutée."
type: "chaînon-verdict (établi (algèbre)) — patch aval de LC-D-G3-ADMISSIBILITE (m4-chaînon rempli). NE bascule aucun front, NE construit rien, NE réduit aucun moyen. Grave la sortie d'un sceau algébrique auditée froid."
statut: "TERMINÉ pour ce lot — verdict SYMÉTRIQUE(statut)/m4-non-vacant gravé sur sceau durci verif_G3_m4_chainon.py (sha 9486b7b2…), cadrage gelé 2d4f167e…, audit froid CONFIRMATION (S-m4-bis). DEUX réserves d'intégrité consignées (non-infirmantes, cf. §5). UN résidu re-nommé (prescription-𝓘⁺, cf. §4). UNE friction de cadrage SOLDÉE v1.1 (§3↔§4.3, cf. §6 : découplage axe statut / axe m4, KB-only, ne réduit rien). β INCHANGÉ (T-b)."
version: 1.1
langue: fr
date: 2026-07-06
maj: "2026-07-06 — v1.1 : solde de la friction de cadrage §3↔§4.3 (item V53 §4.1, KB-only, sur GO Thierry). Ajout §6 RÉSOLUTION : découplage de l'axe STATUT (binaire, sélectionne la case §4) et de l'axe m4 (casse de signe sur convergence OU taux/phase, §3 — dit si le sceau teste genuine-dS). Le cas taux≠/statut= = SYMÉTRIQUE(statut) + m4 non-vacant, T-b maintenu. NE touche PAS le fichier-cadrage gelé (corps figé intact byte-exact, gel consommé 2d4f167e préservé — cible anti-fit pristine, disclosure R-7 au §6) ; NE change aucun verdict gravé (sélection §4.3 + complément m4-non-vacant inchangée) ; N'accorde aucun verrou. §6.4 : ne réduit rien ; {A4 ; A2★ ; N} INCHANGÉ ; β T-b. [v1.0] création. Consomme le cadrage gelé LC-WORK-CADRAGE-G3-M4-CHAINON v1.0 (R-36 2d4f167e…). Chaîne d'exécution : §0-lite PASS (baseline v2.49→v2.50 post-dépôt cadrage) → R-54 (ADM-IMPORTS v1.1 + ADMISSIBILITE v1.4 + TRANSPORT v0.4 lus sur mount) → sceau v1 (e452a49a, verdict pilote INDÉTERMINÉ) → audit froid S-m4 (RÉSERVE : 3 assertions vacantes, asymptotique de prose fausse log vs linéaire, mapping re-scopé, seuils non gelés) → durcissement (fork A) : sceau v2 (9486b7b2, verdict recalé SYMÉTRIQUE-statut) → re-audit froid S-m4-bis (CONFIRMATION, 2 réserves résiduelles). En discordance pilote/incognito, l'incognito a prévalu (R : le verdict INDÉTERMINÉ du pilote a été INFIRMÉ et corrigé en SYMÉTRIQUE-statut)."
prerequis_kb: [LC-WORK-CADRAGE-G3-M4-CHAINON, LC-D-G3-ADMISSIBILITE, LC-D-G3-ADM-IMPORTS, LC-D-G3-TRANSPORT, LC-D-O2-SCATTERING-FG, LC-D-GAMMA-NSTAR-ADS4]
renvois: [LC-D-G3-ADMISSIBILITE, LC-D-G3-ADM-IMPORTS, LC-D-G3-TRANSPORT]
tags: [chainon-verdict, etabli-algebre, m4-chainon, etape-b, sequence-a-b, beta, G3, L2-symplectique, branche-Delta3, spin-2-TT, genuine-dS, sign-Lambda-symetrie, casse-de-taux, statut-symetrique, m4-non-vacant, loi-exponentielle-AdS, loi-lineaire-dS, BP-2, audit-froid, S-m4, S-m4-bis, CONFIRMATION, reserve-integrite, friction-cadrage, residu-prescription-Iplus, R-53, R-54, §6.4, T-b, A4, A2star, N]
---

# Chaînon-verdict — m4-chaînon (étape (b)) : statut L²-symplectique de la branche Δ₊=3

> **En une phrase.** Le passage AdS→dS **casse la symétrie de signe au niveau du TAUX** de
> divergence de la norme symplectique de la branche `Δ₊=3` (exponentiel → linéaire), donc le
> sceau **teste enfin genuine-dS** (m4 non vacant) ; **mais** le **statut binaire** de
> (non-)normalisabilité L²-strict reste **le même** des deux côtés (non-normalisable), donc ce
> test **ne livre aucun verrou β propre**. `β` reste `T-b`.

## §0 — Provenance et pièces
- **Cadrage gelé** : `LC-WORK-CADRAGE-G3-M4-CHAINON` v1.0, gel R-36 sha `2d4f167e…` (hors-fichier,
  au manifeste). Question `Q-m4`, cibles `M4-1..M4-3`, firewall `m1..m5`+`mE`, espace de verdicts
  figé §4, tous fixés AVANT algèbre.
- **Sceau** : `verif_G3_m4_chainon.py`, sha `9486b7b28bd798860c4362ecc310194fd493f6d92799ee68923db3b309d2120a`
  (**durci** post-audit S-m4). 19 assertions, bloc `FW` de 3 mutations firewall auto-testées,
  seuils gelés, robustesse-mesure. Rejeu **19/19, EXIT 0** (SymPy 1.14.0, mpmath).
- **Audits froids** (incognito, pilote disqualifié, Mode B) : passe **S-m4** = **RÉSERVE** (motive le
  durcissement) ; passe **S-m4-bis** (sceau durci) = **CONFIRMATION** conditionnelle aux prémisses
  importées. Discordance pilote/incognito **tranchée en faveur de l'incognito** (le verdict pilote
  initial INDÉTERMINÉ a été infirmé).

## §1 — Solutions (M4-1)
ODE radiales (blocs A/C, `d=3`) : `z²f″ − 2z f′ ∓ k²z² f = 0`. Indiciel `s(s−3)`, racines `{0,3}`
**identiques aux deux signes** (régression sur `a0b962c8`). Solutions fermées
`f = z^{3/2} Z_{3/2}(κz)` : `κ` **réel** en AdS (`I,K` monotones), **imaginaire** en dS (`J,Y`
oscillants — 18/17 changements de signe sur `[5,60]`). Branche `Δ₊=3` (`∼ z³` au bord) portée par
`I_{3/2}` (AdS) et `J_{3/2}` (dS), **coefficient `z³` identique** `√2·k^{3/2}/(3√π)`. Re-dérivé
indépendamment par l'audit froid (`k=0.7`, résidus relatifs `≤10⁻¹³`).

## §2 — Norme FG-symplectique (M4-2), mesure `μ=z^{1-d}=z^{-2}` (`mE`)
- **Bord `z→0`** : intégrande `z^{2Δ+1-d} = z⁴` pour `Δ₊=3` ⟹ **converge**, **symétrique** aux deux
  signes (exposant sans signe). Régression : `Δ₋=0` donne `z^{-2}` ⟹ `∫₀` diverge (charnière
  `ADMISSIBILITE`, reproduite).
- **Bulk `z→∞`** : **divergent des DEUX côtés**, mais par **lois distinctes** —
  AdS **exponentielle** `N(b) ∼ e^{2kb}` (pente `log(N)/b → 2k`) ; dS **linéaire**
  `N(b) ∼ b/(πk)` (`pente_lin·πk → 1`). *Correction d'intégrité vs sceau v1 : la loi dS est
  **linéaire**, non « logarithmique » — établie par régression, confirmée analytiquement par
  l'audit (`I² ∼ e^{2kz}/2πkz` ; `J² ∼ 2cos²/πkz`, moyenne `1/πkz`).*
- **Robustesse** : le contraste exp/linéaire **survit** à `μ ∈ {−1,−2,−3}` ⟹ neutralise la
  contingence `z^{1-d}` vs `z^{2-d}` (audit S-m4).

## §3 — Verdict (M4-3), mappé dans l'espace figé §4
Prédicats **dérivés** (non posés) : `statut binaire identique` (non-norm des deux côtés) **VRAI** ;
`intégrale tranche` (diverge) **VRAI** ⟹ `INDÉTERMINÉ` **exclu** ; `dS converge` **FAUX** ⟹
`NORMALISABLE-dS` **exclu** ; `statut dS ≠ AdS` **FAUX** ⟹ `ASYMÉTRIQUE-NON-NORM` **exclu**.
**Unique case sélectionnée : `SYMÉTRIQUE` (§4.3)**, au sens du **statut binaire**.
**Complément non prévu par §4.3** : `m4` **NON vacant** — la casse de **taux** (exp vs linéaire)
**exhibe** une quantité différant AdS↔dS, satisfaisant l'exigence `m4` du firewall (§3 du cadrage :
« exposant de queue / phase asymptotique »). Cf. friction §6.

## §4 — Résidu re-nommé (hors ce lot)
La non-normalisabilité dS est de **type continuum** (mode oscillant, delta-normalisable). Statuer si
un tel mode est **admissible comme état** (vs strictement non-normalisable) requiert une
**prescription à la frontière conforme `𝓘⁺`** (Bunch-Davies / radiation / `iε`) **non dérivable
KB-only**. Cette question — distincte de `Q-m4`, qui portait sur la norme L²-stricte — est
**re-nommée `PRESCRIPTION-𝓘⁺`** et **routée hors ce lot** vers un cadrage neuf éventuel. Le présent
verdict tranche `Q-m4` (statut L²-strict), **pas** l'admissibilité-continuum.

## §5 — Réserves d'intégrité consignées (non-infirmantes)
Relevées par l'audit froid S-m4-bis, **portant sur deux tests décoratifs, non sur la substance** —
la substance étant portée par les fits de loi `M4-2.d/e` (re-dérivés indépendamment) :
- **FW-2 vacante** : la mutation compare trois évaluations **identiques** `N('J',20)` ; l'inégalité
  est fausse par construction, le firewall « m1 » **ne mord sur rien**. (`FW-1` et `FW-3` mordent.)
- **M4-3.b proxy surclamé** : le label annonce un « test réel de non-normalisabilité » mais teste la
  **croissance stricte** de `N(b)` (proxy à saturation numérique) ; la non-norm réelle est établie
  par `M4-2.d/e`. Conclusion vraie, label **surclamé**.
Ces deux points sont **connus et consignés** (transparence), **non masqués** ; ils n'altèrent ni le
statut symétrique ni la casse de taux (tous deux re-dérivés hors ces tests par l'audit).

## §6 — Friction de cadrage consignée (imputable au cadrage)
L'espace figé §4 est **intérieurement incomplet** : §3 (firewall) admet « exposant de queue / phase
asymptotique » comme quantité `m4` discriminante — **satisfaite ici** — tandis que §4.3 pose
« `SYMÉTRIQUE` ⟹ `m4` vacant ». Le cas **`taux≠ / statut=`** (symétrie cassée au taux, statut
binaire préservé) **n'était pas prévu**. Le présent chaînon le traite explicitement
(`SYMÉTRIQUE`-statut **+** `m4` non vacant) et **consigne la friction** ; la **révision de l'espace
de verdicts** pour couvrir proprement `taux≠/statut=` est **matière à un futur cadrage** (hors ce
lot).

**RÉSOLUTION `[v1.1, KB-only, ne réduit rien]`.** La friction se dissout en **découplant deux axes**
que l'espace figé §4 avait conflés :
- **Axe STATUT** (binaire : normalisable / non-normalisable) — **sélectionne la case §4**. Ici :
  non-norm des deux côtés ⟹ **§4.3 (`SYMÉTRIQUE`-statut)**.
- **Axe `m4`** (casse de signe sur une quantité observable — convergence, **exposant de queue,
  phase asymptotique** : §3 firewall) — dit **si le sceau teste genuine-dS**, INDÉPENDAMMENT du
  statut. Ici : taux **exp** (AdS) vs **linéaire** (dS) ⟹ **`m4` non vacant**.

Le rider de §4.3 « `SYMÉTRIQUE` ⟹ `m4` vacant » n'est valide que sous **`statut= ∧ taux=`**. Le cas
**`statut= ∧ taux≠`** (présent) est **`SYMÉTRIQUE`-statut + `m4` non-vacant**, et **maintient `T-b`**
(aucun verrou propre : le statut binaire est inchangé AdS→dS). Cette lecture à deux axes est à
**reprendre telle quelle** dans tout cadrage futur réutilisant l'espace §4.

**Disclosure anti-fit `[R-7]`.** Cette résolution est **postérieure au sceau** mais : (i) **ne change
aucun verdict gravé** — la sélection §4.3 + complément `m4`-non-vacant du présent chaînon est
**inchangée** ; (ii) **n'accorde aucun verrou `β`** (T-b avant, T-b après) ; (iii) **ne touche pas**
le fichier-cadrage gelé `LC-WORK-CADRAGE-G3-M4-CHAINON` — corps figé **intact byte-exact**, gel
consommé `2d4f167e` **préservé**, la cible anti-fit reste **pristine**. Effet de substance = **nul**
(§6.4).

## §7 — Effet sur le perimètre (R-53) et attestation
- `LC-D-G3-TRANSPORT` v0.4 : **reste `T-b`** (aucun verrou propre acquis).
- `LC-D-G3-ADMISSIBILITE` v1.4 : le **m4-chaînon cesse d'être VACANT** — genuine-dS est **désormais
  testé** (casse de taux) — **mais le test ne fournit pas de verrou β**. La direction
  `T-c`-conditionnelle est **ni convertie en verrou, ni infirmée** ; le résidu `BP-2` est **soldé
  côté `Q-m4`** (statut L²-strict tranché = symétrique) et **re-nommé** côté admissibilité-continuum
  (`PRESCRIPTION-𝓘⁺`, §4).
- **Attestation** : `établi (algèbre)` — algèbre correcte et cibles reproduites indépendamment
  (audit froid), **strictement rien de plus**. Aucune affirmation « D1 close / N fixé / β verrouillé /
  CCC démontrée ».

## §6.4 — Non-surclassement `[terminal]`
Trancher que le statut L²-strict de `Δ₊=3` est **symétrique** (non-normalisable des deux côtés) et que
la symétrie est **cassée au seul taux** ne **fixe NI `N` NI `Λ`**, ne **construit PAS `O₂`**, ne
**réduit PAS `A4`**, ne **tranche PAS `A2★`**, ne **ferme PAS `D1`**, et **ne verrouille PAS `β`**
(qui reste `T-b`). `{A4 ; A2★ ; N}` **INCHANGÉ**. CCC **non démontrée NI réfutée**.
(cf. `LC-D-G3-ADMISSIBILITE` v1.4, `LC-D-G3-ADM-IMPORTS` v1.1, `LC-D-G3-TRANSPORT` v0.4,
`LC-WORK-CADRAGE-G3-M4-CHAINON` v1.0)
