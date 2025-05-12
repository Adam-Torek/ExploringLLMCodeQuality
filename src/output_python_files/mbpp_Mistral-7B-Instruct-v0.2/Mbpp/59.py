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
    if not is_octagonal(n):
        raise ValueError("n must be an octagonal number")
    a = int(math.sqrt(1 + 8 * math.sqrt(n)))
    return a * (a + 2) // 2

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"{i}: {nth_octagonal_number(i)}")