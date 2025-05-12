from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
/python/exercises/lists/list_manipulation.py
from typing import List


def list_manipulation(lst: List[int], command: str, location: str, *args) -> List[int]:
    """
    >>> list_manipulation([1, 2, 3], "remove", "end", 1)
    [1, 2]
    >>> list_manipulation([1, 2, 3], "remove", "beginning", 2)
    [2, 3]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "end", 30)
    [1, 2, 3, 30]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 10, 20)
    [10, 20, 1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "end", 10, 20)
    [1, 2, 3, 10, 20]
    >>> list_manipulation([1, 2, 3], "remove", "beginning", 2)
    [3]
    >>> list_manipulation([1, 2, 3], "remove", "end", 2)
    [1, 2]
    >>> list_manipulation([1, 2, 3], "remove", "beginning", 10)
    [1, 2, 3]
    >>> list_manipulation([1, 2, 3], "remove", "end", 10)
    [1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 10, 20, 30, 40)
    [10, 20, 30, 40, 1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "end", 10, 20, 30, 40)
    [1, 2, 3, 10, 20, 30, 40]
    >>> list_manipulation([1, 2, 3], "remove", "beginning", 10, 20, 30, 40)
    [1, 2, 3]
    >>> list_manipulation([1, 2, 3], "remove", "end", 10, 20, 30, 40)
    [1, 2, 3]
    """
/python/exercises/lists/list_manipulation_2.py
from typing import List


def list_manipulation(lst: List[int], command: str, location: str, *args) -> List[int]:
    """
    >>> list_manipulation([1, 2, 3], "remove", "end", 1)
    [1, 2]
    >>> list_manipulation([1, 2, 3], "remove", "beginning", 2)
    [2, 3]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "end", 30)
    [1, 2, 3, 30]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 10, 20)
    [10, 20, 1, 2,