import numpy as np

A = np.array([[2,1,1],
              [3,2,0],
              [1,1,2]], dtype=float)
b = np.array([8,11,7], dtype=float)

# Vérifier que le système est solvable
detA = np.linalg.det(A)
print("det(A) =", detA)

# Résoudre A X = b
X = np.linalg.solve(A, b)
x_1, x_2, x_3 = X
print(f"Stylo x_1 = {x_1:.2f} XOF")
print(f"Cahier x_2 = {x_2:.2f} XOF")
print(f"Règle x_3 = {x_3:.2f} XOF")

# Contrôle : ||Ax - b||
res = np.linalg.norm(A @ X - b)
print("Erreur (norme du résidu) =", res)
