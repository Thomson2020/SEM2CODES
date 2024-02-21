import numpy as np
import matplotlib.pyplot as plt

# Example data (replace with your actual data)
temperature = np.array([318, 313, 308, 303])  # Temperature in degrees Celsius
resistance = np.array([0.585, 0.544, 0.515, 0.464])  # Resistance in ohms

# Plot resistance vs temperature
plt.figure()
plt.plot(temperature, resistance, '*-', label='Resistance vs Temperature')
plt.xlabel('Temperature (Celsius)')  # Corrected the x-axis label
plt.ylabel('Resistance (Ohms)')
plt.title('Resistance vs Temperature')
plt.grid(True)
plt.legend()

# Calculate the slope (change in resistance / change in temperature)
# We’ll use numpy’s polyfit function to fit a linear regression line
slope, intercept = np.polyfit(temperature, resistance, 1)

# Print the slope
print(f'Slope (R/T): {slope:.4f} Ohms/°C')  # Added formatting to print the slope with four decimal places

# Show plot
plt.show()
