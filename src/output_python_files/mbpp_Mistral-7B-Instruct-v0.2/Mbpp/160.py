"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
from collections import defaultdict


def find_solution(a, b, n):
    if a == 0 and b == 0:
        if n == 0:
            return (0, 0)
        else:
            return None

    gcd = gcd_extended(a, b)

    if gcd > 1:
        x, y = find_solution(b // gcd, a // gcd, n // gcd)
        return (y, x)

    if a < 0 and n % a == 0:
        x = n // a
        y = -x
    else:
        x = (n % a + b // gcd) // b
        y = a // gcd

    return (x, y)


def gcd_extended(a, b):
    if b == 0:
        return a

    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0

    while b != 0:
        a, b = b, a % b
        x1, x2 = x2, x1 - x2 // b
        y1, y2 = y2, y1 - y2 // b

    return a, x1


if __name__ == "__main__":
    print(find_solution(2, 3, 7))
    print(find_solution(3, 4, 12))
    print(find_solution(1, 1, 1))
    print(find_solution(1, 1, 2))
    print(find_solution(1, 1, 0))
    print(find_solution(1, 1, -2))
    print(find_solution(1, 1, 1000000007))</s>