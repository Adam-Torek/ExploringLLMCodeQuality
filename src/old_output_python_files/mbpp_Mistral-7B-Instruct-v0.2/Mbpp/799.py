"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""
def left_rotate(num, d):
    """
    :param num: int, 32 bit number
    :param d: int, number of bits to rotate left
    :return: int, number with d bits rotated left
    """
    return (num << d) | (num >> (32 - d))

if __name__ == "__main__":
    assert left_rotate(16, 2) == 64
    assert left_rotate(1, 31) == 0
    assert left_rotate(1, 0) == 1
    assert left_rotate(1, 32) == 0
    assert left_rotate(1, -1) == 1
    assert left_rotate(1, -32) == 0
    assert left_rotate(0b1111_0000_0011_1111, 1) == 0b1111_0000_0011_1100
    assert left_rotate(0b1111_0000_0011_1111, 31) == 0b0000_1111_1100_0011
    assert left_rotate(0b1111_0000_0011_1111, 32) == 0b1111_0000_0011_1111
    assert left_rotate(0b1111_0000_0011_1111, -1) == 0b1111_0000_0011_1111
    assert left_rotate(0b1111_0000_0011_1111, -32) == 0b1111_0000_0011_1111
    assert left_rotate(0b1111_0000_0011_1111, -33) == 0b1111_0000_0011_1111
    assert left_rotate(0b1111_0000_0011_1111, 33) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 34) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 35) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 36) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 37) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 38) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 39) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 40) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 41) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 42) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 43) == AssertionError
    assert left_rotate(0b1111_0000_0011_1111, 44) == AssertionError
    assert left_rotate(0b1111_000