"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
import math

def surfacearea_sphere(radius):
    """
    Calculate the surface area of a sphere using the formula: 4 * pi * r^2
    :param radius: float, the radius of the sphere
    :return: float, the surface area of the sphere
    """
    return 4 * math.pi * (radius ** 2)