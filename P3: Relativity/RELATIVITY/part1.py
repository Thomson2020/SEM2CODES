import numpy as np
import matplotlib.pyplot as plt

def lorentz_transform(x, t, v):
    gamma = 1 / np.sqrt(1 - (v*2 / c*2))
    x_transformed = gamma * (x - v * t)
    t_transformed = gamma * (t - v * x / c**2)
    return x_transformed, t_transformed

# Constants
c = 299792458  # Speed of light in meters per second

# Input: Relative velocity between K and K'
v = float(input("Enter the relative velocity between K and K' (as a fraction of the speed of light): "))

# Input: Velocity of the third particle in the K frame
u = float(input("Enter the velocity of the third particle in the K frame (as a fraction of the speed of light): "))

# World lines of the third particle in K frame
x_K = np.linspace(0, 10, 100)  # Example trajectory for the third particle in K frame
t_K = np.linspace(0, 10, 100)  # Time coordinate for the third particle in K frame

# Transform to K' frame
x_Kprime, t_Kprime = lorentz_transform(x_K, t_K, v)

# A. Plot of world lines in K frame
plt.figure(figsize=(10, 6))
plt.plot(x_K, t_K, label='Particle in K frame')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('World Line of Particle in K Frame')
plt.legend()
plt.grid(True)
plt.show()

# B. Plot of world lines in K' frame (Part B)
plt.figure(figsize=(10, 6))
plt.plot(x_Kprime, t_Kprime, label='Particle in K\' frame')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('World Line of Particle in K\' Frame')
plt.legend()
plt.grid(True)
plt.show()
