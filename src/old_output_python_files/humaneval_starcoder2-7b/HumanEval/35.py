def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """

def sum_of_elements(l: list):
    """Return sum of all elements in the list.
    >>> sum_of_elements([1, 2, 3])
    6
    >>> sum_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    105
    """

def average_of_elements(l: list):
    """Return average of all elements in the list.
    >>> average_of_elements([1, 2, 3])
    2.0
    >>> average_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    10.5
    """

def count_of_elements(l: list):
    """Return number of elements in the list.
    >>> count_of_elements([1, 2, 3])
    3
    >>> count_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    11
    """

def count_of_elements_greater_than(l: list, n: int):
    """Return number of elements in the list greater than n.
    >>> count_of_elements_greater_than([1, 2, 3], 1)
    2
    >>> count_of_elements_greater_than([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10)
    1
    """

def count_of_elements_less_than(l: list, n: int):
    """Return number of elements in the list less than n.
    >>> count_of_elements_less_than([1, 2, 3], 1)
    0
    >>> count_of_elements_less_than([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10)
    2
    """

def count_of_elements_equal_to(l: list, n: int):
    """Return number of elements in the list equal to n.
    >>> count_of_elements_equal_to([1, 2, 3], 1)
    1
    >>> count_of_elements_equal_to([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10)
    0
    """

def count_of_elements_greater_than_or_equal_to(l: list, n: int):
    """Return number of elements in the list greater than or equal to n.
    >>> count_of_elements_greater_than_or_equal_to([1, 2, 3], 1)
    2
    >>> count_of_elements_greater_than_or_equal_to([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10)
    3
    """

def count_of_elements_less_than_or_equal_to(l: list, n: int):
    """Return number of elements in the list less than or equal to n.
    >>> count_of_elements_less_than_or_equal_to([1, 2, 3], 1)
    1
    >>> count_of_elements_less_than_or_equal_to([5, 3, -5, 2, -3,