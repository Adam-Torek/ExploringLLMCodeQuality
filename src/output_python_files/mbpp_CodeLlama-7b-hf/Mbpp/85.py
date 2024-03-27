"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""

import math


def surfacearea_sphere(radius):
    """
    Calculate the surface area of a sphere.
    :param radius: radius of the sphere
    :return: surface area of the sphere
    """
    return 4 * math.pi * radius ** 2


if __name__ == '__main__':
    print(surfacearea_sphere(10))
</s>