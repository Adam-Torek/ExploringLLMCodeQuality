"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""

def left_rotate(num, d):
    """
    :type num: int
    :type d: int
    :rtype: int
    """
    if d == 0:
        return num
    num = num << d
    num = num >> (32 - d)
    return num


def test_left_rotate():
    assert left_rotate(16, 2) == 64
    assert left_rotate(16, 0) == 16
    assert left_rotate(16, 4) == 0
    assert left_rotate(16, 1) == 32
    assert left_rotate(16, 3) == 8
    assert left_rotate(16, 5) == 4
    assert left_rotate(16, 6) == 2
    assert left_rotate(16, 7) == 1
    assert left_rotate(16, 8) == 0
    assert left_rotate(16, 9) == 0
    assert left_rotate(16, 10) == 0
    assert left_rotate(16, 11) == 0
    assert left_rotate(16, 12) == 0
    assert left_rotate(16, 13) == 0
    assert left_rotate(16, 14) == 0
    assert left_rotate(16, 15) == 0
    assert left_rotate(16, 16) == 0
    assert left_rotate(16, 17) == 0
    assert left_rotate(16, 18) == 0
    assert left_rotate(16, 19) == 0
    assert left_rotate(16, 20) == 0
    assert left_rotate(16, 21) == 0
    assert left_rotate(16, 22) == 0
    assert left_rotate(16, 23) == 0
    assert left_rotate(16, 24) == 0
    assert left_rotate(16, 25) == 0
    assert left_rotate(16, 26) == 0
    assert left_rotate(16, 27) == 0
    assert left_rotate(16, 28) == 0
    assert left_rotate(16, 29) == 0
    assert left_rotate(16, 30) == 0
    assert left_rotate(16, 31) == 0
    assert left_rotate(16, 32) == 0
    assert left_rotate(16, 33) == 0
    assert left_rotate(16, 34) == 0
    assert left_rotate(16, 35) == 0
    assert left_rotate(16, 36) == 0
    assert left_rotate(16, 37) == 0
    assert left_rotate(16, 38) == 0
    assert left_rotate(16, 39) == 0
    assert left_rotate(16, 40) == 0
    assert left_rotate(16, 41) == 0
    assert left_rotate(16, 42) == 0
    assert left_rotate(16, 43) == 0
    assert left_rotate(16, 44) == 0
    assert left_rotate(16, 45) == 0
    assert left_rotate(16, 46) == 0
    assert left_rotate(16, 47) == 0
    assert left_rotate(16, 48) == 0
    assert left_rotate(16, 49) == 0
    assert left_rotate(16, 50) == 0
    assert left_rotate(16, 51) == 0
    assert left_rotate(16, 52) == 0