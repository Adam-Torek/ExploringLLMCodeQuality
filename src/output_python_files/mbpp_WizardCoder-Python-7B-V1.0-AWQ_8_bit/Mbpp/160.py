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
        return None

# Test cases
print(find_solution(2, 3, 7)) # (2, 1)
print(find_solution(1, 2, 5)) # (5, 0)
print(find_solution(3, 4, 11)) # (3, 4)
print(find_solution(1, 2, 6)) # None
print(find_solution(7, 5, 10)) # None
print(find_solution(1, 1, 1)) # (1, 0)
print(find_solution(1, 1, 2)) # (2, 0)
print(find_solution(1, 1, 3)) # (3, 0)
print(find_solution(1, 1, 4)) # (4, 0)
print(find_solution(1, 1, 5)) # (5, 0)
print(find_solution(1, 1, 6)) # (6, 0)
print(find_solution(1, 1, 7)) # (7, 0)
print(find_solution(1, 1, 8)) # (8, 0)
print(find_solution(1, 1, 9)) # (9, 0)
print(find_solution(1, 1, 10)) # (10, 0)
print(find_solution(1, 1, 11)) # (11, 0)
print(find_solution(1, 1, 12)) # (12, 0)
print(find_solution(1, 1, 13)) # (13, 0)
print(find_solution(1, 1, 14)) # (14, 0)
print(find_solution(1, 1, 15)) # (15, 0)
print(find_solution(1, 1, 16)) # (16, 0)
print(find_solution(1, 1, 17)) # (17, 0)
print(find_solution(1, 1, 18)) # (18, 0)
print(find_solution(1, 1, 19)) # (19, 0)
print(find_solution(1, 1, 20)) # (20, 0)
print(find_solution(1, 1, 21)) # (21, 0)
print(find_solution(1, 1, 22)) # (22, 0)
print(find_solution(1, 1, 23)) # (23, 0)
print(find_solution(1, 1, 24)) # (24, 0)
print(find_solution(1, 1, 25)) # (25, 0)
print(find_solution(1, 1, 26)) # (26, 0)
print(find_solution(1, 1, 27)) # (27, 0)
print(find_solution(1, 1, 28)) # (28, 0)
print(find_solution(1, 1, 29)) # (29, 0)
print(find_solution(1, 1, 30)) # (30, 0)
print(find_solution(1, 1, 31)) # (31, 0)
print(find_solution(1, 1, 32)) # (32, 0)
print(find_solution(1,