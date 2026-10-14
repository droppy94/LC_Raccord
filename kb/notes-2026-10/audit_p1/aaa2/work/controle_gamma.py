# controle_gamma.py : verification de Int_0^inf k^{3-N} e^{-(a+2i eta)k} dk = Gamma(4-N) (a+2i eta)^{N-4}
# (a > 0 fixe, quadrature amortie ; la limite a -> 0+ est ensuite analytique, branche principale)
import mpmath as mpm
mpm.mp.dps = 20
ee = mpm.mpf('-0.3')
for aa in (mpm.mpf('0.2'), mpm.mpf('0.05')):
    for Nv in (mpm.mpf('2.5'), mpm.mpf(3), mpm.mpf('3.5')):
        p = aa + 2j*ee
        num = mpm.quad(lambda kk: kk**(3 - Nv)*mpm.exp(-p*kk), mpm.linspace(0, 60/aa, 400))
        theo = mpm.gamma(4 - Nv)*p**(Nv - 4)
        print("a =", aa, " N =", Nv, " quad =", mpm.nstr(num, 10), " Gamma(4-N)(a+2i eta)^{N-4} =", mpm.nstr(theo, 10),
              " ecart =", mpm.nstr(abs(num - theo), 3))
print("limite a -> 0+, N = 3, eta = -0.3 : 1/(2 i eta) =", mpm.nstr(1/(2j*ee), 10), " = -i/(2 eta) : module 1/(2|eta|)")
print("N = 3, F reel : Re[1/(2 i eta)] = 0 ; le 1/eta n'apparait que via une phase (Im F != 0), cf. e^{i phi} du script")
