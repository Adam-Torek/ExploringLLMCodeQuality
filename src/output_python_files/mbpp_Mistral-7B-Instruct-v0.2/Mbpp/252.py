"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(complex_num):
    """
    This function converts a complex number to polar coordinates (magnitude, angle)
    :param complex_num: complex number
    :return: tuple of magnitude and angle
    """
    magnitude, angle = cmath.polar(complex_num)
    return (magnitude, angle)

if __name__ == "__main__":
    assert convert(1) == (1.0, 0.0)
    assert convert(3 + 4j) == (5.0, 0.6435013138598855)
    assert convert(-1 - 1j) == (2.0, 3.141592653589793)