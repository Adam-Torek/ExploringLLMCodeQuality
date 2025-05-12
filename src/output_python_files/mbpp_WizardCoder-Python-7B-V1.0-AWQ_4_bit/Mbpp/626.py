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
assert triangle_area(0) == None
assert round(triangle_area(5), 2) == 1.31
assert round(triangle_area(10), 2) == 15.37
assert round(triangle_area(15), 2) == 40.83
assert round(triangle_area(20), 2) == 70.61
assert round(triangle_area(25), 2) == 101.38
assert round(triangle_area(30), 2) == 136.17
assert round(triangle_area(35), 2) == 173.32
assert round(triangle_area(40), 2) == 209.77
assert round(triangle_area(45), 2) == 251.58
assert round(triangle_area(50), 2) == 297.37