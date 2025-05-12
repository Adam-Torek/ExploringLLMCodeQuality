"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""

def otherside_rightangle(a,b):
    """
    This function takes two sides of a right angled triangle and returns the third side.
    """
    c = (a**2 + b**2)**0.5
    return c

assert otherside_rightangle(7,8)==10.63014581273465