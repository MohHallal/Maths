import numpy as np

# Définition de la matrice de transition T
T = np.array([
    [0.51, 0.03, 0.10, 0.00, 0.31],
    [0.10, 0.21, 0.02, 0.10, 0.21],
    [0.03, 0.10, 0.21, 0.03, 0.03],
    [0.10, 0.21, 0.03, 0.10, 0.21],
    [0.03, 0.10, 0.21, 0.03, 0.03]
])
# Calcul de la matrice de transition après 8 saisons
T_8_seasons = np.linalg.matrix_power(T, 8)
probabilite_troisieme_a_premiere = T_8_seasons[0, 2]
# Affichage de la probabilité
print(f"Probabilité que le l'Olympique de Marseille classé troisiéme en ce moment remporte le championnat en 2030 : "
      f"{probabilite_troisieme_a_premiere}")

