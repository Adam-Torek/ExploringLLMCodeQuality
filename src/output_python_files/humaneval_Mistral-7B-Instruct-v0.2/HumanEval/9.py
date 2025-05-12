from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_num = numbers[0]
    result = [max_num]

    for num in numbers[1:]:
        max_num = max(num, max_num)
        result.append(max_num)

    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 2, 2]
    """
    if not numbers:
        return []

    min_num = numbers[0]
    result = [min_num]

    for num in numbers[1:]:
        min_num = min(num, min_num)
        result.append(min_num)

    return result


def rolling_sum(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling sums of given window size.
    >>> rolling_sum([1, 2, 3, 4, 5], 2)
    [3, 6, 10]
    """
    if not numbers:
        return []

    if window_size > len(numbers):
        raise ValueError("Window size is greater than the length of the list")

    result = [sum(numbers[:window_size])]

    for i in range(window_size, len(numbers)):
        result.append(sum(numbers[i - window_size:i]))

    return result


def rolling_difference(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling differences of given window size.
    >>> rolling_difference([1, 2, 3, 4, 5], 2)
    [1, 1, 1]
    """
    if not numbers:
        return []

    if window_size > len(numbers):
        raise ValueError("Window size is greater than the length of the list")

    result = [numbers[0]]

    for i in range(window_size, len(numbers)):
        result.append(numbers[i] - numbers[i - window_size])

    return result


def rolling_product(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling products of given window size.
    >>> rolling_product([1, 2, 3, 4, 5], 2)
    [2, 6, 12]
    """
    if not numbers:
        return []

    if window_size > len(numbers):
        raise ValueError("Window size is greater than the length of the list")

    result = [numbers[0]]

    for i in range(window_size, len(numbers)):
        result.append(numbers[i - 1] * numbers[i])

    return result


def rolling_mean(numbers: List[int], window_size: int) -> List[float]:
    """ From a given list of integers, generate a list of rolling means of given window size.
    >>> rolling_mean([1, 2, 3,