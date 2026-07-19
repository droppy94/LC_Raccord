#!/usr/bin/env python3
# =====================================================================
# LC-WORK-BOOT-SESSION.py  —  BOOT DE SESSION, OPERATION #1, UNE COMMANDE
# codename: LC-RACCORD   |   v1.3   |   2026-07-20   |   session V95
#
# INVOCATION (premiere action de la session, avant tout autre geste) :
#     python3 "$(ls /mnt/project/LC-WORK-BOOT-SESSION*.py | head -1)"
#
# REGIME : LC-CONST-V1 ; §4.1 (comparateur S2) ; §9.1/§9.2 adoptees par D.
#
# v1.3 — CE QUI A CHANGE (session V95, 2026-07-20). GO D.
#   (a) ATTENDU CORRIGE : N_autre 1 -> 0. Le pdf source a ete RETIRE pour
#       capacite (KB >100%) le 2026-07-20 ; le mount fait foi. Defaut boot-ATTENDU SOLDE.
#   (b) FIREWALL ETENDU : scan BETA-* a cote de LC-ART. !=0 (LC-ART OU BETA-*) = CONTAMINATION.
#   (c) REGLE DE SEQUENCE (opposable, GO D 2026-07-20) : imprimee ci-dessous. Consignation =
#       DERNIER geste ; PKG de cloture calcule UNE fois apres TOUS les depots haches ; porte
#       par le MANIFESTE (PKG-exclu), JAMAIS par la reprise (hachee). Recette C-pkgsha INTOUCHEE.
#
# v1.2 — CE QUI A CHANGE, ET POURQUOI. LIRE AVANT DE S'EN SERVIR.
#   Tier 1 (3)+(4) de LC-WORK-AMENDEMENT-R7-CONVERSION-R56-M1 (gel 2d82fc1e,
#   GO D 2026-07-17). LISTE CLOSE :
#   (3) CONVERSION .txt => .py : l'instrument ENTRE DANS LE HACHAGE. Toute
#       derive deplace desormais le PKG-SHA. La nudite (defaut #1) est
#       ETEINTE PAR CONSTRUCTION. Recette C-pkgsha gelee INTOUCHEE. Exclu
#       NOMMEMENT du scope S2 au comparateur v1.2 (aucune charge de sceau).
#   (4a) ATTENDUS CORRIGES (defauts #7 et #7-aggrave) : N_autre 1 (le pdf
#       source hache), txt_exclus 0 (plus aucun .txt d'instrument), boot
#       compte en .py. L'attendu du v1.1 etait FAUX et le restait.
#   (4b) §6.4 CORRIGE (defaut #9) : la clause « pivot O2 CLOS NEGATIF »
#       etait LA CONTAMINATION DE L'INSTRUMENT — l'etat est « O2 NON
#       construit ». C'est ce que ce boot imprime desormais.
#   Le port bash => python est a IMPRESSION IDENTIQUE hors ces corrections.
#   v1.1 avait supprime §T0 (setsid mort en silence) : INCHANGE ici.
#
# NATURE : INSTRUMENT HACHE. Il ne scelle rien, ne vote rien, ne fait foi
#   de rien. LE MANIFESTE FAIT FOI (R-54). Toute valeur ATTENDUE ci-dessous
#   est une DECLARATION A VERIFIER, jamais une source. En cas d'ecart :
#   LE MOUNT A RAISON.
# =====================================================================
import os, re, sys, glob, hashlib, subprocess

W = '/home/claude/work'
os.makedirs(W, exist_ok=True)
D = '/mnt/project'

print("############ §0-lite — PAR SCRIPT. ZERO OCTET DE GOUVERNANCE EN CONTEXTE ############")
# RAPPEL BLOQUANT : UN FICHIER DE GOUVERNANCE NE SE LIT PAS, IL SE MESURE.
# view/head/cat sur manifeste, IDX, GLO, AUD, cache : PROSCRITS (lecon V85).

