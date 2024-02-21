import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

# Function to calculate multiplicity for given NA, NB, qA
def calculate_multiplicity(NA, NB, qA):
    qB = NA + NB - qA
    omega_A = comb(qA + NA - 1, qA)
    omega_B = comb(qB + NB - 1, qB)
    omega_total = omega_A * omega_B
    return omega_total

# Get user input
NA_values = [int(input("Enter NA for set {}: ".format(i + 1))) for i in range(4)]
NB_values = [int(input("Enter NB for set {}: ".format(i + 1))) for i in range(4)]
qA_values = [int(input("Enter qA for set {}: ".format(i + 1))) for i in range(4)]

# Plot multiplicity for each set of inputs
plt.figure(figsize=(12, 8))

for i in range(4):
    q_values = np.arange(NA_values[i] + NB_values[i] + 1)
    omega_values = [calculate_multiplicity(NA_values[i], NB_values[i], qA) for qA in q_values]

    plt.subplot(2, 2, i + 1)
    plt.plot(q_values, omega_values, '-o')
    plt.xlabel('qA')
    plt.ylabel('W')
    plt.title('Multiplicity for NA={}, NB={}, qA={}'.format(NA_values[i], NB_values[i], qA_values[i]))

plt.tight_layout()
plt.show()

