"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""


def volume_cube(side):
    """
    >>> volume_cube(3)
    27
    >>> volume_cube(4)
    64
    >>> volume_cube(5)
    125
    """
    return side ** 3


if __name__ == "__main__":
    import doctest

    doctest.testmod()