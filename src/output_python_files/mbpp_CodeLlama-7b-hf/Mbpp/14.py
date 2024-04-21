"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""


def find_Volume(a, b, c):
    """
    a, b, c: positive integers
    returns: the volume of the triangular prism with the given side lengths
    """
    # Your code here
    return a * b * c


def test_find_Volume():
    assert find_Volume(10, 8, 6) == 240
    assert find_Volume(1, 2, 3) == 6
    assert find_Volume(1, 1, 1) == 1
    assert find_Volume(1, 1, 10) == 10
    assert find_Volume(10, 10, 10) == 1000
    assert find_Volume(10, 10, 100) == 10000
    assert find_Volume(10, 10, 1000) == 100000
    assert find_Volume(10, 10, 10000) == 1000000
    assert find_Volume(10, 10, 100000) == 10000000
    assert find_Volume(10, 10, 1000000) == 100000000
    assert find_Volume(10, 10, 10000000) == 1000000000
    assert find_Volume(10, 10, 100000000) == 10000000000
    assert find_Volume(10, 10, 1000000000) == 100000000000
    assert find_Volume(10, 10, 10000000000) == 1000000000000
    assert find_Volume(10, 10, 100000000000) == 10000000000000
    assert find_Volume(10, 10, 1000000000000) == 100000000000000
    assert find_Volume(10, 10, 10000000000000) == 1000000000000000
    assert find_Volume(10, 10, 100000000000000) == 10000000000000000
    assert find_Volume(10, 10, 1000000000000000) == 100000000000000000
    assert find_Volume(10, 10, 10000000000000000) == 1000000000000000000
    assert find_Volume(10, 10, 100000000000000000) == 10000000000000000000
    assert find_Volume(10, 10, 1000000000000000000) == 100000000000000000000
    assert find_Volume(10, 10, 10000000000000000000) == 1000000000000000000000
    assert find_Volume(10, 10, 100000000000000000000) ==