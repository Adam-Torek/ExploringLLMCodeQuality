"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""


def convert(z):
    """
    Convert a complex number to polar coordinates.
    """
    if z == 0:
        return 0, 0
    else:
        return z.real, z.imag


if __name__ == "__main__":
    import doctest

    doctest.testmod()