PKGSHA_SRC = '''# Recette C-pkgsha, GELEE R-36, reconstruite depuis le corps du manifeste.
import os, re, hashlib
D = '/mnt/project'
def canon(fn): return re.sub(r'__\\d+_(?=\\.(md|py)$)', '', fn)
rows, n_manif, n_txt = [], 0, 0
for fn in sorted(os.listdir(D)):
    p = os.path.join(D, fn)
    if not os.path.isfile(p): continue
    if fn.startswith('LC-WORK-AUDIT-PAQUET-GEL'): n_manif += 1; continue   # exclu
    if fn.endswith('.txt'): n_txt += 1; continue                            # exclu
    rows.append((canon(fn), hashlib.sha256(open(p,'rb').read()).hexdigest()))
payload = "\\n".join(sorted(f"{c}  {h}" for c, h in rows))   # 2 espaces, PAS de \\n terminal
pkg = hashlib.sha256(payload.encode()).hexdigest()
cn = [c for c, _ in rows]
print("PKG_SHA_8       ", pkg[:8])
print("PKG_SHA_full    ", pkg)
print("N_haches        ", len(rows))
print("N_md            ", sum(1 for c in cn if c.endswith('.md')))
print("N_py            ", sum(1 for c in cn if c.endswith('.py')))
print("N_autre         ", sum(1 for c in cn if not c.endswith(('.md','.py'))))
print("doublons_canon  ", len(cn) - len(set(cn)))
print("manifestes_exclus", n_manif)
print("txt_exclus      ", n_txt)
'''
open(os.path.join(W, 'pkgsha.py'), 'w', encoding='utf-8').write(PKGSHA_SRC)
subprocess.run([sys.executable, os.path.join(W, 'pkgsha.py')])
print()

print("---- SCEAUX S2 — COMPARATEUR (§4.1). NE REJOUE RIEN. DIT QUOI REJOUER. ----")
s2 = sorted(glob.glob(os.path.join(D, 'sceau_s2*.py')))
if not s2:
    print("!! sceau_s2.py ABSENT DU MOUNT => AUCUN sceau S2 n'est acquis. DEFAUT.")
    rc = 2
else:
    rc = subprocess.run([sys.executable, s2[0]], cwd=D).returncode
    print(f"rc_comparateur {rc}   (0=tous acquis | 1=rejeu du OU non-scellable | 2=cache absent)")
    if rc != 0:
        print("   *** §0-full NON ACQUIS. Rejouer EN AVANT-PLAN les .py signales, PAS en detache.")
        print("   *** (le setsid meurt en silence : constat V87, cf. v1.1.)")
print()

print("---- FIREWALL : PAR LS SUR LE MOUNT, JAMAIS PAR GREP DANS UN FICHIER ----")
f = [x for x in os.listdir(D) if os.path.isfile(os.path.join(D, x))]
print("LC-ART_sur_mount", sum(1 for x in f if x.startswith('LC-ART')))
print("BETA_sur_mount  ", sum(1 for x in f if x.startswith('BETA-')))
print("journaux        ", sum(1 for x in f if 'JOURNAL' in x))
print("notes_reprise   ", sum(1 for x in f if 'REPRISE' in x))
print("manifestes      ", sum(1 for x in f if x.startswith('LC-WORK-AUDIT-PAQUET-GEL')))
print("boot_py         ", sum(1 for x in f if 'BOOT-SESSION' in x))
print("txt_sur_mount   ", sum(1 for x in f if x.endswith('.txt')))
print("constitution    ", sum(1 for x in f if x.startswith('LC-CONST-V1')))
print("cache_S2        ", sum(1 for x in f if x.startswith('LC-SCEAU-S2-CACHE')))
print("suffixes_mount  ", sum(1 for x in f if re.search(r'__\d+_\.(md|py)$', x)),
      "(artefact de mount connu, absorbe par canon ; doublons_canon=0 fait foi)")
print()

print("---- REGLE DE SEQUENCE (opposable, adoptee 2026-07-20) ----")
print("  1. La CONSIGNATION est le DERNIER geste de la discussion.")
print("  2. Le PKG de cloture se calcule UNE SEULE fois, APRES tous les depots haches.")
print("  3. Rien de hache n'est depose APRES la consignation (sinon PKG desynchronise).")
print("  4. Le PKG de cloture est porte par le MANIFESTE (PKG-exclu), JAMAIS par la reprise")
print("     (hachee => circularite interdite, R-36 generalise).")
print("  5. Tout fichier SORTI de KB active : sha256 consigne au manifeste (registre de")
print("     sortie) pour authentifier un eventuel re-import.")
print()
print("---- STACK ----")
import sympy, numpy, scipy, networkx
sk = "/".join([sys.version.split()[0], sympy.__version__, numpy.__version__,
               scipy.__version__, networkx.__version__])
