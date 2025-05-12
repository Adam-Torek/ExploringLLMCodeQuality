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
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

# Test cases
print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(7, 24, 25)) # False
print(right_angle_triangle(10, 10, 10)) # True
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(1, 2, 3)) # False
print(right_angle_triangle(4, 5, 6)) # False
print(right_angle_triangle(7, 24, 25)) # False
print(right_angle_triangle(10, 10, 10)) # True

# Test cases with floating point numbers
print(right_angle_triangle(3.0, 4.0, 5.0)) # True
print(right_angle_triangle(1.0, 2.0, 3.0)) # False
print(right_angle_triangle(5.0, 12.0, 13.0)) # True
print(right_angle_triangle(7.0, 24.0, 25.0)) # False
print(right_angle_triangle(10.0, 10.0, 10.0)) # True
print(right_angle_triangle(5.0, 12.0, 13.0)) # True
print(right_angle_triangle(1.0, 2.0, 3.0)) # False
print(right_angle_triangle(4.0, 5.0, 6.0)) # False
print(right_angle_triangle(7.0, 24.0, 25.0)) # False
print(right_angle_triangle(10.0, 10.0, 10.0)) # True

# Test cases with negative numbers
print(right_angle_triangle(-3, 4, 5)) # True
print(right_angle_triangle(-1, -2, 3)) # False
print(right_angle_triangle(-5, 12, 13)) # True
print(right_angle_triangle(-7, 24, 25)) # False
print(right_angle_triangle(-10, -10, -10)) # True
print(right_angle_triangle(-5, -12, -13)) # True
print(right_angle_triangle(-1, -2, -3