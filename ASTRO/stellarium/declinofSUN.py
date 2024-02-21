import matplotlib.pyplot as plt
# Data #FOR SUN
months = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
declination_values_minutes = [(-12, 46, 43), (-1, 51, 30), (10, 1, 12),
                              (19, 2, 4),(23, 20, 11), (21, 24, 11),
                              (13, 49, 18), (2, 44, 58),(-8, 46, 40),
                              (-18, 39, 40), (-23, 18, 2), (-21, 2, 14)]

# Convert declination values to degrees
declination_values_deg = [(deg + min / 60 + sec / 3600) for deg, min, sec in declination_values_minutes]
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(months, declination_values_deg, marker='o', linestyle='-', color='r')
plt.title("Sun's Declination for Different Months")
plt.xlabel('Month')
plt.ylabel('Declination (degrees)')
plt.grid(True)
plt.show()
