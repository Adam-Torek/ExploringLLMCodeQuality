"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
import math

def is_nonagonal(n):
    """
    Check if n is a nonagonal number
    """
    side_length = 3 * math.sqrt(3) * (2 * n - 1)
    return all(side_length % i != 0 for i in range(2, int(math.sqrt(side_length) + 1)) )

def nonagonal_number(n):
    """
    Find the nth nonagonal number
    """
    if not is_nonagonal(n):
        raise ValueError("n must be a nonagonal number")

    side_length = 3 * math.sqrt(3) * (2 * n - 1)
    return int(side_length * (n - 1) / 2 + (side_length / 2) * math.sin(math.pi / 5) + (side_length / 2))

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Nonagonal number {i} is {nonagonal_number(i)}")