import math  # pour les calculs reels
import cmath  # pour les calculs complexes

# Demander a l'utilisateur de saisir les coefficients
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Calculer le discriminant
delta = b**2 - 4*a*c

# Vérifier si le discriminant est négatif
if delta < 0:
    print("L'equation admet deux solutions complexe.")
    # Calculer les deux solutions complexes
    x1_complex = (-b + cmath.sqrt(delta)) / (2*a)
    x2_complex = (-b - cmath.sqrt(delta)) / (2*a)
    # Afficher les solutions complexes
    print(f"Les solutions de l'equations \n {a}x^2 + {b}x + {c} = 0 sont :")
    print(f"x1 = {x1_complex}")
    print(f"x2 = {x2_complex}")
else:
    print("L'equation admet deux solutions réelles.")
    # Calculer les deux solutions
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    # Afficher les solutions
    print(f"Les solutions de l'equations \n {a}x^2 + {b}x + {c} = 0 sont :")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    