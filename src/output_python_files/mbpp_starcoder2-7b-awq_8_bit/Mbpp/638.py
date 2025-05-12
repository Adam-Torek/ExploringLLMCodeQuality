"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind,temp):
    if wind<50 and temp>10:
        return 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    else:
        return "Invalid Input"

print(wind_chill(120,35))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function to calculate the area of a triangle given the base and height.
assert area_triangle(10,5)==25
"""

def area_triangle(base,height):
    return (base*height)/2

print(area_triangle(10,5))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function to calculate the area of a circle given the radius.
assert area_circle(10)==314.1592653589793
"""

def area_circle(radius):
    return 3.141592653589793*radius**2

print(area_circle(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function to calculate the area of a square given the side.
assert area_square(10)==100
"""

def area_square(side):
    return side**2

print(area_square(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function to calculate the area of a rectangle given the length and width.
assert area_rectangle(10,5)==50
"""

def area_rectangle(length,width):
    return length*width

print(area_rectangle(10,5))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function to calculate the area of a pentagon given the side.
assert area_pentagon(10)==157.07963267948966
"""

def area_pentagon(side):
    return (5*side**2)/4*3.141592653589793

print(area_pentagon(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a function to calculate the area of a hexagon given the side.
assert area_hexagon(10)==157.07963267948966
"""

def area_hexagon(side):
    return (6*side**2)/4*3.141592653589793

print(area_hexagon(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a function to calculate the area of a octagon given the side.
assert area_octagon(10)==157.07963267948966
"""

def area_octagon(side):
    return (8*side**2)/4*3.141592653589793

print(area_octagon(10))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a function to calculate the area of a decagon given the side.
assert area_decagon(10)==157.07963267948966
"""

def area_decagon(side):
    return (10*side**2)/4*3.141592653589793

print(area_decagon(10))
/Python/Python_Basics/Python_Basics_1