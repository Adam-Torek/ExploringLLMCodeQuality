"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""


def polar_rect(r, theta):
    """
    Write a function to convert polar coordinates to rectangular coordinates.
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    """
    return (r*math.cos(theta), r*math.sin(theta))


def test_polar_rect():
    assert polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2 + 2.4492935982947064e-16j))


if __name__ == '__main__':
    test_polar_rect()


"""
Write a function to convert rectangular coordinates to polar coordinates.
assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
"""


def rect_polar(r, theta):
    """
    Write a function to convert rectangular coordinates to polar coordinates.
    assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
    """
    return (r*math.cos(theta), r*math.sin(theta))


def test_rect_polar():
    assert rect_polar((5.0, 0.9272952180016122)) == (3.0, 4.0)


if __name__ == '__main__':
    test_rect_polar()


"""
Write a function to convert rectangular coordinates to polar coordinates.
assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
"""


def rect_polar(r, theta):
    """
    Write a function to convert rectangular coordinates to polar coordinates.
    assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
    """
    return (r*math.cos(theta), r*math.sin(theta))


def test_rect_polar():
    assert rect_polar((5.0, 0.9272952180016122)) == (3.0, 4.0)


if __name__ == '__main__':
    test_rect_polar()


"""
Write a function to convert rectangular coordinates to polar coordinates.
assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
"""


def rect_polar(r, theta):
    """
    Write a function to convert rectangular coordinates to polar coordinates.
    assert rect_polar((5.0, 0.9272952180016122))==(3.0, 4.0)
    """
    return (r*math.cos(theta), r*math.sin(theta))


def test_rect_polar():
    assert rect_polar((5.0, 0.9272952180016122)) == (3.0, 4.0)


if __name__ == '__main__':
    test_rect_polar()


"""
Write a function to convert rectangular coordinates to polar coordinates.