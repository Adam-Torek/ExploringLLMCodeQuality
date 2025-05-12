"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""


def median_numbers(a, b, c):
    """
    :param a: int
    :param b: int
    :param c: int
    :return: float
    """
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a == b:
        return a
    if a == c:
        return a
    if b == c:
        return b
    return (a + b) / 2


if __name__ == '__main__':
    print(median_numbers(25, 55, 65))
    print(median_numbers(1, 2, 3))
    print(median_numbers(1, 2, 3, 4))
    print(median_numbers(1, 2, 3, 4, 5))
    print(median_numbers(1, 2, 3, 4, 5, 6))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,