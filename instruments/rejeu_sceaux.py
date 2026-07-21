#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rejeu_sceaux.py — Silo G-3 (harnais de rejeu complet des sceaux sur le
layout git). Spécification figée par NOTE-REPRISE-GIT-S1 §4 (2026-07-21).

S'appuie sur run_sceau.py (G-2) : cwd = racine KB, zéro octet de sceau
modifié. Trois classes d'exécution :

  (i)   LIVE rapides   : verif_paquet_propre, verif_A4_QW,
                         verif_A4_QW_typeI_succ.
  (ii)  Canaris lourds : verif_nonlin_parity, verif_D3_P6_specB_oracle,
                         verif_A2_numerique, diag_bounces — timeout
                         >= 900 s chacun, à lancer en tâche longue.
  (iii) ARCHIVES       : rejeu opportuniste de instruments/
                         archives-scelees/, timeout court (120 s).

Trois issues par sceau : RC0 · RC!=0 · INEXECUTABLE-ICI (dépendance
mount, réseau coupé, timeout court) — la troisième N'EST PAS un échec,
c'est une délimitation d'environnement.

Usage :
  python3 instruments/rejeu_sceaux.py --phase rapides|canaris|archives|all
  python3 instruments/rejeu_sceaux.py --report   # (re)génère le rapport
Options : --timeout-canari S (défaut 900) · --timeout-archive S (défaut
120) · --kb-root DIR (défaut $LC_KB_ROOT sinon <depot>/kb).

Les résultats s'accumulent dans audit/rejeu_sceaux_resultats.json (une
entrée par sceau, la dernière exécution remplace la précédente) ; le
rapport audit/REJEU-SCEAUX.md est régénéré à chaque appel : par sceau —
zone, sha8, rc, durée, issue ; en tête — bilan et confrontation des sha8
au §9ter du manifeste pour les 7 sceaux LIVE.

