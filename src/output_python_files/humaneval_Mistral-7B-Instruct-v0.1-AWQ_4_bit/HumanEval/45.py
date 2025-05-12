def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

def rectangle_area(w, h):
    """Given width and height return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """
    return w * h

def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(3)
    28.274333882308138
    """
    return 3.141592653589793 * r ** 2

def square_area(s):
    """Given side return area for a square.
    >>> square_area(5)
    25
    """
    return s ** 2

def trapezoid_area(a, b, h):
    """Given length of two sides and high return area for a trapezoid.
    >>> trapezoid_area(5, 6, 3)
    13.5
    """
    return (a + b) / 2 * h

def parallelogram_area(a, b, h):
    """Given length of two sides and high return area for a parallelogram.
    >>> parallelogram_area(5, 6, 3)
    15
    """
    return a * h + b * h

def kite_area(a, b, c, d):
    """Given length of four sides return area for a kite.
    >>> kite_area(5, 6, 7, 8)
    20
    """
    return (a + c) * (b + d) / 2

def pentagon_area(a, b, c, d, e):
    """Given length of five sides return area for a pentagon.
    >>> pentagon_area(5, 6, 7, 8, 9)
    30
    """
    return (a + b + c + d + e) / 2 * (a * b + b * c + c * d + d * e + e * a) / 4

def hexagon_area(a, b, c, d, e, f):
    """Given length of six sides return area for a hexagon.
    >>> hexagon_area(5, 6, 7, 8, 9, 10)
    45
    """
    return (a + b + c + d + e + f) / 2 * (a * b + b * c + c * d + d * e + e * f + f * a) / 6

def heptagon_area(a, b, c, d, e, f, g):
    """Given length of seven sides return area for a heptagon.
    >>> heptagon_area(5, 6, 7, 8, 9, 10, 11)
    60
    """
    return (a + b + c + d + e + f + g) / 2 * (a * b + b * c + c * d + d * e + e * f + f * g + g * a) / 7

def octagon_area(a, b, c, d, e, f, g, h):
    """Given length of eight sides return area for an octagon.
    >>> octagon_area(5, 6, 7, 8, 9, 10, 11, 12)
    90