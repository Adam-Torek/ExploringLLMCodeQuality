"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind_speed, temperature):
    """
    Calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
    :param wind_speed: wind speed in km/h
    :param temperature: temperature in celsius
    :return: wind chill index
    """
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * (temperature ** 0.16) * (wind_speed ** 0.16)
    return int(round(wind_chill_index))


if __name__ == '__main__':
    print(wind_chill(120, 35))
    print(wind_chill(100, 10))
    print(wind_chill(100, 100))
    print(wind_chill(100, 1000))
    print(wind_chill(100, 10000))
    print(wind_chill(100, 100000))
    print(wind_chill(100, 1000000))
    print(wind_chill(100, 10000000))
    print(wind_chill(100, 100000000))
    print(wind_chill(100, 1000000000))
    print(wind_chill(100, 10000000000))
    print(wind_chill(100, 100000000000))
    print(wind_chill(100, 1000000000000))
    print(wind_chill(100, 10000000000000))
    print(wind_chill(100, 100000000000000))
    print(wind_chill(100, 1000000000000000))
    print(wind_chill(100, 10000000000000000))
    print(wind_chill(100, 100000000000000000))
    print(wind_chill(100, 1000000000000000000))
    print(wind_chill(100, 10000000000000000000))
    print(wind_chill(100, 100000000000000000000))
    print(wind_chill(100, 1000000000000000000000))
    print(wind_chill(100, 10000000000000000000000))
    print(wind_chill(100, 100000000000000000000000))
    print(wind_chill(100, 1000000000000000000000000))
    print(wind_chill(100, 10000000000000000000000000))
    print(wind_chill(100, 100000000000000000000000000))