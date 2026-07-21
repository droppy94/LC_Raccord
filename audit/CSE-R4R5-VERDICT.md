# CSE INCOGNITO R-4/R-5 — CONSIGNATION DU VERDICT (2026-07-21)

Chaînon de consignation. Le verdict ci-dessous est reproduit VERBATIM
(copie intégrale de la réponse de l'instance neuve, pas un résumé) ;
il PRÉVAUT — le pilote consigne, ne re-juge pas.

## Traçabilité de l'expédition

- Route retenue par l'opérateur : **incognito maximal** — conversation
  neuve HORS projet, sans mount ni mémoire du programme (confirmé par
  l'opérateur à la remise du verdict).
- Gel d'expédition : `audit/CSE-R4R5-GEL.md`, produit AVANT expédition
  par `instruments/cse_gel_expedition.py` ;
  sha256(GEL) = 7b5a341044c8e629aab9f28dc70ddb7a81400359dae20348305ef2b021770b1e
  (consigné hors-fichier en session, R-36).
- Paquet expédié : CSE-R4R5-PAQUET-INCOGNITO.md (33 Ko, 7 pièces
  intégrales) ; sha256(paquet) =
  d0c1e9869c5c3cfe495e7f065e22330a86f31c2644feec9c8d031e1f6cdb11de.
- L'auditeur a recalculé les 7 sha256 internes : 7/7 MATCH, et rejoué
  les deux instruments (32/32, 18/18) avant sondes adverses.

## Issue et effets consignés (aucun surclassement)

- **Issue : E-3** (espace gelé { E-1 ; E-2 ; E-3 }) — déclencheur
  « assert tautologique ou cible paraphrasée », matériellement établi.
- **Grades requalifiés en aval** : R-4 et R-5 se lisent désormais
  **REPRODUIT-SOUS-RÉSERVE, AGGRAVÉ E-3 — instruction pendante**.
  Après instruction des asserts nommés, la lecture serait AU MIEUX
  E-2 (reproduction guidée, valeur de corroboration faible) — jamais E-1.
- **Instruction prescrite** (avant ouverture de tout lot R-n neuf) :
  R-4 prioritaire — T9 à réécrire avec un s vivant ; T8-signé et
  N_action à dériver ou requalifier consignations ; T13 « unique » à
  démontrer ou dégrader. R-5 second — P5-#13 et P6-#16 à requalifier.
- **Huit consignations mandatées** (défauts de rédaction favorisant
  E-1) : reprises verbatim ci-dessous ; opposables aux lots suivants.
- **Leçon de méthode intégrée au protocole §2.0, opposable** :
  (a) tout assert non-discriminant se déclare CONSIGNATION, jamais
  PASS ; (b) les décomptes n'agrègent que les asserts discriminants ;
  (c) aucune disjonction rendant un assert infaillible ; (d) un
  espace-verdict ne maintient pas vivante une issue contredite par une
  pièce du paquet ; (e) « premier passage sans correction » ne se
  présente plus comme force.
- Rapports antérieurs NON réécrits (historique jamais réécrit) ; la
  présente consignation fait foi en aval.

## §6.4

Consigner un verdict n'instruit pas encore, ne scelle, ne réduit, ne
compte, ne démontre rien. { A4 ; A2★ ; N } INCHANGÉ · CCC non
démontrée NI réfutée.

---

# VERDICT DE L'INSTANCE NEUVE — VERBATIM

CSE INCOGNITO R-4/R-5 — RAPPORT D'AUDIT À FROID (2026-07-21)
Auditeur externe, session neuve, aucun contexte hors le paquet. Vérifications matérielles effectuées avant jugement : les 7 sha256 internes recalculés depuis le contenu intégral des pièces — 7/7 MATCH (piège R-36 noté : le paquet ne porte pas son propre sha, conforme). Les deux instruments ont été rejoués tels quels : redemo_R4_CT.py 32/32 PASS EXIT 0, redemo_R5_reductions.py 18/18 PASS EXIT 0 — conformes aux rapports. Des sondes adverses (mutation, code mort, disjonction) ont ensuite été exécutées.

VERDICT : E-3 — DÉFAUT SUBSTANTIEL, instruit aux lots R-4 (principal) et R-5 (secondaire)
L'espace-verdict gelé déclenche E-3 sur « assert tautologique ou cible paraphrasée ». Les deux conditions sont matériellement établies, sur des asserts présentés comme des tests (pas comme des consignations déclarées). E-1 est exclu ; le caractère résiduel du paquet, une fois les défauts instruits, serait E-2 — jamais E-1.

Examen assert par assert
redemo_R4_CT.py (32 asserts). Trois classes :

Calculs authentiques et discriminants (≈17) : T1 (limite η→0⁻ du mode canonique, contrôle EOM), T11 (EOM différentielle de BD), T10 (f_a, f_b solutions, identité f_a−i·f_b, substitution u=−kη, S·c=ic), T2 (résolution de β dans 𝒫_holo=𝒫_canon, β=M_Pl²/4 unique), T3/T4/T5 (arithmétique de A_T, N, et A_T·N=16 réellement calculé), T6 partiel, T12 (compensation du signe par le −2, firewall du retrait). Les tests de mutation mordent : cible T1 altérée (H² au lieu de 2H²) → échec ; G non réduit dans N → A_T·N≠16. Ces asserts calculent.
Arithmétique sur définitions importées (≈7) : S²=−𝟙 et valeurs propres ±i (triviales pour la matrice donnée), ratio dH/prog=4 (vérifie 32/8=4 où CT_prog=N/(32π²) est posé par fiat, non dérivé), A_T·coeff=1/(2π²) (16/32), parités i^{d−1} pour d=2,3,4. Calculent, contenu mince.
Tautologies / paraphrases (6) — c'est ici que E-3 se déclenche :
« γ ∉ 𝒫 » : condition littérale True. γ n'a jamais été introduit dans les expressions ; l'absence est garantie par construction, pas testée.
« N_action = γ/4 » : condition littérale Rational(4,4)==1 and Rational(1,4)==Rational(1,4), soit 1==1 et ¼==¼. Aucun objet N_action n'existe dans le script. Cible T13 paraphrasée.
« C_T_signé(d=3) = −N/(32π²) » : vérifie −CT_prog + N/(32π²) == 0 où CT_prog := N/(32π²). C'est −x+x=0. Cible T8-signé paraphrasée.
« C_T_signé porte δr » : CT_sig = −(Fs+dr) construit à la main, puis test que dr ∈ symboles libres. L'expression est fabriquée pour contenir ce qu'on vérifie qu'elle contient.
« invariance s=±1 » : le symbole s apparaît uniquement dans s*0 — code mort. Sonde exécutée : s=+1 et s=−1 donnent la même expression par construction, pas par calcul. L'assert teste Abs(−Fs)==Abs(Fs), une propriété de la valeur absolue. La cible T9 revendique une invariance jamais testée ; le nom de l'assert surdéclare son contenu. Défaut le plus grave du lot.
« C̃_T/C_T=+1 invariant sous continuation » : vérifie (i²·x)/(i²·x)==1 — vrai pour tout facteur commun. La localisation de i^{d−1} sur le seul ℓ^{d−1} (le contenu de la cible) n'est pas testée.
redemo_R5_reductions.py (18 asserts).

Calculs authentiques (9) : P1 (série de (1+ikη)e^{−ikη}, coefficient η³ = −(i/3)k³g₀, contrôles η¹, η²), P2 (projecteur TT explicite 3D appliqué à c·δ — le meilleur assert du paquet ; sonde : un tenseur anisotrope donne Π^TT≠0, le test discrimine), P3 témoin ⟨g₃g₃⟩=k⁶𝒫₀/9≠0, P4 recombinaison et invariance d'échelle, P5 identification A_T, P6 A_T·N=16.
Triviaux légitimes (2) : témoin ∈ S_A3 (0·x=0, logiquement correct par linéarité de P1), 2Δ−d=3 (arithmétique, Δ=3 importé).
Tautologies / consignations (7) : quatre check(…, True) littéraux (« A4⟹⟨g₃⟩=0 trivial », « inclusion STRICTE », « l'écart ne dépend pas du un-point », « RÉDUCTION PAS FERMETURE ») ; P5 « résidu = 1 nombre » : spec = A·k³/k³ puis test que ses symboles libres = {A} — une constante construite n'a que sa constante, la détermination gaussienne (moyenne + deux-point) n'est pas et ne peut pas être testée ainsi ; P6 « scaling » : disjonction or dont le second membre est A_T·N/16==1, restatement de l'assert précédent déjà passé — l'assert ne peut pas échouer (sonde confirmée) ; P7 « inconnues restantes » : restantes = {"A4","A2*","N"} puis restantes == {"A4","A2*","N"} — set littéral comparé à lui-même. P7 est honnêtement déclaré consignation au rapport R-5 §3 ; P5-#13 et P6-#16 ne le sont pas.
Indépendance vs guidage
E-1 exige « guidage limité au choix de route ». C'est réfuté par les pièces elles-mêmes : les gels de cibles portent le mécanisme, pas seulement les valeurs — R5-CIBLES donne g₃=−(i/3)k³g₀ comme « devise commune » et énonce « projection TT d'un tenseur isotrope = 0 » (la route de P2 entière) ; R4-CIBLES donne la structure de la compensation du −2 (T12), la forme du map c_W=ℓ²/(8κ²) (T13), la cancellation H,G (T5). Les scripts exécutent l'algèbre le long d'une route fournie avec valeurs d'arrivée connues. La réserve (pièce 7) le concède ; la réconciliation R-4 §3(a) le confirme empiriquement : là où le front-matter était ambigu (représentation de S), le pilote a d'abord divergé (−i), puis a choisi la représentation qui reproduit la cible (+i) — ajustement à la cible, qualifié « sans effet » dans le rapport. Reproduction guidée, donc ; mais le déclencheur E-3 prévaut sur la qualification E-2.

Consignations mandatées — défauts de rédaction favorisant E-1
Les décomptes-vitrines « 32/32 PASS » et « 18/18 PASS » comptent tautologies et consignations comme PASS — la force probante affichée est gonflée (contenu discriminant réel : ≈17/32 et ≈9/18).
Le mot « REDÉRIVATION INDÉPENDANTE » figure dans les docstrings des deux instruments alors que la pièce 7 du même paquet établit que l'aveuglement était partiel.
E-1 était mort-né par construction : sa définition gelée (« guidage limité au choix de route ») est contredite par une pièce incluse dans le paquet. Maintenir E-1 comme issue vivante dans l'espace gelé favorise E-1.
Le nom de l'assert T9 (« invariance s=±1 ») revendique un test que son code (s·0) ne réalise pas.
La disjonction vacante de P6-#16 rend un assert infaillible sans le déclarer.
R-5 §2 liste P1–P6 « redérivés de bout en bout » ; P5-#13 et P6-#16 ne le sont pas.
« Premier passage sans correction d'instrument » présenté comme force : avec mécanisme fourni et asserts invérifiables, le premier-coup est un indice de guidage autant que de robustesse.
Réconciliation (a) qualifiée « sans effet » : l'insensibilité de l'aval au signe ±i est plausible mais affirmée, pas testée dans l'instrument.
Portée du verdict — sans surclassement
E-3 instruit, il n'annule pas : le noyau algébrique (T1, T2-β, T5=16, T10/T11/T12, P1–P4, l'identification P5-#14, P6-#15) calcule réellement et survit aux mutations. Ce qui est substantiellement défaillant, c'est la rédaction des instruments comme preuves : cibles T8-signé, T9 et T13-partiel (R-4), P5-partiel (R-5) paraphrasées au niveau des asserts, plus un assert infaillible non déclaré (P6-#16). Instruction au lot R-4 en priorité (T9 à réécrire avec un s vivant ; T8-signé et N_action à dériver ou à requalifier consignations ; T13 « unique » à démontrer ou dégrader), au lot R-5 en second (P5-#13 et P6-#16 à requalifier). Après instruction, le grade des lots se lirait au mieux REPRODUIT-SOUS-RÉSERVE au sens E-2 de la réserve existante.

§6.4 respecté : ce verdict ne scelle, ne réduit, ne compte, ne démontre rien. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
