"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(degree):
    return degree*math.pi/180

print(radian_degree(90))
/python_basics/python_basics_002.py
"""
Write a function to convert Celsius to Fahrenheit.
assert celsius_to_fahrenheit(0)==32
"""

def celsius_to_fahrenheit(celsius):
    return celsius*1.8+32

print(celsius_to_fahrenheit(0))
/python_basics/python_basics_003.py
"""
Write a function to convert Fahrenheit to Celsius.
assert fahrenheit_to_celsius(32)==0
"""

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)/1.8

print(fahrenheit_to_celsius(32))
/python_basics/python_basics_001.py
"""
Write a function to convert Fahrenheit to Celsius.
assert fahrenheit_to_celsius(32)==0
"""

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)/1.8

print(fahrenheit_to_celsius(32))
/python_basics/python_basics_004.py
"""
Write a function to convert Celsius to Kelvin.
assert celsius_to_kelvin(0)==273.15
"""

def celsius_to_kelvin(celsius):
    return celsius+273.15

print(celsius_to_kelvin(0))
/python_basics/python_basics_005.py
"""
Write a function to convert Kelvin to Celsius.
assert kelvin_to_celsius(273.15)==0
"""

def kelvin_to_celsius(kelvin):
    return kelvin-273.15

print(kelvin_to_celsius(273.15))
/python_basics/python_basics_006.py
"""
Write a function to convert Kelvin to Fahrenheit.
assert kelvin_to_fahrenheit(273.15)==32
"""

def kelvin_to_fahrenheit(kelvin):
    return kelvin_to_celsius(kelvin)*1.8+32

print(kelvin_to_fahrenheit(273.15))
/python_basics/python_basics_007.py
"""
Write a function to convert Fahrenheit to Kelvin.
assert fahrenheit_to_kelvin(32)==273.15
"""

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

print(fahrenheit_to_kelvin(32))
/python_basics/python_basics_008.py
"""
Write a function to convert Celsius to Kelvin.
assert celsius_to_kelvin(0)==273.15
"""

def celsius_to_kelvin(celsius):
    return celsius+273.15

print(celsius_to_kelvin(0))