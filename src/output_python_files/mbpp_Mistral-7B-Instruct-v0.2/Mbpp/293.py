"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
def otherside_rightangle(base, height):
    """
    Calculate the length of the third side of a right angled triangle
    given the lengths of the other two sides.

    Parameters:
        base (float): The length of the base side of the triangle.
        height (float): The length of the height side of the triangle.

    Returns:
        float: The length of the third side of the triangle.
    """
    # Calculate the length of the third side using the Pythagorean theorem
    return (base**2 + height**2) ** 0.5

# Test the function
assert otherside_rightangle(7, 8) == 10.63014581273465
print("Test passed!")</s>