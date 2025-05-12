"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""


def wind_chill(wind_velocity, temperature):
    """
    Calculates the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
    :param wind_velocity: wind velocity in km/h
    :param temperature: temperature in celsius
    :return: wind chill index
    """
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * (wind_velocity ** 0.16) + 0.4275 * (
            temperature * (wind_velocity ** 0.16))
    return round(wind_chill_index)


if __name__ == '__main__':
    print(wind_chill(120, 35))
    print(wind_chill(100, 10))
    print(wind_chill(100, 0))
    print(wind_chill(100, -10))
    print(wind_chill(100, -20))
    print(wind_chill(100, -30))
    print(wind_chill(100, -40))
    print(wind_chill(100, -50))
    print(wind_chill(100, -60))
    print(wind_chill(100, -70))
    print(wind_chill(100, -80))
    print(wind_chill(100, -90))
    print(wind_chill(100, -100))
    print(wind_chill(100, -110))
    print(wind_chill(100, -120))
    print(wind_chill(100, -130))
    print(wind_chill(100, -140))
    print(wind_chill(100, -150))
    print(wind_chill(100, -160))
    print(wind_chill(100, -170))
    print(wind_chill(100, -180))
    print(wind_chill(100, -190))
    print(wind_chill(100, -200))
    print(wind_chill(100, -210))
    print(wind_chill(100, -220))
    print(wind_chill(100, -230))
    print(wind_chill(100, -240))
    print(wind_chill(100, -250))
    print(wind_chill(100, -260))
    print(wind_chill(100, -270))
    print(wind_chill(100, -280))
    print(wind_chill(100, -290))
    print(wind_chill(100, -300))
    print(wind_chill(100, -310))
    print(wind_chill(100, -320))
    print(wind_chill(100, -330))
    print(wind_chill(100, -340))
    print(wind_chill(100, -350))
    print(wind_chill(100, -360))
    print(wind_chill(100, -370))
    print(wind_chill(100, -380))
    print(wind_chill(100, -390))
    print(wind_chill(100, -400))
    print(wind_chill(100, -410))
    print(wind_chill