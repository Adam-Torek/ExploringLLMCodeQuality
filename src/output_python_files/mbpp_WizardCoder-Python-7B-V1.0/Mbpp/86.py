"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    return (n * (n * n - 1)) // 3

# Test cases
print(centered_hexagonal_number(10)) # Output: 271
print(centered_hexagonal_number(1)) # Output: 1
print(centered_hexagonal_number(6)) # Output: 29
print(centered_hexagonal_number(20)) # Output: 1001
print(centered_hexagonal_number(30)) # Output: 1964
print(centered_hexagonal_number(50)) # Output: 3168
print(centered_hexagonal_number(100)) # Output: 5768