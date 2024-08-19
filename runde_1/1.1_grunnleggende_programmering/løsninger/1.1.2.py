from math import pi

diameter = 10   # cm
høyde = 15      # cm
volum_i_cm3 = pi*(diameter / 2)**2 * høyde 
volum_i_dm3 = volum_i_cm3 / 1000

print('Volumet av sylinderen er', round(volum_i_dm3, 2), 'dm^3.')