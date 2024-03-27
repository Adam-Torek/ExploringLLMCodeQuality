"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""

def hexagonal_num(n):
    return (n * (3 * n - 1)) // 2

# Test the function
assert hexagonal_num(10) == 190<|endoftext|>