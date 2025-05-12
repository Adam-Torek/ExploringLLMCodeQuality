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
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)


def intersperse_2(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse_2(numbers[1:], delimeter)


def intersperse_3(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse_3(numbers[1:], delimeter)


def intersperse_4(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse_4(numbers[1:], delimeter)


def intersperse_5(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse_5(numbers[1:], delimeter)


def intersperse_6(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    return [numbers[0]] + [delimeter] + intersperse_6(numbers[1:], delimeter)


def intersperse_7(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([],