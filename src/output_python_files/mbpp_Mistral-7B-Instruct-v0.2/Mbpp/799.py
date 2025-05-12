"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""
def left_rotate(num, d):
    """
    :param num: int, 32 bit number
    :param d: int, number of bits to rotate left
    :return: int, the number with d bits rotated left
    """
    return (num << d) | (num >> (32 - d))

if __name__ == "__main__":
    assert left_rotate(16, 2) == 64
    assert left_rotate(1, 31) == 0
    assert left_rotate(1, 0) == 1
    assert left_rotate(1, 32) == 0
    assert left_rotate(1, -1) == 1
    assert left_rotate(1, -32) == 0
    assert left_rotate(1, 33) == 0
    assert left_rotate(1, 34) == 0
    assert left_rotate(1, 35) == 0
    assert left_rotate(1, 36) == 0
    assert left_rotate(1, 37) == 0
    assert left_rotate(1, 38) == 0
    assert left_rotate(1, 39) == 0
    assert left_rotate(1, 40) == 0
    assert left_rotate(1, 41) == 0
    assert left_rotate(1, 42) == 0
    assert left_rotate(1, 43) == 0
    assert left_rotate(1, 44) == 0
    assert left_rotate(1, 45) == 0
    assert left_rotate(1, 46) == 0
    assert left_rotate(1, 47) == 0
    assert left_rotate(1, 48) == 0
    assert left_rotate(1, 49) == 0
    assert left_rotate(1, 50) == 0
    assert left_rotate(1, 51) == 0
    assert left_rotate(1, 52) == 0
    assert left_rotate(1, 53) == 0
    assert left_rotate(1, 54) == 0
    assert left_rotate(1, 55) == 0
    assert left_rotate(1, 56) == 0
    assert left_rotate(1, 57) == 0
    assert left_rotate(1, 58) == 0
    assert left_rotate(1, 59) == 0
    assert left_rotate(1, 60) == 0
    assert left_rotate(1, 61) == 0
    assert left_rotate(1, 62) == 0
    assert left_rotate(1, 63) == 0
    assert left_rotate(1, 64) == 0
    assert left_rotate(1, 65) == 0
    assert left_rotate(1, 66) == 0
    assert left_rotate(1, 67) == 0
    assert left_rotate(1, 68) == 0
    assert left_rotate(1, 69) == 0
    assert left_rotate(1, 70) == 0
    assert left_rotate(1, 71) == 0
    assert left_rotate(1, 72) == 0
    assert left_rotate(1, 73) == 0
    assert left_rotate(1, 74) == 0
    assert left_rotate(1, 75) == 0
    assert left_rotate(1, 76) == 0
    assert left_rotate(1, 77) == 0
    assert left_rotate(1, 78) == 0
    assert left_rotate(1, 79) == 0
    assert left_rotate(1, 80) == 0
    assert left_rotate(1, 81) == 0
    assert left_rotate(1,