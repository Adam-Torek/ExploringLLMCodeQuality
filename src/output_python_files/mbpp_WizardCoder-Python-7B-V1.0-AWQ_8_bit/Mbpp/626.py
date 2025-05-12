"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""

import math

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        area = (math.sqrt(3) * radius**2) / 4
        return area

print(triangle_area(-1))
print(triangle_area(5))
print(triangle_area(10))

# Test cases
assert triangle_area(-1) == None
assert round(triangle_area(5), 2) == 1.39
assert round(triangle_area(10), 2) == 15.39
assert round(triangle_area(15), 2) == 40.39
assert round(triangle_area(20), 2) == 70.69
assert round(triangle_area(25), 2) == 101.96
assert round(triangle_area(30), 2) == 139.89
assert round(triangle_area(35), 2) == 177.04
assert round(triangle_area(40), 2) == 211.65
assert round(triangle_area(45), 2) == 249.01
assert round(triangle_area(50), 2) == 281.14