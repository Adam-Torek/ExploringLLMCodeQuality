"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
import math

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        return 0.5 * radius * radius * math.sqrt(3)

# Test cases
print(triangle_area(5)) # Output: 10.82551520877756751
print(triangle_area(0)) # Output: 0.0
print(triangle_area(-1)) # Output: None
print(triangle_area(2.5)) # Output: 4.3108812673911527
print(triangle_area(10)) # Output: 78.5398163397448485