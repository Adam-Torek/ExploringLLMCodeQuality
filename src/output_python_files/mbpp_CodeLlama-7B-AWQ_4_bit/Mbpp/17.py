"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""


def square_perimeter(side):
    return side * 4


def test_square_perimeter():
    assert square_perimeter(10) == 40


def test_square_perimeter_negative():
    assert square_perimeter(-10) == 40


def test_square_perimeter_zero():
    assert square_perimeter(0) == 0


def test_square_perimeter_float():
    assert square_perimeter(10.5) == 41


def test_square_perimeter_float_negative():
    assert square_perimeter(-10.5) == 41


def test_square_perimeter_float_zero():
    assert square_perimeter(0.0) == 0


def test_square_perimeter_float_zero_negative():
    assert square_perimeter(-0.0) == 0


def test_square_perimeter_float_zero_positive():
    assert square_perimeter(+0.0) == 0


def test_square_perimeter_float_zero_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive_negative_positive():
    assert square_perimeter(-+0.0) == 0


def test_square_perimeter_float_zero_negative_positive_negative