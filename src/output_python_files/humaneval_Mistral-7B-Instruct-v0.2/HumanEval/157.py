def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Check if the given sides can form a right-angled triangle
    # using the Pythagorean theorem: a² + b² = c²
    return (a**2 + b**2 == c**2)

# Test the function
print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(3, 4, 6)) # False</s>