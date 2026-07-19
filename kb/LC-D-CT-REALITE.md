---
id: LC-D-CT-REALITE
titre: "Module D / dS-CFT — LA RÉALITÉ de C_T en dS, CADRÉE ET SCELLÉE (algèbre) PAR TROIS RÉSULTATS + UN TEST DE REPORT D'ERREUR. Successeur de LC-D-CT-ATN (qui a scellé A_T·N=16, le verrouillage C_T∝N en MAGNITUDE et la convergence des deux routes, en ISOLANT la signature non-unitaire SANS trancher la réalité de C_T continué). Exécute la recommandation principale de LC-WORK-REPRISE-POST-NONLIN-VERROU §4 (« réalité de C_T en dS — dernier `à inventer` connexe »). Ce chaînon SCELLE (verif_D_CT_realite.py, EXIT 0, 20 asserts) : [A] CONTINUATION — sur C_T∝c0·ℓ^{d-1}/G, la continuation ℓ_AdS→iℓ_dS attache un facteur i^{d-1} c0-INDÉPENDANT (parité de la puissance de ℓ) : d=2 imaginaire, d=3 RÉEL NÉGATIF, d=4 imaginaire ⟹ en d=3 le C_T continué est RÉEL NÉGATIF, PAS imaginaire (l'« imaginaire/négatif » des chaînons antérieurs était une importation du cas d=2 de Strominger) ; [B] MAGNITUDE vs SIGNÉ — |C_T|=N/(32π²)>0 (sceau ATN) et C_T_signé(d=3)=−N/(32π²)<0 sont DEUX objets distincts (le sceau calcule la magnitude, la continuation attache le signe) : AUCUNE contradiction ; [C] REPORT D'ERREUR (le cœur) — l'observable 𝒫=2H²/(M_Pl²k³) ne dépend que de |Im F| (magnitude) ; sous injection d'une erreur de réalité (partie réelle arbitraire δr) ET de signe (s=±1), l'observable est INVARIANT (δr∉free_symbols ; identique s=±1) alors que C_T_signé PORTE l'erreur (δr∈free_symbols) ⟹ PARE-FEU : report NUL vers l'observable, les `établi` amont sont ROBUSTES au verdict de réalité. DÉCISION OUVERTE (NON scellée comme physique) : [D] LECTURE — C_T<0 n'est pas une charge centrale unitaire (l'unitarité exige C_T>0) ; que ce soit une obstruction de fond (vraie CFT unitaire requise) ou bénin (générateur de fonctions, vue de Maldacena) DÉPEND de l'item déjà catalogué « CFT de raccordement non construite » ⟹ la réalité de C_T ne crée PAS d'obstruction indépendante : elle se RABAT sur cet item (CONSOLIDATION : moins de `à inventer` distincts ; PAS de réduction du compte {A4 ; A2★ ; N}). SANS SURCLASSEMENT (§6.4) : « report nul + C_T<0 (algèbre) » ≠ « D1 fermé / CCC établie ». D1 NON clos ; (A) physique conditionnel au seul A2★ INCHANGÉ ; survie au crossover et fixation de N (circularité LC-E) INCHANGÉS."
codename: LC-RACCORD
tags: [module-D, module-E, ds-cft, charge-centrale, C_T, realite, non-unitarite, continuation, i-puissance-d, parite, magnitude, signe, report-erreur, pare-feu, observable, A_T, N-holographique, verrouillage, CFT-raccordement, consolidation, sceau, D1]
type: chaînon (résultat — cadre et scelle (algèbre) la réalité de C_T en dS ; successeur de LC-D-CT-ATN ; exécute la reco principale de LC-WORK-REPRISE-POST-NONLIN-VERROU §4 ; SCEAU FAIT verif_D_CT_realite.py)
statut: établi (algèbre), SCEAU FAIT — [A] facteur de continuation i^{d-1} c0-indépendant (d=3 RÉEL NÉGATIF, pas imaginaire) ; [B] magnitude |C_T|=N/(32π²)>0 et signé C_T(d=3)=−N/(32π²)<0 sont deux objets distincts (pas de contradiction) ; [C] REPORT D'ERREUR NUL — l'observable 𝒫=2H²/(M_Pl²k³) est invariant sous perturbation de réalité/signe de C_T (δr,s), les `établi` amont robustes. Décision ouverte / à inventer (NON scellé comme physique) : [D] nature (obstruction de fond vs bénin) du C_T<0 = item « CFT de raccordement » (consolidation, pas réduction du compte) ; survie au crossover ; fixation de N (circularité LC-E, non brisée). D1 NON clos.
version: 0.2
langue: fr
date: 2026-06-09
maj: "2026-06-09 — v0.2 : renvoi — LC-D-CT-DUAL v0.1 (dualité graviton-dual de de Haro, étage S1/AdS, verif_D_CT_dual.py EXIT 0) pose la BASE AdS de la 2e route au signe et PROTÈGE ce chaînon : le « − » relatif de W̃ NE retourne PAS C_T (garde-fou C̃_T=+C_T en AdS ; le « − » de W̃ compensé par le « −2 » de ⟨T̃⟩) ⟹ le i^(d-1) de la route électrique [A] n'est PAS compté deux fois. Aucune touche algèbre. | 2026-06-09 — v0.1 : scelle la réalité de C_T en dS (reco principale de LC-WORK-REPRISE-POST-NONLIN-VERROU §4). verif_D_CT_realite.py (EXIT 0, 20 asserts, 4 blocs) : [A] continuation i^{d-1} c0-indépendante (parité de la puissance de ℓ ; d=2 imag, d=3 RÉEL<0, d=4 imag) ; [B] magnitude (sceau ATN) vs signé (continuation) — deux objets, pas de contradiction, C_T_signé(d=3)=−N/(32π²) ; [C] test de report d'erreur — observable invariant sous (δr,s), δr∈C_T_signé mais ∉observable (pare-feu) ; [D] lecture [décision ouverte, NON scellé] — C_T<0 non unitaire, se rabat sur l'item raccordement (consolidation). SANS SURCLASSEMENT (§6.4) : algèbre correcte + cibles reproduites, JAMAIS « D1 fermé ». Aucune touche aux chaînons existants (algèbre ATN intacte). Propagation §6 NON exécutée (proposée)."
statut_id: validé après sceau — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §6) : LC-D-CT-ATN §6 (renvoi : réalité cadrée), LC-D-HOLOGRAPHIE-G3 §3 (non-unitarité précisée), LC-AUDIT-VERDICT §8bis, LC-00-INDEX, 03_glossaire, 02_programme, 04_references.
fichier_compagnon: verif_D_CT_realite.py
prerequis_kb: [LC-D-CT-ATN, LC-WORK-CT-CADRAGE, LC-D-HOLOGRAPHIE-G3, LC-E-PLANCK-RESIDUEL, LC-D3-SPECTRE-K3, LC-D3-WEYL-BUNCHDAVIES, LC-AUDIT-VERDICT, LC-WORK-REPRISE-POST-NONLIN-VERROU, LC-00-INDEX]
fichiers_compagnons_kb: [verif_D_CT_ATN.py, verif_E_planck.py, verif_D3_spectre_k3.py]
renvois: [LC-D-CT-ATN, LC-WORK-CT-CADRAGE, LC-D-HOLOGRAPHIE-G3, LC-E-PLANCK-RESIDUEL, LC-D3-SPECTRE-K3, LC-D3-WEYL-BUNCHDAVIES, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] holographie — précise la signature non-unitaire dS/CFT : en d=3 le C_T continué est RÉEL NÉGATIF (parité de ℓ^{d-1}), non imaginaire ; et la réalité de C_T se rabat sur l'item « CFT de raccordement »."
  - "[E] retour de l'échelle — confirme que le verrouillage C_T~N est en MAGNITUDE (|C_T|=N/(32π²)>0) ; le signe vit dans la continuation, pas dans le compte N ; circularité LC-E inchangée."
  - "[A] / front (a) / D1 — le résidu gaussien A_T (=16/N) et l'observable 𝒫 sont ROBUSTES au verdict de réalité de C_T (report nul) ; D1 non clos ; (A) physique conditionnel au seul A2★ inchangé."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·C_T·réalité — Réalité de `C_T` en dS, cadrée et scellée (algèbre)

