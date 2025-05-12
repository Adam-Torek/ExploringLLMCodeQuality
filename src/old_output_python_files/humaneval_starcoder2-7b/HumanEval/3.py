from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
<file_sep>/python/tests/test_002_list_of_lists.py
from python.exercises.002_list_of_lists import list_of_lists


def test_list_of_lists():
    assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
<file_sep>/python/tests/test_001_sum_of_numbers.py
from python.exercises.001_sum_of_numbers import sum_of_numbers


def test_sum_of_numbers():
    assert sum_of_numbers([1, 2, 3]) == 6
    assert sum_of_numbers([1, 2, 3]) == 6
<file_sep>/python/exercises/002_list_of_lists.py
from typing import List


def list_of_lists(list_of_lists: List[List[int]]) -> List[int]:
    """ Given a list of lists, return a list of all the numbers in the list.
    >>> list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
<file_sep>/python/exercises/001_sum_of_numbers.py
from typing import List


def sum_of_numbers(numbers: List[int]) -> int:
    """ Given a list of numbers, return the sum of all the numbers.
    >>> sum_of_numbers([1, 2, 3])
    6
    """
<file_sep>/python/tests/test_003_below_zero.py
from python.exercises.003_below_zero import below_zero


def test_below_zero():
    assert below_zero([1, 2, 3]) is False
    assert below_zero([1, 2, -4, 5]) is True
<|endoftext|>