from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_data_structures/01_lists/01_list_basics/01_list_basics.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse([])
[]
"""


def reverse(numbers: list) -> list:
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([])
    []
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_data_structures/01_lists/02_list_comprehensions/01_list_comprehensions.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse([])
[]
"""


def reverse(numbers: list) -> list:
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([])
    []
    """
    return [number for number in reversed(numbers)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_data_structures/01_lists/03_list_comprehensions_with_conditions/01_list_comprehensions_with_conditions.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse([])
[]
"""


def reverse(numbers: list) -> list:
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([])
    []
    """
    return [number for number in reversed(numbers) if number % 2 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_data_structures/01_lists/04_list_comprehensions_with_conditions_and_loops/01_list_comprehensions_with_conditions_and_loops.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse([])
[]
"""


def reverse(numbers: list) -> list:
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([])
    []
    """
    return [number for number in reversed(numbers) if number % 2 == 0 for number in numbers if number > 2]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_data_structures/01_lists/05_list_comprehensions_with_conditions_and_loops_and_nested_loops/01_list_comprehensions_with_conditions_and_loops_and_nested_loops.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse([])
[]