from math import radians, degrees, sin, cos, tan, asin, atan2
from astropy.time import Time

def calculate_hour_angle_declination(altitude, azimuth, latitude):
    a = radians(altitude)
    A = radians(azimuth)
    phi = radians(latitude)

    H = degrees(atan2(sin(A), (cos(phi) * cos(A) - sin(phi) * tan(a))))
    delta = degrees(asin(sin(phi) * sin(a) + cos(phi) * cos(a) * cos(A)))

    return H, delta

def degrees_to_hms(degrees):
    hours = int(degrees / 15)
    minutes = int((degrees % 15) * 4)
    seconds = int(((degrees % 15) * 4 - minutes / 60) * 240)
    return hours, minutes, seconds

# Altitude and azimuth information for Northern Hemisphere stars (Akfa_farkadain, Circitores, Alahakan)
altitude_Akfa_farkadain = 13 + 8/60 + 0/3600  # in degrees
azimuth_Akfa_farkadain = 348 + 47/60 + 0/3600  # in degrees

altitude_Circitores = 17 + 10/60 + 0/3600  # in degrees
azimuth_Circitores = 351 + 48/60 + 0/3600  # in degrees

altitude_Alahakan = 21 + 38/60 + 0/3600  # in degrees
azimuth_Alahakan = 341 + 46/60 + 0/3600  # in degrees

latitude_northern = 19.18239  # in degrees

# Altitude and azimuth information for Southern Hemisphere stars (Alpha_tra, Beta_tra, Gamma_tra)
altitude_Alpha_tra = 13 + 3/60 + 0/3600  # in degrees
azimuth_Alpha_tra = 177 + 26/60 + 0/3600  # in degrees

altitude_Beta_tra = 8 + 43/60 + 0/3600  # in degrees
azimuth_Beta_tra = 170 + 52/60 + 0/3600  # in degrees

altitude_Gamma_tra = 14 + 58/60 + 0/3600  # in degrees
azimuth_Gamma_tra = 169 + 41/60 + 0/3600  # in degrees

latitude_southern = 33  # in degrees

# Calculate hour angle and declination for Akfa_farkadain
H_Akfa_farkadain, delta_Akfa_farkadain = calculate_hour_angle_declination(altitude_Akfa_farkadain, azimuth_Akfa_farkadain, latitude_northern)

# Calculate hour angle and declination for Circitores
H_Circitores, delta_Circitores = calculate_hour_angle_declination(altitude_Circitores, azimuth_Circitores, latitude_northern)

# Calculate hour angle and declination for Alahakan
H_Alahakan, delta_Alahakan = calculate_hour_angle_declination(altitude_Alahakan, azimuth_Alahakan, latitude_northern)

# Calculate hour angle and declination for Alpha_tra
H_Alpha_tra, delta_Alpha_tra = calculate_hour_angle_declination(altitude_Alpha_tra, azimuth_Alpha_tra, latitude_southern)

# Calculate hour angle and declination for Beta_tra
H_Beta_tra, delta_Beta_tra = calculate_hour_angle_declination(altitude_Beta_tra, azimuth_Beta_tra, latitude_southern)

# Calculate hour angle and declination for Gamma_tra
H_Gamma_tra, delta_Gamma_tra = calculate_hour_angle_declination(altitude_Gamma_tra, azimuth_Gamma_tra, latitude_southern)

print("Hour Angle and Declination for Circumpolar Stars in Northern Hemisphere (Mumbai):")
print("-" * 80)
print("Akfa Farkadain:\tHour Angle:", H_Akfa_farkadain, "\tDeclination:", delta_Akfa_farkadain)
print("Circitores:\tHour Angle:", H_Circitores, "\tDeclination:", delta_Circitores)
print("Alahakan:\tHour Angle:", H_Alahakan, "\tDeclination:", delta_Alahakan)

print("\nHour Angle and Declination for Circumpolar Stars in Southern Hemisphere (Sydney, Australia):")
print("-" * 80)
print("Alpha_tra:\tHour Angle:", H_Alpha_tra, "\tDeclination:", delta_Alpha_tra)
print("Beta_tra:\tHour Angle:", H_Beta_tra, "\tDeclination:", delta_Beta_tra)
print("Gamma_tra:\tHour Angle:", H_Gamma_tra, "\tDeclination:", delta_Gamma_tra)

# Date and time of the observation
date_time = "2024-02-15 02:30:00"
# Convert to Julian date
jd = Time(date_time).jd
print("\nJulian Date:", jd)
