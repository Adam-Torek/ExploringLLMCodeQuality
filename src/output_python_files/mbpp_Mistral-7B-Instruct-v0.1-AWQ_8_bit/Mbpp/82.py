"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

from math import pi

def volume_sphere(r):
    """
    Calculate the volume of a sphere.
    :param r: radius of the sphere
    :return: volume of the sphere
    """
    return (4/3) * pi * (r**3)