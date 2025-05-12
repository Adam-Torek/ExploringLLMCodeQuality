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
    >>> circle_area(5)
    78.53981633974483
    """
    return 3.141592653589793 * r ** 2

def square_area(s):
    """Given side return area for a square.
    >>> square_area(5)
    25
    """
    return s ** 2

def trapezoid_area(b1, b2, h):
    """Given lengths of two parallel sides and height return area for a trapezoid.
    >>> trapezoid_area(5, 6, 3)
    13.5
    """
    return (b1 + b2) / 2 * h

def parallelogram_area(b1, b2, h):
    """Given lengths of two parallel sides and height return area for a parallelogram.
    >>> parallelogram_area(5, 6, 3)
    15
    """
    return b1 * h + b2 * h

def kite_area(a, b):
    """Given lengths of two sides of a kite return area.
    >>> kite_area(5, 6)
    15
    """
    return a * b / 2

def pentagon_area(a, b, c, d, e):
    """Given lengths of sides of a regular pentagon return area.
    >>> pentagon_area(5, 6, 7, 8, 9)
    120.0
    """
    s = (a + b + c + d + e) / 2
    return s * (s - a) * (s - b) * (s - c) * (s - d)

def hexagon_area(a, b, c, d, e, f):
    """Given lengths of sides of a regular hexagon return area.
    >>> hexagon_area(5, 6, 7, 8, 9, 10)
    360.0
    """
    s = (a + b + c + d + e + f) / 2
    return s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e) * (s - f)

def heptagon_area(a, b, c, d, e, f, g):
    """Given lengths of sides of a regular heptagon return area.
    >>> heptagon_area(5, 6, 7, 8, 9, 10, 11)
    420.0
    """
    s = (a + b + c + d + e + f + g) / 2
    return s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e) * (s - f) * (s - g)

def octagon_area(a, b, c, d, e, f, g, h):
    """Given lengths of sides of a regular octagon return area.
    >>> octagon_area(5, 6, 7, 8, 9, 10, 11, 12)
    600.0
    """
    s = (a + b + c + d + e + f + g + h) / 2
    return s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e) * (s - f) * (s - g) * (s - h)

def star_area(n, a, b, c, d, e):
    """Given