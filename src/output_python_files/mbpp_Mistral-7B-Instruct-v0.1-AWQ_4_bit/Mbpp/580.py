"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

from typing import Tuple


def extract_even(tuple_: Tuple) -> Tuple:
    """
    Remove uneven elements in the nested mixed tuple.
    """
    return tuple(filter(lambda x: isinstance(x, tuple) and len(x) % 2 == 0, tuple_))