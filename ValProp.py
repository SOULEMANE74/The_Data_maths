import sympy as sp

# Déclaration du symbole
a = sp.symbols('a')

# Définition de la matrice
M = sp.Matrix([
    [1, a, 0],
    [a, 2, a],
    [0, a, 3]
])

# Calcul des valeurs propres (sous forme de liste)
valeurs_propres = list(M.eigenvals().keys())

# Affichage clair
for i, val in enumerate(valeurs_propres, start=1):
    print(f"lambda{i} =", sp.simplify(val))

