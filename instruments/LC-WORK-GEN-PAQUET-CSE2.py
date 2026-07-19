#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# LC-WORK-GEN-PAQUET-CSE2.py — v2.1 (mandat P-8, LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE)
# =============================================================================
# INSTRUMENT (hors S2, exclu NOMMÉMENT au comparateur, AUCUNE charge de sceau :
# il n'asserte aucune physique ; son intégrité est portée par le PKG-SHA).
#
# Générateur GÉNÉRAL de paquets incognito. Paquet courant : CSE-KPS
# (confrontation KPS 2503.19957 ↔ résidu PRESCRIPTION-𝓘⁺, gel 172c3730).
# NOTE v2.1 : la source 2503_19957v1.pdf a été RETIRÉE de la KB pour capacité
# (clôture V95). Le build KPS end-to-end est donc DORMANT (paquet rendu K-B).
# La machinerie P-8 ci-dessous ne dépend PAS de cette source : elle se
# vérifie par `--selftest` sur fixtures synthétiques, en conteneur nu.
#
# ------------------------------------------------------------ CE QUI CHANGE v2.1
# Mandat P-8 (§2 de LIVRAISON-SEQUENCEE) — LIVRAISON SÉQUENCÉE INSTRUMENTÉE.
# Le générateur, désormais :
#   (i)   émet DEUX TRANCHES NOMMÉES et REFUSE, PAR DÉFAUT, la tranche unique ;
#   (ii)  n'émet une tranche unique QUE sur DRAPEAU explicite d'inapplicabilité,
#         et alors écrit LUI-MÊME la clause P-6 EN CLAIR dans le bloc PROMPT
#         (texte écrit PAR LE SCRIPT, jamais à la main) ;
#   (iii) SCANNE la tranche 1 pour les formulations INTERDITES par P-7 et rend
#         un CODE DE SORTIE NON NUL si l'une y figure ;
#   (iv)  consigne le régime employé par un CHAMP NOMMÉ (regime_livraison) —
#         un champ absent vaut DÉFAUT, pas conformité.
# Verrou P-1 (contre le pilote) : un paquet qui INSTANCIE UN MÉCANISME DE RETOUR
#   (droit de tirage, question, livraison différée) rend le canal MULTI-TOURS
#   PAR LE FAIT ⟹ le drapeau d'inapplicabilité est REFUSÉ (rc non nul). Le
#   pilote ne peut pas déclarer one-shot un canal dont son paquet exploite le retour.
#
# Ce que ce script fait par ailleurs — et que le pilote NE FAIT PLUS À LA MAIN :
#   1. EXPOSITION MÉCANIQUE du gel selon les loci X-1..X-10 (gel 99bf591c).
#   2. REGISTRE DES RETRAITS (instrument ②) : étiquette + octets + sha256.
#   3. EXTRACTION de la source (zip OCR) — le pilote ne lit pas.
#   4. BLOC SHA DU HARNAIS écrit PAR CE SCRIPT ; injection entre marqueurs.
#   5. SCAN ⑤ (fuite question ↔ lexique des issues) : BLOQUANT, 0 exigé.
#   6. LISTE DES EXCLUSIONS (tous fichiers KB hors paquet, nommés).
#   7. SCAN ANTI-FUITE de l'artefact d'exposition (tokens interdits = 0).
#
# §6.4 : générer un paquet / séquencer une livraison ne scelle, ne réduit,
# ne compte, ne démontre RIEN. Un anti-ancrage instrumenté n'atteste que
# l'ordre de lecture, PAS que le paquet est honnête (Δ-3 SURVIT, b6 TIENT).
# =============================================================================
import hashlib, os, re, sys, zipfile, unicodedata

MOUNT = "/mnt/project"
OUT   = "/home/claude/work/paquet_kps"
HORS_PAQUET = os.path.join(OUT, "hors-paquet")   # verbatims ② + exclusions

# ---------------------------------------------------------------- utilitaires
def canon(fn):
    return re.sub(r'__\d+_(?=\.(md|py|pdf|txt)$)', '', fn)

def resolve(name):
    hits = [f for f in os.listdir(MOUNT) if canon(f) == name]
    assert len(hits) == 1, f"resolution mount: {name} -> {hits}"
    return os.path.join(MOUNT, hits[0])

def sha(b):  return hashlib.sha256(b).hexdigest()

def one(pattern, text, flags=re.DOTALL):
    m = list(re.finditer(pattern, text, flags))
    assert len(m) == 1, f"ancre non unique ({len(m)}): {pattern[:60]}"
    return m[0]

# =============================================================================
# MODULE P-8 — LIVRAISON SÉQUENCÉE (packet-agnostique, mandat LIVRAISON-SEQUENCEE)
# =============================================================================

# --- P-7 : formulations INTERDITES quand une pièce aval est jointe -----------
# Liste CLOSE : les trois explicites du §2/P-7 + équivalents évidents. Toute
# extension est un amendement daté, jamais un ajout au fil de l'eau.
P7_INTERDITS = [
    "cet ordre est contraignant",
    "ordre contraignant",
    "ordre impose",                 # "ordre imposé" (accents strippés)
    "tu ne peux pas",
    "vous ne pouvez pas",
    "cet ordre s impose",
    "cet ordre simpose",
    "il est interdit de lire",
    "interdit d ouvrir",
    "interdit douvrir",
    "l ordre est obligatoire",
    "ordre obligatoire",
]

def _norm(s):
    """minuscule + accents strippés + apostrophes unifiées + espaces compactés.
    Permet à P-7 de mordre les variantes sans faux positifs sur la clause P-6
    ('... une DEMANDE et non une CONTRAINTE' — aucune phrase interdite)."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("’", " ").replace("'", " ").replace("`", " ")
    s = re.sub(r"\s+", " ", s)
    return s

def scan_p7(text):
    """Rend la liste des formulations interdites présentes dans `text`."""
    n = _norm(text)
    return [p for p in P7_INTERDITS if p in n]

# --- P-6 : clause d'inapplicabilité, ÉCRITE PAR LE SCRIPT (jamais à la main) --
P6_CLAUSE = (
    "<!-- P-6:INAPPLICABILITE (écrite par le générateur, non à la main) -->\n"
    "AVIS À L'AUDITEUR — ANTI-ANCRAGE NON INSTRUMENTÉ. Le canal a été déclaré\n"
    "one-shot MATÉRIEL : les pièces aval sont jointes au MÊME envoi. En\n"
    "conséquence, l'ordre de lecture est une DEMANDE et non une CONTRAINTE ;\n"
    "aucune séquence n'est garantie par le dispositif. Grade abaissé en\n"
    "conformité avec P-6.\n"
    "<!-- P-6:END -->\n"
)

# --- P-1 : TEST D'APPLICABILITÉ, MATÉRIEL (le paquet s'auto-classe) ----------
# Indices de mécanisme de retour ⟹ canal MULTI-TOURS PAR LE FAIT.
P1_RETOUR = [
    "droit de tirage", "tirable a la demande", "tirable à la demande",
    "au tour suivant", "livraison differee", "livraison différée",
    "question de clarification", "sera livre", "sera livré",
]

def p1_applicability(out_dir, prompt_text=""):
    """Retourne ('multi-tours'|'one-shot', motif). MATÉRIEL, pas déclaratif :
    un registre de retraits à segments>0, OU un indice de retour dans le
    prompt, prouve le multi-tours."""
    motifs = []
    # (a) bloc-sha : segments_retires > 0
    bloc = os.path.join(out_dir, "BLOC-SHA-HARNAIS.md")
    if os.path.exists(bloc):
        m = re.search(r"segments_retires:\s*(\d+)", open(bloc, encoding="utf-8").read())
        if m and int(m.group(1)) > 0:
            motifs.append(f"registre des retraits ({m.group(1)} segments tirables)")
    # (b) registre autonome présent et non vide
    reg = os.path.join(out_dir, "REGISTRE-RETRAITS.txt")
    if os.path.exists(reg):
        if re.search(r"^etiquette:", open(reg, encoding="utf-8").read(), re.M):
            motifs.append("REGISTRE-RETRAITS.txt (droit de tirage instancié)")
    # (c) indices de retour dans le prompt
    n = _norm(prompt_text)
    for k in P1_RETOUR:
        if _norm(k) in n:
            motifs.append(f"prompt: mécanisme de retour « {k} »")
    if motifs:
        return "multi-tours", " ; ".join(sorted(set(motifs)))
    return "one-shot", "aucun mécanisme de retour instancié"

# --- P-2 / P-4 / P-5 : émission en tranches (défaut) ; refus du bundle -------
def emit_tranches(out_dir, pieces_phase, prompt_text, regime):
    """pieces_phase : dict {nom_fichier: 'amont'|'aval'}.
    regime : 'sequence' (défaut) | 'inapplicable'.
    Retourne (rc, rapport:list[str]).
    - 'sequence'      : DEUX tranches nommées ; refuse tout bundle unique.
    - 'inapplicable'  : bundle unique — HONORÉ SEULEMENT si P-1 == one-shot ;
                        sinon rc=2 (refus, verrou P-1). Clause P-6 écrite PAR LE SCRIPT.
    Dans TOUS les cas : scan P-7 de la tranche 1 (rc=3 si fuite).
    """
    rap = []
    amont = [f for f, ph in pieces_phase.items() if ph == "amont"]
    aval  = [f for f, ph in pieces_phase.items() if ph == "aval"]
    rap.append(f"pieces_amont      {sorted(amont)}")
    rap.append(f"pieces_aval       {sorted(aval)}")

    etat, motif = p1_applicability(out_dir, prompt_text)
    rap.append(f"P1_canal          {etat}  ({motif})")

    # --- verrou P-1 sur l'inapplicabilité ---
    if regime == "inapplicable":
        if etat == "multi-tours":
            rap.append("REFUS P-1        drapeau d'inapplicabilité REFUSÉ : le paquet")
            rap.append("                 instancie un mécanisme de retour ⟹ canal MULTI-TOURS")
            rap.append("                 PAR LE FAIT. Le pilote ne peut pas déclarer one-shot")
            rap.append("                 un canal dont son propre paquet exploite le retour.")
            rap.append("regime_livraison REFUSÉ (rc=2)")
            return 2, rap

    # --- tranche 1 : prompt (phases 0-2) + amont + bloc-sha COMPLET ---
    t1 = os.path.join(out_dir, "TRANCHE-1")
    os.makedirs(t1, exist_ok=True)
    prompt_final = prompt_text
    if regime == "inapplicable":
        prompt_final = prompt_text + "\n" + P6_CLAUSE          # (ii) clause par le script

    # (iii) scan P-7 de la tranche 1 AVANT écriture
    hits = scan_p7(prompt_final)
    rap.append(f"scan_P7_tranche1  {'0 — CONFORME' if not hits else 'INTERDIT ' + str(hits)}")
    if hits:
        rap.append("ARRÊT P-7        formulation de prétention de contrainte dans la")
        rap.append("                 tranche 1 alors qu'une pièce aval est jointe/annoncée.")
        return 3, rap

    open(os.path.join(t1, "PROMPT.md"), "w", encoding="utf-8").write(prompt_final)
    bloc = os.path.join(out_dir, "BLOC-SHA-HARNAIS.md")
    if os.path.exists(bloc):
        open(os.path.join(t1, "BLOC-SHA-HARNAIS.md"), "w", encoding="utf-8").write(
            open(bloc, encoding="utf-8").read())     # bloc COMPLET (inclut sha aval)

    if regime == "inapplicable":
        # bundle unique : toutes les pièces au même envoi, grade abaissé
        for f in amont + aval:
            p = os.path.join(out_dir, f)
            if os.path.exists(p):
                open(os.path.join(t1, f), "wb").write(open(p, "rb").read())
        rap.append("emission          BUNDLE UNIQUE (inapplicabilité déclarée) — grade abaissé")
        regime_field = "inapplicabilité déclarée"
    else:
        # SÉQUENCÉ : amont en tranche 1, aval en tranche 2
        for f in amont:
            p = os.path.join(out_dir, f)
            if os.path.exists(p):
                open(os.path.join(t1, f), "wb").write(open(p, "rb").read())
        t2 = os.path.join(out_dir, "TRANCHE-2")
        os.makedirs(t2, exist_ok=True)
        readme2 = (
            "TRANCHE 2 — À N'EXPÉDIER QU'APRÈS QUE L'AUDITEUR A RENDU SA PHASE 2 (P-2/P-4).\n"
            "L'auditeur recompute le sha de chaque pièce et le confronte au sha\n"
            "pré-communiqué en tranche 1 (P-5). Écart ⟹ ARRÊT, tranche 2 CONTAMINÉE,\n"
            "la Phase 2 RESTE ACQUISE. (γ-1 : le sha bloque, le nom se consigne.)\n")
        open(os.path.join(t2, "_LIRE-APRES-PHASE-2.txt"), "w", encoding="utf-8").write(readme2)
        for f in aval:
            p = os.path.join(out_dir, f)
            if os.path.exists(p):
                open(os.path.join(t2, f), "wb").write(open(p, "rb").read())
        rap.append("emission          DEUX TRANCHES (séquencé) — tranche 2 après Phase 2 rendue")
        regime_field = "séquencé"

    # (iv) champ nommé pour le manifeste — un champ absent vaut DÉFAUT
    open(os.path.join(out_dir, "REGIME-LIVRAISON.txt"), "w", encoding="utf-8").write(
        "# À consigner au manifeste par CHAMP NOMMÉ (P-8-iv). Champ absent = défaut.\n"
        f"regime_livraison: {regime_field}\n")
    rap.append(f"regime_livraison  {regime_field}  (consigné dans REGIME-LIVRAISON.txt)")
    return 0, rap

# ------------------------------------------------------- paquet KPS : le SPEC
GEL_NAME   = "LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION.md"
GEL_SHA8   = "172c3730"
R41_NAME   = "LC-WORK-R41-KPS-MIROIRS.md"
SRC_NAME   = "2503_19957v1.pdf"

PIECE_EXPO = "CADRAGE-KPS-EXPOSITION.md"       # artefact dérivé (jamais en KB) — AVAL
PIECE_R41  = R41_NAME                           # jointe INTÉGRALE, byte-exacte — AMONT
PIECE_SRC  = "SOURCE-2503-19957-OCR.txt"        # AMONT

# P-2/P-3 : classification de phase des pièces du paquet KPS.
# J1 (cadrage/espace-verdict) = AVAL ; J2 (identité R-41), J3 (source) = AMONT.
KPS_PIECES_PHASE = {PIECE_EXPO: "aval", PIECE_R41: "amont", PIECE_SRC: "amont"}

HEADER_EXPO = (
"---\n"
"id: LC-WORK-CADRAGE-G3-KPS-PRESCRIPTION\n"
"objet: cadrage gelé — espace-verdict, discriminants, mapping et bornes d'une "
"confrontation intrant-externe ↔ résidu nommé d'une tête de délimitation\n"
"version: exposition dérivée mécaniquement de v0.1 (artefact hors-KB ; le gel "
"KB demeure seul autoritaire)\n"
"date: 2026-07-17\n"
"---\n")

X3_SUBST = ("*Identité de la source vérifiée par la note de gate R-41 jointe "
            "au paquet.*")
X9_SUBST = "L'origine d'une piste est sans valeur probante."

# lexique ⑤ : labels + radicaux des issues {K-A..K-D} (gel §3)
LEXIQUE_5 = ["K-A", "K-B", "K-C", "K-D", "applicab", "fixeur", "FIXEUR",
             "hors-domaine", "homonym", "neutr", "consolid", "indétermin",
             "indetermin", "différé", "differe"]

# tokens interdits dans l'artefact d'exposition (anti-fuite, 0 exigé)
INTERDITS_EXPO = ["V-A", "BORD-EON", "BORDEON", "NOTE-06", "NOTE-07",
                  "Hollands", "ABK", "signalé", "signaleur", "récusé",
                  "récusation", "F6-BMS", "F6-BORDEON", "F6-NOTE07"]

# exclusions à nommer EN TÊTE de la liste (le reste = tout le mount)
EXCLUSIONS_CRITIQUES = [
    "LC-WORK-AMENDEMENT-R7-KPS-CSE-EXPOSITION.md",   # annule l'aveuglement
    "LC-WORK-CADRAGE-TIRAGE-AUDITEUR.md",
    "LC-WORK-GEN-PAQUET-CSE2.py",                    # ce script
    "LC-D-F6-BORDEON-VA.md", "LC-D-F6-NOTE07-VB.md",
    "NOTE-BORD-EON-06_V1dia1-weyl-verdict.md",
    "NOTE-BORD-EON-07_V1dia1b-fusion-memoire.md",
    "LC-WORK-R41-BORDEON-MIROIRS.md",
    "LC-WORK-CADRAGE-BORDEON-NOTE07-FUSION-N.md",
    "PROMPT-INCOGNITO-NOTE07-FUSION-N.md",
    "LC-WORK-R41-NOTE07-REPARATION-E3-E6.md",
    "LC-WORK-CADRAGE-F6-BORDEON-MEMOIRE.md",
]

# --------------------------------------------------- X-1..X-10 : l'EXPOSITION
def expose(gel_text):
    """Applique l'énumération FERMÉE X-1..X-10. Retourne (artefact, registre).
    registre : liste (etiquette, verbatim_retire_bytes)."""
    reg = []
    t = gel_text

    # X-1 — front-matter intégral -> en-tête minimal (id, objet, version, date)
    m = one(r"\A---\n.*?\n---\n", t)
    reg.append(("X-1", m.group(0)))
    t = HEADER_EXPO + t[m.end():]

    # X-2 — §0 / R-54 : aparté italique entier
    m = one(r" \*Rappel opposable au\n  pilote : dans cette même session.*?"
            r"pas deux\.\*", t)
    reg.append(("X-2", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    # X-3 — §0 / R-41 : antécédent italique -> renvoi à la note jointe
    m = one(r"\*Antécédent : la gate R-41 du corpus BORD-EON.*?"
            r"pas la formulation de\n  NOTE-06\.\*", t)
    reg.append(("X-3", m.group(0)))
    t = t[:m.start()] + X3_SUBST + t[m.end():]

    # X-4 — §0 / Pilote disqualifié : 2e phrase
    m = one(r" Le pilote a \*\*signalé\*\* cette piste : cela ne lui confère "
            r"\*\*aucune\n  autorité\*\* sur son issue, et constitue au "
            r"contraire un motif de récusation renforcée\.", t)
    reg.append(("X-4", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    # X-5 — §1 : ancre (A3) intégrale
    m = one(r"\*\*\(A3\) `LC-D-F6-BORDEON-VA`.*?\n\n(?=\*\*\(A4\))", t)
    reg.append(("X-5", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    # X-6 — §2 intégral (constat + encadré de portée)
    m = one(r"## §2 — Le fait mesuré.*?(?=## §3 — Espace-verdict)", t)
    reg.append(("X-6", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    # X-7 — §4 / D3 : dernière phrase italique (le test SUBSISTE)
    m = one(r"\s*\*Ce sont deux notions distinctes ; les confondre "
            r"reproduirait exactement l'erreur tranchée V-A\.\*", t)
    reg.append(("X-7", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    # X-8 — §5.3 : incise « et récusé comme signaleur »
    m = one(r"pilote \*\*explicitement disqualifié et récusé\n"
            r"   comme signaleur\*\*", t)
    reg.append(("X-8", m.group(0)))
    t = t[:m.start()] + "pilote **explicitement disqualifié**" + t[m.end():]

    # X-9 — §6 / b6 : 1re phrase -> norme nue (la suite subsiste)
    m = one(r"L'origine de la piste \(signalement par le pilote, à partir "
            r"d'un corpus adjugé \*\*informatif\*\*\n  par `V-A`\) est "
            r"\*\*sans valeur probante\*\*\.", t)
    reg.append(("X-9", m.group(0)))
    t = t[:m.start()] + X9_SUBST + t[m.end():]

    # X-10 — §6 / b4 : dernière phrase (renvoi au §2 clos ; b4 subsiste)
    m = one(r" Le constat §2 \(non-confrontation factuelle\) \*\*ne déplace "
            r"PAS\*\* ce défaut\.", t)
    reg.append(("X-10", m.group(0)))
    t = t[:m.start()] + t[m.end():]

    return t, reg

# ---------------------------------------------------------- source : OCR pages
def extract_source():
    zf = zipfile.ZipFile(resolve(SRC_NAME))
    pages = sorted((n for n in zf.namelist() if n.endswith(".txt")),
                   key=lambda n: int(os.path.splitext(os.path.basename(n))[0]))
    parts = []
    for n in pages:
        parts.append(f"===== PAGE {os.path.splitext(os.path.basename(n))[0]} "
                     f"(OCR) =====\n")
        parts.append(zf.read(n).decode("utf-8", errors="replace"))
        parts.append("\n")
    head = ("SOURCE arXiv:2503.19957 v1 — extraction OCR mécanique "
            f"({len(pages)} pages), zéro lecture pilote, zéro rédaction.\n\n")
    return head + "".join(parts)

# ------------------------------------------------------------------- scan ⑤
def scan5(question):
    hits = [tok for tok in LEXIQUE_5 if tok.lower() in question.lower()]
    return hits

# ------------------------------------------------- build KPS (DORMANT si source absente)
def build_kps():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(HORS_PAQUET, exist_ok=True)

    # 0. identité du gel (pin)
    gel_path = resolve(GEL_NAME)
    gel_bytes = open(gel_path, "rb").read()
    assert sha(gel_bytes).startswith(GEL_SHA8), "gel != 172c3730 : STOP"

    # 1. exposition + registre
    artefact, registre = expose(gel_bytes.decode("utf-8"))
    fuites = [tok for tok in INTERDITS_EXPO if tok in artefact]
    assert not fuites, f"FUITE dans l'artefact d'exposition : {fuites}"
    open(os.path.join(OUT, PIECE_EXPO), "w", encoding="utf-8").write(artefact)

    reg_lines = []
    for et, verb in registre:
        vb = verb.encode("utf-8")
        open(os.path.join(HORS_PAQUET, f"RETRAIT-{et}.txt"), "wb").write(vb)
        reg_lines += [f"etiquette: {et}", f"octets: {len(vb)}",
                      f"sha256: {sha(vb)}", ""]
    registre_txt = ("REGISTRE DES RETRAITS (instrument ②) — "
                    f"{len(registre)} segments retirés, énumération FERMÉE.\n"
                    "Tout segment est tirable à la demande (livraison "
                    "sha-attestée, hors paquet initial).\n\n"
                    + "\n".join(reg_lines))
    open(os.path.join(OUT, "REGISTRE-RETRAITS.txt"), "w",
         encoding="utf-8").write(registre_txt)

    # 2. pièce R-41 : copie byte-exacte sous nom canon
    r41 = open(resolve(R41_NAME), "rb").read()
    open(os.path.join(OUT, PIECE_R41), "wb").write(r41)

    # 3. source OCR
    src = extract_source().encode("utf-8")
    open(os.path.join(OUT, PIECE_SRC), "wb").write(src)

    # 4. bloc sha du harnais — UN CHAMP PAR LIGNE (bd495c65)
    pieces = [("J1", PIECE_EXPO), ("J2", PIECE_R41), ("J3", PIECE_SRC)]
    bloc = ["<!-- BLOC-SHA:BEGIN -->", f"pieces_attendues: {len(pieces)}"]
    for pid, fn in pieces:
        b = open(os.path.join(OUT, fn), "rb").read()
        bloc += ["", f"piece: {pid}", f"nom: {fn}",
                 f"octets: {len(b)}", f"sha256: {sha(b)}"]
    bloc += ["", f"segments_retires: {len(registre)}"]
    for et, verb in registre:
        vb = verb.encode("utf-8")
        bloc += ["", f"retrait: {et}", f"octets: {len(vb)}", f"sha256: {sha(vb)}"]
    bloc += ["<!-- BLOC-SHA:END -->"]
    bloc_txt = "\n".join(bloc) + "\n"
    open(os.path.join(OUT, "BLOC-SHA-HARNAIS.md"), "w",
         encoding="utf-8").write(bloc_txt)

    harnais = os.path.join(OUT, "HARNAIS.md")
    if os.path.exists(harnais):
        h = open(harnais, encoding="utf-8").read()
        h2 = re.sub(r"<!-- BLOC-SHA:BEGIN -->.*?<!-- BLOC-SHA:END -->\n?",
                    bloc_txt, h, count=1, flags=re.DOTALL)
        assert h2 != h or bloc_txt in h, "marqueurs BLOC-SHA absents du harnais"
        open(harnais, "w", encoding="utf-8").write(h2)
        mq = re.search(r"<!-- QUESTION:BEGIN -->(.*?)<!-- QUESTION:END -->",
                       h2, re.DOTALL)
        if mq:
            hits = scan5(mq.group(1))
            print(f"scan_5_question   {'0 — CONFORME' if not hits else 'FUITE ' + str(hits)}")
            assert not hits, "scan ⑤ BLOQUANT : réécrire la question"

    # 5. exclusions : tout le mount, critiques en tête
    tout = sorted({canon(f) for f in os.listdir(MOUNT)
                   if f.endswith((".md", ".py", ".pdf"))})
    excl = [c for c in tout if c != R41_NAME]
    lignes = ["EXCLUSIONS CRITIQUES (leur lecture annulerait l'aveuglement) :"]
    lignes += [f"  {c}" for c in EXCLUSIONS_CRITIQUES]
    lignes += ["", f"EXCLUSIONS — LISTE INTÉGRALE ({len(excl)} fichiers KB, "
               "seule la note R-41 est jointe) :"]
    lignes += [f"  {c}" for c in excl]
    open(os.path.join(HORS_PAQUET, "EXCLUSIONS.txt"), "w",
         encoding="utf-8").write("\n".join(lignes) + "\n")

    print("=========== GEN-PAQUET v2.1 — paquet CSE-KPS ===========")
    print(f"gel_pin           {GEL_SHA8} CONFORME")
    print(f"loci_appliques    {len(registre)}/10 (énumération fermée)")
    print(f"fuite_expo        0 (tokens interdits : {len(INTERDITS_EXPO)} scannés)")
    for pid, fn in pieces:
        b = open(os.path.join(OUT, fn), "rb").read()
        print(f"{pid}  {fn}  {len(b)} o  {sha(b)[:8]}")
    print(f"registre          {len(registre)} segments, verbatims hors-paquet")
    print(f"exclusions        {len(excl)} nommées (critiques en tête)")
    # P-8 : livraison séquencée par défaut
    rc, rap = emit_tranches(OUT, KPS_PIECES_PHASE, prompt_text="", regime="sequence")
    for l in rap: print("  " + l)
    print("§6.4 : générer/séquencer un paquet ne scelle/réduit/compte/démontre RIEN.")
    return rc

# =============================================================================
# SELFTEST — prouve P-8 (i)-(iv) sur fixtures synthétiques, SANS la source KPS
# =============================================================================
def _fixture(base, with_return, pieces):
    """Crée un OUT synthétique. with_return=True ⟹ registre à segments>0."""
    import shutil
    if os.path.exists(base): shutil.rmtree(base)
    os.makedirs(base, exist_ok=True)
    for f, content in pieces.items():
        open(os.path.join(base, f), "w", encoding="utf-8").write(content)
    seg = 3 if with_return else 0
    open(os.path.join(base, "BLOC-SHA-HARNAIS.md"), "w", encoding="utf-8").write(
        "<!-- BLOC-SHA:BEGIN -->\npieces_attendues: 2\n"
        f"\nsegments_retires: {seg}\n<!-- BLOC-SHA:END -->\n")
    if with_return:
        open(os.path.join(base, "REGISTRE-RETRAITS.txt"), "w", encoding="utf-8").write(
            "etiquette: X-1\noctets: 10\nsha256: deadbeef\n")

def selftest():
    W = "/home/claude/work/_selftest_p8"
    pieces = {"J1-AVAL.md": "cadrage espace-verdict aval\n",
              "J2-AMONT.md": "note identité amont\n"}
    phase = {"J1-AVAL.md": "aval", "J2-AMONT.md": "amont"}
    ok = True
    def check(label, cond):
        nonlocal ok
        ok = ok and cond
        print(f"  [{'PASS' if cond else 'FAIL'}] {label}")

    print("=========== SELFTEST P-8 (v2.1) ===========")

    # T1 — DÉFAUT = séquencé, deux tranches, refus du bundle (i)
    _fixture(W, with_return=True, pieces=pieces)
    rc, rap = emit_tranches(W, phase, prompt_text="", regime="sequence")
    t1_ok = os.path.isdir(os.path.join(W, "TRANCHE-1"))
    t2_ok = os.path.isdir(os.path.join(W, "TRANCHE-2"))
    aval_in_t2 = os.path.exists(os.path.join(W, "TRANCHE-2", "J1-AVAL.md"))
    aval_not_t1 = not os.path.exists(os.path.join(W, "TRANCHE-1", "J1-AVAL.md"))
    amont_in_t1 = os.path.exists(os.path.join(W, "TRANCHE-1", "J2-AMONT.md"))
    check("(i) défaut séquencé : rc==0", rc == 0)
    check("(i) deux tranches nommées créées", t1_ok and t2_ok)
    check("(P-2) pièce AVAL en tranche 2, PAS en tranche 1", aval_in_t2 and aval_not_t1)
    check("(P-2) pièce AMONT en tranche 1", amont_in_t1)
    bloc_t1 = open(os.path.join(W, "TRANCHE-1", "BLOC-SHA-HARNAIS.md"), encoding="utf-8").read()
    check("(P-2) bloc-sha COMPLET en tranche 1", "segments_retires" in bloc_t1)

    # T2 — verrou P-1 : inapplicable REFUSÉ quand mécanisme de retour présent
    _fixture(W, with_return=True, pieces=pieces)
    rc, rap = emit_tranches(W, phase, prompt_text="", regime="inapplicable")
    check("(P-1) inapplicable REFUSÉ si canal multi-tours : rc==2", rc == 2)
    check("(P-1) aucun bundle unique produit au refus",
          not os.path.exists(os.path.join(W, "TRANCHE-1", "J1-AVAL.md")))

    # T3 — inapplicable HONORÉ si one-shot matériel ; clause P-6 écrite PAR LE SCRIPT (ii)
    _fixture(W, with_return=False, pieces=pieces)
    rc, rap = emit_tranches(W, phase, prompt_text="Paquet one-shot.", regime="inapplicable")
    prompt = open(os.path.join(W, "TRANCHE-1", "PROMPT.md"), encoding="utf-8").read()
    check("(ii) inapplicable honoré si one-shot : rc==0", rc == 0)
    check("(ii) clause P-6 écrite par le script dans le prompt",
          "P-6:INAPPLICABILITE" in prompt and "DEMANDE et non une CONTRAINTE" in prompt)
    check("(ii) bundle unique : pièce aval jointe au même envoi",
          os.path.exists(os.path.join(W, "TRANCHE-1", "J1-AVAL.md")))
    check("(P-6) clause P-6 NE déclenche PAS un faux positif P-7", scan_p7(prompt) == [])

    # T4 — scan P-7 (iii) : formulation interdite ⟹ rc==3
    _fixture(W, with_return=False, pieces=pieces)
    bad = "Lis la source. Cet ordre est contraignant : tu ne peux pas ouvrir J1."
    rc, rap = emit_tranches(W, phase, prompt_text=bad, regime="inapplicable")
    check("(iii) scan P-7 : formulation interdite ⟹ rc==3", rc == 3)
    check("(iii) scan P-7 détecte les deux formulations",
          set(scan_p7(bad)) >= {"cet ordre est contraignant", "tu ne peux pas"})
    check("(iii) P-7 propre sur un prompt licite",
          scan_p7("Merci de lire les pièces amont d'abord ; c'est une demande.") == [])

    # T5 — champ nommé (iv) émis dans les deux régimes valides
    _fixture(W, with_return=True, pieces=pieces)
    emit_tranches(W, phase, prompt_text="", regime="sequence")
    rf = open(os.path.join(W, "REGIME-LIVRAISON.txt"), encoding="utf-8").read()
    check("(iv) champ nommé regime_livraison présent (séquencé)",
          "regime_livraison: séquencé" in rf)
    _fixture(W, with_return=False, pieces=pieces)
    emit_tranches(W, phase, prompt_text="one-shot", regime="inapplicable")
    rf = open(os.path.join(W, "REGIME-LIVRAISON.txt"), encoding="utf-8").read()
    check("(iv) champ nommé regime_livraison présent (inapplicabilité déclarée)",
          "regime_livraison: inapplicabilité déclarée" in rf)

    print(f"\nSELFTEST P-8 : {'TOUS PASS' if ok else 'ÉCHEC'}")
    print("§6.4 : un selftest ne scelle/réduit/compte/démontre RIEN — il atteste")
    print("       le comportement de l'instrument, jamais une conclusion physique.")
    return 0 if ok else 1

# --------------------------------------------------------------------- entrée
def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        sys.exit(selftest())
    regime = "sequence"
    if "--regime" in args:
        i = args.index("--regime")
        regime = args[i + 1] if i + 1 < len(args) else "sequence"
    if regime not in ("sequence", "inapplicable"):
        print(f"régime inconnu : {regime!r} (attendu: sequence | inapplicable)")
        sys.exit(4)
    # build KPS : DORMANT si source retirée (paquet rendu K-B)
    if not [f for f in os.listdir(MOUNT) if canon(f) == SRC_NAME]:
        print(f"source {SRC_NAME} ABSENTE du mount (retirée capacité, clôture V95).")
        print("build KPS DORMANT — paquet rendu K-B. Vérifier P-8 par --selftest.")
        sys.exit(0)
    rc = build_kps()
    sys.exit(rc)

if __name__ == "__main__":
    main()
