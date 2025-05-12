"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""

from math import pi

def surfacearea_sphere(r):
    """
    Calculate the surface area of a sphere.
    """
    return 4 * pi * r**2