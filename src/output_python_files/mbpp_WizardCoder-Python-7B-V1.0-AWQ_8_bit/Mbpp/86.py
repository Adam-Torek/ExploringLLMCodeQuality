"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    return (n * (n * n + 1)) // 3

print(centered_hexagonal_nomber(10))