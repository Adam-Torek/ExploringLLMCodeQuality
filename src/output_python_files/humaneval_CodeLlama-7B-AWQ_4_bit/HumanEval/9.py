from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_value = numbers[0]
    for number in numbers:
        max_value = max(max_value, number)
        result.append(max_value)
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    result = []
    min_value = numbers[0]
    for number in numbers:
        min_value = min(min_value, number)
        result.append(min_value)
    return result


def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum and minimum element found
    until given moment in the sequence.
    >>> rolling_max_min([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (1, 1), (2, 1), (3, 2), (3, 2), (4, 3), (4, 3)]
    """
    result = []
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        max_value = max(max_value, number)
        min_value = min(min_value, number)
        result.append((max_value, min_value))
    return result


def rolling_max_min_sum(numbers: List[int]) -> List[Tuple[int, int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum and sum of elements
    found until given moment in the sequence.
    >>> rolling_max_min_sum([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1), (1, 1, 2), (2, 1, 3), (3, 2, 5), (3, 2, 6), (4, 3, 9), (4, 3, 9)]
    """
    result = []
    max_value = numbers[0]
    min_value = numbers[0]
    sum_value = numbers[0]
    for number in numbers:
        max_value = max(max_value, number)
        min_value = min(min_value, number)
        sum_value += number
        result.append((max_value, min_value, sum_value))
    return result


def rolling_max_min_sum_avg(numbers: List[int]) -> List[Tuple[int, int, int, float]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum, sum and average of
    elements found until given moment in the sequence.
    >>> rolling_max_min_sum_avg([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1, 1.0), (1, 1, 2, 1.5), (2, 1, 3, 2.0), (3, 2, 5, 3.0), (3,