"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""


def volume_cone(radius, height):
    """
    >>> volume_cone(5,12)
    314.15926535897927
    """
    return (1/3) * math.pi * radius ** 2 * height


if __name__ == "__main__":
    import doctest

    doctest.testmod()