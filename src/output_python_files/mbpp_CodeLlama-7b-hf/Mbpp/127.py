"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""


def multiply_int(a, b):
    """
    Multiply two integers
    :param a: int
    :param b: int
    :return: int
    """
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a > b:
        return multiply_int(a - b, b) + multiply_int(a, b - a)
    else:
        return multiply_int(a - b, a) + multiply_int(a, b - a)


if __name__ == '__main__':
    assert multiply_int(10, 20) == 200
    assert multiply_int(10, -20) == -200
    assert multiply_int(-10, 20) == -200
    assert multiply_int(-10, -20) == 200
    assert multiply_int(10, 0) == 0
    assert multiply_int(0, 10) == 0
    assert multiply_int(0, 0) == 0
    assert multiply_int(10, 1) == 10
    assert multiply_int(1, 10) == 10
    assert multiply_int(1, 1) == 1
    assert multiply_int(10, 10) == 100
    assert multiply_int(10, 100) == 1000
    assert multiply_int(100, 10) == 1000
    assert multiply_int(100, 100) == 10000
    assert multiply_int(1000, 100) == 100000
    assert multiply_int(1000, 1000) == 1000000
    assert multiply_int(10000, 1000) == 10000000
    assert multiply_int(10000, 10000) == 100000000
    assert multiply_int(100000, 10000) == 1000000000
    assert multiply_int(100000, 100000) == 10000000000
    assert multiply_int(1000000, 100000) == 100000000000
    assert multiply_int(1000000, 1000000) == 1000000000000
    assert multiply_int(10000000, 1000000) == 10000000000000
    assert multiply_int(10000000, 10000000) == 100000000000000
    assert multiply_int(100000000, 10000000) == 1000000000000000
    assert multiply_int(100000000, 100000000) == 10000000000000000
    assert multiply_int(1000000000, 100000000) == 100000000000000000
    assert multiply_int(1000000000, 1000000000) == 1000000000000000000
    assert multiply_int(10000000000,