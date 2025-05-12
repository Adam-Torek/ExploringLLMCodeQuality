"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

import math

def polar_rect(r, theta):
    """
    Convert polar coordinates to rectangular coordinates.
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def test_polar_rect():
    """
    Test polar_rect.
    """
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))

if __name__ == '__main__':
    test_polar_rect()