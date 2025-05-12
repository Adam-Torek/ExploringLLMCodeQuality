"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""

from math import pi

def surfacearea_cylinder(r,h):
    """
    Calculates the surface area of a cylinder.
    :param r: radius of the cylinder
    :param h: height of the cylinder
    :return: surface area of the cylinder
    """
    return 2*pi*r*h + 2*pi*r**2