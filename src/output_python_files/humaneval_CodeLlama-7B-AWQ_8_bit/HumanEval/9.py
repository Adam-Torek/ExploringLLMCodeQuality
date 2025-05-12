from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for i in range(len(numbers)):
        result.append(max(numbers[i:]))
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    result = []
    for i in range(len(numbers)):
        result.append(min(numbers[i:]))
    return result


def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum and minimum element found
    until given moment in the sequence.
    >>> rolling_max_min([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (4, 4)]
    """
    result = []
    for i in range(len(numbers)):
        result.append((max(numbers[i:]), min(numbers[i:])))
    return result


def rolling_max_min_sum(numbers: List[int]) -> List[Tuple[int, int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum and sum element found
    until given moment in the sequence.
    >>> rolling_max_min_sum([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1), (2, 2, 4), (3, 2, 7), (3, 3, 10), (4, 3, 13), (4, 4, 17), (4, 4, 17)]
    """
    result = []
    for i in range(len(numbers)):
        result.append((max(numbers[i:]), min(numbers[i:]), sum(numbers[i:])))
    return result


def rolling_max_min_sum_avg(numbers: List[int]) -> List[Tuple[int, int, int, float]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum, sum and average element
    found until given moment in the sequence.
    >>> rolling_max_min_sum_avg([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1, 1.0), (2, 2, 4, 2.5), (3, 2, 7, 3.5), (3, 3, 10, 4.0), (4, 3, 13, 4.5), (4, 4, 17, 5.0), (4, 4, 17, 5.0)]
    """
    result = []
    for i in range(len(numbers)):
        result.append((max(numbers[i:]), min(numbers[i:]), sum(numbers[i:]), sum(numbers[i:]) / len(numbers[i:])))
    return result


def rolling_max_min_sum_avg_median(numbers: List[int]) -> List[Tuple[int, int, int, float, float]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum, sum, average and median
    element found until given moment in the sequence.
    >>> rolling_max_min