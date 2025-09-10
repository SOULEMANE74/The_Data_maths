import sympy as sp

# Définition de la variable
x = sp.symbols('x')

# Limite 1 : sin(x)/x quand x -> 0
L1 = sp.limit(sp.sin(x)/x, x, 0)

# Limite 2 : sin(1/x) quand x -> 0
L2 = sp.limit(sp.sin(1/x), x, 0)

print("L1 =", L1)
print("L2 =", L2)

