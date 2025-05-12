"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""


def otherside_rightangle(a, b):
    """
    a, b are the lengths of the two sides of a right angled triangle
    """
    return (a**2 + b**2)**0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()