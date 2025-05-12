from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for i in range(len(numbers)):
        max_list.append(max(numbers[:i + 1]))
    return max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    min_list = []
    for i in range(len(numbers)):
        min_list.append(min(numbers[:i + 1]))
    return min_list


def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum and minimum element found
    until given moment in the sequence.
    >>> rolling_max_min([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (1, 1), (2, 1), (3, 2), (3, 2), (4, 3), (4, 3)]
    """
    max_list = []
    min_list = []
    for i in range(len(numbers)):
        max_list.append((max(numbers[:i + 1]), min(numbers[:i + 1])))
        min_list.append((min(numbers[:i + 1]), max(numbers[:i + 1])))
    return max_list, min_list


def rolling_max_min_sum(numbers: List[int]) -> List[Tuple[int, int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum and sum element found
    until given moment in the sequence.
    >>> rolling_max_min_sum([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1), (1, 1, 1), (2, 1, 3), (3, 2, 6), (3, 2, 6), (4, 3, 10), (4, 3, 10)]
    """
    max_list = []
    min_list = []
    sum_list = []
    for i in range(len(numbers)):
        max_list.append((max(numbers[:i + 1]), min(numbers[:i + 1]), sum(numbers[:i + 1])))
        min_list.append((min(numbers[:i + 1]), max(numbers[:i + 1]), sum(numbers[:i + 1])))
        sum_list.append((sum(numbers[:i + 1]), min(numbers[:i + 1]), max(numbers[:i + 1])))
    return max_list, min_list, sum_list


def rolling_max_min_sum_avg(numbers: List[int]) -> List[Tuple[int, int, int, float]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum, minimum, sum and average element
    found until given moment in the sequence.
    >>> rolling_max_min_sum_avg([1, 2, 3, 2, 3, 4, 2])
    [(1, 1, 1, 1.