> **But.** `LC-D-CT-ATN` a scellé `A_T·N=16`, le verrouillage `C_T∝N` (en **magnitude**) et
> la convergence des deux routes, en **isolant** la signature non-unitaire dS/CFT mais **sans
> trancher** la réalité de `C_T` continué (laissée `à inventer`). Ce chaînon traite la question —
> recommandation principale de `LC-WORK-REPRISE-POST-NONLIN-VERROU §4` — et la **scelle au niveau
> algèbre** (`verif_D_CT_realite.py`, EXIT 0, 20 asserts).
>
> **Verdict (calculé, `verif_D_CT_realite.py`, EXIT 0 ; 4 blocs).**
> **[A] Continuation `i^{d-1}`** `[établi — algèbre]`. Sur `C_T∝c0·ℓ^{d-1}/G`, la continuation
> dS/CFT `ℓ_AdS→iℓ_dS` attache un facteur `i^{d-1}` **indépendant de la normalisation `c0`**
> (parité de la puissance de `ℓ`) : `d=2` imaginaire, **`d=3` RÉEL NÉGATIF**, `d=4` imaginaire.
> ⟹ **en `d=3`, le `C_T` continué est réel négatif, pas imaginaire** ; l'« imaginaire/négatif »
> des chaînons antérieurs était l'importation du cas `d=2` (Strominger, `c∝ℓ¹`).
> **[B] Magnitude vs signé** `[établi — algèbre]`. `|C_T|=N/(32π²)>0` (sceau ATN) et
> `C_T_signé(d=3)=−N/(32π²)<0` sont **deux objets distincts** : le sceau calcule la **magnitude**
> (prescription `|Im F|`), la continuation attache le **signe**. **Aucune contradiction.**
> **[C] Report d'erreur** `[établi — algèbre ; le cœur]`. L'observable `𝒫=2H²/(M_Pl²k³)` ne
> dépend que de `|Im F|` (magnitude). Sous injection d'une **erreur de réalité** (partie réelle
> arbitraire `δr`) **et de signe** (`s=±1`), l'observable est **invariant** (`δr∉free_symbols` ;
> identique `s=±1`) alors que `C_T_signé` **porte** l'erreur (`δr∈free_symbols`). ⟹ **pare-feu :
> report nul** ; les `établi` amont sont **robustes au verdict de réalité**.
> **[D] Lecture** `[décision ouverte — NON scellée comme physique]`. `C_T<0` n'est pas une charge
> unitaire (l'unitarité exige `C_T>0`) ; obstruction **de fond** ou **bénin** selon que le
> raccordement exige une *vraie CFT unitaire* (alors obstruction) ou un simple *générateur de
> fonctions* (alors bénin, vue de Maldacena). Or « vraie CFT unitaire » **est** l'item déjà
> catalogué « CFT de raccordement non construite » ⟹ la réalité de `C_T` **se rabat** dessus.
>
> **Donc : consolidation** (deux `à inventer` — réalité de `C_T` ; CFT de raccordement — sont **le
> même**), **pas réduction du compte** `{A4 ; A2★ ; N}`. **Rien n'est surclassé** (§6.4). `[D1 non
> clos ; (A) physique conditionnel au seul A2★ inchangé ; circularité LC-E non brisée]`

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce chaînon **scelle l'algèbre** d'une question de réalité ; il ne ferme pas D1. Ce qui est
`établi (algèbre)` : les trois résultats `[A][B][C]` du verdict, tous reproduits par
`verif_D_CT_realite.py`. Ce qui reste `décision ouverte / à inventer` : la **nature** (obstruction
de fond vs bénin) du `C_T<0`, qui **n'est pas** un objet algébrique mais dépend de l'item « CFT de
raccordement » (`[D]`) ; la **survie au crossover** ; la **fixation de `N`** (circularité `LC-E`,
**non brisée**). Discipline `LC-AUDIT-VERDICT §6.4` : un `établi` de sceau atteste que **l'algèbre
est correcte et les cibles reproduites**, jamais « la physique de la CCC est établie ».

**Statut adossé (aucun sceau neuf au-delà de celui-ci)** : `A_T·N=16`, verrouillage `C_T∝N` en
magnitude, convergence des routes, signature isolée (`verif_D_CT_ATN.py`) ; `N=S_dS`
(`verif_E_planck.py`) ; forme `⟨TT⟩∝k³`, `Δ=d=3` (`verif_D3_spectre_k3.py`). **L'algèbre d'ATN
n'est pas touchée** — ce chaînon l'**éclaire** (magnitude vs signe).

---

## 1. La réduction, en une ligne `[ce que le sceau confirme]`

Le sceau ATN avait laissé un seul `à inventer` connexe : la **réalité** de `C_T` continué. Ce
chaînon montre, en algèbre, que cette question **ne contamine rien en amont** et **ne crée rien de
neuf en aval** :

$$\boxed{\;C_T^{\text{signé}}(d{=}3)=i^{2}\,|C_T|=-\frac{N}{32\pi^{2}}<0\ \ (\text{réel}),
\qquad \mathcal P=\frac{2H^2}{M_{\rm Pl}^2k^3}\ \text{INVARIANT (report nul)},$$
$$\text{réalité de }C_T\ \equiv\ \text{item « CFT de raccordement »}\ \ (\text{consolidation}).\;}$$

La réalité de `C_T` n'est **plus** un `à inventer` flottant : c'est un **réel négatif** (parité
`d=3`), **insulé** de l'observable, et **identifié** à l'obstruction-raccordement déjà listée.

---

## 2. La continuation `i^{d-1}` — parité de la puissance de `ℓ` `[établi — algèbre]`

La continuation dS/CFT est `ℓ_AdS→iℓ_dS` (`Λ→−Λ`). La charge centrale de bord scale comme
`C_T∝c0·ℓ^{d-1}/G` ; la continuation attache donc `i^{d-1}`, **insensible à `c0`** :

| `d` | `C_T∝ℓ^{d-1}` | facteur `i^{d-1}` | nature |
|---|---|---|---|
| `2` | `ℓ¹` | `i` | **imaginaire** (cas Strominger) |
| `3` | `ℓ²` | `−1` | **réel négatif** ← le cas qui nous concerne |
| `4` | `ℓ³` | `−i` | imaginaire |

C'est le **même type de fait dimensionnel** que `(P3)` (pas d'anomalie en `d` impair) : une **parité**
qui tranche entre deux régimes. Ici, parité de `d−1` : **paire** (`d=3`) ⟹ réel ; **impaire**
(`d=2,4`) ⟹ imaginaire. Le `C_T<0` de `d=3` est donc **structurel** (pas un artefact de
normalisation), et **distinct** de l'« imaginaire » `d=2` qui était importé par analogie.

---

## 3. Magnitude vs signé, et le test de report d'erreur `[établi — algèbre]`

**Pas de contradiction `[B]`.** Le sceau ATN calcule une **magnitude** (réponse holographique
`~|Im F|_fini`, positive par construction) : `|C_T|=M_Pl²/(4H²)=N/(32π²)>0`. La continuation,
elle, attache le **signe** : `C_T_signé(d=3)=−|C_T|<0`. Magnitude (`>0`) et signé (`<0`) sont **deux
nœuds distincts** du graphe de valeurs — il n'y a aucune valeur contradictoire.

**Report d'erreur nul `[C — le cœur]`.** L'observable physique `𝒫=2H²/(M_Pl²k³)` ne dépend que de
`|Im F|_fini` (la **magnitude**). On **injecte une erreur** dans le coefficient fini : une partie
réelle arbitraire `δr` (modèle d'une **réalité fausse** de `C_T`) **et** un signe `s∈{+1,−1}`
(modèle d'une **ambiguïté de signe**). Résultat scellé :

- l'observable est **invariant** : identique pour `s=±1`, et `δr∉free_symbols(𝒫)` ;
- `C_T_signé` **porte** l'erreur : `δr∈free_symbols(C_T_signé)`.

⟹ **pare-feu** : l'erreur de réalité/signe vit **strictement en aval** du nœud-magnitude et **ne
remonte pas** vers l'observable. Les `établi (algèbre)` amont — `A_T·N=16`, le verrouillage en
magnitude, la convergence des deux routes — sont donc **robustes au verdict de réalité, quel qu'il
soit**.

<svg width="100%" viewBox="0 0 680 565" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Graphe de dépendances des valeurs : la réalité/signe de C_T ne se reporte pas sur l'observable</title>
  <desc>Les entrées H et G alimentent A_T égale seize G H carré sur pi et N égale pi sur G H carré égale S_dS, qui se combinent en A_T fois N égale seize, nombre pur où H et G se simplifient (établi). De là, la magnitude de C_T égale N sur trente-deux pi carré (établi) : c'est le pare-feu. Il se sépare en deux branches insulées. À gauche, l'observable carré du module de h, réel, ne dépend que de la magnitude de la partie imaginaire de F, donc insensible au signe de C_T (branche sûre). À droite, la continuation ell AdS vers i ell dS attache le signe i puissance d moins un ; en d égale trois cela donne C_T signé réel négatif, qui est le même item à inventer que la CFT de raccordement. Une erreur sur le signe ou la réalité de C_T ne remonte pas vers l'observable.</desc>
  <defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#534AB7" stroke-width="1.5"/></marker></defs>
  <rect x="220" y="44" width="240" height="44" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.6"/>
  <text x="340" y="71" text-anchor="middle" font-size="13" fill="#444441">H, G — fond dS, conventions</text>
  <line x1="320" y1="88" x2="216" y2="118" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="360" y1="88" x2="464" y2="118" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="110" y="120" width="190" height="44" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="205" y="147" text-anchor="middle" font-size="13" fill="#0F6E56">A_T = 16GH²/π</text>
  <rect x="380" y="120" width="190" height="44" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="475" y="147" text-anchor="middle" font-size="13" fill="#0F6E56">N = π/(GH²) = S_dS</text>
  <line x1="205" y1="164" x2="300" y2="194" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="475" y1="164" x2="380" y2="194" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="200" y="196" width="280" height="56" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="340" y="218" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">A_T · N = 16</text>
  <text x="340" y="238" text-anchor="middle" font-size="11.5" fill="#0F6E56">nombre pur · H,G se simplifient</text>
  <line x1="340" y1="252" x2="340" y2="278" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="210" y="280" width="260" height="56" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="1.1"/>
  <text x="340" y="302" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">|C_T| = N/(32π²)</text>
  <text x="340" y="322" text-anchor="middle" font-size="11.5" fill="#0F6E56">magnitude — pare-feu (établi)</text>
  <line x1="320" y1="336" x2="180" y2="382" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="360" y1="336" x2="500" y2="382" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <line x1="345" y1="358" x2="345" y2="540" stroke="#888780" stroke-width="0.5" stroke-dasharray="4 4"/>
  <rect x="48" y="384" width="252" height="56" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="174" y="406" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">observable ⟨|h|²⟩</text>
  <text x="174" y="426" text-anchor="middle" font-size="11.5" fill="#0F6E56">réel · insensible au signe</text>
  <rect x="385" y="384" width="250" height="56" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="510" y="406" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">continuation dS/CFT</text>
  <text x="510" y="426" text-anchor="middle" font-size="11.5" fill="#993C1D">attache le signe i^(d-1)</text>
  <line x1="510" y1="440" x2="510" y2="468" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="385" y="470" width="250" height="56" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="510" y="492" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">C_T signé (d=3) réel &lt; 0</text>
  <text x="510" y="512" text-anchor="middle" font-size="11.5" fill="#993C1D">= item « CFT raccordement »</text>
  <text x="174" y="462" text-anchor="middle" font-size="11.5" fill="#0F6E56">branche sûre</text>
  <text x="40" y="556" text-anchor="start" font-size="11" fill="#73726c">vert = établi (algèbre) · orange = à inventer / ouvert · gris = entrées · pare-feu = nœud |C_T|</text>
</svg>

*Fig. — Graphe de dépendances des valeurs. Le nœud-magnitude `|C_T|` est le **pare-feu** : il
alimente l'observable (branche sûre, à gauche) **en amont** de la continuation (à droite) qui
attache le signe. Une erreur de réalité/signe de `C_T` reste confinée à droite (`C_T_signé` →
item raccordement) et **ne remonte pas** vers l'observable.*

---

## 4. Lecture : la réalité de `C_T` se rabat sur l'item raccordement `[décision ouverte — NON scellé]`

`C_T<0` (réel) **n'est pas** une charge centrale unitaire : l'unitarité d'une CFT exige `C_T>0`.
Mais « `C_T` déterminé en magnitude » n'a jamais voulu dire « `C_T` unitaire propre » (déjà noté
`LC-D-CT-ATN §0`, `CT-CADRAGE §4.2`). Deux lectures possibles :

- **bénin** — si dS/CFT est un **générateur de fonctions** (vue de Maldacena : `Ψ=e^{iS}` est une
  fonction d'onde, pas une théorie duale physique), la négativité de `C_T` est la signature
  attendue de la non-unitarité euclidienne, sans conséquence sur la physique de bulk (le bulk dS
  est unitaire ; `|Ψ|²` est une probabilité, l'observable est réel positif) ;
- **obstruction de fond** — si le raccordement CCC exige une **vraie CFT unitaire** recollant deux
  éons, alors `C_T<0` l'**interdit**.

Le point : trancher entre les deux **revient exactement** à construire (ou exclure) la **CFT de
raccordement** — item déjà catalogué `à inventer` (`HOLOGRAPHIE-G3 §3`, `CT-CADRAGE §4.3`). Donc la
réalité de `C_T` **ne crée pas d'obstruction indépendante** : elle se **rabat** sur cet item.

⟹ **Consolidation** : deux `à inventer` listés séparément (réalité de `C_T` ; CFT de raccordement)
sont **le même**. Le compte `{A4 ; A2★ ; N}` **ne bouge pas** ; D1 reste ouvert. C'est précisément
l'issue anticipée par la reco (`POST-NONLIN-VERROU §4` : « ne réduit pas le compte, mais **fonde
physiquement** le verrouillage `C_T~N` »).

---

## 5. Format de chaînon

- **Hypothèse testée.** « La continuation dS/CFT admet-elle une prescription de réalité rendant
  `C_T` physique, ou la non-unitarité est-elle une obstruction de fond ? — et une erreur sur la
  réalité de `C_T` se reporte-t-elle vers l'observable ? »
- **Outil.** Continuation `ℓ_AdS→iℓ_dS` sur `C_T∝c0·ℓ^{d-1}/G` (facteur `i^{d-1}`, `c0`-libre) ;
  magnitude `|C_T|=N/(32π²)` adossée à `verif_D_CT_ATN.py` ; prescription `𝒫=1/(2|Im F|_fini)` ;
  injection symbolique d'une erreur `(δr,s)` et test d'invariance de l'observable. Sceau
  `verif_D_CT_realite.py` (sympy ; EXIT 0 ; 20 asserts).
- **Critère de réfutation.** *Issue « report d'erreur »* : si l'observable dépendait de `δr` ou de
  `s` ⟹ une erreur de réalité contaminerait la physique. **Non observé** : `δr∉free_symbols(𝒫)`,
  invariance `s=±1`. *Issue « contradiction magnitude/signe »* : si `|C_T|` et `C_T_signé` étaient
  le même objet ⟹ contradiction `>0` vs `<0`. **Non observé** : deux nœuds distincts.
  *Issue « obstruction indépendante »* : si `C_T<0` créait un `à inventer` neuf, disjoint de la CFT
  de raccordement ⟹ pas de consolidation. **Non observé** : trancher la nature de `C_T<0` =
  construire/exclure la CFT de raccordement.
- **Verdict.** `[A]` continuation `i^{d-1}` (`d=3` réel négatif) **`[établi — algèbre]`** ; `[B]`
  magnitude/signe sans contradiction **`[établi — algèbre]`** ; `[C]` report d'erreur nul
  **`[établi — algèbre]`** ⟹ les `établi` amont robustes au verdict de réalité. `[D]` nature du
  `C_T<0` = item raccordement (consolidation) **`[décision ouverte — NON scellé]`**. Survie au
  crossover, fixation de `N` **`[à inventer]`**. **D1 non clos ; la CCC n'est pas démontrée.**

---

## 6. Propagation / housekeeping `[à appliquer — note de reprise séparée ; NON exécutée]`

À l'enregistrement (cf. `statut_id`), propagation **additive** (jamais réécriture d'historique) :

1. **`LC-D-CT-ATN §6`** (renvoi) — le `à inventer` « valeur/réalité de `C_T` en dS » est **cadré**
   par ce chaînon : parité `d=3`→réel négatif (pas imaginaire) ; magnitude vs signe sans
   contradiction ; report d'erreur nul ; réalité ≡ item raccordement (consolidation). Le sceau ATN
   reste **inchangé** (magnitude).
2. **`LC-D-HOLOGRAPHIE-G3 §3`** — préciser la non-unitarité : en `d=3`, `C_T` continué est **réel
   négatif** (parité de `ℓ^{d-1}`), non imaginaire ; l'« imaginaire » est le cas `d=2`. La réalité
   de `C_T` se rabat sur l'item « CFT de raccordement » (§3 déjà listé `à inventer`).
3. **`LC-AUDIT-VERDICT §8bis`** — bullet daté : « sceau réalité `C_T` : continuation `i^{d-1}`
   (`d=3` réel<0) ; magnitude/signe sans contradiction ; **report d'erreur nul** (observable
   robuste) ; réalité ≡ item raccordement (consolidation, pas réduction du compte) ; D1 non clos ».
4. **`LC-00-INDEX`** — nouvelle ligne carte (`LC-D-CT-REALITE`, module [D]/[E], résultat) +
   changelog (réalité de `C_T` cadrée/scellée ; report nul ; consolidation raccordement).
5. **`03_glossaire`** — entrées : *réalité de `C_T` en dS (réel négatif en `d=3`, parité de
   `ℓ^{d-1}`)* ; *report d'erreur nul (pare-feu magnitude)* ; *consolidation réalité-`C_T` ≡
   raccordement*.
6. **`02_programme`, `04_references`** — renvois (réfs déjà en KB : Strominger 2001, Maldacena
   2003, dHSS 2001).

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D-CT-ATN` (le sceau parent : `A_T·N=16`, verrouillage en magnitude, signature
isolée — ce chaînon en **cadre la réalité**) ; `LC-WORK-CT-CADRAGE` (tri des mécanismes ;
non-unitarité `§4.2`, CFT de raccordement `§4.3`) ; `LC-D-HOLOGRAPHIE-G3 §3` (cadre dS/CFT,
non-unitarité, CFT de raccordement `à inventer`) ; `LC-E-PLANCK-RESIDUEL` (`N=S_dS`, circularité) ;
`LC-D3-SPECTRE-K3` (forme `∝k³`) ; `LC-D3-WEYL-BUNCHDAVIES` (relation d'état BD) ;
`LC-D3-FRONT-A-SYNTHESE` (verdict figé, **inchangé**) ; `LC-AUDIT-VERDICT §6.4` (discipline) ;
`LC-WORK-REPRISE-POST-NONLIN-VERROU §4` (recommandation exécutée ici).

*Renvoi (v0.2) :* `LC-D-CT-DUAL` (étage S1 du lead dualité graviton-dual : pose la base AdS de la 2ᵉ route au signe ; **garde-fou** — la dualité AdS ne flippe pas `C_T`, donc le `i^{d-1}` de [A] n'est pas compté deux fois).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Réalité de `C_T` en dS* : sous continuation `ℓ_AdS→iℓ_dS`, `C_T∝ℓ^{d-1}` reçoit `i^{d-1}` ; en
  `d=3` (puissance paire) `C_T` continué est **réel négatif** (pas imaginaire — l'imaginaire est le
  cas `d=2`). Magnitude `|C_T|=N/(32π²)>0` (sceau ATN) ; signe attaché par la continuation.
- *Report d'erreur nul (pare-feu magnitude)* : l'observable `𝒫=2H²/(M_Pl²k³)` ne dépend que de
  `|Im F|` ; une erreur de réalité/signe de `C_T` (`δr`, `s`) n'entre **pas** dans l'observable ⟹
  les `établi` amont sont robustes au verdict de réalité.
- *Consolidation réalité-`C_T` ≡ raccordement* : trancher si `C_T<0` est une obstruction de fond
  revient à construire/exclure la CFT de raccordement ⟹ pas d'obstruction indépendante neuve ;
  consolidation, sans réduction du compte `{A4 ; A2★ ; N}`.

**Références (`LC-04`, en KB).** Strominger, JHEP **10** (2001) 034 (dS/CFT ; charge centrale
imaginaire en `d=2`) ; Maldacena, JHEP **05** (2003) 013 (fonction d'onde, dS/CFT) ;
de Haro–Skenderis–Solodukhin, CMP **217**, 595 (2001) (`⟨T⟩=(d/16πG)g_{(d)}`) ;
Gibbons & Hawking, Phys. Rev. D **15**, 2738 (1977) (`N=S_dS`).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`). Ici : continuation `i^{d-1}` (`d=3` réel<0) + magnitude/signe sans
contradiction + report d'erreur nul **`établi (algèbre — sceau)`** ; nature du `C_T<0` = item
raccordement **`décision ouverte`** ; survie au crossover + fixation de `N`
**`à inventer`** ; **D1 non clos**.
