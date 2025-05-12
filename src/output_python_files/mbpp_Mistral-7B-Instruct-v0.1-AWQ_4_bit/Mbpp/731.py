"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""

import math

def lateralsurface_cone(r,h):
    """
    This function calculates the lateral surface area of a cone.
    """
    return math.pi*r*(r+h)