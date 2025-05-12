"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
from itertools import combinations

def combinations_colors(input_list, n):
    """
    :param input_list: list of strings
    :param n: int
    :return: list of tuples
    """
    return list(combinations(input_list, n))