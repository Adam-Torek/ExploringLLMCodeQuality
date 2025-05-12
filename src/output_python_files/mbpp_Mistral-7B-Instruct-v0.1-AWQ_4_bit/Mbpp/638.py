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
# assert wind_chill(50,10)==10
# assert wind_chill(200,15)==50
# assert wind_chill(150,20)==60
# assert wind_chill(250,25)==70
# assert wind_chill(300,30)==80
# assert wind_chill(350,35)==90
# assert wind_chill(400,40)==100
# assert wind_chill(450,45)==110
# assert wind_chill(500,50)==120
# assert wind_chill(550,55)==130
# assert wind_chill(600,60)==140
# assert wind_chill(650,65)==150
# assert wind_chill(700,70)==160
# assert wind_chill(750,75)==170
# assert wind_chill(800,80)==180
# assert wind_chill(850,85)==190
# assert wind_chill(900,90)==200
# assert wind_chill(950,95)==210
# assert wind_chill(1000,100)==220
# assert wind_chill(1050,105)==230
# assert wind_chill(1100,110)==240
# assert wind_chill(1150,115)==250
# assert wind_chill(1200,120)==260
# assert wind_chill(1250,125)==270
# assert wind_chill(1300,130)==280
# assert wind_chill(1350,135)==290
# assert wind_chill(1400,140)==300
# assert wind_chill(1450,145)==310
# assert wind_chill(1500,150)==320
# assert wind_chill(1550,155)==330
# assert wind_chill(1600,160)==340
# assert wind_chill(1650,165)==350
# assert wind_chill(1700,170)==360
# assert wind_chill(1750,175)==370
# assert wind_chill(1800,180)==380
# assert wind_chill(1850,185)==390
# assert wind_chill(1900,190)==400
# assert wind_chill(1950,195)==410
# assert wind_chill(2000,2