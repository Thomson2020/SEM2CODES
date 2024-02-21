import numpy as np
import matplotlib.pyplot as plt

# Define parameters
num_atoms = 3
dt = 0.01
num_steps = 200000  # Total time steps
eps = 0.0103
sig = 3.4
m = 39.948  # Mass of Argon

# Define initial conditions
positions = np.array([[0], [4], [10]])
velocities = np.zeros_like(positions)
accelerations = np.zeros_like(positions)

# Store positions and velocities for plotting
all_positions = np.zeros((num_steps, num_atoms, 2))
all_velocities = np.zeros((num_steps, num_atoms, 2))
all_positions[0] = positions.copy()  # Store initial positions
all_velocities[0] = velocities.copy()  # Store initial velocities

def pairwise_distances(positions):
    num_particles = len(positions)
    distance_matrix = np.linalg.norm(positions[:, None] - positions[None], axis=2)
    return distance_matrix

def potential(epsilon, sigma, distance):
    E_attractive = -4 * epsilon * (sigma / distance)**6
    E_repulsive = 4 * epsilon * (sigma / distance)**12
    E = E_attractive + E_repulsive
    return E

def force(distance):
    dE_dr = -4 * eps * (6 * sig**6 / distance**7 - 12 * sig**12 / distance**13)
    f = -dE_dr
    return f

def acceleration(f, m):
    acc = f / m
    return acc

# Main simulation loop
for step in range(1, num_steps):

    # Calculate pairwise distances
    distances = pairwise_distances(positions)

    # Calculate forces for each particle pair
    forces = np.zeros_like(positions, dtype=float)  # Ensure forces are floating-point
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            distance = distances[i, j]
            calculated_force = force(distance)
            forces[i] += calculated_force  # Assign force directly without conversion
            forces[j] -= calculated_force  # Apply equal and opposite forces

    # Update positions and velocities using velocity-Verlet
    accelerations = acceleration(forces, m)
    positions = positions.astype(float)
    velocities = velocities.astype(float)
    positions += velocities * dt + 0.5 * accelerations * dt**2
    velocities += 0.5 * (accelerations + acceleration(forces, m)) * dt

    # Store positions and velocities for plotting
    all_positions[step] = positions.copy()
    all_velocities[step] = velocities.copy()

# Plot positions vs time
for i in range(num_atoms):
    plt.scatter(np.arange(num_steps) * dt, all_positions[:, i, 0], label=f"Atom {i+1} (Position X)", s=2)  # Adjust 's' for marker size
plt.xlabel("Time (dt)")
plt.ylabel("Position")
plt.title("Atom positions vs time")
plt.legend()
plt.grid(True)
plt.show()

# Plot velocities vs time
for i in range(num_atoms):
    plt.scatter(np.arange(num_steps) * dt, all_velocities[:, i, 0], label=f"Atom {i+1} (Velocity X)", s=2)  # Adjust 's' for marker size
plt.xlabel("Time (dt)")
plt.ylabel("Velocity")
plt.title("Atom velocities vs time")
plt.legend()
plt.grid(True)
plt.show()