print("stack    ", sk)
print("sha_stack", hashlib.sha256(sk.encode()).hexdigest()[:8],
      "(cle des sceaux S2 ; s'il bouge, TOUT rejeu est du)")
print("cpu      ", os.cpu_count())
print()

print("---- INTEGRITE DE CET INSTRUMENT (il se verifie, il ne se presume pas) ----")
g = sorted(glob.glob(os.path.join(D, 'LC-WORK-BOOT-SESSION*.py')))
if not g:
    print("boot_sha8  ABSENT DU MOUNT -- tu executes une copie HORS-KB, NON consignee,")
    print("           donc NON confrontable. Ce n'est PAS un succes.")
for p in g:
    print("boot_sha8", hashlib.sha256(open(p, 'rb').read()).hexdigest()[:8],
          "<-- CONFRONTER AU MANIFESTE. Divergence ==> STOP.")
    print("           (un sha conforme n'atteste que les octets, JAMAIS une conclusion.)")
    print("           v1.2 : l'instrument est HACHE => toute derive deplace le PKG-SHA.")
    print("           Le defaut #1 (instrument nu) est ETEINT PAR CONSTRUCTION.")

print("""
############ ATTENDU — DECLARE ICI, A VERIFIER CI-DESSUS. LE MOUNT ARBITRE ############

  PKG_SHA_8        <== porte par le MANIFESTE apres consignation du dernier depot.
                       Tout depot DOIT l'avoir deplace (les instruments sont HACHES
                       depuis v1.2), et l'ecart doit etre BORNE ET NOMME.
  doublons_canon   0
  N_autre          0            <== v1.3 : pdf source RETIRE (capacite, 2026-07-20). Etait 1 en v1.2.
  manifestes_exclus 1 | txt_exclus 0   <== correctif #7-aggrave : plus AUCUN .txt d'instrument
  LC-ART_sur_mount 0 | BETA_sur_mount 0   <== TOUTE valeur !=0 = CONTAMINATION inter-projet : stop.
  txt_sur_mount    0 | boot_py 1 | constitution 1 | cache_S2 1
  rc_comparateur   0            <== 0 = tous sceaux acquis ; instruments_exclus 4 attendu.
  stack            3.12.3/1.14.0/2.4.4/1.17.1/3.6.1  (sha_stack 2a578f37) | cpu 1

############ §0-full — CE QU'IL EST DEVENU (§4.1) ############

  §0-full FRAIS = §0-lite ci-dessus + rc_comparateur == 0.
  Un sceau S2 est ACQUIS ET LE RESTE tant que sa cle est inchangee. Rejouer une
  fonction deterministe sur des entrees gelees ne teste QUE la gelure des entrees
  — que la cle teste mieux, et en 40ms au lieu de 300s.
  SI une cle bouge : rejeu OBLIGATOIRE, EN AVANT-PLAN, et mise a jour du cache.
  Les instruments (liste nommee au comparateur) n'ont AUCUNE charge de sceau :
  ils n'assertent aucune physique ; leur integrite est portee par le PKG-SHA.

  RESERVE, ET ELLE M'EST OPPOSABLE : la definition faisant foi du §0-full est au
  manifeste, dont le corps §0 est en LAG. Si le manifeste exige davantage que ce
  que ce script instrumente, CE SCRIPT EST INCOMPLET ET C'EST UN DEFAUT A
  CONSIGNER, pas un acquis a presumer. Le regime §4.1 prevaut sur le corps §0 du
  manifeste UNIQUEMENT parce que D l'a adopte explicitement le 2026-07-16.

############ §6.4 — SENTINELLE ############

  Booter une session, recomputer un PKG-SHA, comparer des cles de sceaux :
  cela NE SCELLE, NE REDUIT, NE COMPTE, NE DEMONTRE RIEN.
  {A4 ; A2* ; N} INCHANGE. O2 NON CONSTRUIT (correctif #9 : la clause
  « clos negatif » du v1.1 etait la contamination de l'instrument, pas l'etat).
  beta T-b non resolu. R-53 0/4. Tetes scellees = AUTORITE, INTACTES.
  CCC non demontree NI refutee.""")
sys.exit(0)
