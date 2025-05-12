"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * height

print(lateralsuface_cylinder(10,5))

# Test the function with the given test case
assert math.isclose(lateralsuface_cylinder(10,5), 314.1500000000003, rel_tol=0.001)