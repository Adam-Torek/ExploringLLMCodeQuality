"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def is_num_decagonal(n):
    return n * ((n * (n - 1)) // 2)

# Test cases
print(is_num_decagonal(3)) # Output: 27
print(is_num_decagonal(5)) # Output: 75
print(is_num_decagonal(10)) # Output: 750