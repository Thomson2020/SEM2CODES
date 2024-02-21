import matplotlib.pyplot as plt
import numpy as np

# Define parameters
a = 1.0  # Interatomic distance
C = 1.0  # Spring constant
M = 1.0  # Mass of the atom

# Generate values for K
K_values = np.linspace(-np.pi / a, np.pi / a, 100)

# Calculate angular frequency (omega) using the provided formula
omega_values = np.sqrt(4 * C / M * (np.sin(K_values * a / 2))**2)

# Plot omega vs K
plt.plot(K_values, omega_values, label='ω vs K')
plt.xlabel('Wave Number (K)')
plt.ylabel('Angular Frequency (ω)')
plt.title('Dispersion Relation')
plt.legend()
plt.grid()
plt.show()

