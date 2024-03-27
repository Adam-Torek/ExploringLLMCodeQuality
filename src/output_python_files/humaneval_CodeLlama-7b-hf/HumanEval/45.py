def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_angle(a, angle):
    """Given length of a side and angle return area for a triangle.
    >>> triangle_area_from_side_and_angle(5, 30)
    7.5
    """
    return (a * a * math.sin(math.radians(angle))) / 2


def triangle_area_from_side_and_height(a, h):
    """Given length of a side and height return area for a triangle.
    >>> triangle_area_from_side_and_height(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_base(a, b):
    """Given length of a side and base return area for a triangle.
    >>> triangle_area_from_side_and_base(5, 3)
    7.5
    """
    return (a * b) / 2


def triangle_area_from_side_and_altitude(a, h):
    """Given length of a side and altitude return area for a triangle.
    >>> triangle_area_from_side_and_altitude(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_diagonal(a, d):
    """Given length of a side and diagonal return area for a triangle.
    >>> triangle_area_from_side_and_diagonal(5, 3)
    7.5
    """
    return (a * d) / 2


def triangle_area_from_side_and_inradius(a, r):
    """Given length of a side and inradius return area for a triangle.
    >>> triangle_area_from_side_and_inradius(5, 3)
    7.5
    """
    return (a * a * r) / 2


def triangle_area_from_side_and_circumradius(a, r):
    """Given length of a side and circumradius return area for a triangle.
    >>> triangle_area_from_side_and_circumradius(5, 3)
    7.5
    """
    return (a * a * r) / 2


def triangle_area_from_side_and_apothem(a, h):
    """Given length of a side and apothem return area for a triangle.
    >>> triangle_area_from_side_and_apothem(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_orthocenter(a, h):
    """Given length of a side and orthocenter return area for a triangle.
    >>> triangle_area_from_side_and_orthocenter(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_orthocenter_altitude(a, h):
    """Given length of a side and orthocenter altitude return area for a triangle.
    >>> triangle_area_from_side_and_orthocenter_altitude(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_orthocenter_height(a, h):
    """Given length of a side and orthocenter height return area for a triangle.
    >>> triangle_area_from_side_and_orthocenter_height(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_area_from_side_and_orthocenter_base(a, b):
    """Given length of a side and orthocenter base return area for a triangle.
    >>> triangle_area_from_side_and_orthoc