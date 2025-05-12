"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(degrees: float) -> float:
    """
    Function to convert degrees to radians
    :param degrees: float
    :return: float
    """
    return degrees * (math.pi / 180)

import math

assert radian_degree(90) == 1.5707963267948966