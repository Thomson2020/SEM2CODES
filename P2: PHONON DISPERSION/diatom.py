import numpy as np
import matplotlib.pyplot as plt

def dispersion_relation_diatomic(k, spring_constant_1, spring_constant_2, lattice_constant, mass):
    omega_optical = np.sqrt((spring_constant_1 + spring_constant_2) / mass +
                            np.sqrt(((spring_constant_1 + spring_constant_2) / mass)**2 -
                                    4 * (spring_constant_1 * spring_constant_2) / (mass**2) *
                                    np.sin(k * lattice_constant / 2)**2))
    omega_acoustical = np.sqrt((spring_constant_1 + spring_constant_2) / mass -
                               np.sqrt(((spring_constant_1 + spring_constant_2) / mass)**2 -
                                       4 * (spring_constant_1 * spring_constant_2) / (mass**2) *
                                       np.sin(k * lattice_constant / 2)**2))
    return omega_optical, omega_acoustical

# Constants for diatomic lattice
num_atoms = 100
spring_constant_1 = 1.0
spring_constant_2 = 2.0
lattice_constant = 1.0
mass = 1.0

# Calculate dispersion relation for diatomic lattice
k_values = np.linspace(-np.pi / lattice_constant, np.pi / lattice_constant, 1000)
omega_optical, omega_acoustical = dispersion_relation_diatomic(k_values, spring_constant_1, spring_constant_2, lattice_constant, mass)

# Plotting the dispersion relation for diatomic lattice
plt.figure(figsize=(8, 6))
plt.plot(k_values, omega_optical, label='Optical Branch')
plt.plot(k_values, omega_acoustical, label='Acoustical Branch')
plt.xlabel('Wave Vector (k)')
plt.ylabel('Angular Frequency (ω)')
plt.title('Dispersion Relation of Diatomic Lattice')
plt.axvline(x=0, color='r', linestyle='--', label='k=0')
plt.axvline(x=np.pi / lattice_constant, color='g', linestyle='--', label='k=±π/a')
plt.axvline(x=-np.pi / lattice_constant, color='g', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
