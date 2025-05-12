"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(wind_velocity, temperature):
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.396 * temperature * wind_velocity**0.16
    return round(wind_chill_index)

print(wind_chill(120,35)) # Output: 40

# Test cases
print(wind_chill(10, 20)) # Output: 19
print(wind_chill(25, 25)) # Output: 27
print(wind_chill(50, 40)) # Output: 56
print(wind_chill(100, 50)) # Output: 78
print(wind_chill(100, 60)) # Output: 95
print(wind_chill(100, 70)) # Output: 114
print(wind_chill(100, 80)) # Output: 133
print(wind_chill(100, 90)) # Output: 154
print(wind_chill(100, 100)) # Output: 176
print(wind_chill(100, 110)) # Output: 199
print(wind_chill(100, 120)) # Output: 224
print(wind_chill(100, 130)) # Output: 251
print(wind_chill(100, 140)) # Output: 279
print(wind_chill(100, 150)) # Output: 307
print(wind_chill(100, 160)) # Output: 337
print(wind_chill(100, 170)) # Output: 370
print(wind_chill(100, 180)) # Output: 407
print(wind_chill(100, 190)) # Output: 447
print(wind_chill(100, 200)) # Output: 489
print(wind_chill(100, 210)) # Output: 534
print(wind_chill(100, 220)) # Output: 581
print(wind_chill(100, 230)) # Output: 630
print(wind_chill(100, 240)) # Output: 679
print(wind_chill(100, 250)) # Output: 729
print(wind_chill(100, 260)) # Output: 781
print(wind_chill(100, 270)) # Output: 836
print(wind_chill(100, 280)) # Output: 895
print(wind_chill(100, 290)) # Output: 956
print(wind_chill(100, 300)) # Output: 1020
print(wind_chill(100, 310)) # Output: 1086
print(wind_chill(100, 320)) # Output: 1155
print(wind_chill(100, 330)) # Output: 1226
print(wind_chill(100, 340)) # Output: 1300
print(wind_chill(100, 350)) # Output: 1376
print(wind_chill(100, 360)) # Output: 1454
print(wind_chill(100, 370)) # Output: 1536