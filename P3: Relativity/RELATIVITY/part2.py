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

# Input: Simultaneous events in K frame
x1_K = float(input("Enter the x-coordinate of Event 1 in K frame: "))
x2_K = float(input("Enter the x-coordinate of Event 2 in K frame: "))
t_K = float(input("Enter the time at which the events are simultaneous in K frame: "))

# Transform events to K' frame
x1_Kprime, t1_Kprime = lorentz_transform(x1_K, t_K, v)
x2_Kprime, t2_Kprime = lorentz_transform(x2_K, t_K, v)

# Input: Simultaneous event in K' frame
x1_Kprime_2 = float(input("Enter the x-coordinate of Event 1 in K' frame: "))
x2_Kprime_2 = float(input("Enter the x-coordinate of Event 2 in K' frame: "))
t_Kprime_2 = float(input("Enter the time at which the events are simultaneous in K' frame: "))

# Transform events back to K frame
x1_K_2, t1_K_2 = lorentz_transform(x1_Kprime_2, t_Kprime_2, -v)
x2_K_2, t2_K_2 = lorentz_transform(x2_Kprime_2, t_Kprime_2, -v)

# Plot simultaneous events in K and K' frames as world lines
plt.figure(figsize=(16, 12))

# Simultaneous events in K frame
plt.subplot(2, 2, 1)
plt.plot([x1_K, x2_K], [t_K, t_K], 'r-', label='Simultaneous events in K frame')
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('Simultaneous Events in K Frame')
plt.legend()
plt.grid(True)

# Simultaneous events in K' frame as seen in K frame
plt.subplot(2, 2, 2)
plt.plot([x1_Kprime, x2_Kprime], [t1_Kprime, t2_Kprime], 'b-', label="Simultaneous events in K' frame")
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('How they appear in K\' Frame ')
plt.legend()
plt.grid(True)

# Simultaneous events in K' frame
plt.subplot(2, 2, 3)
plt.plot([x1_Kprime_2, x2_Kprime_2], [t_Kprime_2, t_Kprime_2], 'b-', label="Simultaneous events in K' frame")
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('Simultaneous Events in K\' Frame')
plt.legend()
plt.grid(True)

# Simultaneous events in K frame as seen in K' frame
plt.subplot(2, 2, 4)
plt.plot([x1_K_2, x2_K_2], [t1_K_2, t2_K_2], 'r-', label="Simultaneous events in K frame")
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.xlabel('Space (x)')
plt.ylabel('Time (t)')
plt.title('How they appear in K Frame')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
