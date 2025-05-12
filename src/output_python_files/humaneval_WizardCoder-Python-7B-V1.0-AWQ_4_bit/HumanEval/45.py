def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

def rectangle_area(a, b):
    """Given length of two sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """
    return a * b

def square_area(a):
    """Given side of a square return area.
    >>> square_area(5)
    25
    """
    return a ** 2

def circle_area(r):
    """Given radius of a circle return area.
    >>> circle_area(5)
    78.5398
    """
    return 3.14159 * r ** 2

def trapezoid_area(a, b, h):
    """Given two sides and height return area for a trapezoid.
    >>> trapezoid_area(5, 3, 2)
    10.0
    """
    return 0.5 * (a + b) * h

def rhombus_area(d1, d2):
    """Given two diagonals return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    """
    return 0.5 * d1 * d2

def parallelogram_area(a, b):
    """Given two sides return area for a parallelogram.
    >>> parallelogram_area(5, 3)
    15
    """
    return a * b

def kite_area(a, b):
    """Given two sides return area for a kite.
    >>> kite_area(5, 3)
    15
    """
    return 0.5 * a * b

def scalene_triangle_area(a, b, c):
    """Given three sides return area for a scalene triangle.
    >>> scalene_triangle_area(5, 3, 4)
    6.0
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def equilateral_triangle_area(a):
    """Given side return area for an equilateral triangle.
    >>> equilateral_triangle_area(5)
    15
    """
    return (3 ** 0.5) * a ** 2 / 4

def isosceles_triangle_area(a, b, h):
    """Given two sides and height return area for an isosceles triangle.
    >>> isosceles_triangle_area(5, 3, 2)
    10.8284
    """
    return 0.5 * a * b * h

def right_triangle_area(a, h):
    """Given two sides and height return area for a right triangle.
    >>> right_triangle_area(5, 3)
    15
    """
    return 0.5 * a * h

def irregular_triangle_area(a, b, c):
    """Given three sides return area for an irregular triangle.
    >>> irregular_triangle_area(5, 3, 4)
    6.0
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def regular_polygon_area(n