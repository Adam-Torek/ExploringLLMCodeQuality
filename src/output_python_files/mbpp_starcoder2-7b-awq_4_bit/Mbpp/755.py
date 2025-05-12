"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(nums):
    """
    :param nums: list of numbers
    :return: second smallest number
    """
    # TODO: implement this function
    pass
/python/tests/test_second_smallest.py
import pytest

from python.second_smallest import second_smallest


def test_second_smallest():
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    assert second_smallest([1, 2, 3, 4, 5]) == 2
    assert second_smallest([1, 2, 3, 4, 5, 6]) == 3
    assert second_smallest([1, 2, 3, 4, 5, 6, 7]) == 4
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8]) == 5
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 8
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 9
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 10
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 11
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 12
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 13
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 14
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 15
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 16
    assert second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,