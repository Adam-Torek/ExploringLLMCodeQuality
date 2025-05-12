"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""


def find_solution(a, b, n):
    """
    :param a: int
    :param b: int
    :param n: int
    :return: tuple
    """
    if a == 0:
        return None
    else:
        x = n // b
        y = n % b
        if x * a + y == n:
            return x, y
        else:
            return None


if __name__ == '__main__':
    print(find_solution(2, 3, 7))
    print(find_solution(2, 3, 10))
    print(find_solution(2, 3, 11))
    print(find_solution(2, 3, 12))
    print(find_solution(2, 3, 13))
    print(find_solution(2, 3, 14))
    print(find_solution(2, 3, 15))
    print(find_solution(2, 3, 16))
    print(find_solution(2, 3, 17))
    print(find_solution(2, 3, 18))
    print(find_solution(2, 3, 19))
    print(find_solution(2, 3, 20))
    print(find_solution(2, 3, 21))
    print(find_solution(2, 3, 22))
    print(find_solution(2, 3, 23))
    print(find_solution(2, 3, 24))
    print(find_solution(2, 3, 25))
    print(find_solution(2, 3, 26))
    print(find_solution(2, 3, 27))
    print(find_solution(2, 3, 28))
    print(find_solution(2, 3, 29))
    print(find_solution(2, 3, 30))
    print(find_solution(2, 3, 31))
    print(find_solution(2, 3, 32))
    print(find_solution(2, 3, 33))
    print(find_solution(2, 3, 34))
    print(find_solution(2, 3, 35))
    print(find_solution(2, 3, 36))
    print(find_solution(2, 3, 37))
    print(find_solution(2, 3, 38))
    print(find_solution(2, 3, 39))
    print(find_solution(2, 3, 40))
    print(find_solution(2, 3, 41))
    print(find_solution(2, 3, 42))
    print(find_solution(2, 3, 43))
    print(find_solution(2, 3, 44))
    print(find_solution(2, 3, 45))
    print(find_solution(2, 3, 46))
    print(find_solution(2, 3, 47))
    print(find_solution(2, 3, 48))
    print(find_solution(2, 3, 49))
    print(find_solution(2, 3, 50))
    print(find_solution(2, 3, 51))
    print(find_solution(2, 3, 52))
    print(find_solution(2, 3, 53))
    print(find_solution(2, 3, 54