import numpy as np
from sympy import Matrix

#Définir la matrice M
M = Matrix([
    [1, 0, -1],
    [-2, 3, 4],
    [0, 1, 1]
])

# Déterminant
det_M = M.det()

# Comatrice
comatrice_M = M.cofactor_matrix()

# Inverse
inverse_M = M.inv()

# Affichage des resultats
print("Déterminant de M :", det_M)
print("\nComatrice de M :")
print(comatrice_M)
print("\nInverse de M :")
print(inverse_M)
