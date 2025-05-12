"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def is_num_decagonal(n):
    if n < 1:
        return False
    return (n * (3 * n - 1)) // 2

print(is_num_decagonal(3)) # Output: 27<|endoftext|>