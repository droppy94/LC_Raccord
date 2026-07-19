#!/usr/bin/env python3
# =====================================================================
# sceau_s2.py — GESTIONNAIRE DE SCEAUX S2   |  LC-RACCORD  |  v1.3
# Constitution LC-CONST-V1 §4.1 (amendee 2026-07-16).
#
# CE QU'IL FAIT : compare la CLE de chaque .py du mount a la cle consignee
#   au cache. Cle = sha256( sha_py || sha_stack || sha_entrees_declarees ).
#   Cle identique  => sceau S2 ACQUIS, rejeu INTERDIT (il n'apprendrait rien).
#   Cle differente => rejeu OBLIGATOIRE, et le cache est PERIME sur cette ligne.
#
# CE QU'IL N'EST PAS : il ne rejoue rien lui-meme, il ne depose rien, il ne
#   scelle rien. C'est un COMPARATEUR. Il dit quoi rejouer. D decide.
#
# GRADE : INSTRUMENT. Ne fait foi de rien. En ecart avec le mount : LE MOUNT
#   A RAISON (R-54). Un sha conforme n'atteste QUE les octets, JAMAIS un EXIT 0.
#
# ENTREES DECLAREES (§4.1) : tout .py non declare ici n'est PAS scellable S2.
#   La declaration est un ACTE, pas une inference : on ne devine pas les
#   dependances d'un script, on les nomme.
#
# v1.1 — 2026-07-16 — CORRECTION DU SELF-MATCH, 10e entree a la dette d'instrument.
#   v1.0 se scannait LUI-MEME, ne se trouvait pas au cache, se declarait
#   NON SCELLABLE, et rendait rc=1 A PERPETUITE. Un boot testant rc aurait
#   toujours echoue ==> on aurait appris a ignorer son verdict.
#   MEME FAMILLE que la 8e (le scan qui se matche) et la 9e (`pkill -f verif_`
#   qui a tue son propre shell). TROISIEME occurrence du meme motif.
#
#   EXCLUSION PAR NOMS EXPLICITES, ET CE N'EST PAS UN DETAIL : un motif
#   (`^sceau_`, `*_s2.py`) avalerait EN SILENCE tout fichier futur ainsi nomme.
#   Chaque exclusion doit etre un ACTE, visible, nomme, contestable.
#
# v1.2 — 2026-07-17 — TROIS EXCLUSIONS NOMMEES AJOUTEES (Tier 1 (3),
#   amendement R-7 CONVERSION-R56-M1, gel 2d82fc1e, GO D 2026-07-17) :
#   les instruments boot / gen-index / gen-paquet, convertis .txt => .py,
#   entrent au hachage SANS charge de sceau. Chaque ligne ci-dessous est
#   l'ACTE prevu par le present cartouche. AUCUN motif, AUCUNE autre ligne
#   touchee : le corps v1.1 est byte-verbatim hors ces ajouts.
#
# v1.3 — 2026-07-20 — DEUX EXCLUSIONS NOMMEES AJOUTEES (front p_Q, GO D
#   2026-07-20) : dico_Q.py et audit_neutral_dico.py, deposes avec le REPRISE
#   reduction-pQ. AUCUN des deux n'asserte de physique via EXIT-0-gate : ils
#   IMPRIMENT des quantites reproductibles, sans assert ni sys.exit de passage.
#   Le REPRISE etablit que dico_Q « ne tranche rien » (checks garantis par
#   construction) et audit_neutral_dico EST l'audit froid neutralise. Donc
#   INSTRUMENTS, hors S2, integrite portee par le PKG-SHA. Chaque ligne est
#   l'ACTE prevu ; AUCUN motif ; corps v1.2 byte-verbatim hors ces deux ajouts.
# =====================================================================
import os, re, sys, json, hashlib, glob

D = '/mnt/project'
CACHE_GLOB = '/mnt/project/LC-SCEAU-S2-CACHE*.md'

# INSTRUMENTS : n'assertent aucune physique, ne scellent rien ==> hors S2.
# Un instrument n'est pas un sceau : il n'y a rien a rejouer, rien a attester.
# LISTE NOMMEE, JAMAIS UN MOTIF. Ajouter une ligne ici est une DECISION.
INSTRUMENTS = {
    'sceau_s2.py',        # ce comparateur lui-meme (v1.1, self-match corrige)
    'LC-WORK-BOOT-SESSION.py',       # boot de session (v1.2, ex-.txt) — Tier 1 (3)
    'LC-WORK-GEN-INDEX.py',          # generateur d'index derive (ex-.txt) — Tier 1 (3)
    'LC-WORK-GEN-PAQUET-CSE2.py',    # redacteur de paquet CSE-2 (ex-.txt) — Tier 1 (3)
    'dico_Q.py',                     # dict. Q<->N/ell (front p_Q) — « ne tranche rien » — v1.3
    'audit_neutral_dico.py',         # audit froid neutralise de dico_Q — v1.3
}

def canon(fn):
    return re.sub(r'__\d+_(?=\.(md|py)$)', '', fn)

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def resolve(c):
    """Resout un nom canonique vers son chemin reel (les suffixes mount __N_ bougent)."""
    base, ext = os.path.splitext(c)
    g = [p for p in glob.glob(os.path.join(D, base + '*' + ext))
         if canon(os.path.basename(p)) == c]
    return g[0] if g else None

