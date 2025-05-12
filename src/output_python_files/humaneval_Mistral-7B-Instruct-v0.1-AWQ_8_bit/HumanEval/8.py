from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    else:
        sum_numbers = sum(numbers)
        product_numbers = 1
        for number in numbers:
            product_numbers *= number
        return (sum_numbers, product_numbers)


def sum_product_test(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product_test([])
    (0, 1)
    >>> sum_product_test([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    else:
        sum_numbers = sum(numbers)
        product_numbers = 1
        for number in numbers:
            product_numbers *= number
        return (sum_numbers, product_numbers)


if __name__ == '__main__':
    print(sum_product([1, 2, 3, 4]))
    print(sum_product_test([1, 2, 3, 4]))