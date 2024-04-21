from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
<file_sep>/src/01_basics/01_basics.py
"""
Basics
"""

# 1. Write a function that takes a list of numbers and returns the sum of the numbers.
#    The function should return 0 if the list is empty.
#    >>> sum_list([1, 2, 3])
#    6
#    >>> sum_list([])
#    0

def sum_list(numbers: list) -> int:
    """ Sum list of numbers
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([])
    0
    """

# 2. Write a function that takes a list of numbers and returns the average of the numbers.
#    The function should return 0 if the list is empty.
#    >>> average_list([1, 2, 3])
#    2.0
#    >>> average_list([])
#    0

def average_list(numbers: list) -> float:
    """ Average list of numbers
    >>> average_list([1, 2, 3])
    2.0
    >>> average_list([])
    0
    """

# 3. Write a function that takes a list of numbers and returns the smallest number in the list.
#    The function should return 0 if the list is empty.
#    >>> smallest_number([1, 2, 3])
#    1
#    >>> smallest_number([])
#    0

def smallest_number(numbers: list) -> int:
    """ Smallest number in list
    >>> smallest_number([1, 2, 3])
    1
    >>> smallest_number([])
    0
    """

# 4. Write a function that takes a list of numbers and returns the largest number in the list.
#    The function should return 0 if the list is empty.
#    >>> largest_number([1, 2, 3])
#    3
#    >>> largest_number([])
#    0

def largest_number(numbers: list) -> int:
    """ Largest number in list
    >>> largest_number([1, 2, 3])
    3
    >>> largest_number([])
    0
    """

# 5. Write a function that takes a list of numbers and returns the second largest number in the list.
#    The function should return 0 if the list is empty.
#    >>> second_largest_number([1, 2, 3])
#    2
#    >>> second_largest_number([])
#    0

def second_largest_number(numbers: list) -> int:
    """ Second largest number in list
    >>> second_largest_number([1, 2, 3])
    2
    >>> second_largest_number([])
    0
    """

# 6. Write a function that takes a list of numbers and returns the second smallest number in the list.
#    The function should return 0 if the list is empty.
#    >>> second_smallest_number([1, 2, 3])
#    2
#    >>> second_smallest_number([])
#    0

def second_smallest_number(numbers: list) -> int:
    """ Second smallest number in list
    >>> second_smallest_number([1, 2, 3])
    2
    >>> second_smallest_number([])
    0
    """

# 7. Write a function that takes a list of numbers and returns the number of even numbers in the list.
#    The function should return 0 if the list is empty.
#    >>> count_even_numbers([1, 2, 3])
#    1
#    >>> count_even_numbers([])
#    0

def count_even_numbers(numbers: list) -> int:
    """ Count even numbers in list
    >>> count_even_numbers([1, 2, 3])
    1
    >>> count_even_numbers([])
    0
    """

# 8. Write a function that takes a list of numbers and returns the number of odd numbers in the list.
#    The function should return 0 if the list is empty.
#    >>> count_odd_numbers([1, 2, 3])
#    2
#    >>> count_odd_numbers([])
#    0

def count_odd_