#!/usr/bin/env python3
# =====================================================================
# LC-WORK-GEN-INDEX.py — GENERATEUR D'INDEX DERIVE (§5.2 / §9.5)
# codename: LC-RACCORD   |   v1.1   |   2026-07-17   |   session V92
#
# INVOCATION :
#     python3 "$(ls /mnt/project/LC-WORK-GEN-INDEX*.py | head -1)"
#
# REGIME : LC-CONST-V1 §5.2, ADOPTEE par D le 2026-07-16 (§9.5).
#          Execution d'une decision acquise. Ce script ne decide RIEN.
#
# v1.1 — CONVERSION .txt => .py (Tier 1 (3), amendement R-7 CONVERSION-R56-M1
#   gel 2d82fc1e, GO D 2026-07-17). L'instrument ENTRE DANS LE HACHAGE :
#   toute derive deplace desormais le PKG-SHA. La nudite (defaut #1) est
#   ETEINTE PAR CONSTRUCTION, pas par consignation. Recette C-pkgsha gelee
#   INTOUCHEE (elle hachait deja tout .py). Exclu NOMMEMENT du scope S2 au
#   comparateur v1.2 : instrument, aucune physique, rien a sceller.
#   DELTAS vs v1.0 (.txt), LISTE CLOSE : (i) ce cartouche ; (ii) OUT en dur
#   (l'argv bash disparait avec le wrapper) ; (iii) banner de l'index derive
#   .txt => .py. LE CORPS EST BYTE-VERBATIM pour tout le reste.
#
# NATURE : INSTRUMENT HACHE. Il ne scelle rien, ne vote rien, ne fait foi
#          de rien. LE MOUNT FAIT FOI (R-54). Il produit un objet DERIVE et
#          un DIAGNOSTIC DE PARITE ; le remplacement d'IDX/GLO/AUD est un
#          ACTE DE D (b3). Bornes b1-b6 du v1.0 INCHANGEES.
# =====================================================================
import os
os.makedirs('/home/claude/work', exist_ok=True)

import os, re, sys, hashlib, datetime

D   = '/mnt/project'
OUT = '/home/claude/work/LC-INDEX-DERIVE.md'

def canon(fn):
    return re.sub(r'__\d+_(?=\.(md|py)$)', '', fn)

# ---------------------------------------------------------------- collecte
files = sorted(f for f in os.listdir(D) if os.path.isfile(os.path.join(D, f)))
rows  = []
for fn in files:
    p     = os.path.join(D, fn)
    raw   = open(p, 'rb').read()
    sha   = hashlib.sha256(raw).hexdigest()
    c     = canon(fn)
    rec   = {'canon': c, 'sha': sha, 'octets': len(raw), 'id': '', 'version': '',
             'date': '', 'gel': '', 'statut': '', 'prereq': 0, 'fm': False}
    if fn.endswith('.md'):
        try:
            txt = raw.decode('utf-8')
            L   = txt.split('\n')
            b   = [i for i, l in enumerate(L) if l.strip() == '---']
            if len(b) >= 2 and b[0] == 0:
                rec['fm'] = True
                fm = '\n'.join(L[b[0]+1:b[1]])
                def field(k):
                    m = re.search(r'^%s:\s*(.*)$' % k, fm, re.M)
                    return m.group(1).strip().strip('"\'') if m else ''
                rec['id']      = field('id')
                rec['version'] = field('version')
                rec['date']    = field('date')
                rec['gel']     = 'oui' if re.search(r'^gel_R36:', fm, re.M) else ''
                st             = field('statut')
                rec['statut']  = (st[:46] + '…') if len(st) > 47 else st
                mp = re.search(r'^prerequis_kb:\s*\[(.*?)\]', fm, re.M | re.S)
                rec['prereq'] = len([x for x in mp.group(1).split(',') if x.strip()]) if mp else 0
        except Exception:
            pass
    rows.append(rec)

