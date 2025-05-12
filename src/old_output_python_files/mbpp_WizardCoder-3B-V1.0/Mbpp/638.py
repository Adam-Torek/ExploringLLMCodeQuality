"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind_speed, temperature):
    # convert wind speed to m/s
    wind_speed = wind_speed * 1000
    
    # calculate the wind chill index
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    
    # round the wind chill index to the nearest integer
    wind_chill_index = round(wind_chill_index)
    
    return wind_chill_index<|endoftext|>