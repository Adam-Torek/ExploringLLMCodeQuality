"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
import math


def surfacearea_sphere(radius):
    """
    :param radius: float
    :return: float
    """
    return 4 * math.pi * (radius ** 2)</s>