"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

import math

def convert(c):
    r, i = c
    return (math.sqrt(r**2 + i**2), math.atan2(i, r))

assert convert(1) == (1.0, 0.0)
assert convert(3) == (2.0, math.pi/6)
assert convert(-3) == (-2.0, -math.pi/6)
assert convert(0) == (0.0, 0.0)