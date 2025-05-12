"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""


def is_product_even(numbers):
    """
    >>> is_product_even([1,2,3])
    False
    >>> is_product_even([1,2,4])
    True
    >>> is_product_even([1,2,3,4])
    True
    >>> is_product_even([1,2,3,4,5])
    False
    """
    return all(x % 2 == 0 for x in numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()