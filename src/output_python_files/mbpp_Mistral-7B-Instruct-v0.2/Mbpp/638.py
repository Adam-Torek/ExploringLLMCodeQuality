"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(wind_velocity: int, temperature: int) -> int:
    """
    Calculate the wind chill index rounded to the next integer
    :param wind_velocity: wind velocity in km/h
    :param temperature: temperature in celsius
    :return: wind chill index rounded to the next integer
    """
    wind_chill_index = int(35.74 + 0.6215 * temperature - 35.75 * (wind_velocity ** 0.16) + 0.4275 * temperature * (wind_velocity ** 0.16))
    return wind_chill_index

assert wind_chill(120,35)==40