# ---------------------------------------------------------------- classement
def cls(c):
    if c.startswith('LC-D3-'):                     return 'tete-D3'
    if c.startswith('LC-D-'):                      return 'tete-verdict'
    if c.startswith('LC-A-') or c.startswith('LC-E-'): return 'tete-annexe'
    if c.startswith('LC-WORK-CADRAGE-'):           return 'cadrage'
    if c.startswith('LC-WORK-AMENDEMENT-'):        return 'amendement-R7'
    if c.startswith('PROMPT-INCOGNITO-'):          return 'paquet-incognito'
    if c.startswith('LC-JOURNAL-'):                return 'journal'
    if c.startswith('LC-WORK-AUDIT-PAQUET-GEL'):   return 'MANIFESTE'
    if c.startswith('LC-CONST-'):                  return 'constitution'
    if c.startswith('LC-SCEAU-'):                  return 'cache-S2'
    if c in ('IDX.md','GLO.md','AUD.md') or re.match(r'^(IDX|GLO|AUD)(_v\d+)?\.md$', c): return 'INDEX-MANUEL'
    if c.startswith('LC-WORK-'):                   return 'work'
    if c.endswith('.py'):                          return 'sceau/instrument'
    if c.endswith('.txt'):                         return 'instrument-txt'
    if c.endswith('.pdf'):                         return 'source-pdf'
    return 'autre'

for r in rows:
    r['cls'] = cls(r['canon'])

# ---------------------------------------------------------------- PKG-SHA
hrows = [(r['canon'], r['sha']) for r in rows
         if not r['canon'].startswith('LC-WORK-AUDIT-PAQUET-GEL')
         and not r['canon'].endswith('.txt')]
payload = "\n".join(sorted(f"{c}  {h}" for c, h in hrows))
PKG = hashlib.sha256(payload.encode()).hexdigest()

# ---------------------------------------------------------------- ecriture
ORDER = ['constitution','MANIFESTE','INDEX-MANUEL','journal','instrument-txt','cache-S2',
         'sceau/instrument','amendement-R7','cadrage','paquet-incognito',
         'tete-verdict','tete-D3','tete-annexe','work','source-pdf','autre']

