# VA-1 : forme exacte de T_ij (mode plan, repere conforme plat) ; complement de va1_sympy_algebra.py
exec(open('va1_sympy_algebra.py').read().split('# ---- Lemme 2')[0].split('print("T_etaeta')[0])
sgn = -1
for i in range(3):
    for j in range(i,3):
        Tij = T(i+1,j+1)
        for s in (+1,-1):
            cand = s*sp.Rational(1,2)*(kv[i]*sp.expand((ud*alpha[j]*u)[0]) + kv[j]*sp.expand((ud*alpha[i]*u)[0]))
            if sp.simplify(sp.expand(Tij-cand))==0:
                print(f"T_{i+1}{j+1} = {s:+d}*(1/2)(k_i u^dag alpha_j u + k_j u^dag alpha_i u)")
