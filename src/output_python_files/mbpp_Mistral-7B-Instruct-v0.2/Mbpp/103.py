"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

from math import gcd


def eulerian_num(n, m):
    """
    :param n: number of vertices
    :param m: number of edges
    :return: Eulerian number a(n, m)
    """
    if n % 2 == 0 or m % 2 == 0:
        return 0

    if n == 2 and m == 1:
        return 1

    if n - m == 2:
        return eulerian_num(n - 2, m - 2)

    return eulerian_num(n, m - 1) + eulerian_num(n - 1, m)


if __name__ == "__main__":
    n = 3
    m = 1
    print(eulerian_num(n, m))
    assert eulerian_num(3, 1) == 4

    n = 5
    m = 4
    print(eulerian_num(n, m))
    assert eulerian_num(5, 4) == 14

    n = 10
    m = 6
    print(eulerian_num(n, m))
    assert eulerian_num(10, 6) == 120

    n = 12
    m = 11
    print(eulerian_num(n, m))
    assert eulerian_num(12, 11) == 120

    n = 15
    m = 10
    print(eulerian_num(n, m))
    assert eulerian_num(15, 10) == 360

    n = 100
    m = 50
    print(eulerian_num(n, m))
    assert eulerian_num(100, 50) == 1047293360000

    n = 100
    m = 51
    print(eulerian_num(n, m))
    assert eulerian_num(100, 51) == 0

    n = 100
    m = 101
    print(eulerian_num(n, m))
    assert eulerian_num(100, 101) == 0

    n = 1000
    m = 500
    print(eulerian_num(n, m))
    assert eulerian_num(1000, 500) == 1157920892370175200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000