"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
import math

def is_num_decagonal(n):
    """
    Check if n is a decagonal number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    decagon = 10
    p = 0
    q = 1
    while True:
        test = decagon * (p + q) + q
        if test == n:
            return True
        p, q = q, p + q
    return False

def decagonal_number(n):
    """
    Find the nth decagonal number
    """
    if not is_num_decagonal(n):
        raise ValueError("n is not a decagonal number")
    decagon = 10
    p = 0
    q = 1
    while n > decagon * (p + q):
        p, q = q, p + q
    return decagon * (p + q)

if __name__ == "__main__":
    assert is_num_decagonal(3) == True
    assert is_num_decagonal(4) == False
    assert decagonal_number(3) == 27
    assert decagonal_number(10) == 101
    assert decagonal_number(100) == 9901
    assert decagonal_number(1000) == 999001
    assert decagonal_number(10000) == 99990001
    assert decagonal_number(100000) == 9999900001
    assert decagonal_number(1000000) == 999999000001
    assert decagonal_number(10000000) == 99999990000001
    assert decagonal_number(100000000) == 9999999900000001
    assert decagonal_number(1000000000) == 999999999000000001
    assert decagonal_number(10000000000) == 9999999999000000001
    assert decagonal_number(100000000000) == 99999999999000000001
    assert decagonal_number(1000000000000) == 999999999999000000001
    assert decagonal_number(10000000000000) == 9999999999999000000001
    assert decagonal_number(100000000000000) == 99999999999999000000001
    assert decagonal_number(1000000000000000) == 999999999999999000000001
    assert decagonal_number(10000000000000000) == 9999999999999999000000001
    assert decagonal_number(100000000000000000) == 99999999999999999000000001
    assert decagonal_number(1000000000000000000) == 999999999999999999000000001
    assert decagonal_number(10000000000000000000) ==