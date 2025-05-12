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
print(right_angle_triangle(10, 10, 17)) # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(8, 15, 17)) # False
print(right_angle_triangle(5, 12, 17)) # False
print(right_angle_triangle(8, 15, 17)) # False
print(right_angle_triangle(8, 15, 25)) # True
print(right_angle_triangle(10, 10, 17)) # False
print(right_angle_triangle(5, 12, 17)) # False
print(right_angle_triangle(8, 15, 25)) # True
print(right_angle_triangle(10, 10, 17)) # False
print(right_angle_triangle(5, 12, 25)) # False
print(right_angle_triangle(8, 15, 25)) # True
print(right_angle_triangle(10, 10, 27)) # False
print(right_angle_triangle(5, 12, 25)) # False
print(right_angle_triangle(8, 15, 27)) # False
print(right_angle_triangle(10, 10, 27)) # False
print(right_angle_triangle(5, 12, 27)) # False
print(right_angle_triangle(8, 15, 27)) # False
print(right_angle_triangle(10, 10, 27)) # False
print(right_angle_triangle(5, 12, 27)) # False
print(right_angle_triangle(8, 15, 27)) # False
print(right_angle_triangle(10, 10, 27)) # False
print(right_angle_triangle(5, 12, 27)) # False
print(right_angle_triangle(8, 15, 27)) # False
print(right_angle_triangle(10, 10, 27)) # False
print(right_angle_triangle(5,