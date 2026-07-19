#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_paquet_propre.py — sceau LC-RACCORD (attestation de PROPRETÉ, pas de physique)

Atteste que LC-WORK-NACTION-AVEUGLE-PAQUET.md ne contient AUCUNE valeur cible ni
phrase-indice de la réponse cherchée par la tâche aveugle.

Propriétés (conformes à la contrainte : audit FROID + AVEUGLE, sans fit-interne ni circularité) :
  - AVEUGLE : les motifs interdits ne figurent QUE sous forme de SHA-256 (FORBIDDEN_HASHES).
    Ce script ne contient donc aucune valeur en clair et peut être lu par l'agent aveugle
    sans rompre la blindure. Il ne référence jamais le coefficient c ni sa dérivation
    (aucune circularité : la propreté est indépendante de la justesse de la dérivation).
  - FROID  : on vérifie AUSSI que le bon objet est présent et complet (ancres de structure),
    pour qu'un paquet tronqué/vidé ne passe pas trivialement.
  - PARE-FEU : un canari injecté prouve que le détecteur n-gram MORD (error-injection),
    donc qu'un « tout passe » est exclu.

EXIT 0 ssi : paquet présent + complet (froid) ET aucun motif interdit (aveugle) ET pare-feu actif.

PORTÉE & LIMITE (à lire) :
  Ce sceau est un GARDE-FOU, PAS une preuve d'impossibilité de fuite. Il détecte la présence
  EXACTE (après normalisation NFC) des motifs surveillés, dans leurs orthographes Unicode usuelles
  ET quelques variantes ASCII (pi pour π, ^2 pour ², * ou . pour ·, - pour −, N pour 𝒩...).
  Il NE couvre PAS toutes les réécritures possibles d'un copier-coller ultérieur : espaces
  insécables, autres tirets/exposants Unicode, décompositions LaTeX (\\pi, \\frac), valeurs
  numériques développées (0.00101..., 3.16e-3...), ou la même quantité exprimée autrement.
  En clair : EXIT 0 atteste « aucune des formes connues n'est présente », pas « aucune fuite
  concevable n'existe ». La blindure de fond reste l'ABSENCE d'accès KB / l'Incognito.

Usage : python3 verif_paquet_propre.py [chemin_du_paquet]
        (défaut : LC-WORK-NACTION-AVEUGLE-PAQUET.md dans le répertoire courant)
