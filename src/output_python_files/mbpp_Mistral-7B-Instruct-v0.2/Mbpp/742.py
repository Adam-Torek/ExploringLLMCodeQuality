"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(side):
    """
    Calculate the area of a regular tetrahedron with side length 'side'
    :param side: float, length of one side of the tetrahedron
    :return: float, the area of the tetrahedron
    """
    area = (math.sqrt(2) / 4) * side ** 2 * math.sqrt(12 + 5 * math.sqrt(5))
    return area

assert area_tetrahedron(3) == 15.588457268119894