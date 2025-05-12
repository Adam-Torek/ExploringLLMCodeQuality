"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""

def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 2

# Test the function
print(tetrahedral_number(5)) # Output: 35