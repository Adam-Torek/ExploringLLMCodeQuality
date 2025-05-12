"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""


def pair_xor_Sum(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: sum of xor of all pairs of numbers in the given list
    """
    return sum(x^y for x, y in zip(arr, arr[1:]))


if __name__ == '__main__':
    print(pair_xor_Sum([5, 9, 7, 6], 4))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 16))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 18))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 21))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 24))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 26))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 27))
    print(pair_xor_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 28))
    print(