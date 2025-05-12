"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(complex_number):
    """
    This function takes a complex number as an argument and returns a tuple of the magnitude and angle in polar coordinates.
    """
    magnitude, angle = cmath.polar(complex_number)
    return (magnitude, angle)

assert convert(1) == (1.0, 0.0)