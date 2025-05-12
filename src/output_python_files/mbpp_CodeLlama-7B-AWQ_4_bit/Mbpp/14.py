"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""

def find_Volume(a,b,c):
    """
    a,b,c: positive integers
    returns: the volume of the triangular prism with the given side lengths
    """
    return a*b*c


def test_find_Volume():
    assert find_Volume(10,8,6) == 240
    assert find_Volume(1,2,3) == 6
    assert find_Volume(1,1,1) == 1
    assert find_Volume(1,1,2) == 2
    assert find_Volume(1,2,1) == 2
    assert find_Volume(2,1,1) == 2
    assert find_Volume(2,1,2) == 4
    assert find_Volume(2,2,1) == 4
    assert find_Volume(2,2,2) == 8
    assert find_Volume(3,2,1) == 6
    assert find_Volume(3,2,2) == 12
    assert find_Volume(3,3,1) == 9
    assert find_Volume(3,3,2) == 18
    assert find_Volume(3,3,3) == 27
    assert find_Volume(4,3,2) == 24
    assert find_Volume(4,3,3) == 36
    assert find_Volume(4,4,2) == 32
    assert find_Volume(4,4,3) == 48
    assert find_Volume(4,4,4) == 64
    assert find_Volume(5,4,3) == 54
    assert find_Volume(5,4,4) == 72
    assert find_Volume(5,5,3) == 60
    assert find_Volume(5,5,4) == 80
    assert find_Volume(5,5,5) == 100
    assert find_Volume(6,5,4) == 72
    assert find_Volume(6,5,5) == 90
    assert find_Volume(6,6,4) == 84
    assert find_Volume(6,6,5) == 108
    assert find_Volume(6,6,6) == 126
    assert find_Volume(7,6,5) == 96
    assert find_Volume(7,6,6) == 120
    assert find_Volume(7,7,5) == 102
    assert find_Volume(7,7,6) == 132
    assert find_Volume(7,7,7) == 162
    assert find_Volume(8,7,6) == 116
    assert find_Volume(8,7,7) == 148
    assert find_Volume(8,8,6) == 120
    assert find_Volume(8,8,7) == 168
    assert find_Volume(8,8,8) == 192
    assert find_Volume(9,8,7) == 140
    assert find_Volume(9,8,8) == 180
    assert find_Volume(9,9,7) == 132
    assert find_Volume(9,9,8) == 172
    assert find_Volume(9,9,9) == 204
    assert find_Volume(10,9,8) == 128
    assert find_Volume(10,9,9) == 168
    assert find_Volume(10,10,8) == 120
    assert find_Volume(10,10,9) == 172
    assert find_Volume(10,10,10) == 200
    assert find_Volume(11,10,9) ==