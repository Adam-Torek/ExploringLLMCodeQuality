def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''

def is_valid_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form a valid triangle. 
    Otherwise return False
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    is_valid_triangle(3, 4, 5) == True
    is_valid_triangle(1, 2, 10) == False
    '''

def is_equilateral(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an equilateral triangle. 
    Otherwise return False
    An equilateral triangle is a triangle in which all three sides are equal.
    Example:
    is_equilateral(3, 3, 3) == True
    is_equilateral(1, 2, 10) == False
    '''

def is_isosceles(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an isosceles triangle. 
    Otherwise return False
    An isosceles triangle is a triangle in which two sides are equal.
    Example:
    is_isosceles(3, 3, 3) == True
    is_isosceles(1, 2, 10) == False
    '''

def is_scalene(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form a scalene triangle. 
    Otherwise return False
    A scalene triangle is a triangle in which all three sides are different.
    Example:
    is_scalene(3, 3, 3) == False
    is_scalene(1, 2, 10) == True
    '''

def is_right_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form a right triangle. 
    Otherwise return False
    A right triangle is a triangle in which one of the angles is a right angle.
    Example:
    is_right_triangle(3, 4, 5) == True
    is_right_triangle(1, 2, 10) == False
    '''

def is_acute_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an acute triangle. 
    Otherwise return False
    An acute triangle is a triangle in which all three angles are less than 90 degrees.
    Example:
    is_acute_triangle(3, 4, 5) == True
    is_acute_triangle(1, 2, 10) == False
    '''

def is_obtuse_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an obtuse triangle. 
    Otherwise return False
    An obtuse triangle is a triangle in which one of the angles is greater than 90 degrees.
    Example:
    is_obtuse_triangle(3, 4, 5) == False
    is_obtuse_triangle(1, 2, 10) == True
    '''

def is_obtuse_acute_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an obtuse acute triangle. 
    Otherwise return False
    An obtuse acute triangle is a triangle in which one of the angles is greater than 90 degrees and the other two angles are less than 90 degrees.
    Example:
    is_obtuse_acute_triangle(3, 4, 5) == False
    is_obtuse_acute_triangle(1, 2, 10) == True
    '''

def is_acute_obtuse_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three sides form an acute obtuse