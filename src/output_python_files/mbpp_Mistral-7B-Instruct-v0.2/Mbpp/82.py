"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
import math

def volume_sphere(radius):
    """
    Calculate the volume of a sphere with the given radius.
    :param radius: float
    :return: float
    """
    return (4.0/3.0) * math.pi * (radius ** 3)