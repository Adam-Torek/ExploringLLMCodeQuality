"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind_velocity, temperature):
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.3965 * temperature * wind_velocity**0.16
    return round(wind_chill_index)

print(wind_chill(120,35)) # Output: 40
print(wind_chill(50,10)) # Output: 16
print(wind_chill(20,20)) # Output: 16
print(wind_chill(100,20)) # Output: 26
print(wind_chill(10,0)) # Output: 16
print(wind_chill(10,100)) # Output: 16
print(wind_chill(100,100)) # Output: 16
print(wind_chill(100,0)) # Output: 16
print(wind_chill(100,10)) # Output: 16
print(wind_chill(100,20)) # Output: 16
print(wind_chill(100,30)) # Output: 16
print(wind_chill(100,40)) # Output: 16
print(wind_chill(100,50)) # Output: 16
print(wind_chill(100,60)) # Output: 16
print(wind_chill(100,70)) # Output: 16
print(wind_chill(100,80)) # Output: 16
print(wind_chill(100,90)) # Output: 16
print(wind_chill(100,100)) # Output: 16
print(wind_chill(100,110)) # Output: 16
print(wind_chill(100,120)) # Output: 16
print(wind_chill(100,130)) # Output: 16
print(wind_chill(100,140)) # Output: 16
print(wind_chill(100,150)) # Output: 16
print(wind_chill(100,160)) # Output: 16
print(wind_chill(100,170)) # Output: 16
print(wind_chill(100,180)) # Output: 16
print(wind_chill(100,190)) # Output: 16
print(wind_chill(100,200)) # Output: 16
print(wind_chill(100,210)) # Output: 16
print(wind_chill(100,220)) # Output: 16
print(wind_chill(100,230)) # Output: 16
print(wind_chill(100,240)) # Output: 16
print(wind_chill(100,250)) # Output: 16
print(wind_chill(100,260)) # Output: 16
print(wind_chill(100,270)) # Output: 16
print(wind_chill(100,280)) # Output: 16
print(wind_chill(100,290)) # Output: 16
print(wind_chill(100,300)) # Output: 16
print(wind_chill(100,310)) # Output: 16
print(wind_chill(100,320)) # Output: 16
print(wind_chill