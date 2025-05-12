"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(r):
    return (3 * math.sqrt(3) * r ** 2) / 2

print(area_tetrahedron(3)) # Output: 15.588457268119894