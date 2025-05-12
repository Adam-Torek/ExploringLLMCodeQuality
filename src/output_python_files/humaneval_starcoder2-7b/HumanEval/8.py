from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
/02_lists/01_list_basics/01_list_basics.py
"""
List basics
"""

from typing import List


def list_basics(numbers: List[int]) -> List[int]:
    """
    Given a list of integers, return a list with the same elements in reverse order.
    >>> list_basics([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> list_basics([1, 2, 3])
    [3, 2, 1]
    """
/02_lists/03_list_manipulation/01_list_manipulation.py
"""
List manipulation
"""

from typing import List


def list_manipulation(numbers: List[int], command: str, location: str, value: int) -> List[int]:
    """
    Given a list of integers, perform a command on the list.
    >>> list_manipulation([1, 2, 3], "remove", "end", 10)
    [1, 2, 3, 10]
    >>> list_manipulation([1, 2, 3, 4], "remove", "beginning", 20)
    [3, 4, 20]
    >>> list_manipulation([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation([1, 2, 3], "add", "end", 30)
    [1, 2, 3, 30]
    """
/02_lists/02_list_manipulation_2/01_list_manipulation_2.py
"""
List manipulation 2
"""

from typing import List


def list_manipulation_2(numbers: List[int], command: str, location: str, value: int) -> List[int]:
    """
    Given a list of integers, perform a command on the list.
    >>> list_manipulation_2([1, 2, 3], "remove", "end", 10)
    [1, 2, 3, 10]
    >>> list_manipulation_2([1, 2, 3, 4], "remove", "beginning", 20)
    [3, 4, 20]
    >>> list_manipulation_2([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation_2([1, 2, 3], "add", "end", 30)
    [1, 2, 3, 30]
    """
/02_lists/04_list_manipulation_3/01_list_manipulation_3.py
"""
List manipulation 3
"""

from typing import List


def list_manipulation_3(numbers: List[int], command: str, location: str, value: int) -> List[int]:
    """
    Given a list of integers, perform a command on the list.
    >>> list_manipulation_3([1, 2, 3], "remove", "end", 10)
    [1, 2, 3, 10]
    >>> list_manipulation_3([1, 2, 3, 4], "remove", "beginning", 20)
    [3, 4, 20]
    >>> list_manipulation_3([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]
    >>> list_manipulation_3([1, 2, 3], "add", "end", 30)