"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""


def is_product_even(numbers):
    """
    Check whether the product of numbers in a list is even or not.
    :param numbers: list of numbers
    :return: True if the product of numbers in a list is even, False otherwise
    """
    return all(map(lambda x: x % 2 == 0, numbers))


if __name__ == '__main__':
    print(is_product_even([1, 2, 3]))
    print(is_product_even([1, 2, 3, 4]))
    print(is_product_even([1, 2, 3, 4, 5]))
    print(is_product_even([1, 2, 3, 4, 5, 6]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(is_product_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1