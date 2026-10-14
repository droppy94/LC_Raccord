# M-a2, questions 4-6 : integrales angulaires exactes du tenseur de polarisation lineaire L(n).
# Q_tf (partie diagonale, apres sommation k,-k) = - sum_k L[J+(k)] ; sur une couche |k| : - k^2 dk/(2pi)^3 * int dOmega L
import sympy as sp, itertools
nx, ny, nz = sp.symbols('nx ny nz', real=True)
n = sp.Matrix([nx, ny, nz]); I3 = sp.eye(3)
Pp = I3 - n*n.T
def sph(expr):
    """integrale exacte sur S^2 d'un polynome en nx,ny,nz"""
    expr = sp.expand(expr); tot = 0
    for mon, c in sp.Poly(expr, nx, ny, nz).terms():
        a, b, cc = mon
        if a % 2 or b % 2 or cc % 2: continue
        tot += c*2*sp.gamma(sp.Rational(a+1,2))*sp.gamma(sp.Rational(b+1,2))*sp.gamma(sp.Rational(cc+1,2))/sp.gamma(sp.Rational(a+b+cc+3,2))
    return sp.simplify(tot)
def sphM(M): return M.applyfunc(sph)
def cross(u, v): return u.cross(v)
def Lpol(eps):
    """tenseur de polarisation lineaire : Re(eps eps^dag) - 1/2 |eps|^2 P_perp (eps transverse)"""
    M = eps*eps.conjugate().T
    Mr = M.applyfunc(lambda z: sp.re(sp.expand(z)))
    Mr = (Mr + Mr.T)/2
    return Mr - Mr.trace()/2*Pp
def STF(M): M = (M + M.T)/2; return M - M.trace()/3*I3
def Re(M): return M.applyfunc(lambda z: sp.re(sp.expand(z)))
def cvec(name):
    r = sp.symbols(name+'x_r '+name+'y_r '+name+'z_r', real=True)
    i = sp.symbols(name+'x_i '+name+'y_i '+name+'z_i', real=True)
    return sp.Matrix(r) + sp.I*sp.Matrix(i)
# amplitudes J+ (k=1) : dipole electrique -i P_perp p ; dipole magnetique i n x m ; quadrupole electrique 1/2 P_perp Q n
E1 = lambda p: -sp.I*Pp*p
M1 = lambda m: sp.I*cross(n, m)
E2 = lambda Q: sp.Rational(1,2)*Pp*(Q*n)
xh, yh, zh = I3[:,0], I3[:,1], I3[:,2]
c = sp.Rational(8,5)*sp.pi
def show(label, M, ref=None):
    M = sp.simplify(M)
    print(label, M.tolist())
    if ref is not None: print("   ecart a la reference :", sp.simplify(M - ref).tolist())

print("=== Lois generales (p, m complexes generiques) ===")
p, m = cvec('p'), cvec('m')
show("int L[E1(p)]  - (8pi/5) STF Re(p p^dag) =", sphM(Lpol(E1(p))) - c*STF(Re(p*p.conjugate().T)))
show("int L[M1(m)]  + (8pi/5) STF Re(m m^dag) =", sphM(Lpol(M1(m))) + c*STF(Re(m*m.conjugate().T)))
cross_EM = sphM(Lpol(E1(p) + M1(m)) - Lpol(E1(p)) - Lpol(M1(m)))
show("terme croise E1 x M1 (int) =", cross_EM)

print("\n=== Q5 : cas demandes ; on donne int dOmega L (Q_tf ∝ - int L) ===")
show("M1 lineaire m=z :", sphM(Lpol(M1(zh))), -c*STF(zh*zh.T))
show("E1 lineaire p=z :", sphM(Lpol(E1(zh))), c*STF(zh*zh.T))
show("M1 tournant m=x-iy :", sphM(Lpol(M1(xh - sp.I*yh))), c*STF(zh*zh.T))
for s in [1, -1]:
    eps = E1(zh) + M1(s*sp.I*zh)
    Lf = sp.simplify(Lpol(eps))
    print(f"chiral p=z, m={s}i z : L(n) point par point =", Lf.applyfunc(lambda z: sp.simplify(z.subs(nz**2, 1-nx**2-ny**2))).tolist())
eps = E1(zh) + M1(zh)
show("p=m=z en phase (helicite nulle) : int L =", sphM(Lpol(eps)))
print("   L(n) en phase non nul localement, ex. n=x :", Lpol(eps).subs({nx:1,ny:0,nz:0}).tolist())
# helicite (V) locale pour en phase / chiral
def Vloc(eps, pt):
    e = eps.subs(pt); M = e*e.conjugate().T
    return sp.simplify(sp.I*(M - M.T))
