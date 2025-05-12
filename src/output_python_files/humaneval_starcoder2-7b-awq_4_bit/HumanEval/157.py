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

def is_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a triangle, False otherwise.
    Example:
    is_triangle(3, 4, 5) == True
    is_triangle(1, 2, 3) == False
    '''

def is_equilateral(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form an equilateral triangle, False otherwise.
    An equilateral triangle is a triangle in which all three sides are equal.
    Example:
    is_equilateral(3, 3, 3) == True
    is_equilateral(1, 2, 3) == False
    '''

def is_isosceles(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form an isosceles triangle, False otherwise.
    An isosceles triangle is a triangle in which two sides are equal.
    Example:
    is_isosceles(3, 4, 4) == True
    is_isosceles(1, 2, 3) == False
    '''

def is_scalene(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a scalene triangle, False otherwise.
    A scalene triangle is a triangle in which all three sides are different.
    Example:
    is_scalene(3, 4, 5) == True
    is_scalene(1, 2, 3) == False
    '''

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

def is_acute_angled_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form an acute-angled triangle, False otherwise.
    An acute-angled triangle is a triangle in which all three angles are less than
    90 degree.
    Example:
    is_acute_angled_triangle(3, 4, 5) == True
    is_acute_angled_triangle(1, 2, 3) == False
    '''

def is_obtuse_angled_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form an obtuse-angled triangle, False otherwise.
    An obtuse-angled triangle is a triangle in which one angle is greater than 90
    degree.
    Example:
    is_obtuse_angled_triangle(3, 4, 5) == True
    is_obtuse_angled_triangle(1,