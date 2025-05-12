"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
def wind_chill(wind_velocity: float, temperature: float) -> int:
    """
    Calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
    """
    wind_chill_factor = 0.397 + 0.076 * wind_velocity + 0.038 * (wind_velocity ** 2) - 0.104 * temperature + 0.0062 * (temperature ** 2)
    wind_chill_factor = round(wind_chill_factor)
    return wind_chill_factor


# assert wind_chill(120,35)==40
# assert wind_chill(100,25)==30
# assert wind_chill(50,15)==15
# assert wind_chill(150,30)==45
# assert wind_chill(100,20)==25
# assert wind_chill(150,15)==20
# assert wind_chill(100,10)==15
# assert wind_chill(150,5)==10
# assert wind_chill(100,0)==0
# assert wind_chill(150,-5)==-5
# assert wind_chill(100,-10)==-10
# assert wind_chill(150,-15)==-15
# assert wind_chill(100,-20)==-20
# assert wind_chill(150,-25)==-25
# assert wind_chill(100,-30)==-30
# assert wind_chill(150,-35)==-35
# assert wind_chill(100,-40)==-40
# assert wind_chill(150,-45)==-45
# assert wind_chill(100,-50)==-50
# assert wind_chill(150,-55)==-55
# assert wind_chill(100,-60)==-60
# assert wind_chill(150,-65)==-65
# assert wind_chill(100,-70)==-70
# assert wind_chill(150,-75)==-75
# assert wind_chill(100,-80)==-80
# assert wind_chill(150,-85)==-85
# assert wind_chill(100,-90)==-90
# assert wind_chill(150,-95)==-95
# assert wind_chill(100,-100)==-100
# assert wind_chill(150,-105)==-105
# assert wind_chill(100,-110)==-110
# assert wind_chill(150,-115)==-115
# assert wind_chill(100,-120)==-120
# assert wind_chill(150,-125)==-125
# assert wind_chill(100,-130)==-130
# assert wind_chill(150,-135)==-135
# assert wind_chill(100,-140)==-140
# assert wind_chill(150,-145)==-145
# assert wind_chill(100,-150)==-150
# assert wind_chill(150,-155)==-155
# assert wind_chill(100,-160)==-160
# assert wind_chill(150,-165)==-165
# assert wind_chill