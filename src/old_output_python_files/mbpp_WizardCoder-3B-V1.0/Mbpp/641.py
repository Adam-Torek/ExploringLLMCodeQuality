"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""

def is_nonagonal(n):
    """
    Returns the nth nonagonal number.
    """
    return (n * (n + 1)) // 2

# Test the function
assert is_nonagonal(10) == 325<|endoftext|>