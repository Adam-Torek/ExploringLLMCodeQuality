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


def intersperse_with_function(numbers: List[int], delimeter: int, function: callable) -> List[int]:
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
    return [numbers[0]] + [delimeter] + intersperse_with_function(numbers[1:], delimeter, function)


def intersperse_with_function_2(numbers: List[int], delimeter: int, function: callable) -> List[int]:
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
    return [numbers[0]] + [delimeter] + intersperse_with_function_2(numbers[1:], delimeter, function)


def intersperse_with_function_3(numbers: List[int], delimeter: int, function: callable) -> List[int]:
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
    return [numbers[0]] + [delimeter] + intersperse_with_function_3(numbers[1:], delimeter, function)


def intersperse_with_function_4(numbers: List[int], delimeter: int, function: callable) -> List[int]:
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
    return [numbers[0]] + [delimeter] + intersperse_with_function_4(numbers[1:], delimeter, function)


def intersperse_with_function_5(numbers: List[int], delimeter: int, function: callable) -> List[int]:
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
    return [numbers[0]] + [delimeter] + intersperse_with_