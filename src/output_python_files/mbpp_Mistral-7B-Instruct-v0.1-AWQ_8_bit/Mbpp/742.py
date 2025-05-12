"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""

import math

def area_tetrahedron(n):
    """
    Calculate the area of a tetrahedron.
    """
    # Calculate the height of the tetrahedron
    h = math.sqrt(n**2 - 4*n/3)
    # Calculate the area of the base of the tetrahedron
    a = n/2
    b = n/2
    c = n/2
    area_base = 0.5*a*b*c
    # Calculate the area of the tetrahedron
    area_tetrahedron = 0.5*a*b*c*h
    return area_tetrahedron

assert area_tetrahedron(3)==15.588457268119894