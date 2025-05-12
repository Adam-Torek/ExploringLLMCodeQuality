def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -3, -10]
    """
    return [num for num in l if num < 0]


def get_zero(l: list):
    """Return only zeros in the list.
    >>> get_zero([-1, 2, -4, 5, 6])
    []
    >>> get_zero([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [0]
    """
    return [num for num in l if num == 0]


def get_sum(numbers: list):
    """Return the sum of all numbers in the list.
    >>> get_sum([1, 2, 3, 4, 5])
    15
    >>> get_sum([-1, 2, -4, 5, 6])
    2
    >>> get_sum([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    136
    """
    return sum(numbers)


def get_product(numbers: list):
    """Return the product of all numbers in the list.
    >>> get_product([1, 2, 3, 4, 5])
    120
    >>> get_product([-1, 2, -4, 5, 6])
    -120
    >>> get_product([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    0
    """
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return reduce(lambda x, y: x * y, numbers)


def get_min(numbers: list):
    """Return the smallest number in the list.
    >>> get_min([1, 2, 3, 4, 5])
    1
    >>> get_min([-1, 2, -4, 5, 6])
    -4
    >>> get_min([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    return min(numbers)


def get_max(numbers: list):
    """Return the largest number in the list.
    >>> get_max([1, 2, 3, 4, 5])
    5
    >>> get_max([-1, 2, -4, 5, 6])
    5
    >>> get_max([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(numbers)


def get_average(numbers: list):
    """Return the average of all numbers in the list.
    >>> get_average([1, 2, 3, 4, 5])
    3
    >>> get_