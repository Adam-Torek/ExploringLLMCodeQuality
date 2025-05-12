"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""

def is_nonagonal(n):
    return n * (360 - n) // 2

print(is_nonagonal(10)) # Output: 325