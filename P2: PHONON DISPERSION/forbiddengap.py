import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the angular frequencies
def calculate_angular_frequencies(a, C, M1, M2, K_values):
    omega1_values_sqrd = C/(M1*M2)*(M1 + M2 + np.sqrt(M1**2 + M2**2 + 2*M1*M2*np.cos(K_values*a)))
    omega2_values_sqrd = C/(M1*M2)*(M1 + M2 - np.sqrt(M1**2 + M2**2 + 2*M1*M2*np.cos(K_values*a)))
    omega1_values = np.sqrt(omega1_values_sqrd)
    omega2_values = np.sqrt(omega2_values_sqrd)
    return omega1_values, omega2_values

# Define parameters
a = 1  # Interatomic distance
C = 1  # Spring constant
M2 = 1.0  # Mass of the lighter atom (initial value)

# Vary the mass ratio by changing M1 (the mass of the heavier atom)
mass_ratios = np.linspace(0.1, 10, 100)  # Vary M1/M2

forbidden_gaps = []  # List to store forbidden gaps

# Iterate through different mass ratios
for mass_ratio in mass_ratios:
    M1 = M2 * mass_ratio  # Update M1 based on the mass ratio
    K_values = np.linspace(-np.pi / a, np.pi / a, 100)
    omega1_values, omega2_values = calculate_angular_frequencies(a, C, M1, M2, K_values)
    forbidden_gap = min(omega1_values) - max(omega2_values)
    forbidden_gaps.append(forbidden_gap)
    #print(f'Mass Ratio: {mass_ratio:.2f}, Forbidden Gap between Acoustic and Optical branch: {forbidden_gap:.4f}')

# Tabulate the final output
table = {'Mass Ratio': mass_ratios, 'Forbidden Gap': forbidden_gaps}
print("\nFinal Output Table:")
print("{:<15} {:<20}".format('Mass Ratio', 'Forbidden Gap'))
for i in range(len(mass_ratios)):
    print("{:<15.2f} {:<20.4f}".format(mass_ratios[i], forbidden_gaps[i]))

# Plot forbidden gap vs mass ratio
plt.plot(mass_ratios, forbidden_gaps)
plt.xlabel('Mass Ratio $M_1/M_2$')
plt.ylabel('Forbidden Gap')
plt.title('Forbidden Gap vs Mass Ratio')
plt.grid()
plt.show()

