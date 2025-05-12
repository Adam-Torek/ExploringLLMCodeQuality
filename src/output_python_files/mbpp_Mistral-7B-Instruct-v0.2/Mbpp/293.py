"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
def otherside_rightangle(base, height):
    """
    This function takes the base and height of a right angled triangle as arguments and returns the length of the third side.
    """
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    return hypotenuse

assert otherside_rightangle(7, 8) == 10.63014581273465
print("Test passed!")