"""
import sys, hashlib, unicodedata

DEFAULT_PKG = "LC-WORK-NACTION-AVEUGLE-PAQUET.md"
PKG = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PKG
MAXLEN = 24  # borne sup. (codepoints NFC) de longueur des motifs surveillés

# SHA-256 (NFC, utf-8) des motifs INTERDITS : valeurs cibles + phrases-indices.
# Hash uniquement — aucune valeur n'est reconstructible depuis ce fichier.
FORBIDDEN_HASHES = {
    "da94174432f28653e62e5e6d5db71816efd1e318f477d6e0c9629f3169fa3909",
    "40fc4a56efd3f6e21ec2ea995bf087b56acb68ba903cb11152729501521838ed",
    "06165e9d6077a4a5ad93889c67d3422413c3255adaa751322afb91c9fed86d48",
    "d26928bb13010131af26338ee8ce6840cdb261e2cbf4ae8bd9891d4df9be9179",
    "50c0600b0b182370f6266d1ee875a12405389e93fab5623de4538046fc793919",
    "4c5c26c3f56ddfc4b9a1589cc474ab9fc00ab193a8abdeae41543ecd5b2261e8",
    "b862a63b041667affc54379410f23dfbd9c92b7958b5039788051c83eb81f381",
    "2ee77eabde0715de401606b084975151b286230690d5309b3b09883ef7df7302",
    "7a389e0c6286bd1410d1d9b76e3c0d78cd73191c61ab84bcc9c3f002ec89896e",
    "bc0ee05d988a49604e64e0c8027c499bd27e3c985939d1e90d47d42ec8092e6a",
    "3f924599526989277c0eee387fe33526e0a49b79903e4d2f60f756e0d0be359f",
    # --- variantes ASCII / typographiques (pi, ^2, *, ., -, N pour 𝒩...) ---
    "65473892915259c88e4cad74cf53b8fe63e9eaf528e0315f776bbdb0e7cc403a",
    "c992972022ed9ee4a85825a2627d666a0fd9568b8f7b0b3a1b91fd113bc16454",
    "d12d53b0a51ef04b07ca0a2d36c8cebe86888671f216f006a6194cfd1e8fcec0",
    "d243c30fd1f5efc055701923505e07815ae2f08e69352986f9466267be1652f0",
    "4725271b25be93c4f8e875d384e145839773cd86a82f95967e7232286d1bd788",
    "8bafaab031f1e1278d7c5274bbeed8ed9b20530289f829dbd2794f00f0c32503",
    "b8f1b2680d1f96708d3a55ab87ae90e8720e9d45eff78986826fb59cde758b70",
    "2c1690153f75843079685caad47e8f5d118ce5f4627697fbc2259d085fa051ce",
    "4a3882f73370a22d0618bd75b1cd148c413ff256993956239b48b8341e2750c3",
    "cbab2c81a59b4c224e9b12b7f0aa1b1b5dd5d7540c540111f693fbe1032e4f37",
    "0b0a9b0243989edb017ba318b9e9bafe8c8abf616836e1350eb5524aa5576de6",
}

# Ancres de structure attendues (audit FROID : le bon objet, complet).
STRUCTURE_ANCHORS = [
    "Protocole de blindure",
    "AUCUN fichier du projet",        # règle no-KB
    "Osborn",                         # cible de normalisation nommée
    "c = ?",                          # livrable
    "verif_naction_aveugle.py",       # sceau attendu de l'agent
    "scalaire conforme libre",        # ancre de calibration permise
    "i^{d−1}",                        # réconciliation §4 (signe) présente comme item différé
]

def _norm(s: str) -> str:
    return unicodedata.normalize("NFC", s)

def _h(s: str) -> str:
    return hashlib.sha256(_norm(s).encode("utf-8")).hexdigest()

def ngram_hashes(text: str, maxlen: int = MAXLEN) -> set:
    """Tous les sous-mots (longueur 3..maxlen, codepoints NFC), hachés."""
    t = _norm(text)
    n = len(t)
    out = set()
    for L in range(3, maxlen + 1):
        for i in range(0, n - L + 1):
            out.add(_h(t[i:i + L]))
    return out

# ---------------------------------------------------------------------------
_n = 0
def check(cond, msg):
    global _n
    if not cond:
        print(f"ÉCHEC : {msg}", file=sys.stderr)
        sys.exit(1)
    _n += 1

# --- charge le paquet ---
try:
    with open(PKG, encoding="utf-8") as f:
        pkg = f.read()
except FileNotFoundError:
    print(f"ÉCHEC : paquet introuvable ({PKG})", file=sys.stderr)
    sys.exit(1)
check(len(pkg) > 1000, "paquet anormalement court (tronqué/vidé)")

# --- AUDIT FROID : structure attendue présente ---
for a in STRUCTURE_ANCHORS:
    check(_norm(a) in _norm(pkg), f"ancre de structure absente : {a!r}")

# --- AUDIT AVEUGLE : aucun motif interdit présent ---
pkg_hashes = ngram_hashes(pkg)
leaks = FORBIDDEN_HASHES & pkg_hashes
check(not leaks, f"FUITE : {len(leaks)} motif(s) interdit(s) détecté(s) dans le paquet")

# --- PARE-FEU (error-injection) : prouver que le détecteur mord ---
CANARY = "LC_CANARI_" + "NOSHIP42"   # 18 codepoints ≤ MAXLEN (détectable par le scanner)
canary_h = _h(CANARY)
check(canary_h not in pkg_hashes, "le canari ne doit pas préexister dans le paquet propre")
poisoned_hashes = ngram_hashes(pkg + "\n" + CANARY)
check(canary_h in poisoned_hashes, "PARE-FEU : le scanner n-gram ne voit pas le canari injecté")
# le même mécanisme appliqué à l'ensemble interdit étendu DOIT mordre sur le paquet pollué...
check((FORBIDDEN_HASHES | {canary_h}) & poisoned_hashes,
      "PARE-FEU : injection non détectée par le test d'appartenance")
# ...et NE doit PAS mordre sur le paquet propre (pas de faux positif)
check(not ((FORBIDDEN_HASHES | {canary_h}) & pkg_hashes),
      "faux positif : le paquet propre déclenche l'ensemble étendu")

print(f"OK — {_n} assertions. Paquet PROPRE (froid + aveugle), pare-feu actif. "
      f"Aucune valeur cible, aucun indice. EXIT 0.")
sys.exit(0)