§6.4 (G-3c, grade à ne jamais surclasser) : un rc 0 sur le clone atteste
UNE exécution sur CE clone à CETTE date. Il ne rejoue aucune gate, ne
requalifie aucun grade du mount, ne re-scelle rien. Un rc != 0 sur une
ARCHIVE se consigne et s'instruit au lot R-n correspondant — il ne
« casse » rien par lui-même.
"""
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INSTR = os.path.join(ROOT, "instruments")
ARCH = os.path.join(INSTR, "archives-scelees")
AUDIT = os.path.join(ROOT, "audit")
RESULTS = os.path.join(AUDIT, "rejeu_sceaux_resultats.json")
REPORT = os.path.join(AUDIT, "REJEU-SCEAUX.md")

# §9ter du manifeste (v2.124) — les 7 sceaux LIVE et leurs sha8 attendus.
SHA8_9TER = {
    "verif_paquet_propre.py": "051e2833",
    "verif_nonlin_parity.py": "9df8e53e",
    "verif_D3_P6_specB_oracle.py": "162696c1",
    "verif_A2_numerique.py": "76e9257c",
    "diag_bounces.py": "804b7f9b",
    "verif_A4_QW.py": "a4637a2c",
    "verif_A4_QW_typeI_succ.py": "79f09a8c",
}

RAPIDES = ["verif_paquet_propre.py", "verif_A4_QW.py",
           "verif_A4_QW_typeI_succ.py"]
CANARIS = ["verif_nonlin_parity.py", "verif_D3_P6_specB_oracle.py",
           "verif_A2_numerique.py", "diag_bounces.py"]

# Motifs (minuscules) dans stderr/stdout qui signalent une dépendance
# d'environnement et non un échec de sceau.
ENV_PATTERNS = ["/mnt/project", "modulenotfounderror", "no module named",
                "connection", "urlopen", "network", "name resolution",
                "temporary failure", "errno -3", "errno 111"]


def sha8(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:8]


def load_results():
    if os.path.isfile(RESULTS):
        with open(RESULTS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_results(res):
    os.makedirs(AUDIT, exist_ok=True)
    with open(RESULTS, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)


def classify(rc, timed_out, tail, timeout_short):
    if timed_out and timeout_short:
        return "INEXECUTABLE-ICI (timeout court)"
    if timed_out:
        return "RC!=0 (timeout long)"
    if rc == 0:
        return "RC0"
    low = tail.lower()
    for pat in ENV_PATTERNS:
        if pat in low:
            return "INEXECUTABLE-ICI (env: %s)" % pat.strip("/")
    return "RC!=0"


def run_one(path, kb, timeout, timeout_short, zone):
    name = os.path.basename(path)
    digest = sha8(path)
    t0 = time.time()
    timed_out = False
    tail = ""
    try:
        p = subprocess.run([sys.executable, path], cwd=kb, timeout=timeout,
                           capture_output=True, text=True, errors="replace")
        rc = p.returncode
        tail = ((p.stdout or "")[-2000:] + "\n" + (p.stderr or "")[-2000:])
    except subprocess.TimeoutExpired as e:
        rc, timed_out = 124, True
        tail = ((e.stdout or b"")[-2000:].decode("utf-8", "replace")
                if isinstance(e.stdout, bytes) else (e.stdout or ""))
    dt = time.time() - t0
    issue = classify(rc, timed_out, tail, timeout_short)
    entry = {
        "zone": zone, "sha8": digest, "rc": rc, "duree_s": round(dt, 1),
        "issue": issue, "timeout_s": timeout,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tail": tail[-600:].strip(),
    }
    print("  %-44s [%s] sha8=%s rc=%-3s %6.1fs  %s"
          % (name, zone, digest, rc, dt, issue))
    return name, entry


def gen_report(res):
    live = {k: v for k, v in res.items() if v["zone"] == "LIVE"}
    arch = {k: v for k, v in res.items() if v["zone"] == "ARCHIVE"}
    n_rc0 = sum(1 for v in res.values() if v["issue"] == "RC0")
    n_inex = sum(1 for v in res.values()
                 if v["issue"].startswith("INEXECUTABLE"))
    n_ko = len(res) - n_rc0 - n_inex

    lines = []
    a = lines.append
    a("# REJEU-SCEAUX — rapport du harnais G-3 (généré par "
      "`instruments/rejeu_sceaux.py`)")
    a("")
    a("Date de génération : %s · dépôt : layout git (KB sous `kb/`), "
      "lanceur G-2 (cwd = racine KB, zéro octet de sceau modifié)."
      % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    a("")
    a("## Bilan")
    a("")
    a("- Sceaux rejoués : **%d** (%d LIVE, %d ARCHIVE)"
      % (len(res), len(live), len(arch)))
    a("- Issues : **%d RC0** · **%d RC!=0** · **%d INEXECUTABLE-ICI** "
      "(délimitation d'environnement, PAS un échec)"
      % (n_rc0, n_ko, n_inex))
    a("")
    a("## Confrontation §9ter (les 7 sceaux LIVE du manifeste v2.124)")
    a("")
    a("| sceau | sha8 §9ter | sha8 clone | conforme | rc | issue |")
    a("|---|---|---|---|---|---|")
    for name, expected in SHA8_9TER.items():
        v = res.get(name)
        if v is None:
            a("| %s | %s | — | NON REJOUÉ | — | — |" % (name, expected))
            continue
        ok = "OUI" if v["sha8"] == expected else "**ÉCART**"
        a("| %s | %s | %s | %s | %s | %s |"
          % (name, expected, v["sha8"], ok, v["rc"], v["issue"]))
    a("")
    a("Rappel de grade : un sha8 conforme n'atteste que l'identité des "
      "octets ; un rc 0 n'atteste qu'UNE exécution sur CE clone à CETTE "
      "date (G-3c).")
    a("")
    for title, group in (("## Sceaux LIVE", live), ("## ARCHIVES", arch)):
        a(title)
        a("")
        a("| sceau | sha8 | rc | durée (s) | timeout (s) | issue | date |")
        a("|---|---|---|---|---|---|---|")
        for name in sorted(group):
            v = group[name]
            a("| %s | %s | %s | %s | %s | %s | %s |"
              % (name, v["sha8"], v["rc"], v["duree_s"], v["timeout_s"],
                 v["issue"], v["date"]))
        a("")
    a("## §6.4 — grade, à ne jamais surclasser (G-3c)")
    a("")
    a("Un rc 0 sur le clone atteste UNE exécution sur CE clone à CETTE "
      "date. Il ne rejoue aucune gate, ne requalifie aucun grade du "
      "mount, ne re-scelle rien. Un rc != 0 sur une ARCHIVE se consigne "
      "et s'instruit au lot R-n correspondant — il ne « casse » rien par "
      "lui-même. INEXECUTABLE-ICI est une délimitation d'environnement "
      "(dépendance mount, réseau coupé, timeout court), pas un échec. "
      "{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.")
    a("")
    os.makedirs(AUDIT, exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Rapport écrit : %s" % REPORT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["rapides", "canaris", "archives",
                                        "all"], default=None)
    ap.add_argument("--only", help="rejouer un seul sceau (nom)")
    ap.add_argument("--report", action="store_true",
                    help="(re)générer le rapport seulement")
    ap.add_argument("--timeout-canari", type=int, default=900)
    ap.add_argument("--timeout-archive", type=int, default=120)
    ap.add_argument("--kb-root",
                    default=os.environ.get("LC_KB_ROOT",
                                           os.path.join(ROOT, "kb")))
    ns = ap.parse_args()

    kb = os.path.abspath(ns.kb_root)
    if not os.path.isdir(kb):
        sys.exit("ERREUR : racine KB introuvable (%s)" % kb)

    res = load_results()

    def do(names, base, timeout, timeout_short, zone):
        for n in names:
            p = os.path.join(base, n)
            if not os.path.isfile(p):
                print("  %-44s ABSENT" % n)
                continue
            name, entry = run_one(p, kb, timeout, timeout_short, zone)
            res[name] = entry
            save_results(res)

    if ns.only:
        n = ns.only if ns.only.endswith(".py") else ns.only + ".py"
        if os.path.isfile(os.path.join(INSTR, n)):
            do([n], INSTR, ns.timeout_canari, False, "LIVE")
        elif os.path.isfile(os.path.join(ARCH, n)):
            do([n], ARCH, ns.timeout_archive, True, "ARCHIVE")
        else:
            sys.exit("ERREUR : sceau introuvable (%s)" % n)
    elif ns.phase in ("rapides", "all"):
        print("— phase (i) LIVE rapides —")
        do(RAPIDES, INSTR, 300, False, "LIVE")
    if ns.phase in ("canaris", "all"):
        print("— phase (ii) canaris lourds (timeout %ds) —"
              % ns.timeout_canari)
        do(CANARIS, INSTR, ns.timeout_canari, False, "LIVE")
    if ns.phase in ("archives", "all"):
        print("— phase (iii) ARCHIVES (timeout %ds) —"
              % ns.timeout_archive)
        names = sorted(f for f in os.listdir(ARCH) if f.endswith(".py"))
        do(names, ARCH, ns.timeout_archive, True, "ARCHIVE")

    gen_report(res)
    print("§6.4 : ce rapport atteste des exécutions sur CE clone — "
          "rien d'autre.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
