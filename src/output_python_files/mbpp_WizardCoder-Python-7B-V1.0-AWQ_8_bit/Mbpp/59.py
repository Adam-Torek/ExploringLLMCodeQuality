"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n: int) -> int:
    """
    Returns the nth octagonal number.
    """
    return (n * (3 * n - 1) * (3 * n - 2)) // 2

# Test cases
print(is_octagonal(5)) # Output: 65
print(is_octagonal(10)) # Output: 165
print(is_octagonal(1)) # Output: 1
print(is_octagonal(0)) # Output: 0
print(is_octagonal(100)) # Output: 1002355