from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)


def intersperse_str(numbers: List[str], delimeter: str) -> List[str]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_str([], '4')
    []
    >>> intersperse_str(['1', '2', '3'], '4')
    ['1', '4', '2', '4', '3']
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse_str(numbers[1:], delimeter)


def intersperse_str_list(numbers: List[List[str]], delimeter: str) -> List[str]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_str_list([], '4')
    []
    >>> intersperse_str_list([['1', '2', '3']], '4')
    ['1', '4', '2', '4', '3']
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse_str_list(numbers[1:], delimeter)


def intersperse_str_list_list(numbers: List[List[List[str]]], delimeter: str) -> List[str]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_str_list_list([], '4')
    []
    >>> intersperse_str_list_list([[['1', '2', '3']]], '4')
    ['1', '4', '2', '4', '3']
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse_str_list_list(numbers[1:], delimeter)


def intersperse_str_list_list_list(numbers: List[List[List[List[str]]]], delimeter: str) -> List[str]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_str_list_list_list([], '4')
    []
    >>> intersperse_str_list_list_list([[['1', '2', '3']]], '4')
    ['1', '4', '2', '4', '3']
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse_str_list_list_list(numbers[1:], delimeter)


def intersperse_str_list_list_list_list(numbers: List[List[List[List[List[str]]]]], delimeter: str) -> List[str]:
    """ Insert a string 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_str_list_list_list_list([], '4')
    []
    >>> intersperse_str_list_list_list_list([[['1', '2', '3']]], '4')
    ['1', '4', '2', '4', '3']
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse_str_list_list_list_list(numbers[1:], delimeter)


def intersperse_str_list_list_list_list_list(numbers: List[List[List[List[List[List[str]]]]]], delimeter: