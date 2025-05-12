from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
/python/exercises/lists/lists.py
from typing import List


def first(xs: List[int]) -> int:
    """ Return the first element of the list.
    >>> first([1, 2, 3])
    1
    >>> first([1])
    1
    """


def last(xs: List[int]) -> int:
    """ Return the last element of the list.
    >>> last([1, 2, 3])
    3
    >>> last([1])
    1
    """


def rest(xs: List[int]) -> List[int]:
    """ Return the list without the first element.
    >>> rest([1, 2, 3])
    [2, 3]
    >>> rest([1])
    []
    """


def reverse(xs: List[int]) -> List[int]:
    """ Return the list in reverse order.
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse([1])
    [1]
    """


def append(xs: List[int], ys: List[int]) -> List[int]:
    """ Return the list with the elements of ys appended to the end of xs.
    >>> append([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> append([1], [2])
    [1, 2]
    """


def concat(xs: List[List[int]]) -> List[int]:
    """ Return the list of all the elements of the lists in xs.
    >>> concat([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    >>> concat([[1], [2]])
    [1, 2]
    """


def length(xs: List[int]) -> int:
    """ Return the number of elements in the list.
    >>> length([1, 2, 3])
    3
    >>> length([1])
    1
    """


def empty(xs: List[int]) -> bool:
    """ Return True if the list is empty, False otherwise.
    >>> empty([1, 2, 3])
    False
    >>> empty([1])
    False
    >>> empty([])
    True
    """


def index(xs: List[int], i: int) -> int:
    """ Return the element at position i in the list.
    >>> index([1, 2, 3], 0)
    1
    >>> index([1, 2, 3], 1)
    2
    >>> index([1, 2, 3], 2)
    3
    """


def set_index(xs: List[int], i: int, x: int) -> List[int]:
    """ Return the list with the element at position i replaced with x.
    >>> set_index([1, 2, 3], 0, 4)
    [4, 2, 3]
    >>> set_index([1, 2, 3], 1, 4)
    [1, 4, 3]
    >>> set_index([1, 2, 3], 2, 4)
    [1, 2, 4]
    """


def delete_index(xs: List[int], i: int) -> List[int]:
    """ Return the list with the element at position i removed.
    >>> delete_index([1, 2, 3], 0)
    [2, 3]
    >>> delete_index([1, 2, 3], 1)
    [1, 3]
    >>> delete_index([1, 2, 3], 2)
    [1, 2]
    """


def delete(xs: List[int], x: int) -> List[int]:
    """ Return the list with all occurrences of x removed.
    >>> delete([1, 2, 3, 1, 2, 3], 1)
    [2, 3, 2, 3]
    >>> delete([1, 2, 3, 1, 2, 3], 2)
    [1, 3, 1,