"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""


def median_trapezium(a, b, c):
    """
    a, b, c: positive integers
    returns: the median length of a trapezium with sides a, b, c
    """
    # Your code here
    return (a + b + c) / 2


def test_median_trapezium():
    assert median_trapezium(15, 25, 35) == 20
    assert median_trapezium(1, 2, 3) == 2
    assert median_trapezium(1, 2, 3, 4) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5) == 2.5
    assert median_trapezium(1, 2, 3, 4, 5, 6) == 3
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7) == 3.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8) == 4
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9) == 4.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == 5.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == 6
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) == 6.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) == 7
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) == 7.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16) == 8
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) == 8.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18) == 9
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19) == 9.5
    assert median_trapezium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,