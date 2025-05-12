"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(a):
    return (a**2)*math.sqrt(3)/2

print(area_tetrahedron(3))

# Output: 15.58845726811989414