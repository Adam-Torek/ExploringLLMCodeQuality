"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(side):
    """
    Calculate the area of a regular tetrahedron with side length 'side'
    """
    area = (math.sqrt(2)*side**2)/4
    return area

assert area_tetrahedron(3) == 15.588457268119894