import matplotlib.pyplot as plt
# Data for Moon over a period of 2 months with an interval of 2 days
moon_declination_values_minutes = [
    (17, 12, 36), (25, 29, 2), (28, 10, 2), (25, 4, 42), (17, 35, 57), (7, 32, 53), (-3, 29, 48),
    (-14, 11, 32), (-23, 4, 34), (-28, 9, 38), (-27, 9, 59), (-19, 10, 59), (-6, 3, 43), (8, 29, 16),
    (20, 36, 40), (27, 27, 58), (27, 57, 20), (22, 54, 53), (14, 10, 37), (3, 29, 50), (-7, 14, 15),
    (-17, 54, 56), (-25, 32, 45), (-28, 31, 6), (-25, 11, 46), (-15, 41, 10), (-2, 6, 32), (12, 9, 12),
    (23, 19, 26), (28, 28, 0), (26, 54, 34)]
# Convert declination values to degrees
moon_declination_values_deg = [(deg + min / 60 + sec / 3600) for deg, min, sec in moon_declination_values_minutes]
# Create corresponding time axis (assuming an interval of 2 days)
days = list(range(2, len(moon_declination_values_deg) * 2 + 2, 2))
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(days, moon_declination_values_deg, marker='o', linestyle='-', color='m')
plt.title("Moon's Declination Over 2 Months (Interval: 2 Days)")
plt.xlabel('Days')
plt.ylabel('Declination (degrees)')
plt.grid(True)
plt.show()
