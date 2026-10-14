# S-a2 : calcul independant (sympy). Premier ordre en eps.
import sympy as sp
t, eps = sp.symbols('tau epsilon', positive=True)
x, y, z = sp.symbols('x y z')
X = [t, x, y, z]
d = [1, 1, -2]
F = sp.Function('f')(t)

def geom(g):
    gi = sp.simplify(g.inv())
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) for e in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    # Riemann R^a_{bcd}
    R = sp.MutableDenseNDimArray.zeros(n, n, n, n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    R[a, b, c, dd] = sp.diff(Gam[a][b][dd], X[c]) - sp.diff(Gam[a][b][c], X[dd]) + sum(
                        Gam[a][c][e]*Gam[e][b][dd] - Gam[a][dd][e]*Gam[e][b][c] for e in range(n))
    Rl = sp.MutableDenseNDimArray.zeros(n, n, n, n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    Rl[a, b, c, dd] = sum(g[a, e]*R[e, b, c, dd] for e in range(n))
    Ric = sp.Matrix(n, n, lambda b, dd: sum(R[a, b, a, dd] for a in range(n)))
    Rs = sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n))
    return gi, Gam, Rl, Ric, Rs

def lin(e):
    e = sp.series(sp.expand(e), eps, 0, 2).removeO()
    return sp.simplify(e)

out = []
def P(*a):
    s = ' '.join(str(v) for v in a); print(s); out.append(s)

# ---------- metrique pont g ----------
g = sp.diag(-1, *[1 + eps*di*F for di in d])
gi, Gam, Rl, Ric, Rs = geom(g)
n = 4
C = {}
def Weyl(a, b, c, dd, g, Rl, Ric, Rs):
    return Rl[a, b, c, dd] - sp.Rational(1, 2)*(g[a, c]*Ric[b, dd] - g[a, dd]*Ric[b, c] - g[b, c]*Ric[a, dd] + g[b, dd]*Ric[a, c]) \
        + Rs/6*(g[a, c]*g[b, dd] - g[a, dd]*g[b, c])
P('== Q1 : Weyl de g au premier ordre (composantes non nulles, indices bas) ==')
nz = {}
for a in range(n):
    for b in range(a+1, n):
        for c in range(n):
            for dd in range(c+1, n):
                if (a, b) <= (c, dd):
                    v = lin(Weyl(a, b, c, dd, g, Rl, Ric, Rs))
                    if v != 0:
                        nz[(a, b, c, dd)] = v
                        P((a, b, c, dd), v)
P('E_ij = C_0i0j :', [lin(Weyl(0, i, 0, i, g, Rl, Ric, Rs)) for i in (1, 2, 3)])
# divergence de W = C/tau au premier ordre : nabla^mu W_{mu i 0 i}
# au 1er ordre Gamma ~ eps f', W ~ eps => termes Gamma*W d'ordre eps^2 ; la divergence se reduit a g^{00} d_tau W_{0i0i}
E11 = lin(Weyl(0, 1, 0, 1, g, Rl, Ric, Rs))
W11 = E11/t
P('divergence (1er ordre) nabla^mu W_{mu 1 0 1} = -d_tau(C_0101/tau) =', sp.simplify(-sp.diff(W11, t)))

# Imposer dW/dtau = A ln tau  (W = C_0101/tau) et resoudre pour f
A, W0, c0, c1 = sp.symbols('A W0 c0 c1')
# E11 = -eps*f''/2 (verifie ci-dessus) => W11 = -eps f''/(2 tau)
Wsol = W0 + sp.integrate(A*sp.log(t), t)          # W = W0 + A(tau ln tau - tau)
fpp = sp.solve(sp.Eq(E11.subs(sp.Derivative(F, (t, 2)), sp.Symbol('FPP'))/t, eps*Wsol), sp.Symbol('FPP'))[0]
P('f\'\' requis =', sp.expand(fpp))
fsol = sp.expand(sp.integrate(sp.integrate(fpp, t), t) + c0 + c1*t)
P('f(tau) =', fsol)
# verification directe
Wchk = sp.simplify(E11.subs(F, fsol).doit()/t/eps)
P('verif W(tau)/eps =', sp.expand(Wchk), ' ; dW/dtau =', sp.expand(sp.diff(Wchk, t)))
P('lecture alternative (si W := C sans division par Omega) : f\'\' ~ tau ln tau  => f ~ tau^3 ln tau')

