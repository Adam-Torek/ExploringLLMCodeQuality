"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    x, y = 0, 1
    while x * a + y * b != n:
        x += 1
        y -= 1
    return x, y

# Test the function
assert find_solution(2, 3, 7) == (2, 1)
assert find_solution(2, 3, 5) is None
assert find_solution(3, 4, 12) == (2, 3)
assert find_solution(1, 1, 1) == (1, 1)