print("   V local en phase, n=x :", Vloc(E1(zh)+M1(zh), {nx:1,ny:0,nz:0}).tolist())
# ensemble isotrope d'orientations : moyenne de STF(m m) sur la sphere des orientations
u = sp.Matrix(sp.symbols('ux uy uz', real=True))
print("ensemble isotrope : <STF(u u)>_orient =", (STF(u*u.T)).applyfunc(lambda z: sph(z.subs({u[0]:nx,u[1]:ny,u[2]:nz}))/(4*sp.pi)).tolist(), " -> int L = 0")

print("\n=== Q4 : motifs E et B purs ; rang de l'application ===")
ts = sp.symbols('t1:6', real=True)
T = sp.Matrix([[ts[0], ts[1], ts[2]],[ts[1], ts[3], ts[4]],[ts[2], ts[4], -ts[0]-ts[3]]])
LE = STF_perp = (Pp*T*Pp) - (Pp*T*Pp).trace()/2*Pp   # motif E, l=2
Nx = sp.Matrix([[0,-nz,ny],[nz,0,-nx],[-ny,nx,0]])  # n x (.)
LB = (Nx*LE + (Nx*LE).T)/2                           # motif B, l=2 (polarisation tournee de 45 deg)
intE = sphM(LE); intB = sphM(LB)
show("int L_E[T] =", intE); print("   = (8pi/5)*T ?", sp.simplify(intE - c*T) == sp.zeros(3))
show("int L_B[T] =", intB)
J = sp.Matrix([[intE[i,j] for (i,j) in [(0,0),(0,1),(0,2),(1,1),(1,2)]]]).jacobian(ts)
print("   rang de T -> int L_E[T] :", J.rank(), "(nombre de conditions reelles pour annuler Q_tf)")
# l = 3 et l = 4 (E) : integrale nulle
T3 = sp.MutableDenseNDimArray.zeros(3,3,3)
vals = sp.symbols('w1:4', real=True)
# un STF rang 3 simple : partie STF de z z x
def stf_from_vec(vs):
    import itertools as it
    k = len(vs); A = sp.MutableDenseNDimArray.zeros(*([3]*k))
    for perm in it.permutations(range(k)):
        for idx in it.product(range(3), repeat=k):
            A[idx] += sp.prod([vs[perm[q]][idx[q]] for q in range(k)])
    return A
def trace_free(A, k):
    # supprime les traces par projection numerique : polynome harmonique via laplacien
    return A
# construction par polynome harmonique f_l(n) puis L = STF_perp(hessienne tangente)
r = sp.symbols('r', positive=True)
X = sp.Matrix([nx, ny, nz])
for l, f in [(3, nx*ny*nz), (4, nx*ny*(6*nz**2 - nx**2 - ny**2))]:
    assert sp.simplify(sum(sp.diff(f, v, 2) for v in [nx,ny,nz])) == 0
    Hs = sp.hessian(f, (nx,ny,nz))
    Lf = Pp*Hs*Pp; Lf = Lf - Lf.trace()/2*Pp
    show(f"motif E l={l} : int L =", sphM(Lf))
    LBl = (Nx*Lf + (Nx*Lf).T)/2
    show(f"motif B l={l} : int L =", sphM(LBl))

print("\n=== Q5 : combinaison generique p, m, Q (valeurs rationnelles) ===")
pg = sp.Matrix([1, sp.Rational(1,2)*sp.I, -sp.Rational(1,3)])
mg = sp.Matrix([sp.Rational(1,4), -1 + sp.I, sp.Rational(2,3)*sp.I])
Qg = sp.Matrix([[1, sp.Rational(1,2), 0],[sp.Rational(1,2), -sp.Rational(1,3), sp.I/2],[0, sp.I/2, -sp.Rational(2,3)]])
tot = sphM(Lpol(E1(pg) + M1(mg) + E2(Qg)))
show("int L (p+m+Q) =", tot)
show("   croise M1 x E2 =", sphM(Lpol(M1(mg)+E2(Qg)) - Lpol(M1(mg)) - Lpol(E2(Qg))))
show("   croise E1 x E2 =", sphM(Lpol(E1(pg)+E2(Qg)) - Lpol(E1(pg)) - Lpol(E2(Qg))))
show("   E2 seul =", sphM(Lpol(E2(Qg))))

print("\n=== Q6 : <eps_B eps_B - eps_E eps_E> pour M1 lineaire (moyenne 1/4pi int dOmega) ===")
mr = sp.Matrix(sp.symbols('mx my mz', real=True))
eE = cross(n, mr); eB = cross(n, eE)
avg = sphM(eB*eB.T - eE*eE.T)/(4*sp.pi)
show("<eB eB - eE eE> - (4/5)(mm - m^2/3) =", avg - sp.Rational(4,5)*STF(mr*mr.T))
Lm = sphM(Lpol(eE))/(4*sp.pi)
show("<eB eB - eE eE> + 2 <L> =", avg + 2*Lm)
show("<L> M1 (moyenne) + (2/5) STF(mm) =", Lm + sp.Rational(2,5)*STF(mr*mr.T))