P('== Q2 : regularite ==')
for k in range(0, 6):
    P(f'd^{k}f/dtau^{k} =', sp.expand(sp.diff(fsol, t, k)), ' limite tau->0+ :', sp.limit(sp.diff(fsol, t, k), t, 0, '+'))
P('W(0+) =', sp.limit(Wchk, t, 0, '+'), ' ; dW/dtau(0+) =', sp.limit(sp.diff(Wchk, t), t, 0, '+'))

P('== Q3 : metrique physique gcheck = tau^2 g ==')
gc = t**2*g
gci, Gc, Rlc, Ricc, Rsc = geom(gc)
Gein = sp.Matrix(n, n, lambda a, b: Ricc[a, b] - Rsc*gc[a, b]/2)
# repere orthonorme : e_0 = (1/tau) d_tau ; e_i = 1/(tau sqrt(1+eps d f)) d_i
scale = [1/t] + [1/(t*sp.sqrt(1 + eps*di*F)) for di in d]
Gh = sp.Matrix(n, n, lambda a, b: lin(Gein[a, b]*scale[a]*scale[b]))
P('G_hat (general f) :')
for a in range(n):
    for b in range(a, n):
        if Gh[a, b] != 0:
            P(' ', (a, b), sp.simplify(Gh[a, b]))
T = sp.symbols('T', positive=True)        # temps propre : dT = tau dtau => T = tau^2/2
sub = {t: sp.sqrt(2*T)}
G00_0 = sp.simplify(Gh[0, 0].subs(eps, 0))
P('ordre 0 : G_00 =', G00_0, '=', sp.simplify(G00_0.subs(sub)), ' ; G_11 =', sp.simplify(Gh[1, 1].subs(eps, 0)), '=', sp.simplify(Gh[1, 1].subs(eps, 0).subs(sub)))
P('  w = p/rho =', sp.simplify(Gh[1, 1].subs(eps, 0)/G00_0), ' ; facteur d\'echelle a(T)=tau=sqrt(2T) (radiation)')
G1 = {}
for i in (1, 2, 3):
    G1[i] = sp.simplify(sp.diff(Gh[i, i], eps).subs(eps, 0))
P('ordre eps (general) : dG_ii/eps =', [G1[i] for i in (1, 2, 3)], ' ; trace =', sp.simplify(sum(G1.values())))
P('  dG_00/eps =', sp.simplify(sp.diff(Gh[0, 0], eps).subs(eps, 0)), ' ; dG_0i =', [Gh[0, i] for i in (1, 2, 3)])
Sfac = sp.simplify(G1[1].subs(F, fsol).doit())
P('pour f(tau) de Q1 : dG_11/eps =', sp.expand(Sfac))
SfacT = sp.expand(sp.expand_log(sp.simplify(Sfac.subs(sub)), force=True))
P('  en temps propre T : dG_11/eps =', SfacT)
for name, ff in [('c1*tau', c1*t), ('tau^3 (W0)', t**3), ('tau^4 ln tau (A)', t**4*sp.log(t)), ('c0', c0)]:
    v = sp.simplify(G1[1].subs(F, ff).doit())
    P(f'   contribution {name}:', sp.expand(v), ' -> T:', sp.expand(sp.expand_log(sp.simplify(v.subs(sub)), force=True)),
      ' ; rapport / rho0 :', sp.simplify(v.subs(sub)/G00_0.subs(sub)))
# Weyl physique en repere orthonorme
Cc = lin(Weyl(0, 1, 0, 1, gc, Rlc, Ricc, Rsc))*scale[0]**2*(1/t**2)
Cc = sp.simplify(Cc.subs(F, fsol).doit()/eps)
P('Weyl physique E_hat_11/eps =', sp.expand(Cc), ' -> T:', sp.expand(sp.expand_log(sp.simplify(Cc.subs(sub)), force=True)))

open('/home/claude/audit_sa2/sa2_out.txt', 'w').write('\n'.join(out) + '\n')
