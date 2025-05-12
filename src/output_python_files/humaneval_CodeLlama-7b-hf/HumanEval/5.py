from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)


def intersperse_with_list(numbers: List[int], delimeter: List[int]) -> List[int]:
    """ Insert a list 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_list([], [4])
    []
    >>> intersperse_with_list([1, 2, 3], [4])
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + delimeter + intersperse(numbers[1:], delimeter)


def intersperse_with_string(numbers: List[int], delimeter: str) -> List[int]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_string([], '4')
    []
    >>> intersperse_with_string([1, 2, 3], '4')
    [1, '4', 2, '4', 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)


def intersperse_with_tuple(numbers: List[int], delimeter: tuple) -> List[int]:
    """ Insert a tuple 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_tuple([], (4,))
    []
    >>> intersperse_with_tuple([1, 2, 3], (4,))
    [1, (4,), 2, (4,), 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + delimeter + intersperse(numbers[1:], delimeter)


def intersperse_with_set(numbers: List[int], delimeter: set) -> List[int]:
    """ Insert a set 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_set([], {4})
    []
    >>> intersperse_with_set([1, 2, 3], {4})
    [1, {4}, 2, {4}, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + delimeter + intersperse(numbers[1:], delimeter)


def intersperse_with_frozenset(numbers: List[int], delimeter: frozenset) -> List[int]:
    """ Insert a frozenset 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_frozenset([], frozenset({4}))
    []
    >>> intersperse_with_frozenset([1, 2, 3], frozenset({4}))
    [1, frozenset({4}), 2, frozenset({4}), 3]
    """