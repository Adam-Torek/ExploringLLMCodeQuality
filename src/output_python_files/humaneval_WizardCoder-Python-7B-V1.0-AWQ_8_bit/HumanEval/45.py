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
    """Given side length return area for a square.
    >>> square_area(5)
    25
    """
    return a ** 2

def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(3)
    28.2743333882308187
    """
    return 3.14159 * r ** 2

def trapezoid_area(a, b, h):
    """Given base1, base2, and height return area for a trapezoid.
    >>> trapezoid_area(3, 4, 5)
    11.5
    """
    return 0.5 * (a + b) * h

def rhombus_area(d, h):
    """Given diagonal and height return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    """
    return 0.5 * d * h

def parallelogram_area(a, b):
    """Given base and height return area for a parallelogram.
    >>> parallelogram_area(3, 4)
    12
    """
    return a * b

def kite_area(a, b):
    """Given diagonal1 and diagonal2 return area for a kite.
    >>> kite_area(3, 4)
    12
    """
    return 0.5 * a * b

def scalene_triangle_area(a, b, c):
    """Given sides return area for a scalene triangle.
    >>> scalene_triangle_area(3, 4, 5)
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
    """Given base and height return area for an isosceles triangle.
    >>> isosceles_triangle_area(3, 4)
    6.0
    """
    return 0.5 * a * b * h

def right_triangle_area(a, h):
    """Given side and height return area for a right triangle.
    >>> right_triangle_area(3, 4)
    6.0
    """
    return 0.5 * a * h

def irregular_triangle_area(a, b, c):
    """Given sides return area for an irregular triangle.
    >>> irregular_triangle_area(3, 4, 5)
    6.0
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def polygon_area(n, r):
    """Given number of sides and radius return area for a regular polygon.
    >>> polygon_area(5, 3)
    7.08
    """
    return n * r ** 2 * 3.14159 / 2

def polygon_with_n_sides_and_perimeter(n, p):
    """Given number of sides and perimeter return area for a polygon.
    >>> polygon_with_n_sides_and_perimeter(5, 24)
    12.0