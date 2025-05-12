"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""

from math import pi

def lateralsuface_cylinder(r,h):
    """
    This function calculates the lateral surface area of a cylinder.
    :param r: radius of the cylinder
    :param h: height of the cylinder
    :return: lateral surface area of the cylinder
    """
    return 2*pi*r*h