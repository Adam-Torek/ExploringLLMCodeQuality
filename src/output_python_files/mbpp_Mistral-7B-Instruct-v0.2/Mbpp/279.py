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
    p = 1
    q = 1
    while True:
        p += decagon
        q += 10
        if abs(p - n) < abs(p - q):
            return p

def decagonal_number(n):
    """
    Find the nth decagonal number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    decagon = 10
    p = 1
    q = 1
    while True:
        p += decagon
        q += decagon
        if q == n:
            return p - decagon

if __name__ == "__main__":
    assert is_num_decagonal(3) == 27
    assert decagonal_number(3) == 27
    assert is_num_decagonal(10) == 62
    assert decagonal_number(10) == 62
    assert is_num_decagonal(100) == 100953
    assert decagonal_number(100) == 100953
    assert is_num_decagonal(1000) == 104723852
    assert decagonal_number(1000) == 104723852
    assert is_num_decagonal(10000) == 10514088320
    assert decagonal_number(10000) == 10514088320
    assert is_num_decagonal(100000) == 1059612184000
    assert decagonal_number(100000) == 1059612184000
    assert is_num_decagonal(1000000) == 106849340160000
    assert decagonal_number(1000000) == 106849340160000
    assert is_num_decagonal(10000000) == 10779661920160000
    assert decagonal_number(10000000) == 10779661920160000
    assert is_num_decagonal(100000000) == 1087498787201600000
    assert decagonal_number(100000000) == 1087498787201600000
    assert is_num_decagonal(1000000000) == 10970368422016000000
    assert decagonal_number(1000000000) == 10970368422016000000
    assert is_num_decagonal(10000000000) == 110657756620160000000
    assert decagonal_number(10000000000) == 110657756620160000000
    assert is_num_decagonal(10000