o = []
o.append('# LC-INDEX-DERIVE — OBJET DERIVE. NE PAS EDITER A LA MAIN.')
o.append('')
o.append('> **Regenere par `LC-WORK-GEN-INDEX.py` depuis LE MOUNT SEUL.**')
o.append('> **Un objet derive ne s\'atteste pas : il se recalcule** (LC-CONST-V1 §5.2).')
o.append('> **Aucun sceau. Aucun sha d\'index consigne. Ce fichier ne va PAS en KB.**')
o.append('> Toute valeur ci-dessous est **recalculable en une commande**. Si elle diverge')
o.append('> du mount, **c\'est ce fichier qui est perime**, jamais le mount (R-54).')
o.append('')
o.append(f'genere : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
o.append(f'PKG_SHA : {PKG}')
o.append(f'N_haches : {len(hrows)}  |  N_fichiers_mount : {len(rows)}')
o.append('')
o.append('---')
o.append('')
o.append('## Recapitulatif par classe')
o.append('')
o.append('    classe                  n')
for k in ORDER:
    n = sum(1 for r in rows if r['cls'] == k)
    if n:
        o.append(f'    {k:22} {n:3}')
o.append('')
o.append('---')
o.append('')

for k in ORDER:
    sub = [r for r in rows if r['cls'] == k]
    if not sub:
        continue
    o.append(f'## {k}  ({len(sub)})')
    o.append('')
    for r in sorted(sub, key=lambda x: x['canon']):
        o.append(f'    FICHIER  {r["canon"]}')
        o.append(f'    SHA256   {r["sha"]}')
        o.append(f'    OCTETS   {r["octets"]}')
        if r['id']:      o.append(f'    ID       {r["id"]}')
        if r['version']: o.append(f'    VERSION  {r["version"]}')
        if r['date']:    o.append(f'    DATE     {r["date"]}')
        if r['gel']:     o.append(f'    GEL_R36  {r["gel"]}')
        if r['prereq']:  o.append(f'    PREREQ   {r["prereq"]}')
        if r['statut']:  o.append(f'    STATUT   {r["statut"]}')
        o.append('')
    o.append('---')
    o.append('')

o.append('## §6.4 — SENTINELLE')
o.append('')
o.append('Deriver un index / recalculer un PKG-SHA / classer des fichiers :')
o.append('cela **NE SCELLE, NE REDUIT, NE COMPTE, NE DEMONTRE RIEN.**')
o.append('')
o.append('Le champ `STATUT` ci-dessus est **recopie du front-matter**. Il est donc')
o.append('**ECRIT A LA MAIN** et **PEUT MENTIR** — constat V89 (defaut #5(c) : deux')
o.append('paquets tires portaient encore « pret a passer »). **Il est indexe, il n\'est')
o.append('PAS autoritaire.** Seuls `SHA256` et `OCTETS` sont derives des octets.')
o.append('')
o.append('`{A4 ; A2* ; N}` **INCHANGE** ; O2 **non construit** ; beta **T-b non resolu** ;')
o.append('D1 non clos ; N non fixe ; A4 non reduit ; A2* non tranche ; R-53 **0/4**.')
o.append('**CCC n\'est ni demontree ni refutee.**')
o.append('')

open(OUT, 'w', encoding='utf-8').write('\n'.join(o))

# ---------------------------------------------------------------- console
print("############ INDEX DERIVE — GENERE ############")
print("sortie          ", OUT)
print("PKG_SHA_8       ", PKG[:8])
print("N_haches        ", len(hrows))
print("N_fichiers_mount", len(rows))
print("front-matter_ko ", sum(1 for r in rows if r['canon'].endswith('.md') and not r['fm']),
      "(.md sans front-matter parsable)")
print()
print("classe                  n")
for k in ORDER:
    n = sum(1 for r in rows if r['cls'] == k)
    if n: print(f"{k:22} {n:3}")
print()
print("---- DIAGNOSTIC DE PARITE — PAR MESURE, JAMAIS PAR LECTURE (§5.3) ----")
print("Les index manuels sont MESURES : on compte des ids, on n'ouvre rien.")
ids = sorted({r['id'] for r in rows if r['id']})
print("ids_derives_du_mount", len(ids))
for r in rows:
    if r['cls'] in ('INDEX-MANUEL', 'MANIFESTE'):
        try:
            t = open(os.path.join(D, [f for f in files if canon(f) == r['canon']][0]),
                     encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        cites   = sum(1 for i in ids if i in t)
        print(f"  {r['canon']:44} ids_cites {cites:3} / {len(ids):3}   manquants {len(ids)-cites:3}")
print()
print("*** LECTURE DU DIAGNOSTIC — A NE PAS SUR-INTERPRETER ***")
print("  Un id absent d'un index manuel = l'index NE LE CITE PAS.")
print("  Ce n'est PAS forcement une faute : IDX/GLO/AUD peuvent avoir des")
print("  PORTEES DIFFERENTES, que ce script NE CONNAIT PAS (il ne les lit pas).")
print("  ==> CE CHIFFRE EST UN SIGNAL, PAS UN VERDICT. b3 : le remplacement")
print("      d'IDX/GLO/AUD est un ACTE DE D, jamais une consequence de ce script.")
print()
print("############ §6.4 ############")
print("Deriver un index ne scelle, ne reduit, ne compte, ne demontre RIEN.")
print("{A4 ; A2* ; N} INCHANGE. O2 non construit. beta T-b non resolu. R-53 0/4.")
print("CCC n'est ni demontree ni refutee.")
