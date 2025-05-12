"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""

import math

def triangle_area(r):
    """
    :param r: float
    :return: float
    """
    if r < 0:
        return None
    else:
        return (math.sqrt(3) / 4) * r ** 2