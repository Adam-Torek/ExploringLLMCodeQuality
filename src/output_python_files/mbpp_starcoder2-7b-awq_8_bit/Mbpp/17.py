"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""

def square_perimeter(side_length):
    return side_length * 4

print(square_perimeter(10))/01_python_basics/01_python_basics_01.py
"""
Write a function that returns the area of a square given its side length as input.
assert square_area(10)==100
"""

def square_area(side_length):
    return side_length * side_length

print(square_area(10))/01_python_basics/01_python_basics_03.py
"""
Write a function that returns the area of a circle given its radius as input.
assert circle_area(10)==314.1592653589793
"""

def circle_area(radius):
    return 3.141592653589793 * radius * radius

print(circle_area(10))/01_python_basics/01_python_basics_02.py
"""
Write a function that returns the perimeter of a circle given its radius as input.
assert circle_perimeter(10)==62.83185307179586
"""

def circle_perimeter(radius):
    return 2 * 3.141592653589793 * radius

print(circle_perimeter(10))/01_python_basics/01_python_basics_04.py
"""
Write a function that returns the volume of a sphere given its radius as input.
assert sphere_volume(10)==4188.790204786391
"""

def sphere_volume(radius):
    return 4/3 * 3.141592653589793 * radius * radius * radius

print(sphere_volume(10))