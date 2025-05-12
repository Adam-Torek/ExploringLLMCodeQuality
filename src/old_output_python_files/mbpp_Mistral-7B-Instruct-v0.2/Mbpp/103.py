"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
from math import gcd


def eulerian_num(n, m):
    if n % 2 == 0 or m % 2 == 0:
        return 0
    elif n == m:
        return 1
    else:
        return eulerian_num(n, m % n) + eulerian_num(n, m // gcd(n, m))


if __name__ == "__main__":
    n, m = 3, 1
    assert eulerian_num(n, m) == 4
    print(eulerian_num(n, m))