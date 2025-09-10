import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Paramètres du pendule
g = 9.81       # accélération gravitationnelle (m/s²)
L = 1.0        # longueur du pendule (m)
theta0 = np.pi/4  # angle initial (rad)
omega0 = 0.0      # vitesse angulaire initiale (rad/s)

# Fonction représentant les équations différentielles du pendule
def pendule(t, y):
    theta, omega = y
    dydt = [omega, - (g/L) * np.sin(theta)]
    return dydt

# Intervalle de temps
t_span = (0, 10)  # de 0 à 10 secondes
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Résolution numérique
sol = solve_ivp(pendule, t_span, [theta0, omega0], t_eval=t_eval)

# Affichage de l’angle en fonction du temps
plt.figure(figsize=(8,5))
plt.plot(sol.t, sol.y[0], label='Angle θ(t)')
plt.xlabel('Temps (s)')
plt.ylabel('Angle (rad)')
plt.title('Simulation d’un pendule simple')
plt.grid(True)
plt.legend()
plt.show()
