"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""
import math

def is_perfect_square(n):
    """
    :param n: int
    :return: bool
    """
    return math.isqrt(n) * math.isqrt(n) == n

if __name__ == "__main__":
    assert is_perfect_square(16)
    assert not is_perfect_square(10)
    assert is_perfect_square(25)
    assert not is_perfect_square(17)
    assert is_perfect_square(36)
    assert not is_perfect_square(19)
    assert is_perfect_square(49)
    assert not is_perfect_square(20)
    assert is_perfect_square(64)
    assert not is_perfect_square(21)
    assert is_perfect_square(81)
    assert not is_perfect_square(22)
    assert is_perfect_square(121)
    assert not is_perfect_square(23)
    assert is_perfect_square(144)
    assert not is_perfect_square(24)
    assert is_perfect_square(169)
    assert not is_perfect_square(25)
    assert is_perfect_square(289)
    assert not is_perfect_square(27)
    assert is_perfect_square(361)
    assert not is_perfect_square(32)
    assert is_perfect_square(441)
    assert not is_perfect_square(33)
    assert is_perfect_square(529)
    assert not is_perfect_square(34)
    assert is_perfect_square(625)
    assert not is_perfect_square(35)
    assert is_perfect_square(729)
    assert not is_perfect_square(36)
    assert is_perfect_square(841)
    assert not is_perfect_square(37)
    assert is_perfect_square(961)
    assert not is_perfect_square(38)
    assert is_perfect_square(1089)
    assert not is_perfect_square(39)
    assert is_perfect_square(1225)
    assert not is_perfect_square(40)
    assert is_perfect_square(1369)
    assert not is_perfect_square(41)
    assert is_perfect_square(15625)
    assert not is_perfect_square(42)
    assert is_perfect_square(16801)
    assert not is_perfect_square(43)
    assert is_perfect_square(1849)
    assert not is_perfect_square(44)
    assert is_perfect_square(2025)
    assert not is_perfect_square(45)
    assert is_perfect_square(216241)
    assert not is_perfect_square(46)
    assert is_perfect_square(2304961)
    assert not is_perfect_square(47)
    assert is_perfect_square(2621441)
    assert not is_perfect_square(48)
    assert is_perfect_square(2896001)
    assert not is_perfect_square(49)
    assert is_perfect_square(33550625)
    assert not is_perfect_square(50)
    assert is_perfect_square(36028801)
    assert not is_perfect_square(51)
    assert is_perfect_square(39321616)
    assert not