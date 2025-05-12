"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

from math import pi

def volume_cone(r,h):
    """
    Calculate the volume of a cone.
    :param r: radius of the base
    :param h: height of the cone
    :return: volume of the cone
    """
    return (1/3) * pi * r**2 * h