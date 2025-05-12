"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""


def mul_even_odd(lst):
    """
    :param lst: list of numbers
    :return: product of first even and odd number
    """
    even = 1
    odd = 1
    for i in lst:
        if i % 2 == 0:
            even *= i
        else:
            odd *= i
    return even * odd


if __name__ == '__main__':
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14