"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""


def diff_even_odd(lst):
    """
    :param lst: list of integers
    :return: difference of the first even and first odd number of a given list
    """
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even = i
        else:
            odd = i
    return even - odd


if __name__ == '__main__':
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]))
    print(diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8, 10, 12,