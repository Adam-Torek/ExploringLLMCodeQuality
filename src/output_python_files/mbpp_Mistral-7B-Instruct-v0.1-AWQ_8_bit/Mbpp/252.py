"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

import math

def convert(c):
    r, i = c.real, c.imag
    return (r, math.atan(i/r))

assert convert(1) == (1.0, 0.0)
assert convert(3) == (2.0, math.pi/4)
assert convert(-3) == (-2.0, -math.pi/4)