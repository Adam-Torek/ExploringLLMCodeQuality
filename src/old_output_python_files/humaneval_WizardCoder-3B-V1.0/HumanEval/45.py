def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
#    return 0.5 * a * h
    return 0.5 * a * h

def triangle_perimeter(a, h):
    """Given length of a side and high return perimeter for a triangle.
    >>> triangle_perimeter(5, 3)
    15
    """
    return a + a + h

def is_valid_triangle(a, h):
    """Check if given length of a side and high is a valid triangle.
    >>> is_valid_triangle(5, 3)
    True
    >>> is_valid_triangle(4, 4)
    False
    """
    if a + h > a:
        return True
    else:
        return False

def is_equilateral_triangle(a, h):
    """Check if given length of a side and high is an equilateral triangle.
    >>> is_equilateral_triangle(5, 5)
    True
    >>> is_equilateral_triangle(4, 4)
    False
    """
    if a == h:
        return True
    else:
        return False

def is_isosceles_triangle(a, h):
    """Check if given length of a side and high is an isosceles triangle.
    >>> is_isosceles_triangle(5, 5)
    False
    >>> is_isosceles_triangle(4, 4)
    True
    """
    if a == h or a == h:
        return True
    else:
        return False

def is_scalene_triangle(a, h):
    """Check if given length of a side and high is a scalene triangle.
    >>> is_scalene_triangle(5, 5)
    False
    >>> is_scalene_triangle(4, 4)
    False
    """
    if a!= h and a!= h:
        return True
    else:
        return False

def is_right_triangle(a, h):
    """Check if given length of a side and high is a right triangle.
    >>> is_right_triangle(5, 5)
    True
    >>> is_right_triangle(4, 4)
    False
    """
    if a == h:
        return True
    else:
        return False

def is_obtuse_triangle(a, h):
    """Check if given length of a side and high is an obtuse triangle.
    >>> is_obtuse_triangle(5, 5)
    False
    >>> is_obtuse_triangle(4, 4)
    True
    """
    if a > h:
        return True
    else:
        return False

def is_acute_triangle(a, h):
    """Check if given length of a side and high is an acute triangle.
    >>> is_acute_triangle(5, 5)
    False
    >>> is_acute_triangle(4, 4)
    False
    """
    if a < h:
        return True
    else:
        return False

def is_obtuse_acute_triangle(a, h):
    """Check if given length of a side and high is an obtuse and acute triangle.
    >>> is_obtuse_acute_triangle(5, 5)
    False
    >>> is_obtuse_acute_triangle(4, 4)
    True
    """
    if a > h and a < h:
        return True
    else:
        return False

def is_valid_triangle_type(a, h):
    """Check if given length of a side and high is a valid triangle type.
    >>> is_valid_triangle_type(5, 5)
    True
    >>> is_valid_triangle_type(4, 4)
    False
    """
    if is_right_triangle(a, h):
        return "Right"
    elif is_obtuse_triangle(a, h):
        return "Obtuse"
    elif is_acute_triangle(a, h):
        return "Acute"
    elif is_obtuse_acute_triangle(a, h):
        return "Obtuse and Acute"
    else:
        return "Scalene"

def is_valid_triangle_shape(a, h):
    """Check if given length of a side and high is a valid triangle shape.
    >>> is_valid_triangle_shape(5, 5)
    True
    >>> is_valid_triangle_shape(4, 4)
    False
    """
    if is_equilateral_triangle(a, h):
        return "Equ