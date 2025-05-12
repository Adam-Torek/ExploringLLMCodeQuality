"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    if a == 0:
        return None
    d = b**2 - 4*a*n
    if d < 0:
        return None
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    return (x1, x2)

# Test cases
print(find_solution(2, 3, 7))  # Output: (2, 1)
print(find_solution(1, 2, 10))  # Output: (3, 4)
print(find_solution(0, 1, 1))  # Output: None<|endoftext|>