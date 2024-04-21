"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    return (n * (3 * n - 1)) // 2

# Test the function
assert centered_hexagonal_number(10) == 271<|endoftext|>