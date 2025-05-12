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


def intersperse_with(numbers: List[int], delimeter: int, f: callable) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with([], 4, lambda x: x)
    []
    >>> intersperse_with([1, 2, 3], 4, lambda x: x)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + [delimeter] + intersperse_with(numbers[1:], delimeter, f)


def intersperse_with_2(numbers: List[int], delimeter: int, f: callable) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_2([], 4, lambda x: x)
    []
    >>> intersperse_with_2([1, 2, 3], 4, lambda x: x)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [f(numbers[0])] + [delimeter] + intersperse_with_2(numbers[1:], delimeter, f)


def intersperse_with_3(numbers: List[int], delimeter: int, f: callable) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_3([], 4, lambda x: x)
    []
    >>> intersperse_with_3([1, 2, 3], 4, lambda x: x)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [f(numbers[0])] + [delimeter] + intersperse_with_3(numbers[1:], delimeter, f)


def intersperse_with_4(numbers: List[int], delimeter: int, f: callable) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_with_4([], 4, lambda x: x)
    []
    >>> intersperse_with_4([1, 2, 3], 4, lambda x: x)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [f(numbers[0])] + [delimeter] + intersperse_with_4(numbers[1:], delimeter, f)


def intersperse_with_5(numbers: List[int], delimeter: int, f: callable) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>>