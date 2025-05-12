def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    return min(l)


def sum_of_elements(l: list):
    """Return sum of all elements in the list.
    >>> sum_of_elements([1, 2, 3])
    6
    >>> sum_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    135
    """
    return sum(l)


def average_of_elements(l: list):
    """Return average of all elements in the list.
    >>> average_of_elements([1, 2, 3])
    2.0
    >>> average_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    11.0
    """
    return sum(l) / len(l)


def average_of_positive_elements(l: list):
    """Return average of all positive elements in the list.
    >>> average_of_positive_elements([1, 2, 3])
    2.0
    >>> average_of_positive_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    5.0
    """
    return sum(x for x in l if x > 0) / len(l)


def average_of_negative_elements(l: list):
    """Return average of all negative elements in the list.
    >>> average_of_negative_elements([1, 2, 3])
    0.0
    >>> average_of_negative_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -3.0
    """
    return sum(x for x in l if x < 0) / len(l)


def average_of_odd_elements(l: list):
    """Return average of all odd elements in the list.
    >>> average_of_odd_elements([1, 2, 3])
    2.0
    >>> average_of_odd_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    3.0
    """
    return sum(x for x in l if x % 2 != 0) / len(l)


def average_of_even_elements(l: list):
    """Return average of all even elements in the list.
    >>> average_of_even_elements([1, 2, 3])
    2.0
    >>> average_of_even_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    4.0
    """
    return sum(x for x in l if x % 2 == 0) / len(l)


def average_of_first_half_elements(l: list):
    """Return average of all elements in the first half of the list.
    >>> average_of_first_half_elements([1, 2, 3])
    2.0
    >>> average_of_first_half_elements([5, 3, -5, 2, -3, 3