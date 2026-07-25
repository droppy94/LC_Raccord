#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# LC-BETA-BOOT v1.0 — §0-lite-beta. AUTOPORTANT : n'exige NI le mount principal,
# NI reseau, NI dependance hors stdlib.
#
# Ce qu'il fait  : recompute PKG_SHA_BETA (recette C-pkgsha, R-36, REUTILISEE
#                  telle quelle) ; verifie les 35 copies contre le manifeste ;
#                  passe le pare-feu bidirectionnel.
# Ce qu'il ne fait PAS : attester une physique, valider un verdict, remplacer
#                  le mount principal (R-54). Il n'atteste QUE des octets.
#
# R-36 : ce script n'embarque AUCUNE valeur de PKG_SHA_BETA attendue.
#        L'operateur la consigne HORS-FICHIER et compare a l'oeil.
#        Un paquet qui certifie son propre hash ne certifie rien.

import os, re, sys, hashlib

D = os.path.dirname(os.path.abspath(__file__))

def canon(fn):
    return re.sub(r'__\d+_(?=\.(md|py)$)', '', fn)

# ---------------------------------------------------------------- PKG_SHA_BETA
rows, n_manif, n_txt = [], 0, 0
for fn in sorted(os.listdir(D)):
    p = os.path.join(D, fn)
    if not os.path.isfile(p):
        continue
    if fn.startswith('LC-BETA-PAQUET-GEL'):        # le manifeste : exclu
        n_manif += 1; continue
    if fn.endswith('.txt'):                        # exclu
        n_txt += 1; continue
    rows.append((canon(fn), hashlib.sha256(open(p, 'rb').read()).hexdigest()))

payload = "\n".join(sorted(f"{c}  {h}" for c, h in rows))   # 2 espaces, PAS de \n terminal
pkg = hashlib.sha256(payload.encode()).hexdigest()

print("=" * 66)
print("  §0-lite-beta — LC-BETA-BOOT v1.0")
print("=" * 66)
print("PKG_SHA_BETA_8   ", pkg[:8])
print("PKG_SHA_BETA_full", pkg)
print("N_haches         ", len(rows))
cn = [c for c, _ in rows]
print("doublons_canon   ", len(cn) - len(set(cn)))
print("manifestes_exclus", n_manif, "| txt_exclus", n_txt)

# ------------------------------------------------- copies vs manifeste (35 att.)
man = os.path.join(D, 'LC-BETA-PAQUET-GEL.md')
absents, alterees, n_att = [], [], 0
if not os.path.exists(man):
    print("\n!! MANIFESTE ABSENT — le gel de dossier n'est pas verifiable. STOP.")
    sys.exit(2)

for line in open(man, encoding='utf-8'):
    m = re.match(r'^\|\s*`([A-Za-z0-9._-]+\.(?:md|py))`\s*\|\s*`([0-9a-f]{64})`\s*\|', line)
    if not m:
        continue
    n_att += 1
    src_canon, sha_att = m.group(1), m.group(2)
    p = os.path.join(D, 'BETA-COPIE-' + src_canon)
    if not os.path.exists(p):
        absents.append(src_canon); continue
    if hashlib.sha256(open(p, 'rb').read()).hexdigest() != sha_att:
        alterees.append(src_canon)

print("\ncopies_attendues ", n_att)
print("absents          ", len(absents), absents if absents else "")
print("alterees         ", len(alterees), alterees if alterees else "")

# ------------------------------------------------------------------- pare-feu
intrus = [f for f in os.listdir(D)
          if os.path.isfile(os.path.join(D, f))
          and not (f.startswith('LC-BETA-') or f.startswith('BETA-COPIE-'))]
print("pare-feu intrus  ", len(intrus), intrus if intrus else "")

principal = "/mnt/project"
fuite = []
if os.path.isdir(principal):
    fuite = [f for f in os.listdir(principal)
             if f.startswith('LC-BETA-') or f.startswith('BETA-COPIE-')]
    print("fuite vers KB    ", len(fuite), fuite if fuite else "")
else:
    print("fuite vers KB     (mount principal non monte ici — normal, regime consommateur)")

# --------------------------------------------------------------------- verdict
rc = 0
if absents or alterees or intrus or fuite or (len(cn) - len(set(cn))):
    rc = 1

print("\n" + "-" * 66)
if rc:
    print("  ECART. Le BORNER et le NOMMER avant toute suite. Ne pas continuer.")
else:
    print("  Conforme sur les OCTETS.")
    print("  Comparer PKG_SHA_BETA_8 a la valeur consignee HORS-FICHIER (R-36).")
print("-" * 66)
print("""
CE QUE CE rc=0 N'ATTESTE PAS :
  - que le dossier gele est A JOUR   -> il date du 2026-07-18 / V94 / v2.121.
    Si la KB a bouge, il ment PAR AGE. Le mount principal arbitre (R-54).
  - une physique, un verdict, une pertinence de S8/S9/S10.
  - que P-8 est solde. Il ne l'est pas. Pas de gate sans P-8 (V94 §4).
§6.4 : {A4 ; A2*  ; N} INCHANGE. beta T-b, SEUL facteur d'O2 ouvert. R-53 0/4.
       CCC n'est ni demontree ni refutee.
""")
sys.exit(rc)
