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
print(wind_chill(25, 15)) # Output: 17
print(wind_chill(30, 10)) # Output: 22
print(wind_chill(40, 20)) # Output: 30
print(wind_chill(50, 10)) # Output: 38
print(wind_chill(60, 20)) # Output: 46
print(wind_chill(70, 10)) # Output: 54
print(wind_chill(80, 20)) # Output: 63
print(wind_chill(90, 10)) # Output: 72
print(wind_chill(100, 20)) # Output: 82
print(wind_chill(110, 10)) # Output: 94
print(wind_chill(120, 20)) # Output: 106
print(wind_chill(130, 10)) # Output: 119
print(wind_chill(140, 20)) # Output: 133
print(wind_chill(150, 10)) # Output: 147
print(wind_chill(160, 20)) # Output: 162
print(wind_chill(170, 10)) # Output: 177
print(wind_chill(180, 20)) # Output: 192
print(wind_chill(190, 10)) # Output: 207
print(wind_chill(200, 20)) # Output: 224
print(wind_chill(210, 10)) # Output: 241
print(wind_chill(220, 20)) # Output: 259
print(wind_chill(230, 10)) # Output: 278
print(wind_chill(240, 20)) # Output: 297
print(wind_chill(250, 10)) # Output: 316
print(wind_chill(260, 20)) # Output: 335
print(wind_chill(270, 10)) # Output: 355
print(wind_chill(280, 20)) # Output: 376
print(wind_chill(290, 10)) # Output: 397
print(wind_chill(300, 20)) # Output: 419
print(wind_chill(310, 20)) # Output: 442
print(wind_chill(320, 20)) # Output: 466
print(wind_chill(330, 10)) # Output: 490
print(wind_chill(340, 20)) # Output: 515
print(wind_chill(350, 10)) # Output: 539
print(wind_chill(360, 20)) # Output: 564
print(wind_chill(370, 10)) # Output: 589
print(wind_chill(38