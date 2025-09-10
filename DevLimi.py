import sympy as sp

# Variables
x, n = sp.symbols('x n')

# 1) Développement limité de tan(x) en 0 à l'ordre 10
taylor_tan = sp.series(sp.tan(x), x, 0, 11)
print(f"D.L. de tan(x) : {taylor_tan}")

# 2) Développement asymptotique de (1 + 1/n)^n quand 
# n -> imfinie à l'ordre 5
expr = (1 + 1/n)**n
asympt_exp = sp.series(expr, n, sp.oo, 6)
print(f"D.A. de (1+1/n)^n : {asympt_exp}")



