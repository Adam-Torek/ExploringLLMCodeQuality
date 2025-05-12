"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""


def lateralsuface_cylinder(radius, height):
    """
    >>> lateralsuface_cylinder(10,5)
    314.15000000000003
    """
    return 2 * radius * height + 2 * math.pi * radius * radius


if __name__ == "__main__":
    import doctest

    doctest.testmod()