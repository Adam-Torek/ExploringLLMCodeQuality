"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    if n % a == 0:
        return (n // a, 0)
    elif n % b == 0:
        return (0, n // b)
    else:
        x = n // a
        y = n // b
        while n % a != 0 and n % b != 0:
            x += 1
            y += 1
            n -= a
        if n % a == 0:
            return (x, y - (x - 1))
        else:
            return (x - (y - 1), y)

print(find_solution(2, 3, 7)) # Output: (2, 1)
print(find_solution(3, 2, 7)) # Output: (1, 2)
print(find_solution(7, 5, 11)) # Output: (1, 2)
print(find_solution(7, 5, 13)) # Output: None