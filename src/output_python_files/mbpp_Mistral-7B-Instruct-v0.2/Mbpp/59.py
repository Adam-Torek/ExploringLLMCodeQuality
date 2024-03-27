"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
import math

def is_octagonal(n):
    """
    Check if n is an octagonal number
    """
    a = int(math.sqrt(1 + 8 * math.sqrt(n)))
    b = int(math.sqrt(1 + 8 * math.sqrt(n + 8)))
    return a == b

def nth_octagonal_number(n):
    """
    Find the nth octagonal number
    """
    i = 1
    while not is_octagonal(i):
        i += 1
    return i + (n - 1) // 2

if __name__ == "__main__":
    n = 5
    print(nth_octagonal_number(n))
    assert is_octagonal(n)
    assert nth_octagonal_number(n) == 65</s>