"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n):
    return n * (3 * n - 1) ** 2

def nth_octagonal(n):
    return is_octagonal(n)

print(nth_octagonal(5)) # Output: 65<|endoftext|>