def stack_id():
    import sympy, numpy, scipy, networkx
    return "/".join([sys.version.split()[0], sympy.__version__,
                     numpy.__version__, scipy.__version__, networkx.__version__])

def cle(sha_py, sha_stack, shas_entrees):
    payload = sha_py + "|" + sha_stack + "|" + "|".join(sorted(shas_entrees))
    return hashlib.sha256(payload.encode()).hexdigest()

def charger_cache():
    g = glob.glob(CACHE_GLOB)
    if not g:
        return None, "CACHE ABSENT DU MOUNT"
    txt = open(g[0], encoding='utf-8').read()
    m = re.search(r'```json\s*(.*?)```', txt, re.S)
    if not m:
        return None, "CACHE PRESENT MAIS BLOC JSON INTROUVABLE -- DEFAUT"
    return json.loads(m.group(1)), None

def main():
    cache, err = charger_cache()
    sk_now = stack_id()
    sha_stack_now = hashlib.sha256(sk_now.encode()).hexdigest()

    print("stack_courante ", sk_now)
    print("sha_stack      ", sha_stack_now[:8])
    if err:
        print("!! ", err)
        print("   => AUCUN sceau S2 n'est acquis. Tout rejeu est a faire.")
        return 2
    print("cache_stack    ", cache['stack'], "->",
          "IDENTIQUE" if cache['sha_stack'] == sha_stack_now else "*** DIVERGENT : REJEU GLOBAL ***")
    print("cache_date     ", cache['date'])
    print()

    decl = cache['entrees']          # canon_py -> [canon_entree, ...]
    seals = cache['sceaux']          # canon_py -> {...}

    tous = sorted(canon(os.path.basename(p)) for p in glob.glob(os.path.join(D, '*.py')))
    pys = [c for c in tous if c not in INSTRUMENTS]
    exclus = [c for c in tous if c in INSTRUMENTS]

    print(f"{'py':40s} {'sha8':10s} {'verdict':28s} motif")
    print("-" * 110)
    for c in exclus:
        p = resolve(c)
        print(f"{c:40s} {sha(p)[:8]:10s} {'INSTRUMENT — hors S2':28s} exclu NOMMEMENT, n'asserte aucune physique")
    rejeu, acquis, orphelins = [], [], []

    for c in pys:
        p = resolve(c)
        s_py = sha(p)
        if c not in decl:
            orphelins.append(c)
            print(f"{c:40s} {s_py[:8]:10s} {'NON SCELLABLE':28s} entrees NON DECLAREES (§4.1)")
            continue
        shas_e, manquantes = [], []
        for e in decl[c]:
            pe = resolve(e)
            if pe is None:
                manquantes.append(e)
            else:
                shas_e.append(sha(pe))
        if manquantes:
            rejeu.append(c)
            print(f"{c:40s} {s_py[:8]:10s} {'REJEU — ENTREE ABSENTE':28s} {', '.join(manquantes)}")
            continue
        k = cle(s_py, sha_stack_now, shas_e)
        ref = seals.get(c)
        if ref is None:
            rejeu.append(c)
            print(f"{c:40s} {s_py[:8]:10s} {'REJEU — JAMAIS SCELLE':28s} absent du cache")
        elif ref['cle'] != k:
            rejeu.append(c)
            quoi = []
            if ref['sha_py'] != s_py: quoi.append("sha_py a bouge")
            if cache['sha_stack'] != sha_stack_now: quoi.append("stack a bouge")
            if ref.get('sha_entrees', []) != sorted(shas_e): quoi.append("entree a bouge")
            print(f"{c:40s} {s_py[:8]:10s} {'*** REJEU OBLIGATOIRE ***':28s} {' + '.join(quoi) or 'cle divergente'}")
        elif ref['exit'] != 0:
            rejeu.append(c)
            print(f"{c:40s} {s_py[:8]:10s} {'REJEU — EXIT!=0 au cache':28s} exit={ref['exit']}")
        else:
            acquis.append(c)
            print(f"{c:40s} {s_py[:8]:10s} {'ACQUIS (rejeu inutile)':28s} EXIT 0 du {ref['date']} ({ref['duree_s']}s)")

    fantomes = [c for c in seals if c not in pys]
    print("-" * 110)
    print(f"acquis {len(acquis)} | rejeu {len(rejeu)} | non_scellables {len(orphelins)} "
          f"| instruments_exclus {len(exclus)} | fantomes_cache {len(fantomes)}")
    if fantomes:
        print("  fantomes (au cache, absents du mount) :", ", ".join(fantomes))
    if rejeu:
        print("  A REJOUER :", ", ".join(rejeu))
    print()
    print("RAPPEL §4.2 : un sha conforme n'atteste que les octets, JAMAIS un EXIT 0.")
    print("RAPPEL §6.4 : comparer des sceaux ne scelle, ne reduit, ne compte, ne demontre RIEN.")
    return 0 if not rejeu and not orphelins else 1

if __name__ == '__main__':
    sys.exit(main())
