"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""

import math

def otherside_rightangle(a,b):
    """
    This function calculates the other side of a right angled triangle.
    """
    c = math.sqrt(a**2 + b**2)
    return c

assert otherside_rightangle(7,8)==10.63014581273465