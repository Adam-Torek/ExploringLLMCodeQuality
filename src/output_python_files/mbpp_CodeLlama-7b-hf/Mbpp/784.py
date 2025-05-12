"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""


def mul_even_odd(lst):
    """
    :param lst: list
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
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15