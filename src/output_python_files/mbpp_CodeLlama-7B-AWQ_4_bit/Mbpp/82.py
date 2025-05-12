"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

import math


def volume_sphere(radius):
    """
    >>> math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
    True
    """
    return (4/3) * math.pi * radius ** 3


if __name__ == "__main__":
    import doctest

    doctest.testmod()