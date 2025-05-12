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
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def is_valid_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a valid triangle, False otherwise.
    A valid triangle is a triangle in which the sum of the lengths of any two sides
    is greater than the length of the third side.
    Example:
    is_valid_triangle(3, 4, 5) == True
    is_valid_triangle(1, 2, 3) == True
    is_valid_triangle(1, 2, 4) == False
    '''
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def is_right_angled_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angled_triangle(3, 4, 5) == True
    is_right_angled_triangle(1, 2, 3) == False
    '''
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def is_valid_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a valid triangle, False otherwise.
    A valid triangle is a triangle in which the sum of the lengths of any two sides
    is greater than the length of the third side.
    Example:
    is_valid_triangle(3, 4, 5) == True
    is_valid_triangle(1, 2, 3) == True
    is_valid_triangle(1, 2, 4) == False
    '''
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def is_right_angled_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angled_triangle(3, 4, 5) == True
    is_right_angled_triangle(1, 2, 3) == False
    '''
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def