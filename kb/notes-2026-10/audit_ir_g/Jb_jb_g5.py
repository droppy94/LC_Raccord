"""jb_g5.py -- contre-exemples a G5 et ondes progressives (Poynting moyen non nul), via jb_indep.analyse."""
import sympy as sp
from jb_indep import analyse
k=1
# onde progressive le long de x, A = Re[(ey + i h ez) e^{i(kx - ks)}] (s = -tau : phase k x + k tau)
# cos(kx-ks) = cos kx cos ks + sin kx sin ks -> secteur cos : u = cos ks (u0=1,c=0) ; secteur sin : u = sin ks (u0=0,c=k)
# sin(kx-ks) = sin kx cos ks - cos kx sin ks -> secteur sin : u0=1 ; secteur cos : c=-k
def travel(ay,az):
    m=[]
    # composante y : ay cos(kx-ks)
    m.append(((1,0,0),(0,ay,0),1,0,(0,ay,0),0,k))
    # composante z : az sin(kx-ks)
    m.append(((1,0,0),(0,0,az),0,-k,(0,0,az),1,0))
    return m
print("##### onde progressive POLARISEE LINEAIREMENT (E = B en module)")
Q,res,ok=analyse('T6_progressive_lineaire',travel(1,0))
print("##### onde progressive POLARISEE CIRCULAIREMENT (E = B, coherente, polarisee)")
Q,res,ok=analyse('T7_progressive_circulaire',travel(1,1))
print("##### onde progressive elliptique (ay=2, az=1)")
Q,res,ok=analyse('T8_progressive_elliptique',travel(2,1))
print("##### onde stationnaire helicoidale a Q = 0 (cas T4 avec a2=b1=1, a1=b2=1)")
Q,res,ok=analyse('T9_stationnaire_helicoidale_Q0',[((1,0,0),(0,1,0),1,1,(0,0,1),1,1)])
print("##### faisceau non polarise anisotrope : deux polarisations lineaires incoherentes (k differents, meme direction), E = B")
Q,res,ok=analyse('T10_faisceau_non_polarise',travel(1,0)[:1]+[((2,0,0),(0,0,1),1,0,(0,0,1),0,2)])
print("\nEXIT 0")
