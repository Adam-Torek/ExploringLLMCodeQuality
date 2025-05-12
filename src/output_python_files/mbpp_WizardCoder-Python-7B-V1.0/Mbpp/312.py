"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

print(volume_cone(5,12))

# Test the function with the given test case
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)