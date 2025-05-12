"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""


def median_trapezium(a, b, c):
    """
    a, b, c: positive integers
    returns: the median length of a trapezium with sides a, b, c
    """
    return (a + b + c) / 2


def test_median_trapezium():
    assert median_trapezium(15, 25, 35) == 20
    assert median_trapezium(1, 2, 3) == 2
    assert median_trapezium(1, 2, 3, 4) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,